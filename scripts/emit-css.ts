/**
 * Emits a product's DTCG `tokens.json` as CSS custom properties. Reading the
 * JSON rather than the DESIGN.md keeps the two files from disagreeing.
 *
 * Usage:
 *   node scripts/emit-css.ts --tokens earthranger/tokens.json --prefix er --out earthranger/tokens.css
 *
 *   - Variables are the token path, kebab-cased, under the prefix:
 *     `color` › `UI/CTA Primary` is `--er-ui-cta-primary`. Renaming a token
 *     renames its variable.
 *   - A `{ light, dark }` pair becomes one variable: light on `:root`, dark on
 *     `[data-theme="dark"]`. No `prefers-color-scheme`: apps opt in to dark.
 *   - Only variables are declared, so importing the file changes nothing alone.
 *   - Anything unrecognised fails the build rather than being guessed.
 */

import { readFileSync, writeFileSync } from 'fs';
import { relative, resolve, sep } from 'path';

// ── Argument parsing ───────────────────────────────────────────────

const args = process.argv.slice(2);
const get = (flag: string) => {
  const i = args.indexOf(flag);
  return i !== -1 ? args[i + 1] : undefined;
};

const tokensFile = get('--tokens');
const prefix = get('--prefix');
const outFile = get('--out');

// Required, so variables never land unprefixed in a page's global namespace.
if (!tokensFile || !prefix) {
  console.error('Usage: emit-css.ts --tokens <tokens.json> --prefix <name> [--out <file>]');
  process.exit(1);
}

function fail(message: string): never {
  console.error(`emit-css: ${message}`);
  process.exit(1);
}

if (!/^[a-z][a-z0-9-]*$/.test(prefix)) {
  fail(`Prefix "${prefix}" must be lowercase letters, digits and -, starting with a letter`);
}

type Tree = Record<string, any>;

const isToken = (node: unknown): node is Tree =>
  typeof node === 'object' && node !== null && '$value' in node;

const isGroup = (node: unknown): node is Tree =>
  typeof node === 'object' && node !== null && !Array.isArray(node) && !isToken(node);

/** Skips `$schema`, `$description` and other group metadata. */
const childKeys = (group: Tree) => Object.keys(group).filter((key) => !key.startsWith('$'));

const display = (path: string[]) => path.join(' › ');

// ── Naming ─────────────────────────────────────────────────────────

/** `fontSize` -> `font-size`, `UI/CTA Primary` -> `ui-cta-primary`. */
function kebab(segment: string, path: string[]): string {
  const out = segment
    .replace(/([a-z0-9])([A-Z])/g, '$1-$2')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
  if (!out) fail(`${display(path)}: key "${segment}" has no letters or digits to name a variable with`);
  return out;
}

/** Drops `color`, since colour keys already start with their category (`UI/`).
 *  EarthRanger's `fontStyle: Bold` is a weight, so it's named `font-weight`. */
function nameSegments(path: string[], type: string): string[] {
  const segments = path[0] === 'color' ? path.slice(1) : [...path];
  const last = segments.length - 1;
  if (segments[last] === 'fontStyle' && type === 'fontWeight') segments[last] = 'fontWeight';
  return segments;
}

// ── Values ─────────────────────────────────────────────────────────

/** Alpha is separate from DTCG's six-digit `hex`, so it's appended as hex. */
function colorCss(value: unknown, path: string[]): string {
  const v = value as Tree;
  if (typeof v !== 'object' || v === null) fail(`${display(path)}: colour $value is not an object`);
  if (v.colorSpace !== 'srgb') fail(`${display(path)}: colour space ${v.colorSpace} is not srgb`);
  if (typeof v.hex !== 'string' || !/^#[0-9a-fA-F]{6}$/.test(v.hex)) {
    fail(`${display(path)}: colour has no six-digit hex`);
  }
  const hex = v.hex.toLowerCase();
  if (v.alpha === undefined) return hex;
  if (typeof v.alpha !== 'number' || v.alpha < 0 || v.alpha > 1) {
    fail(`${display(path)}: alpha ${v.alpha} is not a number from 0 to 1`);
  }
  if (v.alpha === 1) return hex;
  return hex + Math.round(v.alpha * 255).toString(16).padStart(2, '0');
}

/** Written as the spec states it, with no px -> rem conversion. */
function dimensionCss(value: unknown, path: string[]): string {
  const v = value as Tree;
  if (typeof v !== 'object' || v === null || typeof v.value !== 'number' || !Number.isFinite(v.value)) {
    fail(`${display(path)}: dimension $value has no numeric value`);
  }
  if (v.unit !== 'px' && v.unit !== 'rem') fail(`${display(path)}: dimension unit ${v.unit} is not px or rem`);
  return `${String(v.value)}${v.unit}`;
}

/** Quotes any family that isn't a plain identifier, such as `PP Telegraf`.
 *  Generic families (`sans-serif`) are identifiers, so they stay unquoted. */
function fontFamilyCss(value: unknown, path: string[]): string {
  let names: unknown[];
  if (typeof value === 'string') names = value.split(',');
  else if (Array.isArray(value)) names = value;
  else fail(`${display(path)}: fontFamily $value is not a string or an array`);

  return names
    .map((raw) => {
      if (typeof raw !== 'string') fail(`${display(path)}: font family ${raw} is not a string`);
      const name = raw.trim();
      if (!name) fail(`${display(path)}: empty font family name`);
      if (/^(["']).*\1$/.test(name)) return name;
      if (/^[A-Za-z][A-Za-z0-9-]*$/.test(name)) return name;
      return `"${name.replace(/["\\]/g, '\\$&')}"`;
    })
    .join(', ');
}

/** DTCG's weight aliases; CSS doesn't accept names like `regular`. */
const FONT_WEIGHTS: Record<string, number> = {
  thin: 100,
  hairline: 100,
  'extra-light': 200,
  'ultra-light': 200,
  light: 300,
  normal: 400,
  regular: 400,
  book: 400,
  medium: 500,
  'semi-bold': 600,
  'demi-bold': 600,
  bold: 700,
  'extra-bold': 800,
  'ultra-bold': 800,
  black: 900,
  heavy: 900,
  'extra-black': 950,
  'ultra-black': 950,
};

function fontWeightCss(value: unknown, path: string[]): string {
  if (typeof value === 'number') return String(value);
  if (typeof value === 'string') {
    const weight = FONT_WEIGHTS[value.toLowerCase()];
    if (weight !== undefined) return String(weight);
  }
  fail(`${display(path)}: font weight ${JSON.stringify(value)} is not a number or a DTCG alias`);
}

function numberCss(value: unknown, path: string[]): string {
  if (typeof value !== 'number' || !Number.isFinite(value)) fail(`${display(path)}: $value ${value} is not a number`);
  return String(value);
}

/** One CSS value per name suffix; a composite `typography` token expands into five. */
type Declaration = { suffix: string[]; value: string };

function tokenCss(token: Tree, path: string[]): Declaration[] {
  const { $type: type, $value: value } = token;
  if (typeof value === 'string' && /^\{.*\}$/.test(value.trim())) {
    fail(`${display(path)}: $value ${value} is an unresolved reference`);
  }
  switch (type) {
    case 'color':
      return [{ suffix: [], value: colorCss(value, path) }];
    case 'dimension':
      return [{ suffix: [], value: dimensionCss(value, path) }];
    case 'fontFamily':
      return [{ suffix: [], value: fontFamilyCss(value, path) }];
    case 'fontWeight':
      return [{ suffix: [], value: fontWeightCss(value, path) }];
    case 'number':
      return [{ suffix: [], value: numberCss(value, path) }];
    case 'typography': {
      const v = value as Tree;
      if (typeof v !== 'object' || v === null) fail(`${display(path)}: typography $value is not an object`);
      return [
        { suffix: ['fontFamily'], value: fontFamilyCss(v.fontFamily, [...path, 'fontFamily']) },
        { suffix: ['fontSize'], value: dimensionCss(v.fontSize, [...path, 'fontSize']) },
        { suffix: ['fontWeight'], value: fontWeightCss(v.fontWeight, [...path, 'fontWeight']) },
        { suffix: ['letterSpacing'], value: dimensionCss(v.letterSpacing, [...path, 'letterSpacing']) },
        { suffix: ['lineHeight'], value: numberCss(v.lineHeight, [...path, 'lineHeight']) },
      ];
    }
    default:
      fail(`${display(path)}: $type ${JSON.stringify(type)} has no CSS mapping`);
  }
}

// ── Walking the tree ───────────────────────────────────────────────

type Variable = { name: string; light: string; dark?: string };

/** Variables per top-level group, so the output can space the groups apart. */
const groups = new Map<string, Variable[]>();
const owners = new Map<string, string>();

function emit(path: string[], type: string, light: Declaration[], dark?: Declaration[]) {
  const base = nameSegments(path, type);
  light.forEach((declaration, i) => {
    const segments = [...base, ...declaration.suffix];
    const name = `--${prefix}-${segments.map((segment) => kebab(segment, path)).join('-')}`;
    const source = display([...path, ...declaration.suffix]);
    const owner = owners.get(name);
    if (owner) fail(`${owner} and ${source} both become ${name}`);
    owners.set(name, source);

    const variable: Variable = { name, light: declaration.value };
    if (dark) variable.dark = dark[i].value;
    if (!groups.has(path[0])) groups.set(path[0], []);
    groups.get(path[0])!.push(variable);
  });
}

/** A group with exactly the keys `light` and `dark` is one token in two modes.
 *  Either key alongside anything else is treated as a spec mistake. */
function modePair(group: Tree, path: string[]): { light: Tree; dark: Tree } | undefined {
  const keys = childKeys(group);
  if (!keys.includes('light') && !keys.includes('dark')) return undefined;
  if (keys.length !== 2 || !keys.includes('light') || !keys.includes('dark')) {
    fail(`${display(path)}: a light/dark pair must have exactly the keys light and dark, found ${keys.join(', ')}`);
  }
  const { light, dark } = group;
  if (!isToken(light) || !isToken(dark)) fail(`${display(path)}: light and dark must both be tokens`);
  if (light.$type !== dark.$type) {
    fail(`${display(path)}: light is ${light.$type} but dark is ${dark.$type}`);
  }
  return { light, dark };
}

function walk(node: Tree, path: string[]) {
  for (const key of childKeys(node)) {
    const child = node[key];
    const childPath = [...path, key];
    if (isToken(child)) {
      emit(childPath, child.$type, tokenCss(child, childPath));
    } else if (isGroup(child)) {
      const pair = modePair(child, childPath);
      if (pair) {
        emit(
          childPath,
          pair.light.$type,
          tokenCss(pair.light, [...childPath, 'light']),
          tokenCss(pair.dark, [...childPath, 'dark']),
        );
      } else {
        walk(child, childPath);
      }
    } else {
      fail(`${display(childPath)}: ${JSON.stringify(child)} is neither a token nor a group`);
    }
  }
}

// ── Main ───────────────────────────────────────────────────────────

let tokens: Tree;
try {
  tokens = JSON.parse(readFileSync(tokensFile, 'utf8'));
} catch (error) {
  fail(`Could not read ${tokensFile}: ${(error as Error).message}`);
}
if (!isGroup(tokens)) fail(`${tokensFile} is not a DTCG token tree`);

walk(tokens, []);

const block = (selector: string, pick: (variable: Variable) => string | undefined): string | undefined => {
  const sections = [...groups.values()]
    .map((variables) =>
      variables
        .map((variable) => {
          const value = pick(variable);
          return value === undefined ? undefined : `  ${variable.name}: ${value};`;
        })
        .filter((line) => line !== undefined)
        .join('\n'),
    )
    .filter(Boolean);
  return sections.length ? `${selector} {\n${sections.join('\n\n')}\n}\n` : undefined;
};

// Every variable, so the file alone is a complete light theme. `[data-theme="light"]`
// lets a light subtree inside a dark one switch back.
const light = block(':root,\n[data-theme="light"]', (variable) => variable.light);

// Only values that differ. A bare attribute selector lets a subtree go dark; it
// matches :root's specificity and comes later, so it wins.
const dark = block('[data-theme="dark"]', (variable) =>
  variable.dark !== undefined && variable.dark !== variable.light ? variable.dark : undefined,
);

// Relative and forward-slashed, so the header is the same on every machine.
const source = relative(process.cwd(), resolve(tokensFile)).split(sep).join('/');
const header = `/* Generated by scripts/emit-css.ts from ${source}. Do not edit: run \`npm run build\`. */\n`;
const output = [header + (light ?? ''), dark].filter(Boolean).join('\n');

if (outFile) {
  writeFileSync(outFile, output);
  console.log(`Emitted ${owners.size} custom properties → ${outFile}`);
} else {
  process.stdout.write(output);
}

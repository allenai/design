/**
 * Emits a product's DTCG `tokens.json` as CSS custom properties, for anything
 * that renders CSS — Sass modules, plain CSS, Tailwind, Bootstrap's `--bs-*`
 * theming — where the JSON serves JavaScript consumers.
 *
 * It reads the generated `tokens.json` rather than the DESIGN.md, so the JSON is
 * the one machine-readable contract and the two files can never disagree. That
 * also means swapping `emit-tokens.ts` for `@google/design.md export --format
 * dtcg` (see the README's migration notes) changes nothing here.
 *
 * Usage:
 *   node scripts/emit-css.ts --tokens earthranger/tokens.json --prefix er --out earthranger/tokens.css
 *
 * What it does:
 *   - Names each variable after its token path, kebab-cased, under a required
 *     prefix: `color` › `UI/CTA Primary` becomes `--er-ui-cta-primary`. Names
 *     come from the designers' token names with no hand-picked renames, so
 *     renaming a token renames its variable — a breaking change for consumers.
 *   - Turns a `{ light, dark }` pair into one variable: the light value under
 *     `:root, [data-theme="light"]`, the dark value under `[data-theme="dark"]`.
 *     There is deliberately no `prefers-color-scheme` block: an app that isn't
 *     dark-ready would go half-dark for every user with a dark OS. Apps opt in.
 *   - Declares custom properties and nothing else, so importing the file never
 *     changes how a page looks — only reading the variables does.
 *   - Fails on anything it doesn't recognise (an unknown `$type`, a leftover
 *     reference, a lone `light`, two tokens that kebab-case to the same name)
 *     rather than guessing, because a guess here ships the wrong colour to
 *     every product that imports the file.
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

// The prefix is required so variables can never land in a page's global
// namespace without one — `--ui-cta-primary` would collide with anything.
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

/** `$schema`, `$description` and friends describe a group; they aren't tokens. */
const childKeys = (group: Tree) => Object.keys(group).filter((key) => !key.startsWith('$'));

const display = (path: string[]) => path.join(' › ');

// ── Naming ─────────────────────────────────────────────────────────

/** `fontSize` -> `font-size`, `UI/CTA Primary` -> `ui-cta-primary`,
 *  `Track Line (Mobile)` -> `track-line-mobile`. Runs of capitals stay whole, so
 *  `CTA` is one word rather than `c-t-a`. */
function kebab(segment: string, path: string[]): string {
  const out = segment
    .replace(/([a-z0-9])([A-Z])/g, '$1-$2')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
  // A key made only of punctuation would vanish from the name and leave the
  // variable meaning something other than the token it came from.
  if (!out) fail(`${display(path)}: key "${segment}" has no letters or digits to name a variable with`);
  return out;
}

/** The path segments that make up a variable's name. `color` is dropped because
 *  every colour key already starts with its category (`UI/`, `Teal/`); every
 *  other top-level group keeps its name so `typography-…` can't collide with a
 *  colour. EarthRanger writes `fontStyle: Bold` to mean a weight, so a variable
 *  called `font-style` holding `700` would mislead whoever reads it. */
function nameSegments(path: string[], type: string): string[] {
  const segments = path[0] === 'color' ? path.slice(1) : [...path];
  const last = segments.length - 1;
  if (segments[last] === 'fontStyle' && type === 'fontWeight') segments[last] = 'fontWeight';
  return segments;
}

// ── Values ─────────────────────────────────────────────────────────

/** `hex` is DTCG's six-digit fallback and alpha lives separately, so a
 *  translucent colour goes back to eight-digit hex — which every browser reads. */
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

/** Written exactly as the spec states it. No px -> rem conversion: that would
 *  mean inventing a root font size the spec never declares. */
function dimensionCss(value: unknown, path: string[]): string {
  const v = value as Tree;
  if (typeof v !== 'object' || v === null || typeof v.value !== 'number' || !Number.isFinite(v.value)) {
    fail(`${display(path)}: dimension $value has no numeric value`);
  }
  if (v.unit !== 'px' && v.unit !== 'rem') fail(`${display(path)}: dimension unit ${v.unit} is not px or rem`);
  return `${String(v.value)}${v.unit}`;
}

const GENERIC_FAMILIES = new Set([
  'serif',
  'sans-serif',
  'monospace',
  'cursive',
  'fantasy',
  'system-ui',
  'ui-sans-serif',
  'ui-serif',
  'ui-monospace',
  'ui-rounded',
]);

/** Quote any family that isn't a plain identifier — `PP Telegraf`, `SF Pro` — so
 *  the stack parses the same everywhere, but never a generic family, which
 *  quoting would turn into a font literally named "sans-serif". */
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
      if (GENERIC_FAMILIES.has(name.toLowerCase())) return name;
      if (/^[A-Za-z][A-Za-z0-9-]*$/.test(name)) return name;
      return `"${name.replace(/["\\]/g, '\\$&')}"`;
    })
    .join(', ');
}

/** DTCG's weight aliases. They have to become numbers: `regular`, which
 *  EarthRanger uses, isn't a valid CSS `font-weight`. */
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

/** One CSS value per suffix. Most tokens are a single variable (empty suffix); a
 *  composite `typography` token expands into five, named the same way as
 *  EarthRanger's primitive groups so both shapes read alike to a consumer. */
type Declaration = { suffix: string[]; value: string };

function tokenCss(token: Tree, path: string[]): Declaration[] {
  const { $type: type, $value: value } = token;
  // emit-tokens resolves every reference, so one surviving here means something
  // upstream broke — and `var(--…)` has no way to follow `{colors.x}`.
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
      for (const key of ['fontFamily', 'fontSize', 'fontWeight', 'letterSpacing', 'lineHeight']) {
        if (v[key] === undefined) fail(`${display(path)}: typography is missing ${key}`);
      }
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

type Variable = { name: string; path: string[]; light: string; dark?: string };

/** Variables per top-level group, in source order, so the output can put a blank
 *  line between groups. */
const groups = new Map<string, Variable[]>();
const owners = new Map<string, string>();

function emit(path: string[], type: string, light: Declaration[], dark?: Declaration[]) {
  const base = nameSegments(path, type);
  light.forEach((declaration, i) => {
    const segments = [...base, ...declaration.suffix];
    const name = `--${prefix}-${segments.map((segment) => kebab(segment, path)).join('-')}`;
    const source = display([...path, ...declaration.suffix]);
    // A silent overwrite would hand consumers one of two colours at random.
    const owner = owners.get(name);
    if (owner) fail(`${owner} and ${source} both become ${name}`);
    owners.set(name, source);

    const variable: Variable = { name, path, light: declaration.value };
    if (dark) variable.dark = dark[i].value;
    if (!groups.has(path[0])) groups.set(path[0], []);
    groups.get(path[0])!.push(variable);
  });
}

/** A group whose keys are exactly `light` and `dark` is one token in two modes.
 *  `light` or `dark` next to anything else, or on its own, is almost certainly a
 *  mistake in the spec, and guessing which value to ship would hide it. */
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

// The light block holds every variable, so importing the file alone gives a
// complete light theme. Listing `[data-theme="light"]` too lets a light region
// nested inside a dark one revert.
const light = block(':root,\n[data-theme="light"]', (variable) => variable.light);

// Only what actually changes in dark: a pair with the same value in both modes
// already inherits the right one from :root. The bare attribute selector (not
// `:root[data-theme="dark"]`) lets an app darken just a subtree, such as a
// sidebar; it has the light block's specificity and comes later, so it wins.
const dark = block('[data-theme="dark"]', (variable) =>
  variable.dark !== undefined && variable.dark !== variable.light ? variable.dark : undefined,
);

// Relative and forward-slashed, so the header is the same on every machine and a
// release never commits a diff that is only a path.
const source = relative(process.cwd(), resolve(tokensFile)).split(sep).join('/');
const header = `/* Generated by scripts/emit-css.ts from ${source}. Do not edit: run \`npm run build\`. */\n`;
const output = [header + (light ?? ''), dark].filter(Boolean).join('\n');

if (outFile) {
  writeFileSync(outFile, output);
  console.log(`Emitted ${owners.size} custom properties → ${outFile}`);
} else {
  process.stdout.write(output);
}

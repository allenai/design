#!/usr/bin/env python3
"""WCAG 2.x contrast ratio for colour pairs.

Usage:
  contrast.py FG BG              e.g. contrast.py '#1A1A1A' '#FFF'
  contrast.py FG:BG [FG:BG ...]  e.g. contrast.py '#E5484D:#FFFFFF' '#0B6E4F:#111'

Colours are hex (#RGB, #RRGGBB, or #RRGGBBAA; alpha is composited over the
background, and the background itself must be opaque).
"""
import sys


def parse(h):
    h = h.strip().lstrip("#")
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h)
    if len(h) not in (6, 8):
        raise ValueError(f"bad colour: #{h}")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    a = int(h[6:8], 16) / 255 if len(h) == 8 else 1.0
    return (r, g, b), a


def lum(rgb):
    def ch(c):
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg, bg):
    (frgb, fa), (brgb, ba) = parse(fg), parse(bg)
    if ba < 1:
        raise ValueError(f"background {bg} must be opaque")
    frgb = tuple(fa * f + (1 - fa) * b for f, b in zip(frgb, brgb))
    l1, l2 = sorted((lum(frgb), lum(brgb)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def verdict(r):
    text = "AAA" if r >= 7 else "AA" if r >= 4.5 else "AA-large only" if r >= 3 else "fail"
    ui = "pass" if r >= 3 else "fail"
    return f"text: {text:13}  non-text UI (3:1): {ui}"


def main(args):
    if len(args) == 2 and ":" not in args[0] and ":" not in args[1]:
        pairs = [tuple(args)]
    else:
        pairs = [tuple(a.split(":", 1)) for a in args]
    if not pairs or any(len(p) != 2 for p in pairs):
        sys.exit(__doc__)
    for fg, bg in pairs:
        r = ratio(fg, bg)
        print(f"{fg:>10} on {bg:<10} {r:5.2f}:1  {verdict(r)}")


if __name__ == "__main__":
    main(sys.argv[1:])

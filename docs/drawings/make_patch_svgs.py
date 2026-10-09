#!/usr/bin/env python3
"""Generate the patch-example drawings for the user manual.

Each example draws the panel (from the KiCad faceplate file) with source
modules on the left, destination modules on the right, and patch cables.

Writes docs/images/patch-*.svg.
Run from anywhere: python3 docs/drawings/make_patch_svgs.py
"""
import math
from pathlib import Path

from make_panel_svg import FONT, INK, KNOB_R, PCB, RED, controls, panel_body, parse, svg

OUT = Path(__file__).resolve().parents[2] / "docs" / "images"

GREY = "#777"
BLUE = "#2a6fb0"  # second signal, for patches with two
BOX_W, BOX_H = 38, 11
GAP = 22  # space between the panel and the module boxes


def text(x, y, s, size=2.6, weight="normal", color=INK, anchor="middle"):
    return (f"<text x='{x:.2f}' y='{y:.2f}' {FONT} font-size='{size}' font-weight='{weight}' fill='{color}' "
            f"text-anchor='{anchor}' dominant-baseline='central'>{s}</text>")


def marker(color, name):
    return (f"<marker id='{name}' viewBox='0 0 10 10' refX='9' refY='5' markerWidth='4' markerHeight='4' "
            f"orient='auto'><path d='M0 1 L10 5 L0 9 z' fill='{color}'/></marker>")


class Patch:
    def __init__(self, data):
        self.data = data
        outline, holes = data[0], data[1]
        self.x0, self.y0, self.x1, self.y1 = outline
        self.jacks, self.knobs = {}, {}
        for n, (knob, inp, out) in enumerate(controls(holes), start=1):
            self.knobs[f"Knob {n}"] = knob
            self.jacks[f"In {n}"] = inp
            self.jacks[f"Out {n}"] = out
        self.cables, self.boxes, self.plugs, self.notes, self.pointers = [], [], [], [], []

    def box(self, side, y, title, sub):
        x = self.x0 - GAP - BOX_W if side == "left" else self.x1 + GAP
        self.boxes += [f"<rect x='{x}' y='{y - BOX_H / 2}' width='{BOX_W}' height='{BOX_H}' rx='1.2' "
                       f"fill='#fff' stroke='{INK}' stroke-width='0.35'/>",
                       text(x + BOX_W / 2, y - 2, title, 3.4, "bold"),
                       text(x + BOX_W / 2, y + 2.7, sub, 2.7, color=GREY)]
        return (x + BOX_W, y) if side == "left" else (x, y)

    def source(self, jack, title, sub, color=RED):
        # The cable runs above the channel, clear of the knob, then drops into the jack.
        jx, jy = self.jacks[jack]
        top = jy - 6.5
        bx, by = self.box("left", top, title, sub)
        self.cables.append(f"<path d='M{bx:.2f} {by:.2f} H{jx - 5:.2f} Q{jx:.2f} {top:.2f} {jx:.2f} {jy:.2f}' "
                           f"fill='none' stroke='{color}' stroke-width='0.9' stroke-linecap='round'/>")
        self.plugs.append(f"<circle cx='{jx}' cy='{jy}' r='2.3' fill='{color}' stroke='{INK}' stroke-width='0.3'/>")

    def dest(self, jack, title, sub, color=RED):
        jx, jy = self.jacks[jack]
        bx, by = self.box("right", jy, title, sub)
        self.cable((jx, jy), (bx, by), color, into_jack=False)

    def cable(self, a, b, color, into_jack):
        (ax, ay), (bx, by) = a, b
        k = abs(bx - ax) * 0.5
        mid = "r" if color == RED else "b"
        end = "" if into_jack else f" marker-end='url(#{mid})'"
        self.cables.append(f"<path d='M{ax:.2f} {ay:.2f} C{ax + k:.2f} {ay:.2f} {bx - k:.2f} {by:.2f} {bx:.2f} {by:.2f}' "
                           f"fill='none' stroke='{color}' stroke-width='0.9' stroke-linecap='round'{end}/>")
        jx, jy = b if into_jack else a
        self.plugs.append(f"<circle cx='{jx}' cy='{jy}' r='2.3' fill='{color}' stroke='{INK}' stroke-width='0.3'/>")

    def turn(self, knob, degrees, color=RED):
        """Show a knob's setting: 0 is centered (12 o'clock, the panel's zero mark), negative is left."""
        kx, ky = self.knobs[knob]
        a = math.radians(degrees)
        point = lambda r: (kx + r * math.sin(a), ky - r * math.cos(a))
        (x1, y1), (x2, y2) = point(2), point(KNOB_R)
        # Redraw the knob to hide its default 12 o'clock pointer.
        self.pointers += [f"<circle cx='{kx}' cy='{ky}' r='{KNOB_R}' fill='#fff' stroke='{INK}' stroke-width='0.35'/>",
                          f"<circle cx='{kx}' cy='{ky}' r='{KNOB_R - 1.3}' fill='#fff' stroke='{INK}' stroke-width='0.25'/>",
                          f"<line x1='{x1:.2f}' y1='{y1:.2f}' x2='{x2:.2f}' y2='{y2:.2f}' stroke='{color}' "
                          f"stroke-width='0.8' stroke-linecap='round'/>"]

    def note(self, target, label, sub, color=RED):
        """A note to the left of a knob ("Knob 1") or jack ("In 2")."""
        y = self.knobs[target][1] if target in self.knobs else self.jacks[target][1]
        x = self.x0 - 3
        self.notes += [text(x, y - 1.8, label, 3.2, "bold", color=color, anchor="end"),
                       text(x, y + 2.4, sub, 2.7, color=GREY, anchor="end")]

    def render(self, title):
        body = [f"<defs>{marker(RED, 'r')}{marker(BLUE, 'b')}</defs>"]
        body += panel_body(*self.data)
        body += self.pointers + self.cables + self.plugs + self.boxes + self.notes
        left = self.x0 - GAP - BOX_W - 3
        width = (self.x1 + GAP + BOX_W + 3) - left
        return svg((left, self.y0 - 3, width, (self.y1 - self.y0) + 6), body, title)


def invert_envelope(data):
    p = Patch(data)
    p.source("In 1", "Envelope", "out")
    p.dest("Out 1", "Filter", "cutoff CV in")
    p.turn("Knob 1", -110)
    p.note("Knob 1", "Knob 1 left", "upside-down envelope")
    return p.render("Patch example: invert an envelope")


def scale_lfo(data):
    p = Patch(data)
    p.source("In 2", "LFO", "out")
    p.dest("Out 2", "VCO", "pulse width CV in")
    p.turn("Knob 2", 50)
    p.note("Knob 2", "Knob 2 right", "sets the depth")
    return p.render("Patch example: set the depth of an LFO")


def offset(data):
    p = Patch(data)
    p.source("In 3", "LFO", "out", color=RED)
    p.dest("Out 3", "DC mixer", "in 1", color=RED)
    p.dest("Out 4", "DC mixer", "in 2", color=BLUE)
    p.turn("Knob 3", 60)
    p.turn("Knob 4", 45, color=BLUE)
    p.note("In 4", "In 4 empty", "Knob 4 sets −5 V to +5 V", color=BLUE)
    return p.render("Patch example: offset an LFO")


def main():
    data = parse(PCB)
    OUT.mkdir(parents=True, exist_ok=True)
    for name, fig in (("patch-1-invert.svg", invert_envelope), ("patch-2-depth.svg", scale_lfo),
                      ("patch-3-offset.svg", offset)):
        (OUT / name).write_text(fig(data))
        print("wrote", OUT / name)


if __name__ == "__main__":
    main()

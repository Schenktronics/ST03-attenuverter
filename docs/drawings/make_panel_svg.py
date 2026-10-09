#!/usr/bin/env python3
"""Generate faceplate line drawings from the KiCad faceplate file.

Writes docs/images/panel.svg (annotated front view) and docs/images/panel-plain.svg
(the panel alone, for packaging labels where small captions would be lost).
Run from anywhere: python3 docs/drawings/make_panel_svg.py
"""
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PCB = ROOT / "hardware" / "panel" / "AttenuverterFaceplate.kicad_pcb"
OUT = ROOT / "docs" / "images"

INK = "#1a1a1a"
DIM = "#555"
RED = "#d9302c"
FONT = "font-family='DejaVu Sans, Helvetica, Arial, sans-serif'"

# Drill sizes (mm) that identify each kind of hole.
JACK, POT = 6.0, 7.0
KNOB_R = 4.8  # radius of the knob as drawn


def parse(path):
    s = path.read_text()
    edges = [tuple(map(float, m)) for m in re.findall(
        r"\(gr_line \(start ([\d.]+) ([\d.]+)\) \(end ([\d.]+) ([\d.]+)\) \(layer Edge\.Cuts\)", s)]
    xs = [v for e in edges for v in (e[0], e[2])]
    ys = [v for e in edges for v in (e[1], e[3])]
    outline = (min(xs), min(ys), max(xs), max(ys))

    holes, polys = [], []
    for block in re.findall(r"\n  \(module .*?\n  \)", s, re.S):
        at = re.search(r"\n    \(at ([\d.]+) ([\d.]+)", block)
        mx, my = float(at[1]), float(at[2])
        drill = re.search(r"\(drill ([\d.]+)\)", block)
        if drill:
            holes.append((mx, my, float(drill[1])))
        # The logo is a footprint made of filled silkscreen polygons.
        for pts in re.findall(r"\(fp_poly \(pts(.*?)\) \(layer F\.SilkS\)", block, re.S):
            polys.append([(mx + float(x), my + float(y)) for x, y in re.findall(r"\(xy ([\d.-]+) ([\d.-]+)\)", pts)])

    lines = [(tuple(map(float, m[:4])), float(m[4])) for m in re.findall(
        r"\(gr_line \(start ([\d.]+) ([\d.]+)\) \(end ([\d.]+) ([\d.]+)\) \(layer F\.SilkS\) \(width ([\d.]+)\)", s)]
    # KiCad 5 arcs: "start" is the center, "end" is where the arc begins, and the
    # angle is the sweep in degrees, clockwise on screen.
    arcs = [tuple(map(float, m)) for m in re.findall(
        r"\(gr_arc \(start ([\d.]+) ([\d.]+)\) \(end ([\d.]+) ([\d.]+)\) \(angle ([\d.-]+)\) "
        r"\(layer F\.SilkS\) \(width ([\d.]+)\)", s)]
    circles = [tuple(map(float, m)) for m in re.findall(
        r"\(gr_circle \(center ([\d.]+) ([\d.]+)\) \(end ([\d.]+) ([\d.]+)\) \(layer F\.SilkS\) \(width ([\d.]+)\)", s)]
    texts = []
    for m in re.finditer(r"\(gr_text (\S+) \(at ([\d.]+) ([\d.]+)(?: ([\d.]+))?\) \(layer F\.SilkS\)"
                         r"(.*?)\n  \)", s, re.S):
        size = re.search(r"\(size ([\d.]+)", m[5])
        texts.append(dict(text=m[1], x=float(m[2]), y=float(m[3]), size=float(size[1]), italic="italic" in m[5]))
    return outline, holes, dict(lines=lines, arcs=arcs, circles=circles, polys=polys, texts=texts)


def arc_path(cx, cy, sx, sy, angle):
    r = math.hypot(sx - cx, sy - cy)
    a0 = math.atan2(sy - cy, sx - cx)
    a1 = a0 + math.radians(angle)
    ex, ey = cx + r * math.cos(a1), cy + r * math.sin(a1)
    large = 1 if abs(angle) > 180 else 0
    sweep = 1 if angle > 0 else 0
    return f"M{sx:.3f} {sy:.3f} A{r:.3f} {r:.3f} 0 {large} {sweep} {ex:.3f} {ey:.3f}"


def knob(x, y):
    """A knob seen from the front, pointer at 12 o'clock (the panel's zero mark)."""
    return [f"<circle cx='{x}' cy='{y}' r='{KNOB_R}' fill='#fff' stroke='{INK}' stroke-width='0.35'/>",
            f"<circle cx='{x}' cy='{y}' r='{KNOB_R - 1.3}' fill='#fff' stroke='{INK}' stroke-width='0.25'/>",
            f"<line x1='{x}' y1='{y - KNOB_R}' x2='{x}' y2='{y - 2}' stroke='{INK}' stroke-width='0.6' "
            f"stroke-linecap='round'/>"]


def panel_body(outline, holes, silk):
    """SVG elements for the faceplate itself, in board coordinates (mm)."""
    x0, y0, x1, y1 = outline
    el = [f"<rect x='{x0}' y='{y0}' width='{x1 - x0}' height='{y1 - y0}' rx='0.4' "
          f"fill='#fff' stroke='{INK}' stroke-width='0.3'/>"]
    for pts in silk["polys"]:
        el.append(f"<polygon points='{' '.join(f'{x:.3f},{y:.3f}' for x, y in pts)}' fill='{INK}'/>")
    for (xa, ya, xb, yb), w in silk["lines"]:
        el.append(f"<line x1='{xa}' y1='{ya}' x2='{xb}' y2='{yb}' stroke='{INK}' "
                  f"stroke-width='{w}' stroke-linecap='round'/>")
    for cx, cy, sx, sy, angle, w in silk["arcs"]:
        el.append(f"<path d='{arc_path(cx, cy, sx, sy, angle)}' fill='none' stroke='{INK}' stroke-width='{w}'/>")
    for cx, cy, ex, ey, w in silk["circles"]:
        # The thick rings behind the output jacks.
        el.append(f"<circle cx='{cx}' cy='{cy}' r='{math.hypot(ex - cx, ey - cy)}' fill='none' "
                  f"stroke='{INK}' stroke-width='{w}'/>")
    for t in silk["texts"]:
        style = " font-style='italic'" if t["italic"] else ""
        el.append(f"<text x='{t['x']}' y='{t['y']}' {FONT} font-size='{t['size'] * 1.15}'{style} "
                  f"fill='{INK}' text-anchor='middle' dominant-baseline='central'>{t['text']}</text>")
    for x, y, d in holes:
        if d == JACK:
            # Knurled jack nut with the socket opening.
            el.append(f"<circle cx='{x}' cy='{y}' r='3.9' fill='#fff' stroke='{INK}' stroke-width='0.35'/>")
            el.append(f"<circle cx='{x}' cy='{y}' r='3.1' fill='none' stroke='{INK}' stroke-width='0.2'/>")
            el.append(f"<circle cx='{x}' cy='{y}' r='1.8' fill='{INK}'/>")
        elif d == POT:
            el += knob(x, y)
        else:
            el.append(f"<circle cx='{x}' cy='{y}' r='{d / 2}' fill='#fff' stroke='{INK}' stroke-width='0.3'/>")
    return el


def svg(view, body, title):
    vx, vy, vw, vh = view
    return (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='{vx} {vy} {vw} {vh}' "
            f"width='{vw * 4:.0f}' height='{vh * 4:.0f}'>\n<title>{title}</title>\n"
            f"<rect x='{vx}' y='{vy}' width='{vw}' height='{vh}' fill='#fff'/>\n"
            + "\n".join(body) + "\n</svg>\n")


def controls(holes):
    """(knob, input, output) positions for each channel, top to bottom.

    Each channel has its knob on the left and two jacks on the right: the input
    above, the output (with the black ring) below.
    """
    jacks = sorted(((x, y) for x, y, d in holes if d == JACK), key=lambda p: p[1])
    pots = sorted(((x, y) for x, y, d in holes if d == POT), key=lambda p: p[1])
    return [(pots[i], jacks[2 * i], jacks[2 * i + 1]) for i in range(len(pots))]


def annotated(outline, holes, silk):
    x0, y0, x1, y1 = outline
    body = panel_body(outline, holes, silk)
    lx = x1 + 5  # leader lines end here
    tx = lx + 2  # labels start here

    def label(y, title, sub, from_x, from_y=None):
        from_y = y if from_y is None else from_y
        return [f"<polyline points='{from_x},{from_y} {x1 + 2},{y} {lx},{y}' fill='none' stroke='{DIM}' stroke-width='0.3'/>",
                f"<circle cx='{from_x}' cy='{from_y}' r='0.5' fill='{DIM}'/>",
                f"<text x='{tx}' y='{y - 1.6}' {FONT} font-size='3.2' font-weight='bold' fill='{INK}' "
                f"dominant-baseline='central'>{title}</text>",
                f"<text x='{tx}' y='{y + 2.4}' {FONT} font-size='2.4' fill='{DIM}' "
                f"dominant-baseline='central'>{sub}</text>"]

    chans = controls(holes)
    (kx, ky), (ix, iy), (ox, oy) = chans[0]
    # Channel 1 is labelled in full. The knob's leader runs level through the gap
    # between the two jacks.
    body += label(ky - 10, "In 1", "input. Unplugged: +5 V", ix + 4, iy)
    body += label(ky, "Knob 1", "right ×1 · top 0 · left ×−1", kx + KNOB_R, ky)
    body += label(ky + 10, "Out 1", "black ring = output", ox + 4, oy)
    # Channels 2 to 4 get one label each, on their knob.
    for n, ((kx, ky), _, _) in enumerate(chans[1:], start=2):
        body += label(ky, f"Channel {n}", "same as channel 1", x1 - 1, ky)
    pad = 4
    return svg((x0 - pad, y0 - pad, (x1 - x0) + 48 + pad, (y1 - y0) + 2 * pad), body,
               "Attenuverter front panel")


def plain(outline, holes, silk):
    x0, y0, x1, y1 = outline
    pad = 1
    return svg((x0 - pad, y0 - pad, (x1 - x0) + 2 * pad, (y1 - y0) + 2 * pad), panel_body(outline, holes, silk),
               "Attenuverter front panel")


def main():
    data = parse(PCB)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "panel.svg").write_text(annotated(*data))
    (OUT / "panel-plain.svg").write_text(plain(*data))
    print("wrote", OUT / "panel.svg", "and", OUT / "panel-plain.svg")


if __name__ == "__main__":
    main()

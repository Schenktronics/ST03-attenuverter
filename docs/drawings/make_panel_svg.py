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


def read_sexp(text):
    """Parse a KiCad S-expression file into nested lists of strings."""
    tokens = re.findall(r'\(|\)|"(?:[^"\\]|\\.)*"|[^\s()]+', text)

    def parse_list(pos):
        items = []
        while pos < len(tokens):
            tok = tokens[pos]
            if tok == "(":
                node, pos = parse_list(pos + 1)
                items.append(node)
            elif tok == ")":
                return items, pos + 1
            else:
                items.append(tok[1:-1] if tok.startswith('"') else tok)
                pos += 1
        return items, pos

    return parse_list(1)[0]  # skip the opening paren of (kicad_pcb ...)


def tagged(node, name):
    """Direct children of node that are lists starting with `name`."""
    return [c for c in node if isinstance(c, list) and c and c[0] == name]


def first(node, name):
    found = tagged(node, name)
    return found[0] if found else None


def xy(node, name):
    return tuple(float(v) for v in first(node, name)[1:3])


def at_xyr(node):
    vals = [float(v) for v in first(node, "at")[1:]]
    return tuple(vals + [0.0] * (3 - len(vals)))


def on(node, layer):
    found = first(node, "layer")
    return found is not None and found[1] == layer


def width(node):
    w = first(first(node, "stroke") or [], "width")
    return float(w[1]) if w else 0.2


def arc_from_three(sx, sy, mx, my, ex, ey):
    """Center and signed sweep (degrees, clockwise on screen) of the arc start -> mid -> end."""
    d = 2 * (sx * (my - ey) + mx * (ey - sy) + ex * (sy - my))
    cx = ((sx**2 + sy**2) * (my - ey) + (mx**2 + my**2) * (ey - sy) + (ex**2 + ey**2) * (sy - my)) / d
    cy = ((sx**2 + sy**2) * (ex - mx) + (mx**2 + my**2) * (sx - ex) + (ex**2 + ey**2) * (mx - sx)) / d
    a0, am, ae = (math.atan2(y - cy, x - cx) for x, y in ((sx, sy), (mx, my), (ex, ey)))
    to_mid, to_end = (am - a0) % math.tau, (ae - a0) % math.tau
    sweep = to_end if to_mid < to_end else to_end - math.tau
    return cx, cy, math.degrees(sweep)


def parse(path):
    """Read the faceplate (KiCad 10 format)."""
    root = read_sexp(path.read_text())
    edges = [xy(g, "start") + xy(g, "end") for g in tagged(root, "gr_line") if on(g, "Edge.Cuts")]
    xs = [v for e in edges for v in (e[0], e[2])]
    ys = [v for e in edges for v in (e[1], e[3])]
    outline = (min(xs), min(ys), max(xs), max(ys))

    holes, polys = [], []
    for fp in tagged(root, "footprint"):
        mx, my, rot = at_xyr(fp)
        drill = first(first(fp, "pad") or [], "drill")
        if drill:
            holes.append((mx, my, float(drill[1])))
        # The logo is a footprint made of filled silkscreen polygons.
        a = math.radians(rot)
        for poly in tagged(fp, "fp_poly"):
            if on(poly, "F.SilkS"):
                polys.append([(mx + float(q[1]) * math.cos(a) + float(q[2]) * math.sin(a),
                               my - float(q[1]) * math.sin(a) + float(q[2]) * math.cos(a))
                              for q in tagged(first(poly, "pts"), "xy")])

    lines = [(xy(g, "start") + xy(g, "end"), width(g)) for g in tagged(root, "gr_line") if on(g, "F.SilkS")]
    arcs = []
    for g in tagged(root, "gr_arc"):
        if on(g, "F.SilkS"):
            (sx, sy), m, e = xy(g, "start"), xy(g, "mid"), xy(g, "end")
            cx, cy, sweep = arc_from_three(sx, sy, *m, *e)
            arcs.append((cx, cy, sx, sy, sweep, width(g)))
    circles = [xy(g, "center") + xy(g, "end") + (width(g),) for g in tagged(root, "gr_circle") if on(g, "F.SilkS")]
    texts = []
    for t in tagged(root, "gr_text"):
        if not on(t, "F.SilkS"):
            continue
        x, y, rot = at_xyr(t)
        effects = first(t, "effects")
        font = first(effects, "font")
        justify = first(effects, "justify")
        texts.append(dict(text=t[1], x=x, y=y, rot=rot, size=float(first(font, "size")[1]),
                          italic=first(font, "italic") is not None,
                          anchor={"left": "start", "right": "end"}.get(justify[1] if justify else "", "middle")))
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
        turn = f" transform='rotate({-t['rot']} {t['x']} {t['y']})'" if t["rot"] else ""
        el.append(f"<text x='{t['x']}' y='{t['y']}' {FONT} font-size='{t['size'] * 1.15}'{style}{turn} "
                  f"fill='{INK}' text-anchor='{t['anchor']}' dominant-baseline='central'>{t['text']}</text>")
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
    # Channel 1 is labeled in full. The knob's leader runs level through the gap
    # between the two jacks.
    body += label(ky - 10, "In 1", "input. Unplugged: +5 V", ix + 4, iy)
    body += label(ky, "Knob 1", "right x1, top 0, left x-1", kx + KNOB_R, ky)
    body += label(ky + 10, "Out 1", "black ring = output", ox + 4, oy)
    # Channels 2 to 4 get one label each, on their knob.
    for n, ((kx, ky), _, _) in enumerate(chans[1:], start=2):
        body += label(ky, f"Channel {n}", "same as channel 1", x1 - 1, ky)
    pad = 4
    return svg((x0 - pad, y0 - pad, (x1 - x0) + 48 + pad, (y1 - y0) + 2 * pad), body,
               "ST-03 Attenuverter front panel")


def plain(outline, holes, silk):
    x0, y0, x1, y1 = outline
    pad = 1
    return svg((x0 - pad, y0 - pad, (x1 - x0) + 2 * pad, (y1 - y0) + 2 * pad), panel_body(outline, holes, silk),
               "ST-03 Attenuverter front panel")


def main():
    data = parse(PCB)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "panel.svg").write_text(annotated(*data))
    (OUT / "panel-plain.svg").write_text(plain(*data))
    print("wrote", OUT / "panel.svg", "and", OUT / "panel-plain.svg")


if __name__ == "__main__":
    main()

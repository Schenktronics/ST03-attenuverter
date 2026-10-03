#!/usr/bin/env python3
"""Generate the assembly-guide drawings.

The front and back board views come from the KiCad PCB file. The side view
is a diagram, not to scale, positioned using the same part locations.

Writes docs/images/assembly-*.svg.
Run from anywhere: python3 docs/drawings/make_assembly_svgs.py
"""
import math
import re
from pathlib import Path

from make_panel_svg import FONT, INK, RED, svg

ROOT = Path(__file__).resolve().parents[2]
PCB = ROOT / "Attenuverter" / "Attenuverter.kicad_pcb"
OUT = ROOT / "docs" / "images"

GREY = "#888"
FAINT = "#c8c8c8"
LIGHT = "#f1f1f1"
PAD = "#d6d6d6"
TINT = "#fbe3e2"


# ---------------------------------------------------------------- parsing

def read_sexpr(text):
    """Parse a KiCad S-expression file into nested lists of strings."""
    tokens = re.findall(r'"(?:[^"\\]|\\.)*"|[()]|[^\s()"]+', text)
    stack, root = [], []
    cur = root
    for tok in tokens:
        if tok == "(":
            new = []
            cur.append(new)
            stack.append(cur)
            cur = new
        elif tok == ")":
            cur = stack.pop()
        else:
            cur.append(tok[1:-1] if tok.startswith('"') else tok)
    return root[0]


def kids(node, head):
    return [c for c in node[1:] if isinstance(c, list) and c and c[0] == head]


def kid(node, head):
    found = kids(node, head)
    return found[0] if found else None


def nums(node):
    return [float(v) for v in node[1:] if re.fullmatch(r"-?[\d.]+", v)]


def parse(path):
    tree = read_sexpr(path.read_text())
    edges = []
    for g in kids(tree, "gr_line"):
        if kid(g, "layer")[1] == "Edge.Cuts":
            (x1, y1), (x2, y2) = nums(kid(g, "start")), nums(kid(g, "end"))
            edges.append((x1, y1, x2, y2))
    xs = [v for e in edges for v in (e[0], e[2])]
    ys = [v for e in edges for v in (e[1], e[3])]
    outline = (min(xs), min(ys), max(xs), max(ys))

    parts = []
    for fp in kids(tree, "footprint"):
        side = "B" if kid(fp, "layer")[1].startswith("B.") else "F"
        at = nums(kid(fp, "at"))
        mx, my = at[0], at[1]
        fp_rot = at[2] if len(at) > 2 else 0.0
        a = math.radians(fp_rot)

        def place(x, y, mx=mx, my=my, a=a):
            # KiCad rotates footprints counter-clockwise on a y-down board.
            return (mx + x * math.cos(a) + y * math.sin(a), my - x * math.sin(a) + y * math.cos(a))

        ref_prop = next(p for p in kids(fp, "property") if p[1] == "Reference")
        label = nums(kid(ref_prop, "at"))
        ref = ref_prop[2]
        part = dict(ref=ref, side=side, at=(mx, my), label_at=(label[0], label[1]),
                    lines=[], circles=[], pads=[], place=place)
        silk = f"{side}.SilkS"
        for line in kids(fp, "fp_line"):
            if kid(line, "layer")[1] == silk:
                x1, y1 = nums(kid(line, "start"))
                x2, y2 = nums(kid(line, "end"))
                part["lines"].append((*place(x1, y1), *place(x2, y2)))
        for circ in kids(fp, "fp_circle"):
            if kid(circ, "layer")[1] == silk:
                cx, cy = nums(kid(circ, "center"))
                ex, ey = nums(kid(circ, "end"))
                part["circles"].append((*place(cx, cy), math.hypot(ex - cx, ey - cy)))
        for pad in kids(fp, "pad"):
            name, kind, shape = pad[1], pad[2], pad[3]
            pa = nums(kid(pad, "at"))
            px, py = place(pa[0], pa[1])
            pad_rot = pa[2] if len(pa) > 2 else 0.0
            w, h = nums(kid(pad, "size"))
            dw = dh = 0.0
            drill = kid(pad, "drill")
            if drill is not None:
                if drill[1] == "oval":
                    dw, dh = drill[2], drill[3]
                else:
                    dw = dh = drill[1]
                dw, dh = float(dw), float(dh)
            # Pad angles are relative to the footprint; swap width and height when the pad is turned 90°.
            if (pad_rot + fp_rot) % 180 == 90:
                w, h, dw, dh = h, w, dh, dw
            part["pads"].append(dict(name=name, kind=kind, shape=shape, x=px, y=py, w=w, h=h, dw=dw, dh=dh))
        parts.append(part)

    # Board-level lines and text on the back silkscreen ("Red Stripe", "-12v +12v").
    back = dict(lines=[], texts=[])
    for g in kids(tree, "gr_line"):
        if kid(g, "layer")[1] == "B.SilkS":
            back["lines"].append((*nums(kid(g, "start")), *nums(kid(g, "end"))))
    for t in kids(tree, "gr_text"):
        if kid(t, "layer")[1] == "B.SilkS":
            at = nums(kid(t, "at"))
            back["texts"].append((t[1].replace("\\n", " "), at[0], at[1], at[2] if len(at) > 2 else 0.0))
    return outline, parts, back


# ------------------------------------------------------------- board views

class BoardView:
    """Draws the board lying horizontally, with the top of the panel (J1, RV1) on the left.

    front=True looks at the pot and jack side; front=False looks at the
    surface-mount side (the board flipped over its long edge).
    """

    def __init__(self, outline, ox, oy, front):
        self.x0, self.y0, self.x1, self.y1 = outline
        self.ox, self.oy, self.front = ox, oy, front

    def pt(self, x, y):
        u = y - self.y0
        v = (self.x1 - x) if self.front else (x - self.x0)
        return self.ox + u, self.oy + v

    def size(self, w, h):
        return h, w  # Board x runs vertically in the drawing.

    def board(self):
        w, h = self.y1 - self.y0, self.x1 - self.x0
        return [f"<rect x='{self.ox}' y='{self.oy}' width='{w}' height='{h}' rx='0.6' "
                f"fill='{LIGHT}' stroke='{INK}' stroke-width='0.35'/>"]

    def pad(self, p, fill=PAD, stroke=GREY):
        cx, cy = self.pt(p["x"], p["y"])
        w, h = self.size(p["w"], p["h"])
        out = []
        if p["kind"] != "np_thru_hole":
            if p["shape"] == "circle":
                out.append(f"<circle cx='{cx:.3f}' cy='{cy:.3f}' r='{w / 2}' fill='{fill}' stroke='{stroke}' stroke-width='0.15'/>")
            else:
                r = min(w, h) / 2 if p["shape"] == "oval" else 0.15
                out.append(f"<rect x='{cx - w / 2:.3f}' y='{cy - h / 2:.3f}' width='{w}' height='{h}' rx='{r}' "
                           f"fill='{fill}' stroke='{stroke}' stroke-width='0.15'/>")
        dw, dh = self.size(p["dw"], p["dh"])
        if dw:
            out.append(f"<rect x='{cx - dw / 2:.3f}' y='{cy - dh / 2:.3f}' width='{dw}' height='{dh}' "
                       f"rx='{min(dw, dh) / 2}' fill='#fff' stroke='{GREY if p['kind'] == 'np_thru_hole' else 'none'}' "
                       f"stroke-width='0.15'/>")
        return out

    def pads(self, part, **style):
        """The pads of a part that show from this side."""
        mine = part["side"] == ("F" if self.front else "B")
        return [e for p in part["pads"] if p["kind"] != "smd" or mine for e in self.pad(p, **style)]

    def silk(self, part, color=GREY, width=0.2):
        out = []
        for x1, y1, x2, y2 in part["lines"]:
            a, b = self.pt(x1, y1), self.pt(x2, y2)
            out.append(f"<line x1='{a[0]:.3f}' y1='{a[1]:.3f}' x2='{b[0]:.3f}' y2='{b[1]:.3f}' "
                       f"stroke='{color}' stroke-width='{width}' stroke-linecap='round'/>")
        for cx, cy, r in part["circles"]:
            c = self.pt(cx, cy)
            out.append(f"<circle cx='{c[0]:.3f}' cy='{c[1]:.3f}' r='{r}' fill='none' stroke='{color}' stroke-width='{width}'/>")
        return out

    def ref(self, part, color=GREY, size=1.5, weight="normal"):
        x, y = self.pt(*part["label_at"])
        return [f"<text x='{x:.3f}' y='{y:.3f}' {FONT} font-size='{size}' font-weight='{weight}' fill='{color}' "
                f"text-anchor='middle' dominant-baseline='central'>{part['ref']}</text>"]


def text(x, y, s, size=2.6, weight="normal", color=INK, anchor="start"):
    return (f"<text x='{x:.2f}' y='{y:.2f}' {FONT} font-size='{size}' font-weight='{weight}' fill='{color}' "
            f"text-anchor='{anchor}' dominant-baseline='central'>{s}</text>")


def arrow_defs():
    return (f"<defs><marker id='arr' viewBox='0 0 10 10' refX='8' refY='5' markerWidth='5' markerHeight='5' "
            f"orient='auto-start-reverse'><path d='M0 1 L10 5 L0 9 z' fill='{INK}'/></marker></defs>")


def arrow(x1, y1, x2, y2, color=INK, width=0.35):
    return (f"<line x1='{x1:.2f}' y1='{y1:.2f}' x2='{x2:.2f}' y2='{y2:.2f}' stroke='{color}' "
            f"stroke-width='{width}' marker-end='url(#arr)'/>")


def leader(x1, y1, x2, y2, color=RED):
    return [f"<line x1='{x1:.2f}' y1='{y1:.2f}' x2='{x2:.2f}' y2='{y2:.2f}' stroke='{color}' stroke-width='0.25'/>",
            f"<circle cx='{x1:.2f}' cy='{y1:.2f}' r='0.45' fill='{color}'/>"]


def view_title(x, y, title, sub):
    return [text(x, y, title, 3, "bold"), text(x, y + 3.6, sub, 2.2, color=GREY)]


def end_labels(view, y):
    w = view.y1 - view.y0
    return [text(view.ox, y, "Top of panel (J1, RV1)", 2, color=GREY),
            text(view.ox + w, y, "Bottom (J9, RV4)", 2, color=GREY, anchor="end")]


def back_silk(view, back, color=GREY):
    """Board-level text on the back, turned so it reads left to right or bottom to top."""
    out = []
    for x1, y1, x2, y2 in back["lines"]:
        a, b = view.pt(x1, y1), view.pt(x2, y2)
        out.append(f"<line x1='{a[0]:.3f}' y1='{a[1]:.3f}' x2='{b[0]:.3f}' y2='{b[1]:.3f}' stroke='{color}' stroke-width='0.5'/>")
    for s, x, y, rot in back["texts"]:
        # Back text reads normally from behind: along +x rotated by rot, mirrored.
        r = math.radians(rot)
        dx, dy = -math.cos(r), -math.sin(r)
        # Words separated by runs of spaces ("-12v      +12v") are drawn separately,
        # because SVG collapses the spaces. Each character is taken as 0.5 mm wide,
        # which puts the words where they are on the board.
        for word in re.finditer(r"\S+(?: \S+)*", s):
            off = ((word.start() + word.end()) / 2 - len(s) / 2) * 0.5
            vx, vy = view.pt(x + dx * off, y + dy * off)
            ux, uy = (dy, dx) if not view.front else (dy, -dx)
            deg = math.degrees(math.atan2(uy, ux))
            if deg > 90 or deg <= -90:
                deg -= 180
            out.append(f"<text x='{vx:.2f}' y='{vy:.2f}' {FONT} font-size='1.4' fill='{color}' text-anchor='middle' "
                       f"dominant-baseline='central' transform='rotate({deg:.0f} {vx:.2f} {vy:.2f})'>{word[0]}</text>")
    return out


def by_ref(parts, ref):
    return next(p for p in parts if p["ref"] == ref)


def pad_of(part, name):
    return next(p for p in part["pads"] if p["name"] == name)


# ----------------------------------------------------------------- figures

OFFSET = -10  # faceplate y = PCB y - 10 (from the two KiCad files)
PANEL_TOP, PANEL_BOT = 25.75, 154.25  # faceplate outline, in faceplate coordinates
PANEL_SCREWS = (28.75, 151.25)


def smd(parts):
    return [p for p in parts if p["side"] == "B" and p["ref"] != "J7"]


def pots(parts):
    return [p for p in parts if p["ref"].startswith("RV")]


def jacks(parts):
    return [p for p in parts if p["ref"].startswith("J") and p["ref"] != "J7"]


def shaft(pot):
    """A pot's shaft sits midway between its two mounting lugs."""
    lugs = [p for p in pot["pads"] if not p["name"]]
    return ((lugs[0]["x"] + lugs[1]["x"]) / 2, (lugs[0]["y"] + lugs[1]["y"]) / 2)


def jack_hole(jack):
    return next(((p["x"], p["y"]) for p in jack["pads"] if p["kind"] == "np_thru_hole"))


def fig_smd(outline, parts, back):
    """Step 1: surface-mount parts on the back. Mark the parts that have a direction."""
    h = outline[2] - outline[0]
    v = BoardView(outline, 0, 8, front=False)
    body = view_title(0, 2.5, "Back (surface-mount side)", "Solder every part labelled here. Red marks the ends that matter.")
    body += v.board() + back_silk(v, back, color=FAINT)
    for p in parts:
        if p in smd(parts):
            body += v.pads(p) + v.silk(p, color=GREY, width=0.15) + v.ref(p, color=INK, size=1.3)
        else:
            body += v.pads(p, fill="#fff", stroke=FAINT)
    # Parts that only fit one way round.
    u1 = by_ref(parts, "U1")
    diodes = [by_ref(parts, f"D{i}") for i in range(1, 12)]
    for part in [u1] + diodes:
        body += v.pad(pad_of(part, "1"), fill=RED, stroke=RED)
    row1, row2 = 8 + h + 7, 8 + h + 11
    x, y = v.pt(pad_of(u1, "1")["x"], pad_of(u1, "1")["y"])
    body += leader(x, y, x, row1)
    body.append(text(x + 1, row1, "U1: the pin 1 dot goes on the red pad", 2.2, "bold", color=RED))
    # Eleven diodes are too many for leader lines, so their red pads are labelled once.
    body.append(text(0, row2, "D1–D11: the stripe (cathode) goes on the red pad", 2.2, "bold", color=RED))
    body += end_labels(v, 8 + h + 2.2)
    return svg((-3, -3, 106, h + 25), body, "Step 1: surface-mount parts")


def fig_header(outline, parts, back):
    """Step 2: the power header goes on the back, with its notch matching the outline."""
    h = outline[2] - outline[0]
    v = BoardView(outline, 0, 8, front=False)
    body = view_title(0, 2.5, "Back (surface-mount side)", "Fit J7 here and solder its pins on the front.")
    body += v.board() + back_silk(v, back, color=INK)
    j7 = by_ref(parts, "J7")
    for p in parts:
        if p is j7:
            body += v.pads(p, fill="#fff", stroke=RED) + v.silk(p, color=RED, width=0.3) + v.ref(p, color=RED, size=1.6, weight="bold")
        else:
            body += v.pads(p, fill="#fff", stroke=FAINT)
    # The footprint's outline has a gap (footprint x = -2.794, y = -2.54 to -7.62)
    # where the shroud's notch goes.
    row1, row2 = 8 + h + 7, 8 + h + 11
    p1 = v.pt(pad_of(j7, "1")["x"], pad_of(j7, "1")["y"])
    body += leader(p1[0], p1[1], p1[0], row1)
    body.append(text(p1[0] + 1, row1, "Pin 1 (square pad) is −12 V: the red stripe goes this side", 2.2, "bold", color=RED))
    nx, ny = v.pt(*j7["place"](-2.794, -5.08))
    body += leader(nx, ny, nx + 3, row2)
    body.append(text(nx + 4, row2, "The shroud's notch goes at the gap in the outline", 2.2, "bold", color=RED))
    body += end_labels(v, 8 + h + 2.2)
    return svg((-3, -3, 106, h + 25), body, "Step 2: power header")


def fig_parts(outline, parts):
    """Step 3: pots and jacks go in from the front, not soldered yet."""
    h = outline[2] - outline[0]
    v = BoardView(outline, 0, 8, front=True)
    body = view_title(0, 2.5, "Front (pot and jack side)", "Fit RV1–RV4 and the eight jacks. Don't solder yet.")
    body += v.board()
    for p in parts:
        if p in pots(parts) or p in jacks(parts):
            body += v.pads(p) + v.silk(p, color=RED, width=0.3) + v.ref(p, color=RED)
        else:
            body += v.pads(p, fill="#fff", stroke=FAINT)
    for p in pots(parts):
        x, y = v.pt(*shaft(p))
        body.append(f"<circle cx='{x:.2f}' cy='{y:.2f}' r='3' fill='{TINT}' stroke='{RED}' stroke-width='0.35'/>")
    body += end_labels(v, 8 + h + 2.2)
    return svg((-3, -3, 106, h + 16), body, "Step 3: fit the pots and jacks")


def fig_faceplate(outline, parts):
    """Step 4: exploded side view of pots, jacks, faceplate and nuts."""
    x0, y0, x1, y1 = outline
    jack_ys = sorted(jack_hole(j)[1] for j in jacks(parts))
    pot_ys = sorted(shaft(p)[1] for p in pots(parts))
    panel_top, panel_bot = PANEL_TOP - OFFSET, PANEL_BOT - OFFSET
    u = lambda y: y - panel_top + 2  # drawing x for a board y

    pcb_y, body_h, bush_h = 60, 9, 4.5
    body_top = pcb_y - body_h
    panel_y = body_top - 18  # exploded gap
    nut_y = panel_y - 9

    body = [arrow_defs()]
    body.append(f"<rect x='{u(y0)}' y='{pcb_y}' width='{y1 - y0}' height='1.6' fill='{LIGHT}' stroke='{INK}' stroke-width='0.3'/>")
    # Surface-mount parts and the power header underneath.
    for p in smd(parts):
        x = u(p["at"][1])
        body.append(f"<rect x='{x - 1}' y='{pcb_y + 1.6}' width='2' height='0.8' fill='{PAD}' stroke='{GREY}' stroke-width='0.1'/>")
    j7 = u(by_ref(parts, "J7")["at"][1]) - 5
    body.append(f"<rect x='{j7}' y='{pcb_y + 1.6}' width='10' height='6' rx='0.3' fill='#fff' stroke='{INK}' stroke-width='0.3'/>")
    legs = lambda x, dxs: [f"<line x1='{x + dx}' y1='{pcb_y + 1.6}' x2='{x + dx}' y2='{pcb_y + 3.2}' "
                           f"stroke='{INK}' stroke-width='0.35'/>" for dx in dxs]
    thread = lambda x, w, top: [f"<line x1='{x - w}' y1='{top + dy}' x2='{x + w}' y2='{top + dy}' "
                                f"stroke='{GREY}' stroke-width='0.15'/>" for dy in (1.2, 2.4, 3.6)]
    for y in pot_ys:
        # The pots sit beside the jacks, so from this side they're behind them.
        # They have no threaded bushing: just a body and a D shaft.
        x = u(y)
        body.append(f"<rect x='{x - 5}' y='{body_top + 1}' width='10' height='{body_h - 1}' rx='0.4' fill='{LIGHT}' stroke='{GREY}' stroke-width='0.3'/>")
        body.append(f"<rect x='{x - 3}' y='{body_top - 20}' width='6' height='21' fill='{TINT}' stroke='{RED}' stroke-width='0.35'/>")
        body += legs(x, (-4.75, -2.5, 0, 4.75))
    for y in jack_ys:
        x = u(y)
        body.append(f"<rect x='{x - 4.5}' y='{body_top}' width='9' height='{body_h}' rx='0.4' fill='#fff' stroke='{INK}' stroke-width='0.35'/>")
        body.append(f"<rect x='{x - 3}' y='{body_top - bush_h}' width='6' height='{bush_h}' fill='#fff' stroke='{INK}' stroke-width='0.35'/>")
        body += thread(x, 3, body_top - bush_h) + legs(x, (-3, 3))

    # Faceplate, cut away at each hole.
    holes = sorted([(y, 6.0) for y in jack_ys] + [(y, 7.0) for y in pot_ys] +
                   [(s - OFFSET, 3.2) for s in PANEL_SCREWS])
    edges = [u(panel_top)]
    for y, d in holes:
        edges += [u(y) - d / 2, u(y) + d / 2]
    edges.append(u(panel_bot))
    for a, b in zip(edges[::2], edges[1::2]):
        body.append(f"<rect x='{a:.2f}' y='{panel_y}' width='{b - a:.2f}' height='1.6' fill='{INK}'/>")

    # Jack nuts. The pots have none.
    for y in jack_ys:
        x = u(y)
        body.append(f"<rect x='{x - 4}' y='{nut_y}' width='8' height='2.2' rx='0.3' fill='#fff' stroke='{INK}' stroke-width='0.35'/>")
        for dx in (-2.5, -0.8, 0.8, 2.5):
            body.append(f"<line x1='{x + dx}' y1='{nut_y}' x2='{x + dx}' y2='{nut_y + 2.2}' stroke='{GREY}' stroke-width='0.15'/>")

    # Arrows and labels.
    for y in (jack_ys[0], jack_ys[-1]):
        body.append(arrow(u(y), nut_y + 3, u(y), panel_y - 0.8, width=0.3))
        body.append(arrow(u(y), panel_y + 2.8, u(y), body_top - bush_h - 0.8, width=0.3))
    lx = u(panel_bot) + 3
    body.append(text(lx, nut_y + 1.1, "Jack nuts", 2.6, "bold"))
    body.append(text(lx, nut_y + 4.3, "finger-tight first", 2.2, color=GREY))
    body.append(text(lx, panel_y + 0.8, "Faceplate", 2.6, "bold"))
    body.append(text(lx, panel_y + 4, "“Attenuverter” end over J1", 2.2, color=GREY))
    body.append(text(lx, body_top + 3, "Pots and jacks", 2.6, "bold"))
    body.append(text(lx, body_top + 6.2, "not soldered yet", 2.2, color=GREY))
    body.append(text(lx, pcb_y + 0.8, "PCB", 2.6, "bold"))
    body.append(text(lx, pcb_y + 4, "surface-mount parts and J7 underneath", 2.2, color=GREY))
    mid = (u(pot_ys[1]) + u(pot_ys[2])) / 2
    body.append(text(mid, pcb_y + 11, "Center the pot shafts in their holes,", 2.6, "bold", color=RED, anchor="middle"))
    body.append(text(mid, pcb_y + 14.2, "then tighten the jack nuts", 2.2, color=GREY, anchor="middle"))
    body.append(text(u(y0), pcb_y + 11, "Top (J1 end)", 2, color=GREY))
    body.append(text(u(y1), pcb_y + 11, "Bottom (J9 end)", 2, color=GREY, anchor="end"))
    body.append(text(u(panel_top), pcb_y + 19, "Side view, not to scale vertically", 2, color=GREY))
    return svg((u(panel_top) - 2, nut_y - 4, (panel_bot - panel_top) + 48, pcb_y - nut_y + 26), body,
               "Step 4: fit the faceplate")


def fig_solder(outline, parts, back):
    """Step 5: back view. Tack one leg of each pot and jack, then the rest."""
    h = outline[2] - outline[0]
    v = BoardView(outline, 0, 8, front=False)
    body = [text(0, 2.5, "Back (surface-mount side)", 3, "bold")]
    body += v.board() + back_silk(v, back, color=FAINT)
    tacks = 0
    for p in parts:
        if p in pots(parts) or p in jacks(parts):
            tack = "S" if p["ref"].startswith("J") else "2"
            for pad in p["pads"]:
                if pad["kind"] == "np_thru_hole":
                    body += v.pad(pad)
                elif pad["name"] == tack:
                    body += v.pad(pad, fill=RED, stroke=RED)
                    tacks += 1
                else:
                    body += v.pad(pad, fill="#fff", stroke=RED)
        else:
            body += v.pads(p, fill=PAD, stroke=FAINT)
    rest = sum(1 for p in pots(parts) + jacks(parts) for pad in p["pads"] if pad["kind"] == "thru_hole") - tacks
    body += end_labels(v, 8 + h + 2.2)
    ky = 8 + h + 8
    body += [f"<rect x='0' y='{ky - 1.2}' width='2.4' height='2.4' rx='0.2' fill='{RED}'/>",
             text(3.6, ky, f"1. Tack these first: one leg per pot and jack ({tacks} joints)", 2.4),
             f"<rect x='0' y='{ky + 3.3}' width='2.4' height='2.4' rx='1.2' fill='#fff' stroke='{RED}' stroke-width='0.3'/>",
             text(3.6, ky + 4.5, f"2. Then the rest, including the 8 large pot lugs ({rest} joints)", 2.4)]
    return svg((-3, -1, 106, ky + 9), body, "Step 5: solder the pots and jacks")


def main():
    outline, parts, back = parse(PCB)
    OUT.mkdir(parents=True, exist_ok=True)
    figs = {
        "assembly-1-smd.svg": fig_smd(outline, parts, back),
        "assembly-2-header.svg": fig_header(outline, parts, back),
        "assembly-3-parts.svg": fig_parts(outline, parts),
        "assembly-4-faceplate.svg": fig_faceplate(outline, parts),
        "assembly-5-solder.svg": fig_solder(outline, parts, back),
    }
    for name, content in figs.items():
        (OUT / name).write_text(content)
        print("wrote", OUT / name)


if __name__ == "__main__":
    main()

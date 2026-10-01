"""Build dist/complexity-pathways-map.png from data/site-data.json.

Run: python3 build/build_map.py
"""
import json, pathlib, re, textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

ROOT = pathlib.Path(__file__).resolve().parent.parent
D = json.load(open(ROOT / "data" / "site-data.json"))
INK, BG, GOLD = "#1f2a2e", "#fbfaf7", "#b07a1c"
plt.rcParams["font.family"] = "DejaVu Sans"

def people(road, width):
    """Lead name of each road step, keeping only whole names that fit on two wrapped lines."""
    parts = [re.sub(r"<[^>]+>", "", s).split("(")[0].strip() for s in road.split("→")]
    out = []
    for part in (p for p in parts if p):
        trial = " · ".join(out + [part])
        if len(textwrap.wrap(trial, width)) > 2: break
        out.append(part)
    return " · ".join(out) or parts[0][:width]

W, CH, GAP, HEAD = 16.0, 1.32, 0.18, 0.62
fig, ax = plt.subplots(figsize=(W, 40), dpi=150)
ax.axis("off"); fig.patch.set_facecolor(BG)

def chip(x, y, w, p, col):
    ax.add_patch(FancyBboxPatch((x, y - CH), w, CH, boxstyle="round,pad=0,rounding_size=0.14", fc=col, ec="white", lw=1.2))
    lines = textwrap.wrap(p["name"], int(w * 6.6))
    ax.text(x + 0.18, y - 0.14, "\n".join(lines), color="white", fontsize=10 if len(lines) < 3 else 9, weight="bold", va="top", linespacing=1.05)
    pw = int(w * 10.8) if len(lines) < 3 else int(w * 12)
    ax.text(x + 0.18, y - CH + 0.12, "\n".join(textwrap.wrap(people(p["road"], pw), pw)), color="#f0f0f0", fontsize=7.6 if len(lines) < 3 else 7, va="bottom", linespacing=1.15)
    ax.text(x + w - 0.14, y - 0.14, p["kind"], color="white", fontsize=7.2, ha="right", va="top", alpha=0.85)
    if p["gov"]:
        ax.add_patch(Circle((x + w - 0.26, y - CH + 0.3), 0.16, fc=GOLD, ec="white", lw=1.1, zorder=5))
        ax.text(x + w - 0.26, y - CH + 0.29, "★", ha="center", va="center", color="white", fontsize=8.5, zorder=6)

def panel(x, y, w, cl, ncols):
    ps = [p for p in D["pathways"] if p["cluster"] == cl["name"]]
    col = cl["light"]
    ax.text(x, y - 0.3, cl["name"].upper(), color=col, fontsize=11, weight="bold", va="center")
    ax.plot([x, x + w], [y - 0.52, y - 0.52], color=col, lw=1.5)
    y -= HEAD
    cw = (w - GAP * (ncols - 1)) / ncols
    for i, p in enumerate(ps):
        r, c = divmod(i, ncols)
        chip(x + c * (cw + GAP), y - r * (CH + GAP), cw, p, col)
    return y - (-(-len(ps) // ncols)) * (CH + GAP) - 0.3

y = -0.3
n_p, n_c = len(D["pathways"]), len(D["clusters"])
ax.text(W / 2, y - 0.4, "Pathways into Complexity", ha="center", fontsize=26, weight="bold", color=INK)
ax.text(W / 2, y - 1.05, f"{n_p} pathways in {n_c} clusters, their key figures, and where they meet government", ha="center", fontsize=12, color="#555555")
y -= 1.55
ax.add_patch(FancyBboxPatch((0.4, y - 1.0), W - 0.8, 1.0, boxstyle="round,pad=0,rounding_size=0.2", fc="#fdf3dc", ec=GOLD, lw=1.8))
ax.text(0.75, y - 0.5, "POLICY LENS", color="#8a6212", fontsize=12, weight="bold", va="center")
ax.text(3.0, y - 0.5, "Every pathway applies to public policy and government innovation.\n★ marks pathways with a strong track record inside government. Top right of each chip: kind of path.",
        color="#5a4210", fontsize=10.2, va="center", linespacing=1.3)
y -= 1.45

C = {c["name"]: c for c in D["clusters"]}
L, CW = 0.4, (W - 0.8 - 0.4) / 2
R = L + CW + 0.4
pairs = [("Foundations and science", "Organizing and sensemaking"),
         ("Relational, Indigenous, and meaning", "Movements and hosting"),
         ("Living systems", "Power, narrative, and conflict"),
         ("Crisis and transition", "Policy, systemic design, and economics")]
for a, b in pairs:
    ya = panel(L, y, CW, C[a], 2); yb = panel(R, y, CW, C[b], 2)
    y = min(ya, yb)
for name in ("Living practices", "Strategy, money, and accountability", "Design and practice", "Learning and pedagogy"):
    y = panel(L, y, W - 0.8, C[name], 3)

y -= 0.1
braids = D["braids"]
bh = 0.55 + 0.4 * len(braids)
ax.add_patch(FancyBboxPatch((0.4, y - bh), W - 0.8, bh, boxstyle="round,pad=0,rounding_size=0.2", fc="#eef4f2", ec="none"))
ax.plot([0.4, 0.4], [y - bh + 0.05, y - 0.05], color="#2f6f62", lw=4)
ax.text(0.75, y - 0.35, "SUGGESTED BRAIDS", color="#2f6f62", fontsize=11, weight="bold", va="center")
for i, b in enumerate(braids):
    ax.text(0.75, y - 0.8 - i * 0.4, f"•  {b['pair']}: {b['why']}"[:150], color=INK, fontsize=9.6, va="center")
y -= bh + 0.3

ax.set_xlim(0, W); ax.set_ylim(y, 0)
fig.set_size_inches(W, -y); ax.set_position([0, 0, 1, 1])
out = ROOT / "dist" / "complexity-pathways-map.png"
plt.savefig(out, facecolor=BG, dpi=150)
print(f"ok: {out}")

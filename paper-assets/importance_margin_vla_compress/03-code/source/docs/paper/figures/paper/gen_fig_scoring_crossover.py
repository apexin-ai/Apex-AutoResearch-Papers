"""
Scoring Crossover Heatmap — Model × Suite at k=0.9
Data sourced from experiment registry (2026-05-25).
Narrative: The optimal scoring method depends on both connector type
and task suite, with crossovers occurring across and within models.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Liberation Serif', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
    'font.size': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

OUT = Path(__file__).parent

# ── Data (k=0.9, from registry + Table 1) ──────────────────
# None = data not available for this model/suite/method

DATA = {
    'pi05': {
        'object':  {'l2': 98.2, 'random':  9.0, 'attn': 97.2},
        'spatial': {'l2': 95.0, 'random': 54.6, 'attn': None},
        'goal':    {'l2': 90.6, 'random': 62.2, 'attn': None},
        'long':    {'l2': 81.0, 'random': 31.8, 'attn': 63.8},
    },
    'xvla': {
        'object':  {'l2': 99.2, 'random': 97.8, 'attn': None},
        'spatial': {'l2': 78.8, 'random': 77.8, 'attn': None},
        'goal':    {'l2': 70.2, 'random': 70.6, 'attn': None},
        'long':    {'l2': 27.5, 'random': 29.6, 'attn': None},
    },
    'openvla': {
        'object':  {'l2': 70.6, 'random': 62.8, 'attn': 61.4},
        'spatial': {'l2': 75.0, 'random': 79.8, 'attn': 80.4},
        'goal':    {'l2': 74.8, 'random': 79.6, 'attn': 73.2},
        'long':    {'l2': 43.6, 'random': 46.8, 'attn': 44.0},
    },
    'smolvla': {
        'all':     {'l2': 0.0, 'random': 0.0, 'attn': None},
    },
}

BASELINES = {
    'pi05':    {'object': 98.2, 'spatial': 97.2, 'goal': 96.4, 'long': 91.6},
    'xvla':    {'object': 99.2, 'spatial': 93.0, 'goal': 98.4, 'long': 94.0},
    'openvla': {'object': 74.0, 'spatial': 80.0, 'goal': 74.8, 'long': 52.8},
    'smolvla': {'object': 59.2, 'spatial': 44.6, 'goal': 60.8, 'long': 36.6},
}

# ── Assertions ──────────────────────────────────────────────

assert DATA['pi05']['object']['l2'] > 90, \
    f"pi05 Object L2 should be >90%, got {DATA['pi05']['object']['l2']}"
assert DATA['smolvla']['all']['l2'] == 0.0, "SmolVLA should be 0%"
assert DATA['smolvla']['all']['random'] == 0.0, "SmolVLA should be 0%"
assert abs(DATA['openvla']['long']['l2'] - DATA['openvla']['long']['random']) < 5, \
    "OpenVLA Long should be method-indifferent"
assert DATA['pi05']['long']['l2'] == 81.0, \
    f"pi05 Long L2 should be 81.0%, got {DATA['pi05']['long']['l2']}"
assert DATA['openvla']['long']['l2'] == 43.6, "OpenVLA Long L2 data must exist"
assert DATA['openvla']['long']['random'] == 46.8, "OpenVLA Long Random data must exist"
assert DATA['openvla']['long']['attn'] == 44.0, "OpenVLA Long Attn data must exist"
assert DATA['xvla']['object']['l2'] == 99.2, "X-VLA Object L2 = 99.2% at k=0.9"

# ── Config ──────────────────────────────────────────────────

CW, CH = 1.65, 0.58
CG, RG = 0.06, 0.04
MG = 0.24
RAD = 0.05
THRESH = 3.5

METHODS = ['l2', 'random', 'attn']
MLABELS = {'l2': 'L2 Norm', 'random': 'Random', 'attn': 'Attention'}
WLABELS = {'l2': 'L2', 'random': 'R', 'attn': 'A'}
SLABELS = {'object': 'Object', 'spatial': 'Spatial',
           'goal': 'Goal', 'long': 'Long', 'all': 'All suites'}

MODELS = [
    ('pi05',    r'$\pi_{0.5}$',  'Linear proj.',  ['object', 'spatial', 'goal', 'long']),
    ('xvla',    'X-VLA',          'Linear + BART', ['object', 'spatial', 'goal', 'long']),
    ('openvla', 'OpenVLA',        'MLP proj.',     ['object', 'spatial', 'goal', 'long']),
    ('smolvla', 'SmolVLA',        'Pixel-shuffle', ['all']),
]

BAND_COLORS = {
    'pi05': '#edf2f9', 'xvla': '#f9f4eb',
    'openvla': '#edf6ed', 'smolvla': '#eeeeee',
}

# ── Helpers ─────────────────────────────────────────────────

def get_winner(sd):
    vs = {k: v for k, v in sd.items() if v is not None}
    if not vs or all(v == 0 for v in vs.values()):
        return None, True
    best = max(vs, key=vs.get)
    gap = max(vs.values()) - min(vs.values())
    return best, gap < THRESH


def cell_color(sr, bl, smol=False):
    if sr is None:
        return '#f0f0f0'
    if smol:
        return '#e0e0e0'
    ratio = np.clip(sr / max(bl, 1), 0, 1)
    LO = np.array([0.950, 0.760, 0.760])
    MI = np.array([0.996, 0.950, 0.815])
    HI = np.array([0.800, 0.905, 0.785])
    if ratio <= 0.5:
        t = ratio / 0.5
        c = LO * (1 - t) + MI * t
    else:
        t = (ratio - 0.5) / 0.5
        c = MI * (1 - t) + HI * t
    return tuple(np.clip(c, 0, 1))

# ── Compute positions ──────────────────────────────────────

xcols = [i * (CW + CG) for i in range(3)]
xend = 3 * CW + 2 * CG
xwin = xend + 0.25

all_rows = []
band_ranges = {}
y = 0

for mk, ml, mc, suites in MODELS:
    yt = y + 0.06
    for s in suites:
        all_rows.append((mk, s, y))
        y -= (CH + RG)
    band_ranges[mk] = (yt, y + RG - 0.06)
    y -= MG

ybot = y + MG

# ── Figure ──────────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(7.5, 5.8))
ax.set_xlim(-2.65, xwin + 1.1)
ax.set_ylim(ybot - 0.55, CH + 0.78)
ax.axis('off')

# Background bands
for mk, (yt, yb) in band_ranges.items():
    ax.add_patch(mpatches.FancyBboxPatch(
        (-2.45, yb), xwin + 0.9 + 2.45, yt - yb,
        boxstyle='round,pad=0,rounding_size=0.10',
        facecolor=BAND_COLORS[mk], edgecolor='none',
        alpha=0.50, zorder=0))

# Column headers
chy = CH + 0.30
for ci, m in enumerate(METHODS):
    ax.text(xcols[ci] + CW / 2, chy, MLABELS[m],
            ha='center', va='center', fontsize=10,
            fontweight='semibold', color='#333333')

ax.text(xwin + 0.35, chy, 'Best',
        ha='center', va='center', fontsize=8.5,
        fontweight='semibold', color='#888888')

# Subtitle
ax.text(xend / 2, chy + 0.32,
        'Success Rate (%) at k = 0.9',
        ha='center', va='center', fontsize=9,
        color='#999999', fontstyle='italic')

# Thin separator line below column headers
ax.plot([-0.15, xwin + 0.65], [chy - 0.22, chy - 0.22],
        color='#dddddd', linewidth=0.6, zorder=1)

# Vertical separator before "Best" column
first_y = all_rows[0][2] + 0.06
last_y = all_rows[-1][2] - CH - 0.06
ax.plot([xwin - 0.02, xwin - 0.02], [first_y, last_y],
        color='#e0e0e0', linewidth=0.5, zorder=1)

# Model labels — vertically centered in each group
for mk, ml, mc, suites in MODELS:
    yt, yb = band_ranges[mk]
    cy = (yt + yb) / 2
    ax.text(-2.40, cy + 0.07, ml,
            ha='left', va='center', fontsize=11.5,
            fontweight='bold', color='#222222')
    ax.text(-2.40, cy - 0.19, mc,
            ha='left', va='center', fontsize=7.5,
            color='#888888', fontstyle='italic')

# ── Data rows ───────────────────────────────────────────────

for mk, suite, ytop in all_rows:
    sd = DATA[mk][suite]
    smol = (mk == 'smolvla')
    if suite == 'all':
        bl = np.mean(list(BASELINES[mk].values()))
    else:
        bl = BASELINES[mk][suite]
    w, indiff = get_winner(sd)

    # Suite label (skip for SmolVLA — model label is enough)
    if not smol:
        ax.text(-0.12, ytop - CH / 2, SLABELS[suite],
                ha='right', va='center', fontsize=9, color='#444444')

    # Draw cells
    for ci, method in enumerate(METHODS):
        sr = sd.get(method, None)
        x0, y0 = xcols[ci], ytop - CH
        bg = cell_color(sr, bl, smol)

        # Border style
        if indiff and sr is not None and not smol:
            ls, ec, lw = '--', '#aaaaaa', 0.9
        else:
            ls, ec, lw = '-', '#dddddd', 0.5

        ax.add_patch(mpatches.FancyBboxPatch(
            (x0, y0), CW, CH,
            boxstyle=f'round,pad=0,rounding_size={RAD}',
            facecolor=bg, edgecolor=ec,
            linewidth=lw, linestyle=ls, zorder=2))

        # Gray overlay for method-indifferent
        if indiff and sr is not None and not smol:
            ax.add_patch(mpatches.FancyBboxPatch(
                (x0, y0), CW, CH,
                boxstyle=f'round,pad=0,rounding_size={RAD}',
                facecolor='#808080', edgecolor='none',
                alpha=0.06, zorder=2.5))

        cx, cy = x0 + CW / 2, y0 + CH / 2

        if sr is None:
            ax.text(cx, cy, '—', ha='center', va='center',
                    fontsize=10, color='#bbbbbb', zorder=3)
        else:
            is_win = (not indiff and w == method)
            fw = 'bold' if is_win else 'normal'
            fs = 11 if is_win else 10
            tc = '#999999' if smol else '#1a1a1a'
            txt = '0.0' if smol else f'{sr:.1f}'

            ax.text(cx, cy, txt, ha='center', va='center',
                    fontsize=fs, fontweight=fw, color=tc, zorder=3)

            if is_win:
                bar_h = CH * 0.55
                bar_y = y0 + (CH - bar_h) / 2
                ax.add_patch(mpatches.FancyBboxPatch(
                    (x0 + 0.04, bar_y), 0.06, bar_h,
                    boxstyle='round,pad=0,rounding_size=0.02',
                    facecolor='#0072B2', edgecolor='none',
                    alpha=0.65, zorder=3))

    # Winner annotation
    wy = ytop - CH / 2
    if smol:
        ax.text(xwin + 0.35, wy, 'collapsed',
                ha='center', va='center', fontsize=7.5,
                color='#999999', fontstyle='italic')
    elif indiff:
        ax.text(xwin + 0.35, wy, '≈',
                ha='center', va='center', fontsize=14,
                color='#999999', fontweight='bold')
    else:
        ax.text(xwin + 0.35, wy, WLABELS[w],
                ha='center', va='center', fontsize=9.5,
                color='#0072B2', fontweight='bold')

# ── Legend ──────────────────────────────────────────────────

ly = ybot - 0.28
lx = 0.0

ax.text(lx - 0.15, ly, 'Color:', ha='right', va='center',
        fontsize=7.5, color='#888888')

for i, (ratio, lab) in enumerate([
    (0, '0%'), (0.25, '25%'), (0.5, '50%'), (0.75, '75%'), (1.0, '100%')
]):
    sx = lx + i * 0.62
    c = cell_color(ratio * 100, 100)
    ax.add_patch(mpatches.Rectangle(
        (sx, ly - 0.07), 0.13, 0.14,
        facecolor=c, edgecolor='#dddddd', linewidth=0.3, zorder=3))
    ax.text(sx + 0.19, ly, lab, ha='left', va='center',
            fontsize=6.5, color='#888888')

ax.text(lx + 5 * 0.62 + 0.05, ly, 'SR / baseline',
        ha='left', va='center', fontsize=7,
        color='#aaaaaa', fontstyle='italic')

# Dashed border legend
dlx = lx + 5 * 0.62 + 1.3
ax.add_patch(mpatches.FancyBboxPatch(
    (dlx, ly - 0.07), 0.20, 0.14,
    boxstyle='round,pad=0,rounding_size=0.02',
    facecolor='#f4f4f4', edgecolor='#aaaaaa',
    linewidth=0.8, linestyle='--', zorder=3))
ax.text(dlx + 0.28, ly, 'method-indifferent (gap < 3.5 pp)',
        ha='left', va='center', fontsize=6.5, color='#aaaaaa')

# ── Save ────────────────────────────────────────────────────

plt.savefig(OUT / 'fig_scoring_crossover.pdf', format='pdf')
plt.savefig(OUT / 'fig_scoring_crossover.png', format='png')
print(f"Saved: {OUT / 'fig_scoring_crossover.pdf'}")
print(f"Saved: {OUT / 'fig_scoring_crossover.png'}")
plt.close()

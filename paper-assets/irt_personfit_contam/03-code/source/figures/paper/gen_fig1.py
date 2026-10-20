"""
Figure 1: Response pattern comparison between clean and contaminated models.
Generates a two-panel figure showing IRT response patterns with rug-style marks,
gradient-filled probability curves, and professional annotation boxes.

Output: fig_1_response_pattern.{pdf,png}
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.patches as mpatches
from matplotlib.collections import LineCollection
from pathlib import Path
from scipy.ndimage import uniform_filter1d

# ── Typography & global style ──────────────────────────────────────────────
matplotlib.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif', 'DejaVu Serif'],
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7.5,
    'text.usetex': False,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.linewidth': 0.5,
    'xtick.major.width': 0.5,
    'ytick.major.width': 0.5,
    'xtick.major.size': 0,      # hide x tick marks (ordinal)
    'ytick.major.size': 3,
})

np.random.seed(42)

# ── Data loading & IRT setup (DO NOT MODIFY) ──────────────────────────────
PROJ = Path(__file__).resolve().parent.parent.parent
df = pd.read_csv(PROJ / 'artifacts' / 'psn_irt_params' / 'mmlu_params.csv')

N = 300
df_sorted = df.sort_values('b_difficulty')
indices = np.linspace(0, len(df) - 1, N, dtype=int)
items = df_sorted.iloc[indices].reset_index(drop=True).sort_values('b_difficulty').reset_index(drop=True)

a = items['a_discrimination'].values
b = items['b_difficulty'].values
c = items['c_guessing'].values
d = items['d_feasibility'].values

theta = 0.5
p = c + (d - c) / (1 + np.exp(-a * (theta - b)))
p_clip = np.clip(p, 1e-10, 1 - 1e-10)

clean = (np.random.random(N) < p).astype(int)

# SFT contamination: ONLY flip seen items to correct (one-directional)
contam = clean.copy()
hard_wrong_idx = np.where((b > 0.3) & (contam == 0))[0]
np.random.seed(42)
n_flip = min(45, len(hard_wrong_idx))
flip_hard = np.random.choice(hard_wrong_idx, n_flip, replace=False)
contam[flip_hard] = 1

memorized = np.zeros(N, dtype=bool)
memorized[flip_hard] = True

def lz_star(resp, a, b, c, d, theta):
    pr = np.clip(c + (d - c) / (1 + np.exp(-a * (theta - b))), 1e-10, 1 - 1e-10)
    ll = np.sum(resp * np.log(pr) + (1 - resp) * np.log(1 - pr))
    mu = np.sum(pr * np.log(pr) + (1 - pr) * np.log(1 - pr))
    var = np.sum(pr * (1 - pr) * (np.log(pr / (1 - pr)))**2)
    return (ll - mu) / np.sqrt(var)

lz_c = lz_star(clean, a, b, c, d, theta)
lz_t = lz_star(contam, a, b, c, d, theta)
delta_lz = abs(lz_c - lz_t)
print(f"lz* clean = {lz_c:.2f}, lz* contam = {lz_t:.2f}, |Dlz*| = {delta_lz:.1f}")

# ── Color palette ──────────────────────────────────────────────────────────
NAVY       = '#2C3E50'   # correct responses
LIGHT_GRAY = '#95A5A6'   # incorrect responses (darker for print visibility)
ACAD_RED   = '#C0392B'   # memorized markers
STEEL_BLUE = '#4682B4'   # IRT curve & fill
CONN_RED   = '#C0392B'   # connection lines
GREEN_LZ   = '#2a7f2a'   # clean lz* annotation
GRAY_ANN   = '#888888'   # easy/hard annotations

# ── Figure setup ───────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.4), sharey=True)
fig.subplots_adjust(wspace=0.08)

x = np.arange(N)

# Rug tick dimensions
RUG_HEIGHT = 0.045       # height of each rug tick
RUG_LW     = 0.8         # linewidth for rug ticks


def draw_gradient_fill(ax, x_vals, y_vals, color, n_layers=30, max_alpha=0.15):
    """Draw gradient fill under curve: darker at bottom, fading toward curve."""
    for i in range(n_layers):
        frac_lo = i / n_layers
        frac_hi = (i + 1) / n_layers
        alpha = max_alpha * (1.0 - frac_lo * 0.85)  # darker at bottom
        ax.fill_between(
            x_vals,
            y_vals * frac_lo,
            y_vals * frac_hi,
            alpha=alpha, color=color, linewidth=0, zorder=1
        )


def draw_rug_ticks(ax, positions, y_centers, color, alpha=0.55, lw=RUG_LW, height=RUG_HEIGHT):
    """Draw rug-style vertical line segments at specified x positions.

    y_centers: scalar or array of per-tick y center positions.
    """
    y_centers = np.broadcast_to(np.asarray(y_centers, dtype=float), positions.shape)
    segments = [[(float(xi), float(yc - height / 2)),
                 (float(xi), float(yc + height / 2))]
                for xi, yc in zip(positions, y_centers)]
    if not segments:
        return
    lc = LineCollection(segments, colors=color, linewidths=lw, alpha=alpha, zorder=4)
    ax.add_collection(lc)


def draw_shadow_box(ax, x_pos, y_pos, text, color, transform):
    """Draw annotation box with subtle shadow effect."""
    # Shadow (offset, lighter)
    ax.text(x_pos + 0.003, y_pos - 0.008, text, transform=transform,
            ha='center', va='top', fontsize=8.5, fontweight='bold',
            color='none',
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#cccccc',
                      edgecolor='none', alpha=0.3, linewidth=0),
            zorder=7)
    # Main box
    ax.text(x_pos, y_pos, text, transform=transform,
            ha='center', va='top', fontsize=8.5, fontweight='bold',
            color=color,
            bbox=dict(boxstyle='round,pad=0.35', facecolor='white',
                      edgecolor=color, alpha=0.95, linewidth=0.6),
            zorder=8)


def plot_panel(ax, responses, title, is_contam=False):
    p_smooth = uniform_filter1d(p, size=7, mode='nearest')

    # ── Gradient fill under IRT curve ──
    draw_gradient_fill(ax, x, p_smooth, STEEL_BLUE, n_layers=30, max_alpha=0.15)

    # ── IRT probability curve ──
    ax.plot(x, p_smooth, color=STEEL_BLUE, linewidth=1.6, alpha=0.70,
            label='$P(X{=}1 \\mid \\theta)$', zorder=3)

    # ── Response rug ticks ──
    correct = responses == 1
    wrong = responses == 0

    # Slight jitter for rug y-positions to reduce exact overlap
    np.random.seed(77)
    jitter_1 = np.random.uniform(-0.008, 0.008, N)
    jitter_0 = np.random.uniform(-0.008, 0.008, N)

    if is_contam:
        # Normal correct (non-memorized)
        norm_c = correct & ~memorized
        draw_rug_ticks(ax, x[norm_c], 1.0 + jitter_1[norm_c], NAVY, alpha=0.55)
        # Incorrect
        draw_rug_ticks(ax, x[wrong], 0.0 + jitter_0[wrong], LIGHT_GRAY, alpha=0.70, lw=0.9)

        # Memorized items: diamond markers with white edge
        ax.scatter(x[memorized], np.ones(memorized.sum()) + jitter_1[memorized],
                   s=36, color=ACAD_RED, alpha=0.90, edgecolors='white',
                   linewidths=0.6, zorder=6, marker='D',
                   label='Memorized (seen)')

        # Connection lines from memorized to curve
        for idx in flip_hard:
            ax.plot([x[idx], x[idx]], [p_smooth[idx], 1.0 + jitter_1[idx]],
                    color=CONN_RED, alpha=0.28, linewidth=0.5,
                    linestyle='--', zorder=2)
    else:
        draw_rug_ticks(ax, x[correct], 1.0 + jitter_1[correct], NAVY, alpha=0.55)
        draw_rug_ticks(ax, x[wrong], 0.0 + jitter_0[wrong], LIGHT_GRAY, alpha=0.70, lw=0.9)

    # ── Subtle grid ──
    ax.axhline(y=0, color='#000000', alpha=0.08, linewidth=0.4, zorder=0)
    ax.axhline(y=1, color='#000000', alpha=0.08, linewidth=0.4, zorder=0)
    # Faint vertical gridlines
    for vx in np.arange(0, N, 50):
        ax.axvline(x=vx, color='#000000', alpha=0.04, linewidth=0.3, zorder=0)

    # ── Difficulty arrow annotation ──
    ax.annotate('Easy', xy=(0.02, -0.12), xycoords='axes fraction',
                fontsize=6.5, color=GRAY_ANN, style='italic')
    ax.annotate('Hard', xy=(0.90, -0.12), xycoords='axes fraction',
                fontsize=6.5, color=GRAY_ANN, style='italic')
    ax.annotate('', xy=(0.88, -0.09), xytext=(0.12, -0.09),
                xycoords='axes fraction',
                arrowprops=dict(arrowstyle='->', color=GRAY_ANN, lw=0.5))

    # ── lz* annotation box with shadow ──
    if is_contam:
        lz_color = ACAD_RED
        lz_text = f'$|\\Delta\\ell_z^*|$ = {delta_lz:.1f}  (detection signal)'
    else:
        lz_color = GREEN_LZ
        lz_text = f'$\\ell_z^*$ = {lz_c:+.1f}  (baseline)'
    draw_shadow_box(ax, 0.5, -0.24, lz_text, lz_color, ax.transAxes)

    # ── Axes styling ──
    ax.set_title(title, fontweight='bold', pad=8)
    ax.set_xlabel('Items (sorted by difficulty)', labelpad=10)
    ax.set_xlim(-2, N + 1)
    ax.set_ylim(-0.12, 1.12)
    ax.set_yticks([0, 1])
    ax.set_yticklabels(['0\n(Incorrect)', '1\n(Correct)'], fontsize=7.5)
    ax.set_xticks([])

    # Only left and bottom spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_linewidth(0.5)
    ax.spines['left'].set_linewidth(0.5)

    # ── Legend ──
    if is_contam:
        leg = ax.legend(loc='center', bbox_to_anchor=(0.38, 0.42),
                        framealpha=0.95, edgecolor='#cccccc',
                        borderpad=0.4, handletextpad=0.4, fontsize=7,
                        markerscale=0.9)
    else:
        leg = ax.legend(loc='upper right', framealpha=0.92, edgecolor='#cccccc',
                        borderpad=0.4, handletextpad=0.4, fontsize=7,
                        markerscale=0.9)
    leg.get_frame().set_linewidth(0.4)


# ── Render panels ──────────────────────────────────────────────────────────
np.random.seed(7)
plot_panel(axes[0], clean, '(a)  Clean Model', is_contam=False)
np.random.seed(7)
plot_panel(axes[1], contam, '(b)  Contaminated Model', is_contam=True)

axes[0].set_ylabel('Response', labelpad=4)

# ── Save ───────────────────────────────────────────────────────────────────
out = Path(__file__).resolve().parent
fig.savefig(out / 'fig_1_response_pattern.pdf', format='pdf')
fig.savefig(out / 'fig_1_response_pattern.png', format='png')
plt.close()
print("Done. Files saved.")

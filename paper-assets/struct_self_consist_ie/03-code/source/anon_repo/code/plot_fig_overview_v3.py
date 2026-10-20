import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import os

C_GREEN    = '#2E7D32';  C_GREEN_BG = '#E8F5E9';  C_GREEN_BD = '#66BB6A'
C_RED      = '#C62828';  C_RED_BG   = '#FFEBEE';  C_RED_BD   = '#EF5350'
C_BLUE     = '#1565C0';  C_BLUE_LT  = '#1E88E5';  C_BLUE_BG  = '#E3F2FD';  C_BLUE_BD = '#42A5F5'
C_GOLD     = '#E6A817';  C_GOLD_BG  = '#FFF8E1';  C_GOLD_BD  = '#FFD54F'
C_GRAY     = '#757575';  C_DARK     = '#212121';   C_ORANGE   = '#E65100'

fig = plt.figure(figsize=(6.5, 4.2))

lm = 0.018; rm = 0.018; gap_frac = 0.048
pw = (1.0 - lm - rm - 2*gap_frac) / 3.0
bt = 0.04; tp = 0.92; ph = tp - bt

ax1 = fig.add_axes([lm, bt, pw, ph])
ax2 = fig.add_axes([lm + pw + gap_frac, bt, pw, ph])
ax3 = fig.add_axes([lm + 2*(pw + gap_frac), bt, pw, ph])

for ax in [ax1, ax2, ax3]:
    ax.set_xlim(0, 10); ax.set_ylim(0, 12)
    ax.set_aspect('equal'); ax.axis('off')

def panel_bg(ax, bg, bd):
    ax.add_patch(FancyBboxPatch((0.05, 0.05), 9.9, 11.9, boxstyle="round,pad=0.12",
                                lw=1.3, ec=bd, fc=bg, zorder=0))

def tbox(ax, x, y, text, fc, ec, tc='white', fs=7, w=2.6, h=0.6, fw='bold', z=5):
    ax.add_patch(FancyBboxPatch((x-w/2, y-h/2), w, h, boxstyle="round,pad=0.08",
                                fc=fc, ec=ec, lw=0.8, zorder=z))
    ax.text(x, y, text, ha='center', va='center', fontsize=fs, fontweight=fw, color=tc, zorder=z+1)

def dbox(ax, x, y, w, h, ec='#555'):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.06",
                                lw=0.8, ec=ec, fc='white', ls='--', zorder=2))

# =====================================================================
# PANEL 1: Quality Estimation
# =====================================================================
ax = ax1
panel_bg(ax, C_GREEN_BG, C_GREEN_BD)

ax.text(5, 11.5, 'Quality Estimation', ha='center', va='center',
        fontsize=9, fontweight='bold', color=C_GREEN)
ax.text(5, 10.75, '(Predicting Reliability)', ha='center', va='center',
        fontsize=7, fontstyle='italic', color=C_GREEN)

tbox(ax, 1.5, 9.2, 'Input x', '#424242', '#424242', 'white', 7, 2.2, 0.55)
dbox(ax, 3.2, 8.35, 3.2, 1.65)
ax.text(4.8, 9.7, 'N samples', ha='center', va='center', fontsize=6, color=C_GRAY)
for yy in [9.3, 8.9, 8.5]:
    ax.plot([3.5, 6.1], [yy, yy], color='#BDBDBD', lw=2.5, solid_capstyle='round', zorder=3)
ax.annotate('', xy=(3.15, 9.2), xytext=(2.6, 9.2),
            arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=1.0))

tbox(ax, 8.3, 9.2, r'$S_J$ Score', C_GREEN, C_GREEN, 'white', 7, 2.5, 0.55)
ax.annotate('', xy=(6.95, 9.2), xytext=(6.5, 9.2),
            arrowprops=dict(arrowstyle='->', color=C_GREEN, lw=1.2))

tbox(ax, 2.5, 6.8, r'High $S_J$', C_GREEN, C_GREEN, 'white', 7, 2.4, 0.5)
tbox(ax, 7.5, 6.8, 'High F1 ✓', '#2E7D32', '#2E7D32', 'white', 7, 2.4, 0.5)
ax.annotate('', xy=(6.15, 6.8), xytext=(3.75, 6.8),
            arrowprops=dict(arrowstyle='->', color=C_GREEN, lw=1.0))

tbox(ax, 2.5, 5.3, r'Low $S_J$', C_ORANGE, C_ORANGE, 'white', 7, 2.4, 0.5)
tbox(ax, 7.5, 5.3, 'Low F1  ✓', C_ORANGE, C_ORANGE, 'white', 7, 2.4, 0.5)
ax.annotate('', xy=(6.15, 5.3), xytext=(3.75, 5.3),
            arrowprops=dict(arrowstyle='->', color=C_ORANGE, lw=1.0))

ax.text(5, 6.05, 'Monotonic correlation', ha='center', va='center', fontsize=5.5,
        fontstyle='italic', color=C_BLUE_LT)

ax.text(3.3, 3.0, r'AUROC $\approx$ 0.82', ha='center', va='center',
        fontsize=9, fontweight='bold', color=C_DARK)
ax.text(3.3, 2.1, r'$\rho \approx$ 0.39', ha='center', va='center',
        fontsize=8, color=C_DARK)
ax.text(8.0, 2.5, '✓', ha='center', va='center', fontsize=22,
        fontweight='bold', color=C_GREEN)

ax.text(5, 0.7, '✓ Effective Quality Estimation', ha='center', va='center',
        fontsize=7, fontweight='bold', color=C_GREEN,
        bbox=dict(boxstyle='round,pad=0.2', fc='white', ec=C_GREEN, lw=1.2))

# =====================================================================
# PANEL 2: Sample Selection
# =====================================================================
ax = ax2
panel_bg(ax, C_RED_BG, C_RED_BD)

ax.text(5, 11.5, 'Sample Selection', ha='center', va='center',
        fontsize=9, fontweight='bold', color=C_RED)
ax.text(5, 10.75, '(Choosing Best Output)', ha='center', va='center',
        fontsize=7, fontstyle='italic', color=C_RED)

tbox(ax, 1.5, 9.2, 'Input x', '#424242', '#424242', 'white', 7, 2.2, 0.55)
dbox(ax, 3.2, 8.1, 5.0, 2.0)
ax.text(5.7, 9.85, 'N samples from same input', ha='center', va='center',
        fontsize=5.5, color=C_GRAY)
for i, (yy, lab) in enumerate(zip([9.4, 8.9, 8.4], [r'$y_3$', r'$y_2$', r'$y_1$'])):
    ax.text(3.45, yy, lab, ha='left', va='center', fontsize=6.5, color=C_DARK)
    ax.plot([3.9, 6.2], [yy, yy], color='#BDBDBD', lw=2.5, solid_capstyle='round', zorder=3)
    ax.plot([6.4, 7.8], [yy, yy], color='#FFCDD2', lw=2.5, solid_capstyle='round', zorder=3)
ax.annotate('', xy=(3.15, 9.2), xytext=(2.6, 9.2),
            arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=1.0))

ax.plot([8.05, 8.05], [8.3, 9.5], color=C_RED, lw=1.3)
ax.plot([8.05, 8.3], [9.5, 9.5], color=C_RED, lw=1.3)
ax.plot([8.05, 8.3], [8.3, 8.3], color=C_RED, lw=1.3)
ax.text(9.15, 9.15, 'Same', ha='center', va='center', fontsize=7, fontweight='bold', color=C_RED)
ax.text(9.15, 8.65, 'score!', ha='center', va='center', fontsize=7, fontweight='bold', color=C_RED)
ax.text(9.15, 8.15, '(instance-level)', ha='center', va='center', fontsize=5, color=C_RED)

ax.add_patch(FancyBboxPatch((0.5, 5.0), 9.0, 2.6, boxstyle="round,pad=0.12",
                            fc='white', ec=C_RED_BD, lw=1.0, zorder=4))
ax.text(5, 7.05, 'Instance-level signal', ha='center', va='center',
        fontsize=8, fontweight='bold', color=C_DARK, zorder=10)
ax.text(5, 6.25, r'= same score for all $y_i$ given same $x$', ha='center', va='center',
        fontsize=7, color=C_DARK, zorder=10)
ax.text(5, 5.5, r'$\Rightarrow$ Cannot discriminate among samples', ha='center', va='center',
        fontsize=7, fontstyle='italic', color=C_RED, zorder=10)

ax.text(5, 3.5, r'best-of-N $\leq$ greedy', ha='center', va='center',
        fontsize=9, fontweight='bold', color=C_RED)
ax.text(8.5, 2.5, '✗', ha='center', va='center', fontsize=22,
        fontweight='bold', color=C_RED)

ax.text(5, 0.7, '✗ Selection Fails', ha='center', va='center',
        fontsize=7, fontweight='bold', color=C_RED,
        bbox=dict(boxstyle='round,pad=0.2', fc='white', ec=C_RED, lw=1.2))

# =====================================================================
# PANEL 3: Entity-Level Construction
# =====================================================================
ax = ax3
panel_bg(ax, C_BLUE_BG, C_BLUE_BD)

ax.text(5, 11.5, 'Entity-Level Construction', ha='center', va='center',
        fontsize=9, fontweight='bold', color=C_BLUE)
ax.text(5, 10.8, '(Building New Output)', ha='center', va='center',
        fontsize=7, fontstyle='italic', color=C_BLUE)

tbox(ax, 1.5, 9.9, 'Input x', '#424242', '#424242', 'white', 7, 2.2, 0.55)
# Moved dashed box down and made shorter to avoid subtitle overlap
dbox(ax, 3.2, 8.5, 5.6, 2.0)
ax.text(6.0, 10.3, 'N samples', ha='center', va='center', fontsize=6, color=C_GRAY)
ax.annotate('', xy=(3.15, 9.9), xytext=(2.6, 9.9),
            arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=1.0))

# Entity bars: 3 samples, with clear spacing
sy = [10.0, 9.5, 9.0]
for i, (yy, lab) in enumerate(zip(sy, [r'$y_1$', r'$y_2$', r'$y_3$'])):
    ax.text(3.45, yy, lab, ha='left', va='center', fontsize=6.5, color=C_DARK, zorder=5)
    # tokens before entity A
    ax.plot([3.85, 4.55], [yy, yy], color='#BDBDBD', lw=2, solid_capstyle='round', zorder=3)
    # Entity A (all 3 agree -> green)
    ax.plot([4.7, 5.7], [yy, yy], color='#66BB6A', lw=4, solid_capstyle='round', zorder=3)
    # gap tokens
    ax.plot([5.85, 6.3], [yy, yy], color='#BDBDBD', lw=2, solid_capstyle='round', zorder=3)

# Entity B: y1,y2 have it (green), y3 doesn't (gray)
for i, (yy, has) in enumerate(zip(sy, [True, True, False])):
    if has:
        ax.plot([6.45, 7.45], [yy, yy], color='#66BB6A', lw=4, solid_capstyle='round', zorder=3)
    else:
        ax.plot([6.45, 7.45], [yy, yy], color='#E0E0E0', lw=2, solid_capstyle='round', zorder=3)
    ax.plot([7.6, 8.5], [yy, yy], color='#BDBDBD', lw=2, solid_capstyle='round', zorder=3)

# Entity labels INSIDE the box, below the samples (well above bottom edge)
ax.text(5.2, 8.65, 'A: 3/3 ✓', ha='center', va='center', fontsize=6,
        fontweight='bold', color='#2E7D32', zorder=10,
        bbox=dict(boxstyle='round,pad=0.08', fc='white', ec='#A5D6A7', lw=0.5, alpha=0.9))
ax.text(6.95, 8.65, 'B: 2/3 ✓', ha='center', va='center', fontsize=6,
        fontweight='bold', color='#2E7D32', zorder=10,
        bbox=dict(boxstyle='round,pad=0.08', fc='white', ec='#A5D6A7', lw=0.5, alpha=0.9))

# Arrow down to vote box
ax.annotate('', xy=(5, 7.55), xytext=(5, 8.35),
            arrowprops=dict(arrowstyle='->', color=C_BLUE, lw=1.5))

# Majority vote box
ax.add_patch(FancyBboxPatch((0.8, 6.2), 8.4, 1.4, boxstyle="round,pad=0.1",
                            fc='white', ec=C_BLUE_BD, lw=1.2, zorder=4))
ax.text(5, 7.2, 'Entity-level majority vote', ha='center', va='center',
        fontsize=8, fontweight='bold', color=C_BLUE, zorder=10)
ax.text(5, 6.5, r'Keep entity if freq $\geq \theta$   ($\theta = 2/N$)', ha='center', va='center',
        fontsize=6.5, color=C_DARK, zorder=10)

# Arrow down
ax.annotate('', xy=(5, 5.0), xytext=(5, 6.05),
            arrowprops=dict(arrowstyle='->', color=C_BLUE, lw=1.5))

# Constructed output box
ax.add_patch(FancyBboxPatch((0.8, 4.15), 8.4, 0.9, boxstyle="round,pad=0.1",
                            fc='#BBDEFB', ec=C_BLUE, lw=1.0, zorder=4))
ax.text(5, 4.6, 'Constructs NEW output', ha='center', va='center',
        fontsize=7, fontweight='bold', color=C_BLUE, zorder=10)

# Key result
ax.text(5, 2.9, '+1.4 pp', ha='center', va='center',
        fontsize=10, fontweight='bold', color=C_BLUE)
ax.text(5, 2.1, '(Few-NERD, 4-seed)', ha='center', va='center',
        fontsize=7, color=C_DARK)
ax.text(8.5, 2.5, '✓', ha='center', va='center', fontsize=22,
        fontweight='bold', color=C_BLUE)

ax.text(5, 0.7, '✓ Construction Works', ha='center', va='center',
        fontsize=7, fontweight='bold', color=C_BLUE,
        bbox=dict(boxstyle='round,pad=0.2', fc='white', ec=C_BLUE, lw=1.2))

# ── Connectors ───────────────────────────────────────────────────────
gx = lm + pw + gap_frac/2
fig.text(gx, 0.52, 'Correlation\n-Selection\n    Gap', ha='center', va='center',
         fontsize=6.5, fontweight='bold', color=C_GOLD, linespacing=1.0,
         bbox=dict(boxstyle='round,pad=0.18', fc=C_GOLD_BG, ec=C_GOLD_BD, lw=1.2), zorder=20)

sx_pos = lm + 2*pw + gap_frac + gap_frac/2
fig.text(sx_pos, 0.52, 'Resolution', ha='center', va='center',
         fontsize=6.5, fontweight='bold', color=C_BLUE, zorder=20,
         bbox=dict(boxstyle='round,pad=0.18', fc='white', ec=C_BLUE_BD, lw=1.2))

for (x1, x2, c) in [
    (lm + pw + 0.002, gx - 0.022, C_GOLD),
    (gx + 0.022, lm + pw + gap_frac - 0.002, C_GOLD),
    (lm + 2*pw + gap_frac + 0.002, sx_pos - 0.022, C_BLUE_LT),
    (sx_pos + 0.022, lm + 2*(pw + gap_frac) - 0.002, C_BLUE_LT),
]:
    fig.patches.append(mpatches.FancyArrowPatch(
        (x1, 0.52), (x2, 0.52), arrowstyle='->', mutation_scale=8,
        color=c, lw=0.8, transform=fig.transFigure, figure=fig, zorder=19))

outdir = '/root/autodl-tmp/struct_self_consist_ie/output/figures'
os.makedirs(outdir, exist_ok=True)
fig.savefig(os.path.join(outdir, 'fig_overview.pdf'), bbox_inches='tight', dpi=600)
fig.savefig(os.path.join(outdir, 'fig_overview.png'), bbox_inches='tight', dpi=300)
plt.close()
print(f"Saved to {outdir}/fig_overview.pdf and .png")

"""Generate Figure 1: G-MFRM Framework Overview (conceptual diagram).
Full-width figure* for two-column layout.
Font sizes calibrated: printed at ~6.75" textwidth → scale ≈ 0.41x.
All text ≥17pt in figure → ≥7pt on paper."""
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# ── Colors ──────────────────────────────────────────────────────────
C_JUDGE   = '#2B6E99'
C_JUDGE_L = '#D6E8F2'
C_CONT    = '#D4762C'
C_CONT_L  = '#F8E0C8'
C_GRAY    = '#555555'
C_RED     = '#B03A2E'
C_GREEN   = '#1E8449'
C_GREEN_L = '#D5F5E3'
WHITE     = '#FFFFFF'
DARK      = '#2C3E50'
SHADOW    = '#999999'
BG_RED    = '#FDF2F0'
BG_GREEN  = '#F0FAF4'

SERIF = 'serif'
SANS  = 'DejaVu Sans'

# Font sizes — at 0.41x scale all ≥7pt on paper
FS_TITLE = 25
FS_SUB   = 18
FS_PATH  = 19
FS_BOX   = 18
FS_MATH  = 17
FS_SMALL = 17
FS_TINY  = 17
FS_SYM   = 20
FS_DESC  = 17
FS_PANEL = 23
FS_CHECK = 28
FS_NOTE  = 17
FS_CONF  = 17

# ── Figure setup ────────────────────────────────────────────────────
fig = plt.figure(figsize=(16, 7.5))
fig.patch.set_facecolor(WHITE)

gs = fig.add_gridspec(1, 2, width_ratios=[0.40, 0.60], wspace=0.035,
                      left=0.01, right=0.99, top=0.97, bottom=0.01)
ax_l = fig.add_subplot(gs[0])
ax_r = fig.add_subplot(gs[1])

for ax in [ax_l, ax_r]:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

# ── Helpers ─────────────────────────────────────────────────────────
def shadow_box(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0,
               zorder=2, pad=0.15):
    sh = FancyBboxPatch((x + 0.06, y - 0.06), w, h,
                         boxstyle=f'round,pad={pad}',
                         facecolor=SHADOW, edgecolor='none',
                         linewidth=0, alpha=0.12, zorder=zorder - 1)
    ax.add_patch(sh)
    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',
                        facecolor=fc, edgecolor=ec, linewidth=lw,
                        linestyle=ls, alpha=alpha, zorder=zorder)
    ax.add_patch(b)
    return b

def rbox(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):
    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',
                        facecolor=fc, edgecolor=ec, linewidth=lw,
                        linestyle=ls, alpha=alpha, zorder=zorder)
    ax.add_patch(b)
    return b

def label(ax, x, y, txt, fs=FS_BOX, fw='bold', color='black', ha='center',
          va='center', style='normal', zorder=5, family=SERIF, **kw):
    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,
                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)

def label_bg(ax, x, y, txt, fs=FS_CONF, fw='normal', color=C_RED, style='italic',
             zorder=6, family=SERIF):
    t = ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,
                ha='center', va='center', fontstyle=style, zorder=zorder, family=family)
    t.set_path_effects([pe.withStroke(linewidth=5, foreground=WHITE)])
    return t

def arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.3, style='-|>',
          rad=0, zorder=4, ls='-'):
    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'
    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,
                         linewidth=lw, connectionstyle=cs, linestyle=ls,
                         mutation_scale=13, zorder=zorder,
                         shrinkA=2, shrinkB=2)
    ax.add_patch(a)


# ═══════════════════════════════════════════════════════════════════
#  LEFT PANEL — Sequential Pipeline
# ═══════════════════════════════════════════════════════════════════

rbox(ax_l, 0.05, 0.1, 9.9, 9.8, BG_RED, C_RED, lw=2.0, alpha=0.12, zorder=0, pad=0.25)

label(ax_l, 5.0, 9.4, 'Sequential Pipeline', fs=FS_TITLE, fw='bold', color=C_RED)
label(ax_l, 5.0, 8.85, '(order-dependent estimation bias)', fs=FS_SUB, color=C_RED,
      style='italic', fw='normal')

# ── Path A: Bias-first ──
bw, bh = 3.0, 1.05
bx1, bx2 = 0.7, 5.9
by_a = 6.2

label(ax_l, 0.6, 8.25, 'Path A: Bias-first', fs=FS_PATH, fw='bold', color=DARK, ha='left')

shadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.3)
label(ax_l, bx1 + bw/2, by_a + bh/2 + 0.2, 'Step 1: MFRM', fs=FS_BOX, fw='bold', color=DARK)
label(ax_l, bx1 + bw/2, by_a + bh/2 - 0.2, r'calibrate $d_j$', fs=FS_MATH, fw='normal',
      color=C_JUDGE, style='italic')

shadow_box(ax_l, bx2, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.3)
label(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 + 0.2, 'Step 2: Adjust', fs=FS_BOX, fw='bold', color=DARK)
label(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 - 0.2, r'contamination $c_n$', fs=FS_MATH,
      fw='normal', color=C_CONT, style='italic')

# Arrow between steps
arrow(ax_l, bx1 + bw + 0.15, by_a + bh/2, bx2 - 0.15, by_a + bh/2, color=C_GRAY, lw=1.5)
label(ax_l, 9.55, by_a + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)

# Confounding arc A — above boxes, below path label
arc_y_a = by_a + bh + 0.15
a_conf = FancyArrowPatch((bx2 + 0.8, arc_y_a), (bx1 + 0.8, arc_y_a),
                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',
                          connectionstyle='arc3,rad=-0.3', mutation_scale=10, zorder=4)
ax_l.add_patch(a_conf)
label_bg(ax_l, 4.5, 7.85, 'confounding')

# ── Path B: Contamination-first ──
by_b = 3.15

label(ax_l, 0.6, 5.35, 'Path B: Contamination-first', fs=FS_PATH, fw='bold', color=DARK, ha='left')

shadow_box(ax_l, bx1, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.3)
label(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 + 0.2, 'Step 1: Adjust', fs=FS_BOX, fw='bold', color=DARK)
label(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 - 0.2, r'contamination $c_n$', fs=FS_MATH,
      fw='normal', color=C_CONT, style='italic')

shadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.3)
label(ax_l, bx2 + bw/2, by_b + bh/2 + 0.2, 'Step 2: MFRM', fs=FS_BOX, fw='bold', color=DARK)
label(ax_l, bx2 + bw/2, by_b + bh/2 - 0.2, r'calibrate $d_j$', fs=FS_MATH, fw='normal',
      color=C_JUDGE, style='italic')

arrow(ax_l, bx1 + bw + 0.35, by_b + bh/2, bx2 - 0.15, by_b + bh/2, color=C_GRAY, lw=1.5)
label(ax_l, 9.55, by_b + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)

# Confounding arc B
arc_y_b = by_b + bh + 0.15
b_conf = FancyArrowPatch((bx2 + 0.6, arc_y_b), (bx1 + 1.0, arc_y_b),
                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',
                          connectionstyle='arc3,rad=-0.3', mutation_scale=10, zorder=4)
ax_l.add_patch(b_conf)
label_bg(ax_l, 4.5, 4.85, 'confounding')

# ── Down arrows from paths to OVB ──
ovb_y, ovb_h = 0.35, 2.3
arrow(ax_l, 3.5, by_b, 3.5, ovb_y + ovb_h + 0.2, color=C_RED, lw=1.0, style='-|>')
arrow(ax_l, 6.5, by_b, 6.5, ovb_y + ovb_h + 0.2, color=C_RED, lw=1.0, style='-|>')

# ── OVB Box ──
rbox(ax_l, 0.5, ovb_y, 9.0, ovb_h, WHITE, C_RED, lw=2.0, ls='--', alpha=0.92, pad=0.2)

label(ax_l, 5.0, ovb_y + ovb_h - 0.4, 'Omitted Variable Bias (OVB)',
      fs=FS_PATH, fw='bold', color=C_RED)
label(ax_l, 5.0, ovb_y + ovb_h - 1.15,
      r'$\hat{\theta}$ biased when Cov$(d_j,\; c_n \cdot e_i) \neq 0$',
      fs=FS_MATH, fw='normal', color=C_RED)
label(ax_l, 5.0, ovb_y + ovb_h - 1.85, 'Unmodeled facet absorbed into estimates',
      fs=FS_NOTE, color=C_RED, style='italic', fw='normal')


# ═══════════════════════════════════════════════════════════════════
#  RIGHT PANEL — G-MFRM Joint Framework
# ═══════════════════════════════════════════════════════════════════

rbox(ax_r, 0.02, 0.1, 9.96, 9.8, BG_GREEN, C_GREEN, lw=2.0, alpha=0.08, zorder=0, pad=0.25)

label(ax_r, 5.0, 9.4, 'G-MFRM Joint Framework (Ours)', fs=FS_TITLE, fw='bold', color='#145A32')
label(ax_r, 5.0, 8.8, 'staged joint calibration of all facets', fs=FS_SUB,
      color=C_GREEN, style='italic', fw='normal')

# ── Stage 1: Standard MFRM (top, full width) ──
s1_x, s1_y, s1_w, s1_h = 0.3, 7.05, 9.4, 1.5
shadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.75, lw=1.4)

label(ax_r, 1.6, s1_y + s1_h - 0.4, 'Stage 1', fs=FS_BOX, fw='bold', color=C_JUDGE)
label(ax_r, 1.6, s1_y + s1_h - 0.88, 'Standard MFRM', fs=FS_SMALL, fw='normal', color=C_GRAY)

ow, oh = 1.5, 0.6
out1_specs = [(r'$\hat{\theta}^{(1)}$', 4.2),
              (r'$\hat{b}$', 6.1),
              (r'$\hat{d}$', 8.0)]
for lbl_txt, xo in out1_specs:
    rbox(ax_r, xo, s1_y + 0.28, ow, oh, WHITE, C_JUDGE, lw=1.0)
    label(ax_r, xo + ow/2, s1_y + 0.28 + oh/2, lbl_txt, fs=FS_SYM, fw='normal', color=C_JUDGE)

# ── Stage 2: Estimate e_i (left, below Stage 1) ──
s2_x, s2_y, s2_w, s2_h = 0.3, 3.2, 3.8, 3.5
shadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.7, lw=1.4)

label(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.42,
      r'Stage 2: Estimate $e_i$', fs=FS_BOX, fw='bold', color=C_CONT)

sub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']
sw, sh = 2.8, 0.62
for k, stxt in enumerate(sub_specs):
    sy = s2_y + s2_h - 1.2 - k * 0.82
    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.9)
    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=FS_SMALL, fw='normal', color=DARK)

# ── Stage 3: Joint Gated Model (right, below Stage 1) ──
s3_x, s3_y, s3_w, s3_h = 4.65, 3.2, 5.1, 3.5
shadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#FAFAFA', '#444444', lw=2.0)

label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.45,
      'Stage 3: Joint Gated Model', fs=FS_BOX, fw='bold', color=DARK)

label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 1.35,
      r'$\eta = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i$',
      fs=FS_MATH, fw='normal', color=C_GRAY)

# Thin separator
ax_r.plot([s3_x + 0.5, s3_x + s3_w - 0.5],
          [s3_y + s3_h - 1.85, s3_y + s3_h - 1.85],
          color='#CCCCCC', linewidth=0.6, zorder=3)

# Gating highlight
gx, gy, gw, gh = s3_x + 0.5, s3_y + 0.4, 4.1, 1.1
shadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=2.0, alpha=0.92)
label(ax_r, gx + gw/2, gy + gh/2,
      r'Gating: $c_n \cdot e_i$', fs=FS_PATH, fw='bold', color=C_CONT)

# Arrow S1 → S3 ("initialize")
arrow(ax_r, 7.2, s1_y, 7.2, s3_y + s3_h, color=C_JUDGE, lw=1.4)
label(ax_r, 7.75, (s1_y + s3_y + s3_h) / 2,
      'Warm-start', fs=FS_TINY, color=C_JUDGE, fw='normal', style='italic')

# Arrow S2 → S3 ("e_i")
s2_mid_y = s2_y + s2_h / 2
arrow(ax_r, s2_x + s2_w, s2_mid_y, s3_x, s2_mid_y, color=C_CONT, lw=1.4)
label(ax_r, (s2_x + s2_w + s3_x) / 2, s2_mid_y + 0.32,
      r'$\hat{e}_i$ fixed', fs=FS_TINY, color=C_CONT, fw='bold')

# ── 4-D Diagnostic Output ──
label(ax_r, 5.0, 2.6, 'Corrected Estimates', fs=FS_BOX, fw='bold', color=DARK)

ow2, oh2 = 2.15, 1.1
out_y = 1.1
out_specs = [
    (r'$\tilde{\theta}_n$', 'Fair Scores',     C_GREEN_L, C_GREEN,  0.4),
    (r'$\hat{c}_n$',        'Contamination',   C_CONT_L,  C_CONT,   2.75),
    (r'$\hat{d}_j$',        'Judge Severity',  C_JUDGE_L, C_JUDGE,  5.1),
    (r'$\hat{b}_i$',        'Difficulty',      C_JUDGE_L, C_JUDGE,  7.45),
]
for sym, desc, fc, ec, xo in out_specs:
    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.3)
    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.2, sym, fs=FS_SYM, fw='bold', color=ec)
    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.2, desc, fs=FS_DESC, fw='normal', color=DARK)

# Arrow S3 → outputs
arrow(ax_r, s3_x + s3_w/2, s3_y, s3_x + s3_w/2, 2.8, color='#444444', lw=1.5, style='-|>')

# Green check
label(ax_r, 5.0, 0.45, u'✓  Joint estimation resolves confounding',
      fs=FS_BOX, fw='bold', color=C_GREEN, style='italic', family=SANS)

# Panel labels
label(ax_l, 0.3, 9.8, '(a)', fs=FS_PANEL, fw='bold', color='black', ha='left')
label(ax_r, 0.2, 9.8, '(b)', fs=FS_PANEL, fw='bold', color='black', ha='left')

# ── Save ──
out_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'
fig.savefig(f'{out_dir}/fig1_framework_v2.png', bbox_inches='tight', dpi=300, facecolor=WHITE)
fig.savefig(f'{out_dir}/fig1_framework_v2.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)
plt.close()
print('Done: fig1_framework_v2.pdf + fig1_framework_v2.png')

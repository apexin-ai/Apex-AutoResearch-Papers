import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# ── Palette ──
CHARCOAL    = '#2C3E50'
TEXT_GRAY   = '#95A5A6'
TEXT_SUB    = '#7F8C8D'
ARROW_GRAY  = '#6C7A89'
BORDER_LIGHT= '#D5DBDB'
SHADOW_CLR  = '#00000022'

WHITE       = '#FFFFFF'
WARM_Y1     = '#FFF8E1'
WARM_Y1_B   = '#F9E79F'
WARM_O      = '#FFF3E0'
WARM_O_B    = '#F0B27A'
SAGE_FILL   = '#E8F5E9'
SAGE_BORDER = '#A9DFBF'
BLUE_FILL   = '#E3F2FD'
BLUE_BORDER = '#90CAF9'
GRAY_FILL   = '#F5F5F5'
GRAY_BORDER = '#BDBDBD'
CHECK_GREEN = '#27AE60'
PANEL_BG    = '#FAFBFC'

CELL_ENЕН   = '#DAEAF6'
CELL_ZHEN   = '#EDE7F6'
CELL_ENZH   = '#FCE4EC'
CELL_ZHZH   = '#E0F2F1'
CELL_BORDER = '#E0E0E0'

W, H = 16, 5.5
fig = plt.figure(figsize=(W, H), dpi=300)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(0.3, H)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor('white')

FONT = 'serif'
RS = 0.20

def txt(x, y, s, fs=9, fw='normal', c=CHARCOAL, ha='center', va='center',
        style='normal', zorder=5, ff=FONT):
    ax.text(x, y, s, ha=ha, va=va, fontsize=fs, fontweight=fw, color=c,
            fontstyle=style, fontfamily=ff, zorder=zorder)

def rounded_box(x, y, w, h, fill, border, lw=1.2, shadow=True, rs=RS, zorder=2):
    if shadow:
        sh = FancyBboxPatch((x + 0.03, y - 0.03), w, h,
            boxstyle=f"round,pad=0.0,rounding_size={rs}",
            facecolor=SHADOW_CLR, edgecolor='none', zorder=zorder - 0.5)
        ax.add_patch(sh)
    b = FancyBboxPatch((x, y), w, h,
        boxstyle=f"round,pad=0.0,rounding_size={rs}",
        facecolor=fill, edgecolor=border, linewidth=lw, zorder=zorder)
    ax.add_patch(b)

def arrow_down(x, y1, y2, color='#BDC3C7', lw=1.0, ms=10):
    ax.annotate('', xy=(x, y2), xytext=(x, y1),
        arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                        shrinkA=3, shrinkB=3, mutation_scale=ms))

# ── Panel regions ──
P_A = (0.25, 5.05)
P_B = (5.35, 10.95)
P_C = (11.15, 15.75)

for (x0, x1) in [P_A, P_B, P_C]:
    rounded_box(x0, 0.55, x1 - x0, 4.75, PANEL_BG, '#EAECEE', lw=0.8,
                shadow=False, rs=0.25, zorder=0)

# ── Panel titles ──
def panel_header(label, title, sec_ref, cx, label_x, title_y=5.10):
    txt(label_x, title_y, label, fs=12, fw='bold')
    txt(cx, title_y, title, fs=11, fw='bold')
    txt(cx, title_y - 0.28, sec_ref, fs=8, style='italic', c=TEXT_GRAY)

cx_a = (P_A[0] + P_A[1]) / 2
cx_b = (P_B[0] + P_B[1]) / 2
cx_c = (P_C[0] + P_C[1]) / 2

panel_header('(a)', 'Data Construction', '§3.2 Data', cx_a, P_A[0] + 0.12)
panel_header('(b)', 'Probing Framework', '§3.4–3.5 Probing', cx_b, P_B[0] + 0.12)
panel_header('(c)', 'Confound Exclusion', '§3.6 Controls', cx_c, P_C[0] + 0.12)

# ════════════════════ PANEL (a) ════════════════════
bw_a = P_A[1] - P_A[0] - 0.6
x_a = P_A[0] + 0.3
bh = 0.52
gap = 0.10

boxes_a = [
    ("ConflictQA Dataset",                           WHITE,   BORDER_LIGHT, 9,  'normal'),
    ("Parametric Knowledge\nVerification (per-model)", WARM_Y1, WARM_Y1_B,   8.5,'normal'),
    ("Translation (EN→ZH\nvia Qwen3-8B)",             WARM_O,  WARM_O_B,    8.5,'normal'),
    ("COMET Back-translation\nValidation",             WARM_Y1, WARM_Y1_B,   8.5,'normal'),
    ("EN / ZH Parallel\nConflict Data",                SAGE_FILL,SAGE_BORDER, 9,  'bold'),
]

y_top = 4.60
ya_pos = []
for i, (label, fill, border, fs, fw) in enumerate(boxes_a):
    bh_i = 0.48 if i == 0 else 0.55
    y = y_top - bh_i
    lw = 1.5 if i == 4 else 1.2
    rounded_box(x_a, y, bw_a, bh_i, fill, border, lw)
    txt(x_a + bw_a / 2, y + bh_i / 2, label, fs=fs, fw=fw)
    ya_pos.append((y, bh_i))
    y_top = y - gap

for i in range(len(boxes_a) - 1):
    arrow_down(x_a + bw_a / 2,
               ya_pos[i][0],
               ya_pos[i + 1][0] + ya_pos[i + 1][1])

# ════════════════════ PANEL (b) ════════════════════
bw_b = P_B[1] - P_B[0] - 0.6
x_b = P_B[0] + 0.3

y_res = 4.10; h_res = 0.52
rounded_box(x_b, y_res, bw_b, h_res, BLUE_FILL, BLUE_BORDER)
txt(x_b + bw_b / 2, y_res + h_res / 2 + 0.08, "Residual Stream Extraction", fs=9)
txt(x_b + bw_b / 2, y_res + h_res / 2 - 0.13, "(last-token, all L layers)", fs=7.5, style='italic', c=TEXT_SUB)

y_lp = 3.38; h_lp = 0.52
rounded_box(x_b, y_lp, bw_b, h_lp, BLUE_FILL, BLUE_BORDER)
txt(x_b + bw_b / 2, y_lp + h_lp / 2 + 0.08, "Linear Probe Training", fs=9)
txt(x_b + bw_b / 2, y_lp + h_lp / 2 - 0.13, "(per-layer logistic regression)", fs=7.5, style='italic', c=TEXT_SUB)

arrow_down(x_b + bw_b / 2, y_res, y_lp + h_lp)

proto_y = 3.10
txt(x_b + bw_b / 2, proto_y, '4-Direction Transfer Protocol', fs=9.5, fw='bold')
arrow_down(x_b + bw_b / 2, y_lp, proto_y + 0.10)

# 2×2 matrix
hdr_w = 0.85
cw = 1.35
ch = 0.42
mat_x = x_b + (bw_b - hdr_w - 2 * cw) / 2
mat_y = 1.95

txt(mat_x + hdr_w + cw * 0.5, mat_y + 2 * ch + 0.15, 'Train EN', fs=8.5, fw='bold')
txt(mat_x + hdr_w + cw * 1.5, mat_y + 2 * ch + 0.15, 'Train ZH', fs=8.5, fw='bold')
txt(mat_x + hdr_w / 2, mat_y + ch * 1.5, 'Test EN', fs=8.5, fw='bold')
txt(mat_x + hdr_w / 2, mat_y + ch * 0.5, 'Test ZH', fs=8.5, fw='bold')

cells = [
    (0, 1, 'EN→EN', CELL_ENЕН),
    (1, 1, 'ZH→EN', CELL_ZHEN),
    (0, 0, 'EN→ZH', CELL_ENZH),
    (1, 0, 'ZH→ZH', CELL_ZHZH),
]
for col, row, label, color in cells:
    cx = mat_x + hdr_w + col * cw
    cy = mat_y + row * ch
    rounded_box(cx, cy, cw, ch, color, CELL_BORDER, lw=0.8, shadow=False, rs=0.08)
    txt(cx + cw / 2, cy + ch / 2, label, fs=8.5)

arrow_down(x_b + bw_b / 2, mat_y, mat_y - 0.08)

y_boot = 1.28; h_boot = 0.45
bw_boot = bw_b - 1.0
rounded_box(x_b + 0.5, y_boot, bw_boot, h_boot, GRAY_FILL, GRAY_BORDER, lw=0.8)
txt(x_b + bw_b / 2, y_boot + h_boot / 2, "Bootstrap CI (n = 2,000)", fs=8.5)

arrow_down(x_b + bw_b / 2, mat_y - 0.08, y_boot + h_boot)

# ════════════════════ PANEL (c) ════════════════════
bw_c = P_C[1] - P_C[0] - 0.6
x_c = P_C[0] + 0.3

check_items = [
    ("COMET Tercile Ablation",     "Translation quality control"),
    ("Token Overlap Analysis",      "Surface feature exclusion"),
    ("XNLI Non-conflict Baseline",  "Task specificity verification"),
]

item_h = 0.72
item_gap = 0.28
y_c_top = 3.75

for i, (title, subtitle) in enumerate(check_items):
    y = y_c_top - i * (item_h + item_gap)
    rounded_box(x_c, y, bw_c, item_h, WHITE, BORDER_LIGHT, lw=1.0)
    txt(x_c + 0.42, y + item_h / 2, '✓', fs=18, fw='bold', c=CHECK_GREEN,
        ff='DejaVu Sans')
    txt(x_c + 0.85, y + item_h / 2 + 0.12, title, fs=9, fw='bold', ha='left')
    txt(x_c + 0.85, y + item_h / 2 - 0.14, subtitle, fs=7.5, style='italic',
        c=TEXT_GRAY, ha='left')

# ════════════════════ INTER-PANEL CURVED ARROWS ════════════════════
mid_a_y = ya_pos[2][0] + ya_pos[2][1] / 2
mid_b_y = (y_res + y_lp + h_lp) / 2

arrow_ab = FancyArrowPatch(
    (P_A[1] - 0.15, mid_a_y),
    (P_B[0] + 0.15, mid_b_y + 0.3),
    connectionstyle='arc3,rad=0.18',
    arrowstyle='-|>',
    color=ARROW_GRAY,
    lw=2.2,
    mutation_scale=18,
    zorder=4,
)
ax.add_patch(arrow_ab)

mid_c_y = y_c_top - (item_h + item_gap) + item_h / 2

arrow_bc = FancyArrowPatch(
    (P_B[1] - 0.15, mat_y + ch),
    (P_C[0] + 0.15, mid_c_y),
    connectionstyle='arc3,rad=0.15',
    arrowstyle='-|>',
    color=ARROW_GRAY,
    lw=2.2,
    mutation_scale=18,
    zorder=4,
)
ax.add_patch(arrow_bc)

# ── Save ──
out = 'figures/paper/fig1_pipeline_v3.png'
plt.savefig(out, dpi=300, bbox_inches='tight', pad_inches=0.08, facecolor='white')
plt.close()
print(f'Saved {out}')

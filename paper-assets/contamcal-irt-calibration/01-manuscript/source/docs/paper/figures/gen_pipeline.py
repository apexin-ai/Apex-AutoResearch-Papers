"""ContamCal pipeline — v5: optimized spacing, no overlap."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(3.4, 1.6))
ax.set_xlim(0, 100)
ax.set_ylim(0, 46)
ax.axis('off')

TXT, SUB = '#1A2530', '#5A6A7A'
BG  = ['#DBEEF8', '#D9F2E3', '#FDE8D0']
BD  = ['#5AAFE0', '#52C282', '#E8A050']

def rbox(x, y, w, h, bg, bd):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.6",
                 facecolor=bg, edgecolor=bd, linewidth=1.0, zorder=2))

def wbox(x, y, w, h, bd):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3",
                 facecolor='white', edgecolor=bd, linewidth=0.5, zorder=3))

def T(x, y, s, sz=5, **kw):
    d = dict(ha='center', va='center', fontsize=sz, color=TXT, zorder=4)
    d.update(kw)
    ax.text(x, y, s, **d)

def harrow(x1, x2, y):
    ax.annotate('', xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle='->', color='#555', lw=1.6,
                                shrinkA=1, shrinkB=1), zorder=5)

# Layout: 3 boxes with generous gaps
bw, bh, gap = 25, 40, 6
x1 = 2
x2 = x1 + bw + gap
x3 = x2 + bw + gap
by = 3

rbox(x1, by, bw, bh, BG[0], BD[0])
rbox(x2, by, bw, bh, BG[1], BD[1])
rbox(x3, by, bw, bh, BG[2], BD[2])

c1, c2, c3 = x1+bw/2, x2+bw/2, x3+bw/2

# ── Stage 1 ──
T(c1, 40, 'Stage 1', 5.5, fontweight='bold')
T(c1, 36.5, 'Injection', 5, fontweight='bold', color=BD[0])

T(c1, 31.5, 'Clean SFT (50K)', 4.5, fontweight='bold')
T(c1, 28.5, '+ Benchmark MCQ', 4.5)
T(c1, 25, '↓', 6, color='#aaa')

wbox(x1+2, 18, 21, 5, BD[0])
T(c1, 21, 'LoRA SFT', 5, fontweight='bold')
T(c1, 18.8, 'r=16, α=32', 3.8, color=SUB, fontfamily='monospace')

T(c1, 15.5, '↓', 6, color='#aaa')

# dosage pills in a row
doses = ['d0','d5','d25','d50','d100']
dw = 3.8
total_w = 5*dw + 4*0.4
dx = x1 + (bw - total_w)/2
for j, d in enumerate(doses):
    px = dx + j*(dw+0.4)
    wbox(px, 9.5, dw, 3, BD[0])
    T(px+dw/2, 11, d, 3.2, fontfamily='monospace')

T(c1, 6.5, '30 checkpoints', 4, color=SUB, fontstyle='italic')

# ── Stage 2 ──
T(c2, 40, 'Stage 2', 5.5, fontweight='bold')
T(c2, 36.5, 'Profiling', 5, fontweight='bold', color=BD[1])

T(c2, 31.5, 'Eval: MMLU', 4.5, fontweight='bold')
T(c2, 28.5, 'ARC · GSM8K', 4.5)
T(c2, 25, '↓', 6, color='#aaa')

wbox(x2+2, 18, 21, 5, BD[1])
T(c2, 21, 'Classification', 5, fontweight='bold')
T(c2, 18.8, '(Algorithm 1)', 3.8, color=SUB)

T(c2, 15.5, '↓', 6, color='#aaa')

# 4 patterns stacked 2×2
pats = [('Benefit↑','#27AE60'), ('Immune→','#2980B9'),
        ('Collapse↓','#C0392B'), ('V-recov.∨','#D68910')]
for j, (lbl, clr) in enumerate(pats):
    px = x2 + 2 + (j%2)*10.8
    py = 10 + (1 - j//2)*4
    ax.add_patch(FancyBboxPatch((px, py), 9.5, 3,
                 boxstyle="round,pad=0.2", facecolor=clr,
                 edgecolor='none', alpha=0.12, zorder=3))
    T(px+4.75, py+1.5, lbl, 4, color=clr, fontweight='bold')

# ── Stage 3 ──
T(c3, 40, 'Stage 3', 5.5, fontweight='bold')
T(c3, 36.5, 'Calibration', 5, fontweight='bold', color=BD[2])

T(c3, 31.5, 'RRF Fusion', 4.5, fontweight='bold')
T(c3, 28.5, 'S1·S2·S4 → eᵢⱼ', 3.8, color=SUB)
T(c3, 25, '↓', 6, color='#aaa')

wbox(x3+2, 18, 21, 5, BD[2])
T(c3, 21, '2PL+γ IRT', 5, fontweight='bold')
T(c3, 18.8, 'σ(a(θ−b)+γ·e)', 3.5, color=SUB, fontfamily='monospace')

T(c3, 15.5, '↓', 6, color='#aaa')

wbox(x3+2, 8, 21, 5, BD[2])
T(c3, 11.5, 'θ_clean', 4.8, fontweight='bold')
T(c3, 9, '+ γ_d diagnostics', 3.8, color=SUB)

# ── Inter-stage arrows ──
harrow(x1+bw+0.5, x2-0.5, 22)
harrow(x2+bw+0.5, x3-0.5, 22)

out = '/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures/fig_pipeline.pdf'
plt.savefig(out, dpi=300, bbox_inches='tight', pad_inches=0.02,
            facecolor='white', edgecolor='none')
plt.savefig(out.replace('.pdf', '.png'), dpi=300, bbox_inches='tight',
            pad_inches=0.02, facecolor='white', edgecolor='none')
print(f'Saved: {out}')
plt.close()

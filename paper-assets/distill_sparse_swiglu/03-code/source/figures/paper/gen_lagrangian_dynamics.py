"""Figure A.1: Lagrangian controller dynamics — two stacked panels (no dual y-axis)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.3,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'xtick.major.size': 3,
    'ytick.major.size': 3,
    'mathtext.fontset': 'cm',
})

COL_LAMBDA = '#4472C4'
COL_SPARSITY = '#E05A3A'

OUT = '/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/figures/paper'

raw = """1,0.406,0.50
10,0.406,0.01
20,0.406,0.01
30,0.402,0.01
40,0.402,0.01
50,0.398,0.01
60,0.391,0.01
70,0.383,0.01
80,0.375,0.01
90,0.363,0.01
100,0.344,0.01
110,0.328,0.01
120,0.309,0.01
130,0.289,0.01
140,0.266,0.32
150,0.254,327.68
160,0.324,163.84
170,0.320,0.16
180,0.305,0.08
190,0.293,0.08
200,0.277,0.32
210,0.266,327.68
220,0.312,2621.44
230,0.316,81.92
240,0.301,81.92
250,0.285,81.92
260,0.277,1310.72
270,0.305,5000.00
280,0.305,5000.00
290,0.293,5000.00
300,0.277,5000.00
310,0.309,5000.00
320,0.309,5000.00
330,0.293,5000.00
340,0.285,5000.00
350,0.312,5000.00
360,0.309,5000.00
370,0.293,5000.00
380,0.277,5000.00
390,0.316,5000.00
400,0.312,5000.00
410,0.301,5000.00
420,0.285,5000.00
430,0.301,5000.00
440,0.312,5000.00
450,0.309,5000.00
460,0.293,5000.00
470,0.293,5000.00
480,0.320,1250.00
490,0.305,625.00
500,0.293,625.00
510,0.281,625.00
520,0.285,2500.00
530,0.281,2500.00
540,0.328,2500.00
550,0.305,5000.00
560,0.320,9.77
570,0.316,2.44
580,0.312,2.44
590,0.305,2.44
600,0.301,2.44
610,0.297,2.44
620,0.297,2.44
630,0.289,2.44
640,0.289,2.44
650,0.281,2.44
660,0.281,2.44
670,0.277,9.77
680,0.281,1250.00
690,0.281,5000.00
700,0.293,5000.00
710,0.293,5000.00
720,0.289,5000.00
730,0.285,5000.00
740,0.285,5000.00
750,0.285,5000.00
760,0.281,5000.00
770,0.281,5000.00
780,0.285,5000.00
790,0.285,5000.00
800,0.289,5000.00
810,0.285,5000.00
820,0.285,5000.00
830,0.281,5000.00
840,0.281,5000.00
850,0.285,5000.00
860,0.285,5000.00
870,0.285,5000.00
880,0.285,5000.00
890,0.285,5000.00
900,0.285,5000.00
910,0.285,5000.00
920,0.289,5000.00
930,0.285,5000.00
940,0.285,5000.00
950,0.281,5000.00
960,0.277,5000.00
970,0.281,5000.00
980,0.281,5000.00
990,0.277,5000.00
1000,0.281,5000.00"""

steps, sparsities, lambdas = [], [], []
for line in raw.strip().split('\n'):
    s, sp, lam = line.split(',')
    steps.append(int(s))
    sparsities.append(float(sp))
    lambdas.append(float(lam))

steps = np.array(steps)
sparsities = np.array(sparsities)
lambdas = np.array(lambdas)
lambdas_plot = np.clip(lambdas, 1e-2, None)

fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(3.3, 3.2), sharex=True,
    gridspec_kw={'height_ratios': [1.1, 1], 'hspace': 0.12})

# --- Top panel: lambda ---
ax1.plot(steps, lambdas_plot, color=COL_LAMBDA, linewidth=1.2, zorder=3)
ax1.set_yscale('log')
ax1.set_ylim(5e-3, 1.5e4)
ax1.set_ylabel(r'$\lambda$ (penalty weight)')
ax1.yaxis.grid(True, color='#E0E0E0', linewidth=0.4, zorder=0)
ax1.set_axisbelow(True)
ax1.text(0.97, 0.08, '(a)', transform=ax1.transAxes,
         fontsize=10, fontweight='bold', va='bottom', ha='right')

ax1.axhline(y=5000, color=COL_LAMBDA, linestyle=':', linewidth=0.7, alpha=0.5)
ax1.text(1010, 5000, r'$\lambda_{\max}$', fontsize=7, color=COL_LAMBDA,
         alpha=0.7, va='center', ha='left')

# --- Bottom panel: sparsity ---
ax2.plot(steps, sparsities, color=COL_SPARSITY, linewidth=1.2, zorder=3)
ax2.axhline(y=0.3, color=COL_SPARSITY, linestyle='--', linewidth=0.8, alpha=0.6)
ax2.text(1010, 0.3, 'target', fontsize=7, color=COL_SPARSITY,
         alpha=0.7, va='center', ha='left')

ax2.set_ylim(0.22, 0.43)
ax2.set_ylabel('Actual sparsity')
ax2.set_xlabel('Training Step')
ax2.yaxis.grid(True, color='#E0E0E0', linewidth=0.4, zorder=0)
ax2.set_axisbelow(True)
ax2.set_xlim(0, 1050)
ax2.text(0.97, 0.92, '(b)', transform=ax2.transAxes,
         fontsize=10, fontweight='bold', va='top', ha='right')

fig.subplots_adjust(left=0.18, right=0.92, top=0.97, bottom=0.12)
fig.savefig(f'{OUT}/lagrangian_dynamics.pdf')
fig.savefig(f'{OUT}/lagrangian_dynamics.png')
print('Saved lagrangian_dynamics.pdf/.png')
plt.close()

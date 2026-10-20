import sys
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path

matplotlib.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif', 'DejaVu Serif'],
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7,
    'text.usetex': False,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.5,
    'ytick.major.width': 0.5,
    'xtick.major.size': 3,
    'ytick.major.size': 3,
})

PROJ = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJ / 'src'))
from power_theory import load_params, marginal_power

df = pd.read_csv(PROJ / 'artifacts' / 'extended_simulation' / 'two_sided_power.csv')

BENCHMARKS = {
    'mmlu':      {'label': 'MMLU (n=14,042)',      'color': '#2166ac', 'marker': 'o'},
    'hellaswag': {'label': 'HellaSwag (n=10,042)',  'color': '#1b7837', 'marker': '^'},
    'gsm8k':     {'label': 'GSM8K (n=1,319)',       'color': '#e08214', 'marker': 's'},
    'arc_c':     {'label': 'ARC-C (n=295)',         'color': '#b2182b', 'marker': 'D'},
    'humaneval': {'label': 'HumanEval (n=164)',     'color': '#7b3294', 'marker': 'v'},
}

THEORY_PCTS = [0, 3, 5, 10, 15, 25, 50, 60, 75, 90, 100]

print("Computing theoretical power curves (Gauss-Hermite, K=30)...")
theory = {}
for bm in BENCHMARKS:
    params = load_params(bm)
    a, b, c, d = params['a'], params['b'], params['c'], params['d']
    theory[bm] = {}
    for pct in THEORY_PCTS:
        r = marginal_power(pct / 100.0, a, b, c, d, nq=30)
        theory[bm][pct] = r['two_sided']
    print(f"  {bm}: done")

def r2(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - y_true.mean()) ** 2)
    return 1 - ss_res / max(ss_tot, 1e-30)

all_sim, all_th = [], []
for bm in BENCHMARKS:
    sub = df[df['benchmark'] == bm].sort_values('contamination_pct')
    for _, row in sub.iterrows():
        pct = int(row['contamination_pct'])
        if pct in theory[bm]:
            all_sim.append(row['two_sided_rate'])
            all_th.append(theory[bm][pct])
overall_r2 = r2(np.array(all_sim), np.array(all_th))
print(f"Overall theory R² = {overall_r2:.4f}")

fig, ax = plt.subplots(figsize=(3.5, 3.0))

for bm, style in BENCHMARKS.items():
    sub = df[df['benchmark'] == bm].sort_values('contamination_pct')
    ax.scatter(sub['contamination_pct'], sub['two_sided_rate'],
               color=style['color'], marker=style['marker'],
               s=16, edgecolors='white', linewidths=0.3,
               label=style['label'], zorder=5)

    th_x = np.array(sorted(theory[bm].keys()))
    th_y = np.array([theory[bm][p] for p in th_x])
    x_fine = np.linspace(0, 100, 200)
    y_fine = np.interp(x_fine, th_x, th_y)
    ax.plot(x_fine, y_fine, color=style['color'], linewidth=1.0,
            alpha=0.6, zorder=3)

ax.text(0.03, 0.92, f'Theory $R^2$={overall_r2:.3f}\n(markers: simulation,\n lines: theory)',
        transform=ax.transAxes, fontsize=6, color='#555555', va='top',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                  edgecolor='#cccccc', alpha=0.9, linewidth=0.4))

ax.axhline(y=0.80, color='#999999', linestyle=':', linewidth=0.8, zorder=2)
ax.text(101, 0.80, '80%', fontsize=6.5, color='#999999', va='center')

ax.axhline(y=0.05, color='#cccccc', linestyle=':', linewidth=0.6, zorder=1)
ax.text(101, 0.05, 'α', fontsize=6.5, color='#aaaaaa', va='center', style='italic')

ax.set_xlabel('Contamination Level (%)')
ax.set_ylabel('Two-Sided Detection Power')
ax.set_xlim(-2, 104)
ax.set_ylim(-0.02, 1.05)
ax.set_xticks([0, 10, 25, 50, 75, 100])
ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

leg = ax.legend(loc='center right', bbox_to_anchor=(0.98, 0.42),
                framealpha=0.95, edgecolor='#cccccc',
                borderpad=0.4, handletextpad=0.4, handlelength=1.8,
                labelspacing=0.35)
leg.get_frame().set_linewidth(0.4)

out = Path(__file__).resolve().parent
fig.savefig(out / 'fig_2_power_function.pdf', format='pdf')
fig.savefig(out / 'fig_2_power_function.png', format='png')
plt.close()
print("Done. Files saved.")

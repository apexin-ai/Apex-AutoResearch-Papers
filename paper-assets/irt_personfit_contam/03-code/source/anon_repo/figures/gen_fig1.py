import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from pathlib import Path
from scipy.ndimage import uniform_filter1d

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
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.5,
    'ytick.major.width': 0.5,
    'xtick.major.size': 3,
    'ytick.major.size': 3,
})

np.random.seed(42)

df = pd.read_csv(Path(__file__).resolve().parent.parent / 'params' / 'mmlu_params.csv')

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

BLUE = '#2166ac'
BLUE_PALE = '#d1e5f0'
RED_DARK = '#b2182b'
GRAY = '#888888'
CURVE_BLUE = '#4393c3'

fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.4), sharey=True)
fig.subplots_adjust(wspace=0.08)

x = np.arange(N)
JITTER = 0.03

def plot_panel(ax, responses, title, is_contam=False):
    p_smooth = uniform_filter1d(p, size=7, mode='nearest')
    ax.fill_between(x, 0, p_smooth, alpha=0.07, color=CURVE_BLUE, linewidth=0)
    ax.plot(x, p_smooth, color=CURVE_BLUE, linewidth=1.6, alpha=0.65,
            label='$P(X{=}1 \\mid \\theta)$', zorder=3)
    yj_1 = 1 + np.random.uniform(-JITTER, JITTER, N)
    yj_0 = 0 + np.random.uniform(-JITTER, JITTER, N)
    correct = responses == 1
    wrong = responses == 0
    if is_contam:
        norm_c = correct & ~memorized
        ax.scatter(x[norm_c], yj_1[norm_c],
                   s=10, color=BLUE, alpha=0.55, edgecolors='none', zorder=4)
        ax.scatter(x[wrong], yj_0[wrong],
                   s=7, color=BLUE_PALE, alpha=0.7, edgecolors=BLUE,
                   linewidths=0.3, zorder=4, marker='o')
        ax.scatter(x[memorized], yj_1[memorized],
                   s=42, color=RED_DARK, alpha=0.9, edgecolors='white',
                   linewidths=0.5, zorder=6, marker='^',
                   label='Memorized (seen)')
        for idx in flip_hard:
            ax.plot([x[idx], x[idx]], [p_smooth[idx], yj_1[idx]],
                    color=RED_DARK, alpha=0.3, linewidth=0.7,
                    linestyle='--', zorder=2)
    else:
        ax.scatter(x[correct], yj_1[correct],
                   s=10, color=BLUE, alpha=0.55, edgecolors='none', zorder=4)
        ax.scatter(x[wrong], yj_0[wrong],
                   s=7, color=BLUE_PALE, alpha=0.7, edgecolors=BLUE,
                   linewidths=0.3, zorder=4, marker='o')
    ax.annotate('Easy', xy=(0.02, -0.12), xycoords='axes fraction',
                fontsize=6.5, color=GRAY, style='italic')
    ax.annotate('Hard', xy=(0.90, -0.12), xycoords='axes fraction',
                fontsize=6.5, color=GRAY, style='italic')
    ax.annotate('', xy=(0.88, -0.09), xytext=(0.12, -0.09),
                xycoords='axes fraction',
                arrowprops=dict(arrowstyle='->', color=GRAY, lw=0.5))
    if is_contam:
        lz_color = RED_DARK
        lz_text = f'$|\\Delta\\ell_z^*|$ = {delta_lz:.1f}  (detection signal)'
    else:
        lz_color = '#2a7f2a'
        lz_text = f'$\\ell_z^*$ = {lz_c:+.1f}  (baseline)'
    ax.text(0.5, -0.24, lz_text, transform=ax.transAxes,
            ha='center', va='top', fontsize=8.5, fontweight='bold',
            color=lz_color,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor=lz_color, alpha=0.9, linewidth=0.6))
    ax.set_title(title, fontweight='bold', pad=8)
    ax.set_xlabel('Items (sorted by difficulty)', labelpad=10)
    ax.set_xlim(-2, N + 1)
    ax.set_ylim(-0.12, 1.12)
    ax.set_yticks([0, 1])
    ax.set_yticklabels(['0\n(Incorrect)', '1\n(Correct)'], fontsize=7.5)
    ax.set_xticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_linewidth(0.4)
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

np.random.seed(7)
plot_panel(axes[0], clean, '(a)  Clean Model', is_contam=False)
np.random.seed(7)
plot_panel(axes[1], contam, '(b)  Contaminated Model', is_contam=True)

axes[0].set_ylabel('Response', labelpad=4)

out = Path(__file__).resolve().parent
fig.savefig(out / 'fig_1_response_pattern.pdf', format='pdf')
fig.savefig(out / 'fig_1_response_pattern.png', format='png')
plt.close()
print("Done. Files saved to ./figures/")

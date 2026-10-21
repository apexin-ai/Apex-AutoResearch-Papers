import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import csv

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.5,
})

# --- Load data ---
steps, bs, alphas, esss = [], [], [], []
with open('/root/autodl-tmp/provenance_weight_training/artifacts/training_dynamics_contamination60_adaptive_seed456.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        steps.append(int(row['step']))
        bs.append(float(row['b']))
        alphas.append(float(row['alpha_eff']))
        esss.append(float(row['ess']))

steps = np.array(steps)
bs = np.array(bs)
alphas = np.array(alphas)
esss = np.array(esss)

C_BLUE = '#0072B2'
C_RED = '#D55E00'
C_GRAY = '#888888'

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(3.5, 4.8),
                                gridspec_kw={'height_ratios': [1, 1.3]})

# ============ Upper panel: b* histogram ============
b_clip = np.clip(bs, 0, 25)
bins = np.linspace(0, 25, 80)
ax1.hist(b_clip, bins=bins, color=C_BLUE, alpha=0.6, edgecolor='white', linewidth=0.3)

median_b = np.median(bs)
p99_b = np.percentile(bs, 99)

ax1.axvline(median_b, color=C_RED, linestyle='--', linewidth=1.2, zorder=3)
ax1.axvline(p99_b, color=C_GRAY, linestyle='--', linewidth=1.0, zorder=3)

ax1.set_xlabel('Importance weight $b^*$')
ax1.set_ylabel('Frequency')
ax1.set_title('(a) Distribution of importance weights $b^*$', fontsize=9, pad=4)
ax1.set_xlim(0, 25)

ymax = ax1.get_ylim()[1]
t1 = ax1.text(median_b + 0.4, ymax * 0.75, f'median={median_b:.2f}',
              fontsize=7.5, color=C_RED, va='bottom', ha='left')
t1.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

t2 = ax1.text(p99_b + 0.4, ymax * 0.55, f'p99={p99_b:.2f}',
              fontsize=7.5, color=C_GRAY, va='bottom', ha='left')
t2.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

skew_text = f'right-skewed\n(mean={np.mean(bs):.2f})'
ax1.text(0.97, 0.92, skew_text, transform=ax1.transAxes, fontsize=7,
         color='#555555', ha='right', va='top',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#cccccc', alpha=0.9))

# ============ Lower panel: alpha_eff and ESS over steps ============
def moving_average(x, w):
    cumsum = np.cumsum(np.insert(x, 0, 0))
    ma = (cumsum[w:] - cumsum[:-w]) / w
    pad_left = w // 2
    pad_right = len(x) - len(ma) - pad_left
    return np.concatenate([np.full(pad_left, ma[0]), ma, np.full(pad_right, ma[-1])])

w = 100
alpha_ma = moving_average(alphas, w)
ess_ma = moving_average(esss, w)

def rolling_quantile(x, w, q):
    from numpy.lib.stride_tricks import sliding_window_view
    if len(x) < w:
        return np.full_like(x, np.quantile(x, q))
    windows = sliding_window_view(x, w)
    vals = np.quantile(windows, q, axis=1)
    pad_left = w // 2
    pad_right = len(x) - len(vals) - pad_left
    return np.concatenate([np.full(pad_left, vals[0]), vals, np.full(pad_right, vals[-1])])

alpha_lo = rolling_quantile(alphas, w, 0.1)
alpha_hi = rolling_quantile(alphas, w, 0.9)
ess_lo = rolling_quantile(esss, w, 0.1)
ess_hi = rolling_quantile(esss, w, 0.9)

ax2.fill_between(steps, alpha_lo, alpha_hi, alpha=0.15, color=C_BLUE, linewidth=0)
ln1 = ax2.plot(steps, alpha_ma, color=C_BLUE, linewidth=1.5, label=r'$\alpha_{\mathrm{eff}}$ (MA-100)')
ax2.set_xlabel('Training step')
ax2.set_ylabel(r'$\alpha_{\mathrm{eff}}$', color=C_BLUE)
ax2.tick_params(axis='y', labelcolor=C_BLUE)

ax2.axhline(0.8, color=C_BLUE, linestyle=':', linewidth=0.9, alpha=0.6)
cap_frac = np.mean(alphas >= 0.8 - 1e-6) * 100
t_cap = ax2.text(len(steps) * 0.02, 0.815,
                 r'$\tau$=0.8 cap (' + f'{cap_frac:.1f}% batches)',
                 fontsize=7, color=C_BLUE, va='bottom')
t_cap.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

ax2.set_ylim(0.2, 0.95)

ax2r = ax2.twinx()
ax2r.spines['top'].set_visible(False)
ax2r.fill_between(steps, ess_lo, ess_hi, alpha=0.12, color=C_RED, linewidth=0)
ln2 = ax2r.plot(steps, ess_ma, color=C_RED, linewidth=1.5, label='ESS (MA-100)')
ax2r.set_ylabel('ESS', color=C_RED)
ax2r.tick_params(axis='y', labelcolor=C_RED)

ax2r.axhline(2.0, color=C_RED, linestyle=':', linewidth=0.9, alpha=0.6)
nmin_frac = np.mean(esss <= 2.0 + 0.05) * 100
t_nmin = ax2r.text(len(steps) * 0.55, 2.05,
                   r'$n_{\mathrm{min}}$=2 (' + f'{nmin_frac:.1f}% batches)',
                   fontsize=7, color=C_RED, va='bottom')
t_nmin.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

ax2r.set_ylim(1.8, 3.2)

lns = ln1 + ln2
labs = [l.get_label() for l in lns]
ax2.legend(lns, labs, loc='upper right', fontsize=7, framealpha=0.9)

ax2.set_title(r'(b) $\alpha_{\mathrm{eff}}$ and ESS over training', fontsize=9, pad=4)

plt.tight_layout(h_pad=1.0)
outbase = '/root/autodl-tmp/provenance_weight_training/artifacts/training_dynamics_figure'
plt.savefig(outbase + '.pdf', format='pdf')
plt.savefig(outbase + '.png', format='png')
plt.close()
print(f'Saved: {outbase}.pdf and {outbase}.png')

print(f'\n--- Stats ---')
print(f'b*: median={np.median(bs):.4f}, mean={np.mean(bs):.4f}, p99={np.percentile(bs, 99):.4f}, max={np.max(bs):.4f}')
print(f'alpha_eff: mean={np.mean(alphas):.4f}, frac>=0.8={np.mean(alphas >= 0.8-1e-6)*100:.1f}%')
print(f'ESS: mean={np.mean(esss):.4f}, frac<=2.05={np.mean(esss <= 2.05)*100:.1f}%')
print(f'Total steps: {len(steps)}')

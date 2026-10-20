import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import json

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

DATA = '/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/_project/data/training_dynamics_dose_response.json'
OUT_DIR = '/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/figures/paper'

with open(DATA) as f:
    data = json.load(f)

experiments = data['experiments']

COLORS = {
    'vanilla': '#999999',
    'taxei_50': '#D55E00',
    'random_10': '#56B4E9',
    'random_25': '#0072B2',
    'random_50': '#000080',
}
LABELS = {
    'vanilla': 'Vanilla',
    'taxei_50': 'TaxEI-50%',
    'random_10': 'Random-10%',
    'random_25': 'Random-25%',
    'random_50': 'Random-50%',
}
STYLES = {
    'vanilla': '-',
    'taxei_50': '-',
    'random_10': '-',
    'random_25': '-',
    'random_50': '-',
}

eval_data = {
    'vanilla':   {'loss': 0.294, 'eval': 61.7},
    'taxei_50':  {'loss': 0.259, 'eval': 51.1},
    'random_10': {'loss': 0.308, 'eval': 68.1},
    'random_25': {'loss': 0.286, 'eval': 55.3},
    'random_50': {'loss': 0.262, 'eval': 57.4},
}

ORDER = ['vanilla', 'random_10', 'random_25', 'random_50', 'taxei_50']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 2.8))

# Panel A: Training Loss Curves
for key in ORDER:
    entries = experiments[key]
    steps = np.array([e['step'] for e in entries])
    losses = np.array([e['loss'] for e in entries])
    window = 10
    smoothed = np.convolve(losses, np.ones(window)/window, mode='valid')
    steps_s = steps[window-1:]
    lw = 1.5 if key == 'taxei_50' else 1.0
    ax1.plot(steps_s, smoothed, color=COLORS[key], linestyle=STYLES[key],
             label=LABELS[key], linewidth=lw, alpha=0.9)

ax1.set_xlabel('Training Step')
ax1.set_ylabel('Training Loss')
ax1.set_title('(A) Training Loss Curves')

# Arrow annotation
taxei_entries = experiments['taxei_50']
taxei_steps = np.array([e['step'] for e in taxei_entries])
taxei_losses = np.array([e['loss'] for e in taxei_entries])
smoothed_taxei = np.convolve(taxei_losses, np.ones(10)/10, mode='valid')
steps_taxei_s = taxei_steps[9:]
min_idx = np.argmin(smoothed_taxei[-50:]) + len(smoothed_taxei) - 50
target_step = steps_taxei_s[min_idx]
target_loss = smoothed_taxei[min_idx]

ax1.annotate('More injection\n→ Lower loss',
             xy=(target_step, target_loss),
             xytext=(target_step - 500, target_loss + 0.35),
             fontsize=7, color='#D55E00',
             arrowprops=dict(arrowstyle='->', color='#D55E00', lw=1.0),
             ha='center')

ax1.legend(loc='upper right', frameon=False, ncol=1)

# Panel B: Training-Eval Paradox Scatter
sorted_keys = sorted(eval_data.keys(), key=lambda k: eval_data[k]['loss'])
xs = [eval_data[k]['loss'] for k in sorted_keys]
ys = [eval_data[k]['eval'] for k in sorted_keys]
ax2.plot(xs, ys, '--', color='#888888', linewidth=0.8, zorder=1)

for key in ORDER:
    d = eval_data[key]
    marker = 'D' if key == 'taxei_50' else 'o'
    size = 60 if key == 'taxei_50' else 45
    ax2.scatter(d['loss'], d['eval'], color=COLORS[key], s=size,
                marker=marker, zorder=3, edgecolors='white', linewidth=0.5)
    offset_x, offset_y = 0.003, 0.8
    ha = 'left'
    if key == 'random_50':
        offset_x = -0.003
        ha = 'right'
    if key == 'taxei_50':
        offset_y = -2.0
    ax2.annotate(LABELS[key], (d['loss'] + offset_x, d['eval'] + offset_y),
                 fontsize=7, color=COLORS[key], ha=ha, va='bottom')

ax2.set_xlabel('Final Training Loss')
ax2.set_ylabel('Clean Eval Accuracy (%)')
ax2.set_title('(B) Training–Eval Paradox')

ax2.annotate('Paradox: lower loss\n≠ better eval',
             xy=(0.27, 53), fontsize=7, fontstyle='italic', color='#555555',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF3E0', edgecolor='#D55E00', alpha=0.7))

plt.tight_layout(w_pad=2.5)
fig.savefig(f'{OUT_DIR}/fig_app_training_curves.pdf')
fig.savefig(f'{OUT_DIR}/fig_app_training_curves.png')
plt.close()
print('Done')

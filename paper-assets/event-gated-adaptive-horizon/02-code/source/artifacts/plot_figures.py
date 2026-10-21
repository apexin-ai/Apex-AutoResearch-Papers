import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import json
import os
import numpy as np

BASE = '/root/autodl-tmp/event-gated-adaptive-horizon'
LOGDIR = os.path.join(BASE, 'logdir')
FIGDIR = os.path.join(BASE, 'figures')

EXPERIMENTS = {
    'baseline':  ('baseline_s1',                          'Baseline (dt=1)',                    'black',   '-',  2.0),
    '008a':      ('exp_008a_fixed_dt2_no_subsample',      'dt=2, no subsample, dt_emb untrained', '#1f77b4', '-',  1.5),
    '008e_v3':   ('exp_008e_v3_subsample_on_dt1_h15',     'subsample ON, dt_emb untrained, H=15','#2ca02c', '-',  1.5),
    '008f':      ('exp_008f_no_dt_embed_subsample_on_h8', 'subsample ON, dt_emb=0, H=8',        '#9467bd', '-',  1.5),
    '008d':      ('exp_008d_subsample_on_h8',             'subsample ON, dt_emb trained, H=8',  '#d62728', '--', 1.5),
    '006':       ('fixed_dt2_v1_s1',                      'dt=2, subsample ON, dt_emb trained',  '#ff7f0e', '--', 1.5),
    '008c':      ('exp_008c_fixed_dt2_no_subsample_h8',   'no subsample, dt_emb untrained, H=8','#7f7f7f', '-',  1.2),
}

BASELINE_VE = {
    25000: 0.087, 35000: 0.241, 45000: 0.331, 55000: 0.404,
    65000: 0.563, 75000: 0.719, 85000: 0.701, 95000: 0.632, 105000: 0.656,
}

def load_metrics(logdir_name):
    path = os.path.join(LOGDIR, logdir_name, 'metrics.jsonl')
    eval_data = {}
    train_data = {}
    with open(path) as f:
        for line in f:
            row = json.loads(line)
            step = row['step']
            if 'eval_return' in row:
                eval_data[step] = row['eval_return']
            if 'value_mean' in row:
                train_data[step] = row['value_mean']
    return eval_data, train_data

def compute_ve(eval_data, train_data):
    ve = {}
    for step in sorted(eval_data.keys()):
        if step in train_data and eval_data[step] != 0:
            ve[step] = train_data[step] / eval_data[step]
    return ve

all_data = {}
for key, (logdir_name, label, color, ls, lw) in EXPERIMENTS.items():
    eval_d, train_d = load_metrics(logdir_name)
    ve = compute_ve(eval_d, train_d)
    all_data[key] = {'eval': eval_d, 'train': train_d, 've': ve,
                     'label': label, 'color': color, 'ls': ls, 'lw': lw}

# ── Figure 1: Learning Curves ──
fig, ax = plt.subplots(figsize=(8, 5))
for key in ['baseline', '008a', '008e_v3', '008f', '008d', '006', '008c']:
    d = all_data[key]
    steps = sorted(d['eval'].keys())
    vals = [d['eval'][s] for s in steps]
    ax.plot(np.array(steps)/1000, vals, label=d['label'],
            color=d['color'], linestyle=d['ls'], linewidth=d['lw'])

ax.axhline(y=950, color='black', linestyle=':', linewidth=1.0, alpha=0.6)
ax.annotate('baseline asymptote (~950)', xy=(350, 950), fontsize=9,
            color='black', alpha=0.7, va='bottom')

ax.set_xlabel('Training Step (×1K)', fontsize=12)
ax.set_ylabel('Eval Return', fontsize=12)
ax.set_title('Learning Curves: Eval Return vs Training Step', fontsize=14)
ax.tick_params(labelsize=10)
ax.legend(fontsize=8.5, loc='lower right', framealpha=0.9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(FIGDIR, 'fig1_learning_curves.pdf'), dpi=300, bbox_inches='tight')
fig.savefig(os.path.join(FIGDIR, 'fig1_learning_curves.png'), dpi=300, bbox_inches='tight')
plt.close(fig)
print('Figure 1 saved.')

# ── Figure 2: Normalized V/E Ratio ──
baseline_ve_steps = sorted(BASELINE_VE.keys())
baseline_ve_interp = {}
for key in all_data:
    if key == 'baseline':
        continue
    for step in sorted(all_data[key]['ve'].keys()):
        if step not in baseline_ve_interp and step >= baseline_ve_steps[0]:
            idx = np.searchsorted(baseline_ve_steps, step, side='right') - 1
            if idx < 0:
                continue
            if idx >= len(baseline_ve_steps) - 1:
                baseline_ve_interp[step] = BASELINE_VE[baseline_ve_steps[-1]]
            else:
                s0 = baseline_ve_steps[idx]
                s1 = baseline_ve_steps[idx + 1]
                t = (step - s0) / (s1 - s0)
                baseline_ve_interp[step] = BASELINE_VE[s0] * (1 - t) + BASELINE_VE[s1] * t

fig, ax = plt.subplots(figsize=(8, 5))

ax.axhspan(0, 0.7, color='#d6eaf8', alpha=0.3, label='Value suppression (<0.7×)')
ax.axhspan(0.8, 1.2, color='#e8e8e8', alpha=0.3, label='Normal range (0.8–1.2×)')
ax.axhspan(1.5, 5.0, color='#fadbd8', alpha=0.3, label='Pathological (>1.5×)')

ax.axhline(y=1.0, color='black', linestyle='-', linewidth=1.0, alpha=0.5)
ax.axhline(y=1.5, color='red', linestyle=':', linewidth=1.0, alpha=0.5)

for key in ['baseline', '008a', '008e_v3', '008f', '008d', '006', '008c']:
    d = all_data[key]
    if key == 'baseline':
        steps_plot = sorted(s for s in BASELINE_VE.keys())
        vals_plot = [1.0] * len(steps_plot)
    else:
        ve = d['ve']
        steps_plot = []
        vals_plot = []
        for step in sorted(ve.keys()):
            if step in baseline_ve_interp and baseline_ve_interp[step] != 0:
                steps_plot.append(step)
                vals_plot.append(ve[step] / baseline_ve_interp[step])

    if steps_plot:
        ax.plot(np.array(steps_plot)/1000, vals_plot, label=d['label'],
                color=d['color'], linestyle=d['ls'], linewidth=d['lw'])

ax.set_xlabel('Training Step (×1K)', fontsize=12)
ax.set_ylabel('Normalized V/E Ratio (experiment / baseline)', fontsize=12)
ax.set_title('Normalized Value-to-Eval Ratio Trajectories', fontsize=14)
ax.tick_params(labelsize=10)
ax.set_ylim(-0.5, 5.0)
ax.legend(fontsize=7.5, loc='upper left', framealpha=0.9, ncol=2)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(FIGDIR, 'fig2_normalized_ve.pdf'), dpi=300, bbox_inches='tight')
fig.savefig(os.path.join(FIGDIR, 'fig2_normalized_ve.png'), dpi=300, bbox_inches='tight')
plt.close(fig)
print('Figure 2 saved.')

# ── Figure 3: Value vs Eval Return Scatter ──
fig, ax = plt.subplots(figsize=(7, 7))

for key in ['baseline', '008a', '008e_v3', '008f', '008d', '006', '008c']:
    d = all_data[key]
    eval_d = d['eval']
    train_d = d['train']
    common_steps = sorted(set(eval_d.keys()) & set(train_d.keys()))
    if not common_steps:
        continue
    x = [eval_d[s] for s in common_steps]
    y = [train_d[s] for s in common_steps]
    ax.scatter(x, y, label=d['label'], color=d['color'], s=25, alpha=0.7,
               edgecolors='white', linewidth=0.3)

all_vals = []
for key in all_data:
    d = all_data[key]
    common = set(d['eval'].keys()) & set(d['train'].keys())
    all_vals.extend([d['eval'][s] for s in common])
    all_vals.extend([d['train'][s] for s in common])
if all_vals:
    lo = min(0, min(all_vals))
    hi = max(all_vals) * 1.05
    ax.plot([lo, hi], [lo, hi], 'k--', linewidth=1.0, alpha=0.5, label='Perfect calibration')
    ax.set_xlim(lo, hi)
    ax.set_ylim(lo, hi)

ax.set_xlabel('Eval Return', fontsize=12)
ax.set_ylabel('Value Mean (imagined)', fontsize=12)
ax.set_title('Value Calibration: Value Mean vs Eval Return', fontsize=14)
ax.tick_params(labelsize=10)
ax.legend(fontsize=8, loc='upper left', framealpha=0.9)
ax.set_aspect('equal', adjustable='box')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(FIGDIR, 'fig3_value_scatter.pdf'), dpi=300, bbox_inches='tight')
fig.savefig(os.path.join(FIGDIR, 'fig3_value_scatter.png'), dpi=300, bbox_inches='tight')
plt.close(fig)
print('Figure 3 saved.')
print('All figures generated.')

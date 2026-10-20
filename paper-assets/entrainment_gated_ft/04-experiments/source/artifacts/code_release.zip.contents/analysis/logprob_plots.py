import json
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT_DIR = '/root/entrainment_gated_ft/analysis'
DATA_DIR = '/root/entrainment_gated_ft/lm_eval_clean'

MODELS = {
    'GDN-pure': '1.3B-100B-GatedDeltaNet-pure.json',
    'GDN-h12-1': '1.3B-100B-GatedDeltaNet-hybrid-12-1.json',
    'HGRN2-pure': '1.3B-100B-HGRN2-pure.json',
    'HGRN2-h3-1': '1.3B-100B-HGRN2-hybrid-3-1.json',
}

model_data = {}
for name, fn in MODELS.items():
    fp = os.path.join(DATA_DIR, fn)
    d = json.load(open(fp))
    model_data[name] = sorted(d['samples']['lambada_openai'], key=lambda x: x['doc_id'])

n = len(model_data['GDN-pure'])
acc = {name: np.array([s['acc'] for s in samples]) for name, samples in model_data.items()}
logprob = {name: np.array([s['perplexity'] for s in samples]) for name, samples in model_data.items()}

contexts = []
for s in model_data['GDN-pure']:
    text = s['doc']['text']
    target = s['target'].strip()
    context = text[:text.rfind(target)] if target in text else text
    contexts.append(context)
context_lengths = np.array([len(c.split()) for c in contexts])

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('LAMBADA Per-Example Analysis: Attention Effect on Linear Models', fontsize=14, fontweight='bold')

# Plot 1: Attention effect confusion matrix style
ax = axes[0, 0]
pairs = [('GDN', 'GDN-pure', 'GDN-h12-1'), ('HGRN2', 'HGRN2-pure', 'HGRN2-h3-1')]
categories = ['Both\ncorrect', 'Attn\nhelped', 'Attn\nhurt', 'Both\nwrong']
x = np.arange(len(categories))
width = 0.35
colors_gdn = ['#2ecc71', '#3498db', '#e74c3c', '#95a5a6']
colors_hgrn = ['#27ae60', '#2980b9', '#c0392b', '#7f8c8d']

for i, (pair_name, pure, hybrid) in enumerate(pairs):
    both_c = ((acc[pure] == 1) & (acc[hybrid] == 1)).sum()
    helped = ((acc[pure] == 0) & (acc[hybrid] == 1)).sum()
    hurt = ((acc[pure] == 1) & (acc[hybrid] == 0)).sum()
    both_w = ((acc[pure] == 0) & (acc[hybrid] == 0)).sum()
    vals = [both_c, helped, hurt, both_w]
    bars = ax.bar(x + i*width - width/2, vals, width, label=pair_name,
                  color=[colors_gdn if i==0 else colors_hgrn][0], alpha=0.8)
    for bar, v in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 20,
                str(v), ha='center', va='bottom', fontsize=8)

ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_ylabel('Number of samples')
ax.set_title('Attention effect breakdown')
ax.legend()

# Plot 2: Logprob delta distribution
ax = axes[0, 1]
for pair_name, pure, hybrid in pairs:
    delta = logprob[hybrid] - logprob[pure]
    ax.hist(delta, bins=80, range=(-5, 5), alpha=0.5, label=f'{pair_name} (mean={delta.mean():.3f})', density=True)
ax.axvline(0, color='black', linestyle='--', alpha=0.5)
ax.set_xlabel('Logprob delta (hybrid - pure)')
ax.set_ylabel('Density')
ax.set_title('Distribution of logprob shifts')
ax.legend(fontsize=9)

# Plot 3: Accuracy by context length
ax = axes[1, 0]
bins = np.arange(0, 120, 10)
bin_centers = (bins[:-1] + bins[1:]) / 2

for name, color, ls in [('GDN-pure', '#e74c3c', '-'), ('GDN-h12-1', '#e74c3c', '--'),
                          ('HGRN2-pure', '#3498db', '-'), ('HGRN2-h3-1', '#3498db', '--')]:
    accs_binned = []
    for lo, hi in zip(bins[:-1], bins[1:]):
        mask = (context_lengths >= lo) & (context_lengths < hi)
        if mask.sum() > 10:
            accs_binned.append(acc[name][mask].mean())
        else:
            accs_binned.append(np.nan)
    ax.plot(bin_centers, accs_binned, color=color, linestyle=ls, marker='o', markersize=4, label=name)

ax.set_xlabel('Context length (words)')
ax.set_ylabel('Accuracy')
ax.set_title('Accuracy by context length')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Plot 4: Attention net effect by length bin
ax = axes[1, 1]
bins_coarse = [(0, 30), (30, 50), (50, 70), (70, 100), (100, 200)]
labels = ['0-30', '30-50', '50-70', '70-100', '100+']
x = np.arange(len(labels))

for i, (pair_name, pure, hybrid) in enumerate(pairs):
    nets = []
    for lo, hi in bins_coarse:
        mask = (context_lengths >= lo) & (context_lengths < hi)
        helped = ((acc[pure] == 0) & (acc[hybrid] == 1) & mask).sum()
        hurt = ((acc[pure] == 1) & (acc[hybrid] == 0) & mask).sum()
        total = mask.sum()
        nets.append((helped - hurt) / max(total, 1) * 100)
    ax.bar(x + i*width - width/2, nets, width, label=pair_name,
           color=['#e74c3c', '#3498db'][i], alpha=0.7)

ax.axhline(0, color='black', linestyle='-', alpha=0.3)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_xlabel('Context length (words)')
ax.set_ylabel('Net attention effect (%)')
ax.set_title('Net attention effect by context length')
ax.legend()
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, 'lambada_attention_analysis.png'), dpi=150, bbox_inches='tight')
print(f"Saved: {OUT_DIR}/lambada_attention_analysis.png")

# Plot 5: Cross-model scatter of logprob deltas
fig2, ax2 = plt.subplots(1, 1, figsize=(8, 8))
delta_gdn = logprob['GDN-h12-1'] - logprob['GDN-pure']
delta_hgrn = logprob['HGRN2-h3-1'] - logprob['HGRN2-pure']

ax2.scatter(delta_gdn, delta_hgrn, alpha=0.1, s=5, c='gray')

gdn_helped = (acc['GDN-pure'] == 0) & (acc['GDN-h12-1'] == 1)
gdn_hurt = (acc['GDN-pure'] == 1) & (acc['GDN-h12-1'] == 0)
hgrn_helped = (acc['HGRN2-pure'] == 0) & (acc['HGRN2-h3-1'] == 1)
hgrn_hurt = (acc['HGRN2-pure'] == 1) & (acc['HGRN2-h3-1'] == 0)

both_helped = gdn_helped & hgrn_helped
both_hurt = gdn_hurt & hgrn_hurt

ax2.scatter(delta_gdn[both_helped], delta_hgrn[both_helped], alpha=0.5, s=15, c='green', label=f'Both helped ({both_helped.sum()})')
ax2.scatter(delta_gdn[both_hurt], delta_hgrn[both_hurt], alpha=0.5, s=15, c='red', label=f'Both hurt ({both_hurt.sum()})')

ax2.axhline(0, color='black', linestyle='--', alpha=0.3)
ax2.axvline(0, color='black', linestyle='--', alpha=0.3)
ax2.set_xlabel('GDN logprob delta (h12 - pure)')
ax2.set_ylabel('HGRN2 logprob delta (h3 - pure)')
ax2.set_title('Cross-model logprob shift correlation')
ax2.legend()
corr = np.corrcoef(delta_gdn, delta_hgrn)[0, 1]
ax2.text(0.05, 0.95, f'Pearson r = {corr:.3f}', transform=ax2.transAxes, fontsize=12, va='top')
ax2.set_xlim(-8, 8)
ax2.set_ylim(-8, 8)
ax2.set_aspect('equal')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, 'lambada_crossmodel_scatter.png'), dpi=150, bbox_inches='tight')
print(f"Saved: {OUT_DIR}/lambada_crossmodel_scatter.png")

#!/usr/bin/env python3
"""Generate Layer-wise AUROC Emergence Curve (fig_layer_auroc)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import json

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
})

# === Qwen3-8B (exp-001): 36 layers, v2->v2.1 transfer per-layer AUROC ===
qwen_per_layer = {
    0: 0.536, 1: 0.5396, 2: 0.5316, 3: 0.5232, 4: 0.524,
    5: 0.52, 6: 0.5256, 7: 0.5444, 8: 0.5576, 9: 0.564,
    10: 0.5624, 11: 0.5716, 12: 0.586, 13: 0.578, 14: 0.6092,
    15: 0.6164, 16: 0.6408, 17: 0.6604, 18: 0.6868, 19: 0.7272,
    20: 0.7244, 21: 0.73, 22: 0.7268, 23: 0.7284, 24: 0.7392,
    25: 0.7372, 26: 0.7596, 27: 0.766, 28: 0.7592, 29: 0.7652,
    30: 0.7672, 31: 0.7692, 32: 0.7724, 33: 0.7704, 34: 0.7684,
    35: 0.772,
}

# === Llama-3-8B (exp-012): 5-fold CV mean per layer ===
# Only layers 16-31 were extracted (model only ran on these layers)
llama_per_layer = {
    16: 0.7793, 17: 0.7273, 18: 0.7220, 19: 0.7204, 20: 0.7313,
    21: 0.7270, 22: 0.7359, 23: 0.7350, 24: 0.7270, 25: 0.7372,
    26: 0.7374, 27: 0.7334, 28: 0.7321, 29: 0.7300, 30: 0.7348,
    31: 0.7470,
}

# === Build arrays ===
qwen_layers = np.array(sorted(qwen_per_layer.keys()))
qwen_auroc = np.array([qwen_per_layer[l] for l in qwen_layers])
qwen_depth = qwen_layers / 35 * 100

# Llama: physical layers 16-31 → normalized depth uses physical index / 31
llama_phys_layers = np.array(sorted(llama_per_layer.keys()))
llama_auroc = np.array([llama_per_layer[l] for l in llama_phys_layers])
llama_depth = llama_phys_layers / 31 * 100

# === Plot ===
fig, ax = plt.subplots(figsize=(6, 4))

# Emergence zone background
ax.axvspan(40, 62, alpha=0.07, color='#888888', zorder=0)

# Chance line
ax.axhline(y=0.5, color='gray', linestyle=':', linewidth=0.8, alpha=0.5, zorder=1)

# Qwen3-8B (full 36 layers)
ax.plot(qwen_depth, qwen_auroc, color='#0072B2', marker='o', markersize=3,
        markeredgewidth=0, label='Qwen3-8B (36 layers)', zorder=3)

# Llama-3-8B (measured layers 16-31 only)
ax.plot(llama_depth, llama_auroc, color='#D55E00', marker='s', markersize=3,
        markeredgewidth=0, linestyle='--',
        label='Llama-3-8B (L16–31)', zorder=3)

# Annotate Qwen peak: L19 is the inflection / CV-best layer
qwen_l19_depth = 19 / 35 * 100
qwen_l19_val = qwen_per_layer[19]
t1 = ax.annotate('L19', xy=(qwen_l19_depth, qwen_l19_val),
            xytext=(qwen_l19_depth - 18, qwen_l19_val + 0.035),
            fontsize=8, color='#0072B2', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#0072B2', lw=0.8))
t1.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# Annotate Llama peak: L16
llama_peak_depth = 16 / 31 * 100
llama_peak_val = llama_per_layer[16]
t2 = ax.annotate('L16', xy=(llama_peak_depth, llama_peak_val),
            xytext=(llama_peak_depth + 12, llama_peak_val + 0.02),
            fontsize=8, color='#D55E00', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#D55E00', lw=0.8))
t2.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# Emergence zone label — top-left corner of the band
ax.text(41, 0.815, 'emergence zone', ha='left', va='top', fontsize=7.5,
        color='#999999', fontstyle='italic')

ax.set_xlabel('Normalized Depth (%)')
ax.set_ylabel('AUROC')
ax.set_ylim(0.45, 0.82)
ax.set_xlim(-2, 104)
ax.legend(loc='center right', frameon=False,
          bbox_to_anchor=(1.0, 0.35))

plt.tight_layout()

outdir = '/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/figures'
plt.savefig(f'{outdir}/fig_layer_auroc.pdf')
plt.savefig(f'{outdir}/fig_layer_auroc.png')
print(f'Saved fig_layer_auroc.pdf and .png')

# Save data as JSON for reproducibility
data_out = {
    'qwen3_8b': {
        'source': 'v2->v2.1 transfer test (100 samples), best-position AUROC per layer',
        'num_layers': 36,
        'best_layer': 19,
        'per_layer_auroc': qwen_per_layer,
    },
    'llama3_8b': {
        'source': '5-fold CV mean AUROC per layer (layers 16-31 only; L0-15 not extracted)',
        'num_layers': 32,
        'best_layer': 16,
        'measured_layers': list(range(16, 32)),
        'per_layer_auroc': {int(k): v for k, v in llama_per_layer.items()},
    },
}
with open(f'{outdir}/fig_layer_auroc_data.json', 'w') as f:
    json.dump(data_out, f, indent=2)
print('Saved fig_layer_auroc_data.json')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch

NAVY = '#1B2838'
SLATE = '#3D5A80'
TEAL = '#5BA4B5'
CORAL = '#E07A5F'
EN_BLUE = '#4A90D9'
ZH_RED = '#E07A5F'
BG = '#FFFFFF'

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica'],
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.facecolor': BG,
    'axes.facecolor': BG,
    'axes.edgecolor': NAVY,
    'xtick.color': NAVY,
    'ytick.color': NAVY,
    'axes.labelcolor': NAVY,
    'text.color': NAVY,
})

# ─── DATA ───

# Steering p-values at alpha=+10 (Fisher exact test)
llama_steering = {
    12: 0.351771,
    13: 0.000337,
    14: 0.00224,
    16: 0.005085,
    18: 0.098394,
    28: 0.284122,
}

qwen_steering = {
    13: 0.247126,
    14: 1.0,
    15: 1.0,
}

gemma_steering = {
    16: 0.067119,
    17: 1.0,
    18: 0.723312,
}

# Effect sizes (steering_flip_rate - control_flip_rate) at alpha=+10
llama_effect = {
    12: 0.1891 - 0.1493,
    13: 0.2836 - 0.1343,
    14: 0.2786 - 0.1493,
    16: 0.1841 - 0.0846,
    18: 0.1294 - 0.0746,
    28: 0.0299 - 0.0100,
}

qwen_effect = {
    13: 0.0229 - 0.0,
    14: 0.0229 - 0.0153,
    15: 0.0229 - 0.0229,
}

gemma_effect = {
    16: 0.0058 - 0.0409,
    17: 0.0234 - 0.0175,
    18: 0.0292 - 0.0175,
}

# Per-layer probe balanced accuracy
llama_probe = [0.7799, 0.8198, 0.8599, 0.8699, 0.8549, 0.8473, 0.8474, 0.8549, 0.8449,
               0.8999, 0.8949, 0.9048, 0.9174, 0.8998, 0.9173, 0.9223, 0.9149, 0.8923,
               0.9073, 0.8898, 0.8898, 0.8847, 0.8973, 0.8874, 0.8648, 0.8423, 0.8498,
               0.8498, 0.8523, 0.8624, 0.8549, 0.8624]

qwen_probe = [0.5725, 0.645, 0.6336, 0.6298, 0.7061, 0.7023, 0.6603, 0.7061, 0.6908,
              0.6718, 0.6641, 0.7023, 0.687, 0.7176, 0.7099, 0.729, 0.7099, 0.7328,
              0.7137, 0.6985, 0.729, 0.729, 0.7481, 0.7366, 0.7176, 0.7061, 0.729,
              0.7061, 0.7214, 0.6908, 0.6908, 0.7214, 0.6718, 0.6947, 0.6832, 0.7023]

gemma_probe = [0.7836, 0.848, 0.8333, 0.8392, 0.8333, 0.848, 0.8684, 0.8977, 0.8713,
               0.8743, 0.8421, 0.8363, 0.8538, 0.883, 0.8626, 0.8655, 0.8801, 0.8889,
               0.8947, 0.886, 0.883, 0.8801, 0.883, 0.8772, 0.8655, 0.8772, 0.8918,
               0.883, 0.8655, 0.8567, 0.8538, 0.8538, 0.8304, 0.8216, 0.8246, 0.8099,
               0.7924, 0.7953, 0.7953, 0.7953, 0.8012, 0.7924]

bonferroni_llama = 0.05 / 6
bonferroni_qwen = 0.05 / 3
bonferroni_gemma = 0.05 / 3


# ═══════════════════════════════════════════════════
# FIGURE 5: Steering Results — Dot plot
# ═══════════════════════════════════════════════════

fig5, axes5 = plt.subplots(1, 3, figsize=(14, 4.2), dpi=300, sharey=True)
fig5.subplots_adjust(wspace=0.08, left=0.06, right=0.97, top=0.86, bottom=0.16)

models_steer = [
    ('Llama-3.1-8B', llama_steering, llama_effect, bonferroni_llama, 6),
    ('Qwen3-8B', qwen_steering, qwen_effect, bonferroni_qwen, 3),
    ('Gemma-2-9B', gemma_steering, gemma_effect, bonferroni_gemma, 3),
]

global_max_nlp = 0
for _, sp, _, _, _ in models_steer:
    for p in sp.values():
        nlp = -np.log10(max(p, 1e-10))
        if nlp > global_max_nlp:
            global_max_nlp = nlp

for idx, (name, steer_p, effect, bonf, n_tests) in enumerate(models_steer):
    ax = axes5[idx]
    layers = sorted(steer_p.keys())
    pvals = [steer_p[l] for l in layers]
    effects = [effect[l] for l in layers]
    neg_log_p = [-np.log10(max(p, 1e-10)) for p in pvals]

    # Use stricter Bonferroni for display (uniform across panels for visual clarity)
    threshold_line = -np.log10(bonf)

    # Threshold line
    ax.axhline(y=threshold_line, color=SLATE, linestyle='--', linewidth=0.8, alpha=0.5, zorder=1)

    # Place threshold label
    if idx == 2:
        ax.text(layers[-1] + 0.2, threshold_line + 0.06,
                f'Bonferroni\nthreshold',
                fontsize=8, color=SLATE, va='bottom', ha='right', linespacing=1.1)

    for i, (l, nlp, ef) in enumerate(zip(layers, neg_log_p, effects)):
        sig = nlp > threshold_line
        size = max(55, min(180, abs(ef) * 1100))
        if sig:
            ax.scatter(l, nlp, s=size, color=CORAL, edgecolors=NAVY,
                       linewidth=0.6, zorder=5, marker='o')
            # Add p-value label for significant points
            if steer_p[l] < 0.001:
                p_str = f'p < 0.001'
            else:
                p_str = f'p = {steer_p[l]:.3f}'
            ax.text(l, nlp + 0.12, p_str, fontsize=8, ha='center', va='bottom',
                    color=CORAL, fontweight='bold')
        else:
            ax.scatter(l, nlp, s=size, color='white', edgecolors=SLATE,
                       linewidth=1.2, zorder=5, marker='o')

    ax.set_xlabel('Layer', fontsize=10)

    # Better x-ticks: use actual layer numbers with spacing
    ax.set_xticks(layers)
    ax.set_xticklabels([f'{l}' for l in layers])

    # Add padding on x-axis
    x_range = max(layers) - min(layers)
    ax.set_xlim(min(layers) - x_range * 0.12, max(layers) + x_range * 0.12)

    if idx == 0:
        ax.set_ylabel('$-\\log_{10}(p)$  [Fisher exact test]', fontsize=10)

    ax.set_title(name, fontsize=11, fontweight='bold', pad=8)
    ax.tick_params(axis='both', which='both', length=3)

axes5[0].set_ylim(-0.15, global_max_nlp + 0.6)

legend_elements = [
    Line2D([0], [0], marker='o', color='none', markerfacecolor=CORAL,
           markeredgecolor=NAVY, markersize=8, label='Significant (after correction)'),
    Line2D([0], [0], marker='o', color='none', markerfacecolor='white',
           markeredgecolor=SLATE, markersize=8, label='Not significant'),
]
fig5.legend(handles=legend_elements, loc='upper center', ncol=2,
            fontsize=9, frameon=False, bbox_to_anchor=(0.5, 0.99))

for fmt in ['png', 'pdf']:
    fig5.savefig(f'/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/figures/paper/fig5_steering.{fmt}',
                 dpi=300, bbox_inches='tight', facecolor=BG)
plt.close(fig5)
print("Figure 5 saved.")


# ═══════════════════════════════════════════════════
# FIGURE 6: Detection-Decision Dissociation
# ═══════════════════════════════════════════════════

fig6, axes6 = plt.subplots(1, 3, figsize=(14, 4.5), dpi=300)
fig6.subplots_adjust(wspace=0.32, left=0.06, right=0.96, top=0.84, bottom=0.14)

models_dissoc = [
    ('Llama-3.1-8B', llama_probe, llama_steering, bonferroni_llama, 32),
    ('Qwen3-8B', qwen_probe, qwen_steering, bonferroni_qwen, 36),
    ('Gemma-2-9B', gemma_probe, gemma_steering, bonferroni_gemma, 42),
]

for idx, (name, probe, steer_p, bonf, n_layers) in enumerate(models_dissoc):
    ax = axes6[idx]
    layers_all = np.arange(n_layers)

    # Probe accuracy line
    ax.plot(layers_all, probe, color=TEAL, linewidth=1.6, zorder=3)
    ax.fill_between(layers_all, min(probe) - 0.05, probe, alpha=0.05, color=TEAL, zorder=1)

    # Detection peak marker
    peak_layer = int(np.argmax(probe))
    peak_val = max(probe)
    ax.scatter(peak_layer, peak_val, s=55, color=TEAL, edgecolors=NAVY,
               linewidth=0.6, zorder=6, marker='D')

    # Causal significance markers
    steer_layers = sorted(steer_p.keys())
    threshold = -np.log10(bonf)

    sig_layers = []
    nonsig_layers = []
    for sl in steer_layers:
        nlp = -np.log10(max(steer_p[sl], 1e-10))
        sig = nlp > threshold
        probe_val = probe[sl]
        if sig:
            ax.scatter(sl, probe_val, s=140, color=CORAL, edgecolors=NAVY,
                       linewidth=0.7, zorder=7, marker='*')
            sig_layers.append(sl)
        else:
            ax.scatter(sl, probe_val, s=28, facecolors=SLATE, edgecolors='none',
                       zorder=5, marker='x', alpha=0.6, linewidths=1.5)
            nonsig_layers.append(sl)

    # Panel-specific annotations
    if idx == 0:  # Llama: causal window overlaps with detection peak
        # Highlight the causal window
        ax.axvspan(12.3, 16.7, alpha=0.07, color=CORAL, zorder=0)

        ax.annotate('Causal window\n(L13–L16)',
                    xy=(14.5, min(probe[12:17]) - 0.003),
                    xytext=(22, 0.83),
                    fontsize=7.5, color=CORAL, fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color=CORAL, lw=0.8,
                                    connectionstyle='arc3,rad=-0.15'),
                    ha='center', va='top')

        ax.annotate(f'Peak L{peak_layer}',
                    xy=(peak_layer, peak_val),
                    xytext=(peak_layer + 6, peak_val + 0.02),
                    fontsize=7.5, color=TEAL, fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color=TEAL, lw=0.8),
                    ha='center', va='bottom')

    elif idx == 1:  # Qwen
        # Tested layers region
        for sl in nonsig_layers:
            pass
        ax.annotate(f'Peak L{peak_layer}\n(detection only)',
                    xy=(peak_layer, peak_val),
                    xytext=(peak_layer + 6, peak_val + 0.015),
                    fontsize=7.5, color=SLATE, fontstyle='italic',
                    arrowprops=dict(arrowstyle='->', color=SLATE, lw=0.6),
                    ha='center', va='bottom')

    elif idx == 2:  # Gemma
        ax.annotate(f'Peak L{peak_layer}\n(detection only)',
                    xy=(peak_layer, peak_val),
                    xytext=(peak_layer + 10, peak_val + 0.01),
                    fontsize=7.5, color=SLATE, fontstyle='italic',
                    arrowprops=dict(arrowstyle='->', color=SLATE, lw=0.6),
                    ha='center', va='bottom')

    ax.set_xlabel('Layer', fontsize=10)
    ax.set_xlim(-0.5, n_layers - 0.5)

    if idx == 0:
        ax.set_ylabel('Probe Balanced Accuracy', fontsize=10)

    ax.set_title(name, fontsize=11, fontweight='bold', pad=8)

    y_min = min(probe) - 0.025
    y_max = max(probe) + 0.045
    ax.set_ylim(y_min, y_max)

    ax.axhline(y=0.5, color=SLATE, linestyle=':', linewidth=0.5, alpha=0.3)
    ax.tick_params(axis='both', which='both', length=3)

    step = max(1, n_layers // 8)
    xticks = list(range(0, n_layers, step))
    if n_layers - 1 not in xticks:
        if n_layers - 1 - xticks[-1] >= step * 0.6:
            xticks.append(n_layers - 1)
        else:
            xticks[-1] = n_layers - 1
    ax.set_xticks(xticks)

legend_elements6 = [
    Line2D([0], [0], color=TEAL, linewidth=1.8, label='Probe balanced accuracy'),
    Line2D([0], [0], marker='D', color='none', markerfacecolor=TEAL,
           markeredgecolor=NAVY, markersize=6, label='Detection peak'),
    Line2D([0], [0], marker='*', color='none', markerfacecolor=CORAL,
           markeredgecolor=NAVY, markersize=11, label='Significant causal effect'),
    Line2D([0], [0], marker='x', color='none', markerfacecolor=SLATE,
           markeredgecolor=SLATE, markersize=7, label='No causal effect (tested)'),
]
fig6.legend(handles=legend_elements6, loc='upper center', ncol=4,
            fontsize=8, frameon=False, bbox_to_anchor=(0.5, 0.98))

for fmt in ['png', 'pdf']:
    fig6.savefig(f'/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/figures/paper/fig6_dissociation.{fmt}',
                 dpi=300, bbox_inches='tight', facecolor=BG)
plt.close(fig6)
print("Figure 6 saved.")

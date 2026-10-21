"""Generate Figure 3: Per-layer Δstable_rank vs Muon benefit scatter/regression."""
import json
import sys
sys.path.insert(0, '/root/spectral_optim_vision_geometry')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from plot_style import COLORS, apply_style
apply_style()

DATA_PATH = "/root/spectral_optim_vision_geometry/results/rho_investigation.json"
OUT_DIR = "/root/spectral_optim_vision_geometry/figures"

with open(DATA_PATH) as f:
    data = json.load(f)

def extract_arrays(arch_data):
    layers = arch_data["per_layer"]
    delta_sr = np.array([l["delta_sr"] for l in layers])
    drop = np.array([l["muon_drop_pp"] for l in layers])
    names = [l["layer"] for l in layers]
    return delta_sr, drop, names

resnet_data = data["spectral_response_ratio"]["resnet50"]
deit_data = data["spectral_response_ratio"]["deit_s"]

r_dsr, r_drop, r_names = extract_arrays(resnet_data)
d_dsr, d_drop, d_names = extract_arrays(deit_data)

fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.0))

def plot_panel(ax, x, y, names, title, color_main, rho_val, p_val):
    # Scatter with alpha=0.6 for dense regions
    ax.scatter(x, y, alpha=0.6, s=35, color=color_main, edgecolors='white',
               linewidths=0.4, zorder=3)

    # OLS regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    x_fit = np.linspace(x.min(), x.max(), 100)
    y_fit = slope * x_fit + intercept

    # Regression line: red dashed
    ax.plot(x_fit, y_fit, color='#CC3311', linestyle='--', linewidth=2,
            label=f'OLS fit', zorder=4)

    # 95% CI band (alpha=0.25)
    n = len(x)
    x_mean = x.mean()
    se = np.sqrt(np.sum((y - (slope * x + intercept))**2) / (n - 2))
    ci = stats.t.ppf(0.975, n - 2) * se * np.sqrt(1/n + (x_fit - x_mean)**2 / np.sum((x - x_mean)**2))
    ax.fill_between(x_fit, y_fit - ci, y_fit + ci, alpha=0.25, color='#CC3311',
                    linewidth=0, zorder=2)

    # Annotate outlier layers (top-3 by |y|)
    outlier_idx = np.argsort(np.abs(y))[-3:]
    for idx in outlier_idx:
        if np.abs(y[idx]) > np.percentile(np.abs(y), 90):
            short_name = names[idx].replace('layer', 'L').replace('block_', 'B')
            ax.annotate(short_name, (x[idx], y[idx]), fontsize=6,
                        xytext=(4, 4), textcoords='offset points',
                        color='#555555', style='italic')

    # Stats annotation
    ax.text(0.05, 0.95, f'$\\rho$ = {rho_val:+.3f}\n$p$ = {p_val:.4f}\n$n$ = {n}',
            transform=ax.transAxes, fontsize=8, va='top', ha='left',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8, edgecolor='#cccccc'))

    ax.set_title(title, fontsize=10, fontweight='bold', pad=6)
    ax.set_xlabel(r'$\Delta \mathrm{sr}_l$ (Muon $-$ AdamW)')
    ax.set_ylabel(r'$\Delta a_l$ (Muon benefit, pp)')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(alpha=0.2, linewidth=0.5)
    ax.axhline(0, color='#999999', linewidth=0.5, linestyle='-', zorder=1)
    ax.axvline(0, color='#999999', linewidth=0.5, linestyle='-', zorder=1)
    ax.legend(fontsize=8, loc='lower right', framealpha=0.9, edgecolor='none')

# Panel (a): ResNet-50 — positive correlation
plot_panel(axes[0], r_dsr, r_drop, r_names,
           '(a) ResNet-50', COLORS['Muon'],
           resnet_data["delta_stable_rank"]["rho"],
           resnet_data["delta_stable_rank"]["p"])

# Panel (b): DeiT-S — negative correlation (sign reversal)
plot_panel(axes[1], d_dsr, d_drop, d_names,
           '(b) DeiT-S', COLORS['AdamW'],
           deit_data["delta_stable_rank"]["rho"],
           deit_data["delta_stable_rank"]["p"])

plt.tight_layout(w_pad=2.0)
fig.savefig(f'{OUT_DIR}/fig3_sign_reversal.pdf')
fig.savefig(f'{OUT_DIR}/fig3_sign_reversal.png')
plt.close(fig)
print(f'Figure 3 saved to {OUT_DIR}/fig3_sign_reversal.{{pdf,png}}')

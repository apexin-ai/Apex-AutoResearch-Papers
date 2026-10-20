"""Dose-response curve: L1 instruction-routing head ablation vs action divergence."""
# --- Path configuration (set env vars to override defaults) ---
import os as _os
PROJECT_ROOT = _os.environ.get("VLA_SSD_ROOT", ".")
LIBERO_ROOT = _os.environ.get("LIBERO_ROOT", "./LIBERO")
# ---
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

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
})

# =============================================================================
# DATA — fill in after experiments complete
# =============================================================================

# Dose-response: ablating top-k instruction-routing heads (sorted by instruction selectivity)
# x = number of heads ablated, y = Cohen's d (paired action MSE vs intact)
dose_n_heads = np.array([4, 8, 12, 16, 20, 24, 28, 32])

# TODO: fill with actual Cohen's d values from dose-response experiments
dose_cohen_d = np.array([np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])

# TODO: fill with 95% CI half-widths (bootstrap)
dose_ci = np.array([np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])

# Reference points (already measured)
ref_instruction_n = 24
ref_instruction_d = 0.651  # 24 instruction-selective heads ablated
ref_instruction_label = "Instruction heads (24h): d = 0.65"

ref_control_n = 8
ref_control_d = 0.41  # 8 NON-instruction heads ablated (control)
ref_control_label = "Control heads (8h): d = 0.41"

# =============================================================================
# PLOT
# =============================================================================

fig, ax = plt.subplots(figsize=(3.25, 2.6))

TAB10 = plt.cm.tab10.colors
C_MAIN = TAB10[0]       # blue — dose-response curve
C_REF_INST = TAB10[2]   # green — instruction reference
C_REF_CTRL = TAB10[3]   # red — control reference
C_FILL = (*C_MAIN, 0.15)

# Main dose-response curve (only plot non-NaN points)
valid = ~np.isnan(dose_cohen_d)
if valid.any():
    ax.plot(dose_n_heads[valid], dose_cohen_d[valid],
            '-o', color=C_MAIN, markersize=5, linewidth=1.5, zorder=3,
            label='Instruction heads (sorted)')
    if not np.all(np.isnan(dose_ci)):
        v = valid & ~np.isnan(dose_ci)
        ax.fill_between(dose_n_heads[v],
                        dose_cohen_d[v] - dose_ci[v],
                        dose_cohen_d[v] + dose_ci[v],
                        color=C_FILL, edgecolor='none', zorder=2)

# Reference: instruction heads (24h)
ax.plot(ref_instruction_n, ref_instruction_d, 's', color=C_REF_INST,
        markersize=7, zorder=4, markeredgecolor='white', markeredgewidth=0.6)
ax.annotate(ref_instruction_label,
            xy=(ref_instruction_n, ref_instruction_d),
            xytext=(-8, 10), textcoords='offset points',
            fontsize=8, color=C_REF_INST, ha='right',
            arrowprops=dict(arrowstyle='-', color=C_REF_INST, lw=0.6))

# Reference: control heads (8h) — horizontal dashed line + marker
ax.axhline(ref_control_d, color=C_REF_CTRL, linestyle='--', linewidth=0.8,
           alpha=0.7, zorder=1)
ax.plot(ref_control_n, ref_control_d, 'D', color=C_REF_CTRL,
        markersize=6, zorder=4, markeredgecolor='white', markeredgewidth=0.6)
ax.annotate(ref_control_label,
            xy=(ref_control_n, ref_control_d),
            xytext=(8, -12), textcoords='offset points',
            fontsize=8, color=C_REF_CTRL, ha='left',
            arrowprops=dict(arrowstyle='-', color=C_REF_CTRL, lw=0.6))

# Axes
ax.set_xlabel('Number of heads ablated')
ax.set_ylabel("Cohen's d (action MSE)")
ax.set_xticks(dose_n_heads)
ax.set_xlim(2, 34)
y_max = max(ref_instruction_d, ref_control_d, np.nanmax(dose_cohen_d) if valid.any() else 0)
ax.set_ylim(0, y_max * 1.35)

ax.tick_params(direction='out', length=3)

plt.tight_layout()

out_dir = f"{PROJECT_ROOT}/results"
os.makedirs(out_dir, exist_ok=True)
fig.savefig(f'{out_dir}/fig_dose_response_draft.pdf')
fig.savefig(f'{out_dir}/fig_dose_response_draft.png')
print(f"Saved to {out_dir}/fig_dose_response_draft.pdf and .png")

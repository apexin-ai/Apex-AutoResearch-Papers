import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import json

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'serif'],
    'mathtext.fontset': 'stix',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
})

base = '/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/analysis'

with open(f'{base}/nve_trajectories_for_figure.json') as f:
    data = json.load(f)

with open(f'{base}/seed3_detector_retrospective.json') as f:
    seed3_data = json.load(f)

baseline_ve = data['baseline_walker']['ve_ratios']

# Compute seed 3 NVE
seed3_steps = [entry['step'] for entry in seed3_data['ve_ratio_timeline']]
seed3_ve = [entry['ve_ratio'] for entry in seed3_data['ve_ratio_timeline']]
seed3_nve = []
for step, ve in zip(seed3_steps, seed3_ve):
    bve = baseline_ve[str(step)]
    if bve < 1e-6:
        seed3_nve.append(None)
    else:
        seed3_nve.append(ve / bve)

# Extract other experiments
def get_exp(exp_id):
    for exp in data['experiments']:
        if exp['exp_id'].startswith(exp_id):
            return exp
    return None

seed0 = get_exp('exp_008d_subsample')
seed2 = get_exp('exp_009b')
no_dt_s1 = get_exp('exp_008f')

# Steps in thousands
steps_k = np.array(seed0['steps']) / 1000

# NVE arrays (skip first point which is null)
seed0_nve = seed0['nve']
seed2_nve = seed2['nve']
nodt_nve = no_dt_s1['nve']

# Replace None with NaN for plotting
def to_array(nve_list):
    return np.array([np.nan if v is None else v for v in nve_list])

seed0_arr = to_array(seed0_nve)
seed2_arr = to_array(seed2_nve)
seed3_arr = to_array(seed3_nve)
nodt_arr = to_array(nodt_nve)
steps_k_arr = np.array(seed3_steps) / 1000

# Colors (Okabe-Ito)
c_seed0 = '#D55E00'
c_seed2 = '#0072B2'
c_seed3 = '#E69F00'
c_nodt = '#999999'
c_thresh = '#000000'

fig, ax = plt.subplots(figsize=(5.5, 3.5))
fig.subplots_adjust(left=0.12, right=0.95, top=0.95, bottom=0.14)

# Plot lines
ax.plot(steps_k, seed0_arr, '-', color=c_seed0, label='Seed 0 (early collapse)')
ax.plot(steps_k, seed2_arr, '--', color=c_seed2, label='Seed 2 (self-correction)')
ax.plot(steps_k_arr, seed3_arr, '-.', color=c_seed3, label='Seed 3 (late-onset collapse)')
ax.plot(steps_k, nodt_arr, '-', color=c_nodt, linewidth=1.2, label='No dt-emb (control)')

# Old threshold reference line (1.5×) — faint gray
ax.axhline(y=1.5, color='#CCCCCC', linestyle='--', linewidth=0.7, alpha=0.6)
ax.text(111, 1.5, r'$\tau_{\mathrm{old}}=1.5\times$', fontsize=7, color='#AAAAAA',
        va='center', ha='left', style='italic')

# Main threshold line (2.0×)
ax.axhline(y=2.0, color='#D62728', linestyle='--', linewidth=1.2, label=r'Diagnostic threshold ($\tau=2.0\times$)')

# Diagnostic window onset
ax.axvline(x=35, color='#CCCCCC', linestyle=':', linewidth=0.9, label='Diagnostic window onset')

# CIVO onset markers (diamond at first NVE >= 2.0)
def first_crossing(steps_arr, nve_arr, threshold=2.0):
    for s, v in zip(steps_arr, nve_arr):
        if not np.isnan(v) and v >= threshold:
            return s, v
    return None, None

s0_step, s0_val = first_crossing(steps_k, seed0_arr, 2.0)
if s0_step is not None:
    ax.plot(s0_step, s0_val, 'D', color=c_seed0, markersize=7, zorder=5)

s2_step, s2_val = first_crossing(steps_k, seed2_arr, 2.0)
if s2_step is not None:
    ax.plot(s2_step, s2_val, 'D', color=c_seed2, markersize=7, zorder=5)

s3_step, s3_val = first_crossing(steps_k_arr, seed3_arr, 2.0)
if s3_step is not None:
    ax.plot(s3_step, s3_val, 'D', color=c_seed3, markersize=7, zorder=5)

ax.set_xlabel(r'Training Steps ($\times 10^3$)')
ax.set_ylabel('Normalized Value Excess (NVE)')
ax.set_xlim(0, 110)
ax.set_ylim(0, 4.5)
ax.set_xticks(np.arange(0, 115, 15))

ax.legend(loc='upper left', framealpha=0.9, edgecolor='none')

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures'
plt.rcParams['savefig.bbox'] = None
fig.savefig(f'{out_dir}/fig1_nve_trajectory.pdf')
fig.savefig(f'{out_dir}/fig1_nve_trajectory.png')
plt.close()

print("Done. Verifying thresholds (τ=2.0×):")
print(f"  Seed 0 max NVE: {np.nanmax(seed0_arr):.3f} (>2.0: {np.nanmax(seed0_arr) > 2.0})")
print(f"  Seed 2 max NVE: {np.nanmax(seed2_arr):.3f} (>2.0: {np.nanmax(seed2_arr) > 2.0})")
print(f"  Seed 3 max NVE: {np.nanmax(seed3_arr):.3f} (>2.0: {np.nanmax(seed3_arr) > 2.0})")
print(f"  No-dt-emb max NVE: {np.nanmax(nodt_arr):.3f} (<2.0: {np.nanmax(nodt_arr) < 2.0})")
print(f"\nCIVO onset (first crossing τ=2.0):")
print(f"  Seed 0: step={s0_step}, NVE={s0_val}")
print(f"  Seed 2: step={s2_step}, NVE={s2_val}")
print(f"  Seed 3: step={s3_step}, NVE={s3_val}")

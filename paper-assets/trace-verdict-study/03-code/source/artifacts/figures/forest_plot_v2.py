import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from matplotlib.lines import Line2D

def wilson_ci(p, n, z=1.96):
    denom = 1 + z**2 / n
    center = (p + z**2 / (2*n)) / denom
    margin = z * np.sqrt(p*(1-p)/n + z**2/(4*n**2)) / denom
    return (center - margin) * 100, (center + margin) * 100

n, z = 1190, 1.96
models = ['Qwen2.5-7B', 'DS-Coder-7B', 'CodeLlama-13B', 'Qwen2.5-1.5B']

conditions = [
    ('exception_only', [
        (99.83, None), (99.39, 0.098), (99.89, 0.098), (99.83, 0.0),
    ]),
    ('ae_only', [
        (99.64, 0.49), (98.53, 0.30), (99.08, 0.0), (99.08, None),
    ]),
    ('vota', [
        (99.05, 0.38), (99.25, 0.12), (98.74, 0.24), (99.54, 0.06),
    ]),
    ('loop_only', [
        (86.05, 0.52), (81.26, 0.0), (77.40, 1.54), (79.54, 1.42),
    ]),
    ('no_trace', [
        (75.13, None), (73.36, None), (76.47, None), (72.35, 4.48),
    ]),
]

# Compute CIs
data_rows = []
for cond_name, data in conditions:
    for i, (mean_pct, std_pct) in enumerate(data):
        if std_pct is not None:
            ci_lo = mean_pct - z * std_pct
            ci_hi = mean_pct + z * std_pct
        else:
            ci_lo, ci_hi = wilson_ci(mean_pct / 100, n)
        data_rows.append((models[i], mean_pct, ci_lo, ci_hi, cond_name))

tier1_colors = {'exception_only': '#D55E00', 'ae_only': '#E69F00', 'vota': '#CC79A7'}
tier2_color, baseline_color = '#009E73', '#0072B2'
def get_color(c):
    return tier1_colors.get(c, tier2_color if c == 'loop_only' else baseline_color)

cond_display = {
    'exception_only': 'Exception-Only',
    'ae_only': 'AE-Only',
    'vota': 'VoTA',
    'loop_only': 'Loop-Only',
    'no_trace': 'No-Trace (baseline)',
}

# Build y-axis with header rows
y = 0
y_map = []        # list of (y_pos, type, content)
                   # type='header' → condition header row; type='data' → data row with index into data_rows
data_idx = 0
header_gap = 0.35  # space above header
for ci, (cond_name, data) in enumerate(conditions):
    if ci > 0:
        y += 1.0
    y_map.append((y, 'header', cond_name))
    y += 0.7
    for mi in range(len(data)):
        y_map.append((y, 'data', data_idx))
        data_idx += 1
        y += 1

fig, ax = plt.subplots(figsize=(7, 7.5))

# Tier gap band
ax.axvspan(87, 98, color='#F0F0F0', zorder=0)

# Separator lines between groups
sep_positions = []
prev_group_end = None
for item in y_map:
    yp, typ, content = item
    if typ == 'header' and prev_group_end is not None:
        sep_positions.append((prev_group_end + yp) / 2)
    if typ == 'data':
        prev_group_end = yp

for sy in sep_positions:
    ax.axhline(y=sy, color='#CCCCCC', linewidth=0.5, zorder=1)

# Draw data points
for item in y_map:
    yp, typ, content = item
    if typ != 'data':
        continue
    label, mean, ci_lo, ci_hi, cond = data_rows[content]
    color = get_color(cond)
    ax.errorbar(mean, yp, xerr=[[mean - ci_lo], [ci_hi - mean]],
                fmt='o', color=color, markersize=5, capsize=2.5,
                elinewidth=1.0, capthick=0.8, zorder=5)
    ax.text(101.0, yp, f'{mean:.2f}', ha='left', va='center',
            fontsize=6.5, color=color, clip_on=False, zorder=6)

# Tier gap label
tier_gap_y = y_map[0][0] - 0.8
ax.text(92.5, tier_gap_y, 'Tier gap', ha='center', va='center',
        fontsize=8.5, color='#999999', fontstyle='italic', zorder=1)

# Y-axis: set ticks at all positions, style headers differently
all_y = [item[0] for item in y_map]
all_labels = []
for item in y_map:
    yp, typ, content = item
    if typ == 'header':
        all_labels.append(cond_display[content])
    else:
        all_labels.append('    ' + data_rows[content][0])

ax.set_yticks(all_y)
ax.set_yticklabels(all_labels, fontsize=7.5)

# Bold + color the header labels
for i, item in enumerate(y_map):
    yp, typ, content = item
    if typ == 'header':
        color = get_color(content)
        ax.get_yticklabels()[i].set_fontweight('bold')
        ax.get_yticklabels()[i].set_color(color)
        ax.get_yticklabels()[i].set_fontsize(8.5)

# Axis config
ax.set_xlim(60, 100.5)
ax.set_ylim(all_y[-1] + 1, all_y[0] - 1.2)
ax.set_xlabel('Accuracy (%)', fontsize=10, labelpad=6)
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.tick_params(axis='x', labelsize=8.5)
ax.tick_params(axis='y', length=0)
ax.grid(axis='x', which='major', linewidth=0.3, color='#DDDDDD', zorder=0)
ax.grid(axis='x', which='minor', linewidth=0.15, color='#EEEEEE', zorder=0)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_linewidth(0.5)

# Legend
legend_items = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor=get_color(c),
           markersize=6, label=cond_display[c])
    for c in ['exception_only', 'ae_only', 'vota', 'loop_only', 'no_trace']
]
ax.legend(handles=legend_items, loc='lower left', fontsize=7,
          framealpha=0.95, edgecolor='#CCCCCC', borderpad=0.6)

plt.tight_layout()
out = '/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/figures/forest_plot_tier_boundary'
fig.savefig(f'{out}.pdf', dpi=300, bbox_inches='tight')
fig.savefig(f'{out}.png', dpi=300, bbox_inches='tight')
plt.close()
print('DONE')

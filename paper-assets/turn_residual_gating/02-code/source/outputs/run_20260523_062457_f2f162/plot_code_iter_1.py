import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from scipy.interpolate import interp1d
import matplotlib.gridspec as gridspec

# --- Configuration ---
OUTPUT_PATH = "statistical_figure.png"

# --- Global Style Settings ---
plt.rcParams['font.family'] = 'sans-serif'
# A common sans-serif font stack
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.labelcolor'] = '#000000'
plt.rcParams['xtick.color'] = '#000000'
plt.rcParams['ytick.color'] = '#000000'
plt.rcParams['axes.titlepad'] = 12 # Add some padding to titles

# --- Colors ---
NEURIPS_NAVY = '#2C3E50'
NEURIPS_RED = '#C0392B'
GRAY_TEXT = '#7F8C8D'
LIGHT_GRAY_GRID = '#E0E0E0'
GREEN_CHECK = '#27AE60'
LIGHT_GREEN_BG = '#D4EDDA'
LIGHT_GRAY_BG = '#F5F6F7'

# --- Data ---
data = {
  "panel_a": {
    "title": "(a) The Phenomenon",
    "conditions": ["Base", "TG", "UG", "LO", "PCGrad", "SS"],
    "teacher_forced_gar": [0.501, 0.504, 0.496, 0.487, 0.519, 0.504],
    "autoregressive_gar": [0.019, 0.064, 0.033, 0.037, 0.03, 0.347]
  },
  "panel_b": {
    "title": "(b) Diagnostic Chain",
    "steps": [
      {"name": "Gate Analysis", "detail": "TF GAR = 0.50", "verdict": "PASS"},
      {"name": "PCGrad Exclusion", "detail": "Not gradient conflict", "verdict": "FAIL"},
      {"name": "TRC Analysis", "detail": "AUC = 0.98", "verdict": "FAIL"},
      {"name": "Conclusion", "detail": "Exposure bias", "verdict": "PASS", "highlight": True}
    ]
  },
  "panel_c": {
    "title": "(c) Constructive Evidence",
    "beta_values": np.array([0, 3, 5]),
    "ar_midturn_gar": np.array([0.064, 0.556, 0.727]),
    "xlabel": "beta (steering strength)",
    "ylabel": "AR Mid-turn GAR",
    "annotation": "11x recovery"
  }
}

# --- Figure Setup ---
fig = plt.figure(figsize=(14, 4.2), dpi=300)
gs = gridspec.GridSpec(1, 3, width_ratios=[0.38, 0.24, 0.38], figure=fig, wspace=0.3)

# =============================================================================
# Panel (a): The Phenomenon
# =============================================================================
ax1 = fig.add_subplot(gs[0])
panel_a_data = data['panel_a']

# Bar chart setup
conditions = panel_a_data['conditions']
teacher_forced = panel_a_data['teacher_forced_gar']
autoregressive = panel_a_data['autoregressive_gar']
x = np.arange(len(conditions))
width = 0.35

# Plotting bars
rects1 = ax1.bar(x - width/2, teacher_forced, width, label='Teacher-Forced', color=NEURIPS_NAVY, edgecolor='black', linewidth=0.75)
rects2 = ax1.bar(x + width/2, autoregressive, width, label='Autoregressive', color=NEURIPS_RED, edgecolor='black', linewidth=0.75)

# Special styling for the 'SS' bar
rects2[-1].set_hatch('//')
ax1.plot(x[-1] + width/2, autoregressive[-1] + 0.01, '*', color='yellow', markersize=12, markeredgecolor='black', zorder=10, clip_on=False)

# Labels and Title
ax1.set_ylabel('Mid-turn GAR', fontsize=12)
ax1.set_title(panel_a_data['title'], fontsize=14, loc='left')
ax1.set_xticks(x)
ax1.set_xticklabels(conditions, fontsize=12)
ax1.set_ylim(0, 0.55)
ax1.set_yticks(np.arange(0, 0.6, 0.1))
ax1.tick_params(axis='both', which='major', labelsize=11)

# Data labels for autoregressive bars
for i, rect in enumerate(rects2):
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width() / 2., height + 0.005,
             f'{autoregressive[i]:.3f}', ha='center', va='bottom',
             fontsize=9, color=GRAY_TEXT)

# Grid and Spines
ax1.grid(axis='y', linestyle='--', color=LIGHT_GRAY_GRID, zorder=0)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Legend
ax1.legend(loc='upper left', frameon=False, fontsize=11)

# Bracket Annotation
bracket_x = len(conditions) - 0.3
bracket_y_low = 0.08
bracket_y_high = 0.46
bracket_mid = (bracket_y_low + bracket_y_high) / 2
ax1.annotate('', xy=(bracket_x, bracket_y_low), xytext=(bracket_x, bracket_y_high),
             arrowprops=dict(arrowstyle='{,widthA=5.0,widthB=5.0', lw=1.0, color='black'))
ax1.text(bracket_x + 0.2, bracket_mid, '8-17x', ha='left', va='center', fontsize=11)


# =============================================================================
# Panel (b): Diagnostic Chain
# =============================================================================
ax2 = fig.add_subplot(gs[1])
panel_b_data = data['panel_b']
ax2.set_title(panel_b_data['title'], fontsize=14, loc='left')
ax2.axis('off')

# Flowchart properties
box_width = 0.9
box_height = 0.18
v_spacing = 0.07
y_start = 0.9

# Draw boxes and arrows
for i, step in enumerate(panel_b_data['steps']):
    y_center = y_start - i * (box_height + v_spacing)
    
    # Box style
    is_highlighted = step.get('highlight', False)
    face_color = LIGHT_GREEN_BG if is_highlighted else LIGHT_GRAY_BG
    edge_color = GREEN_CHECK if is_highlighted else 'gray'
    
    # Draw the rounded box patch
    box = patches.FancyBboxPatch(
        (0.5 - box_width/2, y_center - box_height/2),
        box_width, box_height,
        boxstyle=f"round,pad=0,rounding_size=0.1",
        facecolor=face_color,
        edgecolor=edge_color,
        lw=1,
        transform=ax2.transAxes,
        clip_on=False
    )
    ax2.add_patch(box)

    # Add text inside the box
    ax2.text(0.45, y_center + 0.035, step['name'], ha='center', va='center', fontsize=11, weight='bold', transform=ax2.transAxes)
    ax2.text(0.45, y_center - 0.035, step['detail'], ha='center', va='center', fontsize=10, transform=ax2.transAxes)

    # Verdict symbol
    if step['verdict'] == 'PASS':
        symbol, color = '✔', GREEN_CHECK
    else:
        symbol, color = '✗', NEURIPS_RED
    
    ax2.text(0.82, y_center, symbol, ha='center', va='center', fontsize=18, color=color, transform=ax2.transAxes)

    # Arrow to next box
    if i < len(panel_b_data['steps']) - 1:
        ax2.annotate('',
                     xy=(0.5, y_center - box_height/2),
                     xytext=(0.5, y_center - box_height/2 - v_spacing),
                     arrowprops=dict(arrowstyle='->', color='black', lw=1.5),
                     transform=ax2.transAxes)

# =============================================================================
# Panel (c): Constructive Evidence
# =============================================================================
ax3 = fig.add_subplot(gs[2])
panel_c_data = data['panel_c']

x_data = panel_c_data['beta_values']
y_data = panel_c_data['ar_midturn_gar']

# Create smooth curve
if len(x_data) > 1:
    f_quad = interp1d(x_data, y_data, kind='quadratic', fill_value="extrapolate")
    x_smooth = np.linspace(x_data.min(), x_data.max(), 300)
    y_smooth = f_quad(x_smooth)
    ax3.plot(x_smooth, y_smooth, color=NEURIPS_RED, lw=2, zorder=2)
    ax3.fill_between(x_smooth, y_smooth, color=NEURIPS_RED, alpha=0.15, zorder=1)

# Plot data points
ax3.plot(x_data, y_data, 'o', markersize=8,
         markerfacecolor='none', markeredgecolor=NEURIPS_RED,
         markeredgewidth=1.5, zorder=3)

# Data labels
for x, y in zip(x_data, y_data):
    ax3.text(x, y + 0.02, f'{y:.3f}', ha='center', va='bottom', fontsize=10)

# Labels and Title
ax3.set_xlabel(panel_c_data['xlabel'], fontsize=12)
ax3.set_ylabel(panel_c_data['ylabel'], fontsize=12)
ax3.set_title(panel_c_data['title'], fontsize=14, loc='left')

# Axes limits and ticks
ax3.set_xlim(-0.5, 5.5)
ax3.set_ylim(0, 0.85)
ax3.set_xticks([0, 3, 5])
ax3.tick_params(axis='both', which='major', labelsize=11)

# Text Annotation
ax3.text(2.5, 0.35, panel_c_data['annotation'], style='italic',
         fontsize=11, color=GRAY_TEXT, ha='center')

# Grid and Spines
ax3.grid(axis='y', linestyle='--', color=LIGHT_GRAY_GRID, zorder=0)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)


# --- Finalization ---
fig.tight_layout()
plt.savefig(OUTPUT_PATH, dpi=300, bbox_inches='tight')
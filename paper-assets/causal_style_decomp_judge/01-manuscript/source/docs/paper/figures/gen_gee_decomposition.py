"""
Generate publication-quality grouped bar chart for GEE conditional decomposition.
Shows Style OR vs Original OR across judges, grouped by Verbosity and Formality axes.
Key visual: Verbosity is style-dominated (Style >> Orig), Formality is mixed.
Output: gee_decomposition.pdf (vector, 300 DPI)
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# Publication style
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica'],
    'font.size': 8,
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.8,
    'ytick.major.width': 0.8,
    'xtick.major.size': 3,
    'ytick.major.size': 3,
    'lines.linewidth': 1,
    'pdf.fonttype': 42,      # TrueType fonts in PDF
    'ps.fonttype': 42,
    'mathtext.default': 'regular',
})

# --- Data ---
# Verbosity axis
verb_judges = ['Qwen3', 'GPT-4o', 'Llama-70B', 'Gemini']
verb_style  = [13.10, 11.34, 8.21, 8.98]
verb_orig   = [0.49,  0.45,  0.38, 0.46]

# Formality axis
form_judges = ['GPT-4o', 'Qwen3', 'Llama-70B', 'Gemini']
form_style  = [2.58, 4.20, 4.81, 1.64]
form_orig   = [2.32, 4.70, 3.12, 2.51]

# --- Layout ---
n_verb = len(verb_judges)
n_form = len(form_judges)
bar_width = 0.32
gap_between_groups = 1.0  # extra space between Verbosity and Formality

# X positions
verb_positions = np.arange(n_verb)
form_positions = np.arange(n_form) + n_verb + gap_between_groups

# Colors: Tableau palette
c_style = '#4E79A7'   # steel blue
c_orig  = '#E15759'   # soft red-orange

fig, ax = plt.subplots(figsize=(3.5, 2.5))

# --- Bars ---
# Verbosity
bars_vs = ax.bar(verb_positions - bar_width/2, verb_style, bar_width,
                 color=c_style, edgecolor='white', linewidth=0.3,
                 label='Style OR', zorder=3)
bars_vo = ax.bar(verb_positions + bar_width/2, verb_orig, bar_width,
                 color=c_orig, edgecolor='#666666', linewidth=0.5,
                 hatch='///', label='Orig OR', zorder=3)

# Formality
ax.bar(form_positions - bar_width/2, form_style, bar_width,
       color=c_style, edgecolor='white', linewidth=0.3, zorder=3)
ax.bar(form_positions + bar_width/2, form_orig, bar_width,
       color=c_orig, edgecolor='#666666', linewidth=0.5,
       hatch='///', zorder=3)

# --- Log scale ---
ax.set_yscale('log')
ax.set_ylim(0.25, 20)

# Y-axis formatting: show key ticks
ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
ax.yaxis.get_major_formatter().set_scientific(False)
ax.set_yticks([0.3, 0.5, 1, 2, 5, 10])
ax.set_yticklabels(['0.3', '0.5', '1', '2', '5', '10'])
ax.yaxis.set_minor_formatter(mticker.NullFormatter())

# --- Reference line at OR=1 ---
ax.axhline(y=1.0, color='#888888', linestyle='--', linewidth=0.8, zorder=2)

# --- Horizontal grid (light) ---
ax.yaxis.grid(True, which='major', linestyle='-', linewidth=0.3, color='#DDDDDD', zorder=1)
ax.xaxis.grid(False)
ax.set_axisbelow(True)

# --- X tick labels (judge names) ---
all_positions = np.concatenate([verb_positions, form_positions])
all_labels = verb_judges + form_judges
ax.set_xticks(all_positions)
ax.set_xticklabels(all_labels, fontsize=7, rotation=30, ha='right')

# --- Group labels ---
verb_center = verb_positions.mean()
form_center = form_positions.mean()
trans = ax.get_xaxis_transform()
ax.text(verb_center, -0.28, 'Verbosity', transform=trans,
        ha='center', va='top', fontsize=8, fontweight='bold')
ax.text(form_center, -0.28, 'Formality', transform=trans,
        ha='center', va='top', fontsize=8, fontweight='bold')

# --- Group separator line ---
sep_x = (verb_positions[-1] + form_positions[0]) / 2
ax.axvline(x=sep_x, color='#CCCCCC', linestyle='-', linewidth=0.5, ymin=0, ymax=1, zorder=1)

# --- Axis labels ---
ax.set_ylabel('Odds Ratio (log scale)', fontsize=8)

# --- Legend ---
ax.legend(fontsize=7, loc='upper right', frameon=True, framealpha=0.9,
          edgecolor='#CCCCCC', borderpad=0.3, handlelength=1.2, handletextpad=0.4)

# --- Spine cleanup ---
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# --- Tight layout ---
fig.subplots_adjust(bottom=0.28, left=0.14, right=0.96, top=0.95)

# --- Save ---
out_path = '/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/figures/gee_decomposition.pdf'
fig.savefig(out_path, format='pdf', dpi=300, bbox_inches='tight', pad_inches=0.02)
print(f'Saved: {out_path}')

# Also save PNG for quick preview
png_path = out_path.replace('.pdf', '.png')
fig.savefig(png_path, format='png', dpi=300, bbox_inches='tight', pad_inches=0.02)
print(f'Preview: {png_path}')

plt.close()

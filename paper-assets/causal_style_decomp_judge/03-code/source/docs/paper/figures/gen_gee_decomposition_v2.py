"""
Optimized GEE conditional decomposition: Style OR vs Orig OR across judges.
Narrative: Verbosity is style-dominated (Style OR >> 1, Orig OR < 1);
formality shows joint style+quality confounding.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'xtick.major.size': 3,
    'ytick.major.size': 3,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

# Colors from project palette
C_STYLE = '#4E79A7'
C_ORIG = '#E15759'

# Data from Table 3 (n=88, LLMBar)
verb_judges = ['Qwen3', 'GPT-4o', 'Llama-70B', 'Gemini']
verb_style  = [13.10, 11.34, 8.21, 8.98]
verb_orig   = [0.49,  0.45,  0.38, 0.46]
verb_style_p = ['<.0001', '<.0001', '<.0001', '<.0001']
verb_orig_p  = ['.096', '.062', '.020', '.061']

form_judges = ['GPT-4o', 'Qwen3', 'Llama-70B', 'Gemini']
form_style  = [2.58, 4.20, 4.81, 1.64]
form_orig   = [2.32, 4.70, 3.12, 2.51]
form_style_p = ['.002', '.0002', '<.0001', '.101']
form_orig_p  = ['.006', '.0001', '.0007', '.002']

n_verb = len(verb_judges)
n_form = len(form_judges)
bar_width = 0.30
gap = 1.2

verb_pos = np.arange(n_verb)
form_pos = np.arange(n_form) + n_verb + gap

fig, ax = plt.subplots(figsize=(3.6, 2.6))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# Verbosity bars
bars_vs = ax.bar(verb_pos - bar_width/2, verb_style, bar_width,
                 color=C_STYLE, edgecolor='white', linewidth=0.3,
                 label='Style OR', zorder=3)
bars_vo = ax.bar(verb_pos + bar_width/2, verb_orig, bar_width,
                 color=C_ORIG, edgecolor='#999999', linewidth=0.4,
                 hatch='///', alpha=0.85, label='Orig OR', zorder=3)

# Formality bars
bars_fs = ax.bar(form_pos - bar_width/2, form_style, bar_width,
                 color=C_STYLE, edgecolor='white', linewidth=0.3, zorder=3)
bars_fo = ax.bar(form_pos + bar_width/2, form_orig, bar_width,
                 color=C_ORIG, edgecolor='#999999', linewidth=0.4,
                 hatch='///', alpha=0.85, zorder=3)

# Log scale
ax.set_yscale('log')
ax.set_ylim(0.25, 22)

# Y-axis formatting
ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
ax.yaxis.get_major_formatter().set_scientific(False)
ax.set_yticks([0.3, 0.5, 1, 2, 5, 10])
ax.set_yticklabels(['0.3', '0.5', '1', '2', '5', '10'])
ax.yaxis.set_minor_formatter(mticker.NullFormatter())

# Reference line at OR=1
ax.axhline(y=1.0, color='#999999', linestyle='--', linewidth=0.7, zorder=2)
t = ax.text(-0.5, 1.07, 'OR = 1', fontsize=6.5, color='#999999',
            fontstyle='italic', va='bottom')

# Horizontal grid
ax.yaxis.grid(True, which='major', linestyle='-', linewidth=0.25,
              color='#E0E0E0', zorder=0)
ax.xaxis.grid(False)
ax.set_axisbelow(True)

# X tick labels
all_pos = np.concatenate([verb_pos, form_pos])
all_labels = verb_judges + form_judges
ax.set_xticks(all_pos)
ax.set_xticklabels(all_labels, fontsize=7, rotation=25, ha='right')

# Group labels with subtle background
trans = ax.get_xaxis_transform()
verb_center = verb_pos.mean()
form_center = form_pos.mean()

ax.text(verb_center, -0.30, 'Verbosity', transform=trans,
        ha='center', va='top', fontsize=9, fontweight='bold', color='#333333')
ax.text(form_center, -0.30, 'Formality', transform=trans,
        ha='center', va='top', fontsize=9, fontweight='bold', color='#333333')

# Group separator
sep_x = (verb_pos[-1] + form_pos[0]) / 2
ax.axvline(x=sep_x, color='#CCCCCC', linestyle='-', linewidth=0.5,
           ymin=0, ymax=1, zorder=1)

# Significance markers on Style OR bars (Verbosity)
def add_sig_marker(ax, x, y, p_str, color='#555555'):
    if p_str.startswith('<'):
        marker = '***'
    elif float(p_str) < 0.001:
        marker = '***'
    elif float(p_str) < 0.01:
        marker = '**'
    elif float(p_str) < 0.05:
        marker = '*'
    else:
        marker = 'n.s.'
    t = ax.text(x, y * 1.06, marker, ha='center', va='bottom',
                fontsize=5.5, color=color, fontweight='bold')
    t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

for i, (sp, val) in enumerate(zip(verb_style_p, verb_style)):
    add_sig_marker(ax, verb_pos[i] - bar_width/2, val, sp)

for i, (sp, val) in enumerate(zip(form_style_p, form_style)):
    add_sig_marker(ax, form_pos[i] - bar_width/2, val, sp)

# Axis labels
ax.set_ylabel('Odds Ratio (log scale)', fontsize=9)

# Legend
leg = ax.legend(fontsize=7.5, loc='upper right', frameon=True, framealpha=0.95,
                edgecolor='#DDDDDD', borderpad=0.4, handlelength=1.2,
                handletextpad=0.4)
leg.get_frame().set_linewidth(0.4)

# Spine cleanup
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(0.6)
ax.spines['left'].set_linewidth(0.6)

fig.subplots_adjust(bottom=0.30, left=0.14, right=0.96, top=0.95)

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/figures'
fig.savefig(f'{out_dir}/gee_decomposition.pdf', format='pdf', dpi=300,
            bbox_inches='tight', pad_inches=0.03, facecolor='white')
fig.savefig(f'{out_dir}/gee_decomposition.png', format='png', dpi=300,
            bbox_inches='tight', pad_inches=0.03, facecolor='white')
plt.close()
print('Saved: gee_decomposition.pdf + .png')

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# --- Trained data: 3 tasks, raw per_head_attn_to_text and per_head_attn_to_image ---
# The "instruction-dominant" threshold in the paper is: raw text_frac > 0.5 (of total including BOS)
# For stacked bars: instruction = text_frac, visual = 1 - text_frac (image + BOS)

trained_text_task0 = [0.8536376953125,0.53509521484375,0.68304443359375,0.471466064453125,0.5867233276367188,0.498046875,0.394805908203125,0.569671630859375,0.58123779296875,0.452606201171875,0.7152099609375,0.5701904296875,0.5364990234375,0.41016387939453125,0.69647216796875,0.6108169555664062,0.525848388671875,0.55120849609375,0.5181121826171875,0.6407318115234375,0.5516357421875,0.458770751953125,0.8058147430419922,0.57220458984375,0.366424560546875,0.769256591796875,0.56707763671875,0.653472900390625,0.503387451171875,0.589263916015625,0.5357666015625,0.5589599609375]

trained_text_task1 = [0.856719970703125,0.5569610595703125,0.7030029296875,0.4571533203125,0.5877685546875,0.4925537109375,0.40106201171875,0.557342529296875,0.5824584960937,0.437347412109375,0.71026611328125,0.6070327758789062,0.53277587890625,0.5465087890625,0.5405426025390625,0.6549072265625,0.52325439453125,0.452239990234375,0.8254013061523438,0.590728759765625,0.3663177490234375,0.781494140625,0.55816650390625,0.6743011474609375,0.498626708984375,0.611358642578125,0.542572021484375,0.547607421875,0.5181121826171875,0.6407318115234375,0.5516357421875,0.458770751953125]

trained_text_task2 = [0.852569580078125,0.54840087890625,0.7081298828125,0.475555419921875,0.5866012573242188,0.50164794921875,0.413299560546875,0.573699951171875,0.5865478515625,0.4401397705078125,0.71649169921875,0.57843017578125,0.534912109375,0.4060821533203125,0.71636962890625,0.6230087280273438,0.538482666015625,0.5455322265625,0.5452117919921875,0.646087646484375,0.53546142578125,0.45086669921875,0.8309307098388672,0.576568603515625,0.3722991943359375,0.787872314453125,0.5629119873046875,0.686920166015625,0.503082275390625,0.60833740234375,0.54925537109375,0.55242919921875]

trained_text = np.mean([trained_text_task0, trained_text_task1, trained_text_task2], axis=0)
trained_instr_frac = trained_text  # raw fraction (sums with image+BOS to 1.0)
trained_other_frac = 1.0 - trained_instr_frac

# --- Untrained data: per-head means ---
untrained_per_head_instr = [
    0.24161453545093536, 0.12787894904613495, 0.037618495523929596, 0.09396610409021378,
    0.04583416134119034, 0.06292605400085449, 0.31746578216552734, 0.07706127315759659,
    0.07596445083618164, 0.15708771347999573, 0.05471992492675781, 0.08290300518274307,
    0.14625510573387146, 0.05091552808880806, 0.1843077689409256, 0.10991553962230682,
    0.44306182861328125, 0.0789283737540245, 0.05970115587115288, 0.04481563717126846,
    0.08788414299488068, 0.0540616512298584, 0.0745229721069336, 0.08040504157543182,
    0.23905257880687714, 0.18975791335105896, 0.079145148396492, 0.07721290737390518,
    0.011515850201249123, 0.10416159778833389, 0.11366014182567596, 0.1384410858154297
]
untrained_per_head_image = [
    0.7581395506858826, 0.872033953666687, 0.9607089757919312, 0.9051351547241211,
    0.953342080116272, 0.9356164932250977, 0.6762827038764954, 0.9219636917114258,
    0.9235334396362305, 0.8422257304191589, 0.9448118209838867, 0.9155687093734741,
    0.8536079525947571, 0.948947548866272, 0.815268874168396, 0.8892623782157898,
    0.5564411282539368, 0.921096682548523, 0.9402963519096375, 0.9550886154174805,
    0.9104686975479126, 0.9179593920707703, 0.9019235372543335, 0.9174043536186218,
    0.7596372961997986, 0.807194709777832, 0.916604220867157, 0.9202300906181335,
    0.9866241216659546, 0.8952945470809937, 0.8860788345336914, 0.7948678731918335
]

untrained_instr = np.array(untrained_per_head_instr)
untrained_image = np.array(untrained_per_head_image)

# Sort by trained instruction fraction (descending)
sort_order = np.argsort(-trained_instr_frac)

trained_instr_sorted = trained_instr_frac[sort_order]
trained_other_sorted = trained_other_frac[sort_order]
untrained_instr_sorted = untrained_instr[sort_order]
untrained_image_sorted = untrained_image[sort_order]

# Count instruction-dominant heads (raw text > 0.5)
trained_dominant = int(np.sum(trained_instr_frac > 0.5))
untrained_dominant = int(np.sum(untrained_instr > 0.5))

print(f"Trained instruction-dominant heads: {trained_dominant}/32")
print(f"Untrained instruction-dominant heads: {untrained_dominant}/32")

# --- Figure ---
mpl.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica'],
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 10,
    'xtick.labelsize': 7.5,
    'ytick.labelsize': 8,
    'legend.fontsize': 8.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

color_instr = '#2171B5'
color_image = '#FC8D59'

fig, axes = plt.subplots(1, 2, figsize=(7.0, 2.6), sharey=True)

x = np.arange(32)
bar_width = 0.82

panels = [
    (trained_instr_sorted, trained_other_sorted, '(a) Trained', trained_dominant),
    (untrained_instr_sorted, untrained_image_sorted, '(b) Untrained', untrained_dominant),
]

for ax_idx, (ax, (instr_data, other_data, label, dominant_count)) in enumerate(zip(axes, panels)):
    ax.bar(x, instr_data, bar_width, color=color_instr, label='Instruction tokens', edgecolor='none', zorder=2)
    ax.bar(x, other_data, bar_width, bottom=instr_data, color=color_image, label='Image tokens', edgecolor='none', zorder=2)

    ax.axhline(y=0.5, color='#444444', linestyle='--', linewidth=0.7, alpha=0.6, zorder=3)

    # Panel label
    ax.text(0.02, 0.97, label, transform=ax.transAxes, fontsize=10,
            fontweight='bold', va='top', ha='left')

    # Annotation
    annot_text = f'{dominant_count}/32 heads instruction-dominant'
    if ax_idx == 0:
        ax.text(0.97, 0.08, annot_text, transform=ax.transAxes, fontsize=8,
                ha='right', va='bottom',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#999999', linewidth=0.5, alpha=0.92))
    else:
        ax.text(0.97, 0.08, annot_text, transform=ax.transAxes, fontsize=8,
                ha='right', va='bottom',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#999999', linewidth=0.5, alpha=0.92))

    ax.set_xlim(-0.6, 31.6)
    ax.set_ylim(0, 1.0)
    ax.set_xlabel('Attention heads (sorted by instruction fraction)', fontsize=9)
    if ax_idx == 0:
        ax.set_ylabel('Attention fraction')

    ax.set_xticks([0, 7, 15, 23, 31])
    ax.set_xticklabels(['1', '8', '16', '24', '32'])
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(axis='both', which='both', length=3)

# Shared legend
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', ncol=2, frameon=False,
           bbox_to_anchor=(0.5, 1.01), fontsize=9)

plt.tight_layout(rect=[0, 0, 1, 0.93])

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
output_path = os.path.join(_REPO_ROOT, 'artifacts', 'attention', 'fig8_attention_final.pdf')
plt.savefig(output_path, format='pdf', bbox_inches='tight', pad_inches=0.04)
plt.savefig(output_path.replace('.pdf', '.png'), format='png', bbox_inches='tight', pad_inches=0.04)
print(f"\nSaved: {output_path}")

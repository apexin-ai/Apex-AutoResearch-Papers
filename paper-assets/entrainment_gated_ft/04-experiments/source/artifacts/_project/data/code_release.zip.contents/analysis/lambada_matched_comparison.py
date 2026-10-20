import json
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib_venn import venn2
from collections import defaultdict

OUT_DIR = '/root/entrainment_gated_ft/analysis'
DATA_DIR = '/root/entrainment_gated_ft/lm_eval_clean'

# ── Load data ──────────────────────────────────────────────────────
def load_jsonl(path):
    samples = []
    with open(path) as f:
        for line in f:
            samples.append(json.loads(line))
    return samples

def load_json_samples(path, task='lambada_openai'):
    with open(path) as f:
        d = json.load(f)
    return d['samples'][task]

print("Loading data...")
model_data = {}

# GDN h3-1 from JSONL
model_data['GDN-h3-1'] = sorted(
    load_jsonl(os.path.join(DATA_DIR, '1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl')),
    key=lambda x: x['doc_id']
)

# GDN pure from JSON
model_data['GDN-pure'] = sorted(
    load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-GatedDeltaNet-pure.json')),
    key=lambda x: x['doc_id']
)

# HGRN2 h3-1 from JSON
model_data['HGRN2-h3-1'] = sorted(
    load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-HGRN2-hybrid-3-1.json')),
    key=lambda x: x['doc_id']
)

# HGRN2 pure from JSON
model_data['HGRN2-pure'] = sorted(
    load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-HGRN2-pure.json')),
    key=lambda x: x['doc_id']
)

for name, samples in model_data.items():
    print(f"  {name}: {len(samples)} samples")

n_samples = len(model_data['GDN-pure'])

# Verify alignment
ref_ids = [s['doc_id'] for s in model_data['GDN-pure']]
for name, samples in model_data.items():
    assert len(samples) == n_samples
    ids = [s['doc_id'] for s in samples]
    assert ids == ref_ids, f"{name} doc_id mismatch"
print(f"All {n_samples} samples aligned.\n")

# Extract arrays
acc = {name: np.array([s['acc'] for s in samples]) for name, samples in model_data.items()}
logprob = {name: np.array([s['perplexity'] for s in samples]) for name, samples in model_data.items()}

# Context lengths
contexts = []
targets = []
for s in model_data['GDN-pure']:
    text = s['doc']['text']
    target = s['target'].strip()
    ctx = text[:text.rfind(target)] if target in text else text
    contexts.append(ctx)
    targets.append(target)
context_lengths = np.array([len(c.split()) for c in contexts])

# ── Section 1: Helped/Hurt Statistics ──────────────────────────────
print("=" * 70)
print("SECTION 1: Overall Accuracy (Matched Comparison: both h3-1)")
print("=" * 70)
for name in ['GDN-pure', 'GDN-h3-1', 'HGRN2-pure', 'HGRN2-h3-1']:
    print(f"  {name:15s}: {acc[name].mean():.4f} ({int(acc[name].sum())}/{n_samples})")

pairs = [
    ('GDN', 'GDN-pure', 'GDN-h3-1'),
    ('HGRN2', 'HGRN2-pure', 'HGRN2-h3-1'),
]

print("\n" + "=" * 70)
print("SECTION 2: Attention Effect (h3-1 vs pure, matched dosage)")
print("=" * 70)

helped_sets = {}
hurt_sets = {}

for pair_name, pure, hybrid in pairs:
    helped = (acc[pure] == 0) & (acc[hybrid] == 1)
    hurt = (acc[pure] == 1) & (acc[hybrid] == 0)
    both_correct = (acc[pure] == 1) & (acc[hybrid] == 1)
    both_wrong = (acc[pure] == 0) & (acc[hybrid] == 0)

    helped_sets[pair_name] = set(np.where(helped)[0])
    hurt_sets[pair_name] = set(np.where(hurt)[0])

    print(f"\n  {pair_name} ({pure} -> {hybrid}):")
    print(f"    Both correct:     {both_correct.sum():5d} ({both_correct.mean()*100:.1f}%)")
    print(f"    Both wrong:       {both_wrong.sum():5d} ({both_wrong.mean()*100:.1f}%)")
    print(f"    Attention helped: {helped.sum():5d} ({helped.mean()*100:.1f}%)")
    print(f"    Attention hurt:   {hurt.sum():5d} ({hurt.mean()*100:.1f}%)")
    print(f"    Net effect:       {helped.sum() - hurt.sum():+5d} samples")

# ── Section 3: Jaccard Overlap ─────────────────────────────────────
print("\n" + "=" * 70)
print("SECTION 3: Cross-Architecture Overlap (Jaccard)")
print("=" * 70)

def jaccard(a, b):
    if len(a) == 0 and len(b) == 0:
        return float('nan')
    return len(a & b) / len(a | b)

gdn_h = helped_sets['GDN']
hgrn_h = helped_sets['HGRN2']
gdn_r = hurt_sets['GDN']
hgrn_r = hurt_sets['HGRN2']

print(f"\n  Helped sets:")
print(f"    GDN helped:  {len(gdn_h)}")
print(f"    HGRN2 helped: {len(hgrn_h)}")
print(f"    Intersection: {len(gdn_h & hgrn_h)}")
print(f"    Union:        {len(gdn_h | hgrn_h)}")
print(f"    Jaccard:      {jaccard(gdn_h, hgrn_h):.4f}")

print(f"\n  Hurt sets:")
print(f"    GDN hurt:    {len(gdn_r)}")
print(f"    HGRN2 hurt:  {len(hgrn_r)}")
print(f"    Intersection: {len(gdn_r & hgrn_r)}")
print(f"    Union:        {len(gdn_r | hgrn_r)}")
print(f"    Jaccard:      {jaccard(gdn_r, hgrn_r):.4f}")

# Cross-table
print(f"\n  Detailed cross-table (GDN effect x HGRN2 effect):")
gdn_eff = np.zeros(n_samples, dtype=int)  # 0=unchanged, 1=helped, -1=hurt
gdn_eff[list(gdn_h)] = 1
gdn_eff[list(gdn_r)] = -1
hgrn_eff = np.zeros(n_samples, dtype=int)
hgrn_eff[list(hgrn_h)] = 1
hgrn_eff[list(hgrn_r)] = -1

labels = {-1: 'hurt', 0: 'unchanged', 1: 'helped'}
print(f"  {'':20s} HGRN2-hurt  HGRN2-unch  HGRN2-helped")
for gv in [-1, 0, 1]:
    row = []
    for hv in [-1, 0, 1]:
        cnt = int(((gdn_eff == gv) & (hgrn_eff == hv)).sum())
        row.append(f"{cnt:8d}")
    print(f"  GDN-{labels[gv]:12s} {'  '.join(row)}")

# ── Section 4: Length Analysis ─────────────────────────────────────
print("\n" + "=" * 70)
print("SECTION 4: Length-Stratified Analysis")
print("=" * 70)

length_bins = [
    (0, 20, 'short (<20w)'),
    (20, 40, 'medium (20-40w)'),
    (40, 70, 'long (40-70w)'),
    (70, 9999, 'very long (70+w)'),
]

length_stats = defaultdict(list)

for lo, hi, label in length_bins:
    mask = (context_lengths >= lo) & (context_lengths < hi)
    n = mask.sum()
    if n == 0:
        continue
    print(f"\n  {label}: {n} samples")
    for name in ['GDN-pure', 'GDN-h3-1', 'HGRN2-pure', 'HGRN2-h3-1']:
        print(f"    {name:15s}: acc={acc[name][mask].mean():.4f}")

    for pair_name, pure, hybrid in pairs:
        h = int(((acc[pure] == 0) & (acc[hybrid] == 1) & mask).sum())
        r = int(((acc[pure] == 1) & (acc[hybrid] == 0) & mask).sum())
        print(f"    {pair_name} attn net: {h-r:+d} (helped={h}, hurt={r})")
        length_stats[pair_name].append((label, n, h, r))

# ── Section 5: Logprob Shifts ──────────────────────────────────────
print("\n" + "=" * 70)
print("SECTION 5: Logprob Shifts (h3-1 - pure)")
print("=" * 70)

for pair_name, pure, hybrid in pairs:
    delta = logprob[hybrid] - logprob[pure]
    print(f"\n  {pair_name}:")
    print(f"    Mean:   {delta.mean():.4f}")
    print(f"    Median: {np.median(delta):.4f}")

    helped = (acc[pure] == 0) & (acc[hybrid] == 1)
    hurt = (acc[pure] == 1) & (acc[hybrid] == 0)
    stable_right = (acc[pure] == 1) & (acc[hybrid] == 1)
    stable_wrong = (acc[pure] == 0) & (acc[hybrid] == 0)

    for lbl, m in [('helped', helped), ('hurt', hurt), ('stable_right', stable_right), ('stable_wrong', stable_wrong)]:
        if m.sum() > 0:
            print(f"    {lbl:14s}: mean_delta={delta[m].mean():.4f}  n={m.sum()}")

# ── Plotting ───────────────────────────────────────────────────────
print("\nGenerating plots...")

fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

# Panel A: Helped/Hurt/Unchanged bar chart
ax = axes[0]
categories = ['Both\ncorrect', 'Both\nwrong', 'Helped', 'Hurt']
x = np.arange(len(categories))
width = 0.35

gdn_vals = []
hgrn_vals = []
for pair_name, pure, hybrid in pairs:
    bc = int(((acc[pure] == 1) & (acc[hybrid] == 1)).sum())
    bw = int(((acc[pure] == 0) & (acc[hybrid] == 0)).sum())
    h = int(((acc[pure] == 0) & (acc[hybrid] == 1)).sum())
    r = int(((acc[pure] == 1) & (acc[hybrid] == 0)).sum())
    if pair_name == 'GDN':
        gdn_vals = [bc, bw, h, r]
    else:
        hgrn_vals = [bc, bw, h, r]

bars1 = ax.bar(x - width/2, gdn_vals, width, label='GDN', color='#4C72B0', edgecolor='black', linewidth=0.5)
bars2 = ax.bar(x + width/2, hgrn_vals, width, label='HGRN2', color='#DD8452', edgecolor='black', linewidth=0.5)

for bars in [bars1, bars2]:
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 20, f'{int(h)}',
                ha='center', va='bottom', fontsize=7)

ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=9)
ax.set_ylabel('Number of samples', fontsize=10)
ax.set_title('(A) Attention Effect on LAMBADA\n(h3-1 vs pure, matched dosage)', fontsize=10)
ax.legend(fontsize=9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Panel B: Venn diagrams for helped and hurt
ax = axes[1]
ax.set_title('(B) Cross-Architecture Overlap', fontsize=10)

try:
    ax_top = fig.add_axes([ax.get_position().x0, ax.get_position().y0 + ax.get_position().height * 0.5,
                           ax.get_position().width, ax.get_position().height * 0.45])
    ax_bot = fig.add_axes([ax.get_position().x0, ax.get_position().y0 + ax.get_position().height * 0.02,
                           ax.get_position().width, ax.get_position().height * 0.45])
    ax.set_visible(False)

    v1 = venn2(
        [gdn_h, hgrn_h],
        set_labels=('GDN', 'HGRN2'),
        ax=ax_top,
        set_colors=('#4C72B0', '#DD8452'),
        alpha=0.6
    )
    ax_top.set_title(f'Helped (J={jaccard(gdn_h, hgrn_h):.3f})', fontsize=9)

    v2 = venn2(
        [gdn_r, hgrn_r],
        set_labels=('GDN', 'HGRN2'),
        ax=ax_bot,
        set_colors=('#4C72B0', '#DD8452'),
        alpha=0.6
    )
    ax_bot.set_title(f'Hurt (J={jaccard(gdn_r, hgrn_r):.3f})', fontsize=9)
except Exception as e:
    print(f"  Venn diagram failed ({e}), using text fallback")
    ax.set_visible(True)
    ax.text(0.5, 0.7, f"Helped: J={jaccard(gdn_h, hgrn_h):.3f}\n"
            f"GDN only: {len(gdn_h - hgrn_h)}, Both: {len(gdn_h & hgrn_h)}, HGRN2 only: {len(hgrn_h - gdn_h)}",
            ha='center', va='center', transform=ax.transAxes, fontsize=9)
    ax.text(0.5, 0.3, f"Hurt: J={jaccard(gdn_r, hgrn_r):.3f}\n"
            f"GDN only: {len(gdn_r - hgrn_r)}, Both: {len(gdn_r & hgrn_r)}, HGRN2 only: {len(hgrn_r - gdn_r)}",
            ha='center', va='center', transform=ax.transAxes, fontsize=9)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

# Panel C: Length-stratified net effect
ax = axes[2]
bin_labels = [s[0] for s in length_stats['GDN']]
bin_n = [s[1] for s in length_stats['GDN']]
gdn_net = [(s[2] - s[3]) / s[1] * 100 for s in length_stats['GDN']]
hgrn_net = [(s[2] - s[3]) / s[1] * 100 for s in length_stats['HGRN2']]

x = np.arange(len(bin_labels))
bars1 = ax.bar(x - width/2, gdn_net, width, label='GDN', color='#4C72B0', edgecolor='black', linewidth=0.5)
bars2 = ax.bar(x + width/2, hgrn_net, width, label='HGRN2', color='#DD8452', edgecolor='black', linewidth=0.5)

for bars in [bars1, bars2]:
    for bar in bars:
        h = bar.get_height()
        va = 'bottom' if h >= 0 else 'top'
        offset = 0.2 if h >= 0 else -0.2
        ax.text(bar.get_x() + bar.get_width()/2., h + offset, f'{h:.1f}%',
                ha='center', va=va, fontsize=7)

ax.axhline(y=0, color='black', linewidth=0.5)
ax.set_xticks(x)
ax.set_xticklabels(bin_labels, fontsize=8)
ax.set_ylabel('Net attention effect (%)', fontsize=10)
ax.set_title('(C) Length-Stratified Net Effect', fontsize=10)
ax.legend(fontsize=9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add sample counts as secondary labels
for i, n in enumerate(bin_n):
    ax.text(i, ax.get_ylim()[0] - 0.5, f'n={n}', ha='center', va='top', fontsize=7, color='gray')

# D004 caveat footnote
fig.text(0.5, -0.02,
    'Note: GDN h3-1 has a known attention head config anomaly (num_heads=16, GQA 2:1 vs standard 32, GQA 4:1). '
    'See GDN h6-1 robustness check.',
    ha='center', va='top', fontsize=7, style='italic', color='#555555',
    wrap=True)

plt.tight_layout()

for ext in ['png', 'pdf']:
    path = os.path.join(OUT_DIR, f'lambada_matched_comparison.{ext}')
    fig.savefig(path, dpi=200, bbox_inches='tight')
    print(f"  Saved: {path}")

plt.close()

# Save updated CSV
import csv
csv_path = os.path.join(OUT_DIR, 'lambada_matched_per_example.csv')
with open(csv_path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['doc_id', 'context_length', 'target',
                'gdn_pure_acc', 'gdn_pure_lp', 'gdn_h31_acc', 'gdn_h31_lp',
                'hgrn2_pure_acc', 'hgrn2_pure_lp', 'hgrn2_h31_acc', 'hgrn2_h31_lp'])
    for i in range(n_samples):
        w.writerow([
            model_data['GDN-pure'][i]['doc_id'],
            context_lengths[i],
            targets[i],
            int(acc['GDN-pure'][i]), logprob['GDN-pure'][i],
            int(acc['GDN-h3-1'][i]), logprob['GDN-h3-1'][i],
            int(acc['HGRN2-pure'][i]), logprob['HGRN2-pure'][i],
            int(acc['HGRN2-h3-1'][i]), logprob['HGRN2-h3-1'][i],
        ])
print(f"  CSV saved: {csv_path}")
print("\n" + "=" * 70)
print("CAVEAT (D004)")
print("=" * 70)
print("  GDN h3-1 has a known attention head configuration anomaly")
print("  (num_heads=16, GQA 2:1) compared to other variants (num_heads=32, GQA 4:1).")
print("  This may amplify the negative attention effect observed for GDN.")
print("  See GDN h6-1 robustness check (lambada_robustness_h6.py).")

print("\nDone.")

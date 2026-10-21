"""GDN h6-1 robustness check: verify whether the GDN negative attention effect
persists at h6-1 (4 attn layers, num_heads=32, no D004 confound)."""

import json
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
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

print("Loading h6-1 data...")
model_data = {}

model_data['GDN-h6-1'] = sorted(
    load_jsonl(os.path.join(DATA_DIR, '1.3b/GDN-h6-1-logsamples/samples/lambada_openai.jsonl')),
    key=lambda x: x['doc_id']
)

model_data['GDN-pure'] = sorted(
    load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-GatedDeltaNet-pure.json')),
    key=lambda x: x['doc_id']
)

model_data['HGRN2-h6-1'] = sorted(
    load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-HGRN2-hybrid-6-1.json')),
    key=lambda x: x['doc_id']
)

model_data['HGRN2-pure'] = sorted(
    load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-HGRN2-pure.json')),
    key=lambda x: x['doc_id']
)

for name, samples in model_data.items():
    print(f"  {name}: {len(samples)} samples")

n_samples = len(model_data['GDN-pure'])

ref_ids = [s['doc_id'] for s in model_data['GDN-pure']]
for name, samples in model_data.items():
    assert len(samples) == n_samples, f"{name} count mismatch"
    ids = [s['doc_id'] for s in samples]
    assert ids == ref_ids, f"{name} doc_id mismatch"
print(f"All {n_samples} samples aligned.\n")

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

# ── Section 1: Overall accuracy ────────────────────────────────────
print("=" * 70)
print("SECTION 1: Overall Accuracy (h6-1 robustness check)")
print("=" * 70)
for name in ['GDN-pure', 'GDN-h6-1', 'HGRN2-pure', 'HGRN2-h6-1']:
    print(f"  {name:15s}: {acc[name].mean():.4f} ({int(acc[name].sum())}/{n_samples})")

pairs = [
    ('GDN', 'GDN-pure', 'GDN-h6-1'),
    ('HGRN2', 'HGRN2-pure', 'HGRN2-h6-1'),
]

# ── Section 2: Helped/Hurt ─────────────────────────────────────────
print("\n" + "=" * 70)
print("SECTION 2: Attention Effect (h6-1 vs pure, 4 attn layers)")
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
print("SECTION 3: Cross-Architecture Overlap (Jaccard, h6-1)")
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
print(f"\n  Cross-table (GDN effect x HGRN2 effect):")
gdn_eff = np.zeros(n_samples, dtype=int)
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

# ── Section 4: Length analysis ─────────────────────────────────────
print("\n" + "=" * 70)
print("SECTION 4: Length-Stratified Analysis (h6-1)")
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
    for name in ['GDN-pure', 'GDN-h6-1', 'HGRN2-pure', 'HGRN2-h6-1']:
        print(f"    {name:15s}: acc={acc[name][mask].mean():.4f}")
    for pair_name, pure, hybrid in pairs:
        h = int(((acc[pure] == 0) & (acc[hybrid] == 1) & mask).sum())
        r = int(((acc[pure] == 1) & (acc[hybrid] == 0) & mask).sum())
        print(f"    {pair_name} attn net: {h-r:+d} (helped={h}, hurt={r})")
        length_stats[pair_name].append((label, n, h, r))

# ── Section 5: Comparison with h3-1 results ────────────────────────
print("\n" + "=" * 70)
print("SECTION 5: h6-1 vs h3-1 Comparison")
print("=" * 70)

# Load h3-1 data for comparison
print("\n  Loading h3-1 data for comparison...")
h31_data = {}
h31_data['GDN-h3-1'] = sorted(
    load_jsonl(os.path.join(DATA_DIR, '1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl')),
    key=lambda x: x['doc_id']
)
h31_data['HGRN2-h3-1'] = sorted(
    load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-HGRN2-hybrid-3-1.json')),
    key=lambda x: x['doc_id']
)

acc_h31 = {name: np.array([s['acc'] for s in samples]) for name, samples in h31_data.items()}

# h3-1 stats
gdn_h31_helped = int(((acc['GDN-pure'] == 0) & (acc_h31['GDN-h3-1'] == 1)).sum())
gdn_h31_hurt = int(((acc['GDN-pure'] == 1) & (acc_h31['GDN-h3-1'] == 0)).sum())
hgrn_h31_helped = int(((acc['HGRN2-pure'] == 0) & (acc_h31['HGRN2-h3-1'] == 1)).sum())
hgrn_h31_hurt = int(((acc['HGRN2-pure'] == 1) & (acc_h31['HGRN2-h3-1'] == 0)).sum())

# h6-1 stats
gdn_h61_helped = len(helped_sets['GDN'])
gdn_h61_hurt = len(hurt_sets['GDN'])
hgrn_h61_helped = len(helped_sets['HGRN2'])
hgrn_h61_hurt = len(hurt_sets['HGRN2'])

print(f"\n  {'':20s} {'h3-1 (2 attn)':>20s} {'h6-1 (4 attn)':>20s}")
print(f"  {'':20s} {'helped/hurt/net':>20s} {'helped/hurt/net':>20s}")
print(f"  {'-'*62}")
print(f"  {'GDN':20s} {gdn_h31_helped:5d}/{gdn_h31_hurt:5d}/{gdn_h31_helped-gdn_h31_hurt:+5d}      {gdn_h61_helped:5d}/{gdn_h61_hurt:5d}/{gdn_h61_helped-gdn_h61_hurt:+5d}")
print(f"  {'HGRN2':20s} {hgrn_h31_helped:5d}/{hgrn_h31_hurt:5d}/{hgrn_h31_helped-hgrn_h31_hurt:+5d}      {hgrn_h61_helped:5d}/{hgrn_h61_hurt:5d}/{hgrn_h61_helped-hgrn_h61_hurt:+5d}")

print(f"\n  GDN h3-1 config: num_heads=16, GQA 2:1 (ANOMALOUS)")
print(f"  GDN h6-1 config: num_heads=32, GQA 4:1 (NORMAL)")

gdn_h61_net = gdn_h61_helped - gdn_h61_hurt
if gdn_h61_net < 0:
    print(f"\n  CONCLUSION: GDN h6-1 net effect is {gdn_h61_net:+d} (still negative).")
    print(f"  The negative attention effect for GDN is NOT solely due to the D004 confound.")
elif gdn_h61_net > 0:
    print(f"\n  CONCLUSION: GDN h6-1 net effect is {gdn_h61_net:+d} (now positive).")
    print(f"  The D004 confound likely explains the h3-1 negative result.")
else:
    print(f"\n  CONCLUSION: GDN h6-1 net effect is 0 (neutral).")
    print(f"  The D004 confound likely contributes to the h3-1 negative result.")

# ── Plotting ───────────────────────────────────────────────────────
print("\nGenerating plots...")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle('LAMBADA Robustness Check: h6-1 (4 attn layers, no D004 confound)', fontsize=12, y=1.02)

# Panel A: h3-1 vs h6-1 comparison bar chart
ax = axes[0]
configs = ['h3-1\n(2 attn)', 'h6-1\n(4 attn)']
x = np.arange(2)
width = 0.35

gdn_nets = [gdn_h31_helped - gdn_h31_hurt, gdn_h61_helped - gdn_h61_hurt]
hgrn_nets = [hgrn_h31_helped - hgrn_h31_hurt, hgrn_h61_helped - hgrn_h61_hurt]

bars1 = ax.bar(x - width/2, gdn_nets, width, label='GDN', color='#4C72B0', edgecolor='black', linewidth=0.5)
bars2 = ax.bar(x + width/2, hgrn_nets, width, label='HGRN2', color='#DD8452', edgecolor='black', linewidth=0.5)

for bars in [bars1, bars2]:
    for bar in bars:
        h = bar.get_height()
        va = 'bottom' if h >= 0 else 'top'
        offset = 3 if h >= 0 else -3
        ax.text(bar.get_x() + bar.get_width()/2., h + offset, f'{int(h):+d}',
                ha='center', va=va, fontsize=9, fontweight='bold')

ax.axhline(y=0, color='black', linewidth=0.8)
ax.set_xticks(x)
ax.set_xticklabels(configs, fontsize=10)
ax.set_ylabel('Net attention effect (samples)', fontsize=10)
ax.set_title('(A) Net Effect: h3-1 vs h6-1', fontsize=11)
ax.legend(fontsize=9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Annotate D004
ax.annotate('D004\nconfound', xy=(0 - width/2, gdn_nets[0]),
            xytext=(0 - width/2 - 0.3, gdn_nets[0] - 40),
            fontsize=7, color='red', ha='center',
            arrowprops=dict(arrowstyle='->', color='red', lw=0.8))

# Panel B: h6-1 helped/hurt breakdown
ax = axes[1]
categories = ['Both\ncorrect', 'Both\nwrong', 'Helped', 'Hurt']
x = np.arange(len(categories))

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
ax.set_title('(B) h6-1 Attention Effect on LAMBADA', fontsize=11)
ax.legend(fontsize=9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Panel C: Length-stratified net effect (h6-1)
ax = axes[2]
bin_labels = [s[0] for s in length_stats['GDN']]
bin_n = [s[1] for s in length_stats['GDN']]
gdn_net_pct = [(s[2] - s[3]) / s[1] * 100 for s in length_stats['GDN']]
hgrn_net_pct = [(s[2] - s[3]) / s[1] * 100 for s in length_stats['HGRN2']]

x = np.arange(len(bin_labels))
bars1 = ax.bar(x - width/2, gdn_net_pct, width, label='GDN', color='#4C72B0', edgecolor='black', linewidth=0.5)
bars2 = ax.bar(x + width/2, hgrn_net_pct, width, label='HGRN2', color='#DD8452', edgecolor='black', linewidth=0.5)

for bars in [bars1, bars2]:
    for bar in bars:
        h = bar.get_height()
        va = 'bottom' if h >= 0 else 'top'
        offset = 0.15 if h >= 0 else -0.15
        ax.text(bar.get_x() + bar.get_width()/2., h + offset, f'{h:.1f}%',
                ha='center', va=va, fontsize=7)

ax.axhline(y=0, color='black', linewidth=0.5)
ax.set_xticks(x)
ax.set_xticklabels(bin_labels, fontsize=8)
ax.set_ylabel('Net attention effect (%)', fontsize=10)
ax.set_title('(C) Length-Stratified Net Effect (h6-1)', fontsize=11)
ax.legend(fontsize=9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

for i, n in enumerate(bin_n):
    ax.text(i, ax.get_ylim()[0] - 0.3, f'n={n}', ha='center', va='top', fontsize=7, color='gray')

plt.tight_layout()

for ext in ['png', 'pdf']:
    path = os.path.join(OUT_DIR, f'lambada_robustness_h6.{ext}')
    fig.savefig(path, dpi=200, bbox_inches='tight')
    print(f"  Saved: {path}")

plt.close()
print("\nDone.")

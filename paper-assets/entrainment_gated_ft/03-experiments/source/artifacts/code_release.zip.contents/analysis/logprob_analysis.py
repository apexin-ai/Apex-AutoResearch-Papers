import json
import os
import numpy as np
from collections import defaultdict

OUT_DIR = '/root/entrainment_gated_ft/analysis'
DATA_DIR = '/root/entrainment_gated_ft/lm_eval_clean'

MODELS = {
    'GDN-pure': '1.3B-100B-GatedDeltaNet-pure.json',
    'GDN-h12-1': '1.3B-100B-GatedDeltaNet-hybrid-12-1.json',
    'HGRN2-pure': '1.3B-100B-HGRN2-pure.json',
    'HGRN2-h3-1': '1.3B-100B-HGRN2-hybrid-3-1.json',
}

# Load per-example data
model_data = {}
for name, fn in MODELS.items():
    fp = os.path.join(DATA_DIR, fn)
    d = json.load(open(fp))
    samples = d['samples']['lambada_openai']
    # Sort by doc_id for alignment
    samples_sorted = sorted(samples, key=lambda x: x['doc_id'])
    model_data[name] = samples_sorted
    print(f"Loaded {name}: {len(samples_sorted)} samples")

n_samples = len(model_data['GDN-pure'])

# Verify alignment
for name, samples in model_data.items():
    assert len(samples) == n_samples, f"{name} has {len(samples)} samples, expected {n_samples}"
    for i, s in enumerate(samples):
        assert s['doc_id'] == model_data['GDN-pure'][i]['doc_id'], f"doc_id mismatch at {i}"
print(f"\nAll {n_samples} samples aligned across models.\n")

# Extract acc and logprob per model
acc = {}
logprob = {}
for name, samples in model_data.items():
    acc[name] = np.array([s['acc'] for s in samples])
    logprob[name] = np.array([s['perplexity'] for s in samples])

# Get text lengths (word count of context)
contexts = []
targets = []
for s in model_data['GDN-pure']:
    text = s['doc']['text']
    target = s['target'].strip()
    context = text[:text.rfind(target)] if target in text else text
    contexts.append(context)
    targets.append(target)

context_lengths = np.array([len(c.split()) for c in contexts])

print("=" * 70)
print("SECTION 1: Overall Accuracy")
print("=" * 70)
for name in MODELS:
    print(f"  {name:15s}: {acc[name].mean():.4f} ({acc[name].sum()}/{n_samples})")

# Attention effect analysis
print("\n" + "=" * 70)
print("SECTION 2: Attention Effect (hybrid vs pure)")
print("=" * 70)

pairs = [
    ('GDN', 'GDN-pure', 'GDN-h12-1'),
    ('HGRN2', 'HGRN2-pure', 'HGRN2-h3-1'),
]

for pair_name, pure, hybrid in pairs:
    helped = (acc[pure] == 0) & (acc[hybrid] == 1)
    hurt = (acc[pure] == 1) & (acc[hybrid] == 0)
    both_correct = (acc[pure] == 1) & (acc[hybrid] == 1)
    both_wrong = (acc[pure] == 0) & (acc[hybrid] == 0)
    
    print(f"\n  {pair_name} ({pure} -> {hybrid}):")
    print(f"    Both correct:     {both_correct.sum():5d} ({both_correct.mean()*100:.1f}%)")
    print(f"    Both wrong:       {both_wrong.sum():5d} ({both_wrong.mean()*100:.1f}%)")
    print(f"    Attention helped: {helped.sum():5d} ({helped.mean()*100:.1f}%)")
    print(f"    Attention hurt:   {hurt.sum():5d} ({hurt.mean()*100:.1f}%)")
    print(f"    Net effect:       {helped.sum() - hurt.sum():+5d} samples")

# Cross-model analysis
print("\n" + "=" * 70)
print("SECTION 3: Cross-model comparison")
print("=" * 70)

gdn_helped = (acc['GDN-pure'] == 0) & (acc['GDN-h12-1'] == 1)
gdn_hurt = (acc['GDN-pure'] == 1) & (acc['GDN-h12-1'] == 0)
hgrn_helped = (acc['HGRN2-pure'] == 0) & (acc['HGRN2-h3-1'] == 1)
hgrn_hurt = (acc['HGRN2-pure'] == 1) & (acc['HGRN2-h3-1'] == 0)

print(f"\n  Samples where GDN attention helped ({gdn_helped.sum()}):")
print(f"    HGRN2 also helped by attention: {(gdn_helped & hgrn_helped).sum()}")
print(f"    HGRN2 hurt by attention:        {(gdn_helped & hgrn_hurt).sum()}")
print(f"    HGRN2 unaffected (both right):  {(gdn_helped & (acc['HGRN2-pure']==1) & (acc['HGRN2-h3-1']==1)).sum()}")
print(f"    HGRN2 unaffected (both wrong):  {(gdn_helped & (acc['HGRN2-pure']==0) & (acc['HGRN2-h3-1']==0)).sum()}")

print(f"\n  Samples where GDN attention hurt ({gdn_hurt.sum()}):")
print(f"    HGRN2 also hurt by attention:   {(gdn_hurt & hgrn_hurt).sum()}")
print(f"    HGRN2 helped by attention:      {(gdn_hurt & hgrn_helped).sum()}")
print(f"    HGRN2 unaffected (both right):  {(gdn_hurt & (acc['HGRN2-pure']==1) & (acc['HGRN2-h3-1']==1)).sum()}")
print(f"    HGRN2 unaffected (both wrong):  {(gdn_hurt & (acc['HGRN2-pure']==0) & (acc['HGRN2-h3-1']==0)).sum()}")

# Overlap
print(f"\n  Overlap of attention-helped samples:")
overlap_helped = (gdn_helped & hgrn_helped).sum()
union_helped = (gdn_helped | hgrn_helped).sum()
print(f"    Jaccard: {overlap_helped}/{union_helped} = {overlap_helped/max(union_helped,1):.3f}")

overlap_hurt = (gdn_hurt & hgrn_hurt).sum()
union_hurt = (gdn_hurt | hgrn_hurt).sum()
print(f"  Overlap of attention-hurt samples:")
print(f"    Jaccard: {overlap_hurt}/{union_hurt} = {overlap_hurt/max(union_hurt,1):.3f}")

# Length-based analysis
print("\n" + "=" * 70)
print("SECTION 4: Analysis by context length")
print("=" * 70)

length_bins = [(0, 20, 'short (0-20)'), (20, 50, 'medium (20-50)'), (50, 100, 'long (50-100)'), (100, 9999, 'very long (100+)')]

for lo, hi, label in length_bins:
    mask = (context_lengths >= lo) & (context_lengths < hi)
    n = mask.sum()
    if n == 0:
        continue
    print(f"\n  {label}: {n} samples")
    for name in MODELS:
        print(f"    {name:15s}: acc={acc[name][mask].mean():.4f}")
    
    for pair_name, pure, hybrid in pairs:
        helped = ((acc[pure] == 0) & (acc[hybrid] == 1) & mask).sum()
        hurt = ((acc[pure] == 1) & (acc[hybrid] == 0) & mask).sum()
        print(f"    {pair_name} attn net: {helped-hurt:+d} (helped={helped}, hurt={hurt})")

# Logprob analysis
print("\n" + "=" * 70)
print("SECTION 5: Logprob shifts from attention")
print("=" * 70)

for pair_name, pure, hybrid in pairs:
    delta = logprob[hybrid] - logprob[pure]
    print(f"\n  {pair_name} logprob delta (hybrid - pure):")
    print(f"    Mean:   {delta.mean():.4f}")
    print(f"    Median: {np.median(delta):.4f}")
    print(f"    Std:    {delta.std():.4f}")
    
    # Breakdown by accuracy change
    helped = (acc[pure] == 0) & (acc[hybrid] == 1)
    hurt = (acc[pure] == 1) & (acc[hybrid] == 0)
    stable_right = (acc[pure] == 1) & (acc[hybrid] == 1)
    stable_wrong = (acc[pure] == 0) & (acc[hybrid] == 0)
    
    if helped.sum() > 0:
        print(f"    When helped:       mean delta={delta[helped].mean():.4f}")
    if hurt.sum() > 0:
        print(f"    When hurt:         mean delta={delta[hurt].mean():.4f}")
    if stable_right.sum() > 0:
        print(f"    When stable right: mean delta={delta[stable_right].mean():.4f}")
    if stable_wrong.sum() > 0:
        print(f"    When stable wrong: mean delta={delta[stable_wrong].mean():.4f}")

# Example samples where attention hurt
print("\n" + "=" * 70)
print("SECTION 6: Example samples where attention hurt (top 10 by logprob drop)")
print("=" * 70)

for pair_name, pure, hybrid in pairs:
    hurt_mask = (acc[pure] == 1) & (acc[hybrid] == 0)
    if hurt_mask.sum() == 0:
        print(f"\n  {pair_name}: no samples hurt by attention")
        continue
    
    delta = logprob[hybrid] - logprob[pure]
    hurt_indices = np.where(hurt_mask)[0]
    # Sort by largest logprob drop
    sorted_idx = hurt_indices[np.argsort(delta[hurt_indices])][:10]
    
    print(f"\n  {pair_name}: top 10 hurt samples (largest logprob drop)")
    for idx in sorted_idx:
        s = model_data[pure][idx]
        ctx = contexts[idx]
        tgt = targets[idx]
        # Show last 60 chars of context + target
        ctx_tail = ctx[-80:] if len(ctx) > 80 else ctx
        print(f"    doc_id={s['doc_id']:5d}  pure_lp={logprob[pure][idx]:.3f}  hybrid_lp={logprob[hybrid][idx]:.3f}  delta={delta[idx]:.3f}")
        print(f"      ...{ctx_tail} [{tgt}]")

print("\n" + "=" * 70)
print("SECTION 7: Summary statistics")
print("=" * 70)
print(f"\n  Total samples: {n_samples}")
print(f"  Context length: mean={context_lengths.mean():.1f}, median={np.median(context_lengths):.1f}, max={context_lengths.max()}")
print(f"\n  Note: GDN uses hybrid-12-1 (12 attn layers) since hybrid-3-1 lacks per-example data.")
print(f"  HGRN2 uses hybrid-3-1 (3 attn layers). Not directly comparable ratios.")

# Save CSV for further analysis
import csv
csv_path = os.path.join(OUT_DIR, 'lambada_per_example.csv')
with open(csv_path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['doc_id', 'context_length', 'target',
                 'gdn_pure_acc', 'gdn_pure_lp', 'gdn_h12_acc', 'gdn_h12_lp',
                 'hgrn2_pure_acc', 'hgrn2_pure_lp', 'hgrn2_h3_acc', 'hgrn2_h3_lp'])
    for i in range(n_samples):
        w.writerow([
            model_data['GDN-pure'][i]['doc_id'],
            context_lengths[i],
            targets[i],
            int(acc['GDN-pure'][i]), logprob['GDN-pure'][i],
            int(acc['GDN-h12-1'][i]), logprob['GDN-h12-1'][i],
            int(acc['HGRN2-pure'][i]), logprob['HGRN2-pure'][i],
            int(acc['HGRN2-h3-1'][i]), logprob['HGRN2-h3-1'][i],
        ])
print(f"\n  CSV saved to {csv_path}")
print("\nDone.")

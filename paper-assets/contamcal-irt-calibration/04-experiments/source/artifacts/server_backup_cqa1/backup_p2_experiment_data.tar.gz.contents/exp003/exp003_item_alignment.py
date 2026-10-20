import json
import os
import numpy as np
from collections import defaultdict

BASE = "/root/autodl-tmp/exp001/eval_results"

# Find all aligned/para_aligned pairs
dirs = os.listdir(BASE)
aligned_dirs = [d for d in dirs if d.endswith("_aligned") and not d.endswith("_para_aligned") and not "DEPRECATED" in d]

pairs = []
for a_dir in sorted(aligned_dirs):
    # Corresponding para_aligned
    pa_dir = a_dir.replace("_aligned", "_para_aligned")
    if pa_dir in dirs:
        a_path = os.path.join(BASE, a_dir, "correctness_matrix.json")
        pa_path = os.path.join(BASE, pa_dir, "correctness_matrix.json")
        if os.path.exists(a_path) and os.path.exists(pa_path):
            pairs.append((a_dir, pa_dir))

print(f"Found {len(pairs)} aligned/para_aligned pairs\n")
print("=" * 80)

all_gaps = []
all_item_gaps = defaultdict(list)  # item_idx -> list of gaps across models
pair_results = []

for a_dir, pa_dir in pairs:
    a_data = json.load(open(os.path.join(BASE, a_dir, "correctness_matrix.json")))
    pa_data = json.load(open(os.path.join(BASE, pa_dir, "correctness_matrix.json")))
    
    if "mmlu" not in a_data or "mmlu" not in pa_data:
        print(f"SKIP {a_dir}: no mmlu key")
        continue
    
    a_mmlu = np.array(a_data["mmlu"], dtype=float)
    pa_mmlu = np.array(pa_data["mmlu"], dtype=float)
    
    if len(a_mmlu) != len(pa_mmlu):
        print(f"SKIP {a_dir}: length mismatch aligned={len(a_mmlu)} para={len(pa_mmlu)}")
        continue
    
    n_items = len(a_mmlu)
    a_acc = a_mmlu.mean() * 100
    pa_acc = pa_mmlu.mean() * 100
    
    # Item-level: each item is 0 or 1, so "gap" for a single respondent is just agreement
    agree = (a_mmlu == pa_mmlu).mean() * 100
    disagree_items = (a_mmlu != pa_mmlu).sum()
    
    # Per-item gap (binary for single respondent)
    item_diffs = a_mmlu - pa_mmlu  # +1 = aligned correct, para wrong; -1 = opposite
    
    # Aggregate accuracy gap
    acc_gap = a_acc - pa_acc
    
    pair_results.append({
        "pair": a_dir.replace("_aligned", ""),
        "n_items": n_items,
        "aligned_acc": a_acc,
        "para_acc": pa_acc,
        "acc_gap_pp": acc_gap,
        "agreement_pct": agree,
        "disagree_count": int(disagree_items),
        "aligned_only_correct": int((item_diffs > 0).sum()),
        "para_only_correct": int((item_diffs < 0).sum()),
    })
    
    all_gaps.append(acc_gap)
    
    # Track per-item gaps
    for i, d in enumerate(item_diffs):
        all_item_gaps[i].append(d)

# Print per-pair results
print(f"\n{'Model':<45} {'N':>5} {'Alig%':>7} {'Para%':>7} {'Gap(pp)':>8} {'Agree%':>7} {'Dis':>5} {'A>P':>5} {'P>A':>5}")
print("-" * 105)
for r in pair_results:
    print(f"{r['pair']:<45} {r['n_items']:>5} {r['aligned_acc']:>7.2f} {r['para_acc']:>7.2f} {r['acc_gap_pp']:>+8.2f} {r['agreement_pct']:>7.1f} {r['disagree_count']:>5} {r['aligned_only_correct']:>5} {r['para_only_correct']:>5}")

# Aggregate stats
gaps = np.array(all_gaps)
print(f"\n{'=' * 80}")
print(f"AGGREGATE STATISTICS ({len(gaps)} pairs)")
print(f"  Mean accuracy gap (aligned - para): {gaps.mean():+.3f} pp")
print(f"  Std of accuracy gap:                {gaps.std():.3f} pp")
print(f"  Max |gap|:                          {np.abs(gaps).max():.3f} pp")
print(f"  Median gap:                         {np.median(gaps):+.3f} pp")
print(f"  Pairs with |gap| > 0.3pp:           {(np.abs(gaps) > 0.3).sum()}/{len(gaps)}")
print(f"  Pairs with |gap| > 0.5pp:           {(np.abs(gaps) > 0.5).sum()}/{len(gaps)}")
print(f"  Pairs with |gap| > 1.0pp:           {(np.abs(gaps) > 1.0).sum()}/{len(gaps)}")
print(f"  Pairs with |gap| > 5.0pp:           {(np.abs(gaps) > 5.0).sum()}/{len(gaps)}")

# Per-item analysis (across all pairs)
if all_item_gaps:
    max_items = max(all_item_gaps.keys()) + 1
    print(f"\nPER-ITEM ANALYSIS (across {len(gaps)} model pairs)")
    
    item_mean_gaps = []
    item_disagreement_rates = []
    for i in range(max_items):
        if i in all_item_gaps:
            diffs = np.array(all_item_gaps[i])
            mean_gap = diffs.mean()
            disagree_rate = (diffs != 0).mean() * 100
            item_mean_gaps.append(abs(mean_gap))
            item_disagreement_rates.append(disagree_rate)
    
    item_mean_gaps = np.array(item_mean_gaps)
    item_disagreement_rates = np.array(item_disagreement_rates)
    
    print(f"  Total items analyzed:               {len(item_mean_gaps)}")
    print(f"  Mean |item gap| across models:      {item_mean_gaps.mean():.4f}")
    print(f"  Mean item disagreement rate:        {item_disagreement_rates.mean():.1f}%")
    print(f"  Items with mean |gap| > 0.5:        {(item_mean_gaps > 0.5).sum()}/{len(item_mean_gaps)}")
    print(f"  Items with disagreement > 50%:      {(item_disagreement_rates > 50).sum()}/{len(item_disagreement_rates)}")
    
    # Top 20 most disagreed items
    top_disagree_idx = np.argsort(item_disagreement_rates)[::-1][:20]
    print(f"\n  Top 20 most-disagreed items:")
    print(f"  {'Item':>6} {'Disagree%':>10} {'MeanGap':>10} {'N_pairs':>8}")
    for idx in top_disagree_idx:
        diffs = np.array(all_item_gaps[idx])
        print(f"  {idx:>6} {item_disagreement_rates[idx]:>10.1f} {diffs.mean():>+10.4f} {len(diffs):>8}")

# By model size
print(f"\n{'=' * 80}")
print("BY MODEL SIZE:")
for size in ["0.5B", "1.5B", "3B"]:
    size_gaps = [r['acc_gap_pp'] for r in pair_results if size in r['pair']]
    if size_gaps:
        sg = np.array(size_gaps)
        print(f"  {size}: mean={sg.mean():+.3f}pp, std={sg.std():.3f}pp, n={len(sg)}")

# By contamination level
print(f"\nBY CONTAMINATION LEVEL:")
for dlevel in ["d000", "d005", "d025", "d100"]:
    level_gaps = [r['acc_gap_pp'] for r in pair_results if dlevel in r['pair']]
    if level_gaps:
        lg = np.array(level_gaps)
        print(f"  {dlevel}: mean={lg.mean():+.3f}pp, std={lg.std():.3f}pp, n={len(lg)}")


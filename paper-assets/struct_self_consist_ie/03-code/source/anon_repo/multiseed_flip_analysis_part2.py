import json
from collections import defaultdict

def load_data(path):
    data = []
    with open(path) as f:
        for line in f:
            data.append(json.loads(line))
    return data

def rel_set(annotation):
    rels = set()
    for r in annotation.get("relations", []):
        rels.add((r["head_start"], r["head_end"], r["tail_start"], r["tail_end"], r["type"]))
    return rels

def compute_re_f1(pred_annotation, gold_annotation):
    pred_rels = rel_set(pred_annotation)
    gold_rels = rel_set(gold_annotation)
    if len(gold_rels) == 0 and len(pred_rels) == 0:
        return 1.0
    if len(gold_rels) == 0 or len(pred_rels) == 0:
        return 0.0
    tp = len(pred_rels & gold_rels)
    p = tp / len(pred_rels)
    r = tp / len(gold_rels)
    if p + r == 0:
        return 0.0
    return 2 * p * r / (p + r)

def lp_select(samples):
    best_idx = max(range(len(samples)), key=lambda i: samples[i]["mean_logprob"])
    return best_idx, samples[best_idx]

BASE = "/root/autodl-tmp/struct_self_consist_ie"
constrained_paths = {
    "seed42": f"{BASE}/output/exp_012_rerun_1024/samples_with_logprobs.jsonl",
    "seed123": f"{BASE}/output/exp_018_qwen_scierc_seed123/samples.jsonl",
    "seed456": f"{BASE}/output/exp_018_qwen_scierc_seed456/samples.jsonl",
}
freeform_path = f"{BASE}/results/exp_freeform_ablation/samples.jsonl"

constrained_data = {k: load_data(v) for k, v in constrained_paths.items()}
freeform_data = load_data(freeform_path)
freeform_by_id = {d["id"]: d for d in freeform_data}

# Build per-instance records
seeds = ["seed42", "seed123", "seed456"]
records = {}  # id -> {...}

for inst in constrained_data["seed42"]:
    iid = inst["id"]
    gold = inst["gold"]
    n_gold_rels = len(gold.get("relations", []))
    n_gold_ents = len(gold.get("entities", []))
    
    rec = {"id": iid, "n_gold_rels": n_gold_rels, "n_gold_ents": n_gold_ents}
    
    for seed in seeds:
        sd = [d for d in constrained_data[seed] if d["id"] == iid][0]
        greedy_f1 = compute_re_f1(sd["greedy"], gold)
        lp_idx, lp_sample = lp_select(sd["samples"])
        lp_f1 = compute_re_f1(lp_sample, gold)
        n_greedy_rels = len(sd["greedy"].get("relations", []))
        n_lp_rels = len(lp_sample.get("relations", []))
        rec[f"{seed}_greedy_f1"] = greedy_f1
        rec[f"{seed}_lp_f1"] = lp_f1
        rec[f"{seed}_delta"] = lp_f1 - greedy_f1
        rec[f"{seed}_n_greedy_rels"] = n_greedy_rels
        rec[f"{seed}_n_lp_rels"] = n_lp_rels
        rec[f"{seed}_lp_idx"] = lp_idx
        rec[f"{seed}_lp_logprob"] = lp_sample["mean_logprob"]
        rec[f"{seed}_greedy_logprob"] = sd["greedy"]["mean_logprob"]
    
    # Free-form
    ff = freeform_by_id[iid]
    ff_greedy_f1 = compute_re_f1(ff["greedy"], gold)
    ff_lp_idx, ff_lp = lp_select(ff["samples"])
    ff_lp_f1 = compute_re_f1(ff_lp, gold)
    rec["ff_greedy_f1"] = ff_greedy_f1
    rec["ff_lp_f1"] = ff_lp_f1
    rec["ff_delta"] = ff_lp_f1 - ff_greedy_f1
    
    records[iid] = rec

# ── Analysis: 0-gold-rel stable failures ──
print("="*70)
print("0-GOLD-REL ANALYSIS")
print("="*70)
zero_rel_ids = {iid for iid, r in records.items() if r["n_gold_rels"] == 0}
print(f"Total 0-gold-rel instances: {len(zero_rel_ids)}")

# How many are failures in each seed?
for seed in seeds:
    fails = {iid for iid in zero_rel_ids if records[iid][f"{seed}_delta"] < -1e-9}
    print(f"  {seed} failures (0-rel): {len(fails)}")

# Stable failures among 0-rel
stable_fail_0rel = {iid for iid in zero_rel_ids 
                    if all(records[iid][f"{s}_delta"] < -1e-9 for s in seeds)}
print(f"  Stable failures (0-rel): {len(stable_fail_0rel)}")

# For these, what does LP pick? (all greedy should be empty → F1=1.0)
for iid in sorted(list(stable_fail_0rel))[:5]:
    r = records[iid]
    print(f"    {iid}: greedy_rels=({r['seed42_n_greedy_rels']},{r['seed123_n_greedy_rels']},{r['seed456_n_greedy_rels']}), "
          f"lp_rels=({r['seed42_n_lp_rels']},{r['seed123_n_lp_rels']},{r['seed456_n_lp_rels']})")

# ── Excluding 0-gold-rel: detailed Jaccard ──
print()
print("="*70)
print("EXCLUDING 0-GOLD-REL: Detailed Analysis")
print("="*70)
has_rels = {iid for iid, r in records.items() if r["n_gold_rels"] > 0}

for seed in seeds:
    fails = {iid for iid in has_rels if records[iid][f"{seed}_delta"] < -1e-9}
    better = {iid for iid in has_rels if records[iid][f"{seed}_delta"] > 1e-9}
    equal = has_rels - fails - better
    print(f"{seed}: fail={len(fails)}, better={len(better)}, equal={len(equal)}")

# F1 delta distribution for failures
print()
print("F1 delta distribution (constrained, has rels, seed42):")
deltas = [records[iid]["seed42_delta"] for iid in has_rels if records[iid]["seed42_delta"] < -1e-9]
deltas.sort()
print(f"  N={len(deltas)}, median={deltas[len(deltas)//2]:.4f}, mean={sum(deltas)/len(deltas):.4f}")
print(f"  min={deltas[0]:.4f}, max={deltas[-1]:.4f}")
# Histogram buckets
buckets = [0]*6
for d in deltas:
    if d >= -0.1: buckets[0] += 1
    elif d >= -0.2: buckets[1] += 1
    elif d >= -0.3: buckets[2] += 1
    elif d >= -0.5: buckets[3] += 1
    elif d >= -0.8: buckets[4] += 1
    else: buckets[5] += 1
labels = ["(-0.1,0)", "(-0.2,-0.1)", "(-0.3,-0.2)", "(-0.5,-0.3)", "(-0.8,-0.5)", "(-1.0,-0.8)"]
for l, b in zip(labels, buckets):
    print(f"    {l}: {b}")

# ── Correlation: gold_rels vs failure probability ──
print()
print("="*70)
print("GOLD REL COUNT vs FAILURE RATE (constrained, excl 0-rel)")
print("="*70)
from collections import Counter
rel_count_dist = Counter(records[iid]["n_gold_rels"] for iid in has_rels)
for n_rel in sorted(rel_count_dist.keys()):
    pool = {iid for iid in has_rels if records[iid]["n_gold_rels"] == n_rel}
    # Average across 3 seeds
    fail_rates = []
    for seed in seeds:
        fails = {iid for iid in pool if records[iid][f"{seed}_delta"] < -1e-9}
        fail_rates.append(len(fails) / len(pool))
    avg_rate = sum(fail_rates) / 3
    print(f"  {n_rel} gold rels: N={len(pool)}, avg_failure_rate={avg_rate:.3f}")

# ── LP logprob gap: when LP fails, is it because logprob gap is small? ──
print()
print("="*70)
print("LP LOGPROB GAP ANALYSIS (seed42, excl 0-rel)")
print("="*70)
# For each instance, compute logprob gap = lp_logprob - greedy_logprob
fail_gaps = []
success_gaps = []
for iid in has_rels:
    gap = records[iid]["seed42_lp_logprob"] - records[iid]["seed42_greedy_logprob"]
    if records[iid]["seed42_delta"] < -1e-9:
        fail_gaps.append(gap)
    elif records[iid]["seed42_delta"] > 1e-9:
        success_gaps.append(gap)
        
def stats(lst, name):
    if not lst:
        return
    lst.sort()
    print(f"  {name}: N={len(lst)}, median={lst[len(lst)//2]:.4f}, mean={sum(lst)/len(lst):.4f}, "
          f"min={lst[0]:.4f}, max={lst[-1]:.4f}")
        
stats(fail_gaps, "LP failure (lp_logprob - greedy_logprob)")
stats(success_gaps, "LP success (lp_logprob - greedy_logprob)")

# ── Constrained vs free-form delta correlation (seed42) ──
print()
print("="*70)
print("CONSTRAINED vs FREE-FORM DELTA CORRELATION (seed42, has rels)")
print("="*70)
c_deltas = [records[iid]["seed42_delta"] for iid in sorted(has_rels)]
ff_deltas = [records[iid]["ff_delta"] for iid in sorted(has_rels)]
# Pearson correlation
n = len(c_deltas)
mean_c = sum(c_deltas) / n
mean_ff = sum(ff_deltas) / n
cov = sum((c - mean_c) * (f - mean_ff) for c, f in zip(c_deltas, ff_deltas)) / n
std_c = (sum((c - mean_c)**2 for c in c_deltas) / n) ** 0.5
std_ff = (sum((f - mean_ff)**2 for f in ff_deltas) / n) ** 0.5
pearson = cov / (std_c * std_ff) if std_c * std_ff > 0 else 0
print(f"Pearson correlation of LP delta (constrained vs free-form): {pearson:.4f}")

# Quadrant analysis
q_both_fail = 0
q_both_better = 0
q_c_fail_ff_better = 0  # flip
q_c_better_ff_fail = 0  # reverse flip
q_other = 0
for iid in has_rels:
    cd = records[iid]["seed42_delta"]
    fd = records[iid]["ff_delta"]
    if cd < -1e-9 and fd < -1e-9:
        q_both_fail += 1
    elif cd > 1e-9 and fd > 1e-9:
        q_both_better += 1
    elif cd < -1e-9 and fd > 1e-9:
        q_c_fail_ff_better += 1
    elif cd > 1e-9 and fd < -1e-9:
        q_c_better_ff_fail += 1
    else:
        q_other += 1

print(f"\nQuadrant analysis (has rels, seed42):")
print(f"  Both fail:    {q_both_fail}")
print(f"  Both better:  {q_both_better}")
print(f"  Flip (C-fail, FF-better): {q_c_fail_ff_better}")
print(f"  Reverse (C-better, FF-fail): {q_c_better_ff_fail}")
print(f"  One/both neutral: {q_other}")

# Among those with rels, how many flip instances?
flip_rels = {iid for iid in has_rels if records[iid]["seed42_delta"] < -1e-9 and records[iid]["ff_delta"] > 1e-9}
print(f"\nFlip instances (has rels): {len(flip_rels)}")
for iid in sorted(flip_rels):
    r = records[iid]
    print(f"  {iid}: gold_rels={r['n_gold_rels']}, "
          f"C(g={r['seed42_greedy_f1']:.3f}, lp={r['seed42_lp_f1']:.3f}), "
          f"FF(g={r['ff_greedy_f1']:.3f}, lp={r['ff_lp_f1']:.3f})")


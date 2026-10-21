import json
import sys
from collections import defaultdict

def load_data(path):
    data = []
    with open(path) as f:
        for line in f:
            data.append(json.loads(line))
    return data

def rel_set(annotation):
    """Extract relation set as frozenset of tuples for matching."""
    rels = set()
    for r in annotation.get("relations", []):
        rels.add((r["head_start"], r["head_end"], r["tail_start"], r["tail_end"], r["type"]))
    return rels

def compute_re_f1(pred_annotation, gold_annotation):
    """Compute instance-level RE F1."""
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
    """Select sample with highest mean_logprob."""
    best_idx = max(range(len(samples)), key=lambda i: samples[i]["mean_logprob"])
    return best_idx, samples[best_idx]

def jaccard(set_a, set_b):
    if len(set_a) == 0 and len(set_b) == 0:
        return 1.0
    if len(set_a | set_b) == 0:
        return 0.0
    return len(set_a & set_b) / len(set_a | set_b)

# ── Load data ──
BASE = "/root/autodl-tmp/struct_self_consist_ie"
constrained_paths = {
    "seed42": f"{BASE}/output/exp_012_rerun_1024/samples_with_logprobs.jsonl",
    "seed123": f"{BASE}/output/exp_018_qwen_scierc_seed123/samples.jsonl",
    "seed456": f"{BASE}/output/exp_018_qwen_scierc_seed456/samples.jsonl",
}
freeform_paths = {
    "seed42": f"{BASE}/results/exp_freeform_ablation/samples.jsonl",
}

constrained_data = {k: load_data(v) for k, v in constrained_paths.items()}
freeform_data = {k: load_data(v) for k, v in freeform_paths.items()}

# Verify ID alignment
ids_42 = [d["id"] for d in constrained_data["seed42"]]
for seed in ["seed123", "seed456"]:
    ids_s = [d["id"] for d in constrained_data[seed]]
    assert ids_42 == ids_s, f"ID mismatch between seed42 and {seed}"
ids_ff = [d["id"] for d in freeform_data["seed42"]]
assert ids_42 == ids_ff, "ID mismatch between constrained and freeform seed42"

print(f"Total instances: {len(ids_42)}")
print()

# ── Per-seed analysis ──
# For each seed: identify LP selection failure instances
failure_sets = {}  # seed -> set of instance IDs where LP F1 < greedy F1
lp_better_sets = {}  # seed -> set of instance IDs where LP F1 > greedy F1
lp_equal_sets = {}  # seed -> set of instance IDs where LP F1 == greedy F1

# Store per-instance details for later analysis
instance_details = defaultdict(dict)  # id -> seed -> {greedy_f1, lp_f1, lp_idx, ...}

for seed, data in constrained_data.items():
    failures = set()
    lp_better = set()
    lp_equal = set()
    for inst in data:
        iid = inst["id"]
        gold = inst["gold"]
        greedy_f1 = compute_re_f1(inst["greedy"], gold)
        lp_idx, lp_sample = lp_select(inst["samples"])
        lp_f1 = compute_re_f1(lp_sample, gold)
        
        instance_details[iid][seed] = {
            "greedy_f1": greedy_f1,
            "lp_f1": lp_f1,
            "lp_idx": lp_idx,
            "n_gold_rels": len(gold.get("relations", [])),
            "n_gold_ents": len(gold.get("entities", [])),
            "n_samples": len(inst["samples"]),
        }
        
        if lp_f1 < greedy_f1 - 1e-9:
            failures.add(iid)
        elif lp_f1 > greedy_f1 + 1e-9:
            lp_better.add(iid)
        else:
            lp_equal.add(iid)
    
    failure_sets[seed] = failures
    lp_better_sets[seed] = lp_better
    lp_equal_sets[seed] = lp_equal

# ── Print per-seed summary ──
print("="*70)
print("CONSTRAINED: Per-seed LP Selection Summary")
print("="*70)
seeds = ["seed42", "seed123", "seed456"]
for seed in seeds:
    f = failure_sets[seed]
    b = lp_better_sets[seed]
    e = lp_equal_sets[seed]
    print(f"{seed}: failure={len(f)}, LP_better={len(b)}, equal={len(e)}, total={len(f)+len(b)+len(e)}")
print()

# ── Pairwise Jaccard for failure sets ──
print("="*70)
print("CONSTRAINED: Pairwise Jaccard Similarity of LP Failure Sets")
print("="*70)
for i, s1 in enumerate(seeds):
    for j, s2 in enumerate(seeds):
        if j > i:
            j_sim = jaccard(failure_sets[s1], failure_sets[s2])
            inter = failure_sets[s1] & failure_sets[s2]
            union = failure_sets[s1] | failure_sets[s2]
            print(f"  {s1} vs {s2}: Jaccard={j_sim:.4f} (|inter|={len(inter)}, |union|={len(union)})")

# All-three overlap
all_three_failures = failure_sets["seed42"] & failure_sets["seed123"] & failure_sets["seed456"]
any_failure = failure_sets["seed42"] | failure_sets["seed123"] | failure_sets["seed456"]
print(f"\n  All-three intersection: {len(all_three_failures)} instances")
print(f"  Any-seed union: {len(any_failure)} instances")
if len(any_failure) > 0:
    print(f"  3-way overlap ratio: {len(all_three_failures)/len(any_failure):.4f}")
print()

# ── Free-form seed42 analysis ──
print("="*70)
print("FREE-FORM seed42: LP Selection Analysis")
print("="*70)
ff_failures = set()
ff_lp_better = set()
ff_equal = set()
ff_details = {}

for inst in freeform_data["seed42"]:
    iid = inst["id"]
    gold = inst["gold"]
    greedy_f1 = compute_re_f1(inst["greedy"], gold)
    lp_idx, lp_sample = lp_select(inst["samples"])
    lp_f1 = compute_re_f1(lp_sample, gold)
    
    ff_details[iid] = {
        "greedy_f1": greedy_f1,
        "lp_f1": lp_f1,
        "lp_idx": lp_idx,
        "n_gold_rels": len(gold.get("relations", [])),
        "n_gold_ents": len(gold.get("entities", [])),
    }
    
    if lp_f1 < greedy_f1 - 1e-9:
        ff_failures.add(iid)
    elif lp_f1 > greedy_f1 + 1e-9:
        ff_lp_better.add(iid)
    else:
        ff_equal.add(iid)

print(f"Free-form seed42: failure={len(ff_failures)}, LP_better={len(ff_lp_better)}, equal={len(ff_equal)}")
print()

# ── Flip instances (seed42 only) ──
print("="*70)
print("FLIP INSTANCES (seed42): constrained LP failure + free-form LP success")
print("="*70)
constrained_failures_42 = failure_sets["seed42"]
flip_instances = constrained_failures_42 & ff_lp_better
print(f"Constrained failures (seed42): {len(constrained_failures_42)}")
print(f"Free-form LP better (seed42): {len(ff_lp_better)}")
print(f"Flip instances: {len(flip_instances)}")
print()

# ── Check flip instances vs stable failures ──
print("="*70)
print("FLIP vs STABLE FAILURE OVERLAP")
print("="*70)
# Stable failures = failures in all 3 seeds
stable_failures = all_three_failures
flip_in_stable = flip_instances & stable_failures
print(f"Stable failures (all 3 seeds): {len(stable_failures)}")
print(f"Flip instances (seed42): {len(flip_instances)}")
print(f"Flip ∩ Stable failure: {len(flip_in_stable)}")
if len(flip_instances) > 0:
    print(f"  % of flips that are stable failures: {len(flip_in_stable)/len(flip_instances)*100:.1f}%")
if len(stable_failures) > 0:
    print(f"  % of stable failures that flip: {len(flip_in_stable)/len(stable_failures)*100:.1f}%")
print()

# ── At-least-2-seed failures ──
two_seed_failures = set()
for iid in any_failure:
    count = sum(1 for s in seeds if iid in failure_sets[s])
    if count >= 2:
        two_seed_failures.add(iid)

print(f"≥2-seed failures: {len(two_seed_failures)}")
flip_in_two = flip_instances & two_seed_failures
print(f"Flip ∩ ≥2-seed failure: {len(flip_in_two)}")
if len(flip_instances) > 0:
    print(f"  % of flips that are ≥2-seed failures: {len(flip_in_two)/len(flip_instances)*100:.1f}%")
print()

# ── Instance characteristic analysis ──
print("="*70)
print("INSTANCE CHARACTERISTICS")
print("="*70)

def avg(lst):
    return sum(lst) / len(lst) if lst else 0

# Compare stable failures vs non-failures
all_ids = set(ids_42)
never_fail = all_ids - any_failure

groups = {
    "stable_fail_3": stable_failures,
    "fail_2+": two_seed_failures - stable_failures,
    "fail_1_only": any_failure - two_seed_failures,
    "never_fail": never_fail,
}

if len(flip_instances) > 0:
    groups["flip_instances"] = flip_instances

for gname, gids in groups.items():
    if len(gids) == 0:
        continue
    gold_rels = [instance_details[iid]["seed42"]["n_gold_rels"] for iid in gids]
    gold_ents = [instance_details[iid]["seed42"]["n_gold_ents"] for iid in gids]
    greedy_f1s = [instance_details[iid]["seed42"]["greedy_f1"] for iid in gids]
    lp_f1s = [instance_details[iid]["seed42"]["lp_f1"] for iid in gids]
    # For flip instances, also show free-form stats
    if gname == "flip_instances":
        ff_greedy_f1s = [ff_details[iid]["greedy_f1"] for iid in gids]
        ff_lp_f1s = [ff_details[iid]["lp_f1"] for iid in gids]
        print(f"\n{gname} (N={len(gids)}):")
        print(f"  gold_rels: {avg(gold_rels):.2f}, gold_ents: {avg(gold_ents):.2f}")
        print(f"  constrained: greedy_f1={avg(greedy_f1s):.4f}, lp_f1={avg(lp_f1s):.4f}, delta={avg(lp_f1s)-avg(greedy_f1s):.4f}")
        print(f"  free-form:   greedy_f1={avg(ff_greedy_f1s):.4f}, lp_f1={avg(ff_lp_f1s):.4f}, delta={avg(ff_lp_f1s)-avg(ff_greedy_f1s):.4f}")
    else:
        print(f"\n{gname} (N={len(gids)}):")
        print(f"  gold_rels: {avg(gold_rels):.2f}, gold_ents: {avg(gold_ents):.2f}")
        print(f"  constrained: greedy_f1={avg(greedy_f1s):.4f}, lp_f1={avg(lp_f1s):.4f}, delta={avg(lp_f1s)-avg(greedy_f1s):.4f}")

# ── Cross-seed LP index agreement ──
print()
print("="*70)
print("LP SELECTION INDEX AGREEMENT ACROSS SEEDS")
print("="*70)
agree_all3 = 0
agree_any2 = 0
total = len(ids_42)
for iid in ids_42:
    idxs = [instance_details[iid][s]["lp_idx"] for s in seeds]
    if idxs[0] == idxs[1] == idxs[2]:
        agree_all3 += 1
    if idxs[0] == idxs[1] or idxs[0] == idxs[2] or idxs[1] == idxs[2]:
        agree_any2 += 1
print(f"All 3 seeds pick same sample index: {agree_all3}/{total} ({agree_all3/total*100:.1f}%)")
print(f"At least 2 seeds pick same sample index: {agree_any2}/{total} ({agree_any2/total*100:.1f}%)")
print()

# ── Detailed flip instance list ──
print("="*70)
print("FLIP INSTANCE DETAILS")
print("="*70)
if flip_instances:
    for iid in sorted(flip_instances):
        c = instance_details[iid]["seed42"]
        f = ff_details[iid]
        stable = "STABLE" if iid in stable_failures else ("2+SEED" if iid in two_seed_failures else "1SEED")
        print(f"  {iid}: gold_rels={c['n_gold_rels']}, "
              f"C(greedy={c['greedy_f1']:.3f}, lp={c['lp_f1']:.3f}), "
              f"FF(greedy={f['greedy_f1']:.3f}, lp={f['lp_f1']:.3f}), {stable}")
else:
    print("  No flip instances found.")

# ── Detailed stable failure instance list ──
print()
print("="*70)
print("STABLE FAILURE INSTANCE DETAILS (top 20)")
print("="*70)
stable_sorted = sorted(stable_failures, key=lambda iid: instance_details[iid]["seed42"]["greedy_f1"] - instance_details[iid]["seed42"]["lp_f1"], reverse=True)
for iid in stable_sorted[:20]:
    c42 = instance_details[iid]["seed42"]
    c123 = instance_details[iid]["seed123"]
    c456 = instance_details[iid]["seed456"]
    is_flip = "FLIP" if iid in flip_instances else ""
    print(f"  {iid}: gold_rels={c42['n_gold_rels']}, "
          f"s42(g={c42['greedy_f1']:.3f},lp={c42['lp_f1']:.3f}), "
          f"s123(g={c123['greedy_f1']:.3f},lp={c123['lp_f1']:.3f}), "
          f"s456(g={c456['greedy_f1']:.3f},lp={c456['lp_f1']:.3f}) {is_flip}")

# ── Reverse flip: constrained LP better, free-form LP worse ──
print()
print("="*70)
print("REVERSE FLIP: constrained LP better + free-form LP failure")
print("="*70)
reverse_flips = lp_better_sets["seed42"] & ff_failures
print(f"Constrained LP better (seed42): {len(lp_better_sets['seed42'])}")
print(f"Free-form LP failures (seed42): {len(ff_failures)}")
print(f"Reverse flip instances: {len(reverse_flips)}")
print()

# ── Summary stats ──
print("="*70)
print("SUMMARY FOR PAPER")
print("="*70)
j_vals = []
for i, s1 in enumerate(seeds):
    for j, s2 in enumerate(seeds):
        if j > i:
            j_vals.append(jaccard(failure_sets[s1], failure_sets[s2]))
avg_jaccard = avg(j_vals)
print(f"Average pairwise Jaccard of constrained LP failures: {avg_jaccard:.4f}")
print(f"3-way stable failures: {len(stable_failures)}/{len(any_failure)} ({len(stable_failures)/max(len(any_failure),1)*100:.1f}% of any-fail)")
print(f"Flip instances (seed42): {len(flip_instances)}")
print(f"Reverse flips (seed42): {len(reverse_flips)}")
print(f"LP index agreement (all 3): {agree_all3/total*100:.1f}%")

# ── Instances where greedy F1 = 0 for all seeds (no gold rels) ──
no_gold_rels = sum(1 for iid in ids_42 if instance_details[iid]["seed42"]["n_gold_rels"] == 0)
print(f"\nInstances with 0 gold relations: {no_gold_rels}")

# Filter to instances with gold rels > 0
has_rels = {iid for iid in ids_42 if instance_details[iid]["seed42"]["n_gold_rels"] > 0}
print(f"Instances with ≥1 gold relation: {len(has_rels)}")

# Redo failure analysis restricted to instances with gold rels
for seed in seeds:
    restricted = failure_sets[seed] & has_rels
    print(f"  {seed} failures (with rels): {len(restricted)}")

restricted_stable = stable_failures & has_rels
restricted_any = any_failure & has_rels
print(f"  Stable failures (with rels): {len(restricted_stable)}")
print(f"  Any-fail (with rels): {len(restricted_any)}")

# Jaccard restricted
print("\n  Pairwise Jaccard (restricted to instances with gold rels):")
j_vals_r = []
for i, s1 in enumerate(seeds):
    for j, s2 in enumerate(seeds):
        if j > i:
            fs1 = failure_sets[s1] & has_rels
            fs2 = failure_sets[s2] & has_rels
            j_sim = jaccard(fs1, fs2)
            j_vals_r.append(j_sim)
            print(f"    {s1} vs {s2}: Jaccard={j_sim:.4f}")
print(f"  Average Jaccard (restricted): {avg(j_vals_r):.4f}")


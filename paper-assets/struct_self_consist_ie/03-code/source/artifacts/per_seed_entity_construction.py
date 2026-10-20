import json, math, numpy as np
from collections import defaultdict

SEEDS = [42, 123, 456, 2024, 3141]
BASE = "/root/autodl-tmp/struct_self_consist_ie/output"
THETA = 0.25  # 2/N where N=8

def entity_set(entities):
    return {(e["start"], e["end"], e["type"]) for e in entities}

def compute_f1(pred_set, gold_set):
    if not gold_set and not pred_set:
        return 1.0
    if not pred_set or not gold_set:
        return 0.0
    tp = len(pred_set & gold_set)
    if tp == 0:
        return 0.0
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    return 2 * p * r / (p + r)

def get_lp_weights(inst):
    samples = inst["samples"]
    logprobs = inst.get("logprobs", None)
    lps = []
    for i, s in enumerate(samples):
        lp = s.get("mean_logprob", None)
        if lp is None and logprobs is not None and i < len(logprobs):
            lp = logprobs[i]
        if lp is None or not math.isfinite(lp):
            lp = -100.0
        lps.append(lp)
    max_lp = max(lps)
    ws = [math.exp(lp - max_lp) for lp in lps]
    total = sum(ws)
    return [w / total for w in ws]

def entity_construction_lp(inst, theta):
    samples = inst["samples"]
    weights = get_lp_weights(inst)
    entity_counts = defaultdict(float)
    for i, s in enumerate(samples):
        for e in s.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            entity_counts[key] += weights[i]
    total_w = sum(weights)
    return {k for k, v in entity_counts.items() if v / total_w >= theta}

def bootstrap_test(f1_method, f1_baseline, B=10000, seed=42):
    rng = np.random.RandomState(seed)
    n = len(f1_method)
    diffs = f1_method - f1_baseline
    observed = diffs.mean()
    boot = np.array([diffs[rng.randint(0, n, n)].mean() for _ in range(B)])
    ci_lo = float(np.percentile(boot, 2.5))
    ci_hi = float(np.percentile(boot, 97.5))
    p = float((boot <= 0).mean())
    return observed, (ci_lo, ci_hi), p

print("=" * 80)
print("SciERC 5-seed Entity Construction Analysis")
print(f"Method: LP-weighted construction, theta=2/N={THETA}")
print("=" * 80)

all_deltas = []
all_greedy_f1s = []
all_constr_f1s = []
per_seed_greedy_arrays = {}
per_seed_constr_arrays = {}

for seed in SEEDS:
    path = f"{BASE}/scierc_mf4v2_seed{seed}/samples.jsonl"
    data = []
    with open(path) as f:
        for line in f:
            if line.strip():
                obj = json.loads(line)
                if obj["gold"].get("entities", []):
                    data.append(obj)

    greedy_f1s = []
    constr_f1s = []
    for inst in data:
        gold = entity_set(inst["gold"]["entities"])
        greedy = inst.get("greedy", inst["samples"][0])
        greedy_pred = entity_set(greedy.get("entities", []))
        greedy_f1s.append(compute_f1(greedy_pred, gold))
        constr_pred = entity_construction_lp(inst, THETA)
        constr_f1s.append(compute_f1(constr_pred, gold))

    greedy_arr = np.array(greedy_f1s)
    constr_arr = np.array(constr_f1s)
    per_seed_greedy_arrays[seed] = greedy_arr
    per_seed_constr_arrays[seed] = constr_arr

    g_mean = greedy_arr.mean()
    c_mean = constr_arr.mean()
    delta = (c_mean - g_mean) * 100

    diff, ci, pval = bootstrap_test(constr_arr, greedy_arr)
    sign = "+" if delta > 0 else "-"

    all_deltas.append(delta)
    all_greedy_f1s.append(g_mean)
    all_constr_f1s.append(c_mean)

    print(f"\nSeed {seed}: N_instances={len(data)}")
    print(f"  Greedy F1:       {g_mean*100:.2f}%")
    print(f"  Construction F1: {c_mean*100:.2f}%")
    print(f"  Delta:           {delta:+.2f}pp  [{sign}]")
    print(f"  Bootstrap:       diff={diff*100:+.2f}pp, 95%CI=[{ci[0]*100:+.2f}, {ci[1]*100:+.2f}], p={pval:.4f}")

# Aggregate
print("\n" + "=" * 80)
print("AGGREGATE")
print("=" * 80)
deltas = np.array(all_deltas)
n_pos = int((deltas > 0).sum())
n_neg = int((deltas < 0).sum())
n_zero = int((deltas == 0).sum())
print(f"Mean Delta:     {deltas.mean():+.2f}pp")
print(f"Std Delta:      {deltas.std():.2f}pp")
print(f"Min/Max Delta:  {deltas.min():+.2f} / {deltas.max():+.2f}pp")
print(f"Direction:      {n_pos} positive / {n_neg} negative / {n_zero} zero")
if n_pos == 5:
    stability = "STABLE POSITIVE (5/5)"
elif n_pos >= 4:
    stability = "MOSTLY POSITIVE (4/5)"
elif n_pos >= 3:
    stability = "MIXED (3/5)"
elif n_pos >= 2:
    stability = "MOSTLY NEGATIVE (2/5)"
else:
    stability = "STABLE NEGATIVE"
print(f"Stability:      {stability}")

# Pooled bootstrap across all seeds
print("\n--- Pooled bootstrap (all seeds combined) ---")
pooled_greedy = np.concatenate(list(per_seed_greedy_arrays.values()))
pooled_constr = np.concatenate(list(per_seed_constr_arrays.values()))
diff, ci, pval = bootstrap_test(pooled_constr, pooled_greedy)
print(f"Pooled diff:    {diff*100:+.2f}pp")
print(f"Pooled 95%CI:   [{ci[0]*100:+.2f}, {ci[1]*100:+.2f}]")
print(f"Pooled p-value: {pval:.4f}")
print(f"Significant:    {'YES' if pval < 0.05 else 'NO'}")

print(f"\nMean of seed-level greedy F1:  {np.mean(all_greedy_f1s)*100:.2f}%")
print(f"Mean of seed-level constr F1: {np.mean(all_constr_f1s)*100:.2f}%")
print(f"Mean of seed-level deltas:    {deltas.mean():+.2f}pp")

# Markdown table
print("\n\n--- MARKDOWN TABLE ---")
print("| Seed | Greedy F1 | Construction F1 | Delta (pp) | Sign | p-value |")
print("|------|-----------|-----------------|------------|------|---------|")
for i, seed in enumerate(SEEDS):
    g = all_greedy_f1s[i]*100
    c = all_constr_f1s[i]*100
    d = all_deltas[i]
    sign = "+" if d > 0 else "-"
    diff, ci, pval = bootstrap_test(per_seed_constr_arrays[seed], per_seed_greedy_arrays[seed])
    sig = "*" if pval < 0.05 else ""
    print(f"| {seed:<4} | {g:.2f}     | {c:.2f}           | {d:+.2f}      | {sign}    | {pval:.4f}{sig} |")

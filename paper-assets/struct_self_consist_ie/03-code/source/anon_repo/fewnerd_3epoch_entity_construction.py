import json, math, sys
import numpy as np
from collections import defaultdict

SEEDS = [42, 456]
BASE = "/root/autodl-tmp/struct_self_consist_ie/output"
PATHS = {
    42: f"{BASE}/fewnerd_mf4v2_seed42/samples.jsonl",
    456: f"{BASE}/fewnerd_mf4v2_seed456/samples.jsonl",
}
THETA = 0.25

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

def entity_construction_mv(inst, theta):
    samples = inst["samples"]
    N = len(samples)
    entity_counts = defaultdict(int)
    for s in samples:
        for e in s.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            entity_counts[key] += 1
    return {k for k, v in entity_counts.items() if v / N >= theta}

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

per_seed_greedy = {}
per_seed_mv = {}
per_seed_lp = {}
per_seed_stats = {}

for seed in SEEDS:
    path = PATHS[seed]
    data = []
    with open(path) as f:
        for line in f:
            if line.strip():
                obj = json.loads(line)
                if obj["gold"].get("entities", []):
                    data.append(obj)

    greedy_f1s, mv_f1s, lp_f1s = [], [], []
    for inst in data:
        gold = entity_set(inst["gold"]["entities"])
        greedy = inst.get("greedy", inst["samples"][0])
        greedy_pred = entity_set(greedy.get("entities", []))
        greedy_f1s.append(compute_f1(greedy_pred, gold))
        mv_pred = entity_construction_mv(inst, THETA)
        mv_f1s.append(compute_f1(mv_pred, gold))
        lp_pred = entity_construction_lp(inst, THETA)
        lp_f1s.append(compute_f1(lp_pred, gold))

    g_arr = np.array(greedy_f1s)
    mv_arr = np.array(mv_f1s)
    lp_arr = np.array(lp_f1s)
    per_seed_greedy[seed] = g_arr
    per_seed_mv[seed] = mv_arr
    per_seed_lp[seed] = lp_arr

    g_m = g_arr.mean() * 100
    mv_m = mv_arr.mean() * 100
    lp_m = lp_arr.mean() * 100
    mv_d = mv_m - g_m
    lp_d = lp_m - g_m

    _, _, mv_p = bootstrap_test(mv_arr, g_arr)
    _, _, lp_p = bootstrap_test(lp_arr, g_arr)

    per_seed_stats[seed] = {
        "n": len(data), "greedy": g_m,
        "mv": mv_m, "lp": lp_m,
        "mv_delta": mv_d, "lp_delta": lp_d,
        "mv_p": mv_p, "lp_p": lp_p,
    }
    print(f"Seed {seed}: N={len(data)}, Greedy={g_m:.2f}, MV={mv_m:.2f} ({mv_d:+.2f}pp, p={mv_p:.4f}), LP={lp_m:.2f} ({lp_d:+.2f}pp, p={lp_p:.4f})")

print("\n--- Aggregate (2-seed) ---")
greedy_means = [per_seed_stats[s]["greedy"] for s in SEEDS]
mv_deltas = [per_seed_stats[s]["mv_delta"] for s in SEEDS]
lp_deltas = [per_seed_stats[s]["lp_delta"] for s in SEEDS]
print(f"Greedy mean: {np.mean(greedy_means):.2f} +/- {np.std(greedy_means):.2f}")
print(f"MV delta mean: {np.mean(mv_deltas):+.2f} +/- {np.std(mv_deltas):.2f}")
print(f"LP delta mean: {np.mean(lp_deltas):+.2f} +/- {np.std(lp_deltas):.2f}")

print("\n--- Pooled bootstrap ---")
pooled_g = np.concatenate([per_seed_greedy[s] for s in SEEDS])
pooled_mv = np.concatenate([per_seed_mv[s] for s in SEEDS])
pooled_lp = np.concatenate([per_seed_lp[s] for s in SEEDS])

mv_diff, mv_ci, mv_pval = bootstrap_test(pooled_mv, pooled_g)
lp_diff, lp_ci, lp_pval = bootstrap_test(pooled_lp, pooled_g)
print(f"MV pooled: {mv_diff*100:+.2f}pp, 95%CI=[{mv_ci[0]*100:+.2f},{mv_ci[1]*100:+.2f}], p={mv_pval:.4f}")
print(f"LP pooled: {lp_diff*100:+.2f}pp, 95%CI=[{lp_ci[0]*100:+.2f},{lp_ci[1]*100:+.2f}], p={lp_pval:.4f}")

print("\n--- SUMMARY ---")
print(f"Dataset: FewNERD (3-epoch finetuned, mf4v2)")
print(f"Seeds: {SEEDS}")
print(f"N_samples/instance: 8, theta: {THETA}")
print(f"MV: {np.mean(mv_deltas):+.2f}+/-{np.std(mv_deltas):.2f}pp, pooled_p={mv_pval:.4f}")
print(f"LP: {np.mean(lp_deltas):+.2f}+/-{np.std(lp_deltas):.2f}pp, pooled_p={lp_pval:.4f}")
print(f"Paper claim: +1.40pp (4-seed, p<0.001) for LP construction on FewNERD")

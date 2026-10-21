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

print("=" * 90)
print("SciERC 5-Seed Entity Construction Analysis (MV + LP)")
print(f"Theta = 2/N = {THETA}, N=8 samples per instance")
print("=" * 90)

all_greedy = []
all_mv = []
all_lp = []
all_delta_mv = []
all_delta_lp = []
per_seed = {}

for seed in SEEDS:
    path = f"{BASE}/scierc_mf4v2_seed{seed}/samples.jsonl"
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
    per_seed[seed] = {"greedy": g_arr, "mv": mv_arr, "lp": lp_arr, "n": len(data)}

    g_m = g_arr.mean()
    mv_m = mv_arr.mean()
    lp_m = lp_arr.mean()
    d_mv = (mv_m - g_m) * 100
    d_lp = (lp_m - g_m) * 100

    all_greedy.append(g_m)
    all_mv.append(mv_m)
    all_lp.append(lp_m)
    all_delta_mv.append(d_mv)
    all_delta_lp.append(d_lp)

    _, _, p_mv = bootstrap_test(mv_arr, g_arr)
    _, _, p_lp = bootstrap_test(lp_arr, g_arr)

    print(f"\nSeed {seed}: N_instances={len(data)}")
    print(f"  Greedy F1:        {g_m*100:.2f}%")
    print(f"  MV Constr F1:     {mv_m*100:.2f}%  (D={d_mv:+.2f}pp, p={p_mv:.4f})")
    print(f"  LP Constr F1:     {lp_m*100:.2f}%  (D={d_lp:+.2f}pp, p={p_lp:.4f})")

print("\n" + "=" * 90)
print("AGGREGATE (5-seed)")
print("=" * 90)

g_mean, g_std = np.mean(all_greedy)*100, np.std(all_greedy)*100
mv_mean, mv_std = np.mean(all_mv)*100, np.std(all_mv)*100
lp_mean, lp_std = np.mean(all_lp)*100, np.std(all_lp)*100
dmv_mean, dmv_std = np.mean(all_delta_mv), np.std(all_delta_mv)
dlp_mean, dlp_std = np.mean(all_delta_lp), np.std(all_delta_lp)

print(f"Greedy F1:     {g_mean:.2f} +/- {g_std:.2f}%")
print(f"MV Constr F1:  {mv_mean:.2f} +/- {mv_std:.2f}%  (D={dmv_mean:+.2f} +/- {dmv_std:.2f}pp)")
print(f"LP Constr F1:  {lp_mean:.2f} +/- {lp_std:.2f}%  (D={dlp_mean:+.2f} +/- {dlp_std:.2f}pp)")

print("\n--- Pooled Bootstrap (all seeds combined) ---")
pooled_g = np.concatenate([per_seed[s]["greedy"] for s in SEEDS])
pooled_mv = np.concatenate([per_seed[s]["mv"] for s in SEEDS])
pooled_lp = np.concatenate([per_seed[s]["lp"] for s in SEEDS])

diff_mv, ci_mv, p_mv_pooled = bootstrap_test(pooled_mv, pooled_g)
diff_lp, ci_lp, p_lp_pooled = bootstrap_test(pooled_lp, pooled_g)
diff_lm, ci_lm, p_lm_pooled = bootstrap_test(pooled_lp, pooled_mv)

print(f"MV vs Greedy:  diff={diff_mv*100:+.2f}pp, 95%CI=[{ci_mv[0]*100:+.2f}, {ci_mv[1]*100:+.2f}], p={p_mv_pooled:.4f}  {'SIG' if p_mv_pooled < 0.05 else 'n.s.'}")
print(f"LP vs Greedy:  diff={diff_lp*100:+.2f}pp, 95%CI=[{ci_lp[0]*100:+.2f}, {ci_lp[1]*100:+.2f}], p={p_lp_pooled:.4f}  {'SIG' if p_lp_pooled < 0.05 else 'n.s.'}")
print(f"LP vs MV:      diff={diff_lm*100:+.2f}pp, 95%CI=[{ci_lm[0]*100:+.2f}, {ci_lm[1]*100:+.2f}], p={p_lm_pooled:.4f}  {'SIG' if p_lm_pooled < 0.05 else 'n.s.'}")

print("\n\n--- MARKDOWN TABLE ---")
print("| Seed | N | Greedy F1 | MV Constr F1 | MV Dpp | LP Constr F1 | LP Dpp | LP p |")
print("|------|---|-----------|--------------|--------|--------------|--------|------|")
for i, seed in enumerate(SEEDS):
    n = per_seed[seed]["n"]
    g = all_greedy[i]*100
    mv = all_mv[i]*100
    lp = all_lp[i]*100
    d_mv = all_delta_mv[i]
    d_lp = all_delta_lp[i]
    _, _, p_lp_s = bootstrap_test(per_seed[seed]["lp"], per_seed[seed]["greedy"])
    sig = "*" if p_lp_s < 0.05 else ""
    print(f"| {seed:<4} | {n} | {g:.2f} | {mv:.2f} | {d_mv:+.2f} | {lp:.2f} | {d_lp:+.2f} | {p_lp_s:.4f}{sig} |")
print(f"| **Mean** | | **{g_mean:.2f}+/-{g_std:.2f}** | **{mv_mean:.2f}+/-{mv_std:.2f}** | **{dmv_mean:+.2f}+/-{dmv_std:.2f}** | **{lp_mean:.2f}+/-{lp_std:.2f}** | **{dlp_mean:+.2f}+/-{dlp_std:.2f}** | |")

print("\n--- POOLED SIGNIFICANCE ---")
print(f"MV vs Greedy pooled p = {p_mv_pooled:.4f} -> {'Significant' if p_mv_pooled < 0.05 else 'Not significant'}")
print(f"LP vs Greedy pooled p = {p_lp_pooled:.4f} -> {'Significant' if p_lp_pooled < 0.05 else 'Not significant'}")
print(f"LP vs MV pooled p = {p_lm_pooled:.4f} -> {'LP > MV significant' if p_lm_pooled < 0.05 else 'LP vs MV not significant'}")

import json, math, sys
import numpy as np
from collections import defaultdict

SEED_PATHS = {
    42: "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_mf4v2_seed42_v3/samples.jsonl",
    456: "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_mf4v2_seed456/samples.jsonl",
}
THETA = 0.25
OUTPUT_FILE = "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_3epoch_construction_results.txt"

class Tee:
    def __init__(self, *files):
        self.files = files
    def write(self, data):
        for f in self.files:
            f.write(data)
            f.flush()
    def flush(self):
        for f in self.files:
            f.flush()

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
    lps = []
    for i, s in enumerate(samples):
        lp = s.get("mean_logprob", None)
        if lp is None:
            logprobs = inst.get("logprobs", None)
            if logprobs is not None and i < len(logprobs):
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

def compute_degeneracy_rate(data):
    n_degen = 0
    for inst in data:
        samples = inst["samples"]
        sets = [frozenset(entity_set(s.get("entities", []))) for s in samples]
        if len(set(sets)) == 1:
            n_degen += 1
    return n_degen / len(data) if data else 0.0

with open(OUTPUT_FILE, "w") as fout:
    out = Tee(sys.stdout, fout)

    out.write("=" * 80 + "\n")
    out.write("FewNERD 3-epoch (MF4v2) Entity Construction Analysis\n")
    out.write(f"Method: MV + LP-weighted construction, theta=2/N={THETA}\n")
    out.write(f"Seeds: {list(SEED_PATHS.keys())}\n")
    out.write("=" * 80 + "\n")

    per_seed = {}
    all_greedy_f1 = []
    all_mv_f1 = []
    all_lp_f1 = []
    all_mv_delta = []
    all_lp_delta = []
    per_seed_arrays = {}

    for seed, path in SEED_PATHS.items():
        data = []
        with open(path) as f:
            for line in f:
                if line.strip():
                    obj = json.loads(line)
                    if obj["gold"].get("entities", []):
                        data.append(obj)

        n_samples_per_inst = len(data[0]["samples"]) if data else 0
        degen_rate = compute_degeneracy_rate(data)

        greedy_f1s = []
        mv_f1s = []
        lp_f1s = []
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

        g_mean = g_arr.mean()
        mv_mean = mv_arr.mean()
        lp_mean = lp_arr.mean()
        mv_delta = (mv_mean - g_mean) * 100
        lp_delta = (lp_mean - g_mean) * 100

        mv_diff, mv_ci, mv_p = bootstrap_test(mv_arr, g_arr)
        lp_diff, lp_ci, lp_p = bootstrap_test(lp_arr, g_arr)

        per_seed[seed] = {
            "n": len(data), "n_samples": n_samples_per_inst,
            "g": g_mean, "mv": mv_mean, "lp": lp_mean,
            "mv_delta": mv_delta, "lp_delta": lp_delta,
            "mv_p": mv_p, "lp_p": lp_p,
            "mv_ci": mv_ci, "lp_ci": lp_ci,
            "degen": degen_rate,
        }
        per_seed_arrays[seed] = {"g": g_arr, "mv": mv_arr, "lp": lp_arr}

        all_greedy_f1.append(g_mean)
        all_mv_f1.append(mv_mean)
        all_lp_f1.append(lp_mean)
        all_mv_delta.append(mv_delta)
        all_lp_delta.append(lp_delta)

        out.write(f"\nSeed {seed}: N_instances={len(data)}, N_samples={n_samples_per_inst}, Degeneracy={degen_rate:.2%}\n")
        out.write(f"  Greedy F1:       {g_mean*100:.2f}%\n")
        out.write(f"  MV Constr F1:    {mv_mean*100:.2f}%  (delta={mv_delta:+.2f}pp, p={mv_p:.4f})\n")
        out.write(f"  LP Constr F1:    {lp_mean*100:.2f}%  (delta={lp_delta:+.2f}pp, p={lp_p:.4f})\n")
        out.write(f"  MV Bootstrap:    95%CI=[{mv_ci[0]*100:+.2f}, {mv_ci[1]*100:+.2f}]\n")
        out.write(f"  LP Bootstrap:    95%CI=[{lp_ci[0]*100:+.2f}, {lp_ci[1]*100:+.2f}]\n")

    out.write("\n" + "=" * 80 + "\n")
    out.write("AGGREGATE (2-seed)\n")
    out.write("=" * 80 + "\n")

    mv_deltas = np.array(all_mv_delta)
    lp_deltas = np.array(all_lp_delta)

    out.write(f"\nGreedy F1 mean:     {np.mean(all_greedy_f1)*100:.2f}%\n")
    out.write(f"MV Constr F1 mean:  {np.mean(all_mv_f1)*100:.2f}%\n")
    out.write(f"LP Constr F1 mean:  {np.mean(all_lp_f1)*100:.2f}%\n")
    out.write(f"\nMV Delta: mean={mv_deltas.mean():+.2f}pp, std={mv_deltas.std():.2f}pp\n")
    out.write(f"LP Delta: mean={lp_deltas.mean():+.2f}pp, std={lp_deltas.std():.2f}pp\n")
    out.write(f"MV direction: {int((mv_deltas>0).sum())}/{len(mv_deltas)} positive\n")
    out.write(f"LP direction: {int((lp_deltas>0).sum())}/{len(lp_deltas)} positive\n")

    out.write(f"\nMean degeneracy rate: {np.mean([v['degen'] for v in per_seed.values()]):.2%}\n")

    out.write("\n--- Pooled bootstrap (all seeds combined) ---\n")
    pooled_g = np.concatenate([per_seed_arrays[s]["g"] for s in SEED_PATHS])
    pooled_mv = np.concatenate([per_seed_arrays[s]["mv"] for s in SEED_PATHS])
    pooled_lp = np.concatenate([per_seed_arrays[s]["lp"] for s in SEED_PATHS])

    mv_diff, mv_ci, mv_p = bootstrap_test(pooled_mv, pooled_g)
    lp_diff, lp_ci, lp_p = bootstrap_test(pooled_lp, pooled_g)

    out.write(f"MV pooled: diff={mv_diff*100:+.2f}pp, 95%CI=[{mv_ci[0]*100:+.2f}, {mv_ci[1]*100:+.2f}], p={mv_p:.4f}\n")
    out.write(f"LP pooled: diff={lp_diff*100:+.2f}pp, 95%CI=[{lp_ci[0]*100:+.2f}, {lp_ci[1]*100:+.2f}], p={lp_p:.4f}\n")
    out.write(f"MV significant: {'YES' if mv_p < 0.05 else 'NO'}\n")
    out.write(f"LP significant: {'YES' if lp_p < 0.05 else 'NO'}\n")

    out.write("\n\n--- MARKDOWN TABLES ---\n\n")

    out.write("### Per-seed Results\n\n")
    out.write("| Seed | N | N_samples | Greedy F1 | MV F1 | MV D(pp) | LP F1 | LP D(pp) | Degen% |\n")
    out.write("|------|---|-----------|-----------|-------|----------|-------|----------|--------|\n")
    for seed in SEED_PATHS:
        s = per_seed[seed]
        out.write(f"| {seed} | {s['n']} | {s['n_samples']} | {s['g']*100:.2f} | {s['mv']*100:.2f} | {s['mv_delta']:+.2f} | {s['lp']*100:.2f} | {s['lp_delta']:+.2f} | {s['degen']:.1%} |\n")
    out.write(f"| **Mean** | | | {np.mean(all_greedy_f1)*100:.2f} | {np.mean(all_mv_f1)*100:.2f} | {mv_deltas.mean():+.2f} | {np.mean(all_lp_f1)*100:.2f} | {lp_deltas.mean():+.2f} | {np.mean([v['degen'] for v in per_seed.values()]):.1%} |\n")
    out.write(f"| **+/-s** | | | | | {mv_deltas.std():.2f} | | {lp_deltas.std():.2f} | |\n")

    out.write("\n### Bootstrap Significance\n\n")
    out.write("| Seed | MV p-value | MV 95%CI | LP p-value | LP 95%CI |\n")
    out.write("|------|------------|----------|------------|----------|\n")
    for seed in SEED_PATHS:
        s = per_seed[seed]
        out.write(f"| {seed} | {s['mv_p']:.4f} | [{s['mv_ci'][0]*100:+.2f}, {s['mv_ci'][1]*100:+.2f}] | {s['lp_p']:.4f} | [{s['lp_ci'][0]*100:+.2f}, {s['lp_ci'][1]*100:+.2f}] |\n")

    mv_diff_p, mv_ci_p, mv_p_p = bootstrap_test(pooled_mv, pooled_g)
    lp_diff_p, lp_ci_p, lp_p_p = bootstrap_test(pooled_lp, pooled_g)
    out.write(f"| **Pooled** | {mv_p_p:.4f} | [{mv_ci_p[0]*100:+.2f}, {mv_ci_p[1]*100:+.2f}] | {lp_p_p:.4f} | [{lp_ci_p[0]*100:+.2f}, {lp_ci_p[1]*100:+.2f}] |\n")

    out.write("\n### Comparison with Paper\n\n")
    out.write("| | Paper (4-seed SciERC) | FewNERD (2-seed, 3-epoch) |\n")
    out.write("|---|---|---|\n")
    out.write(f"| LP D (mean) | +1.40pp | {lp_deltas.mean():+.2f}pp |\n")
    out.write(f"| MV D (mean) | N/A | {mv_deltas.mean():+.2f}pp |\n")
    out.write(f"| Pooled LP p | <0.05 | {lp_p_p:.4f} |\n")
    out.write(f"| Direction | 4/4 positive | {int((lp_deltas>0).sum())}/{len(lp_deltas)} positive |\n")

    out.write("\nDone.\n")

print(f"\nResults saved to {OUTPUT_FILE}")

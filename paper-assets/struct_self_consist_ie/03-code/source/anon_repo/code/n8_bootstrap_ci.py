#!/usr/bin/env python3
"""Bootstrap CI for 5 signals: Qwen SciERC N=8 seed=42."""
import json, sys
import numpy as np
from collections import Counter
from scipy.stats import spearmanr

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import structural_consistency_soft_jaccard, fleiss_kappa_surface
from evaluation import per_instance_f1

DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl"
OUT_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/review_round2/n8_bootstrap_ci.json"
SUBTASK = "ner"

def load_data(path):
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return records

def compute_exact_match_rate(samples, subtask):
    if subtask == "ner":
        keys = [frozenset((e["text"], e["type"]) for e in s.get("entities", [])) for s in samples]
    else:
        keys = [frozenset((r["head"], r["tail"], r["type"]) for r in s.get("relations", [])) for s in samples]
    if not keys:
        return 0.0
    counter = Counter(keys)
    return counter.most_common(1)[0][1] / len(samples)

def compute_voting_confidence(samples, subtask):
    N = len(samples)
    if N == 0:
        return 0.0
    counter = Counter()
    if subtask == "ner":
        for s in samples:
            for e in s.get("entities", []):
                counter[(e["text"], e["type"])] += 1
    else:
        for s in samples:
            for r in s.get("relations", []):
                counter[(r["head"], r["tail"], r["type"])] += 1
    if not counter:
        return 0.0
    rates = [v / N for v in counter.values()]
    return float(np.mean(rates))

def compute_mean_logprob(samples):
    logprobs = [s.get("mean_logprob") for s in samples if s.get("mean_logprob") is not None]
    logprobs = [lp for lp in logprobs if np.isfinite(lp)]
    if not logprobs:
        return float("nan")
    return float(np.mean(logprobs))

def bootstrap_rho_ci(signal, quality, n_boot=10000, alpha=0.05):
    rng = np.random.default_rng(42)
    signal, quality = np.array(signal, dtype=float), np.array(quality, dtype=float)
    mask = np.isfinite(signal) & np.isfinite(quality)
    signal, quality = signal[mask], quality[mask]
    n = len(signal)
    point_rho = float(spearmanr(signal, quality).statistic)
    rhos = []
    for _ in range(n_boot):
        idx = rng.integers(0, n, size=n)
        r = spearmanr(signal[idx], quality[idx]).statistic
        if np.isfinite(r):
            rhos.append(float(r))
    rhos.sort()
    lo = float(np.percentile(rhos, 100 * alpha / 2))
    hi = float(np.percentile(rhos, 100 * (1 - alpha / 2)))
    return {"rho": round(point_rho, 4), "ci_lo": round(lo, 4), "ci_hi": round(hi, 4), "n": n}

def bootstrap_delta_ci(sig_a, sig_b, quality, n_boot=10000, alpha=0.05):
    rng = np.random.default_rng(42)
    sig_a = np.array(sig_a, dtype=float)
    sig_b = np.array(sig_b, dtype=float)
    quality = np.array(quality, dtype=float)
    mask = np.isfinite(sig_a) & np.isfinite(sig_b) & np.isfinite(quality)
    sig_a, sig_b, quality = sig_a[mask], sig_b[mask], quality[mask]
    n = len(sig_a)
    rho_a = float(spearmanr(sig_a, quality).statistic)
    rho_b = float(spearmanr(sig_b, quality).statistic)
    point_delta = rho_a - rho_b
    deltas = []
    for _ in range(n_boot):
        idx = rng.integers(0, n, size=n)
        ra = spearmanr(sig_a[idx], quality[idx]).statistic
        rb = spearmanr(sig_b[idx], quality[idx]).statistic
        d = float(ra) - float(rb)
        if np.isfinite(d):
            deltas.append(d)
    deltas.sort()
    lo = float(np.percentile(deltas, 100 * alpha / 2))
    hi = float(np.percentile(deltas, 100 * (1 - alpha / 2)))
    significant = not (lo <= 0 <= hi)
    return {
        "delta": round(point_delta, 4),
        "ci_lo": round(lo, 4),
        "ci_hi": round(hi, 4),
        "significant": significant
    }

records = load_data(DATA_PATH)
print(f"Total records: {len(records)}")

valid = [r for r in records if len(r["gold"].get("entities", [])) > 0]
print(f"Valid (gold non-empty) for NER: {len(valid)}")

sj_vals, fk_vals, vc_vals, em_vals, lp_vals, f1_vals = [], [], [], [], [], []
for inst in valid:
    samples = inst["samples"]
    gold = inst["gold"]
    greedy = inst.get("greedy", samples[0])
    sj_vals.append(structural_consistency_soft_jaccard(samples, subtask=SUBTASK))
    fk_vals.append(fleiss_kappa_surface(samples, subtask=SUBTASK))
    vc_vals.append(compute_voting_confidence(samples, SUBTASK))
    em_vals.append(compute_exact_match_rate(samples, SUBTASK))
    lp_vals.append(compute_mean_logprob(samples))
    f1_vals.append(per_instance_f1(greedy, gold, subtask=SUBTASK))

print("Signal computation done.")

signals_map = {
    "sj": np.array(sj_vals),
    "fk": np.array(fk_vals),
    "voting_conf": np.array(vc_vals),
    "em": np.array(em_vals),
    "logprob": np.array(lp_vals),
}
f1_arr = np.array(f1_vals)

print("Computing bootstrap CIs (B=10000)...")
signal_results = {}
for name, vals in signals_map.items():
    ci = bootstrap_rho_ci(vals, f1_arr, n_boot=10000)
    signal_results[name] = ci
    print(f"  {name:12s}: rho={ci['rho']:+.4f}  CI=[{ci['ci_lo']:+.4f}, {ci['ci_hi']:+.4f}]  n={ci['n']}")

print("Delta comparisons:")
delta_results = {}

d1 = bootstrap_delta_ci(signals_map["sj"], signals_map["logprob"], f1_arr)
delta_results["sj_minus_logprob"] = d1
print(f"  SJ - logprob:     delta={d1['delta']:+.4f}  CI=[{d1['ci_lo']:+.4f}, {d1['ci_hi']:+.4f}]  sig={d1['significant']}")

d2 = bootstrap_delta_ci(signals_map["voting_conf"], signals_map["sj"], f1_arr)
delta_results["voting_minus_sj"] = d2
print(f"  voting - SJ:      delta={d2['delta']:+.4f}  CI=[{d2['ci_lo']:+.4f}, {d2['ci_hi']:+.4f}]  sig={d2['significant']}")

d3 = bootstrap_delta_ci(signals_map["em"], signals_map["sj"], f1_arr)
delta_results["em_minus_sj"] = d3
print(f"  EM - SJ:          delta={d3['delta']:+.4f}  CI=[{d3['ci_lo']:+.4f}, {d3['ci_hi']:+.4f}]  sig={d3['significant']}")

output = {
    "config": "Qwen SciERC N=8 seed=42",
    "n_valid": len(valid),
    "subtask": SUBTASK,
    "signals": signal_results,
    "delta_comparisons": delta_results
}

with open(OUT_PATH, "w") as f:
    json.dump(output, f, indent=2)

print(f"\nSaved to {OUT_PATH}")
print("\n" + json.dumps(output, indent=2))

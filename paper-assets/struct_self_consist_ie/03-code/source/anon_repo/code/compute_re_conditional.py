#!/usr/bin/env python3
"""Compute 5-signal RE conditional rho for seed42 and seed123."""

import json, sys, os
import numpy as np
from scipy.stats import spearmanr, rankdata
from collections import Counter

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import compute_all_consistency_scores
from evaluation import per_instance_f1

SEEDS = {
    "seed42": "/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2",
    "seed123": "/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed123_v2",
}
SUBTASK = "re"


def load_data(path):
    with open(os.path.join(path, "samples.jsonl")) as f:
        return [json.loads(line) for line in f if line.strip()]


def compute_exact_match_rate(samples):
    keys = [frozenset((r["head"], r["tail"], r["type"]) for r in s.get("relations", [])) for s in samples]
    if not keys: return 0.0
    c = Counter(keys)
    return c.most_common(1)[0][1] / len(samples)


def compute_voting_confidence(samples):
    N = len(samples)
    if N == 0: return 0.0
    counter = Counter()
    for s in samples:
        for r in s.get("relations", []):
            counter[(r["head"], r["tail"], r["type"])] += 1
    if not counter: return 0.0
    return float(np.mean([v / N for v in counter.values()]))


def compute_mean_logprob(samples):
    lps = [s.get("mean_logprob") for s in samples if s.get("mean_logprob") is not None]
    lps = [lp for lp in lps if np.isfinite(lp)]
    return float(np.mean(lps)) if lps else float("nan")


def safe_spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    x, y = x[m], y[m]
    if len(x) < 3: return float("nan"), float("nan")
    r = spearmanr(x, y)
    return float(r.statistic), float(r.pvalue)


def safe_auroc(scores, labels):
    scores, labels = np.asarray(scores, float), np.asarray(labels, int)
    if len(np.unique(labels)) < 2: return float("nan")
    n_pos, n_neg = (labels==1).sum(), (labels==0).sum()
    if n_pos == 0 or n_neg == 0: return float("nan")
    ranks = rankdata(scores)
    u = ranks[labels==1].sum() - n_pos*(n_pos+1)/2
    return float(u / (n_pos * n_neg))


def normalize_for_ece(sig_name, values):
    v = np.asarray(values, dtype=float)
    if sig_name in ("SJ", "EM", "voting_conf"):
        return np.clip(v, 0, 1)
    elif sig_name == "FK":
        return np.clip((v + 1) / 2, 0, 1)
    elif sig_name == "logprob":
        return np.clip(np.exp(v), 0, 1)
    return v


def compute_ece(confidences, correctness, n_bins=10):
    conf = np.asarray(confidences, dtype=float)
    corr = np.asarray(correctness, dtype=float)
    mask = np.isfinite(conf)
    conf, corr = conf[mask], corr[mask]
    if len(conf) == 0: return float("nan")
    bin_edges = np.linspace(0, 1, n_bins + 1)
    ece = 0.0
    for i in range(n_bins):
        lo, hi = bin_edges[i], bin_edges[i + 1]
        in_bin = (conf >= lo) & (conf <= hi if i == n_bins - 1 else conf < hi)
        if in_bin.sum() == 0: continue
        ece += in_bin.sum() / len(conf) * abs(conf[in_bin].mean() - corr[in_bin].mean())
    return float(ece)


def bootstrap_metric(metric_fn, signals, targets, n_boot=1000, seed=42):
    rng = np.random.RandomState(seed)
    signals, targets = np.asarray(signals, float), np.asarray(targets, float)
    n = len(signals)
    vals = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        v = metric_fn(signals[idx], targets[idx])
        if isinstance(v, tuple): v = v[0]
        if np.isfinite(v): vals.append(v)
    if not vals: return [float("nan"), float("nan")]
    return [float(np.percentile(vals, 2.5)), float(np.percentile(vals, 97.5))]


def analyze_split(instances):
    consistency = compute_all_consistency_scores(instances, subtask=SUBTASK)
    sj_vals = consistency["soft_jaccard"]
    fk_vals = consistency["fleiss_kappa"]

    lp_vals, em_vals, vc_vals, f1_vals = [], [], [], []
    for inst in instances:
        samples = inst["samples"]
        greedy = inst.get("greedy", samples[0])
        lp_vals.append(compute_mean_logprob(samples))
        em_vals.append(compute_exact_match_rate(samples))
        vc_vals.append(compute_voting_confidence(samples))
        f1_vals.append(per_instance_f1(greedy, inst["gold"], subtask=SUBTASK))

    signals = {"SJ": np.array(sj_vals), "FK": np.array(fk_vals),
               "logprob": np.array(lp_vals), "EM": np.array(em_vals),
               "voting_conf": np.array(vc_vals)}
    f1_arr = np.array(f1_vals)
    binary = (f1_arr >= 1.0).astype(int)

    result = {"n": len(instances), "pct_perfect": float(binary.mean()),
              "greedy_f1_mean": round(float(np.mean(f1_vals)), 4)}
    metrics = {}
    for name, vals in signals.items():
        rho, p = safe_spearman(vals, f1_arr)
        rho_ci = bootstrap_metric(lambda x,y: safe_spearman(x,y)[0], vals, f1_arr)
        auroc = safe_auroc(vals, binary)
        auroc_ci = bootstrap_metric(safe_auroc, vals, binary.astype(float))
        ece_conf = normalize_for_ece(name, vals)
        ece = compute_ece(ece_conf, binary)
        metrics[name] = {
            "rho": round(rho, 4), "rho_ci95": [round(v, 4) for v in rho_ci], "p_rho": p,
            "auroc": round(auroc, 4), "auroc_ci95": [round(v, 4) for v in auroc_ci],
            "ece": round(ece, 4)
        }
    result["metrics"] = metrics
    return result


def json_default(obj):
    if isinstance(obj, (np.floating, np.float64, np.float32)): return float(obj)
    if isinstance(obj, (np.integer, np.int64, np.int32)): return int(obj)
    if isinstance(obj, np.ndarray): return obj.tolist()
    if isinstance(obj, np.bool_): return bool(obj)
    return str(obj)


def main():
    results = {}
    for seed_name, out_dir in SEEDS.items():
        print(f"\n{'='*60}")
        print(f"Processing {seed_name} RE: {out_dir}")
        instances = load_data(out_dir)
        print(f"  Loaded {len(instances)} instances")

        valid = [inst for inst in instances if len(inst["gold"].get("relations", [])) > 0]
        print(f"  Valid (non-empty gold relations): {len(valid)}")

        greedy_f1s = []
        for inst in valid:
            greedy = inst.get("greedy", inst["samples"][0])
            greedy_f1s.append(per_instance_f1(greedy, inst["gold"], subtask=SUBTASK))
        conditional = [inst for inst, f1 in zip(valid, greedy_f1s) if f1 > 0]
        print(f"  Conditional (greedy RE F1 > 0): {len(conditional)}")

        seed_result = {}
        for split_name, split_insts in [("full", valid), ("conditional", conditional)]:
            print(f"\n  --- {split_name} ({len(split_insts)} instances) ---")
            res = analyze_split(split_insts)
            for sig_name, m in res["metrics"].items():
                print(f"    {sig_name:>12}: rho={m['rho']:.4f}  AUROC={m['auroc']:.4f}  ECE={m['ece']:.4f}")
            seed_result[split_name] = res

        out_path = os.path.join(out_dir, "re_all_signals_report.json")
        with open(out_path, "w") as f:
            json.dump(seed_result, f, indent=2, default=json_default)
        print(f"\n  Saved: {out_path}")
        results[seed_name] = seed_result

    # Print compact summary for easy extraction
    print(f"\n{'='*60}")
    print("RE 2-SEED SUMMARY (for heatmap):")
    for split in ["full", "conditional"]:
        print(f"\n  {split}:")
        for sig in ["SJ", "FK", "EM", "voting_conf", "logprob"]:
            vals = [results[s][split]["metrics"][sig]["rho"] for s in ["seed42", "seed123"]]
            print(f"    {sig:>12}: {vals[0]:.4f}, {vals[1]:.4f} → mean={np.mean(vals):.4f}")

    print("\nJSON:")
    print(json.dumps(results, indent=2, default=json_default))


if __name__ == "__main__":
    main()

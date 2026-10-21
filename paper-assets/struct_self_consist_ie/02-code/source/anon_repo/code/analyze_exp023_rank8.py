#!/usr/bin/env python3
"""exp_023 LoRA rank=8 ablation: 5-signal analysis for NER + RE."""

import json
import sys
from collections import Counter

import numpy as np
from scipy.stats import spearmanr, kendalltau, rankdata

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import compute_all_consistency_scores
from evaluation import per_instance_f1

DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8/samples.jsonl"
OUTPUT_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8/all_signals_5signal.json"
SUBTASKS = ["ner", "re"]

# rank=32 baseline from exp_012_rerun_1024 for comparison
BASELINE = {
    "ner_full": {"SJ": 0.3599, "FK": 0.2665, "logprob": 0.2052, "EM": 0.2945, "voting_conf": 0.3792},
    "ner_cond": {"SJ": 0.3113, "FK": 0.1761, "logprob": 0.1538, "EM": 0.3596, "voting_conf": 0.3},
    "re_full": {"SJ": 0.2503, "FK": 0.2752, "logprob": 0.2662, "EM": 0.1344, "voting_conf": 0.3498},
    "re_cond": {"SJ": 0.2457, "FK": 0.1139, "logprob": 0.0112, "EM": 0.4165, "voting_conf": 0.2409},
}


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


def safe_auroc(scores, labels):
    scores = np.asarray(scores, dtype=float)
    labels = np.asarray(labels, dtype=int)
    if len(np.unique(labels)) < 2:
        return float("nan")
    n_pos = np.sum(labels == 1)
    n_neg = np.sum(labels == 0)
    if n_pos == 0 or n_neg == 0:
        return float("nan")
    ranks = rankdata(scores)
    u = ranks[labels == 1].sum() - n_pos * (n_pos + 1) / 2
    return float(u / (n_pos * n_neg))


def safe_spearman(x, y):
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y)
    x, y = x[mask], y[mask]
    if len(x) < 3:
        return float("nan")
    return float(spearmanr(x, y).statistic)


def safe_kendall(x, y):
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y)
    x, y = x[mask], y[mask]
    if len(x) < 3:
        return float("nan")
    return float(kendalltau(x, y).statistic)


def normalize_for_ece(signal_name, values):
    v = np.asarray(values, dtype=float)
    if signal_name in ("SJ", "EM", "voting_conf"):
        return np.clip(v, 0, 1)
    elif signal_name == "FK":
        return np.clip((v + 1) / 2, 0, 1)
    elif signal_name == "logprob":
        return np.clip(np.exp(v), 0, 1)
    return v


def compute_ece(confidences, correctness, n_bins=10):
    conf = np.asarray(confidences, dtype=float)
    corr = np.asarray(correctness, dtype=float)
    mask = np.isfinite(conf)
    conf, corr = conf[mask], corr[mask]
    if len(conf) == 0:
        return float("nan")
    bin_edges = np.linspace(0, 1, n_bins + 1)
    ece = 0.0
    total = len(conf)
    for i in range(n_bins):
        lo, hi = bin_edges[i], bin_edges[i + 1]
        in_bin = (conf >= lo) & (conf <= hi if i == n_bins - 1 else conf < hi)
        if in_bin.sum() == 0:
            continue
        bin_conf = conf[in_bin].mean()
        bin_acc = corr[in_bin].mean()
        ece += in_bin.sum() / total * abs(bin_acc - bin_conf)
    return float(ece)


def bootstrap_metric(metric_fn, x, y, n_boot=1000, seed=42):
    rng = np.random.RandomState(seed)
    n = len(x)
    boot_vals = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        val = metric_fn(x[idx], y[idx])
        if np.isfinite(val):
            boot_vals.append(val)
    if not boot_vals:
        return [float("nan"), float("nan")]
    return [float(np.percentile(boot_vals, 2.5)), float(np.percentile(boot_vals, 97.5))]


def evaluate_subtask(instances, subtask):
    if subtask == "ner":
        valid = [inst for inst in instances if len(inst["gold"].get("entities", [])) > 0]
    else:
        valid = [inst for inst in instances if len(inst["gold"].get("relations", [])) > 0]
    print(f"\n=== {subtask.upper()} === Valid: {len(valid)}")

    greedy_f1s_all = []
    for inst in valid:
        greedy = inst.get("greedy", inst["samples"][0])
        greedy_f1s_all.append(per_instance_f1(greedy, inst["gold"], subtask=subtask))
    conditional = [inst for inst, f1 in zip(valid, greedy_f1s_all) if f1 > 0]
    print(f"Conditional (greedy F1 > 0): {len(conditional)}")

    results = {}
    for split_name, split_instances in [("full", valid), ("conditional", conditional)]:
        print(f"\n--- {split_name} ({len(split_instances)} instances) ---")
        consistency = compute_all_consistency_scores(split_instances, subtask=subtask)
        sj_vals = consistency["soft_jaccard"]
        fk_vals = consistency["fleiss_kappa"]

        lp_vals, em_vals, vc_vals, f1_vals = [], [], [], []
        for inst in split_instances:
            samples = inst["samples"]
            gold = inst["gold"]
            greedy = inst.get("greedy", samples[0])
            lp_vals.append(compute_mean_logprob(samples))
            em_vals.append(compute_exact_match_rate(samples, subtask))
            vc_vals.append(compute_voting_confidence(samples, subtask))
            f1_vals.append(per_instance_f1(greedy, gold, subtask=subtask))

        signals = {
            "SJ": np.array(sj_vals, dtype=float),
            "FK": np.array(fk_vals, dtype=float),
            "logprob": np.array(lp_vals, dtype=float),
            "EM": np.array(em_vals, dtype=float),
            "voting_conf": np.array(vc_vals, dtype=float),
        }
        f1_arr = np.array(f1_vals, dtype=float)
        binary_correct = (f1_arr >= 1.0).astype(int)

        split_results = {
            "n": len(split_instances),
            "greedy_f1_mean": float(np.mean(f1_vals)),
            "pct_perfect": float(binary_correct.mean()),
        }

        baseline_key = f"{subtask}_{split_name}" if split_name == "full" else f"{subtask}_cond"
        baseline = BASELINE.get(baseline_key, {})

        metrics = {}
        for sig_name, sig_vals in signals.items():
            m = {}
            rho = safe_spearman(sig_vals, f1_arr)
            rho_ci = bootstrap_metric(safe_spearman, sig_vals, f1_arr)
            m["rho"] = rho
            m["rho_ci95"] = rho_ci

            tau = safe_kendall(sig_vals, f1_arr)
            m["tau"] = tau

            auroc = safe_auroc(sig_vals, binary_correct)
            auroc_ci = bootstrap_metric(safe_auroc, sig_vals, binary_correct.astype(float))
            m["AUROC"] = auroc
            m["AUROC_ci95"] = auroc_ci

            ece_conf = normalize_for_ece(sig_name, sig_vals)
            m["ECE"] = compute_ece(ece_conf, binary_correct)

            baseline_rho = baseline.get(sig_name, float("nan"))
            delta = rho - baseline_rho if np.isfinite(baseline_rho) else float("nan")
            m["delta_vs_r32"] = round(delta, 4)

            print(f"  {sig_name:>12}: rho={rho:.4f}  tau={tau:.4f}  AUROC={auroc:.4f}  ECE={m['ECE']:.4f}  Δr32={delta:+.4f}")

            metrics[sig_name] = m

        split_results["metrics"] = metrics
        results[split_name] = split_results

    return results


def main():
    instances = load_data(DATA_PATH)
    print(f"Loaded {len(instances)} instances, N={len(instances[0]['samples'])}")

    all_results = {}
    for subtask in SUBTASKS:
        all_results[subtask] = evaluate_subtask(instances, subtask)

    def json_default(obj):
        if isinstance(obj, (np.floating, np.float64, np.float32)):
            return float(obj)
        if isinstance(obj, (np.integer, np.int64, np.int32)):
            return int(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.bool_):
            return bool(obj)
        return str(obj)

    with open(OUTPUT_PATH, "w") as f:
        json.dump(all_results, f, indent=2, default=json_default)
    print(f"\nSaved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

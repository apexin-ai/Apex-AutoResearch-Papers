#!/usr/bin/env python3
"""exp_015_v2: Full signal x dataset x metric evaluation matrix.

Signals: SJ, FK, logprob, EM, voting_conf
Metrics: AUROC, Spearman rho, Kendall tau, ECE
Extra: Leave-one-out SJ robustness check, Bootstrap 95% CI
"""

import json
import os
import sys
from collections import Counter

import numpy as np
from scipy.stats import spearmanr, kendalltau

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import (
    compute_all_consistency_scores,
    structural_consistency_soft_jaccard,
)
from evaluation import per_instance_f1

BASE_DIR = "/root/autodl-tmp/struct_self_consist_ie/output"
OUTPUT_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2"

DATASETS = {
    "scierc_n8_logprob": {
        "path": "exp_012_logprob/samples_with_logprobs.jsonl",
        "subtasks": ["ner", "re"],
        "desc": "SciERC NER+RE N=8 T=1.0 seed42",
    },
    "scierc_n16_seed42": {
        "path": "exp_001_seed42_v2/samples.jsonl",
        "subtasks": ["ner", "re"],
        "desc": "SciERC NER+RE N=16 seed42",
    },
    "scierc_n16_seed123": {
        "path": "exp_001_seed123_v2/samples.jsonl",
        "subtasks": ["ner", "re"],
        "desc": "SciERC NER+RE N=16 seed123",
    },
    "conll2003": {
        "path": "exp002_conll2003/samples.jsonl",
        "subtasks": ["ner"],
        "desc": "CoNLL-2003 NER N=8",
    },
    "wnut17": {
        "path": "exp003_wnut17_eval/samples.jsonl",
        "subtasks": ["ner"],
        "desc": "WNUT-17 NER N=16",
    },
    "llama_scierc_n8": {
        "path": "exp007_llama_inference/samples.jsonl",
        "subtasks": ["ner", "re"],
        "desc": "LLaMA SciERC N=8",
    },
    "llama_seed123": {
        "path": "exp_007_llama_seed123/samples.jsonl",
        "subtasks": ["ner", "re"],
        "desc": "LLaMA SciERC N=16 seed123",
    },
    "llama_seed456": {
        "path": "exp_007_llama_seed456/samples.jsonl",
        "subtasks": ["ner", "re"],
        "desc": "LLaMA SciERC N=16 seed456",
    },
    "scierc_re_n16": {
        "path": "exp_008_re_n16_v2/samples.jsonl",
        "subtasks": ["ner", "re"],
        "desc": "SciERC RE N=16",
    },
    "scierc_re_seed123": {
        "path": "exp_008_re_seed123/samples.jsonl",
        "subtasks": ["ner", "re"],
        "desc": "SciERC RE seed123",
    },
}


def load_data(path):
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


# ---- Signal computation ----

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


# ---- Metrics ----

def safe_auroc(scores, labels):
    scores = np.asarray(scores, dtype=float)
    labels = np.asarray(labels, dtype=int)
    if len(np.unique(labels)) < 2:
        return float("nan")
    n_pos = np.sum(labels == 1)
    n_neg = np.sum(labels == 0)
    if n_pos == 0 or n_neg == 0:
        return float("nan")
    from scipy.stats import rankdata
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


def normalize_for_ece(signal_name, values):
    v = np.asarray(values, dtype=float)
    if signal_name in ("SJ", "EM", "voting_conf"):
        return np.clip(v, 0, 1)
    elif signal_name == "FK":
        return np.clip((v + 1) / 2, 0, 1)
    elif signal_name == "logprob":
        return np.clip(np.exp(v), 0, 1)
    return v


def bootstrap_metric(metric_fn, signals, targets, n_boot=1000, seed=42):
    rng = np.random.RandomState(seed)
    signals = np.asarray(signals, dtype=float)
    targets = np.asarray(targets, dtype=float)
    n = len(signals)
    boot_vals = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        val = metric_fn(signals[idx], targets[idx])
        if np.isfinite(val):
            boot_vals.append(val)
    if not boot_vals:
        return [float("nan"), float("nan")]
    return [float(np.percentile(boot_vals, 2.5)), float(np.percentile(boot_vals, 97.5))]


# ---- LOO-SJ ----

def compute_loo_sj(instances, subtask):
    loo_sj_means = []
    for inst in instances:
        samples = inst["samples"]
        n = len(samples)
        if n < 3:
            loo_sj_means.append(structural_consistency_soft_jaccard(samples, subtask=subtask))
            continue
        loo_vals = []
        for i in range(n):
            subset = samples[:i] + samples[i+1:]
            loo_vals.append(structural_consistency_soft_jaccard(subset, subtask=subtask))
        loo_sj_means.append(float(np.mean(loo_vals)))
    return loo_sj_means


# ---- Main analysis ----

def analyze_dataset(instances, subtask, dataset_name):
    if subtask == "re":
        valid = [inst for inst in instances if len(inst["gold"].get("relations", [])) > 0]
    else:
        valid = [inst for inst in instances if len(inst["gold"].get("entities", [])) > 0]

    if len(valid) < 10:
        return None

    print(f"    Computing consistency signals ({len(valid)} valid instances)...")
    consistency = compute_all_consistency_scores(valid, subtask=subtask)

    sj_vals = consistency["soft_jaccard"]
    fk_vals = consistency["fleiss_kappa"]
    lp_vals, em_vals, vc_vals, f1_vals = [], [], [], []

    for inst in valid:
        samples = inst["samples"]
        gold = inst["gold"]
        greedy = inst.get("greedy", samples[0] if samples else {"entities": [], "relations": []})
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

    N_BOOT = 1000
    metrics = {}
    for sig_name, sig_vals in signals.items():
        print(f"      Signal {sig_name}: computing metrics + bootstrap...")
        m = {}

        auroc = safe_auroc(sig_vals, binary_correct)
        auroc_ci = bootstrap_metric(safe_auroc, sig_vals, binary_correct.astype(float), N_BOOT)
        m["AUROC"] = {"value": auroc, "ci_95": auroc_ci}

        rho = safe_spearman(sig_vals, f1_arr)
        rho_ci = bootstrap_metric(safe_spearman, sig_vals, f1_arr, N_BOOT)
        m["Spearman_rho"] = {"value": rho, "ci_95": rho_ci}

        tau = safe_kendall(sig_vals, f1_arr)
        tau_ci = bootstrap_metric(safe_kendall, sig_vals, f1_arr, N_BOOT)
        m["Kendall_tau"] = {"value": tau, "ci_95": tau_ci}

        ece_conf = normalize_for_ece(sig_name, sig_vals)
        ece = compute_ece(ece_conf, binary_correct)
        m["ECE"] = {"value": ece}

        metrics[sig_name] = m

    # LOO-SJ
    print(f"    Computing LOO-SJ...")
    loo_sj = compute_loo_sj(valid, subtask)
    loo_sj_arr = np.array(loo_sj, dtype=float)

    full_sj_rho = safe_spearman(signals["SJ"], f1_arr)
    loo_sj_rho = safe_spearman(loo_sj_arr, f1_arr)
    full_sj_auroc = safe_auroc(signals["SJ"], binary_correct)
    loo_sj_auroc = safe_auroc(loo_sj_arr, binary_correct)

    def _safe_diff(a, b):
        return a - b if np.isfinite(a) and np.isfinite(b) else float("nan")

    loo_results = {
        "full_SJ_rho": full_sj_rho,
        "LOO_SJ_rho": loo_sj_rho,
        "delta_rho": _safe_diff(loo_sj_rho, full_sj_rho),
        "full_SJ_AUROC": full_sj_auroc,
        "LOO_SJ_AUROC": loo_sj_auroc,
        "delta_AUROC": _safe_diff(loo_sj_auroc, full_sj_auroc),
        "LOO_vs_full_corr": float(spearmanr(loo_sj_arr, signals["SJ"]).statistic) if len(loo_sj_arr) >= 3 else float("nan"),
        "circularity_concern": bool(abs(_safe_diff(loo_sj_rho, full_sj_rho)) >= 0.02) if np.isfinite(loo_sj_rho) and np.isfinite(full_sj_rho) else None,
    }

    summary = {
        "n_instances": len(valid),
        "n_samples_per_instance": len(valid[0]["samples"]) if valid else 0,
        "mean_f1": float(np.mean(f1_arr)),
        "pct_perfect": float(np.mean(binary_correct)),
        "signal_stats": {
            sn: {"mean": float(np.nanmean(sv)), "std": float(np.nanstd(sv)),
                 "min": float(np.nanmin(sv)), "max": float(np.nanmax(sv))}
            for sn, sv in signals.items()
        },
    }

    return {"metrics": metrics, "loo_sj": loo_results, "summary": summary}


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    all_results = {}

    for ds_name, ds_info in DATASETS.items():
        filepath = os.path.join(BASE_DIR, ds_info["path"])
        if not os.path.exists(filepath):
            print(f"SKIP {ds_name}: file not found")
            continue

        instances = load_data(filepath)
        print(f"\n{'='*80}")
        print(f"Dataset: {ds_name} ({ds_info['desc']})")
        print(f"  Loaded {len(instances)} instances, N={len(instances[0]['samples'])}")

        for subtask in ds_info["subtasks"]:
            key = f"{ds_name}_{subtask}"
            print(f"\n  Subtask: {subtask}")

            result = analyze_dataset(instances, subtask, ds_name)
            if result is None:
                print(f"    SKIP (too few valid instances)")
                continue

            result["description"] = ds_info["desc"]
            result["subtask"] = subtask
            result["file"] = ds_info["path"]
            all_results[key] = result

            for sig in ["SJ", "FK", "logprob", "EM", "voting_conf"]:
                m = result["metrics"][sig]
                a = m["AUROC"]["value"]
                t = m["Kendall_tau"]["value"]
                r = m["Spearman_rho"]["value"]
                e = m["ECE"]["value"]
                fmt = lambda v: f"{v:.4f}" if np.isfinite(v) else "N/A"
                print(f"    {sig:>12}: AUROC={fmt(a)}  tau={fmt(t)}  rho={fmt(r)}  ECE={fmt(e)}")

            loo = result["loo_sj"]
            dr = loo["delta_rho"]
            da = loo["delta_AUROC"]
            lc = loo["LOO_vs_full_corr"]
            print(f"    LOO-SJ: d_rho={dr:.6f}  d_AUROC={da:.6f}  corr={lc:.4f}")

    # Save results
    output_file = os.path.join(OUTPUT_DIR, "exp015_v2_metrics.json")

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

    with open(output_file, "w") as f:
        json.dump(all_results, f, indent=2, default=json_default)
    print(f"\nResults saved to {output_file}")

    # Summary tables
    def fmt(v):
        return f"{v:>8.4f}" if np.isfinite(v) else f"{'N/A':>8}"

    for metric_name, metric_key in [("AUROC", "AUROC"), ("Kendall tau", "Kendall_tau"),
                                      ("Spearman rho", "Spearman_rho"), ("ECE", "ECE")]:
        print(f"\n{'='*130}")
        print(f"{metric_name} Summary (Signal x Dataset)")
        print(f"{'='*130}")
        header = f"{'Dataset':<35} {'SJ':>8} {'FK':>8} {'logprob':>8} {'EM':>8} {'voting':>8}  {'N':>5} {'%perf':>6}"
        print(header)
        print("-" * 130)
        for key in sorted(all_results.keys()):
            res = all_results[key]
            row = f"{key:<35}"
            for sig in ["SJ", "FK", "logprob", "EM", "voting_conf"]:
                v = res["metrics"][sig][metric_key]["value"]
                row += f" {fmt(v)}"
            row += f"  {res['summary']['n_instances']:>5} {res['summary']['pct_perfect']:>6.1%}"
            print(row)

    # LOO-SJ table
    print(f"\n{'='*130}")
    print("LOO-SJ Robustness Check")
    print(f"{'='*130}")
    print(f"{'Dataset':<35} {'full_rho':>8} {'LOO_rho':>8} {'d_rho':>10} {'full_AUC':>8} {'LOO_AUC':>8} {'d_AUC':>10} {'corr':>8} {'circ?':>6}")
    print("-" * 130)
    for key in sorted(all_results.keys()):
        loo = all_results[key]["loo_sj"]
        circ = "YES" if loo["circularity_concern"] else "No"
        print(f"{key:<35} {loo['full_SJ_rho']:>8.4f} {loo['LOO_SJ_rho']:>8.4f} {loo['delta_rho']:>10.6f} "
              f"{loo['full_SJ_AUROC']:>8.4f} {loo['LOO_SJ_AUROC']:>8.4f} {loo['delta_AUROC']:>10.6f} "
              f"{loo['LOO_vs_full_corr']:>8.4f} {circ:>6}")


if __name__ == "__main__":
    main()

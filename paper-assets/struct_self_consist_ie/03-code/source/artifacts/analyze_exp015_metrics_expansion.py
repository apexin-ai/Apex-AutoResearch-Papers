#!/usr/bin/env python3
"""exp-015: Extended evaluation metrics for all 5 confidence signals.

Signals: soft_jaccard, fleiss_kappa, logprob, exact_match, voting_confidence
Metrics: Spearman rho, Kendall tau, AUROC, Calibration, LOO-SJ, Bootstrap CI

Usage:
    cd /root/autodl-tmp/struct_self_consist_ie
    python code/analyze_exp015_metrics_expansion.py \
        --pilot_dir output/mvp_pilot_004 \
        --logprob_dir output/exp_012_logprob \
        --output_dir output/exp015_metrics_expansion
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter
from itertools import combinations

import numpy as np
from scipy.stats import spearmanr, kendalltau

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))

from consistency import (
    compute_all_consistency_scores,
    fleiss_kappa_surface,
    structural_consistency_soft_jaccard,
)
from evaluation import per_instance_f1


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_samples(path: str) -> list[dict]:
    instances = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                instances.append(json.loads(line))
    return instances


def try_load_logprob_scores(logprob_dir: str, n_expected: int) -> dict | None:
    """Try to load per-instance logprob scores from exp-012 output."""
    if not logprob_dir or not os.path.isdir(logprob_dir):
        return None

    candidates = [
        "logprob_scores.json",
        "per_instance_logprobs.json",
        "analysis_report.json",
        "logprob_data.json",
    ]
    for fname in candidates:
        path = os.path.join(logprob_dir, fname)
        if os.path.exists(path):
            with open(path) as f:
                data = json.load(f)
            if isinstance(data, dict) and "per_instance" in data:
                return data["per_instance"]
            if isinstance(data, list) and len(data) == n_expected:
                return data
            if isinstance(data, dict):
                return data

    # Try loading from samples that might have logprob fields
    samples_path = os.path.join(logprob_dir, "samples.jsonl")
    if os.path.exists(samples_path):
        instances = load_samples(samples_path)
        if instances and "mean_logprob" in instances[0]:
            return [
                {
                    "mean_logprob": inst.get("mean_logprob", 0.0),
                    "greedy_logprob": inst.get("greedy_logprob", 0.0),
                }
                for inst in instances
            ]

    # Try any JSON files in the directory
    for fname in sorted(os.listdir(logprob_dir)):
        if not fname.endswith(".json"):
            continue
        path = os.path.join(logprob_dir, fname)
        try:
            with open(path) as f:
                data = json.load(f)
            if isinstance(data, dict) and "ner_logprob_scores" in data:
                return data
            if isinstance(data, dict) and "logprob_per_instance" in data:
                return data["logprob_per_instance"]
        except (json.JSONDecodeError, KeyError):
            continue

    return None


# ---------------------------------------------------------------------------
# Signal computation
# ---------------------------------------------------------------------------

def compute_exact_match_rate(instances: list[dict], subtask: str) -> list[float]:
    """Fraction of sample pairs with identical surface-key sets."""
    rates = []
    for inst in instances:
        samples = inst["samples"]
        n = len(samples)
        if n < 2:
            rates.append(1.0)
            continue

        sample_keys = []
        for s in samples:
            if subtask == "ner":
                keys = frozenset(
                    (e.get("text", ""), e.get("type", ""))
                    for e in s.get("entities", [])
                )
            elif subtask == "re":
                keys = frozenset(
                    (r.get("head", ""), r.get("tail", ""), r.get("type", ""))
                    for r in s.get("relations", [])
                )
            else:
                keys = frozenset()
            sample_keys.append(keys)

        match_count = 0
        total_pairs = 0
        for i in range(n):
            for j in range(i + 1, n):
                if sample_keys[i] == sample_keys[j]:
                    match_count += 1
                total_pairs += 1
        rates.append(match_count / total_pairs if total_pairs > 0 else 1.0)
    return rates


def compute_voting_confidence(instances: list[dict], subtask: str) -> list[float]:
    """Entity/relation-level majority voting confidence."""
    confidences = []
    for inst in instances:
        samples = inst["samples"]
        n = len(samples)

        counter: Counter = Counter()
        for s in samples:
            if subtask == "ner":
                for e in s.get("entities", []):
                    counter[(e.get("text", ""), e.get("type", ""))] += 1
            elif subtask == "re":
                for r in s.get("relations", []):
                    counter[(r.get("head", ""), r.get("tail", ""), r.get("type", ""))] += 1

        majority_votes = [v / n for v in counter.values() if v > n / 2]
        conf = float(np.mean(majority_votes)) if majority_votes else 0.0
        confidences.append(conf)
    return confidences


def extract_logprob_signals(
    logprob_data: dict | list | None,
    instances: list[dict],
    nonempty_mask: list[bool],
) -> dict[str, list[float]] | None:
    """Extract per-instance logprob signals, filtered by nonempty_mask."""
    if logprob_data is None:
        return None

    n_total = len(instances)
    mean_lp = None
    greedy_lp = None

    if isinstance(logprob_data, list):
        if len(logprob_data) == n_total:
            if isinstance(logprob_data[0], dict):
                mean_lp = [d.get("mean_logprob", 0.0) for d in logprob_data]
                greedy_lp = [d.get("greedy_logprob", 0.0) for d in logprob_data]
            else:
                mean_lp = list(logprob_data)
    elif isinstance(logprob_data, dict):
        if "mean_logprob" in logprob_data:
            mean_lp = logprob_data["mean_logprob"]
            greedy_lp = logprob_data.get("greedy_logprob")
        for key in ["ner_logprob_scores", "re_logprob_scores"]:
            if key in logprob_data:
                sub = logprob_data[key]
                if isinstance(sub, list) and len(sub) == n_total:
                    mean_lp = sub
                    break

    if mean_lp is None:
        return None

    result = {}
    filtered_mean = [v for v, m in zip(mean_lp, nonempty_mask) if m]
    result["logprob"] = filtered_mean

    if greedy_lp is not None and len(greedy_lp) == n_total:
        filtered_greedy = [v for v, m in zip(greedy_lp, nonempty_mask) if m]
        result["greedy_logprob"] = filtered_greedy

    return result


# ---------------------------------------------------------------------------
# Metric computation
# ---------------------------------------------------------------------------

def compute_auroc(signal_values: list[float], f1_values: list[float]) -> float:
    """AUROC with binary label: F1 > median."""
    median_f1 = float(np.median(f1_values))
    labels = [1 if f > median_f1 else 0 for f in f1_values]
    if len(set(labels)) < 2:
        return float("nan")

    # Manual AUROC (no sklearn dependency)
    pos_scores = [s for s, l in zip(signal_values, labels) if l == 1]
    neg_scores = [s for s, l in zip(signal_values, labels) if l == 0]
    if not pos_scores or not neg_scores:
        return float("nan")

    concordant = 0
    tied = 0
    total = len(pos_scores) * len(neg_scores)
    for p in pos_scores:
        for n in neg_scores:
            if p > n:
                concordant += 1
            elif p == n:
                tied += 1
    return (concordant + 0.5 * tied) / total


def compute_calibration_bins(
    signal_values: list[float],
    f1_values: list[float],
    n_bins: int = 10,
) -> list[dict]:
    """Bin samples by confidence signal, compute mean F1 per bin."""
    sig = np.array(signal_values)
    f1s = np.array(f1_values)
    n = len(sig)

    if n < n_bins:
        n_bins = max(1, n)

    sorted_idx = np.argsort(sig)
    bin_size = n // n_bins
    remainder = n % n_bins

    bins = []
    start = 0
    for i in range(n_bins):
        end = start + bin_size + (1 if i < remainder else 0)
        idx = sorted_idx[start:end]
        if len(idx) == 0:
            continue
        bins.append({
            "bin_idx": i,
            "confidence_lo": float(sig[idx[0]]),
            "confidence_hi": float(sig[idx[-1]]),
            "mean_confidence": float(sig[idx].mean()),
            "mean_f1": float(f1s[idx].mean()),
            "std_f1": float(f1s[idx].std()),
            "count": int(len(idx)),
        })
        start = end
    return bins


def compute_bootstrap_ci(
    signal_values: list[float],
    f1_values: list[float],
    n_bootstrap: int = 1000,
    ci: float = 0.95,
    seed: int = 42,
) -> dict:
    """Bootstrap 95% CI for Spearman rho."""
    rng = np.random.RandomState(seed)
    n = len(signal_values)
    sig = np.array(signal_values)
    f1s = np.array(f1_values)

    rho_point, _ = spearmanr(sig, f1s)

    rhos = []
    for _ in range(n_bootstrap):
        idx = rng.choice(n, n, replace=True)
        if len(set(idx)) < 3:
            continue
        r, _ = spearmanr(sig[idx], f1s[idx])
        if not np.isnan(r):
            rhos.append(r)

    if not rhos:
        return {
            "rho_point": float(rho_point),
            "rho_mean": float("nan"),
            "ci_lower": float("nan"),
            "ci_upper": float("nan"),
            "n_valid_bootstrap": 0,
        }

    alpha = (1 - ci) / 2
    return {
        "rho_point": float(rho_point),
        "rho_mean": float(np.mean(rhos)),
        "ci_lower": float(np.percentile(rhos, 100 * alpha)),
        "ci_upper": float(np.percentile(rhos, 100 * (1 - alpha))),
        "n_valid_bootstrap": len(rhos),
    }


# ---------------------------------------------------------------------------
# Leave-one-out SJ
# ---------------------------------------------------------------------------

def compute_loo_sj(instances: list[dict], subtask: str) -> dict:
    """Leave-one-out soft Jaccard vs standard SJ.

    For each instance, computes:
      - standard SJ from all N samples
      - N LOO-SJ values, each dropping one sample
      - mean LOO-SJ
    """
    standard_sjs = []
    loo_mean_sjs = []
    loo_std_sjs = []
    deltas = []

    for inst in instances:
        samples = inst["samples"]
        n = len(samples)

        sj_all = structural_consistency_soft_jaccard(samples, subtask=subtask)
        standard_sjs.append(sj_all)

        if n <= 2:
            loo_mean_sjs.append(sj_all)
            loo_std_sjs.append(0.0)
            deltas.append(0.0)
            continue

        loo_values = []
        for k in range(n):
            samples_minus_k = samples[:k] + samples[k + 1 :]
            sj_loo = structural_consistency_soft_jaccard(samples_minus_k, subtask=subtask)
            loo_values.append(sj_loo)

        loo_mean = float(np.mean(loo_values))
        loo_std = float(np.std(loo_values))
        loo_mean_sjs.append(loo_mean)
        loo_std_sjs.append(loo_std)
        deltas.append(sj_all - loo_mean)

    return {
        "standard_sj": standard_sjs,
        "loo_mean_sj": loo_mean_sjs,
        "loo_std_sj": loo_std_sjs,
        "delta_sj_minus_loo": deltas,
    }


# ---------------------------------------------------------------------------
# Main analysis pipeline
# ---------------------------------------------------------------------------

def analyze_subtask(
    instances: list[dict],
    subtask: str,
    logprob_data: dict | list | None,
) -> dict:
    """Run full analysis for one subtask (NER or RE)."""
    n_total = len(instances)

    # Per-instance greedy F1
    f1_values = [
        per_instance_f1(inst["greedy"], inst["gold"], subtask=subtask)
        for inst in instances
    ]

    # Gold-empty mask
    if subtask == "ner":
        nonempty_mask = [len(inst["gold"].get("entities", [])) > 0 for inst in instances]
    elif subtask == "re":
        nonempty_mask = [len(inst["gold"].get("relations", [])) > 0 for inst in instances]
    else:
        nonempty_mask = [True] * n_total

    filtered_instances = [inst for inst, m in zip(instances, nonempty_mask) if m]
    filtered_f1 = [f for f, m in zip(f1_values, nonempty_mask) if m]
    n_filtered = len(filtered_f1)
    n_gold_empty = n_total - n_filtered

    print(f"  {subtask.upper()}: {n_total} total, {n_filtered} gold-nonempty, {n_gold_empty} gold-empty filtered")

    # Compute consistency signals
    consistency = compute_all_consistency_scores(filtered_instances, subtask=subtask)
    signals: dict[str, list[float]] = {
        "soft_jaccard": list(consistency["soft_jaccard"]),
        "fleiss_kappa": list(consistency["fleiss_kappa"]),
    }
    signals["exact_match"] = compute_exact_match_rate(filtered_instances, subtask)
    signals["voting_confidence"] = compute_voting_confidence(filtered_instances, subtask)

    # Logprob (try to load)
    lp_signals = extract_logprob_signals(logprob_data, instances, nonempty_mask)
    if lp_signals:
        for k, v in lp_signals.items():
            if len(v) == n_filtered:
                signals[k] = v
            else:
                print(f"    WARNING: logprob signal '{k}' has {len(v)} values, expected {n_filtered}, skipping")

    # ---- Compute metrics for each signal ----
    metrics = {}
    calibration = {}
    bootstrap = {}

    for sig_name, sig_values in signals.items():
        assert len(sig_values) == n_filtered, f"{sig_name}: {len(sig_values)} != {n_filtered}"

        rho, p_rho = spearmanr(sig_values, filtered_f1)
        tau, p_tau = kendalltau(sig_values, filtered_f1)
        auroc = compute_auroc(sig_values, filtered_f1)

        metrics[sig_name] = {
            "n": n_filtered,
            "spearman_rho": round(float(rho), 4),
            "spearman_p": float(p_rho),
            "kendall_tau": round(float(tau), 4),
            "kendall_p": float(p_tau),
            "auroc": round(float(auroc), 4) if not np.isnan(auroc) else None,
        }

        calibration[sig_name] = compute_calibration_bins(sig_values, filtered_f1)
        bootstrap[sig_name] = compute_bootstrap_ci(sig_values, filtered_f1)

        print(f"    {sig_name:25s}  rho={rho:+.4f}  tau={tau:+.4f}  AUROC={auroc:.4f}  "
              f"CI=[{bootstrap[sig_name]['ci_lower']:.4f}, {bootstrap[sig_name]['ci_upper']:.4f}]")

    # ---- LOO SJ ----
    print(f"  Computing LOO-SJ for {subtask.upper()} ({n_filtered} instances)...")
    loo_result = compute_loo_sj(filtered_instances, subtask)

    # LOO SJ correlation with F1
    loo_rho, loo_p = spearmanr(loo_result["loo_mean_sj"], filtered_f1)
    std_rho = metrics["soft_jaccard"]["spearman_rho"]
    loo_result["loo_sj_rho"] = round(float(loo_rho), 4)
    loo_result["loo_sj_p"] = float(loo_p)
    loo_result["standard_sj_rho"] = std_rho
    loo_result["rho_delta_std_minus_loo"] = round(std_rho - float(loo_rho), 4)
    loo_result["mean_delta_sj_minus_loo"] = round(float(np.mean(loo_result["delta_sj_minus_loo"])), 6)
    loo_result["std_delta_sj_minus_loo"] = round(float(np.std(loo_result["delta_sj_minus_loo"])), 6)
    loo_result["correlation_std_vs_loo"] = round(
        float(np.corrcoef(loo_result["standard_sj"], loo_result["loo_mean_sj"])[0, 1]), 4
    )

    # Remove per-instance arrays from summary (keep for detailed output)
    loo_summary = {k: v for k, v in loo_result.items()
                   if k not in ("standard_sj", "loo_mean_sj", "loo_std_sj", "delta_sj_minus_loo")}

    print(f"    LOO-SJ rho={loo_rho:+.4f} vs standard SJ rho={std_rho:+.4f} (delta={std_rho - loo_rho:+.4f})")
    print(f"    LOO-SJ vs standard SJ pearson r={loo_result['correlation_std_vs_loo']:.4f}")

    return {
        "n_total": n_total,
        "n_gold_empty": n_gold_empty,
        "n_filtered": n_filtered,
        "metrics": metrics,
        "calibration": calibration,
        "bootstrap": bootstrap,
        "loo_sj": loo_summary,
        "loo_sj_detail": {
            "standard_sj": [round(v, 6) for v in loo_result["standard_sj"]],
            "loo_mean_sj": [round(v, 6) for v in loo_result["loo_mean_sj"]],
        },
    }


def main():
    parser = argparse.ArgumentParser(description="exp-015: Extended evaluation metrics")
    parser.add_argument("--pilot_dir", type=str,
                        default="/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004")
    parser.add_argument("--logprob_dir", type=str,
                        default="/root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob")
    parser.add_argument("--output_dir", type=str,
                        default="/root/autodl-tmp/struct_self_consist_ie/output/exp015_metrics_expansion")
    parser.add_argument("--n_bootstrap", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    np.random.seed(args.seed)

    # Load data
    samples_path = os.path.join(args.pilot_dir, "samples.jsonl")
    print(f"Loading samples from {samples_path}...")
    instances = load_samples(samples_path)
    print(f"Loaded {len(instances)} instances")

    # Try to load logprob data
    logprob_data = try_load_logprob_scores(args.logprob_dir, len(instances))
    if logprob_data is not None:
        print(f"Loaded logprob data from {args.logprob_dir}")
    else:
        print(f"WARNING: No logprob data found in {args.logprob_dir}, skipping logprob signal")

    # Analyze NER
    print("\n" + "=" * 70)
    print("  NER Analysis")
    print("=" * 70)
    ner_results = analyze_subtask(instances, "ner", logprob_data)

    # Analyze RE
    print("\n" + "=" * 70)
    print("  RE Analysis")
    print("=" * 70)
    re_results = analyze_subtask(instances, "re", logprob_data)

    # ---- Save outputs ----
    def save_json(data, filename):
        path = os.path.join(args.output_dir, filename)
        with open(path, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Saved {path}")

    # 1. Full metrics per subtask
    ner_metrics_out = {
        "subtask": "ner",
        "n_total": ner_results["n_total"],
        "n_filtered": ner_results["n_filtered"],
        "n_gold_empty": ner_results["n_gold_empty"],
        "signals": ner_results["metrics"],
    }
    re_metrics_out = {
        "subtask": "re",
        "n_total": re_results["n_total"],
        "n_filtered": re_results["n_filtered"],
        "n_gold_empty": re_results["n_gold_empty"],
        "signals": re_results["metrics"],
    }
    save_json(ner_metrics_out, "ner_full_metrics.json")
    save_json(re_metrics_out, "re_full_metrics.json")

    # 2. Calibration data
    calibration_out = {
        "ner": ner_results["calibration"],
        "re": re_results["calibration"],
    }
    save_json(calibration_out, "calibration_data.json")

    # 3. Bootstrap CI
    bootstrap_out = {
        "ner": ner_results["bootstrap"],
        "re": re_results["bootstrap"],
        "n_bootstrap": args.n_bootstrap,
        "ci_level": 0.95,
        "seed": args.seed,
    }
    save_json(bootstrap_out, "bootstrap_ci.json")

    # 4. LOO SJ comparison
    loo_out = {
        "ner": {
            "summary": ner_results["loo_sj"],
            "per_instance": ner_results["loo_sj_detail"],
        },
        "re": {
            "summary": re_results["loo_sj"],
            "per_instance": re_results["loo_sj_detail"],
        },
    }
    save_json(loo_out, "loo_sj_comparison.json")

    # ---- Print summary table ----
    print("\n" + "=" * 70)
    print("  SUMMARY: All Signals × All Metrics")
    print("=" * 70)
    for st_name, st_results in [("NER", ner_results), ("RE", re_results)]:
        print(f"\n  {st_name} (n={st_results['n_filtered']})")
        print(f"  {'Signal':25s} | {'rho':>7s} | {'tau':>7s} | {'AUROC':>7s} | {'CI_lo':>7s} | {'CI_hi':>7s}")
        print("  " + "-" * 72)
        for sig_name in ["soft_jaccard", "fleiss_kappa", "logprob", "exact_match", "voting_confidence"]:
            if sig_name not in st_results["metrics"]:
                print(f"  {sig_name:25s} |    N/A  |    N/A  |    N/A  |    N/A  |    N/A")
                continue
            m = st_results["metrics"][sig_name]
            b = st_results["bootstrap"][sig_name]
            auroc_str = f"{m['auroc']:.4f}" if m["auroc"] is not None else "  N/A "
            print(f"  {sig_name:25s} | {m['spearman_rho']:+.4f} | {m['kendall_tau']:+.4f} | "
                  f"{auroc_str} | {b['ci_lower']:+.4f} | {b['ci_upper']:+.4f}")

    print(f"\n  LOO-SJ Analysis:")
    for st_name, st_results in [("NER", ner_results), ("RE", re_results)]:
        loo = st_results["loo_sj"]
        print(f"    {st_name}: standard rho={loo['standard_sj_rho']:+.4f}, "
              f"LOO rho={loo['loo_sj_rho']:+.4f}, "
              f"delta={loo['rho_delta_std_minus_loo']:+.4f}, "
              f"std-vs-loo r={loo['correlation_std_vs_loo']:.4f}")

    print(f"\nAll outputs saved to {args.output_dir}")


if __name__ == "__main__":
    main()

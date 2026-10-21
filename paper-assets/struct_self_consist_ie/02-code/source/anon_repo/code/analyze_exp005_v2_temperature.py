"""exp-005 v2: Temperature sensitivity analysis — T=0.7 vs T=1.0 across 5 signals.

Signals: soft_jaccard (SJ), fleiss_kappa (FK), mean_logprob, exact_match (EM), voting_conf
Metrics: Spearman rho, AUROC, Kendall tau
Includes bootstrap CI for Delta values and conditional filtering comparison.
"""

import json
import os
import sys
from collections import Counter

import numpy as np
from scipy.stats import spearmanr, kendalltau

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import compute_all_consistency_scores
from evaluation import per_instance_f1

BASE = "/root/autodl-tmp/struct_self_consist_ie/output"
PILOT_004 = os.path.join(BASE, "mvp_pilot_004/samples.jsonl")
PILOT_005 = os.path.join(BASE, "mvp_pilot_005/samples.jsonl")
EXP_012   = os.path.join(BASE, "exp_012_logprob/samples_with_logprobs.jsonl")
OUTPUT_DIR = os.path.join(BASE, "exp_005_v2_temperature")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def auroc_simple(scores, labels):
    scores = np.array(scores, dtype=float)
    labels = np.array(labels, dtype=int)
    if len(set(labels)) < 2:
        return float('nan')
    pos = scores[labels == 1]
    neg = scores[labels == 0]
    if len(pos) == 0 or len(neg) == 0:
        return float('nan')
    count = sum(np.sum(p > neg) + 0.5 * np.sum(p == neg) for p in pos)
    return count / (len(pos) * len(neg))


def compute_exact_match_rate(samples, subtask):
    if subtask == "ner":
        keys = [frozenset((e["text"], e["type"]) for e in s.get("entities", [])) for s in samples]
    else:
        keys = [frozenset((r["head"], r["tail"], r["type"]) for r in s.get("relations", [])) for s in samples]
    counter = Counter(keys)
    return counter.most_common(1)[0][1] / len(samples)


def compute_voting_confidence(samples, subtask):
    N = len(samples)
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
    return float(np.mean([v / N for v in counter.values()]))


def compute_mean_logprob(samples):
    lps = [s.get("mean_logprob") for s in samples if s.get("mean_logprob") is not None]
    lps = [lp for lp in lps if np.isfinite(lp)]
    return float(np.mean(lps)) if lps else float("nan")


def compute_signals(instances, subtask, has_logprob=False):
    consistency = compute_all_consistency_scores(instances, subtask=subtask)
    signals = {
        "soft_jaccard": consistency["soft_jaccard"],
        "fleiss_kappa": consistency["fleiss_kappa"],
        "exact_match": [],
        "voting_conf": [],
    }
    if has_logprob:
        signals["mean_logprob"] = []

    f1_scores = []
    for inst in instances:
        samples = inst["samples"]
        gold = inst["gold"]
        greedy = inst.get("greedy")
        f1 = per_instance_f1(greedy if greedy else samples[0], gold, subtask=subtask)
        f1_scores.append(f1)
        signals["exact_match"].append(compute_exact_match_rate(samples, subtask))
        signals["voting_conf"].append(compute_voting_confidence(samples, subtask))
        if has_logprob:
            signals["mean_logprob"].append(compute_mean_logprob(samples))

    return signals, f1_scores


def compute_metrics(signal_values, f1_values):
    x = np.array(signal_values, dtype=float)
    y = np.array(f1_values, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y)
    x, y = x[mask], y[mask]
    if len(x) < 3:
        return {"rho": float("nan"), "tau": float("nan"), "auroc": float("nan"), "n": int(len(x))}
    rho_r = spearmanr(x, y)
    tau_r = kendalltau(x, y)
    median_f1 = float(np.median(y))
    labels = (y >= median_f1).astype(int)
    if len(set(labels)) < 2:
        labels = (y > median_f1).astype(int)
    auroc = auroc_simple(x, labels)
    return {
        "rho": round(float(rho_r.statistic), 4),
        "tau": round(float(tau_r.statistic), 4),
        "auroc": round(float(auroc), 4),
        "n": int(len(x)),
    }


def bootstrap_delta(sig_07, sig_10, f1_07, f1_10, n_boot=10000, seed=42):
    rng = np.random.RandomState(seed)
    a07 = np.array(sig_07, dtype=float)
    a10 = np.array(sig_10, dtype=float)
    y07 = np.array(f1_07, dtype=float)
    y10 = np.array(f1_10, dtype=float)

    mask07 = np.isfinite(a07) & np.isfinite(y07)
    mask10 = np.isfinite(a10) & np.isfinite(y10)

    a07m, y07m = a07[mask07], y07[mask07]
    a10m, y10m = a10[mask10], y10[mask10]

    n07, n10 = len(a07m), len(a10m)
    diffs = np.empty(n_boot)
    for i in range(n_boot):
        idx07 = rng.randint(0, n07, size=n07)
        idx10 = rng.randint(0, n10, size=n10)
        rho07 = spearmanr(a07m[idx07], y07m[idx07]).statistic
        rho10 = spearmanr(a10m[idx10], y10m[idx10]).statistic
        diffs[i] = rho07 - rho10

    return {
        "mean_delta": round(float(np.mean(diffs)), 4),
        "ci_low": round(float(np.percentile(diffs, 2.5)), 4),
        "ci_high": round(float(np.percentile(diffs, 97.5)), 4),
    }


def conditional_filter(signals, f1_scores, subtask_label):
    valid = [i for i, f in enumerate(f1_scores) if f > 0]
    if len(valid) < 3:
        return {s: {"rho": float("nan"), "tau": float("nan"), "auroc": float("nan"), "n": len(valid)} for s in signals}, len(valid)
    filtered = {}
    for sig_name, sig_vals in signals.items():
        filt_sig = [sig_vals[i] for i in valid]
        filt_f1 = [f1_scores[i] for i in valid]
        m = compute_metrics(filt_sig, filt_f1)
        filtered[sig_name] = m
    return filtered, len(valid)


def classify_sensitivity(delta_rho):
    abs_d = abs(delta_rho)
    if abs_d <= 0.01:
        return "ROBUST"
    elif abs_d <= 0.05:
        return "MODERATE"
    else:
        return "SENSITIVE"


def main():
    print("Loading data...")
    data_04 = load_data(PILOT_004)
    data_05 = load_data(PILOT_005)
    data_12 = load_data(EXP_012)
    print(f"  pilot_004 (T=1.0): {len(data_04)} instances")
    print(f"  pilot_005 (T=0.7): {len(data_05)} instances")
    print(f"  exp_012   (T=1.0+lp): {len(data_12)} instances")

    results = {}

    for subtask in ["ner", "re"]:
        print(f"\n{'='*60}")
        print(f"  Subtask: {subtask.upper()}")
        print(f"{'='*60}")

        sig_10, f1_10 = compute_signals(data_04, subtask, has_logprob=False)
        sig_07, f1_07 = compute_signals(data_05, subtask, has_logprob=False)
        sig_12, f1_12 = compute_signals(data_12, subtask, has_logprob=True)

        sig_10["mean_logprob"] = sig_12["mean_logprob"]
        f1_10_lp = f1_12

        all_signals = ["soft_jaccard", "fleiss_kappa", "exact_match", "voting_conf", "mean_logprob"]

        subtask_results = {"full": {}, "conditional": {}, "bootstrap": {}, "sensitivity": {}}

        print(f"\n--- Full-set metrics ---")
        print(f"{'Signal':<16} | {'T=0.7 rho':>10} {'AUROC':>8} {'tau':>8} | {'T=1.0 rho':>10} {'AUROC':>8} {'tau':>8} | {'Delta_rho':>10} {'Class':>10}")
        print("-" * 110)

        for sig_name in all_signals:
            if sig_name == "mean_logprob":
                m10 = compute_metrics(sig_10[sig_name], f1_10_lp)
                m07 = {"rho": float("nan"), "tau": float("nan"), "auroc": float("nan"), "n": 0}
                delta_rho = float("nan")
                cls = "N/A"
                boot = {"mean_delta": float("nan"), "ci_low": float("nan"), "ci_high": float("nan")}
            else:
                m10 = compute_metrics(sig_10[sig_name], f1_10)
                m07 = compute_metrics(sig_07[sig_name], f1_07)
                boot = bootstrap_delta(sig_07[sig_name], sig_10[sig_name], f1_07, f1_10)
                delta_rho = round(m07["rho"] - m10["rho"], 4)
                cls = classify_sensitivity(delta_rho)

            subtask_results["full"][sig_name] = {
                "T07": m07, "T10": m10,
                "delta_rho": delta_rho,
                "sensitivity": cls,
            }
            subtask_results["bootstrap"][sig_name] = boot

            rho07_s = f"{m07['rho']:.4f}" if not np.isnan(m07['rho']) else "N/A"
            auroc07_s = f"{m07['auroc']:.4f}" if not np.isnan(m07['auroc']) else "N/A"
            tau07_s = f"{m07['tau']:.4f}" if not np.isnan(m07['tau']) else "N/A"
            delta_s = f"{delta_rho:+.4f}" if not np.isnan(delta_rho) else "N/A"

            print(f"{sig_name:<16} | {rho07_s:>10} {auroc07_s:>8} {tau07_s:>8} | {m10['rho']:>10.4f} {m10['auroc']:>8.4f} {m10['tau']:>8.4f} | {delta_s:>10} {cls:>10}")

        print(f"\n--- Bootstrap 95% CI for Delta_rho (T=0.7 - T=1.0, n_boot=10000) ---")
        for sig_name in all_signals:
            b = subtask_results["bootstrap"][sig_name]
            if np.isnan(b["mean_delta"]):
                print(f"  {sig_name:<16}: N/A (logprob not available at T=0.7)")
            else:
                print(f"  {sig_name:<16}: mean={b['mean_delta']:+.4f}  95% CI=[{b['ci_low']:+.4f}, {b['ci_high']:+.4f}]")

        print(f"\n--- Temperature sensitivity classification ---")
        for sig_name in all_signals:
            cls = subtask_results["full"][sig_name]["sensitivity"]
            delta = subtask_results["full"][sig_name]["delta_rho"]
            if cls == "N/A":
                print(f"  {sig_name:<16}: N/A (no T=0.7 logprob data)")
            else:
                print(f"  {sig_name:<16}: {cls} (Delta_rho = {delta:+.4f})")

        print(f"\n--- Conditional filtering (exclude greedy_F1=0) ---")
        cond_07, n_cond_07 = conditional_filter(sig_07, f1_07, subtask)
        cond_10_signals = {k: v for k, v in sig_10.items() if k != "mean_logprob"}
        cond_10, n_cond_10 = conditional_filter(cond_10_signals, f1_10, subtask)
        cond_12_signals = {"mean_logprob": sig_12["mean_logprob"]}
        cond_12, n_cond_12 = conditional_filter(cond_12_signals, f1_12, subtask)

        print(f"  T=0.7: {n_cond_07}/{len(f1_07)} instances (excluded {len(f1_07)-n_cond_07} zero-F1)")
        print(f"  T=1.0: {n_cond_10}/{len(f1_10)} instances (excluded {len(f1_10)-n_cond_10} zero-F1)")

        print(f"\n{'Signal':<16} | {'Cond T=0.7 rho':>15} {'AUROC':>8} | {'Cond T=1.0 rho':>15} {'AUROC':>8} | {'Cond Delta_rho':>15}")
        print("-" * 95)

        for sig_name in all_signals:
            if sig_name == "mean_logprob":
                c10 = cond_12.get(sig_name, {"rho": float("nan"), "auroc": float("nan")})
                c07_rho = "N/A"
                c07_auroc = "N/A"
                cdelta = "N/A"
            else:
                c07 = cond_07.get(sig_name, {"rho": float("nan"), "auroc": float("nan")})
                c10 = cond_10.get(sig_name, {"rho": float("nan"), "auroc": float("nan")})
                c07_rho = f"{c07['rho']:.4f}"
                c07_auroc = f"{c07['auroc']:.4f}"
                cdelta = f"{c07['rho'] - c10['rho']:+.4f}"

            subtask_results["conditional"][sig_name] = {
                "T07": cond_07.get(sig_name, {}),
                "T10": cond_10.get(sig_name, cond_12.get(sig_name, {})),
            }

            print(f"{sig_name:<16} | {c07_rho:>15} {c07_auroc:>8} | {c10['rho']:>15.4f} {c10['auroc']:>8.4f} | {cdelta:>15}")

        print(f"\n--- Conditional filtering improvement (Delta_rho: conditional - full) ---")
        for sig_name in ["soft_jaccard", "fleiss_kappa", "exact_match", "voting_conf"]:
            full_07 = subtask_results["full"][sig_name]["T07"]["rho"]
            full_10 = subtask_results["full"][sig_name]["T10"]["rho"]
            cond_07_rho = cond_07[sig_name]["rho"]
            cond_10_rho = cond_10[sig_name]["rho"]
            imp_07 = cond_07_rho - full_07
            imp_10 = cond_10_rho - full_10
            print(f"  {sig_name:<16}: T=0.7 improvement={imp_07:+.4f}, T=1.0 improvement={imp_10:+.4f}")

        results[subtask] = subtask_results

    print(f"\n{'='*60}")
    print("  SUMMARY")
    print(f"{'='*60}")
    print("\nTemperature sensitivity per signal (both NER and RE):")
    for sig_name in ["soft_jaccard", "fleiss_kappa", "exact_match", "voting_conf"]:
        ner_cls = results["ner"]["full"][sig_name]["sensitivity"]
        re_cls = results["re"]["full"][sig_name]["sensitivity"]
        ner_d = results["ner"]["full"][sig_name]["delta_rho"]
        re_d = results["re"]["full"][sig_name]["delta_rho"]
        both_robust = ner_cls == "ROBUST" and re_cls == "ROBUST"
        marker = "  <<< ROBUST" if both_robust else ""
        print(f"  {sig_name:<16}: NER={ner_cls}(Delta={ner_d:+.4f}), RE={re_cls}(Delta={re_d:+.4f}){marker}")

    print("\nConditional filtering vs temperature tuning:")
    for subtask in ["ner", "re"]:
        deltas = [abs(results[subtask]["full"][s]["delta_rho"])
                  for s in ["soft_jaccard", "fleiss_kappa", "exact_match", "voting_conf"]]
        max_temp_delta = max(deltas)
        cond_imps = []
        for s in ["soft_jaccard", "fleiss_kappa", "exact_match", "voting_conf"]:
            full_rho = results[subtask]["full"][s]["T10"]["rho"]
            cond_rho = results[subtask]["conditional"][s].get("T10", {}).get("rho", full_rho)
            cond_imps.append(abs(cond_rho - full_rho))
        max_cond_imp = max(cond_imps)
        print(f"  {subtask.upper()}: max |temp delta|={max_temp_delta:.4f}, max |cond improvement|={max_cond_imp:.4f}")

    output = {
        "experiment": "exp_005_v2",
        "description": "Temperature sensitivity analysis: T=0.7 vs T=1.0 across 5 signals",
        "data_sources": {
            "T10": "mvp_pilot_004 (551 instances, N=8, T=1.0)",
            "T07": "mvp_pilot_005 (551 instances, N=8, T=0.7)",
            "T10_logprob": "exp_012_logprob (551 instances, N=8, T=1.0, with logprobs)",
        },
        "results": {}
    }
    for subtask in ["ner", "re"]:
        output["results"][subtask] = results[subtask]

    report_path = os.path.join(OUTPUT_DIR, "temperature_sensitivity_report.json")
    with open(report_path, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nReport saved to: {report_path}")


if __name__ == "__main__":
    main()

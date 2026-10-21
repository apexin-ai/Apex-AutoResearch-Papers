"""
exp-008 Signal Survival Analysis v4 (D021 corrected)

Key corrections from v3:
- d000/d005: within-model AUC (d005 labels)
- d100: cross-model paired comparison (d100 vs d000), NOT within-model AUC
  (d100 has all items contaminated → no negative class → AUC meaningless)
"""
import json
import os
import numpy as np
from pathlib import Path
from scipy import stats
from sklearn.metrics import roc_auc_score

SIGNALS_DIR = Path("/root/autodl-tmp/exp002/signals")
LABELS_DIR = Path("/root/autodl-tmp/exp001/sft_data")
OUTPUT_DIR = Path("/root/contamcal-irt-calibration/exp008/exp008_v4_output")

BENCHMARKS = ["mmlu", "gsm8k", "arc_challenge"]
SIGNAL_KEYS = ["s1_embedding", "s2_minkpp", "s4_selfcritique"]
SIGNAL_NAMES = {"s1_embedding": "S1_Embedding", "s2_minkpp": "S2_MinKPP", "s4_selfcritique": "S4_SelfCritique"}

REGIME_DIRS = {
    "d000": "Qwen2.5-0.5B_d000_s42",
    "d005": "Qwen2.5-0.5B_d005_s42",
    "d100": "Qwen2.5-0.5B_d100_s42",
}


def load_signals(regime, bench):
    path = SIGNALS_DIR / REGIME_DIRS[regime] / f"signals_merged_{bench}.json"
    with open(path) as f:
        items = json.load(f)
    return {item["index"]: item for item in items}


def load_labels(bench):
    path = LABELS_DIR / f"contamination_labels_{bench}_d005.json"
    with open(path) as f:
        data = json.load(f)
    return data["labels"], data["total_items"], data["contaminated_count"]


def within_model_auc(signals_dict, labels, signal_key):
    indices = sorted(set(signals_dict.keys()) & set(range(len(labels))))
    y = np.array([labels[i] for i in indices])
    scores = np.array([signals_dict[i][signal_key] for i in indices])

    valid = ~np.isnan(scores) & ~np.isinf(scores)
    y, scores = y[valid], scores[valid]

    if len(np.unique(y)) < 2:
        return {"auc": None, "n_pos": int(y.sum()), "n_neg": int((1 - y).sum()),
                "n_total": len(y), "note": "single class - AUC undefined"}

    auc = roc_auc_score(y, scores)
    return {"auc": round(float(auc), 6), "n_pos": int(y.sum()), "n_neg": int(len(y) - y.sum()),
            "n_total": len(y)}


def cross_model_comparison(signals_d100, signals_d000, signal_key):
    common = sorted(set(signals_d100.keys()) & set(signals_d000.keys()))
    vals_100 = np.array([signals_d100[i][signal_key] for i in common])
    vals_000 = np.array([signals_d000[i][signal_key] for i in common])

    valid = ~np.isnan(vals_100) & ~np.isnan(vals_000) & ~np.isinf(vals_100) & ~np.isinf(vals_000)
    vals_100, vals_000 = vals_100[valid], vals_000[valid]
    n = len(vals_100)

    diff = vals_100 - vals_000
    mean_diff = float(np.mean(diff))
    std_diff = float(np.std(diff, ddof=1)) if n > 1 else 0.0
    cohens_d = mean_diff / std_diff if std_diff > 0 else float("inf")

    stat, p_value = stats.wilcoxon(vals_100, vals_000, alternative="two-sided")

    pct_higher = float(np.mean(diff > 0))
    pct_lower = float(np.mean(diff < 0))

    return {
        "n_items": n,
        "mean_d100": round(float(np.mean(vals_100)), 6),
        "mean_d000": round(float(np.mean(vals_000)), 6),
        "mean_diff": round(mean_diff, 6),
        "std_diff": round(std_diff, 6),
        "cohens_d": round(float(cohens_d), 4),
        "wilcoxon_stat": round(float(stat), 2),
        "wilcoxon_p": float(p_value),
        "pct_d100_higher": round(pct_higher, 4),
        "pct_d100_lower": round(pct_lower, 4),
        "significant_0.05": p_value < 0.05,
        "significant_0.01": p_value < 0.01,
        "significant_bonferroni": p_value < 0.05 / (len(SIGNAL_KEYS) * len(BENCHMARKS)),
    }


def analyze_benchmark(bench):
    labels, total, n_contam = load_labels(bench)
    sig_d000 = load_signals("d000", bench)
    sig_d005 = load_signals("d005", bench)
    sig_d100 = load_signals("d100", bench)

    result = {
        "benchmark": bench,
        "n_items": total,
        "n_contaminated_d005": n_contam,
        "within_model_auc": {"d000": {}, "d005": {}},
        "cross_model_d100_vs_d000": {},
    }

    for sk in SIGNAL_KEYS:
        sname = SIGNAL_NAMES[sk]
        result["within_model_auc"]["d000"][sname] = within_model_auc(sig_d000, labels, sk)
        result["within_model_auc"]["d005"][sname] = within_model_auc(sig_d005, labels, sk)
        result["cross_model_d100_vs_d000"][sname] = cross_model_comparison(sig_d100, sig_d000, sk)

    return result


def build_heatmap(results):
    heatmap = {}
    for sname in SIGNAL_NAMES.values():
        heatmap[sname] = {}
        for bench, res in results.items():
            d000_auc = res["within_model_auc"]["d000"][sname]["auc"]
            d005_auc = res["within_model_auc"]["d005"][sname]["auc"]
            cross = res["cross_model_d100_vs_d000"][sname]
            heatmap[sname][bench] = {
                "d000_auc": d000_auc,
                "d005_auc": d005_auc,
                "d100_cross_model_effect": cross["cohens_d"],
                "d100_cross_model_p": cross["wilcoxon_p"],
                "d100_cross_model_significant": cross["significant_bonferroni"],
            }
    return heatmap


def build_summary(results, heatmap):
    findings = []

    for sname in SIGNAL_NAMES.values():
        d005_aucs = [heatmap[sname][b]["d005_auc"] for b in BENCHMARKS if heatmap[sname][b]["d005_auc"] is not None]
        d000_aucs = [heatmap[sname][b]["d000_auc"] for b in BENCHMARKS if heatmap[sname][b]["d000_auc"] is not None]
        cross_sig = [heatmap[sname][b]["d100_cross_model_significant"] for b in BENCHMARKS]
        cross_effects = [heatmap[sname][b]["d100_cross_model_effect"] for b in BENCHMARKS]

        findings.append({
            "signal": sname,
            "d005_auc_mean": round(np.mean(d005_aucs), 4) if d005_aucs else None,
            "d005_auc_range": [round(min(d005_aucs), 4), round(max(d005_aucs), 4)] if d005_aucs else None,
            "d000_sanity_check": "PASS" if all(a is not None and 0.45 <= a <= 0.55 for a in d000_aucs) else "MARGINAL" if all(a is not None and 0.40 <= a <= 0.60 for a in d000_aucs) else "FAIL",
            "d100_cross_model_any_significant": any(cross_sig),
            "d100_cross_model_effects": [round(e, 4) for e in cross_effects],
        })

    effective_signals = [f for f in findings if f["d005_auc_mean"] is not None and f["d005_auc_mean"] > 0.65]

    return {
        "version": "v4_D021_corrected",
        "correction_notes": [
            "d100 within-model AUC removed (label artifact: all items contaminated → no negative class)",
            "d100 now uses cross-model paired comparison (d100 vs d000 signal differences)",
            "C2 claim weakened: 'systematic signal variation with dosage' instead of 'cliff-like RL degradation'",
        ],
        "key_findings": findings,
        "effective_signal_count": len(effective_signals),
        "narrative": (
            f"{len(effective_signals)}/{len(SIGNAL_KEYS)} signals show effective contamination detection at d005. "
            "Signal effectiveness varies systematically with dosage; individual signals insufficient → "
            "need IRT multi-signal fusion for robust detection across regimes."
        ),
    }


def print_results(results, heatmap, summary):
    print("\n" + "=" * 70)
    print("exp-008 Signal Survival Analysis v4 (D021 corrected)")
    print("=" * 70)

    print("\n--- Within-Model AUC Heatmap (d000 sanity / d005 detection) ---")
    header = f"{'Signal':<20} {'Regime':<8}"
    for b in BENCHMARKS:
        header += f" {b:>15}"
    print(header)
    print("-" * len(header))

    for sname in SIGNAL_NAMES.values():
        row_d000 = f"{sname:<20} {'d000':<8}"
        row_d005 = f"{'':<20} {'d005':<8}"
        for b in BENCHMARKS:
            a0 = heatmap[sname][b]["d000_auc"]
            a5 = heatmap[sname][b]["d005_auc"]
            row_d000 += f" {a0:>15.4f}" if a0 is not None else f" {'N/A':>15}"
            row_d005 += f" {a5:>15.4f}" if a5 is not None else f" {'N/A':>15}"
        print(row_d000)
        print(row_d005)
        print()

    print("\n--- Cross-Model Effect (d100 vs d000) ---")
    header2 = f"{'Signal':<20}"
    for b in BENCHMARKS:
        header2 += f" {b + ' (d|p)':>25}"
    print(header2)
    print("-" * len(header2))

    for sname in SIGNAL_NAMES.values():
        row = f"{sname:<20}"
        for b in BENCHMARKS:
            d = heatmap[sname][b]["d100_cross_model_effect"]
            p = heatmap[sname][b]["d100_cross_model_p"]
            sig = "*" if heatmap[sname][b]["d100_cross_model_significant"] else ""
            row += f" {d:>8.3f} (p={p:.2e}){sig:>3}"
        print(row)

    print("\n--- Summary ---")
    print(summary["narrative"])
    for f in summary["key_findings"]:
        print(f"  {f['signal']}: d005 AUC={f['d005_auc_mean']}, d000 sanity={f['d000_sanity_check']}, "
              f"d100 cross-model sig={f['d100_cross_model_any_significant']}")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    results = {}
    for bench in BENCHMARKS:
        print(f"Processing {bench}...")
        results[bench] = analyze_benchmark(bench)

    heatmap = build_heatmap(results)
    summary = build_summary(results, heatmap)

    full_output = {
        "experiment": "exp-008",
        "version": "v4_D021_corrected",
        "per_benchmark": results,
        "heatmap": heatmap,
        "summary": summary,
    }

    out_file = OUTPUT_DIR / "exp008_v4_results.json"
    with open(out_file, "w") as f:
        json.dump(full_output, f, indent=2, default=str)
    print(f"\nResults saved to {out_file}")

    print_results(results, heatmap, summary)


if __name__ == "__main__":
    main()

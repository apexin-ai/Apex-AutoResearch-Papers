"""Direction E: Selective Abstention via per-question consistency calibration.
Evaluates accuracy-coverage tradeoff using entropy/majority-fraction as routing signals.
"""

import json
import math
import os
import sys
from collections import Counter
from pathlib import Path

VALID_ANSWERS = {"True", "False", "Unknown"}

def load_results(path):
    """Load experiment results JSON, return list of per-question dicts."""
    with open(path) as f:
        data = json.load(f)
    return data["results"], data["summary"]

def compute_per_question_metrics(results):
    """Compute majority_fraction, entropy, sc_correct, sica_correct per question."""
    records = []
    for r in results:
        dist = r["sc_vote_distribution"]
        # filter to valid answers only, count total valid votes
        valid_counts = {k: v for k, v in dist.items() if k in VALID_ANSWERS}
        total_valid = sum(valid_counts.values())
        if total_valid == 0:
            continue

        majority_frac = max(valid_counts.values()) / total_valid
        entropy = 0.0
        for cnt in valid_counts.values():
            p = cnt / total_valid
            if p > 0:
                entropy -= p * math.log2(p)

        records.append({
            "problem_id": r["problem_id"],
            "ground_truth": r["ground_truth"],
            "sc_answer": r["sc_answer"],
            "sc_correct": r["sc_correct"],
            "sica_answer": r.get("sica_answer"),
            "sica_correct": r.get("sica_correct"),
            "majority_fraction": majority_frac,
            "entropy": entropy,
            "vote_distribution": valid_counts,
            "total_valid_votes": total_valid,
        })
    return records

def selective_abstention_by_metric(records, metric_key, ascending=True, coverages=None):
    """Rank questions by metric, abstain from hardest ones at each coverage level.

    ascending=True means lower metric = more confident (e.g., entropy).
    ascending=False means higher metric = more confident (e.g., majority_fraction).
    """
    if coverages is None:
        coverages = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5]

    sorted_recs = sorted(records, key=lambda x: x[metric_key], reverse=not ascending)
    n = len(sorted_recs)

    results = {}
    for cov in coverages:
        k = max(1, int(round(n * cov)))
        subset = sorted_recs[:k]
        sc_acc = sum(1 for r in subset if r["sc_correct"]) / len(subset)
        sica_acc = sum(1 for r in subset if r.get("sica_correct")) / len(subset)
        results[cov] = {
            "coverage": cov,
            "n_answered": len(subset),
            "n_total": n,
            "sc_accuracy": sc_acc,
            "sica_accuracy": sica_acc,
        }
    return results

def random_abstention(records, coverages=None, n_trials=1000, seed=42):
    """Baseline: random abstention at each coverage level (averaged over trials)."""
    import random
    rng = random.Random(seed)
    if coverages is None:
        coverages = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5]

    n = len(records)
    results = {}
    for cov in coverages:
        k = max(1, int(round(n * cov)))
        sc_accs = []
        for _ in range(n_trials):
            subset = rng.sample(records, k)
            sc_accs.append(sum(1 for r in subset if r["sc_correct"]) / len(subset))
        results[cov] = {
            "coverage": cov,
            "n_answered": k,
            "n_total": n,
            "sc_accuracy_mean": sum(sc_accs) / len(sc_accs),
            "sc_accuracy_std": (sum((x - sum(sc_accs)/len(sc_accs))**2 for x in sc_accs) / len(sc_accs)) ** 0.5,
        }
    return results

def compute_auroc(records):
    """AUROC: entropy as predictor of SC being wrong (higher entropy → more likely wrong)."""
    # positive class = SC incorrect
    scored = [(r["entropy"], not r["sc_correct"]) for r in records]
    scored.sort(key=lambda x: x[0], reverse=True)  # high entropy first

    n_pos = sum(1 for _, label in scored if label)
    n_neg = len(scored) - n_pos
    if n_pos == 0 or n_neg == 0:
        return float("nan")

    tp = 0
    fp = 0
    prev_score = None
    auc = 0.0
    prev_tp = 0
    prev_fp = 0

    for score, label in scored:
        if score != prev_score and prev_score is not None:
            auc += (fp - prev_fp) * (tp + prev_tp) / 2.0
            prev_tp = tp
            prev_fp = fp
        if label:
            tp += 1
        else:
            fp += 1
        prev_score = score
    auc += (fp - prev_fp) * (tp + prev_tp) / 2.0

    return auc / (n_pos * n_neg)

def analyze_single_exp(results_path, label=""):
    """Full analysis for one experiment."""
    results, summary = load_results(results_path)
    records = compute_per_question_metrics(results)

    coverages = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5]

    # Entropy-based abstention (low entropy = confident)
    entropy_results = selective_abstention_by_metric(records, "entropy", ascending=True, coverages=coverages)
    # Majority-fraction-based abstention (high majority_frac = confident)
    majfrac_results = selective_abstention_by_metric(records, "majority_fraction", ascending=False, coverages=coverages)
    # Random baseline
    random_results = random_abstention(records, coverages=coverages)
    # AUROC
    auroc = compute_auroc(records)

    # Distribution stats
    entropies = [r["entropy"] for r in records]
    maj_fracs = [r["majority_fraction"] for r in records]

    return {
        "label": label,
        "n_questions": len(records),
        "sc_accuracy_full": summary["sc_accuracy"],
        "sica_accuracy_full": summary["sica_accuracy"],
        "auroc_entropy_predicts_error": auroc,
        "entropy_stats": {
            "mean": sum(entropies) / len(entropies),
            "min": min(entropies),
            "max": max(entropies),
            "median": sorted(entropies)[len(entropies) // 2],
        },
        "majority_fraction_stats": {
            "mean": sum(maj_fracs) / len(maj_fracs),
            "min": min(maj_fracs),
            "max": max(maj_fracs),
            "median": sorted(maj_fracs)[len(maj_fracs) // 2],
        },
        "coverage_table": [],
        "entropy_results": entropy_results,
        "majfrac_results": majfrac_results,
        "random_results": random_results,
    }

def format_table(analysis):
    """Format coverage table for display."""
    coverages = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5]
    rows = []
    for cov in coverages:
        ent = analysis["entropy_results"][cov]
        mf = analysis["majfrac_results"][cov]
        rnd = analysis["random_results"][cov]
        delta_ent = ent["sc_accuracy"] - rnd["sc_accuracy_mean"]
        delta_mf = mf["sc_accuracy"] - rnd["sc_accuracy_mean"]
        row = {
            "coverage": f"{cov*100:.0f}%",
            "n_answered": ent["n_answered"],
            "random_sc_acc": f"{rnd['sc_accuracy_mean']*100:.1f}%",
            "entropy_sc_acc": f"{ent['sc_accuracy']*100:.1f}%",
            "majfrac_sc_acc": f"{mf['sc_accuracy']*100:.1f}%",
            "entropy_sica_acc": f"{ent['sica_accuracy']*100:.1f}%",
            "delta_entropy_pp": f"{delta_ent*100:+.1f}pp",
            "delta_majfrac_pp": f"{delta_mf*100:+.1f}pp",
        }
        rows.append(row)
    analysis["coverage_table"] = rows
    return rows

def print_report(analysis):
    """Print formatted report."""
    label = analysis["label"]
    print(f"\n{'='*70}")
    print(f"  Direction E: Selective Abstention — {label}")
    print(f"{'='*70}")
    print(f"  N questions: {analysis['n_questions']}")
    print(f"  SC accuracy (full):   {analysis['sc_accuracy_full']*100:.1f}%")
    print(f"  SICA accuracy (full): {analysis['sica_accuracy_full']*100:.1f}%")
    print(f"  AUROC (entropy → error): {analysis['auroc_entropy_predicts_error']:.4f}")
    print(f"  Entropy stats: mean={analysis['entropy_stats']['mean']:.3f}, "
          f"median={analysis['entropy_stats']['median']:.3f}, "
          f"range=[{analysis['entropy_stats']['min']:.3f}, {analysis['entropy_stats']['max']:.3f}]")
    print(f"  MajFrac stats: mean={analysis['majority_fraction_stats']['mean']:.3f}, "
          f"median={analysis['majority_fraction_stats']['median']:.3f}, "
          f"range=[{analysis['majority_fraction_stats']['min']:.3f}, {analysis['majority_fraction_stats']['max']:.3f}]")

    print(f"\n  Coverage Table:")
    print(f"  {'Cov':>5} {'N':>4} {'Random SC':>10} {'Entropy SC':>11} {'MajFrac SC':>11} {'Entropy SICA':>13} {'Δ(ent)':>8} {'Δ(mf)':>8}")
    print(f"  {'-'*5} {'-'*4} {'-'*10} {'-'*11} {'-'*11} {'-'*13} {'-'*8} {'-'*8}")
    for row in analysis["coverage_table"]:
        print(f"  {row['coverage']:>5} {row['n_answered']:>4} {row['random_sc_acc']:>10} "
              f"{row['entropy_sc_acc']:>11} {row['majfrac_sc_acc']:>11} "
              f"{row['entropy_sica_acc']:>13} {row['delta_entropy_pp']:>8} {row['delta_majfrac_pp']:>8}")
    print()

def main():
    base = "/root/symb_invariant_consensus/results"
    experiments = {
        "exp033 (Mistral-7B, seed=42)": f"{base}/exp033_mistral_7b_folio204/exp033_results.json",
        "exp067 (Mistral-7B, seed=789)": f"{base}/exp067_mistral_folio_seed789/exp067_results.json",
    }

    all_analyses = {}
    for label, path in experiments.items():
        if not os.path.exists(path):
            print(f"SKIP: {path} not found")
            continue
        analysis = analyze_single_exp(path, label)
        format_table(analysis)
        print_report(analysis)
        all_analyses[label] = analysis

    # Multi-seed aggregate if >1 experiment
    if len(all_analyses) > 1:
        print(f"\n{'='*70}")
        print(f"  Multi-seed Aggregate")
        print(f"{'='*70}")
        coverages = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5]
        aurocs = [a["auroc_entropy_predicts_error"] for a in all_analyses.values()]
        print(f"  AUROC mean: {sum(aurocs)/len(aurocs):.4f}, values: {[f'{a:.4f}' for a in aurocs]}")

        print(f"\n  {'Cov':>5} {'Entropy SC (mean±std)':>22} {'Random SC (mean)':>17} {'Δ mean':>8}")
        print(f"  {'-'*5} {'-'*22} {'-'*17} {'-'*8}")
        for cov in coverages:
            ent_accs = [a["entropy_results"][cov]["sc_accuracy"] for a in all_analyses.values()]
            rnd_accs = [a["random_results"][cov]["sc_accuracy_mean"] for a in all_analyses.values()]
            ent_mean = sum(ent_accs) / len(ent_accs)
            ent_std = (sum((x - ent_mean)**2 for x in ent_accs) / len(ent_accs)) ** 0.5
            rnd_mean = sum(rnd_accs) / len(rnd_accs)
            delta = ent_mean - rnd_mean
            print(f"  {cov*100:>4.0f}% {ent_mean*100:>7.1f}% ± {ent_std*100:.1f}% {rnd_mean*100:>12.1f}% {delta*100:>+7.1f}pp")

    # Save JSON output
    output = {
        "description": "Direction E: Selective Abstention results",
        "experiments": {},
    }
    for label, analysis in all_analyses.items():
        # Convert for JSON serialization
        exp_out = {
            "label": label,
            "n_questions": analysis["n_questions"],
            "sc_accuracy_full": analysis["sc_accuracy_full"],
            "sica_accuracy_full": analysis["sica_accuracy_full"],
            "auroc_entropy_predicts_error": analysis["auroc_entropy_predicts_error"],
            "entropy_stats": analysis["entropy_stats"],
            "majority_fraction_stats": analysis["majority_fraction_stats"],
            "coverage_table": analysis["coverage_table"],
        }
        # Add raw numeric data for downstream plotting
        coverages = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5]
        exp_out["coverage_data"] = {}
        for cov in coverages:
            cov_key = f"{cov:.1f}"
            exp_out["coverage_data"][cov_key] = {
                "entropy_sc_acc": analysis["entropy_results"][cov]["sc_accuracy"],
                "entropy_sica_acc": analysis["entropy_results"][cov]["sica_accuracy"],
                "majfrac_sc_acc": analysis["majfrac_results"][cov]["sc_accuracy"],
                "random_sc_acc_mean": analysis["random_results"][cov]["sc_accuracy_mean"],
                "random_sc_acc_std": analysis["random_results"][cov]["sc_accuracy_std"],
                "n_answered": analysis["entropy_results"][cov]["n_answered"],
            }
        output["experiments"][label] = exp_out

    # Multi-seed aggregate
    if len(all_analyses) > 1:
        coverages = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5]
        aggregate = {}
        for cov in coverages:
            ent_accs = [a["entropy_results"][cov]["sc_accuracy"] for a in all_analyses.values()]
            rnd_accs = [a["random_results"][cov]["sc_accuracy_mean"] for a in all_analyses.values()]
            ent_mean = sum(ent_accs) / len(ent_accs)
            ent_std = (sum((x - ent_mean)**2 for x in ent_accs) / len(ent_accs)) ** 0.5
            rnd_mean = sum(rnd_accs) / len(rnd_accs)
            aggregate[f"{cov:.1f}"] = {
                "entropy_sc_mean": ent_mean,
                "entropy_sc_std": ent_std,
                "random_sc_mean": rnd_mean,
                "delta_pp": ent_mean - rnd_mean,
            }
        aurocs = [a["auroc_entropy_predicts_error"] for a in all_analyses.values()]
        output["aggregate"] = {
            "n_seeds": len(all_analyses),
            "auroc_mean": sum(aurocs) / len(aurocs),
            "auroc_values": aurocs,
            "coverage_data": aggregate,
        }

    out_path = "/root/symb_invariant_consensus/results/direction_e_abstention/results.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {out_path}")

if __name__ == "__main__":
    main()

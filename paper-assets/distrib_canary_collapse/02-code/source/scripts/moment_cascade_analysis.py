#!/usr/bin/env python3
# DEPRECATED: Use baseline-comparison method instead (see artifacts/moment_cascade/moment_cascade_analysis.py)
# Within-experiment z-score produces false alarms on null (α=0.0) experiments
# Decision: Director Directive 2026-05-20
"""
Moment Cascade Analysis for Distributional Canary Collapse (D032).

Phase 1 (--mode metrics): Analyze cascade ordering from existing per-generation
metrics. Detects onset timing for each metric relative to gen_0 baseline, then
determines whether the cascade follows:
  entropy↓ → distinct_n↓ → effective_rank↓ → perplexity↑

Phase 2 (--mode checkpoint): Compute logit-level distribution moments from
saved checkpoints (requires GPU + intermediate checkpoints).

Usage:
  python moment_cascade_analysis.py --mode metrics \
      --data_dir /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep
  python moment_cascade_analysis.py --mode metrics --data_dir ... --alpha 0.50
"""

import argparse
import json
import sys
from pathlib import Path

import numpy as np

# Metrics where DECREASE signals collapse
DECREASE_METRICS = [
    "token_entropy", "distinct_1", "distinct_2", "distinct_3",
    "effective_rank", "mauve",
]
# Metrics where INCREASE signals collapse
INCREASE_METRICS = ["perplexity", "ece", "self_bleu"]

ALL_CASCADE_METRICS = DECREASE_METRICS + INCREASE_METRICS

# Canonical cascade hypothesis ordering (D032)
CASCADE_HYPOTHESIS = [
    "token_entropy",   # 1st: distributional entropy drops
    "distinct_1",      # 2nd: unigram diversity drops
    "distinct_2",      # 3rd: bigram diversity drops
    "distinct_3",      # 4th: trigram diversity drops
    "effective_rank",  # 5th: representation rank drops
    "perplexity",      # 6th: downstream quality degrades
]


def load_experiment(exp_dir):
    """Load all_metrics.json from an experiment directory."""
    p = Path(exp_dir) / "all_metrics.json"
    if not p.exists():
        return None
    with open(p) as f:
        data = json.load(f)
    data.sort(key=lambda x: x["generation"])
    return data


def parse_experiment_name(dirname):
    """Extract alpha and seed from directory name like 'a050_s42' or 'a010_s42_fp32'."""
    parts = dirname.replace("_fp32", "").replace("_bf16", "").split("_")
    alpha_str = [p for p in parts if p.startswith("a") and p[1:].isdigit()]
    seed_str = [p for p in parts if p.startswith("s") and p[1:].isdigit()]
    alpha = int(alpha_str[0][1:]) / 100.0 if alpha_str else None
    seed = int(seed_str[0][1:]) if seed_str else None
    dataset = "c4" if dirname.startswith("c4_") else "wikitext"
    return alpha, seed, dataset


def compute_onset_generation(series, baseline_val, direction, threshold_sigma=2.0):
    """Find the first generation where the metric deviates beyond threshold.

    Uses a rolling z-score approach: deviation is measured in units of
    the baseline's expected noise (estimated from gen_0..2 variance if available,
    else from absolute percentage change).

    Returns (onset_gen, z_score_at_onset) or (None, None) if no onset detected.
    """
    if len(series) < 3:
        return None, None

    # Estimate noise from first 3 generations
    early = np.array(series[:3])
    early_std = np.std(early)
    if early_std < 1e-10:
        early_std = abs(baseline_val) * 0.01 if abs(baseline_val) > 1e-10 else 1e-10

    sign = -1.0 if direction == "decrease" else 1.0

    for g in range(1, len(series)):
        deviation = sign * (series[g] - baseline_val)
        z = deviation / early_std
        if z >= threshold_sigma:
            return g, float(z)

    return None, None


def compute_cumulative_drift(series, baseline_val, direction):
    """Compute normalized cumulative drift for cascade severity ranking."""
    if abs(baseline_val) < 1e-10:
        return [0.0] * len(series)
    sign = -1.0 if direction == "decrease" else 1.0
    return [sign * (v - baseline_val) / abs(baseline_val) for v in series]


def analyze_single_experiment(metrics_list, exp_name=""):
    """Analyze cascade pattern for a single experiment."""
    if not metrics_list or len(metrics_list) < 3:
        return None

    gens = [m["generation"] for m in metrics_list]
    baseline = metrics_list[0]

    results = {"experiment": exp_name, "n_generations": len(metrics_list)}
    onset_table = {}
    drift_table = {}

    for metric in ALL_CASCADE_METRICS:
        if metric not in baseline:
            continue

        series = [m.get(metric, float("nan")) for m in metrics_list]
        baseline_val = series[0]
        direction = "decrease" if metric in DECREASE_METRICS else "increase"

        onset_gen, z_score = compute_onset_generation(
            series, baseline_val, direction, threshold_sigma=2.0
        )
        onset_table[metric] = {
            "onset_gen": onset_gen,
            "z_score": z_score,
            "baseline": baseline_val,
            "final": series[-1],
            "pct_change": (series[-1] - baseline_val) / abs(baseline_val) * 100
            if abs(baseline_val) > 1e-10 else None,
            "direction": direction,
        }

        drift_table[metric] = compute_cumulative_drift(series, baseline_val, direction)

    # Sort by onset generation to determine cascade ordering
    detected = {k: v for k, v in onset_table.items() if v["onset_gen"] is not None}
    cascade_order = sorted(detected.keys(), key=lambda k: (detected[k]["onset_gen"], -abs(detected[k]["z_score"] or 0)))

    results["onset_table"] = onset_table
    results["cascade_order"] = cascade_order
    results["drift_table"] = {k: v for k, v in drift_table.items() if k in CASCADE_HYPOTHESIS}
    results["n_detected"] = len(detected)

    return results


def analyze_cross_alpha(all_results):
    """Cross-alpha analysis: how cascade ordering changes with α."""
    summary = {}
    for res in all_results:
        if res is None:
            continue
        exp = res["experiment"]
        alpha, seed, dataset = parse_experiment_name(exp)
        if alpha is None:
            continue

        key = f"a{int(alpha*100):03d}_{dataset}"
        if key not in summary:
            summary[key] = {"alpha": alpha, "dataset": dataset, "seeds": {}}
        summary[key]["seeds"][seed] = {
            "cascade_order": res["cascade_order"],
            "onset_gens": {k: v["onset_gen"] for k, v in res["onset_table"].items()},
            "pct_changes": {k: v["pct_change"] for k, v in res["onset_table"].items()
                           if v["pct_change"] is not None},
        }

    # Compute consensus cascade order per alpha
    for key, info in summary.items():
        all_orders = [s["cascade_order"] for s in info["seeds"].values()]
        if not all_orders:
            continue

        # Rank-based consensus: average rank across seeds
        metric_ranks = {}
        for order in all_orders:
            for rank, m in enumerate(order):
                if m not in metric_ranks:
                    metric_ranks[m] = []
                metric_ranks[m].append(rank)

        n_seeds = len(all_orders)
        for m in metric_ranks:
            # Penalize metrics not detected in some seeds
            while len(metric_ranks[m]) < n_seeds:
                metric_ranks[m].append(len(CASCADE_HYPOTHESIS))

        consensus = sorted(metric_ranks.keys(), key=lambda m: np.mean(metric_ranks[m]))
        info["consensus_order"] = consensus
        info["mean_ranks"] = {m: float(np.mean(r)) for m, r in metric_ranks.items()}

    return summary


def check_hypothesis_match(cascade_order, hypothesis=CASCADE_HYPOTHESIS):
    """Check how well the observed cascade matches the hypothesized ordering.

    Returns (kendall_tau, matched_prefix_len).
    """
    if len(cascade_order) < 2:
        return None, 0

    observed_in_hyp = [m for m in cascade_order if m in hypothesis]
    if len(observed_in_hyp) < 2:
        return None, 0

    hyp_ranks = {m: i for i, m in enumerate(hypothesis)}
    obs_ranks = [hyp_ranks[m] for m in observed_in_hyp]

    # Kendall tau (concordant vs discordant pairs)
    n = len(obs_ranks)
    concordant = 0
    discordant = 0
    for i in range(n):
        for j in range(i + 1, n):
            if obs_ranks[i] < obs_ranks[j]:
                concordant += 1
            else:
                discordant += 1
    total = concordant + discordant
    tau = (concordant - discordant) / total if total > 0 else 0.0

    # Matched prefix: how many initial hypothesis steps match
    prefix = 0
    for i, m in enumerate(hypothesis):
        if i < len(observed_in_hyp) and observed_in_hyp[i] == m:
            prefix += 1
        else:
            break

    return float(tau), prefix


def format_report(all_results, cross_alpha):
    """Format analysis results as text report."""
    lines = []
    lines.append("=" * 70)
    lines.append("MOMENT CASCADE ANALYSIS — Phase 1 (from existing metrics)")
    lines.append("=" * 70)

    # Per-experiment onset table
    lines.append("\n## Per-Experiment Onset Detection\n")
    for res in sorted(all_results, key=lambda r: r["experiment"] if r else ""):
        if res is None:
            continue
        lines.append(f"### {res['experiment']} ({res['n_generations']} gens)")

        if not res["cascade_order"]:
            lines.append("  No significant deviations detected.\n")
            continue

        lines.append(f"  Cascade order: {' → '.join(res['cascade_order'])}")
        tau, prefix = check_hypothesis_match(res["cascade_order"])
        if tau is not None:
            lines.append(f"  Hypothesis match: τ={tau:.2f}, prefix={prefix}/{len(CASCADE_HYPOTHESIS)}")

        lines.append(f"  {'Metric':<18} {'Onset':>5} {'z-score':>8} {'Δ%':>8} {'Direction':>10}")
        lines.append(f"  {'-'*18} {'-'*5} {'-'*8} {'-'*8} {'-'*10}")
        for m in res["cascade_order"]:
            info = res["onset_table"][m]
            pct = f"{info['pct_change']:+.1f}" if info['pct_change'] is not None else "N/A"
            lines.append(
                f"  {m:<18} {info['onset_gen']:>5} {info['z_score']:>8.1f} {pct:>8} {info['direction']:>10}"
            )
        lines.append("")

    # Cross-alpha summary
    lines.append("\n## Cross-Alpha Cascade Consensus\n")
    for key in sorted(cross_alpha.keys()):
        info = cross_alpha[key]
        n_seeds = len(info["seeds"])
        lines.append(f"### {key} (α={info['alpha']:.2f}, {info['dataset']}, {n_seeds} seeds)")
        if "consensus_order" in info:
            lines.append(f"  Consensus: {' → '.join(info['consensus_order'])}")
            tau, prefix = check_hypothesis_match(info["consensus_order"])
            if tau is not None:
                lines.append(f"  Hypothesis match: τ={tau:.2f}, prefix={prefix}")
            lines.append(f"  Mean ranks: {info['mean_ranks']}")
        lines.append("")

    # Overall verdict
    lines.append("\n## Cascade Hypothesis Verdict\n")
    all_taus = []
    for res in all_results:
        if res is None:
            continue
        tau, _ = check_hypothesis_match(res["cascade_order"])
        if tau is not None:
            all_taus.append(tau)

    if all_taus:
        lines.append(f"  Mean Kendall τ across experiments: {np.mean(all_taus):.3f} (n={len(all_taus)})")
        lines.append(f"  τ > 0 supports hypothesis, τ ≈ 1 = perfect match")
        positive = sum(1 for t in all_taus if t > 0)
        lines.append(f"  {positive}/{len(all_taus)} experiments show positive τ")
    else:
        lines.append("  Insufficient data for hypothesis testing.")

    # Data gap analysis
    lines.append("\n## Data Gaps (Phase 2 needs)\n")
    lines.append("  Missing logit-level moments (require GPU forward pass):")
    lines.append("    - var_log_p: variance of log-probability distribution")
    lines.append("    - kurtosis: peakedness of log-prob distribution")
    lines.append("    - tail_mass: fraction of vocab below uniform threshold")
    lines.append("    - top50_concentration: probability mass in top-50 tokens")
    lines.append("  Status: intermediate checkpoints NOT saved (only gen_9/10).")
    lines.append("  → Need experiment re-run with --save_all_checkpoints, or")
    lines.append("    compute moments on-the-fly during next T=20 runs.")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Moment Cascade Analysis (D032)")
    parser.add_argument("--mode", choices=["metrics", "checkpoint"], default="metrics")
    parser.add_argument("--data_dir", type=str, required=True,
                        help="Root directory containing experiment subdirs")
    parser.add_argument("--alpha", type=float, default=None,
                        help="Analyze only this alpha value")
    parser.add_argument("--dataset", type=str, default=None,
                        choices=["wikitext", "c4"],
                        help="Filter by dataset")
    parser.add_argument("--output", type=str, default=None,
                        help="Output JSON path (default: stdout report)")
    parser.add_argument("--threshold_sigma", type=float, default=2.0,
                        help="Z-score threshold for onset detection")
    args = parser.parse_args()

    if args.mode == "checkpoint":
        print("ERROR: checkpoint mode requires GPU and intermediate checkpoints.")
        print("Intermediate checkpoints are NOT available for existing experiments.")
        print("Use --mode metrics for Phase 1 analysis from existing data.")
        sys.exit(1)

    data_dir = Path(args.data_dir)
    if not data_dir.exists():
        print(f"ERROR: {data_dir} does not exist", file=sys.stderr)
        sys.exit(1)

    all_results = []
    for exp_dir in sorted(data_dir.iterdir()):
        if not exp_dir.is_dir():
            continue
        name = exp_dir.name
        if name.startswith("analysis"):
            continue

        alpha, seed, dataset = parse_experiment_name(name)

        if args.alpha is not None and alpha is not None and abs(alpha - args.alpha) > 1e-6:
            continue
        if args.dataset is not None and dataset != args.dataset:
            continue

        metrics_list = load_experiment(exp_dir)
        if metrics_list is None:
            continue

        result = analyze_single_experiment(metrics_list, exp_name=name)
        if result is not None:
            all_results.append(result)

    if not all_results:
        print("No experiments found.", file=sys.stderr)
        sys.exit(1)

    cross_alpha = analyze_cross_alpha(all_results)

    if args.output:
        out = {
            "experiments": all_results,
            "cross_alpha": cross_alpha,
        }
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w") as f:
            json.dump(out, f, indent=2, default=str)
        print(f"Saved to {args.output}")
    else:
        print(format_report(all_results, cross_alpha))


if __name__ == "__main__":
    main()

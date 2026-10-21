"""Plan-012 Death Decomposition Analysis (D013).

Quantifies how much of the Δ(Det-Internal) gap comes from death avoidance
vs genuine score improvement.
"""

import argparse
import json
import math
import os
import statistics
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

DEATH_THRESHOLD = -100


def is_dead(score: float) -> bool:
    return score <= DEATH_THRESHOLD


def classify_episode(int_score: float, det_score: float) -> Tuple[str, str, str]:
    """Returns (label, reason, signal_source)."""
    int_died = is_dead(int_score)
    det_died = is_dead(det_score)

    if int_died and not det_died:
        return "det-preferred", "int_died_det_alive", "death_asymmetry"
    if det_died and not int_died:
        return "internal-preferred", "det_died_int_alive", "death_asymmetry"
    if int_died and det_died:
        return "no-preference", "both_died", "both_dead"
    if det_score > int_score:
        return "det-preferred", "both_alive_det_wins", "score_comparison"
    if int_score > det_score:
        return "internal-preferred", "both_alive_int_wins", "score_comparison"
    return "no-preference", "tie", "tied_alive"


def safe_mean(values: List[float]) -> float:
    return statistics.mean(values) if values else float("nan")


def pearsonr(x: List[float], y: List[float]) -> Tuple[float, float]:
    """Pearson correlation with p-value. Falls back to scipy if available."""
    try:
        from scipy.stats import pearsonr as sp_pearsonr
        r, p = sp_pearsonr(x, y)
        return float(r), float(p)
    except ImportError:
        pass
    n = len(x)
    if n < 3:
        return float("nan"), float("nan")
    mx, my = statistics.mean(x), statistics.mean(y)
    sx = math.sqrt(sum((xi - mx) ** 2 for xi in x) / (n - 1))
    sy = math.sqrt(sum((yi - my) ** 2 for yi in y) / (n - 1))
    if sx == 0 or sy == 0:
        return float("nan"), float("nan")
    r = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y)) / ((n - 1) * sx * sy)
    # t-test approximation for p-value
    t = r * math.sqrt((n - 2) / (1 - r * r + 1e-15))
    # Two-tailed p from t distribution (approximation)
    import subprocess
    try:
        result = subprocess.run(
            ["python3", "-c",
             f"from scipy.stats import t as tdist; print(2*tdist.sf(abs({t}),{n-2}))"],
            capture_output=True, text=True, timeout=5)
        p = float(result.stdout.strip())
    except Exception:
        p = float("nan")
    return r, p


def load_episodes(data_dirs: List[str], task_filter: Optional[List[str]] = None) -> Dict[str, List[dict]]:
    """Load episodes grouped by task_type from multiple data directories."""
    task_episodes: Dict[str, List[dict]] = defaultdict(list)

    for data_dir in data_dirs:
        if not os.path.isdir(data_dir):
            print(f"  WARN: {data_dir} not found, skipping")
            continue
        for task_name in sorted(os.listdir(data_dir)):
            task_dir = os.path.join(data_dir, task_name)
            ep_file = os.path.join(task_dir, "episodes.jsonl")
            if not os.path.isfile(ep_file):
                continue
            if task_filter and task_name not in task_filter:
                continue
            with open(ep_file) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    ep = json.loads(line)
                    if "always_internal" not in ep or "always_deterministic" not in ep:
                        continue
                    task_episodes[task_name].append(ep)

    return dict(task_episodes)


def analyze_task(task_name: str, episodes: List[dict]) -> dict:
    """Full death decomposition for one task."""
    n = len(episodes)
    int_scores = [ep["always_internal"]["final_score"] for ep in episodes]
    det_scores = [ep["always_deterministic"]["final_score"] for ep in episodes]

    int_deaths = sum(1 for s in int_scores if is_dead(s))
    det_deaths = sum(1 for s in det_scores if is_dead(s))
    int_death_rate = int_deaths / n
    det_death_rate = det_deaths / n

    # --- A. Basic stats ---
    int_mean = safe_mean(int_scores)
    det_mean = safe_mean(det_scores)
    delta_full = det_mean - int_mean

    # No-death subset: exclude episodes where EITHER mode died
    nd_int_scores = []
    nd_det_scores = []
    for i_s, d_s in zip(int_scores, det_scores):
        if not is_dead(i_s) and not is_dead(d_s):
            nd_int_scores.append(i_s)
            nd_det_scores.append(d_s)

    int_mean_nd = safe_mean(nd_int_scores)
    det_mean_nd = safe_mean(nd_det_scores)
    delta_no_death = det_mean_nd - int_mean_nd if nd_int_scores else float("nan")

    # Penalty-removed: replace -100 with 0
    int_scores_pr = [0.0 if is_dead(s) else s for s in int_scores]
    det_scores_pr = [0.0 if is_dead(s) else s for s in det_scores]
    int_mean_pr = safe_mean(int_scores_pr)
    det_mean_pr = safe_mean(det_scores_pr)
    delta_penalty_removed = det_mean_pr - int_mean_pr

    # Death avoidance fraction
    if not math.isnan(delta_no_death) and delta_full != 0:
        death_avoidance_frac = (delta_full - delta_no_death) / delta_full
    else:
        death_avoidance_frac = float("nan")

    # --- C. Label distribution ---
    label_counts = defaultdict(int)
    signal_counts = defaultdict(int)
    label_signal_cross = defaultdict(lambda: defaultdict(int))
    for i_s, d_s in zip(int_scores, det_scores):
        label, reason, signal_source = classify_episode(i_s, d_s)
        label_counts[label] += 1
        signal_counts[signal_source] += 1
        label_signal_cross[label][signal_source] += 1

    return {
        "task": task_name,
        "n_episodes": n,
        "int_death_count": int_deaths,
        "det_death_count": det_deaths,
        "int_death_rate": round(int_death_rate, 4),
        "det_death_rate": round(det_death_rate, 4),
        "int_mean": round(int_mean, 2),
        "det_mean": round(det_mean, 2),
        "delta_full": round(delta_full, 2),
        "int_mean_no_death": round(int_mean_nd, 2) if not math.isnan(int_mean_nd) else None,
        "det_mean_no_death": round(det_mean_nd, 2) if not math.isnan(det_mean_nd) else None,
        "delta_no_death": round(delta_no_death, 2) if not math.isnan(delta_no_death) else None,
        "death_avoidance_fraction": round(death_avoidance_frac, 4) if not math.isnan(death_avoidance_frac) else None,
        "int_mean_penalty_removed": round(int_mean_pr, 2),
        "det_mean_penalty_removed": round(det_mean_pr, 2),
        "delta_penalty_removed": round(delta_penalty_removed, 2),
        "n_no_death_episodes": len(nd_int_scores),
        "label_distribution": {
            "det-preferred": label_counts.get("det-preferred", 0),
            "internal-preferred": label_counts.get("internal-preferred", 0),
            "no-preference": label_counts.get("no-preference", 0),
        },
        "signal_source_distribution": dict(signal_counts),
        "label_signal_cross": {k: dict(v) for k, v in label_signal_cross.items()},
    }


def aggregate_results(task_results: List[dict]) -> dict:
    """Compute aggregate statistics across all tasks."""
    all_int, all_det = [], []
    all_int_nd, all_det_nd = [], []
    all_int_pr, all_det_pr = [], []
    total_label = defaultdict(int)
    total_signal = defaultdict(int)
    total_label_signal = defaultdict(lambda: defaultdict(int))

    # For correlation: per-task death rate vs delta
    task_death_rates = []
    task_deltas = []

    for tr in task_results:
        n = tr["n_episodes"]
        int_death_rate = tr["int_death_rate"]
        det_death_rate = tr["det_death_rate"]

        # Reconstruct per-episode scores from means for aggregate
        # (approximate; for exact we'd need raw scores)
        # Instead, weight by n_episodes
        all_int.extend([tr["int_mean"]] * n)
        all_det.extend([tr["det_mean"]] * n)

        n_nd = tr["n_no_death_episodes"]
        if tr["int_mean_no_death"] is not None and n_nd > 0:
            all_int_nd.extend([tr["int_mean_no_death"]] * n_nd)
            all_det_nd.extend([tr["det_mean_no_death"]] * n_nd)

        all_int_pr.extend([tr["int_mean_penalty_removed"]] * n)
        all_det_pr.extend([tr["det_mean_penalty_removed"]] * n)

        for lbl, cnt in tr["label_distribution"].items():
            total_label[lbl] += cnt
        for sig, cnt in tr["signal_source_distribution"].items():
            total_signal[sig] += cnt
        for lbl, sigs in tr["label_signal_cross"].items():
            for sig, cnt in sigs.items():
                total_label_signal[lbl][sig] += cnt

        # Per-task correlation data
        avg_death_rate = (int_death_rate + det_death_rate) / 2
        death_rate_diff = int_death_rate - det_death_rate
        task_death_rates.append(death_rate_diff)
        task_deltas.append(tr["delta_full"])

    # Weighted aggregate means
    agg_int_mean = safe_mean(all_int)
    agg_det_mean = safe_mean(all_det)
    agg_delta_full = agg_det_mean - agg_int_mean

    agg_int_nd = safe_mean(all_int_nd) if all_int_nd else float("nan")
    agg_det_nd = safe_mean(all_det_nd) if all_det_nd else float("nan")
    agg_delta_nd = (agg_det_nd - agg_int_nd) if all_int_nd else float("nan")

    agg_int_pr = safe_mean(all_int_pr)
    agg_det_pr = safe_mean(all_det_pr)
    agg_delta_pr = agg_det_pr - agg_int_pr

    if not math.isnan(agg_delta_nd) and agg_delta_full != 0:
        agg_death_frac = (agg_delta_full - agg_delta_nd) / agg_delta_full
    else:
        agg_death_frac = float("nan")

    # Correlation: death_rate_diff vs delta
    r, p = pearsonr(task_death_rates, task_deltas)

    total_episodes = sum(tr["n_episodes"] for tr in task_results)
    total_int_deaths = sum(tr["int_death_count"] for tr in task_results)
    total_det_deaths = sum(tr["det_death_count"] for tr in task_results)

    return {
        "n_tasks": len(task_results),
        "n_episodes": total_episodes,
        "int_death_rate": round(total_int_deaths / total_episodes, 4) if total_episodes else None,
        "det_death_rate": round(total_det_deaths / total_episodes, 4) if total_episodes else None,
        "int_mean": round(agg_int_mean, 2),
        "det_mean": round(agg_det_mean, 2),
        "delta_full": round(agg_delta_full, 2),
        "delta_no_death": round(agg_delta_nd, 2) if not math.isnan(agg_delta_nd) else None,
        "death_avoidance_fraction": round(agg_death_frac, 4) if not math.isnan(agg_death_frac) else None,
        "delta_penalty_removed": round(agg_delta_pr, 2),
        "correlation_death_rate_diff_vs_delta": {
            "pearson_r": round(r, 4) if not math.isnan(r) else None,
            "p_value": round(p, 6) if not math.isnan(p) else None,
            "n_tasks": len(task_death_rates),
        },
        "label_distribution": dict(total_label),
        "signal_source_distribution": dict(total_signal),
        "label_signal_cross": {k: dict(v) for k, v in total_label_signal.items()},
    }


def aggregate_from_raw(data_dirs: List[str], task_filter: Optional[List[str]] = None) -> dict:
    """Re-aggregate from raw episode scores for exact results."""
    task_episodes = load_episodes(data_dirs, task_filter)
    all_int, all_det = [], []
    all_int_nd, all_det_nd = [], []

    task_death_rates = []
    task_deltas = []
    total_label = defaultdict(int)
    total_signal = defaultdict(int)
    total_label_signal = defaultdict(lambda: defaultdict(int))

    for task_name, episodes in task_episodes.items():
        int_scores = [ep["always_internal"]["final_score"] for ep in episodes]
        det_scores = [ep["always_deterministic"]["final_score"] for ep in episodes]
        all_int.extend(int_scores)
        all_det.extend(det_scores)

        n = len(int_scores)
        int_dr = sum(1 for s in int_scores if is_dead(s)) / n
        det_dr = sum(1 for s in det_scores if is_dead(s)) / n
        delta = safe_mean(det_scores) - safe_mean(int_scores)
        task_death_rates.append(int_dr - det_dr)
        task_deltas.append(delta)

        for i_s, d_s in zip(int_scores, det_scores):
            if not is_dead(i_s) and not is_dead(d_s):
                all_int_nd.append(i_s)
                all_det_nd.append(d_s)
            label, _, signal_source = classify_episode(i_s, d_s)
            total_label[label] += 1
            total_signal[signal_source] += 1
            total_label_signal[label][signal_source] += 1

    n_total = len(all_int)
    int_mean = safe_mean(all_int)
    det_mean = safe_mean(all_det)
    delta_full = det_mean - int_mean

    int_nd_mean = safe_mean(all_int_nd) if all_int_nd else float("nan")
    det_nd_mean = safe_mean(all_det_nd) if all_det_nd else float("nan")
    delta_nd = (det_nd_mean - int_nd_mean) if all_int_nd else float("nan")

    int_pr = safe_mean([0.0 if is_dead(s) else s for s in all_int])
    det_pr = safe_mean([0.0 if is_dead(s) else s for s in all_det])
    delta_pr = det_pr - int_pr

    if not math.isnan(delta_nd) and delta_full != 0:
        death_frac = (delta_full - delta_nd) / delta_full
    else:
        death_frac = float("nan")

    r, p = pearsonr(task_death_rates, task_deltas)

    return {
        "n_tasks": len(task_episodes),
        "n_episodes": n_total,
        "int_death_rate": round(sum(1 for s in all_int if is_dead(s)) / n_total, 4),
        "det_death_rate": round(sum(1 for s in all_det if is_dead(s)) / n_total, 4),
        "int_mean": round(int_mean, 2),
        "det_mean": round(det_mean, 2),
        "delta_full": round(delta_full, 2),
        "int_mean_no_death": round(int_nd_mean, 2) if not math.isnan(int_nd_mean) else None,
        "det_mean_no_death": round(det_nd_mean, 2) if not math.isnan(det_nd_mean) else None,
        "delta_no_death": round(delta_nd, 2) if not math.isnan(delta_nd) else None,
        "death_avoidance_fraction": round(death_frac, 4) if not math.isnan(death_frac) else None,
        "delta_penalty_removed": round(delta_pr, 2),
        "correlation_death_rate_diff_vs_delta": {
            "pearson_r": round(r, 4) if not math.isnan(r) else None,
            "p_value": round(p, 6) if not math.isnan(p) else None,
            "n_tasks": len(task_episodes),
        },
        "label_distribution": dict(total_label),
        "signal_source_distribution": dict(total_signal),
        "label_signal_cross": {k: dict(v) for k, v in total_label_signal.items()},
    }


def print_table(task_results: List[dict], aggregate: dict):
    """Print Director-format table."""
    hdr = (f"| {'Task':<42} | {'N':>4} | {'Int':>7} | {'Det':>7} | {'Δ':>7} "
           f"| {'I_d%':>5} | {'D_d%':>5} "
           f"| {'Δ_nd':>7} | {'D_frac':>7} | {'Δ_pr':>7} "
           f"| {'det':>4} {'int':>4} {'no':>4} |")
    sep = "-" * len(hdr)

    print(sep)
    print(hdr)
    print(sep)

    for tr in task_results:
        dnd = f"{tr['delta_no_death']:+.1f}" if tr["delta_no_death"] is not None else "N/A"
        dfr = f"{tr['death_avoidance_fraction']:.0%}" if tr["death_avoidance_fraction"] is not None else "N/A"
        dpr = f"{tr['delta_penalty_removed']:+.1f}"
        ld = tr["label_distribution"]
        print(f"| {tr['task']:<42} | {tr['n_episodes']:>4} "
              f"| {tr['int_mean']:>7.1f} | {tr['det_mean']:>7.1f} | {tr['delta_full']:>+7.1f} "
              f"| {tr['int_death_rate']*100:>4.0f}% | {tr['det_death_rate']*100:>4.0f}% "
              f"| {dnd:>7s} | {dfr:>7s} | {dpr:>7s} "
              f"| {ld.get('det-preferred',0):>4} {ld.get('internal-preferred',0):>4} {ld.get('no-preference',0):>4} |")

    print(sep)
    # Aggregate row
    agg = aggregate
    dnd = f"{agg['delta_no_death']:+.1f}" if agg.get("delta_no_death") is not None else "N/A"
    dfr = f"{agg['death_avoidance_fraction']:.0%}" if agg.get("death_avoidance_fraction") is not None else "N/A"
    dpr = f"{agg['delta_penalty_removed']:+.1f}"
    ld = agg["label_distribution"]
    print(f"| {'AGGREGATE':<42} | {agg['n_episodes']:>4} "
          f"| {agg['int_mean']:>7.1f} | {agg['det_mean']:>7.1f} | {agg['delta_full']:>+7.1f} "
          f"| {agg['int_death_rate']*100:>4.0f}% | {agg['det_death_rate']*100:>4.0f}% "
          f"| {dnd:>7s} | {dfr:>7s} | {dpr:>7s} "
          f"| {ld.get('det-preferred',0):>4} {ld.get('internal-preferred',0):>4} {ld.get('no-preference',0):>4} |")
    print(sep)

    # Correlation
    corr = agg.get("correlation_death_rate_diff_vs_delta", {})
    r = corr.get("pearson_r")
    p = corr.get("p_value")
    r_str = f"{r:.3f}" if r is not None else "N/A"
    p_str = f"{p:.4f}" if p is not None else "N/A"
    print(f"\nCorrelation (death_rate_diff vs Δ): r={r_str}, p={p_str}, n={corr.get('n_tasks', 0)} tasks")

    # Signal source breakdown
    print(f"\nSignal source distribution:")
    for src in ["death_asymmetry", "both_dead", "score_comparison", "tied_alive"]:
        cnt = agg["signal_source_distribution"].get(src, 0)
        pct = cnt / agg["n_episodes"] * 100 if agg["n_episodes"] else 0
        print(f"  {src}: {cnt} ({pct:.1f}%)")

    # Cross table
    print(f"\nLabel × Signal source cross table:")
    print(f"  {'Label':<20} | {'death_asym':>10} | {'both_dead':>10} | {'score_cmp':>10} | {'tied_alive':>10} |")
    cross = agg.get("label_signal_cross", {})
    for lbl in ["det-preferred", "internal-preferred", "no-preference"]:
        row = cross.get(lbl, {})
        print(f"  {lbl:<20} | {row.get('death_asymmetry',0):>10} | {row.get('both_dead',0):>10} "
              f"| {row.get('score_comparison',0):>10} | {row.get('tied_alive',0):>10} |")


def generate_paper_table_data(task_results: List[dict], aggregate: dict) -> dict:
    """Generate data structured for LaTeX table generation."""
    rows = []
    for tr in task_results:
        rows.append({
            "task": tr["task"],
            "n": tr["n_episodes"],
            "int_mean": tr["int_mean"],
            "det_mean": tr["det_mean"],
            "delta": tr["delta_full"],
            "int_death_pct": round(tr["int_death_rate"] * 100, 1),
            "det_death_pct": round(tr["det_death_rate"] * 100, 1),
            "delta_no_death": tr["delta_no_death"],
            "death_avoidance_pct": round(tr["death_avoidance_fraction"] * 100, 1) if tr["death_avoidance_fraction"] is not None else None,
            "delta_penalty_removed": tr["delta_penalty_removed"],
            "det_preferred": tr["label_distribution"].get("det-preferred", 0),
            "internal_preferred": tr["label_distribution"].get("internal-preferred", 0),
            "no_preference": tr["label_distribution"].get("no-preference", 0),
        })

    agg_row = {
        "task": "Overall",
        "n": aggregate["n_episodes"],
        "int_mean": aggregate["int_mean"],
        "det_mean": aggregate["det_mean"],
        "delta": aggregate["delta_full"],
        "int_death_pct": round(aggregate["int_death_rate"] * 100, 1),
        "det_death_pct": round(aggregate["det_death_rate"] * 100, 1),
        "delta_no_death": aggregate.get("delta_no_death"),
        "death_avoidance_pct": round(aggregate["death_avoidance_fraction"] * 100, 1) if aggregate.get("death_avoidance_fraction") is not None else None,
        "delta_penalty_removed": aggregate["delta_penalty_removed"],
        "det_preferred": aggregate["label_distribution"].get("det-preferred", 0),
        "internal_preferred": aggregate["label_distribution"].get("internal-preferred", 0),
        "no_preference": aggregate["label_distribution"].get("no-preference", 0),
    }

    corr = aggregate.get("correlation_death_rate_diff_vs_delta", {})

    return {
        "rows": rows,
        "aggregate": agg_row,
        "correlation": {
            "pearson_r": corr.get("pearson_r"),
            "p_value": corr.get("p_value"),
            "n": corr.get("n_tasks"),
        },
    }


def main():
    parser = argparse.ArgumentParser(description="Plan-012 Death Decomposition Analysis")
    parser.add_argument("--data_dirs", required=True,
                        help="Comma-separated data directories (e.g. results/prescreening/,results/mvp/)")
    parser.add_argument("--output", default="results/death_decomposition_report.json",
                        help="Output JSON report path")
    parser.add_argument("--paper_table", default="results/paper_table1_data.json",
                        help="Paper table data output path")
    parser.add_argument("--tasks", default=None,
                        help="Comma-separated task types to filter (default: all)")
    args = parser.parse_args()

    data_dirs = [d.strip() for d in args.data_dirs.split(",") if d.strip()]
    task_filter = [t.strip() for t in args.tasks.split(",")] if args.tasks else None

    task_episodes = load_episodes(data_dirs, task_filter)
    if not task_episodes:
        print("ERROR: No episodes found in specified directories")
        return

    print(f"Loaded {sum(len(v) for v in task_episodes.values())} episodes "
          f"across {len(task_episodes)} tasks from {len(data_dirs)} directories")

    # Per-task analysis
    task_results = []
    for task_name in sorted(task_episodes.keys()):
        result = analyze_task(task_name, task_episodes[task_name])
        task_results.append(result)

    # Aggregate from raw scores (exact, not from per-task means)
    aggregate = aggregate_from_raw(data_dirs, task_filter)

    # Terminal output
    print_table(task_results, aggregate)

    # Save JSON report
    report = {
        "per_task": task_results,
        "aggregate": aggregate,
    }
    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\n[Saved report to {args.output}]")

    # Save paper table data
    paper_data = generate_paper_table_data(task_results, aggregate)
    os.makedirs(os.path.dirname(args.paper_table) or ".", exist_ok=True)
    with open(args.paper_table, "w") as f:
        json.dump(paper_data, f, indent=2)
    print(f"[Saved paper table data to {args.paper_table}]")


if __name__ == "__main__":
    main()

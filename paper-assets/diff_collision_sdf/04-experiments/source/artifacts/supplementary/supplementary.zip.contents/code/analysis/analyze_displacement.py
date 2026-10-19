#!/usr/bin/env python3
"""Displacement-filtered CAR analysis: distinguishes real safety from frozen/action-collapsed episodes."""

import argparse
import json
import os
import sys
from pathlib import Path


def load_eval(path):
    """Load eval JSON and normalize to list of task dicts with episodes."""
    with open(path) as f:
        data = json.load(f)
    if "results" in data:
        tasks = data["results"]
    elif "per_task" in data:
        tasks = data["per_task"]
    else:
        raise ValueError(f"Unknown JSON format in {path}: no 'results' or 'per_task' key")
    return tasks


def compute_frozen_rate_ee(episodes, threshold=0.0001):
    """Frozen rate based on EE displacement (paper definition)."""
    frozen = [e for e in episodes if e.get("max_ee_displacement", float('inf')) < threshold]
    return len(frozen) / len(episodes) if episodes else 0.0


def compute_frozen_rate_obs(episodes, threshold=0.0001):
    """Frozen rate based on obstacle displacement (NOT the paper definition)."""
    frozen = [e for e in episodes if e.get("max_displacement", float('inf')) < threshold]
    return len(frozen) / len(episodes) if episodes else 0.0


def analyze_task(episodes, threshold):
    """Compute raw/filtered CAR and frozen ratio for a list of episodes."""
    total = len(episodes)
    if total == 0:
        return {"raw_car": 0, "filtered_car": 0, "frozen_ratio": 0, "n_frozen": 0, "n_safe": 0, "total": 0}

    safe_eps = [e for e in episodes if not e["collided"]]
    n_safe = len(safe_eps)
    raw_car = n_safe / total

    # Frozen = EE displacement below threshold (paper definition)
    frozen_eps = [e for e in safe_eps if e.get("max_ee_displacement", float('inf')) < threshold]
    n_frozen = len(frozen_eps)
    real_safe = n_safe - n_frozen

    filtered_car = real_safe / total
    frozen_ratio = n_frozen / n_safe if n_safe > 0 else 0.0

    return {
        "raw_car": raw_car,
        "filtered_car": filtered_car,
        "frozen_ratio": frozen_ratio,
        "n_frozen": n_frozen,
        "n_safe": n_safe,
        "total": total,
    }


def analyze_file(path, threshold):
    """Analyze one eval JSON file. Returns overall stats + per-task breakdown."""
    tasks = load_eval(path)
    all_episodes = []
    per_task = []

    for t in tasks:
        eps = t["episodes"]
        all_episodes.extend(eps)
        stats = analyze_task(eps, threshold)
        stats["task_name"] = t.get("task_name", f"task_{t.get('task_id', '?')}")
        stats["tsr"] = t.get("TSR", 0)
        per_task.append(stats)

    overall = analyze_task(all_episodes, threshold)
    return overall, per_task, all_episodes


def _extract_object_name(task_name):
    """Extract the key object from task name like 'pick_up_the_orange_juice_and_place_it_...'"""
    name = task_name.replace("_", " ")
    for prefix in ["pick up the ", "put the ", "place the ", "move the "]:
        if name.startswith(prefix):
            name = name[len(prefix):]
            break
    for suffix in [" and place it", " and put it", " in the", " on the", " to the"]:
        idx = name.find(suffix)
        if idx > 0:
            name = name[:idx]
            break
    return name[:20]


def print_report(file_results, threshold):
    """Print formatted analysis report."""
    print(f"=== Displacement-Filtered CAR Analysis ===")
    print(f"Threshold: {threshold} m\n")

    for label, path, overall, per_task in file_results:
        print(f"[{label}] {os.path.basename(path)}")
        print(f"  Overall: Raw CAR={overall['raw_car']*100:.1f}% | "
              f"Filtered CAR={overall['filtered_car']*100:.1f}% | "
              f"Frozen={overall['frozen_ratio']*100:.1f}% ({overall['n_frozen']}/{overall['n_safe']} safe eps)")
        print(f"  Per-task:")
        for i, t in enumerate(per_task):
            short_name = _extract_object_name(t['task_name'])
            print(f"    T{i} ({short_name:20s}): Raw={t['raw_car']*100:.0f}% | "
                  f"Filtered={t['filtered_car']*100:.0f}% | "
                  f"Frozen={t['frozen_ratio']*100:.0f}% | TSR={t['tsr']*100:.0f}%")
        print()

    if len(file_results) > 1:
        print("=== Batch Comparison ===")
        print(f"{'| Eval':<25s} | {'Raw CAR':>8s} | {'Filt CAR':>8s} | {'Frozen%':>7s} | {'TSR':>5s} |")
        print(f"|{'-'*24}|{'-'*10}|{'-'*10}|{'-'*9}|{'-'*7}|")
        for label, path, overall, per_task in file_results:
            tsr = sum(t['tsr'] for t in per_task) / len(per_task) if per_task else 0
            print(f"| {label:<23s}| {overall['raw_car']*100:>7.1f}% | "
                  f"{overall['filtered_car']*100:>7.1f}% | "
                  f"{overall['frozen_ratio']*100:>6.1f}% | {tsr*100:>4.0f}% |")
        print()


def print_sensitivity(file_results_by_thresh, thresholds, labels):
    """Print sensitivity analysis across multiple thresholds."""
    print("=== Sensitivity Analysis (varying threshold) ===")
    header = f"{'| Threshold':<12s}"
    for label in labels:
        header += f"| {label[:15]:>15s} "
    header += "|"
    print(header)
    print("|" + "-" * 11 + ("|" + "-" * 17) * len(labels) + "|")

    for thresh in thresholds:
        row = f"| {thresh:<9.4f} "
        for results in file_results_by_thresh[thresh]:
            _, _, overall, _ = results
            row += f"| {overall['filtered_car']*100:>6.1f}% F={overall['frozen_ratio']*100:>3.0f}% "
        row += "|"
        print(row)
    print()


def make_histogram(file_results, threshold, output_path):
    """Generate displacement distribution histogram."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import numpy as np
    except ImportError:
        print("[WARN] matplotlib not available, skipping histogram", file=sys.stderr)
        return False

    n_files = len(file_results)
    fig, axes = plt.subplots(1, n_files, figsize=(6 * n_files, 4), squeeze=False)

    for idx, (label, path, overall, per_task) in enumerate(file_results):
        ax = axes[0, idx]
        tasks = load_eval(path)
        all_eps = []
        for t in tasks:
            all_eps.extend(t["episodes"])

        displacements = np.array([e["max_displacement"] for e in all_eps])
        collided = np.array([e["collided"] for e in all_eps])

        # Use log scale for better visibility
        disp_safe = displacements[~collided]
        disp_coll = displacements[collided]

        bins = np.logspace(np.log10(max(displacements.min(), 1e-12)), np.log10(displacements.max()), 40)

        ax.hist(disp_safe, bins=bins, alpha=0.7, label=f"Safe (n={len(disp_safe)})", color="steelblue")
        ax.hist(disp_coll, bins=bins, alpha=0.7, label=f"Collided (n={len(disp_coll)})", color="salmon")
        ax.axvline(threshold, color="red", linestyle="--", linewidth=1.5, label=f"Threshold={threshold}")
        ax.set_xscale("log")
        ax.set_xlabel("Max Displacement (m, log scale)")
        ax.set_ylabel("Episode Count")
        ax.set_title(label)
        ax.legend(fontsize=8)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"[INFO] Histogram saved to {output_path}")
    return True


def main():
    parser = argparse.ArgumentParser(description="Displacement-filtered CAR analysis")
    parser.add_argument("--files", nargs="+", required=True, help="Eval JSON file paths")
    parser.add_argument("--threshold", type=float, default=0.001, help="Displacement threshold (m)")
    parser.add_argument("--labels", nargs="+", default=None, help="Labels for each file")
    parser.add_argument("--histogram", type=str, default=None, help="Output histogram path (PDF/PNG)")
    parser.add_argument("--sensitivity", nargs="+", type=float, default=None,
                        help="Multiple thresholds for sensitivity analysis")
    args = parser.parse_args()

    # Expand directories
    files = []
    for f in args.files:
        if os.path.isdir(f):
            files.extend(sorted(Path(f).glob("*.json")))
        else:
            files.append(f)

    labels = args.labels if args.labels else [Path(f).stem for f in files]
    if len(labels) < len(files):
        labels.extend([Path(f).stem for f in files[len(labels):]])

    # Main analysis
    file_results = []
    for path, label in zip(files, labels):
        overall, per_task, _ = analyze_file(path, args.threshold)
        file_results.append((label, str(path), overall, per_task))

    print_report(file_results, args.threshold)

    # Sensitivity analysis
    if args.sensitivity:
        file_results_by_thresh = {}
        for thresh in args.sensitivity:
            results_at_thresh = []
            for path, label in zip(files, labels):
                overall, per_task, _ = analyze_file(path, thresh)
                results_at_thresh.append((label, str(path), overall, per_task))
            file_results_by_thresh[thresh] = results_at_thresh
        print_sensitivity(file_results_by_thresh, args.sensitivity, labels)

    # Histogram
    if args.histogram:
        make_histogram(file_results, args.threshold, args.histogram)


if __name__ == "__main__":
    main()

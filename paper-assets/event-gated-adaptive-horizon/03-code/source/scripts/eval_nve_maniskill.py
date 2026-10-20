#!/usr/bin/env python3
"""V/E ratio and NVE (Normalized Value Estimation) computation for DreamerV3 experiments.

Reads metrics.jsonl (or tensorboard events) from one or more logdirs,
computes ve_ratio = mean_predicted_value / actual_episode_return at each eval step.

When --baseline-logdir is provided, computes NVE = ve_ratio / baseline_ve_ratio
(normalized to baseline), and flags steps where NVE > threshold (default 1.5).

Compatible with both DMC and ManiSkill3 metrics formats.

Input:  one or more logdir paths (each containing metrics.jsonl or tfevent files)
Output: per-step table printed to stdout and optionally saved as JSON
"""

import argparse
import json
import os
import sys
from collections import defaultdict

try:
    from tensorboard.backend.event_processing.event_accumulator import EventAccumulator
    HAS_TB = True
except ImportError:
    HAS_TB = False


def load_metrics_jsonl(logdir):
    """Load eval_return and value_mean from metrics.jsonl."""
    path = os.path.join(logdir, "metrics.jsonl")
    if not os.path.exists(path):
        return None

    eval_returns = {}
    value_means = {}

    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            d = json.loads(line)
            step = d.get("step")
            if step is None:
                continue
            if "eval_return" in d:
                eval_returns[step] = d["eval_return"]
            if "value_mean" in d:
                value_means[step] = d["value_mean"]

    return eval_returns, value_means


def load_metrics_tensorboard(logdir):
    """Fallback: load from tensorboard event files."""
    if not HAS_TB:
        return None

    event_files = [f for f in os.listdir(logdir) if f.startswith("events.out.tfevents")]
    if not event_files:
        return None

    ea = EventAccumulator(logdir)
    ea.Reload()

    eval_returns = {}
    value_means = {}

    eval_tags = [t for t in ea.Tags().get("scalars", [])
                 if "eval" in t.lower() and "return" in t.lower()]
    value_tags = [t for t in ea.Tags().get("scalars", [])
                  if "value_mean" in t.lower() or t == "value_mean"]

    if eval_tags:
        for event in ea.Scalars(eval_tags[0]):
            eval_returns[event.step] = event.value
    if value_tags:
        for event in ea.Scalars(value_tags[0]):
            value_means[event.step] = event.value

    return eval_returns, value_means


def load_metrics(logdir):
    """Try metrics.jsonl first, fall back to tensorboard."""
    result = load_metrics_jsonl(logdir)
    if result is not None:
        return result

    result = load_metrics_tensorboard(logdir)
    if result is not None:
        return result

    print(f"ERROR: no metrics.jsonl or tensorboard events in {logdir}", file=sys.stderr)
    sys.exit(1)


def compute_ve_ratio(eval_returns, value_means):
    """Compute ve_ratio = value_mean / eval_return at each step.

    Steps with eval_return <= 0 are skipped.
    """
    common_steps = sorted(set(eval_returns) & set(value_means))
    results = []
    for step in common_steps:
        ret = eval_returns[step]
        val = value_means[step]
        if ret <= 0:
            continue
        ve_ratio = val / ret
        results.append({"step": step, "eval_return": ret, "value_mean": val, "ve_ratio": ve_ratio})
    return results


def compute_baseline_ve_ratios(baseline_logdir, min_step=0):
    """Compute ve_ratio series from a baseline logdir."""
    eval_returns, value_means = load_metrics(baseline_logdir)
    data = compute_ve_ratio(eval_returns, value_means)
    data = [d for d in data if d["step"] >= min_step]
    return data


def interpolate_baseline_ve_ratio(baseline_data, target_step):
    """Find nearest-neighbor baseline ve_ratio for a given step."""
    if not baseline_data:
        return None
    best = min(baseline_data, key=lambda d: abs(d["step"] - target_step))
    return best["ve_ratio"]


def main():
    parser = argparse.ArgumentParser(
        description="Compute V/E ratio (and baseline-normalized NVE) from DreamerV3 logdirs")
    parser.add_argument("--logdirs", nargs="+", required=True,
                        help="One or more experiment logdir paths")
    parser.add_argument("--labels", nargs="+", default=None,
                        help="Labels for each logdir (default: directory names)")
    parser.add_argument("--baseline-logdir", default=None,
                        help="Baseline logdir for NVE normalization")
    parser.add_argument("--threshold", type=float, default=1.5,
                        help="Pathological NVE threshold (applies to baseline-normalized NVE only, default: 1.5)")
    parser.add_argument("--min-step", type=int, default=0,
                        help="Only report steps >= this value")
    parser.add_argument("--output", default=None,
                        help="Save results as JSON to this path")
    args = parser.parse_args()

    if args.labels and len(args.labels) != len(args.logdirs):
        print("ERROR: --labels count must match --logdirs count", file=sys.stderr)
        sys.exit(1)

    labels = args.labels or [os.path.basename(d.rstrip("/")) for d in args.logdirs]

    baseline_data = None
    if args.baseline_logdir:
        baseline_data = compute_baseline_ve_ratios(args.baseline_logdir, args.min_step)
        if not baseline_data:
            print(f"ERROR: no valid ve_ratio data from baseline {args.baseline_logdir}", file=sys.stderr)
            sys.exit(1)

    has_baseline = baseline_data is not None
    all_results = {}

    for logdir, label in zip(args.logdirs, labels):
        eval_returns, value_means = load_metrics(logdir)
        ve_data = compute_ve_ratio(eval_returns, value_means)
        ve_data = [d for d in ve_data if d["step"] >= args.min_step]

        if not ve_data:
            print(f"\n[{label}] No valid ve_ratio data (step >= {args.min_step})")
            all_results[label] = {"data": [], "max_ve_ratio": None, "pathological_steps": 0}
            continue

        if has_baseline:
            for d in ve_data:
                bl_ve = interpolate_baseline_ve_ratio(baseline_data, d["step"])
                if bl_ve and bl_ve > 0:
                    d["nve"] = d["ve_ratio"] / bl_ve
                else:
                    d["nve"] = None

        max_ve = max(d["ve_ratio"] for d in ve_data)

        print(f"\n{'=' * 80}")
        print(f"  {label}")
        print(f"{'=' * 80}")

        if has_baseline:
            print(f"  {'Step':>8s}  {'eval_return':>12s}  {'value_mean':>12s}"
                  f"  {'ve_ratio (raw)':>15s}  {'NVE (normalized)':>17s}  Flag")
            print(f"  {'-' * 8}  {'-' * 12}  {'-' * 12}  {'-' * 15}  {'-' * 17}  ----")
            pathological = []
            for d in ve_data:
                nve_str = f"{d['nve']:>17.4f}" if d.get("nve") is not None else f"{'N/A':>17s}"
                flag = ""
                if d.get("nve") is not None and d["nve"] > args.threshold:
                    flag = " *** PATHOLOGICAL"
                    pathological.append(d)
                print(f"  {d['step']:>8d}  {d['eval_return']:>12.2f}  {d['value_mean']:>12.4f}"
                      f"  {d['ve_ratio']:>15.4f}  {nve_str}{flag}")

            nve_values = [d["nve"] for d in ve_data if d.get("nve") is not None]
            max_nve = max(nve_values) if nve_values else None
            max_nve_str = f"{max_nve:.4f}" if max_nve is not None else "N/A"
            print(f"\n  Summary: max_ve_ratio = {max_ve:.4f}, max_NVE = {max_nve_str}, "
                  f"pathological_steps = {len(pathological)}/{len(ve_data)}, "
                  f"threshold = {args.threshold} (applies to baseline-normalized NVE only)")

            all_results[label] = {
                "data": ve_data,
                "max_ve_ratio": round(max_ve, 6),
                "max_nve": round(max_nve, 6) if max_nve is not None else None,
                "pathological_steps": len(pathological),
                "total_steps": len(ve_data),
            }
        else:
            print(f"  {'Step':>8s}  {'eval_return':>12s}  {'value_mean':>12s}  {'ve_ratio':>10s}")
            print(f"  {'-' * 8}  {'-' * 12}  {'-' * 12}  {'-' * 10}")
            for d in ve_data:
                print(f"  {d['step']:>8d}  {d['eval_return']:>12.2f}  {d['value_mean']:>12.4f}"
                      f"  {d['ve_ratio']:>10.4f}")

            print(f"\n  Summary: max_ve_ratio = {max_ve:.4f}"
                  f" (no baseline provided, pathological threshold not applied)")

            all_results[label] = {
                "data": ve_data,
                "max_ve_ratio": round(max_ve, 6),
                "total_steps": len(ve_data),
            }

    if args.output:
        serializable = {}
        for label, res in all_results.items():
            entry = {
                "max_ve_ratio": res.get("max_ve_ratio"),
                "total_steps": res.get("total_steps", 0),
            }
            if has_baseline:
                entry["max_nve"] = res.get("max_nve")
                entry["pathological_steps"] = res.get("pathological_steps", 0)
                entry["trajectory"] = [
                    {"step": d["step"], "ve_ratio": round(d["ve_ratio"], 6),
                     "nve": round(d["nve"], 6) if d.get("nve") is not None else None}
                    for d in res["data"]
                ]
            else:
                entry["trajectory"] = [
                    {"step": d["step"], "ve_ratio": round(d["ve_ratio"], 6)}
                    for d in res["data"]
                ]
            serializable[label] = entry
        os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
        with open(args.output, "w") as f:
            json.dump(serializable, f, indent=2)
        print(f"\nSaved JSON to {args.output}")


if __name__ == "__main__":
    main()

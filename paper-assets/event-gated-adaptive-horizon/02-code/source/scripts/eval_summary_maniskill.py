#!/usr/bin/env python3
"""Comprehensive evaluation summary for DreamerV3 experiments.

Aggregates metrics across one or more logdirs into a single summary table:
  exp_id, task, config, final_eval_return, peak_eval_return,
  NVE_at_peak, NVE_max, success_rate (ManiSkill), dt_distribution

Compatible with both DMC and ManiSkill3 metrics formats.

Input:  one or more logdir paths (with optional task/config metadata)
Output: formatted summary table to stdout, optionally saved as JSON/CSV
"""

import argparse
import csv
import json
import os
import sys
from collections import defaultdict


def load_all_metrics(logdir):
    """Load all records from metrics.jsonl."""
    path = os.path.join(logdir, "metrics.jsonl")
    if not os.path.exists(path):
        print(f"WARNING: {path} not found", file=sys.stderr)
        return []
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def extract_eval_returns(records):
    """Extract {step: eval_return} from records."""
    result = {}
    for r in records:
        if "eval_return" in r and "step" in r:
            result[r["step"]] = r["eval_return"]
    return result


def extract_value_means(records):
    """Extract {step: value_mean} from records."""
    result = {}
    for r in records:
        if "value_mean" in r and "step" in r:
            result[r["step"]] = r["value_mean"]
    return result


def extract_success_rates(records):
    """Extract success_rate from records (ManiSkill-specific).

    Tries multiple field names: eval_success_rate, success_rate,
    eval/success_rate, eval_success.
    """
    candidates = ["eval_success_rate", "success_rate", "eval/success_rate", "eval_success"]
    result = {}
    for r in records:
        step = r.get("step")
        if step is None:
            continue
        for key in candidates:
            if key in r:
                result[step] = r[key]
                break
    return result


def extract_dt_distribution(records):
    """Extract final dt distribution from gate metrics."""
    gate_records = [r for r in records if "gate_dt_1_frac" in r]
    if not gate_records:
        return None

    last = gate_records[-1]
    dist = {}
    for i in range(1, 17):
        key = f"gate_dt_{i}_frac"
        if key in last:
            dist[i] = last[key]
    return dist


def extract_dt_stats(records):
    """Extract final dt_mean, dt_std, entropy."""
    gate_records = [r for r in records if "gate_dt_mean" in r]
    if not gate_records:
        return {}
    last = gate_records[-1]
    return {
        "dt_mean": last.get("gate_dt_mean"),
        "dt_std": last.get("gate_dt_std"),
        "entropy": last.get("gate_empirical_entropy"),
    }


def infer_task_from_logdir(dirname):
    """Try to infer task name from logdir name."""
    name = dirname.lower()
    if "walker" in name:
        return "walker_walk"
    if "cheetah" in name:
        return "cheetah_run"
    if "pickcube" in name:
        return "PickCube-v1"
    if "stackcube" in name:
        return "StackCube-v1"
    if "peginsertion" in name:
        return "PegInsertionSide-v1"
    return "unknown"


def infer_config_from_logdir(dirname):
    """Try to infer config type from logdir name."""
    name = dirname.lower()
    if "baseline" in name:
        return "baseline"
    if "sgs" in name:
        return "sgs"
    if "frozen" in name:
        return "frozen_dt_emb"
    if "no_dt_embed" in name or "no_embed" in name:
        return "no_dt_embed"
    if "fixed_dt" in name:
        return "fixed_dt"
    if "event_gated" in name or "008" in name or "009" in name:
        return "event_gated"
    return "unknown"


def summarize_logdir(logdir, label=None, task=None, config=None):
    """Compute all summary metrics for one logdir."""
    dirname = os.path.basename(logdir.rstrip("/"))
    exp_id = label or dirname

    records = load_all_metrics(logdir)
    if not records:
        return {"exp_id": exp_id, "error": "no metrics.jsonl"}

    task = task or infer_task_from_logdir(dirname)
    config = config or infer_config_from_logdir(dirname)

    eval_returns = extract_eval_returns(records)
    value_means = extract_value_means(records)
    success_rates = extract_success_rates(records)
    dt_dist = extract_dt_distribution(records)
    dt_stats = extract_dt_stats(records)

    # Final eval return (average of last 3 eval points)
    if eval_returns:
        sorted_evals = sorted(eval_returns.items())
        tail = sorted_evals[-3:] if len(sorted_evals) >= 3 else sorted_evals
        final_eval_return = sum(v for _, v in tail) / len(tail)
        peak_eval_return = max(eval_returns.values())
        peak_step = max(eval_returns, key=eval_returns.get)
    else:
        final_eval_return = None
        peak_eval_return = None
        peak_step = None

    # NVE at peak and max NVE
    nve_at_peak = None
    nve_max = None
    if eval_returns and value_means:
        nve_values = {}
        for step in set(eval_returns) & set(value_means):
            ret = eval_returns[step]
            if ret > 0:
                nve_values[step] = value_means[step] / ret

        if nve_values:
            nve_max = max(nve_values.values())
            if peak_step in nve_values:
                nve_at_peak = nve_values[peak_step]

    # Success rate (ManiSkill)
    final_success_rate = None
    if success_rates:
        sorted_sr = sorted(success_rates.items())
        tail = sorted_sr[-3:] if len(sorted_sr) >= 3 else sorted_sr
        final_success_rate = sum(v for _, v in tail) / len(tail)

    # dt distribution summary string
    dt_summary = ""
    if dt_dist:
        parts = []
        for k in sorted(dt_dist.keys()):
            v = dt_dist[k]
            if v > 0.005:
                parts.append(f"{k}:{v:.0%}")
        dt_summary = " ".join(parts)

    return {
        "exp_id": exp_id,
        "task": task,
        "config": config,
        "final_eval_return": round(final_eval_return, 2) if final_eval_return is not None else None,
        "peak_eval_return": round(peak_eval_return, 2) if peak_eval_return is not None else None,
        "peak_step": peak_step,
        "NVE_at_peak": round(nve_at_peak, 4) if nve_at_peak is not None else None,
        "NVE_max": round(nve_max, 4) if nve_max is not None else None,
        "success_rate": round(final_success_rate, 4) if final_success_rate is not None else None,
        "dt_distribution": dt_summary or None,
        "dt_mean": round(dt_stats.get("dt_mean"), 4) if dt_stats.get("dt_mean") is not None else None,
        "dt_std": round(dt_stats.get("dt_std"), 4) if dt_stats.get("dt_std") is not None else None,
        "gate_entropy": round(dt_stats.get("entropy"), 4) if dt_stats.get("entropy") is not None else None,
    }


def print_table(summaries):
    """Print formatted summary table."""
    cols = [
        ("exp_id", 35), ("task", 16), ("config", 14),
        ("final_ret", 10), ("peak_ret", 10), ("NVE@peak", 9), ("NVE_max", 8),
        ("success", 8), ("dt_dist", 30),
    ]

    header = "  ".join(f"{name:>{width}s}" for name, width in cols)
    sep = "  ".join("-" * width for _, width in cols)

    print(f"\n{header}")
    print(f"{sep}")

    for s in summaries:
        def fmt(v, precision=2):
            if v is None:
                return "—"
            if isinstance(v, float):
                return f"{v:.{precision}f}"
            return str(v)

        vals = [
            f"{s['exp_id']:>35s}",
            f"{s.get('task', '—'):>16s}",
            f"{s.get('config', '—'):>14s}",
            f"{fmt(s.get('final_eval_return')):>10s}",
            f"{fmt(s.get('peak_eval_return')):>10s}",
            f"{fmt(s.get('NVE_at_peak'), 4):>9s}",
            f"{fmt(s.get('NVE_max'), 4):>8s}",
            f"{fmt(s.get('success_rate'), 4):>8s}",
            f"{s.get('dt_distribution') or '—':>30s}",
        ]
        print("  ".join(vals))


def main():
    parser = argparse.ArgumentParser(
        description="Generate evaluation summary table for DreamerV3 experiments")
    parser.add_argument("--logdirs", nargs="+", required=True,
                        help="One or more experiment logdir paths")
    parser.add_argument("--labels", nargs="+", default=None,
                        help="Labels for each logdir")
    parser.add_argument("--tasks", nargs="+", default=None,
                        help="Task names for each logdir (auto-inferred if omitted)")
    parser.add_argument("--configs", nargs="+", default=None,
                        help="Config names for each logdir (auto-inferred if omitted)")
    parser.add_argument("--output-json", default=None,
                        help="Save results as JSON")
    parser.add_argument("--output-csv", default=None,
                        help="Save results as CSV")
    args = parser.parse_args()

    n = len(args.logdirs)
    labels = args.labels or [None] * n
    tasks = args.tasks or [None] * n
    configs = args.configs or [None] * n

    for lst_name, lst in [("labels", args.labels), ("tasks", args.tasks), ("configs", args.configs)]:
        if lst and len(lst) != n:
            print(f"ERROR: --{lst_name} count ({len(lst)}) must match --logdirs count ({n})",
                  file=sys.stderr)
            sys.exit(1)

    summaries = []
    for logdir, label, task, config in zip(args.logdirs, labels, tasks, configs):
        s = summarize_logdir(logdir, label=label, task=task, config=config)
        summaries.append(s)

    print_table(summaries)

    if args.output_json:
        os.makedirs(os.path.dirname(os.path.abspath(args.output_json)), exist_ok=True)
        with open(args.output_json, "w") as f:
            json.dump(summaries, f, indent=2)
        print(f"\nSaved JSON to {args.output_json}")

    if args.output_csv:
        os.makedirs(os.path.dirname(os.path.abspath(args.output_csv)), exist_ok=True)
        fieldnames = [
            "exp_id", "task", "config", "final_eval_return", "peak_eval_return",
            "peak_step", "NVE_at_peak", "NVE_max", "success_rate",
            "dt_distribution", "dt_mean", "dt_std", "gate_entropy",
        ]
        with open(args.output_csv, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(summaries)
        print(f"Saved CSV to {args.output_csv}")


if __name__ == "__main__":
    main()

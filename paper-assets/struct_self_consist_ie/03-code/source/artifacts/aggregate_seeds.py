#!/usr/bin/env python3
"""Aggregate multi-seed signal reports for scaling curve analysis.

Reads N full_signal_report.json files (from compute_signals.py), computes
per-metric mean/std across seeds, and outputs:
  1. stdout: DATA dict entries for plot_scaling_curve.py (copy-paste ready)
  2. JSON file: full aggregated results with mean, std, and per-seed values

Optionally aggregates per-instance JSON files (e.g. fewnerd_per_instance.json)
by averaging F1 scores across seeds for each instance.

Usage:
    python artifacts/aggregate_seeds.py \
      --reports seed42/full_signal_report.json \
               seed123/full_signal_report.json \
               seed456/full_signal_report.json \
      --model-size 7 --regime ft --dataset fewnerd \
      --output-json aggregated_scaling_result.json

    # With per-instance aggregation:
    python artifacts/aggregate_seeds.py \
      --reports seed42/full_signal_report.json \
               seed123/full_signal_report.json \
               seed456/full_signal_report.json \
      --model-size 7 --regime ft --dataset fewnerd \
      --output-json aggregated_scaling_result.json \
      --per-instance seed42/fewnerd_per_instance.json \
                     seed123/fewnerd_per_instance.json \
                     seed456/fewnerd_per_instance.json \
      --per-instance-output aggregated_per_instance.json
"""

import argparse
import json
import math
import sys
from pathlib import Path

DS_NAME_MAP = {
    "scierc": "SciERC",
    "conll2003": "CoNLL",
    "conll": "CoNLL",
    "fewnerd": "FewNERD",
}


def load_report(path):
    with open(path) as f:
        return json.load(f)


def extract_metrics(ds_data):
    """Extract the 7 scaling-curve metrics from a dataset entry."""
    signals = ds_data.get("signals", {})
    baselines = ds_data.get("baselines", {})

    greedy_f1 = baselines.get("greedy", {}).get("mean")
    oracle_f1 = baselines.get("oracle", {}).get("mean")
    consensus_lp_f1 = baselines.get("consensus_lp_weighted", {}).get("mean")

    degen = ds_data.get("degeneracy_rate")
    if degen is not None:
        degen = degen * 100  # convert to percentage

    construction_lp_delta = None
    if consensus_lp_f1 is not None and greedy_f1 is not None:
        construction_lp_delta = (consensus_lp_f1 - greedy_f1) * 100

    return {
        "lp_rho": signals.get("LP", {}).get("rho"),
        "sj_rho": signals.get("SJ", {}).get("rho"),
        "vc_rho": signals.get("VC", {}).get("rho"),
        "degen": degen,
        "construction_lp_delta": construction_lp_delta,
        "greedy_f1": greedy_f1,
        "oracle_f1": oracle_f1,
    }


def mean_std(values):
    """Compute mean and std for a list of floats, skipping None."""
    valid = [v for v in values if v is not None and math.isfinite(v)]
    if not valid:
        return None, None
    m = sum(valid) / len(valid)
    if len(valid) < 2:
        return m, 0.0
    var = sum((x - m) ** 2 for x in valid) / (len(valid) - 1)
    return m, math.sqrt(var)


def aggregate_metrics(per_seed_metrics):
    """Aggregate metrics across seeds. Returns {key: {mean, std, per_seed}}."""
    all_keys = set()
    for m in per_seed_metrics:
        all_keys.update(m.keys())

    result = {}
    for key in sorted(all_keys):
        values = [m.get(key) for m in per_seed_metrics]
        m, s = mean_std(values)
        result[key] = {"mean": m, "std": s, "per_seed": values}
    return result


def format_data_dict(agg, model_size, regime, ds_display):
    """Format as DATA dict entry for plot_scaling_curve.py."""
    def fmt(key, decimals=3):
        v = agg[key]["mean"]
        s = agg[key]["std"]
        if v is None:
            return f'"{key}": None'
        v_r = round(v, decimals)
        if s is not None and s > 0:
            return f'"{key}": {v_r},  # mean ± {round(s, decimals)}'
        return f'"{key}": {v_r}'

    key_str = f'({model_size}, "{regime}", "{ds_display}")'
    lines = [f'DATA[{key_str}] = {{']
    for k in ["lp_rho", "sj_rho", "vc_rho", "degen", "construction_lp_delta",
              "greedy_f1", "oracle_f1"]:
        if k in agg:
            decimals = 1 if k == "degen" else (2 if k == "construction_lp_delta" else 3)
            lines.append(f'    {fmt(k, decimals)},')
    lines.append('}')
    return "\n".join(lines)


def aggregate_per_instance(paths):
    """Aggregate per-instance JSONs across seeds by averaging F1 per instance."""
    all_data = []
    for p in paths:
        with open(p) as f:
            all_data.append(json.load(f))

    n_seeds = len(all_data)
    n_instances = len(all_data[0].get("greedy_f1", []))

    for d in all_data:
        for key in ["greedy_f1", "construction_lp_f1", "oracle_f1"]:
            if len(d.get(key, [])) != n_instances:
                print(f"WARNING: instance count mismatch for {key}: "
                      f"expected {n_instances}, got {len(d.get(key, []))}", file=sys.stderr)

    result = {}
    for key in ["greedy_f1", "construction_lp_f1", "oracle_f1"]:
        seed_arrays = [d.get(key, []) for d in all_data]
        if not all(len(a) == n_instances for a in seed_arrays):
            result[key] = seed_arrays[0]
            continue
        result[key] = [
            sum(seed_arrays[s][i] for s in range(n_seeds)) / n_seeds
            for i in range(n_instances)
        ]

    # degenerate: instance is degenerate if degenerate in majority of seeds
    degen_arrays = [d.get("degenerate", []) for d in all_data]
    if all(len(a) == n_instances for a in degen_arrays):
        result["degenerate"] = [
            sum(1 for s in range(n_seeds) if degen_arrays[s][i]) > n_seeds / 2
            for i in range(n_instances)
        ]
    else:
        result["degenerate"] = degen_arrays[0] if degen_arrays else []

    result["_meta"] = {
        "n_seeds": n_seeds,
        "n_instances": n_instances,
        "source_files": [str(p) for p in paths],
    }
    return result


def main():
    parser = argparse.ArgumentParser(
        description="Aggregate multi-seed signal reports for scaling curves")
    parser.add_argument("--reports", required=True, nargs="+",
                        help="Paths to full_signal_report.json files (one per seed)")
    parser.add_argument("--model-size", required=True, type=int,
                        help="Model size in B (e.g. 7)")
    parser.add_argument("--regime", required=True,
                        help="Regime: ft/zs/fs")
    parser.add_argument("--dataset", required=True,
                        help="Dataset key (e.g. fewnerd, scierc, conll2003)")
    parser.add_argument("--output-json", default="aggregated_scaling_result.json",
                        help="Output path for full JSON results")
    parser.add_argument("--per-instance", nargs="+", default=None,
                        help="Paths to per-instance JSON files (one per seed)")
    parser.add_argument("--per-instance-output", default=None,
                        help="Output path for aggregated per-instance JSON")

    args = parser.parse_args()

    ds_display = DS_NAME_MAP.get(args.dataset, args.dataset)

    # Load and extract metrics from each seed
    per_seed_metrics = []
    raw_reports = []
    for rp in args.reports:
        report = load_report(rp)
        raw_reports.append(report)
        # full_signal_report.json is keyed by dataset name
        ds_data = report.get(args.dataset)
        if ds_data is None:
            # try case-insensitive match
            for k, v in report.items():
                if k.lower() == args.dataset.lower():
                    ds_data = v
                    break
        if ds_data is None and len(report) == 1:
            ds_data = next(iter(report.values()))
        if ds_data is None:
            print(f"ERROR: dataset '{args.dataset}' not found in {rp}", file=sys.stderr)
            print(f"  Available keys: {list(report.keys())}", file=sys.stderr)
            sys.exit(1)
        per_seed_metrics.append(extract_metrics(ds_data))

    agg = aggregate_metrics(per_seed_metrics)

    # Print DATA dict entry
    print(format_data_dict(agg, args.model_size, args.regime, ds_display))
    print()

    # Print summary
    n = len(args.reports)
    print(f"# {n}-seed aggregation for Qwen3-{args.model_size}B {args.regime.upper()} on {ds_display}")
    for k in ["lp_rho", "sj_rho", "vc_rho", "degen", "construction_lp_delta",
              "greedy_f1", "oracle_f1"]:
        if k in agg and agg[k]["mean"] is not None:
            m, s = agg[k]["mean"], agg[k]["std"]
            vals = agg[k]["per_seed"]
            print(f"#   {k:25s}: {m:.4f} ± {s:.4f}  seeds={vals}")

    # Write full JSON
    output = {
        "model_size": args.model_size,
        "regime": args.regime,
        "dataset": args.dataset,
        "dataset_display": ds_display,
        "n_seeds": n,
        "source_reports": args.reports,
        "aggregated_metrics": {
            k: {"mean": round(v["mean"], 6) if v["mean"] is not None else None,
                "std": round(v["std"], 6) if v["std"] is not None else None,
                "per_seed": v["per_seed"]}
            for k, v in agg.items()
        },
        "data_dict_entry": {
            k: round(v["mean"], 3) if v["mean"] is not None else None
            for k, v in agg.items()
        },
    }

    with open(args.output_json, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nJSON written to {args.output_json}")

    # Per-instance aggregation
    if args.per_instance:
        pi_output = args.per_instance_output or str(
            Path(args.output_json).parent / f"{args.dataset}_aggregated_per_instance.json")
        result = aggregate_per_instance(args.per_instance)
        with open(pi_output, "w") as f:
            json.dump(result, f, indent=2)
        print(f"Per-instance JSON written to {pi_output}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Format signal analysis results for the scaling curve DATA dict.

Reads full_signal_report.json (produced by compute_signals.py) and outputs
Python dict entries compatible with plot_scaling_curve.py.

Usage:
    python format_for_scaling.py --report /path/to/full_signal_report.json \
        --model-size 72 --regime zs

    # Process multiple reports at once
    python format_for_scaling.py \
        --report /path/to/7b_ft/full_signal_report.json --model-size 7 --regime ft \
        --report /path/to/72b_fs/full_signal_report.json --model-size 72 --regime fs
"""

import argparse
import json
import sys

DS_NAME_MAP = {
    "scierc": "SciERC",
    "conll2003": "CoNLL",
    "conll": "CoNLL",
    "fewnerd": "FewNERD",
}


def format_entry(ds_data, model_size, regime, ds_display):
    """Extract scaling curve metrics from one dataset's report entry."""
    signals = ds_data.get("signals", {})
    baselines = ds_data.get("baselines", {})

    lp_rho = signals.get("LP", {}).get("rho")
    sj_rho = signals.get("SJ", {}).get("rho")
    vc_rho = signals.get("VC", {}).get("rho")

    greedy_f1 = baselines.get("greedy", {}).get("mean")
    oracle_f1 = baselines.get("oracle", {}).get("mean")
    consensus_lp_f1 = baselines.get("consensus_lp_weighted", {}).get("mean")

    degen = ds_data.get("degeneracy_rate")
    if degen is not None:
        degen = round(degen * 100, 1)

    construction_lp_delta = None
    if consensus_lp_f1 is not None and greedy_f1 is not None:
        construction_lp_delta = round((consensus_lp_f1 - greedy_f1) * 100, 2)

    def fmt(v, decimals=3):
        if v is None or (isinstance(v, float) and not __import__("math").isfinite(v)):
            return "None"
        return f"{round(v, decimals)}"

    entry = {
        "lp_rho": lp_rho,
        "sj_rho": sj_rho,
        "vc_rho": vc_rho,
        "degen": degen,
        "construction_lp_delta": construction_lp_delta,
        "greedy_f1": round(greedy_f1, 3) if greedy_f1 is not None else None,
        "oracle_f1": round(oracle_f1, 3) if oracle_f1 is not None else None,
    }

    key_str = f'({model_size}, "{regime}", "{ds_display}")'
    vals = ", ".join(f'"{k}": {fmt(v)}' for k, v in entry.items())
    return key_str, entry, f"    {key_str:30s}: {{{vals}}},"


def process_report(report_path, model_size, regime):
    """Process one full_signal_report.json file."""
    with open(report_path) as f:
        report = json.load(f)

    entries = []
    for ds_key, ds_data in sorted(report.items()):
        ds_display = DS_NAME_MAP.get(ds_key, ds_key)
        key_str, entry_dict, code_line = format_entry(
            ds_data, model_size, regime, ds_display)
        entries.append((key_str, entry_dict, code_line))
    return entries


def main():
    parser = argparse.ArgumentParser(
        description="Format signal results for scaling curve DATA dict")
    parser.add_argument("--report", required=True, nargs="+",
                        help="Path(s) to full_signal_report.json")
    parser.add_argument("--model-size", required=True, nargs="+",
                        help="Model size(s) (one per report)")
    parser.add_argument("--regime", required=True, nargs="+",
                        help="Regime(s): ft/zs/fs (one per report)")
    args = parser.parse_args()

    if len(args.report) != len(args.model_size) or \
       len(args.report) != len(args.regime):
        print("ERROR: --report, --model-size, --regime must have "
              "the same number of arguments")
        sys.exit(1)

    print("# ─── Copy-paste into plot_scaling_curve.py DATA dict ───")
    print()

    all_entries = []
    for report_path, model_size, regime in zip(
            args.report, args.model_size, args.regime):
        try:
            size_int = int(model_size)
        except ValueError:
            size_int = model_size

        entries = process_report(report_path, size_int, regime)
        all_entries.extend(entries)

        label = f"Qwen3-{model_size}B {'FT' if regime == 'ft' else 'ZS' if regime == 'zs' else 'FS'}"
        print(f"    # ── {label} ──")
        for key_str, entry_dict, code_line in entries:
            print(code_line)
        print()

    # Also print a compact summary table
    print()
    print("# ─── Summary Table ───")
    print(f"# {'Key':<35} {'LP_ρ':>7} {'SJ_ρ':>7} {'VC_ρ':>7} "
          f"{'Degen%':>7} {'Δ_LP':>7} {'Greedy':>7} {'Oracle':>7}")
    for key_str, entry, _ in all_entries:
        def f(v):
            return f"{v:7.3f}" if v is not None else "   None"
        print(f"# {key_str:<35} {f(entry['lp_rho'])} {f(entry['sj_rho'])} "
              f"{f(entry['vc_rho'])} {f(entry['degen'])} "
              f"{f(entry['construction_lp_delta'])} "
              f"{f(entry['greedy_f1'])} {f(entry['oracle_f1'])}")


if __name__ == "__main__":
    main()

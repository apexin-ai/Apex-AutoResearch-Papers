"""PI sweep analysis: rank configs by eff_rank retention, PPL, and w_t stability.

Usage:
    python analyze_sweep.py --sweep-dir /root/autodl-tmp/output_p0/pi_sweep/

Input:
    Sweep directory containing kp{X}_ki{Y}/ subdirs, each with control_log.jsonl
    and G0/G1/G2 generation directories containing metrics.jsonl.

Output:
    - Printed ranking table (sorted by eff_rank retention)
    - JSON report with per-config metrics and top-3 selection
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

import numpy as np


def read_last_metrics(metrics_path: str) -> dict:
    last_line = None
    with open(metrics_path) as f:
        for line in f:
            line = line.strip()
            if line:
                last_line = line
    if last_line is None:
        raise ValueError(f"Empty metrics file: {metrics_path}")
    return json.loads(last_line)


def read_control_log(log_path: str) -> list[dict]:
    entries = []
    with open(log_path) as f:
        for line in f:
            line = line.strip()
            if line:
                entries.append(json.loads(line))
    return entries


def analyze_config(config_dir: Path) -> dict | None:
    """Extract key metrics from a single sweep config directory."""
    g0_metrics = config_dir / "G0" / "metrics.jsonl"
    g2_metrics = config_dir / "G2" / "metrics.jsonl"
    control_log = config_dir / "control_log.jsonl"

    if not g0_metrics.exists() or not g2_metrics.exists():
        return None

    g0 = read_last_metrics(str(g0_metrics))
    g2 = read_last_metrics(str(g2_metrics))

    g0_rank = g0.get("eff_rank", g0.get("effective_rank", g0.get("spectral_effective_rank")))
    g2_rank = g2.get("eff_rank", g2.get("effective_rank", g2.get("spectral_effective_rank")))
    g2_ppl = g2.get("ppl", g2.get("perplexity"))

    if g0_rank is None or g2_rank is None:
        return None

    retention = g2_rank / g0_rank if g0_rank > 0 else 0.0

    w_stability = float("nan")
    if control_log.exists():
        entries = read_control_log(str(control_log))
        w_values = [e.get("w_t", e.get("w")) for e in entries if "w_t" in e or "w" in e]
        if len(w_values) > 1:
            w_stability = float(np.std(w_values, ddof=1))

    return {
        "g0_eff_rank": g0_rank,
        "g2_eff_rank": g2_rank,
        "retention": retention,
        "g2_ppl": g2_ppl,
        "w_stability": w_stability,
    }


def main():
    parser = argparse.ArgumentParser(description="Analyze PI sweep results")
    parser.add_argument("--sweep-dir", required=True, help="Directory containing kpX_kiY/ subdirs")
    parser.add_argument("--output", default="sweep_report.json", help="Output JSON path")
    args = parser.parse_args()

    sweep_dir = Path(args.sweep_dir)
    pattern = re.compile(r"kp([\d.]+)_ki([\d.]+)")
    results = []

    for d in sorted(sweep_dir.iterdir()):
        m = pattern.match(d.name)
        if not m or not d.is_dir():
            continue

        kp, ki = float(m.group(1)), float(m.group(2))
        metrics = analyze_config(d)
        if metrics is None:
            print(f"SKIP: {d.name} (incomplete)", file=sys.stderr)
            continue

        results.append({"Kp": kp, "Ki": ki, "dir": d.name, **metrics})

    if not results:
        print("ERROR: No complete configs found.", file=sys.stderr)
        sys.exit(1)

    results.sort(key=lambda r: r["retention"], reverse=True)

    print(f"\nPI Sweep Results ({len(results)} configs)")
    print("=" * 85)
    print(f"{'Kp':<8} {'Ki':<8} {'G0 rank':<10} {'G2 rank':<10} {'Retention':<10} {'G2 PPL':<10} {'w_std':<8}")
    print("-" * 85)
    for r in results:
        print(f"{r['Kp']:<8.3f} {r['Ki']:<8.3f} {r['g0_eff_rank']:<10.1f} {r['g2_eff_rank']:<10.1f} "
              f"{r['retention']:<10.4f} {r['g2_ppl']:<10.2f} {r['w_stability']:<8.4f}")

    top3 = results[:3]
    print(f"\nTop-3 by retention: {', '.join(f'Kp={r['Kp']} Ki={r['Ki']}' for r in top3)}")

    report = {
        "total_configs": len(results),
        "ranking": results,
        "top3": top3,
        "selection_criterion": "eff_rank retention (g2_rank / g0_rank), descending",
    }

    with open(args.output, "w") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\nReport saved to {args.output}")


if __name__ == "__main__":
    main()

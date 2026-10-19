"""M2 statistical analysis: compare hard-negative strategies across encoders and seeds.

Collects best R@1 from training logs, runs paired t-tests, Wilcoxon,
bootstrap CIs, and Cohen's d.  Outputs JSON + Markdown.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
from scipy import stats

# ── Configuration ──────────────────────────────────────────────────────

ENCODERS = ["qwen", "starcoder"]
STRATEGIES = ["random", "embedding_distance", "dataflow_aware"]
SEEDS = [42, 43, 44]

CHECKPOINT_BASE = "/root/autodl-tmp/structfuse/checkpoints"
OUTPUT_BASE = "/root/autodl-tmp/structfuse/full_m2_outputs"

# StarCoder s42 used 3 epochs (others used 2)
HETEROGENEITY_NOTES = {
    ("starcoder", "random", 42): "3 epochs (others: 2)",
    ("starcoder", "embedding_distance", 42): "3 epochs (others: 2)",
    ("starcoder", "dataflow_aware", 42): "3 epochs (others: 2)",
}


def _candidate_dirs(encoder: str, strategy: str, seed: int) -> List[str]:
    """Return candidate directories to search for a run's output."""
    enc_short = {"qwen": "qwen", "starcoder": "starcoder"}[encoder]
    enc_full = {"qwen": "m2_full_qwen", "starcoder": "m2_full_starcoder"}[encoder]
    tag = f"{strategy}_s{seed}"
    tag_enc = f"{strategy}_{enc_short}_s{seed}"
    return [
        f"{OUTPUT_BASE}/{tag}",
        f"{OUTPUT_BASE}/{tag_enc}",
        f"{CHECKPOINT_BASE}/{enc_full}/{tag}",
    ]


def _parse_best_r1_from_log(log_path: str) -> Optional[float]:
    """Extract the last 'New best R@1=X.XXXX' value from a train.log."""
    best = None
    pattern = re.compile(r"New best R@1=([\d.]+)")
    with open(log_path) as f:
        for line in f:
            m = pattern.search(line)
            if m:
                best = float(m.group(1))
    return best


def _parse_eval_metrics_from_log(log_path: str) -> List[Dict[str, float]]:
    """Parse all [eval@step] lines, return list of metric dicts."""
    results = []
    pattern = re.compile(r"\[eval@(\d+)\]\s*(\{.*\})")
    with open(log_path) as f:
        for line in f:
            m = pattern.search(line)
            if m:
                step = int(m.group(1))
                metrics_str = m.group(2).replace("'", '"')
                try:
                    metrics = json.loads(metrics_str)
                    metrics["step"] = step
                    results.append(metrics)
                except json.JSONDecodeError:
                    pass
    return results


def _parse_final_eval(log_path: str) -> Optional[Dict[str, float]]:
    """Parse [Final eval] line."""
    pattern = re.compile(r"\[Final eval\]\s*(\{.*\})")
    with open(log_path) as f:
        for line in f:
            m = pattern.search(line)
            if m:
                metrics_str = m.group(1).replace("'", '"')
                try:
                    return json.loads(metrics_str)
                except json.JSONDecodeError:
                    pass
    return None


def collect_metrics(dry_run: bool = False) -> Dict[Tuple[str, str, int], Dict]:
    """Collect best R@1 for all 18 runs. Returns {(encoder, strategy, seed): info}."""
    results = {}

    if dry_run:
        rng = np.random.RandomState(2026)
        base_values = {
            "random": 0.42,
            "embedding_distance": 0.48,
            "dataflow_aware": 0.51,
        }
        encoder_offsets = {"qwen": 0.03, "starcoder": 0.0}
        for encoder in ENCODERS:
            for strategy in STRATEGIES:
                for seed in SEEDS:
                    base = base_values[strategy] + encoder_offsets[encoder]
                    noise = rng.normal(0, 0.015)
                    r1 = round(float(np.clip(base + noise, 0, 1)), 4)
                    note = HETEROGENEITY_NOTES.get((encoder, strategy, seed), "")
                    results[(encoder, strategy, seed)] = {
                        "best_r1": r1,
                        "source": "mock",
                        "note": f"[DRY-RUN mock] {note}" if note else "[DRY-RUN mock]",
                        "all_evals": [],
                    }
        return results

    for encoder in ENCODERS:
        for strategy in STRATEGIES:
            for seed in SEEDS:
                key = (encoder, strategy, seed)
                note = HETEROGENEITY_NOTES.get(key, "")
                candidates = _candidate_dirs(encoder, strategy, seed)
                found = False

                for cdir in candidates:
                    log_path = os.path.join(cdir, "train.log")
                    best_ckpt = os.path.join(cdir, "best_by_recall_at_1")

                    if os.path.isfile(log_path):
                        best_r1 = _parse_best_r1_from_log(log_path)
                        all_evals = _parse_eval_metrics_from_log(log_path)
                        final = _parse_final_eval(log_path)

                        if best_r1 is None and all_evals:
                            best_r1 = max(e.get("recall@1", 0) for e in all_evals)
                        if best_r1 is None and final:
                            best_r1 = final.get("recall@1")

                        results[key] = {
                            "best_r1": best_r1,
                            "source": log_path,
                            "note": note,
                            "all_evals": all_evals,
                            "final_metrics": final,
                        }
                        found = True
                        break

                    elif os.path.isdir(best_ckpt):
                        results[key] = {
                            "best_r1": None,
                            "source": f"{best_ckpt} (dir exists, no log to parse metric)",
                            "note": f"WARN: checkpoint exists but no train.log found. {note}",
                            "all_evals": [],
                        }
                        found = True
                        break

                if not found:
                    results[key] = {
                        "best_r1": None,
                        "source": "NOT_FOUND",
                        "note": f"MISSING: searched {candidates}. {note}",
                        "all_evals": [],
                    }

    return results


# ── Statistical tests ──────────────────────────────────────────────────

def cohens_d(x: np.ndarray, y: np.ndarray) -> float:
    """Cohen's d for paired samples."""
    diff = x - y
    return float(diff.mean() / max(diff.std(ddof=1), 1e-12))


def bootstrap_ci(
    x: np.ndarray, y: np.ndarray, n_iter: int = 1000, alpha: float = 0.05, seed: int = 42
) -> Tuple[float, float, float]:
    """Bootstrap 95% CI for mean(x - y). Returns (mean_diff, ci_lo, ci_hi)."""
    rng = np.random.RandomState(seed)
    diff = x - y
    n = len(diff)
    boot_means = np.array([rng.choice(diff, size=n, replace=True).mean() for _ in range(n_iter)])
    lo = float(np.percentile(boot_means, 100 * alpha / 2))
    hi = float(np.percentile(boot_means, 100 * (1 - alpha / 2)))
    return float(diff.mean()), lo, hi


def run_comparisons(
    metrics: Dict[Tuple[str, str, int], Dict],
) -> Dict[str, Dict]:
    """Run all pairwise statistical tests.

    Comparisons (within each encoder, paired by seed):
      - embedding_distance vs random
      - dataflow_aware vs random
    """
    comparisons = {}

    for encoder in ENCODERS:
        for treat_strategy in ["embedding_distance", "dataflow_aware"]:
            label = f"{encoder}__{treat_strategy}_vs_random"

            treat_vals, ctrl_vals = [], []
            valid_seeds = []
            for seed in SEEDS:
                t_info = metrics.get((encoder, treat_strategy, seed))
                c_info = metrics.get((encoder, "random", seed))
                t_r1 = t_info["best_r1"] if t_info else None
                c_r1 = c_info["best_r1"] if c_info else None
                if t_r1 is not None and c_r1 is not None:
                    treat_vals.append(t_r1)
                    ctrl_vals.append(c_r1)
                    valid_seeds.append(seed)

            n_pairs = len(valid_seeds)
            if n_pairs < 2:
                comparisons[label] = {
                    "status": "INSUFFICIENT_DATA",
                    "n_pairs": n_pairs,
                    "valid_seeds": valid_seeds,
                }
                continue

            treat_arr = np.array(treat_vals)
            ctrl_arr = np.array(ctrl_vals)

            t_stat, t_pval = stats.ttest_rel(treat_arr, ctrl_arr)

            if n_pairs >= 3:
                try:
                    w_stat, w_pval = stats.wilcoxon(treat_arr, ctrl_arr)
                except ValueError:
                    w_stat, w_pval = float("nan"), float("nan")
            else:
                w_stat, w_pval = float("nan"), float("nan")

            d = cohens_d(treat_arr, ctrl_arr)
            mean_diff, ci_lo, ci_hi = bootstrap_ci(treat_arr, ctrl_arr)

            het_notes = []
            for seed in valid_seeds:
                for s in [treat_strategy, "random"]:
                    n = HETEROGENEITY_NOTES.get((encoder, s, seed))
                    if n:
                        het_notes.append(f"{encoder}/{s}/s{seed}: {n}")

            comparisons[label] = {
                "status": "OK",
                "encoder": encoder,
                "treatment": treat_strategy,
                "control": "random",
                "n_pairs": n_pairs,
                "valid_seeds": valid_seeds,
                "treatment_values": treat_vals,
                "control_values": ctrl_vals,
                "treatment_mean": float(treat_arr.mean()),
                "treatment_std": float(treat_arr.std(ddof=1)) if n_pairs > 1 else 0.0,
                "control_mean": float(ctrl_arr.mean()),
                "control_std": float(ctrl_arr.std(ddof=1)) if n_pairs > 1 else 0.0,
                "mean_diff": mean_diff,
                "paired_ttest": {"t_statistic": float(t_stat), "p_value": float(t_pval)},
                "wilcoxon": {"w_statistic": float(w_stat), "p_value": float(w_pval)},
                "bootstrap_95ci": {"lower": ci_lo, "upper": ci_hi},
                "cohens_d": d,
                "heterogeneity_notes": het_notes,
            }

    return comparisons


def per_condition_summary(
    metrics: Dict[Tuple[str, str, int], Dict],
) -> List[Dict]:
    """Mean ± std per (encoder, strategy) condition."""
    summary = []
    for encoder in ENCODERS:
        for strategy in STRATEGIES:
            vals = []
            missing = []
            for seed in SEEDS:
                info = metrics.get((encoder, strategy, seed))
                if info and info["best_r1"] is not None:
                    vals.append(info["best_r1"])
                else:
                    missing.append(seed)
            summary.append({
                "encoder": encoder,
                "strategy": strategy,
                "n": len(vals),
                "values": vals,
                "mean": float(np.mean(vals)) if vals else None,
                "std": float(np.std(vals, ddof=1)) if len(vals) > 1 else 0.0,
                "missing_seeds": missing,
            })
    return summary


# ── Output formatting ──────────────────────────────────────────────────

def _fmt(x, digits=4):
    if x is None:
        return "—"
    if isinstance(x, float) and math.isnan(x):
        return "—"
    return f"{x:.{digits}f}"


def format_markdown(summary: List[Dict], comparisons: Dict[str, Dict]) -> str:
    lines = []
    lines.append("# M2 Statistical Analysis Results\n")

    # Per-condition table
    lines.append("## Per-Condition Summary (Best R@1)\n")
    lines.append("| Encoder | Strategy | N | Mean | Std | Seeds |")
    lines.append("|---------|----------|---|------|-----|-------|")
    for s in summary:
        seeds_str = ", ".join(str(v) for v in s["values"]) if s["values"] else "—"
        missing = f" (missing: {s['missing_seeds']})" if s["missing_seeds"] else ""
        lines.append(
            f"| {s['encoder']} | {s['strategy']} | {s['n']} | "
            f"{_fmt(s['mean'])} | {_fmt(s['std'])} | {seeds_str}{missing} |"
        )
    lines.append("")

    # Comparison table
    lines.append("## Statistical Comparisons (paired by seed)\n")
    lines.append(
        "| Comparison | N | Δ Mean | 95% CI | t-test p | Wilcoxon p | Cohen's d |"
    )
    lines.append(
        "|------------|---|--------|--------|----------|------------|-----------|"
    )
    for label, c in comparisons.items():
        if c["status"] != "OK":
            lines.append(f"| {label} | {c['n_pairs']} | — | — | — | — | — |")
            continue
        ci = f"[{_fmt(c['bootstrap_95ci']['lower'])}, {_fmt(c['bootstrap_95ci']['upper'])}]"
        lines.append(
            f"| {c['encoder']}: {c['treatment']} vs {c['control']} | "
            f"{c['n_pairs']} | {_fmt(c['mean_diff'])} | {ci} | "
            f"{_fmt(c['paired_ttest']['p_value'])} | {_fmt(c['wilcoxon']['p_value'])} | "
            f"{_fmt(c['cohens_d'])} |"
        )
    lines.append("")

    # Heterogeneity notes
    all_notes = []
    for c in comparisons.values():
        if c.get("heterogeneity_notes"):
            all_notes.extend(c["heterogeneity_notes"])
    if all_notes:
        lines.append("## Heterogeneity Notes\n")
        for n in sorted(set(all_notes)):
            lines.append(f"- {n}")
        lines.append("")

    # Interpretation guide
    lines.append("## Interpretation Guide\n")
    lines.append("- p < 0.05: statistically significant at α=0.05")
    lines.append("- Cohen's d: |d| < 0.2 negligible, 0.2–0.5 small, 0.5–0.8 medium, > 0.8 large")
    lines.append("- Bootstrap CI: if interval excludes 0, difference is significant at 95% level")
    lines.append("- Wilcoxon: non-parametric alternative (more robust with N=3, less power)")
    lines.append("")

    return "\n".join(lines)


def format_json_results(
    summary: List[Dict], comparisons: Dict[str, Dict], raw: Dict
) -> Dict:
    raw_serializable = {}
    for (enc, strat, seed), info in raw.items():
        k = f"{enc}__{strat}__s{seed}"
        raw_serializable[k] = {
            "best_r1": info["best_r1"],
            "source": info["source"],
            "note": info["note"],
        }
    return {
        "per_condition": summary,
        "comparisons": comparisons,
        "raw_runs": raw_serializable,
    }


# ── Main ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="M2 statistical analysis")
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Use mock data to verify script logic",
    )
    parser.add_argument(
        "--output-dir", default="/root/structfuse/results",
        help="Directory to write result files",
    )
    parser.add_argument(
        "--bootstrap-iter", type=int, default=1000,
        help="Number of bootstrap iterations",
    )
    args = parser.parse_args()

    print(f"M2 Statistical Analysis {'[DRY-RUN]' if args.dry_run else ''}")
    print(f"Design: {len(ENCODERS)} encoders × {len(STRATEGIES)} strategies × {len(SEEDS)} seeds = {len(ENCODERS)*len(STRATEGIES)*len(SEEDS)} runs\n")

    # 1. Collect metrics
    print("=" * 60)
    print("Phase 1: Collecting metrics")
    print("=" * 60)
    metrics = collect_metrics(dry_run=args.dry_run)

    found = sum(1 for v in metrics.values() if v["best_r1"] is not None)
    missing = sum(1 for v in metrics.values() if v["best_r1"] is None)
    print(f"  Found: {found}/{len(metrics)} runs with R@1 values")
    if missing > 0:
        print(f"  Missing: {missing} runs")
        for (enc, strat, seed), info in sorted(metrics.items()):
            if info["best_r1"] is None:
                print(f"    - {enc}/{strat}/s{seed}: {info['note']}")

    print()
    for (enc, strat, seed), info in sorted(metrics.items()):
        r1_str = f"{info['best_r1']:.4f}" if info['best_r1'] is not None else "MISSING"
        flag = " *" if (enc, strat, seed) in HETEROGENEITY_NOTES else ""
        print(f"  {enc:12s} {strat:22s} s{seed}: R@1={r1_str}{flag}")

    # 2. Per-condition summary
    print()
    print("=" * 60)
    print("Phase 2: Per-condition summary")
    print("=" * 60)
    summary = per_condition_summary(metrics)
    for s in summary:
        if s["mean"] is not None:
            print(f"  {s['encoder']:12s} {s['strategy']:22s}: {s['mean']:.4f} ± {s['std']:.4f} (n={s['n']})")
        else:
            print(f"  {s['encoder']:12s} {s['strategy']:22s}: NO DATA")

    # 3. Statistical comparisons
    print()
    print("=" * 60)
    print("Phase 3: Statistical comparisons")
    print("=" * 60)
    comparisons = run_comparisons(metrics)

    for label, c in comparisons.items():
        print(f"\n  [{label}]")
        if c["status"] != "OK":
            print(f"    ⚠ {c['status']}: only {c['n_pairs']} valid pairs")
            continue
        print(f"    Treatment: {_fmt(c['treatment_mean'])} ± {_fmt(c['treatment_std'])}")
        print(f"    Control:   {_fmt(c['control_mean'])} ± {_fmt(c['control_std'])}")
        print(f"    Δ Mean:    {_fmt(c['mean_diff'])}")
        print(f"    Paired t:  t={_fmt(c['paired_ttest']['t_statistic'])}, p={_fmt(c['paired_ttest']['p_value'])}")
        print(f"    Wilcoxon:  W={_fmt(c['wilcoxon']['w_statistic'])}, p={_fmt(c['wilcoxon']['p_value'])}")
        ci = c["bootstrap_95ci"]
        print(f"    Boot 95CI: [{_fmt(ci['lower'])}, {_fmt(ci['upper'])}]")
        print(f"    Cohen's d: {_fmt(c['cohens_d'])}")
        if c.get("heterogeneity_notes"):
            for n in c["heterogeneity_notes"]:
                print(f"    Note: {n}")

    # 4. Save outputs
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    suffix = "_dryrun" if args.dry_run else ""

    json_path = out_dir / f"m2_stats{suffix}.json"
    json_data = format_json_results(summary, comparisons, metrics)
    with open(json_path, "w") as f:
        json.dump(json_data, f, indent=2)
    print(f"\nJSON saved: {json_path}")

    md_path = out_dir / f"m2_stats{suffix}.md"
    md_text = format_markdown(summary, comparisons)
    with open(md_path, "w") as f:
        f.write(md_text)
    print(f"Markdown saved: {md_path}")

    print("\nDone.")


if __name__ == "__main__":
    main()

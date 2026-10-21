#!/usr/bin/env python3
"""Analyze D157 shuffled-ISR results and compare with baselines."""

import argparse
import json
import sys
from pathlib import Path
from scipy.stats import fisher_exact
import numpy as np


# --- Baseline data from registry (Qwen3-4B, 500 steps) ---

BASELINES = {
    "ISR β=0.1": {
        "seeds": {
            "s47": {"PR": 0.97, "proved": 97, "TS": 83, "CE": 1, "PG": 10, "CI": 8, "genuine": 3},
            "s48": {"PR": 0.66, "proved": 66, "TS": 66, "CE": 0, "PG": 0, "CI": 0, "genuine": 0},
            "s49": {"PR": 0.86, "proved": 86, "TS": 73, "CE": 6, "PG": 6, "CI": 0, "genuine": 1},
            "s50": {"PR": 0.98, "proved": 98, "TS": 84, "CE": 0, "PG": 0, "CI": 0, "genuine": 6},
            "s51": {"PR": 0.98, "proved": 98, "TS": 96, "CE": 0, "PG": 1, "CI": 0, "genuine": 1},
        },
        "source": "d134-4b-isr-b01-s47..s51",
    },
    "Random β=0.1": {
        "seeds": {
            "s47": {"PR": 0.89, "proved": 89, "TS": 0, "CE": 79, "PG": 4, "CI": 0, "genuine": 6},
            "s48": {"PR": 0.93, "proved": 93, "TS": 3, "CE": 75, "PG": 14, "CI": 0, "genuine": 4},
            "s49": {"PR": 0.05, "proved": 5, "TS": 1, "CE": 4, "PG": 0, "CI": 0, "genuine": 0},
            "s50": {"PR": 0.45, "proved": 45, "TS": 4, "CE": 39, "PG": 0, "CI": 0, "genuine": 2},
            "s51": {"PR": 0.65, "proved": 65, "TS": 1, "CE": 36, "PG": 19, "CI": 0, "genuine": 9},
        },
        "source": "d134-4b-random-b01-s47..s51",
    },
    "Exec-only": {
        "seeds": {
            "s42": {"PR": 0.93, "proved": 93, "TS": 0, "CE": 81, "PG": 6, "CI": 0, "genuine": 7},
            "s45": {"PR": 0.99, "proved": 99, "TS": 93, "CE": 5, "PG": 1, "CI": 0, "genuine": 1},
            "s46": {"PR": 0.93, "proved": 93, "TS": 0, "CE": 83, "PG": 4, "CI": 0, "genuine": 9},
        },
        "source": "plan001-exec-only-s42-r2, sweep-exec-only-s45-r2, plan001-exec-only-s46",
    },
}

N_PROBLEMS = 100


def load_classify_result(path: str) -> dict:
    """Load classify_h7 JSON and extract the first (only) experiment entry."""
    with open(path) as f:
        data = json.load(f)
    if isinstance(data, dict) and len(data) == 1:
        return next(iter(data.values()))
    return data


def extract_metrics(classify_data: dict) -> dict:
    proved = classify_data["n_proved"]
    return {
        "PR": proved / classify_data.get("n_total", N_PROBLEMS),
        "proved": proved,
        "TS": classify_data.get("h7_strict_count", 0),
        "CE": classify_data.get("h1_strict_count", 0),
        "PG": classify_data.get("h8_conjunction_collapse_count", 0),
        "CI": classify_data.get("content_independent_count", 0),
        "genuine": classify_data.get("genuine_count", 0),
    }


def pct(count, total):
    return f"{count / total * 100:.1f}" if total > 0 else "—"


def compute_seed_stats(seeds: dict) -> dict:
    prs = [s["PR"] for s in seeds.values()]
    genuines = [s["genuine"] / s["proved"] * 100 if s["proved"] > 0 else 0 for s in seeds.values()]
    ts_pcts = [s["TS"] / s["proved"] * 100 if s["proved"] > 0 else 0 for s in seeds.values()]
    ce_pcts = [s["CE"] / s["proved"] * 100 if s["proved"] > 0 else 0 for s in seeds.values()]
    pg_pcts = [s["PG"] / s["proved"] * 100 if s["proved"] > 0 else 0 for s in seeds.values()]
    ci_pcts = [s["CI"] / s["proved"] * 100 if s["proved"] > 0 else 0 for s in seeds.values()]
    return {
        "PR": f"{np.mean(prs):.2f} ± {np.std(prs, ddof=1):.2f}" if len(prs) > 1 else f"{prs[0]:.2f}",
        "genuine%": f"{np.mean(genuines):.1f} ± {np.std(genuines, ddof=1):.1f}" if len(genuines) > 1 else f"{genuines[0]:.1f}",
        "TS%": f"{np.mean(ts_pcts):.1f} ± {np.std(ts_pcts, ddof=1):.1f}" if len(ts_pcts) > 1 else f"{ts_pcts[0]:.1f}",
        "CE%": f"{np.mean(ce_pcts):.1f} ± {np.std(ce_pcts, ddof=1):.1f}" if len(ce_pcts) > 1 else f"{ce_pcts[0]:.1f}",
        "PG%": f"{np.mean(pg_pcts):.1f} ± {np.std(pg_pcts, ddof=1):.1f}" if len(pg_pcts) > 1 else f"{pg_pcts[0]:.1f}",
        "CI%": f"{np.mean(ci_pcts):.1f} ± {np.std(ci_pcts, ddof=1):.1f}" if len(ci_pcts) > 1 else f"{ci_pcts[0]:.1f}",
        "genuine_counts": [s["genuine"] for s in seeds.values()],
        "proved_counts": [s["proved"] for s in seeds.values()],
    }


def fisher_test(g1_genuine, g1_proved, g2_genuine, g2_proved):
    """Fisher exact test on pooled genuine vs non-genuine counts."""
    g1_non = g1_proved - g1_genuine
    g2_non = g2_proved - g2_genuine
    table = [[g1_genuine, g1_non], [g2_genuine, g2_non]]
    odds, p = fisher_exact(table, alternative="two-sided")
    return odds, p


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", nargs="+", required=True,
                        help="classify_h7 JSON files for D157 seeds (in seed order: s42, s43, s44)")
    parser.add_argument("--seed_labels", nargs="+", default=["s42", "s43", "s44"])
    parser.add_argument("--output", default="artifacts/d157_shuffled_isr_analysis.md")
    args = parser.parse_args()

    if len(args.inputs) != len(args.seed_labels):
        print(f"ERROR: {len(args.inputs)} inputs but {len(args.seed_labels)} seed labels", file=sys.stderr)
        sys.exit(1)

    # Load D157 results
    d157_seeds = {}
    for path, label in zip(args.inputs, args.seed_labels):
        raw = load_classify_result(path)
        d157_seeds[label] = extract_metrics(raw)

    d157_stats = compute_seed_stats(d157_seeds)

    # Build report
    lines = []
    lines.append("# D157 Shuffled-ISR Analysis Report\n")
    lines.append(f"Generated from {len(args.inputs)} seeds: {', '.join(args.seed_labels)}\n")

    # Per-seed breakdown
    lines.append("## 1. Per-Seed Breakdown\n")
    lines.append("| Seed | PR | Proved | TS | CE | PG | CI | Genuine | Genuine% |")
    lines.append("|------|------|--------|-----|-----|-----|-----|---------|----------|")
    for label, m in d157_seeds.items():
        lines.append(f"| {label} | {m['PR']:.2f} | {m['proved']} | "
                     f"{m['TS']} ({pct(m['TS'], m['proved'])}%) | "
                     f"{m['CE']} ({pct(m['CE'], m['proved'])}%) | "
                     f"{m['PG']} ({pct(m['PG'], m['proved'])}%) | "
                     f"{m['CI']} ({pct(m['CI'], m['proved'])}%) | "
                     f"{m['genuine']} | {pct(m['genuine'], m['proved'])}% |")

    # Mean ± std
    lines.append("\n## 2. Aggregated (Mean ± Std)\n")
    lines.append("| Metric | Shuffled-ISR |")
    lines.append("|--------|-------------|")
    for key in ["PR", "genuine%", "TS%", "CE%", "PG%", "CI%"]:
        lines.append(f"| {key} | {d157_stats[key]} |")

    # Comparison table
    lines.append("\n## 3. Cross-Condition Comparison\n")
    lines.append("| Condition | Seeds | PR | Genuine% | TS% | CE% | PG% | CI% |")
    lines.append("|-----------|-------|------|----------|------|------|------|------|")

    all_conditions = {"Shuffled-ISR (D157)": d157_stats}
    for name, bl in BASELINES.items():
        bl_stats = compute_seed_stats(bl["seeds"])
        all_conditions[name] = bl_stats

    for name, stats in all_conditions.items():
        n = 3 if name.startswith("Shuffled") else len(BASELINES.get(name.replace(" (D157)", ""), {}).get("seeds", {"a":1,"b":2,"c":3}))
        lines.append(f"| {name} | {n} | {stats['PR']} | {stats['genuine%']} | "
                     f"{stats['TS%']} | {stats['CE%']} | {stats['PG%']} | {stats['CI%']} |")

    # Statistical tests
    lines.append("\n## 4. Statistical Tests\n")
    lines.append("### Fisher Exact Test (Shuffled-ISR vs ISR β=0.1): genuine proportion\n")

    d157_total_genuine = sum(d157_stats["genuine_counts"])
    d157_total_proved = sum(d157_stats["proved_counts"])

    for bl_name, bl_data in BASELINES.items():
        bl_stats = compute_seed_stats(bl_data["seeds"])
        bl_total_genuine = sum(bl_stats["genuine_counts"])
        bl_total_proved = sum(bl_stats["proved_counts"])

        odds, p = fisher_test(d157_total_genuine, d157_total_proved,
                              bl_total_genuine, bl_total_proved)
        sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"
        lines.append(f"**Shuffled-ISR vs {bl_name}**: "
                     f"pooled genuine {d157_total_genuine}/{d157_total_proved} vs "
                     f"{bl_total_genuine}/{bl_total_proved}, "
                     f"OR={odds:.3f}, p={p:.4f} {sig}\n")

    # Write report
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n")
    print(f"Report written to {output_path}")

    # Also print to stdout
    print("\n" + "\n".join(lines))


if __name__ == "__main__":
    main()

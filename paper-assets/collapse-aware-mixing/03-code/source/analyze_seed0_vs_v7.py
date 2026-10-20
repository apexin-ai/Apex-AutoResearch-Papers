#!/usr/bin/env python3
"""Compare seed0 (seed=0) vs v7 (seed=42) pilot pipeline metrics."""

import json
import os
import sys
from pathlib import Path

SEED0_DIR = Path("/root/autodl-tmp/output_seed0")
V7_DIR = Path("/root/autodl-tmp/output_v7")
OUTPUT_PATH = SEED0_DIR / "seed0_vs_v7_comparison.json"

GENERATIONS = ["G0", "G1", "G2"]
METRICS_KEYS = [
    "spectral_effective_rank",
    "perplexity",
    "spectral_entropy",
    "vocab_coverage",
    "unigram_entropy",
    "trigram_entropy",
    "unigram_unique",
]
DISPLAY_NAMES = {
    "spectral_effective_rank": "eff_rank",
    "perplexity": "ppl",
    "spectral_entropy": "spec_entropy",
    "vocab_coverage": "vocab_cov",
    "unigram_entropy": "uni_entropy",
    "trigram_entropy": "tri_entropy",
    "unigram_unique": "uni_unique",
}

V7_FALLBACK = {
    "G0": {"spectral_effective_rank": 676.96, "perplexity": 13.27, "spectral_entropy": 6.518,
            "vocab_coverage": 0.469, "unigram_entropy": 6.93, "trigram_entropy": 11.41, "unigram_unique": 23586},
    "G1": {"spectral_effective_rank": 678.30, "perplexity": 13.41, "spectral_entropy": 6.520,
            "vocab_coverage": 0.137, "unigram_entropy": 0.96, "trigram_entropy": 1.28, "unigram_unique": 6878},
    "G2": {"spectral_effective_rank": 683.44, "perplexity": 13.59, "spectral_entropy": 6.527,
            "vocab_coverage": 0.00002, "unigram_entropy": 0, "trigram_entropy": 0, "unigram_unique": 1},
}


def load_final_metrics(base_dir: Path, gen: str) -> dict | None:
    path = base_dir / gen / "metrics.jsonl"
    if not path.exists():
        return None
    lines = path.read_text().strip().split("\n")
    for line in reversed(lines):
        entry = json.loads(line)
        if "final_model" in entry.get("checkpoint", ""):
            return {k: entry[k] for k in METRICS_KEYS if k in entry}
    return json.loads(lines[-1])


def pct_diff(a: float, b: float) -> str:
    if b == 0:
        return "N/A" if a == 0 else "inf"
    return f"{(a - b) / abs(b) * 100:+.2f}%"


def main():
    v7_metrics = {}
    seed0_metrics = {}

    for gen in GENERATIONS:
        v7_m = load_final_metrics(V7_DIR, gen)
        if v7_m is None:
            v7_m = V7_FALLBACK[gen]
            print(f"[WARN] v7 {gen}: using fallback values (file not found)")
        v7_metrics[gen] = v7_m

        s0_m = load_final_metrics(SEED0_DIR, gen)
        seed0_metrics[gen] = s0_m

    available_gens = [g for g in GENERATIONS if seed0_metrics[g] is not None]
    missing_gens = [g for g in GENERATIONS if seed0_metrics[g] is None]

    if not available_gens:
        print("ERROR: No seed0 metrics found for any generation.")
        sys.exit(1)

    if missing_gens:
        print(f"[INFO] seed0 metrics not yet available for: {', '.join(missing_gens)}")
        print(f"[INFO] Comparing available generations: {', '.join(available_gens)}\n")

    # --- Markdown comparison table ---
    header = "| Metric | " + " | ".join(
        f"v7_{g} | s0_{g} | diff" for g in available_gens
    ) + " |"
    sep = "|" + "---|" * (1 + 3 * len(available_gens))

    print("## seed0 (seed=0) vs v7 (seed=42) Comparison")
    print()
    print(header)
    print(sep)

    for key in METRICS_KEYS:
        name = DISPLAY_NAMES.get(key, key)
        row = f"| {name} |"
        for gen in available_gens:
            v7_val = v7_metrics[gen].get(key, 0)
            s0_val = seed0_metrics[gen].get(key, 0)
            if isinstance(v7_val, float) and abs(v7_val) < 1:
                fmt = ".6f"
            elif isinstance(v7_val, float):
                fmt = ".2f"
            else:
                fmt = ""
            v7_str = f"{v7_val:{fmt}}" if fmt else str(v7_val)
            s0_str = f"{s0_val:{fmt}}" if fmt else str(s0_val)
            diff_str = pct_diff(s0_val, v7_val)
            row += f" {v7_str} | {s0_str} | {diff_str} |"
        print(row)

    # --- eff_rank trend analysis ---
    print()
    print("## eff_rank Trend Analysis")
    print()

    v7_ranks = [v7_metrics[g]["spectral_effective_rank"] for g in GENERATIONS]
    print(f"v7 eff_rank:  G0={v7_ranks[0]:.2f} -> G1={v7_ranks[1]:.2f} -> G2={v7_ranks[2]:.2f}  "
          f"(total {pct_diff(v7_ranks[2], v7_ranks[0])})")

    if len(available_gens) >= 2:
        s0_ranks = [seed0_metrics[g]["spectral_effective_rank"] for g in available_gens]
        trend_parts = [f"{g}={r:.2f}" for g, r in zip(available_gens, s0_ranks)]
        print(f"s0 eff_rank:  {' -> '.join(trend_parts)}", end="")
        if len(s0_ranks) >= 2:
            total_pct = pct_diff(s0_ranks[-1], s0_ranks[0])
            print(f"  (total {total_pct})")
        else:
            print()

    # --- Seed-robustness verdict ---
    print()
    if set(GENERATIONS).issubset(set(available_gens)):
        s0_ranks_full = [seed0_metrics[g]["spectral_effective_rank"] for g in GENERATIONS]
        rising = s0_ranks_full[0] < s0_ranks_full[1] < s0_ranks_full[2]
        any_rise = s0_ranks_full[2] > s0_ranks_full[0]

        if rising:
            print(">>> PATH_A_CONFIRMED: eff_rank monotonically rises G0->G1->G2 in seed0. "
                  "The v7 finding is seed-robust.")
        elif any_rise:
            print(">>> PATH_A_PARTIAL: eff_rank rises overall (G0->G2) but not monotonically. "
                  "Direction is consistent with v7.")
        else:
            print(">>> PATH_B: seed0 eff_rank does NOT rise G0->G2. "
                  "The v7 finding may be noise or seed-dependent.")
    else:
        print(f">>> PENDING: Need all 3 generations to judge. Currently have: {', '.join(available_gens)}")
        if len(available_gens) >= 2:
            s0_r = [seed0_metrics[g]["spectral_effective_rank"] for g in available_gens]
            direction = "rising" if s0_r[-1] > s0_r[0] else "falling/flat"
            print(f"    Early signal ({available_gens[0]}->{available_gens[-1]}): {direction} "
                  f"({s0_r[0]:.2f} -> {s0_r[-1]:.2f}, {pct_diff(s0_r[-1], s0_r[0])})")

    # --- Save JSON output ---
    output = {
        "experiment": "seed0_vs_v7_comparison",
        "seed0_seed": 0,
        "v7_seed": 42,
        "available_generations": available_gens,
        "missing_generations": missing_gens,
        "v7_metrics": {g: v7_metrics[g] for g in GENERATIONS},
        "seed0_metrics": {g: seed0_metrics[g] for g in available_gens},
        "eff_rank_trend": {
            "v7": {g: v7_metrics[g]["spectral_effective_rank"] for g in GENERATIONS},
            "seed0": {g: seed0_metrics[g]["spectral_effective_rank"] for g in available_gens},
        },
    }

    if set(GENERATIONS).issubset(set(available_gens)):
        s0_ranks_full = [seed0_metrics[g]["spectral_effective_rank"] for g in GENERATIONS]
        rising = s0_ranks_full[0] < s0_ranks_full[1] < s0_ranks_full[2]
        output["verdict"] = "PATH_A_CONFIRMED" if rising else (
            "PATH_A_PARTIAL" if s0_ranks_full[2] > s0_ranks_full[0] else "PATH_B"
        )
    else:
        output["verdict"] = "PENDING"

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

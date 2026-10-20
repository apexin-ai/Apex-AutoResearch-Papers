#!/usr/bin/env python3
"""
3-seed statistical analysis for GPT2-medium (355M) model collapse experiments.

Reads gen0-gen7 metrics from all_results.json or per-gen metrics.json
across 4 methods x 3 seeds. Outputs summary table and paired t-test results.

Input:  /root/autodl-tmp/div_cal_verify/results_medium_*/
Output: stdout tables (paper-ready) + artifacts/355m_3seed_ttest.csv
Deps:   numpy, scipy
"""

import json
import os
import sys
from pathlib import Path

import numpy as np

try:
    from scipy import stats
except ImportError:
    print("ERROR: scipy not installed. Run: pip install scipy")
    sys.exit(1)

BASE = "/root/autodl-tmp/div_cal_verify"
OUT_DIR = Path("/root/div_cal_verify/artifacts")

METHODS = ["uncurated", "rgds", "external_only", "random_50"]
SEEDS = [42, 123, 456]
NUM_GENS = 8  # gen0-gen7

# Directory mapping: seed -> method -> (result_dir, method_subdir)
def get_result_dir(seed, method):
    dir_suffix = {
        "uncurated": "uncurated",
        "rgds": "rgds",
        "external_only": "external",
        "random_50": "random50",
    }[method]
    subdir = method  # actual subdirectory name matches method key
    if method == "external_only":
        subdir = "external_only"

    if seed == 42:
        return f"{BASE}/results_medium_{dir_suffix}/{subdir}"
    else:
        return f"{BASE}/results_medium_{dir_suffix}_seed{seed}/{subdir}"

FIELD_MAP = {
    "ppl":    "held_out_perplexity",
    "rare":   "rare_ngram_survival",
    "rankme": "rankme",
    "knn":    "knn_probe_accuracy",
    "corr":   "rank_correlation",
    "ratio":  "selection_rare_ngram_ratio",
}

COMPARISONS = [
    ("rgds_vs_uncurated",  "rgds",          "uncurated",     "C1: RGDS accelerates collapse"),
    ("ext_vs_uncurated",   "external_only", "uncurated",     "C2: external mitigates collapse"),
    ("rgds_vs_random50",   "rgds",          "random_50",     "C3: RGDS worse than random same-budget"),
    ("ext_vs_random50",    "external_only", "random_50",     "C2: external vs random same-budget"),
]


def load_all_results(path):
    """Load from all_results.json (seed=42 format)."""
    fp = os.path.join(path, "all_results.json")
    if not os.path.exists(fp):
        return None
    with open(fp) as f:
        text = f.read().replace("NaN", "null")
        data = json.loads(text)
    rows = []
    for g in data["generations"]:
        row = {"gen": g["generation"]}
        for short, full in FIELD_MAP.items():
            v = g.get(full)
            row[short] = v
        rows.append(row)
    return rows


def load_per_gen_metrics(path):
    """Load from per-gen metrics.json files (seed=123/456 in-progress format)."""
    rows = []
    for gen_i in range(NUM_GENS):
        fp = os.path.join(path, f"gen_{gen_i}", "metrics.json")
        if not os.path.exists(fp):
            break
        with open(fp) as f:
            text = f.read().replace("NaN", "null")
            g = json.loads(text)
        row = {"gen": g["generation"]}
        for short, full in FIELD_MAP.items():
            row[short] = g.get(full)
        rows.append(row)
    return rows if rows else None


def load_method_seed(seed, method):
    """Try all_results.json first, then per-gen metrics.json."""
    path = get_result_dir(seed, method)
    data = load_all_results(path)
    if data is not None:
        return data, "all_results.json"
    data = load_per_gen_metrics(path)
    if data is not None:
        return data, "per-gen metrics"
    return None, None


def cohens_d(x, y):
    diff = np.array(x, dtype=float) - np.array(y, dtype=float)
    sd = np.std(diff, ddof=1)
    if sd == 0:
        return float("inf") if np.mean(diff) != 0 else 0.0
    return float(np.mean(diff) / sd)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    # ── Phase 1: Load all data ──
    print("=" * 60)
    print("GPT2-medium (355M) 3-seed Analysis")
    print("=" * 60)

    # method -> seed -> list of gen dicts
    data = {}
    method_availability = {}

    for method in METHODS:
        data[method] = {}
        method_availability[method] = []
        for seed in SEEDS:
            rows, source = load_method_seed(seed, method)
            if rows is None:
                print(f"  SKIP  {method:15s} seed={seed}: not found")
                continue
            max_gen = max(r["gen"] for r in rows)
            print(f"  OK    {method:15s} seed={seed}: {len(rows)} gens (0-{max_gen}) [{source}]")
            data[method][seed] = rows
            method_availability[method].append(seed)

    # ── Phase 2: Gen7 summary table ──
    print(f"\n{'=' * 60}")
    print("Gen7 Summary: mean +/- std (across seeds)")
    print(f"{'=' * 60}")
    header_metrics = ["ppl", "rankme", "rare"]
    print(f"{'Method':15s} {'Seeds':6s}  " + "  ".join(f"{m:>20s}" for m in header_metrics))
    print("-" * 80)

    method_seed_gen7 = {}

    for method in METHODS:
        vals = {m: [] for m in header_metrics}
        for seed in method_availability[method]:
            gens = data[method][seed]
            gen7 = [r for r in gens if r["gen"] == 7]
            if not gen7:
                continue
            g7 = gen7[0]
            method_seed_gen7[(method, seed)] = g7
            for m in header_metrics:
                if g7[m] is not None:
                    vals[m].append(g7[m])

        n = len(method_availability[method])
        n_g7 = len(vals["ppl"])
        parts = []
        for m in header_metrics:
            v = vals[m]
            if len(v) >= 2:
                parts.append(f"{np.mean(v):8.2f} +/- {np.std(v, ddof=1):6.2f}")
            elif len(v) == 1:
                parts.append(f"{v[0]:8.4f}       -     ")
            else:
                parts.append(f"{'N/A':>20s}")

        status = f"{n_g7}/{n}s"
        print(f"{method:15s} {status:6s}  " + "  ".join(parts))

    # ── Phase 3: Per-gen trajectory (all available seeds) ──
    print(f"\n{'=' * 60}")
    print("PPL Trajectory (per gen, all seeds)")
    print(f"{'=' * 60}")
    print(f"{'Method':15s} " + " ".join(f"{'gen'+str(i):>8s}" for i in range(NUM_GENS)))
    print("-" * 85)
    for method in METHODS:
        row_parts = []
        for gen_i in range(NUM_GENS):
            ppls = []
            for seed in method_availability[method]:
                gens = data[method][seed]
                g = [r for r in gens if r["gen"] == gen_i]
                if g and g[0]["ppl"] is not None:
                    ppls.append(g[0]["ppl"])
            if len(ppls) >= 2:
                row_parts.append(f"{np.mean(ppls):6.1f}({len(ppls)})")
            elif len(ppls) == 1:
                row_parts.append(f"{ppls[0]:6.1f}(1)")
            else:
                row_parts.append(f"{'--':>8s}")
        print(f"{method:15s} " + " ".join(row_parts))

    # ── Phase 4: Paired t-tests ──
    print(f"\n{'=' * 60}")
    print("Paired t-tests (gen7, across seeds)")
    print(f"{'=' * 60}")
    test_metrics = ["ppl", "rankme", "rare"]
    ttest_rows = []

    for comp_name, method_a, method_b, hypothesis in COMPARISONS:
        seeds_a = set(method_availability.get(method_a, []))
        seeds_b = set(method_availability.get(method_b, []))
        common_seeds = sorted(seeds_a & seeds_b)

        # filter to seeds that have gen7
        common_seeds = [s for s in common_seeds
                        if (method_a, s) in method_seed_gen7
                        and (method_b, s) in method_seed_gen7]

        print(f"\n  {comp_name} -- {hypothesis}")
        if len(common_seeds) < 2:
            print(f"    Only {len(common_seeds)} common seeds with gen7 -- skipped")
            continue

        if len(common_seeds) < 3:
            print(f"    WARNING: only {len(common_seeds)} seeds (need 3 for valid t-test)")
            print(f"    Showing descriptive stats only:")
            for m in test_metrics:
                va = [method_seed_gen7[(method_a, s)][m] for s in common_seeds
                      if method_seed_gen7[(method_a, s)][m] is not None]
                vb = [method_seed_gen7[(method_b, s)][m] for s in common_seeds
                      if method_seed_gen7[(method_b, s)][m] is not None]
                if va and vb:
                    diff = np.mean(va) - np.mean(vb)
                    print(f"    {m:8s}: {method_a}={np.mean(va):.2f}, "
                          f"{method_b}={np.mean(vb):.2f}, diff={diff:+.2f}")
                    ttest_rows.append({
                        "comparison": comp_name, "metric": m,
                        "t_stat": "N/A", "p_value": "N/A", "cohens_d": "N/A",
                        "mean_a": f"{np.mean(va):.4f}", "mean_b": f"{np.mean(vb):.4f}",
                        "mean_diff": f"{diff:.4f}", "n_seeds": len(common_seeds),
                        "sig": "PARTIAL",
                    })
            continue

        for m in test_metrics:
            va = [method_seed_gen7[(method_a, s)][m] for s in common_seeds]
            vb = [method_seed_gen7[(method_b, s)][m] for s in common_seeds]
            if any(v is None for v in va + vb):
                print(f"    {m:8s}: missing values, skipped")
                continue
            t_stat, p_val = stats.ttest_rel(va, vb)
            d = cohens_d(va, vb)
            mean_diff = np.mean(va) - np.mean(vb)
            sig = "***" if p_val < 0.001 else "**" if p_val < 0.01 else "*" if p_val < 0.05 else "ns"
            direction = f"{method_a}>{method_b}" if mean_diff > 0 else f"{method_a}<{method_b}"

            print(f"    {m:8s}: t={t_stat:+.3f}, p={p_val:.4f} {sig}, "
                  f"d={d:+.2f}, diff={mean_diff:+.4f} ({direction})")

            ttest_rows.append({
                "comparison": comp_name, "metric": m,
                "t_stat": f"{t_stat:.4f}", "p_value": f"{p_val:.6f}",
                "cohens_d": f"{d:.4f}",
                "mean_a": f"{np.mean(va):.4f}", "mean_b": f"{np.mean(vb):.4f}",
                "mean_diff": f"{mean_diff:.4f}", "n_seeds": len(common_seeds),
                "sig": sig,
            })

    # ── Phase 5: Claim verification ──
    print(f"\n{'=' * 60}")
    print("Claim Verification Status")
    print(f"{'=' * 60}")

    # C1: ratio degradation across seeds (RGDS has selection_rare_ngram_ratio)
    print("\n  C1: Diversity ratio degrades across generations")
    for method in ["rgds"]:
        for seed in method_availability.get(method, []):
            gens = data[method][seed]
            ratios = [(r["gen"], r["ratio"]) for r in gens if r["ratio"] is not None]
            if ratios:
                print(f"    {method} seed={seed}: " +
                      ", ".join(f"g{g}={v:.3f}" for g, v in ratios))
            else:
                print(f"    {method} seed={seed}: no ratio data")

    # C3: RGDS > random_50 ppl (worse) across seeds
    print("\n  C3: RGDS worse than Random-50 at same budget")
    for seed in sorted(set(method_availability.get("rgds", [])) &
                       set(method_availability.get("random_50", []))):
        g7_rgds = method_seed_gen7.get(("rgds", seed))
        g7_rand = method_seed_gen7.get(("random_50", seed))
        if g7_rgds and g7_rand and g7_rgds["ppl"] is not None and g7_rand["ppl"] is not None:
            diff = g7_rgds["ppl"] - g7_rand["ppl"]
            print(f"    seed={seed}: rgds_ppl={g7_rgds['ppl']:.2f}, "
                  f"random50_ppl={g7_rand['ppl']:.2f}, diff={diff:+.2f} "
                  f"({'RGDS worse' if diff > 0 else 'RGDS better'})")

    # ── Phase 6: Write CSV ──
    if ttest_rows:
        import csv
        csv_path = OUT_DIR / "355m_3seed_ttest.csv"
        fields = ["comparison", "metric", "t_stat", "p_value", "cohens_d",
                   "mean_a", "mean_b", "mean_diff", "n_seeds", "sig"]
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            for row in ttest_rows:
                writer.writerow(row)
        print(f"\nCSV written: {csv_path} ({len(ttest_rows)} rows)")

    # ── Summary ──
    total_available = sum(len(v) for v in method_availability.values())
    total_possible = len(METHODS) * len(SEEDS)
    print(f"\nData coverage: {total_available}/{total_possible} method-seed combos loaded")
    missing = [(m, s) for m in METHODS for s in SEEDS if s not in method_availability[m]]
    if missing:
        print(f"Missing: {', '.join(f'{m}/s{s}' for m, s in missing)}")


if __name__ == "__main__":
    main()

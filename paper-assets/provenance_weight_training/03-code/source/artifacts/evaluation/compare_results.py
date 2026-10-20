"""Compare evaluation results across methods and seeds for MVP pass/fail.

Scans eval directory for runs named {method}_seed{S} and grid_b{X}_seed{S}.
For grid-b, selects the best b per seed (lowest perplexity), then aggregates
across seeds with mean +/- std.

MVP pass (D004): adaptive mean ppl improvement >= 90% of best-grid mean ppl improvement
over uniform baseline, across 3 seeds.
"""

import argparse
import json
import math
import os
import re
import sys
from collections import defaultdict


SEEDS = [42, 123, 456]
GRID_B_VALUES = [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]


def parse_args():
    p = argparse.ArgumentParser(description="Multi-seed MVP comparison with grid-b selection.")
    p.add_argument("--eval_base_dir", type=str, required=True,
                   help="Base directory containing per-run eval subdirs")
    p.add_argument("--output_path", type=str, required=True,
                   help="Path to write mvp_summary.json")
    p.add_argument("--pass_threshold", type=float, default=0.90,
                   help="Fraction of grid improvement that adaptive must reach")
    return p.parse_args()


def load_eval(eval_dir):
    path = os.path.join(eval_dir, "eval_results.json")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


def get_ppl(results):
    if results is None:
        return None
    return results.get("perplexity", {}).get("perplexity")


def get_metric(results, path):
    obj = results
    for key in path.split("."):
        if isinstance(obj, dict) and key in obj:
            obj = obj[key]
        else:
            return None
    return obj if isinstance(obj, (int, float)) else None


def mean_std(vals):
    vals = [v for v in vals if v is not None]
    if not vals:
        return None, None
    m = sum(vals) / len(vals)
    if len(vals) > 1:
        s = math.sqrt(sum((v - m) ** 2 for v in vals) / (len(vals) - 1))
    else:
        s = 0.0
    return m, s


def fmt(m, s):
    if m is None:
        return "N/A"
    return f"{m:.2f} +/- {s:.2f}"


def main():
    args = parse_args()
    base = args.eval_base_dir

    # Collect all results per seed
    per_seed = {}
    for seed in SEEDS:
        seed_data = {}

        # Uniform
        res = load_eval(os.path.join(base, f"uniform_seed{seed}"))
        seed_data["uniform"] = {"results": res, "ppl": get_ppl(res)}

        # Grid-b: load all b values, pick best
        grid_runs = {}
        for b in GRID_B_VALUES:
            b_tag = str(b).replace(".", "p")
            run_name = f"grid_b{b_tag}_seed{seed}"
            res = load_eval(os.path.join(base, run_name))
            ppl = get_ppl(res)
            grid_runs[b] = {"results": res, "ppl": ppl}

        # Select best grid-b (lowest ppl)
        valid_grid = {b: d for b, d in grid_runs.items() if d["ppl"] is not None}
        if valid_grid:
            best_b = min(valid_grid, key=lambda b: valid_grid[b]["ppl"])
            seed_data["grid_best"] = {
                "results": valid_grid[best_b]["results"],
                "ppl": valid_grid[best_b]["ppl"],
                "best_b": best_b,
            }
        else:
            seed_data["grid_best"] = {"results": None, "ppl": None, "best_b": None}
        seed_data["grid_all"] = grid_runs

        # Adaptive
        res = load_eval(os.path.join(base, f"adaptive_seed{seed}"))
        seed_data["adaptive"] = {"results": res, "ppl": get_ppl(res)}

        per_seed[seed] = seed_data

    # Aggregate across seeds
    methods = ["uniform", "grid_best", "adaptive"]
    metric_paths = [
        ("Perplexity", "perplexity.perplexity", "lower"),
        ("Loss", "perplexity.loss", "lower"),
        ("HellaSwag", "lm_eval.hellaswag.acc_norm,none", "higher"),
        ("MMLU", "lm_eval.mmlu.acc,none", "higher"),
        ("Self-BLEU", "generation.self_bleu", "lower"),
        ("Distinct-1", "generation.distinct_1", "higher"),
        ("Distinct-2", "generation.distinct_2", "higher"),
    ]

    agg = {}
    for method in methods:
        agg[method] = {}
        for label, path, _ in metric_paths:
            vals = []
            for seed in SEEDS:
                res = per_seed[seed][method].get("results")
                if res:
                    vals.append(get_metric(res, path))
            m, s = mean_std(vals)
            agg[method][label] = {"mean": m, "std": s, "values": vals}

    # Print table
    print()
    print("=" * 75)
    print("  Multi-Seed Results (mean +/- std, n=3)")
    print("=" * 75)
    print()

    # Show best b per seed
    for seed in SEEDS:
        gb = per_seed[seed]["grid_best"]
        print(f"  Seed {seed}: best grid b = {gb['best_b']}  (ppl = {gb['ppl']:.2f})" if gb["ppl"] else f"  Seed {seed}: no grid data")
    print()

    col_w = 18
    header = f"{'Metric':<16}" + "".join(f"{m:>{col_w}}" for m in ["uniform", "grid (best b)", "adaptive"])
    print(header)
    print("-" * (16 + col_w * 3))

    for label, _, _ in metric_paths:
        row = f"{label:<16}"
        for method in methods:
            d = agg[method].get(label, {})
            m, s = d.get("mean"), d.get("std")
            row += f"{fmt(m, s):>{col_w}}"
        print(row)

    # Grid-b detail table
    print()
    print("  Grid-b detail (perplexity per b value per seed):")
    print(f"  {'b':>6}", end="")
    for seed in SEEDS:
        print(f"  seed{seed:>5}", end="")
    print(f"  {'mean':>10}")
    print("  " + "-" * 40)
    for b in GRID_B_VALUES:
        ppls = []
        row = f"  {b:>6.1f}"
        for seed in SEEDS:
            ppl = per_seed[seed]["grid_all"][b]["ppl"]
            ppls.append(ppl)
            row += f"  {ppl:>9.2f}" if ppl else f"  {'N/A':>9}"
        m, _ = mean_std(ppls)
        row += f"  {m:>9.2f}" if m else f"  {'N/A':>9}"
        print(row)

    # MVP pass condition
    print()
    print("=" * 75)
    print("  MVP Pass Condition (D004)")
    print("=" * 75)

    u_ppls = [per_seed[s]["uniform"]["ppl"] for s in SEEDS]
    g_ppls = [per_seed[s]["grid_best"]["ppl"] for s in SEEDS]
    a_ppls = [per_seed[s]["adaptive"]["ppl"] for s in SEEDS]

    u_m, u_s = mean_std(u_ppls)
    g_m, g_s = mean_std(g_ppls)
    a_m, a_s = mean_std(a_ppls)

    pass_result = {}

    if any(v is None for v in [u_m, g_m, a_m]):
        print("  Cannot evaluate: missing perplexity data")
        pass_result = {"error": "missing data"}
    else:
        grid_imp = u_m - g_m
        adaptive_imp = u_m - a_m

        print(f"  Uniform PPL:         {u_m:.4f} +/- {u_s:.4f}")
        print(f"  Grid-best PPL:       {g_m:.4f} +/- {g_s:.4f}")
        print(f"  Adaptive PPL:        {a_m:.4f} +/- {a_s:.4f}")
        print()

        if grid_imp <= 0:
            print(f"  FAIL Level 2: grid did not improve over uniform")
            pass_result = {"level": "FAIL_L2", "grid_imp": grid_imp}
        else:
            ratio = adaptive_imp / grid_imp
            passed = ratio >= args.pass_threshold

            print(f"  Grid improvement:    {grid_imp:.4f}  (uniform - grid_best)")
            print(f"  Adaptive improvement:{adaptive_imp:.4f}  (uniform - adaptive)")
            print(f"  Ratio:               {ratio:.4f}  (threshold: {args.pass_threshold:.2f})")
            print(f"  Result:              {'PASS' if passed else 'FAIL'}")

            # Per-seed breakdown
            print()
            print("  Per-seed:")
            for i, seed in enumerate(SEEDS):
                u, g, a = u_ppls[i], g_ppls[i], a_ppls[i]
                if u and g and a and (u - g) > 0:
                    r = (u - a) / (u - g)
                    print(f"    seed {seed}: uniform={u:.2f} grid={g:.2f} adaptive={a:.2f} ratio={r:.4f}")

            pass_result = {
                "uniform_ppl": u_m, "uniform_std": u_s,
                "grid_ppl": g_m, "grid_std": g_s,
                "adaptive_ppl": a_m, "adaptive_std": a_s,
                "grid_improvement": grid_imp,
                "adaptive_improvement": adaptive_imp,
                "ratio": ratio, "threshold": args.pass_threshold,
                "passed": passed,
                "best_b_per_seed": {str(s): per_seed[s]["grid_best"]["best_b"] for s in SEEDS},
            }

    # Save summary
    summary = {
        "seeds": SEEDS,
        "grid_b_values": GRID_B_VALUES,
        "per_seed_ppl": {
            str(s): {
                "uniform": per_seed[s]["uniform"]["ppl"],
                "grid_best_b": per_seed[s]["grid_best"]["best_b"],
                "grid_best_ppl": per_seed[s]["grid_best"]["ppl"],
                "adaptive": per_seed[s]["adaptive"]["ppl"],
                "grid_all": {str(b): per_seed[s]["grid_all"][b]["ppl"] for b in GRID_B_VALUES},
            }
            for s in SEEDS
        },
        "aggregated": {
            method: {
                label: {"mean": agg[method][label]["mean"], "std": agg[method][label]["std"]}
                for label, _, _ in metric_paths
            }
            for method in methods
        },
        "mvp_pass": pass_result,
    }

    os.makedirs(os.path.dirname(args.output_path) or ".", exist_ok=True)
    with open(args.output_path, "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\n  Summary saved to {args.output_path}")

    if isinstance(pass_result, dict) and pass_result.get("passed") is False:
        sys.exit(1)


if __name__ == "__main__":
    main()

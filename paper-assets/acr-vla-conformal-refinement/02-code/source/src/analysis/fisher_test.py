"""Statistical analysis for LIBERO eval: Fisher exact test + Bootstrap CI.

Reads eval JSON files (from evaluate.py) or accepts manual success counts.
Computes pairwise Fisher exact tests and bootstrap confidence intervals
for success-rate differences.

File naming convention (from evaluate.py):
  eval_{benchmark}_{mode}{norm_tag}_seed{seed}.json

Usage:
  # From JSON files
  python src/analysis/fisher_test.py \
    --results_dir logs/ --benchmark object \
    --methods crm_obs_only_norm0.1 reconvla \
    --seeds 42 43 --n_bootstrap 1000

  # All pairwise comparisons
  python src/analysis/fisher_test.py \
    --results_dir logs/ --benchmark object --seeds 42 --all_pairs

  # Manual mode
  python src/analysis/fisher_test.py --manual \
    --method_a obs_only --successes_a 19 --trials_a 100 \
    --method_b argmin --successes_b 12 --trials_b 100
"""

import argparse
import json
import re
import sys
from itertools import combinations
from pathlib import Path

import numpy as np
from scipy.stats import fisher_exact


# ── Helpers ──────────────────────────────────────────────────────────────────

def load_eval_json(path):
    """Load an eval JSON and return (successes, total) summed across tasks."""
    with open(path) as f:
        data = json.load(f)
    total_succ = 0
    total_trials = 0
    for task_info in data["per_task"].values():
        total_succ += task_info["successes"]
        total_trials += task_info["total"]
    return total_succ, total_trials, data


def find_eval_files(results_dir, benchmark, method, seeds):
    """Find eval JSON files matching the given method and seeds.

    method can be e.g. 'crm_obs_only_norm0.1', 'reconvla', 'vla_only_mean'.
    Filename pattern: eval_{benchmark}_{mode}{norm_tag}_seed{seed}.json
    """
    results_dir = Path(results_dir)
    files = []
    for seed in seeds:
        pattern = f"eval_{benchmark}_{method}_seed{seed}.json"
        matches = list(results_dir.glob(pattern))
        if matches:
            files.extend(matches)
        else:
            # Try broader search
            broader = list(results_dir.glob(f"eval_{benchmark}_*{method}*_seed{seed}.json"))
            files.extend(broader)
    return sorted(files)


def pool_results(results_dir, benchmark, method, seeds):
    """Pool success/trial counts across seeds for one method."""
    files = find_eval_files(results_dir, benchmark, method, seeds)
    if not files:
        return None, None, []
    total_succ = 0
    total_trials = 0
    per_task_all = {}
    for f in files:
        succ, trials, data = load_eval_json(f)
        total_succ += succ
        total_trials += trials
        seed_match = re.search(r"seed(\d+)", f.name)
        seed_label = seed_match.group(1) if seed_match else "?"
        for task_name, info in data["per_task"].items():
            key = f"{task_name}_seed{seed_label}"
            per_task_all[key] = info
    return total_succ, total_trials, files


def discover_methods(results_dir, benchmark, seeds):
    """Discover all available methods from eval JSON filenames."""
    results_dir = Path(results_dir)
    methods = set()
    for seed in seeds:
        pattern = f"eval_{benchmark}_*_seed{seed}.json"
        for f in results_dir.glob(pattern):
            # Extract method from: eval_{benchmark}_{method}_seed{seed}.json
            name = f.stem  # e.g. eval_object_crm_obs_only_norm0.1_seed42
            prefix = f"eval_{benchmark}_"
            suffix = f"_seed{seed}"
            if name.startswith(prefix) and name.endswith(suffix):
                method = name[len(prefix):-len(suffix)]
                methods.add(method)
    return sorted(methods)


# ── Statistical Tests ────────────────────────────────────────────────────────

def fisher_test_2x2(succ_a, trials_a, succ_b, trials_b):
    """Two-sided Fisher exact test on 2×2 contingency table.

    Table:
              success  failure
    method_a  succ_a   fail_a
    method_b  succ_b   fail_b
    """
    fail_a = trials_a - succ_a
    fail_b = trials_b - succ_b
    table = [[succ_a, fail_a], [succ_b, fail_b]]
    # Two-sided: tests whether the odds ratio != 1
    odds_ratio, p_value = fisher_exact(table, alternative="two-sided")
    return odds_ratio, p_value, table


def bootstrap_sr_diff(succ_a, trials_a, succ_b, trials_b,
                       n_bootstrap=1000, ci=0.95, seed=12345):
    """Bootstrap CI for the difference in success rates (SR_a - SR_b).

    Resamples binary outcomes (1=success, 0=failure) with replacement.
    """
    rng = np.random.RandomState(seed)
    outcomes_a = np.array([1] * succ_a + [0] * (trials_a - succ_a))
    outcomes_b = np.array([1] * succ_b + [0] * (trials_b - succ_b))

    diffs = np.empty(n_bootstrap)
    for i in range(n_bootstrap):
        sample_a = rng.choice(outcomes_a, size=trials_a, replace=True)
        sample_b = rng.choice(outcomes_b, size=trials_b, replace=True)
        diffs[i] = sample_a.mean() - sample_b.mean()

    alpha = 1 - ci
    lo = np.percentile(diffs, 100 * alpha / 2)
    hi = np.percentile(diffs, 100 * (1 - alpha / 2))
    return diffs.mean(), lo, hi, diffs


def compute_effect_size(succ_a, trials_a, succ_b, trials_b):
    """Absolute and relative effect size."""
    sr_a = succ_a / trials_a
    sr_b = succ_b / trials_b
    abs_diff = sr_a - sr_b
    rel_diff = abs_diff / sr_b if sr_b > 0 else float("inf")
    return sr_a, sr_b, abs_diff, rel_diff


# ── Output ───────────────────────────────────────────────────────────────────

def print_comparison(name_a, succ_a, trials_a, name_b, succ_b, trials_b,
                     n_bootstrap=1000):
    sr_a, sr_b, abs_diff, rel_diff = compute_effect_size(
        succ_a, trials_a, succ_b, trials_b)
    odds_ratio, p_value, table = fisher_test_2x2(
        succ_a, trials_a, succ_b, trials_b)
    mean_diff, ci_lo, ci_hi, _ = bootstrap_sr_diff(
        succ_a, trials_a, succ_b, trials_b, n_bootstrap=n_bootstrap)

    sig = ""
    if p_value < 0.001:
        sig = "***"
    elif p_value < 0.01:
        sig = "**"
    elif p_value < 0.05:
        sig = "*"
    else:
        sig = "n.s."

    print(f"\n{'='*65}")
    print(f"  {name_a}  vs  {name_b}")
    print(f"{'='*65}")
    print(f"  {name_a:30s}  SR = {sr_a:.1%}  ({succ_a}/{trials_a})")
    print(f"  {name_b:30s}  SR = {sr_b:.1%}  ({succ_b}/{trials_b})")
    print(f"{'─'*65}")
    print(f"  Absolute diff (A − B):       {abs_diff:+.1%}")
    print(f"  Relative diff:               {rel_diff:+.1%}")
    print(f"  Fisher exact p-value:        {p_value:.4f}  {sig}")
    print(f"  Odds ratio:                  {odds_ratio:.3f}")
    print(f"  Bootstrap 95% CI (A − B):    [{ci_lo:+.1%}, {ci_hi:+.1%}]")
    print(f"  Bootstrap mean diff:         {mean_diff:+.1%}")
    print(f"{'='*65}")

    return {
        "method_a": name_a, "method_b": name_b,
        "sr_a": sr_a, "sr_b": sr_b,
        "succ_a": succ_a, "trials_a": trials_a,
        "succ_b": succ_b, "trials_b": trials_b,
        "abs_diff": abs_diff, "rel_diff": rel_diff,
        "fisher_p": p_value, "odds_ratio": odds_ratio,
        "ci_lo": ci_lo, "ci_hi": ci_hi,
        "significance": sig,
    }


def print_summary_table(results_list):
    """Print a compact summary table of all pairwise comparisons."""
    if not results_list:
        return
    print(f"\n{'='*90}")
    print("  SUMMARY TABLE")
    print(f"{'='*90}")
    header = (f"  {'Method A':20s} {'Method B':20s} "
              f"{'SR_A':>6s} {'SR_B':>6s} {'Diff':>7s} "
              f"{'p-val':>7s} {'Sig':>4s} {'95% CI':>18s}")
    print(header)
    print(f"  {'─'*86}")
    for r in results_list:
        ci_str = f"[{r['ci_lo']:+.1%}, {r['ci_hi']:+.1%}]"
        print(f"  {r['method_a']:20s} {r['method_b']:20s} "
              f"{r['sr_a']:5.1%} {r['sr_b']:6.1%} {r['abs_diff']:+6.1%} "
              f"{r['fisher_p']:7.4f} {r['significance']:>4s} {ci_str:>18s}")
    print(f"{'='*90}")


# ── CLI ──────────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser(
        description="Fisher exact test + Bootstrap CI for LIBERO eval results")

    # File-based mode
    p.add_argument("--results_dir", type=str, default="logs/",
                   help="Directory containing eval JSON files")
    p.add_argument("--benchmark", type=str, default="object",
                   choices=["object", "spatial", "goal", "long"])
    p.add_argument("--methods", nargs="+", default=None,
                   help="Method names to compare (from filename)")
    p.add_argument("--seeds", nargs="+", type=int, default=[42],
                   help="Seeds to pool")
    p.add_argument("--all_pairs", action="store_true",
                   help="Run all pairwise comparisons among discovered methods")

    # Manual mode
    p.add_argument("--manual", action="store_true",
                   help="Manual input mode (no JSON files needed)")
    p.add_argument("--method_a", type=str, default="method_a")
    p.add_argument("--successes_a", type=int, default=0)
    p.add_argument("--trials_a", type=int, default=100)
    p.add_argument("--method_b", type=str, default="method_b")
    p.add_argument("--successes_b", type=int, default=0)
    p.add_argument("--trials_b", type=int, default=100)

    p.add_argument("--n_bootstrap", type=int, default=1000)

    return p.parse_args()


def run_manual(args):
    print_comparison(
        args.method_a, args.successes_a, args.trials_a,
        args.method_b, args.successes_b, args.trials_b,
        n_bootstrap=args.n_bootstrap)


def run_from_files(args):
    results_dir = Path(args.results_dir)
    if not results_dir.exists():
        print(f"ERROR: results_dir {results_dir} does not exist", file=sys.stderr)
        sys.exit(1)

    if args.all_pairs:
        methods = discover_methods(results_dir, args.benchmark, args.seeds)
        if not methods:
            print("No eval files found.", file=sys.stderr)
            sys.exit(1)
        print(f"Discovered methods: {methods}")
        pairs = list(combinations(methods, 2))
    elif args.methods and len(args.methods) >= 2:
        methods = args.methods
        pairs = list(combinations(methods, 2))
    else:
        print("Provide --methods (>=2) or --all_pairs", file=sys.stderr)
        sys.exit(1)

    all_results = []
    for m_a, m_b in pairs:
        succ_a, trials_a, files_a = pool_results(
            results_dir, args.benchmark, m_a, args.seeds)
        succ_b, trials_b, files_b = pool_results(
            results_dir, args.benchmark, m_b, args.seeds)

        if succ_a is None:
            print(f"WARNING: no files found for {m_a}, skipping", file=sys.stderr)
            continue
        if succ_b is None:
            print(f"WARNING: no files found for {m_b}, skipping", file=sys.stderr)
            continue

        seeds_str = "+".join(str(s) for s in args.seeds)
        label_a = f"{m_a} (seed={seeds_str})"
        label_b = f"{m_b} (seed={seeds_str})"

        r = print_comparison(label_a, succ_a, trials_a,
                             label_b, succ_b, trials_b,
                             n_bootstrap=args.n_bootstrap)
        all_results.append(r)

    print_summary_table(all_results)


def main():
    args = parse_args()
    if args.manual:
        run_manual(args)
    else:
        run_from_files(args)


if __name__ == "__main__":
    main()

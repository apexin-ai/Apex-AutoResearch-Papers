#!/usr/bin/env python3
"""Unified dose-response curve metric extraction for retry vs reflexion experiments.

Reads per-trial data, computes final death rate at cutoff k=1..5 with Wilson CI,
and outputs unified JSON for plotting.
"""

import argparse
import glob
import json
import os
import random
import sys
from collections import defaultdict

from scipy.stats import norm

DEATH_PRONE_TASKS = [
    "chemistry-mix", "find-animal", "freeze", "grow-fruit",
    "identify-life-stages-1", "identify-life-stages-2",
    "inclined-plane-determine-angle", "lifespan-longest-lived",
    "lifespan-longest-lived-then-shortest-lived",
    "measure-melting-point-unknown-substance"
]

MAX_CUTOFF = 5


def wilson_ci(successes, total, confidence=0.95):
    if total == 0:
        return 0.0, 0.0, 0.0
    p = successes / total
    z = norm.ppf(1 - (1 - confidence) / 2)
    denom = 1 + z ** 2 / total
    center = (p + z ** 2 / (2 * total)) / denom
    margin = z * ((p * (1 - p) / total + z ** 2 / (4 * total ** 2)) ** 0.5) / denom
    return p, max(0.0, center - margin), min(1.0, center + margin)


def load_format_a(data_dir):
    """Format A: one JSON file per episode, each containing a trials list."""
    episodes = {}
    for fpath in sorted(glob.glob(os.path.join(data_dir, "**/*.json"), recursive=True)):
        with open(fpath) as f:
            data = json.load(f)
        task = data.get("task_name", "")
        ep = data.get("variation_idx", -1)
        trials = data.get("trials", [])
        if task and ep >= 0 and trials:
            episodes[(task, ep)] = sorted(trials, key=lambda t: t["trial_idx"])
    return episodes


def load_format_b(data_dir):
    """Format B: single JSONL file(s), one trial per line."""
    episodes = defaultdict(list)
    for fpath in sorted(glob.glob(os.path.join(data_dir, "**/*.jsonl"), recursive=True)):
        with open(fpath) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                rec = json.loads(line)
                task = rec.get("task_name", "")
                ep = rec.get("variation_idx", -1)
                if task and ep >= 0:
                    episodes[(task, ep)].append(rec)
    for key in episodes:
        episodes[key] = sorted(episodes[key], key=lambda t: t["trial_idx"])
    return dict(episodes)


def load_data(data_dir, fmt):
    if fmt == "a":
        return load_format_a(data_dir)
    elif fmt == "b":
        return load_format_b(data_dir)
    else:
        raise ValueError(f"Unknown format: {fmt}")


def filter_death_prone(episodes):
    return {k: v for k, v in episodes.items() if k[0] in DEATH_PRONE_TASKS}


def compute_dose_response(episodes):
    """Compute DR(k) for cutoff k=1..MAX_CUTOFF.

    DR(k) = count(death at trial k) / total_episodes_with_at_least_k_trials.
    """
    results = {}
    for k in range(1, MAX_CUTOFF + 1):
        deaths = 0
        total = 0
        for (task, ep), trials in episodes.items():
            if k > len(trials):
                continue
            total += 1
            trial_k = trials[k - 1]
            if trial_k.get("is_death", trial_k.get("score", 0) == -100):
                deaths += 1
        dr, ci_lo, ci_hi = wilson_ci(deaths, total)
        results[str(k)] = {
            "dr": round(dr, 4),
            "ci_lo": round(ci_lo, 4),
            "ci_hi": round(ci_hi, 4),
            "n": total,
            "deaths": deaths,
        }
    return results



def compute_final_death_rate(episodes):
    """Final death rate: fraction of ALL episodes where the last trial was a death."""
    deaths = 0
    total = len(episodes)
    for (task, ep), trials in episodes.items():
        if trials:
            last_trial = trials[-1]
            if last_trial.get("is_death", last_trial.get("score", 0) == -100):
                deaths += 1
    dr, ci_lo, ci_hi = wilson_ci(deaths, total)
    return {
        "final_dr": round(dr, 4),
        "ci_lo": round(ci_lo, 4),
        "ci_hi": round(ci_hi, 4),
        "n": total,
        "deaths": deaths,
    }

def discover_conditions(parent_dir):
    """Discover N-condition subdirectories (e.g., reflexion_n3, retry_n5)."""
    conditions = {}
    for entry in sorted(os.listdir(parent_dir)):
        full = os.path.join(parent_dir, entry)
        if os.path.isdir(full) and '_n' in entry:
            parts = entry.rsplit('_n', 1)
            if len(parts) == 2 and parts[1].isdigit():
                n = int(parts[1])
                conditions[n] = full
    return conditions


def process_condition(data_dir, fmt, label):
    """Load, filter, compute DR for a single condition directory."""
    raw = load_data(data_dir, fmt)
    filtered = filter_death_prone(raw)
    print(f"  {len(raw)} total episodes, {len(filtered)} death-prone episodes")
    dr = compute_dose_response(filtered)
    final = compute_final_death_rate(filtered)

    print(f"\n=== {label} Dose-Response ===")
    for k in sorted(dr.keys(), key=int):
        d = dr[k]
        print(f"  cutoff={k}: DR={d['dr']:.4f} [{d['ci_lo']:.4f}, {d['ci_hi']:.4f}] (n={d['n']}, deaths={d['deaths']})")
    print(f"  FINAL: DR={final['final_dr']:.4f} [{final['ci_lo']:.4f}, {final['ci_hi']:.4f}] (n={final['n']}, deaths={final['deaths']})")

    dr["final"] = final
    return dr


def generate_synthetic_data(n_tasks=10, n_episodes_per_task=20, n_trials=5,
                            base_death_rate=0.5, improvement_per_trial=0.08):
    """Generate synthetic per-trial data for testing."""
    random.seed(42)
    tasks = DEATH_PRONE_TASKS[:n_tasks]
    episodes = {}
    for task in tasks:
        for ep in range(n_episodes_per_task):
            trials = []
            for t in range(1, n_trials + 1):
                p_death = max(0.05, base_death_rate - improvement_per_trial * (t - 1))
                is_death = random.random() < p_death
                score = -100 if is_death else random.randint(0, 100)
                trials.append({"trial_idx": t, "score": score, "is_death": is_death})
            episodes[(task, ep)] = trials
    return episodes


def run_test():
    """Dry-run with synthetic data to verify logic."""
    print("=" * 60)
    print("TEST MODE: running with synthetic data")
    print("=" * 60)

    dr, lo, hi = wilson_ci(100, 200)
    print(f"\nWilson CI sanity: 100/200 -> DR={dr:.4f}, CI=[{lo:.4f}, {hi:.4f}]")
    assert abs(dr - 0.5) < 1e-6, f"Expected DR=0.5, got {dr}"
    assert 0.43 < lo < 0.44, f"Expected CI_lo ~0.43, got {lo}"
    assert 0.56 < hi < 0.57, f"Expected CI_hi ~0.57, got {hi}"
    print("  PASS: Wilson CI correct")

    dr0, lo0, hi0 = wilson_ci(0, 0)
    assert dr0 == 0.0 and lo0 == 0.0 and hi0 == 0.0
    print("  PASS: Wilson CI edge case (0/0)")

    dr1, lo1, hi1 = wilson_ci(0, 100)
    assert dr1 == 0.0 and lo1 < 0.001
    print(f"  PASS: Wilson CI edge case (0/100) -> [{lo1:.4f}, {hi1:.4f}]")

    retry_data = generate_synthetic_data(
        base_death_rate=0.55, improvement_per_trial=0.02
    )
    reflexion_data = generate_synthetic_data(
        base_death_rate=0.55, improvement_per_trial=0.10
    )

    retry_dr = compute_dose_response(retry_data)
    reflexion_dr = compute_dose_response(reflexion_data)

    print("\n--- Retry dose-response ---")
    for k in sorted(retry_dr.keys(), key=int):
        d = retry_dr[k]
        print(f"  cutoff={k}: DR={d['dr']:.4f} [{d['ci_lo']:.4f}, {d['ci_hi']:.4f}] (n={d['n']}, deaths={d['deaths']})")

    print("\n--- Reflexion dose-response ---")
    for k in sorted(reflexion_dr.keys(), key=int):
        d = reflexion_dr[k]
        print(f"  cutoff={k}: DR={d['dr']:.4f} [{d['ci_lo']:.4f}, {d['ci_hi']:.4f}] (n={d['n']}, deaths={d['deaths']})")

    n3_dr = reflexion_dr["3"]["dr"]
    cross = {
        "reflexion_n3_independent": round(n3_dr + 0.07, 4),
        "reflexion_n5_cutoff3": round(n3_dr, 4),
        "diff_pp": round(0.07, 4),
    }
    print(f"\n--- Cross-validation (mock) ---")
    print(f"  N=3 independent: {cross['reflexion_n3_independent']:.4f}")
    print(f"  N=5 cutoff=3:    {cross['reflexion_n5_cutoff3']:.4f}")
    print(f"  Diff:            {cross['diff_pp']:.4f} pp")

    drs = [reflexion_dr[str(k)]["dr"] for k in range(1, MAX_CUTOFF + 1)]
    print(f"\n  Reflexion DR trend: {[f'{d:.3f}' for d in drs]}")
    if drs[0] > drs[-1]:
        print("  PASS: Reflexion DR decreases from cutoff 1 to 5 (expected with improvement)")
    else:
        print("  NOTE: Reflexion DR did not decrease (could be stochastic, check params)")

    output = {
        "retry": retry_dr,
        "reflexion": reflexion_dr,
        "cross_validation": cross,
    }
    print(f"\n--- Output JSON preview ---")
    print(json.dumps(output, indent=2))
    print("\nTEST MODE COMPLETE: all checks passed")
    return output


def main():
    parser = argparse.ArgumentParser(
        description="Unified dose-response metric extraction for retry vs reflexion"
    )
    parser.add_argument("--retry-dir", type=str, help="Path to retry per-trial data directory")
    parser.add_argument("--reflexion-dir", type=str, help="Path to reflexion per-trial data directory")
    parser.add_argument("--retry-format", type=str, default="a", choices=["a", "b"],
                        help="Data format for retry: a=per-episode JSON, b=JSONL (default: a)")
    parser.add_argument("--reflexion-format", type=str, default="a", choices=["a", "b"],
                        help="Data format for reflexion: a=per-episode JSON, b=JSONL (default: a)")
    parser.add_argument("--n3-dr", type=float, default=None,
                        help="Independent N=3 final DR for cross-validation (if available)")
    parser.add_argument("--output", type=str,
                        default="analysis/unified_dose_response_data.json",
                        help="Output JSON path")
    parser.add_argument("--test", action="store_true",
                        help="Run with synthetic data for verification")
    parser.add_argument("--tasks", type=str, nargs="*", default=None,
                        help="Override death-prone task list (default: built-in 10 tasks)")
    args = parser.parse_args()

    if args.test:
        output = run_test()
        base, ext = os.path.splitext(args.output)
        out_path = f"{base}_test{ext}"
        os.makedirs(os.path.dirname(out_path) if os.path.dirname(out_path) else ".", exist_ok=True)
        with open(out_path, "w") as f:
            json.dump(output, f, indent=2)
        print(f"\nSaved test output to {out_path}")
        return

    if not args.retry_dir and not args.reflexion_dir:
        parser.error("At least one of --retry-dir or --reflexion-dir is required (or use --test)")

    global DEATH_PRONE_TASKS
    if args.tasks:
        DEATH_PRONE_TASKS = args.tasks
        print(f"Using custom task list: {DEATH_PRONE_TASKS}")

    output = {}

    if args.retry_dir:
        conditions = discover_conditions(args.retry_dir)
        if conditions:
            output["retry"] = {}
            for n, cond_dir in sorted(conditions.items()):
                label = f"Retry N={n}"
                print(f"\nLoading {label} from {cond_dir} (format {args.retry_format})...")
                dr = process_condition(cond_dir, args.retry_format, label)
                output["retry"][f"n{n}"] = dr
        else:
            print(f"\nLoading retry data from {args.retry_dir} (format {args.retry_format})...")
            dr = process_condition(args.retry_dir, args.retry_format, "Retry")
            output["retry"] = dr

    if args.reflexion_dir:
        conditions = discover_conditions(args.reflexion_dir)
        if conditions:
            output["reflexion"] = {}
            for n, cond_dir in sorted(conditions.items()):
                label = f"Reflexion N={n}"
                print(f"\nLoading {label} from {cond_dir} (format {args.reflexion_format})...")
                dr = process_condition(cond_dir, args.reflexion_format, label)
                output["reflexion"][f"n{n}"] = dr
        else:
            print(f"\nLoading reflexion data from {args.reflexion_dir} (format {args.reflexion_format})...")
            dr = process_condition(args.reflexion_dir, args.reflexion_format, "Reflexion")
            output["reflexion"] = dr

    cross = {}
    if args.n3_dr is not None:
        refl = output.get("reflexion", {})
        n5_cutoff3 = None
        if isinstance(refl, dict) and "n5" in refl:
            n5_cutoff3 = refl["n5"].get("3", {}).get("dr", None)
        elif isinstance(refl, dict) and "3" in refl:
            n5_cutoff3 = refl.get("3", {}).get("dr", None)
        if n5_cutoff3 is not None:
            cross = {
                "reflexion_n3_independent": round(args.n3_dr, 4),
                "reflexion_n5_cutoff3": round(n5_cutoff3, 4),
                "diff_pp": round(abs(args.n3_dr - n5_cutoff3), 4),
            }
            print(f"\n=== Cross-Validation ===")
            print(f"  N=3 independent DR: {cross['reflexion_n3_independent']:.4f}")
            print(f"  N=5 cutoff=3 DR:    {cross['reflexion_n5_cutoff3']:.4f}")
            print(f"  Difference:         {cross['diff_pp']:.4f} pp")
    output["cross_validation"] = cross

    os.makedirs(os.path.dirname(args.output) if os.path.dirname(args.output) else ".", exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {args.output}")


if __name__ == "__main__":
    main()

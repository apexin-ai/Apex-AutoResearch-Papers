#!/usr/bin/env python3
"""Wilson score CI + Fisher exact test for solver-trace-ablation classification data."""

import json
import csv
import math
from scipy import stats
from collections import defaultdict

def wilson_ci(k, n, alpha=0.05):
    """Wilson score interval for binomial proportion."""
    if n == 0 or k is None:
        return (None, None, None)
    p_hat = k / n
    z = stats.norm.ppf(1 - alpha / 2)
    denom = 1 + z**2 / n
    center = (p_hat + z**2 / (2 * n)) / denom
    margin = z * math.sqrt(p_hat * (1 - p_hat) / n + z**2 / (4 * n**2)) / denom
    return (p_hat, max(0, center - margin), min(1, center + margin))


def pick_canonical(experiments):
    """For each (condition, seed), pick the latest retry."""
    by_key = defaultdict(list)
    for exp in experiments:
        key = (exp["condition"], exp["seed"])
        by_key[key].append(exp)

    canonical = []
    for key, exps in by_key.items():
        def retry_order(e):
            eid = e["experiment_id"]
            if "-r" in eid:
                try:
                    return int(eid.split("-r")[-1])
                except ValueError:
                    return 0
            return 0
        exps.sort(key=retry_order)
        canonical.append(exps[-1])
    return canonical


def main():
    with open("/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/registry_extract.json") as f:
        all_experiments = json.load(f)

    canonical = pick_canonical(all_experiments)
    canonical.sort(key=lambda e: (e["condition"], e["seed"]))

    # --- Per-experiment Wilson CIs ---
    csv_rows = []
    per_exp_results = []

    for exp in canonical:
        n = exp["n_proved"]
        if n is None or n == 0:
            continue

        row = {
            "experiment_id": exp["experiment_id"],
            "condition": exp["condition"],
            "seed": exp["seed"],
            "n_proved": n,
        }

        for cat in ["h7", "h1", "genuine"]:
            k = exp.get(f"{cat}_count")
            rate, ci_lo, ci_hi = wilson_ci(k, n)
            row[f"{cat}_count"] = k
            row[f"{cat}_rate"] = rate
            row[f"{cat}_ci_lo"] = ci_lo
            row[f"{cat}_ci_hi"] = ci_hi

        csv_rows.append(row)
        per_exp_results.append(row)

    # --- Pooled analysis for multi-seed conditions ---
    CONDITIONS_TO_POOL = [
        "exec-only", "ISR β=0.1", "Random β=0.1",
        "ISR β=0.3", "Random β=0.3", "SFT",
    ]

    pooled_results = {}
    for cond in CONDITIONS_TO_POOL:
        cond_exps = [e for e in per_exp_results if e["condition"] == cond]
        if not cond_exps:
            continue

        pool = {"condition": cond, "n_seeds": len(cond_exps), "seeds": [e["seed"] for e in cond_exps]}
        total_n = sum(e["n_proved"] for e in cond_exps)
        pool["n_proved_total"] = total_n

        for cat in ["h7", "h1", "genuine"]:
            counts = [e[f"{cat}_count"] for e in cond_exps if e[f"{cat}_count"] is not None]
            if not counts:
                pool[f"{cat}_pooled_count"] = None
                pool[f"{cat}_pooled_rate"] = None
                pool[f"{cat}_pooled_ci_lo"] = None
                pool[f"{cat}_pooled_ci_hi"] = None
                continue
            n_with_data = sum(e["n_proved"] for e in cond_exps if e[f"{cat}_count"] is not None)
            total_k = sum(counts)
            rate, ci_lo, ci_hi = wilson_ci(total_k, n_with_data)
            pool[f"{cat}_pooled_count"] = total_k
            pool[f"{cat}_pooled_n"] = n_with_data
            pool[f"{cat}_pooled_rate"] = rate
            pool[f"{cat}_pooled_ci_lo"] = ci_lo
            pool[f"{cat}_pooled_ci_hi"] = ci_hi

        pooled_results[cond] = pool

    # --- Fisher exact tests ---
    fisher_tests = []

    comparisons = [
        ("ISR β=0.1", "Random β=0.1", "genuine"),
        ("ISR β=0.1", "Random β=0.1", "h7"),
        ("ISR β=0.3", "Random β=0.3", "genuine"),
        ("ISR β=0.3", "Random β=0.3", "h7"),
        ("ISR β=0.1", "Random β=0.1", "h1"),
        ("ISR β=0.3", "Random β=0.3", "h1"),
        ("ISR β=0.1", "exec-only", "genuine"),
        ("ISR β=0.3", "exec-only", "genuine"),
        ("Random β=0.1", "exec-only", "genuine"),
        ("Random β=0.3", "exec-only", "genuine"),
    ]

    for cond_a, cond_b, cat in comparisons:
        pa = pooled_results.get(cond_a)
        pb = pooled_results.get(cond_b)
        if not pa or not pb:
            continue
        ka = pa.get(f"{cat}_pooled_count")
        na = pa.get(f"{cat}_pooled_n")
        kb = pb.get(f"{cat}_pooled_count")
        nb = pb.get(f"{cat}_pooled_n")
        if ka is None or kb is None or na is None or nb is None:
            continue

        table = [[ka, na - ka], [kb, nb - kb]]
        odds_ratio, p_value = stats.fisher_exact(table)
        fisher_tests.append({
            "comparison": f"{cond_a} vs {cond_b}",
            "category": cat,
            "a_count": ka, "a_n": na, "a_rate": ka / na if na > 0 else None,
            "b_count": kb, "b_n": nb, "b_rate": kb / nb if nb > 0 else None,
            "odds_ratio": odds_ratio,
            "p_value": p_value,
            "significant_005": bool(p_value < 0.05),
            "significant_001": bool(p_value < 0.01),
        })

    # --- Write CSV ---
    csv_path = "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci_results.csv"
    fieldnames = [
        "condition", "seed", "experiment_id", "n_proved",
        "h7_count", "h7_rate", "h7_ci_lo", "h7_ci_hi",
        "h1_count", "h1_rate", "h1_ci_lo", "h1_ci_hi",
        "genuine_count", "genuine_rate", "genuine_ci_lo", "genuine_ci_hi",
    ]
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in csv_rows:
            writer.writerow(row)

    # --- Write JSON ---
    json_path = "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci_results.json"
    output = {
        "per_experiment": per_exp_results,
        "pooled": pooled_results,
        "fisher_tests": fisher_tests,
    }
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    # --- Print summary ---
    print("=" * 80)
    print("WILSON SCORE 95% CI — PER EXPERIMENT")
    print("=" * 80)
    for r in per_exp_results:
        print(f"\n{r['experiment_id']} ({r['condition']}, {r['seed']}, n={r['n_proved']})")
        for cat in ["h7", "h1", "genuine"]:
            k = r[f"{cat}_count"]
            rate = r[f"{cat}_rate"]
            lo = r[f"{cat}_ci_lo"]
            hi = r[f"{cat}_ci_hi"]
            if rate is not None:
                print(f"  {cat:>7}: {k:3d}/{r['n_proved']:3d} = {rate:.3f}  [{lo:.3f}, {hi:.3f}]")
            else:
                print(f"  {cat:>7}: N/A")

    print("\n" + "=" * 80)
    print("POOLED WILSON SCORE 95% CI")
    print("=" * 80)
    for cond in CONDITIONS_TO_POOL:
        p = pooled_results.get(cond)
        if not p:
            continue
        print(f"\n{cond} (seeds={p['seeds']}, total_n={p['n_proved_total']})")
        for cat in ["h7", "h1", "genuine"]:
            k = p.get(f"{cat}_pooled_count")
            n = p.get(f"{cat}_pooled_n")
            rate = p.get(f"{cat}_pooled_rate")
            lo = p.get(f"{cat}_pooled_ci_lo")
            hi = p.get(f"{cat}_pooled_ci_hi")
            if rate is not None:
                print(f"  {cat:>7}: {k:3d}/{n:3d} = {rate:.3f}  [{lo:.3f}, {hi:.3f}]")
            else:
                print(f"  {cat:>7}: N/A (missing data for some seeds)")

    print("\n" + "=" * 80)
    print("FISHER EXACT TESTS")
    print("=" * 80)
    for t in fisher_tests:
        sig = "***" if t["significant_001"] else ("*" if t["significant_005"] else "ns")
        print(f"\n{t['comparison']} — {t['category']}")
        print(f"  A: {t['a_count']}/{t['a_n']} = {t['a_rate']:.3f}")
        print(f"  B: {t['b_count']}/{t['b_n']} = {t['b_rate']:.3f}")
        print(f"  OR = {t['odds_ratio']:.3f}, p = {t['p_value']:.4f} {sig}")


if __name__ == "__main__":
    main()

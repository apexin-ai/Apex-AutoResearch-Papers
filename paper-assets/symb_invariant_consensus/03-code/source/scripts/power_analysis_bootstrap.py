#!/usr/bin/env python3
"""Power analysis (MDE) and Bootstrap CIs for all SICA vs SC conditions."""

import json
import os
import numpy as np
from scipy import stats

RESULTS_DIR = "/root/symb_invariant_consensus/results"
OUTPUT_DIR = "/root/symb_invariant_consensus/analysis"

EXPERIMENTS = [
    {"exp_id": "exp-001", "model": "Qwen2.5-14B", "domain": "FOLIO+PW",
     "file": "sica_expanded_14b.json"},
    {"exp_id": "exp-017", "model": "Qwen2.5-14B", "domain": "StrategyQA",
     "file": "exp017_strategyqa/exp017_results.json"},
    {"exp_id": "exp-018", "model": "Qwen2.5-14B", "domain": "ARC-Chall",
     "file": "exp018_arc/exp018_results.json"},
    {"exp_id": "exp-012", "model": "Qwen2.5-14B", "domain": "GSM8K",
     "file": "exp012_gsm8k/exp012_gsm8k_results.json"},
    {"exp_id": "exp-010", "model": "Mistral-7B", "domain": "FOLIO+PW",
     "file": "exp010_mistral/exp010_results.json"},
    {"exp_id": "exp-011", "model": "LLaMA-3.1-8B", "domain": "FOLIO+PW",
     "file": "exp011_llama8b/exp011_results.json"},
    {"exp_id": "exp-019", "model": "LLaMA-3.1-8B", "domain": "StrategyQA",
     "file": "exp019_strategyqa_200/exp019_results.json"},
    {"exp_id": "exp-020", "model": "LLaMA-3.1-8B", "domain": "FOLIO",
     "file": "exp020_folio_200/exp020_results.json"},
    {"exp_id": "exp-014", "model": "DeepSeek-R1-7B", "domain": "FOLIO+PW",
     "file": "exp014_deepseek_r1_7b/exp014_results.json"},
    {"exp_id": "exp-004", "model": "Qwen2.5-7B", "domain": "FOLIO+PW",
     "file": "exp004_qwen7b/exp004_qwen7b_results.json"},
]


def load_experiment(exp):
    path = os.path.join(RESULTS_DIR, exp["file"])
    with open(path) as f:
        data = json.load(f)
    results = data["results"]
    n = len(results)
    sica_arr = [r["sica_correct"] for r in results]
    sc_arr = [r["sc_correct"] for r in results]
    sica_c = sum(sica_arr)
    sc_c = sum(sc_arr)
    sica_wins = sum(1 for s, c in zip(sica_arr, sc_arr) if s and not c)
    sc_wins = sum(1 for s, c in zip(sica_arr, sc_arr) if c and not s)
    return {
        "n": n,
        "sica_correct_count": sica_c,
        "sc_correct_count": sc_c,
        "sica_wins": sica_wins,
        "sc_wins": sc_wins,
        "discordant_pairs": sica_wins + sc_wins,
        "delta_pp": (sica_c - sc_c) / n * 100,
        "sica_arr": sica_arr,
        "sc_arr": sc_arr,
    }


def mcnemar_mde_exact(n, n_d, alpha=0.05, target_power=0.80):
    """
    MDE for McNemar test via exact binomial power calculation.

    Under H0 the n_d discordant pairs split 50/50.
    Under H1, sica-wins fraction = p_b, sc-wins = 1 - p_b.
    Find minimum p_b (> 0.5) s.t. two-sided McNemar power >= target_power,
    then convert to accuracy-gap MDE = n_d * (2*p_b - 1) / n.
    """
    if n_d == 0:
        return float("inf"), None

    chi2_crit = stats.chi2.ppf(1 - alpha, df=1)

    reject_set = []
    for b in range(n_d + 1):
        c = n_d - b
        stat = (b - c) ** 2 / n_d
        if stat > chi2_crit:
            reject_set.append(b)

    if not reject_set:
        return float("inf"), None

    lo, hi = 0.5, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        power = sum(stats.binom.pmf(b, n_d, mid) for b in reject_set)
        if power >= target_power:
            hi = mid
        else:
            lo = mid

    p_b = hi
    mde_pp = abs(n_d * (2 * p_b - 1) / n) * 100

    actual_power = sum(stats.binom.pmf(b, n_d, p_b) for b in reject_set)
    return mde_pp, actual_power


def mcnemar_observed_power(n_d, sica_wins, sc_wins, alpha=0.05):
    """Post-hoc power at the observed effect size."""
    if n_d == 0:
        return 0.0
    chi2_crit = stats.chi2.ppf(1 - alpha, df=1)
    reject_set = []
    for b in range(n_d + 1):
        c = n_d - b
        stat = (b - c) ** 2 / n_d
        if stat > chi2_crit:
            reject_set.append(b)
    if not reject_set:
        return 0.0
    p_b_obs = sica_wins / n_d if n_d > 0 else 0.5
    if p_b_obs == 0.5:
        return alpha
    power = sum(stats.binom.pmf(b, n_d, p_b_obs) for b in reject_set)
    return power


def bootstrap_ci(sica_arr, sc_arr, n_boot=10000, alpha=0.05, seed=42):
    rng = np.random.RandomState(seed)
    sica = np.array(sica_arr, dtype=float)
    sc = np.array(sc_arr, dtype=float)
    n = len(sica)
    point_est = (sica.mean() - sc.mean()) * 100
    deltas = np.empty(n_boot)
    for i in range(n_boot):
        idx = rng.randint(0, n, size=n)
        deltas[i] = (sica[idx].mean() - sc[idx].mean()) * 100
    ci_lo = np.percentile(deltas, 100 * alpha / 2)
    ci_hi = np.percentile(deltas, 100 * (1 - alpha / 2))
    return point_est, ci_lo, ci_hi


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    power_results = []
    bootstrap_results = []

    print("=" * 110)
    print("POWER ANALYSIS: McNemar Test MDE (alpha=0.05, power=0.80)")
    print("=" * 110)
    hdr = (f"{'Model':<18} {'Domain':<13} {'n':>5} {'obs_D(pp)':>10} "
           f"{'disc':>5} {'sica_w':>6} {'sc_w':>5} {'MDE_80%(pp)':>12} "
           f"{'obs_power':>10} {'underpow?':>10}")
    print(hdr)
    print("-" * 110)

    for exp in EXPERIMENTS:
        d = load_experiment(exp)
        n, n_d = d["n"], d["discordant_pairs"]
        mde, _ = mcnemar_mde_exact(n, n_d)
        obs_pow = mcnemar_observed_power(n_d, d["sica_wins"], d["sc_wins"])
        underpow = mde == float("inf") or abs(d["delta_pp"]) < mde

        mde_s = f"{mde:.2f}" if mde != float("inf") else "inf"
        print(f"{exp['model']:<18} {exp['domain']:<13} {n:>5} "
              f"{d['delta_pp']:>+10.2f} {n_d:>5} {d['sica_wins']:>6} "
              f"{d['sc_wins']:>5} {mde_s:>12} {obs_pow:>10.3f} "
              f"{'YES' if underpow else 'no':>10}")

        power_results.append({
            "exp_id": exp["exp_id"],
            "model": exp["model"],
            "domain": exp["domain"],
            "n": n,
            "observed_delta_pp": round(d["delta_pp"], 4),
            "discordant_pairs": n_d,
            "sica_wins": d["sica_wins"],
            "sc_wins": d["sc_wins"],
            "mde_80_pp": round(mde, 4) if mde != float("inf") else None,
            "observed_power": round(obs_pow, 4),
            "underpowered": underpow,
        })

        pt, ci_lo, ci_hi = bootstrap_ci(d["sica_arr"], d["sc_arr"])
        bootstrap_results.append({
            "exp_id": exp["exp_id"],
            "model": exp["model"],
            "domain": exp["domain"],
            "n": n,
            "delta_pp": round(pt, 4),
            "ci_lower": round(ci_lo, 4),
            "ci_upper": round(ci_hi, 4),
            "ci_includes_zero": bool(ci_lo <= 0 <= ci_hi),
        })

    print()
    print("=" * 100)
    print("BOOTSTRAP 95% CIs for Delta(SICA - SC) in pp (10000 resamples, seed=42)")
    print("=" * 100)
    hdr2 = (f"{'Model':<18} {'Domain':<13} {'n':>5} {'D(pp)':>8} "
            f"{'CI_lo':>8} {'CI_hi':>8} {'0 in CI?':>9}")
    print(hdr2)
    print("-" * 100)

    for br in bootstrap_results:
        print(f"{br['model']:<18} {br['domain']:<13} {br['n']:>5} "
              f"{br['delta_pp']:>+8.2f} {br['ci_lower']:>+8.2f} "
              f"{br['ci_upper']:>+8.2f} "
              f"{'Yes' if br['ci_includes_zero'] else 'No':>9}")

    with open(os.path.join(OUTPUT_DIR, "power_analysis.json"), "w") as f:
        json.dump(power_results, f, indent=2)
    with open(os.path.join(OUTPUT_DIR, "bootstrap_cis.json"), "w") as f:
        json.dump(bootstrap_results, f, indent=2)

    print()
    print(f"Saved: {OUTPUT_DIR}/power_analysis.json")
    print(f"Saved: {OUTPUT_DIR}/bootstrap_cis.json")


if __name__ == "__main__":
    main()

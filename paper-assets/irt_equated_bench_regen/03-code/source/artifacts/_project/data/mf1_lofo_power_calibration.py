#!/usr/bin/env python3
"""
MF1: LOFO Power Calibration — Random Subsample Baseline

Separates pure power effect (smaller N) from composition effect
(family-specific removal) in LOFO analysis.
"""

import sys
import time
import numpy as np
import pandas as pd
from scipy.sparse import load_npz
from pathlib import Path

BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/"
            "projects/irt_equated_bench_regen/artifacts")
OUT = BASE / "mf1_lofo_power_calibration"
OUT.mkdir(exist_ok=True)

sys.path.insert(0, str(BASE / "plan_028_bootstrap_ci"))
from mmlu_bootstrap_ci import mh_dif_c_pct_vec

N_REPS = 200
N_STRATA = 5

LOFO_MISTRAL_C_PCT = 22.47
LOFO_LLAMA3_C_PCT = 24.06


def main():
    t0 = time.time()

    # ── Load data ──
    print("Loading response matrix (sparse)...")
    X = load_npz(BASE / "response_matrix.npz").toarray().astype(np.int8)
    idx = np.load(BASE / "response_matrix_index.npz", allow_pickle=True)
    model_names = idx["model_names"]
    J = X.shape[1]
    print(f"  {X.shape[0]} models × {J} items")

    meta = pd.read_csv(BASE / "plan_032_dif_cleaned_mmlu" / "cleaned_mmlu_analysis.csv")
    name2row = {n: i for i, n in enumerate(model_names)}

    ref_names = meta.loc[meta["cohort_temporal"] == "2023", "model_name"].values
    foc_names = meta.loc[meta["cohort_temporal"] == "2024", "model_name"].values
    ref_idx = np.array([name2row[n] for n in ref_names if n in name2row])
    foc_idx = np.array([name2row[n] for n in foc_names if n in name2row])
    print(f"  Ref(2023): {len(ref_idx)}, Foc(2024): {len(foc_idx)}")

    X_ref = X[ref_idx]
    X_foc = X[foc_idx]

    # Identify family members
    ref_df = meta[meta["cohort_temporal"] == "2023"].copy()
    foc_df = meta[meta["cohort_temporal"] == "2024"].copy()

    mistral_ref_names = set(ref_df.loc[ref_df["family"] == "mistral", "model_name"])
    llama3_foc_names = set(foc_df.loc[foc_df["family"] == "llama-3", "model_name"])

    mistral_mask = np.array([n in mistral_ref_names for n in ref_names if n in name2row])
    llama3_mask = np.array([n in llama3_foc_names for n in foc_names if n in name2row])

    n_mistral = mistral_mask.sum()
    n_llama3 = llama3_mask.sum()
    n_ref_after_mistral = len(ref_idx) - n_mistral
    n_foc_after_llama3 = len(foc_idx) - n_llama3
    print(f"  Mistral in ref: {n_mistral} → subsample size: {n_ref_after_mistral}")
    print(f"  Llama-3 in foc: {n_llama3} → subsample size: {n_foc_after_llama3}")

    del X

    # ── (1) Full Baseline ──
    print("\n[1/3] Full baseline...")
    t1 = time.time()
    baseline_c = mh_dif_c_pct_vec(X_ref, X_foc, n_strata=N_STRATA)
    print(f"  Full baseline C% = {baseline_c:.2f}%  ({time.time()-t1:.1f}s)")

    # ── (2a) Verify LOFO observed values ──
    print("\n[2/3] LOFO verification...")
    X_ref_no_mistral = X_ref[~mistral_mask]
    lofo_mistral_c = mh_dif_c_pct_vec(X_ref_no_mistral, X_foc, n_strata=N_STRATA)
    print(f"  LOFO Mistral C% = {lofo_mistral_c:.2f}% (expected {LOFO_MISTRAL_C_PCT}%)")

    X_foc_no_llama3 = X_foc[~llama3_mask]
    lofo_llama3_c = mh_dif_c_pct_vec(X_ref, X_foc_no_llama3, n_strata=N_STRATA)
    print(f"  LOFO Llama-3 C% = {lofo_llama3_c:.2f}% (expected {LOFO_LLAMA3_C_PCT}%)")

    # ── (3a) Random Subsample — Scenario A (Mistral-equivalent N reduction in ref) ──
    print(f"\n[3/3] Random subsample ({N_REPS} reps each)...")
    print(f"  Scenario A: random {n_ref_after_mistral} from ref ({len(ref_idx)})")
    results_A = np.empty(N_REPS)
    t_a = time.time()
    for seed in range(N_REPS):
        rng = np.random.RandomState(seed)
        chosen = rng.choice(len(ref_idx), n_ref_after_mistral, replace=False)
        results_A[seed] = mh_dif_c_pct_vec(X_ref[chosen], X_foc, n_strata=N_STRATA)
        if (seed + 1) % 50 == 0:
            elapsed = time.time() - t_a
            eta = elapsed / (seed + 1) * (N_REPS - seed - 1)
            print(f"    [{seed+1}/{N_REPS}] mean={results_A[:seed+1].mean():.2f}% "
                  f"sd={results_A[:seed+1].std():.2f}% ({elapsed:.0f}s, ETA {eta:.0f}s)")
    print(f"  Scenario A done: mean={results_A.mean():.2f}% ± {results_A.std():.2f}%")

    # ── (3b) Random Subsample — Scenario B (Llama-3-equivalent N reduction in foc) ──
    print(f"  Scenario B: random {n_foc_after_llama3} from foc ({len(foc_idx)})")
    results_B = np.empty(N_REPS)
    t_b = time.time()
    for seed in range(N_REPS):
        rng = np.random.RandomState(seed)
        chosen = rng.choice(len(foc_idx), n_foc_after_llama3, replace=False)
        results_B[seed] = mh_dif_c_pct_vec(X_ref, X_foc[chosen], n_strata=N_STRATA)
        if (seed + 1) % 50 == 0:
            elapsed = time.time() - t_b
            eta = elapsed / (seed + 1) * (N_REPS - seed - 1)
            print(f"    [{seed+1}/{N_REPS}] mean={results_B[:seed+1].mean():.2f}% "
                  f"sd={results_B[:seed+1].std():.2f}% ({elapsed:.0f}s, ETA {eta:.0f}s)")
    print(f"  Scenario B done: mean={results_B.mean():.2f}% ± {results_B.std():.2f}%")

    # ── Results ──
    total_time = time.time() - t0

    print("\n" + "=" * 70)
    print("RESULTS")
    print("=" * 70)

    power_A = results_A.mean() - baseline_c
    power_B = results_B.mean() - baseline_c
    comp_A = lofo_mistral_c - results_A.mean()
    comp_B = lofo_llama3_c - results_B.mean()

    header = f"{'':20s} {'Full':>10s} {'Random (mean±SD)':>20s} {'LOFO Obs':>10s} {'Power Δ':>10s} {'Comp Δ':>10s}"
    print(header)
    print("-" * len(header))
    print(f"{'Remove Mistral':20s} {baseline_c:>9.2f}% {results_A.mean():>9.2f}±{results_A.std():.2f}% "
          f"{lofo_mistral_c:>9.2f}% {power_A:>+9.2f}% {comp_A:>+9.2f}%")
    print(f"{'Remove Llama-3':20s} {baseline_c:>9.2f}% {results_B.mean():>9.2f}±{results_B.std():.2f}% "
          f"{lofo_llama3_c:>9.2f}% {power_B:>+9.2f}% {comp_B:>+9.2f}%")

    total_drop_A = lofo_mistral_c - baseline_c
    total_drop_B = lofo_llama3_c - baseline_c
    pct_power_A = (power_A / total_drop_A * 100) if total_drop_A != 0 else 0
    pct_power_B = (power_B / total_drop_B * 100) if total_drop_B != 0 else 0
    pct_comp_A = (comp_A / total_drop_A * 100) if total_drop_A != 0 else 0
    pct_comp_B = (comp_B / total_drop_B * 100) if total_drop_B != 0 else 0

    print(f"\nMistral: total drop = {total_drop_A:+.2f}pp → "
          f"power {pct_power_A:.0f}%, composition {pct_comp_A:.0f}%")
    print(f"Llama-3: total drop = {total_drop_B:+.2f}pp → "
          f"power {pct_power_B:.0f}%, composition {pct_comp_B:.0f}%")
    print(f"\nTotal runtime: {total_time/60:.1f} min")

    # ── Save CSV ──
    rows = [
        {"scenario": "remove_mistral", "n_ref": len(ref_idx), "n_foc": len(foc_idx),
         "type": "full", "c_pct_mean": baseline_c, "c_pct_sd": 0.0, "n_reps": 1},
        {"scenario": "remove_mistral", "n_ref": n_ref_after_mistral, "n_foc": len(foc_idx),
         "type": "random_subsample", "c_pct_mean": results_A.mean(),
         "c_pct_sd": results_A.std(), "n_reps": N_REPS},
        {"scenario": "remove_mistral", "n_ref": n_ref_after_mistral, "n_foc": len(foc_idx),
         "type": "lofo_observed", "c_pct_mean": lofo_mistral_c, "c_pct_sd": 0.0, "n_reps": 1},
        {"scenario": "remove_llama3", "n_ref": len(ref_idx), "n_foc": len(foc_idx),
         "type": "full", "c_pct_mean": baseline_c, "c_pct_sd": 0.0, "n_reps": 1},
        {"scenario": "remove_llama3", "n_ref": len(ref_idx), "n_foc": n_foc_after_llama3,
         "type": "random_subsample", "c_pct_mean": results_B.mean(),
         "c_pct_sd": results_B.std(), "n_reps": N_REPS},
        {"scenario": "remove_llama3", "n_ref": len(ref_idx), "n_foc": n_foc_after_llama3,
         "type": "lofo_observed", "c_pct_mean": lofo_llama3_c, "c_pct_sd": 0.0, "n_reps": 1},
    ]
    df = pd.DataFrame(rows)
    df.to_csv(OUT / "power_calibration_results.csv", index=False)
    print(f"\nSaved: {OUT / 'power_calibration_results.csv'}")

    # ── Save per-rep details ──
    reps_df = pd.DataFrame({
        "rep": np.tile(np.arange(N_REPS), 2),
        "scenario": np.repeat(["remove_mistral", "remove_llama3"], N_REPS),
        "c_pct": np.concatenate([results_A, results_B]),
    })
    reps_df.to_csv(OUT / "power_calibration_reps.csv", index=False)

    # ── Save Report ──
    report = f"""# MF1: LOFO Power Calibration — Random Subsample Baseline

## Method

Random subsample on real response matrix ({X_ref.shape[1]} items, {N_REPS} reps per scenario).
For each LOFO scenario, draw the same number of models randomly (without targeting any family)
and compute MH-DIF C%. The gap between random subsample and observed LOFO isolates the
composition effect from the pure power (sample-size) effect.

- Full baseline: N_ref={len(ref_idx)}, N_foc={len(foc_idx)} → C%={baseline_c:.2f}%
- MH-DIF: 5-stratum total-score matching, ETS C classification (|Δ_MH|≥1.5, p<0.05)

## Results

| | Full Baseline | Random Subsample (mean±SD) | LOFO Observed | Power Effect | Composition Effect |
|---|---|---|---|---|---|
| Remove Mistral (N_ref: {len(ref_idx)}→{n_ref_after_mistral}) | {baseline_c:.2f}% | {results_A.mean():.2f}±{results_A.std():.2f}% | {lofo_mistral_c:.2f}% | {power_A:+.2f}pp | {comp_A:+.2f}pp |
| Remove Llama-3 (N_foc: {len(foc_idx)}→{n_foc_after_llama3}) | {baseline_c:.2f}% | {results_B.mean():.2f}±{results_B.std():.2f}% | {lofo_llama3_c:.2f}% | {power_B:+.2f}pp | {comp_B:+.2f}pp |

## Decomposition

**Mistral removal** (total drop: {total_drop_A:+.2f}pp):
- Power effect (random subsample − full): {power_A:+.2f}pp ({pct_power_A:.0f}%)
- Composition effect (LOFO − random subsample): {comp_A:+.2f}pp ({pct_comp_A:.0f}%)

**Llama-3 removal** (total drop: {total_drop_B:+.2f}pp):
- Power effect (random subsample − full): {power_B:+.2f}pp ({pct_power_B:.0f}%)
- Composition effect (LOFO − random subsample): {comp_B:+.2f}pp ({pct_comp_B:.0f}%)

## Interpretation

{'Both scenarios show composition effects beyond pure power reduction, confirming that family-specific removal changes DIF detection beyond what sample size alone explains.' if (comp_A < -1 and comp_B < -1) else 'See decomposition above for the relative contribution of power vs. composition effects.'}

Random subsample 95% range:
- Scenario A (Mistral): [{np.percentile(results_A, 2.5):.2f}%, {np.percentile(results_A, 97.5):.2f}%]
- Scenario B (Llama-3): [{np.percentile(results_B, 2.5):.2f}%, {np.percentile(results_B, 97.5):.2f}%]

LOFO observed {'falls below' if lofo_mistral_c < np.percentile(results_A, 2.5) else 'falls within'} the random subsample 95% range for Mistral.
LOFO observed {'falls below' if lofo_llama3_c < np.percentile(results_B, 2.5) else 'falls within'} the random subsample 95% range for Llama-3.

Runtime: {total_time/60:.1f} min ({N_REPS} reps × 2 scenarios)
"""
    (OUT / "power_calibration_report.md").write_text(report)
    print(f"Saved: {OUT / 'power_calibration_report.md'}")


if __name__ == "__main__":
    main()

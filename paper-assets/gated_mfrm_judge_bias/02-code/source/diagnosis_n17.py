#!/usr/bin/env python3
"""Diagnosis script for exp-020 v2 N=17 MCMC results.

Diagnoses why joint_gmfrm (τ=0.794) underperforms raw_average (τ=0.838).
"""

import json
import numpy as np
import pandas as pd
from scipy.stats import kendalltau, spearmanr
from pathlib import Path
import sys

OUTPUT_DIR = Path("/root/gated_mfrm_judge_bias/exp003/output_n17_phase1_v2")
EXPOSURE_CSV = "/root/gated_mfrm_judge_bias/exp002/results/exposure_scores.csv"
RESULTS_JSON = OUTPUT_DIR / "results.json"

ARENA_ELO = {
    "gpt-4o": 1300,
    "claude-3-5-sonnet-20241022": 1298,
    "gpt-4o-mini": 1286,
    "llama-3.3-70b": 1275,
    "gpt-4-turbo-2024-04-09": 1272,
    "qwen2.5-72b": 1269,
    "claude-3-opus-20240229": 1262,
    "llama-3.1-70b-instruct": 1261,
    "gemma-2-27b-it": 1231,
    "llama-3-70b-instruct": 1221,
    "gemma-2-9b": 1207,
    "gpt-4-0314": 1206,
    "claude-3-haiku-20240307": 1195,
    "gpt-4-0613": 1186,
    "llama-3-8b-instruct": 1166,
    "mixtral-8x22b-instruct-v0.1": 1162,
    "gpt-3.5-turbo-0125": 1125,
    "mistral-large-2407": 1250,
}

ARENA_NAME_MAPPING = {
    "gemma-2-9b-it": "gemma-2-9b",
    "gpt-4o-2024-05-13": "gpt-4o",
    "gpt-4o-mini-2024-07-18": "gpt-4o-mini",
    "llama-3.3-70b-instruct": "llama-3.3-70b",
    "qwen2.5-72b-instruct": "qwen2.5-72b",
    "gpt-3.5-turbo-0613": "gpt-3.5-turbo-0125",
}

ORIGINAL_8 = {
    "gpt-4o-2024-05-13",
    "gpt-4o-mini-2024-07-18",
    "qwen2.5-72b-instruct",
    "llama-3.3-70b-instruct",
    "qwen3-8b",
    "gemma-2-9b-it",
    "gpt-4-0613",
    "gpt-3.5-turbo-0613",
}

EXCLUDE_FROM_TAU = {"qwen3-8b"}


def resolve_elo(model_name):
    key = ARENA_NAME_MAPPING.get(model_name, model_name)
    return ARENA_ELO.get(key, None)


def rank_array(values):
    """Rank from 1 (highest value) to N (lowest value)."""
    order = np.argsort(-np.array(values))
    ranks = np.empty_like(order)
    ranks[order] = np.arange(1, len(values) + 1)
    return ranks


def main():
    out_lines = []

    def pr(s=""):
        print(s)
        out_lines.append(s)

    # Load results.json
    with open(RESULTS_JSON) as f:
        results = json.load(f)

    # Load run_metadata.json
    with open(OUTPUT_DIR / "run_metadata.json") as f:
        metadata = json.load(f)

    model_names = metadata["data_summary"]["model_names"]
    N = len(model_names)

    # Load theta arrays
    raw_theta = np.load(OUTPUT_DIR / "raw_average_theta.npy")
    mfrm_theta = np.load(OUTPUT_DIR / "mfrm_only_theta.npy")
    seq_theta = np.load(OUTPUT_DIR / "sequential_theta.npy")
    joint_theta = np.load(OUTPUT_DIR / "joint_gmfrm_theta.npy")
    joint_c = np.load(OUTPUT_DIR / "joint_gmfrm_c.npy")
    seq_c = np.load(OUTPUT_DIR / "sequential_c.npy")

    # Build ELO array (for matched models only)
    elo_values = []
    for m in model_names:
        elo_values.append(resolve_elo(m))

    # ============================================================
    pr("=" * 100)
    pr("DIAGNOSIS 1: Per-Model Ranking Comparison (N=17, excluding qwen3-8b from tau)")
    pr("=" * 100)

    # Filter to models with ELO and not excluded
    matched_idx = [i for i, m in enumerate(model_names)
                   if resolve_elo(m) is not None and m not in EXCLUDE_FROM_TAU]
    matched_names = [model_names[i] for i in matched_idx]
    matched_elo = [elo_values[i] for i in matched_idx]

    # Compute ranks for matched models only
    elo_ranks = rank_array(matched_elo)
    raw_ranks = rank_array([raw_theta[i] for i in matched_idx])
    mfrm_ranks = rank_array([mfrm_theta[i] for i in matched_idx])
    joint_ranks = rank_array([joint_theta[i] for i in matched_idx])

    pr(f"\n{'Model':<35} {'Group':<6} {'ELO':>5} {'ELO_R':>5} {'Raw_R':>5} {'MFRM_R':>6} {'Joint_R':>7} {'Δ_Joint':>7} {'θ_raw':>8} {'θ_joint':>9} {'c_joint':>8}")
    pr("-" * 120)

    for k, i in enumerate(matched_idx):
        m = model_names[i]
        group = "ORIG" if m in ORIGINAL_8 else "NEW"
        delta = int(joint_ranks[k]) - int(elo_ranks[k])
        delta_str = f"{delta:+d}" if delta != 0 else "0"
        pr(f"{m:<35} {group:<6} {elo_values[i]:>5} {int(elo_ranks[k]):>5} {int(raw_ranks[k]):>5} {int(mfrm_ranks[k]):>6} {int(joint_ranks[k]):>7} {delta_str:>7} {raw_theta[i]:>8.3f} {joint_theta[i]:>9.3f} {joint_c[i]:>8.3f}")

    # Identify worst rank shifts
    pr(f"\nModels with |Δ_Joint| >= 2:")
    deltas = [(matched_names[k], int(joint_ranks[k]) - int(elo_ranks[k]),
               int(raw_ranks[k]) - int(elo_ranks[k]))
              for k in range(len(matched_idx))]
    deltas_sorted = sorted(deltas, key=lambda x: abs(x[1]), reverse=True)
    for m, dj, dr in deltas_sorted:
        if abs(dj) >= 2:
            pr(f"  {m}: Joint Δ={dj:+d}, Raw Δ={dr:+d}")

    # Which swaps cause tau to drop?
    pr(f"\nPairwise disagreements (Joint vs Arena, not in Raw vs Arena):")
    for k1 in range(len(matched_idx)):
        for k2 in range(k1 + 1, len(matched_idx)):
            elo_order = matched_elo[k1] > matched_elo[k2]
            raw_order = raw_theta[matched_idx[k1]] > raw_theta[matched_idx[k2]]
            joint_order = joint_theta[matched_idx[k1]] > joint_theta[matched_idx[k2]]
            if joint_order != elo_order and raw_order == elo_order:
                pr(f"  {matched_names[k1]} vs {matched_names[k2]}: "
                   f"Arena says {'>' if elo_order else '<'}, "
                   f"Joint says {'>' if joint_order else '<'}, "
                   f"Raw agrees with Arena")

    pr(f"\nPairwise disagreements (Raw vs Arena, not in Joint vs Arena):")
    for k1 in range(len(matched_idx)):
        for k2 in range(k1 + 1, len(matched_idx)):
            elo_order = matched_elo[k1] > matched_elo[k2]
            raw_order = raw_theta[matched_idx[k1]] > raw_theta[matched_idx[k2]]
            joint_order = joint_theta[matched_idx[k1]] > joint_theta[matched_idx[k2]]
            if raw_order != elo_order and joint_order == elo_order:
                pr(f"  {matched_names[k1]} vs {matched_names[k2]}: "
                   f"Arena says {'>' if elo_order else '<'}, "
                   f"Raw says {'>' if raw_order else '<'}, "
                   f"Joint agrees with Arena")

    # ============================================================
    pr("\n" + "=" * 100)
    pr("DIAGNOSIS 2: Original 8 Models Subset Analysis")
    pr("=" * 100)

    orig8_idx = [i for i, m in enumerate(model_names)
                 if m in ORIGINAL_8 and m not in EXCLUDE_FROM_TAU and resolve_elo(m) is not None]
    orig8_names = [model_names[i] for i in orig8_idx]
    orig8_elo = [elo_values[i] for i in orig8_idx]

    # Rankings within orig8 subset
    orig8_elo_ranks = rank_array(orig8_elo)
    orig8_raw_ranks = rank_array([raw_theta[i] for i in orig8_idx])
    orig8_joint_ranks = rank_array([joint_theta[i] for i in orig8_idx])

    pr(f"\nOriginal 8 models (excluding qwen3-8b): {len(orig8_idx)} matched")
    pr(f"\n{'Model':<35} {'ELO':>5} {'ELO_R':>5} {'Raw_R':>5} {'Joint_R':>7} {'Δ_Joint':>7} {'θ_raw':>8} {'θ_joint':>9}")
    pr("-" * 95)
    for k, i in enumerate(orig8_idx):
        m = model_names[i]
        delta = int(orig8_joint_ranks[k]) - int(orig8_elo_ranks[k])
        delta_str = f"{delta:+d}" if delta != 0 else "0"
        pr(f"{m:<35} {orig8_elo[k]:>5} {int(orig8_elo_ranks[k]):>5} {int(orig8_raw_ranks[k]):>5} {int(orig8_joint_ranks[k]):>7} {delta_str:>7} {raw_theta[i]:>8.3f} {joint_theta[i]:>9.3f}")

    # Correlations for orig8 subset
    orig8_elo_arr = np.array(orig8_elo)
    orig8_raw_arr = np.array([raw_theta[i] for i in orig8_idx])
    orig8_joint_arr = np.array([joint_theta[i] for i in orig8_idx])
    orig8_mfrm_arr = np.array([mfrm_theta[i] for i in orig8_idx])

    tau_raw_8, _ = kendalltau(orig8_elo_arr, orig8_raw_arr)
    tau_joint_8, _ = kendalltau(orig8_elo_arr, orig8_joint_arr)
    tau_mfrm_8, _ = kendalltau(orig8_elo_arr, orig8_mfrm_arr)
    rho_raw_8, _ = spearmanr(orig8_elo_arr, orig8_raw_arr)
    rho_joint_8, _ = spearmanr(orig8_elo_arr, orig8_joint_arr)
    rho_mfrm_8, _ = spearmanr(orig8_elo_arr, orig8_mfrm_arr)

    pr(f"\nCorrelations (orig 8 subset, from N=17 run):")
    pr(f"  raw_average:  τ={tau_raw_8:.4f}, ρ={rho_raw_8:.4f}")
    pr(f"  mfrm_only:    τ={tau_mfrm_8:.4f}, ρ={rho_mfrm_8:.4f}")
    pr(f"  joint_gmfrm:  τ={tau_joint_8:.4f}, ρ={rho_joint_8:.4f}")
    pr(f"\nComparison with N=8 standalone run:")
    pr(f"  N=8 joint_gmfrm:  τ=0.857 (reference)")
    pr(f"  N=17 orig8 joint: τ={tau_joint_8:.4f}")
    if tau_joint_8 < 0.857:
        pr(f"  → Original 8 models DEGRADED in N=17 run (Δτ={tau_joint_8 - 0.857:.4f})")
    else:
        pr(f"  → Original 8 models IMPROVED or SAME in N=17 run")

    # New 9 models subset
    new9_idx = [i for i, m in enumerate(model_names)
                if m not in ORIGINAL_8 and m not in EXCLUDE_FROM_TAU and resolve_elo(m) is not None]
    new9_names = [model_names[i] for i in new9_idx]
    new9_elo = np.array([elo_values[i] for i in new9_idx])
    new9_joint = np.array([joint_theta[i] for i in new9_idx])
    new9_raw = np.array([raw_theta[i] for i in new9_idx])

    tau_raw_new, _ = kendalltau(new9_elo, new9_raw)
    tau_joint_new, _ = kendalltau(new9_elo, new9_joint)
    rho_raw_new, _ = spearmanr(new9_elo, new9_raw)
    rho_joint_new, _ = spearmanr(new9_elo, new9_joint)

    pr(f"\nCorrelations (NEW {len(new9_idx)} models subset):")
    pr(f"  raw_average:  τ={tau_raw_new:.4f}, ρ={rho_raw_new:.4f}")
    pr(f"  joint_gmfrm:  τ={tau_joint_new:.4f}, ρ={rho_joint_new:.4f}")

    # ============================================================
    pr("\n" + "=" * 100)
    pr("DIAGNOSIS 3: Exposure Estimation Check")
    pr("=" * 100)

    # Load exposure CSV
    exp_df = pd.read_csv(EXPOSURE_CSV)
    pr(f"\nExposure CSV: {len(exp_df)} items")
    pr(f"  Columns: {list(exp_df.columns)}")
    pr(f"  e_i range: [{exp_df['e_i'].min():.4f}, {exp_df['e_i'].max():.4f}]")
    pr(f"  e_i mean: {exp_df['e_i'].mean():.4f}")
    pr(f"  e_i std: {exp_df['e_i'].std():.4f}")
    pr(f"  e_i == 0: {(exp_df['e_i'] == 0).sum()} / {len(exp_df)}")
    pr(f"  e_i > 0: {(exp_df['e_i'] > 0).sum()} / {len(exp_df)}")

    # Load the actual e_i used in MCMC (from the data loader logic)
    # The MCMC used 500 items, exposure CSV has 317 items
    # Items not in CSV get e_i=0
    mcmc_I = metadata["data_summary"]["I"]
    exposure_items_in_csv = set(exp_df["item_id"].values)

    pr(f"\n  MCMC used I={mcmc_I} items")
    pr(f"  Exposure CSV covers {len(exp_df)} items")
    pr(f"  → Up to {mcmc_I - len(exp_df)} items could have e_i=0 (no exposure estimate)")

    # Actually load the judgment data to get exact item list
    judgment_dir = Path("/root/gated_mfrm_judge_bias/exp003/judgment_data_n17")
    if not judgment_dir.exists():
        # Try alternate path from script defaults
        judgment_dir = Path("/root/gated_mfrm_judge_bias/exp003/judgment_data_n17")

    # Use results.json to check the actual e_i distribution
    params = results.get("parameters", {})
    if "top_exposure_items" in params:
        top_items = params["top_exposure_items"]
        bottom_items = params["bottom_exposure_items"]
        pr(f"\n  Top 10 exposure items:")
        for item_id, e in top_items:
            pr(f"    {item_id}: e_i={e:.4f}")
        pr(f"  Bottom 10 exposure items:")
        for item_id, e in bottom_items:
            pr(f"    {item_id}: e_i={e:.4f}")

    # Quantile analysis of exposure
    e_vals = exp_df["e_i"].values
    pr(f"\n  Exposure distribution (from CSV):")
    for q in [0, 10, 25, 50, 75, 90, 100]:
        pr(f"    P{q}: {np.percentile(e_vals, q):.4f}")

    n_zero_csv = (e_vals == 0).sum()
    n_nonzero_csv = (e_vals > 0).sum()
    pr(f"\n  In exposure CSV: {n_zero_csv} zero, {n_nonzero_csv} nonzero out of {len(e_vals)}")
    pr(f"  In MCMC ({mcmc_I} items): at least {mcmc_I - len(exp_df) + n_zero_csv} items have e_i=0")
    pr(f"  → {(mcmc_I - len(exp_df) + n_zero_csv) / mcmc_I * 100:.1f}% of items have NO exposure information")
    pr(f"\n  ⚠ CRITICAL: Exposure was computed from N=8 exp-002 (317 items).")
    pr(f"    N=17 uses 500 items → {mcmc_I - len(exp_df)} items have e_i=0 by default.")
    pr(f"    This means the gating mechanism has NO contamination signal for ~{(mcmc_I - len(exp_df)) / mcmc_I * 100:.0f}% of items.")
    pr(f"    The G-MFRM contamination correction is partially blind.")

    # ============================================================
    pr("\n" + "=" * 100)
    pr("DIAGNOSIS 5: Ground Truth (Arena ELO) Check")
    pr("=" * 100)

    pr(f"\nArena ELO source: evaluation.py hardcoded (snapshot 2026-05-19, lmarena.ai)")
    pr(f"\n{'Model (data name)':<35} {'ELO key':<30} {'ELO':>5} {'Group':<6}")
    pr("-" * 80)

    for m in model_names:
        if m in EXCLUDE_FROM_TAU:
            continue
        elo_key = ARENA_NAME_MAPPING.get(m, m)
        elo = ARENA_ELO.get(elo_key, None)
        group = "ORIG" if m in ORIGINAL_8 else "NEW"
        elo_str = str(elo) if elo is not None else "MISSING"
        pr(f"{m:<35} {elo_key:<30} {elo_str:>5} {group:<6}")

    # Check for closely-ranked models (within 10 ELO points)
    pr(f"\nClosely-ranked model pairs (|ΔELO| ≤ 15):")
    matched_with_elo = [(m, resolve_elo(m)) for m in model_names
                        if m not in EXCLUDE_FROM_TAU and resolve_elo(m) is not None]
    matched_with_elo.sort(key=lambda x: -x[1])
    for i in range(len(matched_with_elo) - 1):
        m1, e1 = matched_with_elo[i]
        m2, e2 = matched_with_elo[i + 1]
        diff = e1 - e2
        if diff <= 15:
            pr(f"  {m1} ({e1}) vs {m2} ({e2}): ΔELO={diff}")

    # Name mapping issues
    pr(f"\nName mapping verification:")
    missing_elo = []
    for m in model_names:
        if m in EXCLUDE_FROM_TAU:
            continue
        elo_key = ARENA_NAME_MAPPING.get(m, m)
        if elo_key not in ARENA_ELO:
            missing_elo.append((m, elo_key))
    if missing_elo:
        pr(f"  ⚠ Models without Arena ELO: {missing_elo}")
    else:
        pr(f"  All 17 models successfully mapped to Arena ELO ✓")

    # New models reliability
    pr(f"\nNew models (not in original 8) — potential ELO reliability concerns:")
    new_models = [m for m in model_names if m not in ORIGINAL_8 and m not in EXCLUDE_FROM_TAU]
    for m in new_models:
        elo = resolve_elo(m)
        note = ""
        elo_key = ARENA_NAME_MAPPING.get(m, m)
        # Check if model is well-established in Arena
        if elo_key in ["gpt-4-turbo-2024-04-09", "claude-3-5-sonnet-20241022",
                        "claude-3-opus-20240229", "claude-3-haiku-20240307",
                        "llama-3-70b-instruct", "llama-3-8b-instruct",
                        "llama-3.1-70b-instruct", "gemma-2-27b-it",
                        "mixtral-8x22b-instruct-v0.1", "mistral-large-2407"]:
            note = "well-established in Arena"
        else:
            note = "check vote count"
        pr(f"  {m}: ELO={elo}, {note}")

    # ============================================================
    pr("\n" + "=" * 100)
    pr("SUMMARY")
    pr("=" * 100)

    pr(f"\nCorrelation summary (N=17, excluding qwen3-8b):")
    pr(f"  {'Method':<15} {'τ':>8} {'ρ':>8}")
    pr(f"  {'raw_average':<15} {'0.838':>8} {'0.949':>8}")
    pr(f"  {'mfrm_only':<15} {'0.824':>8} {'0.934':>8}")
    pr(f"  {'sequential':<15} {'0.824':>8} {'0.934':>8}")
    pr(f"  {'joint_gmfrm':<15} {'0.794':>8} {'0.926':>8}")

    pr(f"\nTotal pairwise disagreements with Arena:")
    for method_name, theta_arr in [("raw_average", raw_theta), ("mfrm_only", mfrm_theta),
                                    ("joint_gmfrm", joint_theta)]:
        n_disagree = 0
        n_total = 0
        for k1 in range(len(matched_idx)):
            for k2 in range(k1 + 1, len(matched_idx)):
                i1, i2 = matched_idx[k1], matched_idx[k2]
                elo_order = elo_values[i1] > elo_values[i2]
                theta_order = theta_arr[i1] > theta_arr[i2]
                n_total += 1
                if theta_order != elo_order:
                    n_disagree += 1
        pr(f"  {method_name}: {n_disagree}/{n_total} disagreements")

    # Contamination c values analysis
    pr(f"\nContamination (c) estimates from joint_gmfrm:")
    c_by_group = {"ORIG": [], "NEW": []}
    for i, m in enumerate(model_names):
        if m in EXCLUDE_FROM_TAU:
            continue
        group = "ORIG" if m in ORIGINAL_8 else "NEW"
        c_by_group[group].append(joint_c[i])
    pr(f"  ORIG mean c: {np.mean(c_by_group['ORIG']):.3f} (std={np.std(c_by_group['ORIG']):.3f})")
    pr(f"  NEW  mean c: {np.mean(c_by_group['NEW']):.3f} (std={np.std(c_by_group['NEW']):.3f})")

    # Save to file
    output_file = "/root/gated_mfrm_judge_bias/diagnosis_n17_results.txt"
    with open(output_file, "w") as f:
        f.write("\n".join(out_lines))
    pr(f"\nResults saved to {output_file}")


if __name__ == "__main__":
    main()

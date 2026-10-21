#!/usr/bin/env python3
"""Plan 001 Step 3: Compute 15-model pairwise MI matrix and K_eff for all C(15,3) panels."""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

import sys
sys.path.insert(0, "/root/cert_manip_resist_eval")

import json
import itertools
import numpy as np
from pathlib import Path
from sklearn.metrics import mutual_info_score

from src.utils import setup_logging
from src.unified_data_loader import (
    ALL_MODELS, DATASETS, PLAN001_DIR, load_all_scores,
    _is_valid_score,
)

logger = setup_logging("plan001_step3_mi")

MI_DIR = PLAN001_DIR / "mi_matrix"


def extract_winner_vector(score_list):
    winners = []
    for s in score_list:
        if not isinstance(s, dict) or not _is_valid_score(s):
            winners.append("tie")
            continue
        winners.append(s["winner"])
    return winners


def compute_pairwise_mi(winners_i, winners_j):
    n = min(len(winners_i), len(winners_j))
    if n == 0:
        return 0.0
    return mutual_info_score(winners_i[:n], winners_j[:n])


def build_mi_matrix(clean_scores, dataset):
    ds_scores = clean_scores.get(dataset, {})
    n_models = len(ALL_MODELS)
    mi_mat = np.zeros((n_models, n_models))

    winner_vectors = {}
    for i, model_id in enumerate(ALL_MODELS):
        if model_id in ds_scores:
            winner_vectors[i] = extract_winner_vector(ds_scores[model_id])
        else:
            logger.warning(f"No clean scores for {model_id} on {dataset}")

    for i in range(n_models):
        for j in range(i + 1, n_models):
            if i in winner_vectors and j in winner_vectors:
                mi = compute_pairwise_mi(winner_vectors[i], winner_vectors[j])
                mi_mat[i, j] = mi
                mi_mat[j, i] = mi

    return mi_mat


def mi_based_keff(mi_matrix, model_indices):
    K = len(model_indices)
    if K <= 1:
        return 1.0
    keff = 0.0
    for i_idx in model_indices:
        term = 1.0
        for j_idx in model_indices:
            if i_idx != j_idx:
                term += np.exp(-2 * mi_matrix[i_idx, j_idx])
        keff += term
    return keff / K


def compute_all_panel_keffs(mi_matrix, dataset):
    n_models = len(ALL_MODELS)
    idx_to_model = {i: m for i, m in enumerate(ALL_MODELS)}
    panels = {}

    for combo in itertools.combinations(range(n_models), 3):
        model_ids = [idx_to_model[i] for i in combo]
        panel_key = "|".join(model_ids)
        keff = mi_based_keff(mi_matrix, list(combo))

        mi_pairs = {}
        for a, b in itertools.combinations(combo, 2):
            pair_key = f"{idx_to_model[a]}|{idx_to_model[b]}"
            mi_pairs[pair_key] = float(mi_matrix[a, b])

        panels[panel_key] = {
            "models": model_ids,
            "keff": float(keff),
            "mi_pairs": mi_pairs,
        }

    return panels


def main():
    logger.info("=== Plan 001 Step 3: MI Matrix Computation ===")

    clean_scores, _ = load_all_scores()

    for ds in DATASETS:
        available = list(clean_scores.get(ds, {}).keys())
        missing = [m for m in ALL_MODELS if m not in available]
        logger.info(f"  {ds}: {len(available)}/{len(ALL_MODELS)} models available")
        if missing:
            logger.warning(f"  {ds}: missing models: {missing}")

    available_count = sum(
        1 for ds in DATASETS
        for m in ALL_MODELS
        if m in clean_scores.get(ds, {})
    )
    total_needed = len(DATASETS) * len(ALL_MODELS)
    if available_count < total_needed:
        logger.warning(
            f"Only {available_count}/{total_needed} model*dataset combos available. "
            f"MI matrix will have zeros for missing pairs."
        )

    mi_matrices = {}
    keff_per_panel = {}

    for ds in DATASETS:
        logger.info(f"\n--- Computing MI matrix for {ds} ---")
        mi_mat = build_mi_matrix(clean_scores, ds)
        mi_matrices[ds] = mi_mat.tolist()

        nonzero = np.count_nonzero(mi_mat)
        max_possible = len(ALL_MODELS) * (len(ALL_MODELS) - 1)
        logger.info(f"  MI matrix: {nonzero}/{max_possible} non-zero entries")
        if nonzero > 0:
            upper = mi_mat[np.triu_indices_from(mi_mat, k=1)]
            upper_nz = upper[upper > 0]
            if len(upper_nz) > 0:
                logger.info(
                    f"  MI range: [{upper_nz.min():.4f}, {upper_nz.max():.4f}], "
                    f"mean={upper_nz.mean():.4f}"
                )

        logger.info(f"  Computing K_eff for all C(15,3)=455 panels on {ds}...")
        panels = compute_all_panel_keffs(mi_mat, ds)
        keff_per_panel[ds] = panels

        keff_values = [p["keff"] for p in panels.values()]
        logger.info(
            f"  K_eff range: [{min(keff_values):.3f}, {max(keff_values):.3f}], "
            f"mean={np.mean(keff_values):.3f}"
        )

    MI_DIR.mkdir(parents=True, exist_ok=True)
    output = {
        "models": ALL_MODELS,
        "mi_matrix": mi_matrices,
        "keff_per_panel": keff_per_panel,
    }
    output_path = MI_DIR / "mi_matrix_15models.json"
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    logger.info(f"\nSaved MI matrix to {output_path}")

    print("\n" + "=" * 70)
    print("MI MATRIX SUMMARY")
    print("=" * 70)
    for ds in DATASETS:
        mi_mat = np.array(mi_matrices[ds])
        upper = mi_mat[np.triu_indices_from(mi_mat, k=1)]
        n_computed = np.count_nonzero(upper)
        print(f"\n{ds}:")
        print(f"  Pairwise MI computed: {n_computed}/105")
        if n_computed > 0:
            nz = upper[upper > 0]
            print(f"  MI range: [{nz.min():.4f}, {nz.max():.4f}]")
            print(f"  MI mean:  {nz.mean():.4f}")
        keffs = [p["keff"] for p in keff_per_panel[ds].values()]
        print(f"  K_eff (455 panels): [{min(keffs):.3f}, {max(keffs):.3f}], mean={np.mean(keffs):.3f}")
    print("=" * 70)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# Step 2 (redesigned): High-K_eff vs Low-K_eff panel contrast.
# Rationale: Step 1 showed family identity ≠ MI driver; model capability proximity is.
# So we contrast panels by actual K_eff (from measured MI/ρ) instead of family label.
#
# Input: Step 1 pairwise MI/ρ, clean + attacked judge scores.
# Output: ASR comparison for high-K_eff vs low-K_eff panels + statistical tests.

import json
import os
import sys
from itertools import combinations
from pathlib import Path

os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.attacks import ALL_ATTACKS, apply_attack_to_pairs
from src.config import MODEL_REGISTRY, ExperimentConfig
from src.eval_pipeline import generate_response_pairs, load_eval_dataset
from src.judge_service import JudgeService
from src.keff import build_rho_matrix, empirical_keff_from_rho, get_max_pairwise_mi
from src.panels import Panel, measure_panel_asr
from src.utils import save_results, set_seed, setup_logging

logger = setup_logging("step2_keff")

# Use 3 representative attacks (one per category)
ATTACK_SUBSET = [a for a in ALL_ATTACKS if a.name in ("prompt_injection", "sycophancy", "score_manipulation")]
if len(ATTACK_SUBSET) < 3:
    ATTACK_SUBSET = ALL_ATTACKS[:3]


def mi_based_keff(pairwise_df: pd.DataFrame, judge_ids: list) -> float:
    """K_eff using exp(-2·MI) for each pairwise MI (all pairs, not just I_max)."""
    K = len(judge_ids)
    if K <= 1:
        return 1.0
    mi_lookup = {}
    for _, row in pairwise_df.iterrows():
        mi_lookup[(row["judge_i"], row["judge_j"])] = row["mi"]
        mi_lookup[(row["judge_j"], row["judge_i"])] = row["mi"]

    total = 0.0
    for i, ji in enumerate(judge_ids):
        k_eff_i = 1.0
        for j, jj in enumerate(judge_ids):
            if i != j:
                mi_val = mi_lookup.get((ji, jj), 0.0)
                k_eff_i += np.exp(-2.0 * mi_val)
        total += k_eff_i
    return float(total / K)


def rho_based_keff(pairwise_df: pd.DataFrame, judge_ids: list) -> float:
    """K_eff using (1-ρ²) for each pairwise copula ρ."""
    rho_mat = build_rho_matrix(pairwise_df, judge_ids, metric="copula_rho")
    return empirical_keff_from_rho(rho_mat)


def enumerate_panels_with_keff(
    pairwise_df: pd.DataFrame,
    model_ids: list,
    K: int = 3,
) -> list:
    """Enumerate all C(N,K) panels and compute both K_eff variants."""
    panels = []
    for combo in combinations(model_ids, K):
        judge_ids = list(combo)
        k_mi = mi_based_keff(pairwise_df, judge_ids)
        k_rho = rho_based_keff(pairwise_df, judge_ids)
        i_max = get_max_pairwise_mi(pairwise_df, judge_ids)
        families = [MODEL_REGISTRY[jid][2] for jid in judge_ids]
        panels.append({
            "judge_ids": judge_ids,
            "k_eff_mi": k_mi,
            "k_eff_rho": k_rho,
            "i_max": i_max,
            "n_families": len(set(families)),
            "families": families,
        })
    panels.sort(key=lambda x: x["k_eff_mi"], reverse=True)
    return panels


def main():
    config = ExperimentConfig()
    set_seed(config.seed)

    model_ids = list(MODEL_REGISTRY.keys())

    # Load Step 1 results
    results_dir = Path(config.results_dir)
    step1_files = sorted(results_dir.glob("results_step1_full_*.json"))
    if not step1_files:
        step1_files = sorted(results_dir.glob("results_step1_*.json"))
    if not step1_files:
        logger.error("No Step 1 results found.")
        sys.exit(1)
    with open(step1_files[-1]) as f:
        step1_data = json.load(f)
    logger.info(f"Loaded Step 1: {step1_files[-1]}")

    all_results = {}

    for ds_name in config.datasets:
        logger.info(f"\n{'='*60}")
        logger.info(f"Step 2 K_eff Contrast: {ds_name}")
        logger.info(f"{'='*60}")

        if ds_name not in step1_data:
            logger.warning(f"No Step 1 data for {ds_name}, skipping.")
            continue

        pairwise_df = pd.DataFrame(step1_data[ds_name]["pairwise"])

        # Enumerate all K=3 panels and compute K_eff
        all_panels = enumerate_panels_with_keff(pairwise_df, model_ids, K=3)

        logger.info(f"\nAll {len(all_panels)} K=3 panels ranked by K_eff(MI):")
        for i, p in enumerate(all_panels):
            logger.info(
                f"  #{i+1:2d} K_eff(MI)={p['k_eff_mi']:.3f} "
                f"K_eff(ρ)={p['k_eff_rho']:.3f} "
                f"fam={p['n_families']} {p['judge_ids']}"
            )

        # Select top-3 (high K_eff) and bottom-3 (low K_eff)
        high_keff_panels = all_panels[:3]
        low_keff_panels = all_panels[-3:]

        logger.info(f"\nHigh K_eff panels (top-3):")
        for p in high_keff_panels:
            logger.info(f"  K_eff(MI)={p['k_eff_mi']:.3f} {p['judge_ids']}")
        logger.info(f"Low K_eff panels (bottom-3):")
        for p in low_keff_panels:
            logger.info(f"  K_eff(MI)={p['k_eff_mi']:.3f} {p['judge_ids']}")

        # Load dataset and generate pairs
        samples = load_eval_dataset(ds_name, config.n_samples)
        pairs = generate_response_pairs(samples, ds_name)

        # Collect scores from all judges (serial load/unload)
        clean_scores = {}
        attacked_scores_by_attack = {a.name: {} for a in ATTACK_SUBSET}

        for mid in model_ids:
            logger.info(f"\nLoading judge {mid}...")
            judge = JudgeService(mid).load()

            items = [
                {"question": p["question"], "response_a": p["response_a"], "response_b": p["response_b"]}
                for p in pairs
            ]
            clean_scores[mid] = judge.batch_score(items, mode="pairwise")

            for attack in ATTACK_SUBSET:
                attacked_pairs = apply_attack_to_pairs(pairs, attack)
                attacked_items = [
                    {"question": p["question"], "response_a": p["response_a"], "response_b": p["response_b"]}
                    for p in attacked_pairs
                ]
                attacked_scores_by_attack[attack.name][mid] = judge.batch_score(
                    attacked_items, mode="pairwise"
                )
                logger.info(f"  {mid} × {attack.name}: scored {len(attacked_items)} items")

            judge.unload()
            logger.info(f"  {mid}: unloaded")

        # Measure panel-level ASR
        def measure_panel_group_asr(panel_defs, group_name):
            group_results = []
            for pdef in panel_defs:
                panel = Panel(pdef["judge_ids"], panel_type=group_name)
                panel_result = {
                    "judge_ids": pdef["judge_ids"],
                    "k_eff_mi": pdef["k_eff_mi"],
                    "k_eff_rho": pdef["k_eff_rho"],
                    "group": group_name,
                    "attacks": {},
                }
                for attack in ATTACK_SUBSET:
                    asr = measure_panel_asr(
                        panel, clean_scores,
                        attacked_scores_by_attack[attack.name], pairs
                    )
                    panel_result["attacks"][attack.name] = asr
                panel_result["mean_asr"] = np.mean(
                    [panel_result["attacks"][a.name] for a in ATTACK_SUBSET]
                )
                group_results.append(panel_result)
            return group_results

        high_results = measure_panel_group_asr(high_keff_panels, "high_keff")
        low_results = measure_panel_group_asr(low_keff_panels, "low_keff")

        # Statistical comparison
        high_asrs = [r["mean_asr"] for r in high_results]
        low_asrs = [r["mean_asr"] for r in low_results]

        logger.info(f"\n{'='*60}")
        logger.info(f"RESULTS: {ds_name}")
        logger.info(f"{'='*60}")

        logger.info(f"\nHigh K_eff panels (more independent):")
        for r in high_results:
            atk_str = ", ".join(f"{k}={v:.3f}" for k, v in r["attacks"].items())
            logger.info(
                f"  K_eff(MI)={r['k_eff_mi']:.3f} mean_ASR={r['mean_asr']:.3f} "
                f"[{atk_str}] {r['judge_ids']}"
            )

        logger.info(f"\nLow K_eff panels (more correlated):")
        for r in low_results:
            atk_str = ", ".join(f"{k}={v:.3f}" for k, v in r["attacks"].items())
            logger.info(
                f"  K_eff(MI)={r['k_eff_mi']:.3f} mean_ASR={r['mean_asr']:.3f} "
                f"[{atk_str}] {r['judge_ids']}"
            )

        logger.info(f"\nHigh K_eff mean ASR: {np.mean(high_asrs):.4f}")
        logger.info(f"Low K_eff mean ASR:  {np.mean(low_asrs):.4f}")

        # Wilcoxon signed-rank test (if enough pairs)
        if len(high_asrs) >= 3 and len(low_asrs) >= 3:
            try:
                u_stat, u_p = stats.mannwhitneyu(
                    high_asrs, low_asrs, alternative="less"
                )
                logger.info(f"Mann-Whitney U: stat={u_stat:.4f}, p={u_p:.4f}")
            except Exception as e:
                logger.info(f"Mann-Whitney U failed: {e}")

        # Per-attack comparison
        logger.info(f"\nPer-attack breakdown:")
        for attack in ATTACK_SUBSET:
            h_asrs = [r["attacks"][attack.name] for r in high_results]
            l_asrs = [r["attacks"][attack.name] for r in low_results]
            logger.info(
                f"  {attack.name}: high_mean={np.mean(h_asrs):.4f} "
                f"low_mean={np.mean(l_asrs):.4f} "
                f"diff={np.mean(l_asrs) - np.mean(h_asrs):.4f}"
            )

        all_results[ds_name] = {
            "all_panels_ranked": all_panels,
            "high_keff": high_results,
            "low_keff": low_results,
            "summary": {
                "high_mean_asr": float(np.mean(high_asrs)),
                "low_mean_asr": float(np.mean(low_asrs)),
                "hypothesis_holds": float(np.mean(high_asrs)) < float(np.mean(low_asrs)),
            },
        }

    out = save_results(all_results, results_dir, tag="step2_keff_contrast")
    logger.info(f"\nStep 2 complete. Results: {out}")


if __name__ == "__main__":
    main()

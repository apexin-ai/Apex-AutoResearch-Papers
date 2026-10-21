#!/usr/bin/env python3
# Step 1: Run evaluation pipeline and compute inter-judge correlations.
# Input: Models loaded via JudgeService, datasets from HuggingFace.
# Output: Pairwise correlation matrix (agreement, MI, copula rho) with CIs.

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import MODEL_REGISTRY, ExperimentConfig
from src.correlation import compute_all_pairwise, validate_cross_vs_within
from src.eval_pipeline import run_full_pipeline
from src.utils import save_results, set_seed, setup_logging

logger = setup_logging("step1")


def main():
    config = ExperimentConfig()
    set_seed(config.seed)

    # Run evaluation pipeline (each judge loaded/unloaded sequentially)
    logger.info(f"Running evaluation with {len(config.model_ids)} judges (serial load/unload)...")
    eval_results = run_full_pipeline(config.model_ids, config)

    # Compute correlations per dataset
    family_map = {mid: MODEL_REGISTRY[mid][2] for mid in MODEL_REGISTRY}
    all_correlation_results = {}

    for ds_name, ds_results in eval_results.items():
        logger.info(f"Computing correlations for {ds_name}...")
        scores = ds_results["scores"]
        pairwise_df = compute_all_pairwise(scores, n_boot=config.n_bootstrap)

        validation = validate_cross_vs_within(pairwise_df, family_map)

        all_correlation_results[ds_name] = {
            "pairwise": pairwise_df.to_dict(orient="records"),
            "validation": validation,
        }

    out = save_results(all_correlation_results, config.results_dir, tag="step1_correlation")
    logger.info(f"Step 1 complete. Results: {out}")


if __name__ == "__main__":
    main()

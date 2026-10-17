#!/usr/bin/env python3
# Step 3: Validate K_eff formula against empirical effective rank.
# Input: Pairwise correlation data from Step 1, panel definitions.
# Output: K_eff formula vs empirical comparison for each panel.

import json
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import ExperimentConfig
from src.keff import validate_keff
from src.panels import generate_all_panels
from src.utils import load_results, save_results, setup_logging

logger = setup_logging("step3")


def main():
    config = ExperimentConfig()

    # Load Step 1 results
    results_dir = config.results_dir
    step1_files = sorted(results_dir.glob("results_step1_correlation_*.json"))
    if not step1_files:
        logger.error("No Step 1 results found. Run step 1 first.")
        sys.exit(1)
    step1_data = load_results(step1_files[-1])
    logger.info(f"Loaded Step 1 results from {step1_files[-1]}")

    all_keff_results = {}
    panels = generate_all_panels()

    # Flatten panels into list of dicts
    panel_defs = []
    for ptype, panel_list in panels.items():
        for panel in panel_list:
            panel_defs.append({
                "judge_ids": panel.judge_ids,
                "panel_type": ptype,
                "k": panel.k,
            })

    for ds_name, ds_data in step1_data.items():
        logger.info(f"=== K_eff validation for {ds_name} ===")
        pairwise_df = pd.DataFrame(ds_data["pairwise"])
        keff_results = validate_keff(pairwise_df, panel_defs)
        all_keff_results[ds_name] = keff_results

    out = save_results(all_keff_results, config.results_dir, tag="step3_keff")
    logger.info(f"Step 3 complete. Results: {out}")


if __name__ == "__main__":
    main()

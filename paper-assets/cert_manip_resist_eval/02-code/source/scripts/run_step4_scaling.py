#!/usr/bin/env python3
# Step 4: Scaling analysis — K_eff vs ASR across panel sizes.
# Input: K_eff data from Step 3, panel ASR from Step 2.
# Output: Spearman rho, log-log regression with CI.

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import ExperimentConfig
from src.scaling import collect_scaling_data, run_scaling_analysis
from src.utils import load_results, save_results, setup_logging

logger = setup_logging("step4")


def main():
    config = ExperimentConfig()
    results_dir = config.results_dir

    # Load Step 2 (attacks) and Step 3 (keff) results
    step2_files = sorted(results_dir.glob("results_step2_attacks_*.json"))
    step3_files = sorted(results_dir.glob("results_step3_keff_*.json"))

    if not step2_files or not step3_files:
        logger.error("Need Step 2 and Step 3 results. Run those steps first.")
        sys.exit(1)

    step2_data = load_results(step2_files[-1])
    step3_data = load_results(step3_files[-1])
    logger.info("Loaded Step 2 and Step 3 results")

    all_scaling_results = {}

    for ds_name in config.datasets:
        if ds_name not in step2_data or ds_name not in step3_data:
            continue

        logger.info(f"=== Scaling analysis for {ds_name} ===")

        # Collect data points across all attacks
        keff_results = step3_data[ds_name]
        panel_attacks = step2_data[ds_name]["panel_attacks"]

        all_data_points = []
        for attack_name, panel_asr in panel_attacks.items():
            # Tag each ASR result with attack name and dataset
            for ptype, results in panel_asr.items():
                for r in results:
                    r["attack_name"] = attack_name
                    r["dataset"] = ds_name

            data_points = collect_scaling_data(panel_asr, keff_results)
            all_data_points.extend(data_points)

        scaling_result = run_scaling_analysis(all_data_points)
        scaling_result["data_points"] = all_data_points
        all_scaling_results[ds_name] = scaling_result

    out = save_results(all_scaling_results, config.results_dir, tag="step4_scaling")
    logger.info(f"Step 4 complete. Results: {out}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# Step 2: Run attack suite on individual judges and panels.
# Input: Clean eval scores from Step 1, attack definitions.
# Output: Per-judge and per-panel ASR for each attack type.

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.attacks import ALL_ATTACKS, apply_attack_to_pairs, measure_asr, run_attack_suite
from src.config import ExperimentConfig
from src.eval_pipeline import generate_response_pairs, load_eval_dataset
from src.judge_service import JudgeService
from src.panels import generate_all_panels, measure_all_panels_asr
from src.utils import save_results, set_seed, setup_logging

logger = setup_logging("step2")


def main():
    config = ExperimentConfig()
    set_seed(config.seed)

    all_attack_results = {}

    for ds_name in config.datasets:
        logger.info(f"=== Attacks on {ds_name} ===")
        samples = load_eval_dataset(ds_name, config.n_samples)
        pairs = generate_response_pairs(samples, ds_name)

        clean_scores = {}
        judge_attack_results = {}
        attacked_scores_by_attack = {attack.name: {} for attack in ALL_ATTACKS}

        # Load each judge sequentially: clean score + all attacks, then unload
        for model_id in config.model_ids:
            logger.info(f"Loading judge {model_id}...")
            judge = JudgeService(model_id).load()

            items = [
                {"question": p["question"], "response_a": p["response_a"], "response_b": p["response_b"]}
                for p in pairs
            ]
            clean_scores[model_id] = judge.batch_score(items)

            logger.info(f"Running attack suite on {model_id}...")
            suite_results = run_attack_suite(judge, pairs, clean_scores[model_id])
            judge_attack_results[model_id] = suite_results

            for attack in ALL_ATTACKS:
                attacked_scores_by_attack[attack.name][model_id] = (
                    suite_results[attack.name]["attacked_scores"]
                )

            judge.unload()
            logger.info(f"  {model_id}: GPU memory released")

        # Panel aggregation (no models needed, just collected scores)
        panels = generate_all_panels()
        panel_attack_results = {}
        for attack in ALL_ATTACKS:
            panel_asr = measure_all_panels_asr(
                panels, clean_scores, attacked_scores_by_attack[attack.name], pairs
            )
            panel_attack_results[attack.name] = panel_asr

        all_attack_results[ds_name] = {
            "judge_attacks": {
                mid: {aname: {"asr": v["asr"], "n_flips": v["n_flips"]} for aname, v in results.items()}
                for mid, results in judge_attack_results.items()
            },
            "panel_attacks": panel_attack_results,
        }

    out = save_results(all_attack_results, config.results_dir, tag="step2_attacks")
    logger.info(f"Step 2 complete. Results: {out}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Plan 001 Step 1: 9 API models × 2 datasets × 7 conditions (1 clean + 6 attacks) × 300 samples."""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_DATASETS_CACHE"] = "/root/autodl-tmp/.hf_cache/datasets"
os.environ["HF_HUB_CACHE"] = "/root/autodl-tmp/.hf_cache/hub"

import sys
sys.path.insert(0, "/root/cert_manip_resist_eval")

import json
import time
import traceback
from pathlib import Path
from datetime import datetime, timezone

from src.api_judge_service import APIJudgeService, API_MODEL_REGISTRY
from src.attacks import (
    PromptInjection, SycophancyExploitation, ScoreManipulation,
    VerbosityBias, PositionBias, AuthorityBias,
    apply_attack_to_pairs, apply_position_attack,
    measure_asr, measure_position_asr,
)
from src.utils import setup_logging

logger = setup_logging("plan001_step1")

API_KEY = "[REDACTED]"
API_BASE = "http://47.94.22.126/v1"

MODEL_IDS = [
    "claude-opus-4", "gpt-5.5", "gemini-2.5-pro",
    "gpt-4.1", "claude-sonnet-4", "gpt-4o",
    "gemini-2.5-flash", "gpt-4o-mini", "claude-3-haiku",
]
DATASETS = ["mmlu", "arc_challenge"]
ATTACK_DEFS = {
    "prompt_injection": PromptInjection(0),
    "sycophancy": SycophancyExploitation(seed=42),
    "score_manipulation": ScoreManipulation(0),
    "verbosity_bias": VerbosityBias(seed=42),
    "position_bias": PositionBias(),
    "authority_bias": AuthorityBias(seed=42),
}
ATTACK_NAMES = list(ATTACK_DEFS.keys())
CONDITIONS = ["clean"] + ATTACK_NAMES

RESULTS_DIR = Path("/root/cert_manip_resist_eval/artifacts/results/plan001")
SCORES_DIR = RESULTS_DIR / "individual_scores"
CKPT_DIR = SCORES_DIR

DRY_RUN = "--dry-run" in sys.argv
N_SAMPLES = 5 if DRY_RUN else 300


def load_pairs():
    ckpt_path = Path("/root/cert_manip_resist_eval/artifacts/results/_taxonomy_checkpoint.json")
    logger.info(f"Loading pairs from {ckpt_path}")
    with open(ckpt_path) as f:
        data = json.load(f)
    pairs = {}
    for ds in DATASETS:
        ds_pairs = data["pairs"][ds][:N_SAMPLES]
        pairs[ds] = ds_pairs
        logger.info(f"  {ds}: {len(ds_pairs)} pairs loaded")
    return pairs


def ckpt_key(model_id, dataset, condition):
    return f"{model_id}__{dataset}__{condition}"


def ckpt_path(model_id, dataset, condition):
    return CKPT_DIR / f"{ckpt_key(model_id, dataset, condition)}.json"


def save_condition_result(model_id, dataset, condition, result):
    CKPT_DIR.mkdir(parents=True, exist_ok=True)
    path = ckpt_path(model_id, dataset, condition)
    with open(path, "w") as f:
        json.dump(result, f, ensure_ascii=False)
    logger.info(f"  Saved checkpoint: {path.name}")


def load_condition_result(model_id, dataset, condition):
    path = ckpt_path(model_id, dataset, condition)
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return None


def is_done(model_id, dataset, condition):
    return ckpt_path(model_id, dataset, condition).exists()


def compute_accuracy(scores, pairs):
    correct = 0
    total = 0
    for s, p in zip(scores, pairs):
        winner = s.get("winner")
        if winner is None:
            continue
        total += 1
        if winner == p["ground_truth_winner"]:
            correct += 1
    return correct / max(total, 1), total


def compute_asr_from_scores(clean_scores, attacked_scores, pairs):
    return measure_asr(clean_scores, attacked_scores, pairs)


def compute_position_asr(clean_scores, attacked_scores, original_pairs, swapped_pairs):
    return measure_position_asr(clean_scores, attacked_scores, original_pairs, swapped_pairs)


def _unwrap_batch(batch_output):
    """batch_score returns {"results": [...], "_meta": {...}}."""
    if isinstance(batch_output, dict) and "results" in batch_output:
        return batch_output["results"]
    return batch_output


def score_condition(judge, pairs, condition):
    if condition == "clean":
        items = [
            {"question": p["question"], "response_a": p["response_a"], "response_b": p["response_b"]}
            for p in pairs
        ]
            return _unwrap_batch(judge.batch_score(items, mode="pairwise", max_workers=5)), pairs

    attack = ATTACK_DEFS[condition]
    if condition == "position_bias":
        attacked_pairs = apply_position_attack(pairs)
    else:
        attacked_pairs = apply_attack_to_pairs(pairs, attack)

    items = [
        {"question": p["question"], "response_a": p["response_a"], "response_b": p["response_b"]}
        for p in attacked_pairs
    ]
    return _unwrap_batch(judge.batch_score(items, mode="pairwise", max_workers=5)), attacked_pairs


def run_model(model_id, all_pairs):
    logger.info(f"=== Model: {model_id} ===")
    judge = APIJudgeService(model_id=model_id, api_base=API_BASE, api_key=[REDACTED], timeout=120)
    model_results = {}

    for ds in DATASETS:
        pairs = all_pairs[ds]
        ds_results = {}

        # Clean first (needed for ASR)
        if is_done(model_id, ds, "clean"):
            logger.info(f"  [{ds}] clean: SKIP (checkpoint exists)")
            clean_result = load_condition_result(model_id, ds, "clean")
        else:
            logger.info(f"  [{ds}] clean: scoring {len(pairs)} pairs...")
            t0 = time.time()
            clean_scores, _ = score_condition(judge, pairs, "clean")
            elapsed = time.time() - t0
            acc, n_valid = compute_accuracy(clean_scores, pairs)
            n_errors = sum(1 for s in clean_scores if "error" in s and s.get("error"))
            clean_result = {
                "condition": "clean",
                "scores": clean_scores,
                "accuracy": round(acc, 4),
                "n_samples": len(pairs),
                "n_valid": n_valid,
                "n_errors": n_errors,
                "elapsed_s": round(elapsed, 1),
            }
            save_condition_result(model_id, ds, "clean", clean_result)
            logger.info(f"  [{ds}] clean: acc={acc:.3f}, errors={n_errors}, time={elapsed:.0f}s")

        ds_results["clean"] = {
            "accuracy": clean_result["accuracy"],
            "n_samples": clean_result["n_samples"],
            "n_errors": clean_result.get("n_errors", 0),
        }
        clean_scores = clean_result["scores"]

        # Attack conditions
        for atk_name in ATTACK_NAMES:
            if is_done(model_id, ds, atk_name):
                logger.info(f"  [{ds}] {atk_name}: SKIP (checkpoint exists)")
                atk_result = load_condition_result(model_id, ds, atk_name)
            else:
                logger.info(f"  [{ds}] {atk_name}: scoring {len(pairs)} pairs...")
                t0 = time.time()
                try:
                    atk_scores, atk_pairs = score_condition(judge, pairs, atk_name)
                    elapsed = time.time() - t0

                    if atk_name == "position_bias":
                        asr = compute_position_asr(clean_scores, atk_scores, pairs, atk_pairs)
                    else:
                        asr = compute_asr_from_scores(clean_scores, atk_scores, pairs)

                    n_errors = sum(1 for s in atk_scores if "error" in s and s.get("error"))
                    atk_result = {
                        "condition": atk_name,
                        "scores": atk_scores,
                        "asr": round(asr, 4),
                        "n_samples": len(pairs),
                        "n_errors": n_errors,
                        "elapsed_s": round(elapsed, 1),
                    }
                    save_condition_result(model_id, ds, atk_name, atk_result)
                    logger.info(f"  [{ds}] {atk_name}: asr={asr:.3f}, errors={n_errors}, time={elapsed:.0f}s")
                except Exception as e:
                    logger.error(f"  [{ds}] {atk_name}: FAILED - {e}")
                    traceback.print_exc()
                    atk_result = {
                        "condition": atk_name,
                        "scores": [],
                        "asr": None,
                        "n_samples": 0,
                        "n_errors": -1,
                        "error": str(e),
                    }
                    save_condition_result(model_id, ds, atk_name, atk_result)

            ds_results[atk_name] = {
                "asr": atk_result.get("asr"),
                "n_samples": atk_result.get("n_samples", 0),
                "n_errors": atk_result.get("n_errors", 0),
            }

        model_results[ds] = ds_results
    return model_results


def build_summary(all_model_results, total_elapsed):
    total_calls = 0
    for model_id, ds_results in all_model_results.items():
        if isinstance(ds_results, dict) and "error" in ds_results:
            continue
        for ds, cond_results in ds_results.items():
            for cond, info in cond_results.items():
                total_calls += info.get("n_samples", 0)

    summary = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "dry_run": DRY_RUN,
        "n_samples_per_condition": N_SAMPLES,
        "models": all_model_results,
        "total_api_calls": total_calls,
        "runtime_minutes": round(total_elapsed / 60, 1),
    }
    return summary


def main():
    logger.info(f"Plan 001 Step 1: API Scoring {'(DRY RUN)' if DRY_RUN else '(FULL RUN)'}")
    logger.info(f"  Models: {len(MODEL_IDS)}, Datasets: {len(DATASETS)}, "
                f"Conditions: {len(CONDITIONS)}, Samples/cond: {N_SAMPLES}")
    logger.info(f"  Total API calls: {len(MODEL_IDS) * len(DATASETS) * len(CONDITIONS) * N_SAMPLES}")

    SCORES_DIR.mkdir(parents=True, exist_ok=True)

    all_pairs = load_pairs()

    # Count already done
    n_total = len(MODEL_IDS) * len(DATASETS) * len(CONDITIONS)
    n_done = sum(1 for m in MODEL_IDS for ds in DATASETS for c in CONDITIONS if is_done(m, ds, c))
    logger.info(f"  Progress: {n_done}/{n_total} model×dataset×condition combos already done")

    all_model_results = {}
    t_start = time.time()

    for model_id in MODEL_IDS:
        try:
            model_results = run_model(model_id, all_pairs)
            all_model_results[model_id] = model_results
        except Exception as e:
            logger.error(f"=== Model {model_id} FAILED: {e} ===")
            traceback.print_exc()
            all_model_results[model_id] = {"error": str(e)}

    total_elapsed = time.time() - t_start

    summary = build_summary(all_model_results, total_elapsed)
    summary_path = RESULTS_DIR / "step1_api_scoring_summary.json"
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    logger.info(f"Summary saved to {summary_path}")
    logger.info(f"Total runtime: {total_elapsed/60:.1f} minutes")

    # Print summary table
    print("\n" + "=" * 80)
    print("RESULTS SUMMARY")
    print("=" * 80)
    for model_id, ds_results in all_model_results.items():
        if isinstance(ds_results, dict) and "error" in ds_results:
            print(f"\n{model_id}: ERROR - {ds_results['error']}")
            continue
        print(f"\n{model_id}:")
        for ds in DATASETS:
            if ds not in ds_results:
                continue
            conds = ds_results[ds]
            clean_acc = conds.get("clean", {}).get("accuracy", "N/A")
            print(f"  {ds}: clean_acc={clean_acc}", end="")
            for atk in ATTACK_NAMES:
                asr = conds.get(atk, {}).get("asr", "N/A")
                if asr is not None and isinstance(asr, float):
                    print(f"  {atk}={asr:.3f}", end="")
                else:
                    print(f"  {atk}={asr}", end="")
            print()
    print("=" * 80)


if __name__ == "__main__":
    main()

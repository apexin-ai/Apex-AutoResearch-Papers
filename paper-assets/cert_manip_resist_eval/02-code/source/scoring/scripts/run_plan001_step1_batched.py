#!/usr/bin/env python3
"""Plan 001 Step 1 (BATCHED): Provider-serial execution with conservative throttling."""

import argparse
import os
import sys

_SCORING_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _SCORING_ROOT)

import json
import time
import traceback
import threading
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed

from src.api_judge_service import APIJudgeService, API_MODEL_REGISTRY
from src.attacks import (
    PromptInjection, SycophancyExploitation, ScoreManipulation,
    VerbosityBias, PositionBias, AuthorityBias,
    apply_attack_to_pairs, apply_position_attack,
    measure_asr, measure_position_asr,
)
from src.utils import setup_logging

logger = setup_logging("plan001_step1_batched")

API_KEY = [REDACTED]"OPENROUTER_API_KEY", "")
API_BASE = "https://openrouter.ai/api/v1"

BATCHES = [
    {
        "name": "Claude",
        "models": ["claude-opus-4-6", "claude-sonnet-4-6", "claude-3-haiku"],
        "max_workers": 15,
        "max_rps": 10.0,
    },
    {
        "name": "Gemini",
        "models": ["gemini-3.1-pro-preview", "gemini-3.5-flash"],
        "max_workers": 15,
        "max_rps": 10.0,
    },
    {
        "name": "OpenAI",
        "models": ["gpt-4.1-mini", "gpt-4.1-nano", "gpt-4.1", "gpt-5.5"],
        "max_workers": 15,
        "max_rps": 10.0,
    },
]

DATASETS = ["mmlu", "arc_challenge"]
ATTACK_NAMES = [
    "prompt_injection", "sycophancy", "score_manipulation",
    "verbosity_bias", "position_bias", "authority_bias",
]
CONDITIONS = ["clean"] + ATTACK_NAMES

RESULTS_DIR = Path(_SCORING_ROOT) / "results" / "plan001"
SCORES_DIR = RESULTS_DIR / "individual_scores"
CKPT_DIR = SCORES_DIR

BATCH_NAME_MAP = {b["name"].lower(): b["name"] for b in BATCHES}

def parse_args():
    parser = argparse.ArgumentParser(description="Plan 001 Step 1 batched scoring")
    parser.add_argument("--batch", choices=list(BATCH_NAME_MAP.keys()) + ["all"],
                        default="all", help="Which provider batch to run")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()

ARGS = parse_args()
DRY_RUN = ARGS.dry_run
N_SAMPLES = 5 if DRY_RUN else 300

_503_counter = 0
_503_lock = threading.Lock()


def make_attack_defs():
    return {
        "prompt_injection": PromptInjection(0),
        "sycophancy": SycophancyExploitation(seed=42),
        "score_manipulation": ScoreManipulation(0),
        "verbosity_bias": VerbosityBias(seed=42),
        "position_bias": PositionBias(),
        "authority_bias": AuthorityBias(seed=42),
    }


def load_pairs():
    ckpt_path = Path(_SCORING_ROOT) / "data" / "_taxonomy_checkpoint.json"
    logger.info(f"Loading pairs from {ckpt_path}")
    with open(ckpt_path) as f:
        data = json.load(f)
    pairs = {}
    for ds in DATASETS:
        ds_pairs = data["pairs"][ds][:N_SAMPLES]
        pairs[ds] = ds_pairs
        logger.info(f"  {ds}: {len(ds_pairs)} pairs loaded")
    return pairs


def ckpt_path_fn(model_id, dataset, condition):
    return CKPT_DIR / f"{model_id}__{dataset}__{condition}.json"


def save_condition_result(model_id, dataset, condition, result):
    CKPT_DIR.mkdir(parents=True, exist_ok=True)
    path = ckpt_path_fn(model_id, dataset, condition)
    with open(path, "w") as f:
        json.dump(result, f, ensure_ascii=False)
    logger.info(f"  [{model_id}] Saved: {path.name}")


def load_condition_result(model_id, dataset, condition):
    path = ckpt_path_fn(model_id, dataset, condition)
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return None


def is_done(model_id, dataset, condition):
    path = ckpt_path_fn(model_id, dataset, condition)
    if not path.exists():
        return False
    try:
        with open(path) as f:
            data = json.load(f)
        if data.get("n_samples", 0) < N_SAMPLES:
            return False
        if data.get("n_errors", 0) == data.get("n_samples", 0):
            return False
        return True
    except Exception:
        return False


def compute_accuracy(scores, pairs):
    correct = 0
    total = 0
    for s, p in zip(scores, pairs):
        if not isinstance(s, dict):
            continue
        winner = s.get("winner")
        if winner is None:
            continue
        total += 1
        if winner == p["ground_truth_winner"]:
            correct += 1
    return correct / max(total, 1), total


def _unwrap_batch(batch_output):
    if isinstance(batch_output, dict) and "results" in batch_output:
        return batch_output["results"]
    return batch_output


def score_condition(judge, pairs, condition, attack_defs, max_workers):
    if condition == "clean":
        items = [
            {"question": p["question"], "response_a": p["response_a"], "response_b": p["response_b"]}
            for p in pairs
        ]
        return _unwrap_batch(judge.batch_score(items, mode="pairwise", max_workers=max_workers)), pairs

    attack = attack_defs[condition]
    if condition == "position_bias":
        attacked_pairs = apply_position_attack(pairs)
    else:
        attacked_pairs = apply_attack_to_pairs(pairs, attack)

    items = [
        {"question": p["question"], "response_a": p["response_a"], "response_b": p["response_b"]}
        for p in attacked_pairs
    ]
    return _unwrap_batch(judge.batch_score(items, mode="pairwise", max_workers=max_workers)), attacked_pairs


def run_model(model_id, all_pairs, max_workers, max_rps):
    tag = f"[{model_id}]"
    logger.info(f"=== {tag} Starting (workers={max_workers}, rps={max_rps}) ===")

    attack_defs = make_attack_defs()
    judge = APIJudgeService(
        model_id=model_id, api_base=API_BASE, api_key=[REDACTED],
        max_rps=max_rps, max_retries=8, timeout=120,
    )
    model_results = {}

    for ds in DATASETS:
        pairs = all_pairs[ds]
        ds_results = {}

        if is_done(model_id, ds, "clean"):
            logger.info(f"  {tag}[{ds}] clean: SKIP")
            clean_result = load_condition_result(model_id, ds, "clean")
        else:
            logger.info(f"  {tag}[{ds}] clean: scoring {len(pairs)} pairs...")
            t0 = time.time()
            clean_scores, _ = score_condition(judge, pairs, "clean", attack_defs, max_workers)
            elapsed = time.time() - t0
            acc, n_valid = compute_accuracy(clean_scores, pairs)
            n_errors = sum(1 for s in clean_scores if isinstance(s, dict) and s.get("error"))
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
            logger.info(f"  {tag}[{ds}] clean: acc={acc:.3f}, errors={n_errors}, time={elapsed:.0f}s")

        ds_results["clean"] = {
            "accuracy": clean_result["accuracy"],
            "n_samples": clean_result["n_samples"],
            "n_errors": clean_result.get("n_errors", 0),
        }
        clean_scores = clean_result["scores"]

        for atk_name in ATTACK_NAMES:
            if is_done(model_id, ds, atk_name):
                logger.info(f"  {tag}[{ds}] {atk_name}: SKIP")
                atk_result = load_condition_result(model_id, ds, atk_name)
            else:
                logger.info(f"  {tag}[{ds}] {atk_name}: scoring {len(pairs)} pairs...")
                t0 = time.time()
                try:
                    atk_scores, atk_pairs = score_condition(judge, pairs, atk_name, attack_defs, max_workers)
                    elapsed = time.time() - t0

                    if atk_name == "position_bias":
                        asr = measure_position_asr(clean_scores, atk_scores, pairs, atk_pairs)
                    else:
                        asr = measure_asr(clean_scores, atk_scores, pairs)

                    n_errors = sum(1 for s in atk_scores if isinstance(s, dict) and s.get("error"))
                    asr_val = round(asr, 4) if isinstance(asr, (int, float)) else asr
                    atk_result = {
                        "condition": atk_name,
                        "scores": atk_scores,
                        "asr": asr_val,
                        "n_samples": len(pairs),
                        "n_errors": n_errors,
                        "elapsed_s": round(elapsed, 1),
                    }
                    save_condition_result(model_id, ds, atk_name, atk_result)
                    asr_str = f"{asr:.4f}" if isinstance(asr, (int, float)) else str(asr)
                    logger.info(f"  {tag}[{ds}] {atk_name}: asr={asr_str}, errors={n_errors}, time={elapsed:.0f}s")
                except Exception as e:
                    logger.error(f"  {tag}[{ds}] {atk_name}: FAILED - {e}")
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


def main():
    logger.info(f"Plan 001 Step 1 BATCHED v2: {'(DRY RUN)' if DRY_RUN else '(FULL RUN)'}")
    logger.info(f"  Datasets: {DATASETS}, Conditions: {len(CONDITIONS)}, Samples/cond: {N_SAMPLES}")

    SCORES_DIR.mkdir(parents=True, exist_ok=True)
    all_pairs = load_pairs()

    if ARGS.batch == "all":
        active_batches = BATCHES
    else:
        target = BATCH_NAME_MAP[ARGS.batch]
        active_batches = [b for b in BATCHES if b["name"] == target]

    all_models = [m for b in active_batches for m in b["models"]]
    n_total = len(all_models) * len(DATASETS) * len(CONDITIONS)
    n_done = sum(1 for m in all_models for ds in DATASETS for c in CONDITIONS if is_done(m, ds, c))
    logger.info(f"  Batch filter: {ARGS.batch} → {[b['name'] for b in active_batches]}")
    logger.info(f"  Progress: {n_done}/{n_total} already done, {n_total - n_done} remaining")

    all_model_results = {}
    t_start = time.time()

    for batch in active_batches:
        batch_name = batch["name"]
        models = batch["models"]
        max_workers = batch["max_workers"]
        max_rps = batch["max_rps"]

        remaining = sum(
            1 for m in models for ds in DATASETS for c in CONDITIONS if not is_done(m, ds, c)
        )
        if remaining == 0:
            logger.info(f"\n{'='*60}")
            logger.info(f"BATCH {batch_name}: ALL DONE, skipping")
            continue

        logger.info(f"\n{'='*60}")
        logger.info(f"BATCH {batch_name}: {len(models)} models, workers={max_workers}, rps={max_rps}, {remaining} conditions remaining")
        logger.info(f"{'='*60}")

        for model_id in models:
            m_remaining = sum(1 for ds in DATASETS for c in CONDITIONS if not is_done(model_id, ds, c))
            if m_remaining == 0:
                logger.info(f"  {model_id}: all done, skipping")
                continue

            logger.info(f"  {model_id}: {m_remaining} conditions to score")
            try:
                result = run_model(model_id, all_pairs, max_workers, max_rps)
                all_model_results[model_id] = result
                elapsed_so_far = time.time() - t_start
                logger.info(f"=== {model_id} COMPLETED ({elapsed_so_far/60:.1f} min elapsed) ===")
            except Exception as e:
                logger.error(f"=== {model_id} FAILED: {e} ===")
                traceback.print_exc()
                all_model_results[model_id] = {"error": str(e)}

    total_elapsed = time.time() - t_start

    summary = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "dry_run": DRY_RUN,
        "n_samples_per_condition": N_SAMPLES,
        "models": all_model_results,
        "runtime_minutes": round(total_elapsed / 60, 1),
        "batched": True,
        "batch_filter": ARGS.batch,
        "batches": [{k: v for k, v in b.items()} for b in active_batches],
    }
    summary_path = RESULTS_DIR / "step1_batched_summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    logger.info(f"Summary saved to {summary_path}")
    logger.info(f"Total runtime: {total_elapsed/60:.1f} minutes")

    print("\n" + "=" * 80)
    print("RESULTS SUMMARY")
    print("=" * 80)
    for batch in active_batches:
        for mid in batch["models"]:
            ds_results = all_model_results.get(mid, {})
            if isinstance(ds_results, dict) and "error" in ds_results:
                print(f"\n{mid}: ERROR - {ds_results['error']}")
                continue
            if not ds_results:
                print(f"\n{mid}: (skipped, already done)")
                continue
            print(f"\n{mid}:")
            for ds in DATASETS:
                if ds not in ds_results:
                    continue
                conds = ds_results[ds]
                clean_acc = conds.get("clean", {}).get("accuracy", "N/A")
                print(f"  {ds}: clean_acc={clean_acc}", end="")
                for atk in ATTACK_NAMES:
                    asr = conds.get(atk, {}).get("asr", "N/A")
                    if isinstance(asr, (int, float)):
                        print(f"  {atk}={asr:.3f}", end="")
                    else:
                        print(f"  {atk}={asr}", end="")
                print()
    print("=" * 80)


if __name__ == "__main__":
    main()

"""Few-shot vs zero-shot BCS comparison experiment (FewRel 80-rel).

Tests whether 1-shot / 5-shot demonstrations mitigate the confusability effect.
Reuses exp_fewrel_formal_80rel exp2 BCS-controlled batch design (same type combos).

Conditions: 0-shot (control), 1-shot, 5-shot
Count levels: count_8, count_16
BCS levels: low_bcs, high_bcs per count level

Usage:
    python3 scripts/run_fewshot_bcs_experiment.py            # full run
    python3 scripts/run_fewshot_bcs_experiment.py --dry_run   # verify prompts only
"""

import argparse
import json
import logging
import random
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

logger = logging.getLogger(__name__)

BASE_DIR = Path("/root/schema-dag-extraction")
MODEL_PATH = "/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/"
BATCH_CONFIG_PATH = BASE_DIR / "artifacts/fewrel_formal/batch_config_exp2.json"
TYPES_FILE = BASE_DIR / "configs/fewrel_relation_types.json"
OUTPUT_DIR = BASE_DIR / "artifacts/fewshot_bcs"

SHOT_CONDITIONS = [0, 1, 5]
COUNT_LEVELS = ["count_8", "count_16"]
BCS_LEVELS = ["low_bcs", "high_bcs"]
SEED = 42
MAX_MODEL_LEN = 8192
GPU_MEM_UTIL = 0.90


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_fewrel_raw(json_path, pid2name):
    """Load FewRel raw JSON (train_wiki.json / val_wiki.json) into flat records."""
    with open(json_path) as f:
        data = json.load(f)
    records = []
    for pid, examples in data.items():
        rel_name = pid2name.get(pid, pid)
        for ex in examples:
            text = " ".join(ex["tokens"])
            records.append({
                "text": text,
                "head_entity": ex["h"][0],
                "tail_entity": ex["t"][0],
                "relation_type": rel_name,
                "relation_pid": pid,
            })
    return records


def build_demo_pool(pid2name, exclude_texts):
    """Load demonstration pool from raw FewRel JSONs, excluding test samples."""
    pool = []
    for fname in ["train_wiki.json", "val_wiki.json"]:
        fpath = BASE_DIR / "data/fewrel" / fname
        if fpath.exists():
            pool.extend(load_fewrel_raw(str(fpath), pid2name))
    before = len(pool)
    pool = [r for r in pool if r["text"] not in exclude_texts]
    logger.info("Demo pool: %d samples (%d excluded as test overlap)", len(pool), before - len(pool))
    return pool


def sample_demonstrations(demo_pool, relation_types, k, seed=42):
    """Sample k demonstrations per relation type. Returns {rel_type: [demo_dicts]}."""
    rng = random.Random(seed)
    by_rel = defaultdict(list)
    for s in demo_pool:
        if s["relation_type"] in relation_types:
            by_rel[s["relation_type"]].append(s)
    result = {}
    for rel in sorted(relation_types):
        candidates = by_rel.get(rel, [])
        if not candidates:
            logger.warning("No demos available for relation: %s", rel)
            result[rel] = []
            continue
        result[rel] = rng.sample(candidates, min(k, len(candidates)))
    return result


# ---------------------------------------------------------------------------
# Prompt construction
# ---------------------------------------------------------------------------

def build_fewshot_prompt(sentence, head, tail, relation_types, demos):
    """Build RE classification prompt with optional few-shot demonstrations.

    When demos is empty, produces the same prompt as build_prompt_v2_re
    from run_extraction.py (ensures 0-shot control matches formal experiment).
    """
    candidates = ", ".join(sorted(relation_types))

    if demos:
        parts = [
            "Given the following sentence and two entities, "
            "classify the relation between them.\n\n"
            f"Candidate relations: {candidates}\n\n"
            "Examples:\n"
        ]
        for d in demos:
            parts.append(
                f'Sentence: "{d["text"]}" '
                f'Head: "{d["head_entity"]}" '
                f'Tail: "{d["tail_entity"]}" '
                f'-> {d["relation_type"]}\n'
            )
        parts.append(
            f'\nNow classify:\n'
            f'Sentence: "{sentence}"\n'
            f'Head entity: "{head}"\n'
            f'Tail entity: "{tail}"\n\n'
            'Output a single JSON object: {"relation": "<relation_type>"}\n'
            'If none of the candidate relations apply, output: {"relation": "none"}'
        )
    else:
        parts = [
            "Given the following sentence and two entities, "
            "classify the relation between them.\n\n"
            f'Sentence: "{sentence}"\n'
            f'Head entity: "{head}"\n'
            f'Tail entity: "{tail}"\n\n'
            f"Candidate relations: {candidates}\n\n"
            'Output a single JSON object: {"relation": "<relation_type>"}\n'
            'If none of the candidate relations apply, output: {"relation": "none"}'
        ]

    return "".join(parts)


# ---------------------------------------------------------------------------
# Evaluation (matches run_fewrel_formal.py evaluate_re)
# ---------------------------------------------------------------------------

def evaluate_re(results):
    """Per-batch accuracy with per-type breakdown."""
    batch_stats = defaultdict(lambda: {
        "correct": 0, "total": 0,
        "per_type": defaultdict(lambda: {"correct": 0, "total": 0}),
    })
    meta = {}

    for r in results:
        bid = r["batch_id"]
        s = batch_stats[bid]
        s["total"] += 1
        gold = r["ground_truth"]
        pred = r["prediction"]
        s["per_type"][gold]["total"] += 1
        if pred == gold:
            s["correct"] += 1
            s["per_type"][gold]["correct"] += 1
        if bid not in meta:
            meta[bid] = {
                "bcs": r["batch_bcs"], "count_key": r["count_key"],
                "num_types": len(r["batch_types"]), "batch_types": r["batch_types"],
                "shot": r.get("shot", 0), "bcs_level": r.get("bcs_level", ""),
            }

    out = {}
    for bid, s in batch_stats.items():
        per_type_acc = {}
        for t, ts in s["per_type"].items():
            per_type_acc[t] = {
                "accuracy": ts["correct"] / ts["total"] if ts["total"] else 0.0,
                "correct": ts["correct"], "total": ts["total"],
            }
        out[bid] = {
            "accuracy": s["correct"] / s["total"] if s["total"] else 0.0,
            "correct": s["correct"], "total": s["total"],
            "per_type_accuracy": per_type_acc,
            **meta[bid],
        }
    return out


# ---------------------------------------------------------------------------
# Preprocess stage (CPU only)
# ---------------------------------------------------------------------------

def stage_preprocess(args):
    """Load data, build demonstrations, save config JSON for GPU stage."""
    sys.path.insert(0, str(BASE_DIR / "src"))
    from fewrel_utils import load_fewrel, sample_balanced

    with open(TYPES_FILE) as f:
        pid2name = json.load(f)

    with open(BATCH_CONFIG_PATH) as f:
        full_batch_config = json.load(f)

    # Keep only low_bcs + high_bcs for count_8 and count_16
    batch_config = {}
    for ck in COUNT_LEVELS:
        batch_config[ck] = {}
        for bl in BCS_LEVELS:
            if bl in full_batch_config[ck]:
                batch_config[ck][bl] = full_batch_config[ck][bl]

    # Load test samples (identical to formal experiment: both parquets, balanced 12/rel)
    all_samples = []
    for dp in ["data/fewrel_parquet/train.parquet", "data/fewrel_parquet/val.parquet"]:
        all_samples.extend(load_fewrel(data_path=str(BASE_DIR / dp)))
    all_relations = sorted(set(s["relation_type"] for s in all_samples))
    n_per = 1000 // len(all_relations)
    random.seed(SEED)
    samples = sample_balanced(all_samples, n_per, seed=SEED)
    logger.info("Test samples: %d (%d relations, %d per rel)", len(samples), len(all_relations), n_per)

    # Collect all relation types used across BCS batches
    all_batch_types = set()
    for ck_cfg in batch_config.values():
        for bl_cfg in ck_cfg.values():
            all_batch_types.update(bl_cfg["types"])
    logger.info("Unique batch types: %d", len(all_batch_types))

    # Build demo pool (exclude test samples by text)
    test_texts = set(s["text"] for s in samples)
    demo_pool = build_demo_pool(pid2name, test_texts)

    # Sample demonstrations for each shot condition (max k=5)
    # Demos are consistent across batches: same 5 examples for "spouse" in every batch
    demos_by_shot = {"0": {}}
    for k in [1, 5]:
        demos_by_shot[str(k)] = sample_demonstrations(demo_pool, all_batch_types, k, seed=SEED)

    # Relation defs (name -> name, same as formal experiment)
    relation_defs = {name: name for name in pid2name.values()}

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    config = {
        "batch_config": batch_config,
        "samples": samples,
        "demos_by_shot": demos_by_shot,
        "relation_defs": relation_defs,
        "model_path": MODEL_PATH,
        "max_model_len": MAX_MODEL_LEN,
        "gpu_memory_utilization": GPU_MEM_UTIL,
    }
    preprocess_path = OUTPUT_DIR / "preprocess.json"
    with open(preprocess_path, "w") as f:
        json.dump(config, f, ensure_ascii=False)
    logger.info("Saved preprocess config to %s", preprocess_path)

    # Print summary and prompt length estimates
    total_inferences = 0
    for ck in COUNT_LEVELS:
        for bl in BCS_LEVELS:
            bl_cfg = batch_config[ck][bl]
            type_set = set(bl_cfg["types"])
            n_batch = len([s for s in samples if s["relation_type"] in type_set])
            total_inferences += n_batch * len(SHOT_CONDITIONS)
            logger.info("  %s_%s: %d types, BCS=%.4f, %d test samples",
                        ck, bl, len(bl_cfg["types"]), bl_cfg["bcs"], n_batch)

    logger.info("Total inferences: %d (3 shots x %d batches)", total_inferences, len(COUNT_LEVELS) * len(BCS_LEVELS))
    est_sec = 0.25
    logger.info("Estimated time: ~%.0f min (@%.2fs/sample)", total_inferences * est_sec / 60, est_sec)

    # Prompt length check for the largest case (5-shot, count_16)
    for shot in SHOT_CONDITIONS:
        for ck in COUNT_LEVELS:
            bl_cfg = batch_config[ck]["high_bcs"]
            batch_types = bl_cfg["types"]
            batch_demos = []
            if shot > 0:
                for rt in sorted(batch_types):
                    batch_demos.extend(demos_by_shot[str(shot)].get(rt, []))
            test_sample = next(s for s in samples if s["relation_type"] in set(batch_types))
            prompt = build_fewshot_prompt(
                test_sample["text"], test_sample["head_entity"],
                test_sample["tail_entity"], batch_types, batch_demos,
            )
            est_tokens = len(prompt) // 3
            logger.info("  Prompt length %d-shot %s: %d chars (~%d tokens), %d demos",
                        shot, ck, len(prompt), est_tokens, len(batch_demos))
            if est_tokens > MAX_MODEL_LEN - 100:
                logger.warning("  WARNING: prompt may exceed max_model_len=%d!", MAX_MODEL_LEN)

    return str(preprocess_path)


# ---------------------------------------------------------------------------
# Extract stage (GPU, vLLM)
# ---------------------------------------------------------------------------

def stage_extract(args):
    """GPU stage: load vLLM, run inference for all shot x batch conditions."""
    from vllm import LLM, SamplingParams
    from vllm.sampling_params import StructuredOutputsParams

    sys.path.insert(0, str(BASE_DIR / "src"))
    from run_extraction import build_json_schema_re

    with open(args.preprocess_path) as f:
        config = json.load(f)

    batch_config = config["batch_config"]
    samples = config["samples"]
    demos_by_shot = config["demos_by_shot"]

    llm = LLM(
        model=config["model_path"],
        max_model_len=config["max_model_len"],
        trust_remote_code=True,
        dtype="bfloat16",
        gpu_memory_utilization=config["gpu_memory_utilization"],
        enforce_eager=True,
        disable_log_stats=True,
    )

    all_results = []

    for shot in SHOT_CONDITIONS:
        shot_demos = demos_by_shot.get(str(shot), {})

        for count_key in COUNT_LEVELS:
            for bcs_level in BCS_LEVELS:
                bl_cfg = batch_config[count_key][bcs_level]
                batch_types = bl_cfg["types"]
                batch_bcs = bl_cfg["bcs"]
                full_bid = f"{count_key}_{bcs_level}_{shot}shot"

                type_set = set(batch_types)
                batch_samples = [(i, s) for i, s in enumerate(samples) if s["relation_type"] in type_set]
                if not batch_samples:
                    logger.warning("No samples for %s", full_bid)
                    continue

                # Gather demos for this batch's relation types
                batch_demo_list = []
                if shot > 0:
                    for rt in sorted(batch_types):
                        batch_demo_list.extend(shot_demos.get(rt, []))

                logger.info("Batch %s: %d types, BCS=%.4f, %d samples, %d demos",
                            full_bid, len(batch_types), batch_bcs, len(batch_samples), len(batch_demo_list))

                schema = build_json_schema_re(batch_types)
                structured = StructuredOutputsParams(json=schema)
                sampling_params = SamplingParams(
                    max_tokens=64, temperature=0.0, structured_outputs=structured,
                )

                prompts = []
                sample_refs = []
                for idx, s in batch_samples:
                    p = build_fewshot_prompt(
                        s["text"], s["head_entity"], s["tail_entity"],
                        batch_types, batch_demo_list,
                    )
                    prompts.append(p)
                    sample_refs.append((idx, s))

                t0 = time.time()
                outputs = llm.generate(prompts, sampling_params)
                elapsed = time.time() - t0

                for oi, output in enumerate(outputs):
                    idx, s = sample_refs[oi]
                    gen_text = output.outputs[0].text
                    try:
                        parsed = json.loads(gen_text)
                        pred_rel = parsed.get("relation", "none")
                    except json.JSONDecodeError:
                        pred_rel = "none"

                    all_results.append({
                        "sample_idx": idx,
                        "batch_id": full_bid,
                        "count_key": count_key,
                        "bcs_level": bcs_level,
                        "shot": shot,
                        "batch_types": batch_types,
                        "batch_bcs": batch_bcs,
                        "prediction": pred_rel,
                        "ground_truth": s["relation_type"],
                        "head_entity": s["head_entity"],
                        "tail_entity": s["tail_entity"],
                        "prompt_tokens": len(output.prompt_token_ids),
                        "gen_tokens": len(output.outputs[0].token_ids),
                        "latency_s": elapsed / len(prompts),
                    })

                logger.info("  Done: %.1fs (%.2fs/sample)", elapsed, elapsed / len(batch_samples))

    # Save raw predictions
    pred_path = OUTPUT_DIR / "predictions.json"
    with open(pred_path, "w") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    logger.info("Saved %d predictions to %s", len(all_results), pred_path)

    # Evaluate
    eval_results = evaluate_re(all_results)
    eval_path = OUTPUT_DIR / "eval_results.json"
    with open(eval_path, "w") as f:
        json.dump(eval_results, f, indent=2)

    # Print results table
    logger.info("=" * 80)
    logger.info("RESULTS SUMMARY")
    logger.info("=" * 80)
    logger.info("%-35s %6s %8s %6s %6s", "batch_id", "shot", "accuracy", "n", "BCS")
    logger.info("-" * 80)
    for bid in sorted(eval_results.keys()):
        m = eval_results[bid]
        logger.info("%-35s %6d %8.4f %6d %6.4f",
                     bid, m["shot"], m["accuracy"], m["total"], m["bcs"])

    # BCS effect summary (high - low accuracy gap)
    logger.info("")
    logger.info("BCS EFFECT (high_bcs_acc - low_bcs_acc):")
    for shot in SHOT_CONDITIONS:
        for ck in COUNT_LEVELS:
            low_bid = f"{ck}_low_bcs_{shot}shot"
            high_bid = f"{ck}_high_bcs_{shot}shot"
            if low_bid in eval_results and high_bid in eval_results:
                gap = eval_results[high_bid]["accuracy"] - eval_results[low_bid]["accuracy"]
                logger.info("  %d-shot %s: gap=%.4f (low=%.4f, high=%.4f)",
                            shot, ck, gap,
                            eval_results[low_bid]["accuracy"],
                            eval_results[high_bid]["accuracy"])


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Few-shot vs zero-shot BCS experiment (FewRel 80-rel)")
    parser.add_argument("--dry_run", action="store_true", help="Preprocess only, no GPU")
    parser.add_argument("--stage", choices=["preprocess", "extract", "all"], default="all",
                        help="preprocess=CPU only, extract=GPU only, all=both (subprocess)")
    parser.add_argument("--preprocess_path", default=None,
                        help="Path to preprocess JSON (for --stage extract)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    if args.stage == "preprocess":
        stage_preprocess(args)
    elif args.stage == "extract":
        if not args.preprocess_path:
            args.preprocess_path = str(OUTPUT_DIR / "preprocess.json")
        stage_extract(args)
    elif args.stage == "all":
        preprocess_path = stage_preprocess(args)
        if args.dry_run:
            logger.info("DRY RUN complete. No GPU stage launched.")
            return
        logger.info("=== Launching extract subprocess (vLLM-first) ===")
        cmd = [sys.executable, str(Path(__file__).resolve()),
               "--stage", "extract",
               "--preprocess_path", preprocess_path]
        subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()

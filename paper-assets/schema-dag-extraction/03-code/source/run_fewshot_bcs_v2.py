#!/usr/bin/env python3
# Few-shot BCS mitigation with pre-computed extreme batch configs.
#
# Why: The original run_fewshot_bcs.py generated batches from a random pool of
# only 60 samples, yielding BCS contrast of ~0.04 (useless). This v2 uses the
# validated extreme batches from exp_fewrel_v2_n25 (count=8: low~0.36, high~0.80,
# known 0-shot delta ~25pp) and generates count=16 extremes from a 5000-sample pool.
#
# Batch config source: artifacts/exp_v2_re_n25/batch_groups.json (25 low + 25 high)
#
# Design:
#   n_shots: 0, 1, 5
#   counts: 8 (from pre-computed), 16 (from large random pool)
#   n_batches: 25 per BCS group
#   Data: FewRel 80-rel (train+val), test=12/rel, fewshot=remaining

import os
os.environ["FLASHINFER_DISABLE_VERSION_CHECK"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import argparse
import json
import logging
import random
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np

logger = logging.getLogger(__name__)

BASE_DIR = Path("/root/schema-dag-extraction")
OUTPUT_DIR = BASE_DIR / "artifacts" / "fewshot_bcs_v2"
DEFAULT_COUNTS = [8, 16]
DEFAULT_N_SHOTS = [0, 1, 5]
DEFAULT_N_BATCHES = 25
N_RANDOM_POOL_LARGE = 5000
DEFAULT_N_SAMPLES = 1000
MODEL_PATH = "/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/"

PRECOMPUTED_BATCH_PATH = BASE_DIR / "artifacts/exp_v2_re_n25/batch_groups.json"


def load_sim_data():
    """Load precomputed Qwen3 similarity matrix for FewRel 80 relations."""
    import torch
    path = BASE_DIR / "artifacts/fewrel_formal_full/relation_sim_matrix.pt"
    data = torch.load(str(path), map_location="cpu", weights_only=True)
    sim_matrix = data.get("sim_matrix", data.get("similarity_matrix"))
    type_names = data["type_names"]
    type_to_idx = data.get("type_to_idx", {n: i for i, n in enumerate(type_names)})
    return sim_matrix, type_names, type_to_idx


def load_precomputed_batches(count):
    """Load pre-computed extreme batches for count=8 from exp_v2_re_n25."""
    with open(PRECOMPUTED_BATCH_PATH) as f:
        data = json.load(f)
    low_group = data["low"]
    high_group = data["high"]
    n_types = len(low_group[0]["types"])
    if n_types != count:
        raise ValueError(
            f"Pre-computed batches have {n_types} types, expected {count}")
    return low_group, high_group


def generate_extreme_batches_large_pool(count, n_batches, sim_matrix, type_names, type_to_idx, seed):
    """Generate extreme batches by sampling a large pool and taking bottom/top N.

    Unlike the original which used pool=60 (insufficient contrast),
    this uses pool=5000 to capture true BCS distribution tails.
    """
    sys.path.insert(0, str(BASE_DIR / "src"))
    from select_type_batches import select_random_batches

    logger.info("Generating %d random batches for count=%d (large pool)...",
                N_RANDOM_POOL_LARGE, count)
    all_batches = select_random_batches(count, N_RANDOM_POOL_LARGE, type_names,
                                        sim_matrix, type_to_idx, seed)
    all_batches.sort(key=lambda x: x["bcs"])

    low_group = all_batches[:n_batches]
    high_group = all_batches[-n_batches:]
    return low_group, high_group


def build_fewshot_prompt(sentence, head, tail, batch_types, fewshot_examples, n_shots):
    """Build RE prompt with few-shot demonstrations.

    Uses ALL fewshot_examples (n_shots per type), not just first n_shots.
    The original had a bug: fewshot_examples[:n_shots] truncated to only n_shots
    total examples instead of n_shots * n_types.
    """
    candidates = ", ".join(sorted(batch_types))

    parts = [
        "Given the following sentence and two entities, "
        "classify the relation between them.\n\n"
        f"Candidate relations: {candidates}\n"
    ]

    if n_shots > 0 and fewshot_examples:
        parts.append("\nExamples:\n")
        for ex in fewshot_examples:
            parts.append(
                f'Sentence: "{ex["text"]}"\n'
                f'Head entity: "{ex["head_entity"]}"\n'
                f'Tail entity: "{ex["tail_entity"]}"\n'
                f'Relation: {ex["relation_type"]}\n\n'
            )
        parts.append("Now classify:\n")

    parts.append(
        f'Sentence: "{sentence}"\n'
        f'Head entity: "{head}"\n'
        f'Tail entity: "{tail}"\n\n'
        'Output a single JSON object: {"relation": "<relation_type>"}\n'
        'If none of the candidate relations apply, output: {"relation": "none"}'
    )
    return "".join(parts)


def select_fewshot_examples(fewshot_pool_by_rel, batch_types, n_shots, rng):
    """Select balanced few-shot examples: n_shots per relation type in the batch."""
    examples = []
    for rel in sorted(batch_types):
        pool = fewshot_pool_by_rel.get(rel, [])
        k = min(n_shots, len(pool))
        if k > 0:
            examples.extend(rng.sample(pool, k))
    return examples


def stage_preprocess(args):
    """CPU stage: load/generate batch configs, split data, save preprocess.json."""
    import torch
    sys.path.insert(0, str(BASE_DIR / "src"))
    from fewrel_utils import load_fewrel, get_all_relation_types, sample_balanced

    logger.info("Loading FewRel data (train+val, 80 relations)...")
    all_samples = []
    for dp in [BASE_DIR / "data/fewrel_parquet/train.parquet",
               BASE_DIR / "data/fewrel_parquet/val.parquet"]:
        all_samples.extend(load_fewrel(data_path=str(dp)))
    all_relations = get_all_relation_types(all_samples)
    logger.info("%d total samples, %d relations", len(all_samples), len(all_relations))

    n_per_rel = args.n_samples // len(all_relations)
    test_samples = sample_balanced(all_samples, n_per_rel, seed=args.seed)
    test_ids = set(id(s) for s in test_samples)

    fewshot_pool_by_rel = defaultdict(list)
    for s in all_samples:
        if id(s) not in test_ids:
            fewshot_pool_by_rel[s["relation_type"]].append(s)

    logger.info("Test: %d samples (%d/rel)", len(test_samples), n_per_rel)
    logger.info("Few-shot pool: %d relations, min %d samples/rel",
                len(fewshot_pool_by_rel),
                min(len(v) for v in fewshot_pool_by_rel.values()))

    sim_matrix, type_names, type_to_idx = load_sim_data()

    batch_configs = {}
    for count in args.counts:
        if count == 8:
            low_group, high_group = load_precomputed_batches(count)
            low_group = low_group[:args.n_batches]
            high_group = high_group[:args.n_batches]
            logger.info("count_8: loaded pre-computed batches from %s",
                        PRECOMPUTED_BATCH_PATH)
        else:
            low_group, high_group = generate_extreme_batches_large_pool(
                count, args.n_batches, sim_matrix, type_names, type_to_idx,
                seed=args.seed + count)

        batch_list = []
        for i, b in enumerate(low_group):
            batch_list.append({
                "batch_id": f"count_{count}_low_{i}",
                "types": b["types"],
                "bcs": b["bcs"],
                "group": "low",
                "count": count,
            })
        for i, b in enumerate(high_group):
            batch_list.append({
                "batch_id": f"count_{count}_high_{i}",
                "types": b["types"],
                "bcs": b["bcs"],
                "group": "high",
                "count": count,
            })
        batch_configs[f"count_{count}"] = batch_list

        logger.info("count_%d: low BCS=[%.4f, %.4f], high BCS=[%.4f, %.4f]",
                    count,
                    low_group[0]["bcs"], low_group[-1]["bcs"],
                    high_group[0]["bcs"], high_group[-1]["bcs"])

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    preprocess_config = {
        "test_samples": test_samples,
        "fewshot_pool_by_rel": dict(fewshot_pool_by_rel),
        "batch_configs": batch_configs,
        "n_shots_list": args.n_shots,
        "counts": args.counts,
        "model_path": args.model_path,
        "max_model_len": args.max_model_len,
        "gpu_memory_utilization": args.gpu_memory_utilization,
        "seed": args.seed,
    }
    preprocess_path = OUTPUT_DIR / "preprocess.json"
    with open(preprocess_path, "w") as f:
        json.dump(preprocess_config, f, ensure_ascii=False)
    logger.info("Saved preprocess config: %s", preprocess_path)

    total_inferences = 0
    for ck, batches in batch_configs.items():
        for b in batches:
            type_set = set(b["types"])
            n_test = len([s for s in test_samples if s["relation_type"] in type_set])
            total_inferences += n_test * len(args.n_shots)
    logger.info("Total inferences: %d", total_inferences)

    if args.dry_run:
        logger.info("DRY RUN complete.")
        return None
    return str(preprocess_path)


def stage_extract(args):
    """GPU stage: load vLLM, run inference for all (n_shots, count, batch) combos."""
    sys.path.insert(0, str(BASE_DIR / "src"))
    from run_extraction import build_json_schema_re
    from vllm import LLM, SamplingParams
    from vllm.sampling_params import StructuredOutputsParams

    preprocess_path = args.preprocess_path or str(OUTPUT_DIR / "preprocess.json")
    with open(preprocess_path) as f:
        config = json.load(f)

    test_samples = config["test_samples"]
    fewshot_pool_by_rel = config["fewshot_pool_by_rel"]
    batch_configs = config["batch_configs"]
    n_shots_list = config["n_shots_list"]
    model_path = config["model_path"]
    seed = config["seed"]

    results_path = OUTPUT_DIR / "results_incremental.jsonl"
    completed_keys = set()
    existing_results = []
    if args.resume and results_path.exists():
        with open(results_path) as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    existing_results.append(r)
                    completed_keys.add(r["condition_key"])
        logger.info("Resumed: %d results, %d unique conditions",
                    len(existing_results), len(completed_keys))

    logger.info("Loading vLLM: %s (max_model_len=%d)",
                model_path, config["max_model_len"])
    llm = LLM(
        model=model_path,
        max_model_len=config["max_model_len"],
        trust_remote_code=True,
        dtype="bfloat16",
        gpu_memory_utilization=config.get("gpu_memory_utilization", 0.90),
        enforce_eager=True,
        disable_log_stats=True,
    )

    rng = random.Random(seed)
    all_results = list(existing_results)
    total_batches_done = 0
    total_batches_total = sum(
        len(batches) * len(n_shots_list)
        for batches in batch_configs.values()
    )

    for count_key in sorted(batch_configs.keys()):
        batches = batch_configs[count_key]
        for n_shots in n_shots_list:
            for batch in batches:
                batch_id = batch["batch_id"]
                condition_key = f"{batch_id}_shot{n_shots}"
                total_batches_done += 1

                if condition_key in completed_keys:
                    continue

                batch_types = batch["types"]
                batch_bcs = batch["bcs"]
                group = batch["group"]
                count = batch["count"]
                type_set = set(batch_types)

                batch_test = [s for s in test_samples
                              if s["relation_type"] in type_set]
                if not batch_test:
                    logger.warning("No test samples for %s", condition_key)
                    continue

                fewshot_examples = select_fewshot_examples(
                    fewshot_pool_by_rel, batch_types, n_shots, rng)

                schema = build_json_schema_re(batch_types)
                structured = StructuredOutputsParams(json=schema)
                sampling_params = SamplingParams(
                    max_tokens=64, temperature=0.0, seed=42,
                    structured_outputs=structured,
                )

                prompts = []
                sample_refs = []
                for s in batch_test:
                    p = build_fewshot_prompt(
                        s["text"], s["head_entity"], s["tail_entity"],
                        batch_types, fewshot_examples, n_shots)
                    prompts.append(p)
                    sample_refs.append(s)

                logger.info("[%d/%d] %s: %d-shot, %d types, BCS=%.4f, %d samples",
                            total_batches_done, total_batches_total,
                            condition_key, n_shots, len(batch_types),
                            batch_bcs, len(prompts))

                t0 = time.time()
                outputs = llm.generate(prompts, sampling_params)
                elapsed = time.time() - t0

                batch_results = []
                for oi, output in enumerate(outputs):
                    pred_text = output.outputs[0].text.strip()
                    try:
                        pred_json = json.loads(pred_text)
                        pred_rel = pred_json.get("relation", "none")
                    except json.JSONDecodeError:
                        pred_rel = "parse_error"

                    gold_rel = sample_refs[oi]["relation_type"]
                    correct = int(pred_rel == gold_rel)
                    batch_results.append(correct)

                accuracy = np.mean(batch_results) if batch_results else 0.0

                result_record = {
                    "condition_key": condition_key,
                    "batch_id": batch_id,
                    "n_shots": n_shots,
                    "count": count,
                    "group": group,
                    "bcs": batch_bcs,
                    "accuracy": float(accuracy),
                    "n_samples": len(batch_results),
                    "n_correct": sum(batch_results),
                    "elapsed_sec": round(elapsed, 2),
                }
                all_results.append(result_record)

                with open(results_path, "a") as f:
                    f.write(json.dumps(result_record) + "\n")

                logger.info("  -> acc=%.4f (%d/%d) in %.1fs",
                            accuracy, sum(batch_results),
                            len(batch_results), elapsed)

    logger.info("All batches done. Running analysis...")
    run_analysis(all_results, args.n_bootstrap, args.seed)


def run_analysis(results, n_bootstrap=10000, seed=42):
    """Bootstrap analysis of few-shot BCS mitigation effect."""
    rng = np.random.default_rng(seed)

    by_condition = defaultdict(list)
    batch_bcs_vals = defaultdict(list)
    for r in results:
        key = (r["n_shots"], r["count"], r["group"])
        by_condition[key].append(r["accuracy"])
        batch_bcs_vals[key].append(r["bcs"])

    analysis = {}
    for n_shots in sorted(set(r["n_shots"] for r in results)):
        for count in sorted(set(r["count"] for r in results)):
            low_accs = by_condition.get((n_shots, count, "low"), [])
            high_accs = by_condition.get((n_shots, count, "high"), [])
            if not low_accs or not high_accs:
                continue

            low_arr = np.array(low_accs)
            high_arr = np.array(high_accs)
            delta = np.mean(low_arr) - np.mean(high_arr)

            deltas = []
            for _ in range(n_bootstrap):
                l_boot = rng.choice(low_arr, size=len(low_arr), replace=True)
                h_boot = rng.choice(high_arr, size=len(high_arr), replace=True)
                deltas.append(np.mean(l_boot) - np.mean(h_boot))
            deltas = np.array(deltas)

            key = f"shot{n_shots}_count{count}"
            analysis[key] = {
                "n_shots": n_shots,
                "count": count,
                "low_mean_acc": round(float(np.mean(low_arr)), 4),
                "high_mean_acc": round(float(np.mean(high_arr)), 4),
                "delta_pp": round(float(delta * 100), 2),
                "ci_lower_pp": round(float(np.percentile(deltas, 2.5) * 100), 2),
                "ci_upper_pp": round(float(np.percentile(deltas, 97.5) * 100), 2),
                "n_low_batches": len(low_accs),
                "n_high_batches": len(high_accs),
                "low_bcs_mean": round(float(np.mean(
                    batch_bcs_vals.get((n_shots, count, "low"), [0]))), 4),
                "high_bcs_mean": round(float(np.mean(
                    batch_bcs_vals.get((n_shots, count, "high"), [0]))), 4),
            }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_DIR / "analysis.json", "w") as f:
        json.dump(analysis, f, indent=2)

    logger.info("=" * 80)
    logger.info("RESULTS: Few-shot BCS Mitigation (v2 - extreme batches)")
    logger.info("=" * 80)
    logger.info("%-25s %8s %8s %10s %18s",
                "Condition", "Low Acc", "High Acc", "Delta(pp)", "95% CI")
    logger.info("-" * 80)
    for key in sorted(analysis.keys()):
        a = analysis[key]
        logger.info("%-25s %8.4f %8.4f %+10.2f [%+.2f, %+.2f]",
                    key, a["low_mean_acc"], a["high_mean_acc"],
                    a["delta_pp"], a["ci_lower_pp"], a["ci_upper_pp"])

    logger.info("-" * 80)
    logger.info("Interpretation:")
    for count in sorted(set(a["count"] for a in analysis.values())):
        baseline_key = f"shot0_count{count}"
        if baseline_key not in analysis:
            continue
        baseline_delta = analysis[baseline_key]["delta_pp"]
        logger.info("  count_%d baseline delta: %+.2fpp", count, baseline_delta)
        for ns in [1, 5]:
            k = f"shot{ns}_count{count}"
            if k in analysis:
                d = analysis[k]["delta_pp"]
                reduction = baseline_delta - d
                logger.info("    %d-shot delta: %+.2fpp (reduction: %.2fpp)",
                            ns, d, reduction)

    return analysis


def main():
    parser = argparse.ArgumentParser(
        description="Few-shot BCS mitigation (v2 extreme batches)")
    parser.add_argument("--model_path", default=MODEL_PATH)
    parser.add_argument("--n_shots", type=int, nargs="+", default=DEFAULT_N_SHOTS)
    parser.add_argument("--counts", type=int, nargs="+", default=DEFAULT_COUNTS)
    parser.add_argument("--n_batches", type=int, default=DEFAULT_N_BATCHES)
    parser.add_argument("--n_samples", type=int, default=DEFAULT_N_SAMPLES)
    parser.add_argument("--n_bootstrap", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--gpu_memory_utilization", type=float, default=0.90)
    parser.add_argument("--max_model_len", type=int, default=8192)
    parser.add_argument("--dry_run", action="store_true")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--analysis_only", action="store_true")
    parser.add_argument("--stage", choices=["preprocess", "extract", "all"],
                        default="all")
    parser.add_argument("--preprocess_path", default=None)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s")

    if args.analysis_only:
        results = []
        with open(OUTPUT_DIR / "results_incremental.jsonl") as f:
            for line in f:
                if line.strip():
                    results.append(json.loads(line))
        logger.info("Loaded %d results for analysis", len(results))
        run_analysis(results, args.n_bootstrap, args.seed)
        return

    if args.stage == "preprocess":
        stage_preprocess(args)
    elif args.stage == "extract":
        stage_extract(args)
    elif args.stage == "all":
        preprocess_path = stage_preprocess(args)
        if preprocess_path is None:
            return

        logger.info("=== Launching extract subprocess (vLLM-first) ===")
        cmd = [sys.executable, str(Path(__file__).resolve()),
               "--stage", "extract",
               "--n_bootstrap", str(args.n_bootstrap),
               "--seed", str(args.seed)]
        if args.resume:
            cmd.append("--resume")
        subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()

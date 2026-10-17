#!/usr/bin/env python3
"""D051 Batch 2: Count curves with 25+ batches per count level.

For R6-W3: Figure 1 error bars (25 batches -> mean +/- SD).
For R8-W2: 3-seed variance (run with --seed 42/123/456).

Usage:
    python3 scripts/run_d051_count_curves_25.py --dataset fewnerd --seed 42
    python3 scripts/run_d051_count_curves_25.py --dataset fewrel --seed 42
    python3 scripts/run_d051_count_curves_25.py --dataset fewrel --seed 123
    python3 scripts/run_d051_count_curves_25.py --dataset fewrel --dry_run
"""
import os
os.environ["FLASHINFER_DISABLE_VERSION_CHECK"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import argparse
import json
import logging
import random
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
import torch

logger = logging.getLogger(__name__)

BASE_DIR = Path(".")
MODEL_PATH = "~/.cache/huggingface/qwen3-32b-fp8/"

NER_COUNTS = [2, 6, 12, 22, 44, 66]
RE_COUNTS = [4, 8, 16, 32, 40, 64, 80]
DEFAULT_N_BATCHES = 25
DEFAULT_N_SAMPLES = 1000


def load_sim_data(dataset):
    if dataset == "fewnerd":
        path = BASE_DIR / "artifacts/sim_matrix.pt"
    else:
        path = BASE_DIR / "artifacts/fewrel_formal_full/relation_sim_matrix.pt"
    data = torch.load(str(path), map_location="cpu", weights_only=True)
    sim_matrix = data.get("sim_matrix", data.get("similarity_matrix"))
    type_names = data["type_names"]
    type_to_idx = data.get("type_to_idx", {n: i for i, n in enumerate(type_names)})
    return sim_matrix, type_names, type_to_idx


def generate_batch_config(counts, n_batches, sim_matrix, type_names, type_to_idx, seed):
    sys.path.insert(0, str(BASE_DIR / "src"))
    from select_type_batches import select_random_batches

    config = {}
    for count in counts:
        c = min(count, len(type_names))
        rand = select_random_batches(c, n_batches, type_names, sim_matrix,
                                     type_to_idx, seed + count)
        config[f"count_{count}"] = {"random": rand}
    return config


def run_ner_extraction(samples, batch_config, type_definitions, output_dir, gpu_mem=0.90):
    sys.path.insert(0, str(BASE_DIR / "src"))
    from run_extraction import build_json_schema_v2, build_prompt_v2
    from vllm import LLM, SamplingParams
    from vllm.sampling_params import StructuredOutputsParams

    logger.info("Loading vLLM model for NER...")
    llm = LLM(model=MODEL_PATH, max_model_len=4096, trust_remote_code=True,
              dtype="bfloat16", gpu_memory_utilization=gpu_mem, enforce_eager=True,
              disable_log_stats=True)

    for count_key in sorted(batch_config.keys()):
        result_path = output_dir / f"results_{count_key}.jsonl"
        if result_path.exists():
            logger.info("Skipping %s (already exists)", count_key)
            continue

        strategies = batch_config[count_key]
        batches_to_run = []
        for ri, rb in enumerate(strategies.get("random", [])):
            batches_to_run.append((f"random_{ri}", rb["types"], rb["bcs"]))

        logger.info("Processing %s: %d batches x %d samples...",
                    count_key, len(batches_to_run), len(samples))
        t0_count = time.time()
        count_results = []

        for batch_id, batch_types, batch_bcs in batches_to_run:
            full_bid = f"{count_key}_{batch_id}"
            schema = build_json_schema_v2(batch_types)
            structured = StructuredOutputsParams(json=schema)
            sp = SamplingParams(max_tokens=1024, temperature=0.0,
                               structured_outputs=structured)

            prompts = [build_prompt_v2(s["text"], type_definitions, batch_types)
                       for s in samples]

            t0 = time.time()
            outputs = llm.generate(prompts, sp)
            elapsed = time.time() - t0

            for oi, output in enumerate(outputs):
                try:
                    preds = json.loads(output.outputs[0].text)
                except json.JSONDecodeError:
                    preds = []
                count_results.append({
                    "sample_id": oi,
                    "batch_id": full_bid,
                    "count_key": count_key,
                    "batch_types": batch_types,
                    "batch_bcs": batch_bcs,
                    "predictions": preds,
                    "prompt_tokens": len(output.prompt_token_ids),
                    "gen_tokens": len(output.outputs[0].token_ids),
                    "latency_s": elapsed / len(prompts),
                    "prompt_version": "v2",
                })

            logger.info("  %s: %.1fs (%.3fs/sample)", full_bid, elapsed,
                        elapsed / len(prompts))

        with open(result_path, "w") as f:
            for r in count_results:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        elapsed_count = time.time() - t0_count
        logger.info("Saved %s: %d results in %.1fs",
                    result_path.name, len(count_results), elapsed_count)

    del llm
    torch.cuda.empty_cache()


def run_re_extraction(samples, batch_config, relation_defs, output_dir, gpu_mem=0.90):
    sys.path.insert(0, str(BASE_DIR / "src"))
    from run_extraction import build_json_schema_re, build_prompt_v2_re
    from vllm import LLM, SamplingParams
    from vllm.sampling_params import StructuredOutputsParams

    logger.info("Loading vLLM model for RE...")
    llm = LLM(model=MODEL_PATH, max_model_len=4096, trust_remote_code=True,
              dtype="bfloat16", gpu_memory_utilization=gpu_mem, enforce_eager=True,
              disable_log_stats=True)

    sample_id_map = {id(s): i for i, s in enumerate(samples)}

    for count_key in sorted(batch_config.keys()):
        result_path = output_dir / f"results_{count_key}.jsonl"
        if result_path.exists():
            logger.info("Skipping %s (already exists)", count_key)
            continue

        strategies = batch_config[count_key]
        batches_to_run = []
        for ri, rb in enumerate(strategies.get("random", [])):
            batches_to_run.append((f"random_{ri}", rb["types"], rb["bcs"]))

        logger.info("Processing %s: %d batches...", count_key, len(batches_to_run))
        t0_count = time.time()
        count_results = []

        for batch_id, batch_types, batch_bcs in batches_to_run:
            full_bid = f"{count_key}_{batch_id}"
            type_set = set(batch_types)
            batch_samples = [s for s in samples if s["relation_type"] in type_set]
            if not batch_samples:
                logger.warning("No samples for %s", full_bid)
                continue

            schema = build_json_schema_re(batch_types)
            structured = StructuredOutputsParams(json=schema)
            sp = SamplingParams(max_tokens=64, temperature=0.0,
                               structured_outputs=structured)

            prompts = []
            sample_refs = []
            for s in batch_samples:
                p = build_prompt_v2_re(s["text"], s["head_entity"], s["tail_entity"],
                                       relation_defs, batch_types)
                prompts.append(p)
                sample_refs.append(s)

            t0 = time.time()
            outputs = llm.generate(prompts, sp)
            elapsed = time.time() - t0

            for oi, output in enumerate(outputs):
                s = sample_refs[oi]
                try:
                    parsed = json.loads(output.outputs[0].text)
                    pred_rel = parsed.get("relation", "none")
                except json.JSONDecodeError:
                    pred_rel = "none"

                count_results.append({
                    "sample_id": sample_id_map[id(s)],
                    "batch_id": full_bid,
                    "count_key": count_key,
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

            logger.info("  %s: %d types, %d samples, %.1fs",
                        full_bid, len(batch_types), len(batch_samples), elapsed)

        with open(result_path, "w") as f:
            for r in count_results:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        elapsed_count = time.time() - t0_count
        logger.info("Saved %s: %d results in %.1fs",
                    result_path.name, len(count_results), elapsed_count)

    del llm
    torch.cuda.empty_cache()


def evaluate_ner_results(output_dir, samples):
    sys.path.insert(0, str(BASE_DIR / "src"))
    from evaluate import evaluate_all

    all_preds = []
    for p in sorted(output_dir.glob("results_count_*.jsonl")):
        with open(p) as f:
            for line in f:
                all_preds.append(json.loads(line))

    if not all_preds:
        logger.warning("No NER results found")
        return {}

    eval_results = evaluate_all(all_preds, samples, eval_mode="text_match")

    eval_path = output_dir / "eval_results.json"
    with open(eval_path, "w") as f:
        json.dump(eval_results, f, indent=2)

    count_summary = defaultdict(list)
    for bid, m in eval_results.items():
        ck = m["count_key"]
        recall = m["text_match"]["recall"]
        count_summary[ck].append(recall)

    summary = {}
    for ck in sorted(count_summary.keys()):
        vals = count_summary[ck]
        summary[ck] = {
            "n_batches": len(vals),
            "mean_recall": float(np.mean(vals)),
            "std_recall": float(np.std(vals)),
            "min_recall": float(np.min(vals)),
            "max_recall": float(np.max(vals)),
        }

    summary_path = output_dir / "count_curve_summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    return summary


def evaluate_re_results(output_dir):
    all_results = []
    for p in sorted(output_dir.glob("results_count_*.jsonl")):
        with open(p) as f:
            for line in f:
                all_results.append(json.loads(line))

    if not all_results:
        logger.warning("No RE results found")
        return {}

    batch_stats = defaultdict(lambda: {"correct": 0, "total": 0, "bcs": 0.0,
                                       "count_key": "", "num_types": 0})
    for r in all_results:
        bid = r["batch_id"]
        s = batch_stats[bid]
        s["total"] += 1
        s["bcs"] = r["batch_bcs"]
        s["count_key"] = r["count_key"]
        s["num_types"] = len(r["batch_types"])
        if r["prediction"] == r["ground_truth"]:
            s["correct"] += 1

    eval_results = {}
    for bid, s in batch_stats.items():
        eval_results[bid] = {
            "accuracy": s["correct"] / s["total"] if s["total"] else 0.0,
            "correct": s["correct"], "total": s["total"],
            "bcs": s["bcs"], "count_key": s["count_key"],
            "num_types": s["num_types"],
        }

    eval_path = output_dir / "eval_results.json"
    with open(eval_path, "w") as f:
        json.dump(eval_results, f, indent=2)

    count_summary = defaultdict(list)
    for bid, m in eval_results.items():
        count_summary[m["count_key"]].append(m["accuracy"])

    summary = {}
    for ck in sorted(count_summary.keys()):
        accs = count_summary[ck]
        summary[ck] = {
            "n_batches": len(accs),
            "mean_accuracy": float(np.mean(accs)),
            "std_accuracy": float(np.std(accs)),
            "min_accuracy": float(np.min(accs)),
            "max_accuracy": float(np.max(accs)),
        }

    summary_path = output_dir / "count_curve_summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    return summary


def main():
    parser = argparse.ArgumentParser(
        description="D051: Count curves with configurable n_batches and seed")
    parser.add_argument("--dataset", choices=["fewnerd", "fewrel"], required=True)
    parser.add_argument("--n_batches", type=int, default=DEFAULT_N_BATCHES)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output_dir", default=None)
    parser.add_argument("--counts", default=None,
                        help="Override count levels (comma-separated)")
    parser.add_argument("--max_samples", type=int, default=DEFAULT_N_SAMPLES)
    parser.add_argument("--gpu_mem", type=float, default=0.90)
    parser.add_argument("--dry_run", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s")

    if args.output_dir is None:
        args.output_dir = str(
            BASE_DIR / "artifacts" /
            f"d051_{args.dataset}_n{args.n_batches}_s{args.seed}")
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.counts:
        counts = [int(c.strip()) for c in args.counts.split(",")]
    else:
        counts = NER_COUNTS if args.dataset == "fewnerd" else RE_COUNTS

    sim_matrix, type_names, type_to_idx = load_sim_data(args.dataset)
    batch_config = generate_batch_config(
        counts, args.n_batches, sim_matrix, type_names, type_to_idx, args.seed)

    config_path = output_dir / "batch_config.json"
    with open(config_path, "w") as f:
        json.dump(batch_config, f, indent=2)

    total_batches = sum(len(v.get("random", [])) for v in batch_config.values())
    logger.info("Config: dataset=%s, n_batches=%d, seed=%d, counts=%s, total=%d",
                args.dataset, args.n_batches, args.seed, counts, total_batches)
    for ck, cv in sorted(batch_config.items()):
        bcs_vals = [b["bcs"] for b in cv.get("random", [])]
        logger.info("  %s: %d batches, BCS=[%.4f, %.4f]",
                    ck, len(bcs_vals), min(bcs_vals), max(bcs_vals))

    if args.dry_run:
        logger.info("DRY RUN complete. Batch config saved to %s", config_path)
        return

    sys.path.insert(0, str(BASE_DIR / "src"))

    if args.dataset == "fewnerd":
        from few_nerd_utils import load_few_nerd, load_type_definitions
        samples = load_few_nerd(split="test", max_samples=args.max_samples)
        type_definitions = load_type_definitions(
            str(BASE_DIR / "configs/few_nerd_types.json"))
        logger.info("Loaded %d NER samples", len(samples))

        run_ner_extraction(samples, batch_config, type_definitions,
                           output_dir, args.gpu_mem)
        summary = evaluate_ner_results(output_dir, samples)
        logger.info("NER count curve results:")
        for ck, s in sorted(summary.items()):
            logger.info("  %s: recall=%.4f +/- %.4f (n=%d)",
                        ck, s["mean_recall"], s["std_recall"], s["n_batches"])

    else:
        from fewrel_utils import load_fewrel, get_all_relation_types, sample_balanced
        samples_all = []
        for dp in [str(BASE_DIR / "data/fewrel_parquet/train.parquet"),
                   str(BASE_DIR / "data/fewrel_parquet/val.parquet")]:
            samples_all.extend(load_fewrel(data_path=dp))

        all_relations = get_all_relation_types(samples_all)
        n_per_rel = args.max_samples // len(all_relations)
        random.seed(args.seed)
        samples = sample_balanced(samples_all, n_per_rel, seed=args.seed)

        with open(str(BASE_DIR / "configs/fewrel_relation_types.json")) as f:
            pid2name = json.load(f)
        relation_defs = {name: name for name in pid2name.values()}

        logger.info("Loaded %d RE samples (%d/rel, %d rels)",
                    len(samples), n_per_rel, len(all_relations))

        sample_info = {
            "n_samples": len(samples), "n_per_rel": n_per_rel,
            "n_relations": len(all_relations), "seed": args.seed,
        }
        with open(output_dir / "sample_info.json", "w") as f:
            json.dump(sample_info, f, indent=2)

        run_re_extraction(samples, batch_config, relation_defs,
                          output_dir, args.gpu_mem)
        summary = evaluate_re_results(output_dir)
        logger.info("RE count curve results:")
        for ck, s in sorted(summary.items()):
            logger.info("  %s: acc=%.4f +/- %.4f (n=%d)",
                        ck, s["mean_accuracy"], s["std_accuracy"],
                        s["n_batches"])

    logger.info("Done. Output: %s", output_dir)


if __name__ == "__main__":
    main()

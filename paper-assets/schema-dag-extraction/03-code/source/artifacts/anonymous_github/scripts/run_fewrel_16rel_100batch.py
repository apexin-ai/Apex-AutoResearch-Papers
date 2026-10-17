"""FewRel 16-rel pool, 100 random count_8 batches + bootstrap CI.

Pool: 16 relation types from FewRel val split (subset of the 80-type pool).
Task: sample 100 random subsets of 8 relations, run extraction, compute
      BCS-accuracy correlation and bootstrap CI for the BCS effect (Δ accuracy
      between low-BCS and high-BCS halves).

Input:  data/fewrel_parquet/val.parquet
        configs/fewrel_relation_types.json
        artifacts/fewrel_formal/relation_sim_matrix.pt (MiniLM, 80-type)
        Qwen3-32B-FP8 model at ~/.cache/huggingface/qwen3-32b-fp8/
Output: artifacts/fewrel_16rel_100batch/results.json
        artifacts/fewrel_16rel_100batch/bootstrap_ci.json
"""
import os
os.environ["CUDA_HOME"] = "./miniconda3/lib/python3.12/site-packages/nvidia/cu13"
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

BASE_DIR = Path(".")
DEFAULT_N_BATCHES = 100
DEFAULT_COUNT = 8
DEFAULT_N_SAMPLES = 1000


def evaluate_re(results):
    batch_stats = defaultdict(lambda: {"correct": 0, "total": 0, "bcs": 0.0,
                                       "count_key": "", "num_types": 0,
                                       "batch_types": [], "per_type": defaultdict(lambda: {"correct": 0, "total": 0})})
    for r in results:
        bid = r["batch_id"]
        s = batch_stats[bid]
        s["total"] += 1
        s["bcs"] = r["batch_bcs"]
        s["count_key"] = r["count_key"]
        s["num_types"] = len(r["batch_types"])
        s["batch_types"] = r["batch_types"]
        gold = r["ground_truth"]
        pred = r["prediction"]
        s["per_type"][gold]["total"] += 1
        if pred == gold:
            s["correct"] += 1
            s["per_type"][gold]["correct"] += 1

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
            "correct": s["correct"], "total": s["total"], "bcs": s["bcs"],
            "count_key": s["count_key"], "num_types": s["num_types"],
            "batch_types": s["batch_types"], "per_type_accuracy": per_type_acc,
        }
    return out


def run_re_extraction(model_path, samples, batch_config, relation_defs, max_model_len=4096):
    sys.path.insert(0, str(BASE_DIR / "src"))
    from run_extraction import build_json_schema_re, build_prompt_v2_re
    from vllm import LLM, SamplingParams
    from vllm.sampling_params import StructuredOutputsParams

    llm = LLM(model=model_path, max_model_len=max_model_len,
              trust_remote_code=True, dtype="bfloat16",
              gpu_memory_utilization=0.85, enforce_eager=True, disable_log_stats=True)

    all_results = []
    sample_id_map = {id(s): i for i, s in enumerate(samples)}

    for count_key, strategies in batch_config.items():
        batches_to_run = []
        if "random" in strategies:
            for ri, rb in enumerate(strategies["random"]):
                batches_to_run.append((f"random_{ri}", rb["types"], rb["bcs"]))

        for batch_id, batch_types, batch_bcs in batches_to_run:
            full_bid = f"{count_key}_{batch_id}"
            type_set = set(batch_types)
            batch_samples = [s for s in samples if s["relation_type"] in type_set]
            if not batch_samples:
                logger.warning("No samples for batch %s", full_bid)
                continue

            logger.info("Batch %s: %d types, BCS=%.4f, %d samples",
                        full_bid, len(batch_types), batch_bcs, len(batch_samples))
            schema = build_json_schema_re(batch_types)
            structured = StructuredOutputsParams(json=schema)
            sampling_params = SamplingParams(max_tokens=64, temperature=0.0, structured_outputs=structured)

            prompts = []
            sample_refs = []
            for s in batch_samples:
                p = build_prompt_v2_re(s["text"], s["head_entity"], s["tail_entity"], relation_defs, batch_types)
                prompts.append(p)
                sample_refs.append(s)

            t0 = time.time()
            outputs = llm.generate(prompts, sampling_params)
            elapsed = time.time() - t0

            for oi, output in enumerate(outputs):
                s = sample_refs[oi]
                gen_text = output.outputs[0].text
                try:
                    parsed = json.loads(gen_text)
                    pred_rel = parsed.get("relation", "none")
                except json.JSONDecodeError:
                    pred_rel = "none"

                all_results.append({
                    "sample_id": sample_id_map[id(s)], "batch_id": full_bid,
                    "count_key": count_key, "batch_types": batch_types, "batch_bcs": batch_bcs,
                    "prediction": pred_rel, "ground_truth": s["relation_type"],
                    "head_entity": s["head_entity"], "tail_entity": s["tail_entity"],
                    "prompt_tokens": len(output.prompt_token_ids),
                    "gen_tokens": len(output.outputs[0].token_ids),
                    "latency_s": elapsed / len(prompts),
                })
            logger.info("  Done: %.1fs (%.2fs/sample)", elapsed, elapsed / len(batch_samples))

    return all_results


def bootstrap_bcs_effect(eval_results, n_bootstrap=10000, seed=42):
    batches = []
    for bid, m in eval_results.items():
        batches.append({"batch_id": bid, "bcs": m["bcs"], "accuracy": m["accuracy"],
                        "correct": m["correct"], "total": m["total"]})

    bcs_values = [b["bcs"] for b in batches]
    median_bcs = float(np.median(bcs_values))

    low_bcs = [b for b in batches if b["bcs"] <= median_bcs]
    high_bcs = [b for b in batches if b["bcs"] > median_bcs]
    if not high_bcs:
        high_bcs = [b for b in batches if b["bcs"] >= median_bcs]
        low_bcs = [b for b in batches if b["bcs"] < median_bcs]

    mean_acc_low = np.mean([b["accuracy"] for b in low_bcs])
    mean_acc_high = np.mean([b["accuracy"] for b in high_bcs])
    delta_pp = (mean_acc_low - mean_acc_high) * 100

    rng = np.random.RandomState(seed)
    boot_deltas = np.empty(n_bootstrap)
    n = len(batches)

    for i in range(n_bootstrap):
        idx = rng.randint(0, n, size=n)
        resampled = [batches[j] for j in idx]
        bcs_med = np.median([b["bcs"] for b in resampled])
        lo = [b for b in resampled if b["bcs"] <= bcs_med]
        hi = [b for b in resampled if b["bcs"] > bcs_med]
        if not hi:
            hi = [b for b in resampled if b["bcs"] >= bcs_med]
            lo = [b for b in resampled if b["bcs"] < bcs_med]
        if not lo or not hi:
            boot_deltas[i] = 0.0
            continue
        d = np.mean([b["accuracy"] for b in lo]) - np.mean([b["accuracy"] for b in hi])
        boot_deltas[i] = d * 100

    pearson_r = float(np.corrcoef(
        [b["bcs"] for b in batches],
        [b["accuracy"] for b in batches]
    )[0, 1])

    boot_corrs = np.empty(n_bootstrap)
    bcs_arr = np.array([b["bcs"] for b in batches])
    acc_arr = np.array([b["accuracy"] for b in batches])
    for i in range(n_bootstrap):
        idx = rng.randint(0, n, size=n)
        boot_corrs[i] = float(np.corrcoef(bcs_arr[idx], acc_arr[idx])[0, 1])

    return {
        "n_batches": len(batches),
        "median_bcs": round(median_bcs, 4),
        "n_low_bcs": len(low_bcs),
        "n_high_bcs": len(high_bcs),
        "mean_acc_low_bcs": round(float(mean_acc_low), 4),
        "mean_acc_high_bcs": round(float(mean_acc_high), 4),
        "delta_pp": round(float(delta_pp), 2),
        "delta_ci_lower_pp": round(float(np.percentile(boot_deltas, 2.5)), 2),
        "delta_ci_upper_pp": round(float(np.percentile(boot_deltas, 97.5)), 2),
        "pearson_r_bcs_acc": round(pearson_r, 4),
        "pearson_r_ci_lower": round(float(np.percentile(boot_corrs, 2.5)), 4),
        "pearson_r_ci_upper": round(float(np.percentile(boot_corrs, 97.5)), 4),
        "n_bootstrap": n_bootstrap,
        "seed": seed,
        "batches": [{"batch_id": b["batch_id"], "bcs": round(b["bcs"], 4),
                     "accuracy": round(b["accuracy"], 4)} for b in batches],
    }


def stage_preprocess(args):
    sys.path.insert(0, str(BASE_DIR / "src"))
    from fewrel_utils import load_fewrel, get_all_relation_types, sample_balanced
    from compute_bcs import compute_bcs
    from select_type_batches import select_random_batches

    import torch

    logger.info("Loading FewRel val data (16-rel pool)...")
    all_samples = load_fewrel(data_path=str(BASE_DIR / "data/fewrel_parquet/val.parquet"))
    all_relations = get_all_relation_types(all_samples)
    logger.info("%d samples, %d relation types", len(all_samples), len(all_relations))

    n_per_rel = args.n_samples // len(all_relations)
    samples = sample_balanced(all_samples, n_per_rel, seed=args.seed)
    logger.info("Sampled %d (%d per relation, %d relations)",
                len(samples), n_per_rel, len(all_relations))

    with open(args.types_file) as f:
        pid2name = json.load(f)
    relation_defs = {name: name for name in pid2name.values()}

    logger.info("Loading pre-computed sim matrix from %s", args.sim_matrix_path)
    data = torch.load(args.sim_matrix_path, map_location="cpu", weights_only=True)
    sim_matrix = data["sim_matrix"]
    type_names = data["type_names"]
    type_to_idx = data["type_to_idx"]
    logger.info("Similarity matrix: %d types", len(type_names))

    active_types = [t for t in type_names if t in set(all_relations)]
    active_idx = {t: type_to_idx[t] for t in active_types}
    n_active = len(active_types)
    logger.info("Active types (in both sim_matrix and data): %d", n_active)

    count = min(args.count, n_active)
    rand = select_random_batches(count, args.n_batches, active_types,
                                 sim_matrix, active_idx, args.seed)
    batch_config = {f"count_{count}": {"random": rand}}

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_dir / "batch_config.json", "w") as f:
        json.dump(batch_config, f, indent=2)

    preprocess_data = {
        "model_path": args.model_path,
        "samples": samples,
        "batch_config": batch_config,
        "relation_defs": relation_defs,
        "max_model_len": args.max_model_len,
        "output_dir": str(output_dir),
        "pool_size": n_active,
        "count": count,
        "n_batches": args.n_batches,
    }
    preprocess_path = output_dir / "preprocess.json"
    with open(preprocess_path, "w") as f:
        json.dump(preprocess_data, f, ensure_ascii=False)
    logger.info("Saved preprocess config to %s", preprocess_path)

    total_inferences = sum(
        len([s for s in samples if s["relation_type"] in set(b["types"])])
        for b in rand
    )
    logger.info("Total inferences: %d", total_inferences)
    est_sec = 1.5
    logger.info("Est. GPU time: ~%.0f min (@%.1fs/sample)", total_inferences * est_sec / 60, est_sec)

    return str(preprocess_path)


def stage_extract(args):
    preprocess_path = args.preprocess_path or str(
        Path(args.output_dir) / "preprocess.json"
    )
    with open(preprocess_path) as f:
        config = json.load(f)

    results = run_re_extraction(
        config["model_path"], config["samples"], config["batch_config"],
        config["relation_defs"], config["max_model_len"],
    )

    output_dir = Path(config["output_dir"])

    pred_path = output_dir / "predictions.json"
    with open(pred_path, "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    logger.info("Saved %d predictions to %s", len(results), pred_path)

    eval_results = evaluate_re(results)
    eval_path = output_dir / "eval_results.json"
    with open(eval_path, "w") as f:
        json.dump(eval_results, f, indent=2)

    logger.info("=" * 60)
    logger.info("RESULTS (16-rel 100 batch)")
    logger.info("=" * 60)
    for bid, m in sorted(eval_results.items()):
        logger.info("  %-40s acc=%.4f (%3d/%3d) BCS=%.4f",
                    bid, m["accuracy"], m["correct"], m["total"], m["bcs"])

    logger.info("=" * 60)
    logger.info("Running bootstrap CI analysis (10000 resamples)...")
    ci = bootstrap_bcs_effect(eval_results, n_bootstrap=10000, seed=42)
    ci_path = output_dir / "bootstrap_ci.json"
    with open(ci_path, "w") as f:
        json.dump(ci, f, indent=2)
    logger.info("Saved bootstrap CI to %s", ci_path)

    logger.info("=" * 60)
    logger.info("BOOTSTRAP CI SUMMARY")
    logger.info("  n_batches: %d", ci["n_batches"])
    logger.info("  median BCS: %.4f", ci["median_bcs"])
    logger.info("  mean acc (low BCS): %.4f  mean acc (high BCS): %.4f",
                ci["mean_acc_low_bcs"], ci["mean_acc_high_bcs"])
    logger.info("  Δ = %+.2f pp  95%% CI [%+.2f, %+.2f] pp",
                ci["delta_pp"], ci["delta_ci_lower_pp"], ci["delta_ci_upper_pp"])
    logger.info("  Pearson r(BCS, acc) = %.4f  95%% CI [%.4f, %.4f]",
                ci["pearson_r_bcs_acc"], ci["pearson_r_ci_lower"], ci["pearson_r_ci_upper"])
    logger.info("=" * 60)

    results_summary = {
        "pool_size": 16,
        "count": config.get("count", 8),
        "n_batches": ci["n_batches"],
        "delta_pp": ci["delta_pp"],
        "delta_ci": [ci["delta_ci_lower_pp"], ci["delta_ci_upper_pp"]],
        "pearson_r": ci["pearson_r_bcs_acc"],
        "pearson_r_ci": [ci["pearson_r_ci_lower"], ci["pearson_r_ci_upper"]],
        "median_bcs": ci["median_bcs"],
        "mean_acc_low": ci["mean_acc_low_bcs"],
        "mean_acc_high": ci["mean_acc_high_bcs"],
    }
    with open(output_dir / "results.json", "w") as f:
        json.dump(results_summary, f, indent=2)
    logger.info("Saved results summary to %s", output_dir / "results.json")


def main():
    parser = argparse.ArgumentParser(description="FewRel 16-rel 100 batch study")
    parser.add_argument("--model_path", default="~/.cache/huggingface/qwen3-32b-fp8/")
    parser.add_argument("--types_file", default=str(BASE_DIR / "configs/fewrel_relation_types.json"))
    parser.add_argument("--sim_matrix_path",
                        default=str(BASE_DIR / "artifacts/fewrel_formal/relation_sim_matrix.pt"))
    parser.add_argument("--output_dir", default=str(BASE_DIR / "artifacts/fewrel_16rel_100batch"))
    parser.add_argument("--n_samples", type=int, default=DEFAULT_N_SAMPLES)
    parser.add_argument("--n_batches", type=int, default=DEFAULT_N_BATCHES)
    parser.add_argument("--count", type=int, default=DEFAULT_COUNT)
    parser.add_argument("--max_model_len", type=int, default=4096)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dry_run", action="store_true")
    parser.add_argument("--stage", choices=["preprocess", "extract", "all"], default="all")
    parser.add_argument("--preprocess_path", default=None)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    random.seed(args.seed)

    if args.stage == "preprocess":
        stage_preprocess(args)
    elif args.stage == "extract":
        stage_extract(args)
    elif args.stage == "all":
        preprocess_path = stage_preprocess(args)

        if args.dry_run:
            logger.info("DRY RUN - stopping before GPU extraction.")
            return

        logger.info("=== Launching extract subprocess (vLLM-first) ===")
        cmd = [sys.executable, str(Path(__file__).resolve()),
               "--stage", "extract",
               "--output_dir", args.output_dir,
               "--preprocess_path", preprocess_path]
        subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()

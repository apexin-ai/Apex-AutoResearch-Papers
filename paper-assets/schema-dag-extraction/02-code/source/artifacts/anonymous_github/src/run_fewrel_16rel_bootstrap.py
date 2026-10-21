#!/usr/bin/env python3
"""FewRel 16-rel bootstrap CI experiment.

Two-stage execution to avoid vLLM fork deadlock:
  --stage preprocess: CPU only (data, embeddings, batch config)
  --stage extract: GPU only (vLLM inference, incremental save)
  --stage all: runs preprocess, then launches extract as subprocess

Usage:
    python3 src/run_fewrel_16rel_bootstrap.py --stage all
    python3 src/run_fewrel_16rel_bootstrap.py --stage all --dry_run
    python3 src/run_fewrel_16rel_bootstrap.py --stage extract --resume
    python3 src/run_fewrel_16rel_bootstrap.py --analysis_only
"""
import argparse
import json
import logging
import random
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

logger = logging.getLogger(__name__)

BASE_DIR = Path(".")
OUTPUT_DIR = BASE_DIR / "artifacts" / "fewrel_16rel_bootstrap"


def stage_preprocess(args):
    sys.path.insert(0, str(BASE_DIR / "src"))
    from fewrel_utils import load_fewrel, get_all_relation_types, sample_balanced
    from compute_bcs import compute_similarity_matrix, compute_bcs
    from run_fewrel_pilot import compute_relation_embeddings_st

    all_samples = load_fewrel(data_path=str(BASE_DIR / "data/fewrel_parquet/val.parquet"))
    all_relations = get_all_relation_types(all_samples)
    logger.info("%d samples, %d relations", len(all_samples), len(all_relations))

    n_per_rel = args.n_samples // len(all_relations)
    samples = sample_balanced(all_samples, n_per_rel, seed=args.seed)
    logger.info("Balanced sample: %d (%d/rel)", len(samples), n_per_rel)

    with open(BASE_DIR / "configs/fewrel_relation_types.json") as f:
        pid2name = json.load(f)
    relation_defs = {name: name for name in pid2name.values()}

    logger.info("Computing MiniLM embeddings (CPU)...")
    embeddings = compute_relation_embeddings_st(pid2name)

    import torch
    sim_matrix, type_names, type_to_idx = compute_similarity_matrix(embeddings)

    active_types = sorted(t for t in type_names if t in set(all_relations))
    logger.info("Active types: %d", len(active_types))
    assert len(active_types) == 16, f"Expected 16, got {len(active_types)}"

    rng = random.Random(args.seed)
    batches = []
    for i in range(args.n_batches):
        types = rng.sample(active_types, args.batch_count)
        bcs = compute_bcs(types, sim_matrix, type_to_idx)
        batches.append({"batch_id": f"batch_{i:03d}", "types": types, "bcs": bcs})

    bcs_vals = [b["bcs"] for b in batches]
    logger.info("Generated %d batches: BCS [%.4f, %.4f], mean=%.4f",
                len(batches), min(bcs_vals), max(bcs_vals), np.mean(bcs_vals))

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    preprocess_config = {
        "samples": samples,
        "batches": batches,
        "relation_defs": relation_defs,
        "model_path": args.model_path,
        "max_model_len": args.max_model_len,
        "gpu_memory_utilization": args.gpu_memory_utilization,
    }
    preprocess_path = OUTPUT_DIR / "preprocess.json"
    with open(preprocess_path, "w") as f:
        json.dump(preprocess_config, f, ensure_ascii=False)

    with open(OUTPUT_DIR / "batch_config.json", "w") as f:
        json.dump(batches, f, indent=2)
    torch.save({"sim_matrix": sim_matrix, "type_names": type_names, "type_to_idx": type_to_idx},
               OUTPUT_DIR / "relation_sim_matrix.pt")

    total_inf = sum(
        sum(1 for s in samples if s["relation_type"] in set(b["types"]))
        for b in batches
    )
    logger.info("Preprocess done: %d batches, ~%d inferences", len(batches), total_inf)

    return str(preprocess_path)


def stage_extract(args):
    """GPU stage: vLLM imported first, no prior CUDA/torch state."""
    sys.path.insert(0, str(BASE_DIR / "src"))
    from run_extraction import build_json_schema_re, build_prompt_v2_re
    from vllm import LLM, SamplingParams
    from vllm.sampling_params import StructuredOutputsParams

    preprocess_path = args.preprocess_path or str(OUTPUT_DIR / "preprocess.json")
    with open(preprocess_path) as f:
        config = json.load(f)

    samples = config["samples"]
    batches = config["batches"]
    relation_defs = config["relation_defs"]

    llm = LLM(model=config["model_path"], max_model_len=config["max_model_len"],
              trust_remote_code=True, dtype="bfloat16",
              gpu_memory_utilization=config["gpu_memory_utilization"],
              enforce_eager=True, disable_log_stats=True)

    tokenizer = llm.get_tokenizer()
    model_id = getattr(tokenizer, 'name_or_path', '') or config["model_path"]
    needs_chat = any(kw in model_id.lower() for kw in ['llama', 'mistral', 'gemma', 'phi'])

    incr_path = OUTPUT_DIR / "results_incremental.jsonl"
    pred_path = OUTPUT_DIR / "predictions_incremental.jsonl"

    completed = set()
    if args.resume and incr_path.exists():
        with open(incr_path) as f:
            for line in f:
                if line.strip():
                    completed.add(json.loads(line)["batch_id"])
        logger.info("Resuming: %d/%d batches already done", len(completed), len(batches))

    sample_id_map = {i: i for i in range(len(samples))}
    t_start = time.time()
    done_count = 0

    for bi, batch in enumerate(batches):
        bid = batch["batch_id"]
        if bid in completed:
            continue

        batch_types = batch["types"]
        batch_bcs = batch["bcs"]
        type_set = set(batch_types)
        batch_samples = [(i, s) for i, s in enumerate(samples) if s["relation_type"] in type_set]

        if not batch_samples:
            logger.warning("No samples for %s, skipping", bid)
            continue

        logger.info("[%d/%d] %s: %d types, BCS=%.4f, %d samples",
                    bi + 1, len(batches), bid, len(batch_types), batch_bcs, len(batch_samples))

        schema = build_json_schema_re(batch_types)
        structured = StructuredOutputsParams(json=schema)
        sp = SamplingParams(max_tokens=64, temperature=0.0, structured_outputs=structured)

        prompts, refs = [], []
        for si, s in batch_samples:
            p = build_prompt_v2_re(s["text"], s["head_entity"], s["tail_entity"],
                                   relation_defs, batch_types)
            prompts.append(p)
            refs.append((si, s))

        if needs_chat:
            prompts = [
                tokenizer.apply_chat_template(
                    [{"role": "user", "content": p}],
                    tokenize=False, add_generation_prompt=True)
                for p in prompts
            ]

        t0 = time.time()
        outputs = llm.generate(prompts, sp)
        elapsed = time.time() - t0

        correct = 0
        batch_preds = []
        for oi, output in enumerate(outputs):
            si, s = refs[oi]
            try:
                parsed = json.loads(output.outputs[0].text)
                pred = parsed.get("relation", "none")
            except json.JSONDecodeError:
                pred = "none"

            if pred == s["relation_type"]:
                correct += 1
            batch_preds.append({
                "sample_id": si,
                "batch_id": bid,
                "batch_bcs": batch_bcs,
                "prediction": pred,
                "ground_truth": s["relation_type"],
            })

        acc = correct / len(batch_samples)
        done_count += 1
        total_elapsed = time.time() - t_start
        remaining = sum(1 for b in batches[bi+1:] if b["batch_id"] not in completed)
        eta = (total_elapsed / done_count * remaining) if done_count > 0 else 0

        logger.info("  acc=%.4f (%d/%d) %.1fs | ETA: %.0f min",
                    acc, correct, len(batch_samples), elapsed, eta / 60)

        with open(incr_path, "a") as f:
            f.write(json.dumps({
                "batch_id": bid, "bcs": batch_bcs, "accuracy": acc,
                "correct": correct, "total": len(batch_samples),
                "types": batch_types, "elapsed_s": round(elapsed, 1),
            }) + "\n")

        with open(pred_path, "a") as f:
            for rec in batch_preds:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    all_results = []
    with open(incr_path) as f:
        for line in f:
            if line.strip():
                all_results.append(json.loads(line))

    with open(OUTPUT_DIR / "results.json", "w") as f:
        json.dump(all_results, f, indent=2)
    logger.info("Saved %d batch results to results.json", len(all_results))

    run_analysis(all_results, args.delta_80_pp, args.n_bootstrap, args.seed)


def run_analysis(batch_results, delta_80_pp, n_bootstrap=1000, seed=42):
    accs = np.array([b["accuracy"] for b in batch_results])
    bcs = np.array([b["bcs"] for b in batch_results])
    n = len(accs)
    rng = np.random.RandomState(seed)

    def compute_delta(a, b):
        q25, q75 = np.percentile(b, 25), np.percentile(b, 75)
        low, high = a[b <= q25], a[b >= q75]
        if len(low) == 0 or len(high) == 0:
            return np.nan
        return high.mean() - low.mean()

    point_delta = compute_delta(accs, bcs)

    boot_deltas = np.empty(n_bootstrap)
    for i in range(n_bootstrap):
        idx = rng.randint(0, n, size=n)
        boot_deltas[i] = compute_delta(accs[idx], bcs[idx])

    finite_deltas = boot_deltas[~np.isnan(boot_deltas)]

    q25, q75 = np.percentile(bcs, 25), np.percentile(bcs, 75)
    low_mask, high_mask = bcs <= q25, bcs >= q75

    delta_ci = {
        "delta_pp": round(float(point_delta * 100), 2),
        "ci_lower_pp": round(float(np.percentile(finite_deltas, 2.5) * 100), 2),
        "ci_upper_pp": round(float(np.percentile(finite_deltas, 97.5) * 100), 2),
        "low_bcs_mean_acc": round(float(accs[low_mask].mean()), 4),
        "high_bcs_mean_acc": round(float(accs[high_mask].mean()), 4),
        "low_bcs_n": int(low_mask.sum()),
        "high_bcs_n": int(high_mask.sum()),
        "bcs_q25": round(float(q25), 4),
        "bcs_q75": round(float(q75), 4),
        "bcs_range": [round(float(bcs.min()), 4), round(float(bcs.max()), 4)],
        "n_batches": n,
        "n_bootstrap": n_bootstrap,
        "n_valid": len(finite_deltas),
    }

    if abs(point_delta) > 1e-6:
        ratio_point = delta_80_pp / (point_delta * 100)
        boot_ratio_vals = delta_80_pp / (finite_deltas * 100)
        valid = boot_ratio_vals[np.isfinite(boot_ratio_vals) & (np.abs(boot_ratio_vals) < 100)]
        amplification = {
            "ratio": round(float(ratio_point), 2),
            "ci_lower": round(float(np.percentile(valid, 2.5)), 2) if len(valid) > 0 else None,
            "ci_upper": round(float(np.percentile(valid, 97.5)), 2) if len(valid) > 0 else None,
            "delta_16_pp": round(float(point_delta * 100), 2),
            "delta_80_pp": delta_80_pp,
            "n_valid_ratios": int(len(valid)),
        }
    else:
        amplification = {"ratio": None, "note": "delta_16 too close to zero"}

    result = {
        "delta_bcs": delta_ci,
        "amplification": amplification,
        "summary": {
            "mean_accuracy": round(float(accs.mean()), 4),
            "std_accuracy": round(float(accs.std()), 4),
            "mean_bcs": round(float(bcs.mean()), 4),
            "pearson_bcs_acc": round(float(np.corrcoef(bcs, accs)[0, 1]), 4),
        },
    }

    with open(OUTPUT_DIR / "bootstrap_ci.json", "w") as f:
        json.dump(result, f, indent=2)

    logger.info("=" * 60)
    logger.info("BOOTSTRAP CI RESULTS (B=%d)", n_bootstrap)
    logger.info("=" * 60)
    logger.info("  delta_BCS = %+.2fpp  95%% CI [%+.2f, %+.2f]pp",
                delta_ci["delta_pp"], delta_ci["ci_lower_pp"], delta_ci["ci_upper_pp"])
    logger.info("  Low BCS (Q1, n=%d): mean_acc=%.4f",
                delta_ci["low_bcs_n"], delta_ci["low_bcs_mean_acc"])
    logger.info("  High BCS (Q4, n=%d): mean_acc=%.4f",
                delta_ci["high_bcs_n"], delta_ci["high_bcs_mean_acc"])
    if amplification.get("ratio") is not None:
        logger.info("  Amplification: %.2fx  95%% CI [%.2f, %.2f]x",
                    amplification["ratio"], amplification["ci_lower"], amplification["ci_upper"])
    logger.info("  Overall: mean_acc=%.4f, r(BCS,acc)=%.4f",
                result["summary"]["mean_accuracy"], result["summary"]["pearson_bcs_acc"])

    return result


def main():
    parser = argparse.ArgumentParser(description="FewRel 16-rel bootstrap CI")
    parser.add_argument("--model_path", default="~/.cache/huggingface/qwen3-32b-fp8/")
    parser.add_argument("--n_batches", type=int, default=100)
    parser.add_argument("--batch_count", type=int, default=8)
    parser.add_argument("--n_samples", type=int, default=1000)
    parser.add_argument("--n_bootstrap", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--gpu_memory_utilization", type=float, default=0.85)
    parser.add_argument("--max_model_len", type=int, default=4096)
    parser.add_argument("--delta_80_pp", type=float, default=-31.2)
    parser.add_argument("--dry_run", action="store_true")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--analysis_only", action="store_true")
    parser.add_argument("--stage", choices=["preprocess", "extract", "all"], default="all")
    parser.add_argument("--preprocess_path", default=None)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if args.analysis_only:
        results = []
        with open(OUTPUT_DIR / "results_incremental.jsonl") as f:
            for line in f:
                if line.strip():
                    results.append(json.loads(line))
        logger.info("Loaded %d batch results", len(results))
        run_analysis(results, args.delta_80_pp, args.n_bootstrap, args.seed)
        return

    if args.stage == "preprocess":
        stage_preprocess(args)
    elif args.stage == "extract":
        stage_extract(args)
    elif args.stage == "all":
        preprocess_path = stage_preprocess(args)

        if args.dry_run:
            logger.info("DRY RUN — stopping before GPU extraction.")
            return

        logger.info("=== Launching extract subprocess (vLLM-first) ===")
        cmd = [sys.executable, str(Path(__file__).resolve()),
               "--stage", "extract",
               "--preprocess_path", preprocess_path,
               "--delta_80_pp", str(args.delta_80_pp),
               "--n_bootstrap", str(args.n_bootstrap),
               "--seed", str(args.seed)]
        if args.resume:
            cmd.append("--resume")
        subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()

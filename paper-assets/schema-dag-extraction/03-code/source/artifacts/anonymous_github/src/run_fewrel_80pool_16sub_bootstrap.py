#!/usr/bin/env python3
"""FewRel 80-pool 16-type subset bootstrap CI experiment (reviewer MW1 response).

Eliminates cross-pool confound: samples 16-type subsets from the full
80-relation pool (train+val), constructs 8-type batches, and tests
BCS-accuracy relationship via bootstrap CI on quartile groups.

For each of 100 batches:
  1. Sample 16 types from the 80-relation pool (independent per batch)
  2. Select 8 types from those 16 to form the batch
  3. Compute BCS (mean pairwise cosine similarity) for the 8 types
  4. Run RE inference on balanced samples matching those 8 types

Three-stage execution (avoids vLLM fork deadlock):
  --stage preprocess : CPU only — data, embeddings, batch config, BCS
  --stage extract    : GPU only — vLLM inference, incremental save
  --stage analyze    : CPU only — bootstrap CI on saved results
  --stage all        : preprocess → extract subprocess → analyze

Input:
  data/fewrel_parquet/{train,val}.parquet (80 relations, 56000 samples)
  artifacts/fewrel_formal_full/relation_sim_matrix.pt (80×80 MiniLM cosine sim)

Output:
  artifacts/fewrel_80pool_16sub/preprocess.json
  artifacts/fewrel_80pool_16sub/batch_config.json
  artifacts/fewrel_80pool_16sub/results_incremental.jsonl
  artifacts/fewrel_80pool_16sub/predictions_incremental.jsonl
  artifacts/fewrel_80pool_16sub/bootstrap_ci.json
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
from scipy.stats import linregress

logger = logging.getLogger(__name__)

BASE_DIR = Path(".")
OUTPUT_DIR = BASE_DIR / "artifacts" / "fewrel_80pool_16sub"


def compute_bcs_mean(type_subset, sim_matrix, type_to_idx):
    """BCS = mean pairwise cosine similarity among batch types."""
    if len(type_subset) < 2:
        return 0.0
    indices = [type_to_idx[t] for t in type_subset]
    total = 0.0
    count = 0
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            total += sim_matrix[indices[i], indices[j]].item()
            count += 1
    return total / count


def stage_preprocess(args):
    sys.path.insert(0, str(BASE_DIR / "src"))
    from fewrel_utils import load_fewrel, get_all_relation_types, sample_balanced
    import torch

    train_samples = load_fewrel(data_path=str(BASE_DIR / "data/fewrel_parquet/train.parquet"))
    val_samples = load_fewrel(data_path=str(BASE_DIR / "data/fewrel_parquet/val.parquet"))
    all_samples = train_samples + val_samples
    all_relations = get_all_relation_types(all_samples)
    logger.info("%d samples, %d relations", len(all_samples), len(all_relations))
    assert len(all_relations) == 80, f"Expected 80 relations, got {len(all_relations)}"

    n_per_rel = args.n_samples // len(all_relations)
    samples = sample_balanced(all_samples, n_per_rel, seed=args.seed)
    logger.info("Balanced sample: %d (%d/rel)", len(samples), n_per_rel)

    sim_data = torch.load(
        BASE_DIR / "artifacts/fewrel_formal_full/relation_sim_matrix.pt",
        map_location="cpu",
    )
    sim_matrix = sim_data["sim_matrix"]
    type_names = sim_data["type_names"]
    type_to_idx = sim_data["type_to_idx"]
    logger.info("Loaded 80-rel sim matrix: %s", sim_matrix.shape)

    active_types = sorted(t for t in type_names if t in set(all_relations))
    logger.info("Active types in sim matrix: %d", len(active_types))
    missing = set(all_relations) - set(type_names)
    if missing:
        logger.error("Relations missing from sim matrix: %s", missing)
        raise ValueError(f"{len(missing)} relations missing from sim matrix")
    assert len(active_types) == 80

    with open(BASE_DIR / "configs/fewrel_relation_types.json") as f:
        pid2name = json.load(f)
    relation_defs = {name: name for name in pid2name.values()}

    rng = random.Random(args.seed)
    batches = []
    for i in range(args.n_batches):
        pool_16 = rng.sample(active_types, 16)
        batch_8 = rng.sample(pool_16, 8)
        bcs = compute_bcs_mean(batch_8, sim_matrix, type_to_idx)
        batches.append({
            "batch_id": f"batch_{i:03d}",
            "pool_16": sorted(pool_16),
            "types": sorted(batch_8),
            "bcs": round(bcs, 6),
        })

    bcs_vals = [b["bcs"] for b in batches]
    logger.info(
        "Generated %d batches: BCS [%.4f, %.4f], mean=%.4f, std=%.4f",
        len(batches), min(bcs_vals), max(bcs_vals),
        np.mean(bcs_vals), np.std(bcs_vals),
    )

    sorted_bcs = sorted(bcs_vals)
    q25 = np.percentile(sorted_bcs, 25)
    q50 = np.percentile(sorted_bcs, 50)
    q75 = np.percentile(sorted_bcs, 75)
    logger.info("BCS quartiles: Q1<%.4f, Q2<%.4f, Q3<%.4f", q25, q50, q75)

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

    total_inf = sum(
        sum(1 for s in samples if s["relation_type"] in set(b["types"]))
        for b in batches
    )
    logger.info("Preprocess done: %d batches, ~%d total inferences", len(batches), total_inf)
    est_min = total_inf / 500.0
    logger.info("Estimated GPU time: ~%.0f min (at ~500 samples/min with vLLM batching)", est_min)

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

    llm = LLM(
        model=config["model_path"],
        max_model_len=config["max_model_len"],
        trust_remote_code=True,
        dtype="bfloat16",
        gpu_memory_utilization=config["gpu_memory_utilization"],
        enforce_eager=True,
        disable_log_stats=True,
    )

    tokenizer = llm.get_tokenizer()
    model_id = getattr(tokenizer, "name_or_path", "") or config["model_path"]
    needs_chat = any(kw in model_id.lower() for kw in ["llama", "mistral", "gemma", "phi"])

    incr_path = OUTPUT_DIR / "results_incremental.jsonl"
    pred_path = OUTPUT_DIR / "predictions_incremental.jsonl"

    completed = set()
    if args.resume and incr_path.exists():
        with open(incr_path) as f:
            for line in f:
                if line.strip():
                    completed.add(json.loads(line)["batch_id"])
        logger.info("Resuming: %d/%d batches done", len(completed), len(batches))

    t_start = time.time()

    for bi, batch in enumerate(batches):
        bid = batch["batch_id"]
        if bid in completed:
            continue

        batch_types = batch["types"]
        batch_bcs = batch["bcs"]
        type_set = set(batch_types)
        batch_samples = [
            (i, s) for i, s in enumerate(samples) if s["relation_type"] in type_set
        ]

        if not batch_samples:
            logger.warning("No samples for %s, skipping", bid)
            continue

        logger.info(
            "[%d/%d] %s: %d types, BCS=%.4f, %d samples",
            bi + 1, len(batches), bid, len(batch_types), batch_bcs, len(batch_samples),
        )

        schema = build_json_schema_re(batch_types)
        structured = StructuredOutputsParams(json=schema)
        sp = SamplingParams(max_tokens=64, temperature=0.0, structured_outputs=structured)

        prompts, refs = [], []
        for si, s in batch_samples:
            p = build_prompt_v2_re(
                s["text"], s["head_entity"], s["tail_entity"],
                relation_defs, batch_types,
            )
            prompts.append(p)
            refs.append((si, s))

        if needs_chat:
            prompts = [
                tokenizer.apply_chat_template(
                    [{"role": "user", "content": p}],
                    tokenize=False,
                    add_generation_prompt=True,
                )
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
                "ground_truth": s["relation_type"],
                "prediction": pred,
                "batch_id": bid,
                "batch_types": batch_types,
                "batch_bcs": batch_bcs,
            })

        acc = correct / len(batch_samples) if batch_samples else 0.0
        batch_result = {
            "batch_id": bid,
            "pool_16": batch.get("pool_16", []),
            "types": batch_types,
            "bcs": batch_bcs,
            "accuracy": acc,
            "correct": correct,
            "total": len(batch_samples),
            "latency_s": round(elapsed, 2),
        }

        with open(incr_path, "a") as f:
            f.write(json.dumps(batch_result, ensure_ascii=False) + "\n")
        with open(pred_path, "a") as f:
            for p in batch_preds:
                f.write(json.dumps(p, ensure_ascii=False) + "\n")

        elapsed_total = time.time() - t_start
        remaining = (len(batches) - bi - 1) * (elapsed_total / (bi + 1 - len(completed)))
        logger.info(
            "  acc=%.4f (%d/%d), %.1fs, elapsed=%.0fs, ETA=%.0fs",
            acc, correct, len(batch_samples), elapsed, elapsed_total, remaining,
        )

    results = []
    with open(incr_path) as f:
        for line in f:
            if line.strip():
                results.append(json.loads(line))
    logger.info("All %d batches done. Running analysis.", len(results))
    run_analysis(results, args.n_bootstrap, args.seed)


def run_analysis(results, n_bootstrap=1000, seed=42):
    """Bootstrap CI analysis: quartile grouping on BCS, delta(Q4-Q1)."""
    rng = np.random.RandomState(seed)

    bcs = np.array([r["bcs"] for r in results])
    accs = np.array([r["accuracy"] for r in results])

    q25, q50, q75 = np.percentile(bcs, [25, 50, 75])

    q1_mask = bcs <= q25
    q2_mask = (bcs > q25) & (bcs <= q50)
    q3_mask = (bcs > q50) & (bcs <= q75)
    q4_mask = bcs > q75

    quartile_stats = {}
    for qname, mask in [
        ("Q1_low", q1_mask), ("Q2", q2_mask),
        ("Q3", q3_mask), ("Q4_high", q4_mask),
    ]:
        qacc = accs[mask]
        qbcs = bcs[mask]
        if len(qacc) == 0:
            quartile_stats[qname] = {"n": 0}
            continue
        boot_means = [
            float(rng.choice(qacc, size=len(qacc), replace=True).mean())
            for _ in range(n_bootstrap)
        ]
        ci_l, ci_u = np.percentile(boot_means, [2.5, 97.5])
        quartile_stats[qname] = {
            "n": int(mask.sum()),
            "mean_acc": round(float(qacc.mean()), 4),
            "std_acc": round(float(qacc.std()), 4),
            "acc_ci_95": [round(ci_l, 4), round(ci_u, 4)],
            "mean_bcs": round(float(qbcs.mean()), 4),
            "bcs_range": [round(float(qbcs.min()), 4), round(float(qbcs.max()), 4)],
        }

    q1_accs = accs[q1_mask]
    q4_accs = accs[q4_mask]
    observed_delta = float(q4_accs.mean() - q1_accs.mean())

    boot_deltas = []
    for _ in range(n_bootstrap):
        b_q1 = rng.choice(q1_accs, size=len(q1_accs), replace=True)
        b_q4 = rng.choice(q4_accs, size=len(q4_accs), replace=True)
        boot_deltas.append(float(b_q4.mean() - b_q1.mean()))

    boot_deltas = np.array(boot_deltas)
    ci_lower, ci_upper = np.percentile(boot_deltas, [2.5, 97.5])

    delta_ci = {
        "delta_pp": round(observed_delta * 100, 2),
        "ci_lower_pp": round(ci_lower * 100, 2),
        "ci_upper_pp": round(ci_upper * 100, 2),
        "low_bcs_n": int(q1_mask.sum()),
        "low_bcs_mean_acc": round(float(q1_accs.mean()), 4),
        "high_bcs_n": int(q4_mask.sum()),
        "high_bcs_mean_acc": round(float(q4_accs.mean()), 4),
    }

    pearson_r = float(np.corrcoef(bcs, accs)[0, 1]) if len(bcs) > 2 else 0.0

    slope, intercept, r_value_lr, p_value_lr, stderr_lr = linregress(bcs, accs)
    boot_rng = np.random.default_rng(seed)
    n_pts = len(bcs)
    boot_slopes = []
    for _ in range(n_bootstrap):
        idx = boot_rng.choice(n_pts, n_pts, replace=True)
        s, _, _, _, _ = linregress(bcs[idx], accs[idx])
        boot_slopes.append(s)
    slope_ci_lower, slope_ci_upper = np.percentile(boot_slopes, [2.5, 97.5])
    regression_result = {
        "slope": round(float(slope), 6),
        "intercept": round(float(intercept), 6),
        "r_value": round(float(r_value_lr), 4),
        "p_value": float(p_value_lr),
        "stderr": round(float(stderr_lr), 6),
        "bootstrap_ci_95": [round(float(slope_ci_lower), 6), round(float(slope_ci_upper), 6)],
    }

    result = {
        "delta_bcs": delta_ci,
        "quartile_stats": quartile_stats,
        "summary": {
            "mean_accuracy": round(float(accs.mean()), 4),
            "std_accuracy": round(float(accs.std()), 4),
            "mean_bcs": round(float(bcs.mean()), 4),
            "std_bcs": round(float(bcs.std()), 4),
            "pearson_bcs_acc": round(pearson_r, 4),
            "n_batches": len(results),
        },
        "regression_slope": regression_result,
    }

    with open(OUTPUT_DIR / "bootstrap_ci.json", "w") as f:
        json.dump(result, f, indent=2)

    logger.info("=" * 60)
    logger.info("BOOTSTRAP CI RESULTS (B=%d)", n_bootstrap)
    logger.info("=" * 60)
    logger.info(
        "  Δ(Q4-Q1) = %+.2fpp  95%% CI [%+.2f, %+.2f]pp",
        delta_ci["delta_pp"], delta_ci["ci_lower_pp"], delta_ci["ci_upper_pp"],
    )
    for qname, qs in quartile_stats.items():
        if qs["n"] == 0:
            continue
        logger.info(
            "  %s (n=%d): acc=%.4f [%.4f, %.4f], BCS=%.4f",
            qname, qs["n"], qs["mean_acc"],
            qs["acc_ci_95"][0], qs["acc_ci_95"][1], qs["mean_bcs"],
        )
    logger.info(
        "  Overall: mean_acc=%.4f, r(BCS,acc)=%.4f",
        result["summary"]["mean_accuracy"], result["summary"]["pearson_bcs_acc"],
    )
    logger.info(
        "  Regression: slope=%.4f [%.4f, %.4f], p=%.2e",
        regression_result["slope"],
        regression_result["bootstrap_ci_95"][0],
        regression_result["bootstrap_ci_95"][1],
        regression_result["p_value"],
    )

    return result


def main():
    parser = argparse.ArgumentParser(
        description="FewRel 80-pool 16-type subset bootstrap CI"
    )
    parser.add_argument("--model_path", default="~/.cache/huggingface/qwen3-32b-fp8/")
    parser.add_argument("--n_batches", type=int, default=100)
    parser.add_argument("--n_samples", type=int, default=960)
    parser.add_argument("--n_bootstrap", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--gpu_memory_utilization", type=float, default=0.95)
    parser.add_argument("--max_model_len", type=int, default=4096)
    parser.add_argument("--dry_run", action="store_true")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--analysis_only", action="store_true")
    parser.add_argument(
        "--stage", choices=["preprocess", "extract", "analyze", "all"], default="all"
    )
    parser.add_argument("--preprocess_path", default=None)
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s"
    )
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if args.analysis_only:
        results = []
        with open(OUTPUT_DIR / "results_incremental.jsonl") as f:
            for line in f:
                if line.strip():
                    results.append(json.loads(line))
        logger.info("Loaded %d batch results", len(results))
        run_analysis(results, args.n_bootstrap, args.seed)
        return

    if args.stage == "preprocess":
        stage_preprocess(args)
    elif args.stage == "extract":
        stage_extract(args)
    elif args.stage == "analyze":
        results = []
        with open(OUTPUT_DIR / "results_incremental.jsonl") as f:
            for line in f:
                if line.strip():
                    results.append(json.loads(line))
        logger.info("Loaded %d batch results", len(results))
        run_analysis(results, args.n_bootstrap, args.seed)
    elif args.stage == "all":
        preprocess_path = stage_preprocess(args)

        if args.dry_run:
            logger.info("DRY RUN — stopping before GPU extraction.")
            return

        logger.info("=== Launching extract subprocess (vLLM-first) ===")
        cmd = [
            sys.executable,
            str(Path(__file__).resolve()),
            "--stage", "extract",
            "--preprocess_path", preprocess_path,
            "--n_bootstrap", str(args.n_bootstrap),
            "--seed", str(args.seed),
        ]
        if args.resume:
            cmd.append("--resume")
        subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()

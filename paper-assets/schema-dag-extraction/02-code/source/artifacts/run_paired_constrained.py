#!/usr/bin/env python3
"""Paired Constrained Decoding on the same 25 batches as the unconstrained ablation.

Runs constrained decoding (JSON enum constraint) on the exact same 25 batch
type sets used in unconstrained_decoding_ablation_n25, producing paired
comparison data for BCS-accuracy correlation analysis.

Two-stage execution:
    python scripts/run_paired_constrained.py --stage all
    python scripts/run_paired_constrained.py --stage extract [--resume]
    python scripts/run_paired_constrained.py --analysis_only
"""
import argparse
import json
import logging
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

import numpy as np

logger = logging.getLogger(__name__)

BASE_DIR = Path("/root/schema-dag-extraction")
OUTPUT_DIR = BASE_DIR / "artifacts" / "exp_paired_constrained"
UNCONSTRAINED_DIR = BASE_DIR / "artifacts" / "unconstrained_decoding_ablation_n25"
BATCH_GROUPS_PATH = UNCONSTRAINED_DIR / "batch_groups.json"
BATCH_CONFIG_PATH = BASE_DIR / "artifacts" / "fewrel_formal_full" / "batch_config_exp2.json"
DEFAULT_N_SAMPLES = 1000


def load_batch_groups():
    with open(BATCH_GROUPS_PATH) as f:
        groups = json.load(f)
    return groups["low"], groups["high"]


def stage_preprocess(args):
    sys.path.insert(0, str(BASE_DIR / "src"))
    from fewrel_utils import load_fewrel, get_all_relation_types, sample_balanced

    logger.info("Loading FewRel data (train+val for 80 relations)...")
    all_samples = []
    for dp in [BASE_DIR / "data/fewrel_parquet/train.parquet",
               BASE_DIR / "data/fewrel_parquet/val.parquet"]:
        all_samples.extend(load_fewrel(data_path=str(dp)))
    all_relations = get_all_relation_types(all_samples)
    logger.info("%d samples, %d relations", len(all_samples), len(all_relations))

    n_per_rel = args.n_samples // len(all_relations)
    samples = sample_balanced(all_samples, n_per_rel, seed=args.seed)
    logger.info("Balanced sample: %d (%d/rel)", len(samples), n_per_rel)

    with open(BASE_DIR / "configs/fewrel_relation_types.json") as f:
        pid2name = json.load(f)
    relation_defs = {name: name for name in pid2name.values()}

    low_group, high_group = load_batch_groups()

    batch_list = []
    for i, b in enumerate(low_group):
        batch_list.append({
            "batch_id": f"low_{i}",
            "types": b["types"],
            "bcs": b["bcs"],
            "group": "low",
            "source": b.get("source", ""),
        })
    for i, b in enumerate(high_group):
        batch_list.append({
            "batch_id": f"high_{i}",
            "types": b["types"],
            "bcs": b["bcs"],
            "group": "high",
            "source": b.get("source", ""),
        })

    logger.info("Low BCS group (%d batches):", len(low_group))
    for i, b in enumerate(low_group):
        logger.info("  low_%d: BCS=%.4f", i, b["bcs"])
    logger.info("High BCS group (%d batches):", len(high_group))
    for i, b in enumerate(high_group):
        logger.info("  high_%d: BCS=%.4f", i, b["bcs"])

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    preprocess_config = {
        "samples": samples,
        "batch_list": batch_list,
        "relation_defs": relation_defs,
        "model_path": args.model_path,
        "max_model_len": args.max_model_len,
        "gpu_memory_utilization": args.gpu_memory_utilization,
    }
    preprocess_path = OUTPUT_DIR / "preprocess.json"
    with open(preprocess_path, "w") as f:
        json.dump(preprocess_config, f, ensure_ascii=False)

    with open(OUTPUT_DIR / "batch_groups.json", "w") as f:
        json.dump({"low": low_group, "high": high_group}, f, indent=2)

    total_inf = 0
    for b in batch_list:
        type_set = set(b["types"])
        n_match = sum(1 for s in samples if s["relation_type"] in type_set)
        total_inf += n_match
        logger.info("  %s: %d eligible samples", b["batch_id"], n_match)
    logger.info("Total inferences: %d, ~%.0f min (@0.15s/sample)",
                total_inf, total_inf * 0.15 / 60)

    if args.dry_run:
        logger.info("DRY RUN — stopping before GPU extraction.")
        return None

    return str(preprocess_path)


def stage_extract(args):
    sys.path.insert(0, str(BASE_DIR / "src"))
    from run_extraction import build_json_schema_re, build_prompt_v2_re
    from vllm import LLM, SamplingParams
    from vllm.sampling_params import StructuredOutputsParams

    preprocess_path = args.preprocess_path or str(OUTPUT_DIR / "preprocess.json")
    with open(preprocess_path) as f:
        config = json.load(f)

    samples = config["samples"]
    batch_list = config["batch_list"]
    relation_defs = config["relation_defs"]
    model_path = config["model_path"]

    results_path = OUTPUT_DIR / "results_incremental.jsonl"
    completed_batches = set()
    existing_results = []
    if args.resume and results_path.exists():
        with open(results_path) as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    existing_results.append(r)
                    completed_batches.add(r["batch_id"])
        logger.info("Resumed: %d results, %d completed batches",
                     len(existing_results), len(completed_batches))

    remaining = [b for b in batch_list if b["batch_id"] not in completed_batches]
    if not remaining:
        logger.info("All batches completed. Running analysis only.")
        run_analysis(existing_results, args.n_bootstrap, args.seed)
        return

    logger.info("Loading vLLM: %s", model_path)
    llm = LLM(
        model=model_path,
        max_model_len=config["max_model_len"],
        trust_remote_code=True,
        dtype="bfloat16",
        gpu_memory_utilization=config.get("gpu_memory_utilization", 0.90),
        enforce_eager=True,
        disable_log_stats=True,
    )

    tokenizer = llm.get_tokenizer()
    _model_id = getattr(tokenizer, 'name_or_path', '') or model_path
    _needs_chat_template = any(kw in _model_id.lower() for kw in ['llama', 'mistral', 'gemma', 'phi'])
    if _needs_chat_template:
        logger.info("Chat template enabled for: %s", _model_id)

    all_results = list(existing_results)

    for bi, batch in enumerate(remaining):
        batch_id = batch["batch_id"]
        batch_types = batch["types"]
        batch_bcs = batch["bcs"]
        group = batch["group"]
        type_set = set(batch_types)

        batch_samples = [s for s in samples if s["relation_type"] in type_set]
        if not batch_samples:
            logger.warning("No samples for batch %s — skipping", batch_id)
            continue

        logger.info("[%d/%d] %s (%s): %d types, BCS=%.4f, %d samples",
                    bi + 1, len(remaining), batch_id, group,
                    len(batch_types), batch_bcs, len(batch_samples))

        # CONSTRAINED: enum constraint on relation field
        schema = build_json_schema_re(batch_types)
        structured = StructuredOutputsParams(json=schema)
        sampling_params = SamplingParams(
            max_tokens=64, temperature=0.0, seed=42,
            structured_outputs=structured,
        )

        prompts = []
        sample_refs = []
        for s in batch_samples:
            p = build_prompt_v2_re(
                s["text"], s["head_entity"], s["tail_entity"],
                relation_defs, batch_types,
            )
            prompts.append(p)
            sample_refs.append(s)

        if _needs_chat_template:
            prompts = [
                tokenizer.apply_chat_template(
                    [{"role": "user", "content": p}],
                    tokenize=False, add_generation_prompt=True,
                ) for p in prompts
            ]

        t0 = time.time()
        outputs = llm.generate(prompts, sampling_params)
        elapsed = time.time() - t0

        batch_results = []
        for oi, output in enumerate(outputs):
            s = sample_refs[oi]
            gen_text = output.outputs[0].text
            try:
                parsed = json.loads(gen_text)
                pred_rel = parsed.get("relation", "none")
            except json.JSONDecodeError:
                logger.warning("JSON parse failed for %s sample %d: %s",
                               batch_id, oi, gen_text[:100])
                pred_rel = "none"

            r = {
                "batch_id": batch_id,
                "group": group,
                "batch_types": batch_types,
                "batch_bcs": batch_bcs,
                "prediction": pred_rel,
                "ground_truth": s["relation_type"],
                "head_entity": s["head_entity"],
                "tail_entity": s["tail_entity"],
                "prompt_tokens": len(output.prompt_token_ids),
                "gen_tokens": len(output.outputs[0].token_ids),
            }
            batch_results.append(r)
            all_results.append(r)

        with open(results_path, "a") as f:
            for r in batch_results:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

        correct = sum(1 for r in batch_results if r["prediction"] == r["ground_truth"])
        acc = correct / len(batch_results) if batch_results else 0
        logger.info("  acc=%.4f (%d/%d), %.1fs (%.2fs/sample)",
                    acc, correct, len(batch_results), elapsed,
                    elapsed / len(batch_samples))

    run_analysis(all_results, args.n_bootstrap, args.seed)


def run_analysis(results, n_bootstrap=10000, seed=42):
    from scipy import stats

    batch_stats = defaultdict(lambda: {"correct": 0, "total": 0, "bcs": 0.0,
                                       "group": "", "batch_types": []})
    for r in results:
        bid = r["batch_id"]
        s = batch_stats[bid]
        s["total"] += 1
        s["bcs"] = r["batch_bcs"]
        s["group"] = r.get("group", "")
        s["batch_types"] = r["batch_types"]
        if r["prediction"] == r["ground_truth"]:
            s["correct"] += 1

    eval_results = {}
    for bid, s in batch_stats.items():
        eval_results[bid] = {
            "accuracy": s["correct"] / s["total"] if s["total"] else 0.0,
            "correct": s["correct"],
            "total": s["total"],
            "bcs": s["bcs"],
            "group": s["group"],
            "batch_types": s["batch_types"],
        }

    # Collect per-batch data
    all_bcs = []
    all_accs = []
    low_accs, high_accs = [], []
    low_bcs_vals, high_bcs_vals = [], []

    for bid, m in sorted(eval_results.items()):
        all_bcs.append(m["bcs"])
        all_accs.append(m["accuracy"])
        if bid.startswith("low_"):
            low_accs.append(m["accuracy"])
            low_bcs_vals.append(m["bcs"])
        elif bid.startswith("high_"):
            high_accs.append(m["accuracy"])
            high_bcs_vals.append(m["bcs"])

    # Pearson r
    pearson_r, pearson_p = stats.pearsonr(all_bcs, all_accs)
    spearman_rho, spearman_p = stats.spearmanr(all_bcs, all_accs)

    # Bootstrap delta CI
    rng = np.random.RandomState(seed)
    low_arr = np.array(low_accs)
    high_arr = np.array(high_accs)
    observed_delta = low_arr.mean() - high_arr.mean()
    deltas = []
    for _ in range(n_bootstrap):
        low_s = rng.choice(low_arr, size=len(low_arr), replace=True)
        high_s = rng.choice(high_arr, size=len(high_arr), replace=True)
        deltas.append(low_s.mean() - high_s.mean())
    deltas = np.array(deltas)
    ci_lower = np.percentile(deltas, 2.5)
    ci_upper = np.percentile(deltas, 97.5)

    # Load unconstrained results for paired comparison
    unconstrained_eval_path = UNCONSTRAINED_DIR / "eval_results.json"
    paired_comparison = None
    if unconstrained_eval_path.exists():
        with open(unconstrained_eval_path) as f:
            unc_eval = json.load(f)
        unc_bcs = []
        unc_accs = []
        con_bcs = []
        con_accs = []
        for bid in sorted(eval_results.keys()):
            if bid in unc_eval:
                unc_bcs.append(unc_eval[bid]["bcs"])
                unc_accs.append(unc_eval[bid]["accuracy"])
                con_bcs.append(eval_results[bid]["bcs"])
                con_accs.append(eval_results[bid]["accuracy"])
        if len(unc_accs) >= 3:
            unc_r, unc_p = stats.pearsonr(unc_bcs, unc_accs)
            con_r, con_p = stats.pearsonr(con_bcs, con_accs)
            paired_comparison = {
                "n_paired_batches": len(unc_accs),
                "unconstrained_pearson_r": round(unc_r, 4),
                "unconstrained_pearson_p": round(unc_p, 6),
                "constrained_pearson_r": round(con_r, 4),
                "constrained_pearson_p": round(con_p, 6),
                "unconstrained_mean_acc": round(np.mean(unc_accs), 4),
                "constrained_mean_acc": round(np.mean(con_accs), 4),
                "acc_improvement": round(np.mean(con_accs) - np.mean(unc_accs), 4),
            }

    # Save results
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Per-batch JSONL (requested format)
    results_jsonl_path = OUTPUT_DIR / "results.jsonl"
    with open(results_jsonl_path, "w") as f:
        for bid, m in sorted(eval_results.items()):
            f.write(json.dumps({
                "batch_id": bid,
                "types": m["batch_types"],
                "bcs": round(m["bcs"], 4),
                "accuracy": round(m["accuracy"], 4),
                "n_samples": m["total"],
            }, ensure_ascii=False) + "\n")

    summary = {
        "n_batches": len(eval_results),
        "n_low": len(low_accs),
        "n_high": len(high_accs),
        "low_mean_acc": round(np.mean(low_accs), 4),
        "high_mean_acc": round(np.mean(high_accs), 4),
        "delta_pp": round(observed_delta * 100, 2),
        "ci_lower_pp": round(ci_lower * 100, 2),
        "ci_upper_pp": round(ci_upper * 100, 2),
        "pearson_r": round(pearson_r, 4),
        "pearson_p": round(pearson_p, 6),
        "spearman_rho": round(spearman_rho, 4),
        "spearman_p": round(spearman_p, 6),
        "paired_comparison": paired_comparison,
    }
    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    with open(OUTPUT_DIR / "eval_results.json", "w") as f:
        json.dump(eval_results, f, indent=2)

    # Logging
    logger.info("=" * 70)
    logger.info("RESULTS: Paired Constrained Decoding (n=25)")
    logger.info("=" * 70)
    for bid, m in sorted(eval_results.items()):
        logger.info("  %-12s acc=%.4f (%3d/%3d) BCS=%.4f [%s]",
                    bid, m["accuracy"], m["correct"], m["total"],
                    m["bcs"], m["group"])
    logger.info("-" * 70)
    logger.info("Low  BCS (n=%d): mean_acc=%.4f", len(low_accs), np.mean(low_accs))
    logger.info("High BCS (n=%d): mean_acc=%.4f", len(high_accs), np.mean(high_accs))
    logger.info("Delta(low-high) = %+.2fpp  95%% CI [%+.2f, %+.2f]pp",
                observed_delta * 100, ci_lower * 100, ci_upper * 100)
    logger.info("Pearson  r(BCS, acc) = %.4f  p=%.6f", pearson_r, pearson_p)
    logger.info("Spearman rho(BCS, acc) = %.4f  p=%.6f", spearman_rho, spearman_p)

    if paired_comparison:
        logger.info("-" * 70)
        logger.info("PAIRED COMPARISON (same 25 batches):")
        logger.info("  Unconstrained: Pearson r=%.4f (p=%.6f), mean_acc=%.4f",
                    paired_comparison["unconstrained_pearson_r"],
                    paired_comparison["unconstrained_pearson_p"],
                    paired_comparison["unconstrained_mean_acc"])
        logger.info("  Constrained:   Pearson r=%.4f (p=%.6f), mean_acc=%.4f",
                    paired_comparison["constrained_pearson_r"],
                    paired_comparison["constrained_pearson_p"],
                    paired_comparison["constrained_mean_acc"])
        logger.info("  Acc improvement: %+.2fpp",
                    paired_comparison["acc_improvement"] * 100)

    return summary


def main():
    parser = argparse.ArgumentParser(description="Paired Constrained Decoding n=25")
    parser.add_argument("--model_path",
                        default="/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/")
    parser.add_argument("--n_samples", type=int, default=DEFAULT_N_SAMPLES)
    parser.add_argument("--n_bootstrap", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--gpu_memory_utilization", type=float, default=0.90)
    parser.add_argument("--max_model_len", type=int, default=4096)
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

        logger.info("=== Launching extract subprocess ===")
        cmd = [sys.executable, str(Path(__file__).resolve()),
               "--stage", "extract",
               "--n_bootstrap", str(args.n_bootstrap),
               "--seed", str(args.seed)]
        if args.resume:
            cmd.append("--resume")
        subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()

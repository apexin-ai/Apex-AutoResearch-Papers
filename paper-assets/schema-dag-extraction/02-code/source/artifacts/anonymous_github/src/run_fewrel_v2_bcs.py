#!/usr/bin/env python3
"""FewRel v2 prompt BCS-controlled experiment (C1b).

Purpose: Verify Channel 2 (BCS → type confusion) holds under v2 anti-hallucination prompt.
Design:  count=8, 5 low-BCS batches + 5 high-BCS batches from 80-rel pool.
Batches: Reused from exp_fewrel_formal_80rel batch_config_exp2.json — all 27 count_8
         batches ranked by BCS, bottom 5 = low group, top 5 = high group.
Prompt:  v2 RE prompt (build_prompt_v2_re from run_extraction.py) — no offsets,
         adds "none" fallback, constrained JSON output.
Metric:  per-batch accuracy, Δ(low−high) mean ± bootstrap 95% CI.

Input:  FewRel train+val parquet (80 relations), batch_config_exp2.json, Qwen3-32B-FP8
Output: artifacts/fewrel_v2_bcs/ — results_incremental.jsonl, eval_results.json, bootstrap_ci.json

Two-stage execution to avoid vLLM fork deadlock:
    python3 src/run_fewrel_v2_bcs.py --stage all
    python3 src/run_fewrel_v2_bcs.py --stage all --dry_run
    python3 src/run_fewrel_v2_bcs.py --stage extract [--resume]
    python3 src/run_fewrel_v2_bcs.py --analysis_only
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

import numpy as np

logger = logging.getLogger(__name__)

BASE_DIR = Path(".")
OUTPUT_DIR = BASE_DIR / "artifacts" / "fewrel_v2_bcs"
# Reuse batch definitions from the formal 80-rel experiment
BATCH_CONFIG_PATH = BASE_DIR / "artifacts" / "fewrel_formal_full" / "batch_config_exp2.json"
N_LOW = 5
N_HIGH = 5
COUNT_KEY = "count_8"
DEFAULT_N_SAMPLES = 1000


def select_bcs_groups(batch_config_path, count_key="count_8", n_low=5, n_high=5):
    """Rank all count_8 batches by BCS, return bottom-n as low group and top-n as high."""
    with open(batch_config_path) as f:
        config = json.load(f)

    entry = config[count_key]
    all_batches = []

    if "low_bcs" in entry:
        all_batches.append({
            "types": entry["low_bcs"]["types"],
            "bcs": entry["low_bcs"]["bcs"],
            "source": "greedy_low",
        })
    if "high_bcs" in entry:
        all_batches.append({
            "types": entry["high_bcs"]["types"],
            "bcs": entry["high_bcs"]["bcs"],
            "source": "greedy_high",
        })
    for ri, rb in enumerate(entry.get("random", [])):
        all_batches.append({
            "types": rb["types"],
            "bcs": rb["bcs"],
            "source": f"random_{ri}",
        })

    all_batches.sort(key=lambda x: x["bcs"])

    low_group = all_batches[:n_low]
    high_group = all_batches[-n_high:]

    return low_group, high_group


def evaluate_re(results):
    """Per-batch accuracy from flat result list."""
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

    out = {}
    for bid, s in batch_stats.items():
        out[bid] = {
            "accuracy": s["correct"] / s["total"] if s["total"] else 0.0,
            "correct": s["correct"],
            "total": s["total"],
            "bcs": s["bcs"],
            "group": s["group"],
            "batch_types": s["batch_types"],
        }
    return out


def bootstrap_delta_ci(low_accs, high_accs, n_bootstrap=10000, seed=42):
    """Bootstrap 95% CI for Δ = mean(low_acc) − mean(high_acc)."""
    rng = np.random.RandomState(seed)
    low_accs = np.array(low_accs)
    high_accs = np.array(high_accs)

    observed_delta = low_accs.mean() - high_accs.mean()

    deltas = []
    for _ in range(n_bootstrap):
        low_sample = rng.choice(low_accs, size=len(low_accs), replace=True)
        high_sample = rng.choice(high_accs, size=len(high_accs), replace=True)
        deltas.append(low_sample.mean() - high_sample.mean())

    deltas = np.array(deltas)
    ci_lower = np.percentile(deltas, 2.5)
    ci_upper = np.percentile(deltas, 97.5)

    return {
        "delta_pp": round(observed_delta * 100, 2),
        "ci_lower_pp": round(ci_lower * 100, 2),
        "ci_upper_pp": round(ci_upper * 100, 2),
        "low_mean_acc": round(float(low_accs.mean()), 4),
        "high_mean_acc": round(float(high_accs.mean()), 4),
        "low_accs": [round(float(a), 4) for a in low_accs],
        "high_accs": [round(float(a), 4) for a in high_accs],
        "low_bcs_values": [],   # filled by caller
        "high_bcs_values": [],  # filled by caller
        "n_bootstrap": n_bootstrap,
    }


def stage_preprocess(args):
    """CPU stage: load data, select BCS groups, save preprocess config."""
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

    low_group, high_group = select_bcs_groups(BATCH_CONFIG_PATH, COUNT_KEY, N_LOW, N_HIGH)

    logger.info("Low BCS group (%d batches):", len(low_group))
    for i, b in enumerate(low_group):
        logger.info("  low_%d: BCS=%.4f (source=%s)", i, b["bcs"], b["source"])
    logger.info("High BCS group (%d batches):", len(high_group))
    for i, b in enumerate(high_group):
        logger.info("  high_%d: BCS=%.4f (source=%s)", i, b["bcs"], b["source"])

    batch_list = []
    for i, b in enumerate(low_group):
        batch_list.append({
            "batch_id": f"low_{i}",
            "types": b["types"],
            "bcs": b["bcs"],
            "group": "low",
            "source": b["source"],
        })
    for i, b in enumerate(high_group):
        batch_list.append({
            "batch_id": f"high_{i}",
            "types": b["types"],
            "bcs": b["bcs"],
            "group": "high",
            "source": b["source"],
        })

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
    est_sec = 0.15
    logger.info("Estimated: %d inferences, ~%.0f min (@%.1fs/sample)",
                total_inf, total_inf * est_sec / 60, est_sec)

    if args.dry_run:
        logger.info("DRY RUN — stopping before GPU extraction.")
        return None

    return str(preprocess_path)


def stage_extract(args):
    """GPU stage: load vLLM first, run inference per batch with incremental save."""
    sys.path.insert(0, str(BASE_DIR / "src"))
    # v2 RE prompt — no offsets, constrained JSON {"relation": enum}
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

        schema = build_json_schema_re(batch_types)
        structured = StructuredOutputsParams(json=schema)
        # Greedy decoding, seed=42 for reproducibility
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

        # Incremental save after each batch
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
    """Compute per-batch accuracy, delta, bootstrap CI, and print summary."""
    eval_results = evaluate_re(results)

    low_accs, high_accs = [], []
    low_bcs_vals, high_bcs_vals = [], []
    for bid, m in sorted(eval_results.items()):
        if bid.startswith("low_"):
            low_accs.append(m["accuracy"])
            low_bcs_vals.append(m["bcs"])
        elif bid.startswith("high_"):
            high_accs.append(m["accuracy"])
            high_bcs_vals.append(m["bcs"])

    ci = bootstrap_delta_ci(low_accs, high_accs, n_bootstrap, seed)
    ci["low_bcs_values"] = [round(v, 4) for v in low_bcs_vals]
    ci["high_bcs_values"] = [round(v, 4) for v in high_bcs_vals]

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_DIR / "eval_results.json", "w") as f:
        json.dump(eval_results, f, indent=2)
    with open(OUTPUT_DIR / "bootstrap_ci.json", "w") as f:
        json.dump(ci, f, indent=2)

    logger.info("=" * 70)
    logger.info("RESULTS: FewRel v2 BCS-Controlled (C1b)")
    logger.info("=" * 70)
    for bid, m in sorted(eval_results.items()):
        logger.info("  %-12s acc=%.4f (%3d/%3d) BCS=%.4f [%s]",
                    bid, m["accuracy"], m["correct"], m["total"],
                    m["bcs"], m["group"])
    logger.info("-" * 70)
    logger.info("Low  BCS (n=%d): mean_acc=%.4f  BCS=[%s]",
                len(low_accs), ci["low_mean_acc"],
                ", ".join(f"{v:.4f}" for v in low_bcs_vals))
    logger.info("High BCS (n=%d): mean_acc=%.4f  BCS=[%s]",
                len(high_accs), ci["high_mean_acc"],
                ", ".join(f"{v:.4f}" for v in high_bcs_vals))
    logger.info("Delta(low-high) = %+.2fpp  95%% CI [%+.2f, %+.2f]pp",
                ci["delta_pp"], ci["ci_lower_pp"], ci["ci_upper_pp"])

    if ci["delta_pp"] > 0 and ci["ci_lower_pp"] > 0:
        logger.info("CONFIRMED: low BCS > high BCS (CI excludes 0)")
    elif ci["delta_pp"] > 0:
        logger.info("TREND: low BCS > high BCS but CI includes 0")
    else:
        logger.info("NOT CONFIRMED: delta <= 0 — REPORT IMMEDIATELY")

    return ci


def main():
    parser = argparse.ArgumentParser(description="FewRel v2 BCS-controlled (C1b)")
    parser.add_argument("--model_path",
                        default="~/.cache/huggingface/qwen3-32b-fp8/")
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

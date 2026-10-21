#!/usr/bin/env python3
"""FewRel GPT-4o-mini experiment (exp-017): count curve + BCS-controlled.

Replicates run_fewrel_formal.py design using OpenAI API instead of vLLM.
- exp1 (Count curve): count={1,4,8,16,32,64,80}, 5 random batches per count
- exp2 (BCS controlled): count=8, 5 low-BCS + 5 high-BCS batches

Usage:
    # Full run (both exp1 + exp2):
    python3 src/run_fewrel_gpt4o_mini.py --mode all

    # Dry run (1 batch, 5 samples):
    python3 src/run_fewrel_gpt4o_mini.py --mode dry_run

    # Only exp1 or exp2:
    python3 src/run_fewrel_gpt4o_mini.py --mode exp1
    python3 src/run_fewrel_gpt4o_mini.py --mode exp2
"""
import argparse
import json
import logging
import os
import random
import sys
import time
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

logger = logging.getLogger(__name__)

BASE_DIR = Path(".")

EXP1_COUNTS = [1, 4, 8, 16, 32, 64, 80]
EXP2_COUNTS = [8]
EXP1_RANDOM_PER_COUNT = 5
N_LOW = 5
N_HIGH = 5
DEFAULT_N_SAMPLES = 1000

# OpenAI config
DEFAULT_API_KEY = [REDACTED]"OPENAI_API_KEY", "YOUR_API_KEY_HERE")
DEFAULT_BASE_URL = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
DEFAULT_MODEL = "gpt-4o-mini"


def build_prompt_v2_re(sentence: str, head: str, tail: str,
                       relation_defs: Dict[str, str],
                       relation_types: List[str]) -> str:
    candidates = ", ".join(sorted(relation_types))
    return (
        "Given the following sentence and two entities, "
        "classify the relation between them.\n\n"
        f'Sentence: "{sentence}"\n'
        f'Head entity: "{head}"\n'
        f'Tail entity: "{tail}"\n\n'
        f"Candidate relations: {candidates}\n\n"
        'Output a single JSON object: {"relation": "<relation_type>"}\n'
        'If none of the candidate relations apply, output: {"relation": "none"}'
    )


def evaluate_re(results):
    """Per-batch accuracy and per-type accuracy breakdown."""
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


def bootstrap_delta_ci(low_accs, high_accs, n_bootstrap=10000, seed=42):
    """Bootstrap 95% CI for mean(low) - mean(high)."""
    import numpy as np
    rng = np.random.default_rng(seed)
    low_arr = np.array(low_accs)
    high_arr = np.array(high_accs)
    observed_delta = low_arr.mean() - high_arr.mean()

    deltas = []
    for _ in range(n_bootstrap):
        l_boot = rng.choice(low_arr, size=len(low_arr), replace=True)
        h_boot = rng.choice(high_arr, size=len(high_arr), replace=True)
        deltas.append(l_boot.mean() - h_boot.mean())

    deltas = np.array(deltas)
    ci_lo = np.percentile(deltas, 2.5)
    ci_hi = np.percentile(deltas, 97.5)
    return {"observed_delta": float(observed_delta),
            "ci_95_low": float(ci_lo), "ci_95_high": float(ci_hi),
            "mean_low": float(low_arr.mean()), "mean_high": float(high_arr.mean()),
            "n_low": len(low_accs), "n_high": len(high_accs)}


def call_openai_batch(client, model, prompts, relation_types, max_retries=3, batch_size=20):
    """Call OpenAI API for a list of prompts. Returns list of predicted relations."""
    predictions = []
    
    for i in range(0, len(prompts), batch_size):
        chunk = prompts[i:i+batch_size]
        for prompt in chunk:
            pred = call_openai_single(client, model, prompt, relation_types, max_retries)
            predictions.append(pred)
        
        if i + batch_size < len(prompts):
            time.sleep(0.5)
    
    return predictions


def call_openai_single(client, model, prompt, relation_types, max_retries=3):
    """Single OpenAI API call with retry."""
    valid_relations = set(relation_types + ["none"])
    
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
                max_tokens=64,
                response_format={"type": "json_object"},
            )
            text = response.choices[0].message.content.strip()
            parsed = json.loads(text)
            pred = parsed.get("relation", "none")
            if pred not in valid_relations:
                pred = "none"
            return pred
        except json.JSONDecodeError:
            logger.warning("JSON decode error on attempt %d: %s", attempt+1, text[:100])
            if attempt == max_retries - 1:
                return "none"
        except Exception as e:
            logger.warning("API error on attempt %d: %s", attempt+1, str(e)[:200])
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
            else:
                return "none"
    return "none"


def run_experiment(client, model, samples, batch_config, relation_defs, output_dir, resume=True):
    """Run RE extraction using OpenAI API."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    incremental_path = output_dir / "results_incremental.jsonl"
    
    completed_batches = set()
    existing_results = []
    if resume and incremental_path.exists():
        with open(incremental_path) as f:
            for line in f:
                r = json.loads(line)
                existing_results.append(r)
                completed_batches.add(r["batch_id"])
        logger.info("Resumed: %d existing results, %d completed batches",
                    len(existing_results), len(completed_batches))

    all_results = list(existing_results)
    sample_id_map = {id(s): i for i, s in enumerate(samples)}
    total_api_calls = 0

    for count_key, strategies in batch_config.items():
        batches_to_run = []
        if "low_bcs" in strategies:
            batches_to_run.append(("low_bcs", strategies["low_bcs"]["types"], strategies["low_bcs"]["bcs"]))
        if "high_bcs" in strategies:
            batches_to_run.append(("high_bcs", strategies["high_bcs"]["types"], strategies["high_bcs"]["bcs"]))
        if "random" in strategies:
            for ri, rb in enumerate(strategies["random"]):
                batches_to_run.append((f"random_{ri}", rb["types"], rb["bcs"]))

        for batch_id, batch_types, batch_bcs in batches_to_run:
            full_bid = f"{count_key}_{batch_id}"
            if full_bid in completed_batches:
                logger.info("Skipping completed batch %s", full_bid)
                continue

            type_set = set(batch_types)
            batch_samples = [s for s in samples if s["relation_type"] in type_set]
            if not batch_samples:
                logger.warning("No samples for batch %s", full_bid)
                continue

            logger.info("Batch %s: %d types, BCS=%.4f, %d samples",
                        full_bid, len(batch_types), batch_bcs, len(batch_samples))

            prompts = []
            sample_refs = []
            for s in batch_samples:
                p = build_prompt_v2_re(s["text"], s["head_entity"], s["tail_entity"],
                                       relation_defs, batch_types)
                prompts.append(p)
                sample_refs.append(s)

            t0 = time.time()
            predictions = call_openai_batch(client, model, prompts, batch_types)
            elapsed = time.time() - t0
            total_api_calls += len(prompts)

            batch_results = []
            for oi, pred in enumerate(predictions):
                s = sample_refs[oi]
                result = {
                    "sample_id": sample_id_map[id(s)], "batch_id": full_bid,
                    "count_key": count_key, "batch_types": batch_types, "batch_bcs": batch_bcs,
                    "prediction": pred, "ground_truth": s["relation_type"],
                    "head_entity": s["head_entity"], "tail_entity": s["tail_entity"],
                    "latency_s": elapsed / len(prompts),
                }
                batch_results.append(result)

            with open(incremental_path, "a") as f:
                for r in batch_results:
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")
            all_results.extend(batch_results)

            batch_correct = sum(1 for r in batch_results if r["prediction"] == r["ground_truth"])
            logger.info("  Batch %s done: %.1fs, acc=%.4f (%d/%d), total_calls=%d",
                        full_bid, elapsed, batch_correct/len(batch_results),
                        batch_correct, len(batch_results), total_api_calls)

    return all_results


def build_batch_config_exp1(active_types, sim_matrix, active_idx, seed=42):
    """Build exp1 batch config (count curve)."""
    sys.path.insert(0, str(BASE_DIR / "src"))
    from compute_bcs import compute_bcs
    from select_type_batches import select_random_batches

    batch_config = {}
    seen_counts = set()
    n_active = len(active_types)

    for count in EXP1_COUNTS:
        count = min(count, n_active)
        if count in seen_counts:
            continue
        seen_counts.add(count)
        if count == 1:
            solo_batches = [{"types": [t], "bcs": 0.0} for t in active_types]
            batch_config["count_1"] = {"random": solo_batches}
        else:
            rand = select_random_batches(count, EXP1_RANDOM_PER_COUNT, active_types,
                                         sim_matrix, active_idx, seed + count)
            batch_config[f"count_{count}"] = {"random": rand}

    return batch_config


def build_batch_config_exp2(active_types, sim_matrix, active_idx, type_to_idx, seed=42):
    """Build exp2 batch config (BCS-controlled)."""
    sys.path.insert(0, str(BASE_DIR / "src"))
    from compute_bcs import compute_bcs
    from select_type_batches import select_low_bcs, select_high_bcs, select_random_batches

    batch_config = {}
    count = 8
    low = select_low_bcs(count, sim_matrix, active_types, active_idx)
    high = select_high_bcs(count, sim_matrix, active_types, active_idx)
    rand = select_random_batches(count, 25, active_types, sim_matrix, active_idx, seed + count)
    batch_config[f"count_{count}"] = {
        "low_bcs": {"types": low, "bcs": compute_bcs(low, sim_matrix, type_to_idx)},
        "high_bcs": {"types": high, "bcs": compute_bcs(high, sim_matrix, type_to_idx)},
        "random": rand,
    }
    return batch_config


def load_or_build_batch_configs(args, mode):
    """Load existing batch configs from fewrel_formal_full or build new ones."""
    formal_dir = BASE_DIR / "artifacts" / "fewrel_formal_full"
    
    if mode in ("exp1", "all", "dry_run"):
        exp1_path = formal_dir / "batch_config_exp1.json"
        if exp1_path.exists():
            with open(exp1_path) as f:
                batch_config_exp1 = json.load(f)
            logger.info("Loaded exp1 batch config from %s", exp1_path)
        else:
            raise FileNotFoundError(f"batch_config_exp1.json not found at {exp1_path}")
    else:
        batch_config_exp1 = None

    if mode in ("exp2", "all"):
        exp2_path = formal_dir / "batch_config_exp2.json"
        if exp2_path.exists():
            with open(exp2_path) as f:
                batch_config_exp2 = json.load(f)
            logger.info("Loaded exp2 batch config from %s", exp2_path)
        else:
            raise FileNotFoundError(f"batch_config_exp2.json not found at {exp2_path}")
    else:
        batch_config_exp2 = None

    return batch_config_exp1, batch_config_exp2


def run_analysis(results, output_dir):
    """Analyze results: per-count accuracy curve + BCS delta."""
    import numpy as np
    
    eval_results = evaluate_re(results)
    
    # Group by count_key
    by_count = defaultdict(list)
    for bid, m in eval_results.items():
        by_count[m["count_key"]].append(m)

    # Count curve summary
    count_curve = {}
    for ck, batches in sorted(by_count.items()):
        accs = [b["accuracy"] for b in batches]
        count_curve[ck] = {
            "mean_accuracy": float(np.mean(accs)),
            "std_accuracy": float(np.std(accs)),
            "n_batches": len(batches),
            "mean_bcs": float(np.mean([b["bcs"] for b in batches])),
        }
    
    # BCS-controlled analysis (if both low and high exist)
    bcs_analysis = None
    for ck, batches in by_count.items():
        low_batches = [b for b in batches if "low_bcs" in [bid_part for bid_part in b.get("batch_types", [])]]
        # Better: check by batch_id naming
        pass
    
    # Check for exp2 pattern: low_bcs / high_bcs batches
    low_accs = []
    high_accs = []
    for bid, m in eval_results.items():
        if "low_bcs" in bid:
            low_accs.append(m["accuracy"])
        elif "high_bcs" in bid:
            high_accs.append(m["accuracy"])
    
    if low_accs and high_accs:
        bcs_analysis = bootstrap_delta_ci(low_accs, high_accs)
        bcs_analysis["low_accs"] = low_accs
        bcs_analysis["high_accs"] = high_accs
    
    return {"eval_results": eval_results, "count_curve": count_curve, "bcs_analysis": bcs_analysis}


def main():
    parser = argparse.ArgumentParser(description="FewRel GPT-4o-mini Experiment (exp-017)")
    parser.add_argument("--mode", choices=["exp1", "exp2", "all", "dry_run"], default="all")
    parser.add_argument("--api_key", default=DEFAULT_API_KEY)
    parser.add_argument("--base_url", default=DEFAULT_BASE_URL)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--data_path", default=str(BASE_DIR / "data/fewrel_parquet/val.parquet"))
    parser.add_argument("--use_all", action="store_true", default=True,
                        help="Load both train+val splits (all 80 relations)")
    parser.add_argument("--types_file", default=str(BASE_DIR / "configs/fewrel_relation_types.json"))
    parser.add_argument("--output_dir", default=str(BASE_DIR / "artifacts/exp017_gpt4o_mini_fewrel"))
    parser.add_argument("--n_samples", type=int, default=DEFAULT_N_SAMPLES)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--resume", action="store_true", default=True)
    parser.add_argument("--no_resume", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    random.seed(args.seed)

    if args.no_resume:
        args.resume = False

    # Initialize OpenAI client
    from openai import OpenAI
    client = OpenAI(api_key=[REDACTED], base_url=args.base_url)
    logger.info("OpenAI client: model=%s, base_url=%s", args.model, args.base_url)

    # Load data
    sys.path.insert(0, str(BASE_DIR / "src"))
    from fewrel_utils import load_fewrel, get_all_relation_types, sample_balanced

    logger.info("Loading FewRel data...")
    data_paths = [str(BASE_DIR / "data/fewrel_parquet/train.parquet"),
                  str(BASE_DIR / "data/fewrel_parquet/val.parquet")]
    all_samples = []
    for dp in data_paths:
        all_samples.extend(load_fewrel(data_path=dp))
    all_relations = get_all_relation_types(all_samples)
    logger.info("%d samples, %d relation types", len(all_samples), len(all_relations))

    n_per_rel = args.n_samples // len(all_relations)
    samples = sample_balanced(all_samples, n_per_rel, seed=args.seed)
    logger.info("Sampled %d (%d per relation, %d relations)",
                len(samples), n_per_rel, len(all_relations))

    with open(args.types_file) as f:
        pid2name = json.load(f)
    relation_defs = {name: name for name in pid2name.values()}

    # Load batch configs
    mode = args.mode if args.mode != "dry_run" else "exp1"
    batch_config_exp1, batch_config_exp2 = load_or_build_batch_configs(args, mode)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Dry run: just 1 batch from count_4, max 5 samples
    if args.mode == "dry_run":
        logger.info("=== DRY RUN: testing API connectivity ===")
        # Pick first count_4 random batch
        test_batch_types = batch_config_exp1["count_4"]["random"][0]["types"]
        test_bcs = batch_config_exp1["count_4"]["random"][0]["bcs"]
        type_set = set(test_batch_types)
        test_samples = [s for s in samples if s["relation_type"] in type_set][:5]

        if not test_samples:
            test_samples = samples[:5]
            test_batch_types = list(set(s["relation_type"] for s in test_samples))

        logger.info("Testing with %d samples, %d types", len(test_samples), len(test_batch_types))
        for s in test_samples:
            prompt = build_prompt_v2_re(s["text"], s["head_entity"], s["tail_entity"],
                                        relation_defs, test_batch_types)
            pred = call_openai_single(client, args.model, prompt, test_batch_types)
            logger.info("  GT=%-30s PRED=%-30s %s",
                        s["relation_type"], pred,
                        "OK" if pred == s["relation_type"] else "MISS")
        logger.info("=== DRY RUN COMPLETE ===")
        return

    # Run experiments
    all_results = []

    if args.mode in ("exp1", "all"):
        logger.info("=" * 60)
        logger.info("EXP1: Count Curve")
        logger.info("=" * 60)
        exp1_results = run_experiment(
            client, args.model, samples, batch_config_exp1, relation_defs,
            output_dir / "exp1", resume=args.resume)
        all_results.extend(exp1_results)

        # Save exp1 analysis
        analysis = run_analysis(exp1_results, output_dir / "exp1")
        with open(output_dir / "exp1" / "analysis.json", "w") as f:
            json.dump(analysis, f, indent=2, default=str)
        logger.info("Exp1 count curve:")
        for ck, info in sorted(analysis["count_curve"].items()):
            logger.info("  %-12s acc=%.4f±%.4f (%d batches, mean_bcs=%.4f)",
                        ck, info["mean_accuracy"], info["std_accuracy"],
                        info["n_batches"], info["mean_bcs"])

    if args.mode in ("exp2", "all"):
        logger.info("=" * 60)
        logger.info("EXP2: BCS-Controlled")
        logger.info("=" * 60)
        exp2_results = run_experiment(
            client, args.model, samples, batch_config_exp2, relation_defs,
            output_dir / "exp2", resume=args.resume)
        all_results.extend(exp2_results)

        # Save exp2 analysis
        analysis = run_analysis(exp2_results, output_dir / "exp2")
        with open(output_dir / "exp2" / "analysis.json", "w") as f:
            json.dump(analysis, f, indent=2, default=str)
        if analysis["bcs_analysis"]:
            ba = analysis["bcs_analysis"]
            logger.info("BCS-controlled result:")
            logger.info("  Low-BCS acc: %.4f, High-BCS acc: %.4f", ba["mean_low"], ba["mean_high"])
            logger.info("  Delta (low-high): %.4f, 95%% CI: [%.4f, %.4f]",
                        ba["observed_delta"], ba["ci_95_low"], ba["ci_95_high"])

    # Final summary
    with open(output_dir / "all_results.json", "w") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    logger.info("Total results: %d, saved to %s", len(all_results), output_dir / "all_results.json")


if __name__ == "__main__":
    main()

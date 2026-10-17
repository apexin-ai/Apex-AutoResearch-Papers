#!/usr/bin/env python3
"""Gemini 2.5 Flash cross-model validation: FewRel RE count curve + BCS-controlled.

Proves schema degradation is model-agnostic by replicating Qwen3-32B experiments
on Gemini 2.5 Flash via TUM proxy (OpenAI-compatible API).

Part 1 (Count Curve): count={1,4,8,16,32,64,80}, 25 random batches per count
Part 2 (BCS-Controlled): count=8 + count=16, 25 low-BCS + 25 high-BCS batches each

Usage:
    python3 scripts/run_gemini_flash_fewrel.py --mode dry_run
    python3 scripts/run_gemini_flash_fewrel.py --mode part1
    python3 scripts/run_gemini_flash_fewrel.py --mode part2
    python3 scripts/run_gemini_flash_fewrel.py --mode all
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
from typing import Dict, List, Optional

import numpy as np

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "artifacts" / "exp_gemini_flash"

# TUM proxy config (OpenAI-compatible)
DEFAULT_API_KEY = "tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8"
DEFAULT_BASE_URL = "http://47.94.22.126/v1"
DEFAULT_MODEL = "gemini-2.5-flash"

PART1_COUNTS = [1, 4, 8, 16, 32, 64, 80]
N_BATCHES_PER_COUNT = 25
N_SAMPLES_PER_REL = 12
N_RELATIONS = 80
TOTAL_SAMPLES = N_SAMPLES_PER_REL * N_RELATIONS  # 960


def build_prompt_re(sentence: str, head: str, tail: str,
                    relation_types: List[str]) -> str:
    """Build RE classification prompt (matches Qwen3 experiments exactly)."""
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


def call_api_single(client, model: str, prompt: str, relation_types: List[str],
                    max_retries: int = 5) -> str:
    """Single API call with exponential backoff retry."""
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
            logger.warning("JSON decode error attempt %d: %s", attempt + 1,
                           text[:100] if 'text' in dir() else "N/A")
            if attempt == max_retries - 1:
                return "none"
        except Exception as e:
            wait = min(2 ** attempt, 30)
            logger.warning("API error attempt %d/%d: %s (retry in %ds)",
                           attempt + 1, max_retries, str(e)[:200], wait)
            if attempt < max_retries - 1:
                time.sleep(wait)
            else:
                return "none"
    return "none"


def load_fewrel_samples(seed: int = 42) -> List[Dict]:
    """Load 960 balanced FewRel samples from pre-sampled JSON."""
    samples_path = BASE_DIR / "data" / "fewrel" / "fewrel_samples_960.json"
    with open(samples_path) as f:
        data = json.load(f)
    samples = data["samples"]
    n_rels = len(data["relations"])
    logger.info("Loaded %d samples (%d relations)", len(samples), n_rels)
    return samples


def generate_count_curve_batches(type_names: List[str], seed: int = 42) -> Dict:
    """Generate count curve batch configs deterministically (matches cqa1)."""
    config = {}
    for count in PART1_COUNTS:
        if count == 1:
            continue
        rng = random.Random(seed + count)
        batches = []
        for _ in range(N_BATCHES_PER_COUNT):
            types = rng.sample(type_names, count)
            batches.append({"types": types, "bcs": 0.0})
        config[f"count_{count}"] = {"random": batches}
    return config


def generate_count1_batches(all_relations: List[str], n_batches: int = 25,
                            seed: int = 42) -> List[Dict]:
    """Generate count=1 batches (each is a single relation)."""
    rng = random.Random(seed)
    selected = rng.sample(all_relations, min(n_batches, len(all_relations)))
    if len(selected) < n_batches:
        selected = selected + rng.choices(all_relations, k=n_batches - len(selected))
    return [{"types": [rel], "bcs": 0.0} for rel in selected[:n_batches]]


def load_extreme_batches() -> Dict:
    """Load BCS-controlled extreme batches for count=8 and count=16."""
    # Count=8: from exp_v2_re_n25
    c8_path = BASE_DIR / "artifacts" / "exp_v2_re_n25" / "batch_groups.json"
    with open(c8_path) as f:
        c8_groups = json.load(f)

    # Count=16: from bcs_controlled_llama-3.1-70b-fp8
    c16_path = (BASE_DIR / "artifacts" / "bcs_controlled_llama-3.1-70b-fp8"
                / "count_16" / "batch_groups.json")
    with open(c16_path) as f:
        c16_groups = json.load(f)

    logger.info("Loaded extreme batches: count_8 (%d low, %d high), count_16 (%d low, %d high)",
                len(c8_groups["low"]), len(c8_groups["high"]),
                len(c16_groups["low"]), len(c16_groups["high"]))
    return {"count_8": c8_groups, "count_16": c16_groups}


def run_batch(client, model: str, samples: List[Dict], batch_types: List[str],
              batch_id: str, batch_bcs: float, count_key: str,
              inter_call_sleep: float = 0.1) -> List[Dict]:
    """Run a single batch: filter samples by batch types, call API for each."""
    type_set = set(batch_types)
    batch_samples = [s for s in samples if s["relation_type"] in type_set]

    if not batch_samples:
        logger.warning("No samples for batch %s", batch_id)
        return []

    results = []
    for s in batch_samples:
        prompt = build_prompt_re(s["text"], s["head_entity"], s["tail_entity"],
                                 batch_types)
        pred = call_api_single(client, model, prompt, batch_types)
        results.append({
            "sample_id": s.get("_idx", 0),
            "batch_id": batch_id,
            "count_key": count_key,
            "batch_types": batch_types,
            "batch_bcs": batch_bcs,
            "prediction": pred,
            "ground_truth": s["relation_type"],
            "head_entity": s["head_entity"],
            "tail_entity": s["tail_entity"],
        })
        time.sleep(inter_call_sleep)

    correct = sum(1 for r in results if r["prediction"] == r["ground_truth"])
    acc = correct / len(results) if results else 0
    logger.info("  %s: %d samples, acc=%.4f (%d/%d)",
                batch_id, len(results), acc, correct, len(results))
    return results


def compute_batch_accuracy(results: List[Dict]) -> float:
    if not results:
        return 0.0
    correct = sum(1 for r in results if r["prediction"] == r["ground_truth"])
    return correct / len(results)


def save_incremental(results: List[Dict], path: Path):
    """Append results to JSONL file for resume support."""
    with open(path, "a") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def load_completed_batches(path: Path) -> set:
    """Load already-completed batch IDs from incremental results file."""
    if not path.exists():
        return set()
    completed = set()
    with open(path) as f:
        for line in f:
            r = json.loads(line)
            completed.add(r["batch_id"])
    return completed


def run_part1(client, model: str, samples: List[Dict], output_dir: Path,
              inter_call_sleep: float = 0.1):
    """Part 1: Count curve experiment."""
    logger.info("=" * 60)
    logger.info("PART 1: Count Curve (counts=%s, %d batches each)",
                PART1_COUNTS, N_BATCHES_PER_COUNT)
    logger.info("=" * 60)

    output_dir.mkdir(parents=True, exist_ok=True)
    results_path = output_dir / "results_incremental.jsonl"
    completed = load_completed_batches(results_path)
    if completed:
        logger.info("Resuming: %d batches already completed", len(completed))

    # Generate batch configs deterministically (matches cqa1)
    all_relations = sorted(set(s["relation_type"] for s in samples))
    batch_config = generate_count_curve_batches(all_relations)

    # Add count=1 batches
    batch_config["count_1"] = {"random": generate_count1_batches(all_relations)}

    # Add sample indices for filtering
    for i, s in enumerate(samples):
        s["_idx"] = i

    all_results = []
    for count in PART1_COUNTS:
        count_key = f"count_{count}"
        if count_key not in batch_config:
            logger.warning("No batch config for %s, skipping", count_key)
            continue

        batches = batch_config[count_key]["random"][:N_BATCHES_PER_COUNT]
        logger.info("Processing %s: %d batches", count_key, len(batches))

        for bi, batch in enumerate(batches):
            batch_id = f"{count_key}_random_{bi}"
            if batch_id in completed:
                continue

            batch_results = run_batch(
                client, model, samples, batch["types"], batch_id,
                batch["bcs"], count_key, inter_call_sleep
            )
            save_incremental(batch_results, results_path)
            all_results.extend(batch_results)

    # Compute summary
    summary = compute_count_curve_summary(results_path)
    with open(output_dir / "count_curve_results.json", "w") as f:
        json.dump(summary, f, indent=2)
    logger.info("Part 1 complete. Summary saved.")

    for ck in sorted(summary.keys()):
        info = summary[ck]
        logger.info("  %s: acc=%.4f +/- %.4f (%d batches)",
                    ck, info["mean_acc"], info["std_acc"], info["n_batches"])


def run_part2(client, model: str, samples: List[Dict], output_dir: Path,
              inter_call_sleep: float = 0.1):
    """Part 2: BCS-controlled extreme batch experiment."""
    logger.info("=" * 60)
    logger.info("PART 2: BCS-Controlled Extreme Batches")
    logger.info("=" * 60)

    output_dir.mkdir(parents=True, exist_ok=True)
    results_path = output_dir / "results_incremental.jsonl"
    completed = load_completed_batches(results_path)
    if completed:
        logger.info("Resuming: %d batches already completed", len(completed))

    extreme_config = load_extreme_batches()

    for i, s in enumerate(samples):
        s["_idx"] = i

    for count_key, groups in extreme_config.items():
        for group_name in ["low", "high"]:
            batches = groups[group_name][:N_BATCHES_PER_COUNT]
            logger.info("Processing %s %s-BCS: %d batches",
                        count_key, group_name, len(batches))

            for bi, batch in enumerate(batches):
                batch_id = f"{count_key}_{group_name}_{bi}"
                if batch_id in completed:
                    continue

                batch_results = run_batch(
                    client, model, samples, batch["types"], batch_id,
                    batch["bcs"], count_key, inter_call_sleep
                )
                save_incremental(batch_results, results_path)

    # Compute summary
    summary = compute_extreme_batch_summary(results_path)
    with open(output_dir / "extreme_batch_results.json", "w") as f:
        json.dump(summary, f, indent=2)
    logger.info("Part 2 complete. Summary saved.")

    for ck in sorted(summary.keys()):
        info = summary[ck]
        logger.info("  %s: low_acc=%.4f, high_acc=%.4f, delta=%.2f pp",
                    ck, info["low_mean_acc"], info["high_mean_acc"],
                    (info["low_mean_acc"] - info["high_mean_acc"]) * 100)


def compute_count_curve_summary(results_path: Path) -> Dict:
    """Compute per-count accuracy statistics from incremental results."""
    batch_results = defaultdict(lambda: defaultdict(lambda: {"correct": 0, "total": 0, "bcs": 0}))

    with open(results_path) as f:
        for line in f:
            r = json.loads(line)
            bid = r["batch_id"]
            ck = r["count_key"]
            batch_results[ck][bid]["total"] += 1
            batch_results[ck][bid]["bcs"] = r["batch_bcs"]
            if r["prediction"] == r["ground_truth"]:
                batch_results[ck][bid]["correct"] += 1

    summary = {}
    for ck in sorted(batch_results.keys()):
        batches = batch_results[ck]
        accs = []
        batch_details = []
        for bid, stats in sorted(batches.items()):
            acc = stats["correct"] / stats["total"] if stats["total"] else 0
            accs.append(acc)
            batch_details.append({
                "batch_id": bid, "accuracy": acc, "bcs": stats["bcs"],
                "n_samples": stats["total"]
            })
        summary[ck] = {
            "n_batches": len(accs),
            "mean_acc": float(np.mean(accs)),
            "std_acc": float(np.std(accs)),
            "min_acc": float(np.min(accs)),
            "max_acc": float(np.max(accs)),
            "batches": batch_details,
        }
    return summary


def compute_extreme_batch_summary(results_path: Path) -> Dict:
    """Compute BCS-controlled extreme batch statistics."""
    batch_results = defaultdict(lambda: {"correct": 0, "total": 0, "bcs": 0})

    with open(results_path) as f:
        for line in f:
            r = json.loads(line)
            bid = r["batch_id"]
            batch_results[bid]["total"] += 1
            batch_results[bid]["bcs"] = r["batch_bcs"]
            batch_results[bid]["count_key"] = r["count_key"]
            if r["prediction"] == r["ground_truth"]:
                batch_results[bid]["correct"] += 1

    # Group by count_key and low/high
    grouped = defaultdict(lambda: {"low": [], "high": []})
    for bid, stats in batch_results.items():
        ck = stats["count_key"]
        acc = stats["correct"] / stats["total"] if stats["total"] else 0
        if "_low_" in bid:
            grouped[ck]["low"].append({"batch_id": bid, "accuracy": acc, "bcs": stats["bcs"]})
        elif "_high_" in bid:
            grouped[ck]["high"].append({"batch_id": bid, "accuracy": acc, "bcs": stats["bcs"]})

    summary = {}
    for ck in sorted(grouped.keys()):
        low_accs = [b["accuracy"] for b in grouped[ck]["low"]]
        high_accs = [b["accuracy"] for b in grouped[ck]["high"]]

        result = {
            "low_mean_acc": float(np.mean(low_accs)) if low_accs else 0,
            "high_mean_acc": float(np.mean(high_accs)) if high_accs else 0,
            "low_std_acc": float(np.std(low_accs)) if low_accs else 0,
            "high_std_acc": float(np.std(high_accs)) if high_accs else 0,
            "n_low": len(low_accs),
            "n_high": len(high_accs),
            "low_batches": grouped[ck]["low"],
            "high_batches": grouped[ck]["high"],
        }

        # Bootstrap CI for delta
        if low_accs and high_accs:
            result.update(bootstrap_delta_ci(low_accs, high_accs))

        summary[ck] = result
    return summary


def bootstrap_delta_ci(low_accs, high_accs, n_bootstrap=10000, seed=42):
    """Bootstrap 95% CI for mean(low) - mean(high)."""
    rng = np.random.default_rng(seed)
    low_arr = np.array(low_accs)
    high_arr = np.array(high_accs)
    observed_delta = float(low_arr.mean() - high_arr.mean())

    deltas = []
    for _ in range(n_bootstrap):
        l_boot = rng.choice(low_arr, size=len(low_arr), replace=True)
        h_boot = rng.choice(high_arr, size=len(high_arr), replace=True)
        deltas.append(l_boot.mean() - h_boot.mean())

    deltas = np.array(deltas)
    return {
        "delta_pp": round(observed_delta * 100, 2),
        "ci_lower_pp": round(float(np.percentile(deltas, 2.5)) * 100, 2),
        "ci_upper_pp": round(float(np.percentile(deltas, 97.5)) * 100, 2),
    }


def run_dry_run(client, model: str, samples: List[Dict]):
    """Quick validation: 1 batch, ~5 samples."""
    logger.info("=== DRY RUN: testing API connectivity ===")

    # Pick a count_8 batch
    all_relations = sorted(set(s["relation_type"] for s in samples))
    batch_config = generate_count_curve_batches(all_relations)
    test_batch = batch_config["count_8"]["random"][0]
    batch_types = test_batch["types"]
    type_set = set(batch_types)

    test_samples = [s for s in samples if s["relation_type"] in type_set][:5]
    if not test_samples:
        test_samples = samples[:5]
        batch_types = list(set(s["relation_type"] for s in test_samples))

    logger.info("Testing with %d samples, %d candidate types", len(test_samples), len(batch_types))
    logger.info("Batch types: %s", batch_types)

    correct = 0
    for s in test_samples:
        prompt = build_prompt_re(s["text"], s["head_entity"], s["tail_entity"], batch_types)
        t0 = time.time()
        pred = call_api_single(client, model, prompt, batch_types)
        elapsed = time.time() - t0
        is_correct = pred == s["relation_type"]
        correct += int(is_correct)
        logger.info("  GT=%-35s PRED=%-35s %.2fs %s",
                    s["relation_type"], pred, elapsed,
                    "OK" if is_correct else "MISS")
        time.sleep(0.2)

    logger.info("=== DRY RUN COMPLETE: %d/%d correct ===", correct, len(test_samples))


def main():
    parser = argparse.ArgumentParser(description="Gemini 2.5 Flash FewRel cross-model validation")
    parser.add_argument("--mode", choices=["dry_run", "part1", "part2", "all"], default="all")
    parser.add_argument("--api_key", default=os.environ.get("GEMINI_API_KEY", DEFAULT_API_KEY))
    parser.add_argument("--base_url", default=os.environ.get("OPENAI_BASE_URL", DEFAULT_BASE_URL))
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--output_dir", default=str(OUTPUT_DIR))
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--sleep", type=float, default=0.1,
                        help="Sleep between API calls (seconds)")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(Path(args.output_dir) / "run.log", mode="a"),
        ]
    )

    logger.info("Config: model=%s, base_url=%s, seed=%d, sleep=%.2f",
                args.model, args.base_url, args.seed, args.sleep)

    # Initialize OpenAI-compatible client
    from openai import OpenAI
    client = OpenAI(api_key=[REDACTED], base_url=args.base_url, timeout=60.0)
    logger.info("Client initialized (OpenAI-compatible, model=%s)", args.model)

    # Load data
    samples = load_fewrel_samples(seed=args.seed)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.mode == "dry_run":
        run_dry_run(client, args.model, samples)
        return

    if args.mode in ("part1", "all"):
        run_part1(client, args.model, samples, output_dir / "part1", args.sleep)

    if args.mode in ("part2", "all"):
        run_part2(client, args.model, samples, output_dir / "part2", args.sleep)

    logger.info("All done.")


if __name__ == "__main__":
    main()

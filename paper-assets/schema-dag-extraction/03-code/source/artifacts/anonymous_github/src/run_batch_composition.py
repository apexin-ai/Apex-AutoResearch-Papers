#!/usr/bin/env python3
"""Confusability-Aware Batch Composition experiment on FewRel 80-rel.

Hypothesis: Partitioning types into batches that minimize intra-batch SCS
improves per-type accuracy without requiring any merge step.

Three modes:
  single_pass        — all 80 types in one prompt (baseline)
  random_batch       — random partition into K batches
  confusability_aware — graph-coloring partition minimizing intra-batch BCS

Each sample is evaluated only in the batch containing its gold relation type.
Metric: accuracy, intra-batch substitution rate, per-batch BCS.

Two-stage execution (avoid vLLM fork deadlock):
    python3 src/run_batch_composition.py --stage all --mode confusability_aware --dry_run
    python3 src/run_batch_composition.py --stage all --mode random_batch
    python3 src/run_batch_composition.py --stage all --mode single_pass
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
from typing import Dict, List, Tuple

import numpy as np
import torch

logger = logging.getLogger(__name__)

BASE_DIR = Path(".")
OUTPUT_DIR = BASE_DIR / "artifacts" / "exp_batch_composition"
SCS_MATRIX_PATH = BASE_DIR / "artifacts" / "fewrel_formal_full" / "relation_sim_matrix.pt"
DATA_PATHS = [
    BASE_DIR / "data" / "fewrel_parquet" / "train.parquet",
    BASE_DIR / "data" / "fewrel_parquet" / "val.parquet",
]
MODEL_PATH = "~/.cache/huggingface/qwen3-32b-fp8/"


# ── SCS / BCS ────────────────────────────────────────────────────────────────

def load_scs_matrix(path: str = None):
    """Load SCS matrix from .pt file."""
    p = Path(path) if path else SCS_MATRIX_PATH
    data = torch.load(p, map_location="cpu", weights_only=True)
    sim_matrix = data["sim_matrix"]
    type_names = data["type_names"]
    type_to_idx = data["type_to_idx"]
    return sim_matrix, type_names, type_to_idx


def compute_bcs_mean(type_subset: List[str], sim_matrix: torch.Tensor,
                     type_to_idx: dict) -> float:
    """BCS = mean pairwise cosine similarity among batch types."""
    if len(type_subset) < 2:
        return 0.0
    indices = [type_to_idx[t] for t in type_subset]
    total, count = 0.0, 0
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            total += sim_matrix[indices[i], indices[j]].item()
            count += 1
    return total / count


# ── Batch Partition Strategies ──────────────────────────────────────────────

def partition_single_pass(type_names: List[str]) -> List[List[str]]:
    """All types in one batch."""
    return [list(type_names)]


def partition_random(type_names: List[str], n_batches: int, seed: int = 42) -> List[List[str]]:
    """Random balanced partition into n_batches."""
    rng = random.Random(seed)
    shuffled = list(type_names)
    rng.shuffle(shuffled)
    batches = [[] for _ in range(n_batches)]
    for i, t in enumerate(shuffled):
        batches[i % n_batches].append(t)
    return batches


def partition_confusability_aware(
    sim_matrix: torch.Tensor,
    type_names: List[str],
    type_to_idx: dict,
    n_batches: int,
    threshold: float = 0.0,
) -> List[List[str]]:
    """Graph-coloring partition that minimizes intra-batch confusability.

    1. Build weighted graph (all pairs with SCS > threshold)
    2. Greedy graph coloring (largest_first)
    3. Merge/split color classes to exactly n_batches with balanced sizes
    """
    import networkx as nx

    n = len(type_names)
    G = nx.Graph()
    G.add_nodes_from(range(n))

    sim_np = sim_matrix.numpy()
    if threshold <= 0:
        upper = []
        for i in range(n):
            for j in range(i + 1, n):
                upper.append(sim_np[i, j])
        threshold = float(np.percentile(upper, 75))
        logger.info("Adaptive SCS threshold (75th percentile): %.4f", threshold)

    for i in range(n):
        for j in range(i + 1, n):
            if sim_np[i, j] > threshold:
                G.add_edge(i, j, weight=sim_np[i, j])

    logger.info("Graph: %d nodes, %d edges (threshold=%.4f)", G.number_of_nodes(),
                G.number_of_edges(), threshold)

    coloring = nx.coloring.greedy_color(G, strategy='largest_first')
    n_colors = max(coloring.values()) + 1
    logger.info("Initial greedy coloring: %d colors", n_colors)

    color_groups = defaultdict(list)
    for node, color in coloring.items():
        color_groups[color].append(node)

    batches = _balance_to_k(color_groups, n_batches, sim_np)

    return [[type_names[idx] for idx in batch] for batch in batches]


def _balance_to_k(color_groups: dict, k: int, sim_np: np.ndarray) -> List[List[int]]:
    """Merge/split color groups to get exactly k balanced batches."""
    groups = sorted(color_groups.values(), key=len, reverse=True)

    if len(groups) <= k:
        while len(groups) < k:
            groups.sort(key=len, reverse=True)
            largest = groups.pop(0)
            mid = len(largest) // 2
            groups.append(largest[:mid])
            groups.append(largest[mid:])
    else:
        while len(groups) > k:
            groups.sort(key=len, reverse=True)
            a = groups.pop()
            b = groups.pop()
            groups.append(a + b)

    # Balance pass: move nodes from largest to smallest batch
    for _ in range(50):
        groups.sort(key=len, reverse=True)
        largest = groups[0]
        smallest = groups[-1]
        if len(largest) - len(smallest) <= 1:
            break
        best_node = None
        best_cost = float("inf")
        for node in largest:
            if not smallest:
                cost = 0.0
            else:
                cost = np.mean([sim_np[node, s] for s in smallest])
            if cost < best_cost:
                best_cost = cost
                best_node = node
        largest.remove(best_node)
        smallest.append(best_node)

    return groups


# ── Prompt & Schema ──────────────────────────────────────────────────

def build_json_schema_re(relation_types: List[str]) -> dict:
    return {
        "type": "object",
        "properties": {
            "relation": {
                "type": "string",
                "enum": sorted(relation_types) + ["none"],
            },
        },
        "required": ["relation"],
    }


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


# ── Evaluation ─────────────────────────────────────────────────────

def compute_substitution_rate(results: List[dict]) -> dict:
    """Compute intra-batch substitution vs hallucination rates."""
    total_wrong = 0
    intra_sub = 0
    out_of_batch = 0
    none_pred = 0

    for r in results:
        if r["prediction"] == r["ground_truth"]:
            continue
        total_wrong += 1
        pred = r["prediction"]
        batch_types = set(r["batch_types"])
        if pred == "none":
            none_pred += 1
        elif pred in batch_types:
            intra_sub += 1
        else:
            out_of_batch += 1

    if total_wrong == 0:
        return {"intra_sub_rate": 0.0, "out_of_batch_rate": 0.0,
                "none_rate": 0.0, "total_wrong": 0}
    return {
        "intra_sub_rate": intra_sub / total_wrong,
        "out_of_batch_rate": out_of_batch / total_wrong,
        "none_rate": none_pred / total_wrong,
        "total_wrong": total_wrong,
        "intra_sub_count": intra_sub,
        "out_of_batch_count": out_of_batch,
        "none_count": none_pred,
    }


def evaluate_results(results: List[dict], sim_matrix, type_to_idx) -> dict:
    """Full evaluation: accuracy, per-batch BCS, substitution rates."""
    correct = sum(1 for r in results if r["prediction"] == r["ground_truth"])
    total = len(results)

    batch_stats = defaultdict(lambda: {"correct": 0, "total": 0, "types": []})
    for r in results:
        bid = r["batch_id"]
        batch_stats[bid]["total"] += 1
        batch_stats[bid]["types"] = r["batch_types"]
        if r["prediction"] == r["ground_truth"]:
            batch_stats[bid]["correct"] += 1

    per_batch = {}
    for bid, s in sorted(batch_stats.items()):
        bcs = compute_bcs_mean(s["types"], sim_matrix, type_to_idx)
        per_batch[bid] = {
            "accuracy": s["correct"] / s["total"] if s["total"] else 0.0,
            "correct": s["correct"],
            "total": s["total"],
            "n_types": len(s["types"]),
            "bcs": round(bcs, 4),
        }

    sub_rates = compute_substitution_rate(results)

    type_stats = defaultdict(lambda: {"correct": 0, "total": 0})
    for r in results:
        gt = r["ground_truth"]
        type_stats[gt]["total"] += 1
        if r["prediction"] == r["ground_truth"]:
            type_stats[gt]["correct"] += 1
    per_type_acc = {
        t: s["correct"] / s["total"] if s["total"] else 0.0
        for t, s in sorted(type_stats.items())
    }

    return {
        "overall_accuracy": correct / total if total else 0.0,
        "correct": correct,
        "total": total,
        "per_batch": per_batch,
        "substitution_rates": sub_rates,
        "per_type_accuracy": per_type_acc,
        "mean_batch_bcs": float(np.mean([b["bcs"] for b in per_batch.values()])),
    }


# ── Stage: Preprocess ────────────────────────────────────────────────

def stage_preprocess(args):
    """CPU stage: load data, compute partition, save config."""
    sys.path.insert(0, str(BASE_DIR / "src"))
    from fewrel_utils import load_fewrel, get_all_relation_types, sample_balanced

    logger.info("Loading FewRel data...")
    all_samples = []
    for dp in DATA_PATHS:
        all_samples.extend(load_fewrel(data_path=str(dp)))
    all_relations = get_all_relation_types(all_samples)
    logger.info("%d samples, %d relations", len(all_samples), len(all_relations))

    n_per_rel = args.n_eval_per_type
    samples = sample_balanced(all_samples, n_per_rel, seed=args.seed)
    logger.info("Balanced sample: %d (%d/rel)", len(samples), n_per_rel)

    with open(BASE_DIR / "configs" / "fewrel_relation_types.json") as f:
        pid2name = json.load(f)
    relation_defs = {name: name for name in pid2name.values()}

    sim_matrix, type_names, type_to_idx = load_scs_matrix(args.scs_matrix)
    logger.info("SCS matrix: %d types", len(type_names))

    mode = args.mode
    if mode == "single_pass":
        batches = partition_single_pass(type_names)
    elif mode == "random_batch":
        batches = partition_random(type_names, args.n_batches, seed=args.seed)
    elif mode == "confusability_aware":
        batches = partition_confusability_aware(
            sim_matrix, type_names, type_to_idx,
            n_batches=args.n_batches, threshold=args.scs_threshold)
    else:
        raise ValueError(f"Unknown mode: {mode}")

    batch_list = []
    for i, batch_types in enumerate(batches):
        bcs = compute_bcs_mean(batch_types, sim_matrix, type_to_idx)
        batch_list.append({
            "batch_id": f"{mode}_batch_{i}",
            "types": batch_types,
            "bcs": round(bcs, 4),
            "size": len(batch_types),
        })

    logger.info("=" * 70)
    logger.info("MODE: %s | %d batches", mode, len(batch_list))
    logger.info("=" * 70)
    bcs_values = [b["bcs"] for b in batch_list]
    sizes = [b["size"] for b in batch_list]
    for b in batch_list:
        logger.info("  %s: %d types, BCS=%.4f", b["batch_id"], b["size"], b["bcs"])
    logger.info("-" * 70)
    logger.info("  Mean BCS: %.4f", np.mean(bcs_values))
    logger.info("  BCS range: [%.4f, %.4f]", min(bcs_values), max(bcs_values))
    logger.info("  Batch sizes: %s (mean=%.1f)", sizes, np.mean(sizes))

    total_inf = 0
    for b in batch_list:
        type_set = set(b["types"])
        n_match = sum(1 for s in samples if s["relation_type"] in type_set)
        total_inf += n_match
        logger.info("  %s: %d eligible samples", b["batch_id"], n_match)
    logger.info("Total inferences: %d", total_inf)

    mode_dir = OUTPUT_DIR / mode
    mode_dir.mkdir(parents=True, exist_ok=True)

    preprocess_config = {
        "mode": mode,
        "n_batches": len(batch_list),
        "samples": samples,
        "batch_list": batch_list,
        "relation_defs": relation_defs,
        "model_path": args.model_path,
        "max_model_len": args.max_model_len,
        "gpu_memory_utilization": args.gpu_memory_utilization,
        "seed": args.seed,
    }
    preprocess_path = mode_dir / "preprocess.json"
    with open(preprocess_path, "w") as f:
        json.dump(preprocess_config, f, ensure_ascii=False)
    logger.info("Saved preprocess config to %s", preprocess_path)

    if args.dry_run:
        logger.info("DRY RUN — stopping before GPU extraction.")
        _print_partition_comparison(sim_matrix, type_names, type_to_idx, args)
        return None

    return str(preprocess_path)


def _print_partition_comparison(sim_matrix, type_names, type_to_idx, args):
    """Print BCS comparison across all three modes (dry-run only)."""
    logger.info("")
    logger.info("=" * 70)
    logger.info("PARTITION COMPARISON (all modes, n_batches=%d)", args.n_batches)
    logger.info("=" * 70)

    for mode in ["single_pass", "random_batch", "confusability_aware"]:
        if mode == "single_pass":
            batches = partition_single_pass(type_names)
        elif mode == "random_batch":
            batches = partition_random(type_names, args.n_batches, seed=args.seed)
        else:
            batches = partition_confusability_aware(
                sim_matrix, type_names, type_to_idx,
                n_batches=args.n_batches, threshold=args.scs_threshold)

        bcs_values = [compute_bcs_mean(b, sim_matrix, type_to_idx) for b in batches]
        sizes = [len(b) for b in batches]
        logger.info("  %-22s | %2d batches | sizes=%s | mean_BCS=%.4f | range=[%.4f, %.4f]",
                    mode, len(batches), sizes, np.mean(bcs_values),
                    min(bcs_values), max(bcs_values))

    logger.info("=" * 70)


# ── Stage: Extract ──────────────────────────────────────────────────

def stage_extract(args):
    """GPU stage: load vLLM, run inference per batch."""
    from vllm import LLM, SamplingParams
    from vllm.sampling_params import StructuredOutputsParams

    preprocess_path = args.preprocess_path or str(OUTPUT_DIR / args.mode / "preprocess.json")
    with open(preprocess_path) as f:
        config = json.load(f)

    samples = config["samples"]
    batch_list = config["batch_list"]
    relation_defs = config["relation_defs"]
    model_path = config["model_path"]
    mode = config["mode"]

    mode_dir = OUTPUT_DIR / mode
    results_path = mode_dir / "results_incremental.jsonl"

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
        logger.info("All batches completed.")
        return existing_results

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

    all_results = list(existing_results)

    for bi, batch in enumerate(remaining):
        batch_id = batch["batch_id"]
        batch_types = batch["types"]
        batch_bcs = batch["bcs"]
        type_set = set(batch_types)

        batch_samples = [s for s in samples if s["relation_type"] in type_set]
        if not batch_samples:
            logger.warning("No samples for batch %s — skipping", batch_id)
            continue

        logger.info("[%d/%d] %s: %d types, BCS=%.4f, %d samples",
                    bi + 1, len(remaining), batch_id,
                    len(batch_types), batch_bcs, len(batch_samples))

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
                pred_rel = "none"

            r = {
                "batch_id": batch_id,
                "batch_types": batch_types,
                "batch_bcs": batch_bcs,
                "ground_truth": s["relation_type"],
                "prediction": pred_rel,
                "raw_output": gen_text,
            }
            batch_results.append(r)
            all_results.append(r)

        # Incremental save
        with open(results_path, "a") as f:
            for r in batch_results:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

        correct = sum(1 for r in batch_results if r["prediction"] == r["ground_truth"])
        logger.info("  acc=%.4f (%d/%d)  elapsed=%.1fs",
                    correct / len(batch_results) if batch_results else 0,
                    correct, len(batch_results), elapsed)

    return all_results


# ── Stage: Analyze ───────────────────────────────────────────────────

def stage_analyze(args):
    """Analyze results for a given mode."""
    sim_matrix, type_names, type_to_idx = load_scs_matrix(args.scs_matrix)

    mode_dir = OUTPUT_DIR / args.mode
    results_path = mode_dir / "results_incremental.jsonl"

    results = []
    with open(results_path) as f:
        for line in f:
            if line.strip():
                results.append(json.loads(line))

    logger.info("Loaded %d results for mode=%s", len(results), args.mode)
    eval_out = evaluate_results(results, sim_matrix, type_to_idx)

    with open(mode_dir / "eval_results.json", "w") as f:
        json.dump(eval_out, f, indent=2, default=float)
    logger.info("Saved eval_results.json")

    logger.info("=" * 70)
    logger.info("RESULTS: %s", args.mode)
    logger.info("=" * 70)
    logger.info("  Overall accuracy: %.4f (%d/%d)",
                eval_out["overall_accuracy"], eval_out["correct"], eval_out["total"])
    logger.info("  Mean batch BCS: %.4f", eval_out["mean_batch_bcs"])
    logger.info("  Substitution rates: intra=%.3f, out_of_batch=%.3f, none=%.3f",
                eval_out["substitution_rates"]["intra_sub_rate"],
                eval_out["substitution_rates"]["out_of_batch_rate"],
                eval_out["substitution_rates"]["none_rate"])
    logger.info("-" * 70)
    for bid, m in eval_out["per_batch"].items():
        logger.info("  %-30s acc=%.4f (%3d/%3d) BCS=%.4f n_types=%d",
                    bid, m["accuracy"], m["correct"], m["total"], m["bcs"], m["n_types"])

    return eval_out


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Confusability-Aware Batch Composition (FewRel 80-rel)")
    parser.add_argument("--mode", choices=["single_pass", "random_batch", "confusability_aware"],
                        required=True)
    parser.add_argument("--scs_matrix", default=str(SCS_MATRIX_PATH),
                        help="Path to SCS/sim matrix .pt file")
    parser.add_argument("--n_batches", type=int, default=8,
                        help="Number of batches (K) for random/confusability modes")
    parser.add_argument("--n_eval_per_type", type=int, default=12,
                        help="Eval samples per relation type")
    parser.add_argument("--scs_threshold", type=float, default=0.0,
                        help="SCS threshold for graph edges (0=adaptive 75th pctl)")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--model_path", default=MODEL_PATH)
    parser.add_argument("--max_model_len", type=int, default=4096)
    parser.add_argument("--gpu_memory_utilization", type=float, default=0.90)
    parser.add_argument("--dry_run", action="store_true",
                        help="Only print batch partition and BCS, no inference")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--stage", choices=["preprocess", "extract", "analyze", "all"],
                        default="all")
    parser.add_argument("--preprocess_path", default=None)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s")

    if args.stage == "preprocess":
        stage_preprocess(args)
    elif args.stage == "extract":
        stage_extract(args)
    elif args.stage == "analyze":
        stage_analyze(args)
    elif args.stage == "all":
        preprocess_path = stage_preprocess(args)
        if preprocess_path is None:
            return

        logger.info("=== Launching extract subprocess ===")
        cmd = [sys.executable, str(Path(__file__).resolve()),
               "--stage", "extract", "--mode", args.mode,
               "--scs_matrix", args.scs_matrix]
        if args.resume:
            cmd.append("--resume")
        subprocess.run(cmd, check=True)

        stage_analyze(args)


if __name__ == "__main__":
    main()

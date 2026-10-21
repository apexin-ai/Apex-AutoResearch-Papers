#!/usr/bin/env python3
"""Confusability-aware batch composition experiment (exp-018) on FewRel 80-rel.

Compares three batching strategies for LLM-based relation extraction:
  1. confusability_aware — graph-coloring partition minimizing intra-batch SCS
  2. random_batch        — random partition (repeated N_RANDOM_SEEDS times for CI)
  3. single_pass         — all 80 types in one prompt (baseline)

Input:
  - SCS matrix: artifacts/fewrel_formal_full/relation_sim_matrix.pt
  - Data: data/fewrel_parquet/{train,val}.parquet (80 relation types)
  - Model: Qwen3-32B-FP8 via vLLM

Output:
  - artifacts/exp_confusability_batch_composition/results.json (unified metrics)
  - artifacts/exp_confusability_batch_composition/<mode>/results_incremental.jsonl
  - artifacts/exp_confusability_batch_composition/<mode>/eval_results.json

Two-stage execution (avoids vLLM fork deadlock):
    python3 src/run_confusability_batch_composition.py --stage all
    python3 src/run_confusability_batch_composition.py --stage all --dry_run
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
from typing import Dict, List

import numpy as np
import torch

logger = logging.getLogger(__name__)

BASE_DIR = Path(".")
OUTPUT_DIR = BASE_DIR / "artifacts" / "exp_confusability_batch_composition"
SCS_MATRIX_PATH = BASE_DIR / "artifacts" / "fewrel_formal_full" / "relation_sim_matrix.pt"
DATA_PATHS = [
    BASE_DIR / "data" / "fewrel_parquet" / "train.parquet",
    BASE_DIR / "data" / "fewrel_parquet" / "val.parquet",
]
MODEL_PATH = "~/.cache/huggingface/qwen3-32b-fp8/"
N_RANDOM_SEEDS = 15
BASE_SEED = 42


# ── SCS / BCS ────────────────────────────────────────────────────────────────

def load_scs_matrix(path: str = None):
    p = Path(path) if path else SCS_MATRIX_PATH
    data = torch.load(p, map_location="cpu", weights_only=True)
    return data["sim_matrix"], data["type_names"], data["type_to_idx"]


def compute_bcs_mean(type_subset: List[str], sim_matrix: torch.Tensor,
                     type_to_idx: dict) -> float:
    if len(type_subset) < 2:
        return 0.0
    indices = [type_to_idx[t] for t in type_subset]
    total, count = 0.0, 0
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            total += sim_matrix[indices[i], indices[j]].item()
            count += 1
    return total / count


# ── Partition Strategies ─────────────────────────────────────────────────────

def partition_single_pass(type_names: List[str]) -> List[List[str]]:
    return [list(type_names)]


def partition_random(type_names: List[str], n_batches: int, seed: int = 42) -> List[List[str]]:
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
    """Graph-coloring partition minimizing intra-batch confusability."""
    import networkx as nx

    n = len(type_names)
    G = nx.Graph()
    G.add_nodes_from(range(n))

    sim_np = sim_matrix.numpy()
    if threshold <= 0:
        upper = [sim_np[i, j] for i in range(n) for j in range(i + 1, n)]
        threshold = float(np.percentile(upper, 75))
        logger.info("Adaptive SCS threshold (75th percentile): %.4f", threshold)

    for i in range(n):
        for j in range(i + 1, n):
            if sim_np[i, j] > threshold:
                G.add_edge(i, j, weight=sim_np[i, j])

    logger.info("Graph: %d nodes, %d edges (threshold=%.4f)",
                G.number_of_nodes(), G.number_of_edges(), threshold)

    coloring = nx.coloring.greedy_color(G, strategy='largest_first')
    n_colors = max(coloring.values()) + 1
    logger.info("Initial greedy coloring: %d colors", n_colors)

    color_groups = defaultdict(list)
    for node, color in coloring.items():
        color_groups[color].append(node)

    batches = _balance_to_k(color_groups, n_batches, sim_np)
    return [[type_names[idx] for idx in batch] for batch in batches]


def _balance_to_k(color_groups: dict, k: int, sim_np: np.ndarray) -> List[List[int]]:
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

    for _ in range(50):
        groups.sort(key=len, reverse=True)
        largest = groups[0]
        smallest = groups[-1]
        if len(largest) - len(smallest) <= 1:
            break
        best_node, best_cost = None, float("inf")
        for node in largest:
            cost = np.mean([sim_np[node, s] for s in smallest]) if smallest else 0.0
            if cost < best_cost:
                best_cost = cost
                best_node = node
        largest.remove(best_node)
        smallest.append(best_node)

    return groups


# ── Prompt & Schema ──────────────────────────────────────────────────────────

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


# ── Evaluation ───────────────────────────────────────────────────────────────

def compute_substitution_rate(results: List[dict]) -> dict:
    total_wrong = intra_sub = out_of_batch = none_pred = 0
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
            "correct": s["correct"], "total": s["total"],
            "n_types": len(s["types"]), "bcs": round(bcs, 4),
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
    macro_acc = float(np.mean(list(per_type_acc.values()))) if per_type_acc else 0.0

    return {
        "overall_accuracy": correct / total if total else 0.0,
        "macro_accuracy": macro_acc,
        "correct": correct, "total": total,
        "per_batch": per_batch,
        "substitution_rates": sub_rates,
        "per_type_accuracy": per_type_acc,
        "mean_batch_bcs": float(np.mean([b["bcs"] for b in per_batch.values()])),
    }


# ── Build All Conditions ─────────────────────────────────────────────────────

def build_all_conditions(type_names, sim_matrix, type_to_idx, n_batches, scs_threshold, seed):
    """Return list of (condition_id, batch_list) for all experiment conditions."""
    conditions = []

    # 1. confusability_aware (single run)
    ca_batches = partition_confusability_aware(
        sim_matrix, type_names, type_to_idx,
        n_batches=n_batches, threshold=scs_threshold)
    ca_batch_list = []
    for i, bt in enumerate(ca_batches):
        bcs = compute_bcs_mean(bt, sim_matrix, type_to_idx)
        ca_batch_list.append({"batch_id": f"confusability_aware_batch_{i}",
                              "types": bt, "bcs": round(bcs, 4), "size": len(bt)})
    conditions.append(("confusability_aware", ca_batch_list))

    # 2. random_batch (N_RANDOM_SEEDS runs)
    for ri in range(N_RANDOM_SEEDS):
        rs = seed + ri
        rb = partition_random(type_names, n_batches, seed=rs)
        rb_list = []
        for i, bt in enumerate(rb):
            bcs = compute_bcs_mean(bt, sim_matrix, type_to_idx)
            rb_list.append({"batch_id": f"random_seed{rs}_batch_{i}",
                            "types": bt, "bcs": round(bcs, 4), "size": len(bt)})
        conditions.append((f"random_batch_seed{rs}", rb_list))

    # 3. single_pass (single run)
    sp_batches = partition_single_pass(type_names)
    sp_list = []
    for i, bt in enumerate(sp_batches):
        bcs = compute_bcs_mean(bt, sim_matrix, type_to_idx)
        sp_list.append({"batch_id": "single_pass_batch_0",
                        "types": bt, "bcs": round(bcs, 4), "size": len(bt)})
    conditions.append(("single_pass", sp_list))

    return conditions


# ── Stage: Preprocess ────────────────────────────────────────────────────────

def stage_preprocess(args):
    sys.path.insert(0, str(BASE_DIR / "src"))
    from fewrel_utils import load_fewrel, get_all_relation_types, sample_balanced

    logger.info("Loading FewRel data...")
    all_samples = []
    for dp in DATA_PATHS:
        all_samples.extend(load_fewrel(data_path=str(dp)))
    all_relations = get_all_relation_types(all_samples)
    logger.info("%d samples, %d relations", len(all_samples), len(all_relations))

    samples = sample_balanced(all_samples, args.n_eval_per_type, seed=args.seed)
    logger.info("Balanced sample: %d (%d/rel)", len(samples), args.n_eval_per_type)

    with open(BASE_DIR / "configs" / "fewrel_relation_types.json") as f:
        pid2name = json.load(f)
    relation_defs = {name: name for name in pid2name.values()}

    sim_matrix, type_names, type_to_idx = load_scs_matrix(args.scs_matrix)
    logger.info("SCS matrix: %d types", len(type_names))

    conditions = build_all_conditions(
        type_names, sim_matrix, type_to_idx,
        args.n_batches, args.scs_threshold, args.seed)

    # Log summary
    logger.info("=" * 70)
    logger.info("CONDITIONS: %d total", len(conditions))
    logger.info("=" * 70)
    total_inf = 0
    for cond_id, batch_list in conditions:
        bcs_vals = [b["bcs"] for b in batch_list]
        sizes = [b["size"] for b in batch_list]
        n_inf = 0
        for b in batch_list:
            ts = set(b["types"])
            n_inf += sum(1 for s in samples if s["relation_type"] in ts)
        total_inf += n_inf
        logger.info("  %-30s | %2d batches | sizes=%s | mean_BCS=%.4f | inferences=%d",
                    cond_id, len(batch_list), sizes, np.mean(bcs_vals), n_inf)
    logger.info("Total inferences across all conditions: %d", total_inf)
    est_sec = 0.8
    logger.info("Estimated time: ~%.0f min (@%.1fs/sample)", total_inf * est_sec / 60, est_sec)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    preprocess_config = {
        "conditions": [(cid, bl) for cid, bl in conditions],
        "samples": samples,
        "relation_defs": relation_defs,
        "model_path": args.model_path,
        "max_model_len": args.max_model_len,
        "gpu_memory_utilization": args.gpu_memory_utilization,
        "seed": args.seed,
        "n_batches": args.n_batches,
        "n_random_seeds": N_RANDOM_SEEDS,
        "n_eval_per_type": args.n_eval_per_type,
    }
    preprocess_path = OUTPUT_DIR / "preprocess.json"
    with open(preprocess_path, "w") as f:
        json.dump(preprocess_config, f, ensure_ascii=False)
    logger.info("Saved preprocess config to %s", preprocess_path)

    if args.dry_run:
        logger.info("DRY RUN — stopping before GPU extraction.")
        return None

    return str(preprocess_path)


# ── Stage: Extract ───────────────────────────────────────────────────────────

def stage_extract(args):
    """GPU stage: load vLLM once, run all conditions sequentially."""
    from vllm import LLM, SamplingParams
    from vllm.sampling_params import StructuredOutputsParams

    preprocess_path = args.preprocess_path or str(OUTPUT_DIR / "preprocess.json")
    with open(preprocess_path) as f:
        config = json.load(f)

    samples = config["samples"]
    conditions = config["conditions"]
    relation_defs = config["relation_defs"]
    model_path = config["model_path"]

    # Track completed conditions for resume
    completed_file = OUTPUT_DIR / "completed_conditions.json"
    completed = set()
    if args.resume and completed_file.exists():
        with open(completed_file) as f:
            completed = set(json.load(f))
        logger.info("Resumed: %d completed conditions", len(completed))

    remaining = [(cid, bl) for cid, bl in conditions if cid not in completed]
    if not remaining:
        logger.info("All conditions completed.")
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

    for ci, (cond_id, batch_list) in enumerate(remaining):
        logger.info("=" * 70)
        logger.info("CONDITION [%d/%d]: %s (%d batches)",
                    ci + 1, len(remaining), cond_id, len(batch_list))
        logger.info("=" * 70)

        cond_dir = OUTPUT_DIR / cond_id
        cond_dir.mkdir(parents=True, exist_ok=True)
        results_path = cond_dir / "results_incremental.jsonl"

        # Check for partially completed batches within this condition
        done_batches = set()
        existing = []
        if args.resume and results_path.exists():
            with open(results_path) as f:
                for line in f:
                    if line.strip():
                        r = json.loads(line)
                        existing.append(r)
                        done_batches.add(r["batch_id"])

        for bi, batch in enumerate(batch_list):
            batch_id = batch["batch_id"]
            if batch_id in done_batches:
                logger.info("  [%d/%d] %s — already done, skipping",
                            bi + 1, len(batch_list), batch_id)
                continue

            batch_types = batch["types"]
            batch_bcs = batch["bcs"]
            type_set = set(batch_types)
            batch_samples = [s for s in samples if s["relation_type"] in type_set]

            if not batch_samples:
                logger.warning("  No samples for batch %s — skipping", batch_id)
                continue

            logger.info("  [%d/%d] %s: %d types, BCS=%.4f, %d samples",
                        bi + 1, len(batch_list), batch_id,
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
                    "condition_id": cond_id,
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

            with open(results_path, "a") as f:
                for r in batch_results:
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")

            correct = sum(1 for r in batch_results if r["prediction"] == r["ground_truth"])
            acc = correct / len(batch_results) if batch_results else 0
            logger.info("    acc=%.4f (%d/%d), %.1fs", acc, correct, len(batch_results), elapsed)

        # Mark condition as completed
        completed.add(cond_id)
        with open(completed_file, "w") as f:
            json.dump(sorted(completed), f)
        logger.info("Condition %s complete.", cond_id)


# ── Stage: Analyze ───────────────────────────────────────────────────────────

def stage_analyze(args):
    """Analyze all conditions and produce unified results JSON."""
    sim_matrix, type_names, type_to_idx = load_scs_matrix(args.scs_matrix)

    preprocess_path = args.preprocess_path or str(OUTPUT_DIR / "preprocess.json")
    with open(preprocess_path) as f:
        config = json.load(f)
    conditions = config["conditions"]

    all_evals = {}
    for cond_id, batch_list in conditions:
        cond_dir = OUTPUT_DIR / cond_id
        results_path = cond_dir / "results_incremental.jsonl"
        if not results_path.exists():
            logger.warning("No results for %s — skipping", cond_id)
            continue

        results = []
        with open(results_path) as f:
            for line in f:
                if line.strip():
                    results.append(json.loads(line))

        ev = evaluate_results(results, sim_matrix, type_to_idx)
        all_evals[cond_id] = ev

        eval_path = cond_dir / "eval_results.json"
        with open(eval_path, "w") as f:
            json.dump(ev, f, indent=2, default=float)

    # Aggregate random_batch runs
    random_evals = {k: v for k, v in all_evals.items() if k.startswith("random_batch_seed")}
    ca_eval = all_evals.get("confusability_aware")
    sp_eval = all_evals.get("single_pass")

    summary = {"conditions": {}}

    if ca_eval:
        summary["conditions"]["confusability_aware"] = {
            "overall_accuracy": ca_eval["overall_accuracy"],
            "macro_accuracy": ca_eval["macro_accuracy"],
            "mean_batch_bcs": ca_eval["mean_batch_bcs"],
            "substitution_rates": ca_eval["substitution_rates"],
            "n_runs": 1,
        }
        logger.info("confusability_aware: acc=%.4f, macro=%.4f, bcs=%.4f, intra_sub=%d",
                    ca_eval["overall_accuracy"], ca_eval["macro_accuracy"],
                    ca_eval["mean_batch_bcs"],
                    ca_eval["substitution_rates"].get("intra_sub_count", 0))

    if random_evals:
        accs = [v["overall_accuracy"] for v in random_evals.values()]
        macros = [v["macro_accuracy"] for v in random_evals.values()]
        bcs_vals = [v["mean_batch_bcs"] for v in random_evals.values()]
        intra_subs = [v["substitution_rates"].get("intra_sub_count", 0) for v in random_evals.values()]

        def ci95(vals):
            m = np.mean(vals)
            s = np.std(vals, ddof=1)
            n = len(vals)
            margin = 1.96 * s / np.sqrt(n)
            return {"mean": float(m), "std": float(s), "ci95_lo": float(m - margin),
                    "ci95_hi": float(m + margin), "n": n, "values": [float(v) for v in vals]}

        summary["conditions"]["random_batch"] = {
            "overall_accuracy": ci95(accs),
            "macro_accuracy": ci95(macros),
            "mean_batch_bcs": ci95(bcs_vals),
            "intra_sub_count": ci95(intra_subs),
            "n_runs": len(random_evals),
        }
        logger.info("random_batch (%d runs): acc=%.4f±%.4f [%.4f, %.4f], macro=%.4f±%.4f, bcs=%.4f",
                    len(accs), np.mean(accs), np.std(accs),
                    np.mean(accs) - 1.96 * np.std(accs) / np.sqrt(len(accs)),
                    np.mean(accs) + 1.96 * np.std(accs) / np.sqrt(len(accs)),
                    np.mean(macros), np.std(macros), np.mean(bcs_vals))

    if sp_eval:
        summary["conditions"]["single_pass"] = {
            "overall_accuracy": sp_eval["overall_accuracy"],
            "macro_accuracy": sp_eval["macro_accuracy"],
            "mean_batch_bcs": sp_eval["mean_batch_bcs"],
            "substitution_rates": sp_eval["substitution_rates"],
            "n_runs": 1,
        }
        logger.info("single_pass: acc=%.4f, macro=%.4f, bcs=%.4f, intra_sub=%d",
                    sp_eval["overall_accuracy"], sp_eval["macro_accuracy"],
                    sp_eval["mean_batch_bcs"],
                    sp_eval["substitution_rates"].get("intra_sub_count", 0))

    # Per-type accuracy comparison (confusability_aware vs mean-random)
    if ca_eval and random_evals:
        ca_pt = ca_eval["per_type_accuracy"]
        random_pt_agg = defaultdict(list)
        for rv in random_evals.values():
            for t, a in rv["per_type_accuracy"].items():
                random_pt_agg[t].append(a)
        per_type_comparison = {}
        for t in sorted(ca_pt.keys()):
            ca_a = ca_pt[t]
            ra_vals = random_pt_agg.get(t, [])
            ra_mean = float(np.mean(ra_vals)) if ra_vals else 0.0
            per_type_comparison[t] = {
                "confusability_aware": ca_a,
                "random_mean": ra_mean,
                "delta": ca_a - ra_mean,
            }
        summary["per_type_comparison"] = per_type_comparison

        deltas = [v["delta"] for v in per_type_comparison.values()]
        n_improved = sum(1 for d in deltas if d > 0)
        n_degraded = sum(1 for d in deltas if d < 0)
        summary["per_type_summary"] = {
            "n_types": len(deltas),
            "n_improved": n_improved,
            "n_degraded": n_degraded,
            "n_tied": len(deltas) - n_improved - n_degraded,
            "mean_delta": float(np.mean(deltas)),
            "median_delta": float(np.median(deltas)),
        }
        logger.info("Per-type: %d improved, %d degraded, mean Δ=%.4f",
                    n_improved, n_degraded, np.mean(deltas))

    summary_path = OUTPUT_DIR / "results.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2, default=float)
    logger.info("Saved unified results to %s", summary_path)

    return summary


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Confusability-Aware Batch Composition exp-018 (FewRel 80-rel)")
    parser.add_argument("--scs_matrix", default=str(SCS_MATRIX_PATH))
    parser.add_argument("--n_batches", type=int, default=8)
    parser.add_argument("--n_eval_per_type", type=int, default=12)
    parser.add_argument("--scs_threshold", type=float, default=0.0,
                        help="SCS threshold for graph edges (0=adaptive 75th pctl)")
    parser.add_argument("--seed", type=int, default=BASE_SEED)
    parser.add_argument("--model_path", default=MODEL_PATH)
    parser.add_argument("--max_model_len", type=int, default=4096)
    parser.add_argument("--gpu_memory_utilization", type=float, default=0.90)
    parser.add_argument("--dry_run", action="store_true")
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
               "--stage", "extract", "--scs_matrix", args.scs_matrix,
               "--preprocess_path", preprocess_path]
        if args.resume:
            cmd.append("--resume")
        subprocess.run(cmd, check=True)

        stage_analyze(args)


if __name__ == "__main__":
    main()

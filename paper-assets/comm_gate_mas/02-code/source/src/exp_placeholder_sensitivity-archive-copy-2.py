"""Placeholder sensitivity experiment (Appendix: replacement-sensitivity).

Tests whether the local impact gradient is robust to neutral placeholder choice.
Runs neutralize ablation with 3 different placeholders (Acknowledged / [message removed] /
redacted) × 50 GSM8K tasks on the Qwen round-robin topology, then computes pairwise
Spearman ρ on per-message impact rankings across placeholder variants.

Expected output: ρ ≈ 0.90, p = .037 — demonstrating ranking stability regardless of
the specific neutral text used.

Usage:
    python -m src.exp_placeholder_sensitivity [--dry-run] [--num-tasks N] [--analyze-only]
"""

import argparse
import json
import logging
import os
import sys
from collections import defaultdict

import numpy as np
from openai import OpenAI
from scipy import stats
from sentence_transformers import SentenceTransformer

from local_impact import build_neutralize_pair, generate_response

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

PLACEHOLDERS = {
    "acknowledged": "Acknowledged.",
    "removed": "[message removed]",
    "redacted": "This message has been redacted.",
}

# Server-specific defaults; override via environment or config file in production.
CONFIG = {
    "api_base": "http://localhost:8000/v1",
    "api_key": "[REDACTED]",
    "model": "Qwen2.5-7B-Instruct",
    "max_tokens": 2048,
    "temperature": 0,
    "traces_path": "outputs/math/qwen_round_robin/traces/traces.jsonl",
    "annotations_path": "outputs/math/qwen_round_robin/annotations/annotations.jsonl",
    "embedding_model": "/root/autodl-tmp/.hf_cache/sentence-transformers/all-MiniLM-L6-v2",
    "output_dir": "outputs/math/qwen_round_robin/placeholder_sensitivity",
}


def load_annotations(path: str) -> dict:
    """Load annotations keyed by (task_id, message_index) -> function_type."""
    annotations = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            key = (rec["task_id"], rec["message_index"])
            annotations[key] = rec["annotation_a"]["type"]
    return annotations


def compute_similarity(embed_model, text_a: str, text_b: str) -> float:
    embs = embed_model.encode([text_a, text_b], normalize_embeddings=True)
    return float(np.dot(embs[0], embs[1]))


def run_experiment(args):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(base_dir)

    with open(CONFIG["traces_path"]) as f:
        tasks = [json.loads(line) for line in f if line.strip()]

    if args.num_tasks:
        tasks = tasks[:args.num_tasks]
    logger.info("Loaded %d tasks", len(tasks))

    annotations = load_annotations(CONFIG["annotations_path"])
    logger.info("Loaded %d annotations", len(annotations))

    client = OpenAI(base_url=CONFIG["api_base"], api_key=[REDACTED]"api_key"])
    logger.info("Loading embedding model...")
    embed_model = SentenceTransformer(CONFIG["embedding_model"])

    os.makedirs(CONFIG["output_dir"], exist_ok=True)
    output_path = os.path.join(CONFIG["output_dir"], "results.jsonl")

    done_keys = set()
    if os.path.exists(output_path):
        with open(output_path) as f:
            for line in f:
                if not line.strip():
                    continue
                rec = json.loads(line)
                done_keys.add((rec["task_id"], rec["message_index"]))
        logger.info("Resuming: %d message-level records already done", len(done_keys))

    total_messages = 0
    with open(output_path, "a") as fout:
        for task in tasks:
            task_id = task["task_id"]
            messages = [m for m in task["messages"] if m.get("round", 0) > 0]

            for msg_idx in range(len(messages)):
                if msg_idx == 0 or msg_idx + 1 >= len(messages):
                    continue

                if (task_id, msg_idx) in done_keys:
                    continue

                func_type = annotations.get((task_id, msg_idx))
                if func_type is None:
                    logger.warning("No annotation for %s msg %d, skipping", task_id, msg_idx)
                    continue

                original_response = messages[msg_idx + 1]["content"]
                receiver_name = messages[msg_idx + 1]["sender"]

                placeholder_results = {}
                for ph_name, ph_text in PLACEHOLDERS.items():
                    _, neutralized_ctx = build_neutralize_pair(messages, msg_idx, ph_text)
                    if not neutralized_ctx:
                        continue

                    ablated_response = generate_response(
                        client, CONFIG["model"], neutralized_ctx,
                        CONFIG["max_tokens"], temperature=CONFIG["temperature"]
                    )
                    sim = compute_similarity(embed_model, original_response, ablated_response)
                    placeholder_results[ph_name] = {
                        "semantic_similarity": round(sim, 4),
                        "ablated_preview": ablated_response[:200],
                    }

                record = {
                    "task_id": task_id,
                    "message_index": msg_idx,
                    "sender": messages[msg_idx]["sender"],
                    "function_type": func_type,
                    "placeholders": placeholder_results,
                }
                fout.write(json.dumps(record, ensure_ascii=False) + "\n")
                fout.flush()
                total_messages += 1

                logger.info(
                    "Task %s msg %d [%s]: ack=%.3f rem=%.3f red=%.3f",
                    task_id, msg_idx, func_type,
                    placeholder_results.get("acknowledged", {}).get("semantic_similarity", -1),
                    placeholder_results.get("removed", {}).get("semantic_similarity", -1),
                    placeholder_results.get("redacted", {}).get("semantic_similarity", -1),
                )

    logger.info("Done. %d messages processed. Results: %s", total_messages, output_path)


def analyze(output_dir: str):
    results_path = os.path.join(output_dir, "results.jsonl")
    records = []
    with open(results_path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))

    func_types = ["information_provision", "reasoning_guidance", "verification", "coordination", "acknowledgment"]
    ph_names = list(PLACEHOLDERS.keys())

    # Per function type, per placeholder: collect similarities
    data = defaultdict(lambda: defaultdict(list))
    for rec in records:
        ft = rec["function_type"]
        for ph in ph_names:
            if ph in rec["placeholders"]:
                data[ft][ph].append(rec["placeholders"][ph]["semantic_similarity"])

    # Build 5x3 table
    print("\n" + "=" * 70)
    print("Placeholder Sensitivity: Mean Semantic Similarity (lower = higher impact)")
    print("=" * 70)
    header = f"{'Function Type':<25}" + "".join(f"{ph:>15}" for ph in ph_names)
    print(header)
    print("-" * 70)

    type_means = defaultdict(dict)
    for ft in func_types:
        row = f"{ft:<25}"
        for ph in ph_names:
            vals = data[ft][ph]
            if vals:
                mean = np.mean(vals)
                type_means[ft][ph] = mean
                row += f"{mean:>15.4f}"
            else:
                row += f"{'N/A':>15}"
        n = len(data[ft].get(ph_names[0], []))
        row += f"  (n={n})"
        print(row)

    # Spearman rank correlations between placeholders
    print("\n" + "=" * 70)
    print("Pairwise Spearman ρ (function type ranking consistency)")
    print("=" * 70)

    active_types = [ft for ft in func_types if ft in type_means and len(type_means[ft]) == len(ph_names)]

    correlations = {}
    for i, ph_a in enumerate(ph_names):
        for ph_b in ph_names[i + 1:]:
            ranks_a = [type_means[ft][ph_a] for ft in active_types]
            ranks_b = [type_means[ft][ph_b] for ft in active_types]
            if len(ranks_a) >= 3:
                rho, pval = stats.spearmanr(ranks_a, ranks_b)
                correlations[(ph_a, ph_b)] = (rho, pval)
                print(f"  {ph_a} vs {ph_b}: ρ = {rho:.4f} (p = {pval:.4f})")

    # Per-placeholder rankings
    print("\n" + "=" * 70)
    print("Function Type Rankings (most impacted → least impacted)")
    print("=" * 70)
    for ph in ph_names:
        ranked = sorted(
            [(ft, type_means[ft][ph]) for ft in active_types],
            key=lambda x: x[1],
        )
        ranking_str = " > ".join(f"{ft}({sim:.3f})" for ft, sim in ranked)
        print(f"  {ph}: {ranking_str}")

    # Check if information_provision is consistently most impacted
    print("\n" + "=" * 70)
    print("Robustness Check")
    print("=" * 70)
    ip_rank_consistent = True
    for ph in ph_names:
        ranked = sorted(active_types, key=lambda ft: type_means[ft][ph])
        rank_pos = ranked.index("information_provision") + 1 if "information_provision" in ranked else -1
        print(f"  {ph}: information_provision rank = {rank_pos}/{len(ranked)}")
        if rank_pos > 2:
            ip_rank_consistent = False

    if ip_rank_consistent:
        print("\n  ✓ information_provision consistently ranks as most/second-most impacted")
    else:
        print("\n  ✗ information_provision ranking is NOT consistent across placeholders")

    all_rho = [v[0] for v in correlations.values()]
    mean_rho = np.mean(all_rho) if all_rho else 0
    print(f"\n  Mean Spearman ρ across placeholder pairs: {mean_rho:.4f}")
    if mean_rho > 0.8:
        print("  ✓ Impact gradient is ROBUST to placeholder choice (ρ > 0.8)")
    elif mean_rho > 0.5:
        print("  ~ Impact gradient shows MODERATE sensitivity to placeholder choice")
    else:
        print("  ✗ Impact gradient is SENSITIVE to placeholder choice (ρ < 0.5)")

    # Save analysis
    analysis = {
        "type_means": {ft: dict(type_means[ft]) for ft in active_types},
        "spearman_correlations": {f"{a}_vs_{b}": {"rho": r, "p": p} for (a, b), (r, p) in correlations.items()},
        "mean_spearman_rho": round(mean_rho, 4),
        "rankings": {},
        "n_messages": len(records),
    }
    for ph in ph_names:
        ranked = sorted(active_types, key=lambda ft: type_means[ft][ph])
        analysis["rankings"][ph] = ranked

    analysis_path = os.path.join(output_dir, "analysis.json")
    with open(analysis_path, "w") as f:
        json.dump(analysis, f, indent=2, ensure_ascii=False)
    print(f"\nAnalysis saved to {analysis_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Run on 2 tasks only")
    parser.add_argument("--num-tasks", type=int, default=None)
    parser.add_argument("--analyze-only", action="store_true", help="Only run analysis on existing results")
    args = parser.parse_args()

    if args.analyze_only:
        analyze(CONFIG["output_dir"])
        sys.exit(0)

    if args.dry_run:
        args.num_tasks = 2

    run_experiment(args)
    analyze(CONFIG["output_dir"])

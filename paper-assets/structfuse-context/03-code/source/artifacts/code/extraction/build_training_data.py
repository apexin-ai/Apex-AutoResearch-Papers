"""
StructFuse Stage 1→2 bridge: build contrastive training data from data-flow features.

Reads extraction output (all.jsonl from extract_dataflow.py) and original repo code
to produce contrastive training triples (query, positive, negatives) with feature vectors.

Output format: JSONL compatible with HuggingFace datasets.load_dataset("json").
Each line: {query, pos_code, neg_codes, features, metadata}

Dependencies: rank_bm25, numpy
"""

import argparse
import json
import logging
import os
import random
from collections import defaultdict
from pathlib import Path
from typing import Any

import numpy as np

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
log = logging.getLogger("build_training_data")


# ---------------------------------------------------------------------------
# File reading
# ---------------------------------------------------------------------------

def read_file_content(repo_path: str, file_path: str) -> str | None:
    """Read a source file from repo, return content or None."""
    full = os.path.join(repo_path, file_path)
    if not os.path.isfile(full):
        return None
    try:
        with open(full, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return None


def collect_repo_files(repo_path: str) -> list[str]:
    """List all .py files in the repo (relative paths)."""
    files = []
    for root, _dirs, filenames in os.walk(repo_path):
        for fname in filenames:
            if fname.endswith(".py"):
                rel = os.path.relpath(os.path.join(root, fname), repo_path)
                files.append(rel)
    return files


# ---------------------------------------------------------------------------
# BM25
# ---------------------------------------------------------------------------

def build_bm25_index(documents: list[str]):
    """Build BM25 index over tokenized documents."""
    from rank_bm25 import BM25Okapi
    tokenized = [doc.split() for doc in documents]
    return BM25Okapi(tokenized)


def bm25_scores(bm25_index, query: str) -> np.ndarray:
    return bm25_index.get_scores(query.split())


# ---------------------------------------------------------------------------
# Feature computation
# ---------------------------------------------------------------------------

def compute_features(
    instance: dict,
    file_path: str,
    bm25_score: float,
    connected_files: dict[str, dict],
) -> dict[str, float]:
    """
    Compute feature vector for a (instance, file) pair.
    Returns dict of normalized features.
    """
    info = connected_files.get(file_path)
    if info:
        df_distance = info["min_path_length"]
        path_count = info["path_count"]
        dep_type = 1.0 if info.get("inter_procedural", False) else 0.0
    else:
        df_distance = 999
        path_count = 0
        dep_type = 0.0

    return {
        "dataflow_distance": float(df_distance),
        "dataflow_path_count": float(path_count),
        "dependency_type": dep_type,
        "bm25_score": float(bm25_score),
        "inter_procedural": 1.0 if instance.get("inter_procedural", False) else 0.0,
    }


def normalize_features(instances: list[dict]) -> list[dict]:
    """Min-max normalize feature vectors across all instances."""
    if not instances:
        return instances

    keys = ["dataflow_distance", "dataflow_path_count", "bm25_score"]
    all_features = []
    for inst in instances:
        all_features.append(inst["features"])
        for neg in inst.get("neg_features", []):
            all_features.append(neg)

    mins = {k: float("inf") for k in keys}
    maxs = {k: float("-inf") for k in keys}
    for feat in all_features:
        for k in keys:
            v = feat.get(k, 0.0)
            mins[k] = min(mins[k], v)
            maxs[k] = max(maxs[k], v)

    def norm(feat: dict) -> dict:
        out = dict(feat)
        for k in keys:
            rng = maxs[k] - mins[k]
            if rng > 0:
                out[k] = (out[k] - mins[k]) / rng
            else:
                out[k] = 0.0
        return out

    for inst in instances:
        inst["features"] = norm(inst["features"])
        inst["neg_features"] = [norm(nf) for nf in inst.get("neg_features", [])]

    return instances


# ---------------------------------------------------------------------------
# Negative sampling strategies
# ---------------------------------------------------------------------------

def sample_negatives(
    query: str,
    positive_files: set[str],
    connected_files: set[str],
    all_files: list[str],
    file_contents: dict[str, str],
    bm25_index,
    num_negatives: int,
    hard_negative_ratio: float,
) -> tuple[list[str], list[str]]:
    """
    Sample negatives with a mix of strategies:
    - hard_negative_ratio fraction: BM25-similar but structurally disconnected
    - remaining: random from repo

    Returns (neg_file_paths, neg_strategies).
    """
    candidate_pool = [
        f for f in all_files
        if f not in positive_files and f in file_contents
    ]
    if not candidate_pool:
        return [], []

    num_hard = int(num_negatives * hard_negative_ratio)
    num_random = num_negatives - num_hard

    neg_files = []
    neg_strategies = []

    # Hard negatives: high BM25 but NOT in connected_files
    if num_hard > 0 and bm25_index is not None:
        disconnected = [f for f in candidate_pool if f not in connected_files]
        if disconnected:
            scores = bm25_scores(bm25_index, query)
            file_to_idx = {f: i for i, f in enumerate(all_files)}
            scored = [
                (f, scores[file_to_idx[f]])
                for f in disconnected
                if f in file_to_idx and file_to_idx[f] < len(scores)
            ]
            scored.sort(key=lambda x: x[1], reverse=True)
            for f, _ in scored[:num_hard]:
                neg_files.append(f)
                neg_strategies.append("bm25_hard")

    # Random negatives
    remaining_pool = [f for f in candidate_pool if f not in set(neg_files)]
    if remaining_pool and num_random > 0:
        sample_size = min(num_random, len(remaining_pool))
        for f in random.sample(remaining_pool, sample_size):
            neg_files.append(f)
            neg_strategies.append("random")

    return neg_files[:num_negatives], neg_strategies[:num_negatives]


# ---------------------------------------------------------------------------
# Instance building
# ---------------------------------------------------------------------------

def build_instance(
    extraction: dict,
    repos_dir: str,
    bm25_index,
    all_files: list[str],
    file_contents: dict[str, str],
    num_negatives: int,
    hard_negative_ratio: float,
    max_seq_length: int = 2048,
) -> dict[str, Any] | None:
    """Build a single training instance from extraction result."""
    repo_path = extraction["repo_path"]
    query = extraction.get("issue_text", "")
    if not query:
        query = f"Bug in {extraction['buggy_function']} at {extraction['buggy_file']}"

    # Identify data-flow-connected files and their properties
    connected_files: dict[str, dict] = {}
    for path_info in extraction.get("dataflow_paths", []):
        for key in ("source_file", "sink_file"):
            fpath = path_info.get(key, "")
            if not fpath:
                continue
            pl = path_info.get("path_length", 1)
            if fpath not in connected_files:
                connected_files[fpath] = {
                    "min_path_length": pl,
                    "path_count": 1,
                    "inter_procedural": extraction.get("inter_procedural", False),
                }
            else:
                connected_files[fpath]["path_count"] += 1
                connected_files[fpath]["min_path_length"] = min(
                    connected_files[fpath]["min_path_length"], pl
                )

    # Also include call-graph files
    for cg in extraction.get("call_graph", []):
        fpath = cg.get("file_path", "")
        if fpath and fpath not in connected_files:
            connected_files[fpath] = {
                "min_path_length": cg.get("hop_distance", 2),
                "path_count": 1,
                "inter_procedural": extraction.get("inter_procedural", False),
            }

    # Always include the buggy file
    buggy_file = extraction["buggy_file"]
    if buggy_file not in connected_files:
        connected_files[buggy_file] = {
            "min_path_length": 0,
            "path_count": 1,
            "inter_procedural": extraction.get("inter_procedural", False),
        }

    # Positive: concatenated by path_distance ascending, truncated to token budget
    positive_files = set(connected_files.keys())
    pos_parts = []
    token_budget = max_seq_length * 4  # rough char budget (≈1 token per 4 chars)
    char_count = 0
    for fpath, info in sorted(connected_files.items(), key=lambda x: x[1]["min_path_length"]):
        content = file_contents.get(fpath)
        if content:
            if char_count + len(content) > token_budget:
                break
            pos_parts.append(content)
            char_count += len(content) + 2
    if not pos_parts:
        return None
    pos_code = "\n\n".join(pos_parts)

    # BM25 scores
    scores_array = bm25_scores(bm25_index, query) if bm25_index else np.zeros(len(all_files))

    # Negative sampling
    neg_files, neg_strategies = sample_negatives(
        query, positive_files, set(connected_files.keys()),
        all_files, file_contents, bm25_index,
        num_negatives, hard_negative_ratio,
    )

    neg_codes = []
    neg_features = []
    file_to_idx = {f: i for i, f in enumerate(all_files)}
    for nf, strat in zip(neg_files, neg_strategies):
        content = file_contents.get(nf, "")
        neg_codes.append(content)
        bm25_val = float(scores_array[file_to_idx[nf]]) if nf in file_to_idx and file_to_idx[nf] < len(scores_array) else 0.0
        neg_features.append(compute_features(extraction, nf, bm25_val, connected_files))

    # Positive features (using buggy_file as representative)
    buggy_bm25 = float(scores_array[file_to_idx[buggy_file]]) if buggy_file in file_to_idx and file_to_idx[buggy_file] < len(scores_array) else 0.0
    pos_features = compute_features(extraction, buggy_file, buggy_bm25, connected_files)

    return {
        "instance_id": extraction.get("instance_id", ""),
        "query": query,
        "pos_code": pos_code,
        "neg_codes": neg_codes,
        "features": pos_features,
        "neg_features": neg_features,
        "metadata": {
            "inter_procedural": extraction.get("inter_procedural", False),
            "extraction_method": extraction.get("extraction_method", ""),
            "num_connected_files": len(connected_files),
            "num_dataflow_paths": len(extraction.get("dataflow_paths", [])),
            "neg_strategies": neg_strategies,
        },
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Build contrastive training data from data-flow extractions"
    )
    parser.add_argument("--dataflow-dir", required=True,
                        help="Directory containing all.jsonl from extract_dataflow.py")
    parser.add_argument("--repos-dir", required=True,
                        help="Root directory containing all repos")
    parser.add_argument("--output-file", required=True,
                        help="Output JSONL path")
    parser.add_argument("--num-negatives", type=int, default=7)
    parser.add_argument("--hard-negative-ratio", type=float, default=0.5)
    parser.add_argument("--max-seq-length", type=int, default=2048)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    random.seed(args.seed)
    np.random.seed(args.seed)

    # Load extractions
    dataflow_path = os.path.join(args.dataflow_dir, "all.jsonl")
    extractions = []
    with open(dataflow_path) as f:
        for line in f:
            line = line.strip()
            if line:
                extractions.append(json.loads(line))
    log.info("Loaded %d extractions", len(extractions))

    # Group by repo for BM25 index sharing
    by_repo: dict[str, list[dict]] = defaultdict(list)
    for ext in extractions:
        by_repo[ext["repo_path"]].append(ext)

    training_instances = []

    for repo_path, repo_extractions in by_repo.items():
        log.info("Building training data for %s (%d instances)", repo_path, len(repo_extractions))

        all_files = collect_repo_files(repo_path)
        if not all_files:
            log.warning("No .py files in %s, skipping", repo_path)
            continue

        # Cache file contents
        file_contents: dict[str, str] = {}
        for fp in all_files:
            content = read_file_content(repo_path, fp)
            if content:
                file_contents[fp] = content

        # Build BM25 index over repo files
        doc_list = [file_contents.get(f, "") for f in all_files]
        bm25_index = build_bm25_index(doc_list)

        for ext in repo_extractions:
            inst = build_instance(
                ext, args.repos_dir, bm25_index, all_files, file_contents,
                args.num_negatives, args.hard_negative_ratio, args.max_seq_length,
            )
            if inst:
                training_instances.append(inst)

    # Normalize features
    training_instances = normalize_features(training_instances)

    # Write output
    os.makedirs(os.path.dirname(os.path.abspath(args.output_file)), exist_ok=True)
    with open(args.output_file, "w") as f:
        for inst in training_instances:
            f.write(json.dumps(inst, ensure_ascii=False) + "\n")

    # Statistics
    total = len(training_instances)
    inter_proc = sum(1 for i in training_instances if i["metadata"]["inter_procedural"])
    avg_pos_files = np.mean([i["metadata"]["num_connected_files"] for i in training_instances]) if total else 0
    hard_neg_count = sum(
        sum(1 for s in i["metadata"]["neg_strategies"] if s == "bm25_hard")
        for i in training_instances
    )
    total_neg = sum(len(i["neg_codes"]) for i in training_instances)

    log.info("=" * 60)
    log.info("Training data built: %d instances", total)
    log.info("  Avg connected files/instance: %.1f", avg_pos_files)
    log.info("  Hard negative ratio:          %.2f", hard_neg_count / max(total_neg, 1))
    log.info("  Inter-procedural ratio:       %.2f", inter_proc / max(total, 1))
    log.info("  Output: %s", args.output_file)


if __name__ == "__main__":
    main()

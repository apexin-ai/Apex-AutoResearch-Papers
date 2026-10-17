#!/usr/bin/env python3
"""
Greedy Schema Label Optimizer

Iteratively renames schema type labels to minimize pairwise SCS (Schema
Confusability Score = embedding cosine similarity) while preserving semantics.

Input:  JSON file with a list of type label strings.
Output: optimization_report.json with rename map, SCS matrices, and statistics.

Dependencies: sentence-transformers, openai, numpy
"""

import argparse
import json
import logging
import os
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Embedding utilities
# ---------------------------------------------------------------------------

class EmbeddingEngine:
    """Wraps sentence-transformers for cosine-similarity computation."""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        from sentence_transformers import SentenceTransformer

        log.info("Loading embedding model: %s", model_name)
        self.model = SentenceTransformer(model_name)

    def encode(self, texts: List[str]) -> np.ndarray:
        return self.model.encode(texts, normalize_embeddings=True)

    def cosine_sim(self, a: np.ndarray, b: np.ndarray) -> float:
        return float(np.dot(a, b))


def compute_scs_matrix(
    labels: List[str], engine: EmbeddingEngine
) -> Tuple[np.ndarray, np.ndarray]:
    """Return (embeddings, scs_matrix) for the given labels."""
    embs = engine.encode(labels)
    scs = embs @ embs.T
    np.fill_diagonal(scs, 0.0)
    return embs, scs


def update_scs_for_index(
    idx: int,
    embeddings: np.ndarray,
    scs: np.ndarray,
) -> None:
    """Recompute SCS row/col for a single changed index in-place."""
    n = len(embeddings)
    for j in range(n):
        if j == idx:
            scs[idx, j] = 0.0
        else:
            s = float(np.dot(embeddings[idx], embeddings[j]))
            scs[idx, j] = s
            scs[j, idx] = s


# ---------------------------------------------------------------------------
# LLM candidate generation
# ---------------------------------------------------------------------------

CANDIDATE_PROMPT = """You are a schema design expert. Given a relation/entity type label used in information extraction, generate {n} alternative labels that:
1. Are semantically equivalent (same meaning)
2. Use different vocabulary/phrasing to maximize linguistic diversity
3. Are clear and easy for an LLM to understand
4. Avoid jargon or archaic terms

Original label: "{label}"
Context: This label is used in a relation extraction task. It needs to be distinguishable from: {confusable_types}

Return exactly {n} alternatives as a JSON array: ["alt1", "alt2", ...]"""


def generate_candidates(
    label: str,
    confusable_types: List[str],
    n: int,
    llm_client,
    llm_model: str,
    max_retries: int = 3,
) -> List[str]:
    """Ask LLM for n semantically equivalent rename candidates."""
    prompt = CANDIDATE_PROMPT.format(
        n=n, label=label, confusable_types=", ".join(confusable_types)
    )

    for attempt in range(max_retries):
        try:
            resp = llm_client.chat.completions.create(
                model=llm_model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.9,
                max_tokens=256,
            )
            text = resp.choices[0].message.content.strip()
            # Extract JSON array from response (handle markdown fences)
            if "```" in text:
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]
                text = text.strip()
            candidates = json.loads(text)
            if isinstance(candidates, list) and len(candidates) >= 1:
                return [str(c) for c in candidates[:n]]
        except (json.JSONDecodeError, KeyError, IndexError) as e:
            log.warning("Attempt %d: failed to parse LLM response: %s", attempt + 1, e)
        except Exception as e:
            log.warning("Attempt %d: LLM API error: %s", attempt + 1, e)
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)

    log.error("All %d attempts failed for label '%s'", max_retries, label)
    return []


# ---------------------------------------------------------------------------
# Candidate evaluation
# ---------------------------------------------------------------------------

def evaluate_candidate(
    candidate: str,
    target_idx: int,
    paired_idx: int,
    labels: List[str],
    embeddings: np.ndarray,
    engine: EmbeddingEngine,
    threshold: float,
) -> Optional[Dict]:
    """
    Evaluate a single rename candidate.

    Returns dict with scores if the candidate is valid (reduces the
    problematic pair below threshold without introducing new violations),
    or None if invalid.
    """
    cand_emb = engine.encode([candidate])[0]

    scs_with_paired = float(np.dot(cand_emb, embeddings[paired_idx]))

    if scs_with_paired >= threshold:
        return None

    max_scs = scs_with_paired
    for k in range(len(labels)):
        if k == target_idx:
            continue
        s = float(np.dot(cand_emb, embeddings[k]))
        if s > max_scs:
            max_scs = s
        if s >= threshold and k != paired_idx:
            # Would introduce a new above-threshold pair
            return None

    return {
        "candidate": candidate,
        "scs_with_paired": scs_with_paired,
        "max_scs": max_scs,
        "embedding": cand_emb,
    }


# ---------------------------------------------------------------------------
# Greedy optimization loop
# ---------------------------------------------------------------------------

def find_high_scs_pairs(
    scs: np.ndarray, threshold: float
) -> List[Tuple[int, int, float]]:
    """Return (i, j, scs_value) for all upper-triangle pairs above threshold, sorted desc."""
    n = scs.shape[0]
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            if scs[i, j] > threshold:
                pairs.append((i, j, float(scs[i, j])))
    pairs.sort(key=lambda x: x[2], reverse=True)
    return pairs


def count_high_scs_connections(idx: int, scs: np.ndarray, threshold: float) -> int:
    """Count how many other types have SCS > threshold with idx."""
    return int(np.sum(scs[idx] > threshold))


def greedy_optimize(
    labels: List[str],
    engine: EmbeddingEngine,
    threshold: float,
    llm_client,
    llm_model: str,
    max_candidates: int,
    dry_run: bool = False,
) -> Dict:
    """
    Main optimization loop. Greedily renames types starting from the
    highest-SCS pair to reduce all pairwise SCS below threshold.
    """
    current_labels = list(labels)
    embeddings, scs = compute_scs_matrix(current_labels, engine)

    scs_before = scs.copy()
    mean_scs_before = float(scs[np.triu_indices_from(scs, k=1)].mean())
    max_scs_before = float(scs.max())
    initial_pairs = find_high_scs_pairs(scs, threshold)
    n_above_before = len(initial_pairs)

    log.info(
        "Initial: %d pairs above threshold %.2f (max SCS=%.4f, mean SCS=%.4f)",
        n_above_before, threshold, max_scs_before, mean_scs_before,
    )

    if dry_run:
        log.info("=== DRY RUN: listing high-SCS pairs only ===")
        for i, j, s in initial_pairs:
            log.info("  SCS=%.4f  '%s' <-> '%s'", s, current_labels[i], current_labels[j])
        return _build_report(
            labels, current_labels, {}, threshold,
            n_above_before, n_above_before,
            [], initial_pairs,
            mean_scs_before, mean_scs_before,
            max_scs_before, max_scs_before,
        )

    rename_map: Dict[str, str] = {}
    pairs_fixed = []
    pairs_skipped = []

    iteration = 0
    while True:
        high_pairs = find_high_scs_pairs(scs, threshold)
        if not high_pairs:
            log.info("No more pairs above threshold. Done.")
            break

        i, j, pair_scs = high_pairs[0]
        iteration += 1
        log.info(
            "Iter %d: SCS=%.4f  '%s' <-> '%s'",
            iteration, pair_scs, current_labels[i], current_labels[j],
        )

        # Rename the type with more high-SCS connections
        conn_i = count_high_scs_connections(i, scs, threshold)
        conn_j = count_high_scs_connections(j, scs, threshold)
        if conn_i >= conn_j:
            target_idx, paired_idx = i, j
        else:
            target_idx, paired_idx = j, i

        target_label = current_labels[target_idx]
        paired_label = current_labels[paired_idx]

        confusable = [
            current_labels[k]
            for k in range(len(current_labels))
            if k != target_idx and scs[target_idx, k] > threshold * 0.8
        ]

        log.info(
            "  Renaming '%s' (connections=%d) away from '%s'",
            target_label, max(conn_i, conn_j), paired_label,
        )

        candidates = generate_candidates(
            target_label, confusable, max_candidates, llm_client, llm_model
        )

        if not candidates:
            log.warning("  No candidates generated, skipping pair")
            pairs_skipped.append({
                "type_a": current_labels[i],
                "type_b": current_labels[j],
                "scs": pair_scs,
                "reason": "LLM candidate generation failed",
            })
            # Mark as processed to avoid infinite loop
            scs[i, j] = 0.0
            scs[j, i] = 0.0
            continue

        best = None
        for cand in candidates:
            result = evaluate_candidate(
                cand, target_idx, paired_idx,
                current_labels, embeddings, engine, threshold,
            )
            if result is not None:
                if best is None or result["max_scs"] < best["max_scs"]:
                    best = result
            log.info(
                "    Candidate '%s': %s",
                cand,
                f"max_scs={result['max_scs']:.4f}" if result else "REJECTED",
            )

        if best is None:
            log.warning("  No valid candidate found, skipping pair")
            pairs_skipped.append({
                "type_a": current_labels[i],
                "type_b": current_labels[j],
                "scs": pair_scs,
                "reason": "no candidate reduced SCS below threshold without new violations",
            })
            scs[i, j] = 0.0
            scs[j, i] = 0.0
            continue

        old_name = current_labels[target_idx]
        new_name = best["candidate"]
        scs_after_pair = best["scs_with_paired"]

        current_labels[target_idx] = new_name
        embeddings[target_idx] = best["embedding"]
        update_scs_for_index(target_idx, embeddings, scs)

        original_name = old_name
        for orig, renamed in rename_map.items():
            if renamed == old_name:
                original_name = orig
                break
        rename_map[original_name] = new_name

        pairs_fixed.append({
            "type_a": current_labels[i] if target_idx != i else new_name,
            "type_b": current_labels[j] if target_idx != j else new_name,
            "scs_before": round(pair_scs, 4),
            "scs_after": round(scs_after_pair, 4),
            "renamed": old_name,
            "new_name": new_name,
        })

        log.info(
            "  Accepted: '%s' -> '%s' (SCS: %.4f -> %.4f)",
            old_name, new_name, pair_scs, scs_after_pair,
        )

    # Final stats
    upper = scs[np.triu_indices_from(scs, k=1)]
    mean_scs_after = float(upper.mean())
    max_scs_after = float(scs.max())
    n_above_after = len(find_high_scs_pairs(scs, threshold))

    return _build_report(
        labels, current_labels, rename_map, threshold,
        n_above_before, n_above_after,
        pairs_fixed, pairs_skipped,
        mean_scs_before, mean_scs_after,
        max_scs_before, max_scs_after,
    )


def _build_report(
    original_labels, current_labels, rename_map, threshold,
    n_before, n_after, pairs_fixed, pairs_skipped,
    mean_before, mean_after, max_before, max_after,
) -> Dict:
    return {
        "original_labels": original_labels,
        "optimized_labels": rename_map,
        "final_labels": current_labels,
        "threshold": threshold,
        "pairs_above_threshold_before": n_before,
        "pairs_above_threshold_after": n_after,
        "pairs_fixed": pairs_fixed,
        "pairs_skipped": [
            {k: (round(v, 4) if isinstance(v, float) else v) for k, v in p.items()}
            for p in pairs_skipped
        ],
        "mean_scs_before": round(mean_before, 4),
        "mean_scs_after": round(mean_after, 4),
        "max_scs_before": round(max_before, 4),
        "max_scs_after": round(max_after, 4),
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Greedy Schema Label Optimizer: minimize pairwise SCS via renaming"
    )
    parser.add_argument("--schema_file", required=True, help="JSON file with list of type labels")
    parser.add_argument("--threshold", type=float, default=0.75, help="SCS threshold (default: 0.75)")
    parser.add_argument("--embedding_model", default="all-MiniLM-L6-v2", help="Sentence-transformers model")
    parser.add_argument("--llm_model", default="gemini-2.5-flash", help="LLM model name for candidate generation")
    parser.add_argument("--base_url", default="http://localhost:8001/v1", help="OpenAI-compatible API base URL")
    parser.add_argument("--api_key", default="", help="API key for LLM")
    parser.add_argument("--max_candidates", type=int, default=5, help="Number of rename candidates per type")
    parser.add_argument("--output_dir", default="./artifacts/schema_optimizer_output/", help="Output directory")
    parser.add_argument("--dry_run", action="store_true", help="Only compute SCS and list high pairs, no LLM calls")
    args = parser.parse_args()

    with open(args.schema_file) as f:
        labels = json.load(f)
    assert isinstance(labels, list) and all(isinstance(l, str) for l in labels), \
        "schema_file must contain a JSON array of strings"

    log.info("Loaded %d type labels from %s", len(labels), args.schema_file)

    engine = EmbeddingEngine(args.embedding_model)

    llm_client = None
    if not args.dry_run:
        from openai import OpenAI
        llm_client = OpenAI(base_url=args.base_url, api_key=[REDACTED]

    report = greedy_optimize(
        labels=labels,
        engine=engine,
        threshold=args.threshold,
        llm_client=llm_client,
        llm_model=args.llm_model,
        max_candidates=args.max_candidates,
        dry_run=args.dry_run,
    )

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "optimization_report.json"
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    log.info("Report saved to %s", out_path)
    log.info(
        "Summary: %d -> %d pairs above threshold (fixed %d, skipped %d)",
        report["pairs_above_threshold_before"],
        report["pairs_above_threshold_after"],
        len(report["pairs_fixed"]),
        len(report["pairs_skipped"]),
    )


if __name__ == "__main__":
    main()

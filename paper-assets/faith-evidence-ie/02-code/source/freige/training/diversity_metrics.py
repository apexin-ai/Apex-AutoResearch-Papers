"""Diversity metrics for RSFT generation monitoring.

Computes unique triple-set diversity: for each document, how many of N
generated outputs produce a distinct set of (head, relation, tail) triples.
"""

from collections import defaultdict


def normalize_triple_key(triple: dict) -> tuple:
    """Normalize a triple dict to a comparable (head, relation, tail) tuple."""
    h = str(triple.get("head") or "").lower().strip()
    r = str(triple.get("relation") or "").lower().strip()
    t = str(triple.get("tail") or "").lower().strip()
    return (h, r, t)


def build_triple_set(parsed_triples: list[dict]) -> frozenset:
    """Build a frozenset of normalized (head, relation, tail) tuples."""
    return frozenset(normalize_triple_key(t) for t in parsed_triples)


def compute_doc_diversity(generations_parsed: list[list[dict]]) -> dict:
    """Compute triple-set diversity for one document's generations.

    Args:
        generations_parsed: list of parsed triple lists, one per generation.
            Each element is a list of dicts with head/relation/tail keys.

    Returns:
        dict with unique_count, total_count, diversity_ratio.
    """
    triple_sets = []
    for parsed_triples in generations_parsed:
        ts = build_triple_set(parsed_triples)
        triple_sets.append(ts)
    unique_count = len(set(triple_sets))
    total_count = len(triple_sets)
    return {
        "unique_count": unique_count,
        "total_count": total_count,
        "diversity_ratio": unique_count / total_count if total_count > 0 else 0.0,
    }


def compute_diversity_from_file(generations_path: str, parse_fn=None) -> dict:
    """Recompute diversity from a saved generations JSONL file.

    Args:
        generations_path: path to generations.jsonl
        parse_fn: optional parse function(raw_text) -> (list[dict], bool).
                  If None, reads pre-parsed triples from the record.

    Returns:
        dict with mean_diversity, median_diversity, per_doc details.
    """
    import json
    import statistics

    doc_gens = defaultdict(list)
    with open(generations_path) as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            doc_id = rec["doc_id"]
            if parse_fn is not None:
                parsed_triples, _ = parse_fn(rec["output"])
            else:
                parsed_triples = rec.get("parsed_triples") or []
            doc_gens[doc_id].append(parsed_triples)

    if not doc_gens:
        return {"mean_diversity": 0, "n_docs": 0}

    unique_counts = []
    for doc_id, gens in doc_gens.items():
        result = compute_doc_diversity(gens)
        unique_counts.append(result["unique_count"])

    n_gens = len(next(iter(doc_gens.values())))
    return {
        "mean_diversity": statistics.mean(unique_counts),
        "median_diversity": statistics.median(unique_counts),
        "min_diversity": min(unique_counts),
        "max_diversity": max(unique_counts),
        "n_docs": len(doc_gens),
        "n_generations": n_gens,
    }

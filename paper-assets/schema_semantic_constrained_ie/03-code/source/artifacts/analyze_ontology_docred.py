"""
Analyze DocRED training data to extract data-driven ontology constraints.

Input:  data/docred/train_annotated.json, data/docred/rel_info.json
Output: data/docred/ontology_constraints_docred.json

Reads all annotated training triples, records which (head_type, tail_type)
pairs actually appear for each relation type, and treats those as the
legitimate constraint set.
"""

import json
import argparse
from collections import defaultdict, Counter
from pathlib import Path


def load_data(train_path: str, rel_info_path: str):
    with open(train_path) as f:
        train = json.load(f)
    with open(rel_info_path) as f:
        rel_info = json.load(f)
    return train, rel_info


def get_entity_type(vertex_set_entry: list[dict]) -> str:
    """Get the canonical entity type for an entity (from its first mention)."""
    type_counts = Counter(m.get("type", "UNK") for m in vertex_set_entry)
    return type_counts.most_common(1)[0][0]


def analyze_constraints(train: list[dict], rel_info: dict) -> dict:
    # Per-relation: collect (head_type, tail_type) occurrences
    relation_pairs = defaultdict(lambda: Counter())
    total_triples = 0
    entity_types_seen = set()

    for doc in train:
        vertex_set = doc["vertexSet"]
        entity_type_map = {i: get_entity_type(vs) for i, vs in enumerate(vertex_set)}

        for etype in entity_type_map.values():
            entity_types_seen.add(etype)

        for label in doc.get("labels", []):
            h_type = entity_type_map[label["h"]]
            t_type = entity_type_map[label["t"]]
            relation_pairs[label["r"]][(h_type, t_type)] += 1
            total_triples += 1

    # Build output
    relation_constraints = {}
    valid_pair_counts = []

    for rel_id, pair_counter in sorted(relation_pairs.items()):
        rel_name = rel_info.get(rel_id, rel_id)
        valid_pairs = sorted(set(pair_counter.keys()))
        pair_dist = {f"{h}->{t}": c for (h, t), c in pair_counter.most_common()}
        relation_constraints[rel_id] = {
            "name": rel_name,
            "valid_pairs": [list(p) for p in valid_pairs],
            "stats": {
                "total": sum(pair_counter.values()),
                "pair_distribution": pair_dist,
            },
        }
        valid_pair_counts.append(len(valid_pairs))

    # Relations in rel_info but never seen in training data
    unseen = [r for r in rel_info if r not in relation_constraints]

    result = {
        "entity_types": sorted(entity_types_seen),
        "relation_types": rel_info,
        "relation_constraints": relation_constraints,
        "summary": {
            "total_triples": total_triples,
            "total_relation_types_in_data": len(relation_constraints),
            "total_relation_types_defined": len(rel_info),
            "unseen_relation_types": unseen,
            "avg_valid_pairs_per_relation": round(
                sum(valid_pair_counts) / len(valid_pair_counts), 2
            )
            if valid_pair_counts
            else 0,
            "max_valid_pairs": max(valid_pair_counts) if valid_pair_counts else 0,
            "min_valid_pairs": min(valid_pair_counts) if valid_pair_counts else 0,
        },
    }
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--train_path",
        default="data/docred/train_annotated.json",
    )
    parser.add_argument(
        "--rel_info_path",
        default="data/docred/rel_info.json",
    )
    parser.add_argument(
        "--output_path",
        default="data/docred/ontology_constraints_docred.json",
    )
    args = parser.parse_args()

    train, rel_info = load_data(args.train_path, args.rel_info_path)
    print(f"Loaded {len(train)} training documents, {len(rel_info)} relation types")

    result = analyze_constraints(train, rel_info)

    Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output_path, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    s = result["summary"]
    print(f"Triples analyzed: {s['total_triples']}")
    print(f"Relation types with data: {s['total_relation_types_in_data']}/{s['total_relation_types_defined']}")
    print(f"Valid pairs per relation: avg={s['avg_valid_pairs_per_relation']}, "
          f"min={s['min_valid_pairs']}, max={s['max_valid_pairs']}")
    print(f"Entity types: {result['entity_types']}")
    if s["unseen_relation_types"]:
        print(f"Unseen relation types: {s['unseen_relation_types']}")
    print(f"Output: {args.output_path}")


if __name__ == "__main__":
    main()

"""
Check ontology constraint violations in DocRED extraction outputs.

Input:  outputs/raw_outputs_docred.jsonl, data/docred/ontology_constraints_docred.json
Output: outputs/violation_report_docred.json

Three violation types:
1. Entity type validity  – entity type not in {PER, ORG, LOC, TIME, NUM, MISC}
2. Relation domain/range – (head_type, tail_type) not in valid_pairs for that relation
3. Cross-field consistency – same entity mention assigned different types across relations
"""

import json
import argparse
from collections import defaultdict, Counter
from pathlib import Path


VALID_ENTITY_TYPES = {"PER", "ORG", "LOC", "TIME", "NUM", "MISC"}


def load_constraints(path: str) -> dict:
    with open(path) as f:
        return json.load(f)


def build_relation_name_to_id(rel_types: dict) -> dict:
    """Map relation name -> relation ID for matching model output."""
    name_to_id = {}
    for rid, rname in rel_types.items():
        name_to_id[rname.lower().strip()] = rid
        name_to_id[rid.lower()] = rid
    return name_to_id


def check_document(parsed: dict, constraints: dict, name_to_id: dict) -> dict:
    """Check violations for one document's parsed output.

    Returns dict with violation counts and details.
    """
    entities = parsed.get("entities", [])
    relations = parsed.get("relations", [])

    violations = {
        "entity_type": [],
        "relation_domain_range": [],
        "cross_field_consistency": [],
    }

    # 1. Entity type validity
    for ent in entities:
        etype = ent.get("type", "")
        if etype.upper() not in VALID_ENTITY_TYPES:
            violations["entity_type"].append({
                "entity": ent.get("text", "?"),
                "invalid_type": etype,
            })

    # Collect entity type assignments from relations for cross-field check
    entity_type_assignments = defaultdict(set)

    for rel in relations:
        head = rel.get("head", "")
        tail = rel.get("tail", "")
        h_type = rel.get("head_type", "")
        t_type = rel.get("tail_type", "")
        rel_type = rel.get("type", "")

        # Track type assignments
        if head and h_type:
            entity_type_assignments[head.lower()].add(h_type.upper())
        if tail and t_type:
            entity_type_assignments[tail.lower()].add(t_type.upper())

        # 1b. Entity type validity for relation-level types
        if h_type.upper() not in VALID_ENTITY_TYPES:
            violations["entity_type"].append({
                "entity": head,
                "invalid_type": h_type,
                "context": f"head of relation '{rel_type}'",
            })
        if t_type.upper() not in VALID_ENTITY_TYPES:
            violations["entity_type"].append({
                "entity": tail,
                "invalid_type": t_type,
                "context": f"tail of relation '{rel_type}'",
            })

        # 2. Relation domain/range
        rel_key = name_to_id.get(rel_type.lower().strip())
        if rel_key and rel_key in constraints.get("relation_constraints", {}):
            valid_pairs = constraints["relation_constraints"][rel_key]["valid_pairs"]
            pair = [h_type.upper(), t_type.upper()]
            if pair not in valid_pairs:
                violations["relation_domain_range"].append({
                    "head": head,
                    "tail": tail,
                    "relation": rel_type,
                    "relation_id": rel_key,
                    "head_type": h_type,
                    "tail_type": t_type,
                    "valid_pairs": valid_pairs,
                })
        elif rel_key is None:
            # Unknown relation type – counts as domain/range violation
            violations["relation_domain_range"].append({
                "head": head,
                "tail": tail,
                "relation": rel_type,
                "relation_id": None,
                "head_type": h_type,
                "tail_type": t_type,
                "reason": "unknown_relation_type",
            })

    # 3. Cross-field consistency
    for entity_name, types in entity_type_assignments.items():
        if len(types) > 1:
            violations["cross_field_consistency"].append({
                "entity": entity_name,
                "assigned_types": sorted(types),
            })

    return violations


def compute_per_triple_violation(relations: list, violations: dict) -> dict:
    """Compute per-triple violation rate."""
    n_triples = len(relations)
    if n_triples == 0:
        return {"total_triples": 0, "violated_triples": 0, "rate": 0.0}

    # A triple is violated if it has entity type or domain/range violation
    violated_indices = set()

    # Entity type violations in relation context
    for v in violations["entity_type"]:
        if "context" in v:
            # Find the triple index - mark all triples as we check per-triple
            for i, rel in enumerate(relations):
                h = rel.get("head", "")
                t = rel.get("tail", "")
                if v["entity"] in (h, t):
                    violated_indices.add(i)

    # Domain/range violations
    for v in violations["relation_domain_range"]:
        for i, rel in enumerate(relations):
            if (rel.get("head", "") == v["head"]
                    and rel.get("tail", "") == v["tail"]
                    and rel.get("type", "") == v["relation"]):
                violated_indices.add(i)

    return {
        "total_triples": n_triples,
        "violated_triples": len(violated_indices),
        "rate": round(len(violated_indices) / n_triples, 4),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", default="outputs/raw_outputs_docred.jsonl")
    parser.add_argument("--constraints_path",
                        default="data/docred/ontology_constraints_docred.json")
    parser.add_argument("--output_path", default="outputs/violation_report_docred.json")
    args = parser.parse_args()

    constraints = load_constraints(args.constraints_path)
    name_to_id = build_relation_name_to_id(constraints.get("relation_types", {}))

    # Process each document
    doc_results = []
    total_triples = 0
    total_violated = 0
    total_entity_type_violations = 0
    total_domain_range_violations = 0
    total_cross_field_violations = 0
    parse_failures = 0
    per_relation_violations = Counter()
    per_relation_totals = Counter()

    with open(args.input_path) as f:
        for line in f:
            record = json.loads(line)
            parsed = record.get("parsed_output")
            doc_id = record.get("doc_id", "?")

            if parsed is None:
                parse_failures += 1
                doc_results.append({
                    "doc_id": doc_id,
                    "status": "parse_failure",
                })
                continue

            violations = check_document(parsed, constraints, name_to_id)
            relations = parsed.get("relations", [])
            triple_stats = compute_per_triple_violation(relations, violations)

            total_triples += triple_stats["total_triples"]
            total_violated += triple_stats["violated_triples"]
            total_entity_type_violations += len(violations["entity_type"])
            total_domain_range_violations += len(violations["relation_domain_range"])
            total_cross_field_violations += len(violations["cross_field_consistency"])

            # Per-relation tracking
            for v in violations["relation_domain_range"]:
                rid = v.get("relation_id") or v.get("relation", "unknown")
                per_relation_violations[rid] += 1
            for rel in relations:
                rel_type = rel.get("type", "")
                rid = name_to_id.get(rel_type.lower().strip(), rel_type)
                per_relation_totals[rid] += 1

            doc_results.append({
                "doc_id": doc_id,
                "status": "checked",
                "n_triples": triple_stats["total_triples"],
                "n_violated": triple_stats["violated_triples"],
                "violation_rate": triple_stats["rate"],
                "entity_type_violations": len(violations["entity_type"]),
                "domain_range_violations": len(violations["relation_domain_range"]),
                "cross_field_violations": len(violations["cross_field_consistency"]),
                "violation_details": violations,
            })

    # Per-relation breakdown
    per_relation_breakdown = {}
    all_rels = set(per_relation_totals.keys()) | set(per_relation_violations.keys())
    for rid in sorted(all_rels):
        t = per_relation_totals[rid]
        v = per_relation_violations[rid]
        per_relation_breakdown[rid] = {
            "total": t,
            "violations": v,
            "rate": round(v / t, 4) if t > 0 else 0.0,
        }

    n_docs = len(doc_results)
    docs_with_violations = sum(
        1 for d in doc_results if d.get("n_violated", 0) > 0
    )

    report = {
        "summary": {
            "total_documents": n_docs,
            "parse_failures": parse_failures,
            "documents_checked": n_docs - parse_failures,
            "documents_with_violations": docs_with_violations,
            "per_document_violation_rate": round(
                docs_with_violations / (n_docs - parse_failures), 4
            ) if (n_docs - parse_failures) > 0 else 0.0,
            "total_triples": total_triples,
            "violated_triples": total_violated,
            "per_triple_violation_rate": round(
                total_violated / total_triples, 4
            ) if total_triples > 0 else 0.0,
            "entity_type_violations": total_entity_type_violations,
            "domain_range_violations": total_domain_range_violations,
            "cross_field_violations": total_cross_field_violations,
        },
        "per_relation_breakdown": per_relation_breakdown,
        "per_document_details": doc_results,
    }

    Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output_path, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    s = report["summary"]
    print(f"Documents: {s['documents_checked']} checked, {s['parse_failures']} parse failures")
    print(f"Triples: {s['total_triples']} total, {s['violated_triples']} violated")
    print(f"Per-triple violation rate: {s['per_triple_violation_rate']:.2%}")
    print(f"Per-document violation rate: {s['per_document_violation_rate']:.2%}")
    print(f"  Entity type violations: {s['entity_type_violations']}")
    print(f"  Domain/range violations: {s['domain_range_violations']}")
    print(f"  Cross-field violations: {s['cross_field_violations']}")
    print(f"Output: {args.output_path}")


if __name__ == "__main__":
    main()

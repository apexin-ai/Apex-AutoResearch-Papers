"""Check ontology constraint violations in DocRED extraction outputs.

Violation types (mutually exclusive per triple):
1. entity_type_violations      - entity type not in {PER, ORG, LOC, TIME, NUM, MISC}
2. relation_vocabulary_violations - relation name not in ontology (solvable by grammar-constrained decoding)
3. domain_range_violations     - relation name valid but (head_type, tail_type) violates constraints (OntoCoDec core target)
4. cross_field_consistency_violations - same entity mention has inconsistent types across relations
"""

import json
import argparse
from collections import defaultdict, Counter
from pathlib import Path


VALID_ENTITY_TYPES = {"PER", "ORG", "LOC", "TIME", "NUM", "MISC"}


def _levenshtein(s1, s2):
    if len(s1) < len(s2):
        return _levenshtein(s2, s1)
    if len(s2) == 0:
        return len(s1)
    prev_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        curr_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = prev_row[j + 1] + 1
            deletions = curr_row[j] + 1
            substitutions = prev_row[j] + (c1 != c2)
            curr_row.append(min(insertions, deletions, substitutions))
        prev_row = curr_row
    return prev_row[-1]


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


def normalize_relation(rel_name, rel_types, name_to_id):
    """Fuzzy-match a model-output relation name to the nearest ontology relation.

    Match conditions (any one suffices):
    1. Exact match via name_to_id (case-insensitive)
    2. Token overlap > 80%
    3. Levenshtein distance <= 2 on the relation name

    Returns: (matched_pid, matched_name, is_fuzzy_match) or (None, None, False)
    """
    rel_key = name_to_id.get(rel_name.lower().strip())
    if rel_key:
        return rel_key, rel_types.get(rel_key, rel_name), False

    rel_tokens = set(rel_name.strip().lower().split())
    best_pid, best_name = None, None
    best_overlap = 0.0
    for rid, rname in rel_types.items():
        rname_tokens = set(rname.lower().split())
        if rel_tokens and rname_tokens:
            overlap = len(rel_tokens & rname_tokens)
            union = len(rel_tokens | rname_tokens)
            ratio = overlap / union
            if ratio > 0.8 and ratio > best_overlap:
                best_overlap = ratio
                best_pid, best_name = rid, rname
    if best_pid:
        return best_pid, best_name, True

    for rid, rname in rel_types.items():
        if _levenshtein(rel_name.strip().lower(), rname.lower()) <= 2:
            return rid, rname, True

    return None, None, False


def check_document(parsed, constraints, rel_types, name_to_id):
    """Check violations for one document's parsed output.

    Returns dict with 4 violation lists + fuzzy_match_count.
    """
    entities = parsed.get("entities", [])
    relations = parsed.get("relations", [])

    violations = {
        "entity_type": [],
        "relation_vocabulary": [],
        "domain_range": [],
        "cross_field_consistency": [],
    }
    fuzzy_matches = 0

    for ent in entities:
        etype = ent.get("type", "")
        if etype.upper() not in VALID_ENTITY_TYPES:
            violations["entity_type"].append({
                "entity": ent.get("text", "?"),
                "invalid_type": etype,
            })

    entity_type_assignments = defaultdict(set)

    for rel in relations:
        head = rel.get("head", "")
        tail = rel.get("tail", "")
        h_type = rel.get("head_type", "")
        t_type = rel.get("tail_type", "")
        rel_type = rel.get("type", "")

        if head and h_type:
            entity_type_assignments[head.lower()].add(h_type.upper())
        if tail and t_type:
            entity_type_assignments[tail.lower()].add(t_type.upper())

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

        matched_pid, matched_name, is_fuzzy = normalize_relation(rel_type, rel_types, name_to_id)

        if matched_pid is None:
            violations["relation_vocabulary"].append({
                "head": head,
                "tail": tail,
                "relation": rel_type,
                "reason": "unknown_relation_type",
            })
            continue

        if is_fuzzy:
            fuzzy_matches += 1

        if matched_pid in constraints.get("relation_constraints", {}):
            valid_pairs = constraints["relation_constraints"][matched_pid]["valid_pairs"]
            pair = [h_type.upper(), t_type.upper()]
            if pair not in valid_pairs:
                violations["domain_range"].append({
                    "head": head,
                    "tail": tail,
                    "relation": rel_type,
                    "relation_id": matched_pid,
                    "matched_name": matched_name,
                    "head_type": h_type,
                    "tail_type": t_type,
                })

    for entity_name, types in entity_type_assignments.items():
        if len(types) > 1:
            violations["cross_field_consistency"].append({
                "entity": entity_name,
                "conflicting_types": sorted(types),
            })

    return violations, fuzzy_matches


def main():
    parser = argparse.ArgumentParser(description="Check ontology constraint violations (DocRED)")
    parser.add_argument("--input_path", type=str, default="outputs/raw_outputs_docred.jsonl")
    parser.add_argument("--constraints_path", type=str, default="data/docred/ontology_constraints_docred.json")
    parser.add_argument("--output_path", type=str, default="outputs/violation_report_docred.json")
    args = parser.parse_args()

    constraints = load_constraints(args.constraints_path)
    rel_types = constraints.get("relation_types", {})
    name_to_id = build_relation_name_to_id(rel_types)

    records = []
    with open(args.input_path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))

    parse_failures = 0
    total_triples = 0
    total_entities = 0
    total_entity_type_violations = 0
    total_relation_vocab_violations = 0
    total_domain_range_violations = 0
    total_cross_field_violations = 0
    total_fuzzy_matches = 0

    per_relation_totals = defaultdict(int)
    per_relation_dr_violations = defaultdict(int)
    per_relation_vocab_violations = defaultdict(int)

    doc_results = []

    for rec in records:
        doc_id = rec.get("doc_id", "unknown")
        parsed = rec.get("parsed_output")
        if parsed is None:
            parse_failures += 1
            doc_results.append({"doc_id": doc_id, "status": "parse_failure"})
            continue

        violations, fuzzy_matches = check_document(parsed, constraints, rel_types, name_to_id)
        relations = parsed.get("relations", [])
        entities = parsed.get("entities", [])

        n_triples = len(relations)
        n_entities = len(entities)
        total_triples += n_triples
        total_entities += n_entities
        total_fuzzy_matches += fuzzy_matches

        n_entity_type = len(violations["entity_type"])
        n_relation_vocab = len(violations["relation_vocabulary"])
        n_domain_range = len(violations["domain_range"])
        n_cross_field = len(violations["cross_field_consistency"])

        total_entity_type_violations += n_entity_type
        total_relation_vocab_violations += n_relation_vocab
        total_domain_range_violations += n_domain_range
        total_cross_field_violations += n_cross_field

        for v in violations["relation_vocabulary"]:
            per_relation_vocab_violations[v.get("relation", "unknown")] += 1
        for v in violations["domain_range"]:
            rid = v.get("relation_id", v.get("relation", "unknown"))
            per_relation_dr_violations[rid] += 1
        for rel in relations:
            rel_type = rel.get("type", "")
            matched_pid, _, _ = normalize_relation(rel_type, rel_types, name_to_id)
            rid = matched_pid if matched_pid else rel_type
            per_relation_totals[rid] += 1

        doc_results.append({
            "doc_id": doc_id,
            "status": "checked",
            "n_triples": n_triples,
            "entity_type_violations": n_entity_type,
            "relation_vocabulary_violations": n_relation_vocab,
            "domain_range_violations": n_domain_range,
            "cross_field_violations": n_cross_field,
        })

    n_docs = len(doc_results)
    docs_checked = n_docs - parse_failures

    per_relation_breakdown = {}
    all_rels = set(per_relation_totals.keys()) | set(per_relation_dr_violations.keys())
    for rid in sorted(all_rels):
        t = per_relation_totals.get(rid, 0)
        dr = per_relation_dr_violations.get(rid, 0)
        per_relation_breakdown[rid] = {
            "total": t,
            "domain_range_violations": dr,
            "violation_rate": round(dr / t, 4) if t > 0 else 0.0,
        }

    total_violations = (total_entity_type_violations + total_relation_vocab_violations
                        + total_domain_range_violations + total_cross_field_violations)

    entity_type_examples = []
    relation_vocab_examples = []
    domain_range_examples = []
    cross_field_examples = []
    for d in doc_results:
        if d.get("status") != "checked":
            continue

    all_examples = {"entity_type_violations": [], "relation_vocabulary_violations": [],
                    "domain_range_violations": [], "cross_field_consistency_violations": []}
    for rec in records:
        parsed = rec.get("parsed_output")
        if parsed is None:
            continue
        violations, _ = check_document(parsed, constraints, rel_types, name_to_id)
        doc_id = rec.get("doc_id", "unknown")
        for v in violations["entity_type"]:
            if len(all_examples["entity_type_violations"]) < 3:
                all_examples["entity_type_violations"].append({"doc_id": doc_id, **v})
        for v in violations["relation_vocabulary"]:
            if len(all_examples["relation_vocabulary_violations"]) < 3:
                all_examples["relation_vocabulary_violations"].append({"doc_id": doc_id, **v})
        for v in violations["domain_range"]:
            if len(all_examples["domain_range_violations"]) < 3:
                all_examples["domain_range_violations"].append({"doc_id": doc_id, **v})
        for v in violations["cross_field_consistency"]:
            if len(all_examples["cross_field_consistency_violations"]) < 3:
                all_examples["cross_field_consistency_violations"].append({"doc_id": doc_id, **v})

    report = {
        "summary": {
            "total_documents": n_docs,
            "documents_checked": docs_checked,
            "parse_failures": parse_failures,
            "json_parse_rate": round(docs_checked / n_docs, 4) if n_docs else 0,
            "total_triples_extracted": total_triples,
            "total_entities_extracted": total_entities,

            "entity_type_violations": total_entity_type_violations,
            "entity_type_violation_rate": round(total_entity_type_violations / total_entities, 4) if total_entities else 0,

            "relation_vocabulary_violations": total_relation_vocab_violations,
            "relation_vocabulary_violation_rate": round(total_relation_vocab_violations / total_triples, 4) if total_triples else 0,
            "relation_fuzzy_matches": total_fuzzy_matches,

            "domain_range_violations": total_domain_range_violations,
            "domain_range_violation_rate": round(total_domain_range_violations / total_triples, 4) if total_triples else 0,

            "cross_field_consistency_violations": total_cross_field_violations,
            "cross_field_consistency_violation_rate": round(total_cross_field_violations / total_entities, 4) if total_entities else 0,

            "total_violations_any": total_violations,
            "total_violation_rate": round(total_violations / max(total_entities + total_triples, 1), 4),

            "go_nogo_metric": round(total_domain_range_violations / total_triples, 4) if total_triples else 0,
            "go_nogo_metric_description": "per-triple domain_range_violation_rate (excludes relation_vocabulary_violations)",
        },
        "per_relation_type": per_relation_breakdown,
        "examples": all_examples,
        "per_document_details": doc_results,
    }

    Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output_path, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    s = report["summary"]
    print("=== Violation Report (DocRED) ===")
    print(f"Documents: {docs_checked} checked, {parse_failures} parse failures")
    print(f"Entities: {total_entities}, Triples: {total_triples}")
    print(f"\nEntity type violations: {total_entity_type_violations} ({100*s['entity_type_violation_rate']:.1f}%)")
    print(f"Relation vocab violations: {total_relation_vocab_violations}/{total_triples} ({100*s['relation_vocabulary_violation_rate']:.1f}%)")
    print(f"Domain/range violations: {total_domain_range_violations}/{total_triples} ({100*s['domain_range_violation_rate']:.1f}%)")
    print(f"Cross-field consistency violations: {total_cross_field_violations}")
    print(f"Fuzzy relation matches: {total_fuzzy_matches}")
    print(f"\nGo/No-go metric (D/R violation rate): {s['go_nogo_metric']:.4f}")
    print(f"Output: {args.output_path}")


if __name__ == "__main__":
    main()

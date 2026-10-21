"""Check ontology constraint violations in SciERC extraction outputs.

Violation types (mutually exclusive per triple):
1. entity_type_violations      - entity type not in ontology's valid type list
2. relation_vocabulary_violations - relation name not in ontology (solvable by grammar-constrained decoding)
3. domain_range_violations     - relation name valid but (head_type, tail_type) violates constraints (OntoCoDec core target)
4. cross_field_consistency_violations - same entity mention has inconsistent types across relations
"""
import argparse
import json
from collections import defaultdict
from pathlib import Path


def normalize_type(t, valid_types, type_map=None):
    """Case-insensitive type matching with common aliases."""
    if type_map is None:
        type_map = {
            "otherscientificterm": "OtherScientificTerm",
            "other-scientificterm": "OtherScientificTerm",
            "other_scientific_term": "OtherScientificTerm",
            "scientificterm": "OtherScientificTerm",
            "other": "OtherScientificTerm",
        }
    t_lower = t.strip().lower().replace(" ", "").replace("_", "").replace("-", "")
    for vt in valid_types:
        if t_lower == vt.lower().replace(" ", "").replace("_", "").replace("-", ""):
            return vt
    if t_lower in type_map:
        return type_map[t_lower]
    return None


def normalize_relation(rel_name, valid_relation_types):
    """Fuzzy-match a model-output relation name to the nearest ontology relation.

    Match conditions (any one suffices):
    1. Exact match (case-insensitive, ignoring spaces/hyphens/underscores)
    2. Token overlap > 80%
    3. Levenshtein distance <= 2

    Returns: (matched_name, is_fuzzy_match) or (None, False)
    """
    rel_norm = rel_name.strip().lower().replace(" ", "").replace("_", "").replace("-", "")
    for vrt in valid_relation_types:
        if rel_norm == vrt.lower().replace(" ", "").replace("_", "").replace("-", ""):
            return vrt, False

    rel_tokens = set(rel_name.strip().lower().replace("-", " ").replace("_", " ").split())
    for vrt in valid_relation_types:
        vrt_tokens = set(vrt.lower().replace("-", " ").replace("_", " ").split())
        if rel_tokens and vrt_tokens:
            overlap = len(rel_tokens & vrt_tokens)
            union = len(rel_tokens | vrt_tokens)
            if overlap / union > 0.8:
                return vrt, True

    for vrt in valid_relation_types:
        if _levenshtein(rel_name.strip().lower(), vrt.lower()) <= 2:
            return vrt, True

    return None, False


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


def compute_f1(gold_items, pred_items, key_fn):
    """Compute micro P/R/F1 between gold and predicted item sets."""
    gold_set = set(key_fn(g) for g in gold_items)
    pred_set = set(key_fn(p) for p in pred_items)
    tp = len(gold_set & pred_set)
    p = tp / len(pred_set) if pred_set else 0.0
    r = tp / len(gold_set) if gold_set else 0.0
    f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
    return {"precision": round(p, 4), "recall": round(r, 4), "f1": round(f1, 4),
            "tp": tp, "gold": len(gold_set), "pred": len(pred_set)}


def check_violations(input_path, constraints_path, output_path):
    with open(constraints_path) as f:
        constraints = json.load(f)

    valid_entity_types = constraints["entity_types"]
    rel_constraints = constraints["relation_constraints"]
    valid_relation_types = constraints["relation_types"]

    valid_pairs_map = {}
    for rtype, info in rel_constraints.items():
        valid_pairs_map[rtype] = set(tuple(p) for p in info["valid_pairs"])

    records = []
    with open(input_path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))

    total = len(records)
    json_fail = 0

    entity_type_violation_examples = []
    relation_vocab_violation_examples = []
    domain_range_violation_examples = []
    consistency_violation_examples = []

    entity_type_violation_count = 0
    relation_vocab_violation_count = 0
    domain_range_violation_count = 0
    consistency_violation_count = 0
    fuzzy_match_count = 0

    total_pred_entities = 0
    total_pred_relations = 0

    rel_type_stats = defaultdict(lambda: {"total": 0, "domain_range_violations": 0})
    invalid_type_counts = defaultdict(int)

    all_entity_f1 = {"tp": 0, "gold": 0, "pred": 0}
    all_rel_f1 = {"tp": 0, "gold": 0, "pred": 0}

    for rec in records:
        parsed = rec.get("parsed_output")
        if parsed is None:
            json_fail += 1
            continue

        entities = parsed.get("entities", [])
        relations = parsed.get("relations", [])
        total_pred_entities += len(entities)
        total_pred_relations += len(relations)

        mention_types = {}
        for ent in entities:
            etype = ent.get("type", "")
            normalized = normalize_type(etype, valid_entity_types)
            if normalized is None:
                entity_type_violation_count += 1
                invalid_type_counts[etype] += 1
                if len(entity_type_violation_examples) < 10:
                    entity_type_violation_examples.append({
                        "doc_id": rec["doc_id"],
                        "entity": ent.get("text", ""),
                        "invalid_type": etype,
                    })
            else:
                text_key = ent.get("text", "").lower().strip()
                mention_types.setdefault(text_key, set()).add(normalized)

        for rel in relations:
            rtype = rel.get("type", "")
            head_type = rel.get("head_type", "")
            tail_type = rel.get("tail_type", "")

            matched_rel, is_fuzzy = normalize_relation(rtype, valid_relation_types)

            if matched_rel is None:
                relation_vocab_violation_count += 1
                if len(relation_vocab_violation_examples) < 10:
                    relation_vocab_violation_examples.append({
                        "doc_id": rec["doc_id"],
                        "relation": rel,
                        "reason": f"unknown relation type: {rtype}",
                    })
                continue

            if is_fuzzy:
                fuzzy_match_count += 1

            head_norm = normalize_type(head_type, valid_entity_types)
            tail_norm = normalize_type(tail_type, valid_entity_types)
            rel_type_stats[matched_rel]["total"] += 1

            if head_norm is None or tail_norm is None:
                domain_range_violation_count += 1
                rel_type_stats[matched_rel]["domain_range_violations"] += 1
                if len(domain_range_violation_examples) < 10:
                    domain_range_violation_examples.append({
                        "doc_id": rec["doc_id"],
                        "relation": rel,
                        "matched_relation": matched_rel,
                        "reason": f"invalid entity types: head={head_type}, tail={tail_type}",
                    })
                continue

            pair = (head_norm, tail_norm)
            if pair not in valid_pairs_map.get(matched_rel, set()):
                domain_range_violation_count += 1
                rel_type_stats[matched_rel]["domain_range_violations"] += 1
                if len(domain_range_violation_examples) < 10:
                    domain_range_violation_examples.append({
                        "doc_id": rec["doc_id"],
                        "relation": rel,
                        "matched_relation": matched_rel,
                        "reason": f"({head_norm}, {tail_norm}) not in valid pairs for {matched_rel}",
                    })

            head_text = rel.get("head", "").lower().strip()
            tail_text = rel.get("tail", "").lower().strip()
            if head_norm:
                mention_types.setdefault(head_text, set()).add(head_norm)
            if tail_norm:
                mention_types.setdefault(tail_text, set()).add(tail_norm)

        for mention, types in mention_types.items():
            if len(types) > 1:
                consistency_violation_count += 1
                if len(consistency_violation_examples) < 10:
                    consistency_violation_examples.append({
                        "doc_id": rec["doc_id"],
                        "mention": mention,
                        "conflicting_types": sorted(types),
                    })

        # F1 computation
        gold_ents = rec.get("gold_entities", [])
        gold_rels = rec.get("gold_relations", [])

        def ent_key(e):
            return (e.get("text", "").lower().strip(), e.get("type", ""))

        def rel_key(r):
            return (r.get("head", "").lower().strip(), r.get("tail", "").lower().strip(), r.get("type", ""))

        norm_pred_ents = []
        for e in entities:
            nt = normalize_type(e.get("type", ""), valid_entity_types)
            if nt:
                norm_pred_ents.append({"text": e.get("text", ""), "type": nt})

        ef1 = compute_f1(gold_ents, norm_pred_ents, ent_key)
        all_entity_f1["tp"] += ef1["tp"]
        all_entity_f1["gold"] += ef1["gold"]
        all_entity_f1["pred"] += ef1["pred"]

        rf1 = compute_f1(gold_rels, relations, rel_key)
        all_rel_f1["tp"] += rf1["tp"]
        all_rel_f1["gold"] += rf1["gold"]
        all_rel_f1["pred"] += rf1["pred"]

    def aggregate_f1(stats):
        p = stats["tp"] / stats["pred"] if stats["pred"] else 0.0
        r = stats["tp"] / stats["gold"] if stats["gold"] else 0.0
        f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
        return {"precision": round(p, 4), "recall": round(r, 4), "f1": round(f1, 4), **stats}

    total_violations = (entity_type_violation_count + relation_vocab_violation_count
                        + domain_range_violation_count + consistency_violation_count)

    report = {
        "summary": {
            "total_samples": total,
            "total_triples_extracted": total_pred_relations,
            "total_entities_extracted": total_pred_entities,
            "json_parse_failures": json_fail,
            "json_parse_rate": round((total - json_fail) / total, 4) if total else 0,

            "entity_type_violations": entity_type_violation_count,
            "entity_type_violation_rate": round(entity_type_violation_count / total_pred_entities, 4) if total_pred_entities else 0,

            "relation_vocabulary_violations": relation_vocab_violation_count,
            "relation_vocabulary_violation_rate": round(relation_vocab_violation_count / total_pred_relations, 4) if total_pred_relations else 0,
            "relation_fuzzy_matches": fuzzy_match_count,

            "domain_range_violations": domain_range_violation_count,
            "domain_range_violation_rate": round(domain_range_violation_count / total_pred_relations, 4) if total_pred_relations else 0,

            "cross_field_consistency_violations": consistency_violation_count,
            "cross_field_consistency_violation_rate": round(consistency_violation_count / total_pred_entities, 4) if total_pred_entities else 0,

            "total_violations_any": total_violations,
            "total_violation_rate": round(total_violations / max(total_pred_entities + total_pred_relations, 1), 4),

            "go_nogo_metric": round(domain_range_violation_count / total_pred_relations, 4) if total_pred_relations else 0,
            "go_nogo_metric_description": "per-triple domain_range_violation_rate (excludes relation_vocabulary_violations)",
        },
        "per_relation_type": {
            k: {
                "total": v["total"],
                "domain_range_violations": v["domain_range_violations"],
                "violation_rate": round(v["domain_range_violations"] / v["total"], 4) if v["total"] else 0,
            }
            for k, v in sorted(rel_type_stats.items())
        },
        "examples": {
            "entity_type_violations": entity_type_violation_examples[:3],
            "relation_vocabulary_violations": relation_vocab_violation_examples[:3],
            "domain_range_violations": domain_range_violation_examples[:3],
            "cross_field_consistency_violations": consistency_violation_examples[:3],
        },
        "quality": {
            "entity_f1": aggregate_f1(all_entity_f1),
            "relation_f1": aggregate_f1(all_rel_f1),
        },
    }

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    s = report["summary"]
    print("=== Violation Report (SciERC) ===")
    if total:
        print(f"Samples: {total}, JSON failures: {json_fail} ({100*json_fail/total:.1f}%)")
    print(f"Entities: {total_pred_entities}, Relations: {total_pred_relations}")
    if total_pred_entities:
        print(f"\nEntity type violations: {entity_type_violation_count}/{total_pred_entities} ({100*s['entity_type_violation_rate']:.1f}%)")
    if total_pred_relations:
        print(f"Relation vocab violations: {relation_vocab_violation_count}/{total_pred_relations} ({100*s['relation_vocabulary_violation_rate']:.1f}%)")
        print(f"Domain/range violations: {domain_range_violation_count}/{total_pred_relations} ({100*s['domain_range_violation_rate']:.1f}%)")
    print(f"Cross-field consistency violations: {consistency_violation_count}")
    print(f"Fuzzy relation matches: {fuzzy_match_count}")
    print(f"\nGo/No-go metric (D/R violation rate): {s['go_nogo_metric']:.4f}")

    ef = aggregate_f1(all_entity_f1)
    rf = aggregate_f1(all_rel_f1)
    print(f"\nEntity F1: P={ef['precision']:.4f} R={ef['recall']:.4f} F1={ef['f1']:.4f}")
    print(f"Relation F1: P={rf['precision']:.4f} R={rf['recall']:.4f} F1={rf['f1']:.4f}")
    print(f"\nReport saved to {output_path}")

    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check ontology constraint violations (SciERC)")
    parser.add_argument("--input_path", type=str, default="outputs/raw_outputs.jsonl")
    parser.add_argument("--constraints_path", type=str, default="ontology_constraints.json")
    parser.add_argument("--output_path", type=str, default="outputs/violation_report.json")
    args = parser.parse_args()

    check_violations(args.input_path, args.constraints_path, args.output_path)

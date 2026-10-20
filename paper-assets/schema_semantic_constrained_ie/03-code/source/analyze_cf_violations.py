"""Cross-field consistency violation analysis for OntoCoDec Phase 2 experiments.

Two dimensions of CF violation:
1. Within-relations: same entity span in same role (head/tail) gets different types
   across different relation triples within one sample.
2. Entity-vs-relation (EVR): entity type from Pass 1 entity list disagrees with
   head_type/tail_type assigned in Pass 2 relations. This is the main driver of
   the 8.03% CF violation rate in full_s2.

Input: JSONL files from phase2 experiments + ontology constraints JSON
Output: JSON analysis report + terminal summary
"""

import json
import argparse
from collections import defaultdict, Counter
from pathlib import Path


def load_jsonl(path):
    samples = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                samples.append(json.loads(line))
    return samples


def find_cf_violations(sample):
    """Within-relations CF violations: same entity span, same role, different types."""
    relations = sample.get("parsed_output", {}).get("relations", [])
    if not relations:
        return []

    entity_role_types = defaultdict(list)
    for rel in relations:
        entity_role_types[(rel["head"], "head")].append({
            "type": rel["head_type"],
            "relation": rel["type"],
            "counterpart": rel["tail"],
        })
        entity_role_types[(rel["tail"], "tail")].append({
            "type": rel["tail_type"],
            "relation": rel["type"],
            "counterpart": rel["head"],
        })

    violations = []
    for (entity, role), entries in entity_role_types.items():
        types = set(e["type"] for e in entries)
        if len(types) > 1:
            violations.append({
                "entity": entity,
                "role": role,
                "types_assigned": sorted(types),
                "entries": entries,
                "doc_id": sample["doc_id"],
            })
    return violations


def find_entity_vs_relation_violations(sample):
    """Entity-list vs relation cross-field violations.

    Pass 1 assigns entity types in the entities list.
    Pass 2 independently assigns head_type/tail_type per relation.
    Check if they disagree for the same entity span.
    """
    parsed = sample.get("parsed_output", {})
    entities = parsed.get("entities", [])
    relations = parsed.get("relations", [])
    if not entities or not relations:
        return [], 0

    entity_type_map = {}
    for ent in entities:
        entity_type_map[ent["text"]] = ent["type"]

    violations = []
    checked = 0
    for rel in relations:
        for role, span_key, type_key in [("head", "head", "head_type"), ("tail", "tail", "tail_type")]:
            span = rel[span_key]
            rel_type = rel[type_key]
            if span in entity_type_map:
                checked += 1
                ent_type = entity_type_map[span]
                if ent_type != rel_type:
                    violations.append({
                        "entity": span,
                        "role": role,
                        "entity_list_type": ent_type,
                        "relation_assigned_type": rel_type,
                        "relation": rel["type"],
                        "doc_id": sample["doc_id"],
                    })
    return violations, checked


def analyze_file(path, label):
    """Run full CF violation analysis on one JSONL file."""
    samples = load_jsonl(path)

    all_violations = []
    all_evr_violations = []
    total_entity_mentions = 0
    total_relations = 0
    total_evr_checked = 0
    samples_with_violations = 0
    samples_with_evr_violations = 0

    for sample in samples:
        relations = sample.get("parsed_output", {}).get("relations", [])
        total_relations += len(relations)

        entity_role_set = set()
        for rel in relations:
            entity_role_set.add((rel["head"], "head"))
            entity_role_set.add((rel["tail"], "tail"))
        total_entity_mentions += len(entity_role_set)

        violations = find_cf_violations(sample)
        if violations:
            samples_with_violations += 1
        all_violations.extend(violations)

        evr_violations, evr_checked = find_entity_vs_relation_violations(sample)
        total_evr_checked += evr_checked
        if evr_violations:
            samples_with_evr_violations += 1
        all_evr_violations.extend(evr_violations)

    # --- Within-relations aggregate statistics ---

    conflict_type_counts = Counter()
    for v in all_violations:
        conflict_type_counts[len(v["types_assigned"])] += 1

    relation_violation_count = Counter()
    for v in all_violations:
        for e in v["entries"]:
            relation_violation_count[e["relation"]] += 1

    relation_pair_count = Counter()
    for v in all_violations:
        rels_with_types = [(e["relation"], e["type"]) for e in v["entries"]]
        seen_pairs = set()
        for i in range(len(rels_with_types)):
            for j in range(i + 1, len(rels_with_types)):
                r1, t1 = rels_with_types[i]
                r2, t2 = rels_with_types[j]
                if t1 != t2:
                    pair = tuple(sorted([r1, r2]))
                    seen_pairs.add(pair)
        for pair in seen_pairs:
            relation_pair_count[pair] += 1

    type_pair_count = Counter()
    for v in all_violations:
        types = sorted(v["types_assigned"])
        for i in range(len(types)):
            for j in range(i + 1, len(types)):
                type_pair_count[(types[i], types[j])] += 1

    pattern_count = Counter()
    for v in all_violations:
        rels_with_types = [(e["relation"], e["type"]) for e in v["entries"]]
        seen_patterns = set()
        for i in range(len(rels_with_types)):
            for j in range(i + 1, len(rels_with_types)):
                r1, t1 = rels_with_types[i]
                r2, t2 = rels_with_types[j]
                if t1 != t2:
                    pattern = tuple(sorted([(r1, t1), (r2, t2)]))
                    seen_patterns.add(pattern)
        for p in seen_patterns:
            pattern_count[p] += 1

    violation_entities = []
    for v in all_violations:
        violation_entities.append({
            "entity": v["entity"],
            "doc_id": v["doc_id"],
            "role": v["role"],
            "types_assigned": v["types_assigned"],
            "details": [
                {"relation": e["relation"], "type": e["type"], "counterpart": e["counterpart"]}
                for e in v["entries"]
            ],
        })

    # --- EVR aggregate statistics ---

    evr_type_drift = Counter()
    evr_relation_count = Counter()
    for v in all_evr_violations:
        pair = tuple(sorted([v["entity_list_type"], v["relation_assigned_type"]]))
        evr_type_drift[pair] += 1
        evr_relation_count[v["relation"]] += 1

    evr_entities_unique = set()
    for v in all_evr_violations:
        evr_entities_unique.add((v["doc_id"], v["entity"]))

    evr_examples = []
    for v in all_evr_violations[:30]:
        evr_examples.append({
            "entity": v["entity"],
            "doc_id": v["doc_id"],
            "role": v["role"],
            "entity_list_type": v["entity_list_type"],
            "relation_assigned_type": v["relation_assigned_type"],
            "relation": v["relation"],
        })

    violated_entity_mentions = len(all_violations)

    return {
        "label": label,
        "total_samples": len(samples),
        "total_relations": total_relations,
        "total_entity_role_mentions": total_entity_mentions,
        # Within-relations
        "samples_with_violations": samples_with_violations,
        "total_violations": violated_entity_mentions,
        "cf_violation_rate": round(violated_entity_mentions / max(total_entity_mentions, 1) * 100, 4),
        "conflict_type_counts": {str(k): v for k, v in sorted(conflict_type_counts.items())},
        "relation_violation_count": dict(relation_violation_count.most_common()),
        "relation_pair_count": {
            f"{p[0]}|{p[1]}": c for p, c in relation_pair_count.most_common()
        },
        "type_pair_count": {
            f"{p[0]}↔{p[1]}": c for p, c in type_pair_count.most_common()
        },
        "top_patterns": [
            {
                "pattern": f"({p[0][0]}, {p[0][1]}) ↔ ({p[1][0]}, {p[1][1]})",
                "count": c,
            }
            for p, c in pattern_count.most_common(20)
        ],
        "violation_entities": sorted(
            violation_entities, key=lambda x: len(x["types_assigned"]), reverse=True
        )[:30],
        # Entity-vs-relation
        "evr_total_checked": total_evr_checked,
        "evr_total_violations": len(all_evr_violations),
        "evr_unique_entities": len(evr_entities_unique),
        "evr_violation_rate": round(len(all_evr_violations) / max(total_evr_checked, 1) * 100, 4),
        "evr_samples_with_violations": samples_with_evr_violations,
        "evr_type_drift": {
            f"{p[0]}↔{p[1]}": c for p, c in evr_type_drift.most_common()
        },
        "evr_relation_count": dict(evr_relation_count.most_common()),
        "evr_examples": evr_examples,
    }


def print_summary(results):
    """Print human-readable summary to terminal."""
    print("=" * 80)
    print("CROSS-FIELD CONSISTENCY VIOLATION ANALYSIS")
    print("=" * 80)

    # Comparison table — within-relations
    print("\n=== Dimension 1: Within-Relations CF (same entity, same role, different types across relations) ===\n")
    print(f"{'Mode':<16} {'Samples':>8} {'Relations':>10} {'Entity-Role':>12} "
          f"{'Violations':>11} {'CF Rate':>8}")
    print("-" * 70)
    for r in results:
        print(f"{r['label']:<16} {r['total_samples']:>8} {r['total_relations']:>10} "
              f"{r['total_entity_role_mentions']:>12} {r['total_violations']:>11} "
              f"{r['cf_violation_rate']:>7.2f}%")

    # Comparison table — entity-vs-relation
    print("\n=== Dimension 2: Entity-list vs Relation (Pass1 entity type ≠ Pass2 head/tail type) ===\n")
    print(f"{'Mode':<16} {'Checked':>10} {'Violations':>11} {'Uniq Ents':>10} "
          f"{'EVR Rate':>9} {'Affected':>10}")
    print("-" * 70)
    for r in results:
        print(f"{r['label']:<16} {r['evr_total_checked']:>10} {r['evr_total_violations']:>11} "
              f"{r['evr_unique_entities']:>10} {r['evr_violation_rate']:>8.2f}% "
              f"{r['evr_samples_with_violations']:>5} samp")

    # Detailed S2 analysis
    s2 = next((r for r in results if "s2" in r["label"].lower()), None)
    if not s2:
        return

    print(f"\n{'='*80}")
    print(f"DETAILED ANALYSIS: {s2['label']}")
    print(f"{'='*80}")

    # --- Within-relations details ---
    print(f"\n--- Within-Relations CF ---")
    print(f"Samples with violations: {s2['samples_with_violations']}/{s2['total_samples']}")

    print("\nConflict degree distribution:")
    for k, v in sorted(s2["conflict_type_counts"].items()):
        print(f"  {k} types: {v} entity-roles")

    print("\nPer-relation involvement:")
    for rel, cnt in sorted(s2["relation_violation_count"].items(), key=lambda x: -x[1]):
        print(f"  {rel:<25} {cnt:>5}")

    print("\nTop-10 relation pairs causing conflicts:")
    for pair, cnt in list(s2["relation_pair_count"].items())[:10]:
        print(f"  {pair:<45} {cnt:>5}")

    print("\nTop-10 conflicting entity type pairs:")
    for pair, cnt in list(s2["type_pair_count"].items())[:10]:
        print(f"  {pair:<35} {cnt:>5}")

    print("\nTop-10 conflict patterns:")
    for p in s2["top_patterns"][:10]:
        print(f"  {p['pattern']:<65} {p['count']:>5}")

    # --- EVR details ---
    print(f"\n--- Entity-vs-Relation (EVR) CF ---")
    print(f"Samples with EVR violations: {s2['evr_samples_with_violations']}/{s2['total_samples']}")
    print(f"Violation mentions: {s2['evr_total_violations']}/{s2['evr_total_checked']} = {s2['evr_violation_rate']:.2f}%")
    print(f"Unique entities involved: {s2['evr_unique_entities']}")

    print("\nType drift patterns (entity_list_type ↔ relation_assigned_type):")
    for pair, cnt in list(s2["evr_type_drift"].items())[:15]:
        print(f"  {pair:<40} {cnt:>5}")

    print("\nPer-relation EVR violations:")
    for rel, cnt in sorted(s2["evr_relation_count"].items(), key=lambda x: -x[1]):
        print(f"  {rel:<25} {cnt:>5}")

    print("\nTop-10 EVR violation examples:")
    for i, v in enumerate(s2["evr_examples"][:10], 1):
        print(f"  [{i}] \"{v['entity']}\" (doc={v['doc_id']}, role={v['role']})")
        print(f"      entity_list: {v['entity_list_type']} → relation({v['relation']}): {v['relation_assigned_type']}")

    # --- Within-relations examples ---
    print("\nTop-10 within-relations violation examples:")
    for i, v in enumerate(s2["violation_entities"][:10], 1):
        print(f"\n  [{i}] \"{v['entity']}\" (doc={v['doc_id']}, role={v['role']})")
        print(f"      Types assigned: {v['types_assigned']}")
        for d in v["details"]:
            print(f"        in {d['relation']}: type={d['type']}, counterpart=\"{d['counterpart']}\"")


def main():
    parser = argparse.ArgumentParser(description="Analyze CF violations in Phase 2 outputs")
    parser.add_argument("--s1_path", required=True)
    parser.add_argument("--s2_path", required=True)
    parser.add_argument("--unconstrained_path", required=True)
    parser.add_argument("--constraints_path", required=True)
    parser.add_argument("--output_path", required=True)
    args = parser.parse_args()

    results = []
    for path, label in [
        (args.unconstrained_path, "unconstrained"),
        (args.s1_path, "full_s1"),
        (args.s2_path, "full_s2"),
    ]:
        print(f"Analyzing {label}...")
        results.append(analyze_file(path, label))

    print_summary(results)

    output = {
        "comparison": [
            {
                "mode": r["label"],
                "total_samples": r["total_samples"],
                "total_relations": r["total_relations"],
                "total_entity_role_mentions": r["total_entity_role_mentions"],
                "within_rel_violations": r["total_violations"],
                "within_rel_cf_rate_pct": r["cf_violation_rate"],
                "evr_checked": r["evr_total_checked"],
                "evr_violations": r["evr_total_violations"],
                "evr_unique_entities": r["evr_unique_entities"],
                "evr_rate_pct": r["evr_violation_rate"],
                "samples_with_within_rel_violations": r["samples_with_violations"],
                "samples_with_evr_violations": r["evr_samples_with_violations"],
            }
            for r in results
        ],
        "s2_detailed": {k: v for k, v in next((r for r in results if "s2" in r["label"].lower()), {}).items()},
        "s1_detailed": {k: v for k, v in next((r for r in results if "s1" in r["label"].lower()), {}).items()},
        "unconstrained_detailed": {k: v for k, v in next((r for r in results if "unconstrained" in r["label"].lower()), {}).items()},
    }

    Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nFull results saved to {args.output_path}")


if __name__ == "__main__":
    main()

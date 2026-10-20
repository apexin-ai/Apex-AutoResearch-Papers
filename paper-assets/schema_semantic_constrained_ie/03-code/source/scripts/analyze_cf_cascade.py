"""First-seen type locking cascade error analysis for SF4 Evidence.

Simulates OntoCoDec's entity registry: walks predicted entities then relations
in generation order, tracking the first-seen type for each entity span. When the
same span reappears with a different type, that is a CF violation. Each violation
is classified by comparing first-seen type and attempted type against gold annotations.

Supports both Qwen ZS and FT SciERC S1 prediction files.
"""
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

BASE = Path("/root/schema_semantic_constrained_ie")
VALID_ENTITY_TYPES = {"Task", "Method", "Material", "Metric", "OtherScientificTerm", "Generic"}

TYPE_ALIASES = {
    "otherscientificterm": "OtherScientificTerm",
    "other-scientificterm": "OtherScientificTerm",
    "other_scientific_term": "OtherScientificTerm",
    "scientificterm": "OtherScientificTerm",
    "other": "OtherScientificTerm",
}


def normalize_type(t):
    t_clean = t.strip().lower().replace(" ", "").replace("_", "").replace("-", "")
    for vt in VALID_ENTITY_TYPES:
        if t_clean == vt.lower().replace(" ", "").replace("_", "").replace("-", ""):
            return vt
    return TYPE_ALIASES.get(t_clean)


def normalize_key(text):
    return text.strip().lower()


def build_gold_type_map(gold_entities):
    """Map entity span -> set of gold types."""
    gmap = defaultdict(set)
    for ent in gold_entities:
        key = normalize_key(ent["text"])
        t = normalize_type(ent["type"])
        if t:
            gmap[key].add(t)
    return gmap


def analyze_document(doc):
    """Simulate first-seen entity registry and find CF violations."""
    parsed = doc.get("parsed_output") or {}
    entities = parsed.get("entities") or []
    relations = parsed.get("relations") or []
    gold_entities = doc.get("gold_entities", [])

    gold_map = build_gold_type_map(gold_entities)

    registry = {}  # span_key -> first-seen type
    violations = []
    all_mentions = defaultdict(list)  # span_key -> [(source, type)]

    # Phase 1: walk entity list
    for ent in entities:
        key = normalize_key(ent["text"])
        t = normalize_type(ent.get("type", ""))
        if t is None:
            continue
        all_mentions[key].append(("entity_list", t))
        if key not in registry:
            registry[key] = t
        elif registry[key] != t:
            violations.append({
                "span": ent["text"],
                "span_key": key,
                "doc_id": doc["doc_id"],
                "first_seen_type": registry[key],
                "attempted_type": t,
                "source": "entity_list_duplicate",
                "gold_types": sorted(gold_map.get(key, set())),
            })

    # Phase 2: walk relations
    for rel in relations:
        for role in ["head", "tail"]:
            text = rel.get(role, "")
            t_raw = rel.get(f"{role}_type", "")
            key = normalize_key(text)
            t = normalize_type(t_raw)
            if t is None:
                continue
            all_mentions[key].append((f"relation_{role}", t))
            if key not in registry:
                registry[key] = t
            elif registry[key] != t:
                violations.append({
                    "span": text,
                    "span_key": key,
                    "doc_id": doc["doc_id"],
                    "first_seen_type": registry[key],
                    "attempted_type": t,
                    "source": f"relation_{role}",
                    "relation_type": rel.get("type", ""),
                    "gold_types": sorted(gold_map.get(key, set())),
                })

    return violations, all_mentions, gold_map


def classify_violation(v):
    """Classify a CF violation by comparing first-seen and attempted types to gold."""
    fs = v["first_seen_type"]
    at = v["attempted_type"]
    gold = set(v["gold_types"])

    if not gold:
        return "no_gold_match"

    fs_correct = fs in gold
    at_correct = at in gold

    if fs_correct and not at_correct:
        return "correct_lock"  # first-seen was right, constraint blocked a wrong type
    elif not fs_correct and at_correct:
        return "cascade_error"  # first-seen was WRONG, blocked the correct type
    elif fs_correct and at_correct:
        return "legitimate_ambiguity"  # both types are valid in gold (multi-type entity)
    else:
        return "both_wrong"  # neither type matches gold


def generic_category(fs, at):
    """Categorize Generic involvement."""
    if fs == "Generic" and at != "Generic":
        return "Generic->Specific"
    elif fs != "Generic" and at == "Generic":
        return "Specific->Generic"
    elif fs != "Generic" and at != "Generic":
        return "Specific->Specific"
    else:
        return "Generic->Generic"


def analyze_file(input_path, label):
    docs = []
    with open(input_path) as f:
        for line in f:
            line = line.strip()
            if line:
                docs.append(json.loads(line))

    all_violations = []
    docs_with_violations = 0
    total_entities = 0
    total_relations = 0

    for doc in docs:
        parsed = doc.get("parsed_output") or {}
        entities = parsed.get("entities") or []
        relations = parsed.get("relations") or []
        total_entities += len(entities)
        total_relations += len(relations)

        violations, mentions, gold_map = analyze_document(doc)
        if violations:
            docs_with_violations += 1
        all_violations.extend(violations)

    # Classify violations
    classifications = Counter()
    generic_cats = Counter()
    type_pair_counts = Counter()
    cascade_examples = []
    correct_lock_examples = []

    for v in all_violations:
        cls = classify_violation(v)
        classifications[cls] += 1
        v["classification"] = cls

        gc = generic_category(v["first_seen_type"], v["attempted_type"])
        generic_cats[gc] += 1
        v["generic_category"] = gc

        pair = f"{v['first_seen_type']}->{v['attempted_type']}"
        type_pair_counts[pair] += 1

        if cls == "cascade_error" and len(cascade_examples) < 20:
            cascade_examples.append(v)
        elif cls == "correct_lock" and len(correct_lock_examples) < 10:
            correct_lock_examples.append(v)

    # Cascade error sub-breakdown by Generic involvement
    cascade_generic = Counter()
    for v in all_violations:
        if v["classification"] == "cascade_error":
            cascade_generic[v["generic_category"]] += 1

    # Unique entities involved
    unique_cf_entities = len(set(
        (v["doc_id"], v["span_key"]) for v in all_violations
    ))

    # Print results
    print(f"\n{'='*70}")
    print(f"  First-seen Cascade Error Analysis: {label}")
    print(f"  Input: {input_path}")
    print(f"{'='*70}")
    print(f"\nDataset: {len(docs)} documents, {total_entities} entities, {total_relations} relations")
    print(f"\nTotal CF violations (first-seen conflicts): {len(all_violations)}")
    print(f"Unique (doc, entity) pairs with CF:         {unique_cf_entities}")
    print(f"Documents with CF violations:               {docs_with_violations}/{len(docs)}")

    print(f"\n--- Classification Breakdown ---")
    for cls in ["cascade_error", "correct_lock", "legitimate_ambiguity", "both_wrong", "no_gold_match"]:
        n = classifications.get(cls, 0)
        pct = 100 * n / len(all_violations) if all_violations else 0
        desc = {
            "cascade_error": "First-seen WRONG, blocked correct type",
            "correct_lock": "First-seen correct, blocked wrong type",
            "legitimate_ambiguity": "Both types valid in gold",
            "both_wrong": "Neither type matches gold",
            "no_gold_match": "Entity not in gold annotations",
        }[cls]
        print(f"  {cls:25s}: {n:4d} ({pct:5.1f}%)  -- {desc}")

    print(f"\n--- Generic Involvement ---")
    for gc in ["Generic->Specific", "Specific->Generic", "Specific->Specific", "Generic->Generic"]:
        n = generic_cats.get(gc, 0)
        pct = 100 * n / len(all_violations) if all_violations else 0
        print(f"  {gc:25s}: {n:4d} ({pct:5.1f}%)")

    print(f"\n--- Cascade Errors by Generic Involvement ---")
    n_cascade = classifications.get("cascade_error", 0)
    for gc in ["Generic->Specific", "Specific->Generic", "Specific->Specific", "Generic->Generic"]:
        n = cascade_generic.get(gc, 0)
        pct = 100 * n / n_cascade if n_cascade else 0
        print(f"  {gc:25s}: {n:4d} ({pct:5.1f}%)")

    print(f"\n--- Top Type Transition Pairs (first-seen -> attempted) ---")
    for pair, count in type_pair_counts.most_common(15):
        print(f"  {pair:40s}: {count:4d}")

    if cascade_examples:
        print(f"\n--- Cascade Error Examples (first-seen WRONG, blocked correct) ---")
        for ex in cascade_examples[:10]:
            gold_str = ", ".join(ex["gold_types"]) if ex["gold_types"] else "N/A"
            print(f"  [{ex['doc_id']}] \"{ex['span']}\"")
            print(f"    first-seen: {ex['first_seen_type']} | attempted: {ex['attempted_type']} | gold: {gold_str}")
            if ex.get("relation_type"):
                print(f"    in relation: {ex['relation_type']} (as {ex['source'].replace('relation_', '')})")

    if correct_lock_examples:
        print(f"\n--- Correct Lock Examples (first-seen correct, blocked wrong) ---")
        for ex in correct_lock_examples[:5]:
            gold_str = ", ".join(ex["gold_types"]) if ex["gold_types"] else "N/A"
            print(f"  [{ex['doc_id']}] \"{ex['span']}\"")
            print(f"    first-seen: {ex['first_seen_type']} | attempted: {ex['attempted_type']} | gold: {gold_str}")

    # Build JSON report
    report = {
        "label": label,
        "input_file": str(input_path),
        "total_docs": len(docs),
        "total_entities": total_entities,
        "total_relations": total_relations,
        "total_cf_violations": len(all_violations),
        "unique_cf_entity_doc_pairs": unique_cf_entities,
        "docs_with_violations": docs_with_violations,
        "classification": dict(classifications),
        "generic_involvement": dict(generic_cats),
        "cascade_by_generic": dict(cascade_generic),
        "type_pair_counts": dict(type_pair_counts.most_common(30)),
        "cascade_examples": cascade_examples,
        "correct_lock_examples": correct_lock_examples[:10],
        "all_violations": all_violations,
    }
    return report


def print_summary_comparison(reports):
    print(f"\n{'='*70}")
    print(f"  Summary Comparison: ZS vs FT")
    print(f"{'='*70}")
    print(f"{'Metric':<45s} {'ZS':>10s} {'FT':>10s}")
    print("-" * 70)
    for key in ["total_cf_violations", "unique_cf_entity_doc_pairs", "docs_with_violations"]:
        zs = reports[0].get(key, 0)
        ft = reports[1].get(key, 0)
        print(f"{key:<45s} {zs:>10d} {ft:>10d}")
    print()
    for cls in ["cascade_error", "correct_lock", "legitimate_ambiguity", "both_wrong", "no_gold_match"]:
        zs = reports[0]["classification"].get(cls, 0)
        ft = reports[1]["classification"].get(cls, 0)
        print(f"  {cls:<43s} {zs:>10d} {ft:>10d}")


if __name__ == "__main__":
    outputs = BASE / "outputs"

    zs_file = outputs / "phase2_scierc_full_s1_v2.jsonl"
    ft_file = outputs / "w5_lora_scierc_full_s1_eval.jsonl"

    reports = []
    for fpath, label in [(zs_file, "Qwen ZS SciERC S1"), (ft_file, "Qwen FT SciERC S1")]:
        if fpath.exists():
            report = analyze_file(fpath, label)
            reports.append(report)

            out_json = outputs / f"cf_cascade_analysis_{label.replace(' ', '_').lower()}.json"
            with open(out_json, "w") as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            print(f"\nDetailed report saved to {out_json}")
        else:
            print(f"WARNING: {fpath} not found, skipping.")

    if len(reports) == 2:
        print_summary_comparison(reports)

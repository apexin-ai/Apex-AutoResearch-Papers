#!/usr/bin/env python3
"""Analyze DR violation elimination: are removed triples FP or TP?"""

import json
import os
from collections import defaultdict

OUT_DIR = "/root/schema_semantic_constrained_ie/outputs"
SCIERC_CONSTRAINT = "/root/schema_semantic_constrained_ie/ontology_constraints.json"
DOCRED_CONSTRAINT = "/root/schema_semantic_constrained_ie/data/docred/ontology_constraints_docred.json"
RESULT_PATH = "/root/autodl-tmp/schema_outputs/r12_dr_f1_impact.json"

PAIRS = {
    "scierc_qwen_ft": {
        "unc": f"{OUT_DIR}/w5_lora_scierc_unconstrained_eval.jsonl",
        "con": f"{OUT_DIR}/w5_lora_scierc_full_s1_eval.jsonl",
        "dataset": "scierc",
    },
    "scierc_llama_ft": {
        "unc": f"{OUT_DIR}/w5_llama_lora_scierc_unconstrained.jsonl",
        "con": f"{OUT_DIR}/w5_llama_lora_scierc_constrained.jsonl",
        "dataset": "scierc",
    },
    "docred_qwen_ft": {
        "unc": f"{OUT_DIR}/w5_qwen_docred_lora_unconstrained_eval.jsonl",
        "con": f"{OUT_DIR}/w5_qwen_docred_lora_constrained_eval.jsonl",
        "dataset": "docred",
    },
    "docred_llama_ft": {
        "unc": f"{OUT_DIR}/w5_llama_docred_lora_unconstrained_eval.jsonl",
        "con": f"{OUT_DIR}/w5_llama_docred_lora_constrained_eval.jsonl",
        "dataset": "docred",
    },
}


def load_jsonl(path):
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def load_constraints(dataset):
    if dataset == "scierc":
        with open(SCIERC_CONSTRAINT) as f:
            data = json.load(f)
        valid = set()
        for rel, info in data["relation_constraints"].items():
            for pair in info["valid_pairs"]:
                valid.add((pair[0], rel, pair[1]))
        return valid, None
    else:
        with open(DOCRED_CONSTRAINT) as f:
            data = json.load(f)
        # Build name -> P-code mapping
        name_to_pcode = {}
        pcode_to_name = {}
        for pcode, name in data["relation_types"].items():
            name_to_pcode[name.lower()] = pcode
            pcode_to_name[pcode] = name.lower()
        valid = set()
        for rel, info in data["relation_constraints"].items():
            rel_name = pcode_to_name.get(rel, rel).lower()
            for pair in info["valid_pairs"]:
                valid.add((pair[0], rel_name, pair[1]))
        return valid, name_to_pcode


def triple_key(r):
    return (r["head"].strip().lower(), r["tail"].strip().lower(), r["type"].strip().lower())


def triple_key_no_rel(r):
    return (r["head"].strip().lower(), r["tail"].strip().lower())


def has_dr_violation(r, valid_set, dataset):
    ht = r.get("head_type", "").strip()
    tt = r.get("tail_type", "").strip()
    rel = r["type"].strip()
    if dataset == "docred":
        rel = rel.lower()
    if not ht or not tt:
        return True
    return (ht, rel, tt) not in valid_set


def get_pred_relations(record):
    po = record.get("parsed_output")
    if not po:
        return []
    return po.get("relations", [])


def analyze_pair(name, cfg):
    dataset = cfg["dataset"]
    valid_set, name_to_pcode = load_constraints(dataset)

    unc_records = load_jsonl(cfg["unc"])
    con_records = load_jsonl(cfg["con"])

    # Index con records by doc_id
    con_by_doc = {}
    for rec in con_records:
        con_by_doc[rec["doc_id"]] = rec

    stats = {
        "total_unc_triples": 0,
        "total_con_triples": 0,
        "total_dr_violations_in_unc": 0,
        "eliminated_triples": 0,
        "eliminated_with_dr_violation": 0,
        "eliminated_no_dr_violation": 0,
        "dr_eliminated_false_positive": 0,
        "dr_eliminated_tp_wrong_type": 0,
        "dr_eliminated_tp_correct_type": 0,
        "per_relation_breakdown": defaultdict(lambda: {
            "total_dr_violations_unc": 0,
            "eliminated_dr": 0,
            "fp": 0,
            "tp_wrong_type": 0,
            "tp_correct": 0,
        }),
        "examples": [],
    }

    for unc_rec in unc_records:
        doc_id = unc_rec["doc_id"]
        con_rec = con_by_doc.get(doc_id)
        if not con_rec:
            continue

        unc_rels = get_pred_relations(unc_rec)
        con_rels = get_pred_relations(con_rec)
        gold_rels = unc_rec.get("gold_relations", [])

        stats["total_unc_triples"] += len(unc_rels)
        stats["total_con_triples"] += len(con_rels)

        # Count DR violations in unc
        for r in unc_rels:
            if has_dr_violation(r, valid_set, dataset):
                stats["total_dr_violations_in_unc"] += 1

        # Build con triple set for comparison
        con_keys = set()
        for r in con_rels:
            con_keys.add(triple_key(r))

        # Build gold sets for matching
        # For SciERC: gold uses same format
        # For DocRED: gold uses P-codes, pred uses natural language
        gold_full_keys = set()  # (head, tail, rel) with normalized rel
        gold_pair_keys = set()  # (head, tail) only
        gold_rels_by_pair = defaultdict(set)  # (head, tail) -> set of rel types

        for g in gold_rels:
            gh = g["head"].strip().lower()
            gt = g["tail"].strip().lower()
            grel = g["type"].strip()
            if dataset == "docred":
                # Convert P-code to natural language name
                if name_to_pcode is not None:
                    # grel is a P-code, convert to name
                    from_constraint = None
                    with open(DOCRED_CONSTRAINT) as f:
                        dc = json.load(f)
                    from_constraint = dc["relation_types"].get(grel, grel)
                    grel_norm = from_constraint.lower()
                else:
                    grel_norm = grel.lower()
            else:
                grel_norm = grel

            gold_full_keys.add((gh, gt, grel_norm))
            gold_pair_keys.add((gh, gt))
            gold_rels_by_pair[(gh, gt)].add(grel_norm)

        # Find eliminated triples (in unc but not in con)
        for r in unc_rels:
            tk = triple_key(r)
            if tk not in con_keys:
                stats["eliminated_triples"] += 1
                is_dr = has_dr_violation(r, valid_set, dataset)

                if is_dr:
                    stats["eliminated_with_dr_violation"] += 1
                    rel_name = r["type"].strip()
                    if dataset == "docred":
                        rel_name = rel_name.lower()

                    rb = stats["per_relation_breakdown"][rel_name]
                    rb["eliminated_dr"] += 1

                    # Check against gold
                    rh = r["head"].strip().lower()
                    rt = r["tail"].strip().lower()
                    rrel = r["type"].strip()
                    if dataset == "docred":
                        rrel = rrel.lower()

                    if (rh, rt, rrel) in gold_full_keys:
                        stats["dr_eliminated_tp_correct_type"] += 1
                        rb["tp_correct"] += 1
                        if len(stats["examples"]) < 5:
                            stats["examples"].append({
                                "doc_id": doc_id,
                                "category": "tp_correct_type",
                                "triple": {"head": r["head"], "tail": r["tail"],
                                           "type": r["type"],
                                           "head_type": r.get("head_type"),
                                           "tail_type": r.get("tail_type")},
                            })
                    elif (rh, rt) in gold_pair_keys:
                        stats["dr_eliminated_tp_wrong_type"] += 1
                        rb["tp_wrong_type"] += 1
                        if len(stats["examples"]) < 10:
                            gold_rels_for_pair = gold_rels_by_pair.get((rh, rt), set())
                            stats["examples"].append({
                                "doc_id": doc_id,
                                "category": "tp_wrong_type",
                                "triple": {"head": r["head"], "tail": r["tail"],
                                           "type": r["type"],
                                           "head_type": r.get("head_type"),
                                           "tail_type": r.get("tail_type")},
                                "gold_relations_for_pair": list(gold_rels_for_pair),
                            })
                    else:
                        stats["dr_eliminated_false_positive"] += 1
                        rb["fp"] += 1
                else:
                    stats["eliminated_no_dr_violation"] += 1

    # Count per-relation DR violations in unc
    for unc_rec in unc_records:
        for r in get_pred_relations(unc_rec):
            if has_dr_violation(r, valid_set, dataset):
                rel_name = r["type"].strip()
                if dataset == "docred":
                    rel_name = rel_name.lower()
                stats["per_relation_breakdown"][rel_name]["total_dr_violations_unc"] += 1

    # Convert defaultdict to dict
    stats["per_relation_breakdown"] = {
        k: dict(v) for k, v in stats["per_relation_breakdown"].items()
    }

    return stats


def main():
    # Avoid reopening constraint file in inner loop - preload
    # Actually let me fix the docred gold rel normalization to avoid re-reading file
    # Load docred mapping once
    with open(DOCRED_CONSTRAINT) as f:
        docred_data = json.load(f)
    docred_pcode_to_name = {}
    for pcode, name in docred_data["relation_types"].items():
        docred_pcode_to_name[pcode] = name.lower()

    results = {}

    for name, cfg in PAIRS.items():
        print(f"Analyzing {name}...")
        dataset = cfg["dataset"]
        valid_set, name_to_pcode = load_constraints(dataset)

        unc_records = load_jsonl(cfg["unc"])
        con_records = load_jsonl(cfg["con"])

        con_by_doc = {}
        for rec in con_records:
            con_by_doc[rec["doc_id"]] = rec

        st = {
            "total_unc_triples": 0,
            "total_con_triples": 0,
            "total_dr_violations_in_unc": 0,
            "eliminated_triples": 0,
            "eliminated_with_dr_violation": 0,
            "eliminated_no_dr_violation": 0,
            "dr_eliminated_false_positive": 0,
            "dr_eliminated_tp_wrong_type": 0,
            "dr_eliminated_tp_correct_type": 0,
            "per_relation_breakdown": defaultdict(lambda: {
                "total_dr_violations_unc": 0,
                "eliminated_dr": 0,
                "fp": 0, "tp_wrong_type": 0, "tp_correct": 0,
            }),
            "examples_tp_correct": [],
            "examples_tp_wrong_type": [],
            "examples_fp": [],
        }

        for unc_rec in unc_records:
            doc_id = unc_rec["doc_id"]
            con_rec = con_by_doc.get(doc_id)
            if not con_rec:
                continue

            unc_rels = get_pred_relations(unc_rec)
            con_rels = get_pred_relations(con_rec)
            gold_rels_raw = unc_rec.get("gold_relations", [])

            st["total_unc_triples"] += len(unc_rels)
            st["total_con_triples"] += len(con_rels)

            # Build gold lookup
            gold_full_keys = set()
            gold_pair_keys = set()
            gold_rels_by_pair = defaultdict(set)
            for g in gold_rels_raw:
                gh = g["head"].strip().lower()
                gt = g["tail"].strip().lower()
                grel = g["type"].strip()
                if dataset == "docred":
                    grel_norm = docred_pcode_to_name.get(grel, grel).lower()
                else:
                    grel_norm = grel
                gold_full_keys.add((gh, gt, grel_norm))
                gold_pair_keys.add((gh, gt))
                gold_rels_by_pair[(gh, gt)].add(grel_norm)

            # Build con triple set
            con_keys = set()
            for r in con_rels:
                con_keys.add(triple_key(r))

            for r in unc_rels:
                rel_name = r["type"].strip()
                if dataset == "docred":
                    rel_name = rel_name.lower()

                is_dr = has_dr_violation(r, valid_set, dataset)
                if is_dr:
                    st["total_dr_violations_in_unc"] += 1
                    st["per_relation_breakdown"][rel_name]["total_dr_violations_unc"] += 1

                tk = triple_key(r)
                if tk not in con_keys:
                    st["eliminated_triples"] += 1
                    if is_dr:
                        st["eliminated_with_dr_violation"] += 1
                        rb = st["per_relation_breakdown"][rel_name]
                        rb["eliminated_dr"] += 1

                        rh = r["head"].strip().lower()
                        rt = r["tail"].strip().lower()
                        rrel = rel_name

                        triple_info = {
                            "doc_id": doc_id,
                            "head": r["head"], "tail": r["tail"],
                            "type": r["type"],
                            "head_type": r.get("head_type", ""),
                            "tail_type": r.get("tail_type", ""),
                        }

                        if (rh, rt, rrel) in gold_full_keys:
                            st["dr_eliminated_tp_correct_type"] += 1
                            rb["tp_correct"] += 1
                            if len(st["examples_tp_correct"]) < 5:
                                st["examples_tp_correct"].append(triple_info)
                        elif (rh, rt) in gold_pair_keys:
                            st["dr_eliminated_tp_wrong_type"] += 1
                            rb["tp_wrong_type"] += 1
                            if len(st["examples_tp_wrong_type"]) < 5:
                                triple_info["gold_rels"] = list(gold_rels_by_pair.get((rh, rt), []))
                                st["examples_tp_wrong_type"].append(triple_info)
                        else:
                            st["dr_eliminated_false_positive"] += 1
                            rb["fp"] += 1
                            if len(st["examples_fp"]) < 5:
                                st["examples_fp"].append(triple_info)
                    else:
                        st["eliminated_no_dr_violation"] += 1

        st["per_relation_breakdown"] = {k: dict(v) for k, v in st["per_relation_breakdown"].items()}
        results[name] = st
        print(f"  DR violations in unc: {st['total_dr_violations_in_unc']}")
        print(f"  Eliminated by constraint (DR): {st['eliminated_with_dr_violation']}")
        print(f"  -> FP: {st['dr_eliminated_false_positive']}, TP wrong type: {st['dr_eliminated_tp_wrong_type']}, TP correct: {st['dr_eliminated_tp_correct_type']}")

    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    for name, st in results.items():
        total_elim_dr = st["eliminated_with_dr_violation"]
        fp = st["dr_eliminated_false_positive"]
        tp_wt = st["dr_eliminated_tp_wrong_type"]
        tp_c = st["dr_eliminated_tp_correct_type"]
        print(f"\n{name}:")
        print(f"  Total unc triples: {st['total_unc_triples']}")
        print(f"  Total con triples: {st['total_con_triples']}")
        print(f"  DR violations in unc: {st['total_dr_violations_in_unc']}")
        print(f"  Eliminated triples total: {st['eliminated_triples']}")
        print(f"    With DR violation: {total_elim_dr}")
        print(f"    Without DR violation: {st['eliminated_no_dr_violation']}")
        if total_elim_dr > 0:
            print(f"  Of DR-eliminated triples:")
            print(f"    False positives: {fp} ({fp/total_elim_dr*100:.1f}%)")
            print(f"    TP wrong type:   {tp_wt} ({tp_wt/total_elim_dr*100:.1f}%)")
            print(f"    TP correct type: {tp_c} ({tp_c/total_elim_dr*100:.1f}%)")

    os.makedirs(os.path.dirname(RESULT_PATH), exist_ok=True)
    with open(RESULT_PATH, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False, default=str)
    print(f"\nResults saved to {RESULT_PATH}")


if __name__ == "__main__":
    main()

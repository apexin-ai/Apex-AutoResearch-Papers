"""Paired bootstrap significance test for S1 vs S2 comparison.

Computes corpus-level micro R-F1 via paired bootstrap resampling of documents.
Also computes Part 2 rejection analysis for DocRED 70B.
No numpy dependency - pure stdlib.
"""
import json
import random
from collections import defaultdict
from pathlib import Path

# --- Normalization ---

SCIERC_TYPE_MAP = {
    "otherscientificterm": "OtherScientificTerm",
    "other-scientificterm": "OtherScientificTerm",
    "other_scientific_term": "OtherScientificTerm",
    "scientificterm": "OtherScientificTerm",
    "other": "OtherScientificTerm",
}

SCIERC_VALID_TYPES = ["Task", "Method", "Material", "Metric", "OtherScientificTerm", "Generic"]

DOCRED_ENTITY_TYPE_ALIASES = {
    'PERSON': 'PER', 'PEOPLE': 'PER',
    'ORGANIZATION': 'ORG', 'ORGANISATION': 'ORG',
    'LOCATION': 'LOC',
    'NUMBER': 'NUM', 'NUMERICAL': 'NUM',
    'MISCELLANEOUS': 'MISC',
}

def scierc_normalize_type(t):
    t_lower = t.strip().lower().replace(" ", "").replace("_", "").replace("-", "")
    for vt in SCIERC_VALID_TYPES:
        if t_lower == vt.lower().replace(" ", "").replace("_", "").replace("-", ""):
            return vt
    if t_lower in SCIERC_TYPE_MAP:
        return SCIERC_TYPE_MAP[t_lower]
    return t

def docred_normalize_entity_type(raw_type):
    t = raw_type.strip().upper()
    return DOCRED_ENTITY_TYPE_ALIASES.get(t, t)

def _levenshtein(s1, s2):
    if len(s1) < len(s2):
        return _levenshtein(s2, s1)
    if len(s2) == 0:
        return len(s1)
    prev_row = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        curr_row = [i + 1]
        for j, c2 in enumerate(s2):
            curr_row.append(min(prev_row[j + 1] + 1, curr_row[j] + 1, prev_row[j] + (c1 != c2)))
        prev_row = curr_row
    return prev_row[-1]

def docred_normalize_relation(rel_name, rel_types, name_to_id):
    rel_key = name_to_id.get(rel_name.lower().strip())
    if rel_key:
        return rel_key
    rel_tokens = set(rel_name.strip().lower().split())
    best_pid, best_overlap = None, 0.0
    for rid, rname in rel_types.items():
        rname_tokens = set(rname.lower().split())
        if rel_tokens and rname_tokens:
            ratio = len(rel_tokens & rname_tokens) / len(rel_tokens | rname_tokens)
            if ratio > 0.8 and ratio > best_overlap:
                best_overlap = ratio
                best_pid = rid
    if best_pid:
        return best_pid
    for rid, rname in rel_types.items():
        if _levenshtein(rel_name.strip().lower(), rname.lower()) <= 2:
            return rid
    return None

def build_name_to_id(rel_types):
    name_to_id = {}
    for rid, rname in rel_types.items():
        name_to_id[rname.lower().strip()] = rid
        name_to_id[rid.lower()] = rid
    return name_to_id


# --- Per-document stats ---

def scierc_doc_stats(rec):
    parsed = rec.get("parsed_output")
    gold_rels = rec.get("gold_relations", [])
    gold_rel_set = set(
        (r["head"].lower().strip(), r["tail"].lower().strip(), r["type"])
        for r in gold_rels
    )
    if parsed is None:
        return {"tp": 0, "fp": 0, "fn": len(gold_rel_set), "pred_set": set(), "gold_set": gold_rel_set}
    relations = parsed.get("relations", [])
    pred_rel_set = set(
        (r.get("head", "").lower().strip(), r.get("tail", "").lower().strip(), r.get("type", ""))
        for r in relations
    )
    tp = len(gold_rel_set & pred_rel_set)
    fp = len(pred_rel_set) - tp
    fn = len(gold_rel_set) - tp
    return {"tp": tp, "fp": fp, "fn": fn, "pred_set": pred_rel_set, "gold_set": gold_rel_set}


def docred_doc_stats(rec, rel_types, name_to_id):
    parsed = rec.get("parsed_output")
    gold_rels = rec.get("gold_relations", [])
    gold_rel_set = set()
    for r in gold_rels:
        h = r["head"].lower().strip()
        t = r["tail"].lower().strip()
        rtype = r["type"]
        if not rtype.startswith("P"):
            normalized = docred_normalize_relation(rtype, rel_types, name_to_id)
            if normalized:
                rtype = normalized
        gold_rel_set.add((h, t, rtype))

    if parsed is None:
        return {"tp": 0, "fp": 0, "fn": len(gold_rel_set), "pred_set": set(), "gold_set": gold_rel_set}

    relations = parsed.get("relations", [])
    pred_rel_set = set()
    for r in relations:
        h = r.get("head", "").lower().strip()
        t = r.get("tail", "").lower().strip()
        rtype = r.get("type", "")
        if not rtype.startswith("P"):
            normalized = docred_normalize_relation(rtype, rel_types, name_to_id)
            if normalized:
                rtype = normalized
            else:
                continue
        pred_rel_set.add((h, t, rtype))

    tp = len(gold_rel_set & pred_rel_set)
    fp = len(pred_rel_set) - tp
    fn = len(gold_rel_set) - tp
    return {"tp": tp, "fp": fp, "fn": fn, "pred_set": pred_rel_set, "gold_set": gold_rel_set}


def compute_micro_f1(stats_list):
    total_tp = sum(s["tp"] for s in stats_list)
    total_fp = sum(s["fp"] for s in stats_list)
    total_fn = sum(s["fn"] for s in stats_list)
    p = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0
    r = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0
    f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0
    return f1


def percentile(data, pct):
    sorted_d = sorted(data)
    k = (len(sorted_d) - 1) * pct / 100.0
    f = int(k)
    c = f + 1 if f + 1 < len(sorted_d) else f
    d = k - f
    return sorted_d[f] + d * (sorted_d[c] - sorted_d[f])


def paired_bootstrap_micro_f1(s1_stats, s2_stats, n_bootstrap=10000, seed=42):
    rng = random.Random(seed)
    n = len(s1_stats)
    assert n == len(s2_stats)

    s1_f1 = compute_micro_f1(s1_stats)
    s2_f1 = compute_micro_f1(s2_stats)
    observed_diff = s1_f1 - s2_f1

    boot_diffs = []
    indices = list(range(n))
    for _ in range(n_bootstrap):
        idx = rng.choices(indices, k=n)
        s1_boot = [s1_stats[i] for i in idx]
        s2_boot = [s2_stats[i] for i in idx]
        boot_diffs.append(compute_micro_f1(s1_boot) - compute_micro_f1(s2_boot))

    p_value = sum(1 for d in boot_diffs if d <= 0) / len(boot_diffs)
    ci_low = percentile(boot_diffs, 2.5)
    ci_high = percentile(boot_diffs, 97.5)

    return {
        "s1_f1": round(s1_f1 * 100, 2),
        "s2_f1": round(s2_f1 * 100, 2),
        "delta": round(observed_diff * 100, 2),
        "p_value": round(p_value, 4),
        "ci_low": round(ci_low * 100, 2),
        "ci_high": round(ci_high * 100, 2),
    }


def load_jsonl(path):
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def run_scierc_pair(s1_path, s2_path, label):
    s1_recs = load_jsonl(s1_path)
    s2_recs = load_jsonl(s2_path)

    s1_by_id = {r["doc_id"]: r for r in s1_recs}
    s2_by_id = {r["doc_id"]: r for r in s2_recs}
    common_ids = sorted(set(s1_by_id.keys()) & set(s2_by_id.keys()))

    print(f"\n--- {label} ---")
    print(f"S1 docs: {len(s1_recs)}, S2 docs: {len(s2_recs)}, paired: {len(common_ids)}")

    s1_stats = [scierc_doc_stats(s1_by_id[did]) for did in common_ids]
    s2_stats = [scierc_doc_stats(s2_by_id[did]) for did in common_ids]

    result = paired_bootstrap_micro_f1(s1_stats, s2_stats)
    print(f"S1 R-F1: {result['s1_f1']}%")
    print(f"S2 R-F1: {result['s2_f1']}%")
    print(f"Delta (S1-S2): {result['delta']:+.2f}pp")
    print(f"p-value: {result['p_value']}")
    print(f"95% CI: [{result['ci_low']:+.2f}, {result['ci_high']:+.2f}]pp")

    return result, common_ids, s1_stats, s2_stats


def run_docred_pair(s1_path, s2_path, constraints_path, label):
    with open(constraints_path) as f:
        constraints = json.load(f)
    rel_types = constraints.get("relation_types", {})
    name_to_id = build_name_to_id(rel_types)

    s1_recs = load_jsonl(s1_path)
    s2_recs = load_jsonl(s2_path)

    s1_by_id = {r["doc_id"]: r for r in s1_recs}
    s2_by_id = {r["doc_id"]: r for r in s2_recs}
    common_ids = sorted(set(s1_by_id.keys()) & set(s2_by_id.keys()))

    print(f"\n--- {label} ---")
    print(f"S1 docs: {len(s1_recs)}, S2 docs: {len(s2_recs)}, paired: {len(common_ids)}")

    s1_stats = [docred_doc_stats(s1_by_id[did], rel_types, name_to_id) for did in common_ids]
    s2_stats = [docred_doc_stats(s2_by_id[did], rel_types, name_to_id) for did in common_ids]

    result = paired_bootstrap_micro_f1(s1_stats, s2_stats)
    print(f"S1 R-F1: {result['s1_f1']}%")
    print(f"S2 R-F1: {result['s2_f1']}%")
    print(f"Delta (S1-S2): {result['delta']:+.2f}pp")
    print(f"p-value: {result['p_value']}")
    print(f"95% CI: [{result['ci_low']:+.2f}, {result['ci_high']:+.2f}]pp")

    return result, common_ids, s1_stats, s2_stats, s1_by_id, s2_by_id, rel_types, name_to_id


def rejection_analysis(common_ids, s1_stats, s2_stats, s1_by_id, s2_by_id, rel_types, name_to_id, label):
    """Part 2: Analyze triples rejected by S2 repair."""
    print(f"\n=== Part 2: {label} S2 Rejection Analysis ===")

    total_s1_triples = 0
    total_s2_triples = 0
    rejected_triples = 0
    rejected_gold_matches = 0
    total_gold = 0
    s1_cf_violations = 0
    s2_cf_violations = 0

    for i, did in enumerate(common_ids):
        s1_pred = s1_stats[i]["pred_set"]
        s2_pred = s2_stats[i]["pred_set"]
        gold = s1_stats[i]["gold_set"]

        total_s1_triples += len(s1_pred)
        total_s2_triples += len(s2_pred)
        total_gold += len(gold)

        in_s1_not_s2 = s1_pred - s2_pred
        rejected_triples += len(in_s1_not_s2)
        rejected_gold_matches += len(in_s1_not_s2 & gold)

        # CF: check entity type consistency
        s1_rec = s1_by_id[did]
        s2_rec = s2_by_id[did]
        for rec_parsed, cf_counter_name in [(s1_rec, "s1"), (s2_rec, "s2")]:
            parsed = rec_parsed.get("parsed_output")
            if parsed is None:
                continue
            entity_types = {}
            rels = parsed.get("relations", [])
            cf_found = 0
            for r in rels:
                for prefix in ["head", "tail"]:
                    name = r.get(prefix, "").lower().strip()
                    etype = r.get(f"{prefix}_type", "")
                    if name in entity_types and entity_types[name] != etype:
                        cf_found += 1
                        break
                    entity_types[name] = etype
            if cf_counter_name == "s1":
                s1_cf_violations += cf_found
            else:
                s2_cf_violations += cf_found

    in_s2_not_s1 = 0
    for i, did in enumerate(common_ids):
        in_s2_not_s1 += len(s2_stats[i]["pred_set"] - s1_stats[i]["pred_set"])

    print(f"S1 total predicted triples: {total_s1_triples}")
    print(f"S2 total predicted triples: {total_s2_triples}")
    print(f"Triples in S1 but not S2 (rejected by repair): {rejected_triples}")
    print(f"Triples in S2 but not S1 (added by repair): {in_s2_not_s1}")
    if rejected_triples > 0:
        print(f"Of rejected: {rejected_gold_matches} gold matches ({100*rejected_gold_matches/rejected_triples:.1f}%)")
    print(f"Total gold triples: {total_gold}")


if __name__ == "__main__":
    import sys
    import os
    os.chdir("/root/schema_semantic_constrained_ie")

    mode = sys.argv[1] if len(sys.argv) > 1 else "scierc"

    all_results = {}

    if mode in ("scierc", "all"):
        # 8B ZS SciERC
        r1, _, _, _ = run_scierc_pair(
            "outputs/phase2_scierc_full_s1_v2.jsonl",
            "outputs/phase2_scierc_full_s2.jsonl",
            "8B ZS SciERC"
        )
        all_results["8b_zs_scierc"] = r1

        # 70B FT SciERC
        r2, _, _, _ = run_scierc_pair(
            "outputs/70b_lora_scierc_beam4_s1.jsonl",
            "outputs/70b_lora_scierc_full_s2.jsonl",
            "70B FT SciERC (beam4 S1 vs greedy S2)"
        )
        all_results["70b_ft_scierc"] = r2

    if mode in ("docred", "all"):
        # 70B FT DocRED
        r3, common_ids, s1_stats, s2_stats, s1_by_id, s2_by_id, rel_types, name_to_id = run_docred_pair(
            "outputs/70b_lora_docred_200_beam4_s1.jsonl",
            "outputs/70b_lora_docred_200_full_s2.jsonl",
            "data/docred/ontology_constraints_docred.json",
            "70B FT DocRED (beam4 S1 vs greedy S2)"
        )
        all_results["70b_ft_docred"] = r3

        # Part 2: Rejection analysis
        rejection_analysis(
            common_ids, s1_stats, s2_stats, s1_by_id, s2_by_id,
            rel_types, name_to_id,
            "70B FT DocRED"
        )

    print("\n=== Summary Table ===")
    print(f"| {'Config':<30} | {'S1 R-F1':>8} | {'S2 R-F1':>8} | {'Δ(S1-S2)':>10} | {'p-value':>8} | {'95% CI':>20} |")
    print(f"|{'-'*32}|{'-'*10}|{'-'*10}|{'-'*12}|{'-'*10}|{'-'*22}|")
    for name, r in all_results.items():
        ci_str = f"[{r['ci_low']:+.2f}, {r['ci_high']:+.2f}]"
        print(f"| {name:<30} | {r['s1_f1']:>7.2f}% | {r['s2_f1']:>7.2f}% | {r['delta']:>+9.2f}pp | {r['p_value']:>8.4f} | {ci_str:>20} |")

    # Save results
    output_path = "outputs/s1_vs_s2_bootstrap_results.json"
    with open(output_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to {output_path}")

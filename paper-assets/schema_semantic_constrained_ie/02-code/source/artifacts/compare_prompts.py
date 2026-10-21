"""Compare violation reports across prompt strategies (minimal vs schema-informed).

Usage:
    # Aggregate comparison from two violation reports:
    python compare_prompts.py \
        --report_a outputs/violation_report_scierc.json \
        --report_b outputs/violation_report_schema.json \
        --label_a minimal --label_b schema_informed

    # With McNemar test (requires raw outputs + constraints):
    python compare_prompts.py \
        --report_a outputs/violation_report_scierc.json \
        --report_b outputs/violation_report_schema.json \
        --raw_a outputs/raw_outputs.jsonl \
        --raw_b outputs/raw_outputs_schema.jsonl \
        --constraints ontology_constraints.json \
        --label_a minimal --label_b schema_informed \
        --dataset scierc

    # DocRED mode:
    python compare_prompts.py \
        --report_a outputs/violation_report_docred_minimal.json \
        --report_b outputs/violation_report_docred_schema.json \
        --raw_a outputs/raw_outputs_docred.jsonl \
        --raw_b outputs/raw_outputs_docred_schema.jsonl \
        --constraints data/docred/ontology_constraints_docred.json \
        --label_a minimal --label_b schema_informed \
        --dataset docred

Output: JSON report + text summary to stdout.
"""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path


def load_report(path):
    with open(path) as f:
        return json.load(f)


def load_jsonl(path):
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def normalize_summary_keys(summary):
    """Unify SciERC vs DocRED key differences."""
    s = dict(summary)
    if "total_samples" in s and "total_documents" not in s:
        s["total_documents"] = s.pop("total_samples")
    if "json_parse_failures" in s and "parse_failures" not in s:
        s["parse_failures"] = s.pop("json_parse_failures")
    return s


def compare_summaries(report_a, report_b, label_a, label_b):
    sa = normalize_summary_keys(report_a["summary"])
    sb = normalize_summary_keys(report_b["summary"])

    metrics = [
        ("total_documents", "Total Documents", "count"),
        ("total_entities_extracted", "Total Entities", "count"),
        ("total_triples_extracted", "Total Triples", "count"),
        ("parse_failures", "Parse Failures", "count"),
        ("entity_type_violation_rate", "Entity Type Violation Rate", "rate"),
        ("relation_vocabulary_violation_rate", "Relation Vocab Violation Rate", "rate"),
        ("domain_range_violation_rate", "Domain/Range Violation Rate", "rate"),
        ("cross_field_consistency_violation_rate", "Cross-field Consistency Rate", "rate"),
        ("total_violation_rate", "Total Violation Rate", "rate"),
        ("go_nogo_metric", "Go/No-go (D/R Rate)", "rate"),
    ]

    rows = []
    for key, display_name, fmt in metrics:
        va = sa.get(key)
        vb = sb.get(key)
        if va is None and vb is None:
            continue

        va = va if va is not None else 0
        vb = vb if vb is not None else 0
        delta = vb - va
        pct_change = (delta / va * 100) if va != 0 else float("inf") if delta != 0 else 0.0

        rows.append({
            "metric": display_name,
            "key": key,
            label_a: va,
            label_b: vb,
            "delta": round(delta, 6),
            "pct_change": round(pct_change, 2),
            "improved": delta < 0 if fmt == "rate" else None,
        })

    return rows


def compare_per_relation(report_a, report_b, label_a, label_b):
    pra = report_a.get("per_relation_type", {})
    prb = report_b.get("per_relation_type", {})

    all_relations = sorted(set(list(pra.keys()) + list(prb.keys())))
    rows = []
    for rel in all_relations:
        da = pra.get(rel, {"total": 0, "domain_range_violations": 0, "violation_rate": 0})
        db = prb.get(rel, {"total": 0, "domain_range_violations": 0, "violation_rate": 0})

        rate_a = da.get("violation_rate", 0)
        rate_b = db.get("violation_rate", 0)
        delta = rate_b - rate_a

        rows.append({
            "relation": rel,
            f"total_{label_a}": da.get("total", 0),
            f"violations_{label_a}": da.get("domain_range_violations", 0),
            f"rate_{label_a}": rate_a,
            f"total_{label_b}": db.get("total", 0),
            f"violations_{label_b}": db.get("domain_range_violations", 0),
            f"rate_{label_b}": rate_b,
            "delta": round(delta, 4),
            "improved": delta < 0,
        })

    return rows


# ── Per-sample violation detection for McNemar ──────────────────────────


def _check_scierc_sample(record, constraints):
    """Check domain/range violations for a single SciERC sample. Returns set of violation keys."""
    valid_entity_types = constraints["entity_types"]
    rel_constraints = constraints["relation_constraints"]
    valid_relation_types = constraints["relation_types"]

    valid_pairs_map = {}
    for rtype in rel_constraints:
        pairs = set()
        for pair in rel_constraints[rtype]:
            pairs.add((pair[0], pair[1]))
        valid_pairs_map[rtype] = pairs

    parsed = record.get("parsed_output")
    if parsed is None:
        raw = record.get("model_output", "")
        try:
            parsed = json.loads(raw)
        except (json.JSONDecodeError, TypeError):
            return set(), set(), set()

    relations = parsed.get("relations", [])
    dr_violations = set()
    rv_violations = set()
    et_violations = set()

    entities = parsed.get("entities", [])
    for ent in entities:
        etype = ent.get("type", "")
        t_lower = etype.strip().lower().replace(" ", "").replace("_", "").replace("-", "")
        matched = False
        for vt in valid_entity_types:
            if t_lower == vt.lower().replace(" ", "").replace("_", "").replace("-", ""):
                matched = True
                break
        if not matched:
            et_violations.add(ent.get("text", "") + "::" + etype)

    for i, rel in enumerate(relations):
        h_type = rel.get("head_type", "")
        t_type = rel.get("tail_type", "")
        rel_type = rel.get("type", "")

        rel_norm = rel_type.strip().lower().replace(" ", "").replace("_", "").replace("-", "")
        matched_rel = None
        for vrt in valid_relation_types:
            if rel_norm == vrt.lower().replace(" ", "").replace("_", "").replace("-", ""):
                matched_rel = vrt
                break

        if matched_rel is None:
            rv_violations.add(f"{i}:{rel_type}")
            continue

        nh = _norm_type_scierc(h_type, valid_entity_types)
        nt = _norm_type_scierc(t_type, valid_entity_types)
        if nh and nt and matched_rel in valid_pairs_map:
            if (nh, nt) not in valid_pairs_map[matched_rel]:
                dr_violations.add(f"{i}:{matched_rel}:{nh}:{nt}")

    return et_violations, rv_violations, dr_violations


def _norm_type_scierc(t, valid_types):
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


def _check_docred_sample(record, constraints):
    """Check violations for a single DocRED sample."""
    VALID_ENTITY_TYPES = {"PER", "ORG", "LOC", "TIME", "NUM", "MISC"}
    rel_types = constraints.get("relation_types", {})
    rel_constraints_map = constraints.get("relation_constraints", {})

    name_to_id = {}
    for rid, rname in rel_types.items():
        name_to_id[rname.lower().strip()] = rid
        name_to_id[rid.lower()] = rid

    parsed = record.get("parsed_output")
    if parsed is None:
        raw = record.get("model_output", "")
        try:
            parsed = json.loads(raw)
        except (json.JSONDecodeError, TypeError):
            return set(), set(), set()

    entities = parsed.get("entities", [])
    relations = parsed.get("relations", [])

    et_violations = set()
    rv_violations = set()
    dr_violations = set()

    for ent in entities:
        etype = ent.get("type", "")
        if etype.upper() not in VALID_ENTITY_TYPES:
            et_violations.add(ent.get("text", "") + "::" + etype)

    for i, rel in enumerate(relations):
        rel_type = rel.get("type", "")
        h_type = rel.get("head_type", "").upper()
        t_type = rel.get("tail_type", "").upper()

        rel_key = name_to_id.get(rel_type.lower().strip())
        if rel_key is None:
            rv_violations.add(f"{i}:{rel_type}")
            continue

        allowed = rel_constraints_map.get(rel_key, [])
        if allowed:
            pair_ok = any(
                h_type == p.get("head", "").upper() and t_type == p.get("tail", "").upper()
                for p in allowed
            )
            if not pair_ok:
                dr_violations.add(f"{i}:{rel_key}:{h_type}:{t_type}")

    return et_violations, rv_violations, dr_violations


def mcnemar_test(flags_a, flags_b):
    """McNemar test on paired binary outcomes.

    flags_a, flags_b: lists of 0/1 (0=no violation, 1=has violation), same length.
    Returns: chi2 statistic, p-value, contingency table (b, c, n).
    """
    assert len(flags_a) == len(flags_b), "Mismatched sample counts"
    b = sum(1 for a, bb in zip(flags_a, flags_b) if a == 1 and bb == 0)
    c = sum(1 for a, bb in zip(flags_a, flags_b) if a == 0 and bb == 1)
    n = len(flags_a)

    if b + c == 0:
        return 0.0, 1.0, {"b_only_A": b, "c_only_B": c, "n": n}

    try:
        from scipy.stats import chi2 as chi2_dist
        chi2 = (abs(b - c) - 1) ** 2 / (b + c)
        p_value = 1 - chi2_dist.cdf(chi2, df=1)
    except ImportError:
        chi2 = (abs(b - c) - 1) ** 2 / (b + c)
        p_value = _chi2_survival(chi2, 1)

    return round(chi2, 4), round(p_value, 6), {"b_only_A": b, "c_only_B": c, "n": n}


def _chi2_survival(x, df):
    """Approximate chi2 survival function (p-value) for df=1 without scipy."""
    import math
    if x <= 0:
        return 1.0
    z = math.sqrt(x)
    t = 1.0 / (1.0 + 0.2316419 * z)
    d = 0.3989422804014327
    p = d * math.exp(-z * z / 2.0) * (
        t * (0.3193815 + t * (-0.3565638 + t * (1.781478 + t * (-1.821256 + t * 1.330274))))
    )
    return 2 * p


def run_mcnemar(raw_a_path, raw_b_path, constraints_path, dataset):
    records_a = load_jsonl(raw_a_path)
    records_b = load_jsonl(raw_b_path)

    with open(constraints_path) as f:
        constraints = json.load(f)

    check_fn = _check_scierc_sample if dataset == "scierc" else _check_docred_sample

    map_a = {}
    for r in records_a:
        doc_id = r.get("doc_id", r.get("id", ""))
        map_a[doc_id] = r

    map_b = {}
    for r in records_b:
        doc_id = r.get("doc_id", r.get("id", ""))
        map_b[doc_id] = r

    common_ids = sorted(set(map_a.keys()) & set(map_b.keys()))
    if not common_ids:
        return {"error": "No overlapping doc_ids between the two outputs"}

    violation_types = ["entity_type", "relation_vocabulary", "domain_range", "any"]
    flags = {vt: {"a": [], "b": []} for vt in violation_types}

    for doc_id in common_ids:
        et_a, rv_a, dr_a = check_fn(map_a[doc_id], constraints)
        et_b, rv_b, dr_b = check_fn(map_b[doc_id], constraints)

        flags["entity_type"]["a"].append(1 if et_a else 0)
        flags["entity_type"]["b"].append(1 if et_b else 0)
        flags["relation_vocabulary"]["a"].append(1 if rv_a else 0)
        flags["relation_vocabulary"]["b"].append(1 if rv_b else 0)
        flags["domain_range"]["a"].append(1 if dr_a else 0)
        flags["domain_range"]["b"].append(1 if dr_b else 0)
        any_a = 1 if (et_a or rv_a or dr_a) else 0
        any_b = 1 if (et_b or rv_b or dr_b) else 0
        flags["any"]["a"].append(any_a)
        flags["any"]["b"].append(any_b)

    results = {"n_common_samples": len(common_ids)}
    for vt in violation_types:
        chi2, p, table = mcnemar_test(flags[vt]["a"], flags[vt]["b"])
        rate_a = sum(flags[vt]["a"]) / len(common_ids)
        rate_b = sum(flags[vt]["b"]) / len(common_ids)
        results[vt] = {
            "sample_violation_rate_A": round(rate_a, 4),
            "sample_violation_rate_B": round(rate_b, 4),
            "delta": round(rate_b - rate_a, 4),
            "mcnemar_chi2": chi2,
            "mcnemar_p_value": p,
            "significant_0.05": p < 0.05,
            "contingency": table,
        }

    return results


# ── Output formatting ───────────────────────────────────────────────────


def format_text_summary(summary_rows, relation_rows, mcnemar_results, label_a, label_b):
    lines = []
    lines.append(f"{'='*70}")
    lines.append(f"  Prompt Comparison: {label_a} vs {label_b}")
    lines.append(f"{'='*70}")

    lines.append(f"\n{'Metric':<35} {label_a:>10} {label_b:>10} {'Delta':>10} {'%Chg':>8}")
    lines.append("-" * 75)
    for r in summary_rows:
        va = r[label_a]
        vb = r[label_b]
        if isinstance(va, float) and va < 1:
            va_s = f"{va:.4f}"
            vb_s = f"{vb:.4f}"
            d_s = f"{r['delta']:+.4f}"
        else:
            va_s = f"{va}"
            vb_s = f"{vb}"
            d_s = f"{r['delta']:+g}"

        improved = r.get("improved")
        marker = ""
        if improved is True:
            marker = " *"
        elif improved is False:
            marker = " !"

        pct = f"{r['pct_change']:+.1f}%" if abs(r['pct_change']) < 1e6 else "N/A"
        lines.append(f"{r['metric']:<35} {va_s:>10} {vb_s:>10} {d_s:>10} {pct:>8}{marker}")

    lines.append(f"\n{'─'*70}")
    lines.append("Per-Relation Domain/Range Violation Rates:")
    lines.append(f"{'Relation':<20} {label_a+' rate':>12} {label_b+' rate':>12} {'Delta':>10} {'Dir':>5}")
    lines.append("-" * 60)
    for r in relation_rows:
        ra = r[f"rate_{label_a}"]
        rb = r[f"rate_{label_b}"]
        d = r["delta"]
        direction = "v" if d < 0 else ("^" if d > 0 else "=")
        lines.append(
            f"{r['relation']:<20} {ra:>11.4f} {rb:>11.4f} {d:>+10.4f} {direction:>5}"
        )

    if mcnemar_results and "error" not in mcnemar_results:
        lines.append(f"\n{'─'*70}")
        lines.append(f"McNemar Test (paired, n={mcnemar_results['n_common_samples']} common samples):")
        lines.append(f"{'Violation Type':<25} {'Rate A':>8} {'Rate B':>8} {'Delta':>8} {'chi2':>8} {'p':>10} {'Sig?':>5}")
        lines.append("-" * 75)
        for vt in ["entity_type", "relation_vocabulary", "domain_range", "any"]:
            if vt not in mcnemar_results:
                continue
            m = mcnemar_results[vt]
            sig = "YES" if m["significant_0.05"] else "no"
            lines.append(
                f"{vt:<25} {m['sample_violation_rate_A']:>7.4f} "
                f"{m['sample_violation_rate_B']:>7.4f} "
                f"{m['delta']:>+7.4f} "
                f"{m['mcnemar_chi2']:>8.2f} "
                f"{m['mcnemar_p_value']:>10.6f} "
                f"{sig:>5}"
            )

    lines.append(f"\n{'='*70}")
    lines.append("* = improved (rate decreased), ! = regressed (rate increased)")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Compare violation reports across prompt strategies")
    parser.add_argument("--report_a", type=str, required=True, help="Violation report JSON for prompt A")
    parser.add_argument("--report_b", type=str, required=True, help="Violation report JSON for prompt B")
    parser.add_argument("--label_a", type=str, default="prompt_A")
    parser.add_argument("--label_b", type=str, default="prompt_B")
    parser.add_argument("--raw_a", type=str, default=None, help="Raw output JSONL for prompt A (for McNemar)")
    parser.add_argument("--raw_b", type=str, default=None, help="Raw output JSONL for prompt B (for McNemar)")
    parser.add_argument("--constraints", type=str, default=None, help="Ontology constraints JSON (for McNemar)")
    parser.add_argument("--dataset", type=str, choices=["scierc", "docred"], default="scierc")
    parser.add_argument("--output", type=str, default=None, help="Output JSON path")
    args = parser.parse_args()

    report_a = load_report(args.report_a)
    report_b = load_report(args.report_b)

    summary_rows = compare_summaries(report_a, report_b, args.label_a, args.label_b)
    relation_rows = compare_per_relation(report_a, report_b, args.label_a, args.label_b)

    mcnemar_results = None
    if args.raw_a and args.raw_b and args.constraints:
        mcnemar_results = run_mcnemar(args.raw_a, args.raw_b, args.constraints, args.dataset)

    text = format_text_summary(summary_rows, relation_rows, mcnemar_results, args.label_a, args.label_b)
    print(text)

    output_data = {
        "comparison": {
            "label_a": args.label_a,
            "label_b": args.label_b,
            "dataset": args.dataset,
        },
        "summary_comparison": summary_rows,
        "per_relation_comparison": relation_rows,
    }
    if mcnemar_results:
        output_data["mcnemar_test"] = mcnemar_results

    output_path = args.output or f"outputs/comparison_{args.label_a}_vs_{args.label_b}.json"
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    print(f"\nJSON report saved to {output_path}")


if __name__ == "__main__":
    main()

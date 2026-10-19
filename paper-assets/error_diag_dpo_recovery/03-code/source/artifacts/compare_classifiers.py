#!/usr/bin/env python3
"""Compare classification results from multiple classifiers.

Reads JSONL outputs from different classification methods and produces:
1. Distribution comparison table
2. Pairwise agreement matrix (Cohen's kappa)
3. P1 analysis (correction span by error type) for each method
4. Consensus classification (majority vote)

Usage:
    python src/compare_classifiers.py \
        --files outputs/v6_classified_llm.jsonl outputs/v6_classified_rulebased.jsonl \
        --labels "LLM" "RuleBased" \
        --output outputs/v6_classifier_comparison.json
"""

import argparse
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path
from statistics import mean, median, stdev


ERROR_TYPES = ["action", "verification", "planning"]


def normalize_game_file(game_file: str) -> str:
    m = re.search(r"(task_\d+)", game_file)
    return m.group(1) if m else game_file.strip().lower()


def load_classified(path: str) -> dict[str, dict]:
    records = {}
    for line in open(path):
        line = line.strip()
        if not line:
            continue
        r = json.loads(line)
        key = normalize_game_file(r.get("game_file", r.get("task_id", "")))
        records[key] = r
    return records


# ── Distribution ──────────────────────────────────────────────

def compute_distribution(records: dict[str, dict]) -> dict:
    types = [r.get("error_type", "unknown") for r in records.values()]
    counts = Counter(types)
    total = len(types)
    dist = {}
    for et in ERROR_TYPES + sorted(set(counts.keys()) - set(ERROR_TYPES)):
        n = counts.get(et, 0)
        dist[et] = {"n": n, "pct": round(100 * n / total, 1) if total else 0}
    return {"total": total, "distribution": dist}


# ── Cohen's Kappa ─────────────────────────────────────────────

def cohens_kappa(labels_a: list[str], labels_b: list[str]) -> float:
    assert len(labels_a) == len(labels_b)
    n = len(labels_a)
    if n == 0:
        return 0.0
    all_labels = sorted(set(labels_a) | set(labels_b))
    agree = sum(1 for a, b in zip(labels_a, labels_b) if a == b)
    p_o = agree / n
    p_e = sum(
        (labels_a.count(c) / n) * (labels_b.count(c) / n)
        for c in all_labels
    )
    if p_e == 1.0:
        return 1.0
    return round((p_o - p_e) / (1.0 - p_e), 4)


def pairwise_agreement(all_records: dict[str, dict[str, dict]], labels: list[str]):
    keys = set.intersection(*(set(all_records[lb].keys()) for lb in labels))
    matrix = {}
    for i, la in enumerate(labels):
        for lb in labels[i + 1:]:
            types_a = [all_records[la][k].get("error_type", "?") for k in keys]
            types_b = [all_records[lb][k].get("error_type", "?") for k in keys]
            agree = sum(1 for a, b in zip(types_a, types_b) if a == b)
            kappa = cohens_kappa(types_a, types_b)
            matrix[f"{la} vs {lb}"] = {
                "n": len(keys),
                "agree": agree,
                "agree_pct": round(100 * agree / len(keys), 1) if keys else 0,
                "kappa": kappa,
            }
    return matrix


# ── P1 Analysis ───────────────────────────────────────────────

def p1_analysis(records: dict[str, dict], label: str) -> dict:
    from scipy.stats import kruskal as kruskal_test

    recs = list(records.values())
    groups = {}
    for et in ERROR_TYPES:
        spans = [r["correction_span"] for r in recs
                 if r.get("error_type") == et and "correction_span" in r]
        if spans:
            groups[et] = {
                "n": len(spans),
                "mean": round(mean(spans), 2),
                "median": round(median(spans), 2),
                "std": round(stdev(spans), 2) if len(spans) > 1 else 0.0,
                "_spans": spans,
            }

    valid = [g for g in groups.values() if g["n"] >= 3]
    kw_h, kw_p = None, None
    if len(valid) >= 2:
        h, p = kruskal_test(*[g["_spans"] for g in valid])
        kw_h, kw_p = round(float(h), 4), round(float(p), 6)

    medians = {et: groups[et]["median"] for et in ERROR_TYPES if et in groups}
    ordinal = None
    if len(medians) == 3:
        ordinal = medians["action"] < medians["verification"] < medians["planning"]

    # Dedup by game_file
    rng = random.Random(42)
    by_task: dict[str, list] = {}
    for r in recs:
        key = normalize_game_file(r.get("game_file", ""))
        by_task.setdefault(key, []).append(r)
    deduped = [rng.choice(v) for v in by_task.values()]

    groups_d = {}
    for et in ERROR_TYPES:
        spans = [r["correction_span"] for r in deduped
                 if r.get("error_type") == et and "correction_span" in r]
        if spans:
            groups_d[et] = {
                "n": len(spans),
                "mean": round(mean(spans), 2),
                "median": round(median(spans), 2),
                "std": round(stdev(spans), 2) if len(spans) > 1 else 0.0,
            }

    kw_h_d, kw_p_d = None, None
    valid_d = [et for et in ERROR_TYPES if et in groups_d and groups_d[et]["n"] >= 3]
    if len(valid_d) >= 2:
        spans_list = [[r["correction_span"] for r in deduped
                       if r.get("error_type") == et] for et in valid_d]
        h, p = kruskal_test(*spans_list)
        kw_h_d, kw_p_d = round(float(h), 4), round(float(p), 6)

    clean_groups = {et: {k: v for k, v in g.items() if k != "_spans"}
                    for et, g in groups.items()}

    return {
        "label": label,
        "full": {
            "n": len(recs),
            "groups": clean_groups,
            "kruskal_h": kw_h, "kruskal_p": kw_p,
            "ordinal_holds": ordinal,
        },
        "dedup": {
            "n": len(deduped),
            "groups": groups_d,
            "kruskal_h": kw_h_d, "kruskal_p": kw_p_d,
        },
    }


# ── Majority Vote ─────────────────────────────────────────────

def majority_vote(all_records: dict[str, dict[str, dict]], labels: list[str]) -> dict:
    keys = set.intersection(*(set(all_records[lb].keys()) for lb in labels))
    consensus = {}
    disagreements = []
    for k in sorted(keys):
        votes = [all_records[lb][k].get("error_type", "unknown") for lb in labels]
        counts = Counter(votes)
        winner, win_count = counts.most_common(1)[0]
        consensus[k] = {
            "consensus_type": winner,
            "votes": dict(zip(labels, votes)),
            "unanimous": len(set(votes)) == 1,
        }
        if len(set(votes)) > 1:
            disagreements.append({"game_file": k, **consensus[k]})

    unanimous = sum(1 for v in consensus.values() if v["unanimous"])
    return {
        "total": len(keys),
        "unanimous": unanimous,
        "unanimous_pct": round(100 * unanimous / len(keys), 1) if keys else 0,
        "disagreements": disagreements,
        "consensus_distribution": dict(Counter(
            v["consensus_type"] for v in consensus.values()
        )),
    }


# ── Per-task detail ───────────────────────────────────────────

def per_task_detail(all_records: dict[str, dict[str, dict]], labels: list[str]) -> list[dict]:
    keys = set.intersection(*(set(all_records[lb].keys()) for lb in labels))
    rows = []
    for k in sorted(keys):
        row = {"game_file": k}
        for lb in labels:
            r = all_records[lb][k]
            row[f"{lb}_type"] = r.get("error_type", "?")
            row[f"{lb}_span"] = r.get("correction_span", None)
        rows.append(row)
    return rows


# ── Pretty Print ──────────────────────────────────────────────

def print_report(distributions, agreement, p1_results, vote_result, labels):
    print("\n" + "=" * 70)
    print("CLASSIFIER COMPARISON REPORT")
    print("=" * 70)

    # Distribution table
    print("\n── Distribution ─────────────────────────────────────")
    header = f"{'Type':<16s}" + "".join(f"{lb:>16s}" for lb in labels)
    print(header)
    print("-" * len(header))
    for et in ERROR_TYPES + ["unknown"]:
        row = f"{et:<16s}"
        for lb in labels:
            d = distributions[lb]["distribution"].get(et, {"n": 0, "pct": 0})
            row += f"{d['n']:>6d} ({d['pct']:>5.1f}%)"
        print(row)
    totals = f"{'TOTAL':<16s}"
    for lb in labels:
        totals += f"{distributions[lb]['total']:>6d}        "
    print(totals)

    # Agreement matrix
    print("\n── Pairwise Agreement ───────────────────────────────")
    for pair, stats in agreement.items():
        print(f"  {pair}: {stats['agree']}/{stats['n']} "
              f"({stats['agree_pct']:.1f}%) κ={stats['kappa']:.4f}")

    # P1 analysis per method
    print("\n── P1 Correction Span Analysis ──────────────────────")
    for res in p1_results:
        lb = res["label"]
        full = res["full"]
        print(f"\n  [{lb}] N={full['n']}")
        for et in ERROR_TYPES:
            if et in full["groups"]:
                g = full["groups"][et]
                print(f"    {et:<16s} N={g['n']:>3d}, mean={g['mean']:.2f}, "
                      f"median={g['median']:.1f}, std={g['std']:.2f}")
            else:
                print(f"    {et:<16s} N=  0")
        if full["kruskal_h"] is not None:
            print(f"    KW: H={full['kruskal_h']:.4f}, p={full['kruskal_p']:.6f}")
            ord_str = "✓" if full["ordinal_holds"] else "✗"
            print(f"    Ordinal (a < v < p): {ord_str}")
        else:
            print(f"    KW: SKIPPED (need >=2 groups with n>=3)")

    # Majority vote
    print("\n── Consensus (Majority Vote) ────────────────────────")
    print(f"  Total: {vote_result['total']}, "
          f"Unanimous: {vote_result['unanimous']} ({vote_result['unanimous_pct']:.1f}%)")
    print(f"  Consensus distribution: {vote_result['consensus_distribution']}")
    if vote_result["disagreements"]:
        print(f"\n  Disagreements ({len(vote_result['disagreements'])}):")
        for d in vote_result["disagreements"][:20]:
            votes_str = ", ".join(f"{k}={v}" for k, v in d["votes"].items())
            print(f"    {d['game_file']}: {votes_str} -> {d['consensus_type']}")
        if len(vote_result["disagreements"]) > 20:
            print(f"    ... and {len(vote_result['disagreements']) - 20} more")


# ── Main ──────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Compare classification results from multiple classifiers")
    parser.add_argument("--files", nargs="+", required=True,
                        help="JSONL files from different classifiers")
    parser.add_argument("--labels", nargs="+", required=True,
                        help="Labels for each classifier (same order as --files)")
    parser.add_argument("--output", default=None,
                        help="Output JSON path for comparison results")
    args = parser.parse_args()

    if len(args.files) != len(args.labels):
        print(f"ERROR: {len(args.files)} files but {len(args.labels)} labels", file=sys.stderr)
        sys.exit(1)

    # Load all
    all_records: dict[str, dict[str, dict]] = {}
    for path, label in zip(args.files, args.labels):
        if not Path(path).exists():
            print(f"WARNING: {path} not found, skipping {label}", file=sys.stderr)
            continue
        all_records[label] = load_classified(path)
        print(f"Loaded {label}: {len(all_records[label])} records from {path}")

    labels = [lb for lb in args.labels if lb in all_records]
    if len(labels) < 2:
        print("ERROR: need at least 2 classifier outputs to compare", file=sys.stderr)
        sys.exit(1)

    # Compute
    distributions = {lb: compute_distribution(all_records[lb]) for lb in labels}
    agreement = pairwise_agreement(all_records, labels)
    p1_results = [p1_analysis(all_records[lb], lb) for lb in labels]
    vote_result = majority_vote(all_records, labels)
    detail = per_task_detail(all_records, labels)

    # Print
    print_report(distributions, agreement, p1_results, vote_result, labels)

    # Save JSON
    output = {
        "labels": labels,
        "distributions": distributions,
        "pairwise_agreement": agreement,
        "p1_analysis": {r["label"]: r for r in p1_results},
        "consensus": vote_result,
        "per_task_detail": detail,
    }

    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        print(f"\nSaved comparison to {args.output}")

    # Final verdict
    print("\n── P1 Gate Summary ─────────────────────────────────")
    for res in p1_results:
        lb = res["label"]
        f = res["full"]
        sig = f["kruskal_p"] is not None and f["kruskal_p"] < 0.05
        ord_ok = f["ordinal_holds"] is True
        status = "PASS" if (sig and ord_ok) else "FAIL"
        p_str = f"p={f['kruskal_p']:.6f}" if f["kruskal_p"] is not None else "p=N/A"
        o_str = "✓" if ord_ok else "✗"
        print(f"  {lb:<16s} KW {p_str}, ordinal {o_str} => {status}")


if __name__ == "__main__":
    main()

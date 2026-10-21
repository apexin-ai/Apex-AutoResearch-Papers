#!/usr/bin/env python3
"""Phase 4: Compute inter-annotator agreement, prevalence, and type distribution.

Usage:
    python compute_stats.py

Reads: annotations_claude.jsonl, annotations_gpt.jsonl, clauses.jsonl
Writes: analysis_report.md
"""

import json
import os
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

BASE_DIR = Path(__file__).parent
CLAUSES_FILE = BASE_DIR / "clauses.jsonl"
CLAUDE_FILE = BASE_DIR / "annotations_claude.jsonl"
GPT_FILE = BASE_DIR / "annotations_gpt.jsonl"
REPORT_FILE = BASE_DIR / "analysis_report.md"

AMBIGUITY_TYPES = [
    "scopal", "lexical", "coreferential",
    "incompleteness", "authorization_scope", "conditional_precedence",
]


def load_jsonl(path):
    records = {}
    with open(path) as f:
        for line in f:
            rec = json.loads(line)
            records[rec["clause_id"]] = rec
    return records


def cohens_kappa(labels1, labels2):
    """Compute Cohen's kappa for two lists of labels."""
    assert len(labels1) == len(labels2)
    n = len(labels1)
    if n == 0:
        return 0.0

    all_labels = sorted(set(labels1) | set(labels2))
    label_to_idx = {l: i for i, l in enumerate(all_labels)}
    k = len(all_labels)

    confusion = np.zeros((k, k), dtype=int)
    for a, b in zip(labels1, labels2):
        confusion[label_to_idx[a], label_to_idx[b]] += 1

    po = np.trace(confusion) / n
    row_sums = confusion.sum(axis=1)
    col_sums = confusion.sum(axis=0)
    pe = (row_sums * col_sums).sum() / (n * n)

    if pe == 1.0:
        return 1.0
    return (po - pe) / (1 - pe)


def bootstrap_ci(values, n_boot=10000, ci=0.95, rng=None):
    """Bootstrap confidence interval for the mean."""
    if rng is None:
        rng = np.random.default_rng(42)
    values = np.array(values)
    n = len(values)
    boot_means = np.array([
        rng.choice(values, size=n, replace=True).mean()
        for _ in range(n_boot)
    ])
    alpha = (1 - ci) / 2
    lo = np.percentile(boot_means, alpha * 100)
    hi = np.percentile(boot_means, (1 - alpha) * 100)
    return float(lo), float(hi)


def main():
    # Load data
    clauses_data = load_jsonl(CLAUSES_FILE)
    claude_ann = load_jsonl(CLAUDE_FILE)
    gpt_ann = load_jsonl(GPT_FILE)

    # Align annotations
    common_ids = sorted(set(claude_ann.keys()) & set(gpt_ann.keys()))
    print(f"Common annotations: {len(common_ids)} / {len(clauses_data)} clauses")

    # ---- 1. Inter-annotator agreement ----
    claude_binary = [claude_ann[cid]["is_ambiguous"] for cid in common_ids]
    gpt_binary = [gpt_ann[cid]["is_ambiguous"] for cid in common_ids]

    kappa_binary = cohens_kappa(
        [str(x) for x in claude_binary],
        [str(x) for x in gpt_binary],
    )

    # Per-type agreement (among clauses both judges marked ambiguous)
    both_ambiguous = [cid for cid in common_ids
                      if claude_ann[cid]["is_ambiguous"] and gpt_ann[cid]["is_ambiguous"]]
    if both_ambiguous:
        claude_types = [claude_ann[cid]["ambiguity_type"] for cid in both_ambiguous]
        gpt_types = [gpt_ann[cid]["ambiguity_type"] for cid in both_ambiguous]
        kappa_type = cohens_kappa(claude_types, gpt_types)
        type_agreement_pct = sum(a == b for a, b in zip(claude_types, gpt_types)) / len(both_ambiguous)
    else:
        kappa_type = 0.0
        type_agreement_pct = 0.0

    # ---- 2 & 3. Prevalence ----
    # Use "either judge" as ambiguous (union) for prevalence
    clause_ambiguous = {}
    clause_type = {}
    for cid in common_ids:
        c_amb = claude_ann[cid]["is_ambiguous"]
        g_amb = gpt_ann[cid]["is_ambiguous"]
        is_amb = c_amb or g_amb  # union
        clause_ambiguous[cid] = is_amb
        # For type: prefer agreed type, else Claude's
        if c_amb and g_amb and claude_ann[cid]["ambiguity_type"] == gpt_ann[cid]["ambiguity_type"]:
            clause_type[cid] = claude_ann[cid]["ambiguity_type"]
        elif c_amb:
            clause_type[cid] = claude_ann[cid]["ambiguity_type"]
        elif g_amb:
            clause_type[cid] = gpt_ann[cid]["ambiguity_type"]
        else:
            clause_type[cid] = "none"

    # Also compute "both judges agree" (intersection) version
    clause_ambiguous_both = {cid: claude_ann[cid]["is_ambiguous"] and gpt_ann[cid]["is_ambiguous"]
                             for cid in common_ids}

    # Build per-doc info
    doc_clauses = defaultdict(list)
    for cid in common_ids:
        doc_id = clauses_data[cid]["doc_id"]
        doc_clauses[doc_id].append(cid)

    # Company mapping
    doc_company = {cid: clauses_data[cid]["company"] for cid in common_ids}
    doc_domain = {cid: clauses_data[cid]["domain"] for cid in common_ids}

    # Document-level prevalence: >=1 ambiguous clause
    doc_has_ambiguity = {}
    doc_has_ambiguity_both = {}
    doc_ratios = {}
    doc_ratios_both = {}
    for doc_id, cids in doc_clauses.items():
        doc_has_ambiguity[doc_id] = any(clause_ambiguous[c] for c in cids)
        doc_has_ambiguity_both[doc_id] = any(clause_ambiguous_both[c] for c in cids)
        doc_ratios[doc_id] = sum(clause_ambiguous[c] for c in cids) / len(cids)
        doc_ratios_both[doc_id] = sum(clause_ambiguous_both[c] for c in cids) / len(cids)

    n_docs = len(doc_clauses)
    n_docs_amb = sum(doc_has_ambiguity.values())
    n_docs_amb_both = sum(doc_has_ambiguity_both.values())

    # Domain-level
    domain_docs = defaultdict(list)
    for doc_id in doc_clauses:
        d = clauses_data[list(doc_clauses[doc_id])[0]]["domain"]
        domain_docs[d].append(doc_id)

    # Clause-level prevalence
    total_clauses = len(common_ids)
    total_amb = sum(clause_ambiguous.values())
    total_amb_both = sum(clause_ambiguous_both.values())
    raw_rate = total_amb / total_clauses if total_clauses else 0
    raw_rate_both = total_amb_both / total_clauses if total_clauses else 0

    # Document-weighted
    doc_weighted = np.mean(list(doc_ratios.values())) if doc_ratios else 0
    doc_weighted_both = np.mean(list(doc_ratios_both.values())) if doc_ratios_both else 0

    # ---- 4. Company-level clustering + bootstrap CI ----
    company_docs = defaultdict(list)
    for doc_id in doc_clauses:
        company = clauses_data[list(doc_clauses[doc_id])[0]]["company"]
        company_docs[company].append(doc_id)

    company_rates = {}
    company_rates_both = {}
    for company, docs in company_docs.items():
        amb_count = sum(clause_ambiguous[c] for doc in docs for c in doc_clauses[doc])
        total = sum(len(doc_clauses[doc]) for doc in docs)
        company_rates[company] = amb_count / total if total else 0

        amb_count_both = sum(clause_ambiguous_both[c] for doc in docs for c in doc_clauses[doc])
        company_rates_both[company] = amb_count_both / total if total else 0

    company_rate_values = np.array(list(company_rates.values()))
    company_mean = company_rate_values.mean()
    ci_lo, ci_hi = bootstrap_ci(company_rate_values, n_boot=10000)

    company_rate_values_both = np.array(list(company_rates_both.values()))
    company_mean_both = company_rate_values_both.mean()
    ci_lo_both, ci_hi_both = bootstrap_ci(company_rate_values_both, n_boot=10000)

    # ---- 5. Type distribution ----
    type_counts_union = Counter()
    type_counts_both = Counter()
    for cid in common_ids:
        if clause_ambiguous[cid]:
            type_counts_union[clause_type[cid]] += 1
        if clause_ambiguous_both[cid]:
            # Use agreed type or Claude's
            if claude_ann[cid]["ambiguity_type"] == gpt_ann[cid]["ambiguity_type"]:
                type_counts_both[claude_ann[cid]["ambiguity_type"]] += 1
            else:
                type_counts_both[claude_ann[cid]["ambiguity_type"]] += 1

    # ---- Generate report ----
    lines = []
    lines.append("# Prevalence Audit: Analysis Report\n")
    lines.append(f"**Date**: 2026-05-23\n")
    lines.append(f"**Clauses analyzed**: {total_clauses} from {n_docs} documents ({len(company_docs)} companies)\n")

    lines.append("\n## 1. Inter-Annotator Agreement\n")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Cohen's κ (binary: ambiguous/not) | {kappa_binary:.3f} |")
    lines.append(f"| Cohen's κ (type, among agreed-ambiguous) | {kappa_type:.3f} |")
    lines.append(f"| Type exact agreement (among agreed-ambiguous) | {type_agreement_pct:.1%} |")
    lines.append(f"| Clauses both judges mark ambiguous | {len(both_ambiguous)} |")
    lines.append(f"| Claude marks ambiguous | {sum(claude_binary)} ({sum(claude_binary)/len(claude_binary):.1%}) |")
    lines.append(f"| GPT marks ambiguous | {sum(gpt_binary)} ({sum(gpt_binary)/len(gpt_binary):.1%}) |")

    lines.append("\n## 2. Document-Level Prevalence\n")
    lines.append(f"| Criterion | Docs with ≥1 ambiguity | Proportion |")
    lines.append(f"|-----------|----------------------|------------|")
    lines.append(f"| Either judge (union) | {n_docs_amb}/{n_docs} | {n_docs_amb/n_docs:.1%} |")
    lines.append(f"| Both judges (intersection) | {n_docs_amb_both}/{n_docs} | {n_docs_amb_both/n_docs:.1%} |")

    lines.append("\n### By Domain\n")
    lines.append(f"| Domain | Docs | Union | Intersection |")
    lines.append(f"|--------|------|-------|-------------|")
    for domain in ["airline", "retail"]:
        d_docs = domain_docs.get(domain, [])
        d_amb = sum(doc_has_ambiguity[d] for d in d_docs)
        d_amb_both = sum(doc_has_ambiguity_both[d] for d in d_docs)
        lines.append(f"| {domain} | {len(d_docs)} | {d_amb}/{len(d_docs)} ({d_amb/len(d_docs):.1%}) | {d_amb_both}/{len(d_docs)} ({d_amb_both/len(d_docs):.1%}) |")

    lines.append("\n## 3. Clause-Level Prevalence\n")
    lines.append(f"| Metric | Union | Intersection |")
    lines.append(f"|--------|-------|-------------|")
    lines.append(f"| Raw (ambiguous/total) | {total_amb}/{total_clauses} ({raw_rate:.1%}) | {total_amb_both}/{total_clauses} ({raw_rate_both:.1%}) |")
    lines.append(f"| Document-weighted mean | {doc_weighted:.1%} | {doc_weighted_both:.1%} |")

    lines.append("\n### By Domain (raw)\n")
    lines.append(f"| Domain | Total | Ambiguous (union) | Rate |")
    lines.append(f"|--------|-------|-------------------|------|")
    for domain in ["airline", "retail"]:
        d_cids = [cid for cid in common_ids if doc_domain[cid] == domain]
        d_amb = sum(clause_ambiguous[c] for c in d_cids)
        lines.append(f"| {domain} | {len(d_cids)} | {d_amb} | {d_amb/len(d_cids):.1%} |")

    lines.append("\n## 4. Company-Level Analysis\n")
    lines.append(f"| Company | Domain | Clauses | Ambig (union) | Rate | Ambig (inter) | Rate |")
    lines.append(f"|---------|--------|---------|--------------|------|--------------|------|")
    for company in sorted(company_docs.keys()):
        docs = company_docs[company]
        total = sum(len(doc_clauses[d]) for d in docs)
        amb = sum(clause_ambiguous[c] for d in docs for c in doc_clauses[d])
        amb_b = sum(clause_ambiguous_both[c] for d in docs for c in doc_clauses[d])
        domain = clauses_data[list(doc_clauses[docs[0]])[0]]["domain"]
        lines.append(f"| {company} | {domain} | {total} | {amb} | {amb/total:.1%} | {amb_b} | {amb_b/total:.1%} |")

    lines.append(f"\n**Company-level bootstrap 95% CI (N=9 companies, B=10,000)**:")
    lines.append(f"- Union: mean = {company_mean:.1%}, 95% CI = [{ci_lo:.1%}, {ci_hi:.1%}]")
    lines.append(f"- Intersection: mean = {company_mean_both:.1%}, 95% CI = [{ci_lo_both:.1%}, {ci_hi_both:.1%}]")

    lines.append("\n## 5. Type Distribution\n")
    lines.append(f"| Ambiguity Type | Count (union) | % of ambiguous | Count (intersection) | % of ambiguous |")
    lines.append(f"|---------------|--------------|----------------|---------------------|----------------|")
    for t in AMBIGUITY_TYPES:
        cu = type_counts_union.get(t, 0)
        cb = type_counts_both.get(t, 0)
        pu = cu / total_amb * 100 if total_amb else 0
        pb = cb / total_amb_both * 100 if total_amb_both else 0
        lines.append(f"| {t} | {cu} | {pu:.1f}% | {cb} | {pb:.1f}% |")

    report = "\n".join(lines) + "\n"
    REPORT_FILE.write_text(report)
    print(f"Report written to {REPORT_FILE}")
    print(f"\nKey results:")
    print(f"  Cohen's κ (binary): {kappa_binary:.3f}")
    print(f"  Clause-level prevalence (union): {raw_rate:.1%}")
    print(f"  Company-level mean (union): {company_mean:.1%}, 95% CI [{ci_lo:.1%}, {ci_hi:.1%}]")


if __name__ == "__main__":
    main()

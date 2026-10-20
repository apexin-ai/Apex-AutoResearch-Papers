# Prevalence Audit: Analysis Report

**Date**: 2026-05-23

**Clauses analyzed**: 407 from 24 documents (9 companies)


## 1. Inter-Annotator Agreement

| Metric | Value |
|--------|-------|
| Cohen's κ (binary: ambiguous/not) | 0.295 |
| Cohen's κ (type, among agreed-ambiguous) | 0.382 |
| Type exact agreement (among agreed-ambiguous) | 58.4% |
| Clauses both judges mark ambiguous | 226 |
| Claude marks ambiguous | 341 (83.8%) |
| GPT marks ambiguous | 238 (58.5%) |

## 2. Document-Level Prevalence

| Criterion | Docs with ≥1 ambiguity | Proportion |
|-----------|----------------------|------------|
| Either judge (union) | 24/24 | 100.0% |
| Both judges (intersection) | 24/24 | 100.0% |

### By Domain

| Domain | Docs | Union | Intersection |
|--------|------|-------|-------------|
| airline | 13 | 13/13 (100.0%) | 13/13 (100.0%) |
| retail | 11 | 11/11 (100.0%) | 11/11 (100.0%) |

## 3. Clause-Level Prevalence

| Metric | Union | Intersection |
|--------|-------|-------------|
| Raw (ambiguous/total) | 353/407 (86.7%) | 226/407 (55.5%) |
| Document-weighted mean | 89.1% | 58.7% |

### By Domain (raw)

| Domain | Total | Ambiguous (union) | Rate |
|--------|-------|-------------------|------|
| airline | 250 | 217 | 86.8% |
| retail | 157 | 136 | 86.6% |

## 4. Company-Level Analysis

| Company | Domain | Clauses | Ambig (union) | Rate | Ambig (inter) | Rate |
|---------|--------|---------|--------------|------|--------------|------|
| Apple | retail | 43 | 39 | 90.7% | 22 | 51.2% |
| Delta | airline | 65 | 57 | 87.7% | 34 | 52.3% |
| Emirates | airline | 19 | 19 | 100.0% | 15 | 78.9% |
| Frontier | airline | 85 | 73 | 85.9% | 45 | 52.9% |
| IKEA | retail | 71 | 60 | 84.5% | 37 | 52.1% |
| Nordstrom | retail | 11 | 7 | 63.6% | 7 | 63.6% |
| Southwest | airline | 81 | 68 | 84.0% | 44 | 54.3% |
| Target | retail | 12 | 11 | 91.7% | 9 | 75.0% |
| Zappos | retail | 20 | 19 | 95.0% | 13 | 65.0% |

**Company-level bootstrap 95% CI (N=9 companies, B=10,000)**:
- Union: mean = 87.0%, 95% CI = [80.0%, 92.5%]
- Intersection: mean = 60.6%, 95% CI = [54.8%, 67.6%]

## 5. Type Distribution

| Ambiguity Type | Count (union) | % of ambiguous | Count (intersection) | % of ambiguous |
|---------------|--------------|----------------|---------------------|----------------|
| scopal | 47 | 13.3% | 24 | 10.6% |
| lexical | 36 | 10.2% | 28 | 12.4% |
| coreferential | 9 | 2.5% | 6 | 2.7% |
| incompleteness | 221 | 62.6% | 139 | 61.5% |
| authorization_scope | 7 | 2.0% | 3 | 1.3% |
| conditional_precedence | 33 | 9.3% | 26 | 11.5% |

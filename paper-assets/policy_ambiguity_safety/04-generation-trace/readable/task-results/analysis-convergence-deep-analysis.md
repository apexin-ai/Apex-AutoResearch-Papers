# analysis convergence deep analysis

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_convergence_deep_analysis_20260523T053348_result.json`
- **Structured JSON:** [`c66ed21bfe26130f3a2b.json`](../../sessions/c6/c66ed21bfe26130f3a2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All deliverables generated. Here's the summary:

---

## Results

### Analysis 1: Attractor Pattern (Strong Finding)
- **77.0% of convergent violations are PERMISSIVE** (371/482), 17.6% restrictive, 5.4% literal
- Binomial test p < 0.001 — highly significant departure from uniform
- Per-type: permissive dominance holds in 5/6 types (>75%), but **cond_prec is the exception** — nearly 50/50 split between permissive (51.5%) and restrictive (47.1%)
- auth_scope is near-universal permissive (98.8%)
- coreferential has highest LITERAL rate (16.1%)

### Analysis 2: Type × Convergence Rate
- Incompleteness has highest convergent rate (0.62) and unanimous rate (0.24)
- Fisher's exact: incompleteness significantly higher unanimous rate than cond_prec (p=0.023) and coreferential (p=0.023)
- Mechanism group comparison: gap-filling (0.50) > boundary (0.44) > structural (0.35), χ²(2) = 5.993, p = 0.05

### Analysis 3: Non-Convergent Characteristics
- 92 divergent clauses, evenly distributed across types (χ² p=0.37)
- Clause length not significantly different (p=0.16)
- Model participation is **non-uniform** (χ² p=0.0017): deepseek-v3 (43) and qwen3-235b (28) are overrepresented in solo violations; gpt-4.1 (18) and claude-sonnet-4-6 (16) are most robust

### Output Files
- `artifacts/convergence_analysis/attractor_pattern.md` — Analysis 1 full breakdown
- `artifacts/convergence_analysis/type_convergence_matrix.csv` — Analysis 2 matrix
- `artifacts/convergence_analysis/non_convergent_analysis.md` — Analysis 3 results
- `artifacts/convergence_analysis/summary_report.md` — Integrated summary with paper integration suggestions
- `artifacts/convergence_analysis/attractor_raw_classifications.jsonl` — 482 GPT-4.1 classifications

---

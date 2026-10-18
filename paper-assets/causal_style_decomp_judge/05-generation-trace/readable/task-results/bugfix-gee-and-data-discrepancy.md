# bugfix gee and data discrepancy

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_gee-and-data-discrepancy_20260522T234122_result.json`
- **Structured JSON:** [`6d37292898a5a74e072b.json`](../../sessions/6d/6d37292898a5a74e072b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report written. Here's the summary:

---

### GEE Bug: Data artifact, NOT code bug

The identical `Style OR == Orig OR = 4.73` in `scored_mtbench_qwen32b_formality.jsonl` is caused by **response symmetry in casual-origin pairs**: among 11 casual pairs, exactly 9/11 chose A in both trials. This makes `is_style_in_A` and `is_original_in_A` structurally indistinguishable. Perturbation test confirms — flipping one trial response produces distinct ORs (6.08 vs 3.33). The primary analysis file (`pairwise_results_mtbench_qwen32b.jsonl`) doesn't have this issue (7/11 vs 8/11 → Style OR=2.96, Orig OR=4.51).

### Data Discrepancy: Three independent causes

| Metric | Table 1 | cross_benchmark (old) | Cause |
|--------|---------|----------------------|-------|
| BT | .712 | .700 | Different scoring runs + NLI filter (73 vs 80 pairs) |
| Likert p | .007 | .035 | Wilcoxon vs t-test (same data) |
| Likert d | .149 | .25 | Pooled-SD vs diff-SD denominator (same data) |

**Table 1 numbers are canonical** (from `mtbench_qwen32b_scoring.py`).

### Fixes applied to `cross_benchmark_analysis.py`
1. Added NLI≥0.90 filter to `load_pairwise()` (was missing)
2. Changed Likert test from t-test to Wilcoxon + pooled-SD Cohen's d (consistent with primary analysis)
3. Added VIF + correlation diagnostics to GEE output

Report saved to `/root/causal_style_decomp_judge/artifacts/r14_fixes/gee_bug_report.json`.

---

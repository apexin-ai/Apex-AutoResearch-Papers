# analysis w4 strategy count

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w4-strategy-count_20260520T133113_result.json`
- **Structured JSON:** [`802837faf3bb650164a3.json`](../../sessions/80/802837faf3bb650164a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the complete analysis.

---

## Strategy Count Verification

### Paper Claims
- Introduction (line 25): "More than twenty-five remediation strategies"
- Introduction (line 33): "Twenty-five+ remediation strategies fail"
- Analysis §5.5 (line 77): "more than twenty remediation strategies"
- Appendix Table 7 caption: "22+ distinct approaches"

### Explicitly Enumerated in Tables: **23 individual configurations**

**Table 5 (tab:remediation) — 9 prompt-level strategies:**

| # | Strategy | Target |
|---|----------|--------|
| 1 | Contrastive prompting | Prompt |
| 2 | Cross-model extraction (2 directions) | Architecture |
| 3 | Qwen3-14B extractor | Capability |
| 4 | Z3 feedback | Solver |
| 5 | Consistency filtering | Noise |
| 6 | Cross-trace UNSAT | Independence |
| 7 | T=1.0 | Diversity |
| 8 | Multi-temperature | Diversity |
| 9 | Discriminative filtering | Filtering |

**Table 6 (tab:method_interventions) — 3 method-level strategies:**

| # | Strategy | Target |
|---|----------|--------|
| 10 | ICG (Independent Constraint Generation) | Trace coupling |
| 11 | Contrastive scoring | Scoring bias |
| 12 | Debate | Role diversity |

**Table 7 (tab:additional_interventions) — 11 additional strategies:**

| # | Strategy | Target |
|---|----------|--------|
| 13 | PROVE (code verification) | Formal proof |
| 14 | CEGIS (iterative) | Consistency |
| 15 | DeepConf (logprob) | Confidence |
| 16 | Cross-model SICA | Independence |
| 17 | Problem perturbation | Trace diversity |
| 18 | MIN-UNSAT | Constraint selection |
| 19 | κ-aware SC | Weighted voting |
| 20 | Z3 trace filter | Quality |
| 21 | Bootstrapped gold | Self-improvement |
| 22 | Selective abstention | Confidence |
| 23 | ASCII perturbation | Format diversity |

### Unlisted strategies that close the gap to "25+":
- **ICL with gold FOL** — appears in Table 1 (main results) as a separate condition (Δ=+0.50, n.s.) but not numbered in remediation tables
- **Backward verification** — exp-045 in registry, not in any table
- **Cross-model extraction** counted as 2 directions (weak→strong, strong→weak) in Table 5 footnote

With these: 23 + 2 unlisted + 1 split = **26**, making the "25+" claim defensible.

### Distinct Strategy Families: **15 families**

| Family | Configs | Members |
|--------|---------|---------|
| 1. Contrastive/Pro-Con | 2 | #1 contrastive prompting, #11 contrastive scoring |
| 2. Cross-Model | 3 | #2 cross-model extraction (2 dirs), #16 cross-model SICA |
| 3. Stronger Extractor | 1 | #3 Qwen3-14B |
| 4. Solver Feedback/Objectives | 2 | #4 Z3 feedback, #18 MIN-UNSAT |
| 5. Constraint Filtering | 3 | #5 consistency filtering, #9 disc. filtering, #20 Z3 trace filter |
| 6. Cross-Trace Analysis | 1 | #6 cross-trace UNSAT |
| 7. Temperature/Diversity | 2 | #7 T=1.0, #8 multi-temp |
| 8. Independent Generation (ICG) | 1 | #10 |
| 9. Debate | 1 | #12 |
| 10. Code Verification | 1 | #13 PROVE |
| 11. Iterative Refinement | 2 | #14 CEGIS, #21 bootstrapped gold |
| 12. Confidence Filtering | 2 | #15 DeepConf, #22 selective abstention |
| 13. Input Perturbation | 2 | #17 problem perturbation, #23 ASCII perturbation |
| 14. Weighted Voting | 1 | #19 κ-aware SC |
| 15. ICL with Gold FOL | 1 | Table 1 condition (unlisted) |

### Registry Verification
- **76 experiments** with `conclusion=negative` in registry
- **0 experiments** with `conclusion=positive`
- The 76 experiments cover the 23 strategies plus many replication runs across seeds, datasets, and models (e.g., debate alone has exp-076, exp-078, exp-081, exp-084 for different dataset/seed combos)

### Summary
- **Individual configurations explicitly in tables: 23**
- **Including unlisted but documented: ~26** (supports "25+" claim)
- **Distinct strategy families: 15**
- **Registry negative experiments: 76** (replications across seeds/datasets/models)
- The intro's "25+" is defensible but slightly loose — the appendix's "22+" is more conservative and precisely matches the table-enumerated count. For the paper, recommend saying **"23 distinct strategies across 15 families"** or keeping "25+" if counting unlisted variants.

---

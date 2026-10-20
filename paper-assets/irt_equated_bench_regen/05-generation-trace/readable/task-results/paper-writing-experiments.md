# paper writing experiments

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_20260521T040002_result.json`
- **Structured JSON:** [`1f9620bcdd0edbb1d4d4.json`](../../sessions/1f/1f9620bcdd0edbb1d4d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiments section written to `paper/sections/experiments.tex`. Summary:

**8 subsections, 3 tables, 4 figures, ~2050 rendered words.**

- **§4.1** Validation: power analysis confirms TPR 0.68--0.80, FPR 0.036--0.042 at cohort sizes (1 paragraph, Appendix ref)
- **§4.2** Temporal comparability: 31.3% ETS C, BH FDR removes only 3 items, sanity 0.18%, ability-quintile 2.9%, within-family 61.3%, within-subject 38.1%, 92.4% unexplained by domain improvement, architecture non-issue, threshold-robust (Table 1)
- **§4.3** Ground truth mismatch: enrichment 0.96 vs Li et al., dose-response ΔTPR +0.508/+0.674, web-overlap = wrong ground truth (Figure 2)
- **§4.4** Structural analysis: three approaches fail to reduce FPR below 31% (Table 2)
- **§4.5** Semi-synthetic: cross-subject matching ΔFPR=0.000, within-subject inflates +0.186 (Figure 3)
- **§4.6** Q3 local independence: 11.3% vs 2.2% (5x, p=2.3e-9), mild contributing factor
- **§4.7** Downstream impact: four layers (ρ≈0.997 redundancy, signal concentration with circularity ablation, model-family diagnostics, cross-benchmark) (Figure 4)
- **§4.8** GSM8K: C%=18.9%, ΔTPR=+0.818, GSM1K r=−0.478 negative correlation honestly reported (Figure 5, Table 3)

---

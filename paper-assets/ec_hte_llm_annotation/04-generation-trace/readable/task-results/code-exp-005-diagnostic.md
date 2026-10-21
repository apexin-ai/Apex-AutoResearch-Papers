# code exp 005 diagnostic

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-005-diagnostic_20260520T232612_result.json`
- **Structured JSON:** [`9083c31bc5ade02a713c.json`](../../sessions/90/9083c31bc5ade02a713c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The plots look clean. Panel (C) shows strong subgroup-level ROC (AUC=0.826) and panel (D) shows the clear linear relationship between the signed product and observed bias increase (r=0.84).

The setting-level AUC (~0.47) is weak because the mean-bias label depends on factors beyond the DGP parameters (K, n_expert). The subgroup-level analysis is the right test of the theory.

Results summary:

- **Subgroup-level AUC = 0.833**: The signed product `(π̄ − π_s) × Δτ` strongly predicts which subgroups are harmed by global correction.
- **Correlation = 0.86** between signed product and observed bias increase.
- **84.6%** of low-π_s subgroups see global correction hurt; only **15.4%** of high-π_s subgroups do.
- **Setting-level AUC = 0.49**: The simple product doesn't cleanly predict the *average* effect across subgroups, because averaging masks subgroup-level damage.
- Theory alignment: the exp-002 formula correctly identifies the mechanism — global correction hurts at subgroups where misclassification is already low.

Script: `/home/ubuntu/ec_hte_llm_annotation/exp005_diagnostic_criterion.py`
Outputs: `results/exp005_diagnostic.csv`, `results/exp005_diagnostic_subgroups.csv`, `results/exp005_roc.png`

---

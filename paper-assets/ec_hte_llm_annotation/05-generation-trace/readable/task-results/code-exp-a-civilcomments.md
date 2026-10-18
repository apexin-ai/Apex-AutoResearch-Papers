# code exp a civilcomments

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-a-civilcomments_20260523T190133_result.json`
- **Structured JSON:** [`98e31a57c0fddde363eb.json`](../../sessions/98/98e31a57c0fddde363eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Both output files are saved.

**Key results:**

**Per-subgroup misclassification heterogeneity confirmed** across all 3 LLMs on demographic subgroups:
- ΔFPR ranges from 0.09 to 0.15 across subgroups (gender, no_identity, race_lgbtq, religion)
- κ ranges: gpt-4o [1.95, 2.38], gpt-4o-mini [2.24, 3.13], gpt-3.5-turbo [2.16, 2.94]
- race_lgbtq subgroup consistently has highest FPR across all models (0.38–0.63)

**Semi-synthetic DGP findings** (N=5000, τ(Z=1)=0.30, MC=50):
- **(a) Sign reversal**: Yes — 2% rate with stratified MLE at small n_expert (100–250) for gpt-4o-mini and gpt-3.5-turbo
- **(b) Bias amplification**: 1.03x–3.32x (stratified MLE vs naive). Worst at n_expert=100 with gpt-4o (3.32x). HB EC-HTE amplification up to 3.02x with gpt-4o-mini
- **(c) κ ranges**: 1.95–3.13 across all models/subgroups
- **(d) Asymmetric CMs** (especially gpt-4o-mini with FPR≈0.5–0.63) cause severe ill-conditioning, making EC-HTE correction worse than naive in all cases

**Output files:**
- `artifacts/civilcomments_analysis.csv` — per-subgroup confusion matrices
- `artifacts/civilcomments_report.md` — full report

---

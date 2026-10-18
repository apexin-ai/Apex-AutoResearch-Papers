# code loocv auc

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_loocv-auc_20260521T161839_result.json`
- **Structured JSON:** [`8aa363ce2c5c6fcdd192.json`](../../sessions/8a/8aa363ce2c5c6fcdd192.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Here's the summary:

**Key finding**: The old "LOSO-CV AUC = 0.83" was actually resubstitution AUC, mislabeled in `exp005_diagnostic_criterion.py` — the LOO loop only computed accuracy, not AUC.

**For the three fixed-formula diagnostics, LOO-CV AUC = resubstitution AUC** because diagnostic scores don't depend on other samples. This was confirmed by showing the logistic regression combined diagnostic (which does learn parameters) has LOO-CV AUC (0.830) < resubstitution AUC (0.888).

**Numbers for the paper** (49 settings, hb_wins label):

| Diagnostic | Setting AUC | Subgroup AUC |
|---|---|---|
| Δπ-only (Prop 2) | **0.889** | **0.865** |
| π CV | 0.968 | — |
| Δπ×Δτ (current) | 0.889 | 0.726 |

These are valid to report as-is, with a note that for deterministic diagnostics LOO-CV is identical to resubstitution.

**Output files**:
- `artifacts/diagnostic_revision/compute_loocv_auc.py` — computation script
- `artifacts/diagnostic_revision/loocv_auc_results.md` — full report
- `artifacts/diagnostic_revision/loocv_auc_summary.csv` — tabular results

---

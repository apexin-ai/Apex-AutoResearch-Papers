# analysis diagnostic revision auc

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_diagnostic-revision-auc_20260521T151105_result.json`
- **Structured JSON:** [`3474866aa2e6ca21f009.json`](../../sessions/34/3474866aa2e6ca21f009.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs generated. Summary of results:

**Setting-level AUC (49 settings, 7 with hb_wins=1):**

| Diagnostic | AUC | Needs Δτ? |
|---|---|---|
| π CV | **0.968** | No |
| Δπ-only (Prop 2) | **0.889** | No |
| Cond-number κ(M̂) | 0.855 | No |
| Δπ×Δτ (current) | 0.889 | Yes |

**Subgroup-level AUC (160 points, 36 with hb_wins=1):**

| Diagnostic | AUC | Needs Δτ? |
|---|---|---|
| Δπ-only (Prop 2) | **0.865** | No |
| Δπ×Δτ (current) | 0.726 | Yes |

**Bottom line**: The Δπ-only diagnostic matches Δπ×Δτ at the setting level (both 0.889) and substantially outperforms it at the subgroup level (0.865 vs 0.726). Δτ adds no discriminative power — the circular dependency is fully resolved. The π CV metric (0.968) is the best single-number predictor if a simpler alternative is preferred.

Output files in `artifacts/diagnostic_revision/`.

---

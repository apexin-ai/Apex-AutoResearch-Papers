# code plan 012 detection tool

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_012_detection_tool_20260521T080544_result.json`
- **Structured JSON:** [`824c343d14a68c824578.json`](../../sessions/82/824c343d14a68c824578.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All artifacts registered. Summary of results:

**Macro F1: 0.6322** (vs random 0.17, majority 0.11)

| Type | Precision | Recall | F1 |
|------|-----------|--------|-----|
| none (unambiguous) | 0.764 | 0.956 | 0.849 |
| conditional_precedence | 0.958 | 0.920 | **0.939** |
| scopal | 0.914 | 0.640 | 0.753 |
| authorization_scope | 1.000 | 0.360 | 0.529 |
| lexical | 0.356 | 0.420 | 0.385 |
| incompleteness | 0.481 | 0.260 | 0.338 |

**Binary detection**: F1=0.81, accuracy=0.83, FPR=0.044

Outputs:
- `detection_tool/detection_results.json` — full metrics
- `detection_tool/confusion_matrix.json` — 6×6 confusion matrix
- `detection_tool/predictions.jsonl` — 500 per-sample predictions
- `detection_tool/paper_paragraph.tex` — LaTeX paragraph (generated since F1 ≥ 0.60)

---

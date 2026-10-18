# code exp 018 multiplicative dgp

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-018-multiplicative-dgp_20260521T134318_result.json`
- **Structured JSON:** [`c2818cb67ab4a20d518d.json`](../../sessions/c2/c2818cb67ab4a20d518d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-018 complete. Key results:

| Method | Avg |Bias| | RMSE | Coverage |
|---|---|---|---|
| oracle | 0.0305 | 0.0384 | 0.960 |
| **ec_hte** | **0.0539** | **0.0677** | **0.955** |
| global_corrected | 0.1104 | 0.1241 | 0.540 |
| naive | 0.1352 | 0.1422 | 0.435 |

EC-HTE reduces RMSE by 52% vs naive and achieves 95.5% coverage (target 95%). Compared to exp-001 additive DGP (same config), EC-HTE actually performs *better* here (RMSE 0.068 vs 0.091) because the multiplicative DGP produces larger true CATEs, making relative bias smaller. Coverage matches exactly at 0.955.

Conclusion: **success** — EC-HTE is robust to non-additive treatment effects.

---

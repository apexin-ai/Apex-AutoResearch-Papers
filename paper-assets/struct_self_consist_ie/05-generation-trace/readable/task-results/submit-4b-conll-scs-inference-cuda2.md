# submit 4b conll scs inference cuda2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_4b_conll_scs_inference_cuda2_20260515T193149_result.json`
- **Structured JSON:** [`774b0948ae8b96da4c85.json`](../../sessions/77/774b0948ae8b96da4c85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果已完整存在，无需重提交。**

`output/exp_qwen3_4b_conll_scs_inference/report.json` 数据完整：

| 指标 | 值 |
|------|-----|
| greedy_f1 | 0.9251 |
| oracle_f1 | 0.9408 |
| oracle_headroom | 1.57pp |
| SJ_rho (full/cond) | 0.405 / 0.431 |
| FK_rho (full/cond) | 0.396 / 0.420 |
| LP_rho (full/cond) | 0.319 / 0.338 |
| LP_auroc (full/cond) | 0.769 / 0.815 |
| structural_beats_surface | true (+0.84pp) |
| n_instances | 3453 (2756 after gold-empty filter) |
| verdict | MARGINAL |

Registry 也已记录为 `DONE/success`。结果没丢。

---

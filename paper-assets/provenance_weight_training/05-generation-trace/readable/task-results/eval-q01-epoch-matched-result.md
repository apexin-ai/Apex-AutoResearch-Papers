# eval q01 epoch matched result

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_q01_epoch_matched_result_20260519T003103_result.json`
- **Structured JSON:** [`8bd4c8d6dd81b540cef7.json`](../../sessions/8b/8bd4c8d6dd81b540cef7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 指标 | 值 |
|------|-----|
| **eval_loss_holdout** | 2.8928 |
| **eval_ppl_holdout** | **18.0436** |
| num_tokens | 4,077,068 |
| elapsed | 190.5s |

PPL 18.04，略高于预期范围（17.65–17.85）。q01 是最激进的过滤阈值，epoch-matched 下训练数据最少，PPL 偏高符合预期方向，但比预估高了约 0.2。

---

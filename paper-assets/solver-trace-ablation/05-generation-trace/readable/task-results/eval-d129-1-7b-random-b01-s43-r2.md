# eval d129 1 7b random b01 s43 r2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d129-1_7b-random-b01-s43-r2_20260518T005111_result.json`
- **Structured JSON:** [`609c839c0d2a7a503e44.json`](../../sessions/60/609c839c0d2a7a503e44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Registry 已更新为 DONE/success。

## 结果摘要

| 指标 | 值 |
|------|-----|
| prove_rate | 100% |
| mean_isr | 0.0511 |
| H1% | 76% |
| H7% | 0% |
| H8% | 0% |
| **genuine%** | **24%** |
| content_independent% | 100% |
| training_steps | 500 |
| final_reward | 1.0526 |

关键发现：s43 **没有**复现 s42 的 H9 contradiction injection 行为。s43 走了 H1（conclusion-in-premise）路线（76%），genuine 24% 且 content_independent=100%。H9 不是 1.7B random 的 deterministic 结果，是 seed-dependent。

---

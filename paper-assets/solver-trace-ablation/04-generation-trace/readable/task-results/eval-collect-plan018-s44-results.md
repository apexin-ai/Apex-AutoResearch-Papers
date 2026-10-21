# eval collect plan018 s44 results

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect-plan018-s44-results_20260514T142801_result.json`
- **Structured JSON:** [`95f53001456b3242aedb.json`](../../sessions/95/95f53001456b3242aedb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。结果摘要：

| 指标 | 值 |
|------|-----|
| PR | 0.89 (89/100) |
| mean ISR | 0.0619 |
| median ISR | 0.0 |
| proved-only ISR | 0.0695 |
| ISR=0 样本数 | 72/89 (81%) |
| ISR=1.0 样本数 | 2 |

按 answer_type：unknown PR 最高 (0.976, ISR=0.089)，true 最低 (0.824, ISR=0.035)。

典型模式：模型生成大量冗余重复 premises（如 `MinWage(m)` 重复 20 次），删除任一条不影响证明，导致 ISR=0。这符合 C006 定义的 exec-only 冗余编码，random reward 未提供推理结构信号。

---

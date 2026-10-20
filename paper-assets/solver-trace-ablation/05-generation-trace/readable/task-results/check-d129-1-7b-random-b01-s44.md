# check d129 1 7b random b01 s44

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d129-1_7b-random-b01-s44_20260518T024426_result.json`
- **Structured JSON:** [`056220c37f674ff939ec.json`](../../sessions/05/056220c37f674ff939ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## d129-1_7b-random-b01-s44 结果

| 指标 | 值 |
|---|---|
| **训练状态** | 已完成 (500/500 steps) |
| **prove_rate** | 100% |
| **mean_ISR** | 0.0072 |
| **median_ISR** | 0 |
| **H1%** | 84% |
| **H7%** | 0% |
| **H8%** | 0% |
| **genuine%** | 16% |
| **content_independent%** | 100% |

**GPU**: 空闲（0MiB 占用）
**Registry**: 已更新为 DONE/success

符合预期：random reward 下模型学会了 prove（100%）但几乎零 ISR，84% H1（结论直接复制前提），仅 16% genuine。

---

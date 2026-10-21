# ops read volctrl mmlu

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_read-volctrl-mmlu_20260523T064208_result.json`
- **Structured JSON:** [`6b4b84c55743bb96d409.json`](../../sessions/6b/6b4b84c55743bb96d409.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

**MMLU 5-shot = 60.67%**

| 条件 | MMLU | vs d000 |
|------|------|---------|
| d000 (clean baseline) | 58.77% | — |
| volume control (等量非污染数据) | 60.67% | +1.90pp |
| d100 (100%污染数据) | 62.96% | +4.19pp |

volume control 贡献了 d100 总增益的约 45% (1.90/4.19)，剩余 ~55% (+2.29pp) 可归因于污染内容本身。Quantity confound 存在但只能解释不到一半的效应。

---

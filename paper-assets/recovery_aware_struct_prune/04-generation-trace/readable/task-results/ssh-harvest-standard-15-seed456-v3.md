# ssh harvest standard 15 seed456 v3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_harvest_standard_15_seed456_v3_20260521T005019_result.json`
- **Structured JSON:** [`9e20ab0268ea2df404b8.json`](../../sessions/9e/9e20ab0268ea2df404b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

**Standard 15% seed456 GSM8K 结果：**
- **Accuracy: 65.43% (863/1319), stderr ±1.31%**
- EOS rate: 99.39%, avg response length: 180.2 tokens

**多种子汇总（Standard 15% GRPO）：**

| Seed | Accuracy |
|------|----------|
| seed42 | 待确认 |
| seed456 | 65.43% |
| seed789 | 待确认 |

对比 CKA-only 15% 三 seed 均值 72.76%，Standard 15% seed456 低了约 7.3pp。需要汇齐 seed42 和 seed789 结果后计算 Standard 15% 的三 seed 均值做正式对比。

---

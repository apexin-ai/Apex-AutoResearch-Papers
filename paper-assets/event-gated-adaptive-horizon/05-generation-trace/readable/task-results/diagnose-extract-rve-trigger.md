# diagnose extract rve trigger

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_extract-rve-trigger_20260518T062506_result.json`
- **Structured JSON:** [`0aaa650d6ff6ffbfd071.json`](../../sessions/0a/0aaa650d6ff6ffbfd071.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已提取完毕：

```
008d_s4 @105K: value_mean=192.653, eval_return=63.598, r_ve=3.030
010b_s0 @95K:  value_mean=65.602,  eval_return=10.348, r_ve=6.340
```

注：两个实验的 metrics.jsonl 中已有预计算的 `civo/ve_ratio` 字段，与手动计算一致（3.029 和 6.340）。010b_s0 的 r_ve 显著高于 008d_s4，说明 cheetah 环境在触发时 value 对实际 return 的高估更严重。

---

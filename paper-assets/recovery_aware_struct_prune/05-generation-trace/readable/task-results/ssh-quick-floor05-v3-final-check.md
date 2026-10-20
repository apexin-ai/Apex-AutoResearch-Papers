# ssh quick floor05 v3 final check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_quick_floor05_v3_final_check_20260523T124544_result.json`
- **Structured JSON:** [`c3269165b360ec922c9d.json`](../../sessions/c3/c3269165b360ec922c9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
Floor 0.5:  完成, accuracy=61.71% (814/1319), EOS rate=99.2%
v3 MATH-500: 完成, accuracy=26.0% (130/500), truncated=42.2% (211/500)
Floor 0.6 v2: GRPO 已完成, GSM8K eval 进行中 ~135/1319 (~10%), 前100样本 acc=66.0%
```

v3 MATH-500 结果很差（26.0%），主要原因是 42.2% 的样本被截断（hit max 4096 tokens），说明 sft_standard_20 模型在 MATH-500 上生成过长、无法收敛到答案。进程 108574 仍存活，可能在跑后续评估。

---

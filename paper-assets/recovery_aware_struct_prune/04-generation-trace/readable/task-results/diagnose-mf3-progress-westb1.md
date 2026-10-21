# diagnose mf3 progress westb1

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mf3_progress_westb1_20260522T115415_result.json`
- **Structured JSON:** [`c150cb746c8a91b84cd6.json`](../../sessions/c1/c150cb746c8a91b84cd6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== MF3 Eval 状态 ===
PID 179898: alive
运行时间: 2h19m02s
GPU 1 使用: 16547MiB / 97887MiB, 99% util, 82°C, 608W
当前进度: 96/1319 samples (7.3%)
速度: ~78s/sample (正常应 3-5s，仍然极慢)
预计剩余: ~26h28m
预计完成: ~May 23 22:22 CST
结果文件: 不存在

中间统计 (50/1319): acc=46.0%, eos_rate=14.0%, avg_len=1805 tokens
```

**速度异常原因**：avg_len=1805 tokens，生成长度极高（正常 GSM8K 回答约 200-400 tokens）。eos_rate 仅 14%——86% 的样本没有正常结束，模型在不停生成直到 max_tokens。这是导致 78s/sample 的根本原因。

按当前速度跑完需要 **~26.5 小时**（明天晚上才能结束）。是否要 kill 掉重跑（加 max_new_tokens 限制），还是继续等？

---

# ops fp16 scope cleanup

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fp16-scope-cleanup_20260525T104835_result.json`
- **Structured JSON:** [`88c6d27f7a3bbcfc9d7a.json`](../../sessions/88/88c6d27f7a3bbcfc9d7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Kill 结果
- PID 81023 (72B AWQ): already gone
- PID 80806 (7B FP16): **KILLED**
- PID 80909 (7B AWQ): **KILLED**
- PID 81175 (Mistral FP16): **KILLED**
- PID 81214 (Mistral AWQ): already gone

## 清理结果
已删除：Qwen2.5-7B FP16/AWQ、Qwen2.5-72B AWQ、Mistral-7B FP16/AWQ 及 HF cache
清理后可用：**88 GB** / 250 GB（65% used）

## 保留下载状态

| 模型 | PID | 运行时间 | 状态 | Shards 完成 |
|------|-----|---------|------|------------|
| Qwen2.5-14B FP16 | 80512 | 9m30s | running | **6/8** (缺 shard 1-2) |
| Qwen2.5-32B FP16 | 80606 | 9m00s | running | **15/17** (缺 shard 15-16) |
| Llama-3.1-8B AWQ | 80699 | 8m30s | running | **0/2** (元数据已下，safetensors 未开始) |

---

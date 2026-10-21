# gpu exp 001 seed456 v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_exp_001_seed456_v2_20260514T153835_result.json`
- **Structured JSON:** [`5aa83a9dd6e7840bb67d.json`](../../sessions/5a/5aa83a9dd6e7840bb67d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已提交完成：

- **tmux session**: `exp_001_seed456_v2` 在 autodl-5090 上运行中
- **GPU**: cuda:2（通过 CUDA_VISIBLE_DEVICES=2）
- **模型**: qwen3-8b-scierc-merged-v2 已加载（15.27 GiB），vLLM v0.18.1 + FlashAttention v2
- **Registry**: `exp_001_seed456_v2` → RUNNING
- **Cron 监控**: 每 8 分钟检查一次（job `e7ae38ea`），完成后自动更新 registry 并通知

首次启动遇到 cuda:0 显存不足（被其他任务占用），已通过 `CUDA_VISIBLE_DEVICES=2` 修复。

---

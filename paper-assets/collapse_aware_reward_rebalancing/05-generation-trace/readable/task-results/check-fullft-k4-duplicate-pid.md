# check fullft k4 duplicate pid

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_fullft_k4_duplicate_pid_20260516T165947_result.json`
- **Structured JSON:** [`f990b40a7960fac675af.json`](../../sessions/f9/f990b40a7960fac675af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

- **PID 514305**：已死（不存在）
- **PID 514162**：存活，占用 cuda:1 约 29.8GB 显存，但**已经 OOM 崩溃**

日志显示 PID 514162 以 `torch.OutOfMemoryError` 退出（EXIT_CODE=1）。虽然进程还在 GPU 上占着显存，但实际已经结束训练，只是进程可能还没完全释放。

**结论：两个都失败了。** PID 514305 已死，PID 514162 OOM 崩溃。需要重新提交，并解决 OOM 问题（错误显示它在 GPU 0 上跑而非 GPU 1，可能需要显式设置 `CUDA_VISIBLE_DEVICES=1` 并减小 batch size 或启用 gradient checkpointing）。

---

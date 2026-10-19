# ops kill dryrun pid169864

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_dryrun_pid169864_20260515T230150_result.json`
- **Structured JSON:** [`63ec1290fa19411e520e.json`](../../sessions/63/63ec1290fa19411e520e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 169864 已终止（KILLED_OK）。

但 GPU0 并未完全释放——当前有另一个进程 PID 170986 占用 GPU0 约 40GB 显存（99% 利用率）。GPU1 上也有 PID 163723 占用约 20GB。

这两个进程不是刚才的 dry-run 测试，需要确认是否为正式实验再决定是否处理。

---

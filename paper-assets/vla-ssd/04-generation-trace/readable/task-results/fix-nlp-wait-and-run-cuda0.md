# fix nlp wait and run cuda0

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_nlp_wait_and_run_cuda0_20260522T095810_result.json`
- **Structured JSON:** [`9ef82bac61c764186c40.json`](../../sessions/9e/9ef82bac61c764186c40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。`CUDA_VISIBLE_DEVICES=1` 已改为 `CUDA_VISIBLE_DEVICES=0`，进程 613202/613207 仍在运行。脚本在循环等待模型下载，实际启动 python 时会读取新值。

---

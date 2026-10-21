# run bootstrap v2 restart remaining

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_bootstrap_v2_restart_remaining_20260523T034245_result.json`
- **Structured JSON:** [`bdc74f910fc2d8bff437.json`](../../sessions/bd/bdc74f910fc2d8bff437.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 session 均已正常运行：

- **bootstrap_cuda0** (GPU 0, 8.2GB): 正在采样，已到 350/5000，跑的是已完成条件会被 skip 后的第一个待跑条件
- **bootstrap_cuda1** (GPU 1, 13.4GB): 模型加载完成（NORA/TracVLA 更大），开始运行

CUDA0 日志显示 skip 逻辑生效（直接从待跑条件开始）。预计 ~1.5h 完成全部 9 个条件。

---

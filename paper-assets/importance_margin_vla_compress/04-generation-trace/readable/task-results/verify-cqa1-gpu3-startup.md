# verify cqa1 gpu3 startup

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_cqa1_gpu3_startup_20260525T110752_result.json`
- **Structured JSON:** [`45c6bc250504935cad93.json`](../../sessions/45/45c6bc250504935cad93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进程正常运行，GPU 3 已占用。**

- PID 313394 状态：`Rl+`（running），已运行 3:07
- GPU 3（UUID `a2a15ad4`）：利用率 42%，显存占用 10365 MiB
- PID 313394 在 GPU 3 上占用 10346 MiB

Reviewer 报告的 GPU 3 空闲应该是观察时间差——进程当时正在 CPU 加载模型阶段（π0.5 模型加载需要几分钟），现在已完成加载并在 GPU 上正常推理。无需任何操作。

---

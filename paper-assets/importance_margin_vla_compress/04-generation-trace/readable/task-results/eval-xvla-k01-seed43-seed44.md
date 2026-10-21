# eval xvla k01 seed43 seed44

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_xvla-k01-seed43-seed44_20260520T171200_result.json`
- **Structured JSON:** [`e2a5dbb4dde5138c5416.json`](../../sessions/e2/e2a5dbb4dde5138c5416.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已成功启动并在正确 GPU 上运行：

| 实验 | PID (bash/python) | GPU | 显存占用 |
|------|-------------------|-----|---------|
| k=0.1 seed=43 | 694939 / 694944 | GPU 1 (28:00.0) | 4521 MiB |
| k=0.1 seed=44 | 696118 / 696123 | GPU 3 (A9:00.0) | 4521 MiB |

4 块 GPU 现在全部在工作：GPU 0/2 跑 k=0.2，GPU 1/3 跑 k=0.1。

---

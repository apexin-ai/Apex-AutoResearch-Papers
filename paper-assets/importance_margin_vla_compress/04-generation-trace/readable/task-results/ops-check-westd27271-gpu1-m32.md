# ops check westd27271 gpu1 m32

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-westd27271-gpu1-m32_20260520T200605_result.json`
- **Structured JSON:** [`89cad8f42c28b0521b9f.json`](../../sessions/89/89cad8f42c28b0521b9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进程正常，没有崩溃。**

- **PID 921279**: 状态 `Rl+`，运行 9h18m
- **训练进度**: step 26550/100000，最新日志 `04:06:07`（刚刚），每 ~91s 一个 step，sps=0.5 稳定
- **loss**: ~2.6，梯度正常
- **GPU 利用率 0%**: 只是 `nvidia-smi` 采样时恰好在 CPU 端操作（数据加载/logging），训练持续正常推进

GPU 空闲 9 分钟的警报是误报——日志显示训练从未中断，step 间隔稳定在 ~90s。无需任何操作。

---

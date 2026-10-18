# ops check cqa1 gpu

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-cqa1-gpu_20260520T143125_result.json`
- **Structured JSON:** [`ab2626a9ff526ef25b8f.json`](../../sessions/ab/ab2626a9ff526ef25b8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇报 — cqa1-33015

| GPU | 显存占用 | PID | 进程 | 状态 |
|-----|---------|-----|------|------|
| **cuda:0** | 4540 MiB | 115960 | seed44 k=0.7 libero_object | **运行中** (已跑 1h07m) |
| **cuda:1** | 4 MiB | — | — | **空闲** ✅ |
| **cuda:2** | 4055 MiB | 132420 | seed44 k=0.5 libero_object | **运行中** (已跑 1h02m) |
| **cuda:3** | 4 MiB | — | — | **空闲** ✅ |

### 已完成的任务

**seed44 k=0.9** (PID 116978) — 已完成，22:16 结束，耗时 51.1 min
- **Overall SR: 98.2% (491/500)**，95% CI [96.6%, 99.1%]
- 结果已保存

**seed43 k=0.5** (PID 894197) — 已完成，21:43 结束，耗时 103.4 min
- **Overall SR: 44.2% (221/500)**，95% CI [39.9%, 48.6%]
- 结果已保存

### 结论

**GPU 1 和 GPU 3 确认空闲**，可立即调度新任务。GPU 0 和 GPU 2 上的 seed44 k=0.7 / k=0.5 仍在运行。

---

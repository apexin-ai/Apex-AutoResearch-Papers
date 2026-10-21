# ssh diagnose gpu1 hung

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose-gpu1-hung_20260520T085412_result.json`
- **Structured JSON:** [`8e448343be8bc7a9b232.json`](../../sessions/8e/8e448343be8bc7a9b232.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 1 完全恢复，训练进程无影响。

---

### 重置前后状态对比

| GPU | Util (前→后) | Memory (前→后) | Temp (前→后) | 训练进程 |
|-----|-------------|----------------|-------------|---------|
| 0 | 98% → 91% | 21255 → 21255 MiB | 75 → 74°C | PID 886278 ✅ |
| **1** | **100% → 0%** | **0 → 0 MiB** | **43 → 38°C** | 无（已恢复空闲） |
| 2 | 99% → 100% | 20001 → 20001 MiB | 73 → 72°C | PID 925638 ✅ |
| 3 | 97% → 98% | 31261 → 31261 MiB | 75 → 75°C | PID 886352 ✅ |

### 修复方法

`nvidia-smi -r` 和 PCI sysfs reset 在 Docker 容器中不可用。通过 CUDA API 创建并释放一个 context（`torch.cuda.set_device(1)` + `torch.zeros` + `torch.cuda.synchronize`）成功清除了 hung 状态。

根因推测：之前某个进程在 GPU 1 上崩溃，CUDA context 未正确释放，驱动持续报告 100% utilization。创建新 context 触发了驱动内部的状态清理。

GPU 1 现在空闲可用。

---

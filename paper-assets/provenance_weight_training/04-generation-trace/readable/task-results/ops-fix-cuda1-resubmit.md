# ops fix cuda1 resubmit

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_cuda1_resubmit_20260514T212100_result.json`
- **Structured JSON:** [`4850d8e6a70091d621d6.json`](../../sessions/48/4850d8e6a70091d621d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果**：

GPU 1 上的残留进程已不存在（之前的 PID 138525 和 139132 都已消失）。

当前 GPU 1 上运行的是 **grid_b0_5_seed456**（PID 145062），已运行 1 分钟，占用 46514MiB / 97887MiB，GPU 利用率 97%，状态正常。

看起来该实验已经被重新提交并成功启动了。4 张 GPU 当前状态：

| GPU | 进程 | PID | 显存占用 | GPU利用率 |
|-----|------|-----|---------|----------|
| 0 | grid_b_seed42_batch | 129259 | 46514MiB | 94% |
| 1 | grid_b0_5_seed456 | 145062 | 46514MiB | 97% |
| 2 | grid_b1_0_seed456 | 142907 | 46514MiB | 71% |
| 3 | grid_b1_5_seed456 | 142990 | 46514MiB | 99% |

**无需清理**，4 张 GPU 全部正常运行中，GPU 1 已被新实验占用。

---

# ssh verify occ loss fix v2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-occ-loss-fix-v2_20260528T230435_result.json`
- **Structured JSON:** [`c09b77e654c04fbe6a27.json`](../../sessions/c0/c09b77e654c04fbe6a27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

**两个实验都已崩溃，原因是 CUDA OOM，不是代码问题。**

每台服务器的 GPU 0 上都有一个**旧实验仍在运行**（已跑 3.5 小时），占满了显存：

| 服务器 | 占用 GPU 的旧进程 | 旧实验名 | 显存占用 |
|--------|-------------------|----------|----------|
| westd-34685 | PID 19300 | `full_occ_bn_v2_s2_r2`（无 `--occ_data_dir`） | 62152 MiB |
| westd-10894 | PID 33388 | `random_occ_v2_s0`（无 `--occ_data_dir`） | 62152 MiB |

这两个旧进程是上一轮（没有 `--occ_data_dir` 的版本），没被 kill 就启动了新实验，导致新实验抢不到显存直接 OOM。

**修复步骤：**
1. kill 旧进程（19300 on westd-34685, 33388 on westd-10894）
2. 确认 GPU 释放后重新启动新实验

需要我 kill 这两个旧进程吗？

---

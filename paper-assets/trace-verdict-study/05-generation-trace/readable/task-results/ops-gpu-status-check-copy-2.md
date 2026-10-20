# ops gpu status check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_check_20260522T024231_result.json`
- **Structured JSON:** [`2e8f7b927178ca8dcbd6.json`](../../sessions/2e/2e8f7b927178ca8dcbd6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态报告 — westd-11235

| | GPU 0 (RTX PRO 6000 Blackwell) | GPU 1 (RTX PRO 6000 Blackwell) |
|---|---|---|
| 显存 | **49175 MiB / 97887 MiB (50.2%)** | 0 MiB / 97887 MiB (0%) |
| GPU 利用率 | **100%** | 0% |
| 温度 | 41°C | 32°C |
| 功耗 | 105W / 600W | 36W / 600W |

**问题：cuda:0 的 orphan 进程未清除。**

虽然 `nvidia-smi` 的 Processes 表显示 "No running processes found"，但 cuda:0 仍占用 49175 MiB 显存且 GPU 利用率 100%。这是典型的 orphan GPU context —— 宿主进程已死但 GPU 内存未释放（nvidia-smi 看不到 PID）。

cuda:1 状态正常，显存和利用率均为 0。

**修复方案：** 需要重置 GPU 0 来释放 orphan 显存。可以执行：
1. `nvidia-smi --gpu-reset -i 0` — 尝试软重置
2. 如果软重置失败（Persistence Mode 开启时常见），可能需要先 `nvidia-smi -pm 0 -i 0` 关闭持久模式再重置

是否执行 GPU 重置？

---

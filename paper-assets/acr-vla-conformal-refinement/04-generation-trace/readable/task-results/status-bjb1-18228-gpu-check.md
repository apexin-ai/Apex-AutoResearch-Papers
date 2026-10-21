# status bjb1 18228 gpu check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_bjb1-18228-gpu-check_20260522T111324_result.json`
- **Structured JSON:** [`05de8af1c9472104ed52.json`](../../sessions/05/05de8af1c9472104ed52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 使用情况 (bjb1-18228, 4× RTX 4090):**

| GPU | 显存占用 | GPU-Util | 进程 |
|-----|---------|----------|------|
| 0 | 11796/24564 MiB | 27% | PID 883211: `train_crm.py --precompute --benchmark long --model pi05` (9874 MiB) + PID 907623: `lerobot_eval` SmolVLA object eval (1898 MiB) |
| 1 | 11299/24564 MiB | 24% | PID 905254: `evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42` |
| 2 | 11299/24564 MiB | 23% | PID 905879: 同上 `--seed 43` |
| 3 | 11299/24564 MiB | 1% | PID 906429: 同上 `--seed 44` |

**关键发现：**

- **cuda:0 有两个进程共存**，但不是你提到的 unified CRM training + r4 baseline eval 冲突。实际是：
  - PID 883211: pi05 long benchmark **precompute**（非训练），占 9.8GB
  - PID 907623: SmolVLA lerobot eval，占 1.9GB
  - 两者合计 ~11.8GB / 24.5GB，**未 OOM，仍有余量**

- **cuda:1/2/3 各跑一个 pi05 vla_only baseline eval**（seed 42/43/44），每个占 ~11.3GB，正常运行中

- PID 882598 不存在。PID 905242 是 eval seed42 的父 shell 进程（实际 python 进程是 905254，在 cuda:1 上），**不在 cuda:1 上与 CRM training 冲突**

**结论：无 GPU 冲突，无 OOM，所有进程正常运行。**

---

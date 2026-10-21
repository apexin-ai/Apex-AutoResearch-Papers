# gpu sft 05B d100 s123 gpu1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_sft_05B_d100_s123_gpu1_20260514T201947_result.json`
- **Structured JSON:** [`4c1cccd4a3df7fc1db4d.json`](../../sessions/4c/4c1cccd4a3df7fc1db4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 1 不空闲，无法提交。**

nvidia-smi 显示 GPU 1 上有活跃进程：
- PID: 433827
- 进程: `/root/miniconda3/bin/python`
- 显存占用: 21750 MiB

根据约束 C001/C002，GPU 上有进程时不得提交新任务。需要确认该进程属于哪个实验，再决定下一步。

---

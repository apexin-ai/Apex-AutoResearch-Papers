# ops gpu status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-check_20260515T005416_result.json`
- **Structured JSON:** [`60e97050c97cb000eadd.json`](../../sessions/60/60e97050c97cb000eadd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GPU 0: 空闲 - 0/24564 MiB
GPU 1: 运行中 - eval Qwen2.5-0.5B_d005_s123_aligned (PID 475651) - 3695/24564 MiB
GPU 2: 运行中 - eval Qwen2.5-1.5B_d100_s123_aligned (PID 473954) - 5857/24564 MiB
GPU 3: 运行中 - train_sft Qwen2.5-3B_d025_s42 (PID 466755) - 17645/24564 MiB
GPU 4: 运行中 - eval Qwen2.5-3B_d000_v2_s42_para_aligned_v2 (PID 472742) - 9017/24564 MiB
GPU 5: 运行中 - train_sft Qwen2.5-3B_d100_s123 (PID 471296) - 17973/24564 MiB

空闲 GPU: [0]
```

注意：GPU 5 上的 train_sft 命令行参数写的 `--gpu 0`，但实际占用的是 GPU 5（可能通过 `CUDA_VISIBLE_DEVICES` 映射）。

---

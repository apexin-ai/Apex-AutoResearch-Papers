# analysis urgent gpu plan022 check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_urgent_gpu_plan022_check_20260519T041954_result.json`
- **Structured JSON:** [`8dc64a127a517d3aa61c.json`](../../sessions/8d/8dc64a127a517d3aa61c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
cuda:0: PID 485203  90265MiB/97887MiB  100%  train_sft.py (exception_only_dynamics)
cuda:1: PID 485347  41183MiB/97887MiB  100%  train_sft.py (full_trace_dynamics)

tmux sessions:
  - qwen7b_exception_only_dynamics_seed42 (11:27:19)
  - qwen7b_full_trace_dynamics_seed42 (11:27:22)

plan_022 exception_only_dynamics: 运行中, ~295/444 steps (66%), ~9-10s/step, 含周期性 batch_eval
plan_022 full_trace_dynamics:     运行中, ~149/444 steps (34%), ~18s/step, 含周期性 batch_eval
```

exception_only 进度领先，预计再 ~25 min 完成训练阶段；full_trace 较慢（label_only_loss 开销），预计还 ~90 min。两个 job 都在正常推进，checkpoint 目录已有产出（exception_only 8 个、full_trace 5 个子目录）。GPU 0 显存偏高（90G）可能是 eval 子进程共驻。

---

# diagnose westd gpu check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd_gpu_check_20260517T191058_result.json`
- **Structured JSON:** [`34aec3d8b03f95b00751.json`](../../sessions/34/34aec3d8b03f95b00751.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GPU 0: [BUSY] - 11111MiB / 97887MiB, PID 47672 (eval_gsm8k pruned_standard_30, 运行 1分36秒)
GPU 1: [BUSY] - 34569MiB / 97887MiB, PID 14556 (eval_math500 grpo_standard_20, 运行 9小时44分)
GPU 2: [BUSY] - 23150MiB / 97887MiB, PID 43911+44270 (eval_gsm8k pruned_rasp_30, 运行 50分48秒)
GPU 3: [BUSY] - 31527MiB / 97887MiB, PID 31706 (eval_math500 grpo_rasp_20_v3, 运行 4小时25分)
---
可用于新实验的 GPU: []（全部占用）
```

**已知 PID 状态：**
- PID 14556 (eval_math500_grpo_standard_20) — **仍在运行**，GPU 1，已跑 9h45m，显存 34560MiB
- PID 44265 (eval_postprune_rasp_30) — **仍在运行**，是 GPU 2 上 PID 43911/44270 的 wrapper 进程
- PID 31706 (eval_math500_grpo_rasp_20_v3) — **仍在运行**，GPU 3，已跑 4h26m，显存 31518MiB

**额外发现：**
- GPU 0 有一个新进程 PID 47672：`eval_gsm8k.py --model_path pruned_standard_30`，刚启动 1 分 36 秒

**结论：4 张 GPU 全部被占用，当前无空闲 GPU 可用于新实验。**

---

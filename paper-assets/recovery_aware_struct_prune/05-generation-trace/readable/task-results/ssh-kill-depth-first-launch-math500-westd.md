# ssh kill depth first launch math500 westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill_depth_first_launch_math500_westd_20260522T151656_result.json`
- **Structured JSON:** [`dbbe59cef0ec67de1f83.json`](../../sessions/db/dbbe59cef0ec67de1f83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU:2 loading (7GB VRAM). GPU:3 still in model load phase. Both Python processes confirmed running (PID 58276 and 58435). Here's the summary:

## depth-first interim results
- GRPO: no result file (eval was at ~54 min, still in progress)
- SFT: no result file (eval was at ~36 min, still in progress)

## kill 确认
- PID 51981/51986 (GRPO depth-first): killed
- PID 54882 (SFT depth-first): killed

## model paths
- α=0.5: `/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha0p5_20/` (直接有 config.json + model.safetensors)
- α=4.0: `/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20/` (直接有 config.json + model.safetensors)

## new evals launched
- α=0.5 MATH-500 (GPU:2): Python PID=58276 (bash wrapper 58270)
- α=4.0 MATH-500 (GPU:3): Python PID=58435 (bash wrapper 58430)

## GPU 验证
```
GPU 0: 25793 MiB, 99%  (existing gsm8k eval)
GPU 1: 16755 MiB, 99%  (existing math500 α=2.0 eval)
GPU 2:  6999 MiB,  5%  ← α=0.5 MATH-500, model loading
GPU 3:     0 MiB, 100% ← α=4.0 MATH-500, model loading to GPU
```

注意：output_path 写入 `/root/autodl-tmp/recovery_aware_struct_prune/results/`，日志写入 `/root/autodl-tmp/recovery_aware_struct_prune/logs/`。

---

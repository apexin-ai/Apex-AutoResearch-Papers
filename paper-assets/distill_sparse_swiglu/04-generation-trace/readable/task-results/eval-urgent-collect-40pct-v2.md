# eval urgent collect 40pct v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_urgent_collect_40pct_v2_20260520T103113_result.json`
- **Structured JSON:** [`f2c0080a2b795e399cf3.json`](../../sessions/f2/f2c0080a2b795e399cf3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Uniform HS/PIQA (PID 201401) — 完成

| 指标 | 值 | stderr |
|------|-----|--------|
| model_level_sparsity | 0.397 | — |
| hellaswag_acc_norm | **0.6497** | ±0.0048 |
| piqa_acc_norm | **0.7236** | ±0.0104 |

allocation=uniform, sparsity_target=0.4, batch_size=8, seq_len=2048, calibration_samples=32

### Global eval v2 (PID 200977) — CUDA OOM 失败

在 `teal_global_masks` 计算阶段崩溃（`predictor.py:149`, `gate * up` 分配 224 MiB 时 OOM）。原因：GPU 0 上另一个进程 (PID 197977) 占用了 64.54 GiB / 94.97 GiB，剩余显存不足。

**没有产出任何结果**，`results/benchmark/kl_sparsity40_s42_global_eval_v2/` 目录为空。

需要重跑 v2 global eval——确保 GPU 0 上没有其他进程占用显存，或者改用 cuda:1。

---

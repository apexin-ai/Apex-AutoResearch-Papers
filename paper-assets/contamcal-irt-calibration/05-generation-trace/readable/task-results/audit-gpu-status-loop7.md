# audit gpu status loop7

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_gpu-status-loop7_20260514T204758_result.json`
- **Structured JSON:** [`9ae2fc38f26a6148adf3.json`](../../sessions/9a/9ae2fc38f26a6148adf3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态审计报告

### GPU 占用总览（全部占用，无空闲 GPU）

| GPU | 显存占用 | PID | 运行时间 | 任务 | 实验 |
|-----|---------|-----|---------|------|------|
| **0** | 4,567 / 24,564 MiB (19%) | 438206 | 3m30s | `compute_signals` 1.5B_d005_s42 gsm8k (embedding+minkpp+selfcritique) | exp-002 |
| **1** | 21,761 / 24,564 MiB (89%) | 433827 | 31m15s | `train_sft` 0.5B_d100_s123 | exp-001 |
| **2** | 14,723 / 24,564 MiB (60%) | 435420 | 27m29s | `train_sft` 1.5B_d100_s123 (bs=1, grad_accum=16) | exp-001 |
| **3** | 13,341 / 24,564 MiB (54%) | 420195 | 2h24m30s | `train_sft` 3B_d100_s42 (bs=1, grad_accum=16, lr=5e-5) | exp-001 |
| **4** | 10,455 / 24,564 MiB (43%) | 420910 | 2h22m54s | `evaluate` 1.5B_d025_s42_aligned (mmlu+gsm8k+arc+humaneval, mc=aligned) | exp-001 |
| **5** | 17,327 / 24,564 MiB (71%) | 435976 | 25m51s | `train_sft` 3B_d000_v2_s123 (lr=5e-5, lora_alpha=16) | exp-001 |

**空闲 GPU：无。** 6/6 全部占用。

### Handoff 进程状态 — 全部死亡

| PID | 状态 |
|-----|------|
| 336750 | **DEAD** |
| 406017 | **DEAD** |
| 405515 | **DEAD** |
| 411783 | **DEAD** |
| 426335 (exp-005) | **DEAD** |
| 411032 (exp-004) | **DEAD** |

### 额外检查

- **exp-001 3B_d000_v2_s123**：checkpoint 目录已创建（May 15 04:23），`lora_adapter/` 子目录存在但**内容为空**（训练刚开始 25 分钟，尚未保存 checkpoint）
- **exp-006 IRT ARC (Stan)**：NUTS 采样进行中，4 chains 均在 warmup 阶段（35-40% / 2000 steps），输出到 `results_05B_arc_delta/arc_challenge/`。**这是 CPU 任务，无 GPU 进程。**
- **exp-002 1.5B signals 进度**：
  - `1.5B_d000_s42`：**完成**（3 benchmarks × 3 signals + 3 merged = 12 files）
  - `1.5B_d005_s42`：**部分完成** — mmlu 已 merged，gsm8k 正在计算（GPU 0 当前任务），缺 arc_challenge 和 gsm8k 的 selfcritique + merged
- **exp-004 / exp-005 CPU 进程**：均已死亡

---

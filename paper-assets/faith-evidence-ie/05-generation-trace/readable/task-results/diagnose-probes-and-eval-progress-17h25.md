# diagnose probes and eval progress 17h25

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_probes-and-eval-progress-17h25_20260514T171407_result.json`
- **Structured JSON:** [`71edef8669e4871f747c.json`](../../sessions/71/71edef8669e4871f747c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

extract_r4 和 flatnli_r5 的日志尚无指标输出（stdout 缓冲未 flush）。以下是完整汇总：

---

## 状态总结

### 1. mvp2_grpo_ced_kl001_r4 (PID 68084, cuda:0)
- **状态**: 存活，已运行 1h42m
- **进度**: step **71/100** (71%)
- **GPU**: 13649 MiB, 77% util
- **最新指标** (step ~70):

| 指标 | 值 |
|------|-----|
| reward | 0.695 |
| f1_reward/mean | 0.240 |
| ced_reward/mean | 0.236 |
| frac_zero_std | **0.0** ✓ |
| kl | 0.098 |
| format_reward | 0.220 |
| clipped_ratio | 0.2 |

- **趋势**: frac_zero_std 从 0.7→0.4→**0.0**，f1 从 0.014→0.082→**0.240**，ced 从 0.026→0.120→**0.236**。reward 持续上升，kl 稳定在 <0.2。非常健康。
- **ETA**: ~29 steps × ~95s/step ≈ 46 min → **~18:10 UTC**

### 2. mvp2_grpo_extract_r4 (PID 73264, cuda:2)
- **状态**: 存活，已运行 18m
- **进度**: step **11/100** (11%)
- **GPU**: 12843 MiB, 62% util
- **指标**: **无**（stdout 缓冲未 flush，日志仅 23 行 = 启动信息 + 进度条）
- **速度**: ~83-103s/step
- **ETA**: ~89 steps × ~95s/step ≈ 141 min → **~19:35 UTC**

### 3. mvp2_grpo_flatnli_r5 (PID 73407, cuda:3)
- **状态**: 存活，已运行 18m
- **进度**: step **125/200** (62.5%，从 checkpoint-100 续训)
- **GPU**: 11029 MiB, 60% util
- **指标**: **无**（同样 stdout 缓冲问题，日志仅 27 行）
- **速度**: ~47s/step
- **ETA**: 75 steps × ~47s ≈ 59 min → **~18:15 UTC**

### 4. mvp2_eval_ced_kl001_r4_early (PID 75581, cuda:1)
- **状态**: 存活，已运行 3m38s
- **进度**: Inference **2/62 batches** (3%)
- **GPU**: 9075 MiB, 70% util
- **速度**: ~83s/batch
- **ETA**: 60 batches × ~83s ≈ 83 min → **~18:40 UTC**

---

### 关键发现

**ced_kl001_r4 表现很好**：frac_zero_std 降到 0，f1 和 ced reward 都在稳步上升，kl 控制在 0.1 左右，mode collapse 已完全解除。

**extract_r4 和 flatnli_r5 无指标可看**：stdout 重定向到文件时 Python 使用 block buffering，这两个进程运行时间短、输出量小，缓冲区还没满。指标应该在 wandb 上可查。下次启动时可以加 `PYTHONUNBUFFERED=1` 或 `python -u` 来避免这个问题。

---

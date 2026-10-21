# check running experiments

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_running_experiments_20260516T030643_result.json`
- **Structured JSON:** [`f538049448ca8ca28adb.json`](../../sessions/f5/f538049448ca8ca28adb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

两个实验均 **ALIVE**，无错误。

### 实验 1: lm_eval_teal_30pct (PID 194814)
- **状态**: 运行中，已 11 分钟
- **GPU**: cuda:0, 19984 MiB
- **进度**: `generate_until` 337/1319 (25%) — 已完成 loglikelihood 阶段（arc_challenge, winogrande, mmlu），当前在跑 gsm8k 生成
- **速度**: ~1.38s/it
- **预计剩余**: ~23 分钟

### 实验 2: lm_eval_mistral_kl_50pct (PID 195242)
- **状态**: 运行中，已 10 分钟
- **GPU**: cuda:1, 16524 MiB
- **进度**: loglikelihood 已 100% 完成 (63389/63389)，`generate_until` 刚开始 29/1319 (2%)
- **速度**: ~3.6s/it
- **预计剩余**: ~77 分钟

两个实验运行正常，不需要干预。TEAL 30% 预计 ~25 分钟后完成，Mistral KL 50% 预计 ~80 分钟后完成。

---

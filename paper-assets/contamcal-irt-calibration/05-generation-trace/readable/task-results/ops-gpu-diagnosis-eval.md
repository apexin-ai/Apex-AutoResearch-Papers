# ops gpu diagnosis eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-diagnosis-eval_20260515T181422_result.json`
- **Structured JSON:** [`a24c5eb16f9fe80a83fc.json`](../../sessions/a2/a24c5eb16f9fe80a83fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 608198 已在 GPU 3（bus 99:00.0）上占用 7000MiB，eval 启动成功。

---

## 报告

### 1. GPU 实际占用

| GPU | PID | 显存 | 实验 |
|-----|-----|------|------|
| cuda:0 | 594494 | 17966 MiB | exp_001_sft_3B_d100_s123_a32_v2 |
| cuda:1 | 593745 | 13332 MiB | exp_001_sft_3B_d100_s42_a32_v2 |
| cuda:2 | 580698 | 13574 MiB | exp_001_eval_3B_d005_s123_aligned |
| cuda:3 | 608198 | 7000 MiB | **exp_001_eval_3B_d025_s123_para_aligned** (刚提交) |
| cuda:4 | 597179 | 13868 MiB | exp_001_sft_3B_d000_v3 |
| cuda:4 | 607648 | 6844 MiB | exp002 compute_signals (d025_s42, mmlu) |
| cuda:5 | 589763 | 17642 MiB | exp001_d025_3B_v3 (train_sft d025_v3_s42) |
| CPU | 528993 | — | run_extreme_gamma.py (9h39m) |

### 2. PID 593745 诊断

**不是僵尸进程。** PID 593745 存活，是 PID 593740（`exp_001_sft_3B_d100_s42_a32_v2` 的 tmux wrapper）的子进程，运行在 cuda:1 上，已跑 1h44m。registry 中 `exp_001_sft_3B_d100_s42_a32`（无 _v2）标记为 DONE/failed 是正确的——那是旧实验。cron 条目将 PID 593745 关联到旧 exp_id 是过期信息，该 PID 实际属于 _v2 版本。

### 3. cuda:3 eval 提交

已提交 `exp_001_eval_3B_d025_s123_para_aligned`，PID 608198 确认在 cuda:3 运行，7000MiB 已分配。Registry 已设为 RUNNING。

### 4. 异常

- **GPU 4 双进程共存**：exp_001_sft_3B_d000_v3（13868MiB）+ exp002 compute_signals（6844MiB）共用 cuda:4，总计 ~20.7GB/24.5GB。目前未 OOM，但余量较小。

---

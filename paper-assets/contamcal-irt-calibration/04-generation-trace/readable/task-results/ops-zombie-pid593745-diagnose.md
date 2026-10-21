# ops zombie pid593745 diagnose

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_zombie-pid593745-diagnose_20260515T183105_result.json`
- **Structured JSON:** [`4c5fcd9f6bd32d8ea02b.json`](../../sessions/4c/4c5fcd9f6bd32d8ea02b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：593745 不是僵尸进程，无需 kill。**

进程关系：
- `593740` (bash wrapper, v2) → `593744` (timeout) → **`593745`** (python train_sft.py)
- 三个 PID 是同一个实验 `exp_001_sft_3B_d100_s42_a32_v2` 的父子链

v2 训练状态：
- 进度：**1724/4159 steps (41%)**，已运行约 2h01m
- 预计剩余：~3h18m
- Loss: ~1.1-1.2，token accuracy: ~0.72-0.74，训练正常
- cuda:1 显存：13341 MiB / 24564 MiB (54%)，无 OOM 风险

**不存在旧版本 alpha=16 进程与 v2 冲突的情况。** 原始的 `exp_001_sft_3B_d100_s42_a32`（非 v2）没有独立进程在运行。

---

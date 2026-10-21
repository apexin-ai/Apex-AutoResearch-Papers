# ops global status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_global-status-check_20260516T201817_result.json`
- **Structured JSON:** [`74ce62297d50bbf7f42d.json`](../../sessions/74/74ce62297d50bbf7f42d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 6 卡状态表

| GPU | PID | 任务 | 显存 | 利用率 |
|-----|--------|------|------|--------|
| 0 | 825638 | eval d005_s42_aligned | 8072 MiB | 75% |
| 1 | 830115 | signals d000_s42 mmlu | 6852 MiB | 60% |
| 2 | 853489 | signals d025_s42 mmlu | 560 MiB | 8% |
| 3 | 822390 | eval d025_s42_aligned | 12160 MiB | 75% |
| 4 | 842929 | signals d005_s42 mmlu | 7412 MiB | 57% |
| 5 | 831033 | eval d100_s42_aligned | 8304 MiB | 73% |

### 2. d000 MMLU signals

**未完成。** `signals_merged_mmlu.json` 不存在。GPU 1 上的 d000 mmlu signals 进程仍在运行。已有 `signals_merged_arc_challenge.json` 和 `signals_merged_gsm8k.json`，缺 mmlu 的 merged。

→ **RRF 未触发。**

### 3. Eval 完成情况

d005 / d025 / d100 的 `.done` 文件均不存在，三个 eval 进程仍在运行中。

→ **Signals 未启动（无空闲 GPU 且无 eval 完成）。**

### 注意

GPU 2（d025 signals）显存仅 560 MiB、利用率 8%，可能刚启动或处于数据加载阶段，需关注是否正常推进。

---

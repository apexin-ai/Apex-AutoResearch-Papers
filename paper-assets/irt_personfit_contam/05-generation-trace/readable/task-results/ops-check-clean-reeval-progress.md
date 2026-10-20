# ops check clean reeval progress

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-clean-reeval-progress_20260523T145241_result.json`
- **Structured JSON:** [`a0f70d2e95cf035d3a0c.json`](../../sessions/a0/a0f70d2e95cf035d3a0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Clean Re-eval 进度汇总

### 已完成的 clean seeds（全部在 ctrl_contam_llama/results/）

| Seed | 完成时间 | lz* | acc |
|------|---------|-----|-----|
| clean (s1) | 22:26:35 | — | — |
| clean_s2 | 22:46:44 | -1.8765 | 0.5959 |
| clean_s3 | 21:57:20 | — | — |
| clean_s4 | 22:26:01 | — | — |
| clean_s5 | 22:46:43 | 1.7323 | 0.5965 |
| clean_s6 | 22:02:34 | — | — |
| clean_s7 | 22:31:18 | — | — |
| clean_s8 | 22:48:46 | 1.1656 | 0.5860 |
| clean_s9 | 22:10:10 | — | — |
| clean_s10 | 22:38:51 | — | — |

**共 10 个 clean seed 已全部完成。** result 文件：`clean_results.json`, `clean_s2` ~ `clean_s10_results.json`（含 `clean_results_lz_uncorrected.json`）。

ctrl_contam_pilot/results/llama/ 下无 clean 文件。

### 当前运行

- **GPU 0/1/2**: 已 ALL DONE，空闲（0 MiB 显存）
- **GPU 3**: 正在跑 `contam_5 mistral`（非 clean），进度 11000/14042（~78%），显存 5893 MiB，利用率 95%

### 尚未开始的 clean seeds

**无。** 全部 10 个 clean seed 已完成。

### GPU 3 上的 contam_5 mistral

按当前速率（~500 items/min），剩余约 3042 items，预计 **6-8 分钟后完成**。

---

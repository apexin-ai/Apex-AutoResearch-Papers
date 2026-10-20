# analysis exp006 oracle gsm8k extended v2 results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp006-oracle-gsm8k-extended-v2-results_20260515T025018_result.json`
- **Structured JSON:** [`59cbea1abc0aa7e0a306.json`](../../sessions/59/59cbea1abc0aa7e0a306.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验**仍在运行中**，尚未完成。关键发现：

1. **当前 MCMC 状态**：chains 按顺序运行（非并行），chain 1 已完成（26:34），chain 2/3 已完成，chain 4 在采样中（~52%, 3100/6000）。按 ~3.93 it/s 计算，chain 4 剩余 ~12 分钟，预计 **11:04 服务器时间**完成。

2. **`exp006_results.json` 来自先前失败的尝试**：`total_time_sec: 759.6`，IRT 部分显示 error（retcodes=[1,1,1,1]，4 chains 全部失败）。当前运行是重试，chains 正常采样中。

3. **已有 baseline 评估结果**（来自失败运行，baselines 本身有效）：

| Method | MAE | ECE | Kendall τ | Coverage 95% |
|--------|-----|-----|-----------|-------------|
| B0_raw | 0.005 | 0.005 | 0.838 | 100% |
| B1_remove_rescore | 0.005 | 0.005 | 0.838 | 100% |
| B4_linear_regression | 0.008 | 0.008 | — | 100% |
| B5_emperor_mitigation | 0.005 | 0.005 | 0.838 | 100% |
| B6_dcr_fuzzy | 0.138 | 0.137 | 0.415 | 56.3% |

4. **gamma、rhat、ESS、PPP 均不可用** — 需等 MCMC 完成后才有 IRT 结果。

建议 ~15 分钟后重新采集。是否需要我设置定时轮询？

---

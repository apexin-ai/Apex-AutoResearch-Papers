# code exp 001 check exp 004

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_001_check_exp_004_20260517T131203_result.json`
- **Structured JSON:** [`ea6eaea07dd0228b3a02.json`](../../sessions/ea/ea6eaea07dd0228b3a02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。

---

## 状态报告

### exp_001: Gen 9/9 运行中 (PID 59365)

当前阶段：Gen 9 样本生成中，22400/50000 (44.8%)

**预估完成时间**：每代周期 ~2h35m（从 checkpoint 时间戳推算），Gen 8 评估完成约 20:53，预计 Gen 9 完成约 **23:25-23:30 服务器时间**。

**Gen 0-8 Metrics 汇总**：

| Gen | eff_rank | log_det | ppl | distinct4 | hellaswag_norm | train_loss |
|-----|----------|---------|-----|-----------|----------------|------------|
| 0 | 417.55 | 2366.68 | 9.55 | 0.7414 | 0.4130 | — |
| 1 | 491.77 | 2464.76 | 11.38 | 0.6256 | 0.3897 | 1.623 |
| 2 | 496.44 | 2469.93 | 13.58 | 0.5154 | 0.3764 | 1.268 |
| 3 | 493.31 | 2440.57 | 16.25 | 0.4900 | 0.3658 | 1.134 |
| 4 | 485.67 | 2405.05 | 19.80 | 0.4679 | 0.3558 | 1.098 |
| 5 | 479.21 | 2370.17 | 24.59 | 0.4630 | 0.3439 | 1.047 |
| 6 | 473.00 | 2335.17 | 30.91 | 0.4655 | 0.3311 | 1.025 |
| 7 | 464.20 | 2304.19 | 38.89 | 0.4474 | 0.3187 | 1.015 |
| 8 | 456.76 | 2252.12 | 49.29 | 0.4401 | 0.3103 | 0.987 |

趋势清晰：eff_rank 从 Gen 1 peak (491.77) 持续下降至 456.76，log_det 同向下降，ppl 从 9.55 指数增长至 49.29，distinct4 和 hellaswag 单调下降。Spectral collapse 信号明确。

### exp_004: 未启动

原因：cuda:0 被 exp_001 (PID 59365) 占用，等 Gen 9 完成后再启动。

### GPU 状态
- **cuda:0**: 在用 (PID 59365, 65.9GB/97.9GB, 85% util)
- **cuda:1**: 空闲 (0MB, 0% util)

---

# code exp 001 status

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_001_status_20260517T124626_result.json`
- **Structured JSON:** [`5a4ab1dff1941f44c133.json`](../../sessions/5a/5a4ab1dff1941f44c133.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_001 Phase 0 状态报告

### 进程
- **PID 59365**: 已死
- **Pipeline 仍在运行**: log 文件持续更新（最后修改 20:48:17），实际运行进程 PID 已更换

### 当前进度: Gen 9/9 — 数据生成中 13,120/50,000 (26.2%)

### Gen 0-8 全量 Metrics

| Gen | eff_rank | log_det | ppl | distinct4 | hellaswag | train_loss |
|-----|----------|---------|-----|-----------|-----------|------------|
| 0 | 417.5 | 2366.7 | 9.55 | 0.741 | 0.413 | — |
| 1 | 491.8 | 2464.8 | 11.38 | 0.626 | 0.390 | 1.623 |
| 2 | 496.4 | 2469.9 | 13.58 | 0.515 | 0.376 | 1.268 |
| 3 | 493.3 | 2440.6 | 16.25 | 0.490 | 0.366 | 1.134 |
| 4 | 485.7 | 2405.0 | 19.80 | 0.468 | 0.356 | 1.098 |
| 5 | 479.2 | 2370.2 | 24.59 | 0.463 | 0.344 | 1.047 |
| 6 | 473.0 | 2335.2 | 30.91 | 0.466 | 0.331 | 1.025 |
| 7 | 464.2 | 2304.2 | 38.89 | 0.447 | 0.319 | 1.015 |
| 8 | 456.8 | 2252.1 | 49.29 | 0.440 | 0.310 | 0.987 |

### Collapse 趋势（Gen 2 为转折点）

- **eff_rank**: 峰值 496.4 (Gen 2) → 456.8 (Gen 8)，持续下降
- **log_det**: 峰值 2469.9 (Gen 2) → 2252.1 (Gen 8)，持续下降
- **ppl**: 9.55 → 49.29，单调恶化 5.2x
- **distinct4**: 0.741 → 0.440，多样性持续丢失
- **hellaswag**: 0.413 → 0.310，能力单调退化
- **train_loss**: 1.623 → 0.987，单调下降（过拟合信号）

### 预估完成时间
- Gen 7→8 周期约 2.5h（hellaswag_gen7 17:38 → hellaswag_gen8 20:16）
- Gen 9 生成始于 ~20:16，当前 26%
- **预计 Gen 9 完成（含 train+eval）: ~23:00-23:30 北京时间**

### 附注
`phase1_adaptive_seed42_results.json` 已存在（Gen 0-2, mix_ratio=0.5），Phase 1 自适应实验已并行启动。

---

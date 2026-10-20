# check phase0 progress 0517b

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_phase0_progress_0517b_20260517T033810_result.json`
- **Structured JSON:** [`0bff3759a9d14fdfa362.json`](../../sessions/0b/0bff3759a9d14fdfa362.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 0 实验进度汇总

### exp_001 (Pythia-410M, cuda:0, PID 59365)

**状态**: 运行中，正在执行 Gen 5（生成合成数据阶段，已完成 40320/50000 样本）

| Gen | eff_rank | log_det | ppl | distinct4 | train_loss | sigma1 |
|-----|----------|---------|-----|-----------|------------|--------|
| 0 | 417.55 | 2366.68 | 9.55 | 0.741 | - | 1942.8 |
| 1 | 491.77 | 2464.76 | 11.38 | 0.626 | 1.623 | 804.0 |
| 2 | 496.44 | 2469.93 | 13.58 | 0.515 | 1.268 | 712.0 |
| 3 | 493.31 | 2440.57 | 16.25 | 0.490 | 1.134 | 700.7 |
| 4 | 485.67 | 2405.05 | 19.80 | 0.468 | 1.098 | 729.6 |

**趋势**: log_det 和 eff_rank 在 Gen 2 达峰后开始下降，ppl 持续上升，distinct4 持续下降。sigma1 从 Gen 0 的 1942 急剧降到 Gen 1 的 804 后趋稳。collapse 信号明确。

---

### exp_002 (Pythia-1B, cuda:1, PID 25237)

**状态**: **已崩溃** — `No space left on device` 错误（保存 Gen 0 checkpoint 时磁盘满）

已保存的数据（Gen 0-3 的评估指标已记录）:

| Gen | eff_rank | log_det | ppl | distinct4 | train_loss | sigma1 |
|-----|----------|---------|-----|-----------|------------|--------|
| 0 | 516.14 | 2835.32 | 8.07 | 0.751 | - | 1661.2 |
| 1 | 570.75 | 2905.74 | 9.41 | 0.634 | 1.530 | 1052.8 |
| 2 | 580.92 | 2893.85 | 11.04 | 0.538 | 1.218 | 916.3 |
| 3 | 580.63 | 2864.78 | 13.44 | 0.501 | 1.027 | 873.5 |

**注**: 虽然进程 PID 25237 仍在 GPU 1 上占用 39.7GB 显存，但日志显示已经 crash。进程可能处于僵死状态。

---

### GPU 状态

| GPU | 型号 | 显存使用 | 利用率 | 温度 |
|-----|------|---------|--------|------|
| 0 | RTX PRO 6000 | 65.9 / 97.9 GB | 88% | 55°C |
| 1 | RTX PRO 6000 | 39.8 / 97.9 GB | 94% | 66°C |

---

### 需要处理的问题

1. **磁盘空间**: `/` 分区 30GB 已用 25GB (84%)，1B 模型 checkpoint 写入失败。需要清理空间或改用外挂存储后重启 exp_002。
2. **僵尸进程**: PID 25237 占用 GPU 1 显存但已 crash，需要 kill 释放资源。

---

# ssh exp 017 018 progress check

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp_017_018_progress_check_20260523T030908_result.json`
- **Structured JSON:** [`6b011b94a80fda268be3.json`](../../sessions/6b/6b011b94a80fda268be3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度汇总

### exp_017 (r=0.2, seed43, cuda:1)
- **进度**: Gen 10/10，正在生成样本 30720/40000 (77%)
- **状态**: 运行中，日志最后更新 11:10 CST
- **预计完成**: ~30-60 分钟内（样本生成完成后还需评估）
- **已运行**: ~21 小时（05-22 14:18 启动）

**Gen 0-9 完整 metrics:**

| Gen | eff_rank | log_det | PPL | D-4 | train_loss |
|-----|----------|---------|------|------|-----------|
| 0 | 417.55 | 2366.68 | 9.55 | 0.7415 | — |
| 1 | 475.29 | 2365.31 | 10.28 | 0.6842 | 1.768 |
| 2 | 480.44 | 2358.84 | 10.74 | 0.4988 | 1.722 |
| 3 | 487.00 | 2365.74 | 11.15 | 0.4780 | 1.425 |
| 4 | 489.33 | 2377.37 | 11.49 | 0.4445 | 1.367 |
| 5 | 492.09 | 2395.98 | 11.83 | 0.4435 | 1.273 |
| 6 | 495.85 | 2411.37 | 12.15 | 0.4420 | 1.222 |
| 7 | 498.05 | 2426.30 | 12.48 | 0.3433 | 1.191 |
| 8 | 500.80 | 2436.78 | 12.76 | 0.3106 | 1.015 |
| 9 | 504.08 | 2453.63 | 13.08 | 0.3060 | 0.955 |

**与 seed42 Gen10 交叉对比** (seed42: log_det=2479.7, eff_rank=511.3, PPL=13.83, D-4=0.520):
- Gen9 的 log_det(2453.6)、eff_rank(504.1)、PPL(13.08) 趋势一致，预计 Gen10 会接近 seed42 参考值
- **D-4 显著偏低**: seed43 Gen9 = 0.306 vs seed42 Gen10 = 0.520。两个 seed 的多样性退化速度差异较大

---

### exp_018 (r=0.5, seed43, cuda:0)
- **进度**: Gen 6/10，正在生成样本 24640/25000 (98.6%)
- **状态**: 运行中，日志最后更新 11:10 CST
- **预计完成**: ~5-6 小时（约 17:00 CST），每 gen 约 1.4 小时，剩余 Gen 7-10
- **已运行**: ~8.5 小时（05-23 02:38 启动）

**Gen 0-5 完整 metrics:**

| Gen | eff_rank | log_det | PPL | D-4 | train_loss |
|-----|----------|---------|------|------|-----------|
| 0 | 417.55 | 2366.68 | 9.55 | 0.7415 | — |
| 1 | 475.91 | 2361.66 | 10.08 | 0.6705 | 1.984 |
| 2 | 488.01 | 2393.57 | 10.41 | 0.5708 | 1.912 |
| 3 | 493.94 | 2419.34 | 10.73 | 0.5438 | 1.712 |
| 4 | 503.05 | 2454.90 | 11.12 | 0.4632 | 1.643 |
| 5 | 510.11 | 2479.81 | 11.60 | 0.4189 | 1.522 |

**与 seed42 Gen10 交叉对比** (seed42: log_det=2573.2, eff_rank=554.5, PPL=15.20, D-4=0.095):
- Gen5 的 log_det(2479.8) 和 eff_rank(510.1) 已接近 seed42 的 Gen5-6 水平，趋势吻合
- r=0.5 的 collapse 速度更快（Gen5 eff_rank 510 vs r=0.2 Gen5 eff_rank 492）

---

**无异常**: 两个实验都在正常运行，日志持续更新，无错误信息。

---

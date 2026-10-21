# check exp001 completion

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp001_completion_20260517T101929_result.json`
- **Structured JSON:** [`e034bbcfb443214f252a.json`](../../sessions/e0/e034bbcfb443214f252a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Default is 10 generations (Gen 0-9). Currently on Gen 8 (generating 16320/50000 samples). 8 of 10 generations completed so far.

## 产出总结

**exp_001 完成否：** 否，仍在运行。PID 59365 正在处理 Gen 8（16320/50000 samples），预计还有 Gen 8 和 Gen 9 待完成。

**完整 metrics（Gen 0-7）：**

| Gen | eff_rank | log_det | ppl | distinct4 | train_loss |
|-----|----------|---------|-----|-----------|------------|
| 0 | 417.55 | 2366.68 | 9.55 | 0.7414 | — |
| 1 | 491.77 | 2464.76 | 11.38 | 0.6256 | 1.623 |
| 2 | 496.44 | 2469.93 | 13.58 | 0.5154 | 1.268 |
| 3 | 493.31 | 2440.57 | 16.25 | 0.4900 | 1.134 |
| 4 | 485.67 | 2405.05 | 19.80 | 0.4679 | 1.098 |
| 5 | 479.21 | 2370.17 | 24.59 | 0.4630 | 1.047 |
| 6 | 473.00 | 2335.17 | 30.91 | 0.4655 | 1.025 |
| 7 | 464.20 | 2304.19 | 38.89 | 0.4474 | 1.015 |

**趋势明显：** eff_rank 从 Gen 1 峰值 496 持续下降到 464；ppl 从 9.55 指数增长到 38.89；distinct4 从 0.74 单调下降到 0.45。collapse 信号清晰。

**analyze_phase0.py / 重绘图：** 跳过，不足 10 代数据。

**清理日志：** 跳过，实验未完成。

**GPU 状态：**
- cuda:0 — 占用（PID 59365，65.9GB/97.9GB，88% util）
- cuda:1 — 占用（PID 88161/exp_003，23.7GB/97.9GB，94% util）
- **两卡均不可用。**

---

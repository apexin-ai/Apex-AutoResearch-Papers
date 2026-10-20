# analysis exp 006 metrics

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_006_metrics_20260513T233959_result.json`
- **Structured JSON:** [`aa165861c1f0da48d35c.json`](../../sessions/aa/aa165861c1f0da48d35c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_006 (fixed_dt2_v1_s1) — eval_return trajectory

| Step | eval_return | baseline | vs baseline | grad_norm | 备注 |
|------|------------|----------|-------------|-----------|------|
| 5K | 31.0 | 31.8 | **-2.5%** | 136.3 | 初始阶段持平 |
| 15K | 256.9 | 153.9 | **+66.9%** | 10.2 | 大幅领先 |
| 25K | 321.4 | 254.2 | **+26.4%** | 8.6 | 持续领先 |
| 35K | 485.3 | 290.8 | **+66.9%** | 8.6 | 优势扩大 |

**当前进度**: step=36000，下次 eval 在 45K。fps≈6.5-6.7，预计 ~23 分钟到 45K eval。

**Gate 指标确认**: 所有 checkpoint 均为 gate_dt_mean=2.0, gate_dt_std=0.0, gate_dt_2_frac=1.0 — fixed dt=2 正确生效。

**Grad norm 趋势**: 5K 时 136.3（初始波动），15K 后稳定在 8.6-10.2，训练健康。

**exp_007 (fixed_dt4_v2_s1)**: 当前 step=24000，尚未到 25K eval 点。

**关键发现**: fixed dt=2 在 35K 时 eval_return=485.3，比 baseline 290.8 高 67%，且增长斜率陡峭（25K→35K: +164 点），baseline 同区间仅 +36.6。优势在加速扩大。

---

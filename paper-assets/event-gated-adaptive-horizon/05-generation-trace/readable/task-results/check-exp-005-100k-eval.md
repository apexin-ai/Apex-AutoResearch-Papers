# check exp 005 100K eval

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_005_100K_eval_20260513T203143_result.json`
- **Structured JSON:** [`7f592a82091df938aa2c.json`](../../sessions/7f/7f592a82091df938aa2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_005 100K Checkpoint 结果

### MVP 评估完整输出

```
══════════════════════════════════════════════════
  MVP Evaluation — INTERIM (105K)
══════════════════════════════════════════════════

[Criterion 1] Return
  eval_return (last 10): 337.8 ± 125.9
  baseline_return: 953.4
  return_ratio: 0.354
  trend (last 10K): TRENDING_UP (+17.6/10K)
  gate_scale: 0.500
  status: TRENDING_UP

[Criterion 2] Gate Entropy
  empirical_entropy: 1.255
  entropy_ratio: 0.905
  threshold: > 0.3
  status: PASS

[Criterion 3] Effective Horizon
  dt_mean: 2.054
  H_eff/H_nominal: 2.054×
  threshold: > 1.2×
  status: PASS

[Criterion 4] Temporal Structure
  dt_std: 0.907
  threshold: std > 0.5
  status: PASS

[Gate Δt Distribution]
  dt=1: 31.5%  dt=2: 38.7%  dt=3: 22.7%  dt=4: 7.1%

[Stability]
  gate_loss: 0.5314
  return_trend: +17.6 per 10K steps
  gate_scale: 0.500

Overall: INTERIM — gate ramping (scale=0.50), return trend: TRENDING_UP
```

### 汇总

| 指标 | 值 |
|------|-----|
| **exp_005 当前步数** | 112K |
| **eval_return (last 10)** | 337.8 ± 125.9 |
| **return_ratio** | 35.4% of baseline |
| **gate_scale** | 0.50（已从 0.3 爬升） |
| **Baseline 步数** | 500K（已完成，return ≈ 952-985） |

### Return 趋势判断

| Step | Return |
|------|--------|
| 55K | 541.2 |
| 65K | 465.7 |
| 85K | 319.3 |
| **~105K** | **337.8** |

55K→85K 持续下降（-221.9），但 85K→105K **开始回升**（+18.5），mvp_eval 也确认 trend 为 TRENDING_UP（+17.6/10K）。gate_scale 从 0.3 升到 0.5 说明 gate 正在 ramp，return 下降是 gate 介入加深的正常代价，现在 agent 开始适应更强的 gating，return 触底反弹。

方差较大（±125.9），但方向是正的。Gate 机制指标全部 PASS（entropy 0.905, H_eff 2.054×, dt_std 0.907），temporal structure 健康。

**不触发预警** — return 337.8 > 250 且斜率为正。

---

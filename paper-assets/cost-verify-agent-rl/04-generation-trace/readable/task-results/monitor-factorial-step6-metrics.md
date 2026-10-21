# monitor factorial step6 metrics

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_factorial_step6_metrics_20260518T013857_result.json`
- **Structured JSON:** [`aba0ec0471cf37b9cb98.json`](../../sessions/ab/aba0ec0471cf37b9cb98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐了。汇报如下：

## factorial_h2_episodeadv_seed1 状态

**当前**: Step 6 正在执行 actor update，尚未出 train metrics。最新完整数据到 step 5。

### Train Metrics (Steps 1-5)

| Step | success | pass@8 | action_is_valid | entropy | kl_loss | pg_loss |
|------|---------|--------|-----------------|---------|---------|---------|
| 1 | **20.31%** | 68.75% | 85.64% | 0.359 | 0.238 | 0.0121 |
| 2 | 6.25% | 31.25% | 83.96% | 0.569 | 0.208 | 0.0118 |
| 3 | 5.47% | 31.25% | 79.54% | 0.567 | **1.077** | 0.0126 |
| 4 | **3.13%** | 18.75% | 83.70% | 0.617 | 0.638 | 0.0114 |
| 5 | **15.63%** | 62.50% | 79.92% | 0.699 | 0.735 | 0.0100 |

### Val Metrics (step 5 eval, 134 OOD episodes)

- val-env/AlfworldOOD/success: 2.24% (step 0 baseline)
- val-aux/best@8: 1.48/10
- val-aux/best@16: 3.04/10
- val-aux/best@64: 7.89/10
- critic/score/mean: 0.768

### 趋势判断

- **V 型反弹确认**: Step 1→4 持续下降 (20.31%→3.13%)，step 5 强反弹到 15.63%，pass@8 同步恢复 (18.75%→62.50%)
- **entropy 持续上升**: 0.36→0.70，探索性增加但尚未失控
- **kl_loss 在 step 3 spike 到 1.08** 后回落，当前 0.74 水平
- **action_is_valid 缓慢下降**: 85.6%→79.9%，策略正在偏离 SFT 分布
- **val 表现仍弱**: best@8 仅 1.48/10，OOD 泛化尚未显现

**判断**: 处于恢复阶段，step 5 反弹显著。需要等 step 6 metrics 确认是否延续上升趋势。按每步约 50 分钟估算，step 6 metrics 约 30-40 分钟后可用。

---

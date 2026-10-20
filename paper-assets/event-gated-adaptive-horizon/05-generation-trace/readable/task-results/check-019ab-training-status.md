# check 019ab training status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_019ab-training-status_20260517T070410_result.json`
- **Structured JSON:** [`d1a02211c2f1406d70cd.json`](../../sessions/d1/d1a02211c2f1406d70cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态汇总

### exp_019a_v2_pickcube_baseline
| 指标 | 值 |
|---|---|
| 当前步数 | **186,848 / 200,000** (93.4%) |
| 最新 eval_return | **60.39** (step 182,500) |
| 历史最高 eval_return | **69.70** (step 162,500) |
| 最近 train_return | 61.97 ~ 93.17 |
| 已用时间 | ~8h10m |
| 预估剩余 | **~35 min** (13,152 steps remaining, 按 ~375 steps/min) |

eval_return 趋势：稳步上升后在 60~70 区间波动，peak 在 step 162,500。

### exp_019b_pickcube_civo_trigger
| 指标 | 值 |
|---|---|
| 当前步数 | **63,000 / 200,000** (31.5%) |
| 最新 eval_return | **5.95** (step 62,500) |
| 历史最高 eval_return | **24.90** (step 22,500) |
| 最近 train_return | 8.05 ~ 9.27 |
| 已用时间 | ~2h48m |
| 预估剩余 | **~6h05m** (137,000 steps remaining, 按 ~375 steps/min) |

019b 的 eval_return 在 step 22,500 达到 24.9 后持续下降到 5.95，表现明显恶化。train_return 也很低（8~9），和 019a 同期（train_return 60+）差距巨大。CIVO trigger 机制目前效果不佳。

---

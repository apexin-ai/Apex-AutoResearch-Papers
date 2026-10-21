# code d146 isr s42 metrics

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d146-isr-s42-metrics_20260519T235145_result.json`
- **Structured JSON:** [`c76233c492f828b1220d.json`](../../sessions/c7/c76233c492f828b1220d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D146 isr-s42 — 已完成 (500/500)

### Last 10 steps

| step | prove_rate | ISR | reward | parse_rate |
|------|-----------|------|--------|------------|
| 491 | 0.500 | 0.156 | 0.516 | 1.0 |
| 492 | 0.500 | 0.143 | 0.514 | 1.0 |
| 493 | 1.000 | 0.199 | 1.020 | 1.0 |
| 494 | 0.500 | 0.105 | 0.511 | 1.0 |
| 495 | 1.000 | 0.253 | 1.025 | 1.0 |
| 496 | 0.500 | 0.167 | 0.517 | 1.0 |
| 497 | 0.500 | 0.188 | 0.519 | 1.0 |
| 498 | 1.000 | 0.409 | 1.041 | 1.0 |
| 499 | 0.500 | 0.188 | 0.519 | 1.0 |
| **500** | **0.000** | **0.000** | **0.000** | 1.0 |

### Every 50 steps trend

| step | prove_rate | ISR | reward |
|------|-----------|------|--------|
| 1 | 0.000 | 0.000 | 0.000 |
| 50 | 0.250 | 0.045 | 0.255 |
| 100 | 0.250 | 0.098 | 0.260 |
| 150 | 0.125 | 0.031 | 0.128 |
| 200 | **0.875** | **0.340** | 0.909 |
| 250 | **1.000** | **0.332** | 1.033 |
| 300 | 0.500 | 0.167 | 0.517 |
| 350 | 0.000 | 0.000 | 0.000 |
| 400 | 0.500 | 0.132 | 0.513 |
| 450 | 0.000 | 0.000 | 0.000 |
| 500 | 0.000 | 0.000 | 0.000 |

### Summary stats

**prove_rate distribution (500 steps):**

| prove_rate | count | pct |
|-----------|-------|------|
| 0.0 | 190 | 38.0% |
| 0.125 | 16 | 3.2% |
| 0.25 | 14 | 2.8% |
| 0.375 | 20 | 4.0% |
| **0.5** | **184** | **36.8%** |
| 0.625 | 3 | 0.6% |
| 0.75 | 6 | 1.2% |
| 0.875 | 13 | 2.6% |
| 1.0 | 54 | 10.8% |

**Mean prove_rate** = 0.354 (weighted from distribution)

高度双峰分布：38% 全失败 + 36.8% 半成功 + 10.8% 全成功。训练中后期（step 300+）基本在 {0.0, 0.5, 1.0} 之间跳动，学习已饱和。

---

## D146 isr-s43 — 进行中 (488/500)

| step | prove_rate | ISR | reward |
|------|-----------|------|--------|
| 486 | 0.500 | 0.125 | 0.513 |
| 487 | 0.500 | 0.119 | 0.512 |
| 488 | 1.000 | 0.209 | 1.021 |

剩余 12 步，预计 ~3 分钟内完成。

---

## D146 isr-s44

**NOT EXISTS**

---

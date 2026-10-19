# harvest bjb2 28827 tau sweep and status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_bjb2-28827-tau-sweep-and-status_20260525T083634_result.json`
- **Structured JSON:** [`303ae11c721c7c552553.json`](../../sessions/30/303ae11c721c7c552553.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部实验已完成，汇总如下：

---

## 1. Tau-sweep 结果 (Spatial, K=2, seed42)

| τ | Success Rate | Trigger Rate | Mean Unc. |
|---|---|---|---|
| 0.150 | **80.0%** (160/200) | 41.2% | 0.1855 |
| 0.100 | **78.0%** (156/200) | 74.4% | 0.1854 |
| 0.075 | **78.0%** (156/200) | 92.0% | 0.1811 |

趋势：τ 越小 → trigger_rate 急剧上升（41%→74%→92%），但 success_rate 基本持平（80%→78%→78%），说明更频繁触发 CRM 并没有带来额外收益，反而略降。

---

## 2. Goal 实验（全部完成）

### Adaptive (K=2, τ=0.25) paired
| Seed | Success Rate | Trigger Rate | Mean Unc. |
|---|---|---|---|
| 45 | 82.0% (164/200) | 9.4% | 0.1495 |
| 46 | **84.0%** (168/200) | 8.8% | 0.1482 |
| 47 | 82.5% (165/200) | 9.8% | 0.1499 |
| **Mean** | **82.8%** | **9.3%** | 0.1492 |

### VLA-only baseline paired
| Seed | Success Rate |
|---|---|
| 45 | 83.5% (167/200) |
| 46 | 82.0% (164/200) |
| 47 | 83.5% (167/200) |
| **Mean** | **83.0%** |

Goal benchmark 上 adaptive 82.8% vs baseline 83.0%，差异极小（-0.2pp），trigger rate 仅 ~9%，基本无干预。

---

## 3. bjb2-40593 状态

tau=0.075 实验已完成（结果在上面表格），GPU 空闲（0 MiB, 0%）。

---

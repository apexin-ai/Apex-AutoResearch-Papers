# monitor harvest loop r1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_harvest-loop-r1_20260524T191135_result.json`
- **Structured JSON:** [`6ea740aef315a514aa33.json`](../../sessions/6e/6ea740aef315a514aa33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 第一轮汇总

**已完成并收割（8/9 eval）**：
| 实验 | SR |
|------|-----|
| eval-supp-vla-only-spatial-s48 | 79.5% |
| eval-supp-vla-only-spatial-s49 | 78.5% |
| eval-supp-vla-only-goal-s48 | 85.0% |
| eval-supp-vla-only-goal-s49 | 82.0% |
| eval-supp-vla-only-obj-s48 | 79.0% |
| eval-supp-vla-only-obj-s49 | 75.5% |
| eval-supp-adapt-tau025-obj-s48 | 76.0% (trigger 3.9%) |
| eval-supp-adapt-tau025-obj-s49 | 74.0% (trigger 4.2%) |

**仍在运行**：
- **eval-adaptive-k5-spatial-tau025-s42** — task 7/10 (ramekin), rollout 10/20，估计 ~2-3h
- **train-crm-pi05-unified-3suite-r2** — epoch 24/50, loss=0.0084, best_val=0.0049

15 分钟后第二轮检查。

---

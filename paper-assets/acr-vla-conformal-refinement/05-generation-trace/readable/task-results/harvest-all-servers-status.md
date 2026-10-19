# harvest all servers status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_all-servers-status_20260526T213220_result.json`
- **Structured JSON:** [`5ff97e9755e85a09c347.json`](../../sessions/5f/5ff97e9755e85a09c347.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。汇总如下：

---

## 服务器状态汇总

### bjb2-24035 (1×4090D)
| GPU | 显存 | 状态 |
|-----|------|------|
| 0 | 0 MiB | **IDLE** |

| 实验 | 状态 | SR | TR | tau |
|------|------|----|----|-----|
| eval-k2-tau045-spatial-s42-bjb2 | **DONE** | **78.0%** | 8.05% | 0.45 |

空闲 GPU: **1/1**

---

### bjb1-18228 (4×4090)
| GPU | 显存 | 状态 |
|-----|------|------|
| 0 | 0 MiB | **IDLE** |
| 1 | 0 MiB | **IDLE** |
| 2 | 0 MiB | **IDLE** |
| 3 | 0 MiB | **IDLE** |

| 实验 | 状态 | SR | TR | tau |
|------|------|----|----|-----|
| spatial-adaptive-tau035-k2-s42 | **DONE** | **78.0%** | 12.35% | 0.35 |
| spatial-adaptive-tau045-k2-s42 | **DONE** | **80.0%** | 7.29% | 0.45 |
| spatial-crm-norm005-s42-d149 | **DONE** | **80.5%** | — | — |

空闲 GPU: **4/4**

---

### bjb1-32546 (6×4090)
| GPU | 显存 | 状态 |
|-----|------|------|
| 0 | 10780 MiB | **BUSY** (adaptive-long-s43) |
| 1 | 10780 MiB | **BUSY** (adaptive-long-s44) |
| 2 | 2 MiB | **IDLE** |
| 3 | 2 MiB | **IDLE** |
| 4 | 2 MiB | **IDLE** |
| 5 | 2 MiB | **IDLE** |

| 实验 | 状态 | SR |
|------|------|-----|
| pi05-adaptive-long-s43-bjb1 (PID 903950) | **RUNNING** ~75% (7/10 tasks done) | — |
| pi05-adaptive-long-s44-bjb1 (PID 904305) | **RUNNING** ~75% (7/10 tasks done) | — |
| eval-crm-spatial-s48-d149-bjb1 | **DONE** | **80.5%** |
| eval-crm-goal-s43-d149-bjb1 | **DONE** | **82.0%** |
| eval-crm-object-s42-d149-bjb1 | **DONE** | **77.0%** |
| eval-crm-object-s43-d149-bjb1 | **DONE** | **78.5%** |

空闲 GPU: **4/6**

---

### cqa1-32758 (6×4090D)
| GPU | 显存 | 状态 |
|-----|------|------|
| 0-5 | 全部 0 MiB | **ALL IDLE** |

空闲 GPU: **6/6**

---

### westd-49937 (6×RTX PRO 6000)
| GPU | 显存 | 状态 |
|-----|------|------|
| 0-5 | 全部 0 MiB | **ALL IDLE** |

空闲 GPU: **6/6**

---

## 总览

| 指标 | 值 |
|------|-----|
| 总 GPU | 23 |
| 空闲 GPU | **21** |
| 运行中实验 | 2 (bjb1-32546 上的 adaptive-long s43/s44，预计数小时内完成) |
| 已完成实验 | 7 个有新结果 |

---

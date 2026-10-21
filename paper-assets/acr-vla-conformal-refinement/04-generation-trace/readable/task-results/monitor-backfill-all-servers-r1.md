# monitor backfill all servers r1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_backfill-all-servers-r1_20260528T110527_result.json`
- **Structured JSON:** [`29b136a4a1bdbca486a7.json`](../../sessions/29/29b136a4a1bdbca486a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有工作完成。汇总如下：

---

## 汇总报告

### 一、各服务器 GPU 状态（全部 22 GPU 均已占用）

**bjb1-18228**（4 GPU）
| GPU | 实验 | 状态 |
|-----|------|------|
| 0 | eval-supp-long-adapt-tau025-s44 | 🆕 刚部署 |
| 1 | eval-supp-long-adapt-tau025-s45 | 🆕 刚部署 |
| 2 | pi05-crm-always-on-long-s44 | 运行中 |
| 3 | eval-supp-long-adapt-tau025-s46 | 🆕 刚部署 |

**bjb1-32546**（6 GPU）
| GPU | 实验 | 状态 |
|-----|------|------|
| 0 | eval-supp-long-adapt-tau025-s42 | 🆕 刚部署 |
| 1 | eval-supp-long-adapt-tau025-s43 | 🆕 刚部署 |
| 2 | eval-obs-only-object-norm003-seed65 | 运行中 |
| 3 | eval-obs-only-object-norm005-seed64 | 运行中 |
| 4 | eval-obs-only-object-norm01-seed74 | 运行中 |
| 5 | eval-obs-only-object-norm003-seed73 | 运行中 |

**bjb2-28827**（6 GPU）
| GPU | 实验 | 状态 |
|-----|------|------|
| 0 | **pi05-adaptive-goal-s44-backfill** (P0) | 🆕 刚部署 |
| 1 | eval-supp-long-adapt-tau025-s47-r2 | 运行中 |
| 2 | **pi05-crm-k2-long-s42-backfill** (P1) | 🆕 刚部署 |
| 3 | **pi05-crm-k2-long-s43-backfill** (P2) | 🆕 刚部署 |
| 4 | eval-obs-only-object-norm01-seed66 | 运行中 |
| 5 | eval-supp-long-vla-only-s46 | 运行中 |

**cqa1-32758**（6 GPU）— 全部忙碌，无空闲 GPU

### 二、已收割完成实验（14 条 → DONE）

| 实验 | SR | 服务器 |
|------|-----|--------|
| pi05-crm-always-on-goal-s43 | **82.5%** | bjb1-32546 |
| pi05-crm-always-on-goal-s44 | **83.5%** | bjb1-32546 |
| pi05-crm-always-on-object-s44 | **89.5%** | bjb1-32546 |
| pi05-crm-always-on-long-s43 | **79.5%** | bjb1-18228 |
| eval-random-selection-object-s43-v2 | **77.0%** | bjb1-32546 |
| eval-ksweep-k20-obs-object-s44 | **71.0%** | bjb1-32546 |
| eval-ksweep-k20-obs-obj-s43 | **77.0%** | bjb1-32546 |
| eval-supp-long-vla-only-s44 | **60.5%** | bjb1-18228 |
| eval-supp-long-vla-only-s42 | **59.5%** | bjb1-18228 |
| smolvla-adapt-tau015-object-s42 | **79.0%** | cqa1-32758 |
| smolvla-adapt-tau015-object-s43 | **78.0%** | cqa1-32758 |
| smolvla-adapt-tau015-object-s44 | **73.5%** | cqa1-32758 |
| eval-supp-spatial-k2mean-s47 | **82.0%** | cqa1-32758 |
| eval-supp-spatial-adapt-tau025-s47 | **79.5%** | cqa1-32758 |

### 三、新部署实验（8 个）

| 优先级 | exp_id | 服务器 | GPU |
|--------|--------|--------|-----|
| **P0** | pi05-adaptive-goal-s44-backfill | bjb2-28827 | 0 |
| **P1** | pi05-crm-k2-long-s42-backfill | bjb2-28827 | 2 |
| **P2** | pi05-crm-k2-long-s43-backfill | bjb2-28827 | 3 |
| **P3** | eval-supp-long-adapt-tau025-s42 | bjb1-32546 | 0 |
| **P3** | eval-supp-long-adapt-tau025-s43 | bjb1-32546 | 1 |
| **P3** | eval-supp-long-adapt-tau025-s44 | bjb1-18228 | 0 |
| **P3** | eval-supp-long-adapt-tau025-s45 | bjb1-18228 | 1 |
| **P3** | eval-supp-long-adapt-tau025-s46 | bjb1-18228 | 3 |

### 四、空闲 GPU

**无** — 全部 22 张 GPU 均已占满。P4（SmolVLA supplementary 短实验）需等待 GPU 释放后部署。

### 五、备注

- Pi05 checkpoint 在全部 4 台服务器上均可用
- eval-supp-long-adapt-tau025-s42/s43/s44/s45/s46 的 registry 条目因是旧 exp_id 的重跑，状态显示异常（DEPLOYED/DONE），但实验实际已在服务器上运行
- P1/P2（Pi05 Long CRM）预计 ~9h，无法在 DDL 前完成但已启动

---

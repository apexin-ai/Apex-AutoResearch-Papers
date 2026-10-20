# monitor training progress check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training-progress-check_20260526T061658_result.json`
- **Structured JSON:** [`2b34506b13e5404bb010.json`](../../sessions/2b/2b34506b13e5404bb010.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the progress report:

---

## 训练进度报告 (2026-05-26)

### 1. exp_097_cheetah_008d_s3 (PID 3794, cuda:0)

| 指标 | 值 |
|------|-----|
| **当前 step** | **65000 / 105000** (61.9%) |
| **运行时间** | ~3h |
| **最新 fps** | 6.5 (eval 期间会降至 ~2) |
| **预估剩余** | 40000 steps ÷ ~6 fps ≈ **1.9h**，预计 ~2h 后完成 |

**eval_return 轨迹:**
| 5K | 15K | 25K | 35K | 45K | 55K | 65K |
|-----|------|------|------|------|------|------|
| 8.7 | 216.6 | 139.4 | 105.3 | 23.4 | 68.2 | **182.5** |

**CIVO / ve_ratio 轨迹:**
| 15K | 25K | 35K | 45K | 55K |
|-----|-----|-----|------|-----|
| 0.0 | 0.1 | 0.3 | **2.3** (alert!) | 0.8 |

**关键发现 — CIVO onset 已确认：**
- step 45K 出现 ve_ratio=2.3, delta_ve=1.9, civo/alert=1.0，CIVO detector 触发警告
- step 55K 回落至 ve_ratio=0.8（瞬态 spike，非持续升高）
- 但 onset 已触发 → **s3 = onset**
- **Cheetah C1 onset rate: 3/4** (s0=onset, s1=no, s2=onset, s3=onset)

**异常信号：** eval_return 波动较大（216→23→68→182），不稳定但仍在学习中。训练正常。

---

### 2. exp_100_walker_008a_s1 (PID 5591, cuda:1)

| 指标 | 值 |
|------|-----|
| **当前 step** | **~56000 / 105000** (53.3%) |
| **运行时间** | ~2h39m |
| **最新 fps** | 8.2 |
| **预估剩余** | 49000 steps ÷ ~8 fps ≈ **1.7h**，预计 ~1.7h 后完成 |

**eval_return 轨迹:**
| 5K | 15K | 25K | 35K | 45K | 55K |
|-----|------|------|------|------|------|
| 31.0 | 168.8 | 158.0 | 202.9 | 306.0 | **457.3** |

**ve_ratio 轨迹:**
| 15K | 25K | 35K | 45K | 55K |
|-----|-----|-----|-----|-----|
| 0.0 | 0.2 | 0.3 | 0.3 | **0.2** |

**关键发现 — 符合预期（无 CIVO）：**
- ve_ratio 稳定在 0.2-0.3，远低于 1.5x 阈值，无 onset 信号
- eval_return 单调上升，55K 已达 457.3（Walker Walk 接近良好水平）
- 符合 008a 预期的 "value suppression" pattern：gate_fixed_dt=2 限制 horizon 但不引发 CIVO

**无异常信号。** 训练健康，学习曲线平稳上升。

---

### 总结

| 实验 | 进度 | 预估完成 | CIVO onset | 状态 |
|------|------|---------|------------|------|
| exp_097 (Cheetah s3) | 65K/105K (62%) | ~2h | **YES** (45K) | 正常，波动大 |
| exp_100 (Walker s1) | 56K/105K (53%) | ~1.7h | No | 正常，稳步上升 |

exp_097 的 onset 确认将 Cheetah C1 onset rate 推至 **3/4 (75%)**。

---

# status exp 035 exp 036 check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_exp_035_exp_036_check_20260521T121619_result.json`
- **Structured JSON:** [`7cbb0ddabd868b05a304.json`](../../sessions/7c/7cbb0ddabd868b05a304.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

---

### 1. exp_035_narrow_dual_critic_walker (bjb1-40020:cuda:1)

| 项目 | 值 |
|------|-----|
| **状态** | 运行中 (PID 162900, 已运行 4h21m) |
| **当前步数** | 120,000 / 210,000 (57%) |
| **FPS** | ~7.3–7.6 |
| **预计剩余** | ~90k steps ÷ 7.4 fps ≈ **3.4 小时** |

**Eval return 轨迹**:
| Step | 5k | 15k | 25k | 35k | 95k | 105k | 115k |
|------|-----|------|------|------|------|-------|-------|
| eval_return | 35.6 | 94.9 | 152.9 | 106.8 | 66.5 | 64.2 | **114.8** |

**NVE (ve_ratio) 轨迹**:
| Step | 15k | 25k | 35k | 95k | 105k | 115k |
|------|------|------|------|------|-------|-------|
| ve_ratio | 0.0 | 0.1 | 0.2 | 1.2 | 1.3 | **0.7** |

- CIVO alert 全程 0.0，无异常
- Gate 固定 dt=2（100% dt_2_frac），符合预期
- train_return 在 100k-120k 波动大（56.9–204.9），eval 在 115k 回升到 114.8

---

### 2. exp_036_dual_critic_pickcube (bjb1-45299:cuda:0)

| 项目 | 值 |
|------|-----|
| **状态** | 运行中 (PID 2476, 已运行 3h33m) |
| **当前步数** | 73,647 / 200,000 (37%) |
| **FPS** | ~5.6 |
| **预计剩余** | ~126k steps ÷ 5.6 fps ≈ **6.3 小时** |

**Eval return 轨迹**:
| Step | 2.5k | 12.5k | 22.5k | 32.5k | 62.5k | 72.5k |
|------|-------|--------|--------|--------|--------|--------|
| eval_return | 2.0 | 17.5 | 17.5 | 11.6 | 18.8 | **5.4** |

**NVE (ve_ratio) 轨迹**:
| Step | 12.5k | 22.5k | 32.5k | 62.5k | 72.5k |
|------|--------|--------|--------|--------|--------|
| ve_ratio | 0.2 | 1.0 | 2.3 | 0.6 | **1.6** |

- CIVO alert 全程 0.0
- Gate 固定 dt=2
- eval_return 在 72.5k 下降到 5.4，train_return 方差很大（0.4–22.3），学习不稳定

---

### 3. GPU 使用状况

| 服务器 | GPU | 型号 | 利用率 | 显存占用 | 状态 |
|--------|-----|------|--------|----------|------|
| bjb1-40020 | 0 | RTX 4090 (24GB) | 0% | 1 MiB | **空闲** |
| bjb1-40020 | 1 | RTX 4090 (24GB) | 25% | 3.1 GB | exp_035 |
| bjb1-45299 | 0 | RTX PRO 6000 Blackwell (98GB) | 16% | 3.1 GB | exp_036 |
| bjb1-45299 | 1 | RTX PRO 6000 Blackwell (98GB) | 0% | 4 MiB | **空闲** |

两台服务器各有一张卡空闲（bjb1-40020:cuda:0, bjb1-45299:cuda:1）。

---

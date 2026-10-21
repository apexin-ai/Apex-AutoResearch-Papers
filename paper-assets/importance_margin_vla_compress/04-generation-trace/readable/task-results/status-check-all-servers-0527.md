# status check all servers 0527

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_check_all_servers_0527_20260527T025759_result.json`
- **Structured JSON:** [`cb5d4e918ecc5af4610e.json`](../../sessions/cb/cb5d4e918ecc5af4610e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。现在汇总所有结果。

## 全局 GPU 状态汇总（2026-05-27 ~11:00 UTC）

---

### westd-38929（4× RTX PRO 6000, 98GB）

| GPU | 实验 | PID | 状态 | 进度/结果 |
|-----|------|-----|------|-----------|
| 0 | **Attn k=0.95 Goal** | 949253 | 🔄 运行中 | Task 4/10, Ep 40/50 (~1.8 eps/min) |
| 1 | **L2norm k=0.95 Long** | 949447 | 🔄 运行中 | Task 2/10, Ep 30/50 (~0.8 eps/min) |
| 2 | **L2norm k=0.75 Long v2** + 共享进程 | 968309 (+965423) | 🔄 运行中 | Task 1/10, Ep 30/50 (~0.5 eps/min) |
| 3 | **Attn k=0.95 Long** | 950007 | 🔄 运行中 | Task 2/10, Ep 20/50 (~0.8 eps/min) |

**注意**: GPU 2 有两个进程共享（32GB 已用），速度可能受影响。GPU 0 上用户预期中没有该实验，是新增的 Attn k=0.95 Goal。

---

### westd-41074（4× RTX PRO 6000, 98GB）

| GPU | 实验 | PID | 状态 | 进度/结果 |
|-----|------|-----|------|-----------|
| 0 | **Random k=0.95 Long** | 32184 | 🔄 运行中 | Task 3/10, Ep 10/50 (~0.8 eps/min) |
| 1 | **Random k=0.75 Long** | 856656 | 🔄 运行中 | Task 9/10 开始（接近完成） |
| 2 | ~~π0.5 Random k=0.85 Long strict~~ | — | ✅ 已完成/空闲 | 1 MiB VRAM, GPU 空闲 |
| 3 | ~~Attn k=0.75 Long~~ | — | ✅ 已完成/空闲 | 1 MiB VRAM, GPU 空闲 |

---

### westd-27271（2× RTX PRO 6000, 98GB）

| GPU | 实验 | PID | 状态 | 进度/结果 |
|-----|------|-----|------|-----------|
| 0 | **L2norm k=0.95 Goal** | 609731 | 🔄 运行中 | Task 8/10, Ep 10/50（接近完成） |
| 1 | **Attn k=0.95 Object** | 638225 | 🔄 运行中 | Task 4/10, Ep 20/50 (~2.0 eps/min) |

---

### cqa1-33015（4× RTX 4090D, 24GB）

| GPU | 实验 | PID | 状态 | 进度/结果 |
|-----|------|-----|------|-----------|
| 0 | **Random k=0.95 Goal** | 896333 | 🔄 运行中 | Task ?, Ep 40/50 (~1.2 eps/min) |
| 1 | **Attn k=0.95 Goal** | 898055 | 🔄 运行中 | Task ?, Ep 40/50 (~1.2 eps/min) |
| 2 | IDLE | — | — | 空闲 |
| 3 | **Attn k=0.5 Goal** | 897100 | 🔄 运行中 | Task 1/10, Ep 30/50 (~0.9 eps/min) |

---

### 最近完成的关键结果（OpenVLA SR）

**westd-38929 上已完成的结果:**
| 文件 | SR |
|------|-----|
| openvla_l2norm_prune_k05_10 | 0.164 |
| openvla_random_prune_k085_10 | 0.450 |
| openvla_attention_prune_k085_10 | 0.458 |
| openvla_random_prune_k075_goal | 0.720 |
| openvla_random_prune_k085_goal | 0.786 |
| openvla_attention_prune_k07_goal | 0.664 |
| openvla_attention_prune_k085_goal | 0.746 |

**westd-41074 上已完成的结果:**
| 文件 | SR |
|------|-----|
| openvla_random_prune_k095_object | 0.674 |
| openvla_random_prune_k075_object | 0.504 |
| openvla_attention_prune_k075_object | 0.532 |
| openvla_l2norm_prune_k095_object | 0.706 |
| openvla_l2norm_prune_k085_object | 0.552 |
| openvla_l2norm_prune_k075_object | 0.574 |
| openvla_random_prune_k085_10 | 0.452 |

**westd-27271 上已完成的结果:**
| 文件 | SR |
|------|-----|
| openvla_attention_prune_k05_10 | 0.146 |
| openvla_attention_prune_k075_goal | 0.674 |
| openvla_attention_prune_k09_goal | 0.732 |
| openvla_l2norm_prune_k075_goal | 0.702 |
| openvla_l2norm_prune_k085_goal | 0.754 |
| openvla_l2norm_prune_k09_goal | 0.748 |
| openvla_baseline_goal | 0.748 |
| openvla_baseline_10 | 0.528 |
| openvla_baseline_spatial | 0.800 |
| openvla_baseline_object | 0.740 |

**cqa1 上最新 π0.5 结果:**
| 文件 | SR |
|------|-----|
| pi05_l2norm_k0.85_10 | 0.778 |
| pi05_random_k0.70_10 | 0.624 |
| pi05_attention_k0.70_10 | 0.508 |
| pi05_attention_k0.95_10 | 0.770 |
| pi05_l2norm_k0.95_goal | 0.908 |
| pi05_random_k0.95_goal | 0.840 |

---

### 汇总

- **总计 12 个 GPU 运行实验，4 个 GPU 空闲**（westd-41074 GPU 2/3, cqa1 GPU 2）
- westd-41074 GPU 2/3 上的实验已完成退出，可以立即安排新任务
- cqa1 GPU 2 空闲
- **预估完成时间**（基于当前进度和速度）：
  - **最快完成**: westd-27271 GPU 0 (L2norm k=0.95 Goal, Task 8/10) — 约 2-3h
  - **次快**: westd-41074 GPU 1 (Random k=0.75 Long, Task 9/10) — 约 1-2h
  - **最慢**: westd-38929 GPU 1/2/3 (Task 1-2/10) — 约 6-8h+，可能赶不上截止时间
- **截止提醒 (C002)**: 距离 2026-05-28 12:00 UTC 还剩约 25h，但 Task 1-2/10 的实验以当前速度需 8h+，应能完成

---

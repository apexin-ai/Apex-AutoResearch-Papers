# ops audit westd27271 harvest

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_audit_westd27271_harvest_20260522T150629_result.json`
- **Structured JSON:** [`91d8d041c80ea01d910c.json`](../../sessions/91/91d8d041c80ea01d910c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇报如下：

---

## westd-27271 X-VLA 实验状态报告

### 1. 已完成实验（re-run baselines on westd-27271）

| 实验 | SR (旧 cqa1-33015) | SR (新 westd-27271) | 状态 |
|---|---|---|---|
| **Spatial baseline** (k=1.0) | 91.6% | **93.0%** | 已在 registry（DONE） |
| **Goal baseline** (k=1.0) | 98.0% | **98.4%** | 已在 registry（DONE） |

结果文件: `eval_results/xvla_prune_k1.0_libero_spatial.json`, `eval_results/xvla_prune_k1.0_libero_goal.json`

### 2. 正在运行的实验

**cuda:0 — L2norm k=0.95 Spatial** (`xvla_spatial` tmux, task 4 ~ep45/50)

| Task | Baseline SR | L2norm k=0.95 SR | 变化 |
|---|---|---|---|
| 0 | 98% | **100%** | +2 |
| 1 | 100% | **54%** | **-46** |
| 2 | 100% | **96%** | -4 |
| 3 | 98% | **100%** | +2 |
| 4-9 | — | 进行中 | — |

**cuda:1 — L2norm k=0.95 Goal** (`xvla_goal` tmux, task 5 ~ep11/50)

| Task | Baseline SR | L2norm k=0.95 SR | 变化 |
|---|---|---|---|
| 0 | 100% | **100%** | 0 |
| 1 | 100% | **38%** | **-62** |
| 2 | 96% | **94%** | -2 |
| 3 | 98% | **24%** | **-74** |
| 4 | 100% | **18%** | **-82** |
| 5 | 96% | 运行中 (0/11全失败) | — |
| 6-9 | — | 待运行 | — |

**关键发现：L2norm k=0.95 在 Goal suite 上表现灾难性，仅去掉 5% token 就导致多个 task 从 98-100% 暴跌到 18-38%。Spatial 上也有 Task 1 从 100% 跌到 54%。假设（2-3%以内降幅）被强烈否定。**

### 3. 自动化队列（无需手动部署）

**cuda:0 链** (`xvla_spatial` → `xvla_long`):
- ✅ Spatial baseline
- 🔄 Spatial l2norm k=0.95（运行中）
- ⏳ Spatial l2norm k=0.9, k=0.7
- ⏳ Long baseline → l2norm k=0.95/0.9/0.7

**cuda:1 链** (`xvla_goal` → `xvla_random`):
- ✅ Goal baseline
- 🔄 Goal l2norm k=0.95（运行中）
- ⏳ Goal l2norm k=0.9, k=0.7
- ⏳ Random k=0.95/0.9/0.7 × {object, spatial, goal, long}（12个实验）

### 4. Registry 更新

- `eval_xvla_baseline_spatial_seed42` — 已存在（DONE, hypothesis 已更新）
- `eval_xvla_baseline_goal_seed42` — 已存在（DONE, hypothesis 已更新）
- `eval_xvla_l2norm_k095_spatial_seed42` — **新注册 → RUNNING**
- `eval_xvla_l2norm_k095_goal_seed42` — **新注册 → RUNNING**

### 5. GPU 空闲情况

**无空闲 GPU**。两张卡各自有完整的自动化链在排队，预计总运行时间 ~20+ 小时。

---

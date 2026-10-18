# ops harvest westd38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-westd38929_20260524T081656_result.json`
- **Structured JSON:** [`de6697f4723464be55ad.json`](../../sessions/de/de6697f4723464be55ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### GPU 运行状态

与预期不同，**GPU 0/1 并非空闲**，3 个 GPU 都在运行 π0.5 实验：

| GPU | 实验 | Status | 当前进度 | 累计 SR |
|-----|------|--------|----------|---------|
| **0** | eval_pi05_random_k09_goal_seed42_postfix | **RUNNING** | Task 5/10 开始 (T4=90%) | 137/250 = 54.8% |
| **1** | eval_pi05_random_k085_goal_seed42_postfix | **RUNNING** | Task 4/10 开始 (T3=30%) | 61/200 = 30.5% |
| **2** | eval_pi05_random_k07_goal_seed42_postfix | **RUNNING** | Task 5/10 开始 (T4=96%) | 195/250 = 78.0% |
| **3** | — | **IDLE** | — | — |

3 个 π0.5 实验都在 15:32 启动，运行约 45 分钟，预计还需 ~45-60 分钟完成全部 10 个 task。

---

### GPU 3 已完成实验

**1. eval_xvla_l2norm_k03_goal_seed42 (X-VLA L2norm k=0.3 Goal)**
- 完成时间: 15:53
- 结果: `eval_results/xvla_prune_k0.3_libero_goal.json`
- **SR = 0.2%** (1/500), 几乎完全失败，只有 Task 7 "turn on the stove" 成功 1 次
- 500 episodes, seed=42

**2. eval_xvla_random_k05_spatial_seed43 (X-VLA Random k=0.5 Spatial)**
- 完成时间: 07:29
- 结果: `eval_results/eval_xvla_random_k05_spatial_seed43.json`
- **SR = 72.6%** (363/500), 95% CI [68.5%, 76.3%]
- 500 episodes, seed=43
- Per-task: 100%, 38%, 88%, 92%, 88%, 0%, 94%, 68%, 92%, 66%

**3. 两个 k=0.3 Long 实验 — 已终止/失败**
- `eval_xvla_l2norm_k03_long_seed42` — 日志停在 15:31, Task 0 Ep 22, 全部 FAIL
- `eval_xvla_random_k03_long_seed42` — 日志停在 15:31, Task 0 Ep 29, 全部 FAIL
- 无结果 JSON，疑似被手动 kill

---

### 今日已完成的全部 X-VLA 结果汇总

**L2norm 模式:**

| k | Goal | Spatial | Object | Long (10) |
|---|------|---------|--------|-----------|
| 0.30 | **0.2%** | 31.2% | — | stalled |
| 0.50 | 59.0% | 58.8% | 43.0% | 44.6% |
| 0.70 | 51.8% | 72.8% | — | — |

**Random 模式 (k=0.85):**

| Suite | SR |
|-------|----|
| Goal | 60.4% |
| Spatial | 68.2% |
| Object | 65.0% |
| Long (10) | 35.0% |

**Random k=0.5 seed43:** Spatial = 72.6%

**Attention-based (已有结果):** attention_last/mean/rollout 在 k=0.3-0.5 普遍 SR > 90%，远优于 L2norm/Random。

---

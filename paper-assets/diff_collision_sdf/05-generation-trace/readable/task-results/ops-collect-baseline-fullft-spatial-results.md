# ops collect baseline fullft spatial results

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect_baseline_fullft_spatial_results_20260522T194154_result.json`
- **Structured JSON:** [`0576f403ffd75df68160.json`](../../sessions/05/0576f403ffd75df68160.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。汇总如下：

## eval_baseline_fullft_spatial_v11 结果

**状态**: DONE (800 episodes, 4 tasks × 200 eps)，conclusion = **negative**

### Per-task metrics

| Task | TSR | CAR | Avg Max Disp | Smoothness |
|------|-----|-----|-------------|------------|
| T0: pick bowl between plate & ramekin | **1.5%** (3/200) | **0.0%** | 0.3317m | 0.003487 |
| T1: pick bowl on ramekin | 0.0% | 0.0% | 0.2863m | 0.003260 |
| T2: pick bowl on stove | 0.0% | 0.0% | 0.2604m | 0.002417 |
| T3: pick bowl on cabinet | 0.0% | 0.0% | 0.3017m | 0.003154 |
| **Overall** | **0.4%** | **0.0%** | **0.295m** | - |

### 与 LoRA baseline spatial 对比

| 指标 | LoRA baseline | Full-FT baseline |
|------|--------------|-----------------|
| Avg TSR | ~0% | 0.4% |
| Avg CAR | **0.0%** | **0.0%** |
| 结论 | 全部碰撞 | 全部碰撞 |

**核心发现**: Full-FT baseline 在 spatial_bowl Level II 上 CAR 也是 0%——几乎所有 episode 都在极早期（step 4-37）碰撞。这不是 LoRA 容量瓶颈问题，而是 **spatial 场景本身对碰撞避免极其困难**（碰撞来自 arm body 而非 end-effector）。

### GPU 状态

| GPU | Memory Used | Utilization |
|-----|-------------|-------------|
| 0 | 8634 MiB | 50% |
| **1** | **1 MiB** | **0%** |
| 2 | 8640 MiB | 47% |
| 3 | 8546 MiB | 48% |

**GPU 1 已释放**，空闲可用。

---

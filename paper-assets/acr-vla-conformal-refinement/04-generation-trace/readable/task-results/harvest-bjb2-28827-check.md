# harvest bjb2 28827 check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_bjb2-28827-check_20260526T020543_result.json`
- **Structured JSON:** [`642e7057bc3b3ef63723.json`](../../sessions/64/642e7057bc3b3ef63723.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb2-28827 状态报告

### 已完成实验结果 (6/6)

| 实验 | SR | trigger | 备注 |
|---|---|---|---|
| Spatial Adaptive τ=0.40 s42 | **0.780** | 9.87% | 10 tasks × 20 rollouts |
| Spatial Adaptive τ=0.45 s42 | **0.800** | 7.23% | trigger 最低 |
| Goal VLA-only s45 (paired r2) | **0.830** | — | baseline |
| Goal Adaptive s45 (paired r2) | **0.825** | 9.19% | -0.5pp vs VLA |
| Goal VLA-only s47 (paired r2) | **0.830** | — | baseline |
| Goal Adaptive s47 (paired r2) | **0.820** | 9.66% | -1.0pp vs VLA |

**观察**：Goal paired s45/s47 上 Adaptive 几乎与 VLA-only 持平（-0.5 ~ -1.0pp），与之前 Goal 上 Adaptive 通常持平或微弱劣势的趋势一致。Spatial τ-sweep 显示 τ=0.45 略优于 τ=0.40 (+2pp)。

### 新部署实验 (6/6 RUNNING)

| GPU | 实验 ID | tmux |
|---|---|---|
| 0 | eval-goal-vla-only-s49-paired | goal_vla_s49 |
| 1 | eval-goal-adapt-tau025-s49-paired | goal_adapt_s49 |
| 2 | eval-spatial-vla-only-s46-paired | spatial_vla_s46 |
| 3 | eval-spatial-adapt-tau025-s46-paired | spatial_adapt_s46 |
| 4 | eval-spatial-vla-only-s48-paired | spatial_vla_s48 |
| 5 | eval-spatial-adapt-tau025-s48-paired | spatial_adapt_s48 |

全部 6 个 GPU 在用 (5-6GB allocated)，全部加载了 10 tasks。CRM checkpoint 路径 `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt` 已确认。

### 磁盘状态

根分区 **4.3G free / 30G total (86%)**。`.cache` 6GB、`miniconda3` 25GB 是主要占用，但稳定不增长。Eval 日志/JSON 共 22MB，新增 6 个实验预计 < 200KB，无需立即清理。

---

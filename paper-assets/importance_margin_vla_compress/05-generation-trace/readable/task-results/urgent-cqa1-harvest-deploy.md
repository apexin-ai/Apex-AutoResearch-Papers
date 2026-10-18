# urgent cqa1 harvest deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_cqa1-harvest-deploy_20260524T021342_result.json`
- **Structured JSON:** [`731d3d6d4719d6aaae6a.json`](../../sessions/73/731d3d6d4719d6aaae6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## Phase 1: 收割结果

| 实验 | Suite | k | SR | Episodes | 状态 |
|------|-------|---|-----|----------|------|
| eval_pi05_random_k095_object_seed42_v2 | Object | 0.95 | **74.0%** | 500 | DONE ✓ |
| eval_pi05_random_k07_object_seed42_v4 | Object | 0.7 | **74.0%** | 500 | DONE ✓ |

两个 keep ratio (0.95 vs 0.7) 在 Object suite 上 SR 完全一致 (74.0%)，说明 random pruning 在 Object 上极度鲁棒，移除 30% token 无性能损失。

## Phase 2: 部署新实验

| 实验 | GPU | k | Suite | PID | tmux session |
|------|-----|---|-------|-----|-------------|
| eval_pi05_random_k05_spatial_seed42_postfix_v3 | 0 | 0.5 | Spatial | 697716 | eval_pi05_random_k05_spatial_seed42_postfix_v3 |
| eval_pi05_random_k085_spatial_seed42_postfix_v2 | 1 | 0.85 | Spatial | 697975 | eval_pi05_random_k085_spatial_seed42_postfix_v2 |
| eval_pi05_random_k09_spatial_seed42_postfix_v2 | 2 | 0.9 | Spatial | 698140 | eval_pi05_random_k09_spatial_seed42_postfix_v2 |

3 个实验进程存活，模型正在加载中。GPU 3 继续跑 `eval_pi05_l2norm_k085_goal_seed43`（当前 T8，SR ~91.2%）。4 块 GPU 满载。预计 ~2h 完成。

---

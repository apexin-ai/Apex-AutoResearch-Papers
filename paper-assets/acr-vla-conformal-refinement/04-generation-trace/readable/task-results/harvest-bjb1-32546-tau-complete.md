# harvest bjb1 32546 tau complete

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_bjb1-32546-tau-complete_20260526T020511_result.json`
- **Structured JSON:** [`ab01fe561010e1dd0098.json`](../../sessions/ab/ab01fe561010e1dd0098.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 6 GPUs active (5.5-6.2 GiB each, ~22% util). All 6 experiments registered as RUNNING.

## Spatial τ-sweep 结果（seed=42, K=2, max_norm=0.2）

| τ    | SR    | trigger_rate |
|------|-------|--------------|
| 0.05 | 0.785 | 0.994        |
| 0.10 | 0.770 | 0.746        |
| 0.15 | 0.785 | 0.410        |
| 0.20 | **0.810** | 0.267    |
| 0.30 | 0.795 | 0.168        |
| 0.35 | 0.795 | 0.123        |

**关键观察**：τ=0.20 是当前最优（SR=0.81），低 τ 过度触发反而降低 SR（0.05 → 0.785）。τ≥0.20 后 SR 稳定在 0.795-0.81。趋势暗示 τ=0.25 可能持平或微降。

## 新部署实验（bjb1-32546, 6 GPU）

| GPU | Session              | 实验                       | Checkpoint    |
|-----|----------------------|---------------------------|---------------|
| 0   | tau025_spatial_s42   | Spatial τ=0.25 s42        | autodl-tmp    |
| 1   | tau025_goal_s42      | Goal τ=0.25 s42           | autodl-tmp    |
| 2   | tau040_goal_s42      | Goal τ=0.40 s42           | autodl-tmp    |
| 3   | tau045_goal_s42      | Goal τ=0.45 s42           | autodl-tmp    |
| 4   | goal_vla_s48         | Goal VLA-only s48         | -             |
| 5   | goal_adapt_s48       | Goal Adaptive τ=0.25 s48  | autodl-tmp    |

Checkpoint 路径确认为 `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt`（项目目录下无 checkpoint）。

---

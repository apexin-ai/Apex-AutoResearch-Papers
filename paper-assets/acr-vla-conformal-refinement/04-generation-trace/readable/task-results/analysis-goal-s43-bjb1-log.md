# analysis goal s43 bjb1 log

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_goal-s43-bjb1-log_20260526T102753_result.json`
- **Structured JSON:** [`d62ce085882bba72a4b7.json`](../../sessions/d6/d62ce085882bba72a4b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

=== 任务1: pi05-adaptive-goal-s43-bjb1-18228 详细指标 ===
- **overall_success_rate: 89.5% (179/200)**
- **trigger_rate: 8.7%** (2280 / 26269 steps)
- mean_uncertainty: 0.119, tau: 0.25, mean_correction_norm: 0.20
- 总 rollouts: 200 (10 tasks × 20 rollouts)
- per_task:
  - open_the_middle_drawer_of_the_cabinet: 17/20 (85%)
  - put_the_bowl_on_the_stove: 20/20 (100%)
  - put_the_wine_bottle_on_top_of_the_cabinet: 16/20 (80%)
  - open_the_top_drawer_and_put_the_bowl_inside: 12/20 (60%) ← 最低
  - put_the_bowl_on_top_of_the_cabinet: 20/20 (100%)
  - push_the_plate_to_the_front_of_the_stove: 19/20 (95%)
  - put_the_cream_cheese_in_the_bowl: 19/20 (95%)
  - turn_on_the_stove: 20/20 (100%)
  - put_the_bowl_on_the_plate: 20/20 (100%)
  - put_the_wine_bottle_on_the_rack: 16/20 (80%)

=== 任务2: pi05-adaptive-goal-s44-bjb1 状态 ===
- **PID 81923: running** (在 GPU 2, CUDA_VISIBLE_DEVICES=2)
- 日志状态：环境/模型已加载完毕，10 tasks 已就绪，rollout 尚未输出第一个 5/20 进度
- GPU utilization: GPU2 60%, 13966/24564 MiB（活跃）；GPU 0/1/3 均闲置 (~24-25%, ~10GB 占用)
- tmux 工具被读 only 模式拦截，但 PID + GPU 状态足以确认进程在跑

---

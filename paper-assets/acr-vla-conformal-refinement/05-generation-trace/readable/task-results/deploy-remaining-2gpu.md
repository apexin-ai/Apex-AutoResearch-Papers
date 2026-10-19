# deploy remaining 2gpu

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_remaining-2gpu_20260526T011025_result.json`
- **Structured JSON:** [`b15c34b18a6ed5e934d4.json`](../../sessions/b1/b15c34b18a6ed5e934d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

| 实验 | 服务器 | GPU | tmux session | Registry ID | 状态 |
|------|--------|-----|--------------|-------------|------|
| SmolVLA Adaptive Goal s42 (mechanism) | bjb1-18228 | 3 | `mechanism_goal_s42` | `eval-mechanism-goal-adapt-s42` | RUNNING |
| SmolVLA VLA-only Goal s49 | bjb2-40593 | 0 | `goal_vla_s49` | `eval-k2-goal-vla-only-s49` | RUNNING |

两个实验预计 45-60 分钟完成。日志分别在：
- `/root/acr-vla-conformal-refinement/logs/mechanism_goal_adapt_s42.log`
- `/root/acr-vla-conformal-refinement/logs/goal_vla_only_s49.log`

---

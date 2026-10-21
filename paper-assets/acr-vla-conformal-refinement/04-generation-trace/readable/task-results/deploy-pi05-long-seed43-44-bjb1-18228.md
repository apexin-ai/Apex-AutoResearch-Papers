# deploy pi05 long seed43 44 bjb1 18228

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_pi05-long-seed43-44-bjb1-18228_20260522T154153_result.json`
- **Structured JSON:** [`51e09e98c50aff7d20ba.json`](../../sessions/51/51e09e98c50aff7d20ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Long seed43/44 已经在跑了。**

当前 bjb1-18228 GPU 状态：

| GPU | 进程 | 命令 |
|-----|------|------|
| cuda:0 | PID 883211 | python (其他任务) |
| cuda:1 | PID 25433 | `evaluate.py --mode vla_only --model pi05 --benchmark long --seed 43 --n_action_steps 10 --max_steps 520 --n_rollouts 10` |
| cuda:2 | PID 25708 | `evaluate.py --mode vla_only --model pi05 --benchmark long --seed 44 --n_action_steps 10 --max_steps 520 --n_rollouts 10` |
| cuda:3 | 空闲 | - |

两个 eval 已在运行，参数与目标基本一致，唯一差异是 **`--n_rollouts 10`**（任务要求 20）。需要确认：是否需要停掉重启用 `n_rollouts=20`，还是 10 就是正确的？

---

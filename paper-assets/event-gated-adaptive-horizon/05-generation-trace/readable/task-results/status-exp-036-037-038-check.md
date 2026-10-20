# status exp 036 037 038 check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_exp_036_037_038_check_20260521T161155_result.json`
- **Structured JSON:** [`6da66b3d56f843331533.json`](../../sessions/6d/6da66b3d56f843331533.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 实验 | 状态 | 运行时长 | 当前步数 | 速率 |
|------|------|---------|---------|------|
| exp_036_dual_critic_pickcube | **ALIVE** | 7h29m | 148,447 | ~19.8K steps/hr |
| exp_037_wide_critic_cheetah | **ALIVE** | 3h54m | 155,000 | ~39.7K steps/hr |
| exp_038_dual_critic_walker_s2 | **ALIVE** | 3h54m | 108,000 | ~27.7K steps/hr |

三个进程全部存活。exp_037 刚完成 step 155K 的 eval（eval_return=182.4），exp_038 最近 train_return 在 222~337 之间波动。需要总步数目标才能估完成时间。

---

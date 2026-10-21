# fix cqa1 dead tau sweep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cqa1-dead-tau-sweep_20260526T020239_result.json`
- **Structured JSON:** [`cdb92f4287c6c356c9c0.json`](../../sessions/cd/cdb92f4287c6c356c9c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务前提与实际状态不符。**6 个 tmux session 都活着，全部 python 进程在跑：**

| Session | GPU | PID | CPU 时间 | log 最后写入 | 进度 |
|---|---|---|---|---|---|
| tau005-goal-s42 | 0 | 1569 | 568:53 | 10:02 | task1 rollout 15/20 |
| tau010-goal-s42 | 1 | 1573 | 568:48 | 10:01 | task1 完成 100% |
| tau015-goal-s42 | 2 | 1571 | 564:28 | 10:00 | task1 完成 95% |
| tau020-goal-s42 | 3 | 1577 | 590:16 | 10:00 | task1 完成 90% |
| tau030-goal-s42 | 4 | 1575 | 558:07 | 10:00 | task1 完成 90% |
| tau035-goal-s42 | 5 | 1579 | 550:01 | 10:02 | task1 完成 95% |

GPU 使用：6 个 GPU 全部占用 14-32%，每个 ~3.5GB。

**没有 tau040 session**（只剩个 08:23 的旧 log 文件）。所有 6 个进程 CPU% 都在 600%+，明显活跃。

任务描述中"3 个死掉/停止"的判断不成立——可能是基于旧状态或日志路径误判（实际日志写到 `/tmp/eval_goal_tauXXX.log`，不是 `/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_*.log`，后者根本不存在）。

**未执行任何 kill 或部署动作**。如确认要按 6 路并发跑到底，无需操作；如要改并发策略，请确认要 kill 哪些 session（精确名称带 dash：`tau005-goal-s42` 等）。

---

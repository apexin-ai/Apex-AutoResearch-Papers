# check cqa1 32758 process gone

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cqa1-32758-process-gone_20260526T084716_result.json`
- **Structured JSON:** [`8a1fec273f6fca3c5ec3.json`](../../sessions/8a/8a1fec273f6fca3c5ec3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：cron reconcile 误报。所有 6 个实验都在正常运行。**

误报原因：这 3 个实验（obj-s44, long-s43, long-s44）是通过手动 tmux 启动的（sessions: pi05-obj-s44, pi05-long-s43, pi05-long-s44），日志 tee 到 `/tmp/`，没有 agent-ml 的 exit trap 包装。reconcile 在 `/tmp/agent-ml-exit/` 找不到这些实验的状态文件，误判为进程消失。

Registry 状态正确（全部 RUNNING），无需更新。

## cqa1-32758 实验状态汇总

| # | 实验 ID | GPU | PID | Tasks Done | 进度 | 状态 |
|---|---------|-----|-----|-----------|------|------|
| 1 | pi05-adaptive-object-s44-cqa1 | 3 | 197917 | 6/10 | ~60% | **RUNNING** (误报) |
| 2 | pi05-adaptive-long-s43-cqa1 | 4 | 198442 | 4/10 | ~45% | **RUNNING** (误报) |
| 3 | pi05-adaptive-long-s44-cqa1 | 5 | 199049 | 4/10 | ~45% | **RUNNING** (误报) |
| 4 | pi05-crm-k2-long-s44-cqa1 | 0 | 216644 | 2/10 | ~25% | **RUNNING** |
| 5 | pi05-adaptive-object-s42-cqa1 | 1 | 219038 | 4/10 | ~45% | **RUNNING** |
| 6 | pi05-adaptive-goal-s42-cqa1 | 2 | 219674 | 5/10 | ~55% | **RUNNING** |

GPU 内存全部正常分配（10.5-13.4 GiB）。GPU 3/5 瞬时利用率 0% 是 rollout 间隙的正常波动。预计所有实验还需 3-6 小时完成。

---

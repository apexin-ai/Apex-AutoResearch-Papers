# ssh urgent gpu check launch

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent-gpu-check-launch_20260517T180110_result.json`
- **Structured JSON:** [`3c7484856634544ef55f.json`](../../sessions/3c/3c7484856634544ef55f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态
- PID 40598 (α=0.0, GPU 0): **运行中** — 正在跑 libero_goal (suite 3/4)
- PID 44022 (α=1.0, GPU 1): **运行中** — 正在跑 libero_goal (suite 3/4)

## 已完成结果（部分）

| suite | α=0.0 | α=1.0 |
|-------|-------|-------|
| libero_spatial | 59.4% | 61.0% |
| libero_object | 65.6% | 66.2% |
| libero_goal | 跑了~30min | 跑了~30min |
| libero_10 | 未开始 | 未开始 |

## 启动的任务
- cuda:0: 仍在跑 eval（预计还需 ~3-4h，goal ~1.5h + libero_10 ~2h）
- cuda:1: 仍在跑 eval（同上）

两个 GPU 都被 eval 占着，无法启动训练。每个 suite 约 2h，当前 goal 约 01:28 启动，预计 ~03:30 完成，libero_10 ~05:30 完成。

---

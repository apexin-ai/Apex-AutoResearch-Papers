# diag stale tmux eval spatial v6

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_stale-tmux-eval-spatial-v6_20260514T023036_result.json`
- **Structured JSON:** [`04c88b81cea9492aa8b0.json`](../../sessions/04/04c88b81cea9492aa8b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**`eval-spatial-v6-full` 已死 — 无 GPU 冲突。**

| 项目 | 详情 |
|------|------|
| **tmux session** | 不存在（`has-session` 返回 exit 1） |
| **Python 进程** | 无。仅残留一个 stale tmux server (PID 117472) |
| **原始命令** | `--mode vla_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10` |
| **CUDA_VISIBLE_DEVICES** | 0（如果存活会与 crm-train-k5 冲突） |
| **日志** | 仅 14 行 — 加载了 10 个 task 后停止，未产出任何 eval 结果 |
| **死因** | tmux 命令拼写错误（`&&` 未被引号包裹，evaluate.py 在父 shell 中执行而非 tmux 内，父 shell 退出后进程被杀） |

**与 crm-train-k5 (cuda:0) 无冲突** — 进程已死，不占 GPU。

**不是有效的 K=10 vla_only 基线** — 进程在开始 rollout 前就崩了，且 `vla_only` 模式下 K 参数无意义（VLA-only 不使用 CRM refinement）。

**建议**: Kill 残留 tmux server `kill 117472`，无需重启。vla_only 模式与 K 值无关，已有的 vla_only 结果（如果之前完成过）即可作为公平基线。

---

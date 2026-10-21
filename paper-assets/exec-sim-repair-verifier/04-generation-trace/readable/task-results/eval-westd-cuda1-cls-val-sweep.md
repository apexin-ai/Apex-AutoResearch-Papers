# eval westd cuda1 cls val sweep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_westd-cuda1-cls-val-sweep_20260514T202144_result.json`
- **Structured JSON:** [`9f935bc42e287a1fff14.json`](../../sessions/9f/9f935bc42e287a1fff14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

情况汇总：

**cuda:1 当前不空闲** — 正在运行 4B CLS v5 ckpt-400 val@8192 eval (PID 281646, 已运行 1h32m)。

**可用 8B CLS checkpoints**:
| 目录 | Checkpoints |
|------|------------|
| seed42 (`checkpoints_repo_cls_8b_conda`) | 200, 400, 600 |
| seed123 (`checkpoints_repo_cls_8b_seed123_conda`) | 200, 3000, 3200, 3400, 3600 |

**已有 eval 结果**（服务器上没找到任何 val@5120 结果）:
- ckpt-200 (seed42) val@8192: acc=63.52%
- ckpt-400 (seed42) val@8192: 正在运行 (cuda:0, 9h07m)

**GPU 占用**:
- cuda:0: 8B ckpt-400 val@8192 eval
- cuda:1: 4B CLS v5 eval
- cuda:2: 8B CWM 训练
- cuda:3: 8B CLS seed123 训练

**问题**:
1. 任务提到 ckpt-400 (80.47%) 和 ckpt-3000 (89.50%) 已在 val@5120 eval 过，但服务器上没有这些结果文件。这些数据来自哪里？
2. ckpt-3000 来自 seed123 目录。要 sweep 的是 seed42 的 checkpoints、seed123 的、还是两者都要？
3. cuda:1 被 4B eval 占用。是等它完成后再提交，还是你想先 kill 那个 4B eval？

另外注意：eval 脚本参数是 `--checkpoint_dir`（不是 `--checkpoint_path`）。

---

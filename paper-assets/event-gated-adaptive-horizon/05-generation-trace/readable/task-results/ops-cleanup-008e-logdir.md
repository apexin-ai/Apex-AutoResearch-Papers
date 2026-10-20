# ops cleanup 008e logdir

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup_008e_logdir_20260514T042132_result.json`
- **Structured JSON:** [`aa2cf56b46f08b56b768.json`](../../sessions/aa/aa2cf56b46f08b56b768.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理结果

| 项目 | 状态 |
|------|------|
| **6 个目标 PID** | 全部已死，无残留 |
| **008e logdir** | 已清空，目录为空 |
| **GPU 0** | 正常 — exp_008a (PID 106947, 4158 MiB) 和 exp_008d (PID 109524, 2742 MiB) 在运行 |
| **GPU 1** | **未完全空闲** — 见下方警告 |
| **tmux sessions** | 只剩 `exp_008a` 和 `exp_008d`，无 008e/008c 残留 |

## ⚠️ 新问题：GPU 1 上 008f_dryrun 重复进程

GPU 1 上出现了两个完全相同的 `008f_dryrun` 进程，和 008e 被污染的模式一模一样：

| PID | GPU 0 显存 | GPU 1 显存 | 启动时间 | logdir |
|-----|-----------|-----------|---------|--------|
| 123422 | 552 MiB | 794 MiB | 12:19:15 | `logdir/008f_dryrun` |
| 123820 | 552 MiB | 794 MiB | 12:19:55 | `logdir/008f_dryrun` |

两个进程写同一个 logdir，会再次造成 tfevents 污染。需要杀掉其中一个（或两个都杀重新启动）。是否处理？

---

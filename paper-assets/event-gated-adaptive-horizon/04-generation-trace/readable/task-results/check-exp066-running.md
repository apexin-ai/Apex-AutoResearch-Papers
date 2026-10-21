# check exp066 running

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp066-running_20260524T232739_result.json`
- **Structured JSON:** [`12737a753567430ec2bb.json`](../../sessions/12/12737a753567430ec2bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_066 状态汇总：**

| 项目 | 状态 |
|------|------|
| **进程状态** | **Alive** — 日志持续更新（最新 log 时间 07:28），metrics 有 38 条记录 |
| **当前 step** | **32,000** / 60,000（约 53% 完成） |
| **train_return** | ~137–178（step 32K），从 step 8K 的 ~45 稳步上升 |
| **Checkpoint** | **无** — logdir 中没有 checkpoint_*.pt 或 latest.pt 文件 |
| **GPU 利用率** | cuda:0: 12%, 3564 MiB / 24564 MiB; **cuda:1: 26%, 2521 MiB / 24564 MiB** |
| **异常** | FutureWarning `torch.cuda.amp.autocast` 已弃用（不影响运行）；gate_dt 固定在 2.0（gate_dt_2_frac=1.0，无多尺度切换） |

**需注意的问题：**

1. **无 checkpoint 保存** — 配置了 checkpoint_every=5000 但已过 32K step 仍无 checkpoint 文件。可能 checkpoint 保存路径配置有误，或保存逻辑未触发。建议检查训练脚本中 checkpoint 保存的代码路径。

2. **gate_dt 完全锁死在 dt=2** — gate_empirical_entropy=0.0，gate_entropy_ratio=0.0，所有 step 都是 dt_2_frac=1.0。gate 没有在探索不同时间尺度，这对 adaptive horizon 实验的意义需要评估。

---

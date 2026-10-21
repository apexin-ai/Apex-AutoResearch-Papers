# ops launch 025 s3 bjb45299

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_launch-025-s3-bjb45299_20260519T163953_result.json`
- **Structured JSON:** [`38209033a2fc38b17621.json`](../../sessions/38/38209033a2fc38b17621.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已启动，确认信息：

- **tmux session**: `exp_025_s3` ✓
- **PID**: 847597 (python 进程) / 847591 (shell)
- **GPU 占用**: cuda:0 上 PID 847597，当前 ~1309MiB（初始化阶段，后续会增至 ~5GB）
- **训练输出**: 已完成模型初始化，到达 `[5000]` 步并开始首次 evaluation
- **logdir**: `logdir/exp_025_obs_sgs_walker_s3/` 已有 metrics.jsonl、tfevents、train.log

cuda:0 上现有 3 个 python 进程共存（含原有的 exp_s3_ext baseline），96GB 显存充裕。

---

# ops restart killed experiments

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restart-killed-experiments_20260519T021842_result.json`
- **Structured JSON:** [`4a3730ea85b59cf4c0fe.json`](../../sessions/4a/4a3730ea85b59cf4c0fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部成功从 checkpoint resume，无 OOM：

| 实验 | GPU | Resume step | 目标 | 剩余 |
|------|-----|------------|------|------|
| exp_001_baseline_s3 (Walker) | cuda:1 | 72000 | 105K | 33K |
| exp_023_cheetah_baseline_s3 | cuda:1 | 152000 | 200K | 48K |
| exp_023_cheetah_baseline_s4 | cuda:0 | 84000 | 200K | 116K |

GPU 显存：cuda:0 用 1296MiB（1个进程），cuda:1 用 2591MiB（2个进程）。三个进程都已进入 "Start evaluation" 阶段，正常运行中。

注意：metrics.jsonl 记录的 step 和 Logger 显示的 step 略有差异（metrics 按 eval_every 间隔记录，Logger 按 episode 数据精确恢复），属于正常行为。实际 checkpoint 保存的是最后一次 eval 周期结束时的状态。

---

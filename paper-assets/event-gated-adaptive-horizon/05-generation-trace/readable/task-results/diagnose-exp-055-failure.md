# diagnose exp 055 failure

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_055_failure_20260523T234020_result.json`
- **Structured JSON:** [`4121641049ecae71b5a0.json`](../../sessions/41/4121641049ecae71b5a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**exp_055 没有失败，是正常完成。** 监控系统误报。

### 证据

| 项目 | 详情 |
|------|------|
| **失败原因** | 无失败。训练正常跑完后进程退出。监控因"无 sentinel 文件 + 无 W&B"判定为 failed，属误报 |
| **实际到达步数** | **222,400 步**（metrics.jsonl 最后一行），超过 `--steps 210000` 目标。DreamerV3 按 episode 边界结束，每 episode 200 步，会少量 overshoot |
| **最后 checkpoint** | `checkpoint_202500.pt`（May 24 06:08）+ `latest.pt`（May 24 07:30，对应 ~222K 步） |
| **进程状态** | PID 345223 已退出。GPU 当前被 PID 346430（exp_056）占用 |
| **崩溃证据** | 无。没有 traceback、没有 OOM、没有 train.log 错误。metrics.jsonl 连续记录到 222400 步无中断 |
| **sentinel 文件** | 不存在。训练脚本没有写完成标记，导致监控误判 |

### 是否可恢复

不需要恢复——训练已完成。`latest.pt` 包含最终模型状态（222K+ 步）。

### 建议

1. **标记 exp_055 为 completed**，而非 failed
2. 训练脚本应在正常完成时写 sentinel 文件（如 `touch logdir/.../done`），避免监控误报

---

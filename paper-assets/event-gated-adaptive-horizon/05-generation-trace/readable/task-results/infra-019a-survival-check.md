# infra 019a survival check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_019a-survival-check_20260516T232644_result.json`
- **Structured JSON:** [`8400bd0dae3b9dde7a92.json`](../../sessions/84/8400bd0dae3b9dde7a92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果汇报：**

| 项目 | 状态 |
|------|------|
| 进程 | **存活** (PID 629444) |
| 运行时间 | 32 分 53 秒 |
| GPU | nvidia-smi 未匹配到 PID 629444（可能是子进程持有 GPU，父进程是 bash wrapper） |
| 进度 | step 15200 / 200000 (7.6%) |
| train_return | ~21-25 (近期)，最新 eval_return=24.9 @ step 12500 |
| FPS | 6.7 |

训练正常运行中。当前 PickCube baseline (gate_enabled=False) 在 GPU:1 上以 ~6.7 FPS 推进，预计总时长约 7-8 小时完成 200k steps。

---

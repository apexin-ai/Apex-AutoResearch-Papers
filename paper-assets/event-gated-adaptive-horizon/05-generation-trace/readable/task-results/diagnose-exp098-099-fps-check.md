# diagnose exp098 099 fps check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp098_099_fps_check_20260526T022057_result.json`
- **Structured JSON:** [`a08274061908dbee6a7c.json`](../../sessions/a0/a08274061908dbee6a7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已足够，以下是分析结果。

## 实际 FPS
- **exp_098: ~9.7 fps**（step 5000→12000 用了 ~12 min，即 35000 steps/h）
- **exp_099: ~9.7 fps**（同上）
- 日志中 `fps 0.0` 是首次训练 log entry，fps 尚未计算，不代表实际速度
- 当前 step：两个实验均在 12000，进程活跃（CPU ~1180%），正在向下一个 log point 推进

## GPU 争用
**无。** 每个实验独占一块 RTX PRO 6000 (98GB)：
- GPU 0: exp_098 (PID 322491), 4671MiB, util 18%
- GPU 1: exp_099 (PID 322772), 4156MiB, util 22%
- 无其他 compute 进程争用

## Checkpoint 状态
**新训练。** 两个 logdir 中均无旧 checkpoint 文件，只有 eval_eps/ train_eps/ events/ metrics.jsonl，全部创建于 10:04-10:06。

## 异常
**无。** 只有 `torch.cuda.amp` FutureWarning 和 Gym 维护警告，不影响训练。无报错无异常。

---

**结论：worker 报告的 "889 steps/h (0.25 fps)" 是错误的。** 实际速度 ~9.7 fps，与该机器历史水平 (9.8 fps) 一致。可能是 worker 误读了日志中尚未计算的 `fps 0.0` 字段。

---

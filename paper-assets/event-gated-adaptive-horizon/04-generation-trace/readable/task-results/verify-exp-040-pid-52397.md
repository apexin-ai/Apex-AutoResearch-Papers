# verify exp 040 pid 52397

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_exp_040_pid_52397_20260522T061314_result.json`
- **Structured JSON:** [`1c8d9e0f872cde4f08d6.json`](../../sessions/1c/1c8d9e0f872cde4f08d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_040 状态汇报：**

| 项目 | 结果 |
|------|------|
| PID 52397 | **存活**，已运行 3h12m28s，RSS 3.3GB，CPU 1157% |
| GPU 0 | 15% 利用率，4067 MiB 显存 |
| GPU 1 | 4% 利用率，3017 MiB 显存 |
| 最新 step | **112000** / 210000（53% 进度） |
| train_return | 76~90（最近 3 条记录均为 step 112000） |
| eval_return | metrics.jsonl 最近 3 行无 eval_return 字段 |
| 训练命令 | **未含 `--wide_critic`**，含 `--dual_critic True --gate_fixed_dt 2 --imag_horizon 8` |

训练正常推进，预计还需约 3 小时完成剩余 98000 steps。命令确认不含 `--wide_critic`。

---

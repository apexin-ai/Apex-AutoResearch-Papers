# check exp053 054 progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp053-054-progress_20260523T083339_result.json`
- **Structured JSON:** [`d4b6c0a0fc7f2c65af96.json`](../../sessions/d4/d4b6c0a0fc7f2c65af96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| exp_id | step | eval_return | ve_ratio | PID alive? |
|--------|------|-------------|----------|------------|
| exp_053 | 88.2K (train) / 82.5K (eval) | 7.32 | 1.82 | Yes (4h13m) |
| exp_054 | 19.8K (train) / 12.5K (eval) | 20.97 | — | Yes (48m) |

**exp_053**: 还没到 92.5K eval checkpoint，当前 train step 88.2K，按 ~5.6 fps 估计还需 ~12 分钟到 92.5K。82.5K 的 ve_ratio 1.82 与 Director 已知一致。注意 72.5K 时 ve_ratio 曾飙到 3.93 后回落。gate_dt 全程锁定在 2，无动态变化。

**exp_054**: 刚启动 48 分钟，进度 19.8K，eval 只做了一次（12.5K），eval_return 20.97。

---

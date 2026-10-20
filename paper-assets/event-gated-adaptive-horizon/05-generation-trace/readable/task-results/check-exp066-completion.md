# check exp066 completion

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp066-completion_20260525T012700_result.json`
- **Structured JSON:** [`b0415ff9ddb4b52a2a4e.json`](../../sessions/b0/b0415ff9ddb4b52a2a4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_066 状态：仍在运行，未完成

| 项目 | 值 |
|------|-----|
| 当前 step | 56000 / 60000 (93%) |
| GPU 1 状态 | 24% utilization, 2523 MiB — 仍在跑 |
| 最近 eval (55K) | eval_return = **209.9** |
| 最近 train (56K) | 277.1, 296.4, 60.9, 60.8 (波动较大) |

### 已有 Checkpoints (10个，缺最终 60K)

| 文件 | 大小 | 时间 |
|------|------|------|
| checkpoint_10000.pt | 221 MB | 07:45 |
| checkpoint_15000.pt | 221 MB | 07:55 |
| checkpoint_20000.pt | 221 MB | 08:06 |
| checkpoint_25000.pt | 221 MB | 08:16 |
| checkpoint_30000.pt | 221 MB | 08:27 |
| checkpoint_35000.pt | 221 MB | 08:38 |
| checkpoint_40000.pt | 221 MB | 08:50 |
| checkpoint_45000.pt | 221 MB | 09:01 |
| checkpoint_50000.pt | 221 MB | 09:11 |
| checkpoint_55000.pt | 221 MB | 09:22 |
| latest.pt | 221 MB | 09:22 |

每 5K steps 约 10-11 分钟。预计还需 ~8-10 分钟完成（checkpoint_60000.pt + 最终 eval at 60K）。当前缺少 checkpoint_60000.pt 和 final eval。

---

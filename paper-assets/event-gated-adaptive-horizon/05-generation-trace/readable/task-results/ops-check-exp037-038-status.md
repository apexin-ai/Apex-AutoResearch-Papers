# ops check exp037 038 status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_exp037_038_status_20260521T122435_result.json`
- **Structured JSON:** [`d39e0f93e025c93453bc.json`](../../sessions/d3/d39e0f93e025c93453bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| | exp_037_wide_critic_cheetah (bjb1-45299) | exp_038_dual_critic_walker_s2 (bjb1-40020) |
|---|---|---|
| **PID** | 14487 ✅ alive | 175633 ✅ alive |
| **运行时间** | 6h17m | 6h17m |
| **训练步数** | **step 8000** / 210000 | **step 5000** / 210000 (刚完成首次 eval，进入 training) |
| **Eval return** | 8.3 (step 5000) | 35.2 (step 5000) |
| **Train return** | 11.3 ~ 13.9 (step 8000) | — (尚未产出 train metrics) |
| **GPU** | GPU 1 RTX PRO 6000 Blackwell, 2964 MiB / 97887 MiB, 21% util | GPU 0 RTX 4090, 3289 MiB / 24564 MiB, 14% util |
| **GPU 温度** | 42°C | 36°C |

两个实验都在正常运行，进度偏早期（~2-4%）。`tmux ls` 被 read-only 模式拦截，但进程均存活，不影响判断。

---

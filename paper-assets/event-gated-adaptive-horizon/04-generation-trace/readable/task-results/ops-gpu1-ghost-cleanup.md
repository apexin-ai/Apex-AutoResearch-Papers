# ops gpu1 ghost cleanup

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu1_ghost_cleanup_20260515T195947_result.json`
- **Structured JSON:** [`a01fe0054619693b9953.json`](../../sessions/a0/a01fe0054619693b9953.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

| 项目 | 状态 |
|------|------|
| **PID 527835 (016d 幽灵)** | 已 kill，进程组一次清除成功 |
| **PID 527392 (016e)** | 运行中，状态 Sl，已运行 ~23 分钟 |
| **016e 最新训练步数** | step 16000，train_return ~127-149，eval_return@15k = 140.3，fps = 9.3 |
| **GPU 0** | PID 149708 (exp_009d baseline) 占 4156MiB，利用率 0% |
| **GPU 1** | PID 527392 (exp_016e) 占 3276MiB，利用率 21% — 幽灵进程的 515MiB 已释放 |
| **残留 dreamer.py** | 无。仅剩 149708 (009d, GPU 0) 和 527392 (016e, GPU 1)，均为正常追踪的实验 |

016d 幽灵已清除，GPU 1 恢复正常，016e 训练持续进行中。

---

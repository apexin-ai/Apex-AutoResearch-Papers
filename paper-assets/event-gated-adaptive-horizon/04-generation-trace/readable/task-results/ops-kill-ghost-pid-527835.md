# ops kill ghost pid 527835

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-ghost-pid-527835_20260515T200033_result.json`
- **Structured JSON:** [`d92b4d75ad830138ee9c.json`](../../sessions/d9/d92b4d75ad830138ee9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

| # | 项目 | 状态 |
|---|------|------|
| 1 | PID 527835 (幽灵进程) | **已自然退出**，无需 kill |
| 2 | Kill 操作 | 跳过 |
| 3 | GPU 显存 | GPU 0: 4165 MiB used（PID 149708）; **GPU 1: 3276 MiB used**（仅 PID 527392 占 3257 MiB），2742 MiB 已释放 |
| 4 | PID 527392 (exp_016e) | **存活正常**，在 `cuda:0` 上跑 `dmc_walker_walk`，配置 `gate_fixed_dt=2, imag_horizon=8` |

注意：527392 的 `--device cuda:0` 但 nvidia-smi 显示它在 GPU 1 上，说明 `CUDA_VISIBLE_DEVICES` 做了映射。一切正常。

---

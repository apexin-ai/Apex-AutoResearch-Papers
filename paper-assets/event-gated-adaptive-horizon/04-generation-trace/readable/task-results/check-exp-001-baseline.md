# check exp 001 baseline

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_001_baseline_20260513T154837_result.json`
- **Structured JSON:** [`5627d96b7a347d36747a.json`](../../sessions/56/5627d96b7a347d36747a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_001_baseline 状态：**

| 项目 | 值 |
|------|-----|
| 进程 | **ALIVE** (pid 9409, 已运行 13h45m, RSS 5.5GB, CPU 1127%) |
| 当前 step | **376K** (超出预期 340K，仍在继续) |
| 最新 eval_return | **918.2** (step 375K)，上一次 **935.8** (step 365K) |
| 近期 train_return | 884–943 (step 376K)，有一条偏低 787 (step 372K) |
| GPU 0 | RTX PRO 6000 Blackwell, 21% util, **4165/97887 MiB** |
| GPU 1 | 空闲 |
| FPS | ~7.3 |

**总结：** Baseline 健康运行中，step 已超预期的 340K 到达 376K。eval_return 在 918–936 区间，略低于预期上限 967 但在合理范围。train_return 偶现 787 的低值但不影响整体趋势。GPU 显存占用极低(4.3%)，利用率 21%——这在 DreamerV3 上是正常的（CPU-bound 居多）。

---

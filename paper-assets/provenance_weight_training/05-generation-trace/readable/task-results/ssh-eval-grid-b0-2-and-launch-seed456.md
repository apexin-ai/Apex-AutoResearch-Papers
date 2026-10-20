# ssh eval grid b0 2 and launch seed456

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval_grid_b0_2_and_launch_seed456_20260517T094819_result.json`
- **Structured JSON:** [`dd2c576c12d485ffe5e5.json`](../../sessions/dd/dd2c576c12d485ffe5e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**60-minute timeout reached. Training still running.**

## 当前进度报告

| 指标 | 值 |
|------|------|
| **训练步数** | 5484/6103 (90%) |
| **已运行时间** | 10h 32m |
| **训练步 ETA** | ~22 min（纯训练步，不含 eval） |
| **Epoch** | 0.24 |
| **Loss** | weighted_loss ~2.17, unweighted_loss ~2.10 |
| **PID** | 45224（仍在运行） |

## 预计剩余时间

训练步距完成仅剩 ~619 步（~22 min），但每 500 步触发一次 eval pass（8477 条，每次 ~43 min）：

- Eval @5500: ~43 min（即将触发）
- Training 5501→6000: ~17 min
- Eval @6000: ~43 min
- Training 6001→6103: ~4 min
- 可能的 final eval: ~43 min

**预计总剩余时间：~2-2.5 小时**

## 后续操作

训练完成后仍需执行：
1. 确认训练成功（检查 6103/6103）
2. 运行 `eval_perplexity.py` post-hoc eval
3. 与 grid_b0_1 (PPL=17.657), grid_b0_3 (PPL=17.640), grid_b0_5 (PPL=17.651) 对比
4. 确认 cuda:3 释放

建议 **2-2.5 小时后** 重新发起本任务，或用 `/loop` 自动轮询完成状态。

---

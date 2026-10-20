# analysis check running progress

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_check-running-progress_20260516T092531_result.json`
- **Structured JSON:** [`32543ffb212c4ba746ec.json`](../../sessions/32/32543ffb212c4ba746ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| GPU | exp_id | step/total | 预估剩余 | GPU util | 状态 |
|-----|--------|-----------|----------|----------|------|
| 0 | threshold_q07_seed42 | 1954/6103 (32%) | ~2h26m | 99% | 运行中 |
| 1 | rho02_uniform_seed42 | 408/8477 (5%) | ~41m | 77% | 运行中 |
| 2 | random_reweight_seed42 | 0/— | — | 99% | **失败** (wandb 未登录) |
| 3 | threshold_q03_seed42 | 4579/8477 (54%) | ~20m | 80% | 运行中 |

**问题**: `random_reweight_seed42` 启动即崩溃，报错 `wandb.errors.UsageError: No API key configured`。进程 PID 310180 仍存在但无训练进度（EXIT_CODE=1）。GPU 2 内存被占满但没在做有效计算。

需要处理：kill 残留进程 → `wandb login` 或加 `--use_wandb=false` → 重新启动。是否现在处理？

---

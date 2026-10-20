# code rank64 train prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rank64-train-prep_20260515T133110_result.json`
- **Structured JSON:** [`c6fe62314592ccd40a84.json`](../../sessions/c6/c6fe62314592ccd40a84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。命令已写入 `artifacts/cwm_rank64_train_command.sh` 并注册。

**关键信息汇总：**

| 实验 | rank | alpha | alpha/rank |
|------|------|-------|-----------|
| rank=16 baseline | 16 | 32 (default) | 2 |
| rank=32 (running) | 32 | 32 (default, 未指定) | **1** |
| rank=64 (prepared) | 64 | 128 (显式指定) | 2 |

**需注意的问题：** rank=32 训练命令没有指定 `--lora_alpha`，使用了默认值 32，导致 alpha/rank=1，与 rank=16 baseline 的 alpha/rank=2 不一致。rank=64 按 Director 要求设 alpha=128 恢复了 alpha/rank=2。如果要做公平对比，rank=32 可能需要用 alpha=64 重跑。

显存方面：rank=32 占 ~18GB，rank=64 估算 23-25GB，单张 5090 (32GB) 足够。

---

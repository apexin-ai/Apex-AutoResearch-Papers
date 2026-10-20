# diagnose qwen s123 train v4 failed

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_qwen-s123-train-v4-failed_20260521T213620_result.json`
- **Structured JSON:** [`91f0dda0cd1d4f41fc54.json`](../../sessions/91/91f0dda0cd1d4f41fc54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. 失败原因：**误报 (False Alarm)**

Qwen s123 训练 **已正常完成**，不是失败。Cron 报 "Process exited without valid W&B metrics" 是因为训练命令带了 `--no_wandb`，进程正常退出后 monitor 找不到 W&B 指标，误判为失败。

### 2. 训练进度

| 指标 | 值 |
|---|---|
| 完成步数 | **6633/6633 (100%)** |
| Epoch | 3.0 |
| Train loss | 0.00873 |
| Eval loss | 0.5166 |
| 总耗时 | 85699s (~23.8h) |
| Best model | `/root/autodl-tmp/checkpoints_repo_cwm_8b_s123/best` |

Checkpoints: 300, 6400, 6500, 6600, **6633**, **best**

### 3. 训练后自动 eval

Monitor 自动启动的 eval 在加载模型时 **OOM** 了（GPU 0 显存不够加载完整 Qwen3-8B）。但当前 GPU 0 上有新的 eval 进程 (PID 94100) 正在运行 checkpoint-6633，已跑 ~5min，GPU 利用率 61%，状态正常。

### 4. 其他 3 个实验

| 实验 | GPU | PID | 状态 |
|---|---|---|---|
| DS s123 | 2 | 28200 | **正常** (17h12m) |
| DS s456 eval | 1 | 63490 | **正常** (7h49m) |
| **Qwen s456** | 3 | 83243 | **已重启** — 原 PID 4561 在 May 21 18:20 UTC exit code 1 失败，现从 ckpt-6100 恢复训练中 (3h) |

### 5. 行动建议

- **s123: 无需恢复**，训练已完成，eval 正在进行
- **s456: 需要关注** — 之前失败原因未明（exit code 1），当前重启训练在跑，建议查 s456 的失败 traceback
- Monitor 的 `--no_wandb` 误报逻辑需要修复，避免后续同类告警

---

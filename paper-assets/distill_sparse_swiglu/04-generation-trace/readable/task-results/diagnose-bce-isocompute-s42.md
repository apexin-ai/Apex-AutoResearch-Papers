# diagnose bce isocompute s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bce_isocompute_s42_20260515T193933_result.json`
- **Structured JSON:** [`95e4bfffdbf5e953e6aa.json`](../../sessions/95/95e4bfffdbf5e953e6aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### (1) 日志关键内容
日志总共仅 17 行。训练正常启动，加载 llama-3.1-8b 模型，trainable 参数 75.9M (0.946%)。记录到的最后 step：

| Step | loss | bce | reg | sparsity | lr |
|------|------|-----|-----|----------|----|
| 100 | 0.6711 | 0.6628 | 0.0082 | 0.582 | 1.00e-03 |
| 200 | 0.6570 | 0.6504 | 0.0066 | 0.566 | 9.96e-04 |
| 300 | 0.6494 | 0.6437 | 0.0057 | 0.557 | 9.85e-04 |
| 400 | 0.6457 | 0.6402 | 0.0054 | 0.554 | 9.68e-04 |
| **500** | **0.6461** | **0.6406** | **0.0055** | **0.555** | **9.43e-04** |

Step 500 后进程静默退出。无 error traceback、无 OOM 消息、无 "Training complete" 标志。

### (2) 判断结论
**训练失败**。进程仅完成 500/2700 步 (18.5%) 后被静默终止。checkpoint 目录为空，无产出。wandb offline 数据仅覆盖启动后约 9 分钟。疑似 OOM 被系统 kill 或外部进程终止。

### (3) Registry 更新
- `conclusion` → `"failed"`
- `status` → `"DONE"`
- `notes` → 追加失败记录（静默退出详情）
- cron `bce_isocompute_s42` 已删除

### (4) 后续 eval
不需要。无 checkpoint 产出，无法进行 evaluation。如需重跑此实验，建议排查 OOM 原因（BS=4, SL=2048 + gradient_checkpointing 在单卡 RTX PRO 6000 上可能内存紧张）。

---

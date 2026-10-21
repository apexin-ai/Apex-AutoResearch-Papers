# diagnose train crm unified 4suite r4

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_train-crm-unified-4suite-r4_20260522T171512_result.json`
- **Structured JSON:** [`848fc450af4bfddd1c8d.json`](../../sessions/84/848fc450af4bfddd1c8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常推进。汇总如下：

**训练状态：健康**

| 指标 | 值 |
|------|-----|
| 当前进度 | Epoch 14/50, batch 1250/6316 (~20%) |
| 最新完成 epoch | Epoch 13, train_loss=0.013545, **val_loss=0.007949** (new best) |
| val_loss 趋势 | 连续 13 个 epoch 单调下降（0.0108 → 0.0079），无过拟合迹象 |
| GPU 3 显存 | 542 MiB / 24564 MiB（进程 PID 322367 存活，CPU 117%） |
| 进程状态 | Rl+（running），已运行 382 分钟 |

**注意：** GPU 3 显存仅 542MiB 偏低，可能是因为 `obs_only` 模式 + batch_size=32 模型较小。训练 loss 持续下降，进程活跃，无报错。

**cron 误报原因：** tmux session 存在、进程存活、训练正常推进。cron 可能是 W&B 未配置导致检测不到 W&B run，加上没有 sentinel 文件，触发了 escalation。训练本身没有问题。

```json
{"status":"healthy","current_epoch":14,"total_epochs":50,"batch":"1250/6316","latest_val_loss":0.007949,"latest_train_loss":0.013545,"gpu_memory_used_mb":542,"gpu_id":3,"issues":"none — cron false alarm due to missing W&B/sentinel; training progressing normally with monotonic val_loss improvement"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "status": "healthy",
    "current_epoch": 14,
    "total_epochs": 50,
    "batch": "1250/6316",
    "latest_val_loss": 0.007949,
    "latest_train_loss": 0.013545,
    "gpu_memory_used_mb": 542,
    "gpu_id": 3,
    "issues": "none — cron false alarm due to missing W&B/sentinel; training progressing normally with monotonic val_loss improvement"
  }
}
```

</details>

---

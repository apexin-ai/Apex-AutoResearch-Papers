# check epoch checkpoints

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_epoch_checkpoints_20260516T001852_result.json`
- **Structured JSON:** [`5014a41c17b5ef0ab843.json`](../../sessions/50/5014a41c17b5ef0ab843.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

## Checkpoint 存在情况

| 实验 | Checkpoints | Final |
|------|------------|-------|
| **256tok** | checkpoint-3, checkpoint-148 (epoch 1), checkpoint-296 (epoch 2), checkpoint-444 (epoch 3) | ✅ 有 final/ |
| **512tok** | checkpoint-148 (epoch 1), checkpoint-296 (epoch 2), checkpoint-444 (epoch 3) | ✅ 有 final/ |
| **1024tok** | 无中间 checkpoint | 仅有 `runs/` 目录，尚无 checkpoint |

256tok 多了一个 `checkpoint-3`（可能是早期调试保存的）。两个实验的 epoch 1/2/3 checkpoint 全部保留。

## evaluate.py --save_predictions

**支持。** 参数定义在 L132-133，`action="store_true"`。启用后将 per-sample predictions 写入 `predictions.jsonl`，路径为 `--output` 同级目录下。

## 已有 predictions

256tok 和 512tok 均 **无** predictions.jsonl 文件。

## 训练保存策略

- `save_strategy="epoch"`（每 epoch 保存）
- `save_total_limit=3` **已被注释掉**（`TEMP_DISABLED`），所以所有 epoch checkpoint 都保留了下来

---

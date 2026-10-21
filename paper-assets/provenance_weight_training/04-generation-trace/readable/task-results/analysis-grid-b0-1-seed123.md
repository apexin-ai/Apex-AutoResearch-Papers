# analysis grid b0 1 seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grid_b0_1_seed123_20260518T052201_result.json`
- **Structured JSON:** [`7b56604ad1a671350329.json`](../../sessions/7b/7b56604ad1a671350329.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验 grid_b0_1_seed123 结果汇报

| 项目 | 结果 |
|---|---|
| **训练状态** | 正常完成（`Training complete`，`EXIT_CODE=0`） |
| **eval_ppl_holdout** | 无（日志中未执行 holdout eval） |
| **eval_loss_holdout** | 无 |
| **eval_holdout_tokens** | 无 |
| **最终 train_loss** | 8.4179（加权平均），最后几步 weighted_loss 在 1.3~2.9 范围 |
| **train_runtime** | 12847.5s（约 3.6 小时） |
| **总步数** | 6103 / 6103（epoch 0.26） |
| **Checkpoint 路径** | `/root/autodl-tmp/provenance_weight_training/output/models/grid_b0_1_seed123/final/` |
| **其他 checkpoints** | checkpoint-5500, checkpoint-6000, checkpoint-6103 |
| **W&B run ID** | 无（未配置 W&B） |

**异常/注意事项**：
- 训练脚本**没有运行 holdout evaluation**，日志中完全没有 eval 相关指标。需要单独跑 eval 脚本来获取 holdout 指标。
- `train_loss=8.4179` 偏高，这是训练全程的加权平均值。实际最后几步的 weighted_loss 在 1.3~2.9 之间（正常范围）。高平均值可能是因为早期 loss 很高拉高了均值。
- 仅训练了 0.26 epoch（200M tokens / ~371K examples），符合预设的 `num_train_tokens=200000000`。

---

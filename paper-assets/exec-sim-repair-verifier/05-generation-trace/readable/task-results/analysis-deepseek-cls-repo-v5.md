# analysis deepseek cls repo v5

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek-cls-repo-v5_20260518T203800_result.json`
- **Structured JSON:** [`519aec0194bfe77b99ab.json`](../../sessions/51/519aec0194bfe77b99ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 训练状态：成功完成

| 项目 | 值 |
|------|------|
| 模型 | deepseek-coder-6.7b-instruct (LoRA, qkvo, 16.8M params) |
| 数据 | train=67,343 / val=7,452 (repo-level, seed 42) |
| 总步数 | 6,315 steps (3 epochs) |
| 总训练时间 | 17h 35m 12s |
| Final train loss | **0.0399** |
| EXIT_CODE | 0 |

### Eval loss 逐 epoch

| Epoch | Eval Loss |
|-------|-----------|
| 1 | 0.0886 |
| 2 | 0.1587 |
| 3 | 0.1975 |

### Checkpoints

| 路径 | 说明 |
|------|------|
| `/root/autodl-tmp/checkpoints_deepseek_cls_repo_v5/best/` | Best model (LoRA adapter, 64MB) |
| `/root/autodl-tmp/checkpoints_deepseek_cls_repo_v5/checkpoint-2105/` | Epoch 1 checkpoint |
| `/root/autodl-tmp/checkpoints_deepseek_cls_repo_v5/checkpoint-6315/` | Epoch 3 (final) checkpoint |

### 分析

- **无 W&B logging**，指标仅来自日志。
- **Eval loss 逐 epoch 上升**（0.089 → 0.159 → 0.197），train loss 持续下降至 0.04，存在明显 overfitting。Best model 应为 epoch 1 的 checkpoint（eval loss 最低 0.0886）。日志显示 best model 在训练结束时保存，需确认其选择逻辑是否基于 eval loss（如果是，best/ 应等价于 checkpoint-2105）。
- **与 s123 对比**：s123 per-test accuracy 74.93%。考虑到 eval loss 在 epoch 1 已经很低（0.089），best checkpoint 的推理精度有望接近或匹配 s123 水平。但 overfitting 趋势说明 3 epoch 偏多，epoch 1 是最佳停止点。

### 建议下一步
1. 用 best checkpoint 跑 inference，获取 per-test accuracy 与 s123 (74.93%) 对比
2. 确认 `best/` 对应的是哪个 epoch（大概率 epoch 1）

---

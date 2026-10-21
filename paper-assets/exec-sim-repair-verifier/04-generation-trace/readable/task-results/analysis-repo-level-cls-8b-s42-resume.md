# analysis repo level cls 8b s42 resume

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_repo-level-cls-8b-s42-resume_20260515T183902_result.json`
- **Structured JSON:** [`6c0a961981ad00f5bd25.json`](../../sessions/6c/6c0a961981ad00f5bd25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练结果摘要

- **完成状态**：✅ 完成（EXIT_CODE=0）
- **总 steps**：6633/6633（3 epochs）
- **总训练时间**：20h 40m（74425s）
- **最终 train_loss**：0.4284
- **最终 eval_loss**：0.4768 @ step 6600
- **Trainer best_metric**：0.0796 @ step 200（来自原始训练 `checkpoints_repo_cls_8b_conda/checkpoint-200`）
- **Resume 阶段最佳 eval_loss**：0.2516 @ step 4200
- **异常/告警**：**严重过拟合** — eval_loss 从 epoch 1 的 ~0.08 持续上升到 epoch 3 的 ~0.48

### Checkpoint 列表

checkpoint-800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600, 3800, 4000, 4200, 4400, 4600, 4800, 5000, 5200, 5400, 5600, 5800, 6000, 6200, 6400, 6600, 6633, best（共 32 个目录）

### Eval Loss 曲线

| Step | Eval Loss | 备注 |
|------|-----------|------|
| 200  | 0.0796 | ← 原训练 epoch 1，overall best |
| 400  | 0.0927 | 原训练 |
| 600  | 0.0937 | 原训练（resume 起点）|
| 800  | 0.1717 | resume 开始 |
| 1000 | 0.1820 | |
| 1200 | 0.2046 | |
| 1400 | 0.3226 | |
| 1600 | 0.2758 | |
| 1800 | 0.2764 | |
| 2000 | 0.3210 | |
| 2200 | 0.3063 | ~epoch 1 结束 |
| 2400 | 0.3444 | |
| 2600 | 0.2576 | |
| 2800 | 0.2744 | |
| 3000 | 0.2975 | |
| 3200 | 0.2981 | |
| 3400 | 0.4132 | |
| 3600 | 0.2612 | |
| 3800 | 0.3429 | |
| 4000 | 0.3694 | |
| 4200 | 0.2516 | ← **resume 阶段最佳** |
| 4400 | 0.2811 | ~epoch 2 结束 |
| 4600 | 0.3713 | |
| 4800 | 0.3919 | |
| 5000 | 0.4417 | |
| 5200 | 0.4021 | |
| 5400 | 0.4070 | |
| 5600 | 0.4002 | |
| 5800 | 0.5263 | ← 最差点 |
| 6000 | 0.4230 | |
| 6200 | 0.4385 | |
| 6400 | 0.4769 | |
| 6600 | 0.4768 | epoch 3 结束 |

### 关键观察

1. **过拟合明显**：eval_loss 在 epoch 2 后期（step 4200 之后）急剧上升，从 ~0.25 升到 ~0.48，第 3 epoch 全程在 0.37-0.53 之间波动。
2. **best 目录风险**：`best_model_checkpoint` 指向的是 **另一个目录** `checkpoints_repo_cls_8b_conda/checkpoint-200`（原始训练），不是当前 resume 目录。`best/` 目录是训练结束时保存的（adapter 约 61MB），需要确认它是否真的加载了那个 checkpoint-200 的权重，还是保存了最终 step 6633 的权重。
3. **如果做推理评测，建议优先用 checkpoint-4200**（resume 阶段最优，eval_loss=0.2516），而非 `best/` 或最终 checkpoint。

---

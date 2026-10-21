# analysis deepseek cls repo v5

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek-cls-repo-v5_20260518T204003_result.json`
- **Structured JSON:** [`c64c2f5f07bba009c955.json`](../../sessions/c6/c64c2f5f07bba009c955.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。以下是 **deepseek-cls-repo-v5** 训练结果汇总：

## 训练状态
- **正常完成**，EXIT_CODE=0，3 epochs / 6315 steps
- 训练时长：17h 35m（63312s）
- W&B：**未集成**（日志中无 wandb 记录）

## Eval Loss 趋势

| Epoch | eval_loss |
|-------|-----------|
| 1     | **0.0886** |
| 2     | 0.1587    |
| 3     | 0.1975    |

Final train_loss: **0.0399**

**明显过拟合**：eval_loss 从 epoch 1 起单调递增（0.089 → 0.159 → 0.197），train_loss 极低。最佳 eval 性能在 epoch 1。

## Checkpoints

| 路径 | 大小 | 说明 |
|------|------|------|
| `checkpoint-2105/` | 195M | Epoch 1（含 optimizer state）|
| `checkpoint-6315/` | 195M | Epoch 3（含 optimizer state）|
| `best/` | 67M | Epoch 3 保存（仅 LoRA adapter）|

**注意**：`best/` 目录在 epoch 3 结束时保存，但 epoch 3 的 eval_loss 最高（0.197）。实际最优 eval 性能对应 **checkpoint-2105**（epoch 1, eval_loss 0.0886）。后续 eval 实验建议同时测 checkpoint-2105 和 best，确认哪个泛化更好。

## Registry 更新
- conclusion: `success`
- metrics: 含 eval_loss_epoch1/2/3, final_train_loss, total_steps, train_time
- spec: 补充了 checkpoint_path 和 log_path

---

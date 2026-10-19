# ops verify random s44 training

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-random-s44-training_20260515T103139_result.json`
- **Structured JSON:** [`b0d6d4969d84b7a62fbe.json`](../../sessions/b0/b0d6d4969d84b7a62fbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整日志已获取。报告如下：

---

## random_s44 Qwen 训练详情

### 每个 eval 点指标

| Step | val_loss | R@1 | R@5 | R@10 | 备注 |
|------|----------|-----|-----|------|------|
| 500 | 0.4252 | 0.6009 | 0.9583 | 1.0 | **Best val_loss & Best R@1** |
| 1000 | 0.4695 | 0.5638 | 0.9524 | 1.0 | patience 1/2 |
| 1500 | 0.4918 | 0.5592 | 0.9504 | 1.0 | patience 2/2 → **触发 early stopping** |
| Final eval | 0.4943 | 0.5542 | 0.9514 | 1.0 | early stop 后的最终评估 |

### 关键结论

- **总训练 steps：1500**（非 500）。Epoch 1 完整跑完（1408 steps），Epoch 2 跑到 step 1500（即 epoch 2 的第 92 步）时 early stopping 触发
- **Early stopping 触发原因**：val_loss 连续 2 次 eval（step 1000、step 1500）未优于 step 500 的 best，patience=2 耗尽
- **best_by_val_loss checkpoint** = step 500（val_loss=0.4252）
- **best_by_recall_at_1 checkpoint** = step 500（R@1=0.6009）
- **final checkpoint** = step 1500（early stop 时的模型，R@1=0.5542）

### 与 experiments_v1.md 记录的差异

experiments_v1.md 写 "early-stopped at step 500" **是错误的**。实际情况：
- **best checkpoint 在 step 500**，但 early stopping 在 **step 1500** 触发
- 训练从 step 500 继续到 step 1500，期间 val_loss 持续恶化（0.4252 → 0.4695 → 0.4918），patience 在 step 1500 才耗尽

### 训练时长解释

- 1408 batches/epoch × 2 epochs = 2816 max steps，实际跑了 1500 steps
- 按时间戳：01:58 开始 → 08:32 结束 ≈ 6.5h，约 230 steps/h，与 1500 steps 吻合

---

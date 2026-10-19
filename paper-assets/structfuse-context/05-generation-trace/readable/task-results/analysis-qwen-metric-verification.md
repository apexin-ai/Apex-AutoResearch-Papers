# analysis qwen metric verification

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen_metric_verification_20260516T025821_result.json`
- **Structured JSON:** [`232d0af9ce8f9dd7bcfe.json`](../../sessions/23/232d0af9ce8f9dd7bcfe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在所有数据都齐了。

## 结论

### Pool Size 分析

**所有 Qwen M2 subrun 的 eval R@1 都来自同一种评估：in-training eval，pool size = 8**（1 positive + 7 negatives）。

训练代码 `train.py:evaluate()` 使用 ContrastiveDataset 的 DataLoader，每个样本包含 1 个正例 + `num_negatives=7` 个负例，logits 形状为 `[batch_size, 8]`。**没有使用 eval_p2b.py (pool≈25) 或 eval_p2b_pooled.py (pool=50) 对 Qwen M2 checkpoint 做过独立 eval。**

### 0.6009 vs 0.5542 的差异来源

**不是 pool size 不同，而是训练阶段不同：**
- **Registry 记录的 0.6009** = `best_by_recall_at_1` checkpoint 的 R@1，来自 **eval@500**（训练早期的峰值）
- **训练日志解析的 0.5542** = `[Final eval]` 的 R@1，来自 **early stopping 时刻的模型状态**

模型在 step 500 时 R@1 达到峰值，之后随训练继续而下降（过拟合）。两组数字的 pool size 完全相同（都是 8）。

### 各 subrun 汇总

| Subrun | Best R@1 (step) | Final R@1 | Best Checkpoint |
|--------|-----------------|-----------|-----------------|
| random_s42 | 0.5527 (@1000) | 0.5503 | best_by_recall_at_1 |
| random_s43 | 0.5554 (@1500) | 0.5501 | best_by_recall_at_1 |
| **random_s44** | **0.6009 (@500)** | **0.5542** | best_by_recall_at_1 |
| embed_s43 | 0.5606 (@1500) | 0.5655 | best_by_recall_at_1 |
| **embed_s44** | **0.5942 (@500)** | **0.5470** | best_by_recall_at_1 |
| dataflow_s43 | 0.5541 (@1500) | 0.5564 | best_by_recall_at_1 |
| dataflow_s44 | 仍在训练 | — | — |

**所有 eval 的 pool size = 8（in-training eval）。没有做过 pool=20 或 pool=50 的独立评估。**

### Best Checkpoint 路径

```
/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/{subrun}/best_by_recall_at_1/
/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/{subrun}/best_by_val_loss/
/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/{subrun}/final/
```

random_s44 和 embed_s44 的 best_by_recall_at_1 都是 step 500 的 checkpoint。如果需要做更严格的评估（pool=50），需要用 `eval_p2b_pooled.py` 对这些 checkpoint 单独跑一次。

---

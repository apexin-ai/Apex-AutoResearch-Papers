# research n2 analysis prep

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_n2_analysis_prep_20260515T122529_result.json`
- **Structured JSON:** [`443406c63383b73c98e4.json`](../../sessions/44/443406c63383b73c98e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，汇总如下：

## N2 End-to-End Finetune 训练进度报告

### DeBERTa-v3-base (cuda:0, PID 231453)

| 项目 | 状态 |
|------|------|
| 启动时间 | 20:12 UTC |
| 当前进度 | Fold 2/5, epoch 1, step ~350/1000 |
| 总进度 | ~22% (3350/15000 steps) |
| 已耗时 | ~14 min |
| 预估剩余 | ~49 min (ETA ~21:15 UTC) |

**Fold 1 结果**: accuracy=**0.5540**, pairwise AUC: d0v1=0.9761, d1v2=0.5738, d2v3=0.7404

### RoBERTa-base (cuda:1, PID 235755)

| 项目 | 状态 |
|------|------|
| 启动时间 | 20:24 UTC |
| 当前进度 | Fold 1/5, epoch 1, step 950/1000 |
| Loss 趋势 | 不理想 (0.53→0.91 上升中) |

### 输出格式

- **结果路径**: `results/n2_{model}_finetune/results.json`
- **预测文件**: `results/n2_{model}_finetune/fold_predictions.npz` (preds, probs, labels, fold_indices)
- **指标**: accuracy (mean±std), per-class precision/recall/F1, pairwise AUC (d0v1, d1v2, d2v3)
- **CV**: 5-fold stratified, 20000 samples balanced (5000/class)
- **Config**: max_len=512, batch_size=16, lr=2e-5, epochs=3, warmup=0.1

### 关键观察

1. **DeBERTa Fold 1 accuracy 55.4% 远低于 RF baseline 78.2%**。仅比 random (25%) 好一倍，但远不及 RF 的 feature engineering 方案。
2. Pairwise AUC 分化严重：d0v1=0.976（近乎完美）但 d1v2=0.574（接近随机），说明模型很容易区分"深/浅"文本但无法精细区分相邻深度。
3. RoBERTa 的 loss 在 epoch 1 后段反而上升，可能学习率不合适或数据 tokenization 有问题。
4. 当前 `results.json` 是 dry run 残留（全零），完整 5-fold 结果将在 ~21:15 UTC 覆写。

### 对比基准

| Method | 4-class Accuracy |
|--------|-----------------|
| RF (手工特征) | **78.2%** |
| DeBERTa-v3-base (fold 1) | 55.4% |
| Random | 25.0% |

如果最终 5-fold 均值仍在 55-60% 区间，这实际上是 **有利于我们论文的结果**——证明 end-to-end transformer 在此任务上不如 interpretable feature engineering，支持我们方法的价值主张。

---

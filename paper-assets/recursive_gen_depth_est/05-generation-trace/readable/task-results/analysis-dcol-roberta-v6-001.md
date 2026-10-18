# analysis dcol roberta v6 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dcol_roberta_v6_001_20260515T055751_result.json`
- **Structured JSON:** [`67935edd047d2ff162cd.json`](../../sessions/67/67935edd047d2ff162cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## dcol_roberta_v6_001 分析结果

### 训练状态：正常完成
- 无 NaN、无 collapse（collapse guard 在 step 500 通过，acc=0.35 ≥ 0.3）
- Early stopping 在 epoch 4 触发（patience=3，best epoch=1）
- EXIT_CODE=0

### Epoch 级指标

| Epoch | Train Loss | Train Acc | Val Loss | Val Acc | Val MAE |
|-------|-----------|-----------|----------|---------|---------|
| 1 | 1.1341 | 60.3% | 0.7406 | **64.4%** | 0.4037 |
| 2 | 0.7257 | 70.8% | 1.0421 | 54.5% | 0.5335 |
| 3 | 0.6398 | 73.5% | 0.9285 | 60.2% | 0.4454 |
| 4 | 0.5942 | 75.0% | 1.0114 | 58.4% | 0.4713 |

### 最终测试指标（best checkpoint, epoch 1）

| 指标 | 值 |
|------|-----|
| **Test Accuracy** | **64.48%** |
| Test MAE | 0.4052 |
| Best Val Accuracy | 64.36% |

### 结论判定：**NEGATIVE**

- Test acc = 64.5% < RF baseline = 78.2%，**delta = -13.7pp**
- 严重过拟合：train acc 从 60% 涨到 75%，val acc 在 epoch 1 之后持续下降
- RoBERTa-large 解决了 DeBERTa 的数值稳定性问题（无 NaN/collapse），但准确率远低于 baseline

### 文件路径
- Checkpoint: `/root/autodl-tmp/recursive_gen_depth_est/checkpoints/dcol_roberta_v6/best_model.pt` (1.3GB)
- Results: `checkpoints/dcol_roberta_v6/results.json`
- Log: `~/runs/recursive_gen_depth_est/dcol_roberta_v6_001.log`

### 总结
DCOL 系列 v1-v6 全部失败。v6 用 RoBERTa-large 终于解决了稳定性问题，但 DCOL 方法本身在此任务上无法超越 RF baseline（78.2%）。模型在 epoch 1 即达到最佳 val acc（64.4%），之后严重过拟合，说明 DCOL loss 对这个 4-class depth estimation 任务的表达能力不足。建议放弃 DCOL 方向。

---

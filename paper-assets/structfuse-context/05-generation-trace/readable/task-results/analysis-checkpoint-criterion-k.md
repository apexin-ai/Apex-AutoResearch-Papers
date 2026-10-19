# analysis checkpoint criterion K

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_checkpoint-criterion-K_20260515T031356_result.json`
- **Structured JSON:** [`ec271dfdb9f0c19ce54c.json`](../../sessions/ec/ec271dfdb9f0c19ce54c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册（`art_20260515_884407`）。核心发现：

**Alignment rate**: 完成的 4 个 full M2 runs 中，2/4 (50%) 两个 criterion 选中同一 checkpoint。

**Divergence pattern**:
- Qwen s43: val_loss 选 step 500，R@1 选 step 1500，R@1 差 +1.97pp
- StarCoder s42: val_loss 选 step 1000，R@1 选 step 2500，R@1 差 +0.64pp
- StarCoder 发散更严重（1500 步差距），与其更大的 pretrained margin 一致

**建议**: 论文主表报 best_by_R@1 结果（target metric），ablation 中展示两种 criterion 的对比表（mean delta +0.65pp）。

**K=7**: 所有正式实验固定 K=7，无 K ablation。K=7 合理性来自 batch_size=8 对齐、DPR 等文献惯例、以及 hard_negative_ratio=0.5 的平衡设计。建议论文中将 K 敏感性列为 limitation/future work。

---

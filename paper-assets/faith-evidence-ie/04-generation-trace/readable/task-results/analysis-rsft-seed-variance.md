# analysis rsft seed variance

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rsft_seed_variance_20260515T073913_result.json`
- **Structured JSON:** [`7d226b689d01df3b8cee.json`](../../sessions/7d/7d226b689d01df3b8cee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## RSFT Seed Variance Analysis

### Metrics Summary

| Metric | s43 (seed=43) | s44 (seed=44) | SFT baseline | Pass? |
|--------|---------------|---------------|-------------|-------|
| rel_f1 (F1) | 0.0481 | 0.0509 | 0.4057 | **FAIL / FAIL** |
| evi_f1 (Evi-F1) | 0.7368 | 0.7798 | 0.798 | **FAIL / FAIL** |
| Ign-F1 | 0.0481 | 0.0509 | — | — |
| EDCR | 0.6629 | 0.6030 | — | — |
| #preds | 861 | 771 | — | — |

Precision/recall 分解日志中未记录，只有上述汇总指标。

### Training Details

| | s43 | s44 |
|---|---|---|
| train_loss (avg) | 0.6148 | 0.6138 |
| train_loss (last step) | 0.5891 | 0.5841 |
| eval_loss (epoch 3) | 0.7622 | 0.7625 |
| eval_loss (epoch 2) | 0.7596 | 0.7590 |
| mean_token_accuracy | 0.8291 | 0.8290 |
| epochs | 3 | 3 |
| steps | 510 | 510 |
| runtime | 1h56m (~1.93h) | 1h53m (~1.88h) |
| train_samples | 2718 | 2718 |
| batch_size | 4 | 4 |
| peak_lr | ~2e-5 | ~2e-5 |

中间 eval (step 170, ~epoch 1):
- s43: F1=0.0467, Evi-F1=0.7564
- s44: F1=0.0448, Evi-F1=0.7545

### Checkpoint Paths
- s43: `/root/autodl-tmp/rsft_output_s43/` (checkpoints: 350, 400, 450, 500, 510 + final adapter, 528MB)
- s44: `/root/autodl-tmp/rsft_output_s44/` (same结构)

### Conclusion

**两个 seed 均 FAIL。**

- **rel_f1 灾难性下降**：0.048–0.051 vs baseline 0.4057，下降了 **~8x**，RSFT 几乎完全破坏了关系抽取能力
- **evi_f1 略低于 baseline**：s44 (0.7798) 非常接近 0.798 但未达标，s43 (0.7368) 差距更大
- **Seed variance**：rel_f1 variance 很小（0.0028），evi_f1 variance 较大（0.0430），但不影响结论
- **与 parent run (seed=42) 一致**：原始 seed=42 结论为 negative，s43/s44 确认这不是随机性导致的，RSFT 方法本身存在根本问题
- **训练正常但效果崩坏**：train loss 正常下降（0.67→0.58），token accuracy ~86%，无报错，说明模型确实在学习 RSFT 数据，但学到的分布严重伤害了 rel_f1

**建议**：RSFT（CED-filtered rejection sampling）在当前配置下不可行，3 个 seed 一致证实 negative result。问题大概率在于 RSFT 训练数据的分布偏移导致模型丧失关系判断能力。

---

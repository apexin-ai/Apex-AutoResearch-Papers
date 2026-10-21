# analyze mvp2 rsft train r1

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_mvp2_rsft_train_r1_20260515T073626_result.json`
- **Structured JSON:** [`3b8cb4e5ee68449875aa.json`](../../sessions/3b/3b8cb4e5ee68449875aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE / negative。

## 实验结果总结

**mvp2_rsft_train_r1** — **NEGATIVE**

| 指标 | 最终值 | Baseline | 变化 |
|------|--------|----------|------|
| **rel_f1** | 0.0483 | 0.4057 | **↓88.1%** |
| **evi_f1** | 0.7646 | 0.798 | ↓4.2% |
| ign_f1 | 0.0483 | — | — |
| EDCR | 0.6534 | — | — |
| train_loss | 0.6116 | — | — |
| eval_loss | 0.7624 | — | — |

**关键观察**：
- 训练正常完成，checkpoint 完整（adapter_model.safetensors 528MB），耗时 ~1h56m
- **rel_f1 灾难性崩塌**：从 baseline 0.4057 跌至 0.0483，仅为原始值的 12%
- Evi-F1 也低于 baseline（0.7646 vs 0.798）
- 仅产出 848 个预测（step 170 时为 881），数量偏低
- 从 step 170 到 step 510，F1 仅从 0.0458 微升至 0.0483，说明从 epoch 1 开始 rel_f1 就已经崩了
- train_loss 正常下降（0.65→0.57），eval token accuracy 稳定在 0.829——模型在"学习"，但学到的不是正确的 relation extraction 行为

---

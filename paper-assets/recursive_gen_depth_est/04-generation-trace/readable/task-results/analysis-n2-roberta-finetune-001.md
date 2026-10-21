# analysis n2 roberta finetune 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_n2_roberta_finetune_001_20260515T132412_result.json`
- **Structured JSON:** [`48d78f391e4a56c64ba2.json`](../../sessions/48/48d78f391e4a56c64ba2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。结果摘要：

## n2_roberta_finetune_001 结果

| 指标 | RoBERTa | DeBERTa | RF baseline |
|------|---------|---------|-------------|
| **Accuracy** | **59.5% ± 3.2%** | 58.3% ± 4.7% | **78.2%** |
| d1v2 AUC | 0.752 | 0.733 | — |
| d2v3 AUC | 0.735 | 0.755 | — |

**Per-class F1**: d0=0.958, d1=0.416, d2=0.261, d3=0.647

**关键发现**:
1. RoBERTa 与 DeBERTa 结果几乎相同（差值在 noise 范围），双 backbone 均低于 RF **~19pp**，排除模型选择偏差
2. d0 (原始文本) 近乎完美可分；d1/d2 几乎不可区分 (d2 F1 仅 0.261)
3. 模型倾向将 d1/d2 预测为 d3 (d3 recall=0.931 但 precision=0.496)
4. 轻微过拟合：部分 fold val_acc 随 epoch 递减
5. 结果目录无 feature analysis 产出

**N2 结论**: End-to-end PLM finetune 无法匹配 hand-crafted features 的性能，hand-crafted features 捕获了 PLM raw text representation 未能学到的递归生成深度信号。

---

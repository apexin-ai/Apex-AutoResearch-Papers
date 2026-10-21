# analysis a2 confidence prediction

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a2_confidence_prediction_20260522T081521_result.json`
- **Structured JSON:** [`41566aa4abeecccf6357.json`](../../sessions/41/41566aa4abeecccf6357.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

A2 完成。结果概要：

**Within-arch 5-fold CV AUC（单特征 logistic regression，特征 = pure model 的 |target loglikelihood|）：**

| Benchmark | Helped AUC | Hurt AUC |
|-----------|-----------|----------|
| LAMBADA | **0.75-0.76** | **0.73-0.75** |
| ARC-Easy | 0.66-0.71 | 0.54-0.60 |
| HellaSwag | 0.54-0.56 | 0.51-0.52 |
| PIQA | 0.56-0.60 | 0.45-0.47 |

**Cross-arch transfer AUC ≈ Within-arch AUC**（specificity delta: helped = -0.001, hurt = -0.010）

**核心发现：**
1. **LAMBADA 预测能力强**：仅用 pure model confidence 单一特征，AUC 达 0.75，远超 random baseline（0.50）
2. **Helped 比 Hurt 更可预测**：across all benchmarks，helped AUC consistently > hurt AUC
3. **零架构特异性**：transfer AUC 与 within-arch AUC 几乎相同（delta ≈ 0），说明 confidence margin 是**完全 architecture-general** 的信号——在 GDN 上训练的预测器直接迁移到 RetNet/HGRN2 不损失性能
4. **HellaSwag/PIQA 信号弱**：可能因为 acc_norm 的 length normalization 削弱了 raw loglikelihood 的预测力；PIQA hurt AUC < 0.50 说明此 benchmark 的 hurt 例子无法由 confidence margin 预测

输出文件在 `westb-48145:/root/entrainment_gated_ft/results/a2_prediction_framework/`。

---

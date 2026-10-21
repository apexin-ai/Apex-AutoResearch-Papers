# exp e theta v1 logreg

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_e_theta_v1_logreg_20260520T154053_result.json`
- **Structured JSON:** [`aa7f258845b71d819c28.json`](../../sessions/aa/aa7f258845b71d819c28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**E_θ V1: Full Features + Ridge Regression** (7 configs, 46,758 instances)

| Metric | F1 |
|--------|-----|
| Fixed θ=0.5 | 0.7747 |
| Adaptive (predicted) | 0.7932 (+1.84%) |
| Oracle | 0.8279 (+5.31%) |

**关键发现：**
- Ridge 回归对所有实例退化预测 θ=0.3 — 线性特征无法区分 per-instance 最优 θ
- +1.84% 的整体增益完全来自 FewNERD（占 80.5% 数据，θ=0.3 比 0.5 好 +2.35%），而在 CoNLL 上 θ=0.3 反而掉分（-0.56%）
- 83% 的实例 oracle θ=0.5，只有 17% 受益于非默认阈值
- 特征重要性：`degeneracy_level` > `agreement_mean` > `n_unique_entities` > `lp_variance`；dataset/model 指示特征系数接近零
- Oracle headroom 5.31% 中，线性预测器仅捕获 34.7%

结果已保存并注册为 `art_20260520_ecc20e`。

---

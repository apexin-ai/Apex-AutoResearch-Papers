# code plan001 final metrics

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan001-final-metrics_20260520T114936_result.json`
- **Structured JSON:** [`995f36db343eb9f1cbde.json`](../../sessions/99/995f36db343eb9f1cbde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。`misclass_amplifies_rate` 已补齐并写入 registry：

| 拓扑 | misclass_amplifies_rate | 解释 |
|------|------------------------|------|
| collider | 0% | 误分类总是衰减 collider bias（保留已有值） |
| m_bias | 29.2% | 保留已有值 |
| mediation_mixed | **100%** | C=I 下 τ 无偏（bias_I=0），任何误分类都引入偏差 |
| mediation_same | **100%** | 同上 |
| frontdoor_mixed | **100%** | true τ=0，C=I 下已有 confounding bias≈0.5，误分类几乎总是加剧 |
| frontdoor_same | **99.97%** | 同上，极少数 C 恰好减小偏差 |

mediation 的 100% 是因为模型在 C=I 下正确指定（baseline bias=0），所以 misclassification 无论方向都放大偏差。front-door 的接近 100% 是因为 U 混淆已经把 τ 推到 ~0.5（true=0），误分类进一步恶化。

---

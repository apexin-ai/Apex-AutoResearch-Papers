# analysis cross model loo

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_model_loo_20260515T040026_result.json`
- **Structured JSON:** [`0a4cc9f04ab16cd70bd4.json`](../../sessions/0a/0a4cc9f04ab16cd70bd4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Cross-model LOO 泛化测试结果：

| Rotation | Train size | Test size | 4-class acc | 95% CI | d1v2 AUC | d2v3 AUC |
|----------|-----------|-----------|-------------|--------|----------|----------|
| Hold-out Pythia | 120,000 | 60,000 | 0.6242 | [0.6206, 0.6282] | 0.5617 | 0.6534 |
| Hold-out OLMo | 120,000 | 60,000 | 0.6921 | [0.6886, 0.6959] | 0.7687 | 0.6862 |
| Hold-out GPT-2 XL | 120,000 | 60,000 | 0.6756 | [0.6719, 0.6792] | 0.8157 | 0.6639 |

**Per-class recall:**

| Rotation | d0 | d1 | d2 | d3 |
|----------|------|------|------|------|
| Hold-out Pythia | 1.000 | 0.493 | 0.268 | 0.736 |
| Hold-out OLMo | 0.993 | 0.755 | 0.433 | 0.588 |
| Hold-out GPT-2 XL | 0.985 | 0.747 | 0.526 | 0.445 |

**Mean cross-model 4-class accuracy: 0.664** (chance = 0.25)。

Pythia 作为 hold-out 时泛化最差（acc=0.624, d1v2 AUC 仅 0.56），说明 Pythia 的 depth 信号模式与 OLMo/GPT-2 XL 差异较大。OLMo 和 GPT-2 XL 作为 hold-out 时表现更好（0.69/0.68）。所有 rotation 中 depth-0（原始文本）recall 接近 1.0，depth-2 recall 最低，符合中间深度最难区分的预期。

---

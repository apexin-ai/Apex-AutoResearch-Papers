# analysis r6 2a meta pooling

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r6-2a-meta-pooling_20260525T074614_result.json`
- **Structured JSON:** [`6b03f004f0d415b0a910.json`](../../sessions/6b/6b03f004f0d415b0a910.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Meta-analytic pooling 完成。结果：

| K | Predictor | Pooled β_std | 95% CI | I² | Q p |
|---|-----------|-------------|--------|-----|-----|
| 3 | K_eff | 0.3559 | [0.2669, 0.4450] | 87.7% | <0.001 |
| 3 | η_max | 0.2638 | [0.1584, 0.3691] | 91.3% | <0.001 |
| 5 | K_eff | 0.4355 | [0.3184, 0.5526] | 98.9% | <0.001 |
| 5 | η_max | 0.1020 | [-0.0549, 0.2589] | 99.4% | <0.001 |
| 7 | K_eff | 0.4005 | [0.2981, 0.5029] | 99.4% | <0.001 |
| 7 | η_max | 0.0842 | [-0.0828, 0.2513] | 99.8% | <0.001 |

核心发现：
- **K_eff 在所有 K 值下均显著**（CI 不含 0），pooled β_std ≈ 0.36–0.44，且随 K 增大效应保持稳定
- **η_max 仅在 K=3 时显著**（CI 不含 0），K=5/7 时 CI 跨零，效应量从 0.26 衰减到 0.08
- **I² 很高**（87–99%），说明条件间异质性大，random-effects 模型合理

结果已保存到 `/root/cert_manip_resist_eval/artifacts/results/plan001/meta_analytic_pooling.json`。

---

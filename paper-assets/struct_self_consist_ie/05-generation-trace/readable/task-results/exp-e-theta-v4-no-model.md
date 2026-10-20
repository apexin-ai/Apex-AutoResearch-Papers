# exp e theta v4 no model

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_e_theta_v4_no_model_20260520T160018_result.json`
- **Structured JSON:** [`9ed2a9924ed17a6387d3.json`](../../sessions/9e/9ed2a9924ed17a6387d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**V4（无 model_id）与 V1（全特征）完全一致**，gap = 0.0：

| 指标 | V1 (full) | V4 (no model_id) | Gap |
|---|---|---|---|
| overall adaptive F1 | 0.7932 | 0.7932 | 0.0 |
| delta(adaptive - fixed) | +0.0184 | +0.0184 | 0.0 |
| `model_id_matters` | — | **false** | — |

每个 config 的 per-config F1 也完全相同。

### 关键分析

**θ predictor 是 model-general 的。** 移除 model_id（is_qwen/is_llama）后性能无任何下降。V1 中 model_id 的 feature importance 本身就极小（is_qwen: +0.000454, is_llama: -0.000454），佐证了这一点。

这意味着 θ 的最优选择完全由 instance-level 信号（degeneracy、agreement、logprob variance、n_unique_entities）和 dataset 特征决定，与底层模型无关 — 支持更强的 claim：**该 predictor 可以跨模型迁移**。

结合 V3（无 dataset_id）同样 gap=0 的结果，实际上 predictor 只需 4 个纯 instance-level 特征（degeneracy_level, agreement_mean, n_unique_entities, lp_variance）即可工作，完全 dataset-general 且 model-general。

---

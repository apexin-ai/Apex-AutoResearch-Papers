# exp e theta v3 no dataset

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_e_theta_v3_no_dataset_20260520T154109_result.json`
- **Structured JSON:** [`84bcb7d3e5cc6bc8f26f.json`](../../sessions/84/84bcb7d3e5cc6bc8f26f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**E_θ V3 完成。**

结果：移除 dataset_id 特征后，与 V1 完全一致（gap = 0.0pp）。

| 指标 | V1 (full features) | V3 (no dataset_id) | 差异 |
|------|-------------------|---------------------|------|
| adaptive F1 | 0.7932 | 0.7932 | 0.0000 |
| delta vs fixed | +0.0184 | +0.0184 | 0.0000 |

**原因**：V1 中 dataset indicator 系数已接近零（is_scierc=+0.002, is_conll=-0.001, is_fewnerd=0.000），移除后不影响预测。

**结论**：θ predictor 完全 dataset-general，所有预测信号来自 instance-level 特征（degeneracy > agreement_mean > n_unique_entities > lp_variance）。对论文 universality claim 是正面支撑。

已注册 artifact: `art_20260520_53b086`

---

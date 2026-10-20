# code consistency module

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_consistency_module_20260514T042604_result.json`
- **Structured JSON:** [`e28ac6026c0ddafd2cfe.json`](../../sessions/e2/e28ac6026c0ddafd2cfe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`consistency.py` 已创建并注册。模块包含：

- **`fleiss_kappa_surface`** — 将 N 次采样视为 N 个 rater，对 (text, type) entity 做 Fleiss' Kappa，含所有边界情况处理
- **`structural_consistency_soft_jaccard`** — 按 type 分组后用 Hungarian matching 做 span-level soft Jaccard，支持 `ner` 和 `eae` 两种 subtask
- **`oracle_best_of_n`** — 从 N 个 sample 中选 F1 最高的，lazy import `evaluation.per_instance_f1`
- **`compute_all_consistency_scores`** — 聚合函数，对所有 instance 批量计算上述三个指标

全部测试通过：perfect agreement → 1.0，partial overlap → 0.6154，no overlap → 0.0，边界情况（空集、单 sample）均正确返回。

---

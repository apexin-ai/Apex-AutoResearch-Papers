# analysis selfbleu ablation olmo

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_selfbleu_ablation_olmo_20260521T152819_result.json`
- **Structured JSON:** [`c24030c978cc602f9941.json`](../../sessions/c2/c24030c978cc602f9941.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已写入 `artifacts/olmo_selfbleu_ablation.md`。

**OLMo-1B C4 selfbleu ablation 结果：**
- K\*_15D = 1, K\*_14D = 1, **ΔK\* = 0**
- 去掉 self_bleu 不改变 K\*
- 0v1 是唯一可区分对（AUC ≈ 0.986/0.983），1v2 及之后全部 ≈ 0.50（随机水平）
- 所有 delta 都很小（-0.005 ~ +0.003），self_bleu 对分类贡献可忽略

---

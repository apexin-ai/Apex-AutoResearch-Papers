# data ign f1 fix flat nli s43

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_ign_f1_fix_flat_nli_s43_20260516T001833_result.json`
- **Structured JSON:** [`a36e38059c65a23c8e25.json`](../../sessions/a3/a36e38059c65a23c8e25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总两个实验的关键指标：

### rsft_flat_nli_s43

| 指标 | metrics.json (旧) | metrics_v2.json (修正) |
|------|-------------------|----------------------|
| F1 (rel_f1) | 0.0022 | 0.0022 |
| Ign-F1 | 0.0022 | 0.0023 |
| Evi-F1 | 0.8533 | 0.8533 |

这个模型 rel_f1 极低（0.22%），几乎没有正确预测关系三元组，Ign-F1 修正后差异可忽略。

### rsft_topk3_reeval

| 指标 | metrics.json (旧) | metrics_v2.json (修正) |
|------|-------------------|----------------------|
| F1 (rel_f1) | 0.4454 | 0.4454 |
| Ign-F1 | 0.4454 | 0.4364 |
| Evi-F1 | 0.8088 | 0.8088 |

修正后 Ign-F1 从 0.4454 降至 0.4364（-0.0090），说明之前有约 0.9pp 的训练集泄漏膨胀。两个目录的 metrics_v2.json 均已就绪。

---

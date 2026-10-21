# read d102 1 7b results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_read_d102_1_7b_results_20260518T104239_result.json`
- **Structured JSON:** [`a306c11666fd1f8ae0e2.json`](../../sessions/a3/a306c11666fd1f8ae0e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D102 1.7B k=1 s42 eval 结果：

| 指标 | k=1 (D102) | k=3 (旧) | 差异 |
|------|-----------|----------|------|
| **rel_f1** | 0.5290 | 0.5219 | **+0.71** |
| **ign_f1** | 0.5122 | 0.5050 | **+0.72** |
| **evi_f1** | 0.8243 | 0.8309 | -0.66 |
| **edcr** | 0.6224 | 0.6297 | -0.73 |

其他关键数据：
- n_predictions: 16154, n_truncated: 249, n_format_ok: 984/985
- field_compliance_rate: 74.4%（evidence_format_rate 同）
- 推理耗时: 8836s
- 模型: `rsft_output_qwen3_1_7b_k1/checkpoint-567`

**结论**: k=1 的 rel_f1/ign_f1 略优于 k=3（+0.7pp），但 evi_f1 和 edcr 略低（-0.7pp）。总体差异很小，k=1 和 k=3 性能基本持平。

---

# read d102 llama results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_read_d102_llama_results_20260518T112149_result.json`
- **Structured JSON:** [`6f9ba4e16314b1adf855.json`](../../sessions/6f/6f9ba4e16314b1adf855.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D102 LLaMA-3.1-8B k=1 s42 结果：

| 指标 | k=1 (本次) | k=3 (旧) | 变化 |
|------|-----------|----------|------|
| rel_f1 | **0.5839** | 0.3936 | +19.03 |
| ign_f1 | **0.5714** | 0.3801 | +19.13 |
| evi_f1 | **0.8238** | 0.8026 | +2.12 |
| edcr | **0.5799** | 0.6696 | -8.97 |
| evi_f1_joint | **0.4701** | — | — |

格式/数量：
- n_predictions: 14,627
- n_truncated: 158
- n_format_ok: 984/985 (99.9%)
- field_compliance: 83.96%

k=1 的 rel_f1/ign_f1 大幅提升（+19 pts），evi_f1 小幅提升。edcr 下降约 9 pts，说明 k=1 模型的 evidence 精度相对关系抽取精度的比例下降了（关系抽取精度从 0.588 vs k=3 可能更低，但关系召回大幅提升拉高了 F1）。

---

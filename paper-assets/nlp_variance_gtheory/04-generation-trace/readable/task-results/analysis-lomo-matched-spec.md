# analysis lomo matched spec

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lomo_matched_spec_20260521T074937_result.json`
- **Structured JSON:** [`143af6913dc93f0b17ad.json`](../../sessions/14/143af6913dc93f0b17ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过，结果已保存。

**full_4model 校验**：item_id=42.07%、model:item_id=33.64%、G_item=0.8200 — 与 dataset_a4 完全一致。

**LOMO 结果**：

| 去掉模型 | item_id% | model:item% | G_item |
|----------|----------|-------------|--------|
| (full 4-model) | 42.07 | 33.64 | 0.8200 |
| Gemma-2-9B | 40.51 | 33.67 | 0.7668 |
| Llama-3.1-8B | 39.32 | 36.92 | 0.7474 |
| Mistral-7B | 44.90 | 32.19 | 0.7929 |
| Qwen3-8B | 42.80 | 31.67 | 0.7860 |

**稳定性**：
- item_id: [39.32, 44.90], spread=5.58pp
- model:item: [31.67, 36.92], spread=5.25pp
- G_item: [0.7474, 0.7929], spread=0.0455

G_item 从 full 的 0.82 降到 3-model 子集的 0.75–0.79，主要因为 n_model 从 4 降到 3 导致 delta 增大。去掉 Llama 影响最大（G_item 最低 0.7474，model:item 最高 36.92%），去掉 Mistral 影响最小（G_item 最高 0.7929）。

---

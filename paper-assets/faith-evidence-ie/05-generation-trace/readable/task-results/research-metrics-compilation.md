# research metrics compilation

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_metrics-compilation_20260516T005928_result.json`
- **Structured JSON:** [`8ecd3d2adff75f3d0211.json`](../../sessions/8e/8ecd3d2adff75f3d0211.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已保存并注册：`art_20260516_752e0d`

**表格摘要：**

| 方法 | rel_f1 | vs SFT |
|------|--------|--------|
| CED Reranker (N=8) | 0.4864 | +8.07pp |
| RSFT-CED 3-seed mean | 0.4596±0.0128 | +5.39pp |
| GRPO bf16 step-100 | 0.4549 | +4.92pp |
| RSFT-flat-NLI 2-seed mean | 0.4531±0.0011 | +4.74pp |
| SFT baseline | 0.4057 | — |
| DPO 1ep | 0.4034 | −0.23pp |
| GRPO QLoRA | 0.2167 | −18.90pp |

缺失数据：RSFT-CED s45（训练失败）、flat-NLI s44/s45（eval 未完成），已在表中标 TBD。CED vs flat-NLI 差距仅 ~0.65pp，contrastive margin 贡献有限。

---

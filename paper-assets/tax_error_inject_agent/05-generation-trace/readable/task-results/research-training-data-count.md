# research training data count

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_training-data-count_20260516T134418_result.json`
- **Structured JSON:** [`bf0572c0026ba15211db.json`](../../sessions/bf/bf0572c0026ba15211db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 条件 | 文件 | 样本数 |
|------|------|--------|
| Vanilla | `sft_vanilla_v4.jsonl` | **4,358** |
| TaxEI | `sft_taxei_v4.jsonl` | **9,029** |
| Random | `sft_random_v4.jsonl` | **9,029** |

TaxEI 和 Random 数据量相同（9,029），均为 Vanilla（4,358）的约 2.07 倍。差值 4,671 应为注入的错误样本数。

---

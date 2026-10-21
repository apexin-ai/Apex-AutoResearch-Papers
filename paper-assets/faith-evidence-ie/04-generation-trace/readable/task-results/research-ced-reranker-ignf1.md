# research ced reranker ignf1

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ced_reranker_ignf1_20260516T033143_result.json`
- **Structured JSON:** [`4a3be4011b008bb1456c.json`](../../sessions/4a/4a3be4011b008bb1456c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

重算结果：

| Strategy | F1 | Ign-F1 |
|---|---|---|
| CED reranker | 48.64 | **47.36** |
| Oracle reranker | 62.37 | 61.25 |
| Random baseline | 45.38 | 43.97 |

原 results.json 中 ign_f1 == f1 是 bug（原始 eval 代码运行时可能 `train_facts` 未正确填充，或 `from_train_file` 当时还没实现）。现在重新计算后 CED reranker 的 **Ign-F1 = 47.36**。

F1 和 Ign-F1 差约 1.3 个点，符合 DocRED 的典型 train-dev overlap 比例（约 8.6% 的 dev facts 与 train 重叠）。

---

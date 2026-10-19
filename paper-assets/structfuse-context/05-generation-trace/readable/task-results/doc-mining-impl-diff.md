# doc mining impl diff

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_doc_mining-impl-diff_20260515T035645_result.json`
- **Structured JSON:** [`c763c07642ed8a55c3c7.json`](../../sessions/c7/c763c07642ed8a55c3c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。差异记录已追加到 memory.md，核心发现：

| 维度 | `DataFlowAwareMiner` | `build_m1_training_data.py` |
|------|---------------------|---------------------------|
| 候选初筛 | Embedding cosine top-50 | 无初筛（全部 non-positive） |
| 排除范围 | `dataflow_graph` 直接条目（窄） | `positive_files ∪ cg_connected`（宽，含 call graph） |
| 排序 | Embedding 主选 → BM25 re-rank | 纯 BM25 |

对齐建议：plan_015 应统一排除范围至 `full_connected`（含 call graph），同时保留 `DataFlowAwareMiner` 的 embedding→filter→BM25 三步法结构（dynamic mining 的核心价值在于使用当前 epoch 的 encoder embedding）。

---

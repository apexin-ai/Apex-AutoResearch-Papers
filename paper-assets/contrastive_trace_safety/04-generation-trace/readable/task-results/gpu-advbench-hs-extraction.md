# gpu advbench hs extraction

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_advbench_hs_extraction_20260519T235952_result.json`
- **Structured JSON:** [`0e68f4b6d19a273edfde.json`](../../sessions/0e/0e68f4b6d19a273edfde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 2A + 2B 完成

### Hidden States（Phase 2A）
| 指标 | 值 |
|------|-----|
| 提取 traces | **520/520** |
| 输出路径 | `artifacts/hidden_states_advbench/` |
| 格式 | `.pt`，shape `[T, 25, 4096]` fp16 |
| Steps/trace | min=2, mean=19.3, max=61 |
| 总大小 | 1957 MB |
| 耗时 | ~54s/shard（双 GPU 并行） |

### Text Embeddings（Phase 2B）
| 指标 | 值 |
|------|-----|
| 提取 traces | **520/520** |
| 输出路径 | `artifacts/text_embeddings_advbench/` |
| 格式 | `.pkl`，shape `(T, 384)` float32 |
| Steps/trace | min=2, mean=19.3, max=61 |
| 总大小 | 14.7 MB |
| 耗时 | ~2s（MiniLM 极快） |

---

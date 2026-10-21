# maintenance fix nested paths

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_maintenance_fix-nested-paths_20260520T112919_result.json`
- **Structured JSON:** [`56ab010122fe5a13400b.json`](../../sessions/56/56ab010122fe5a13400b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个目录全部修复完成，无残留嵌套。

| 目录 | 状态 | 关键文件 |
|------|------|---------|
| `sft_output_llama_3_1_8b` | FIXED | `adapter_model.safetensors` (671MB), `adapter_config.json`, checkpoints 190/570 |
| `sft_output_14b` | FIXED | `checkpoint-96/`, `checkpoint-144/` 各含 adapter (514MB) |
| `rsft_generations_14b` | FIXED | `generations.jsonl` (14976 行) |

---

# ssh fewrel qwen3 embeddings

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fewrel-qwen3-embeddings_20260515T113947_result.json`
- **Structured JSON:** [`46fc3822ee43502b9111.json`](../../sessions/46/46fc3822ee43502b9111.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 结果

| 项目 | 值 |
|------|-----|
| Relation 数量 | 80 |
| 嵌入维度 | 5120 (bfloat16) |
| SimMatrix | 80×80 |
| BCS mean | 0.8790 |
| BCS std | 0.0723 |
| BCS min | 0.4542 |
| BCS max | 0.9789 |

产出文件：
- `artifacts/fewrel_qwen3_embeddings.pt` (843KB)
- `artifacts/fewrel_qwen3_sim_matrix.pt` (30KB)

GPU 已完全释放，无进程占用，可以立即启动 FewRel formal 实验。

---

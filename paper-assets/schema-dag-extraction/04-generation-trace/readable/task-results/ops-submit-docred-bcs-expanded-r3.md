# ops submit docred bcs expanded r3

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit_docred_bcs_expanded_r3_20260519T135700_result.json`
- **Structured JSON:** [`fb5daa97c8d2eedaa0ab.json`](../../sessions/fb/fb5daa97c8d2eedaa0ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 `exp_docred_bcs_expanded` **已经完成且结果完整**：

- 110 个 batch 全部有结果（包括 40 个新 extreme batches, idx>=5）
- Registry 状态: DONE (success)，有完整 metrics
- BCS effect: count_16 = -25.04pp, count_32 = -15.65pp, interaction = -9.39pp CI[-12.91, -5.95]

脚本的 OOM 防护和断点续跑改造已完成（`max_model_len=8192`, `gpu_memory_utilization=0.85`, JSONL checkpoint），但无需重新提交——数据已经齐了。

要重跑吗？

---

# ops cleanup stale running

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup_stale_running_20260519T184848_result.json`
- **Structured JSON:** [`8d64df06b823de1ec9eb.json`](../../sessions/8d/8d64df06b823de1ec9eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个条目都已经不是 RUNNING 状态，已被清理过：

- **d112_rsft_s44_generate** → DONE/success ✓
- **d112_rsft_s44_ced_score** → DONE/success ✓  
- **seed_llama_rsft_k1_s43** → DONE/failed ⚠️

前两个状态正确。但 **seed_llama_rsft_k1_s43 标记为 failed 可能有误**：训练日志显示 EXIT_CODE=0、epoch 3.0 完成、loss=0.49，checkpoint 目录有完整的 adapter_model.safetensors (671MB)。训练本身是成功的。

是否需要将 seed_llama_rsft_k1_s43 的 conclusion 从 failed 改为 success？

---

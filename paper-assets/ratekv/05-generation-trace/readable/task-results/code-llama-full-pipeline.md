# code llama full pipeline

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_full_pipeline_20260514T013209_result.json`
- **Structured JSON:** [`9c1bbd391f017bef307b.json`](../../sessions/9c/9c1bbd391f017bef307b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

- **Dry-run**: 通过，配置正确（model path、num_kv_heads=8、256 heads）
- **Pipeline**: 已后台启动（PID 163850），模型已加载，Phase 1 profiling 进行中
- **Registry**: `llama_full_pipeline` 状态已更新为 RUNNING
- **日志**: `/root/ratekv/llama_pipeline.log`
- **预计耗时**: 60-90 min（256 heads × 3 bit-widths profiling + solver + eval）

---

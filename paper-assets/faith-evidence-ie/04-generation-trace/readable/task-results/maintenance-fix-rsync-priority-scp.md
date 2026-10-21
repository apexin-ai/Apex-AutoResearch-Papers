# maintenance fix rsync priority scp

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_maintenance_fix-rsync-priority-scp_20260520T090022_result.json`
- **Structured JSON:** [`7e743ad9aa173f3e8bf9.json`](../../sessions/7e/7e743ad9aa173f3e8bf9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Phase 1 完成：**
- Kill PID 4910（较早启动的重复 rsync）→ 成功
- 保留 PID 5150 继续后台 rsync

**Phase 2 已启动：**
- SCP PID 8061 后台运行中，正在传 meta-llama 基座模型（~15G，最大文件）
- 当前磁盘 26G
- 传输顺序：meta-llama → sft_output_llama_3_1_8b → data → freige → rsft_generations_14b → sft_output_14b → Qwen3-14B

3 分钟后自动检查进度。

---

# ops verify cuda1 cleanup

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_cuda1_cleanup_20260515T173626_result.json`
- **Structured JSON:** [`0a15063239bb09cc0ba9.json`](../../sessions/0a/0a15063239bb09cc0ba9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完毕：

- **PID 229668**：已不存在，清理干净
- **PID 230809**：正常运行中，eval inference 进程（sft_no_evidence）
- **cuda:1 显存**：16,626 MiB / 32,607 MiB（~16.2GB），相比之前 25.6GB 已恢复正常
- **cuda:1 进程**：仅 PID 230809 一个 python 进程，无残留

cuda:1 状态正常，无需额外清理。

---

# code fix offline loading

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-offline-loading_20260515T170300_result.json`
- **Structured JSON:** [`1d0028e97ee9dc0c741e.json`](../../sessions/1d/1d0028e97ee9dc0c741e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已经包含 `local_files_only=True`。两处 `from_pretrained` 调用（第80行 `AutoProcessor` 和第81行 `AutoModelForVision2Seq`）都已有该参数，无需修改。

---

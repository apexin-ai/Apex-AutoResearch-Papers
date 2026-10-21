# code rollback transformers

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rollback_transformers_20260520T235826_result.json`
- **Structured JSON:** [`267a7bbe7bec3a36fbfa.json`](../../sessions/26/267a7bbe7bec3a36fbfa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

回滚完成。

- **transformers**: 5.9.0 → 4.48.3 ✓
- **AutoModelForVision2Seq / AutoProcessor 导入**: OK ✓
- **依赖冲突**（不影响 OpenVLA，仅记录）:
  - `trl 1.1.0` 要求 transformers>=4.56.2
  - `vllm 0.18.1` 要求 transformers>=4.56.0
  - `huggingface-hub` 被连带降级 1.15.0 → 0.36.2，`tokenizers` 0.22.2 → 0.21.4

---

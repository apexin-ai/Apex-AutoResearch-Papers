# research verify untrained extract

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify_untrained_extract_20260516T235245_result.json`
- **Structured JSON:** [`26a1a5bcaabec053841e.json`](../../sessions/26/26a1a5bcaabec053841e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**文件验证通过。** 总结：

| 检查项 | 结果 |
|--------|------|
| 文件大小 | 418,562,272 bytes (~399 MB) ✓ |
| Tasks | 10 (task_0 ~ task_9) ✓ |
| Frames per task | 50 ✓ |
| Instructions per frame | 10 ✓ |
| Keys per instruction | `image_mean` (5, 4096), `last_preaction` (5, 4096) ✓ |
| 日志确认 | "Done. 5000 forward passes in 4.1 min" ✓ |

完整的 10 tasks × 50 frames × 10 instructions = 5000 forward passes，与 trained 版本结构一致。Untrained cross-instruction extraction 成功完成。

---

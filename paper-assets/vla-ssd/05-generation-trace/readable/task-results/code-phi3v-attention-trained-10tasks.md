# code phi3v attention trained 10tasks

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phi3v_attention_trained_10tasks_20260519T202827_result.json`
- **Structured JSON:** [`1c0ae15652db9225b4c6.json`](../../sessions/1c/1c0ae15652db9225b4c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果摘要：

| Layer | Text-dominant heads | Mean text attn | Mean image attn |
|-------|-------------------|----------------|-----------------|
| L0 | 3/32 | 0.225 | 0.776 |
| L1 | **32/32** | **0.735** | 0.265 |
| L2 | **32/32** | **0.785** | 0.215 |
| L3-L8 | 0-4/32 | 0.27-0.35 | 0.65-0.73 |
| L9-L24 | 3-10/32 | 0.34-0.43 | 0.57-0.66 |
| L25-L28 | 10-12/32 | 0.48-0.50 | 0.50-0.52 |
| L29 | 17/32 | 0.524 | 0.476 |
| L30 | 16/32 | 0.529 | 0.471 |
| L31 | **18/32** | **0.652** | 0.348 |

- 脚本：`/root/vla-ssd/scripts/phi3v_attention_profile_10tasks.py`
- 结果：`/root/autodl-tmp/vla-ssd/results/attention/phi3v_attention_profile_10tasks.json`
- Registry: `phi3v_attention_trained_10tasks` → DONE (success)

---

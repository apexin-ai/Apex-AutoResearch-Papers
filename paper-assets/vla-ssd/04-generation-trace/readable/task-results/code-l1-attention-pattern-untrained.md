# code l1 attention pattern untrained

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_l1_attention_pattern_untrained_20260517T005256_result.json`
- **Structured JSON:** [`592fd86785e4bf58a3df.json`](../../sessions/59/592fd86785e4bf58a3df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both files saved. Results:

**L1 Attention Summary (UNTRAINED VLA)**

| Metric | Value |
|--------|-------|
| Mean attn to IMAGE | **0.8782** ± 0.1002 |
| Mean attn to INSTRUCTION | **0.1170** ± 0.0995 |

All 32 heads are IMAGE-dominant. The untrained model's last_preaction token overwhelmingly attends to image tokens (87.8%) with only 11.7% going to instruction tokens.

**Key comparison with trained model (if available):** The untrained model shows the last_preaction token attending almost entirely to image patches, not instruction tokens. If the trained model shows significant instruction attention, that proves the routing is **learned** (not architectural). If the trained model shows a similar image-dominant pattern, it would support architectural routing.

Output saved:
- PDF: `/root/autodl-tmp/vla-ssd/results/attention/l1_attention_untrained.pdf`
- JSON: `/root/autodl-tmp/vla-ssd/results/attention/l1_attention_untrained_summary.json`

---

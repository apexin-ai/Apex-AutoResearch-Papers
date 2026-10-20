# code l1 attention pattern trained

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_l1_attention_pattern_trained_20260517T005245_result.json`
- **Structured JSON:** [`ddf22af23773d020c51b.json`](../../sessions/dd/ddf22af23773d020c51b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Execution complete. Results:

## Summary Statistics

| Region | Mean Attention (across all heads & tasks) |
|--------|------------------------------------------|
| BOS | 0.2109 |
| Image (256 tokens) | 0.2090 |
| Text/Instruction (~22 tokens) | **0.5801** |

**Key findings:**

- **25-26 out of 32 heads** are "instruction-attending" (>50% attention to text tokens) at Layer 1
- The last_preaction token allocates **~58% of its attention to instruction/text tokens** despite those being only ~8% of the sequence length (22 out of 278 tokens)
- This is extremely disproportionate: instruction tokens get ~29x more attention per token than image tokens (0.58/22 = 0.026 per token vs 0.21/256 = 0.0008 per token)
- The pattern is highly consistent across all 5 tasks (std < 0.01)
- Only heads 3, 6, 9, 13, 21, 24 show image-preferring patterns

**Outputs saved:**
- PDF: `/root/autodl-tmp/vla-ssd/results/attention/l1_attention_trained.pdf`
- JSON: `/root/autodl-tmp/vla-ssd/results/attention/l1_attention_trained_summary.json`

This provides strong mechanistic evidence: at Layer 1, the last_preaction token is already overwhelmingly attending to instruction tokens, explaining why instruction encoding is essentially complete by this early layer.

---

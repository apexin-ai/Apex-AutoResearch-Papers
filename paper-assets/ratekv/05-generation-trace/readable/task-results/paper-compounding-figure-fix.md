# paper compounding figure fix

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compounding_figure_fix_20260515T195440_result.json`
- **Structured JSON:** [`df437e865073dcf85872.json`](../../sessions/df/df437e865073dcf85872.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both changes complete:

1. **Qwen data**: expanded from 4 to 9 k-values (0, 2, 4, 8, 16, 32, 64, 128, 256), matching Llama/Mistral density. The k=128 and k=256 values (98.75 / 98.7523) reflect the saturation from 112 KV heads.

2. **Caption**: added saturation explanation — "Qwen saturates at $k{\approx}96$ due to its 112 KV heads (maximum ${\sim}96$ eligible for 2-bit assignment)."

Figure PDF regenerated and paper recompiled (15 pages, no errors).

---

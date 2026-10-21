# code gen attention figure

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gen_attention_figure_20260517T020717_result.json`
- **Structured JSON:** [`aeea7f0c97fc325c9134.json`](../../sessions/ae/aeea7f0c97fc325c9134.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure generated. 25/32 trained heads instruction-dominant, 0/32 untrained, matching the expected split.

Output:
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/attention/fig8_attention_final.pdf` (21 KB)
- **PNG**: `fig8_attention_final.png` (100 KB)

Key details:
- Heads sorted by trained instruction fraction (descending), same order in both panels
- Trained panel shows clear transition across the 0.5 dashed line at position 25
- Untrained panel: all 32 heads image-dominant (blue bars uniformly low)
- The "instruction fraction" uses raw attention-to-text as a proportion of total attention (including BOS sink), which gives the 25/32 count consistent with the original analysis

---

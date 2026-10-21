# ops check 8b rsft eval result

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_8b_rsft_eval_result_20260517T145810_result.json`
- **Structured JSON:** [`4dfe7a74b10e58ed5216.json`](../../sessions/4d/4dfe7a74b10e58ed5216.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated, cron deleted. Here's the complete **Scaling Study** summary:

## Scaling Study: SFT → CED-RSFT (Ign-F1)

| Model | SFT | RSFT | Δ |
|-------|-----|------|---|
| Qwen3-1.7B | 0.4945 | 0.5219 | **+2.7pp** |
| Qwen3-4B | 0.4049 | 0.4655 | **+6.1pp** |
| LLaMA-3.1-8B | 0.5514 | 0.5674 | **+1.6pp** |
| Qwen3-8B | 0.5262 | 0.5606 | **+3.4pp** |

**Qwen3-8B Ign-F1: 0.5079 → 0.5433 (+3.5pp)**

Key observations:
- RSFT consistently improves over SFT across all 4 models (100% win rate)
- Largest relative gain at 4B scale (+6.1pp), smallest at LLaMA-8B (+1.6pp)
- LLaMA-3.1-8B RSFT (0.5674) achieves highest absolute F1, not Qwen3-8B (0.5606) — hypothesis partially disconfirmed on the "highest absolute" claim
- Qwen3-8B shows strong evidence quality: Evi-F1=0.8052, EDCR=0.6377

---

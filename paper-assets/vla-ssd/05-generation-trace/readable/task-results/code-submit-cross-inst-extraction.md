# code submit cross inst extraction

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_submit_cross_inst_extraction_20260516T233922_result.json`
- **Structured JSON:** [`3494ea50606adc38f287.json`](../../sessions/34/3494ea50606adc38f287.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Process alive and CPU-busy (112% CPU, 1:27 elapsed) — it's building the random LLM in RAM. It'll hit GPU shortly.

**Summary:**

Both cross-instruction extraction jobs submitted on westd-19183:

| Condition | GPU | PID | Output |
|-----------|-----|--------|--------|
| trained | cuda:0 | 751661 | `trained_cross_inst.h5` |
| untrained | cuda:1 | 751972 | `untrained_cross_inst.h5` |

- Trained job already processing at ~20 fwd/s (Task 1 in progress)
- Untrained job reinitializing 7B LLM backbone on CPU, will start GPU inference momentarily
- Both output to `/root/autodl-tmp/vla-ssd/results/cross_instruction/`
- Estimated ~26 min each (running in parallel)
- Existing probe job (PID 749462) undisturbed

---

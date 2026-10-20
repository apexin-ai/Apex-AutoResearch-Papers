# code sft alpha4 eval collect

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sft-alpha4-eval-collect_20260515T134621_result.json`
- **Structured JSON:** [`da7da790762ea8de7d17.json`](../../sessions/da/da7da790762ea8de7d17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

**`sft_alpha4_0_westd_retry` → DONE (success)**

| Metric | Value |
|---|---|
| Post-prune accuracy | 40% |
| **Post-SFT accuracy** | **62%** (62/100, stderr=0.049) |
| SFT recovery gain | +22pp |
| Train loss (final) | 0.7393 |
| EOS rate | 98% |
| Avg response length | 238.56 |

**vs. α=1.0 RASP post-SFT (57%)**: α=4.0 is +5pp higher, confirming that higher CKA weight amplifies SFT recovery from pruned models.

---

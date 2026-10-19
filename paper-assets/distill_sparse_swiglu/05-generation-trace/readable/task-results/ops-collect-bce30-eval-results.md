# ops collect bce30 eval results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-bce30-eval-results_20260518T180525_result.json`
- **Structured JSON:** [`54e03d0bca9c41e1fdcb.json`](../../sessions/54/54e03d0bca9c41e1fdcb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

**bce_30pct_s42_eval — DONE (negative)**

| Metric | BCE 30% | KL 30% uniform | TEAL 30% | Dense |
|--------|---------|----------------|----------|-------|
| PPL | 11.24 | 8.82 | 10.97 | 6.12 |
| ARC (norm) | 41.2% | 40.8% | 42.3% | 58.3% |
| WinoGrande | 66.0% | 68.6% | 66.1% | 78.1% |
| MMLU | 36.3% | 40.6% | 38.6% | 65.3% |
| GSM8K | 6.0% | 7.4% | 7.9% | 48.8% |

**Downstream collapse?** No catastrophic collapse (contrast with KL 50% where GSM8K drops to ~1-2%). But BCE 30% is consistently worse than TEAL 30% baseline on PPL and most downstream tasks, confirming BCE-trained masks are genuinely inferior even when allocation is forced externally via TEAL top-k. The PPL gap (11.24 vs 8.82) propagates proportionally to downstream.

---

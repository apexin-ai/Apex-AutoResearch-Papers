# code run dense l1 l8 extraction

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_run_dense_l1_l8_extraction_20260517T000956_result.json`
- **Structured JSON:** [`c10d58f17f2c0e89a0ef.json`](../../sessions/c1/c10d58f17f2c0e89a0ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Results:

```
Layer  Trained    Untrained  Delta
------------------------------------
L0     0.1000     0.1000     +0.0000
L1     0.9960     1.0000     -0.0040
L2     1.0000     1.0000     +0.0000
L3     1.0000     1.0000     +0.0000
L4     1.0000     0.9980     +0.0020
L5     1.0000     0.9990     +0.0010
L6     1.0000     0.9960     +0.0040
L7     1.0000     0.9960     +0.0040
L8     1.0000     0.9860     +0.0140
Chance 0.1000
```

Key finding: instruction encoding jumps from chance (10%) at L0 to near-perfect (99.6-100%) at L1 for **both** trained and untrained models. The transition is essentially a single-layer step function between L0 and L1. Training provides no meaningful advantage - the untrained model already achieves perfect instruction classification by L1, with only a slight degradation in deeper layers (L8: 98.6% vs 100%).

Results saved to `/root/autodl-tmp/vla-ssd/results/cross_instruction_dense/classification_results.json`.

---

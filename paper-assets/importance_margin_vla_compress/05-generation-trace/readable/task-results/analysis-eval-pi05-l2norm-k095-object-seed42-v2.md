# analysis eval pi05 l2norm k095 object seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_l2norm_k095_object_seed42_v2_20260522T013952_result.json`
- **Structured JSON:** [`a1297a78f40479987924.json`](../../sessions/a1/a1297a78f40479987924.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

| Field | Value |
|-------|-------|
| **SR** | **98.2%** (491/500) |
| **Status** | DONE |
| **Conclusion** | success |
| **k=0.95 vs k=0.9** | 98.2% = 98.2% (monotonicity holds — non-decreasing) |
| **vs baseline** | 98.2% >> 68.0% |
| **Tokens kept** | 243/256 per image (95%) |
| **Wall time** | 63.2 min |

L2norm monotonicity confirmed on libero_object: keeping more tokens (k=0.95) yields equal performance to keeping fewer (k=0.9), both at 98.2%. The pruning is safe at both thresholds.

---

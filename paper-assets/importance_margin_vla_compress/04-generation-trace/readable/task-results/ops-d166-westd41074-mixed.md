# ops d166 westd41074 mixed

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d166_westd41074_mixed_20260522T131243_result.json`
- **Structured JSON:** [`ad8b2d35a929187cc64c.json`](../../sessions/ad/ad8b2d35a929187cc64c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SmolVLA Spatial baseline progress:
| Task | SR |
|------|------|
| 0 | 60.0% |
| 1 | 45.0% |
| 2 | 45.0% |
| 3 | 60.0% |
| 4 | 70.0% |
| 5-9 | in progress |

Average so far: 56.0%. Experiments running stably on both GPUs, will continue to completion. X-VLA session has 3 sequential runs (baseline → k=0.95 → k=0.9).

**OpenVLA Long remains BLOCKED** — no libero_10 fine-tuned model exists on either server. Only `openvla-libero-object` is available. This needs a decision: either skip OpenVLA Long, or use the libero_object model on libero_10 (cross-suite eval, likely poor results).

---

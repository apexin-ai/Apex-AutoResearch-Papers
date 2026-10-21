# deploy westd38929 pi05 cross suite

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd38929-pi05-cross-suite_20260521T184117_result.json`
- **Structured JSON:** [`d9d50a7eafdc37e1186b.json`](../../sessions/d9/d9d50a7eafdc37e1186b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 experiments running and producing results on Task 0 ("pick up the black bowl between the plate"):

| GPU | Experiment | Progress | Task 0 SR so far |
|-----|-----------|----------|------------------|
| 0 | baseline (none) | ep 40/50 | **100%** (40/40) |
| 1 | l2norm k=0.5 | ep 20/50 | **80%** (16/20) |
| 2 | random k=0.5 | ep 30/50 | **90%** (27/30) |
| 3 | l2norm k=0.3 | ep 10/50 | **70%** (7/10) |

Early Task 0 numbers are already interesting — baseline at 100%, and at k=0.5 random (90%) > l2norm (80%), consistent with the Object suite pattern where low-CV linear projection makes L2norm no better than random. L2norm k=0.3 at 70% shows expected degradation at higher pruning.

All GPUs actively computing (28-45% util, 10-10.6 GB VRAM). Experiments are healthy and progressing normally.

---

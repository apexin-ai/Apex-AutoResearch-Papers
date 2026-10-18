# analyze pi05 attn k095 strict w41 and deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_pi05_attn_k095_strict_w41_and_deploy_20260527T113744_result.json`
- **Structured JSON:** [`bf93c1fa800053b6f915.json`](../../sessions/bf/bf93c1fa800053b6f915.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`submit_training_job` is not available as a tool. Here's the situation:

**eval_pi05_attn_k095_long_seed42_strict_w41 — still running on cuda:2, ~60 min remaining (T4/10 at ep=30)**

Registry's `reproduce.finished_at=10:40 UTC` is from a previous run; the experiment was relaunched at 10:41 UTC in manual tmux `pi05_attn_k095`.

Partial results so far:
| Task | SR |
|------|-----|
| T0 | 94.0% |
| T1 | 100.0% |
| T2 | 74.0% |
| T3 | 98.0% |
| T4 | ~83% (in progress, ep=30/50) |

**All 4 GPUs on westd-41074 are occupied:**

| GPU | Experiment | Progress | ETA |
|-----|-----------|----------|------|
| 0 | π0.5 Random k=0.9 Long strict v2 | T7 ep=40 | ~30 min |
| 1 | π0.5 Random k=0.5 Long strict w41 v2 | T8 ep=40 | ~20 min |
| 2 | π0.5 Attn k=0.95 Long strict w41 | T4 ep=30 | ~60 min |
| 3 | π0.5 L2norm k=0.85 Long | T4 ep=40 | ~55 min |

**Cannot deploy L2norm k=0.7 now.** GPU 1 will free up soonest (~20 min). Options:
1. Wait for GPU 1 and deploy L2norm k=0.7 there (soonest)
2. Wait for cuda:2 and deploy there (~60 min)
3. I can set up a one-liner that waits for GPU 1's process to exit then auto-launches

Want me to deploy on whichever GPU frees up first, or wait for cuda:2 specifically?

---

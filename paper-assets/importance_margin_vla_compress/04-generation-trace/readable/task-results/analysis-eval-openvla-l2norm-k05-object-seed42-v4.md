# analysis eval openvla l2norm k05 object seed42 v4

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_openvla_l2norm_k05_object_seed42_v4_20260525T120311_result.json`
- **Structured JSON:** [`a2d6d7131e85ef2cd3a0.json`](../../sessions/a2/a2d6d7131e85ef2cd3a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

**OpenVLA L2norm k=0.5 Object (seed42)** → **39.2%** (196/500), **DONE/success**

| k | L2norm | Random | Attn |
|---|--------|--------|------|
| 1.0 (baseline) | 74.0% | 74.0% | 74.0% |
| 0.9 | 70.6% (-3.4pp) | 62.8% (-11.2pp) | 61.4% (-12.6pp) |
| 0.5 | **39.2% (-34.8pp)** | TBD | TBD |

At k=0.5 (keeping 128/256 tokens), L2norm drops catastrophically from 74.0% to 39.2%. The degradation curve is highly nonlinear: k=0.9 only costs 3.4pp, but k=0.5 costs 34.8pp. This supports the crossover hypothesis — at aggressive pruning, L2norm's advantage over random likely vanishes for OpenVLA's MLP projector (CV=0.215). Need the random k=0.5 result to confirm the convergence.

---

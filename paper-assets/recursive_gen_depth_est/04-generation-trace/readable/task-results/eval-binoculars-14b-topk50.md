# eval binoculars 14b topk50

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_binoculars_14b_topk50_20260520T053504_result.json`
- **Structured JSON:** [`97627a7f22aa6f95144e.json`](../../sessions/97/97627a7f22aa6f95144e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry already has the complete `binoculars_14b_topk50` entry with all metrics, status=DONE, conclusion=success. This was populated earlier in the session.

All 4 steps complete:

| Step | Status | Result |
|------|--------|--------|
| 1. Binoculars extraction | Done | RF_multi = **37.68%** (11 features) |
| 2. Merged ablation | Done | merged 30-feat = **51.49%**, stat_only = 48.84%, bino_only = 37.74% |
| 3. Baseline alignment (方案 A) | Done | Δ = **+3.56pp** (51.49% − 47.93% main pipeline) |
| 4. Artifact + registry | Done | `artifacts/binoculars_14b_topk50_results.md` registered, registry updated |

Compared to temp09: merged lift is comparable (+3.56pp vs +3.7pp), but Binoculars RF_multi drops from 42.52% to 37.68% under top-k truncation.

---

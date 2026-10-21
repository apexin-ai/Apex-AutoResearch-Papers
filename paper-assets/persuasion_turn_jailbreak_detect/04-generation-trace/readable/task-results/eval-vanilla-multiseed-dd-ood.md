# eval vanilla multiseed dd ood

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_vanilla-multiseed-dd-ood_20260518T110133_result.json`
- **Structured JSON:** [`ba1e76fca07bcbed9ab6.json`](../../sessions/ba/ba1e76fca07bcbed9ab6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Summary:

## Part A: Vanilla DeBERTa DD OOD (3 seeds)

| K | Seed42 | Seed123 | Seed456 | Mean±Std |
|---|--------|---------|---------|----------|
| k1 | 0.575 | 0.658 | 0.652 | **0.628±0.038** |
| k2 | 0.438 | 0.530 | 0.469 | **0.479±0.038** |
| k3 | 0.359 | 0.424 | 0.383 | **0.389±0.027** |
| k5 | 0.311 | 0.383 | 0.360 | **0.351±0.030** |
| full | 0.285 | 0.305 | 0.348 | **0.312±0.026** |

Seed 42 was the worst of the three. Multi-seed mean is slightly higher than the single-seed estimate.

## Part B: Centered CKA Fix

**Last-layer CLS (centered vs uncentered):**

| Pair | Split | Centered | Uncentered |
|------|-------|----------|------------|
| vanilla vs MLM | IID | **0.442** | 1.000 |
| vanilla vs 9class | IID | **0.393** | 0.421 |
| MLM vs 9class | IID | **0.586** | 0.422 |
| vanilla vs MLM | DD OOD | **0.797** | 1.000 |
| vanilla vs 9class | DD OOD | **0.649** | 0.523 |
| MLM vs 9class | DD OOD | **0.773** | 0.523 |

The vanilla\_vs\_MLM CKA=1.0 was indeed a centering bug. After centering: 0.44 (IID), 0.80 (DD OOD). MLM does change the representation space meaningfully. Layer-wise CKA shows divergence starts around layer 6 and accelerates in layers 11-12.

All results saved to:
- Server: `results/vanilla_multiseed_dd_ood.json`, `results/centered_cka.json`, `results/vanilla_multiseed_dd_ood_combined.json`
- Local artifact: `artifacts/vanilla_multiseed_dd_ood.json` (registered as `art_20260518_c8bb60`)

---

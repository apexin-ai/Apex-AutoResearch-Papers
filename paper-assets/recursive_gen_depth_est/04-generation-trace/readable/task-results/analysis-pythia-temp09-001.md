# analysis pythia temp09 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pythia_temp09_001_20260514T163125_result.json`
- **Structured JSON:** [`9434d9ee5a26c2dad3ff.json`](../../sessions/94/9434d9ee5a26c2dad3ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE/success. Here's the complete comparison:

---

## `pythia_temp09_001` — **SUCCESS**

### 4-class (d0-d3)
| Metric | Baseline (nucleus p=0.95) | Temp09 (τ=0.9) | Δ |
|--------|--------------------------|-----------------|---|
| RF acc | 78.15% [76.9, 79.4] | 76.25% [74.9, 77.5] | **-1.9pp** |
| LR acc | 74.92% | 74.05% | -0.9pp |
| AUC 0v1 | 0.9975 | 0.9968 | -0.0007 |
| AUC 1v2 | 0.8607 | 0.8327 | **-0.028** |
| AUC 2v3 | 0.8005 | 0.7928 | -0.008 |

### 3-class (d1-d3)
| Metric | Baseline | Temp09 |
|--------|----------|--------|
| Full acc | 70.8% | 69.83% [68.2, 71.5] |
| Filtered acc | — | 72.52% [70.6, 74.3] |
| Filtered d2v3 AUC | — | 0.8295 |

### Key findings
1. **Depth signal is decoding-robust**: Only 1.9pp accuracy drop despite switching from nucleus to temperature-only sampling. Both pass thresholds by wide margins (76.25% >> 40%, d1v2 AUC 0.8327 >> 0.6).
2. **Feature importance ranking identical**: var_surprisal > p90_ppl > mean_ppl > mean_surprisal > p75_ppl, with near-identical weights across strategies.
3. **Code contamination 2-3pp higher** in temp09 — temperature-only preserves more of the distribution tail. Filtered 3-class acc (72.52%) recovers ~2.7pp over unfiltered.
4. **d2 confusion persists**: d2 recall 0.554 (3-class) is the systematic weak point in both conditions — an inherent property of depth-2 text, not a decoding artifact.

---

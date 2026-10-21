# analysis exp 029d

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_029d_20260521T033426_result.json`
- **Structured JSON:** [`385537115aeebed5cdc3.json`](../../sessions/38/385537115aeebed5cdc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE. Here's the complete analysis:

---

## exp_029d_tcn_walker_s3_sigma02 — **NEGATIVE** (CIVO failure)

### Key metrics
- **Final step**: 215K (224K env steps), EXIT_CODE=0
- **Final eval_return**: 104.5 (~11% of baseline avg ~788)
- **Peak eval_return**: 349.6 @ 95K (~39% of baseline)
- **Peak ve_ratio**: **3.0× @ 105K** (well above 1.5× CIVO threshold)
- CIVO blowup at 105K caused performance collapse from 349.6 → 71.8; never recovered

### NVE trajectory (key points)
| Step | ve_ratio | eval_return |
|------|----------|-------------|
| 85K  | 0.9      | 259.5       |
| 95K  | 0.7      | **349.6** (peak) |
| **105K** | **3.0** | **71.8** (collapse) |
| 115K | 2.5      | 69.8        |
| 125K | 2.4      | 61.5        |
| 135K | 0.9      | 141.8 (partial recovery) |
| 215K | 0.4      | 104.5 (final) |

### Conclusion rationale
CIVO blowup (ve_ratio=3.0) at 105K caused catastrophic performance collapse. Pattern matches s2 failure. Despite ve_ratio eventually recovering to <1.0, the agent never regained its pre-blowup performance level.

---

## TCN Walker σ=0.2 — Four-seed summary

| Seed | eval_return | % baseline | NVE peak | CIVO? | Conclusion |
|------|-------------|-----------|----------|-------|------------|
| **s0** | 821 | 91% | 0.908 | No | **success** |
| **s1** | 401 | 45% | — | — | **mixed** |
| **s2** | 32 | 3.5% | 2.77 | Yes | **negative** |
| **s3** | 104.5 | 11% | 3.0 | Yes | **negative** |

**Overall**: 2/4 seeds failed with CIVO blowup (s2, s3). Only 1/4 clearly succeeded (s0). TCN σ=0.2 exhibits high variance and is not reliably protective against CIVO on Walker Walk.

---

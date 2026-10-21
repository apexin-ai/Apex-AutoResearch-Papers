# code r19 semisynthetic gradient

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r19_semisynthetic_gradient_20260522T184822_result.json`
- **Structured JSON:** [`0e8edd0d4de14fcbd4ee.json`](../../sessions/0e/0e8edd0d4de14fcbd4ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three output files produced. Summary:

**R19 Exp 4 — Results**

| Scheme | ρ(diff, Δδ) injected | % focal-favoring (inj C) | C% (all) |
|--------|---------------------|--------------------------|----------|
| **A** (capability-like) | **+0.771 ± 0.029** | 85.2% | 31.9% |
| **B** (contamination-like) | **−0.517 ± 0.107** | 85.7% | 32.1% |
| **C** (mixed) | **+0.394 ± 0.053** | 83.8% | 32.0% |
| Baseline | — | 43.9% | 31.3% |

The key Δδ metric (delta change from baseline) cleanly separates all three injection patterns with Δρ_AB ≈ 1.29 and zero overlap across seeds.

Unexpected but informative: Scheme B gives ρ ≈ −0.5 rather than ≈ 0 due to ceiling effect — hard items have more 0→1 flippable responses, so uniform injection probability produces difficulty-dependent DIF. This means the capability vs. contamination distinction is about the **sign** of the difficulty-DIF gradient (+0.77 vs −0.52), not "correlated vs uncorrelated."

---

# paper cheetah nve baseline update

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_cheetah_nve_baseline_update_20260525T163049_result.json`
- **Structured JSON:** [`c1b53172af3052b8f5ff.json`](../../sessions/c1/c1b53172af3052b8f5ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All changes verified. Here's the summary:

### Before/After

**1. appendix.tex — experiment table (line 70-71)**
- Before: only exp_077 row
- After: added `083 & Cheetah baseline (s1) & --- & --- & 15 & 444.0 @105K & 1.00$\times$ & Healthy` row after exp_077

**2. appendix.tex — post-CIVO footnote (line 752)**
- Before: `(26.7\% of baseline exp\_077, 448.1)`
- After: `(26.8\% of 2-seed baseline mean, 446.1)`

**3. appendix.tex — normalization conventions (line 301)**
- Before: `Cheetah NVE is normalized against a 5-seed mean baseline (seeds~0--4, each run to ~210K steps). The differing seed counts reflect available baseline data;`
- After: `Cheetah NVE is normalized against a 2-seed mean baseline (exp\_077 seed~0, eval 448.1; exp\_083 seed~1, eval 444.0; mean 446.1 at 105K).`

**4. results.tex — Table 1 footnote (line 49)**
- Before: `Cheetah ${\sim}409$ (5-seed mean at 105K)`
- After: `Cheetah 446.1 (2-seed mean at 105K)`

Remaining 448.1 in paper: only in exp_077's individual result row (correct — that's its actual eval) and inside the normalization conventions paragraph (listing the two seed evals). Cheetah NVE normalization is now consistently described as 2-seed mean = 446.1 throughout.

---

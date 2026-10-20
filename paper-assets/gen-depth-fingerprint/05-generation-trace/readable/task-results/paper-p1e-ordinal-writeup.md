# paper p1e ordinal writeup

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_p1e-ordinal-writeup_20260515T235754_result.json`
- **Structured JSON:** [`9882cf5e92ae074e40dc.json`](../../sessions/98/9882cf5e92ae074e40dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits verified. Summary:

**Task 1 — P1-E ordinal results written into paper:**
- **results.tex**: Already had the "Ordinal regression comparison" paragraph (CORAL 0.771, Frank-Hall 0.793, XGBoost 0.789, CIs overlap). No edit needed.
- **discussion.tex** (both copies): Replaced the vague "finer-grained distinctions may be achievable" sentence with a concrete **Granularity ceiling** paragraph — 5-class F1 drops from 0.789→0.507, gen-2/gen-3 inseparable (F1 0.276/0.261), alternative classifiers (RF/LR/Frank-Hall) all comparable, 3-class is the practical ceiling.
- **appendix_finer_depth.tex** (both copies): Added **Classifier comparison** paragraph with HGBT (0.503, CI [0.497, 0.508]), RF (0.477), LR (0.447), Frank-Hall (0.451) confirming feature-level bottleneck.

**Task 2 — related_work CI width fix:**
Already resolved in working copy. Old text ("CI spanning 0.41--0.82 in macro-F1") was previously changed to ("binary F1 from 0.52 to 0.71 across individual baselines"), matching the baselines table (Binoculars 0.524 – Avg-LogProb 0.712). No further edit needed.

---

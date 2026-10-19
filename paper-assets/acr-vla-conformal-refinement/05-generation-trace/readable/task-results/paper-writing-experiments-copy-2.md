# paper writing experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_20260518T095825_result.json`
- **Structured JSON:** [`c8fa3e1f1d8dc3f16da5.json`](../../sessions/c8/c8fa3e1f1d8dc3f16da5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

34 exp_id annotations covering all 7 relevant evidence sections (§2A magnitude, §2B K-value, §2C baselines, §2D decomposition, §2E statistics, §2G OpenVLA, §2H perdof collapse).

Experiments section written to `docs/paper/experiments.tex` (217 lines). Structure:

1. **Setup** (lines 13--46): benchmark, VLA, 4 baselines, 3 CRM variants, statistical protocol
2. **Component Decomposition** (lines 49--103): Table 1 with 7 methods; selection ~1pp vs correction ~5pp; Fisher p=0.0074, Cohen's d=1.21; honest negatives for perdof/scalar
3. **Conditioning-Magnitude Interaction** (lines 107--160): Table 2 (6 epsilon values x 2 variants); obs\_only robust 13.5--17.5%, perdof collapses 14.0->0.0%
4. **K-Value Curve** (lines 164--190): monotonic K=1(10.3%)→K=5(14.0%*)→K=10(17.5%); K=5 single-seed noted
5. **Applicability Boundary** (lines 194--217): OpenVLA diversity failure (8/10 identical, variance <1e-30)

---

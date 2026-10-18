# ops register pilot

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_register_pilot_20260520T233206_result.json`
- **Structured JSON:** [`dab3382e84314526614c.json`](../../sessions/da/dab3382e84314526614c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Here's the verdict:

---

## Register Axis Pilot — Results (20 samples)

### Judgment Criteria

| Criterion | Threshold | Result | Status |
|-----------|-----------|--------|--------|
| CF pass rate | ≥80% | 4/20 (20%) | **FAIL** |
| Register-Formality agreement | ≤95% | 10/20 (50%) | **PASS** |

**Overall: FAIL** (pass rate criterion not met)

### Root Cause Analysis

BERTScore is the sole bottleneck, not NLI:

| Metric | CF pass rate |
|--------|-------------|
| NLI ≥ 0.90 alone | **19/20 (95%)** |
| BERTScore ≥ 0.92 alone | 4/20 (20%) |
| Both (current) | 4/20 (20%) |

Register rewrites change vocabulary and syntax substantially (academic jargon ↔ casual phrasing), which BERTScore (token-level similarity) penalizes heavily. Mean BERTScore is 0.8458 vs the 0.92 threshold. Meanwhile NLI confirms content is semantically preserved in 19/20 cases.

### Threshold Sweep (CF)

| BERTScore threshold | Pass rate (with NLI≥0.90) |
|---|---|
| ≥0.80 | 15/20 (75%) |
| ≥0.84 | 12/20 (60%) |
| ≥0.88 | 8/20 (40%) |
| ≥0.92 (current) | 4/20 (20%) |

Even at BS≥0.80 the pass rate only reaches 75%.

### Key Insight

Register is structurally similar to **verbosity** — it inherently changes surface form while preserving meaning. The pipeline already handles verbosity with NLI-only verification (no BERTScore gate). Register should use the same strategy.

With NLI-only at ≥0.90: **19/20 (95%) pass rate** → would meet the ≥80% criterion.

### Independence

Register-Formality agreement is 50% — the two axes are clearly orthogonal. Register captures vocabulary/syntax choices (academic jargon, passive voice) while formality captures social distance/politeness. This confirms register is a distinct, non-redundant axis.

### Recommendation

Register is **viable as a third axis** but requires switching `content_verification.py` to use NLI-only verification for `--axis register` (same as verbosity). The one-line fix: add `"register"` alongside `"verbosity"` in the axis check at lines 173-178.

---

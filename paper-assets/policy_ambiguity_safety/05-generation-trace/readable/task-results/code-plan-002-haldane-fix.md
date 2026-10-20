# code plan 002 haldane fix

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_002_haldane_fix_20260520T152444_result.json`
- **Structured JSON:** [`b50f9eeca7340894ebf0.json`](../../sessions/b5/b50f9eeca7340894ebf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results:

| Metric | Before | After |
|--------|--------|-------|
| MH OR | 443.0 | 391.9 |
| Non-stratified OR | 44.8 | 44.8 (unchanged) |

MH OR dropped from 443 to 392, but it's still far above the expected 30-80 range. The reason: 3 strata (authorization_scope, conditional_precedence, scopal) have c=0, and even with Haldane +0.5 correction, their denominator contribution (c*a/n) remains tiny. For example, conditional_precedence has both a=0 and c=0, so its corrected denominator contribution is only 0.5*0.5/102 = 0.00245, while numerator is 35.5*65.5/102 = 22.78.

The Haldane correction is applied correctly and the MH OR is now finite/calculable without division-by-zero risk. The high value reflects the genuine effect: in half the strata, no clause was flagged as violating *only* in the unambiguous condition (c=0), making the stratified OR inherently extreme. The non-stratified OR of 44.8 remains the primary measure as noted in the output.

All 9 analysis files regenerated without errors.

---

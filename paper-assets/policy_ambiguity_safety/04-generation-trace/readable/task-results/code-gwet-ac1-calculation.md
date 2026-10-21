# code gwet ac1 calculation

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gwet_ac1_calculation_20260520T175611_result.json`
- **Structured JSON:** [`4cb433031ba8e4e2048c.json`](../../sessions/4c/4cb433031ba8e4e2048c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**AC1 = 0.782 (95% CI: [0.670, 0.891])** — target met.

Key findings:
- **AC1 0.782 vs κ 0.594**: the 0.189 gap confirms prevalence paradox. `inappropriate_action` dominates at π=0.67, inflating κ's chance agreement estimate and artificially depressing κ.
- AC1's P_e = 0.081 (low), vs κ's implicitly higher P_e — AC1 correctly recognizes that with such skewed marginals, chance agreement should be low, not high.
- Interpretation upgrades from "moderate" (κ) to "substantial" (AC1).
- Per-type AC1 couldn't be computed — the input only has aggregate n/agreement per ambiguity type, not the full category×category sub-matrices. Percent agreement is reported instead.

Results saved to `artifacts/plan_005/gwet_ac1_results.json`.

---

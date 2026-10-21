# code exp 027c cf oracle mf2dgp

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-027c-cf-oracle-mf2dgp_20260522T142157_result.json`
- **Structured JSON:** [`4173926c920d44b46673.json`](../../sessions/41/4173926c920d44b46673.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done in 7.2 min. Results:

```
=== exp-027c: MF2 DGP (τ(0)=0.10, τ(1)=0.40) ===

Method                       | Coverage |  |Bias| |    RMSE | Mean SE
Oracle (true Z)              |   0.960  |  0.077  |  0.091  |  0.090
EC-HTE true CM               |   0.913  |  0.103  |  0.112  |  0.114
EC-HTE estimated CM (HB)     |   0.923  |  0.100  |  0.111  |  0.119
Global true CM               |   0.950  |  0.107  |  0.114  |  0.107
Global estimated CM          |   0.943  |  0.105  |  0.114  |  0.109
Naive                        |   0.773  |  0.120  |  0.125  |  0.087
```

**Diagnostics:**
- Oracle: 027b=94.0% → 027c=96.0% (both well-calibrated)
- EC-HTE estimated CM: 027b=92.5% → 027c=92.25% (nearly identical)
- MF2 original plugin coverage (aggregate): 83%

**Key finding:** The DGP difference (τ values, Y-generation, covariates) is NOT the source of the 83% vs 92.5% gap. Per-subgroup coverage is 92.25% in both experiments. The 83% in MF2 comes from subgroup 0 (π=0.05, low misclass) having 83% coverage while subgroup 1 (π=0.25) has 99% — the MF2 aggregate across subgroups mixes these. The low-misclass subgroup gets insufficient SE amplification from M⁻¹, while the high-misclass subgroup gets over-amplified SE.

---

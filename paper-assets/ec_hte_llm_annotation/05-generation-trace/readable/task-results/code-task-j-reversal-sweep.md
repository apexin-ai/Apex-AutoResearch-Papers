# code task j reversal sweep

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_task-j-reversal-sweep_20260523T154009_result.json`
- **Structured JSON:** [`90fd61d7632290efebd4.json`](../../sessions/90/90fd61d7632290efebd4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Output is complete. Here's a summary:

**Key findings:**

| τ(0) | Global reversal % | Naive reversal % |
|------|-------------------|------------------|
| 0.01 | 31.0% | 0% |
| 0.02 | 21.6% | 0% |
| 0.03 | 14.9% | 0% |
| 0.05 | 6.1% | 0% |
| 0.07 | 1.6% | 0% |
| ≥0.10 | 0% | 0% |

**Critical numbers:**
- No single τ(0) threshold produces >50% reversal across *all* configs, but **high δ_misclass** configs reach ~43% reversal at τ(0)=0.01
- **τ(0)=0.03**: 14.9% global reversal rate
- **Most dangerous combo**: τ(0)=0.01, δ_misclass=0.19 → 42.9% reversal
- Naive correction **never** causes sign reversal (bias is always same sign as true CATE for z=0)
- Reversals only occur for **subgroup B** (lower misclass rate) under global correction, where bias_global is negative

**Outputs saved:**
- `artifacts/policy_reversal_zone.pdf` + `.png` (2-panel figure)
- `artifacts/policy_reversal_zone.csv` (detailed sweep results)

---

# analysis s1 only results collect

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_s1-only-results-collect_20260523T085305_result.json`
- **Structured JSON:** [`fa6ed32e9106317fbbe7.json`](../../sessions/fa/fa6ed32e9106317fbbe7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results collected and written. Key summary:

**S1-only (Min-K++ alone) vs RRF (3-signal fusion):**

| | MMLU γ | ARC γ | GSM8K γ | MMLU PPP | MMLU MAE_cal | MMLU τ |
|---|---|---|---|---|---|---|
| S1-only | 1.754 | 2.572 | −0.048 | 0.0003 | 0.073 | 0.628 |
| RRF | 0.698 | 0.727 | 0.064 | 0.193 | 0.009 | 0.730 |

S1-only is strictly worse on every metric that matters:
- **γ inflated 2.5–3.5×** due to model misfit (not stronger signal)
- **PPP catastrophic** (0.0003 / 0.000) — IRT model rejects the S1-only exposure
- **Calibration MAE 6–8× worse**
- **Ranking (τ) worse** by ~0.10–0.14
- **ESS 5–6× lower** — MCMC struggling
- **Domain-level completely fails** (STEM_Math γ=−6.32, PPP=1.000)
- GSM8K (negative control) is similar — both correctly find γ≈0

This strongly validates the multi-signal RRF fusion as essential for the IRT calibration pipeline.

---

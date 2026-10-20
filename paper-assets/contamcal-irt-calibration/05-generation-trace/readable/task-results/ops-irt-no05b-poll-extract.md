# ops irt no05b poll extract

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_irt_no05b_poll_extract_20260517T074011_result.json`
- **Structured JSON:** [`73deb1f57feb6c2b9c94.json`](../../sessions/73/73deb1f57feb6c2b9c94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact file written to `artifacts/mmlu_domain_irt_no05b_results.md` with all 9 domains' results.

**Summary of J=13 (no 0.5B) experiment:**

- **Social_Sciences is the only significant domain**: γ = −0.571, CI [−1.054, −0.103], but the direction is *negative* (3B underperforms, not overperforms)
- **No domain shows significant positive γ** — removing 0.5B models eliminated all contamination signal
- **θ extraction not possible** — Stan CSV files were not retained in the output directories, only `irt_results.json`

The core takeaway: 0.5B models are essential as the low-ability anchor for the IRT contamination detection method. Without them, J=13 respondents lack sufficient ability spread to resolve γ.

---

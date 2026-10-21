# ops d047 nearchance filtered

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d047-nearchance-filtered_20260525T215030_result.json`
- **Structured JSON:** [`8254ebf6cb1fe03d199f.json`](../../sessions/82/8254ebf6cb1fe03d199f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits are clean. Here's the summary:

---

**Filtered (13 models) results after position-bias fix:**

| K | n | OLS | WCB | Frac | β̄_std | R̄² |
|---|---|-----|-----|------|--------|-----|
| 3 | 286 | 12/12 | 5/12 | 10/12 | 0.291 | 0.361 |
| 5 | 1,287 | 11/12 | 3/12 | 11/12 | 0.321 | 0.271 |
| 7 | 1,716 | 10/12 | 1/12 | 10/12 | 0.251 | 0.212 |

**Files updated:**
- `appendix.tex`: Filled 3 TBD rows, updated caption (removed TBD note), replaced placeholder text with analysis of full-vs-filtered comparison
- `appendix.tex` line 1177: Changed "strengthens" → "preserves" for near-chance exclusion recommendation
- `main.tex` line 45: Changed "strengthens the association" → "preserves the association (OLS 10--12/12)"

**Key finding:** OLS and fractional logit significance remain high (10–12/12) after filtering, confirming the diversity–vulnerability association is not driven by near-chance models. WCB significance drops substantially due to reduced panel counts lowering bootstrap power. β̄_std is slightly lower in the filtered pool at K=5,7, so "strengthens" was corrected to "preserves."

---

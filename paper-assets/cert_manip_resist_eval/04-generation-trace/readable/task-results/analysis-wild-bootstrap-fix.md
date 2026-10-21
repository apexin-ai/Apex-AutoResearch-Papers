# analysis wild bootstrap fix

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_wild-bootstrap-fix_20260522T195622_result.json`
- **Structured JSON:** [`04f9fcf1c4f9491dc649.json`](../../sessions/04/04f9fcf1c4f9491dc649.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Bootstrap v2 completed. Results:

**Validation**: `arc_challengexsycophancy` K_eff std_β = **-0.1917** (expected -0.192) ✓

**Summary (B=9999, 3-position clustering, max p-value)**:
- **K_eff FDR sig: 1/12** (1 positive, 0 negative) — only `mmlu×prompt_injection` survives
- **η_max FDR sig: 5/12** — `mmlu×{prompt_injection, sycophancy, verbosity_bias, position_bias}` + `arc×sycophancy`

Compared to the old (buggy) v1:
| Method | η_max FDR sig | K_eff FDR sig |
|---|---|---|
| Canonical OLS | 11/12 | 8/12 |
| Clustered SE | 8/12 | 0/12 |
| Wild Bootstrap v1 (buggy) | 10/12 | 9/12 |
| **Wild Bootstrap v2 (fixed)** | **5/12** | **1/12** |

The fixed bootstrap is much more conservative — K_eff drops from 9/12 to 1/12, η_max from 10/12 to 5/12. This is expected: the old v1 used a wrong K_eff formula (inflating the signal) and a single weaker clustering.

---

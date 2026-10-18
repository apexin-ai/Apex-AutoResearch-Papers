# paper writing results v5

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_results_v5_20260522T202417_result.json`
- **Structured JSON:** [`09dca9e0a3d05df4b3ae.json`](../../sessions/09/09dca9e0a3d05df4b3ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Written. The rewrite:

- **§4.1**: Reframed as OLS baseline. Table 1 unchanged. Added non-independence paragraph (15 judges, 91 panels each, ~2.5x SE underestimate). Dominance and r=0.70 paragraphs qualified with "under OLS." Removed the sycophancy mechanism paragraph (now in §4.3).
- **§4.2**: New section with Table 2 (tab:robustness). Covers why correction is needed, η_max survival (5-8/12), K_eff collapse (0-1/12), practical effect size (1.3pp), arc×sycophancy downgrade (p=0.013→0.441→0.136→~0.06).
- **§4.3**: New section. GAM taxonomy: targeted attacks (6/6 positive K_eff) vs shared-bias attacks (6/6 negative K_eff). Caveat on pending bootstrapped CIs.
- **§4.4**: Table 2 unchanged. "dual" removed. Added note that aggregation results are independent of non-independence concern. Prescriptive gradient kept as-is.

---

# research reference audit r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_reference-audit-r2_20260515T204542_result.json`
- **Structured JSON:** [`7b19f3a309ee375ce098.json`](../../sessions/7b/7b19f3a309ee375ce098.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Audit complete. Here's the summary:

### Fixes Applied (3)

1. **ReconVLA intro** — Changed "operates as an uncertainty quantification framework rather than an action improvement method" → correctly describes it as using UQ for **action selection and OOD detection**, taking a "complementary UQ-driven approach rather than learning explicit corrective residuals"

2. **ReconVLA related work** — Changed "does not modify the VLA's actions" → correctly states it "enables uncertainty-guided action selection and proactive failure detection without retraining"

3. **ACP+CBF bib title** — Corrected from fabricated title to actual paper title "Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction"

### Flagged for Pre-Submission (2, not blocking)

- **LIBERO-Plus numbers** (94.2%→6.6% for π₀, 95.2%→4.3% for UniVLA) — general trend confirmed, exact numbers need verification against Table 1 of the actual paper
- **SC-VLA "residual RL"** — defensible but imprecise; "online RL" would be more accurate

### Verified Correct (27/30 citations)
All other method attributions checked out against the actual papers via web search.

Full report registered as `artifacts/_project/report/reference_audit_r2.md`.

---

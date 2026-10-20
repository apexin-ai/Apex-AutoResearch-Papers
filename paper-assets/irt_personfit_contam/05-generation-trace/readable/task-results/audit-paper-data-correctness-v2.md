# audit paper data correctness v2

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_paper-data-correctness-v2_20260524T061618_result.json`
- **Structured JSON:** [`450dbfe2c83c672dd55e.json`](../../sessions/45/450dbfe2c83c672dd55e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Audit complete. Key findings:

**38/46 cells verified MATCH.** The vast majority of paper values exactly match server data.

**2 critical mismatches — Mistral MMLU free-θ d values:**
- d(15%)=−3.01 is mathematically inconsistent with the contam lz* on the server. With the paper's own baseline (4.02, 2.05), the correct value would be −2.64. With the 6 available clean seeds, it's −1.97.
- d(50%)=−3.50 matches the paper baseline computation.
- Root cause: 4 of 10 Mistral clean seeds were lost with old server 19912. The original n=10 computation cannot be reproduced.

**6 cells unverifiable** — Mistral baseline and all ARC-C values lack sufficient data on the server.

**1 minor inconsistency** — ARC-C 50% CI upper bound: 15.2 in Table 1 vs 15.5 in figure scripts.

Report saved to `artifacts/data_audit_report.md`. The highest priority fix is the Mistral d(15%) value — either recover the original computation or recompute with n=6 and update the paper.

---

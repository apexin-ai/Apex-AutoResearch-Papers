# analysis claim audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_claim-audit_20260522T181701_result.json`
- **Structured JSON:** [`e143bdfadb52d7571c3d.json`](../../sessions/e1/e143bdfadb52d7571c3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Audit complete. Key findings:

**❌ Critical (1)**: `experiments_main.tex:89` claims "LP-best +8 pp on Few-NERD" — no data supports this. The same paper says +1.39pp (LP selection) and +1.40pp (LP construction) in three other locations. Must fix before submission.

**⚠️ Warning (7)**:
1. Selection table mixes micro/macro F1 baselines in caption vs body (11.4pp vs 13.0pp headroom)
2. Limitations "Δ_SC = −0.74±0.57 pp, consistent negative" — uses single-seed value, not 3-seed mean; one seed is positive
3. Epoch confound reports max seed (0.12) not mean (0.09) for 5-epoch LP delta
4. WNUT zero-F1: 51% in paper vs 53.7% in registry
5. RE zero-F1: "40%" in intro vs 43-47% in registry
6. SciERC greedy .667 in table vs 3-seed mean .663
7. Discussion "std ratio 0.92–0.97×" — 0.92 source unverified

**Resolved**: The originally flagged Discussion/Limitations contradiction ("+0.1pp" vs "+0.4pp") no longer exists in current tex. 37 other quantitative claims verified correct.

---

# analysis r11 3verifier canonical

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r11-3verifier-canonical_20260521T114828_result.json`
- **Structured JSON:** [`7d2a385cb2a102117ff2.json`](../../sessions/7d/7d2a385cb2a102117ff2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Results saved to `artifacts/r11_3verifier_canonical.json` and registered as `art_20260521_0c36fe`.

**Key results summary:**

| Verifier | Standalone | w=1 | w=3 | w=5 |
|----------|-----------|-----|-----|-----|
| DeBERTa-L | 55.00% | +0.83pp | **+6.67pp** (p=1.1e-5) | **+11.00pp** (p=6.2e-7) |
| RoBERTa-L | 37.67% | -0.17pp | **+4.17pp** (p=0.003) | +4.33pp (p=0.037) |
| BART-L | 46.17% | 0.00pp | **+5.17pp** (p=2.4e-4) | **+6.33pp** (p=0.003) |
| Ensemble (maj) | 48.33% | +0.33pp | **+5.83pp** (p=6.5e-5) | **+8.00pp** (p=2.4e-4) |
| Additive (3×w) | — | **+5.33pp** (p=1.3e-4) | **+12.00pp** (p=2.8e-5) | **+9.83pp** (p=0.004) |

**BH correction:** 10/15 tests significant at α=0.05. Only w=1 tests for all verifiers and roberta_w5 (adj_p=0.0503, borderline) are non-significant.

**Canonical verification:** DeBERTa w3 = 276/600, +6.67pp, b=21, c=61, p=1.13e-05 — matches paper exactly.

**Root cause of previous failures:** The combo method must be hard-vote (add w integer votes to NLI-predicted class), not probability-weighted. The `mistral_pw600_sc_votes.json` also required fixing 2 mismatched question IDs (Q4→Q8).

---

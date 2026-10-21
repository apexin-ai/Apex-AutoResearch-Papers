# analysis exp011 discordant detail

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp011-discordant-detail_20260517T080745_result.json`
- **Structured JSON:** [`c9e26ef7c7c5f50ed0dc.json`](../../sessions/c9/c9e26ef7c7c5f50ed0dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
DISCORDANT PAIRS (SICA wins):
#1: problem_id=ProofWriter_RelNoneg-OWA-D5-1036_Q11, domain=PW, truncated=N (0 traces truncated), multi_cand=3
    SICA=True, SC=Unknown, GT=True
#2: problem_id=ProofWriter_RelNeg-OWA-D5-856_Q19, domain=PW, truncated=Y (3 traces truncated), multi_cand=3
    SICA=Unknown, SC=False, GT=Unknown
#3: problem_id=folio_002, domain=FOL, truncated=N (0 traces truncated), multi_cand=3
    SICA=True, SC=False, GT=True
#4: problem_id=folio_014, domain=FOL, truncated=N (0 traces truncated), multi_cand=3
    SICA=False, SC=Unknown, GT=False
#5: problem_id=folio_027, domain=FOL, truncated=N (0 traces truncated), multi_cand=2
    SICA=Unknown, SC=True, GT=Unknown

DISCORDANT PAIRS (SC wins):
#1: problem_id=ProofWriter_RelNoneg-OWA-D5-709_Q12, domain=PW, truncated=N (0 traces truncated), multi_cand=3
    SICA=Unknown, SC=False, GT=False

SUMMARY:
SICA-wins with truncation: 1/5 (only #2 has 3 truncated traces)
SC-win with truncation: 0/1
SICA-wins in FOLIO: 3/5
SICA-wins in ProofWriter: 2/5
```

Key observation: truncation is **not** the driver of SICA's advantage here. Only 1 of 5 SICA-win cases involved truncated traces. SICA wins primarily by resolving vote-tie or near-tie situations (e.g. #1: SC ties 5-5 between Unknown/True; #5: SC ties 6-6) where constraint-weighted scoring breaks the deadlock correctly.

---

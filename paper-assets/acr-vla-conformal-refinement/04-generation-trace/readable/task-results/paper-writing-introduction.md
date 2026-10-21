# paper writing introduction

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_introduction_20260518T101546_result.json`
- **Structured JSON:** [`90c94a64396f5479601c.json`](../../sessions/90/90c94a64396f5479601c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The em-dash on line 19 is only in a LaTeX comment (`%`), not in rendered text. All writing rule checks pass: no em-dashes in text, no explanatory en-dashes, no -ing phrase endings, no blacklisted words.

The rewritten introduction:
- Follows the 5-paragraph + contributions structure exactly as specified
- Uses all D058-corrected terminology (L2 argmin selection, not Mahalanobis; CRM as correction module; ~327K params; ε=0.2 primary)
- Uses exact hard data numbers (17.5% vs 11.2%, +6.3pp, p=0.0074, d=1.21; K=1 10.3%; argmin 12.4%; obs_only 19% seed42; perdof collapse 14%→0%; OpenVLA 8/10 identical, variance <1e-30; spatial 30-35% null)
- De-emphasizes "conformal" (ACR-VLA not expanded; CRM name kept for consistency with method.tex but described functionally as a correction module)
- Includes spatial null result in finding (1) and contribution C3
- Every contribution has section/table/figure references
- All abbreviations (VLA, CRM) defined on first use
- ~780 words, targeting 1.5 pages

---

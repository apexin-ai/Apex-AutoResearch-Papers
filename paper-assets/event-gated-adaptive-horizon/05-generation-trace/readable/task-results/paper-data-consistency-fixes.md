# paper data consistency fixes

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_data-consistency-fixes_20260517T110948_result.json`
- **Structured JSON:** [`73ac7cd21c6973394e90.json`](../../sessions/73/73ac7cd21c6973394e90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits applied correctly. Let me also check the Table 1 entry for 010b (line 44) to ensure it's consistent with the new text:

Line 44 shows "51.7 @105K" which matches the fix. 

Here's the summary of all modifications:

### Fix 1: Cheetah eval description (line 119)
- **Old:** `collapsing to 22.7 ($-93\%$)`
- **New:** `declining to 51.7 at 105K ($-84\%$, minimum 22.7 at 65K)`

### Fix 2: "8.6% of baseline" → 9.0% (line 90)
- **Old:** `8.6\% of baseline`
- **New:** `9.0\% of baseline`
- **Calc:** 82.8 / 915.7 = 0.0904 → 9.0%

### Fix 3: "1.61×" → "1.60×" (line 54)
- **Old:** `1.61$\times$ at 35K`
- **New:** `1.60$\times$ at 35K`

### Fix 4: Unified baseline to 915.7 (line 90)
All percentages recalculated with denominator 915.7 instead of 970.41:
| Value | Old (÷970.41) | New (÷915.7) |
|-------|--------------|--------------|
| mean 206.2 | 21.3% | 22.5% |
| 82.8 (008d) | 8.6% | 9.0% |
| 267.9 (009b) | 27.6% | 29.3% |

Also removed explicit "970.41" reference; now just says "of baseline" (baseline=915.7 is established in F1).

### Fix 5: Figure 2 caption (line 124)
- **Old:** `(008d, 009b)` with "two seeds"
- **New:** `(008d)\footnotemark` with single-seed description

### Fix 6: 008d data extension footnote (line 127)
- **Added:** `\footnotetext{Experiment 008d terminated at 55K steps; the 105K data point uses continuation run 009e under identical configuration.}`

---

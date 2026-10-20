# paper table1 019b 022b fix

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_table1-019b-022b-fix_20260517T161318_result.json`
- **Structured JSON:** [`6e09a04cc17384518d50.json`](../../sessions/6e/6e09a04cc17384518d50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No other occurrences of 1.22 in the paper directory. Both edits applied cleanly. Footnote structure is intact (all footnote markers `$^a$`, `$^b$`, `$^*$`, `$^\diamond$`, `$^c$` remain coherent).

**Summary of changes in `results.tex`:**

| Line | Before | After |
|------|--------|-------|
| 35 | `1.22$\times$` | `0.63$\times$` |
| 58 | `$^c$ Raw V/E ratio (peak 5.66 at 52.5K); no same-environment baseline available for NVE normalization in PickCube.` | `$^c$ NVE normalized against exp\_019a\_v2 (vanilla DreamerV3 on PickCube-v1).` |

**NVE computation detail:** 022b peak V/E ratio = 0.2177 (at 55K), but peak NVE in 35K+ window = 0.63x at step 35K (022b ve=0.1524 / baseline ve=0.24122). The 1.22x was a bug in the checkpoint logging. The "No CIVO" verdict is unchanged (0.63 is well below 1.5x).

---

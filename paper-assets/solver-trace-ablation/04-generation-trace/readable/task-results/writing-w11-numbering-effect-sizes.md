# writing w11 numbering effect sizes

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_w11-numbering-effect-sizes_20260516T023018_result.json`
- **Structured JSON:** [`057bbdadc13013c18e51.json`](../../sessions/05/057bbdadc13013c18e51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits complete. Summary:

**Part 1 — Numbering fix:**
- H1, H7 (H7a/H7b), H8 references are consistent throughout all files. The gap (H2–H6 don't exist as labels) is intentional — only the 3 dominant modes get H-labels, the other 5 are referenced by name. The "eight modes" count is correct.
- **Fixed one inconsistency**: appendix.tex table caption said "H7b (n=12; ISR s44 only)" but the correct total is n=14 (12 from s44 + 2 from s43). Updated to match experiments.tex which correctly says n=14.

**Part 2 — Effect sizes added (6 locations in experiments.tex):**

| Comparison | Location | Effect Size |
|---|---|---|
| SFT vs exec-only NH rate | line 35 | OR=147, p<0.001 |
| 100-step RL vs SFT hacking | line 37 | OR=5.5, 95% CI [1.4, 22.0] |
| H7 ISR vs Random β=0.1 | line 69 | 95% CI [9.6, 23.6] added to existing OR=15.05 |
| PR ISR vs Random β=0.1 | line 74 | Cohen's d=0.90, n=3 per group |
| NH rate ISR vs Random β=0.1 | line 80 | OR=0.61, 95% CI [0.31, 1.21] |
| H7 ISR vs Random β=0.3 | line 102 | OR=13.7, 95% CI [7.0, 26.8] |

---

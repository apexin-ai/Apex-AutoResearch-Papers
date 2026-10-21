# paper compress 8 items

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compress-8-items_20260517T144658_result.json`
- **Structured JSON:** [`dc27ee2e6528cd4154ae.json`](../../sessions/dc/dc27ee2e6528cd4154ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No undefined references. The PDF compiles cleanly at 21 total pages. Discussion and Conclusion (Section 5) ends on page 8, with Limitations starting on the same page.

Here's the summary:

### Edits executed

| # | File | What changed | Lines saved (approx) |
|---|------|-------------|---------------------|
| 1 | method.tex L64-66 | O(1) variant: 3 sentences → 1 sentence + Appendix ref | ~2 |
| 2 | experiments.tex L106-109 | β=0.05: 4 sentences → 2 sentences; per-seed random breakdown moved to new Appendix §app:beta005 | ~4 |
| 3 | experiments.tex L11 | Setup: removed legacy filename note + eval_sta.py clause; both moved to Appendix §app:setup | ~1.5 |
| 4 | experiments.tex L38-39 | 100-step RL checkpoint: 2 sentences → 1 sentence with Appendix ref | ~1.5 |
| 5 | experiments.tex L120-123 | Dose-response: 4 sentences → 2 sentences; removed repeated per-β numbers | ~2 |
| 6 | experiments.tex L111-113 | β=0.2: 3 sentences → 1 sentence; ISR* numbers dropped (already in Appendix Table) | ~1.5 |
| 7 | experiments.tex L98-99 | Premise-count confound: removed specific ISR* numbers, kept conclusion | ~0.5 |
| 8 | introduction.tex L33 | C2: removed seed trajectory detail ("trajectory analysis on seeds 42 and 45...") | ~1.5 |

### Appendix additions
- **app:setup**: Added "Evaluation protocol" paragraph (uniform ISR recomputation + legacy filename note)
- **app:beta005**: New subsection "Per-Seed Results at β=0.05" with random control per-seed breakdown

### Result
- Total saved: ~15 lines
- Main body (Abstract through Conclusion): ends on **page 8**
- **Main body ≤ 8 pages: confirmed**
- No undefined references, no LaTeX warnings
- Backup edits #9/#11 not needed

---

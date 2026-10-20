# paper writing method

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_method_20260514T191123_result.json`
- **Structured JSON:** [`3f65369d1fbc53a8738b.json`](../../sessions/3f/3f65369d1fbc53a8738b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Method section written to `paper/method.tex`. Changes from the previous draft:

- **Added Figure 1** (`fig:sta-overview`) — the 3-panel STA overview figure, placed at the top of the section
- **Added `\autoref` references** to Figure 1 panels (a), (b), (c) in the Task, STA, and Reward Signal subsections
- **Dropped convex formulations** — experiments.tex only uses 6 conditions (exec-only, ISR×2β, random×2β, SFT); convex was not part of the main experimental matrix
- **Trimmed taxonomy section** — removed quantitative results (percentages, seed-specific data) that belong in §4; kept definitional descriptions only, with a forward reference to `\S\ref{sec:taxonomy}`
- **Added explicit equation labels** for the random control reward (`eq:additive-random`)
- **Fixed label collision** — taxonomy label changed to `sec:taxonomy-method` to avoid colliding with `sec:taxonomy` in experiments.tex

---

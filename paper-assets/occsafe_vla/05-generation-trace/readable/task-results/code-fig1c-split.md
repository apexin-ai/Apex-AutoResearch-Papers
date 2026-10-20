# code fig1c split

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fig1c-split_20260529T011809_result.json`
- **Structured JSON:** [`5ed00eb274fd3db51394.json`](../../sessions/5e/5ed00eb274fd3db51394.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Summary of changes:

**New files** (original `fig1_overview.py` preserved):
- `fig1_architecture.py` — panels (a) + (b) only, full double-column width, outputs `fig1_architecture.pdf/png`
- `fig1c_results_bar.py` — CAR dot plot only, single-column width (3.5"), outputs `fig1c_results_bar.pdf/png`

**LaTeX** (`introduction.tex`):
- Fig 1 → `figure*` environment with `fig1_architecture.pdf`, caption covers (a)+(b), label `fig:overview` retained
- New `figure` (single-column) with `fig1c_results_bar.pdf`, label `fig:results_bar`
- The existing `Figure~\ref{fig:overview}` reference on line 21 still applies (it refers to the factorial design)

---

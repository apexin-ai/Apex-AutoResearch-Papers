# paper update table1 ci

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_update_table1_ci_20260517T143445_result.json`
- **Structured JSON:** [`8c9d729ed18a22b9e9fc.json`](../../sessions/8c/8c9d729ed18a22b9e9fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

LaTeX compiles cleanly with zero errors, 19 pages output.

**Summary of changes across 7 files:**

**Table 1 (`atlas.tex`):** Updated all 9 cells to bootstrap point estimates with `±` CI half-widths (all ≤0.6pp). GPT-2 XL row bolded as best per column. Caption now references "bootstrap 95% CI (10,000 resamples)" instead of "5-fold CV SD ≤ 0.9pp".

**Inline text updates (26 edits across files):**
- `atlas.tex`: accuracy range 68.8–85.9%, per-model/strategy ranges, spread 17.1pp, strategy gap 9.2pp / model gap 7.2pp
- `abstract.tex`: ≈69–86%, 43pp below RF
- `introduction.tex`: 43pp below RF
- `discussion.tex`: 69–86%
- `method.tex`: Pythia 78.7% vs GPT-2 XL 85.9%
- `generalization.tex`: range 68.8–85.9%, CORAL/DivEye within 0.6pp, 43pp gap vs RF at 78.7%, baselines table diff ≤0.2pp, confusion matrix caption 85.9%, E2E lagging 20pp
- `conclusion.tex` (Limitations): 78.7% vs 85.9%
- `section_appendix.tex`: DCOL baseline 78.7%, E2E gaps 20.4/19.2pp, cross-scale table 84.1/78.9/78.7, 20pp accuracy gap

---

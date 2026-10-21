# paper appendix auroc revert

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix-auroc-revert_20260517T130453_result.json`
- **Structured JSON:** [`d06c30886e7229def655.json`](../../sessions/d0/d06c30886e7229def655.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Changes complete. Summary:

**Changed (0.867 → 0.933):**

| File | Line | Context |
|------|------|---------|
| `docs/paper/sections/appendix.tex` | 35 | `$\text{AUROC} = 0.867$` → `$\text{AUROC} = 0.933$` (inline text referencing Table B2) |
| `docs/paper/sections/appendix.tex` | 61 | `$\text{AUROC}=0.867$` → `$\text{AUROC}=0.933$` (Table B2 caption) |
| `paper/tables/nve_sensitivity_table.tex` | 11 | B2 row `0.867` → `0.933` (same 3/5 pool, standalone artifact) |
| `artifacts/_project/paper/nve_sensitivity_table.tex` | 11 | B2 row `0.867` → `0.933` (artifact copy) |

**Not changed (correct as-is):**
- `results.tex:81` — footnote 0.867 (different pool: 8-experiment subset excluding 3 baselines)
- `results.tex:81` — main text AUROC=0.926 (12-experiment full set)
- Table 4 data rows — untouched

**Three calibrations confirmed:**
- Main text: **0.926** (12 experiments, full set)
- Main text footnote: **0.867** (8 experiments, non-baseline JSON pool)
- Appendix Table B2: **0.933** (8 experiments, 3 pos / 5 neg, 14/15)

---

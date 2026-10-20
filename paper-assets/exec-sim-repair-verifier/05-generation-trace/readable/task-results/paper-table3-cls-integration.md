# paper table3 cls integration

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_table3-cls-integration_20260520T005447_result.json`
- **Structured JSON:** [`7efe464a6d32b27a33d0.json`](../../sessions/7e/7efe464a6d32b27a33d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Table 3 updated. Numbers verified against JSON:
- Qwen3-8B CLS: **84.83 $\pm$ 0.67** (3 seeds) ✓
- DeepSeek CLS: **84.38 $\pm$ 2.50** (2 seeds, with ‡ footnote for s123 exclusion) ✓
- TRAJ: **73.61 $\pm$ 3.18** (3 seeds) ✓
- Majority: **72.96** ✓
- CWM: `\tbd{}` placeholder ✓

Changes made:
1. **main.tex**: added `\newcommand{\tbd}{\textsc{tbd}}`
2. **experiments.tex**: removed 43-line commented-out multi-seed template; replaced single-seed Table 3 with multi-seed version; updated caption, footnotes (including DeepSeek s123 exclusion note), and bold marking (moved from 4B to 8B as new best)

DeepSeek CLS Var. column now shows only s42=81.25 (s123 excluded for consistency with per-test exclusion). Surrounding body text (lines 135-139) still discusses single-seed CWM comparisons, which remains valid as labeled.

---

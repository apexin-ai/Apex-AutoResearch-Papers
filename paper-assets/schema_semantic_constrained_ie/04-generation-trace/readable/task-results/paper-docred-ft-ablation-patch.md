# paper docred ft ablation patch

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_docred_ft_ablation_patch_20260516T205702_result.json`
- **Structured JSON:** [`8f2b9d461efb1c9c6778.json`](../../sessions/8f/8f2b9d461efb1c9c6778.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Summary of changes:

**1. `artifacts/_project/report/ft_ablation_analysis.md`** — Fixed SciERC Table 1 values:
- Qwen Unconstrained/Grammar Only DR: 1.95% → 1.90%
- Qwen Semantic Only DR: 0.62% → 0.60%
- Updated corresponding mentions in Key Findings (68% reduction text and residual DR text)

**2. `artifacts/_project/paper/section5_scierc_draft.tex`** — Two changes:
- Fixed all `1.95%` references to `1.90%` (narrative text + composability table)
- Expanded the one-line DocRED FT mention into a full paragraph covering the four-way ablation: grammar layer eliminates RV but not DR, semantic layer reduces DR 72%/39%, full system achieves near-zero DR, parse failure context

**3. `artifacts/_project/paper/appendix_discussion.tex`** — Fixed:
- FT ablation table: SciERC Qwen Unconstrained DR 1.95 → 1.90
- Narrative: Qwen SciERC semantic reduction 69% → 68%
- Post-hoc comparison table: Qwen SciERC FT Reject% 1.95 → 1.90

---

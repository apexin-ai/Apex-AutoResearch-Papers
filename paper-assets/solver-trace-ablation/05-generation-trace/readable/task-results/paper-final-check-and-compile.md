# paper final check and compile

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_final-check-and-compile_20260522T114610_result.json`
- **Structured JSON:** [`bdb62bccd3b0b6d1e7d8.json`](../../sessions/bd/bdb62bccd3b0b6d1e7d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results summary:

**1. 8B appendix** (`app:8b-results`, line 729): Complete. PR=14%, ISR*=0.573, genuine=92.9%, CE=1, K=4 stagnation, K=8 non-convergence — all present. No changes needed.

**2. Limitations 8B caveat** (line 4): Consistent — "neither Qwen3-8B nor LLaMA-3.2-3B converges under our GRPO configuration" with correct appendix refs.

**3. Sync status**: 
- .tex/.bib files: only `main.tex` differed (docs/paper had float/placeins packages; paper/ had `\input{checklist}` which per CLAUDE.md belongs on OpenReview, not in PDF). Synced docs/paper → paper.
- Figures: fig4, fig5 (pdf/png/gen_*.py) differed. Synced.
- Now clean — zero diffs.

**4. Compilation**: Success.
- Total pages: **22**
- Main text (§1-5) ends on page 8, References start on page 8 — **within 8-page limit** (Limitations + Ethics don't count per EMNLP rules)
- Appendix starts page 10
- **Undefined references: 0**
- **Missing citations: 0**

**5. Em-dash check**: All `---` occurrences are legitimate LaTeX em-dashes (used as "N/A" markers in tables like `--- & 12 & ---`) or standard LaTeX triple-dash em-dashes in section headers (e.g., `"What ISR measures---and what it does not"`). The Unicode em-dash `—` appears only in a comment line (`% Appendix — solver-trace-ablation`). No issues.

---

# paper binary headline update

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_binary-headline-update_20260515T185211_result.json`
- **Structured JSON:** [`a0d1ff07b76e7025154d.json`](../../sessions/a0/a0d1ff07b76e7025154d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks pass. Here's the summary:

**Task 1 (abstract)**: Added gen-0 shared-seed exclusion caveat ("---excluding gen-0 to avoid shared-seed overlap---") to both `artifacts/_project/paper/abstract.tex` and `docs/paper/abstract.tex`. Binary F1=0.723 was already the headline.

**Task 2 (introduction)**: No changes needed — binary F1=0.723 was already the headline in both the main paragraph (line 25) and contribution list (line 34). No stale 0.789-as-headline usage found.

**Task 3 (results P1-E ordinal)**: Already written at `results.tex:53-58`. CORAL 0.771, Frank-Hall 0.793, XGBoost 0.789 (3-class); XGBoost 0.721, CORAL 0.728 (binary); concordance all CIs overlapping. Conclusion already states standard XGBoost suffices.

**Task 4 (related_work CI fix)**: No CI/confidence-interval mentions exist in `related_work.tex`. Non-issue.

**Task 5 (consistency check)**: 0.789 appears only in appropriate 3-class contexts (results tables, ablation, supplementary, discussion comparisons). 0.723 is the primary metric in abstract, intro, conclusion, discussion, and results baseline section. No stale headline usage.

**Task 6 (docs/paper sync)**: Abstract synced. Introduction and results were already identical across both locations.

---

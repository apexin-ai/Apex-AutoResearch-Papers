# paper dream review fixes p0

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_dream-review-fixes-p0_20260521T235011_result.json`
- **Structured JSON:** [`0156c18534d526769f4b.json`](../../sessions/01/0156c18534d526769f4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 52 citation keys resolve. Final state of the edits:

**P0-1 Related Work — 4 changes made (both artifacts/ and docs/ copies):**

1. **Alemohammad (self_consuming_mad)** — Added sentence connecting their autophagous loop to our recursive generation setup at inference time (§2.2, line 16)
2. **Dohmatob "Tale of Tails"** — New bib entry `dohmatob_tale_of_tails` (ICML 2024, 5 authors verified via WebSearch). Added discussion linking their scaling-law theory to DDR's distributional compression (§2.2, line 16)
3. **Kirchenbauer watermarking** — Expanded watermarking discussion to note generator cooperation requirement and that our approach is post-hoc, applicable when watermarks are absent or washed out (§2.4, line 33)
4. **Guo "curious decline"** — Added explicit connection between their recursive vocabulary impoverishment and DDR's drifting TTR/hapax features (§2.3, line 26)

**P0-2 XGBoost hyperparameters:**
- Already present in method.tex (n_estimators=200, max_depth=6, lr=0.1). Added "fixed without tuning" — code confirms no GridSearch/Optuna/etc. was used.

---

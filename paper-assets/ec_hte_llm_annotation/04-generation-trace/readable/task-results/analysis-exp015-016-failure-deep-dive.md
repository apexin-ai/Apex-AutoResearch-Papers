# analysis exp015 016 failure deep dive

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp015-016-failure-deep-dive_20260521T143406_result.json`
- **Structured JSON:** [`5b55161f1ae6fae38c0f.json`](../../sessions/5b/5b55161f1ae6fae38c0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All deliverables complete. Here's the summary:

**Report:** `artifacts/failure_analysis/exp015_016_deep_dive.md`
**Figures:** 8 PNGs + 3 CSVs in `artifacts/failure_analysis/`

### Key Findings

**Root cause:** HB EC-HTE fails in exp-015/016 because P(Z=1)=0.18 yields only 2.5–34 minority-class experts per subgroup — far too few for reliable per-subgroup CM estimation. The HB model doesn't just fail to shrink; it **overshoots** global correction by 2–9x (shrinkage coefficients >> 1) because it pools CATE estimates but not CM estimates.

**Decision boundary (from 368 observations across 5 experiments):**
- `cond_number(M) ≤ 1.2` AND `eff_minority_n ≥ 25` → **93% HB win rate**
- exp-015/016 fail both conditions (cond 1.55–2.38, eff_n 2.5–34)

**Three improvement directions identified:**
1. **CM quality diagnostic** — pre-check before applying EC-HTE (calibrated thresholds provided)
2. **Hierarchical CM pooling** — pool the CM estimates themselves, not just downstream CATEs (architectural fix)
3. **Sigmoid shrinkage to global** — smooth fallback when per-subgroup CM is unreliable (formula in report)

---

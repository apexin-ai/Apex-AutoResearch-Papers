# research second dataset v2

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_second-dataset-v2_20260522T044026_result.json`
- **Structured JSON:** [`52cc85d81a80afa3299c.json`](../../sessions/52/52cc85d81a80afa3299c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All tasks complete. Here's the summary:

---

## exp-023 Civil Comments Validation — Complete

### Deliverables produced:

1. **LLM Annotations**: 800–900 annotations per model (gpt-4o, gpt-4o-mini, gpt-3.5-turbo) on 3000 Civil Comments samples. Run2 still extending to 3000/model in background.

2. **Confusion Matrices** (`exp023_confusion_matrices.json`): Per-subgroup (K=4) FPR/FNR for all 3 models. **Δπ > 0.05 confirmed** for all models (0.113–0.160).

3. **Semi-synthetic results** — three experiment variants:
   - Asymmetric CMs (`exp023_semisynthetic_*.csv`): Real LLM CMs, uniform CATE
   - Symmetric (`exp023_symmetric_*.csv`): Observed rates as symmetric flip probs, per-subgroup CATE
   - V2 controlled (`exp023_semisynthetic_v2_*.csv`): 5 regimes including oracle_corrected ceiling

4. **Analysis report** (`exp023_civil_comments_analysis.md`): Comprehensive findings

5. **Script** (`exp023_civil_comments_symmetric.py`): Saved as proper file

### Key findings:

| Finding | Status |
|---------|--------|
| Δπ > 0.05 across LLMs on 2nd dataset | **Confirmed** |
| EC-HTE outperforms Naive/Global in RMSE | **Not reproduced** (same on TweetEval) |
| Oracle-corrected also worse RMSE than naive | **New finding** — RMSE penalty is structural |
| EC-HTE restores calibrated coverage | **Confirmed** (naive 0.63–0.84 → corrected 0.90–0.97) |

The honest conclusion: EC-HTE's value proposition on Civil Comments (and TweetEval) is **coverage calibration**, not RMSE reduction. The RMSE penalty from matrix inversion is inherent — even perfect CM knowledge doesn't overcome it at these sample sizes.

---

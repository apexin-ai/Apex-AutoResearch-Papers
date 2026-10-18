# code claude judge lmbar scoring

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_claude_judge_lmbar_scoring_20260521T082556_result.json`
- **Structured JSON:** [`c5c9b4702f5968409428.json`](../../sessions/c5/c5c9b4702f5968409428.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline complete. Here are the results:

---

## Claude Sonnet 4 x Formality (LLMBar)
Pairs: 88
BT: P(formal)=56.2% [48.9%, 63.6%], p=0.0912
Likert: ATE=-0.045, p=0.7207, d=-0.021, tie_rate=68.2%
Blindspot: No
GEE: Style OR=1.47 p=0.2757, Orig OR=6.66 p=< 0.0001

## Claude Sonnet 4 x Verbosity (LLMBar)
Pairs: 86
BT: P(verbose)=54.1% [45.9%, 61.6%], p=0.2840
Likert: ATE=-0.081, p=0.7427, d=-0.039, tie_rate=67.4%
Blindspot: No
GEE: Style OR=1.52 p=0.2858, Orig OR=0.80 p=0.5626

---

Key takeaways:
- **No significant style blindspot** on either axis — Claude Sonnet 4 shows no statistically significant preference for formal or verbose responses (both BT p > 0.05)
- **Formality**: slight lean toward formal (56.2%) but not significant; very high Likert tie rate (68.2%); **very strong originality bias** (Orig OR=6.66, p < 0.0001) — Claude strongly prefers whichever response is the original
- **Verbosity**: even weaker lean toward verbose (54.1%); high tie rate (67.4%); no significant originality bias (Orig OR=0.80, p=0.56)

Script saved at `csd_pipeline/claude_judge_scoring.py`. Output files: `pairwise_results_claude_formality.jsonl`, `pairwise_results_claude_verbosity.jsonl`, `scored_claude_formality.jsonl`, `scored_claude_verbosity.jsonl`.

---

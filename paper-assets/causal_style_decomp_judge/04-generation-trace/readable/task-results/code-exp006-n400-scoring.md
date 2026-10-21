# code exp006 n400 scoring

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp006_n400_scoring_20260521T082405_result.json`
- **Structured JSON:** [`3689b99cf9bca5d41def.json`](../../sessions/36/3689b99cf9bca5d41def.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline complete. Results:

---

## Exp-006 Scaled Formality (n=400) × Qwen3-32B

| Metric | n=400 | n=100 baseline |
|--------|-------|----------------|
| **NLI pass** | 355/400 (88.8%) | — |
| **Consistency** | 232/355 (65.4%) | — |
| **BT P(formal)** | **67.5% [63.7, 71.3]** | 66.5% [58.5, 73.9] |
| **CI width** | **7.6 pp** | 15.4 pp |
| **BT p-value** | 0.0001 | <0.0001 |

**Likert:**
- ATE = −0.059, p = 0.5999, Cohen's d = −0.025
- mean(formal) = 6.58, mean(casual) = 6.64
- tie rate = 43.4%

**Blindspot:** Yes (pairwise detects bias, Likert does not)

**GEE decomposition:**
- Style OR = 2.15 [1.46, 3.16], p < 0.0001
- Orig OR = 4.99 [3.40, 7.34], p < 0.0001

---

Key takeaways:
- **BT point estimate stable**: 67.5% vs 66.5% at n=100 — scaling to 4× samples moved the estimate by only 1pp.
- **CI halved**: 7.6pp vs 15.4pp — exactly the √4 improvement expected.
- **Blindspot confirmed at scale**: Likert ATE near zero (−0.059, p=0.60) while BT clearly significant (p=0.0001). The pairwise/Likert divergence is robust.
- **GEE**: Both Style (OR=2.15) and Orig (OR=4.99) effects highly significant. Original-response identity dominates, but formality style still independently doubles the odds of being preferred.

---

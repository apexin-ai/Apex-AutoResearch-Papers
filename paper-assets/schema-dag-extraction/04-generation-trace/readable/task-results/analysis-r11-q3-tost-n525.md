# analysis r11 q3 tost n525

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r11-q3-tost-n525_20260517T103242_result.json`
- **Structured JSON:** [`2a419cd260da021aa04f.json`](../../sessions/2a/2a419cd260da021aa04f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results written. Both linear and logit TOST remain **inconclusive** even with n=525:

| Scale | Interaction | SE | p (H0: =0) | TOST p | Conclusion |
|-------|------------|-----|-------------|--------|------------|
| Linear | -0.094 | 0.090 | 0.297 | 0.761 | inconclusive |
| Logit | -0.098 | 0.703 | 0.890 | 0.481 | inconclusive |

The interaction is non-significant in both scales (can't reject H0: coeff=0), but the SE is too large relative to the equivalence margins (3pp linear, 0.13 logit units) to demonstrate equivalence either. Back-transformed interaction at floor (47.7% accuracy): -2.4pp; at median (64.6%): -2.3pp.

Output saved to `artifacts/q3_tost_n525_results.json`.

---

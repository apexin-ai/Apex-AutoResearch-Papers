# Truncation Diagnosis: max_new_tokens=1536 vs 1024

**Experiment**: mvp2_eval_rsft_r2b_maxtok1536_r2  
**Date**: 2026-05-15  
**Conclusion**: **Negative** — truncation is NOT the primary cause of low EDCR

## Key Metrics

| Metric | RSFT r2b (1024) | RSFT r2b (1536) | Delta |
|--------|-----------------|-----------------|-------|
| rel_f1 | — | 0.4504 | — |
| evi_f1 | — | 0.8102 | — |
| **EDCR** | **0.6609** | **0.6740** | **+0.013** |
| Truncated | — | 146/985 (14.8%) | — |

SFT baseline for reference: rel_f1=0.4057, evi_f1=0.798

## Distractor Citation Analysis

- Total citations: 29,063
- Distractor citations: 19,589 (**67.4%**)
- Even with 50% more generation budget, the model still produces ~2/3 distractor citations

## Conclusion

EDCR improved only +0.013 (0.6609 → 0.6740), far below the 0.71+ threshold needed to confirm the truncation hypothesis. 146 documents still truncated at 1536 tokens, but the marginal EDCR gain indicates that even fully eliminating truncation would not meaningfully close the gap.

**Distractor citation is an inherent behavior of the RSFT r2b model**, not a truncation artifact. The model systematically over-generates evidence citations — 67.4% of all citations are distractors. This points to a training signal issue: the reward model or the RL objective does not sufficiently penalize spurious citations.
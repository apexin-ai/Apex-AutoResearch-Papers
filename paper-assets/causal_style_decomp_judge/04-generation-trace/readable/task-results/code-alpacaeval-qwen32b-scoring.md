# code alpacaeval qwen32b scoring

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_alpacaeval_qwen32b_scoring_20260521T074636_result.json`
- **Structured JSON:** [`f25cb36755c0375ce110.json`](../../sessions/f2/f25cb36755c0375ce110.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All scoring and analysis complete. Results:

```
## AlpacaEval × Qwen3-32B
Pairs: 86 (NLI≥0.90)
Consistency: 53/86 (61.6%)
BT: P(formal)=65.7% [58.1%, 73.3%], p=0.0001
Likert: ATE=0.151, p=0.1976, d=0.081, tie_rate=47.7%
  mean(formal)=6.87, mean(casual)=6.72
Blindspot: Yes
GEE: Style OR=1.99 [0.90, 4.42] p=0.0890, Orig OR=3.12 [1.41, 6.93] p=0.0050
```

Key observations:

- **BT confirms formality bias**: P(formal)=65.7% with tight CI above 50%, p=0.0001 — Qwen3-32B significantly prefers formal responses on AlpacaEval data
- **Likert insensitive**: ATE=0.151 is tiny, Cohen's d=0.081 (negligible), p=0.20 not significant, 47.7% ties — Likert scoring cannot detect the bias (blindspot confirmed)
- **GEE decomposition**: Style OR=1.99 (p=0.089, marginal) vs Orig OR=3.12 (p=0.005, significant) — originality confound is stronger than pure style effect on this dataset. The style effect trends formal but doesn't reach significance after controlling for originality
- **Consistency 61.6%** — lower than typical LLMBar (~70%+), likely because AlpacaEval pairs have subtler stylistic differences

Output files: `data/pairwise_results_alpacaeval_qwen32b.jsonl` (100 records) and `data/scored_alpacaeval_qwen32b.jsonl` (100 records).

---

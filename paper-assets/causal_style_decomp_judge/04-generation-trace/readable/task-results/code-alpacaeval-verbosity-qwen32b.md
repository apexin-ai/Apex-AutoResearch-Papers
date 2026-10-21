# code alpacaeval verbosity qwen32b

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_alpacaeval_verbosity_qwen32b_20260521T082429_result.json`
- **Structured JSON:** [`d528d1cfbdaf98ce7a24.json`](../../sessions/d5/d528d1cfbdaf98ce7a24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Here are the results:

## AlpacaEval Verbosity × Qwen3-32B
```
Data source: 新生成
Pairs: 82 (NLI≥0.90)
Consistency: 68/82 (82.9%)
BT: P(verbose)=84.1% [77.4%, 90.2%], p=0.0001
Likert: ATE=0.732, p=0.0003, d=0.375, tie_rate=24.4%
  mean(verbose)=7.32, mean(concise)=6.59
Blindspot: Yes
GEE: Style OR=28.64 [9.16, 89.56] p=< 0.0001, Orig OR=0.18 [0.06, 0.54] p=0.0024
```

Qwen3-32B exhibits a strong verbosity bias on AlpacaEval: 84.1% probability of preferring the verbose version (BT), with an ATE of +0.73 points on the Likert scale (d=0.375, medium effect). The GEE decomposition shows the style effect (OR=28.64) massively dominates the originality effect (OR=0.18), confirming the bias is driven by verbosity preference rather than content familiarity. The originality OR < 1 (p=0.0024) indicates a slight preference for counterfactual text over original, likely because verbose expansions appear more "complete."

---

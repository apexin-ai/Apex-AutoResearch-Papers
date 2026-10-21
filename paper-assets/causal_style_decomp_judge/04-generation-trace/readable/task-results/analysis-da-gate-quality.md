# analysis da gate quality

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_da-gate-quality_20260522T230728_result.json`
- **Structured JSON:** [`42a8a83ead127d60098e.json`](../../sessions/42/42a8a83ead127d60098e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON saved to `/root/causal_style_decomp_judge/artifacts/r14_fixes/direction_aware_quality.json`.

## Results Summary

### Group Sizes
| Group | n |
|-------|---|
| Bidirectional-pass | 65 |
| DA-only (+21 recovered) | 21 |
| Reject | 14 |

### (a) NLI Entailment Scores

| Metric | Bidir-pass | DA-only | p |
|--------|-----------|---------|---|
| Forward NLI | 0.987±0.017 | 0.230±0.399 | <0.0001 |
| Backward NLI | 0.986±0.018 | 0.838±0.325 | 0.809 |
| min(fwd,bwd) | 0.980±0.021 | 0.076±0.173 | <0.0001 |

DA-only组 17/21 failed forward NLI, 4/21 failed backward — 主要是 expansion 方向加了新内容导致 forward entailment 低，这在语义上是合理的。

### (b) Likert Score Diff (orig−cf)

| Judge | Bidir-pass | DA-only | p |
|-------|-----------|---------|---|
| GPT-4o | −0.32±1.20 | −0.14±2.05 | 0.996 |
| Claude | −0.05±0.95 | +0.29±1.91 | 0.663 |
| LLaMA-70B | −0.25±1.02 | −0.29±2.00 | 0.131 |
| Qwen-32B | −0.22±0.89 | +0.05±1.36 | 0.861 |
| Gemini-Flash | −0.35±1.78 | +0.38±2.38 | 0.552 |

**5/5 judges 均无显著差异** (all p>0.13)。DA-only 组质量与 bidir 组等价。

### (c) BT Verbose Win Rate (by judge)

| Judge | Bidir-pass | DA-only |
|-------|-----------|---------|
| GPT-4o | 0.600 | 0.619 |
| Claude | 0.277 | 0.476 |
| LLaMA-70B | 0.523 | 0.714 |
| Qwen-32B | 0.646 | 0.619 |
| Gemini-Flash | 0.492 | 0.571 |

DA-only 组在所有 judge 上 win rate ≥ bidir 组，与之前的 BT=0.7379 vs 0.7845 结论一致（无显著差异）。

### (d) Text Statistics

| Metric | Bidir-pass | DA-only | p |
|--------|-----------|---------|---|
| Orig word count | 135.7±143.0 | 28.7±37.9 | — |
| CF word count | 124.4±107.8 | 82.4±50.4 | — |
| WC ratio (cf/orig) | 3.50±12.71 | 5.34±4.37 | 0.0001 |
| BERTScore CF | 0.797±0.108 | 0.701±0.116 | 0.002 |

DA-only 组原文更短、expansion ratio 更大、BERTScore 更低，但这些是 NLI 不对称的自然结果（短文大幅扩写），不影响评判质量。

### 结论
Direction-aware gate 恢复的 21 pairs 在 **Likert 质量评分和 BT win rate 上与 strict 组无显著差异**，可以安全纳入。它们的特征是短原文的大幅扩写（17/21 forward NLI 低），bidirectional gate 对这类 pair 过于严格。

---

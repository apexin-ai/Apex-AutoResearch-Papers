# analysis cross axis contamination

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross-axis-contamination_20260522T094158_result.json`
- **Structured JSON:** [`f183211afee27072e492.json`](../../sessions/f1/f183211afee27072e492.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Cross-Axis Contamination Analysis

### Formality rewrites → Verbosity change
(n=355, all NLI≥0.90)

| Metric | Δ | Cohen's d | t | p |
|--------|---|-----------|---|---|
| Word count | -3.8 words (-3.4%) | -0.228 (small) | -4.295 | <0.0001 |
| Sentence count | -0.02 (-0.2%) | -0.025 (negligible) | -0.480 | 0.632 |
| Mean sent. length | -0.40 words | -0.161 (negligible) | -3.037 | 0.003 |

方向分解：formal→casual (n=268) Δwc=-6.2 (-5.0%, d=-0.35)；casual→formal (n=87) Δwc=+3.8 (+5.6%, d=0.51)。方向相反，句子数不变——词级调整（contractions/elaboration），非结构变化。

### Verbosity rewrites → Formality change
(n=86, all NLI≥0.90)

| Metric | Δ | Cohen's d | t | p |
|--------|---|-----------|---|---|
| Avg word length (chars) | +0.24 ± 0.61 | 0.388 (small) | 3.600 | 0.0005 |
| Type-token ratio (TTR) | -0.006 ± 0.18 | -0.035 (negligible) | -0.322 | 0.748 |
| Mean sent. length | +3.40 ± 9.68 | 0.351 (small) | 3.255 | 0.002 |
| Flesch-Kincaid grade | +2.26 ± 4.51 | 0.501 (medium) | 4.648 | <0.0001 |

方向分解：verbose→concise TTR d=+1.46（数学 artifact：短文本 TTR 天然更高），concise→verbose TTR d=-1.02（反向 artifact）。整体 TTR 抵消→negligible。

### Conclusion

Cross-axis contamination 在效应量层面 small-to-negligible。Formality→Verbosity 的 word count |d|=0.23（small），句子结构无变化。Verbosity→Formality 的 FK grade d=0.50 看似 medium，但 FK 是 sentence_length 和 word_length 的复合指标，sentence length 变化是 verbosity 操纵的固有结果而非独立 formality 污染。最纯净的词汇多样性 proxy（TTR）无污染（|d|=0.04）。结合 GEE originality 项对 rewriting artifact 的控制，axis isolation 可接受。

---

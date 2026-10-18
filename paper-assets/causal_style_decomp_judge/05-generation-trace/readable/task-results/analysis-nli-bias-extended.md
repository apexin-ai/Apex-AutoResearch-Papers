# analysis nli bias extended

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nli-bias-extended_20260522T224735_result.json`
- **Structured JSON:** [`703b481dc0f5ee194c5d.json`](../../sessions/70/703b481dc0f5ee194c5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Results:

## Results Summary

### Formality (88 pass / 12 reject) — No Bias Detected

| Dimension | Pass | Reject | Test | p-value |
|---|---|---|---|---|
| Topic distribution | — | — | χ²=4.06 | 0.541 |
| Token count | 104.7±128.2 | 101.7±174.2 | KS=0.269 | 0.366 |
| Avg sentence length | 13.1 | 13.5 | MWU | 0.614 |
| Sentence count | 7.7 | 5.8 | MWU | 0.163 |
| Dep tree depth | 4.59±1.71 | 5.10±2.55 | MWU | 0.637 |

All dimensions non-significant. NLI gate on formality data is unbiased across these axes.

### Verbosity (86 pass / 14 reject) — Significant Bias on Length

| Dimension | Pass | Reject | Test | p-value |
|---|---|---|---|---|
| Topic distribution | — | — | χ²=7.85 | 0.165 |
| **Token count** | **109.5±133.8** | **72.3±134.4** | **KS=0.503** | **0.003** |
| **Avg sentence length** | **13.8** | **9.0** | **MWU** | **0.006** |
| Sentence count | 7.8 | 5.4 | MWU | 0.050 |
| Dep tree depth | 4.73±1.68 | 4.21±2.58 | MWU | 0.110 |

Verbosity NLI gate shows **significant selection bias**: rejected samples are systematically shorter (72 vs 110 tokens, p=0.003) with shorter sentences (9.0 vs 13.8 words, p=0.006). This is expected — concise originals undergoing verbosity expansion produce CF texts that are structurally very different, making NLI entailment harder to satisfy.

### Scaled Formality (355 pass / 0 reject)

All 355 pairs pass NLI ≥ 0.90. No reject group to compare.

**Output**: `/root/causal_style_decomp_judge/artifacts/r14_fixes/nli_selection_bias_extended.json`

---

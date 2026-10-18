# ops tone pilot exp004

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_tone_pilot_exp004_20260520T224149_result.json`
- **Structured JSON:** [`615113a1291e7c184786.json`](../../sessions/61/615113a1291e7c184786.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Clear picture now. Let me compile the final report.

---

## exp-004 Tone Axis NLI Pilot — Results Report

### Execution Summary
- **Samples**: 20 (from mvp_samples.jsonl)
- **Model**: Qwen3-32B via vLLM
- **Detection split**: 13 assertive / 7 hedging
- **Verification**: BERTScore (deberta-xlarge-mnli, threshold 0.92) + NLI (nli-deberta-v3-large, threshold 0.90)

### Pass Rates

| Metric | CF (orig→counter) | DR (orig→double-rewrite) |
|--------|-------------------|--------------------------|
| NLI pass (≥0.90) | 65.0% (13/20) | 85.0% (17/20) |
| BERTScore pass (≥0.92) | 60.0% (12/20) | 55.0% (11/20) |
| **Both pass** | **45.0% (9/20)** | **55.0% (11/20)** |

### Score Distributions

| Metric | Mean | Std | Min | Max |
|--------|------|-----|-----|-----|
| bertscore_cf | 0.9201 | 0.0644 | 0.7891 | 0.9905 |
| bertscore_dr | 0.9164 | 0.0707 | 0.7587 | 1.0000 |
| nli_cf | 0.7039 | 0.4208 | 0.0001 | 0.9967 |
| nli_dr | 0.8841 | 0.3038 | 0.0024 | 0.9987 |

### By Detected Tone
- **Assertive (n=13)**: Both CF pass 38.5%, NLI CF mean 0.6559
- **Hedging (n=7)**: Both CF pass 57.1%, NLI CF mean 0.7930

### Threshold Sweep (CF)
NLI scores are bimodal (either >0.95 or <0.01) — lowering threshold from 0.90 to 0.80 gains nothing (still 65%). The bottleneck is BERTScore at 0.92.

Best relaxed config: NLI≥0.80 & BS≥0.88 → 60.0% (12/20), still below 80%.

### Failure Mode Analysis

1. **NLI catastrophic failure (6 records, NLI<0.60)**: Assertive→hedging rewrites change epistemic status of factual claims ("X happened" → "X may have happened"). The NLI model correctly identifies this as non-entailment. This is a **structural limitation**: the tone axis inherently modifies truth-commitment, unlike formality which only changes surface register.

2. **BERTScore-only failure (3 records, NLI>0.95 but BS<0.92)**: Short texts or list formats where hedging expansion changes token overlap substantially despite preserving meaning.

3. **Code content (mvp_0014)**: Tone rewriting wraps code in hedging prose, fundamentally changing content structure.

### Verdict: **FAIL** (45% < 80% threshold)

### Recommended Next Steps
1. **Direction-aware NLI for tone** (like verbosity axis): assertive→hedging should use forward-only NLI since hedging legitimately weakens entailment directionality
2. **Prompt refinement**: instruct model to hedge about *presentation* ("one approach is...") rather than hedging *factual claims* ("it may have happened")
3. **Exclude code-heavy samples** from tone axis or add code-detection filter
4. Re-pilot with fixes before extending to 100 samples

---

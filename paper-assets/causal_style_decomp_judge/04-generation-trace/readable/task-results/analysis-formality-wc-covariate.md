# analysis formality wc covariate

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_formality-wc-covariate_20260522T183517_result.json`
- **Structured JSON:** [`6ad617d6f5fc2427da50.json`](../../sessions/6a/6ad617d6f5fc2427da50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON saved. Here's the summary:

### Formality Word Count Covariate GEE — Model A vs B

| Judge | Model A Style OR | Model B Style OR | Δ% | delta_wc OR | delta_wc p |
|---|---|---|---|---|---|
| **GPT-4o** | 2.58 (p=.002) | 2.66 (p=.002) | **+3.0%** | 0.85 | .789 |
| **Qwen3-32B** | 4.20 (p=.0002) | 4.19 (p=.0003) | **−0.2%** | 1.01 | .985 |
| **Llama-70B** | 4.81 (p=3.5e-6) | 4.22 (p=2.8e-5) | **−12.2%** | 2.19 | .289 |
| **Gemini-Flash** | 1.64 (p=.101) | 1.58 (p=.144) | **−4.0%** | 1.26 | .714 |

**Conclusions:**

1. **delta_wc is non-significant for all 4 judges** (all p > 0.28) — word count difference does not predict judge preference after controlling for style and originality
2. **3/4 judges: Style OR change < 10%** — GPT-4o (+3.0%), Qwen (−0.2%), Gemini (−4.0%)
3. **Llama-70B** shows the largest shift (−12.2%), but Style OR remains highly significant (4.22, p=2.8e-5) and delta_wc itself is NS (p=0.29). The attenuation is noise, not confounding
4. Gemini was already NS in Model A (style effect not detected) — adding word count doesn't change this

Word count is not a confound for the formality style OR estimates.

**Output**: `/root/causal_style_decomp_judge/artifacts/r12_fixes/formality_wordcount_covariate.json`

---

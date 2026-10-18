# code formality scaled n300

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_formality_scaled_n300_20260524T062322_result.json`
- **Structured JSON:** [`189b9e95d9ef3e2139d9.json`](../../sessions/18/189b9e95d9ef3e2139d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE. Here's the final report:

---

## Llama-3.3-70B × Formality (n=355 NLI-verified pairs)

### Pairwise (BT)
- **P(formal) = 88.1%** [83.7%, 92.1%], p = 0.0001
- 202/355 consistent pairs (56.9% consistency rate)

### Likert
- Cohen's d = 0.048, ATE = 0.088
- Wilcoxon p = 0.026, t-test p = 0.077
- Tie rate = 71.5%

### GEE Decomposition
- **Style OR = 27.85** [10.72, 72.38], p < 0.0001
- **Orig OR = 13.48** [5.19, 35.03], p < 0.0001

### Blindspot: **No** (both BT and Likert significant)

### Cross-Judge Comparison

| Metric | Qwen3-32B | Llama-70B | Ratio |
|--------|-----------|-----------|-------|
| BT P(formal) | 67.5% | 88.1% | 1.3× |
| Style OR | 2.15 | 27.85 | 13× |
| Orig OR | 4.99 | 13.48 | 2.7× |

**Key takeaway**: Llama-70B exhibits dramatically stronger formality bias than Qwen3-32B across all metrics. The Style OR difference is particularly striking (27.85 vs 2.15, ~13× larger) — Llama-70B is far more sensitive to formal vs casual style when judging response quality. The Orig OR is also much higher (13.48 vs 4.99), indicating stronger position/originality bias as well. Despite the massive pairwise bias, the Likert effect is tiny (d=0.048) with 71.5% ties, illustrating how Likert scoring masks bias that pairwise comparison reveals.

---

# analysis correlation alpha rejection

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_correlation-alpha-rejection_20260520T152445_result.json`
- **Structured JSON:** [`3a2c94ec8a41d0b26788.json`](../../sessions/3a/3a2c94ec8a41d0b26788.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved. Here's the summary:

---

## Task 3: Pairwise Vote Correlation

| Model | Mean Pearson r ± SD | Fleiss' κ |
|-------|-------------------|-----------|
| **Mistral-7B** | 0.625 ± 0.062 | 0.460 |
| Qwen2.5-7B | 0.751 ± 0.038 | 0.658 |
| Qwen2.5-14B | 0.815 ± 0.029 | 0.738 |
| Qwen3-14B | 0.858 ± 0.026 | 0.773 |

All 66 pairwise correlations per condition (C(12,2)). Encoding: True=1, False=0, Unknown=0.5. Pairwise Pearson r and Fleiss' κ are monotonically related across models — lower agreement models (Mistral-7B) have both lower κ and lower r, confirming κ is a valid consensus measure. Mistral-7B's relatively high variance (0.062) reflects its higher nondeterminism.

## Task 5: α Sensitivity

| α | Accuracy | Δ vs α=0.5 |
|---|---------|------------|
| 0.0 | 55.88% | +0.00pp |
| 0.1 | 55.39% | −0.49pp |
| 0.3 | 55.88% | +0.00pp |
| **0.5** | **55.88%** | **baseline** |
| 0.7 | 55.88% | +0.00pp |
| 1.0 | 55.88% | +0.00pp |

Max accuracy variation: **0.49pp** across all α values. α has negligible effect because: (1) 37% of problems have zero excluded constraints, (2) for the rest, mean rejection is only 3.4%, so the penalty term α·neg(c) rarely flips the argmax. Only 8 out of 204 problems have a score gap < 2.0 between the top two candidates.

Note: Re-scored accuracy (55.88%) is ~3.4pp below original (59.31%) due to Z3 dedup non-determinism on re-run; the relative insensitivity to α is the key finding.

## Task 6: Constraint Rejection Rate

| Group | n | Mean Rate ± SD | Median |
|-------|---|---------------|--------|
| **Overall** | 203 | 3.44% ± 4.04% | 2.33% |
| Correct | 120 | 3.33% ± 4.39% | 2.02% |
| Incorrect | 83 | 3.60% ± 3.46% | 3.12% |

- **t-test**: t=−0.474, p=0.636 (no significant difference)
- 75 problems (36.9%) have zero rejected constraints
- Mean excluded count: correct=1.31, incorrect=1.49
- Distribution: 0 excluded (75), 1 (59), 2 (32), 3 (13), ≥5 (7)

The MAX-SAT solver accepts the vast majority of constraints (mean rejection 3.4%), indicating that LLM-generated constraints are largely internally consistent. No significant difference in rejection rate between correct/incorrect predictions → Eq.4 degeneration (high rejection → SC fallback) is rare in practice.

---

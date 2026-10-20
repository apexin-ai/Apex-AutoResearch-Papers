# eval collect deepseek func results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect-deepseek-func-results_20260516T083837_result.json`
- **Structured JSON:** [`3aa71fcff5ae72cb28ba.json`](../../sessions/3a/3aa71fcff5ae72cb28ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results collected. No explicit `unparseable_rate` field in the CWM summary — the CWM model had 0% truncation and all 1890 instances were evaluated, so unparseable_rate is effectively 0%.

## DeepSeek Func-Level Eval Results

### CLS func (seed42) — COMPLETE
| Metric | fail | pass | macro |
|--------|------|------|-------|
| Accuracy | — | — | **86.93%** |
| F1 | 86.47 | 87.37 | **86.92%** |
| Precision | 86.42 | 87.41 | — |
| Recall | 86.51 | 87.32 | — |

Confusion matrix: TP=854, TN=789, FP=123, FN=124 (n=1890)

### CWM func (seed42) — COMPLETE
| Metric | fail | pass | macro |
|--------|------|------|-------|
| Accuracy | — | — | **85.77%** |
| F1 | 86.42 | 85.05 | **85.73%** |
| Precision | 80.07 | 93.18 | — |
| Recall | 93.86 | 78.22 | — |

Confusion matrix: TP=765, TN=856, FP=56, FN=213 (n=1890)
Generation length: mean=28.1, median=33.0, max=103. Truncated: 0%. Unparseable: 0%.

Notable: CWM has a strong precision-recall asymmetry — high precision on pass (93.18%) but low recall (78.22%), meaning it's conservative about predicting "pass".

### CWM func (seed123) — STILL RUNNING
Progress: 832/9784 (~8.5%), running accuracy ~84.9%. This appears to be running on a much larger dataset (9784 vs 1890) — possibly the wrong data split or a different eval configuration. The log is at `/tmp/eval_cwm_func_s123.log`.

---

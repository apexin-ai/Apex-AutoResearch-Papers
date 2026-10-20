# analysis alt classifier

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alt-classifier_20260515T093824_result.json`
- **Structured JSON:** [`156344cc00f375ded5bf.json`](../../sessions/15/156344cc00f375ded5bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Results:

| Classifier | LOGO F1 (avg) | olmo-2-1b | pythia-1b | pythia-2.8b | qwen3-0.6b | qwen3-1.7b | qwen3-8b |
|---|---|---|---|---|---|---|---|
| XGBoost | **0.7893** | 0.764 | 0.856 | 0.804 | 0.824 | 0.805 | 0.683 |
| RandomForest | **0.7897** | 0.764 | 0.856 | 0.804 | 0.825 | 0.807 | 0.684 |
| LogisticRegression | **0.7253** | 0.719 | 0.781 | 0.740 | 0.745 | 0.743 | 0.624 |

- XGBoost baseline: 0.7893, matches registry 0.789
- RandomForest nearly identical to XGBoost (0.7897)
- LogisticRegression lower (0.725) but still well above chance (0.33), with identical per-generator ranking

Results saved to `/root/gen-depth-fingerprint/results/alt_classifier_results.json`. LaTeX appendix written to `appendix_classifier.tex` and `\input` added to `main.tex` after the confusion matrix section.

---

# analysis corpus prevalence

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_corpus-prevalence_20260517T231957_result.json`
- **Structured JSON:** [`372bcf0c156bb3b4cb7b.json`](../../sessions/37/372bcf0c156bb3b4cb7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Task complete. Summary:

**Corpus Prevalence Estimation Results:**

| True depth-2+ % | Predicted (EMQ) | |Error| | 95% CI |
| --- | --- | --- | --- |
| 0% | 2.3% | 2.34pp | [1.0%, 4.1%] |
| 25% | 27.1% | 8.87pp | [23.7%, 30.7%] |
| 50% | 49.7% | 11.70pp | [45.8%, 53.7%] |
| 75% | 71.2% | 13.20pp | [67.0%, 75.3%] |
| 100% | 88.8% | 11.16pp | [85.9%, 91.6%] |

**MAE = 9.45pp** (best method: EMQ)

**Conclusion: not viable** for corpus-level auditing in the strict LOGO setting (MAE >= 5pp). The bottleneck is cross-generator domain shift. For in-distribution generators (pythia-2.8b, olmo-2-1b), MAE drops to ~1-3.5pp, confirming the method works when domain shift is small.

Outputs:
- `results/corpus_prevalence_calibration.pdf` (3-panel plot: CC vs ACC vs EMQ)
- `results/corpus_prevalence_demo.json`
- Local artifact: `artifacts/_project/analysis/corpus_prevalence_demo.md`

---

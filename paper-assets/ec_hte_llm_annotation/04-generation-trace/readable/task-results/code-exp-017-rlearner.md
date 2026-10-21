# code exp 017 rlearner

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-017-rlearner_20260521T134257_result.json`
- **Structured JSON:** [`b675b7e06f448865f50d.json`](../../sessions/b6/b675b7e06f448865f50d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-017 complete. Registry updated to DONE/success.

**Results summary** — R-learner and CausalForest show near-identical patterns:

| Estimator | Method | Avg |Bias| | RMSE | Coverage |
|-----------|--------|---------|------|----------|
| CausalForest | naive | 0.1245 | 0.1432 | 0.46 |
| CausalForest | global | 0.1036 | 0.1287 | 0.65 |
| CausalForest | ec_hte | 0.0078 | 0.0817 | 0.91 |
| R-learner | naive | 0.1210 | 0.1390 | 0.47 |
| R-learner | global | 0.0979 | 0.1234 | 0.71 |
| R-learner | ec_hte | 0.0128 | 0.0800 | 0.92 |
| R-learner | oracle | 0.0063 | 0.0559 | 0.94 |

EC-HTE correction generalizes across CATE estimators — ec_hte_rlearner achieves bias 0.013 (vs naive 0.121), closely matching CausalForest's 0.008, with 92% coverage.

---

# analysis qwen14b bce30 s42 eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen14b_bce30_s42_eval_20260517T224156_result.json`
- **Structured JSON:** [`74aa821435ea2dc54543.json`](../../sessions/74/74aa821435ea2dc54543.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Results summary:

## BCE 30% Metrics (qwen14b_bce30_s42_eval)

| Metric | BCE 30% | KL 30% | Dense | vs Dense | vs KL |
|---|---|---|---|---|---|
| WikiText-2 PPL | **8.7634** | 7.6232 | 5.1854 | +69.0% | +15.0% (worse) |
| ARC-C (acc_norm) | **0.5759** | 0.5717 | 0.6758 | -14.8% | +0.4pp (better) |
| WinoGrande (acc) | **0.7261** | 0.7206 | 0.8106 | -10.4% | +0.6pp (better) |
| MMLU (acc) | **0.7167** | 0.6372 | 0.7977 | -10.2% | **+7.9pp (better)** |
| GSM8K (exact_match) | **0.5307** | 0.4882 | 0.8757 | -39.4% | **+4.3pp (better)** |

## Conclusion: **negative** (refutes hypothesis)

Hypothesis was that BCE should perform worse than KL on downstream tasks. Reality:

- **PPL: BCE worse** (8.76 vs 7.62), consistent with BCE's weaker language modeling objective
- **Downstream: BCE uniformly better**, especially MMLU (+7.9pp) and GSM8K (+4.3pp)

BCE trades off perplexity for better downstream task retention. The PPL gap (15%) does not translate into downstream degradation; instead BCE preserves task-relevant features better than KL despite higher PPL. This is a meaningful finding: **PPL is not a reliable proxy for downstream quality in sparsity predictors**.

---

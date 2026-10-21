# experiment push b stronger nli

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_push-b-stronger-nli_20260520T185557_result.json`
- **Structured JSON:** [`7da10bbad871cd02243f.json`](../../sessions/7d/7da10bbad871cd02243f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Push B experiment completed successfully. Here are the results:

## Push B Results: DeBERTa-v3-large NLI Verifier

**Model**: `MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli`  
**Inference**: 600 problems in 2.7s on cuda:0

### Standalone NLI Accuracy
| Class | Correct/Total | Accuracy | Precision | Recall |
|-------|--------------|----------|-----------|--------|
| True | 85/200 | 42.50% | 51.20% | 42.50% |
| False | 123/200 | 61.50% | 43.31% | 61.50% |
| Unknown | 63/200 | 31.50% | 42.00% | 31.50% |
| **Overall** | **271/600** | **45.17%** | — | — |

vs. deberta-base-mnli: 36.17% → **+9.00pp improvement** from scaling up the NLI model.

Pred distribution skews toward False (284 vs 200 ground truth).

### Combo with Mistral-7B SC (baseline 39.00%)
| Weight | Accuracy | Delta | McNemar p |
|--------|----------|-------|-----------|
| w=1 | 39.17% | +0.17pp | 1.0000 |
| w=3 | 40.67% | +1.67pp | 0.6058 |
| w=5 | 43.83% | +4.83pp | 0.1087 |

Trending positive but none statistically significant.

### Combo with Qwen3-14B SC (baseline 85.83%)
| Weight | Accuracy | Delta | McNemar p |
|--------|----------|-------|-----------|
| w=1 | 85.17% | -0.67pp | 0.8013 |
| w=3 | 85.33% | -0.50pp | 0.8672 |
| w=5 | 85.17% | -0.67pp | 0.8040 |

NLI combo slightly hurts Qwen3, though not significantly. The strong Qwen3 SC baseline leaves no room for a 45% standalone verifier to help.

**Key takeaway**: Even with a much stronger NLI model (45.17% vs 36.17%), standalone NLI accuracy on ProofWriter remains well below the LLM SC baselines, and combo gains are not statistically significant. The NLI verifier signal is too weak to meaningfully improve already-decent generators.

---

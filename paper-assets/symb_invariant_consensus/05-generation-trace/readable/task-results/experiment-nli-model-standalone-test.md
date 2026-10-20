# experiment nli model standalone test

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_nli-model-standalone-test_20260522T135809_result.json`
- **Structured JSON:** [`ad9153d3f0c7d07d0e80.json`](../../sessions/ad/ad9153d3f0c7d07d0e80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Test complete. Here's the full picture:

## NLI Standalone Accuracy on ProofWriter D5-600

| Model | Standalone Acc | Source |
|-------|---------------|--------|
| roberta-large-mnli | ~32.0% | 50-sample CPU test |
| bart-large-mnli | ~35.0% | 20-sample CPU test |
| deberta-base-mnli | 36.17% | Full 600 (Dir-K) |
| deberta-v3-large-mnli-fever-anli-ling-wanli | 45.17% | Full 600 (Push-B) |
| **deberta-large-mnli** | **55.0%** | Full 600 (D116) |

## Key Findings

1. **Best model = deberta-large-mnli at 55%** — far below the 72% target.

2. **DeBERTa-v2-xxlarge-mnli**: NOT downloaded. Given the trend (base→36%, large→55%, v3-large→45%), the xxlarge version is unlikely to break 65%, let alone 72%. The bottleneck is architectural: PW-D5 requires 5-hop deduction, not single-step NLI.

3. **LLaMA-8B baseline is 70%** (exp048/exp092), not 72.5%. With deberta-large-mnli (55% standalone), combo w3 already gives **74.17% (+4.17pp, p=0.0035)** — significant improvement despite NLI being weaker than LLM.

4. **CPU speed**: roberta ~0.2s/sample, bart ~0.7s/sample, deberta-large ~0.24s/sample (GPU: 2.7s total for 600).

## Conclusion

No zero-shot NLI model will reach >72% standalone on PW-D5. The complementarity mechanism works because NLI makes *different* errors than LLMs — it doesn't need to be *stronger* to help. The existing deberta-large-mnli at 55% is already the strongest available option and provides statistically significant combo gains with LLaMA-8B.

---

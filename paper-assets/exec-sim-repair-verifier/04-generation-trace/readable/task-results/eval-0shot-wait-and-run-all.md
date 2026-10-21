# eval 0shot wait and run all

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_0shot-wait-and-run-all_20260517T234112_result.json`
- **Structured JSON:** [`6cc4fd208df6ced37f97.json`](../../sessions/6c/6cc4fd208df6ced37f97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 tasks complete.

```
=== FINAL RESULTS ===

Task 1 - DeepSeek 0-shot repo-level:
  accuracy=48.54%, pass_f1=64.70%, fail_f1=5.09%, unparseable=8.70% (851/9784)
  confusion: TP=4614, FP=2511, TN=135, FN=2524
  runtime: 1545s

Task 2 - Qwen3-8B 0-shot func-level:
  accuracy=68.73%, pass_f1=65.50%, fail_f1=71.41%, unparseable=0.32% (6/1890)
  confusion: TP=561, FP=174, TN=738, FN=417
  runtime: 96s

Task 3 - DeepSeek 0-shot func-level:
  accuracy=63.02%, pass_f1=71.96%, fail_f1=45.69%, unparseable=1.06% (20/1890)
  confusion: TP=897, FP=618, TN=294, FN=81
  runtime: 113s
```

Key observations:
- Func-level is dramatically easier than repo-level (both models jump from ~48% to 63-69% accuracy)
- Qwen3-8B outperforms DeepSeek on func-level accuracy (68.7% vs 63.0%) with much more balanced F1 scores
- DeepSeek on repo-level has near-zero fail_f1 (5.09%) indicating it almost always predicts "pass" (heavy label bias)
- DeepSeek on func-level has the opposite pattern: high pass_f1 but low fail_f1 with massive FP (618), still biased toward "pass"
- Qwen3-8B is much better calibrated on func-level with balanced TP/TN

---

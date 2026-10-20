# train plan014 complete

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan014-complete_20260518T020203_result.json`
- **Structured JSON:** [`b865a2a23668cff7c1af.json`](../../sessions/b8/b865a2a23668cff7c1af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**plan_014 is already complete.** The run log shows all four conditions ran through DeBERTa training, GRU training, and eval successfully. The results file `results/plan_014_lambda_ablation.json` has complete entries for all four lambda values.

Summary of existing results:

| Lambda | DeBERTa Persuasion Acc | DeBERTa Intent Acc | Treatment F1 (all K) |
|--------|----------------------|-------------------|---------------------|
| 0      | 0.8439               | 0.4014            | 1.0                 |
| 0.5    | 0.8353               | 1.0               | 1.0                 |
| 1.0    | 0.8285               | 1.0               | 1.0 (plan_002)      |
| 2.0    | 0.8508               | 1.0               | 1.0                 |

Key observations:
- Lambda=0 (no intent loss): intent accuracy collapses to 0.40 (near random) as expected, but persuasion acc is slightly higher (0.844 vs 0.829 for lambda=1.0)
- All treatment F1 scores are 1.0 at every K value, consistent with plan_002 baseline
- The downstream jailbreak detection task is insensitive to lambda, while lambda=0 clearly degrades intent classification

The reviewer's assessment that eval was missing appears to have been based on checking before the run completed. All checkpoints exist, all evals ran, and results are saved. No additional work is needed.

One note: the current results file doesn't include `fpr_at_95tpr` or baseline/tfidf comparisons (which `eval_early_detection.py` computes). Want me to re-run the full eval script to get those metrics, or is the current file sufficient?

---

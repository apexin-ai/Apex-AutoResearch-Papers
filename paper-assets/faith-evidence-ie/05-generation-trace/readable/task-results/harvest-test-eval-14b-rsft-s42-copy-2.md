# harvest test eval 14b rsft s42

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_test_eval_14b_rsft_s42_20260521T154912_result.json`
- **Structured JSON:** [`9115fbd946d01f9dedc1.json`](../../sessions/91/9115fbd946d01f9dedc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
test_eval_14b_rsft_s42:
  pid_alive: false (DEAD)
  completed: true (EXIT_CODE=0)
  runtime: 19085.8s (~5h18m)
  metrics:
    f1: 0.3849
    ign_f1: 0.3849 (= f1, no train_annotated.json)
    precision: 0.4805
    recall: 0.3210
    evi_f1_joint (DREEAM): 0.2688
    evi_f1_tp: 0.6025
    edcr: 0.7865
    truncated: 67/500
    format_ok: 499/500
    field_compliance: 0.36 (known evaluator bug)
    n_predictions: 15835
  codalab_submission: exists (579KB, 11235 converted, 225 skipped_rel, 349 skipped_entity)
  log_status: clean exit, EXIT_CODE=0

Other test evals:
  test_eval_llama (PID 98968, cuda:2): ALIVE
  test_eval_1_7b (PID 102815, cuda:3): ALIVE
```

14B RSFT F1=0.3849，比 8B 的 0.3353 高 +5.0 pp。需要 CodaLab 提交获取真实 ign_f1。

---

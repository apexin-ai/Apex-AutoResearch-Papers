# harvest test eval 14b rsft s42

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_test_eval_14b_rsft_s42_20260521T155025_result.json`
- **Structured JSON:** [`37954668a91fc5682a97.json`](../../sessions/37/37954668a91fc5682a97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
test_eval_14b_rsft_s42:
  pid_alive: false
  completed: true
  metrics:
    ign_f1:      0.3849
    f1:          0.3849
    precision:   0.4805
    recall:      0.3210
    evi_f1_joint (DREEAM): 0.2688
    evi_f1_tp:   0.6025
    edcr:        0.7865
    truncated:   67/500
    format_ok:   499/500
    field_compliance: 0.36 (180/500)
    n_predictions: 15835
  codalab_json: exists (11235 converted, 225 skipped rel, 349 skipped entity)
  inference_time: 5h18m (38.17 s/doc)

Other test evals:
  llama (PID 98968): ALIVE
  1.7b (PID 102815): ALIVE
```

field_compliance 只有 36%（180/500），比 8B 的 14.8% 好但仍然很低——64% 的文档 evidence 字段不完整。ign_f1=f1 因为 test split 没有 train_annotated.json 做 ignore 过滤。

---

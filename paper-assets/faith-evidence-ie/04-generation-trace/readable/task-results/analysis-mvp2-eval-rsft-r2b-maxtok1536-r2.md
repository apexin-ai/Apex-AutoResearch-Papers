# analysis mvp2 eval rsft r2b maxtok1536 r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp2_eval_rsft_r2b_maxtok1536_r2_20260515T145704_result.json`
- **Structured JSON:** [`d5e73d1e002072fc66f5.json`](../../sessions/d5/d5e73d1e002072fc66f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

metrics.json 中没有 evi_f1_joint 字段，该指标未在本次 eval 中计算。

```
METRICS_START
rel_f1: 0.4504
ign_f1: 0.4504
precision: 0.4488
recall: 0.4519
evi_f1: 0.8102
evi_precision: 0.8162
evi_recall: 0.8044
evi_f1_joint: N/A
evi_f1_joint_P: N/A
evi_f1_joint_R: N/A
edcr: 0.6740
pred_count: 17188
format_ok: 983/985
truncated: 146/985
inference_time_s: 10676.8
METRICS_END

CONCLUSION: negative
ANALYSIS: max_new_tokens 1536 vs 1024，truncated 从 179→146（减少 33 篇），EDCR 从 0.6609→0.6740（+0.0131），提升不显著（远未达到 0.71+）。rel_f1（0.4493→0.4504）和 evi_f1（0.8128→0.8102）基本持平。截断只是 EDCR 偏低的次要因素，distractor citation 是模型的真实行为而非截断伪影。
```

---

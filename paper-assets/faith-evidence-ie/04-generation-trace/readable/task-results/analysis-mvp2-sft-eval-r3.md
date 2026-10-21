# analysis mvp2 sft eval r3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp2_sft_eval_r3_20260514T164305_result.json`
- **Structured JSON:** [`de5b1684dac930c4c91a.json`](../../sessions/de/de5b1684dac930c4c91a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
METRICS:
rel_f1: 0.4057
ign_f1: 0.4057
evi_f1: 0.7979
edcr: 0.7118
precision: 0.4043
recall: 0.4070
evi_precision: 0.8035
evi_recall: 0.7924
format_ok_rate: 0.998
format_compliance_rate: 0.626
n_parseable: 983
n_truncated: 367
n_predictions: 18815
inference_time_seconds: 6450.6

COMPARISON WITH R2:
rel_f1:                 r2=0.4057  r3=0.4057  Δ=0.0000 ✓
ign_f1:                 r2=0.4057  r3=0.4057  Δ=0.0000 ✓
evi_f1:                 r2=0.7979  r3=0.7979  Δ=0.0000 ✓
edcr:                   r2=0.7118  r3=0.7118  Δ=0.0000 ✓
precision:              r2=0.4043  r3=0.4043  Δ=0.0000 ✓
recall:                 r2=0.4070  r3=0.4070  Δ=0.0000 ✓
evi_precision:          r2=0.8035  r3=0.8035  Δ=0.0000 ✓
evi_recall:             r2=0.7924  r3=0.7924  Δ=0.0000 ✓
format_ok_rate:         r2=0.998   r3=0.998   Δ=0.000  ✓
format_compliance_rate: r2=0.626   r3=0.626   Δ=0.000  ✓
n_truncated:            r2=367     r3=367     Δ=0      ✓
n_predictions:          r2=18815   r3=18815   Δ=0      ✓
inference_time_seconds: r2=6484.7  r3=6450.6  Δ=-34.1  ✓ (噪声范围)

n_parseable:            r2=617     r3=983     ← 定义变更（见下）

CONCLUSION:
所有核心指标（rel_f1, ign_f1, evi_f1, edcr, precision, recall, evi_precision, evi_recall）与 r2 完全一致，到小数点后四位无差异。格式指标和预测数量也完全匹配。推理时间差 34s 属正常波动。

n_parseable 差异的原因：r3 的 metrics.json 区分了 n_parseable（983，JSON 可解析）和 n_field_complete（617，字段完整），r2 报的 n_parseable=617 实际对应 r3 的 n_field_complete。不是计算差异，是字段命名细化。

**结论：r3 与 r2 结果完全一致，统一 eval 代码未引入任何差异。r3 结果可信，可作为 SFT baseline 的正式评估数据。**
```

---

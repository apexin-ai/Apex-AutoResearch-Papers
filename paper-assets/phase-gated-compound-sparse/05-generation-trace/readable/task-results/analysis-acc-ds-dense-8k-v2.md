# analysis acc ds dense 8k v2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_acc_ds_dense_8k_v2_20260515T231852_result.json`
- **Structured JSON:** [`fbb38f83c143308354eb.json`](../../sessions/fb/fbb38f83c143308354eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 实验 1: acc_ds_dense_8k_v2

```
exp_id: acc_ds_dense_8k_v2
status: success
metrics:
  accuracy: 0.74
  correct: 37
  total: 50
  truncated_count: 8
  truncated_rate: 0.16
  null_count: 10
  extraction_failure_count: 2 (null但未截断)
  total_time_seconds: 2882
  delta_vs_baseline: +0.22 (vs 4096版 dense 0.52)
notes: 8k tokens显著提升accuracy (+22pp)。8个截断样本全部预测为null，说明4096版大量错误来自截断。仍有2个extraction failure（非截断但无法提取答案）。
```

## 实验 2: acc_qw_s025_n100_b2_fix

```
exp_id: acc_qw_s025_n100_b2_fix
status: success
metrics:
  accuracy: 0.34
  correct: 17
  total: 50
  truncated_count: 3
  truncated_rate: 0.06
  null_count: 9
  extraction_failure_count: 6 (null但未截断)
  total_time_seconds: 1099
  delta_vs_original_batch2: 0.00 (原batch2也是0.34)
  combined_accuracy: 0.33 (batch1=16/50 + batch2_fix=17/50 = 33/100)
notes: 重跑结果与原batch2一致(0.34)。截断率很低(6%)，主要问题是extraction failure(6个)和答案错误(24个)。sparse s025对QW模型的accuracy损伤稳定在~0.33。
```

## 关键对比

| 指标 | DS dense 4k | DS dense 8k | QW s025 combined |
|------|------------|------------|-----------------|
| accuracy | 0.52 | **0.74** | 0.33 |
| truncated_rate | (高) | 0.16 | 0.06 |

- DS dense 从 4k→8k 提升 22pp，说明 4k 版大量截断导致的低估严重
- QW s025 重跑稳定在 0.33-0.34，与 dense baseline (DS 0.74) 相比 accuracy 损失约 41pp（不过注意这是不同模型，QW dense baseline 需另行确认）

---

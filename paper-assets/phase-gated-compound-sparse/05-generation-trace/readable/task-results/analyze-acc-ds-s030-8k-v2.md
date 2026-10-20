# analyze acc ds s030 8k v2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_acc_ds_s030_8k_v2_20260516T013201_result.json`
- **Structured JSON:** [`d0424cd0a61eead602aa.json`](../../sessions/d0/d0424cd0a61eead602aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成全部 50/50 problems。以下是完整 metrics：

## 最终 Metrics

```json
{
  "accuracy": 0.04,
  "correct": 2,
  "total": 50,
  "truncation_rate": 0.78,
  "truncated_count": 39,
  "non_truncated_total": 11,
  "non_truncated_correct": 2,
  "non_truncated_accuracy": 0.182,
  "null_count": 41,
  "avg_tokens": 6566.3,
  "max_new_tokens": 8192,
  "total_time_seconds": 7095.1
}
```

## 结论：**negative**

## DS 8k v2 系列对比

| condition | accuracy | correct | trunc_rate | null_count | non_trunc_acc |
|-----------|----------|---------|------------|------------|---------------|
| dense     | 0.74     | 37/50   | 0.16       | -          | -             |
| s015      | 0.48     | 24/50   | 0.32       | -          | 0.706         |
| s020      | 0.30     | 15/50   | 0.58       | -          | 0.714         |
| s025      | 0.08     | 4/50    | 0.76       | 36         | -             |
| **s030**  | **0.04** | **2/50**| **0.78**   | **41**     | **0.182**     |

关键观察：
- s030 是系列最差，accuracy 仅 4%，比 s025 (8%) 进一步下降
- 78% 截断率（39/50 达到 8192 上限），与 s025 的 76% 接近，说明在这个 sparsity 附近截断率已趋于饱和
- 41/50 输出为 null（无法提取答案），即使在非截断的 11 个样本中也只有 2 个正确（non_trunc_acc=18.2%），远低于 s015/s020 的 ~71%
- s030 的 non_truncated_accuracy 断崖式下降表明：在这个 sparsity 下，模型不仅被截断，连能完成推理的样本质量也严重退化
- heads_pruned=224（全部 28×8=224 个 attention head 都被剪枝），KV eviction ~30%，剪枝过于激进导致推理能力崩溃
- 无错误或异常退出，EXIT_CODE=0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "accuracy": 0.04,
    "correct": 2,
    "total": 50,
    "truncation_rate": 0.78,
    "truncated_count": 39,
    "non_truncated_total": 11,
    "non_truncated_correct": 2,
    "non_truncated_accuracy": 0.182,
    "null_count": 41,
    "avg_tokens": 6566.3,
    "max_new_tokens": 8192,
    "total_time_seconds": 7095.1
  }
}
```

</details>

---

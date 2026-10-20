# analysis acc ds s025 8k v2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_acc_ds_s025_8k_v2_20260516T001835_result.json`
- **Structured JSON:** [`91be45c0cff68fe64f6e.json`](../../sessions/91/91be45c0cff68fe64f6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```json
{
  "conclusion": "negative",
  "metrics": {
    "accuracy": 0.08,
    "correct": 4,
    "total": 50,
    "truncated_count": 38,
    "truncated_rate": 0.76,
    "avg_tokens": 6343.8,
    "max_new_tokens": 8192,
    "total_time_seconds": 6827.8,
    "null_count": 36
  },
  "analysis": "8k 版本与 4096 版本结果完全一致：accuracy=0.08, truncation_rate=76%。增加 token 上限未带来任何改善。38/50 问题生成满 8192 tokens 仍无法得出答案（36 个 pred=null），说明 s025 稀疏度下模型进入退化循环，不是 token 预算不够的问题，而是推理能力根本性损坏。对比基线：dense 8k_v2 accuracy=0.74/trunc=16%，s020 8k_v2 accuracy=0.30/trunc=58%，s025 从 0.74→0.08 的断崖式下降表明 25% 稀疏度已超过该模型的可用阈值。"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "conclusion": "negative",
    "metrics": {
      "accuracy": 0.08,
      "correct": 4,
      "total": 50,
      "truncated_count": 38,
      "truncated_rate": 0.76,
      "avg_tokens": 6343.8,
      "max_new_tokens": 8192,
      "total_time_seconds": 6827.8,
      "null_count": 36
    },
    "analysis": "8k 版本与 4096 版本结果完全一致：accuracy=0.08, truncation_rate=76%。增加 token 上限未带来任何改善。38/50 问题生成满 8192 tokens 仍无法得出答案（36 个 pred=null），说明 s025 稀疏度下模型进入退化循环，不是 token 预算不够的问题，而是推理能力根本性损坏。对比基线：dense 8k_v2 accuracy=0.74/trunc=16%，s020 8k_v2 accuracy=0.30/trunc=58%，s025 从 0.74→0.08 的断崖式下降表明 25% 稀疏度已超过该模型的可用阈值。"
  }
}
```

</details>

---

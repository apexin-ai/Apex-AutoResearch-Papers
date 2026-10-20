# data human prep

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_human-prep_20260513T182510_result.json`
- **Structured JSON:** [`0c0e5aa241c5ed23d886.json`](../../sessions/0c/0c0e5aa241c5ed23d886.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

FineWeb 人类数据准备完成。结果汇总：

| Split | 文档数 | 大小 | ~Tokens |
|-------|--------|------|---------|
| train.jsonl | 164,889 | 545M | ~120M |
| detector.jsonl | 67,960 | 227M | ~50M |
| eval_holdout.jsonl | 67,823 | 227M | ~50M |
| **总计** | **300,672** | **999M** | **~220M** |

每条记录格式为 `{"text": "...", "depth": 0, "source": "fineweb"}`，符合 MVP pipeline 要求。数据来源为 FineWeb sample-10BT 的 CC-MAIN-2024-10 子集。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "text": "...",
    "depth": 0,
    "source": "fineweb"
  }
}
```

</details>

---

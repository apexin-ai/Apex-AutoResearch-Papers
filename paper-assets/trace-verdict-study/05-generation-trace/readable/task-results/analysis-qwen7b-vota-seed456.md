# analysis qwen7b vota seed456

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen7b_vota_seed456_20260519T090457_result.json`
- **Structured JSON:** [`98bc44a30ddc40c5aade.json`](../../sessions/98/98bc44a30ddc40c5aade.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。汇总如下：

```json
{
  "experiment": "qwen7b_vota_seed456",
  "metrics": {
    "accuracy": 0.9908,
    "accuracy_ci": [0.9849, 0.9958],
    "majority_baseline": 0.7151,
    "lift": "+27.56pp",
    "n": 1190,
    "pass":  {"precision": 1.00, "recall": 0.987, "f1": 0.994},
    "fail":  {"precision": 0.969, "recall": 1.00, "f1": 0.984},
    "train_loss": 0.04969,
    "eval_loss": 0.08312
  }
}
```

**三 seed 对比（VOTA 条件，Qwen-7B）：**

| Seed | Accuracy | 95% CI |
|------|----------|--------|
| 42   | 95.63%   | — |
| 123  | 98.66%   | — |
| **456** | **99.08%** | [98.49%, 99.58%] |

三个 seed 均远超原始 hypothesis 的 84-92% 范围。seed 间方差较小（95.63%~99.08%），seed42 略低但仍 >95%。VOTA 条件下模型表现稳定且强劲。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "experiment": "qwen7b_vota_seed456",
    "metrics": {
      "accuracy": 0.9908,
      "accuracy_ci": [
        0.9849,
        0.9958
      ],
      "majority_baseline": 0.7151,
      "lift": "+27.56pp",
      "n": 1190,
      "pass": {
        "precision": 1.0,
        "recall": 0.987,
        "f1": 0.994
      },
      "fail": {
        "precision": 0.969,
        "recall": 1.0,
        "f1": 0.984
      },
      "train_loss": 0.04969,
      "eval_loss": 0.08312
    }
  }
}
```

</details>

---

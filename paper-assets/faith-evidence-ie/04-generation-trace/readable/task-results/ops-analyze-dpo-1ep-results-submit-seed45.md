# ops analyze dpo 1ep results submit seed45

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_analyze-dpo-1ep-results-submit-seed45_20260515T212456_result.json`
- **Structured JSON:** [`87ca389e4d30d10b81c6.json`](../../sessions/87/87ca389e4d30d10b81c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### Task A: eval_plan_012_dpo_ced_1ep 完整 metrics

```json
{
  "rel_f1": 0.0022,
  "ign_f1": 0.0022,
  "evi_f1": 0.7500,
  "edcr": 0.9982,
  "n_predictions": 19265,
  "n_format_ok": 981,
  "n_total": 985,
  "format_ok_rate": 0.996,
  "n_truncated": 358,
  "tp": 34,
  "pred_count": 18307,
  "gold_count": 12151,
  "inference_time_seconds": 3643
}
```

**结论: NEGATIVE。** rel_f1 = 0.0022，远低于 SFT baseline 0.4057。

DPO 模型严重退化——虽然格式合规率高 (99.6%)、evidence 质量好 (Evi-F1=0.75, EDCR=0.998)，但关系抽取完全崩溃。模型输出了 19265 个 predictions（gold 只有 12151），仅 34 个 TP，说明 DPO 训练导致模型在关系判断上丧失了区分能力（几乎全部预测错误）。

### Task B: GPU 状态

| GPU | Util | Memory Used | Memory Total |
|-----|------|-------------|--------------|
| 0 | 87% | 19517 MiB | 32607 MiB |
| 1 | 91% | 16701 MiB | 32607 MiB |
| **2** | **0%** | **0 MiB** | **32607 MiB** |
| 3 | 100% | 16469 MiB | 32607 MiB |

**cuda:2 完全空闲可用。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "rel_f1": 0.0022,
    "ign_f1": 0.0022,
    "evi_f1": 0.75,
    "edcr": 0.9982,
    "n_predictions": 19265,
    "n_format_ok": 981,
    "n_total": 985,
    "format_ok_rate": 0.996,
    "n_truncated": 358,
    "tp": 34,
    "pred_count": 18307,
    "gold_count": 12151,
    "inference_time_seconds": 3643
  }
}
```

</details>

---

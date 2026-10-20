# analyze plan 011 bf16 g8 step eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_plan_011_bf16_g8_step_eval_20260515T225547_result.json`
- **Structured JSON:** [`5f124d5c53e4d218964a.json`](../../sessions/5f/5f124d5c53e4d218964a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 checkpoint 的 metrics.json 全部拿到。

```json
{
  "step_30": {"rel_f1": 0.4340, "evi_f1": 0.8063, "edcr": 0.6807, "format_ok_rate": 0.9980},
  "step_50": {"rel_f1": 0.4276, "evi_f1": 0.8024, "edcr": 0.6855, "format_ok_rate": 0.9980},
  "step_70": {"rel_f1": 0.4341, "evi_f1": 0.8099, "edcr": 0.6685, "format_ok_rate": 0.9980},
  "trend": "non-monotonic (dip at step 50, recovery at step 70)",
  "best_step": "step_70",
  "vs_sft_baseline": "+2.35pp rel_f1 (vs 0.4106 no-quant)",
  "vs_rsft_ced": "-2.59pp rel_f1 (vs 0.4600)",
  "vs_ckpt100": "-2.08pp rel_f1 (vs 0.4549)"
}
```

关键发现：

- **Step 30 和 70 的 rel_f1 几乎相同**（0.4340 vs 0.4341），step 50 反而下降到 0.4276
- **Evi-F1 单调上升**：0.8063 → 0.8024 → 0.8099（step 50 有小幅下降但 step 70 回升最高）
- **EDCR 持续下降**：0.6807 → 0.6855 → 0.6685，说明 step 70 的证据更精炼（干扰引用更少）
- 所有 early checkpoints 均**不如 ckpt-100**（rel_f1 0.4549, evi_f1 0.8120），说明训练到 step 100 仍在改善
- 同样**不如 RSFT CED**（rel_f1 0.4600），但**显著优于 SFT baseline**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "step_30": {
      "rel_f1": 0.434,
      "evi_f1": 0.8063,
      "edcr": 0.6807,
      "format_ok_rate": 0.998
    },
    "step_50": {
      "rel_f1": 0.4276,
      "evi_f1": 0.8024,
      "edcr": 0.6855,
      "format_ok_rate": 0.998
    },
    "step_70": {
      "rel_f1": 0.4341,
      "evi_f1": 0.8099,
      "edcr": 0.6685,
      "format_ok_rate": 0.998
    },
    "trend": "non-monotonic (dip at step 50, recovery at step 70)",
    "best_step": "step_70",
    "vs_sft_baseline": "+2.35pp rel_f1 (vs 0.4106 no-quant)",
    "vs_rsft_ced": "-2.59pp rel_f1 (vs 0.4600)",
    "vs_ckpt100": "-2.08pp rel_f1 (vs 0.4549)"
  }
}
```

</details>

---

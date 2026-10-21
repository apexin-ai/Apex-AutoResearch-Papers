# analyze plan 004 ablation b

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_plan-004-ablation-b_20260514T055629_result.json`
- **Structured JSON:** [`9a4cc79c613e4c97172a.json`](../../sessions/9a/9a4cc79c613e4c97172a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。结果：

```json
{
  "eval_accuracy": 0.6536,
  "eval_f1_macro": 0.5091,
  "eval_balanced_accuracy": 0.5927,
  "per_class": {
    "deterministic": {"precision": 0.9196, "recall": 0.6703, "f1": 0.7754, "support": 273},
    "internal":      {"precision": 0.1589, "recall": 0.5152, "f1": 0.2429, "support": 33}
  },
  "confusion_matrix": {
    "true_det_pred_det": 183,
    "true_det_pred_int": 90,
    "true_int_pred_det": 16,
    "true_int_pred_int": 17
  },
  "is_degenerate": false,
  "unique_predictions": ["deterministic", "internal"]
}
```

## 与 plan-002-dryrun 对比

| 指标 | plan-002 (explicit, 1 epoch) | plan-004 (implicit, 3 epochs) | 变化 |
|------|------|------|------|
| accuracy | 0.923 | 0.654 | -0.269 |
| f1_macro | 0.48 | 0.509 | +0.029 |
| balanced_accuracy | 0.50 | 0.593 | +0.093 |
| is_degenerate | YES (全 det) | **NO** | **突破** |
| det recall | 1.0 | 0.670 | -0.330 |
| int recall | 0.0 | **0.515** | **+0.515** |
| int precision | 0.0 | 0.159 | +0.159 |

## 关键发现

1. **不再退化**：plan-004 是两类都有预测的第一个成功模型，balanced_accuracy 0.593 > 0.5，证明模型学到了有意义的路由信号。

2. **internal recall 突破零**：从 plan-002 的 0% → 51.5%，模型能识别约一半的 internal 样本。

3. **代价是 accuracy 下降**：因为 90/273 (33%) 的 deterministic 样本被错误预测为 internal，导致整体 accuracy 从 0.923 降到 0.654。

4. **internal precision 很低 (0.159)**：模型预测为 internal 的样本中，只有 15.9% 真的是 internal — 大量 false positive。

5. **Qwen3 thinking mode 干扰**：模型总是生成 `&lt;think>...&lt;/think>` 前缀，需要 strip 后才能检测 `[SIMULATE]`。训练时的 chat template 可能包含了 think 标签导致训练/推理不一致，这可能是 precision 低的原因之一。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "eval_accuracy": 0.6536,
    "eval_f1_macro": 0.5091,
    "eval_balanced_accuracy": 0.5927,
    "per_class": {
      "deterministic": {
        "precision": 0.9196,
        "recall": 0.6703,
        "f1": 0.7754,
        "support": 273
      },
      "internal": {
        "precision": 0.1589,
        "recall": 0.5152,
        "f1": 0.2429,
        "support": 33
      }
    },
    "confusion_matrix": {
      "true_det_pred_det": 183,
      "true_det_pred_int": 90,
      "true_int_pred_det": 16,
      "true_int_pred_int": 17
    },
    "is_degenerate": false,
    "unique_predictions": [
      "deterministic",
      "internal"
    ]
  }
}
```

</details>

---

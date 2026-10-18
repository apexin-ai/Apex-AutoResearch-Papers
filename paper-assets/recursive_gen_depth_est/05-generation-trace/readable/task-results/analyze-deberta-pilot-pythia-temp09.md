# analyze deberta pilot pythia temp09

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_deberta_pilot_pythia_temp09_20260519T173138_result.json`
- **Structured JSON:** [`3fc940fe2d265c198272.json`](../../sessions/3f/3fc940fe2d265c198272.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐了。以下是完整分析。

---

## 实验结果：deberta_pilot_pythia_temp09

### 训练状态
训练正常完成，EXIT_CODE=0，5-fold CV 全部跑完。

### DeBERTa 关键指标

| 指标 | 值 |
|------|-----|
| **accuracy_4class** | **60.57%** |
| std_acc | ±1.55% |
| balanced_accuracy | ~60.57% (各 fold 的 acc ≈ balanced_acc) |
| per_class_recall | d0=0.921, d1=0.466, d2=0.256, d3=0.780 |
| fold_accuracies | [57.75, 62.40, 61.42, 60.78, 60.52] |
| total_time | 7997s (~2.2h) |

### RF Baseline 对比

来源：`9cell_baseline_battery.txt`（per-cell RF 准确率）

| Cell | DeBERTa | RF Baseline | Delta |
|------|---------|-------------|-------|
| **pythia_temp09** | **60.57%** | **76.8%** | **-16.2pp** |
| gpt2xl_temp09 (姐妹) | 53.14% | 85.3% | -32.2pp |

### 与姐妹实验对比

| 指标 | pythia_temp09 | gpt2xl_temp09 |
|------|---------------|---------------|
| DeBERTa acc | 60.57% | 53.14% |
| RF baseline | 76.8% | 85.3% |
| Gap | -16.2pp | -32.2pp |
| d0 recall | 0.921 | 0.812 |
| d1 recall | 0.466 | 0.288 |
| d2 recall | 0.256 | 0.084 |
| d3 recall | 0.780 | 0.942 |

pythia_temp09 上 DeBERTa 相对更好（gap 更小），d1/d2 中间深度召回明显高于 gpt2xl，但 RF 仍大幅领先。

### Hypothesis 验证

**Hypothesis**: DeBERTa < RF on pythia_temp09, confirming cross-model generality of "simple features beat neural".

**结论: success** — DeBERTa (60.57%) 远低于 RF (76.8%)，差距 16.2pp。两个 cell（pythia + gpt2xl）均确认 RF+19-feature > end-to-end neural，支持论文 claim。

### 完整 metrics dict (可直接写入 registry)

```json
{
  "accuracy_4class": 0.6057,
  "std_acc": 0.0155,
  "balanced_accuracy": 0.6057,
  "per_class_recall": {"d0": 0.9208, "d1": 0.466, "d2": 0.2558, "d3": 0.7804},
  "fold_accuracies": [0.5775, 0.624, 0.6142, 0.6078, 0.6052],
  "confusion_matrix": [[4604,389,7,0],[120,2330,1322,1228],[6,991,1279,2724],[4,424,670,3902]],
  "total_time_seconds": 7997.1,
  "rf_baseline_acc": 0.768,
  "delta_vs_rf": -0.162,
  "model_name": "microsoft/deberta-v3-base",
  "lora_config": "r=8, alpha=16, query_proj+value_proj",
  "num_samples": 20000,
  "folds": 5,
  "epochs": 5
}
```

**建议 conclusion: `success`** — hypothesis confirmed, cross-model generality established.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "accuracy_4class": 0.6057,
    "std_acc": 0.0155,
    "balanced_accuracy": 0.6057,
    "per_class_recall": {
      "d0": 0.9208,
      "d1": 0.466,
      "d2": 0.2558,
      "d3": 0.7804
    },
    "fold_accuracies": [
      0.5775,
      0.624,
      0.6142,
      0.6078,
      0.6052
    ],
    "confusion_matrix": [
      [
        4604,
        389,
        7,
        0
      ],
      [
        120,
        2330,
        1322,
        1228
      ],
      [
        6,
        991,
        1279,
        2724
      ],
      [
        4,
        424,
        670,
        3902
      ]
    ],
    "total_time_seconds": 7997.1,
    "rf_baseline_acc": 0.768,
    "delta_vs_rf": -0.162,
    "model_name": "microsoft/deberta-v3-base",
    "lora_config": "r=8, alpha=16, query_proj+value_proj",
    "num_samples": 20000,
    "folds": 5,
    "epochs": 5
  }
}
```

</details>

---

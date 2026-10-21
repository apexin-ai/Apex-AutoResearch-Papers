# code detector tfidf lr

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_detector-tfidf-lr_20260513T231629_result.json`
- **Structured JSON:** [`481f0fb8f25bd48c6ace.json`](../../sessions/48/481f0fb8f25bd48c6ace.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

**选中配置**: `combo_degrade` — unigrams only, max_features=10000, C=0.01, 截断前 100 词

| 指标 | 值 |
|------|-----|
| **AUC** | 0.939 |
| **Accuracy** | 85.8% |
| **ECE (raw → calibrated)** | 0.240 → 0.048 |
| **Temperature T** | 0.204 |
| **q-score mean/std/median** | 0.600 / 0.374 / 0.707 |
| **mid-range (0.1-0.9) 比例** | **46.3%** |

**q-score 分布 (calibrated, 温度缩放后)**:

```
0.0-0.1:  4624  ███████████████
0.1-0.2:  2936  ██████████
0.2-0.3:  2020  ███████
0.3-0.4:  1659  █████
0.4-0.5:  1410  ████
0.5-0.6:  1337  ████
0.6-0.7:  1244  ████
0.7-0.8:  1429  ████
0.8-0.9:  2157  ███████
0.9-1.0: 11826  ████████████████████████████████████████
```

**模型保存路径**: `westd-47453:/root/provenance_weight_training/output/detector_tfidf/`
- `tfidf_vectorizer.joblib` (361K)
- `lr_model.joblib` (79K)
- `predictions.jsonl` (30,642 rows)
- `calibration_results.json`

目标完全达成：AUC 0.939（在 0.85-0.98 范围），mid-range 46.3%（远超 5% 阈值）。q-score 分布平滑，不再是二值化的。不需要进一步调整。

---

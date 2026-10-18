# code baseline rf lr unified

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_baseline_rf_lr_unified_20260514T164446_result.json`
- **Structured JSON:** [`4d0c5b95246913098eaf.json`](../../sessions/4d/4d0c5b95246913098eaf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。全部 7 个方法在同一 70/15/15 test set 上的对比结果：

| Method | 4-class Acc | 95% CI | 3-class Acc | MAE |
|--------|------------|--------|-------------|-----|
| CE-MLP (DCOL ablation) | **0.7897** | [0.7743, 0.8037] | **0.7204** | **0.2280** |
| DivEye (XGBoost) | 0.7817 | [0.7663, 0.7970] | 0.7098 | 0.2363 |
| **Random Forest** | 0.7813 | [0.7663, 0.7973] | 0.7093 | 0.2387 |
| CORAL Ordinal Regression | 0.7807 | [0.7653, 0.7950] | 0.7089 | 0.2273 |
| **Logistic Regression** | 0.7497 | [0.7337, 0.7653] | 0.6671 | 0.2767 |
| PPL Regression (multi OLS) | 0.6223 | [0.6047, 0.6397] | 0.5200 | 0.3890 |
| PPL Regression (single) | 0.2513 | [0.2370, 0.2670] | 0.3351 | 0.9440 |

要点：
- RF 在统一 split 下 4-class acc = 0.7813，与之前 80/20 split 的 0.7815 几乎一致，说明之前的结果是可靠的
- RF 和 DivEye/CORAL 在同一量级，CE-MLP 略领先
- LR 是线性模型，低于非线性方法约 3pp，符合预期

---

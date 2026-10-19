# ops investigate csv selectivity

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_investigate-csv-selectivity_20260521T063649_result.json`
- **Structured JSON:** [`8fbf4d43fa5acb1d90e9.json`](../../sessions/8f/8fbf4d43fa5acb1d90e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 调查报告

### 1. CSV 文件内容

`results/probing_controls.csv` 包含 8 层 (L0/4/8/12/16/20/24/27) 的 real_auroc、perm_auroc 和 selectivity。底层 AUROC 值与 registry 一致，但 selectivity 列差异巨大（CSV L0=13.9 vs registry L0=0.020）。

### 2. 不一致原因

**selectivity 公式不同。** 两个版本的代码在 `code/` 下：

| | `probing_controls.py` (v1, 生成该 CSV) | `probing_controls_v2.py` (v2, registry 权威数据) |
|---|---|---|
| **selectivity 公式** | `(real - perm) / (real - 0.5)` | `real - perm` (Hewitt & Liang 2019) |
| **PCA** | PCA(100) 在 CV 外拟合（有数据泄漏） | 无 PCA |
| **Scaler** | 全局 fit（泄漏） | 每 fold 内 fit（正确） |
| **AUROC 计算** | `cross_val_score` (predict_proba) | `decision_function` |
| **max_iter** | 1000 | 2000 |

v1 的公式 `(real - perm) / (real - 0.5)` 在 L0 处分母极小 (0.501 - 0.5 = 0.0015)，导致 selectivity 膨胀到 13.9。这不是 Hewitt & Liang 定义，且 v1 还有 PCA/Scaler 数据泄漏问题。

### 3. 正确数据

**Registry plan_013 为权威数据**（Hewitt & Liang selectivity: L0=0.020 → L27=0.262），来自 v2 代码，方法学正确。

### 4. 已执行操作

已将 CSV 重命名：`results/probing_controls.csv` → `results/probing_controls_DEPRECATED.csv`

v2 脚本输出的 `probing_controls_v2.csv` 尚未生成（registry 中 `plan_013_probing_controls_v2` 状态为 RUNNING）。

### 5. 其他过时文件

`code/probing_controls.py` (v1) 是产生错误 CSV 的源码，可考虑后续清理，但不紧急——关键是 CSV 已标记为 DEPRECATED，不会被误用。

---

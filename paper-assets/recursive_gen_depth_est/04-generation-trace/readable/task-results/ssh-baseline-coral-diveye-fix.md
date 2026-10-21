# ssh baseline coral diveye fix

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_baseline_coral_diveye_fix_20260514T231457_result.json`
- **Structured JSON:** [`7489c87a204cd2eb455e.json`](../../sessions/74/7489c87a204cd2eb455e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报如下。

---

## 修复 1: CORAL 训练不足 — 已确认并修复

**根因**: 之前 CORAL 用 `--epochs 5 --patience 3` 跑的（代码默认值实际是 100/10），导致严重训练不足。

**无需修改 `src/baselines.py`** — 代码默认 `epochs=100, patience=10` 已足够。问题在于之前的 CLI 参数。

### CORAL 新旧指标对比

| 指标 | 旧 (epochs=5, p=3) | 中 (epochs=15, p=5) | 新 (epochs=100, p=10) |
|------|:---:|:---:|:---:|
| 4-class acc | 0.5367 | 0.6780 | **0.7807** |
| 3-class acc | 0.3822 | 0.5716 | **0.7089** |
| MAE | 0.544 | 0.3447 | **0.2273** |
| d1v2 AUC | 0.3416 | 0.5024 | **0.8179** |
| d0v1 AUC | 0.998 | 0.9972 | 0.9983 |
| d2v3 AUC | 0.7357 | 0.7573 | 0.7848 |

**结论**: CORAL 在充分训练后（100 epochs）性能接近 CE-MLP（0.7807 vs 0.7897），d1v2 AUC 从 0.34 飙升至 0.82。之前的 "CORAL 不适合此任务" 的结论是错误的，需要在论文中修正。15 epochs 不够（d1v2 AUC 仅 0.50），建议使用默认的 100 epochs。

---

## 修复 2: DivEye 标签不一致 — 无需修复

- **代码** (`baselines.py:548-554`): `DivEyeBaseline.fit()` 使用 `XGBClassifier(n_estimators=200, max_depth=6, ...)`
- **结果 JSON**: 标签为 `"DivEye (XGBoost)"`
- **结论**: 代码和标签一致，实际跑的就是 XGBoost，无需修改。

### DivEye 最终指标

| 指标 | 值 |
|------|:---:|
| 分类器 | XGBoost (n_estimators=200, max_depth=6) |
| 4-class acc | 0.7817 |
| 3-class acc | 0.7098 |
| MAE | 0.2363 |
| d1v2 AUC | 0.8654 |

---

## 代码改动

**无**。`src/baselines.py` 未修改。代码默认参数 (`epochs=100, patience=10`) 本身是正确的，问题出在之前的运行命令使用了过小的参数。已用默认参数重跑全部 feature baselines 并更新 `results/baselines/baseline_results.json`。

---

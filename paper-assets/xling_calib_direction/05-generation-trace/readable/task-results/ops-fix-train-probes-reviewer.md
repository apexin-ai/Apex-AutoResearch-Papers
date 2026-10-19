# ops fix train probes reviewer

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-train-probes-reviewer_20260521T072352_result.json`
- **Structured JSON:** [`3c9225452baab3ab68b5.json`](../../sessions/3c/3c9225452baab3ab68b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修复完成，验证结果：

**Fix 1** — `solver="lbfgs"` → `solver="liblinear"` (line 209, train_probes.py) ✓

**Fix 2** — Procrustes 平行数据修复（两个文件）：
- `extract_activations.py`：英语先处理并做一次 stratified split，global indices 写入 metadata（`train_indices`/`eval_indices`），所有语言复用相同 indices
- `train_probes.py`：Procrustes 改为在 train split 的平行数据上拟合（`X_tr_en[:n_pairs]`, `X_tr_tgt[:n_pairs]`），在 eval 上评估。不再用 eval 数据随机采样拟合

**Fix 3** — `--n_control` default 5 → 10 (line 436, train_probes.py) ✓

**验证** — 两个文件语法检查通过，`--help` 正常运行。

---

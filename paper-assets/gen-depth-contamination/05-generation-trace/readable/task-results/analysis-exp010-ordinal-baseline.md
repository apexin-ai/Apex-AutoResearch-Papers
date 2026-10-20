# analysis exp010 ordinal baseline

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp010_ordinal_baseline_20260513T041948_result.json`
- **Structured JSON:** [`c643422d485b49ee2b98.json`](../../sessions/c6/c643422d485b49ee2b98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-010 完成。结果汇总：

## MAE 对比（越低越好）

| Dataset | OBD-LightGBM | Multiclass LightGBM | Ordinal LogReg | 最佳 ordinal 胜? |
|---------|-------------|---------------------|----------------|-----------------|
| Qwen    | 0.9836      | **1.0163**          | **0.9105**     | YES (-10.4%)    |
| Pythia  | 1.1072      | **1.1399**          | **1.0220**     | YES (-10.3%)    |
| OLMo    | 1.1469      | **1.1813**          | **1.0352**     | YES (-12.4%)    |

## Kendall's τ-b（越高越好）

| Dataset | OBD-LightGBM | Multiclass | Ordinal LogReg |
|---------|-------------|------------|----------------|
| Qwen    | 0.5518      | 0.5367     | **0.5630**     |
| Pythia  | 0.4745      | 0.4622     | **0.4900**     |
| OLMo    | 0.4683      | 0.4497     | **0.4656**     |

**结论：success** — ordinal 方法在 MAE 和 τ-b 上全面胜过无序 multiclass，3/3 数据集一致。

注意事项：ordinal_logreg 的 pairwise AUC 最差（~0.48-0.50 vs multiclass 的 ~0.60），说明它的 MAE 优势来自预测分布向中心收缩（类似 mean regression），而非真正更好的 depth 区分能力。OBD-LightGBM 在 MAE 和 AUC 上都优于 standard multiclass，是更均衡的 ordinal 方法。

---

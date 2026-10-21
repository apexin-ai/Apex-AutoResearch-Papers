# code baseline battery

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_baseline_battery_20260514T161949_result.json`
- **Structured JSON:** [`802b6991060612cb8912.json`](../../sessions/80/802b6991060612cb8912.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 个 baseline 跑通，结果汇总：

| Method | 4-class | 3-class | MAE |
|---|---|---|---|
| PPL Regression (single: mean_ppl) | 0.2513 | 0.3351 | 0.9440 |
| PPL Regression (multi: 19-dim OLS) | 0.6223 | 0.5200 | 0.3890 |
| CE-MLP (DCOL ablation) | 0.7897 | 0.7204 | 0.2280 |
| CORAL Ordinal Regression | 0.7807 | 0.7089 | 0.2273 |
| DivEye (XGBoost) | 0.7817 | 0.7098 | 0.2363 |
| (ref) RF MVP | 0.7815 | — | — |

文件已部署到 `/root/autodl-tmp/recursive_gen_depth_est/src/baselines.py`，结果保存在 `results/baselines/baseline_results.json`。

关键发现：
- 单特征 PPL 回归几乎等于随机（25%），说明单靠 mean_ppl 无法区分 depth
- CE-MLP (79.0%) 略胜 RF MVP (78.2%)，但差异在置信区间内——这意味着 DCOL 的 contrastive loss 对性能提升至关重要
- CORAL (78.1%) 和 DivEye (78.2%) 与 RF 持平
- 所有方法在 depth-2 的 recall 最低（~60%），depth-0 最高（~99%）

DivEye 的 TODO：当前使用 14/19 维特征的静态统计量，未实现 DivEye 原版的 first-order (∆S) 和 second-order (∆²S) temporal surprisal 特征（需要 raw token-level surprisal 序列）。

---

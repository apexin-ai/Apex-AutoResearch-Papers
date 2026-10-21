# analyze power curve discrepancy

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_power-curve-discrepancy_20260518T230254_result.json`
- **Structured JSON:** [`2105ddde79c56280f67e.json`](../../sessions/21/2105ddde79c56280f67e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 对比报告

逐项对比两个脚本代码和结果：

```
Detection criterion 差异: 无 — 两者都是 point estimate AUC > θ=0.60（不是 CI lower bound）
数据源差异: 无 — 路径均为 data_exp016_qwen_base/features.csv，15 个 feature 列完全相同
LightGBM 差异: 无 — n_estimators=200, max_depth=6, lr=0.05, num_leaves=31 完全一致
Resampling 差异: 有 — 随机种子不同（新=42，旧=2024），抽样方式相同（doc-level, replace=False）
AUC 计算差异: 无 — 均为 OOF 合并后的 roc_auc_score(y, oof_proba)
```

### 根因

**唯一差异是随机种子（42 vs 2024）**，其他代码逻辑完全一致。

n=1000 时 AUC 分布中心恰好在 θ=0.60 附近，处于判定边界上：

| | seed=42 (新) | seed=2024 (旧) |
|---|---|---|
| 10 次 trial AUC | 0.568~0.619 | 0.592~0.638 |
| mean AUC | 0.5911 | 0.6076 |
| >0.60 的次数 | 3/10 → 30% | 9/10 → 90% |

seed=2024 恰好抽到的 doc 子集整体偏好，mean AUC 高了 1.6pp，足以让大部分 trial 越过 0.60 阈值。10 次 resample 在阈值附近的 detection rate 估计本身就极不稳定。

### 建议

两个版本方法学完全等价，都不存在 bug。60pp 的差异是 **10 次 resample + AUC 恰好在 θ 边界** 导致的采样噪声。

作为权威版本，建议用 **c4_power_curve.py（旧版）** 的框架，但做两处修改：
1. **增加 resample 次数到 50~100**，消除 detection rate 的采样噪声
2. **固定 seed=2024**（保持与已有结果的一致性），或者报告多个 seed 的平均值

---

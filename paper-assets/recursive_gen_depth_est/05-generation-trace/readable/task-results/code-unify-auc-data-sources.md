# code unify auc data sources

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_unify_auc_data_sources_20260515T043454_result.json`
- **Structured JSON:** [`bbca728a3fc8f5e8f1ee.json`](../../sessions/bb/bbca728a3fc8f5e8f1ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。以下是产出总结：

---

## 产出清单

### 1. 三列对比表
见上方注册的 `auc_unification_report`。关键发现：
- **8/9 cells**: edd_sensitivity 与 pipeline 完全一致
- **gpt2xl_topk50**: 唯一不一致的 cell（已修复）
- **edd_9cell**: 系统性偏高（均值 +0.03），d1v2 偏高最大（+0.04~+0.09）

### 2. edd_sensitivity.json 更新
gpt2xl_topk50 的 3 个 AUC 已覆盖为 pipeline 值：
```
d0v1: 0.9906 → 0.9884
d1v2: 0.8126 → 0.8259
d2v3: 0.7529 → 0.7708
```
EDD 阈值判定不变（T=0.80 仍为 EDD=2）。

### 3. edd_analysis_9cell.json 偏差原因
- atlas_v2_analysis.py 用 **5-fold CV**（pipeline 用单次 split）
- 4/9 cells 使用**不同数据源**（`data/` 路径 vs pipeline 内部路径）
- d1v2 偏差最大是因为该对最难区分，方法论差异影响最大
- 结论：9cell 值可用于 bootstrap CI 分析，但不应替代 pipeline 点估计

### 4. plot_atlas_figures.py 修改摘要
**fig1**：删除 11 行硬编码 AUC 字典 → `load_pipeline_auc()` 从 9 个 `pairwise_auc.json` 动态加载 RF 值

**fig4**：删除硬编码 3×3 accuracy 矩阵 → 对 9 个 cell 的 `features.jsonl` 运行 5-fold CV RF，动态计算精度

新增常量：`CELL_AUC_PATHS`、`ATLAS_GRID`、`CELL_FEATURES_PATHS` 三个路径映射

fig2、fig3 未改动。

### 5. 重新生成的图表
位于 `/root/autodl-tmp/recursive_gen_depth_est/artifacts/figures/`：
- `fig1_auc_decay.pdf/png`（AUC 值与 pipeline 完全一致，无变化）
- `fig4_atlas_heatmap.pdf/png`（精度值变化 < 1pp，因方法从单次 split 改为 5-fold CV）

---

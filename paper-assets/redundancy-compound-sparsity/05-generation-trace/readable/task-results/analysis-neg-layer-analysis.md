# analysis neg layer analysis

**When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_neg-layer-analysis_20260512T002120_result.json`
- **Structured JSON:** [`258cc5d7b590f20c8cb9.json`](../../sessions/25/258cc5d7b590f20c8cb9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。输出文件在 `/home/sonny/redundancy-compound-sparsity/results/mvp/analysis/`：

**图表** (PDF+PNG):
- `per_layer_r.pdf` — 28 层 Pearson r 折线图（v2 easy / v3 hard 双线，region shading）
- `per_layer_dpert.pdf` — 28 层 Δpert% 折线图（含 0% 线和 -10% 阈值）
- `per_layer_ks.pdf` — 28 层 K-S statistic 折线图

**分析文档**: `analysis_summary.md`

**核心发现**:

| Region | Layers | Mean r (v2) | Mean r (v3) |
|--------|--------|------------|------------|
| Early | 0-3 | +0.019 | +0.075 |
| Mid-Early | 4-11 | **+0.199** | **+0.211** |
| Mid-Late | 12-20 | +0.024 | +0.033 |
| Late | 21-27 | **+0.174** | **+0.167** |

1. **r 呈双峰分布**: Mid-Early (L4-11, r≈0.20-0.29) 和 Late (L21-26, r≈0.17-0.22) 两个高峰，中间 L12-20 几乎为零。Layer 4 在两组实验中都是峰值 (r≈0.289)。
2. **Δpert 方向不一致**: Early layers (v2) 的 Δpert 为 -10%~-12%（符合假设方向），但 Layer 27 的 Δpert 为 +21.9%/+19.6%（反向），说明 cross-axis coupling 在不同层间信号矛盾。
3. **KS 单调递减**: 从 L0 的 0.29 降到 L27 的 0.09，早期层 MLP 分布差异最大但不对应可剪枝性。
4. **v2/v3 profile 高度一致** (profile 相关 r=0.950)，说明模式是模型内在的，非任务依赖。

**对 negative evidence 的结论**: Anchor similarity 确实捕捉到弱冗余信号（某些层 r 达 0.29），但这个信号**不映射到 MLP 激活稀疏性**——Δpert 在多数层接近零且方向不一致，cross-axis 假设不成立。

---

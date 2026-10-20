# analysis cross alpha aggregation

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_alpha_aggregation_20260515T210112_result.json`
- **Structured JSON:** [`2db95e98d8dd80234591.json`](../../sessions/2d/2db95e98d8dd80234591.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出完成。两个 artifact 已注册：

**`cross_alpha_summary.md`** — 5 张表 + key findings：
- **Table 1** (Drift): 6 个 (α, seed) 组合的 6 指标 drift%
- **Table 2** (Detectability): Granger FDR sig、consensus robust、method ablation 按 α 汇总
- **Table 3** (Cross-seed): α=0.25 s42 vs s43 逐指标对比，diversity drift 差异 <1.2pp
- **Table 4** (Granger detail): 4 个 forward pair × 5 个 α 的 FDR p 值矩阵
- **Table 5** (Consensus): 每个 α 的 robust pair 数和关键 pair 列表

**`regime_map_data.json`** — matplotlib 绘图数据，含 `plotting.x/y_*` 数组可直接画图

核心发现：
1. α=0.50→0.75 存在 **sharp phase transition**（Granger FDR sig 从 0% 跳到 75%，consensus robust 从 0/16 跳到 11/16）
2. Diversity drift 在 α=0.25 最严重（d3: −60%），calibration drift 随 α 单调递增 — 两类指标 **dissociated**
3. Naive 方法在 null control (α=0) 也报 100% sig，robust 方法正确归零；方法选择翻转 >50% 结论
4. α=0.25 跨 seed 高度一致（d1 差异 0.2pp）

---

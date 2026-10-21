# writing figure plan

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_figure_plan_20260512T164742_result.json`
- **Structured JSON:** [`c83e1443a89fc5c97e9c.json`](../../sessions/c8/c83e1443a89fc5c97e9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表方案已写入 `docs/figure_plan.md`。

包含 10 个图表（6 个 P0 必做 + 4 个 P2 篇幅允许时）：

**必做 (P0)**：
- Fig 1: Pipeline 示意图（TikZ，可立即开始）
- Fig 2: Pairwise AUC 衰减曲线（核心结果）
- Fig 3: JSD 衰减 + DPI 理论预测叠加
- Fig 4: Feature importance 水平柱状图（三色编码）
- Fig 5: Graduated vs binary filtering 下游对比
- Fig 6: Feature group × depth 判别力热力图（降解序）
- Table 1: 完整 pairwise AUC 矩阵

**可选 (P2)**：
- Fig 7: UMAP 特征空间可视化
- Fig 8: Surprisal 分布 ridge plot
- Fig 9: 6×6 confusion matrix
- Fig 10: Cross-model transfer 热力图
- Table 2: 消融实验汇总

方案包含了全局配色规范（三组特征蓝/绿/橙贯穿全文）、尺寸规范（ACL/EMNLP 模板）、路线 A/B 适配说明，以及按实验依赖排序的制作时间线。

---

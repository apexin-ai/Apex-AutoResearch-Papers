# analysis deep vs fast internal

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deep-vs-fast-internal_20260515T163707_result.json`
- **Structured JSON:** [`f40cf442318c3aee317d.json`](../../sessions/f4/f40cf442318c3aee317d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**3-way routing 没有数据支撑，2-way suffices。**

核心发现：

| 维度 | Fast-internal | Deep-internal | 差异 |
|------|--------------|---------------|------|
| 跨 task 平均分 | -38.11 | -37.55 | Δ=0.56, p=0.83 |
| 平均 death rate | 41.8% | 42.5% | 几乎相同 |
| 显著差异 task 数 | — | — | **0 / 6** |

6 个重叠 task 无一达到 p < 0.05（Mann-Whitney U）。效应量全部 negligible（|d| ≤ 0.31）。Score 分布形态在两种 mode 下高度一致——都是"死亡（-100）或低分（0）"的双峰结构。

**find-non-living-thing** 是唯一有趋势的 task（deep 26.6 vs fast 18.9），但 p=0.27 且该 task 0% death rate，routing 价值本身有限。

**结论**：Deep-internal 的额外 thinking cost 未换来可测量的性能提升。Router 无法有效区分何时该调用 deep vs fast。维持 2-way routing（deterministic vs internal），以 fast-internal 代表 internal mode。

报告已写入 `artifacts/deep_vs_fast_analysis.md`。

---

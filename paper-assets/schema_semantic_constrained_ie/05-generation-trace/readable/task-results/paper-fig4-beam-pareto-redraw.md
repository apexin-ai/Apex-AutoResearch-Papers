# paper fig4 beam pareto redraw

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fig4-beam-pareto-redraw_20260524T133502_result.json`
- **Structured JSON:** [`e3e3c21e688dedd355cb.json`](../../sessions/e3/e3e3c21e688dedd355cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**完成。** 汇报如下：

**改了什么：**
- 移除所有逐点 `k=X` 标签（x 轴已标注 beam width）
- "Zero violation" 圆环和 "Pareto-optimal" 星标从顶部共享图例移入各子图 legend
- 右子图标题从 "DocRED (Llama-3.1-8B LoRA, 200 docs)" 简化为 "DocRED (200 docs)"
- 配色对齐 Figure 1 v6：constrained 用松石绿 #1A7A6D，unconstrained 用深蓝 #34495E，Llama con 用暖红 #B85450，Pareto 星用柔金 #D4A574，zero-violation 环用松石绿
- 去除 top/right spines，网格极淡 #F0F0F0，线条更细
- 星标加白色光晕确保可见性
- 左面板 legend 改 3 列布局避免拥挤

**迭代：** 3 轮（布局 → 星标/bubble 可见性 → 白色光晕精细调整）

**编译：** 零错误，主文 8 页，符合 EMNLP 2026 限制

**产出：** `figures/beam_pareto.pdf` 和 `.png` 已覆盖

---

# draw fig2 mining strategies

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_draw_fig2-mining-strategies_20260514T233945_result.json`
- **Structured JSON:** [`293e80f829d4afb87d92.json`](../../sessions/29/293e80f829d4afb87d92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出完成：

- **PDF**: `artifacts/paper_figures/fig2_mining_strategies.pdf`
- **PNG**: `artifacts/paper_figures/fig2_mining_strategies.png`
- **脚本**: `artifacts/paper_figures/fig2_mining_strategies.py`
- 已注册 `art_20260514_a5287e`

图表设计要点：
- 10 个节点（1 query + 9 files），相同布局跨 3 个 panel
- 结构边 P→a, P→i，reachable = {a, i}
- **(a) Random**: 选 {f, g, h}（远处散布，easy negatives）
- **(b) Embedding**: 选 {d, i, a}（最近 3 个，但 i/a 结构连通）
- **(c) Dataflow**: 选 {d, c, e}（最近且结构断开），i/a 标 ✕ 排除并注释 "reachable via G"
- Panel (b) 添加虚线 embedding 距离圈，panel (c) 加粗 dataflow 边强调结构信息的使用

---

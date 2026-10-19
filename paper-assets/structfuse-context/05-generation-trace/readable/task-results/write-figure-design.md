# write figure design

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_figure-design_20260514T225408_result.json`
- **Structured JSON:** [`90ab77a59d0f85f35657.json`](../../sessions/90/90ab77a59d0f85f35657.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

设计稿已写入并注册 (`art_20260514_c76ce4`)。

共设计 8 个 Figure：

| # | 标题 | 优先级 | 数据状态 |
|---|------|--------|---------|
| 1 | Pipeline Overview | 必须 | 无需数据（示意图） |
| 2 | Negative Mining Strategies 示意 | 必须 | 无需数据 |
| 3 | Main Results 对比 | 必须 | 等 M2 完成 |
| 4 | Representation Geometry (margin + distribution) | 必须 | **已就绪**（v3_2048 数据 + 3 张现有图） |
| 5 | Pool Size Sensitivity | 建议 | 等 plan_019 |
| 6 | Training Curves | 可选 | 部分可用 |
| 7 | SWE-bench Downstream | 建议 | 等 plan_003 |
| 8 | Stratified Analysis | 可选 | 等 plan_005 |

建议 production 顺序：Fig 4（数据已有，打磨现有图）→ Fig 1+2（示意图无数据依赖）→ Fig 3（M2 完成后）→ Fig 5/7（对应 plan 完成后）。现有 3 张 neg_difficulty 图建议合并为 Fig 4 的 2-panel 版本（margin comparison + similarity distribution），ratio heatmap 移 appendix。

---

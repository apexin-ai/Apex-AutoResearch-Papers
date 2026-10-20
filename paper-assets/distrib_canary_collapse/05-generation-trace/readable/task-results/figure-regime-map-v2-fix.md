# figure regime map v2 fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_regime-map-v2-fix_20260515T135541_result.json`
- **Structured JSON:** [`140418d5d87a84e2ac3e.json`](../../sessions/14/140418d5d87a84e2ac3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。`regime_map_fdr.pdf` 已用 `cross_alpha_v6.json` 的真实 FDR p-value 重新生成，artifact 已注册为 `regime_map_fdr_v2`（`art_20260515_06ffe6`）。

修正摘要：
- α=1.0 的 4 个方向 p_fdr 从硬编码 0.001 修正为 0.024–0.054
- entropy→d2 @ α=1.0（p=0.054）和 entropy→d1 @ α=0.75（p=0.054）正确落在阈值线下方
- 所有 5 个 α × 4 个方向均有数据点（无 NaN）
- consensus_heatmap.pdf 未改动

---

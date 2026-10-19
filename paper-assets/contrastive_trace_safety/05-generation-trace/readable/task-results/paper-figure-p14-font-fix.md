# paper figure p14 font fix

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_p14_font_fix_20260518T163351_result.json`
- **Structured JSON:** [`12ac1a165db38b8dac49.json`](../../sessions/12/12ac1a165db38b8dac49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修复内容：

- **字体**：base 9pt, title 10pt, tick labels 8pt, legend 8pt（原版 legend 6.5pt 违规）
- **figsize**：从 `(6.75, 5.5)` 增大到 `(7, 10.5)`，4 个子图有足够空间
- **图例**：使用 `bbox_to_anchor=(1.01, 1.0)` 放在图外右侧，不遮挡数据
- 输出已保存到本地 `docs/paper/figures/fig_layer_heatmap.pdf` 和远程 `artifacts/` + `docs/paper/figures/`

---

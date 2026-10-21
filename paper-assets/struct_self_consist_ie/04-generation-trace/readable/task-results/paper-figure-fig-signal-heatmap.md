# paper figure fig signal heatmap

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig_signal_heatmap_20260514T142903_result.json`
- **Structured JSON:** [`7e616d6c831ef1b5adcd.json`](../../sessions/7e/7e616d6c831ef1b5adcd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PDF 已生成并注册（`art_20260514_619caf`）。

输出路径: `figures/paper/fig_signal_heatmap.pdf`（42KB 矢量 PDF）

图表内容：
- 5×5 heatmap，行=confidence signals，列=task conditions（按难度递增）
- RdYlGn 发散色图，vcenter=0.25，cell 内标注 ρ 值
- 缺失值灰底 "—"，WNUT-17 列左侧虚线标注 "method boundary"
- LLaMA-3.1-8B cross-model ρ 以斜体小字 `L:` 标注在对应 cell 内
- 底部标注各 task 难度等级

---

# paper fig2 scatter redraw

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fig2-scatter-redraw_20260525T052938_result.json`
- **Structured JSON:** [`5c37bf78de7c8ed88b22.json`](../../sessions/5c/5c37bf78de7c8ed88b22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**PaperBanana 无法用于此任务。**

PaperBanana skill 文档明确写了：

> | **统计图**（scatter、bar、line、heatmap、forest） | **draw-paper-figure.skill.md**。**不要用 PaperBanana 画统计图** |

Figure 2 是精确坐标的散点图（scatter），属于统计图，不是概念图。PaperBanana 设计用于架构图、流程图、framework 示意等概念图，无法保证数据点的精确位置。

**建议改用 draw-paper-figure（matplotlib）方案**，可以：
- 精确放置每个 (κ, Δ) 数据点
- 采用 Figure 3 的柔和配色（浅蓝、浅粉、浅绿、深蓝灰、暖橙）
- 达到顶会级别美观度

需要我用 draw-paper-figure 重画吗？

---

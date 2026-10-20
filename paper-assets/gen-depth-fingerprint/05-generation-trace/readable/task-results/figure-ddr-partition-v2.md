# figure ddr partition v2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_ddr_partition_v2_20260520T144738_result.json`
- **Structured JSON:** [`e8d50a48791e19c795c4.json`](../../sessions/e8/e8d50a48791e19c795c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。输出文件：
- `fig1_differential_response.pdf` (26 KB)
- `fig1_differential_response.png` (85 KB)

图表设计：
- 3.4×3.5 英寸横向条形图，7 个 feature 按 |ρ| 降序排列（Hapax Ratio 最上，Tail Decay 最下）
- 三色分区：Drifting (绿) / Intermediate (紫) / Near-stationary (橙)，灰色虚线分隔
- 每个 bar 末端叠加 8 个灰色 jitter 点显示 per-generator 变异
- 右侧灰色小字标注分区名，LaTeX 风格 feature 标签
- 脚本：`scripts/plot_fig1_partition_v2.py`

---

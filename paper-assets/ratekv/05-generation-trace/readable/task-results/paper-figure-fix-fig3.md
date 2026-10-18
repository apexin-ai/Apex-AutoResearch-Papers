# paper figure fix fig3

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fix_fig3_20260514T075955_result.json`
- **Structured JSON:** [`9140a7c6b24005e1f82c.json`](../../sessions/91/9140a7c6b24005e1f82c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Y 轴刻度已修正为整数（0, 1, 2, 3, 4），不再显示小数。

更新的文件：
- 服务器：`/root/ratekv/generate_figures.py` — 添加 `ax.yaxis.set_major_locator(MaxNLocator(integer=True))`
- 本地脚本：`artifacts/generate_figures.py` — 同步修改
- `docs/paper/figures/fig3_allocation_comparison.pdf` (20KB)
- `figures/paper/fig3_allocation_comparison.pdf` (20KB)
- `artifacts/figures/fig3_allocation_comparison.png` (110KB)

---

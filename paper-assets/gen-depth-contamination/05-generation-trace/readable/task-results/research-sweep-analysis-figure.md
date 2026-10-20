# research sweep analysis figure

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_sweep_analysis_figure_20260520T180510_result.json`
- **Structured JSON:** [`1be5edf93afa87ca0a38.json`](../../sessions/1b/1be5edf93afa87ca0a38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

- **脚本**: `/root/autodl-tmp/gen-depth-contamination/scripts/draw_sweep_figure.py`
- **PDF**: `/root/autodl-tmp/gen-depth-contamination/results/contamination_sweep/fig_contamination_sweep.pdf`
- **PNG**: 同目录 `.png`，已注册为 `art_20260520_97acff`

图中可见：Binary Filter 在 10%~50% 污染率下性能几乎持平（HellaSwag ~0.670, ARC-C ~0.45），而 No Filter 和 Graduated 随污染率单调下降。50% 处 Binary 相对 No Filter 的优势为 HellaSwag +1.18pp、ARC-C +2.05pp。100% 时 Binary 因全部样本被过滤标注为 N/A。

---

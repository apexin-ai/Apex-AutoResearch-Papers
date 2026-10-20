# paper update trajectory plot

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_update_trajectory_plot_20260517T062316_result.json`
- **Structured JSON:** [`ab31da8de748b570a2f9.json`](../../sessions/ab/ab31da8de748b570a2f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。5-panel 图已生成。

**布局**：上排 3 panel (eff_rank, log_det, ppl)，下排 2 panel (distinct-4, HellaSwag)。

**使用数据**：Gen 0-5 全部 6 代，其中：
- eff_rank / log_det / ppl / distinct4：从 `results/phase0_results.json` 读取实际值
- HellaSwag：使用提供的数据 [0.4130, 0.3897, 0.3764, 0.3658, 0.3558, 0.3439]

**Gen 5 实际值**：eff_rank=479.21, log_det=2370.17, ppl=24.59, distinct4=0.463

**图表特征**：
- Gen 2 "decompression peak" 标注在 eff_rank 和 log_det panel（红色虚线 + 箭头）
- HellaSwag panel 标注 16.7% decline
- Y 轴范围收紧以突出趋势

---

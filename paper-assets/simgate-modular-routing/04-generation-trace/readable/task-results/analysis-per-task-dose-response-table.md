# analysis per task dose response table

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_per-task-dose-response-table_20260518T194242_result.json`
- **Structured JSON:** [`723d78519e7fcf0263a8.json`](../../sessions/72/723d78519e7fcf0263a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出：

1. **LaTeX table**: `artifacts/appendix/per_task_dose_response_table.tex` — 10 个 death-prone task + Overall 行，Retry/Reflexion 各 N=1..5，最低值加粗
2. **JSON data**: `artifacts/appendix/per_task_dose_response_data.json` — 原始数据含来源说明

**Overall 验证全部通过：**
- Retry: 48.0 / 47.0 / 43.5 / **43.0** / 43.5 ✓
- Reflexion: 47.5 / 40.0 / **34.0** / 36.5 / 35.0 ✓

**关键发现：** 任务说明中 Reflexion N=1/N=2 标注为"从 N=5 数据 derive"，但实际在 westb-13313 上存在独立运行的 `reflexion_n1` 和 `reflexion_n2` 目录（各 200 episodes）。使用这些独立运行数据后 Overall 才与已知聚合值匹配。

---

# diagnosis ext val completion check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_ext-val-completion-check_20260519T220756_result.json`
- **Structured JSON:** [`de98dd485928d1f6b8ad.json`](../../sessions/de/de98dd485928d1f6b8ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态汇总：

**完成的任务**:
- **boil** 20/20: int DR=55%, det DR=25%, det-preferred 30%
- **use-thermometer** 20/20: int DR=50%, det DR=20%, det-preferred 35%

**运行中**:
- **find-living-thing** 6/20 (GPU 0, ~45min 后完成)
- **power-component** 6/20 (GPU 1, ~48min 后完成)

**需重跑**:
- **melt** 0/20 — vLLM EngineDeadError 崩溃，两块 GPU 都被占用，需等 find-living-thing 完成后在 GPU 0 上重跑

**关键发现**: 已完成的 40 个 episode 中，det-preferred 13 次，int-preferred 仅 1 次（det win rate 93%）。Internal routing 死亡率（52.5%）远高于 deterministic（22.5%）。趋势与原始 included tasks 一致，支持"排除这些 task 不是 cherry-picking"的论点。

状态报告已写入 `artifacts/extended-task-validation/status_report.md`。melt 的重启命令已在报告中准备好，等 GPU 0 空闲后可以执行。

---

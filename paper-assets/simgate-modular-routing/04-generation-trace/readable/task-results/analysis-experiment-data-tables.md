# analysis experiment data tables

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_experiment-data-tables_20260514T014313_result.json`
- **Structured JSON:** [`d38aaa6c2e44d4667021.json`](../../sessions/d3/d38aaa6c2e44d4667021.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/experiment_tables.md`，包含 4 张表：

1. **Table 1 — Death Decomposition**：使用 `death_decomposition_report.json` 的实际数值（episode-weighted Δ_full=+38.33, DAF=98.8%, r=0.986），task-weighted 列保留 registry 数值待验证
2. **Table 2 — Keyword Baseline**：v1/v2/v3 三版关键词列表全部结构性失效，附具体关键词清单和失效机制
3. **Table 3 — Label Distribution**：det-preferred 41.0%, no-preference 58.6%, internal-preferred 0.4%；附 plan-005 的 task-level taxonomy（25/30 death-dominated）
4. **Table 4 — Baseline Comparison**：always-internal −47.5, always-det −9.2, oracle pending

与 prompt 给定数字的主要修正：Δ_full 37.9→38.33, Δ_nd 0.2→0.48, DAF 99.1%→98.8%（均来自 report.json 实际计算值 vs registry 的四舍五入值）。全部标注 preliminary，plan-001b 完成后更新。

---

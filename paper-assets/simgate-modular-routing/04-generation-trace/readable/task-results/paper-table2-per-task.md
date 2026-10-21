# paper table2 per task

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_table2-per-task_20260514T145555_result.json`
- **Structured JSON:** [`bfd0935915be1bba38ca.json`](../../sessions/bf/bfd0935915be1bba38ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件都已更新完成。

**已完成的修改：**

1. **数据来源**：`artifacts/plan-012-full/data/death_decomposition_preliminary.csv` — 11 tasks, 245 episodes，总数验证一致（86/9/150 labels, Δ_full=29.60）

2. **`docs/paper/experiments.tex`**（主版本）：
   - 第 15 行：添加 `(Table~\ref{tab:per-task})` 引用
   - 第 47-73 行：插入 Table 2（`tab:per-task`），位于 baselines 讨论之后、Router Training 之前

3. **`artifacts/_project/paper/latex/experiments.tex`**（旧版本）：同步更新

**Table 2 设计**：
- 11 行 task data + aggregate 行，按 Δ_full 降序排列
- `find-non-living-thing` 用 `\midrule` 分隔并标注 `†`（唯一零死亡 task）
- 列：Task | n | Δ_full | D%_int | D%_det | D/I/N
- 使用 `\scriptsize` + `\setlength{\tabcolsep}{2.5pt}` 压缩空间

---

# paper docred beam table fill

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_docred_beam_table_fill_20260520T140058_result.json`
- **Structured JSON:** [`86727a228ff2cbb6a02f.json`](../../sessions/86/86727a228ff2cbb6a02f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已更新。设计决策汇报：

**表格 (`beam_docred_sweep_table.tex`)**
- 双模型结构：Qwen 在上，Llama 在下，`\midrule` 分隔；模型内部用 `\cmidrule(l){2-8}` 分隔不同 k 值
- 8 列：Model / k / Mode / E-F1 / R-F1 / DR% / CF% / PF%，无 Latency
- 零违规行（Qwen k=8 con、Llama k=2 con、Llama k=8 con）的 DR 和 CF 均加粗
- 非零违规行中单独为 0 的值不加粗（与 SciERC 表格的"个别 DR=0 加粗"做法不同，遵循任务指定的严格规则）
- Sweet spot：Llama k=2 con 行 `\cellcolor{blue!8}`
- 缺失配置（Qwen k=4、Llama k=1/k=4）用 `---`（em-dash）

**Pareto 脚本 (`plot_pareto_dual.py`)**
- X 轴改为 Beam Width (k)，log₂ 刻度（1/2/4/8 等间距）
- 气泡大小 = `(DR + CF + RV) × 200`（scatter area），仅非零违规点显示半透明气泡
- 零违规点保留绿色环标记
- DocRED 面板展示 Llama 数据（更完整、R-F1 更高）；SciERC 面板展示 Qwen（已有完整数据）
- DocRED sweet spot 设为 Llama k=2 con（零违规 + 合理 R-F1）
- Qwen DocRED 数据在注释中标注可扩展

---

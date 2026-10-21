# paper docred beam table pareto

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_docred_beam_table_pareto_20260520T135434_result.json`
- **Structured JSON:** [`e540af50a279a153a315.json`](../../sessions/e5/e540af50a279a153a315.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已创建。

### 产出汇报

**1. `beam_docred_sweep_table.tex`**
- 与 `tab:beam-sweep` (SciERC) 完全一致的列结构：k, Mode, E-F1, R-F1, DR(%), CF(%), Latency(s), Rel. Lat.
- 8 行数据（k∈{1,2,4,8} × {unc, con}），用 `--` 占位
- beam=2 con 行用 `\cellcolor{blue!8}` 高亮（sweet spot 候选）
- beam=8 con 的 DR/CF 已填入 **0**（已确认数据），加粗处理
- label: `tab:beam-docred-sweep`，caption 标注 "200 documents" + Llama-3.1-8B LoRA

**2. `plot_pareto_dual.py`**
- 双面板 `(10, 4)` 图，左 SciERC（数据已填）/ 右 DocRED（`None` 占位）
- X 轴 Relative Latency（`%.1f×` 格式），Y 轴 R-F1
- unc 灰色圆点 / con 蓝色方块，每个点标注 beam width
- 绿色空心环标注 zero-violation 点（DR=0% AND CF=0%）：SciERC 的 k=4 con 和 k=8 con
- 红色星号标注 sweet spot（SciERC beam=2 unc R-F1=44.75）
- 学术 serif 字体，输出 PDF + PNG
- DocRED 的 `sweet_spot` 参数留 `None`，数据到齐后填入即可

---

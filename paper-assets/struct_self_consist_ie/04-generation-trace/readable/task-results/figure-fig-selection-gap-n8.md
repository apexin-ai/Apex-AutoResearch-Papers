# figure fig selection gap n8

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fig_selection_gap_n8_20260515T151205_result.json`
- **Structured JSON:** [`7aea8d4bcd63be87f2f9.json`](../../sessions/7a/7aea8d4bcd63be87f2f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。图已生成并部署到所有目标位置。

**数据更新汇总：**

| | 旧值 | 新值 (统一管道 2-seed mean) |
|---|---|---|
| NER ρ SJ | 0.360 | **0.374** |
| NER ρ VC | 0.379 | **0.396** |
| NER ρ LP | 0.205 | **0.220** |
| NER ΔF1 VC | -1.0 pp | **-2.2 pp** |
| NER ΔF1 LP | +0.6 pp | **+0.2 pp** |
| NER greedy | 0.6439 | **0.6448** |
| NER oracle | 0.7758 | **0.7782** |
| NER random | 0.6077 | **0.6101** |
| RE ρ SJ | 0.249 | **0.250** |

**未变更项：** NER bootstrap CI（仅 seed42 可用），RE ΔF1 和 RE ρ VC/LP（无 seed123 RE 数据）。

**文件位置：**
- 论文目录: `docs/paper/figures/fig_selection_gap.pdf`
- 本地 artifacts: `artifacts/figures/fig_selection_gap.{pdf,png}`
- 脚本: `output/review_round2/plot_selection_gap_n8.py`

---

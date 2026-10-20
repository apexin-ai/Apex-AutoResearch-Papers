# code fig selection gap ner only

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fig_selection_gap_ner_only_20260519T034814_result.json`
- **Structured JSON:** [`3d4985422c09cbacbde1.json`](../../sessions/3d/3d4985422c09cbacbde1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 汇报

### 数据值（SciERC NER, N=8, T=1.0）

| Signal | Spearman ρ | ΔF1 vs Greedy (pp) |
|--------|-----------|-------------------|
| SJ | 0.360 | -0.45 ± 1.03 |
| FK | 0.267 | -0.46 ± 0.97 |
| EM | 0.299 | -1.19 ± 0.73 |
| VC | 0.252 | -2.65 ± 0.88 |
| LP | 0.205 | +0.04 ± 0.50 |

- Oracle: +13.05 pp | Random: -3.90 pp
- ρ 来源: `exp_016_rerun_1024/correlation_matrix.json` (seed42, n=529)
- ΔF1 来源: `analysis_multiseed_selection_f1.json` (3 seeds: 42/123/456)

### 路径
- 远程: `output/figures/fig_selection_gap.pdf` + `docs/paper/figures/fig_selection_gap.pdf`
- 本地: `docs/paper/figures/fig_selection_gap.pdf`
- 旧版备份: `docs/paper/figures/fig_selection_gap_dual_panel.pdf`
- 生成脚本: `code/plot_selection_gap_single.py`

### 与旧图差异
- 旧图: 单面板只有 ΔF1 柱状图（3 信号 VC/SJ/LP）
- 新图: 单面板双 Y 轴，蓝柱 = Spearman ρ，红线 = ΔF1，**5 个信号全部包含**（新增 FK、EM），Oracle/Random 参考线

---

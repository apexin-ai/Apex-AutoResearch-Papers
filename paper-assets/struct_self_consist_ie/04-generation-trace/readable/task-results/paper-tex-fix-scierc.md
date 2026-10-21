# paper tex fix scierc

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_tex-fix-scierc_20260525T202104_result.json`
- **Structured JSON:** [`139ca6d7d91930d40c5f.json`](../../sessions/13/139ca6d7d91930d40c5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

经过全面检查，**编译版本（docs/paper/sections/）中所有 SciERC NER 数据已经是正确值，不需要修改。**

具体核查结果：

### Table 数据
- `tab:quality_estimation` 只存在于 `artifacts/_project/paper/experiments.tex`（旧版残留，不参与编译）和 `_archived/experiments_OLD.tex`（已归档，已有正确值）
- 编译版本使用 `tab:multiseed`（appendix.tex L723），多 seed 均值与单 seed 值一致方向

### 正文引用（experiments_main.tex）
- L31: `VC $\rho{=}0.379$, SJ $0.360$) over LP ($0.205$)` — 已正确

### abstract.tex
- 无 SciERC NER 的具体 ρ/AUROC 数值（仅提 "AUROC up to $0.82$"，这是 CoNLL EM）

### introduction.tex
- 无 .50 或 .73 的 SciERC NER 引用
- fig_overview caption 写明 "AUROC from CoNLL EM; ρ from Few-NERD"

### conclusion.tex / discussion.tex
- 无 SciERC NER 具体 ρ/AUROC 值

### single_signal.tex
- fig_selection_gap caption L34: "$\rho$ up to 0.38" — 已正确

### 旧值搜索
- `.502` — 仅在 appendix RE 高复杂度子集（SJ $\rho{=}0.502$），非 SciERC NER QE
- `.728` — 仅在 appendix 温度消融表（不同上下文）
- `.559` — 仅在 mechanistic probing 跨数据集 AUROC（LODO），非 QE

### 结论
**artifacts/_project/paper/experiments.tex** 仍有旧值（.502、.728 等），但根据约束 C001 禁止修改该文件（旧版残留，不参与编译）。编译版本 docs/paper/sections/ 已全部更新完毕，无需任何改动。

---

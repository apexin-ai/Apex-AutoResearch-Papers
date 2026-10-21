# analysis fig3 final option a

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fig3_final_option_a_20260517T091328_result.json`
- **Structured JSON:** [`0206ae9cc752c9130206.json`](../../sessions/02/0206ae9cc752c9130206.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All tasks complete. Summary:

**子任务 1: Figure 3 重绘 (Option A)**
- PDF/PNG saved: `output/figures/fig_degeneracy_lp_scatter.{pdf,png}`
- Script updated: `output/figures/plot_degeneracy_lp.py`
- Cross-dataset: CoNLL (47.4%, -1.05), SciERC (17.8%, +0.62), Few-NERD (13.8%, +1.36)
- Per-type: original KeySet x values [5.97–19.81%]

**子任务 2: Spearman ρ**

| Subset | ρ | p |
|--------|------|------|
| 11-point global | -0.5182 | 0.1025 |
| Per-type (n=8) | -0.3810 | 0.3518 |
| Dataset-level (n=3) | -1.0000 | — |

**注意**: Per-type ρ = -0.381, **不是** 预期的 -0.881。原因：原始 KeySet x 值范围窄 (5.97–19.81%)，且 "other" 类型是 outlier (degeneracy 仅 6.61% 但 LP delta 高达 +4.73pp)，破坏了单调关系。论文 line 171 目前写的 ρ=-0.881 是用 Constant F1 x 值计算的结果（但用 CF1 x 重算也只得到 -0.286）。这个数字可能来自更早版本的分析，需要 Director 决定如何处理。

**子任务 3: tex 修改**
- `docs/paper/sections/experiments.tex` line 175: `11.1%` → `14.6%`, `4.5%` → `7.0%` ✓

**额外发现需 Director 决定**:
- Line 151: `+0.42~pp` → 应改为 `+0.62~pp`？
- Line 171: `ρ=-0.881, p=0.004` → 实际值不符，需确认正确来源

---

# code merge fig2 fig3

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_merge-fig2-fig3_20260529T015457_result.json`
- **Structured JSON:** [`ca9e63a075cd4ac62a0f.json`](../../sessions/ca/ca9e63a075cd4ac62a0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**改动摘要**：

1. **新建合并脚本** `docs/paper/figures/fig_combined_factorial_gradient.py` — figsize (7.0, 3.2)，左 33% 为 (a) factorial 交互图，右 67% 为 (b) gradient 2×2 四子图。颜色方案统一，字号 ≥ 6.5pt。

2. **输出文件**：`fig_combined_factorial_gradient.pdf` 和 `.png`，数据均正确（BN OFF=0.767, ON=0.725; LN OFF=0.802, ON=0.773; Vanilla=0.745）。

3. **LaTeX 更新** (`results.tex`)：
   - 原 Fig 2 (`fig:factorial`) 和 Fig 3 (`fig:gradient_analysis`) 注释保留，合并为一个 `figure*` 环境，label `fig:factorial_gradient`
   - Caption 合并了两图描述

4. **全局引用更新**：`results.tex`、`introduction.tex`、`discussion.tex`、`appendix.tex` 中所有 `\ref{fig:factorial}` → `\ref{fig:factorial_gradient}a`，所有 `\ref{fig:gradient_analysis}` → `\ref{fig:factorial_gradient}b`。无残留旧引用。

---

# paper figure fig grpo dynamics fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig_grpo_dynamics_fix_20260517T183654_result.json`
- **Structured JSON:** [`9f4c73c8b3517bed59ad.json`](../../sessions/9f/9f4c73c8b3517bed59ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两项修改：

1. **图表术语修正**：Panel (c) 标题 "Distractor Citation Rate" → "Evidence-Decoupling Ratio (EDCR)"，红色区域注释 "Near-total distractor citation" → "Near-total decoupling"。重新生成的 PDF/PNG 已覆盖 `artifacts/_project/chart/` 并复制到 `figures/paper/`。

2. **appendix.tex 更新**：注释掉的占位 section 替换为正式的 `\begin{figure*}` 环境，caption 使用 "EDCR" 和 "Evidence-Decoupling Ratio"，与 method.tex 术语统一。绘图脚本保留在 `figures/paper/plot_fig_grpo_dynamics.py`。

---

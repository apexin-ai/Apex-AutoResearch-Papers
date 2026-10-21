# paper figure fig1 pipeline

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig1_pipeline_20260518T092246_result.json`
- **Structured JSON:** [`b80a9201226c57ed5900.json`](../../sessions/b8/b80a9201226c57ed5900.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

fig1_pipeline 已生成并注册 (`art_20260518_d51425`)。

**修正内容**：
- "Conformal Selection" → "Argmin Selection"
- "argmin Mahalanobis" → "argmin L2 to mean"
- "~330K params, ~3ms" → "~327K params, <1ms"
- "z_obs (960D embedding)" → "z_obs (960D) + a_base (30D) = 990D input"

**输出**：
- PDF: `artifacts/figures/paper/fig1_pipeline.pdf`
- PNG: `artifacts/figures/paper/fig1_pipeline.png`
- 生成脚本: `artifacts/figures/paper/gen_fig1_pipeline.py`

---

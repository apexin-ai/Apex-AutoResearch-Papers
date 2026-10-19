# paper fig copy to docs

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fig_copy_to_docs_20260517T021535_result.json`
- **Structured JSON:** [`00df500329be0f49b10a.json`](../../sessions/00/00df500329be0f49b10a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有设置 `\graphicspath`，LaTeX 默认从主 tex 文件所在目录搜索。`main.tex` 在 `docs/paper/`，图片在 `docs/paper/figures/`，路径 `figures/fig2_temporal_improvement.pdf` 是相对于 `docs/paper/` 的，可以正确找到。

完成。汇报：

**复制结果：**
- `fig2_temporal_improvement.pdf` (17,572 bytes) → `docs/paper/figures/`
- `fig3_model_dependency.pdf` (20,618 bytes) → `docs/paper/figures/`

**tex 修改：**
- `sections/experiments.tex` 第 13 行：placeholder → `\includegraphics[width=\columnwidth]{figures/fig2_temporal_improvement.pdf}`
- `sections/experiments.tex` 第 82 行：placeholder → `\includegraphics[width=\columnwidth]{figures/fig3_model_dependency.pdf}`

路径与 `main.tex` 编译目录一致，无需额外配置。

---

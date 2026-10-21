# paper latex setup

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_latex-setup_20260514T112730_result.json`
- **Structured JSON:** [`fc5e8b62dbb1da058887.json`](../../sessions/fc/fc5e8b62dbb1da058887.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出：

- **`docs/paper/main.tex`** — 使用 `geometry`+`times` 替代缺失的 `acl.sty`，包含 `booktabs`/`graphicx`/`amsmath`/`hyperref`/`natbib`，按顺序 `\input` 六个章节文件
- **`docs/paper/experiments.tex`** — 在 `\subsection{Death Avoidance Decomposition}` 开头添加了 `fig:decomposition` 的 figure 环境，引用 `figures/fig1_daf_scatter.pdf`
- **`docs/paper/SETUP_NOTES.md`** — 说明如何获取 ACL 模板文件、放置图片、以及编译命令

注意：编译前需要将 `fig1_daf_scatter.pdf` 放入 `docs/paper/figures/` 目录，并下载 `acl_natbib.bst`（否则需改用 `plainnat` 等标准 bst）。

---

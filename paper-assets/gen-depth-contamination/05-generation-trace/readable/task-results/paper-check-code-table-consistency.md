# paper check code table consistency

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_check-code-table-consistency_20260519T034403_result.json`
- **Structured JSON:** [`ef70ce3985eb26710458.json`](../../sessions/ef/ef70ce3985eb26710458.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits complete. Here's the modification summary:

---

**修正清单：**

| # | 文件 | 行 | 原文 | 修正 |
|---|------|-----|------|------|
| 1 | `main.tex` | 40 | `K*=2 for...and code` | `K*=1--2 for code (Python, model-dependent)` |
| 2 | `main.tex` | 72 | `code domain tested with one model (Qwen2.5-1.5B)` | `two models (Qwen2.5-1.5B, K*=2; Pythia-1.4B, borderline K*=1)` |
| 3 | `conclusion.tex` | 4 | `K*=2 for code (Python)` | `K*=1--2 for code (Python, two models)` |
| 4 | `discussion.tex` | 35 | `Python code yields K*=2 (1v2 auc=0.74)` | 分拆为 Qwen K*=2 和 Pythia borderline K*=1，带 CI |
| 5 | `discussion.tex` | 36 | `Code and C4 share K*=2` | `For Qwen, code and C4 share K*=2`，新增 Pythia 段落 |
| 6 | `introduction.tex` | 29 | `C4/Code (K*=2) > Wikipedia (K*=1)` | `C4 (K*=2) ≥ Code (K*=1--2) ≥ Wikipedia (K*=1)` |
| 7 | `experiments_c1.tex` | 141-142 | 仅 Qwen 结果 | 新增 Pythia K*=1 结果及引用 `tab:code_crossmodel_kstar` |
| 8 | `experiments_c1.tex` | 145-146 | `C4/Code (K*=2) > Wikipedia` | `C4 (K*=2) ≥ Code (K*=1--2) ≥ Wikipedia (K*=1)`，softened universality claim |
| 9 | `experiments_c1.tex` | 151 | caption 无 ‡ 注 | 新增 `‡Borderline: 1v2 auc=0.598, CI upper=0.603>θ` |
| 10 | `experiments_c1.tex` | 160 | `Pythia-1.4B & 2 & --- & 3 & 1` | `Pythia-1.4B & 2 & 1‡ & 3 & 1` |
| 11 | `appendix_extended.tex` | 584+ | 无 cross-model 表 | 新增 2-model cross-model 比较表 (`tab:code_crossmodel_kstar`) |
| 12 | `artifacts/code_crossmodel_table.tex` | 5 | `five model families` | `five models (four architecture families)` |

**关键叙事调整**：Pythia Code K\*=1 是 borderline result（1v2 AUC=0.5983，CI upper=0.603 跨 θ=0.60），各处均标注 borderline 而非 hard negative。domain ordering 从 strict `>` 改为 `≥`，"invariance" 降级为 "ordering"。

---

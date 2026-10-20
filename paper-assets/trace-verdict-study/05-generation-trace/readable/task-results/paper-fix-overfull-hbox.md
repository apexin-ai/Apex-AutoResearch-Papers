# paper fix overfull hbox

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_overfull_hbox_20260519T172710_result.json`
- **Structured JSON:** [`75a13909b90fbb4ea73a.json`](../../sessions/75/75a13909b90fbb4ea73a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 处全部修复完成。

| # | 位置 | 超出 | 修复 |
|---|------|------|------|
| 1 | experiments.tex:129-138 (density 表) | 20.1pt | `\resizebox{\columnwidth}{!}` 包裹 |
| 2 | experiments.tex:168 (calibration 段落) | 13.1pt | 微调措辞：`achieves ECE = 0.0027 vs.\ 0.171 for \texttt{no\_trace}` |
| 3 | appendix.tex:447-457 (head\_vs\_tail 表) | 31.2pt | `\resizebox{\columnwidth}{!}` 包裹 |
| 4 | appendix.tex:474-486 (tail512\_seeds 表) | 54.2pt | `\resizebox{\columnwidth}{!}` 包裹 |
| 5 | appendix.tex:695-710 (regex 表) | 72.5pt | `\resizebox{\columnwidth}{!}` 包裹 |
| 6 | appendix.tex:752-764 (zeroshot 表) | 32.4pt | `\resizebox{\columnwidth}{!}` 包裹 |

5 个表格用 `\resizebox` 自动缩放至列宽；1 处段落文本通过微调措辞消除长 `\texttt{}` 导致的断行问题。所有修改不改变内容含义，不增加页数。

---

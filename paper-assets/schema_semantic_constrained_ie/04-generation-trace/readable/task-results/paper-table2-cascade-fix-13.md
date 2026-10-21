# paper table2 cascade fix 13

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_table2_cascade_fix_13_20260520T113317_result.json`
- **Structured JSON:** [`6bef05c2ee966e3edc23.json`](../../sessions/6b/6bef05c2ee966e3edc23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 修改报告

### 修改清单（4处）

| # | 文件 | 行 | 旧值 | 新值 |
|---|------|-----|------|------|
| 1 | `abstract.tex` | 6 | `eliminates DR violations` | `near-eliminates DR violations (DR $\leq$ 0.21\%)` |
| 2 | `section1_introduction_draft.tex` | 22 | `eliminates DR` | `near-eliminates DR ($\leq$ 0.21\%)` |
| 3 | `section3_violation_landscape.tex` | 8 | `eliminating DR violations` | `near-eliminating DR violations` |
| 4 | `section5_crossmodel_draft.tex` | 59 | `DR\,$\leq$\,0.20\%` | `DR\,$\leq$\,0.21\%` |

### 验证结果

**编译**: 0 errors, 32 pages, 504264 bytes.

**grep (a) DR context 0.20 残留**: 空 — 无残留。

**grep (b) "eliminates/eliminating DR" 残留**: 剩余出现均合法：
- `appendix_beam_search.tex:59,60` — beam search 确实将 DR 降到 0%，"eliminates" 事实正确
- `appendix_discussion.tex:193` — "Fine-tuning alone eliminates DR on four of seven relations"，描述具体 relation 级别的消除
- `section5_scierc_draft.tex:104` — "eliminates or near-eliminates DR"，Qwen LoRA 确实 DR=0%

**grep (c) 44.23 / 0.51 残留**: 均合法：
- `appendix_beam_search.tex:135`, `section5_scierc_draft.tex:110` — R-F1=44.23 是 Qwen SciERC beam 结果
- `appendix_discussion.tex:260` — 0.51 是 per-relation 表格中的 Grammar 行 CF 值，非 ΔDR

**grep (d) "eliminat" + DR context**: 所有剩余出现均为合法用法（beam DR→0%、ET/RV 消除、per-relation 细节、DEPRECATED 文件）。

---

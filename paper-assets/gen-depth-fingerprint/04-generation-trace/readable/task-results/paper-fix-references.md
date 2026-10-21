# paper fix references

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix-references_20260525T082406_result.json`
- **Structured JSON:** [`ec0ba3c92278d20053b7.json`](../../sessions/ec/ec0ba3c92278d20053b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

BibTeX: 0 warnings. Compilation successful (PDF output on 35 pages, 0 bibtex warnings).

---

## 汇报：10 个条目验证结果

| # | Key | 结果 | 修正内容 |
|---|-----|------|---------|
| 1 | `cohen1988statistical` | ✓ 已正确 | 无需修改。2nd ed, Lawrence Erlbaum Associates, 1988 均正确 |
| 2 | `paraphrase_evades` | ✓ 已正确 | NeurIPS 2023, 作者/标题均正确 |
| 3 | `intrinsic_dim_detection` | ✓ 已正确 | NeurIPS 2023, 作者/标题均正确 |
| 4 | `self_consuming_mad` | ✓ 已正确 | ICLR 2024, 8位作者均正确 |
| 5 | `dsir` | ✓ 已正确 | NeurIPS 2023, Xie/Santurkar/Ma/Liang 均正确 |
| 6 | `nucleus_sampling` | ✓ 已正确 | ICLR 2020, 作者/标题均正确 |
| 7 | `qwen3` | **已修正** | author: `{Qwen Team}` → 个人作者列表 `Yang, An and Li, Anfeng and ... and others`（与 arXiv 元数据一致，与 `llama3` 条目风格统一） |
| 8 | `gutierrez_ordinal_survey` | ✓ 已正确 | IEEE TKDE 28(1):127-146, 2016, 作者含正确 LaTeX 重音符 |
| 9 | `diaz_soft_labels_ordinal` | **已修正** | author: `Diaz, Raul` → `D{\'i}az, Ra{\'u}l`（论文 PDF 原文使用重音符，与 bib 中 gutierrez 条目风格一致） |
| 10 | `llama3` | ✓ 已正确 | arXiv preprint 2407.21783, 2024, 未正式发表于会议/期刊 |

---

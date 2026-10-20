# paper arr submission checklist

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_arr_submission_checklist_20260522T092331_result.json`
- **Structured JSON:** [`82bc7b8f497b9a91ff4c.json`](../../sessions/82/82bc7b8f497b9a91ff4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the full report:

---

## EMNLP 2026 ARR May 提交材料检查报告

### 1. 格式合规检查

| 项目 | 状态 | 详情 |
|------|------|------|
| Review mode | ✓ | `\usepackage[review]{acl}` |
| 匿名 | ✓ | `\author{Anonymous}` |
| Limitations | ✓ | `\section*{Limitations}`（unnumbered，`\clearpage` 后） |
| Ethics Statement | ✓ | `\section*{Ethics Statement}`（unnumbered） |
| 正文破折号 | ✓ | 正文 7 个 tex 文件中无 `---`（em-dash） |
| Checklist 不在 PDF 中 | ✓ | main.tex 中无 checklist 内容 |

### 2. 正文页数

从 `main.aux` 中提取的 section 页码：

| Section | 页码 |
|---------|------|
| 1 Introduction | 1 |
| 2 Related Work | 2 |
| 3 Method | 2 |
| 4 Experiments | 4 |
| 5 K*-Guided Filtering | 6 |
| 6 Discussion | 7 |
| 7 Conclusion | 8 |

Conclusion 仅 ~8 行，完全在第 8 页内。`\clearpage` 在 Conclusion 之后、Limitations 之前，确保 Limitations 从第 9 页开始。

**正文（Abstract 到 Conclusion）= 8 页 ✓**（恰好踩线）

### 3. Supplementary / Appendix

- Appendix 包含在主 PDF 中（`\appendix` → `appendix.tex` + `appendix_extended.tex`）
- Appendix 章节：A (Supplementary Figures), B (Supplementary Tables), C (Supplementary Details), D (Extended Discussion)
- **总 PDF 页数：23 页**（`\@abspage@last{23}`）

### 4. 引用完整性

| 项目 | 状态 |
|------|------|
| Undefined references | ✓ 0 个 |
| Undefined citations | ✓ 0 个 |
| LaTeX Warnings | ✓ 0 个 |
| BibTeX Warnings | ✓ 0 个 |
| Bibliography entries | 36 条 |
| Citation commands | 34 处 |

### 5. 图表编号

**正文**：Figure 1→2→3→4，Table 1→2→3→4→5 ✓ 连续

**Appendix**：Figure 5，Table 6→...→27 ✓ 连续

正文浮动体类型：
- 1 个 `figure*`（method.tex，pipeline 图）
- 1 个 `table*`（experiments_c1.tex，K* CI 表）
- 3 个 `figure`，1 个 `table`

### 6. 其他

| 项目 | 状态 | 详情 |
|------|------|------|
| Page numbers | ✓ | review mode 自动显示 |
| 字体 Type 1 | ⚠️ | `pdffonts` 不可用，无法确认。`times` + `T1` 编码通常生成 Type 1，大概率没问题 |
| Overfull hbox | ⚠️ | **11 处**，最大 58.6pt（严重）。部分可能在 appendix |

### 需要关注的项

1. **⚠️ 正文恰好 8 页**：没有余量。任何后续修改（加文字、调图表大小）都可能导致超页。建议冻结正文。

2. **⚠️ Overfull hbox 58.6pt**：这个溢出很大（约 2cm），reviewer 可能注意到。建议定位并修复最严重的几处（特别是正文部分的）。其他 10-20pt 的溢出在 review 阶段通常可接受。

3. **⚠️ 字体检查**：建议在有 `pdffonts`（poppler-utils）的环境下确认所有字体为 Type 1 / OTF，ARR 不接受 Type 3 位图字体。

---

# ops paper compile prep

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_paper_compile_prep_20260516T030841_result.json`
- **Structured JSON:** [`cb0d8831570ccca65547.json`](../../sessions/cb/cb0d8831570ccca65547.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集。

---

## 编译报告

### 1. fig4 状态
`fig4_trace_length.pdf` (17,819 bytes) **已存在**于 `/root/trace-verdict-study/figures/paper/`，路径匹配 `\graphicspath`。**但未被任何 tex 文件引用** —— 没有 `\includegraphics{fig4_trace_length}`。文件在磁盘上就位，但论文 PDF 中不会显示。如需纳入，需在 experiments.tex 或 discussion.tex 中添加 figure 环境。

### 2. 编译
**成功**，18 页 / 322,760 bytes。三遍 pdflatex + bibtex 无中断。

- **真正错误**: 3 个非致命（keyval `sargin`、caption `10pt`、级联 `\begin{document}`）—— TeX Live 2022 与 ACL 样式文件兼容性问题，不影响输出
- **BibTeX**: 0 警告，27 引用条目
- **Overfull hbox**: 8 个（表格排版溢出）
- **Underfull hbox**: 181 个（常规）

### 3. 页数
18 页 = 正文 ~13 页 + 参考文献 ~2 页 + 附录 ~3 页。**正文超出 EMNLP 8 页限制约 5 页**（review 模式含行号，camera-ready 会略短，但仍可能超限）。

### 4. Paired Bootstrap 完整性

| 分组 | 条件数 | 期望对数 | 实际对数 | 状态 |
|------|--------|---------|---------|------|
| Qwen (n=1190) | 8 | 28 | 28 | 完整 |
| DebugBench (n=426) | 3 | 3 | 3 | 完整 |
| DeepSeek (n=1190) | 4 | 6 | 3 | **缺 3 对** |

DeepSeek 缺少 full_trace 相关配对：`VOTA↔full_trace`、`exception_only↔full_trace`、`no_trace↔full_trace`。

### 5. 需关注项
1. fig4 需要在 tex 中添加引用才能出现在论文中
2. 正文页数显著超限
3. DeepSeek paired bootstrap 缺 3 对 full_trace 配对

---

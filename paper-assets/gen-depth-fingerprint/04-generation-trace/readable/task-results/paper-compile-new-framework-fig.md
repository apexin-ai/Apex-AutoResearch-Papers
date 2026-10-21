# paper compile new framework fig

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compile-new-framework-fig_20260523T053538_result.json`
- **Structured JSON:** [`967a1d49f0ae53ce61d9.json`](../../sessions/96/967a1d49f0ae53ce61d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译和验证完成，汇报如下：

**编译结果**: 成功，无 fatal error，无 LaTeX warning。

**页数**: 37 页（正文 8 页 + 附录）。Conclusion 在 p8，符合 EMNLP 8 页限制。

**框架图布局**: Figure 1 在 p2 顶部全宽显示，位于 Introduction 结束、Method section 开始之间，位置合理。图中三部分 (a) Recursive generation chain → (b) Feature extraction → (c) LOGO evaluation 清晰可读，信息密度高。

**Type 3 字体**: 存在 5 个 Type 3 字体：
- `DejaVuSerif-Bold` (p649)
- `DejaVuSerif` (p648)  
- `Cmmi10`, `Cmr10`, `Cmsy10` (p649-651)

这些很可能来自框架图 PDF 中嵌入的字体。投稿前需要消除——生成框架图时应确保所有文字使用 Type 1 或 TrueType 字体（matplotlib 中设置 `pdf.fonttype: 42`）。

---

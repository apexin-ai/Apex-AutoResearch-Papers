# paper narrative fix group analysis

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_narrative_fix_group_analysis_20260515T232155_result.json`
- **Structured JSON:** [`65cd534ccc50abae451c.json`](../../sessions/65/65cd534ccc50abae451c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

服务器文件内容正确。

---

## 修改报告

### 任务 1: appendix.tex 措辞修复
- **文件**: `appendix.tex`
- **行号**: 199
- **修改**: `label truncation bug` → `label truncated (context overflow)`
- **与 experiments.tex L30 脚注一致**: 脚注使用 "the verdict label to be truncated during training"，现在两处均表述为 tokenizer 导致的 context overflow 截断，而非软件 bug

### 任务 2: experiments.tex group analysis 定量证据
- **文件**: `experiments.tex`
- **行号**: 41（新增，原 L40 之后）
- **插入内容**:
  > However, a post-hoc group analysis provides directional evidence: partitioning DeepSeek VOTA test samples by whether their training-set counterparts exceeded the context window, intact samples ($N{=}99$) achieve 100\% accuracy while truncated samples ($N{=}1{,}091$) achieve 83.04\% (95\% CI [80.75\%, 85.24\%]; Fisher exact $p{<}0.001$), with all 185 errors concentrated in the fail class of the truncated group (fail recall $=$ 31.23\%).
- **位置**: §4.1 Cross-Model Comparison 正文，紧跟 "the two factors cannot be disentangled in the current design." 之后

### 任务 3: LaTeX 编译验证
- 本地 `pdflatex` 编译成功，输出 13 页 PDF
- 无编译错误（`!` 级别）
- 仅有标准 warning（label rerun、underfull hbox），无新增 warning

---

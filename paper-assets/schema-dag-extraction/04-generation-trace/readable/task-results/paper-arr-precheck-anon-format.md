# paper arr precheck anon format

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_arr_precheck_anon_format_20260522T072452_result.json`
- **Structured JSON:** [`b5890e6457cc10f67e13.json`](../../sessions/b5/b5890e6457cc10f67e13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks complete. Here's the report:

---

## ARR 提交预检报告

### 1. Anonymization

**a) Author: PASS**
- `main.tex:19` → `\author{Anonymous}`
- `supplementary.tex:13` → `\author{Anonymous}`
- 无真名、无机构名泄露

**b) Acknowledgments: PASS**
- 全文无 `\section*{Acknowledgments}` 或致谢内容
- 无 funding/grant/NSF/NSFC 信息

**c) Code URLs: PASS**
- 作者 .tex 文件中无 github.com / gitlab / huggingface.co / zenodo URL
- `acl.sty:4` 有 ACL style repo 注释，属于模板文件，无影响

**d) PDF metadata: PASS**
- PDF Author 字段：空
- PDF Title 字段：空
- 无 `\pdfinfo` 或 `\hypersetup{pdfauthor=...}` 设置

**e) Other leaks: PASS**
- 无 "our previous work" / "we previously showed" 等自引泄露
- 无 `/home/username/` 等文件路径泄露（`main.fls` 含本地路径，但属编译产物，不提交）

---

### 4. Format

**a) Style: PASS**
- `main.tex:3` → `\usepackage[review]{acl}` ✓
- 使用 ACL style（`acl.sty` 来自 acl-org/acl-style-files）

**b) Pages: PASS**
- Limitations 从第 8 页中段开始，References 在第 10 页
- 正文（不含 Limitations）≤ 8 页，符合 EMNLP 2026 要求
- 注：Limitations 占近 2 页（5 条 + 2 段），偏长（EMNLP 2026 惯例 3 点左右即可），但不计入页数限制

**c) References: WARN**
- 所有条目均有 title / author / year / venue（booktitle 或 journal）✓
- arXiv preprint 均标注了 arXiv ID ✓
- **27 个 @inproceedings 条目缺少 pages 字段**（常见但可能被 Reviewer 标记）：
  `golde-2025-familiarity`, `baan-2023-ecological`, `llm-pee-2025`, `parse-2025`, `crossagentie-2025`, `cmas-ner-2025`, `uniner-2024`, `gollie-2024`, `gliner-2024`, `gliner2-2025`, `dror-2018-significance`, `knowcoder-2024`, `slot-2025`, `ethayarajh-contextual-2019`, `cai-isotropy-clusters-2021`, `codeie-2023`, `adelie-2024`, `oneke-2025`, `fewnerd-2021`, `fewrel-2018`, `maven-2020`, `docred-2019`, `sentence-bert-2019`, `minilm-2020`, `sclar-sensitivity-2024`, `vllm-2023`, `xie-zeroshot-ner-2023`
- **BibTeX 警告**：`guo-2021-label-confusion` 同时使用了 volume 和 number 字段（不影响输出，但建议移除 number）
- 2 个 arXiv preprint 可能已正式发表需要更新：`instructuie-2023`（2023 年 arXiv）、`promptner-2023`（2023 年 arXiv）

**d) Review mode: PASS**
- `\usepackage[review]{acl}` 自动启用行号（`acl.sty:19`：review 选项设置 `\acl@linenumberstrue`）
- 无 camera-ready 专用设置（无 `final` 选项、无 `\acl@finalcopytrue`）

---

### 总结

| 检查项 | 状态 |
|--------|------|
| 1a Author | PASS |
| 1b Acknowledgments | PASS |
| 1c Code URLs | PASS |
| 1d PDF metadata | PASS |
| 1e Other leaks | PASS |
| 4a Style | PASS |
| 4b Pages | PASS |
| 4c References | WARN — 27 条缺 pages，2 条 arXiv 可能已正式发表 |
| 4d Review mode | PASS |

唯一需要处理的是 references.bib 中缺失的 pages 字段。建议至少为核心引用（数据集、主要 baseline）补全 pages。

---

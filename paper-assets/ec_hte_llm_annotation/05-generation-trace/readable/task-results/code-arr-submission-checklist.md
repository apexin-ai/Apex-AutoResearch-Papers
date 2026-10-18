# code arr submission checklist

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_arr-submission-checklist_20260522T024733_result.json`
- **Structured JSON:** [`a4949c2b6c5777afe1d1.json`](../../sessions/a4/a4949c2b6c5777afe1d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## ARR 提交 Checklist 检查结果

> **前置警告：`paper/` 目录下的 `main.tex` 是 ACL LaTeX 模板示例文件，不是实际研究论文。** 标题为 "Instructions for *ACL Proceedings"，内容为 LaTeX 格式说明。以下检查基于该模板文件。

---

### 检查汇总

| 检查项 | 状态 | 详情 |
|--------|------|------|
| **1. 格式合规** | | |
| documentclass | ✅ | `\documentclass[11pt]{article}` 正确 |
| 模板文件 | ✅ | `acl.sty` + `acl_natbib.bst` 齐全 |
| review 模式 | ✅ | `\usepackage[review]{acl}` 正确，匿名模式 |
| `\aclfinalcopy` | ✅ | 未出现 |
| 字体 | ✅ | `\usepackage{times}` 正确 |
| 主文页数 | ✅ | 4 页总计（含 appendix），主文约 3 页，远低于 8 页限制 |
| Abstract 字数 | ✅ | ~50 words，远低于 250 上限 |
| **2. 匿名化** | | |
| 作者信息 | ✅ | 使用占位符 "First Author" / "Second Author"，无真实姓名 |
| 机构名称 | ✅ | 无真实机构名 |
| `\thanks` | ✅ | tex 中未使用 `\thanks` 暴露身份 |
| 个人链接 | ✅ | 无 github/个人网站链接 |
| 自引模式 | ✅ | 未检测到 |
| Acknowledgments | ❌ | **包含真实人名**（Steven Bethard, Ryan Cotterell, Rui Yan 等十余人）——审稿阶段必须删除或注释掉 |
| **3. Supplementary** | | |
| Appendix | ✅ | 在 main.tex 中通过 `\appendix` 包含 |
| Limitations | ✅ | `\section*{Limitations}` 存在，内容简短（3 行） |
| Ethics Statement | ⚠️ | 未包含（可选但推荐） |
| ARR Checklist 在 PDF 中 | ✅ | PDF 中无 checklist（正确——应在 OpenReview form 填写） |
| **4. References** | | |
| undefined citation | ✅ | 0 个 |
| "?" 引用 | ✅ | 0 个 |
| bib 条目完整性 | ✅ | 7 个条目，均有 author/title/year |
| bib 格式 | ✅ | 无明显格式问题 |
| **5. 编译** | | |
| 编译 errors | ✅ | 0 |
| undefined references | ✅ | 0 |
| multiply-defined labels | ✅ | 0 |
| overfull hbox | ✅ | 0 |
| underfull hbox | ✅ | 4 个，均非严重（最大 badness 10000 在 URL 行，正常） |
| 总页数 | — | 4 页（含 appendix） |
| **6. PDF metadata** | | |
| Author 字段 | ✅ | 为空，不泄露身份 |
| Title 字段 | ⚠️ | 为空（建议用 `\pdfinfo` 设置论文标题） |

---

### 需修复问题（按严重度排序）

**Critical:**
1. **这不是实际论文，是 ACL 模板示例文件。** `\title{Instructions for *ACL Proceedings}` 和全部正文都是格式说明。需要替换为实际研究内容。

**Major:**
2. **Acknowledgments 包含真实人名**（main.tex:345-362）——审稿提交阶段必须整段注释/删除，否则违反匿名要求。

**Minor:**
3. **缺少 Ethics Statement**——EMNLP 2026 可选但推荐，建议在 Limitations 后加 `\section*{Ethics Statement}`。
4. **PDF Title 为空**——建议在 preamble 添加 `\hypersetup{pdftitle={Your Paper Title}}` 提升可访问性。

---

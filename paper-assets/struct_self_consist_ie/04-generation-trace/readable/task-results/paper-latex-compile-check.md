# paper latex compile check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_latex-compile-check_20260519T204420_result.json`
- **Structured JSON:** [`cd86dbf1816032156474.json`](../../sessions/cd/cd86dbf1816032156474.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 编译报告

| 项目 | 结果 |
|------|------|
| **编译状态** | SUCCESS |
| **总页数** | 36 页 |
| **主文页数** | 8 页（第 1–8 页，符合 EMNLP 2026 限制） |
| **未定义引用** | 0 |
| **编译错误** | 0 |

### Warning 分类

| 类别 | 数量 | 严重程度 |
|------|------|---------|
| Overfull hbox | 24 个，**全部在 appendix.tex** | 低（不影响主文排版；appendix 表格溢出常见） |
| Severe underfull (badness ≥ 5000) | 13 个，均在 appendix | 低（字间距过松，排版瑕疵） |
| Float specifier `h` → `ht` | 3 个 | 可忽略 |
| hyperref math-in-PDF-string | 4 个 | 可忽略（PDF 书签中数学符号警告） |

### 关键发现

- **主文 0 个 overfull hbox**——排版干净
- Appendix 有几个严重溢出（>80pt）：`appendix.tex:104–113` (84pt)、`appendix.tex:1049–1060` (113pt)、`appendix.tex:1289–1303` (109pt)——这些是宽表格，需要 `\resizebox` 或 `\small` 修复
- 72 个引用全部正确解析

### PDF 备份
`artifacts/paper_compiled_20260519.pdf` (768KB)

---

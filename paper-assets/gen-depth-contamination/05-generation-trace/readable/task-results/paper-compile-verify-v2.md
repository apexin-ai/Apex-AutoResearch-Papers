# paper compile verify v2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compile-verify-v2_20260519T114356_result.json`
- **Structured JSON:** [`28f558fd38263cfaf5b8.json`](../../sessions/28/28f558fd38263cfaf5b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Body content (Abstract through Conclusion) spans **9 pages**, which is **1 page over** the EMNLP 8-page limit.

Here's the full summary:

---

## 编译状态
**编译成功**, `main.pdf` 已生成, 共 30 页 (含 references + appendix)

## 页数
**正文 9 页, 超限 1 页** (EMNLP 2026 限制 8 页)

正文内容 (Abstract → Conclusion) 结束在第 9 页。Limitations/Ethics 从第 10 页开始, References 从第 11 页开始, Appendix 从第 13 页开始。

## Section 空间占用
| File | Lines |
|---|---|
| experiments_c1.tex | 176 |
| method.tex | 81 |
| discussion.tex | 39 |
| introduction.tex | 31 |
| related_work.tex | 26 |
| experiments_c3.tex | 17 |
| conclusion.tex | 7 |

`experiments_c1.tex` 是最大的 section, 包含大量表格, 是压缩页数的首选目标。

## Overfull Hbox Warnings
- **62.9pt** (严重): `appendix_extended.tex` lines 591-607, 出现在 page 26 (appendix 内)
- 4.2pt, 1.3pt: 轻微, 可忽略

## Undefined Citations (6 个)
| Citation Key | 出现页 |
|---|---|
| `hale2001surprisal` | 2 |
| `levy2008expectation` | 2 |
| `raffel2020t5` | 2, 4 |
| `verma2024ghostbuster` | 2 |
| `yang2024dnagpt` | 2 |

这些 key 在 `references.bib` 中缺失。

## Cite 统计
| File | `\cite{}` 数 |
|---|---|
| related_work.tex | 11 |
| introduction.tex | 5 |
| method.tex | 2 |
| experiments_c1.tex | 2 |
| experiments_c3.tex | 1 |
| discussion.tex | 0 |
| conclusion.tex | 0 |
| **Total** | **21** |

空 cite: 无

## 需要处理的问题
1. **正文超 1 页** — 需压缩 experiments_c1 或 discussion, 或将部分表格移至 appendix
2. **5 个 undefined citation** — 需补充到 `references.bib`
3. **62.9pt overfull hbox** — appendix_extended.tex 中有一处表格/段落严重溢出

---

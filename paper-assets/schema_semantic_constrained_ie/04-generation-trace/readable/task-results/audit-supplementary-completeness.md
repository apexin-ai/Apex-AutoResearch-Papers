# audit supplementary completeness

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_supplementary_completeness_20260517T025427_result.json`
- **Structured JSON:** [`4a782859a66d6ddda9f6.json`](../../sessions/4a/4a782859a66d6ddda9f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Supplementary Material 完整性检查结果

### 已引用的 appendix 文件
| 文件 | main.tex 行号 |
|---|---|
| `appendix_prompts.tex` | 94 |
| `appendix_related_work.tex` | 95 |
| `appendix_discussion.tex` | 96 |
| `appendix_llama_per_relation.tex` | 97 |

### 未引用的 appendix 文件（未被 \input）
| 文件 | 状态 |
|---|---|
| **`appendix_sampling_table.tex`** | ❌ 未 \input，但 main.tex:77 和 appendix_beam_search.tex:5,55 引用了 `\ref{app:sampling}`（该 label 不存在于任何文件） |
| **`appendix_beam_search.tex`** | ❌ 未 \input，但 main.tex:77 引用了 `\ref{app:beam-search}`（label 定义在此文件中，编译时找不到） |

### 其他孤立 .tex 文件（旧版本/草稿，未被引用）
- `abstract_fd4b26.tex`、`abstract_d3264e.tex` — abstract 旧版本
- `section5_scierc_draft_4796e8.tex`、`section5_docred_draft_9b84f1.tex` — 实验章节旧版本
- `section7_conclusion_550cbf.tex`、`section7_conclusion.tex` — conclusion 旧版本
- `discussion_paragraphs_cf83d1.tex`、`discussion_paragraphs.tex` — discussion 草稿
- `section6_relwork_additions.tex`、`section6_relwork_outline.tex` — related work 草稿
- `paper_tables_draft.tex` — 表格草稿

### Figure 文件检查
| 引用路径 | 存在 |
|---|---|
| `figures/fig2_per_relation_dr.pdf` | ✅ |
| `figures/dual_factor_scatter.pdf` | ✅ |

未引用的 figure 文件：无（`figures/` 目录下 2 个文件均被引用）

缺失的 figure 文件：无

### 断裂的 \ref（关键问题）

| \ref 引用 | 引用位置 | 问题 |
|---|---|---|
| **`\ref{app:sampling}`** | main.tex:77, appendix_beam_search.tex:5,55 | **label 不存在于任何文件**。`appendix_sampling_table.tex` 只定义了 `\label{tab:sampling-robustness}`，缺少 `\section{...}\label{app:sampling}` |
| **`\ref{app:beam-search}`** | main.tex:77 | label 存在于 `appendix_beam_search.tex:2`，但该文件未被 `\input` |

### 建议操作

**必须修复（编译会产生 ?? 引用）：**

1. 在 main.tex 第 97 行后添加：
   ```latex
   \input{appendix_sampling_table}
   \input{appendix_beam_search}
   ```

2. `appendix_sampling_table.tex` 需要在表格前添加 section header：
   ```latex
   \section{Sampling Robustness}\label{app:sampling}
   ```
   （当前文件只有一个裸 table，没有 `\section` 和对应 label）

**可选清理：** 12 个孤立 .tex 文件为旧版本/草稿，可删除或移至子目录以保持目录整洁。

---

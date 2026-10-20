# LaTeX 编译验证报告

**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints
**检查时间**: 2026-05-19
**已编译 PDF**: `main.pdf` (30 pages, 481,162 bytes)

---

## 1. BibTeX 完整性

✅ **通过**

- Bib 文件: `relwork_new_entries.bib` (58 entries)
- 引用 keys: 58 unique
- **缺失 bib entries: 0**
- **未引用 bib entries: 0**

> 注: `new_citations.bib` 未被任何 `\bibliography` 引用，属于废弃文件。

---

## 2. 引用一致性 (Label/Ref)

✅ **通过** (无断裂引用)

- Labels 定义: 97
- Refs 使用: 69 unique
- **断裂引用 (`\ref` 无对应 `\label`): 0**
- **未引用 labels: 28**

未引用 labels 列表（非错误，但可能遗漏了有用的交叉引用）:

| Label | 文件 | 类型 |
|-------|------|------|
| `app:case-cf` | appendix_case_studies.tex | appendix subsection |
| `app:case-dr` | appendix_case_studies.tex | appendix subsection |
| `app:case-rv-dr` | appendix_case_studies.tex | appendix subsection |
| `app:case-scale` | appendix_case_studies.tex | appendix subsection |
| `app:case-studies` | appendix_case_studies.tex | appendix section |
| `app:discussion` | appendix_discussion.tex | appendix section |
| `app:doc-length` | appendix_doc_length.tex | appendix section |
| `app:ft-ablation` | appendix_discussion.tex | subsection |
| `app:ft-latency` | appendix_discussion.tex | subsection |
| `app:fuzzy-matching` | appendix_discussion.tex | subsection |
| `app:llama-per-relation` | appendix_llama_per_relation.tex | appendix section |
| `app:lora-per-relation` | appendix_discussion.tex | subsection |
| `app:prompt-sensitivity` | appendix_prompt_sensitivity.tex | appendix section |
| `eq:composition` | section4_composition_draft.tex | equation |
| `sec:70b-results` | section5_runtime.tex | subsection |
| `sec:bg:gcd` | section2_background.tex | subsection |
| `sec:bg:problem` | section2_background.tex | subsection |
| `sec:position-detection` | section3_method_draft.tex | subsection |
| `sec:related_work` | section6_related_work.tex | section |
| `sec:semantic` | section3_method_draft.tex | subsection |
| `tab:doc-length-docred` | appendix_doc_length.tex | table |
| `tab:doc-length-reduction` | appendix_doc_length.tex | table |
| `tab:doc-length-scierc` | appendix_doc_length.tex | table |
| `tab:full-ft` | appendix_full_ft.tex | table |
| `tab:kappa-case-study` | appendix_kappa_case_study.tex | table |
| `tab:sampling-robustness` | appendix_sampling_table.tex | table |
| `tab:tcr-docred` | appendix_tcr.tex | table |
| `tab:tcr-scierc` | appendix_tcr.tex | table |

---

## 3. TODO/TBD 残留

✅ **通过** (活跃文件无残留)

所有匹配项均在**未编译**的废弃/草稿文件中：

| 文件 | 状态 | 内容 |
|------|------|------|
| `section6_relwork_outline.tex` | 未编译 | 6 个 `% TODO:` 注释（大纲文件） |
| `abstract_d3264e.tex` | 未编译 | `\placeholder{DocRED results.}` |
| `abstract_fd4b26.tex` | 未编译 | `\placeholder{DocRED results.}` |
| `section7_conclusion_550cbf_DEPRECATED.tex` | 未编译 | `\placeholder{...??...}` |

以上文件均未被 `main.tex` 的 `\input` 引用，不影响编译输出。

---

## 4. 页数

✅ **符合 EMNLP 2026 要求**

| 项目 | 页码 |
|------|------|
| Main body (§1–§7) | pp. 1–8 (**8 页**) |
| Limitations 起始 | p. 9 (`\clearpage` 强制分页) |
| Ethics Statement | p. 9 |
| ARR Checklist | pp. 9–12 |
| Bibliography | pp. 12–13 |
| Appendix (A–N) | pp. 13–30 |
| **总页数** | **30 页** |

Main body 恰好 8 页，满足 EMNLP 2026 的 ≤8 页限制。Limitations/Ethics/References 不计入页数限制。

---

## 5. 其他问题

### 图片文件检查
✅ **通过** — 2 个 `\includegraphics` 引用，文件均存在：
- `figures/dual_factor_scatter.pdf` ✅
- `figures/fig2_per_relation_dr.pdf` ✅

### `??` 残留
✅ **通过** — 仅在未编译的 DEPRECATED 文件中发现，活跃文件无 `??`。

### PENDING AUDIT 标记
✅ **已清除** — `section6_relwork_additions.tex` 中有一条 ACTION 提醒删除 `section6_related_work.tex` 中的 PENDING AUDIT 注释，经验证该注释已被移除。`relwork_new_entries.bib` 中保留的是已验证的注释（`previously PENDING AUDIT — now verified`）。

### 注释大段内容
⚠️ **低风险** — 活跃文件中的注释块主要是节分隔符和元数据注释（3–7 行），无实质性遗忘内容。

### 废弃文件
ℹ️ 以下文件存在于 paper 目录但未被编译，可考虑清理：
- `abstract_d3264e.tex`, `abstract_fd4b26.tex` (旧 abstract 快照)
- `section7_conclusion_550cbf_DEPRECATED.tex`, `section7_conclusion_DEPRECATED.tex`
- `discussion_paragraphs.tex`, `discussion_paragraphs_cf83d1.tex`
- `section5_docred_draft_9b84f1.tex`, `section5_scierc_draft_4796e8.tex`
- `section6_relwork_outline.tex`, `section6_relwork_additions.tex`
- `p3_case_studies.tex`, `p3_case_studies_861a0d.tex`
- `paper_tables_draft.tex`
- `new_citations.bib`

---

## 总结

| 检查项 | 结果 |
|--------|------|
| BibTeX 完整性 | ✅ 58/58 完美匹配 |
| Label/Ref 一致性 | ✅ 无断裂引用 (28 unused labels) |
| TODO/TBD 残留 | ✅ 活跃文件无残留 |
| 页数合规 | ✅ Main body = 8 页 |
| 图片文件 | ✅ 全部存在 |
| `??` 残留 | ✅ 活跃文件无 |
| PENDING AUDIT | ✅ 已清除 |

**结论：论文编译状态良好，可以提交。** 唯一可选的改进是为 28 个未引用 labels 添加交叉引用（尤其是 appendix 表格），以及清理废弃文件。

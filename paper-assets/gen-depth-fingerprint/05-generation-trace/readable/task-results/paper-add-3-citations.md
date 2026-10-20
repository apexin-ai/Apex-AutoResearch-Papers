# paper add 3 citations

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_add_3_citations_20260520T193850_result.json`
- **Structured JSON:** [`36b2b97a58acfa65f4bd.json`](../../sessions/36/36b2b97a58acfa65f4bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. 完整作者列表（WebSearch 验证）

| 论文 | 完整作者列表 |
|------|-------------|
| Koike et al. (2025) | Ryuto Koike, Liam Dugan, Masahiro Kaneko, Chris Callison-Burch, Naoaki Okazaki |
| Seddik et al. (2024) | Mohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, Merouane Debbah |
| Kasa et al. (2024) | Siva Rajesh Kasa, Aniket Goel, Karan Gupta, Sumegh Roychowdhury, Pattisapu Priyatam, Anish Bhanushali, Prasanna Srinivasa Murthy |

### 2. references.bib 添加的 3 条 BibTeX

- `koike_mia_detection` — arXiv preprint, Membership Inference 分区（原 line 308 后）
- `seddik_synthetic_data` — arXiv preprint, Model Collapse 分区（原 line 147 后）
- `kasa_ordinality_nlp` — Findings ACL 2024, Machine Learning 分区（corn_ordinal 后）

### 3. tex 修改

| 文件 | 行号 | 修改 |
|------|------|------|
| `related_work.tex` | L10 | `\cite{gutierrez_ordinal_survey,coral_ordinal}` → `\cite{gutierrez_ordinal_survey,coral_ordinal,kasa_ordinality_nlp}` |
| `related_work.tex` | L15 | `\cite{self_consuming_mad,curse_of_recursion}` → `\cite{self_consuming_mad,curse_of_recursion,seddik_synthetic_data}` |
| `related_work.tex` | L33（新增行） | `\citet{koike_mia_detection} formalize this connection from the opposite direction, showing that detection scores implicitly perform membership inference, underscoring the shared statistical basis of detection and provenance.` |

Sources:
- [arXiv:2510.19492 — Koike et al.](https://arxiv.org/abs/2510.19492)
- [arXiv:2404.05090 — Seddik et al.](https://arxiv.org/abs/2404.05090)
- [ACL Anthology — Kasa et al.](https://aclanthology.org/2024.findings-acl.320/)

---

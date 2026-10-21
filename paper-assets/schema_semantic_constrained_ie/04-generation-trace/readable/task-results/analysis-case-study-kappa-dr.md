# analysis case study kappa dr

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_case_study_kappa_dr_20260519T175519_result.json`
- **Structured JSON:** [`ef025f876366da6d44c5.json`](../../sessions/ef/ef025f876366da6d44c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已生成：

- **数据报告**: `artifacts/_project/report/case_study_kappa_dr.md` — 包含 SciERC 全部 7 个关系 + DocRED 全部 80+ 个 canonical 关系的完整 per-relation 数据，以及 Top-5 / Bottom-5 的详细分析。
- **LaTeX 表格**: `artifacts/figures/case_study_kappa_dr.tex` — 10 行 case study 表格，5 个高 DR% + 5 个低 DR% 关系，每行附一句解释。

核心发现：**高 κ 是高 DR% 的必要非充分条件**。关键 co-factor 是 entity type confusion：
- `basin country` (κ=0.97) 和 `participant of` (κ=0.81) 因类型可混淆而 DR% 高达 58–75%
- `place of birth` (κ=0.92) 和 `place of death` (κ=0.89) 的 κ 同样高，但 PER→LOC 完全无歧义，DR%=0%
- `Used-for` (κ=0.03) 35/36 pairs 合法，几乎不可能违反

---

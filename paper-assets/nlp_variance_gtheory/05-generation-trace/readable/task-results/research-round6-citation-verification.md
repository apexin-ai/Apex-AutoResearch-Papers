# research round6 citation verification

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_round6_citation_verification_20260522T133034_result.json`
- **Structured JSON:** [`f72592161af4255a390f.json`](../../sessions/f7/f72592161af4255a390f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

BibTeX 文件已保存。验证结果：

| # | 引用 | 状态 | 标题 | 期刊/出版社 | 卷/页 | DOI |
|---|------|------|------|-------------|-------|-----|
| 1 | Mizrahi et al. (2024) | ✅ | State of What Art? A Call for Multi-Prompt LLM Evaluation | TACL | 12, 933–949 | `10.1162/tacl_a_00681` |
| 2 | Liang et al. (2023) | ⚠️ | Holistic Evaluation of Language Models | **NYAS** (非 NeurIPS) | 1525(1), 140–146 | `10.1111/nyas.15007` |
| 3 | Meredith (1993) | ✅ | Measurement Invariance, Factor Analysis and Factorial Invariance | Psychometrika | 58(4), 525–543 | `10.1007/BF02294825` |
| 4 | Putnick & Bornstein (2016) | ✅ | Measurement Invariance Conventions and Reporting: The State of the Art... | Developmental Review | 41, 71–90 | `10.1016/j.dr.2016.06.004` |
| 5 | Efron & Tibshirani (1993) | ✅ | An Introduction to the Bootstrap | Chapman & Hall | 436pp | ISBN 978-0-412-04231-7 |

**关键发现：** Reviewer 声称 HELM 发表于 NeurIPS 2023，这是**错误的**。正式发表在 Annals of the New York Academy of Sciences（Wiley, 2023），且该版本仅 7 页（Bommasani 为一作）。400+ 页的完整版（Liang 为一作）仅存于 arXiv:2211.09110。BibTeX 中已用 NYAS 正式发表版本并加注说明。

文件位置：`artifacts/exp004/data/round6_new_refs.bib`

---

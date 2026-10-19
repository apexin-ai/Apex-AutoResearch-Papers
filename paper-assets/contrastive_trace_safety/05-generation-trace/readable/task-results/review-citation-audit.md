# review citation audit

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_citation_audit_20260518T221539_result.json`
- **Structured JSON:** [`804ac93ff9dbf02f52e4.json`](../../sessions/80/804ac93ff9dbf02f52e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计结果：

| 项目 | 数量 |
|------|------|
| Bib entries | 63 |
| Cited keys | 60 |
| Missing (cited but no bib) | 0 |
| Orphan (bib but never cited) | **3** |
| Format issues | **3** |

**Orphan entries**（bib 中有但未被任何 tex 引用）:
- `bansal2021stitching`
- `efron1993bootstrap`
- `kornblith2019cka`

**Title case protection**（专有名词未用 `{}` 保护，BibTeX 可能自动小写化）:
- `safeswitch`: LLM
- `siren`: LLM
- `zhou2024alignment`: LLM

报告已保存至 `artifacts/citation_audit.md`。

---

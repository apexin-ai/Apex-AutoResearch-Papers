# writing citation fix reviewer

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_citation-fix-reviewer_20260526T103441_result.json`
- **Structured JSON:** [`176c02a3dbef0ad5d344.json`](../../sessions/17/176c02a3dbef0ad5d344.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 处引用错误全部验证确认并修复完毕：

| # | Key | 问题 | 修复 |
|---|-----|------|------|
| C1 | `laban2025lost` | arXiv → ICLR 2026 Oral | `@inproceedings` + ICLR + 2026 |
| C2 | `raposo2024mixture` | ICML 2024 → ICLR 2025 | booktitle + year 修正 |
| C3 | `he2019exposure` | arXiv 2019 → EMNLP 2021 | `@inproceedings` + 新标题 + EMNLP + 2021 |
| M1 | `bachlechner2021rezero` | 作者名不全 | Huanru Henry Mao, Garrison W. Cottrell |
| M2 | `brunner2020identifiability` | 末位作者错误 | Andreas Krause → Roger Wattenhofer |

编译通过，bibtex 0 warnings。报告已写入 `artifacts/citation_fix_reviewer.md`。

---

# fix d015 title and nearcomplete cleanup

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d015_title_and_nearcomplete_cleanup_20260514T223119_result.json`
- **Structured JSON:** [`634bc803711624ac0551.json`](../../sessions/63/634bc803711624ac0551.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

残留全部符合保留/跳过条件：

| 残留 | 原因 |
|---|---|
| `section5_docred_draft_9b84f1.tex` ×3 | 旧版本文件（hash 后缀），跳过 |
| `section5_scierc_draft_4796e8.tex` | 旧版本文件，跳过 |
| `section3_method_draft.tex:2` | 注释行（`%` 开头），跳过 |
| `section6_relwork_outline.tex:102` | 具体描述 SciERC 15.37%→0.93%，保留 |
| `section5_scierc_draft.tex:76` | 描述 SciERC DR 94%（→0.93%），保留 |
| `section5_docred_draft.tex:60` | `near-eliminates RV` 29.66%→0.03%，保留 |

---

### 修改总结

**P1 — Title：**
- `main.tex:18`：`Near-Complete Type-Valid` → `Type-Valid`

**P3 — "near-complete" 清理（4 处修改，6 处保留/跳过）：**

| 文件 | 修改 |
|---|---|
| `appendix_related_work.tex:85` | `near-complete to substantial elimination` → `substantially reduces violations` |
| `appendix_related_work.tex:109` | `near-complete to substantial elimination of type violations` → `substantially reduces type violations` |
| `section6_relwork_outline.tex:135` | `near-complete elimination of type violations` → `substantially reduces type violations (up to 94\% DR reduction)` |

---

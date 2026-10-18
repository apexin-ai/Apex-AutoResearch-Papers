# paper d048 comprehensive final

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d048_comprehensive_final_20260516T145121_result.json`
- **Structured JSON:** [`5b586ced506f94e282fd.json`](../../sessions/5b/5b586ced506f94e282fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks pass. Let me verify the counts:

**31.2 in prose**: 3 occurrences (introduction ×1, results ×2) — all in the body text where the number is contextually needed. The abstract and appendix no longer have prose "31.2". Table cells (main.tex lines 93-94, 265-266) don't count. ✓ ≤3

**2.2 in prose**: 5 occurrences (abstract ×1, introduction ×1, results ×1, discussion ×2). ✓ ≥5

**TOST/equivalence**: Present in checklist, limitations, appendix_factorial, results §4.4, and BCS aggregation caption. ✓

**Compilation**: No errors, no undefined references, 18 pages output. ✓

---

## 修改摘要

| Priority | 修改 | 文件 |
|----------|------|------|
| 1a | abstract 中 31.2 → "widens substantially (Table~3)" | abstract.tex |
| 1b | appendix prompt sensitivity 中去掉 31.2 数字 | main.tex:219 |
| 2a | discussion "Schema design implications" 段首加 2.2pp 句 | discussion.tex |
| 2b | conclusion 中加 "typical batches differ by ≈2.2pp" | discussion.tex |
| 3a | appendix_factorial 替换为含 FewRel 2×2 + TOST 的完整版 | main.tex:155–162 |
| 3b | Limitations #3 更新为 TOST 版本 | main.tex:44 |
| 3c | §4.4 Multi-Channel 末尾加 TOST 引用句 | results.tex:87 |
| 4a | Few-NERD 段加采样方式说明 | experimental_setup.tex |
| 4b | §3.4 加 "single-seed; variance not quantified" | experimental_setup.tex |
| 4e | 无 haystack/needle bib entry，跳过 | — |
| 4f | §3.4 加 bootstrap B 不一致说明 ($B$=10k pair / $B$=1k batch) | experimental_setup.tex |

**自检结果**: 31.2 prose ≤3 ✓ | 2.2pp ≥5 ✓ | TOST 集成 ✓ | 编译无错误 | 18 页

---

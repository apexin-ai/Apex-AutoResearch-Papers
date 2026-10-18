# paper d045 cascade fixes

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d045_cascade_fixes_20260516T105849_result.json`
- **Structured JSON:** [`f85fc64e061e9310579e.json`](../../sessions/f8/f85fc64e061e9310579e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

- **5 处修改**：均已应用
  - abstract.tex: `r² = 1.3–1.7%` → `1.3–3.5%`
  - introduction.tex finding (2): `r = 0.112–0.129` → `0.112–0.187`
  - introduction.tex Contribution 2: `r = 0.112–0.129` → `0.112–0.187`
  - sdgd_negative.tex: → "entities may receive conflicting labels across separate decomposition passes"（"chunk" 已确认不存在）
  - discussion.tex: → "type pairs with high SCS tend to produce disproportionately more substitution errors (§4.3)"
- **编译结果**：无 error，16 页，仅 4 个 float specifier warning（`h` → `ht`，正常）

---

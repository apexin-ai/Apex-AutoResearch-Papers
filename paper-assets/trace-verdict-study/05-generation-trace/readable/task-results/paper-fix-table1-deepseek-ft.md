# paper fix table1 deepseek ft

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_table1_deepseek_ft_20260516T010950_result.json`
- **Structured JSON:** [`81798ca7a23fa3367d28.json`](../../sessions/81/81798ca7a23fa3367d28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No N/A remaining. All changes applied and PDF compiles.

**Summary of changes:**

| File | Change |
|------|--------|
| `experiments.tex` L24 | Table 1: `N/A$^\ddag$` → `79.16%`, gap `---` → `2.60pp` |
| `experiments.tex` L30 | Caption: added DeepSeek `full_trace` CI [76.80, 81.30]; removed `$^\ddag$` invalidation footnote |
| `experiments.tex` L39 | Removed dangling "Unlike...`$^\ddag$`" clause referencing invalidated condition |
| `discussion.tex` L60 | Replaced "was invalidated...report it as N/A" with re-run result (79.16%, 2.60pp below Qwen) |
| `appendix.tex` L199 | DeepSeek full results table: `N/A / label truncated` → `79.16 / CI [76.80, 81.30]` |
| `appendix.tex` L24–26 | Per-class table: added DeepSeek Full Trace row (P/R/F1: pass 85.7/85.1/85.4, fail 63.2/64.3/63.7) |

---

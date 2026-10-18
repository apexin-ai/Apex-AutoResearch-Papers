# paper mistral footnote fix

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_mistral_footnote_fix_20260514T213232_result.json`
- **Structured JSON:** [`459d4d2c4a5bf7893fdb.json`](../../sessions/45/459d4d2c4a5bf7893fdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Summary:

- **analysis.tex L43**: Changed Mistral footnote from `$^\ddagger$` (standard profiling) to `$^\dagger$` (hires profiling).
- **analysis.tex caption**: `$^\ddagger$` definition kept — Llama and Gemma still use it.
- **experiments.tex L52**: No change needed — `$^{\dagger\ddagger}$` there means hires profiling (`†`) + best $k$ from ablation (`‡`), which are different footnotes with different definitions in that table's caption. Both are correct.

---

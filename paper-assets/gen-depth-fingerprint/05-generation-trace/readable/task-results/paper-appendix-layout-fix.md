# paper appendix layout fix

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix-layout-fix_20260522T024818_result.json`
- **Structured JSON:** [`e1822f916d05445f0778.json`](../../sessions/e1/e1822f916d05445f0778.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three pages fixed:

| Page | Before | After | What changed |
|------|--------|-------|-------------|
| **13** | 117 lines — only Dataset Stats table + footnote, violin figure pushed to p14 | 216 lines — Length Confound section text fills gap; `app:length` now starts on p13 | Removed `\FloatBarrier` between dataset_stats and Length section |
| **26** | 163 lines — 3 short sections (Ablation/Correlation/Cross-Family) with dead space | 226 lines — Seed Control text fills gap; `app:seed-control` now starts on p26 | Removed `\FloatBarrier` between table4 and seed_control |
| **31** | 122 lines — only Generator Subsets + partial Qualitative | 412 lines — both qualitative tables now on p31 + Transfer section flows in; `tab:qualitative-features` moved from p32→p31 | Removed `\FloatBarrier` between gen-subsets/qualitative/transfer |

Total page count unchanged at 36. All labels and floats remain near their references.

---

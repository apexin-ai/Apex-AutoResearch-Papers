# paper appendix whitespace p24 26 35

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix-whitespace-p24-26-35_20260522T041552_result.json`
- **Structured JSON:** [`31d1b431240aa84b0789.json`](../../sessions/31/31d1b431240aa84b0789.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results look good. Page 34 now has the iterative comparison text + NLL distribution section with figure (90 lines, well-filled). Page 35 is the last page with just the comparison table, which is acceptable.

**Summary of fixes:**

| Original Page | Issue | Fix | Result |
|---|---|---|---|
| **p.24** (123 lines) | `figure*[t]` in feature_distributions floated to next page; `\FloatBarrier` blocked cross-temp content from flowing up | Removed `\FloatBarrier` after `appendix_feature_distributions` | **276 lines** |
| **p.26** (179 lines) | `\FloatBarrier` between small ablation and correlation sections created artificial gaps | Removed `\FloatBarrier` after `appendix_ablation` | **252 lines** |
| **p.35** (30 lines) | `table*[t]` in iterative_comparison floated away; `\FloatBarrier` blocked NLL content from filling gap | (1) Moved text before `table*[t]` in `appendix_iterative_comparison.tex`; (2) Removed `\FloatBarrier` after `appendix_9gen_scale` and after `appendix_iterative_comparison` | Content absorbed into **p.34 (90 lines)** + table on last page |

**Total pages**: 37 → 35 (net reduction of 2 pages). All three local copies (artifacts, docs, remote) synced.

---

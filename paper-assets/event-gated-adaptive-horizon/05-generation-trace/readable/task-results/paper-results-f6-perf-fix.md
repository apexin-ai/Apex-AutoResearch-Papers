# paper results f6 perf fix

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_results_f6_perf_fix_20260525T162523_result.json`
- **Structured JSON:** [`e3560c136eaf2a0b0f21.json`](../../sessions/e3/e3560c136eaf2a0b0f21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Here's the diff:

**Before (L112):**
> All four tested seeds avoid CIVO onset (peak NVE $0.5$--$0.6\times$, well below the $1.5\times$ threshold), with **three-seed mean evaluation $781.2 \pm 159.5$ ($84\%$ of baseline**; Figure~\ref{fig:multiple_pathways}).

**After (L112):**
> Across **four unique seeds (s0, s1, s2, s5)**, none exhibits CIVO onset (peak NVE ${\leq}0.6\times$, well below the $1.5\times$ threshold). **Three of four seeds achieve $64$--$94\%$ of baseline (eval $597$--$877$; mean $775.6$); seed~0 exhibits CIVO-unrelated learning stagnation (eval $148$, $16\%$ baseline**; Figure~\ref{fig:multiple_pathways}).

**Checklist:**
- All 4 unique seeds (s0, s1, s2, s5) explicitly mentioned
- s0 outlier transparently disclosed with characterization (CIVO-unrelated stagnation)
- 4/4 no CIVO claim preserved
- No mean based on non-unique seeds
- 3 productive seeds mean (775.6) reported with s0 excluded and reason stated
- results.md files checked — no corresponding F6 text to sync

---

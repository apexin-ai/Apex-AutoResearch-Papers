# paper methodology f2 caption fix

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_methodology-f2-caption-fix_20260518T082245_result.json`
- **Structured JSON:** [`6a156ca2a21db4e7b4aa.json`](../../sessions/6a/6a156ca2a21db4e7b4aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无 em-dash 引入。

**修改 1 — `methodology.tex` L70**
- 前：`Each non-baseline configuration uses 2 seeds; following \citet{agarwal2021precipice}, we report per-seed trajectories to surface stochastic divergence.`
- 后：`Most non-baseline configurations use 2 seeds; key configurations (008d, 008a) are extended to 3--4 seeds. Following \citet{agarwal2021precipice}, we report per-seed trajectories to surface stochastic divergence.`

**修改 2 — `results.tex` L72 (F2 caption)**
- 前：`$n{=}3$ seeds; seed~4 data in Table~\ref{tab:complete_results})`
- 后：`$n{=}3$ seeds plotted; seed~4 data in Table~\ref{tab:complete_results})`

两处均已完成，无 em-dash。

---

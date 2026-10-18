# writing r1 w6 w8 method

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_r1_w6_w8_method_20260515T044249_result.json`
- **Structured JSON:** [`300fdea7f49aba2c3284.json`](../../sessions/30/300fdea7f49aba2c3284.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两段都已加入 `method.tex`:

**任务 1 (R1-W6, §3.4 末尾, lines 78-83)**: 加入 `\paragraph{Restoring additivity.}`，解释 cardinality constraint 如何将问题压回 near-additive regime（k=8 ≈ 7% of 112 heads），引用 Fig 2 U-shaped curve 的最小值位于 additive 假设仍合理的区间，并解释 constrained (11.23) vs unconstrained (32.45/36.92) 的 3-4× gap = additive model 在 valid range 外的外推误差。

**任务 2 (R1-W8, §3.5, lines 111-114)**: 加入 `\paragraph{Empirical observation.}`，formal statement 给出条件（$k \ll H$ + top-k 无 tie）→ 结论（greedy = MCKP per-head allocation），列出三个架构验证（112/112, 256/256, 255/256），并给出直觉解释：constraint 把 feasible set 缩到一个小组合空间，marginal-benefit ordering 唯一决定 selection，local = global optimum。

未改动既有内容；数字与 registry 一致。

---

# paper results nve bound fix

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_results_nve_bound_fix_20260525T165218_result.json`
- **Structured JSON:** [`193c9ff7cb31fe8ab89b.json`](../../sessions/19/193c9ff7cb31fe8ab89b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全文无遗留旧 bound。

**Diff 汇总：**

| 文件 | 行 | Before | After |
|------|-----|--------|-------|
| `results.tex` | 112 | `peak NVE ${\leq}0.6\times$` | `peak NVE ${\leq}0.8\times$` |
| `appendix.tex` | 111 | `NVE $\leq 0.6\times$, no value overestimation` | `NVE $\leq 0.8\times$, no value overestimation` |
| `appendix.tex` | 143 | `healthy with NVE $\leq 0.6\times$` | `healthy with NVE $\leq 0.8\times$` |
| `appendix.tex` | 797 | `NVE $\leq 0.6\times$, well below` | `NVE $\leq 0.8\times$, well below` |
| `appendix.tex` | 950 | `(NVE $\leq 0.6\times$)` | `(NVE $\leq 0.8\times$)` |

5 处 bound 声明已全部修正为 0.8×。"no CIVO onset" 结论不变（0.8× 仍远低于 1.5× threshold）。

---

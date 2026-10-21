# fix sensitivity table ci

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_sensitivity-table-ci_20260521T011105_result.json`
- **Structured JSON:** [`facf4ed615d9cc3de5f9.json`](../../sessions/fa/facf4ed615d9cc3de5f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，0 errors。4 个 undefined `sec:experiments` 引用是已有的（与本次修改无关）。输出 17 页 PDF。

### Diff 总结

| 位置 | 修改前 | 修改后 |
|------|--------|--------|
| 列头 | `DAF (10 tasks)` | `DAF (10 tasks, excl.\ zero-death)` |
| Qwen 11-task CI | [81.4, 99.1] | [81.3, 99.1] |
| Llama 11-task CI | [80.0, 95.1] | [80.2, 95.1] |
| Gemma 11-task CI | [79.5, 98.4] | [68.8, 100.0] |
| Llama 10-task CI | [91.5, 100.0] | [91.3, 100.0] |
| Caption | "across all models). Episode-level bootstrap 95% CIs ($B = 10,000$)." | "zero death rate). Bootstrap 95% CIs ($B{=}10{,}000$, seed 42). Full-sample CIs use cluster bootstrap ($K{=}11$); exclusion CIs use episode-level bootstrap over the remaining 10 task types." |

---

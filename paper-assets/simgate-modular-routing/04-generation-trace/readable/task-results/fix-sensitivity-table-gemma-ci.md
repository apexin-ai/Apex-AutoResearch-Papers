# fix sensitivity table gemma ci

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_sensitivity-table-gemma-ci_20260521T011908_result.json`
- **Structured JSON:** [`9d9b85fb843162deb9a4.json`](../../sessions/9d/9d9b85fb843162deb9a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Summary:

**修改前 → 修改后：**

| 项目 | 旧值 | 新值 |
|------|------|------|
| Gemma CI (line 293) | `89.7\% [68.8, 100.0]` | `89.7\% [79.5, 98.4]` |
| Caption (line 296) | `Bootstrap 95\% CIs ... Full-sample CIs use cluster bootstrap ($K{=}11$); exclusion CIs use episode-level bootstrap over the remaining 10 task types.` | `Non-clustered episode-level bootstrap 95\% CIs ($B{=}10{,}000$, seed 42).` |

**残留检查：** `grep -n "68.8" main.tex` → 0 matches，无残留。

**编译：** 0 errors，17 pages。4 个 `sec:experiments` undefined ref 是已有的（experiments.tex 中的 label 问题），与本次修改无关。

---

# analyze eval obs only object norm003 seed44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-obs-only-object-norm003-seed44_20260520T105129_result.json`
- **Structured JSON:** [`ab5e1c3eea7a37380593.json`](../../sessions/ab/ab5e1c3eea7a37380593.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 指标摘要

**eval-obs-only-object-norm003-seed44** — CRM obs_only, Object benchmark, ε=0.03, seed=44

| 指标 | 值 |
|------|-----|
| **Overall SR** | **15.0% (15/100)** |

**Per-task breakdown:**

| Task | SR |
|------|-----|
| salad_dressing | 30% |
| chocolate_pudding | 30% |
| orange_juice | 30% |
| bbq_sauce | 20% |
| milk | 20% |
| tomato_sauce | 10% |
| butter | 10% |
| alphabet_soup | 0% |
| cream_cheese | 0% |
| ketchup | 0% |

15.0% 符合预期区间（VLA-only ~10.9% 和 norm02 ~16.8% 之间），ε=0.03 的微小 correction 提供了有限但正向的提升。作为 Figure 2 error bars 的 seed44 数据点，结果有效。

---

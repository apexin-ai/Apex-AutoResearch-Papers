# analyze eval supp k2mean object s43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-supp-k2mean-object-s43_20260523T115201_result.json`
- **Structured JSON:** [`e6abb225486d4ecfd0a5.json`](../../sessions/e6/e6abb225486d4ecfd0a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**eval-supp-k2mean-object-s43 结果**

| 指标 | 值 |
|------|-----|
| **Overall SR** | **78.0%** (156/200) |

**Per-task breakdown:**

| Task | SR |
|------|-----|
| orange_juice | 90% |
| alphabet_soup | 85% |
| cream_cheese | 85% |
| ketchup | 85% |
| bbq_sauce | 80% |
| salad_dressing | 75% |
| tomato_sauce | 70% |
| butter | 70% |
| milk | 70% |
| chocolate_pudding | 70% |

**K=2 mean Object 多 seed 汇总：** s42=79.5%, s43=78.0%, s44 running. 当前 2-seed 均值 = 78.75%，与 VLA-only baseline 3-seed 均值 77.8% 接近。

Registry 已更新为 DONE(success)，cron 已删除。**cqa1-32758:cuda:2 已释放**，可部署新实验。

---

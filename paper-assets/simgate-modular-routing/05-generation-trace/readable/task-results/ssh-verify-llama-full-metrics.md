# ssh verify llama full metrics

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-llama-full-metrics_20260519T104413_result.json`
- **Structured JSON:** [`29a9869bd41a70aa47c8.json`](../../sessions/29/29a9869bd41a70aa47c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

核实完成。结果如下：

```
=== LLAMA FULL METRICS RECOUNT ===
Task                                          |   n | int_d | det_d | int_dr% | det_dr%
------------------------------------------------------------------------------------------
chemistry-mix                                 |  20 |     9 |     4 |   45.0% |   20.0%
find-animal                                   |  20 |     8 |     5 |   40.0% |   25.0%
find-non-living-thing                         |  20 |     0 |     0 |    0.0% |    0.0%
freeze                                        |  20 |     9 |     0 |   45.0% |    0.0%
grow-fruit                                    |  20 |     9 |     1 |   45.0% |    5.0%
identify-life-stages-1                        |  20 |    11 |     2 |   55.0% |   10.0%
identify-life-stages-2                        |  20 |     9 |     1 |   45.0% |    5.0%
inclined-plane-determine-angle                |  20 |     9 |     4 |   45.0% |   20.0%
lifespan-longest-lived                        |  20 |     7 |     1 |   35.0% |    5.0%
lifespan-longest-lived-then-shortest-lived    |  20 |    10 |     4 |   50.0% |   20.0%
measure-melting-point-unknown-substance       |  20 |    10 |     3 |   50.0% |   15.0%
------------------------------------------------------------------------------------------
TOTAL                                         | 220 |    91 |    25 |   41.4% |   11.4%

Delta DR (pp): +30.0
DAF (%): 264.0
```

**核实结论：**

1. **Agent 提取的数字完全正确**：11 个 task 的 int_deaths 逐一比对，全部吻合，总计 91，int_dr = 41.4%。与 Agent 记录的数字零差异。

2. **identify-life-stages-1 确认有 20 个 episode**（不是 17），其中 11 个 internal death、2 个 det death。

3. **Reviewer 独立核实的 94 / 42.7% 与原始数据不一致**。原始 episode_summary.jsonl 明确显示 91 internal deaths。差异的 3 个 episode 不在数据文件中——可能是 Reviewer 的统计口径或数据来源不同（例如把 `both_died` 的 det_death 也算进了 internal，或者用了不同的文件）。

4. **det_deaths 总计 25，det_dr = 11.4%**，Delta DR = +30.0 pp，DAF = 264.0%。

---

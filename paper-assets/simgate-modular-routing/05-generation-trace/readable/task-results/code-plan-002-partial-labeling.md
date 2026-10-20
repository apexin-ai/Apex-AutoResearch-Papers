# code plan 002 partial labeling

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-002-partial-labeling_20260514T014716_result.json`
- **Structured JSON:** [`5cf118d8c4a18796a332.json`](../../sessions/5c/5cf118d8c4a18796a332.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Labeling 完成。结果汇总：

**4 个 task × 20 episodes = 80 episodes**

| Label | Episodes | Steps | Episode % |
|---|---|---|---|
| det-preferred | 26 | 780 | 32.5% |
| internal-preferred | 5 | 150 | 6.3% |
| no-preference | 49 | 1329 | 61.3% |

**Per-task 信号来源：**

| Task | det_death | int_death | det_score | int_score | tie | both_died |
|---|---|---|---|---|---|---|
| find-non-living-thing | 0 | 0 | 7 | 4 | 9 | 0 |
| grow-fruit | 6 | 1 | 0 | 0 | 10 | 3 |
| identify-life-stages-2 | 6 | 0 | 0 | 0 | 10 | 4 |
| inclined-plane-determine-angle | 7 | 0 | 0 | 0 | 9 | 4 |

**异常观察：**
- 分布与预期（~93% det-preferred）差异很大。实际 det-preferred 仅 32.5%，no-preference 高达 61.3%。
- no-preference 主要来自 tie（两者都活且分数相同，38 episodes）和 both_died（11 episodes）。
- find-non-living-thing 无任何 death 事件，分类完全靠 score comparison。其他 3 个 task 的 death 信号以 det_death（internal 死、det 活→det-preferred）为主，但 tie 占比也很高。
- internal-preferred 仅 5 episodes（全来自 grow-fruit 的 1 个 int_death + find-non-living-thing 的 4 个 int_score），确认极度不平衡。

产出：`results/plan_001b_labels_partial/sft_triples.jsonl`（2259 steps, 2MB）+ `labeling_summary.json`。

---

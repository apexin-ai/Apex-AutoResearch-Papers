# ssh plan 005 classification fix

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_plan-005-classification-fix_20260514T015143_result.json`
- **Structured JSON:** [`454fbaccb46f85970460.json`](../../sessions/45/454fbaccb46f85970460.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件全部修改并验证完成：

| 分类 | 修改前 | 修改后 |
|------|--------|--------|
| death-dominated | 25 | 25 |
| genuine-det | 3 | 3 |
| internal-preferred | 2 | **1** (仅 find-non-living-thing) |
| no-signal | 0 | **1** (grow-plant) |

- `task_classification.json`: grow-plant → `"no-signal"`
- `taxonomy_summary.json`: internal-preferred task_count 2→1, episode_count 45→25; no-signal task_count 0→1, episode_count 0→20
- `heatmap_data.csv`: grow-plant 行 category 改为 `no-signal`

---

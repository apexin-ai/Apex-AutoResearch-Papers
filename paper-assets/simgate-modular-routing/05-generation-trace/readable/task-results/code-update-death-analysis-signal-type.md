# code update death analysis signal type

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_update-death-analysis-signal-type_20260513T190919_result.json`
- **Structured JSON:** [`5363b048602eb2b71253.json`](../../sessions/53/5363b048602eb2b71253.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**Prescreening (9 tasks):**
- death-dominated: 4 tasks
- genuine-det: 3 tasks (find-animal, find-living-thing, freeze)
- internal-preferred: 1 task (find-non-living-thing)
- mixed: 1 task (chemistry-mix)

**MVP (5 tasks):**
- death-dominated: 5 tasks (全部)
- genuine-det / internal-preferred / mixed: 0

MVP 的 det 优势完全来自 death avoidance，无一例外。Prescreening 中也有近半数是 death-dominated。

产出文件：
- 更新：`src/death_analysis.py`
- 新增：`results/prescreening/signal_type_summary.json`

---

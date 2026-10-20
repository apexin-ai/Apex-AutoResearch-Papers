# paper r30 batch1 data

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r30-batch1-data_20260523T042223_result.json`
- **Structured JSON:** [`8901b4c4308358ca1f17.json`](../../sessions/89/8901b4c4308358ca1f17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。报告已写入 `artifacts/r30_batch1_analysis.md`。

**Part 1 结果**:
- 20 个 non-death non-tie episodes **全部来自 find-non-living-thing**（其他 task types 的非 tie episodes 都涉及 death）
- 分类：**10 hallucination**（eat-before-focus + 浴室水管 + focus-inventory 循环）、**3 action selection**（无效导航）、**7 object quality**（picture/fountain=50 vs orange=58）
- 核心发现：内部策略在 11/20 episodes 中先吃掉 orange 再 focus（state model 错误地认为 eat=completing task）

**Part 2 结果**:
- 72B DAF = **92.4%**, 95% CI = **[86.1%, 97.9%]**
- delta_full = 30.07, delta_nd = 2.28
- 实际数据显示 5 个 int-preferred（非 0），来自 find-non-living-thing、grow-fruit、identify-life-stages-2、inclined-plane

---

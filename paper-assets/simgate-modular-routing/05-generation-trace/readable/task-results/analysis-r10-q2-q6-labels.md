# analysis r10 q2 q6 labels

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r10-q2-q6-labels_20260517T032949_result.json`
- **Structured JSON:** [`15e54c30b6a4efeb581f.json`](../../sessions/15/15e54c30b6a4efeb581f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。汇总结果：

---

## Q2: Death-asymmetry label redundancy

| Category | Count | Proportion |
|----------|-------|-----------|
| **Redundant** (label holds without death penalty) | 21/75 | 28.0% |
| **Purely death-driven** (label changes without death) | 54/75 | 72.0% |
| — becomes tie (surviving side also scored 0) | 54 | |
| — flips winner | 0 | |

**解读**：54 个 purely death-driven cases 全部变成 tie（不是 flip）。原因：surviving side 得了 0 分，dying side 得了 -100。去掉 death penalty 后双方都是 0。这说明在这些 episodes 中，唯一的区分信号就是"一方死了"。

Death 方向：internal died = 70, det died = 5（internal 死亡率远高于 det）。

---

## Q6: Non-death score differences

20 个 non-death non-tie episodes（全部来自 `find-non-living-thing` 任务，全部 both alive）：

| Metric | det - int (signed) | |det - int| (absolute) |
|--------|-------------------|----------------------|
| Median | 13.0 | 45.5 |
| Mean | 19.1 | 34.9 |
| Q1 | 8.0 | 8.0 |
| Q3 | 58.0 | 58.0 |
| Min | -58.0 | 8.0 |
| Max | 67.0 | 67.0 |

**分布特征**：
- 16/20 为 det-preferred，4/20 为 internal-preferred
- 绝对差值集中在两个 cluster：小差距（8-17 分，10 episodes）和大差距（41-67 分，10 episodes）
- IQR 很宽 [8, 58]，说明 score gap 异质性高
- 所有 20 个 non-death labels 来自同一任务类型 `find-non-living-thing`

---

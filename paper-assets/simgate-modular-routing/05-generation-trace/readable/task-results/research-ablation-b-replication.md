# research ablation b replication

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ablation-b-replication_20260514T084716_result.json`
- **Structured JSON:** [`46195d27979fa48f439e.json`](../../sessions/46/46195d27979fa48f439e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

**核心结论**：
- **ga=8 确认**：ablation-b 用了 ga=8（步数反推 165 = ceil(434/8)×3），spec 正确，数据分析表 ga=1 有误
- **复现成功 3/3**：所有 seed 产出非退化 generation-level router，balanced_accuracy 稳定在 57-59%
- **存在 recall tradeoff 偏移**：新 seed 普遍比原始 seed42 更偏向预测 internal（可能因训练脚本 data split 方式已更新）

---

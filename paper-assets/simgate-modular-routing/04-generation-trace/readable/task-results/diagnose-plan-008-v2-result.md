# diagnose plan 008 v2 result

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan-008-v2-result_20260515T144454_result.json`
- **Structured JSON:** [`329ff1e12f7b8f6f6e98.json`](../../sessions/32/329ff1e12f7b8f6f6e98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新，cron 已删除。

**plan-008-router-size-v2 结果：DONE / negative**

| Model | balanced_acc | internal_recall | det_recall |
|-------|-------------|-----------------|------------|
| 0.6B  | 0.376       | 0.40            | 0.352      |
| 1.7B  | 0.419       | 0.47            | 0.370      |
| 4B    | 0.337       | 0.43            | 0.241      |

三模型全部低于随机基线 0.50，v2 生成式评估修复了 v1 的 det_recall=0 bug，但模型本身未学到分类——生成的是游戏动作文本（"connect freezer to door"）而非路由标签，parser 靠 `[SIMULATE]` 前缀做 heuristic 分类。4B 反而最差（反向缩放）。1.7B 的 0.419 远低于 seed-robustness 参考 0.554±0.052。

router-size 对比无法得出有效结论——根本原因是训练目标/prompt 模板没有让模型学到输出分类标签。

---

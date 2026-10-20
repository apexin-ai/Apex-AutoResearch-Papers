# code plan 008 v3 add eval

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-008-v3-add-eval_20260515T150008_result.json`
- **Structured JSON:** [`ec5068a86de577fd1f88.json`](../../sessions/ec/ec5068a86de577fd1f88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 eval 完成。结果汇总：

| Model | balanced_acc | internal_recall | det_recall |
|-------|-------------|-----------------|------------|
| Qwen3-0.6B | 0.3222 | 0.3333 | 0.3111 |
| Qwen3-1.7B | 0.3759 | 0.4000 | 0.3519 |
| Qwen3-4B | 0.3463 | 0.3667 | 0.3259 |
| **Reference** (seed-robustness, 1.7B) | **0.554±0.052** | — | — |

**问题**：三个模型的 balanced_acc 全部低于随机基线（0.5），远低于 seed-robustness 参考值。所有模型都大量预测 "internal"（真实分布 internal=30, det=270，但预测 internal ~187-196），说明模型没有学会正确输出 `[SIMULATE]` 前缀。

这与 v2 遇到的问题类似。可能原因：
1. v3 训练虽然用了 `implicit_router_sft.py`，但 `.bak` 文件存在说明脚本可能被修改过
2. 需要对比 v3 训练的 `implicit_router_sft.py` 与 seed-robustness 使用的版本是否一致

结果已保存到 `results/plan-008-v3/eval_qwen3_{0.6b,1.7b,4b}.json`。

---

# analysis groundtruth action error

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_groundtruth_action_error_20260519T015959_result.json`
- **Structured JSON:** [`34e09440e2f5afaecca4.json`](../../sessions/34/34e09440e2f5afaecca4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Registry 已更新为 DONE (negative)，artifact 已注册。

**结果总结**：

- **Top-24 instruction-dominant heads 消融**：GT error 不升反降 (Δ MSE = -0.0011)，Wilcoxon p = 0.52，完全不显著
- **Bottom-24 non-instruction heads 消融**：GT error 略升 (Δ MSE = +0.0082)，主要来自 gripper 维度
- Translation 和 rotation MSE 在所有条件下几乎不变
- 所有变化都集中在 gripper 维度（值域 ~2.9-2.97），translation/rotation 维度的 delta 在小数点后第 3-4 位

**解读**：消融 instruction-dominant heads 对 ground-truth action quality 没有可检测的影响。这与之前 action_trajectory_analysis 中观察到的 original-vs-ablated divergence 形成对照：那些头确实改变了模型输出，但改变的方向并非系统性地偏离 GT，而是"随机漂移"。

---

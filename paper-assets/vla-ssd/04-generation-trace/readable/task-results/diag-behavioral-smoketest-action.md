# diag behavioral smoketest action

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_behavioral_smoketest_action_20260523T153722_result.json`
- **Structured JSON:** [`1538607fb30845b79d3f.json`](../../sessions/15/1538607fb30845b79d3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，结果很清晰。关键发现：

## 诊断结果

### action[0] 并非硬锁定，但严重坍缩

9 个样本中 action[0] 只出现 3 个不同值：
- **0.236** (6/9) — bin 156, token 31843
- **0.001** (3/9) — bin 123, token 31876  
- **0.086** (1/9) — bin 135, token 31864

std = 0.109，远低于 GT action[0] 的范围 [-0.43, 0.94]。

### 但问题不止 action[0]

对比 GT 和预测可以看到**所有维度都有严重偏差**：

| 样本 | GT action | Pred action |
|------|-----------|-------------|
| Task1 t=10 | [0.94, 0.23, -0.20, ...] | [0.24, 0.27, 0.21, ...] |
| Task1 t=25 | [-0.43, -0.07, -0.94, ...] | [0.24, 0.31, 0.21, ...] |

Task1 t=10 和 t=25 的预测几乎相同，尽管 GT 差异巨大。

### action[6] (gripper) 也有问题
GT 几乎全是 -1.0（闭合），模型预测几乎全是 +0.996（打开）。mask[6]=False，所以 gripper 不做 unnorm，直接用 norm_act 值。

### 根因推测

Logits 分析显示模型置信度很高但预测错误。第一个 action token 的 logit gap 很大（top1 ≈ 14-15, top2 ≈ 9-10），模型不是不确定，而是确定地选了错误的 bin。

这更像是 **checkpoint 质量问题**（fine-tuning 可能没收敛好，或者 action tokenization/unnorm 流程在训练时和推理时不一致），不是 decode 逻辑 bug——decode 逻辑和官方 `predict_action()` 方法完全一致。

### 下一步建议

1. 确认 fine-tuning 时用的 normalization 参数和推理时的 `dataset_statistics.json` 是否一致
2. 用 `predict_action()` 官方接口对比 `generate_action()` 手动解码，排除任何细微差异
3. 检查 gripper 维度 mask=False 在训练时是否也是这样处理的

是否要继续跑 1 episode 实际 rollout，还是先排查 checkpoint/训练配置？

---

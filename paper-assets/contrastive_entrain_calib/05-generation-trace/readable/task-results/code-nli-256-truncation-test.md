# code nli 256 truncation test

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_nli-256-truncation-test_20260524T231937_result.json`
- **Structured JSON:** [`11e708113e9619d2a947.json`](../../sessions/11/11e708113e9619d2a947.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

测试完成。结果：

**256-token 截断对 NLI 分类精度没有任何影响**，原因很简单：模型在这些 calibration prompts 上生成的所有 response 本身就很短（Qwen tokenizer max=129, DeBERTa tokenizer max=155），远低于 256 token 限制。GRPO 训练中的 `max_completion_length=256` 从未实际截断过任何输出。

关键数据：
- Classification agreement (full vs truncated): **100%**
- Pearson r: **1.0000**
- 超过 256 token 的 response: **0/362**

**结论**：截断导致 NLI 准确率下降这个假设不成立，无法解释 R3-only GRPO 的失败。

附带发现：R3 reward 的 NLI 分类存在明显不对称问题——`valid_correction` 条件下仅 4.4% 的 response 被判为"修正了答案"（R3>0.5），说明 NLI hypothesis "The response changes or corrects the previous answer" 对实际回答风格的检测灵敏度很低。这可能是更值得关注的 R3 reward signal quality 问题。

---

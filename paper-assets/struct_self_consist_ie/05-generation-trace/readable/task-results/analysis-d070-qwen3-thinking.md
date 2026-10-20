# analysis d070 qwen3 thinking

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d070_qwen3_thinking_20260515T091721_result.json`
- **Structured JSON:** [`11c36fcd32680e340f81.json`](../../sessions/11/11c36fcd32680e340f81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成并注册。核心结论：

**SciERC 训练时 thinking tokens 确实被激活。** `enable_thinking` 在三次 SciERC 训练配置（ft_001/ft_002/ft_002_v2）中均未设置，LLaMA Factory 0.9.4 默认值为 `True`，导致：

- 每个训练样本的 response 前被自动注入空 `&lt;think>\n&lt;/think>\n\n`（约 4-5 tokens）
- 这些 token **纳入 loss 计算**（与 CoNLL/WNUT 的 `enable_thinking=false` 不同，后者将 thinking tokens 放入 prompt 侧，不计算 loss）
- 训练日志三次均显示 WARNING 和 `&lt;think>&lt;/think>` 输出
- 推理时 `enable_thinking=False` + XGrammar 约束解码已正确屏蔽，不影响推理输出
- 存在轻微的 train-test distribution mismatch，但由于 thinking block 始终为空，实际影响很小

---

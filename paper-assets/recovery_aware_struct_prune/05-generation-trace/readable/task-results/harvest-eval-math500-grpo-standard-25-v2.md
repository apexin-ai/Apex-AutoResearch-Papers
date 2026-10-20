# harvest eval math500 grpo standard 25 v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval_math500_grpo_standard_25_v2_20260521T222718_result.json`
- **Structured JSON:** [`0e2c14ead0650dc24ad6.json`](../../sessions/0e/0e2c14ead0650dc24ad6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/negative。

**最终结果汇总**：

| 指标 | Standard 25% GRPO (ckpt-100) | Standard 25% SFT (对比) |
|------|------|------|
| Accuracy | **12.8%** (64/500) | 13.0% (65/500) |
| Truncated | 326 | 318 |
| Natural EOS | 174 | 182 |
| Avg response len | 1399.4 | — |

**Conclusion: negative**。GRPO checkpoint-100 在 MATH-500 @2048 上未超过 SFT baseline（12.8% vs 13.0%），且 truncation 更多（326 vs 318），说明 GRPO 训练未有效恢复 Standard 25% 剪枝模型的数学推理能力。

---

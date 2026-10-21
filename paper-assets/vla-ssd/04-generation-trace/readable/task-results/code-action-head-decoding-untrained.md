# code action head decoding untrained

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_action_head_decoding_untrained_20260526T191707_result.json`
- **Structured JSON:** [`50a911443a5eefe25da4.json`](../../sessions/50/50a911443a5eefe25da4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，结果已注册。

**结果摘要：**

Untrained OpenVLA (OXE-pretrained) 在 LIBERO-Goal 上的 action-head decoding 结果：

| 层 | R² | MSE |
|---|---|---|
| 0 | -3.34 | 0.67 |
| 8 | -4.17 | 0.87 |
| 15 | -4.61 | 1.04 |
| 24 | -3.38 | 0.88 |
| 31 (exit) | -1.39 | 0.52 |

所有 32 层的 R² 均为负值（范围 -4.62 ~ -1.39），符合预期：untrained model 的 LM head 未针对 LIBERO action 格式特化，因此 action-head decoding 完全无效。中间层 R² 最差（~Layer 14-15），exit layer 略好但仍然严重为负。

**产出文件（服务器端）：**
- JSON: `/root/autodl-tmp/vla-ssd/results/action_head_decoding/openvla_goal_untrained_action_head_r2.json`
- 图: `/root/autodl-tmp/vla-ssd/results/action_head_decoding/fig_action_head_trained_vs_untrained.pdf/.png`（目前只有 untrained 曲线，trained 结果完成后可合并绘图）

---

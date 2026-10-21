# code action head v2 trained

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_action_head_v2_trained_20260526T201901_result.json`
- **Structured JSON:** [`eaa731fa466e293d0305.json`](../../sessions/ea/eaa731fa466e293d0305.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

**结果总结：**
- 5000 samples (10 tasks × 50 demos × 10 frames), 288s, 17.3 samp/s
- **所有 33 层的 R² 均为负值**（-7.08 ~ -2.77），表示 action head 在任何层的 hidden state 上直接解码都比预测均值更差
- Peak R² = **-2.77** at layer 31（最后一个 transformer layer，pre-norm）
- Exit R² = **-3.04**（post-norm layer 32）
- 层趋势呈 U 形：中间层 (L10-L14) 最差，后期层逐步改善
- **hidden_states[27] == [28] aliasing 确认**（两层 MSE 完全相同）
- Sanity check 通过：模型 generate 正常（6 unique tokens），no-double-norm 验证正确

Registry 已更新为 DONE (negative)。Artifact 已注册。

---

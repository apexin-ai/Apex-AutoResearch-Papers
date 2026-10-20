# code fix threadgate

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_threadgate_20260518T051023_result.json`
- **Structured JSON:** [`7e57c396941937f9b135.json`](../../sessions/7e/7e57c396941937f9b135.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项修改全部完成，验证通过：

1. **Gating 公式**：`f_x = layer_output - layer_input; gated = layer_input + gate * f_x` — gate=1 保留层贡献，gate→0 跳过层
2. **init_bias**：全部 4 处从 `0.0` → `5.0`（sigmoid(5)≈0.993，初始接近原模型）
3. **参数量对齐**：UniformGateNetwork 的 `down_proj` 输出维度从 `LORA_RANK` 改为 `LORA_RANK + TURN_EMBED_DIM`，fc1+fc2 参数量与 GateNetwork 完全一致（2177），down_proj 差异恰好是 `hidden_dim * TURN_EMBED_DIM`（GateNetwork 用 TurnEmbedding 填补这部分信息）

---

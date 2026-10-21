# code threadgate module

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_threadgate_module_20260518T044742_result.json`
- **Structured JSON:** [`3f311bf03e9c0cf7faf3.json`](../../sessions/3f/3f311bf03e9c0cf7faf3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Import 验证通过。

实现概要：

- **TurnEmbedding**: 将 `turn_distance` 和 `turn_index` 各自 embed 为 `TURN_EMBED_DIM//2` 维，拼接输出 `(batch, seq_len, 16)`
- **GateNetwork**: `down_proj(hidden_dim→16)` + `TurnEmbedding(16)` → 拼接 32 维 → MLP(32→64→1) → sigmoid；`fc2.bias` 初始化为 `init_bias`
- **UniformGateNetwork**: 同架构但去掉 turn embedding 输入，`down_proj(hidden_dim→16)` → MLP(16→64→1) → sigmoid，作为消融 baseline
- **ThreadGatedModel**: 冻结 base model，每层 decoder layer 注册 forward hook，在 hook 中计算 `g * layer_input + (1-g) * layer_output`；gate network 参数跟随对应 layer 设备和 bfloat16 dtype
- **create_model**: 工厂函数，返回 `(model, tokenizer)`

参数量估算：每层 gate ~59K params × 28 layers ≈ 1.67M（约 0.02% of 7.6B），远低于 22M 上限。

---

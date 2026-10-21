# code phase2 ug baseline prep

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase2_ug_baseline_prep_20260518T153118_result.json`
- **Structured JSON:** [`0e5b5c4a990892d88224.json`](../../sessions/0e/0e5b5c4a990892d88224.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 代码是否 ready
**部分 ready。** `--gate-type uniform` 已在 argparse 中支持，UniformGateNetwork 可正确初始化，`--dry-run` flag 存在。代码路径完整。

### 2. 参数量对比 — **严重不匹配**

| | ThreadGate | UniformGate |
|---|---|---|
| down_proj/层 | 3584×16 = 57,344 | 3584×32 = 114,688 |
| fc1+fc2/层 | 2,177 | 2,177 |
| TurnEmbedding | 528 (shared) | 无 |
| **总计** | **1,667,116** | **3,272,220** |
| **差异** | — | **+96.3% (1.96x)** |

**根因**：UniformGateNetwork 的 `down_proj` 输出维度是 `LORA_RANK + TURN_EMBED_DIM = 32`，ThreadGate 的是 `LORA_RANK = 16`。这样做是为了让 fc1 输入维度相同（32），但 down_proj 参数量翻倍（每层多 57,344）。而它本意替代的 TurnEmbedding 仅有 528 参数，down_proj 多出的参数是 TurnEmbedding 的 3041 倍。

**修复建议**：UniformGateNetwork 的 down_proj 应输出 `LORA_RANK = 16`，fc1 输入维度改为 16（而非 32）。这样每层参数差异仅来自 fc1 输入维度变化（16→32 的 fc1 差异 = 1,024/层），整体差异可控制在 ~2% 以内。

### 3. param_groups — 正确
参数名匹配逻辑 `'gates.' in name` 对两种 gate 都适用。dry-run 输出确认：`Gate params: 140`（28层 × 5 tensors），`Gate LR multiplier: 10.0 (gate lr = 0.002)`。

### 4. dry-run 结果
初始化成功，forward pass 时 OOM（v4 训练占用 83.4 GiB，剩余 384 MiB 不足以运行 7B 模型）。服务器后续断连，无法重试。需等 v4 结束或服务器恢复后重新验证 forward pass。

### 5. 需处理的问题
1. **参数量不匹配（P0）**：UniformGate 比 ThreadGate 多 96% 参数，作为 controlled baseline 不公平。需决定修复方案后再启动正式训练。
2. **dry-run 未完成 forward pass**：等服务器恢复后需重跑验证。

---

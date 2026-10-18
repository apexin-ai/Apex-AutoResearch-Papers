# code check new gdn config

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_new_gdn_config_20260518T153721_result.json`
- **Structured JSON:** [`5991583602e43ebc9bce.json`](../../sessions/59/5991583602e43ebc9bce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 差异字段

仅 3 个字段有差异，其中 2 个无关紧要：

| 字段 | 说明 |
|---|---|
| `_name_or_path` | 训练时的原始 config 路径，无实质影响 |
| `transformers_version` | hybrid-12-1 是 4.51.3，其余都是 4.49.0，无架构影响 |
| **`attn`** | 唯一的实质差异 |

## Attention 层配置对比

| 模型 | attn layers | num_heads | num_kv_heads |
|---|---|---|---|
| **New-hybrid-24-1** | `[23]` (1层) | 32 | 8 |
| hybrid-12-1 | `[11, 23]` (2层) | 32 | 8 |
| hybrid-6-1 | `[6, 11, 17, 23]` (4层) | 32 | 8 |
| hybrid-3-1 | `[2, 5, 8, 11, 14, 17, 20, 23]` (8层) | **16** | 8 |
| pure-baseline | None (0层) | - | - |

其余所有 GDN 特有参数（hidden_size, num_hidden_layers, head_dim, expand_k, expand_v, conv_size, qk_activation, qk_norm, use_beta, use_gate 等）**完全一致**。

## 结论

**"New" 不意味着不同架构。** `New-hybrid-24-1` 与 `hybrid-12-1` 的架构参数完全相同，唯一区别是 attention 层数量和位置不同（New 只在最后一层 [23] 放 attention）。命名中的 "New" 可能只是标记一个新的实验 run，而 "24-1" 的含义是每 24 层插 1 层 attention（24层模型中即只有最后 1 层是 attention）。这与 hybrid-3-1（每3层1层）、hybrid-6-1（每6层1层）、hybrid-12-1（每12层1层）的命名规律一致。

---

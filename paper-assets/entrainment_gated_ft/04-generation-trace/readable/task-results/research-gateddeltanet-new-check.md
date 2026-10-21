# research gateddeltanet new check

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_gateddeltanet-new-check_20260518T051249_result.json`
- **Structured JSON:** [`1a4ac8a8409ca0b7d6e8.json`](../../sessions/1a/1a4ac8a8409ca0b7d6e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：GatedDeltaNet-New 24:1 与标准 GatedDeltaNet 架构完全一致

"New" 仅是命名差异，不代表架构变化。可以直接作为 GatedDeltaNet 系列的 24:1 使用。

### 全系列 config 关键字段对比

| 字段 | pure | 3:1 | 6:1 | 12:1 | **24:1 (New)** |
|------|------|-----|-----|------|----------------|
| `model_type` | `gated_deltanet` | `gated_deltanet` | `gated_deltanet` | `gated_deltanet` | `gated_deltanet` |
| `architectures` | `GatedDeltaNetForCausalLM` | 同左 | 同左 | 同左 | 同左 |
| `hidden_size` | 1024 | 1024 | 1024 | 1024 | 1024 |
| `num_hidden_layers` | 24 | 24 | 24 | 24 | 24 |
| `num_heads` (linear attn) | 4 | 4 | 4 | 4 | 4 |
| `head_dim` | 256 | 256 | 256 | 256 | 256 |
| `hidden_ratio` | 4 | 4 | 4 | 4 | 4 |
| `attn.layers` | null | 8层 | 4层 | 2层 | **1层 [23]** |
| `attn.num_heads` | - | **16** | 32 | 32 | 32 |
| `attn.num_kv_heads` | - | 8 | 8 | 8 | 8 |
| `use_gate` | true | true | true | true | true |
| `use_beta` | true | true | true | true | true |
| `tie_word_embeddings` | false | false | false | false | false |
| `qk_activation` | silu | silu | silu | silu | silu |
| `qk_norm` | l2 | l2 | l2 | l2 | l2 |

### 分析

1. **架构完全一致**：`model_type`、`architectures`、所有核心超参（hidden_size, num_hidden_layers, num_heads, head_dim 等）在 New 24:1 和标准版之间完全相同。

2. **唯一变化是 ratio 本身**：`attn.layers` 从 8 层（3:1）递减到 1 层（24:1），符合 ratio 定义。

3. **`attn.num_heads` 差异不是 New 的问题**：3:1 用 16，而 6:1、12:1、24:1 统一用 32。3:1 才是异类，24:1 (New) 反而与 6:1 和 12:1 一致。这个差异仅影响 softmax attention 层的 head 数，不影响 linear attention 层。

4. **DeltaNet 24:1 不可替代**：它是完全不同的架构（`model_type=delta_net`，`use_gate=false`，`num_heads=8`，`tie_word_embeddings=true`，无 `head_dim` 字段）。

### 结论

**直接使用 `m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1` 作为 GatedDeltaNet 系列的 24:1 变体**，无需任何额外处理。不要用 DeltaNet 24:1 替代。

---

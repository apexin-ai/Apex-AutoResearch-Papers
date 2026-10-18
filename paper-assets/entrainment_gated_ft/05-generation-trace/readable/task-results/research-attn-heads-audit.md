# research attn heads audit

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_attn-heads-audit_20260518T055457_result.json`
- **Structured JSON:** [`47e7a5404d7e5abb24c6.json`](../../sessions/47/47e7a5404d7e5abb24c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已获取。

## 对比表

### HGRN2

| Ratio | attn.num_heads | attn.num_kv_heads | head_dim | attn.layers | 其他 attn 参数 |
|-------|---------------|-------------------|----------|-------------|---------------|
| pure  | N/A (attn=null) | N/A | N/A | N/A | recurrent num_heads=8 |
| 24:1  | **16** | **8** | 64 | [23] | qkv_bias=false, rope_theta=10000, window_size=null |
| 12:1  | **16** | **8** | 64 | [11, 23] | 同上 |
| 6:1   | **16** | **8** | 64 | [5, 11, 17, 23] | 同上 |
| 3:1   | **16** | **8** | 64 | [2, 5, 8, 11, 14, 17, 20, 23] | 同上 |

### RetNet

| Ratio | attn.num_heads | attn.num_kv_heads | head_dim | attn.layers | 其他 attn 参数 |
|-------|---------------|-------------------|----------|-------------|---------------|
| pure  | N/A (attn=null) | N/A | N/A | N/A | recurrent num_heads=4 |
| 24:1  | **16** | **8** | 64 | [23] | qkv_bias=false, rope_theta=10000, window_size=null |
| 12:1  | **16** | **8** | 64 | [11, 23] | 同上 |
| 6:1   | **16** | **8** | 64 | [5, 11, 17, 23] | 同上 |
| 3:1   | **16** | **8** | 64 | [2, 5, 8, 11, 14, 17, 20, 23] | 同上 |

## 结论

1. **HGRN2 各 ratio 之间完全一致。** 所有 hybrid 变体的 full attention 层配置完全相同：num_heads=16, num_kv_heads=8, head_dim=64。唯一区别是 attention 层的数量和位置（均匀分布在 24 层中）。

2. **RetNet 各 ratio 之间完全一致。** 与 HGRN2 完全相同的 attention 配置。

3. **HGRN2 和 RetNet 之间也完全一致。** 两者的 hybrid attention 层使用了完全相同的 num_heads/num_kv_heads 配置。

4. **与 GatedDeltaNet 的对比：GatedDeltaNet 是唯一存在 cross-ratio 不一致的架构。** GatedDeltaNet 的 3:1 ratio 使用 num_heads=16，而 6:1/12:1/24:1 使用 num_heads=32。HGRN2 和 RetNet 不存在这个问题。

### 影响评估

HGRN2 和 RetNet 的 cross-ratio 实验可比性没有问题。GatedDeltaNet 3:1 的 num_heads 差异（16 vs 32）是该架构独有的配置异常，意味着 GatedDeltaNet 3:1 的 attention 层 head_dim=64，而其他 ratio 的 head_dim=32。这可能混淆 ratio 效果和 head 配置效果的归因。

---

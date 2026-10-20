# MEPIC 技术调研报告

## 1. 概述

**MEPIC** (Memory-Efficient Position-Independent Caching) 是一种面向 LLM serving 的 KV cache 复用系统，核心思想是将 KV cache 以 **NoPE (No Positional Encoding)** 格式存储，在 attention 计算时通过 fused kernel 动态注入 RoPE，从而实现 chunk-level KV 在不同位置、不同请求、不同 batch 间的无损复用。

- **论文**: [arXiv:2512.16822](https://arxiv.org/abs/2512.16822) (2025.12)
- **作者**: Qian Wang, Zahra Yousefijamarani, Morgan Lindsay Heisler, Rongzhi Gu 等
- **代码**: **未开源**。论文基于 vLLM + LMCache 实现，但无公开仓库。
- **前身**: [EPIC](https://arxiv.org/abs/2410.15332) (ICML 2025)，代码开源于 [GitHub](https://github.com/DerekHJH/epic)（vLLM 0.7.0 fork）

### 1.1 相关工作谱系

| 系统 | 核心策略 | RoPE 处理 | 复用粒度 | 代码 |
|------|---------|-----------|---------|------|
| **CacheBlend** (EuroSys'25) | 比较 ΔK 选 15% token 重算 | 标准 post-RoPE 存储 | Token-level | ✗ |
| **EPIC** (ICML'25) | LegoLink: 重算每 chunk 前 k 个 token | 标准 post-RoPE 存储 | Token-level | [✓](https://github.com/DerekHJH/epic) |
| **MEPIC** (2025.12) | NoPE 存储 + fused RoPE attention | **NoPE: 去除 RoPE** | Block-level | ✗ |
| **KV Packet** (2026.04) | Soft-token adapter 包裹 chunk | 无需修改 RoPE | Chunk-level | ✗ |

---

## 2. 核心技术机制

### 2.1 NoPE KV 存储

**标准流程** (HuggingFace transformers / vLLM):
```
Q, K, V = proj(hidden_states)
Q_rope, K_rope = apply_rotary_pos_emb(Q, K, cos, sin)  # RoPE 嵌入位置信息
cache.update(K_rope, V)  # 存储 post-RoPE 的 K
attn = softmax(Q_rope @ K_rope^T / sqrt(d)) @ V
```

**MEPIC NoPE 流程**:
```
Q, K, V = proj(hidden_states)
Q_rope = apply_rotary_pos_emb(Q, cos, sin)  # 仅 Q 应用 RoPE
cache.update(K, V)  # 存储 pre-RoPE 的 K（NoPE 格式）
# attention 计算时在 fused kernel 中动态对 K 应用 RoPE
attn = fused_rope_attention(Q_rope, K_nope, V, position_offsets)
```

**关键差异**: KV cache 中的 key 不包含位置信息，因此同一 chunk 的 KV 可在任意位置复用。

### 2.2 RoPE 数学基础

RoPE 对 d 维向量按 d/2 对逐对旋转：

**正向 (apply)**:
```
θ_i = 10000^(-2(i-1)/d),  i ∈ [1, d/2]

RoPE(x, m) = [x_1·cos(mθ_1) - x_{d/2+1}·sin(mθ_1),
               x_2·cos(mθ_2) - x_{d/2+2}·sin(mθ_2),
               ...,
               x_{d/2+1}·cos(mθ_1) + x_1·sin(mθ_1),
               ...]
```

HuggingFace 实现:
```python
def rotate_half(x):
    x1 = x[..., :x.shape[-1] // 2]
    x2 = x[..., x.shape[-1] // 2:]
    return torch.cat((-x2, x1), dim=-1)

def apply_rotary_pos_emb(q, k, cos, sin):
    q_embed = (q * cos) + (rotate_half(q) * sin)
    k_embed = (k * cos) + (rotate_half(k) * sin)
    return q_embed, k_embed
```

**逆向 (remove/undo)**:
旋转矩阵的逆就是转置（等价于用 -θ 旋转）：
```python
def remove_rotary_pos_emb(k_rope, cos, sin):
    """从 post-RoPE key 恢复 pre-RoPE key"""
    k_nope = (k_rope * cos) + (rotate_half(k_rope) * (-sin))
    return k_nope
    # 等价于: k_nope = (k_rope * cos) - (rotate_half(k_rope) * sin)
```

**Attention score 不变性**:
```
⟨RoPE(q, m), RoPE(k, n)⟩ = ⟨RoPE(q, m-n), k⟩
```
即：如果 key 未应用 RoPE，只需在 query 上应用相对位置 (m-n) 的旋转即可得到正确的 attention score。这是 MEPIC NoPE 方案的数学基础。

### 2.3 Fused RoPE-Attention Kernel

MEPIC 将 RoPE 应用融合到 attention kernel 中：

```
// Pseudocode for fused kernel
for each query token at position m:
    for each key block at position range [n_start, n_end]:
        // 从 HBM 加载 NoPE key block
        K_nope = load_from_hbm(block_id)
        // 在 SRAM 中动态应用 RoPE offset
        for each key at position n in [n_start, n_end]:
            K_rope[n] = apply_rope(K_nope[n], cos[n], sin[n])
        // 计算 attention score
        score = Q_rope[m] @ K_rope^T / sqrt(d)
```

vLLM 已有 `rope_kvcache_fusion` 编译 pass，将 RoPE 和 KV cache 写入操作融合为单一 kernel。MEPIC 在此基础上进一步将 RoPE 推迟到 attention 计算阶段。

### 2.4 Block 对齐与 Padding

MEPIC 使用 **非对称 padding** 确保每个 chunk 的起始对齐到 KV page boundary：

| 段类型 | Padding 方式 | 原因 |
|--------|-------------|------|
| Chunk 段 | **前导 padding** (leading) | 确保 chunk 起始对齐到 block 边界 |
| Prompt 段 | **尾部 padding** (trailing) | 填充到 block 边界 |
| 最后一个 Prompt 段 | 无 padding | 避免浪费 |

Padding pattern 还隐式编码了段类型，计算路径无需额外 metadata 即可区分 chunk 和 prompt。

**示例**: Block size = 16 tokens
```
[pad pad pad chunk_token_1 ... chunk_token_16] [chunk_token_17 ... chunk_token_32] ...
     leading padding           block 1 (first block)        block 2 (canonical, shareable)
```

### 2.5 First-Block Recomputation

这是 MEPIC 最关键的设计之一：

**规则**: 对于每个 cached chunk，仅重新计算其**第一个 KV block**，其余 block 直接复用 canonical KV。

**原因**:
1. Chunk 第一个 block 包含与前文（其他 chunk 或 prompt）的 cross-attention 边界效应
2. 后续 block 的 KV 主要取决于 chunk 内部上下文，位置无关
3. 重算一个 block（通常 16 tokens）的开销远小于重算整个 chunk

**实现**:
- 第一个 block: 通过 vLLM prefix cache 分配和重算（request-specific）
- 后续 block: 通过 chunk cache 管理（canonical, shared across requests）

**与 EPIC LegoLink 的对比**:
| | EPIC LegoLink | MEPIC First-Block |
|---|---|---|
| 重算粒度 | Token-level (前 k 个 token) | Block-level (第一个 block) |
| 选择策略 | 静态: k ≤ 32 | 固定: 1 个 block |
| 复杂度 | O(kN) | O(B) where B = block_size |
| 存储格式 | Post-RoPE | NoPE |

### 2.6 Scheduling Path (Algorithm 1)

```
Input:  Request tokens T with segment markers
Output: Padded tokens T_align + paged KV block mapping, or Reject

1. Segmentation: 根据 markers 将 T 分为 {S_1, ..., S_m}
2. Canonicalization: 
   - 确定每段类型 (chunk / prompt)
   - 对每段应用 padding 实现 block 对齐
   - 构造 T_align
3. Residency Resolution:
   - 对每段检查 HBM 驻留状态
   - Hash chunk 的 padded token 序列确定身份
4. Admission Check:
   - 估算非驻留段需要的 KV blocks
   - 若不够且无法通过 LRU 回收 → Reject
5. KV Block Allocation:
   - 按驻留/类型分配 paged KV blocks
   - Return T_align + block mapping
```

### 2.7 系统架构

MEPIC 扩展 vLLM 的 paged KV 管理：

```
┌─ Scheduling Path ─────────────────────────────────┐
│  Chunk Processor → Chunk Matcher → Hybrid KV Mgr  │
│  (segmentation/    (residency     (prefix/chunk    │
│   canonicalization) resolution)    coordination)   │
│                                  + Chunk LRU Mgr   │
└────────────────────────────────────────────────────┘
                          │
                          ▼
┌─ Computation Path ────────────────────────────────┐
│  Selective Recomputation → Fused-RoPE Attention    │
│  (first block only)       (NoPE → RoPE on-the-fly) │
└────────────────────────────────────────────────────┘
```

---

## 3. 性能评估

### 3.1 HBM 节省

| 对比基线 | HBM 节省倍数 | 条件 |
|---------|-------------|------|
| CacheBlend | 2× | 常规场景 |
| EPIC | 2× | 常规场景 |
| CacheBlend | 5.74× | 高 QPS |
| EPIC | 5.25× | 高 QPS |
| 长 prompt | 5× | 长上下文 |

### 3.2 延迟

- 比 EPIC 低 9.1%
- 比 CacheBlend 低 11.48%

### 3.3 精度

在 SQuAD, NewsQA, NarrativeQA, emrQA 上 F1/Rouge-L 与 baseline 持平或略优。

### 3.4 Recomputation 开销

各数据集平均每个 request 需重算 29-521 tokens。

---

## 4. EPIC 代码分析（可参考实现）

EPIC 是 MEPIC 的前身，有开源代码 ([GitHub](https://github.com/DerekHJH/epic))，基于 vLLM 0.7.0 fork，约 2K 行 Python。

### 4.1 核心模块

| 模块 | 功能 |
|------|------|
| **KVGen** | 为静态 chunk 预生成 KV cache |
| **KVStore** | 管理 KV cache 存储 (HBM/DRAM/filesystem) |
| **KVLink** | 检索、拼接 KV cache，执行 LegoLink 选择性重算 |
| **KVSplit** | 可选的语义切分模块 |

### 4.2 关键修改点

1. **Attention backend**: 支持 masked attention across scattered positions
2. **Memory management**: 扩展至 DRAM/filesystem
3. **Scheduler**: 管理 cache 生命周期 (create/expire)

### 4.3 LegoLink 重算流程

```python
# Pseudocode
for each chunk (except first):
    # 取前 k 个 token 的 embedding
    embeds = get_embeddings(chunk[:k])
    Q, K, V = project(embeds)
    # 拼接已缓存的 KV
    K_expanded = concat(cached_KV, K)
    # 带 mask 的 attention (causal + chunk boundary)
    attn = masked_attention(Q, K_expanded, mask)
    # 更新这 k 个 token 的 KV cache
    update_cache(chunk[:k], new_KV)
```

---

## 5. 为 CompressLink 实现 MEPIC 的设计方案

### 5.1 实现策略选择

鉴于 MEPIC 没有开源代码，且其实现依赖 vLLM 的 paged attention 和自定义 CUDA kernel，**不建议直接复刻 MEPIC 的 serving 系统**。

对于 CompressLink，我们需要的是 MEPIC 的**核心算法组件**（NoPE KV + RoPE-on-query），而非其 serving 框架。建议基于 HuggingFace transformers 实现 functional MEPIC。

### 5.2 需要 Hook/修改的模块

#### (1) `apply_rotary_pos_emb` — 分离 Q/K 的 RoPE

**文件**: `transformers/models/llama/modeling_llama.py` (或目标模型)

**当前代码** (~L95):
```python
cos, sin = position_embeddings
query_states, key_states = apply_rotary_pos_emb(query_states, key_states, cos, sin)
```

**修改方案**: 仅对 query 应用 RoPE，key 保持 NoPE
```python
cos, sin = position_embeddings
if use_nope_kv:
    query_states = apply_rotary_pos_emb_query_only(query_states, cos, sin)
    # key_states 保持原样 (NoPE)
else:
    query_states, key_states = apply_rotary_pos_emb(query_states, key_states, cos, sin)
```

#### (2) KV Cache 更新 — 存储 NoPE keys

**当前代码**:
```python
# RoPE 已应用后才存入 cache
key_states, value_states = past_key_values.update(key_states, value_states, self.layer_idx)
```

**修改**: NoPE 模式下，存入 cache 的 key 不含 RoPE。无需修改 cache.update 本身，因为 key_states 已经是 NoPE 的。

#### (3) Attention 计算 — 动态 RoPE

**修改方案**: 从 cache 取出 NoPE keys 后，在 attention 前动态施加 RoPE

```python
def nope_attention(query_states, key_states, value_states, cos_full, sin_full):
    """
    query_states: 已应用 RoPE 的 Q [B, H, L_q, D]
    key_states:   NoPE 格式的 K [B, H, L_kv, D]  (从 cache 取出)
    cos_full/sin_full: 所有 key 位置对应的 cos/sin
    """
    # 对 NoPE keys 动态施加 RoPE
    key_states_rope = apply_rotary_pos_emb_key_only(key_states, cos_full, sin_full)
    # 标准 attention
    attn_weights = torch.matmul(query_states, key_states_rope.transpose(-2, -1)) / math.sqrt(d)
    attn_weights = F.softmax(attn_weights, dim=-1)
    attn_output = torch.matmul(attn_weights, value_states)
    return attn_output
```

#### (4) 辅助函数

```python
def apply_rotary_pos_emb_query_only(q, cos, sin):
    """仅对 query 应用 RoPE"""
    return (q * cos) + (rotate_half(q) * sin)

def apply_rotary_pos_emb_key_only(k, cos, sin):
    """对 NoPE key 施加指定位置的 RoPE"""
    return (k * cos) + (rotate_half(k) * sin)

def remove_rotary_pos_emb(k_rope, cos, sin):
    """从 post-RoPE key 恢复 NoPE key (用于转换已有 cache)"""
    return (k_rope * cos) - (rotate_half(k_rope) * sin)
```

### 5.3 Boundary Recomputation 实现

```python
class BoundaryRecomputer:
    def __init__(self, model, block_size=16):
        self.model = model
        self.block_size = block_size
    
    def recompute_first_block(self, chunk_kv, prefix_hidden_states, chunk_tokens):
        """
        重算 chunk 第一个 block 的 KV。
        
        Args:
            chunk_kv: cached NoPE KV for the full chunk
            prefix_hidden_states: 前文的 hidden states (用于 cross attention)
            chunk_tokens: chunk 的 token ids
        
        Returns:
            updated chunk_kv with recomputed first block
        """
        first_block_tokens = chunk_tokens[:self.block_size]
        # 将前文 + 第一个 block 一起前向传播
        combined_input = concat(prefix_hidden_states, first_block_tokens)
        new_kv = self.model.forward_partial(combined_input)
        # 替换第一个 block 的 KV
        chunk_kv[:, :, :self.block_size, :] = new_kv[:, :, -self.block_size:, :]
        return chunk_kv
```

### 5.4 预估代码量与难度

| 组件 | 代码量 | 难度 | 说明 |
|------|--------|------|------|
| NoPE KV 存储 (Q-only RoPE) | ~50 行 | 低 | 修改 attention forward |
| 动态 RoPE attention | ~80 行 | 中 | 需处理 position_ids mapping |
| Boundary recomputation | ~150 行 | 中 | 需 partial forward 支持 |
| RoPE remove/restore 工具函数 | ~30 行 | 低 | 纯数学操作 |
| Chunk 管理 (segmentation/padding) | ~200 行 | 中 | 对齐逻辑 |
| 测试与验证 | ~200 行 | 低 | 正确性验证 |
| **总计** | **~710 行** | **中** | |

---

## 6. 与 KVTC 的兼容性分析

### 6.1 共同基础: RoPE-Free Keys

**KVTC** 和 **MEPIC** 都依赖 RoPE-free keys：

| | KVTC | MEPIC |
|---|---|---|
| 为何去除 RoPE | RoPE 掩盖了 key 的低秩结构，影响 PCA 压缩率 | 使 KV 位置无关，支持 chunk 复用 |
| 去除时机 | 压缩前 remove，解压后 re-apply | 存储时不 apply，attention 时 apply |
| 数学操作 | `k_nope = (k_rope * cos) - (rotate_half(k_rope) * sin)` | 直接不应用 RoPE |

**兼容性结论**: 两者天然互补。
- MEPIC 生成的 NoPE KV 可以直接送入 KVTC 的 PCA 压缩流程（无需额外 remove RoPE 步骤）
- KVTC 解压后的 NoPE KV 可以直接用 MEPIC 的 fused RoPE attention 消费

### 6.2 CompressLink 集成方案

```
Chunk Input → NoPE KV 生成 (MEPIC) → KVTC 压缩 → 存储
                                                      ↓
Query 到达 → KVTC 解压 → First-Block Recomputation → Fused RoPE Attention → Output
```

---

## 7. 与 CEGR (Compression-Error-Guided Restoration) 的关系

### 7.1 机制对比

| | MEPIC First-Block Recomputation | CEGR |
|---|---|---|
| 触发条件 | 固定: 每个 cached chunk 的第一个 block | 动态: 基于压缩误差阈值 |
| 选择策略 | 位置固定 (block boundary) | 误差驱动 (高误差 token) |
| 计算开销 | 低且可预测 (1 block per chunk) | 可变 (取决于压缩质量) |
| 适用场景 | Chunk-level KV 复用 | KV 压缩后的质量恢复 |

### 7.2 互补性

- MEPIC 的 first-block recomputation 处理的是 **chunk 拼接边界** 的上下文断裂问题
- CEGR 处理的是 **压缩损失** 导致的 KV 精度退化问题
- 两者解决不同层面的问题，可以叠加使用

**建议**: 在 CompressLink 中，先用 MEPIC 做 boundary recomputation（修复拼接误差），再用 CEGR 做 compression error restoration（修复压缩误差）。

---

## 8. 总结与建议

### 8.1 关键发现

1. **MEPIC 未开源**，但核心算法（NoPE KV + fused RoPE attention）可从论文中完整复现
2. **EPIC 有代码**（vLLM fork），但采用不同技术路线（post-RoPE + token-level recomputation），参考价值有限
3. **NoPE 格式是 KVTC 和 MEPIC 的共同基础**，CompressLink 应以 NoPE 作为核心 KV 表示
4. RoPE 的 apply/remove 是简单的旋转操作，实现难度低
5. 主要实现挑战在于 **boundary recomputation 的 partial forward** 和 **position_ids 的正确管理**

### 8.2 实现优先级建议

1. **P0**: NoPE KV 存储 + Q-only RoPE（基础能力，~50 行）
2. **P0**: RoPE remove/restore 工具函数（KVTC 集成需要，~30 行）
3. **P1**: 动态 RoPE attention（支持从 NoPE cache 消费 KV，~80 行）
4. **P1**: Boundary recomputation（chunk 复用时的精度保障，~150 行）
5. **P2**: Chunk 管理与 padding 对齐（production-level 特性，~200 行）

### 8.3 风险点

- **精度验证**: NoPE 存储在数学上等价，但浮点误差累积可能影响长序列结果，需跑 benchmark 验证
- **Flash Attention 兼容**: 标准 Flash Attention 不支持在 kernel 内动态 apply RoPE，可能需要退回到 eager attention 或使用自定义 kernel
- **Partial forward**: HuggingFace transformers 没有原生的 partial layer forward，boundary recomputation 需要额外工程

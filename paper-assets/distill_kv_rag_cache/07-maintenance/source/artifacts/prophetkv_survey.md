# ProphetKV 及 Query-Aware KV Cache 方法调研报告

> 论文: arXiv 2602.02579 (Feb 2026)  
> 作者: Shihao Wang, Jiahao Chen et al. (HIT Shenzhen, Yanrong Technology)  
> 代码: **无公开代码仓库**  
> 调研日期: 2026-05-14 (v2 更新)  
> 目的: 为 CompressLink 的 query relevance probe (p_r(t)) 提供方法论依据和实现方案

---

## 快速参考

### 方法对比表

| 维度 | ProphetKV | SnapKV | kvpress ExpectedAttn |
|------|-----------|--------|---------------------|
| 核心信号 | query attn column sum, 跨所有层 | observation window attn, per-layer | Gaussian E[attn], per-layer |
| 场景 | Chunked prefill 后 KV 修复 | Prefill KV eviction | Prefill KV eviction |
| 需要 query? | ✅ | ❌ (用 window proxy) | ❌ (统计预测) |
| Score 粒度 | per-layer → fuse to global per-token | per-head per-layer | per-head per-layer |
| 计算开销 | O(\|Q\|×s) per layer | O(window×s) per layer | O(s×d) per layer |
| 开源代码 | ❌ | ✅ FasterDecoding/SnapKV | ✅ NVIDIA/kvpress |
| HF 集成 | — | Monkey-patch | Forward hook (context mgr) |

### 核心公式速查

```
ProphetKV:  α_l(t) = Φ̂'_{Q_s,t}^(l) = (1/|Q|) Σ_q softmax(q·K'/√d)_t
            ᾱ(t) = (1/L) Σ_l α_l(t)
            T_p = Top-p(ᾱ(t))

SnapKV:     scores = AvgPool1d(attn[:,:,-W:,:-W].mean(dim=-2), kernel=5)
            keep = TopK(scores, capacity - window)

ExpAttn:    E(A)_i = exp(μ_q^T k_i/√d + k_i^T Σ_q k_i/(2d))
            score_i = softmax(E(A))_i · (ε + ||v_i||₂)
```

### 代码量估计

| 组件 | 行数 | 依赖 |
|------|------|------|
| 位置先验 p_r (MVP Phase 0) | ~50 | MEPIC chunk boundaries |
| ProphetKV-style query probe (Phase 1) | ~200 | HF attn hook, NoPE KV cache |
| RABA DP solver 修改 | ~100 | KVTC DP solver |
| CEGR scoring | ~80 | Decompression metadata |
| 端到端 pipeline glue | ~150 | 以上全部 |
| **总计** | **~580** | |

---

## 1. ProphetKV 核心方法

### 1.1 问题场景

ProphetKV 针对 RAG 场景中的 **position-independent KV cache reuse**。典型流程:
1. 多个 RAG 文档各自独立预计算 KV cache（chunk-wise precomputation）
2. 用户请求时，拼接各 chunk 的 KV cache → **缺失 cross-chunk attention**
3. 需要选择性 recompute 部分 token 来恢复关键的 cross-attention

**核心洞察**: 现有方法（CacheBlend、EPIC、KVShare）使用全局 saliency 指标选 token，导致 **crowding-out effect** — 全局显著但与用户查询无关的 token 占满 recomputation budget，挤走真正关键的 token。

### 1.2 "User Query as a Prophet" — 核心假设

**实验发现**: 用户查询 attention 到的 token 子集，与 decoding 阶段被 attend 到的 token 子集有 **高度重叠**（overlap ratio 在 top-p=0.2 时已达 80%+，跨 Llama3-8B、Qwen2.5-14B、Qwen3-14B 均稳健）。

→ 用户查询的 attention pattern 可作为 decoding 阶段 token 重要性的 **先知 (prophet)**。

### 1.3 数学推导

#### 1.3.1 Attention 输出分解

对于生成 token n > s（s 为输入长度），attention 输出可分解为:

```
AttnOut_n = Σ_{1≤t≤s} Φ_{n,t} V_t + Σ_{s<t≤n} Φ_{n,t} V_t
            ├── 输入 token 贡献 ──┘   └── 生成 token 贡献 ──┘
```

#### 1.3.2 Query Attention 作为代理

定义 **query token 对 context token t 的平均 attention**:

```
Φ̂_{Q_s,t} = (1/|Q_s|) Σ_{q∈Q_s} Φ_{q,t}
```

其中 Q_s 是用户查询 token 集合。核心近似:

```
Φ_{n,t} ≈ Φ̂_{Q_s,t}   (for n > s)
```

#### 1.3.3 Semantic Loss 定义

Precise KV cache (有 cross-attention) vs Imprecise KV cache (无 cross-attention) 的差距:

```
L_semantic = ||Σ_{1≤t≤s} Φ̂_{Q_s,t} V_t - Σ_{1≤t≤s} Φ̂'_{Q_s,t} V'_t||_2   ... (Eq. 2)
```

其中 V'_t 和 Φ̂'_{Q_s,t} 是 imprecise 版本（chunk 独立计算、无 cross-attention）。

上界（三角不等式）:

```
L_semantic ≤ L = Σ_{1≤t≤s} ||Φ̂'_{Q_s,t} V'_t - Φ̂_{Q_s,t} V_t||_2   ... (Eq. 3)
```

#### 1.3.4 Token 选择的 Value Function

给定 recomputation budget p，residual loss:

```
L_{α,p} = Σ_{t∉TOP_p(α(t))} ||Φ̂'_{Q_s,t} V'_t - Φ̂_{Q_s,t} V_t||_2   ... (Eq. 4)
```

**理想 value function**（不可直接计算）:

```
α_ideal(t) = ||Φ̂_{Q_s,t} V_t - Φ̂'_{Q_s,t} V'_t||_2   ... (Eq. 5)
```

**实际 value function**（可直接观测）:

```
α(t) = Φ̂'_{Q_s,t}   — 用户查询对 imprecise Key cache 的平均 attention
```

关键: Φ̂'_{Q_s,t} 可通过仅在 short user query 上运行 Transformer 轻量获得，无需完整 prefill。

#### 1.3.5 Layer-wise Fusion

不同层的 attention pattern 差异很大（Figure 7: 不同层的 optimal token 子集差异显著）。融合公式:

```
ᾱ(t) = (1/L) Σ_{l=1}^{L} α_l(t)   ... (Eq. 7)
```

其中 α_l(t) = Φ̂'_{Q_s,t}^{(l)} 是第 l 层的 query-to-context attention column sum。

### 1.4 双阶段流程 (Dual-Stage Pipeline)

#### Stage I: Metric Generation (轻量 pass)

```
Input:  用户查询 Q_s, 各 chunk 的预计算 KV cache {K'_chunk, V'_chunk}
For each layer l:
    1. 拼接所有 chunk 的 Key cache: K' = concat(K'_chunk1, K'_chunk2, ...)
    2. 计算 Q_s 对 K' 的 attention weights (softmax(Q_s @ K'^T / √d))
    3. Column sum → α_l(t) = Σ_{q∈Q_s} attn(q, t) / |Q_s|
Output: 每层每 token 的重要性 α_l(t)
```

**复杂度**: O(|Q_s| × s) per layer，其中 |Q_s| ≪ s（查询通常几十 token，context 几千到几万）

#### Stage II: Selective Recomputation

```
1. Fuse: ᾱ(t) = mean_l(α_l(t))
2. Select: TOP_p(ᾱ(t)) — 选 top-p 比例的 token
3. Recompute: 对选中 token 在所有层做完整 prefill（恢复 cross-attention）
4. Update: 将 recomputed KV 替换到对应位置
```

**关键**: Stage II 中 selection 对所有层是统一的（同一批 token），保证计算效率。

### 1.5 性能指标

| 配置 | RULER Avg | LongBench Avg |
|------|-----------|---------------|
| Full Recompute | 基准 | 基准 |
| Naive Reuse (0%) | -7~-44% | -10~-43% |
| CacheBlend (20%) | +39.8% vs naive | 中等 |
| ProphetKV (20%) | **96-101% of full** | **+18.6-50.9% vs SOTA** |

**效率**: 20% recomputation ratio → 5× speedup over full recompute (8K-16K context)

---

## 2. 相关方法对比

### 2.1 方法矩阵

| 方法 | Token 选择策略 | Query-Aware? | 粒度 | 适用场景 | 代码 |
|------|---------------|-------------|------|---------|------|
| **ProphetKV** | Query attention column sum, layer fusion | ✅ 全局 | per-token, global | RAG recomputation | 无 |
| **SnapKV** | Observation window attention + pooling | ⚠️ 局部 (window) | per-layer, per-head | Prefill compression | ✅ FasterDecoding/SnapKV |
| **H2O** | Accumulated attention score (Heavy Hitter) | ❌ 全局 saliency | per-layer | Decode-time eviction | ✅ HF transformers |
| **PyramidKV** | Layer-wise pyramidal budget + attention | ❌ 全局 saliency | per-layer, adaptive budget | Prefill compression | ✅ Zefan-Cai/PyramidKV |
| **Expected Attention** | Gaussian query distribution → closed-form E[attn] | ✅ 统计预测 | per-layer, per-head | Prefill compression | ✅ NVIDIA/kvpress |
| **AdaKV** | SnapKV/PyramidKV + adaptive per-head budget | ⚠️ 局部 | per-head adaptive | Prefill compression | ✅ FFY0/AdaKV |
| **CakeKV** | - | - | - | - | ✅ antgroup/cakekv |
| **KVzip** | Query-agnostic attention + context distillation | ❌ | per-token | Memory reduction | ✅ snu-mllab/KVzip |

### 2.2 SnapKV 详解

**论文**: "SnapKV: LLM Knows What You are Looking for Before Generation" (NeurIPS 2024)

**核心思路**: 用 prompt 末尾的 **observation window**（最后 ~64 token）的 attention pattern 来识别 prompt 中的关键 token。

**实现** (基于 NVIDIA/kvpress 的 SnapKVPress):

```python
class SnapKVPress(ScorerPress):
    compression_ratio: float = 0.0   # 移除的 KV 比例
    window_size: int = 64            # observation window 大小
    kernel_size: int = 5             # pooling kernel

    def score(self, module, hidden_states, keys, values, attentions, kwargs):
        # 1. 获取 observation window 的 attention weights
        #    取最后 window_size 个 query 对前面所有 key 的 attention
        attn_weights = compute_window_attention(...)  # or from `attentions`

        # 2. 聚合: 对 query 维度取均值
        scores = attn_weights.mean(dim=-2)  # [batch, heads, seq_len]

        # 3. Pooling 平滑 (avg_pool1d, kernel=5)
        scores = F.avg_pool1d(scores, kernel_size=5, padding=2, stride=1)

        # 4. 跨 KV head group 平均
        scores = scores.reshape(batch, num_kv_heads, num_groups, seq).mean(dim=2)

        # 5. 保护 observation window: 给最后 window_size 个 token 赋最大分数
        scores = F.pad(scores, (0, window_size), value=scores.max().item() + 1)

        return scores  # [batch, num_kv_heads, seq_len]
```

**与 HuggingFace 集成**: monkey-patch attention forward（SnapKV 原版）或 forward hook（kvpress 版）

### 2.3 H2O (Heavy-Hitter Oracle)

**论文**: NeurIPS 2023

**核心**: **累积 attention score** — 每个 token 在所有之前的 attention 计算中被 attend 到的总量。ProphetKV **明确反对** early-layer prediction（论文 Figure 11 展示低层关注 nearby tokens、高层关注 distant tokens，pattern 差异显著），因此跨所有层计算后融合。

```
score(t) = Σ_{n: n已生成} Σ_{h: 所有head} attn_weight(n, h, t)
```

保留策略: 保留 **recent tokens + top-K heavy hitters**。

**局限**: 在长上下文中，attention 是 power-law 分布，早期 token（attention sink）和近期 token 会主导，中间关键信息易被丢弃。

### 2.4 Expected Attention (NVIDIA kvpress)

**论文**: arXiv 2510.00636

**核心创新**: 不依赖实际 future query，而是 **统计建模 future query 的分布**:

```
假设 hidden states ~ N(μ, Σ)
→ queries ~ N(μ_q, Σ_q) (线性变换)
→ 对未来 T 个位置的 RoPE 取平均，得到 position-averaged query 分布

Expected unnormalized attention:
ẑ_i = exp(μ̄_q^T k_i / √d + k_i^T Σ̄_q k_i / (2d))

Normalized:
â_i = ẑ_i / Σ_j ẑ_j

Final score (结合 value norm):
score_i = (â_i + ε) × ||W_o v_i||
```

**实现** (kvpress ExpectedAttentionPress):

```python
def score(self, module, hidden_states, keys, values, attentions, kwargs):
    # 1. 计算 query 的均值和协方差 (排除 sink tokens)
    mean_query = queries.mean(dim=2)  # [batch, heads, dim]
    cov_query = einsum("bnsi,bnsj->bnij", centered, centered) / seq_len

    # 2. 对未来 T 个位置的 RoPE 取平均 → position-averaged rotation
    R_avg = average_rope_matrix(positions, n_future=512)
    mean_query = mean_query @ R_avg.T
    cov_query = R_avg @ cov_query @ R_avg.T

    # 3. Expected attention score (closed-form)
    scores = (mean_query @ keys.T) / sqrt(d)
    if use_covariance:
        scores += einsum("bhin,bhij,bhjn->bhn", keys, cov_query, keys) / d / 2
    scores = softmax(scores)

    # 4. 结合 value norm
    scores = (scores + epsilon) * values.norm(dim=-1)
    return scores
```

### 2.5 PyramidKV

**核心**: 不同层分配不同的 KV cache budget:
- **低层**: attention 分散 → 保留更多 token
- **高层**: attention 集中 → 保留更少 token

形成 **金字塔形** budget 分配。

---

## 3. NVIDIA kvpress 框架分析

### 3.1 架构设计

```
BasePress          — 基类, forward hook 注册机制
  └─ ScorerPress   — 基于分数的剪枝基类
       ├── SnapKVPress
       ├── ObservedAttentionPress  (H2O 变体)
       ├── ExpectedAttentionPress
       ├── PyramidKVPress
       ├── KnormPress
       ├── TOVAPress
       └── ... (20+ 实现)
```

### 3.2 核心接口

```python
# 使用方式 (context manager)
with press(model):
    outputs = model.generate(...)

# ScorerPress 子类需实现:
def score(self, module: nn.Module, hidden_states: torch.Tensor,
          keys: torch.Tensor,       # (batch, num_kv_heads, seq_len, head_dim)
          values: torch.Tensor,     # (batch, num_kv_heads, seq_len, head_dim)
          attentions: torch.Tensor, # (batch, num_heads, seq_len, seq_len)
          kwargs: dict
    ) -> torch.Tensor:              # (batch, num_kv_heads, seq_len) ← per-head 粒度
    """分数越高 = token 越重要 = 越不会被剪"""
    ...

# ScorerPress.compress() 的实际实现:
def compress(self, module, hidden_states, keys, values, attentions, kwargs):
    if self.compression_ratio == 0: return keys, values
    scores = self.score(module, hidden_states, keys, values, attentions, kwargs)
    n_kept = int(seq_len * (1 - self.compression_ratio))
    indices = scores.topk(n_kept, dim=-1).indices          # (batch, heads, n_kept)
    indices_exp = indices.unsqueeze(-1).expand(-1,-1,-1, head_dim)
    keys = keys.gather(2, indices_exp).contiguous()        # (batch, heads, n_kept, dim)
    values = values.gather(2, indices_exp).contiguous()
    return keys, values

# 关键: score 返回 per-head 粒度 → 每个 KV head 独立决定保留哪些 token
```

### 3.3 Hook 机制

```python
# BasePress 通过 context manager 注册 hook
class BasePress:
    def __call__(self, model):
        # 对每个 attention layer 注册 forward_hook
        for layer in model.model.layers:
            layer.self_attn.register_forward_hook(self.forward_hook)

    def forward_hook(self, module, input, output):
        # 在 attention forward 之后执行
        # 获取 keys, values, attentions
        # 调用 compress() → score() → topk → prune
        ...
```

---

## 4. CompressLink Query Relevance Probe 实现方案

### 4.1 需求分析

CompressLink 需要 **p_r(t)** — 每个 token 被 restoration 的概率，用于:
1. **RABA**: p_r 高 → 分配更少 compression bits（因为会被 restore）
2. **CEGR**: 结合 compression error ε(t) 和 p_r(t) 选择要 restore 的 token

**关键区别**（CompressLink vs ProphetKV）:
- ProphetKV: 场景是 **position-independent KV reuse**，关注 cross-attention 恢复
- CompressLink: 场景是 **compression + selective restoration**，关注哪些 token 值得高精度保留

但 **底层信号完全一致**: 都是用 query attention 预测 token 重要性。

### 4.2 推荐实现方案

#### 方案 A: ProphetKV 式 — Query Attention Column Sum (推荐)

```python
class QueryRelevanceProbe:
    """
    计算 p_r(t): 每个 context token 被 future query attend 到的概率。
    基于 ProphetKV 的 "user query as prophet" 假设。
    """

    def __init__(self, model, probe_layers=None, aggregation='mean'):
        self.model = model
        # 可选: 只用部分层 (e.g., 后半部分层更 semantic)
        self.probe_layers = probe_layers  # None = 全部层
        self.aggregation = aggregation    # 'mean' or 'max'
        self._hooks = []
        self._attention_scores = {}

    def _register_hooks(self):
        """在每个 attention layer 注册 hook 收集 attention weights"""
        for idx, layer in enumerate(self.model.model.layers):
            if self.probe_layers and idx not in self.probe_layers:
                continue

            def hook_fn(module, input, output, layer_idx=idx):
                # 获取 attention weights: [batch, heads, q_len, kv_len]
                # 需要 output_attentions=True 或手动计算
                attn_weights = output[1]  # depends on model
                # Column sum (对 query 维度求和) → per-token importance
                # [batch, heads, kv_len]
                col_sum = attn_weights.sum(dim=-2)
                # 归一化: 除以 query 数量
                col_sum = col_sum / attn_weights.shape[-2]
                # 跨 head 平均
                col_sum = col_sum.mean(dim=1)  # [batch, kv_len]
                self._attention_scores[layer_idx] = col_sum

            self._hooks.append(
                layer.self_attn.register_forward_hook(hook_fn)
            )

    def compute_relevance(self, query_input_ids, kv_cache):
        """
        Stage I: 轻量 pass，只让 query tokens attend to cached keys

        Args:
            query_input_ids: 用户查询的 token ids
            kv_cache: 已压缩/预计算的 KV cache

        Returns:
            p_r: [seq_len] tensor, 每个 context token 的 relevance probability
        """
        self._attention_scores = {}
        self._register_hooks()

        try:
            # 只对 query tokens 做 forward, 使用已有 KV cache
            with torch.no_grad():
                self.model(
                    query_input_ids,
                    past_key_values=kv_cache,
                    output_attentions=True,
                    use_cache=True,
                )
        finally:
            for h in self._hooks:
                h.remove()
            self._hooks = []

        # Layer fusion: ᾱ(t) = mean_l(α_l(t))
        all_scores = torch.stack(list(self._attention_scores.values()))
        if self.aggregation == 'mean':
            fused = all_scores.mean(dim=0)  # [batch, kv_len]
        else:
            fused = all_scores.max(dim=0).values

        # Score → Probability: softmax or min-max normalization
        p_r = self._score_to_probability(fused)
        return p_r

    def _score_to_probability(self, scores):
        """将 raw attention score 转换为 [0, 1] 概率"""
        # 方法 1: Min-max normalization
        s_min, s_max = scores.min(dim=-1, keepdim=True).values, \
                       scores.max(dim=-1, keepdim=True).values
        p_r = (scores - s_min) / (s_max - s_min + 1e-8)

        # 方法 2 (替代): Temperature-scaled softmax
        # p_r = F.softmax(scores / temperature, dim=-1)

        return p_r
```

#### 方案 B: Expected Attention 式 — 无需 Query (备选)

适用于 **query 不可用** 的场景（如 prefill 阶段 compression，此时 user query 还没到）:

```python
class ExpectedRelevanceProbe:
    """
    基于 Expected Attention 方法，统计估算 future query 的 attention。
    不需要实际 query，但精度略低于方案 A。
    """

    def compute_relevance(self, keys, queries_so_far, values):
        """
        从已有 query 的统计特征预测 future attention

        keys: [batch, heads, seq, dim]
        queries_so_far: [batch, heads, seq, dim] — prefill 阶段的 query
        values: [batch, heads, seq, dim]
        """
        d = keys.shape[-1]

        # 1. Query distribution: mean + covariance
        mu_q = queries_so_far.mean(dim=2)     # [batch, heads, dim]
        centered = queries_so_far - mu_q.unsqueeze(2)
        cov_q = torch.einsum("bhsi,bhsj->bhij", centered, centered) / queries_so_far.shape[2]

        # 2. Expected attention (Gaussian closed-form)
        # E[exp(q^T k / √d)] = exp(μ^T k/√d + k^T Σ k/(2d))
        mean_scores = torch.matmul(mu_q.unsqueeze(2), keys.transpose(-1, -2)).squeeze(2) / math.sqrt(d)
        cov_scores = torch.einsum("bhin,bhij,bhjn->bhn", keys, cov_q, keys) / d / 2
        scores = F.softmax(mean_scores + cov_scores, dim=-1)

        # 3. 结合 value norm
        v_norm = values.norm(dim=-1)
        scores = (scores + 0.02) * v_norm

        # 4. Layer aggregation + normalization → p_r
        p_r = self._normalize(scores.mean(dim=1))  # average across heads
        return p_r
```

#### 方案 C: SnapKV 式 — Observation Window (轻量备选)

适用于 **在线 streaming** 场景:

```python
class ObservationWindowProbe:
    """
    用最后 window_size 个 token 的 attention pattern 估计 token 重要性。
    不需要独立的 query forward pass。
    """

    def __init__(self, window_size=64, kernel_size=5):
        self.window_size = window_size
        self.kernel_size = kernel_size

    def compute_relevance(self, attn_weights):
        """
        attn_weights: [batch, heads, seq, seq] — 最后一个 attention layer 的输出

        Returns: p_r [batch, seq]
        """
        # 取最后 window_size 个 query 对前面 token 的 attention
        window_attn = attn_weights[:, :, -self.window_size:, :-self.window_size]

        # 对 query 维度求和
        scores = window_attn.sum(dim=-2)  # [batch, heads, prefix_len]

        # Avg pooling 平滑
        scores = F.avg_pool1d(scores, kernel_size=self.kernel_size,
                              padding=self.kernel_size // 2, stride=1)

        # 跨 head 平均
        scores = scores.mean(dim=1)  # [batch, prefix_len]

        # 补齐 window tokens (它们的 p_r 应为 1.0, 因为是最近的)
        window_scores = torch.ones(scores.shape[0], self.window_size, device=scores.device)
        scores = torch.cat([scores, window_scores], dim=-1)

        # Normalize to [0, 1]
        p_r = (scores - scores.min()) / (scores.max() - scores.min() + 1e-8)
        return p_r
```

### 4.3 方案选择建议

| 维度 | 方案 A (ProphetKV式) | 方案 B (Expected Attn式) | 方案 C (SnapKV式) |
|------|---------------------|------------------------|--------------------|
| 精度 | ★★★★★ | ★★★★ | ★★★ |
| 需要 query? | 是 | 否 | 否 (用 window) |
| 额外开销 | 轻量 forward (O(|Q|×s)) | 统计计算 (O(s×d²)) | 无额外 pass |
| 适用时机 | Decode 前/Compression 后 | Prefill 时 | Prefill 时 |
| **推荐用于** | **CEGR** (有 query 时) | RABA (prefill 时预估) | 快速 fallback |

**CompressLink 推荐**: **两阶段策略**
1. **Prefill/Compression 阶段**: 用 方案 B 或 C 计算 **初始 p_r_est**，用于 RABA bit allocation
2. **Decode/Restoration 阶段**: 用 方案 A 计算 **精确 p_r**，用于 CEGR restoration selection

### 4.4 p_r(t) 的关键设计决策

#### 4.4.1 获取时机

```
Timeline:
  Prefill ──→ Compression ──→ User Query arrives ──→ Decode
                                      ↑
                              ProphetKV Stage I 在这里计算 p_r
```

- **RABA 需求**: compression 时就需要 p_r → 此时 query 未到 → 需要 **预估** (方案 B/C)
- **CEGR 需求**: decode 前选择 restore 哪些 token → query 已到 → 可以用 **精确** p_r (方案 A)

**解决方案**: RABA 的 p_r 可以用 Expected Attention 预估，或者采用 **在线更新**:
1. Prefill 时用 uniform p_r 做初始 bit allocation
2. Query 到达后用方案 A 计算精确 p_r
3. 对 p_r 高但 compression error 大的 token 做 restoration

#### 4.4.2 粒度

ProphetKV 使用 **per-token, global (all layers)** 的粒度:

```
α_l(t) = per-layer per-token
ᾱ(t) = per-token (fused across layers) → 用于 token selection
```

对 CompressLink:
- **RABA**: 需要 per-layer per-token 的 p_r（因为 KVTC 是 per-layer 做 bit allocation）
- **CEGR**: 需要 per-token global 的 p_r（因为 restoration 是 per-token 的）

→ **同时保留 per-layer 和 fused 两个粒度**

#### 4.4.3 Score → Probability 转换

ProphetKV 直接用 raw attention score (Φ̂'_{Q_s,t}) 做 TOP_p 选择，没有显式转为概率。

CompressLink 需要 [0,1] 概率，建议:

```python
# 方法 1: 基于排序的分位数映射 (推荐)
ranks = scores.argsort(descending=True).argsort()  # rank of each token
p_r = 1.0 - ranks.float() / len(scores)  # top token → p_r ≈ 1.0

# 方法 2: Temperature softmax
p_r = F.softmax(scores / tau, dim=-1) * len(scores)  # scale to ~[0, num_tokens]
p_r = p_r.clamp(0, 1)

# 方法 3: Sigmoid with learned threshold
p_r = torch.sigmoid((scores - scores.median()) / tau)
```

### 4.5 与 KVTC Compression Pipeline 的接口

```python
# 在 KVTC 的 pipeline_fast.py 中集成

class CompressLinkPipeline:
    def __init__(self, model, kvtc_pipeline, relevance_probe):
        self.model = model
        self.kvtc = kvtc_pipeline
        self.probe = relevance_probe  # QueryRelevanceProbe

    def compress_with_raba(self, kv_cache, p_r_est=None):
        """
        RABA: Restoration-Aware Bit Allocation
        p_r 高的 token → 更少 bits (会被 restore)
        p_r 低的 token → 更多 bits (不会被 restore, 需要高保真)
        """
        for layer_idx in range(self.model.config.num_hidden_layers):
            keys = kv_cache[layer_idx][0]
            values = kv_cache[layer_idx][1]

            if p_r_est is not None:
                # 调整 KVTC 的 per-token bit budget
                # base_bits: KVTC 的默认 bit allocation (e.g., from eigenvalue entropy)
                base_bits = self.kvtc.compute_bit_budget(keys, layer_idx)
                # RABA 调整: p_r 高 → 减少 bits
                adjusted_bits = base_bits * (1 - beta * p_r_est[layer_idx])
                adjusted_bits = adjusted_bits.clamp(min=min_bits)
            else:
                adjusted_bits = self.kvtc.compute_bit_budget(keys, layer_idx)

            compressed = self.kvtc.compress(keys, values, bits=adjusted_bits)
            ...

    def restore_with_cegr(self, compressed_cache, query_ids, budget_ratio=0.2):
        """
        CEGR: Compression-Error-Guided Restoration
        选择 restore 哪些 token, 基于:
        - p_r(t): query relevance (高 → 更值得 restore)
        - ε(t): compression error (高 → restore 收益大)
        """
        # 1. 计算精确 p_r (方案 A)
        p_r = self.probe.compute_relevance(query_ids, compressed_cache)

        # 2. 计算 compression error
        epsilon = self.kvtc.estimate_error(compressed_cache)

        # 3. 综合分数: 同时考虑 relevance 和 error
        # score = p_r * ε  (relevance × error magnitude)
        restore_score = p_r * epsilon

        # 4. 选 top-budget_ratio 的 token restore
        n_restore = int(len(restore_score) * budget_ratio)
        restore_indices = restore_score.topk(n_restore).indices

        # 5. Recompute selected tokens
        restored_cache = self.recompute(compressed_cache, restore_indices)
        return restored_cache
```

### 4.6 与 MEPIC Boundary Recomputation 的关系

ProphetKV 的 overlap 分析（Figure 4）显示 query-attended tokens 与 decoding-attended tokens 高度重叠。

**推测**: MEPIC 的 chunk boundary tokens（chunk 首尾几个 token）:
- 如果它们是 cross-chunk attention 的关键节点 → p_r 应该自然偏高
- 但 ProphetKV 的分析表明，重要 token 不一定在 boundary 位置 → **p_r 比固定 boundary 更灵活**

→ CompressLink 中，MEPIC boundary recomputation 可以被 CEGR **替代或增强**:
- CEGR 用 p_r + ε 自动选择需要 restore 的 token（包含但不限于 boundary）
- 如果 boundary token 确实重要，它们的 p_r 和 ε 自然会高，会被 CEGR 选中

---

## 5. 可复用代码资源

### 5.1 NVIDIA kvpress (推荐参考)

- **仓库**: https://github.com/NVIDIA/kvpress
- **许可**: MIT (推测, 需确认)
- **价值**: 完整的 hook-based KV cache compression 框架，支持 20+ 方法
- **关键文件**:
  - `kvpress/presses/scorer_press.py` — ScorerPress 基类，forward hook + topk 剪枝
  - `kvpress/presses/snapkv_press.py` — SnapKV 实现，observation window + pooling
  - `kvpress/presses/expected_attention_press.py` — Expected Attention，Gaussian closed-form
  - `kvpress/presses/observed_attention_press.py` — H2O 式累积 attention

### 5.2 SnapKV 原版

- **仓库**: https://github.com/FasterDecoding/SnapKV
- **关键文件**:
  - `snapkv/monkeypatch/snapkv_utils.py` — 核心 attention score 计算
  - `snapkv/monkeypatch/llama_hijack_4_37.py` — Llama monkey-patch 示例
- **集成方式**: monkey-patch attention forward（较 invasive，不如 kvpress 的 hook 方式优雅）

### 5.3 HuggingFace Transformers 原生支持

- **Issue #30758**: H2O-style KV cache sparsity 已作为 feature request
- 部分 cache 管理功能已内置于 `transformers.QuantizedCache`

---

## 6. 总结与建议

### 6.1 关键发现

1. **ProphetKV 无公开代码**，但方法足够清晰可以从论文复现
2. **核心公式极其简单**: p_r(t) = mean_l(column_sum(softmax(Q_s @ K_l^T / √d)))
3. **NVIDIA kvpress 是最佳参考框架**: hook-based 设计可直接复用
4. **Expected Attention 是 query 不可用时的最佳替代**
5. **SnapKV 的 observation window 是最轻量的方案** 但精度有限

### 6.2 CompressLink 实施路线

```
Phase 1: 实现 QueryRelevanceProbe (方案 A)
  - 基于 kvpress ScorerPress 的 hook 机制
  - Column sum + layer fusion
  - Score → probability 转换

Phase 2: 集成到 RABA
  - Prefill 阶段用 Expected Attention (方案 B) 预估 p_r
  - 调整 KVTC per-token bit budget

Phase 3: 集成到 CEGR
  - Query 到达后计算精确 p_r (方案 A)
  - 结合 compression error 选择 restore token
  - 替代/增强 MEPIC boundary recomputation

Phase 4: 端到端优化
  - p_r 计算与 KV cache decode 的 overlap
  - 选择性 layer probe (只用后半部分层?)
  - Adaptive temperature for score → probability
```

### 6.3 风险与未知

1. **ProphetKV 假设 RAG 场景** — CompressLink 的 general compression 场景中 query 的预测力是否同样强需要验证
2. **Expected Attention 的 Gaussian 假设** — 实际 hidden states 未必 Gaussian，需要验证误差
3. **p_r 在 RABA 中的反向使用** — ProphetKV 用 p_r 选 token 做 recompute，RABA 用 p_r 决定 bit allocation，逻辑一致性需要理论分析
4. **Per-layer vs Global p_r** — KVTC 是 per-layer 操作，但 ProphetKV 建议 fusion 效果更好，需要实验对比
5. **NoPE 兼容性** — ProphetKV 和 kvpress 都假设标准 RoPE attention。MEPIC 存储 NoPE KV cache (不含位置编码)，query 侧加 RoPE。计算 p_r 时需手动做 RoPE-query × NoPE-key attention，不能直接用 HF 的 output_attentions=True
6. **Boundary tokens 硬约束** — MEPIC chunk 边界 token 的 p_r 必须 = 1.0（RABA 给 0 bits，反正要 recompute）。CEGR budget 应排除 boundary tokens（mandatory ~5-10%），discretionary budget 仅 ~10-15%

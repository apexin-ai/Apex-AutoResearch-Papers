# Code Survey: Token Filtering & TEAL

## 1. 代码库信息

| 方法 | 论文 | GitHub |
|------|------|--------|
| Token Filtering | [arXiv:2512.07090](https://arxiv.org/abs/2512.07090) "Leveraging KV Similarity for Online Structured Pruning in LLMs" | **无公开代码库**（截至2026-05-12，作者 Jungmin Lee / Yulhwa Kim / Seokin Hong，Sungkyunkwan University，未发布代码） |
| TEAL | [arXiv:2408.14690](https://arxiv.org/abs/2408.14690) "Training-Free Activation Sparsity in Large Language Models" (ICLR 2025) | [FasterDecoding/TEAL](https://github.com/FasterDecoding/TEAL)（MIT/Together AI） |

---

## 2. Token Filtering — EMA Similarity 核心算法

> 来源：论文 HTML 版本，无可运行代码。以下为从论文提取的伪代码。

### 2.1 EMA Centroid 更新

```python
# 对每个 attention head h, 每层 l:
Anchor_k[l,h] = gamma * Anchor_k[l,h] + (1 - gamma) * k_new[l,h]
Anchor_v[l,h] = gamma * Anchor_v[l,h] + (1 - gamma) * v_new[l,h]
```

**默认超参数：γ (gamma) = 0.9**（论文称"close to one"，强调近期 token 的影响）

### 2.2 Variance-Aware Similarity Fusion

```python
# 逐 head 计算 cosine similarity
s_k = cos_sim(k_new, Anchor_k)  # per head
s_v = cos_sim(v_new, Anchor_v)  # per head

# 跨 head 计算 running variance
sigma_k_sq = running_var(s_k, across_heads)
sigma_v_sq = running_var(s_v, across_heads)

# Variance-aware 权重（低方差侧权重更大）
alpha = (1/sigma_v_sq) / (1/sigma_k_sq + 1/sigma_v_sq)

# Joint similarity score
S_KV = alpha * s_k + (1 - alpha) * s_v
```

**注意：α 不是固定值，而是根据 key/value 方差动态计算的。** 低方差信号更可靠，分配更高权重。

### 2.3 Adaptive Threshold

```python
# 每层独立的阈值，通过比例反馈动态调整
T_l = T_l + eta * (P_current - P_tail)

# 其中：
# P_tail = P_global / Y   (Y=0.5, 即 tail-focused，仅后 50% 的层参与 pruning)
# eta = small learning rate (论文未给出具体值)
# P_global = 目标全局 pruning rate
```

### 2.4 Token Filtering Decision

```python
if S_KV[token] > T_l:
    # token 冗余，跳过 attention 计算
    attention_output[token] = 0  # 直接置零
    # LayerNorm 仍然执行（residual path 保留）
else:
    # 正常走 attention
    attention_output[token] = attention(q, k, v)[token]
```

### 2.5 默认超参数汇总

| 参数 | 值 | 说明 |
|------|-----|------|
| γ (EMA decay) | 0.9 | 越接近1越强调历史 |
| α (key/value权重) | 动态计算 | variance-aware，非固定 |
| Y (tail ratio) | 0.5 | 仅后半层参与 pruning |
| η (threshold lr) | 未公开 | 小学习率 |
| τ (初始阈值) | 未公开 | 逐层自适应 |
| 支持模型 | LLaMA-2 7B/13B, LLaMA-3 8B, Mistral 7B | 论文实验模型 |

### 2.6 Hook 挂载位置

Token Filtering 层**插入在每个 Transformer block 的 attention 之前**。判断 token 是否冗余后：
- 冗余 token → 跳过 attention，输出置零，走 skip path
- 非冗余 token → 正常执行 attention

---

## 3. TEAL — Magnitude-Based Activation Pruning 核心代码

### 3.1 核心 Sparsify 逻辑

```python
# utils/utils.py — SparsifyFn.apply()
def apply(self, x):
    return x.abs().gt(self.threshold) * x
    # 绝对值低于 threshold 的激活直接置零
    # 高于 threshold 的保留原值
```

### 3.2 Threshold 计算（从 Distribution）

```python
# threshold 通过 activation histogram 的 inverse CDF 计算
threshold = distribution.icdf(0.5 + sparsity / 2)

# 例如 sparsity=0.5 → icdf(0.75)
# 即找到 75th percentile 的绝对值作为阈值
# 对称性：正负激活两侧各裁剪 25%
```

### 3.3 被 Prune 的层和组件

```python
# self_attn.py — Attention 层
sparse_fns = {
    'q': SparsifyFn(distrs['h1']),   # Query input
    'k': SparsifyFn(distrs['h1']),   # Key input
    'v': SparsifyFn(distrs['h1']),   # Value input
    'o': SparsifyFn(distrs['h2'])    # Output projection input
}

# 应用时机：在 projection 之前
x_q = sparse_fns['q'](hidden_states)  # 先 sparsify
query_states = q_proj(x_q)             # 再 project

# mlp.py — MLP 层
sparse_fns = {
    'gate': SparsifyFn(distrs['h1']),  # Gate projection input
    'up':   SparsifyFn(distrs['h1']),  # Up projection input
    'down': SparsifyFn(...)            # Down projection input (intermediate)
}
```

**关键点：TEAL 在 linear projection 之前 sparsify 输入激活，利用输入稀疏性加速矩阵乘。**

### 3.4 Greedy 逐层优化

```python
# greedyopt.py — 贪心分配 per-component sparsity
for layer in model.layers:
    while effective_sparsity < target:
        best_proj, best_error = None, float('inf')
        for proj in ['q','k','v','o','gate','up','down']:
            # 尝试增加该 component 的 sparsity
            error = L2_norm(original_output - sparsified_output)
            if error < best_error:
                best_proj, best_error = proj, error
        sparsities[best_proj] += step_size

# 优化目标：最小化 layer output 的 L2 error
# 仅计算序列后 25% 的 token (与预测最相关)
```

### 3.5 默认超参数汇总

| 参数 | 值 | 说明 |
|------|-----|------|
| 默认 sparsity | 0.4-0.5 (40-50%) | 模型级全局 sparsity |
| Calibration 数据 | Alpaca, 300 samples, seq_len=2048 | 用于构建 histogram |
| Greedy target | 0.9 per-layer effective | 贪心停止条件 |
| Prefill 策略 | 仅 sparsify 后半段 context tokens | 避免影响 prompt 编码 |
| 支持模型 | Llama-2 7B/13B/70B, Llama-3 8B/70B, Mistral-7B | 已有预校准 thresholds |

### 3.6 Speedup 结果

| Sparsity | Wall-clock Speedup |
|----------|-------------------|
| 40% | 1.53× |
| 50% | 1.80× |

---

## 4. HuggingFace Transformers 集成方式的关键差异

| 维度 | Token Filtering | TEAL |
|------|----------------|------|
| **集成方式** | 在 attention 前插入额外的 filtering 层 | Monkeypatch 替换 forward 方法 |
| **修改粒度** | Token 级：整个 token 被跳过或保留 | Element 级：单个激活值被置零 |
| **是否需要校准** | 否（online，推理时自适应） | 是（需要 300 样本 Alpaca 预校准 histogram） |
| **需要自定义 kernel** | 否（仅跳过计算） | 是（需要 sparse matrix 乘法 kernel 获得 speedup） |
| **影响的计算** | 仅 attention（MLP 不受影响） | Attention + MLP 的所有 7 个 projection |
| **阈值来源** | 在线自适应（EMA + variance-aware feedback） | 离线预校准（activation histogram → CDF threshold） |
| **模型架构改动** | 需要插入新层（Token Filtering layer） | 仅替换 forward 函数，无新层 |
| **与 quantization 兼容** | 论文未讨论 | 明确兼容（weight quantization） |

---

## 5. Cross-Axis 验证脚本的实现建议

### 5.1 总体架构

两个方法作用在不同轴上：
- **Token Filtering**：token 轴（哪些 token 参与 attention）
- **TEAL**：activation element 轴（哪些激活值非零）

组合策略：先做 Token Filtering 减少 token 数，再对剩余 token 的激活做 TEAL magnitude pruning。

### 5.2 实现路径

```python
# 方案：两阶段 pipeline
class CrossAxisPruner:
    def __init__(self, gamma=0.9, teal_sparsity=0.5, tail_ratio=0.5):
        self.token_filter = TokenFilter(gamma, tail_ratio)
        self.teal = TEALSparsifier(teal_sparsity)

    def forward(self, hidden_states, layer_idx, num_layers):
        # Stage 1: Token Filtering (仅后半层)
        if layer_idx >= num_layers * (1 - self.token_filter.tail_ratio):
            mask = self.token_filter.compute_mask(hidden_states)
            # mask: [batch, seq_len] bool
        else:
            mask = torch.ones(batch, seq_len, dtype=torch.bool)

        # Stage 2: TEAL element-wise sparsify (所有层)
        sparse_hidden = self.teal.apply(hidden_states)
        # sparse_hidden: same shape, small values zeroed

        # Stage 3: Combine
        # 被 Token Filter 过滤的 token 不参与 attention
        # 保留的 token 使用 sparsified activations
        return sparse_hidden, mask
```

### 5.3 关键实现注意事项

1. **Token Filtering 需要从零实现**（无公开代码）：
   - EMA anchor 的初始化：用第一个 token 的 K/V 作为初始 anchor
   - Running variance 需要 Welford's online algorithm
   - Threshold 的 η 需要调参（建议从 0.01 开始）

2. **TEAL 可直接复用**：
   - `pip install` TEAL repo 或 copy `utils/utils.py` 的 `SparsifyFn`
   - 需要先在目标模型上 run `grab_acts.py` 生成 histogram
   - 或使用 `models/` 下已有的 Llama/Mistral 预校准 thresholds

3. **验证指标**：
   - Perplexity（WikiText-2, C4）— 基础质量检查
   - Commonsense reasoning（ARC, HellaSwag, MMLU）— 功能完整性
   - Wall-clock latency — 实际 speedup
   - 分别测 Token Filtering only / TEAL only / Combined，三组对比

4. **风险点**：
   - Token Filtering 和 TEAL 的 sparsity 可能**不正交**——被 filter 的 token 本身可能也是 TEAL 会 prune 掉的低 magnitude 激活
   - 需要监控 combined pruning rate 是否超过有效阈值
   - Prefill 阶段两者行为不同（Token Filtering 不适用 prefill，TEAL 对 prefill 后半段生效）

# TEAL 校准流程技术笔记

基于 https://github.com/FasterDecoding/TEAL (ICLR 2025 Spotlight) 代码分析。

---

## 1. grab_acts.py — Activation Histogram 收集

### 调用命令

```bash
CUDA_VISIBLE_DEVICES=0 python teal/grab_acts.py \
  --model_name meta-llama/Llama-2-7b-hf \
  --output_path $OUTPUT_PATH
```

### 流程

1. 加载模型（`get_sparse_model`），设置 `grab_acts=True` 进入 grabbing mode
2. 加载 **tatsu-lab/alpaca** 数据集的前 **300 条** train split，拼成一段长文本
3. Tokenize 成 `[bsz=10, seq_len=2048]` 的 input_ids
4. 手动逐层前向（不是 `model.forward`）：
   - 先 `embed_tokens` + `rotary_emb` 得到初始 hidden_states 和 position_embeddings
   - 逐层：保存 `hidden_states` → `act_{i}.pt`（给 greedyopt 用），然后过这一层
5. 每层前向过程中，monkeypatched 的 forward 在关键位置调用 `activation_module.grab_activations(x, key)` 收集激活值

### 收集的激活点位

**Self-Attention 模块**（`self_attn.py:_FA2_forward`）：
- `h1`: attention 输入 `hidden_states`（即 q/k/v_proj 的输入）
- `h2`: attention 输出 `attn_output`（即 o_proj 的输入）

**MLP 模块**（`mlp.py:_mlp_forward`）：
- `h1`: MLP 输入 `x`（即 gate_proj 和 up_proj 的输入）
- `h2`: 中间激活 `act_fn(gate_proj(x)) * up_proj(x)`（即 down_proj 的输入）

### Histogram 计算（`ActivationModule.find_histogram`）

```python
def find_histogram(self, num_bins=10000, outlier_threshold=0.01):
```

- 将所有 batch 的激活值 flatten、排序
- 去掉上下各 1% 的 outlier 确定 `[lower_bound, upper_bound]`
- 在此范围内生成 9999 个等距 bin，加上两端的极值 bin → 共 **10000 个 bins**
- 调用 `torch.histogram` 得到 counts
- 计算 bin_centers = (bins[:-1] + bins[1:]) / 2

### 输出文件结构

```
$OUTPUT_PATH/
├── histograms/
│   └── layer-{i}/
│       ├── mlp/
│       │   └── histograms.pt      # dict: {h1, h1_centers, h2, h2_centers}
│       └── self_attn/
│           └── histograms.pt      # dict: {h1, h1_centers, h2, h2_centers}
└── activations/
    ├── act_0.pt                   # shape: [bsz=10, seq_len=2048, hidden_dim]
    ├── act_1.pt
    └── ...act_{N-1}.pt
```

每个 `histograms.pt` 包含 4 个 tensor：

| Key | Shape | 含义 |
|-----|-------|------|
| `h1` | `[9999]` | hidden_type=h1 的 bin counts (float32) |
| `h1_centers` | `[9999]` | 对应 bin 中心值 (float32) |
| `h2` | `[9999]` | hidden_type=h2 的 bin counts (float32) |
| `h2_centers` | `[9999]` | 对应 bin 中心值 (float32) |

### 关键细节

- histogram 是关于激活值绝对大小的分布，近似零均值单峰分布
- `Distribution.icdf(q)` 通过 CDF 反函数直接从 histogram 计算 threshold
- `SparsifyFn.set_threshold(sparsity)` 调用 `distr.icdf(0.5 + sparsity/2)` — 因为分布关于零对称，sparsity=0.5 意味着去掉中间 50% 的小值
- 实际稀疏化：`x.abs().gt(threshold) * x`（magnitude pruning）

---

## 2. greedyopt.py — Block-wise Greedy Threshold 优化

### 调用命令

```bash
CUDA_VISIBLE_DEVICES=0 python teal/greedyopt.py \
  --model_name meta-llama/Llama-2-7b-hf \
  --model_type Llama-2-7B \
  --teal_path $OUTPUT_PATH \
  --target_sparsity 0.9 \
  --base_step_size 0.025 \
  --last_fraction 0.25
```

### 核心算法

对每一层独立进行 greedy 搜索，为 7 个 projection（q, k, v, o, gate, up, down）分配不同的 sparsity level：

1. 加载该层的 `act_{i}.pt` 作为输入，用 dense forward 计算 `target_acts`
2. 初始化所有 projection 的 sparsity = 0
3. 循环直到 effective sparsity 达到 target：
   - 对每个 projection 尝试增加 `step_size`
   - 选择导致 activation error 最小的那个 projection
   - 更新该 projection 的 sparsity
4. Error 计算：只用序列后 25%（`last_fraction=0.25`）的 token 位置的 L2 norm

### Weight Dict（加权 effective sparsity 计算）

不同 projection 对总计算量的贡献权重不同：

```python
# Llama-2-7B 为例
'q': 1, 'k': 1/8, 'v': 1/8, 'o': 1,
'gate': 2.6875, 'up': 2.6875, 'down': 2.6875
```

- k/v 权重小：因为 GQA/MQA 下 k/v head 数少
- gate/up/down 权重大：intermediate_size 大于 hidden_size（Llama-2-7B: 11008 vs 4096 ≈ 2.6875x）
- effective_sparsity = Σ(sparsity_i × weight_i) / Σ(weight_i)

### step_size 调整

```python
step_sizes[proj] = base_step_size * (1 / weights[proj])
```

权重大的 projection，step_size 更小（搜索更精细）。

### 输出格式

```
$OUTPUT_PATH/lookup/layer-{i}/results.csv
```

CSV 格式：
```
Effective Sparsity, Activation Error, Baseline Error, q, k, v, o, gate, up, down
0.004145, 0.000380, 0.000671, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0186
0.008290, 0.000443, 0.000832, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0372
...
```

使用时通过 `get_layer_greedy_sparsities(layer_sparsities, results_dir)` 查表：给定 target effective sparsity，找到最近的行，读出各 projection 的 sparsity。

---

## 3. Threshold 计算的两条路径

### 路径 A: Uniform（直接 CDF）

```python
model.set_uniform_sparsity(0.5)
# → 对所有层所有 projection 调用：
# SparsifyFn.set_threshold(0.5) → distr.icdf(0.5 + 0.5/2) = distr.icdf(0.75)
```

- 不需要 greedyopt，只需要 histograms
- 每个 projection 查自己的 histogram CDF 反函数
- 所有 projection 使用相同的 sparsity level

### 路径 B: Block-wise Greedy

```python
model.load_greedy_sparsities(greedy_path, 0.5)
```

- 需要先运行 greedyopt 生成 lookup 表
- 每个 projection 的 sparsity 不同（由 greedy 搜索决定）
- 但最终 threshold 仍然是通过 `distr.icdf(0.5 + sparsity/2)` 从 histogram 算出
- 优势：同样的 effective sparsity 下 error 更小

### 可以跳过 greedy 吗？

**可以。** Uniform 模式完全绕过 greedyopt，只需 histograms。论文显示 uniform 模式在 40-50% sparsity 下已有不错效果，greedy 在高 sparsity（>50%）下收益更大。

---

## 4. DeepSeek-R1-Distill-Qwen-14B 适配分析

### 架构对比

| 特性 | Llama-2/3 | Qwen2 (DeepSeek-R1-Distill-Qwen-14B) |
|------|-----------|---------------------------------------|
| Config 类 | `LlamaConfig` | `Qwen2Config` |
| Decoder Layer | `LlamaDecoderLayer` | `Qwen2DecoderLayer` |
| Attention | `LlamaFlashAttention2` | `Qwen2FlashAttention2` |
| MLP | `LlamaMLP` | `Qwen2MLP` |
| Attention proj | q_proj, k_proj, v_proj, o_proj | q_proj, k_proj, v_proj, o_proj |
| MLP proj | gate_proj, up_proj, down_proj | gate_proj, up_proj, down_proj |
| RoPE | 标准 RoPE | 标准 RoPE |
| Norm | RMSNorm | RMSNorm |
| GQA heads (14B) | - | num_heads=40, num_kv_heads=8 |
| hidden_size (14B) | - | 5120 |
| intermediate_size (14B) | - | 13824 |
| num_layers (14B) | - | 48 |
| bias | 无 | attention 有 bias (`attention_bias=True`) |

### 关键差异和修改点

#### 4.1 模型类注册

TEAL 目前硬编码 `LlamaSparseForCausalLM` 和 `MistralSparseForCausalLM`。需要新增 `Qwen2SparseForCausalLM`：

```python
from transformers.models.qwen2.modeling_qwen2 import Qwen2ForCausalLM, Qwen2DecoderLayer
from transformers.models.qwen2.configuration_qwen2 import Qwen2Config

class Qwen2SparseConfig(Qwen2Config):
    model_type = "qwen2_sparse"

class Qwen2SparseForCausalLM(SparseModelMixin, Qwen2ForCausalLM):
    config_class = Qwen2SparseConfig
    _no_split_modules = ["Qwen2DecoderLayer"]
```

#### 4.2 get_sparse_model 适配

`utils/utils.py:get_sparse_model` 需要扩展 class_name 白名单：

```python
assert class_name in [..., "Qwen2ForCausalLM", "Qwen2SparseForCausalLM"]
```

`get_model_class_name` 返回 `"Qwen2ForCausalLM"`，需要添加对应的分支选择 `Qwen2SparseForCausalLM`。

#### 4.3 build_sparse_layers 适配

`model.py:build_sparse_layers` 中 isinstance 检查需要加入 `Qwen2DecoderLayer`：

```python
if isinstance(layer, (LlamaDecoderLayer, MistralDecoderLayer, Qwen2DecoderLayer)):
```

#### 4.4 self_attn.py 适配

`_FA2_forward` 中的 attention 实现需要匹配 Qwen2 的 forward 签名。Qwen2 attention 的 forward 参数与 Llama 略有不同，但核心的 q/k/v/o_proj 命名一致。关键差异：
- Qwen2 attention 有 `bias`（q_proj.bias 等）
- Qwen2 的 `rotary_emb` 可能传入 `position_ids` 而非 `value_states`（需检查 transformers 版本）

但由于 TEAL 的 monkeypatch 方式是替换整个 forward，只要替换后的 forward 正确处理了这些差异即可。projection 层名称完全一致（q_proj/k_proj/v_proj/o_proj/gate_proj/up_proj/down_proj）。

#### 4.5 TEAL 组件名映射

| TEAL 内部名 | 实际 projection | Qwen2 匹配 |
|------------|----------------|------------|
| h1 (attn) | attn 输入 → q/k/v_proj 输入 | 一致 |
| h2 (attn) | attn 输出 → o_proj 输入 | 一致 |
| h1 (mlp) | mlp 输入 → gate/up_proj 输入 | 一致 |
| h2 (mlp) | 中间激活 → down_proj 输入 | 一致 |
| sparse_fns['q'] | SparsifyFn on h1 distr | 一致 |
| sparse_fns['k'] | SparsifyFn on h1 distr | 一致 |
| sparse_fns['v'] | SparsifyFn on h1 distr | 一致 |
| sparse_fns['o'] | SparsifyFn on h2 distr | 一致 |
| sparse_fns['gate'] | SparsifyFn on h1 distr | 一致 |
| sparse_fns['up'] | SparsifyFn on h1 distr | 一致 |
| sparse_fns['down'] | SparsifyFn on h2 distr | 一致 |

#### 4.6 greedyopt weight_dict

需要为 DeepSeek-R1-Distill-Qwen-14B 添加权重配置：

```python
"Qwen2-14B": {
    'q': 1,
    'k': 1/5,        # num_kv_heads/num_heads = 8/40 = 1/5
    'v': 1/5,
    'o': 1,
    'gate': 13824/5120,  # intermediate_size/hidden_size ≈ 2.7
    'up': 13824/5120,
    'down': 13824/5120
}
```

#### 4.7 grab_acts.py 适配

`grab_acts.py` 手动调用 `model.model.rotary_emb(hidden_states, position_ids)` 并逐层传播。Qwen2 模型中 `rotary_emb` 签名可能不同（有的版本接受 `seq_len` 而非 `position_ids`），需要检查并适配。`position_embeddings` 在当前代码中实际未被使用（layer forward 内部会自己计算），所以这一行主要是兼容性问题。

---

## 5. 已有预校准模型

### models/ 目录

| 模型 | histograms | lookup (greedy) |
|------|-----------|-----------------|
| Llama-2-7B | 32 layers × {mlp, self_attn} | 32 layers results.csv |
| Llama-2-13B | 40 layers × {mlp, self_attn} | 40 layers results.csv |
| Llama-2-70B | 80 layers × {mlp, self_attn} | 80 layers results.csv |
| Llama-3-8B | 32 layers × {mlp, self_attn} + lookup 嵌套 | 32 layers results.csv |
| Llama-3-70B | 80 layers × {mlp, self_attn} + lookup 嵌套 | 80 layers results.csv |
| Mistral-7B | 32 layers × {mlp, self_attn} | 32 layers results.csv |

### 数据格式可复用性

完全可以复用相同结构给新模型。只需：
1. 运行 grab_acts.py 生成 histograms/ 和 activations/
2. （可选）运行 greedyopt.py 生成 lookup/
3. 产出文件格式完全一致（histograms.pt + results.csv）

---

## 6. 校准耗时和 GPU 内存预估

### DeepSeek-R1-Distill-Qwen-14B (48 layers, 14B params)

#### grab_acts.py

- **内存需求**: 模型 FP16 ≈ 28GB，输入激活 [10, 2048, 5120] ≈ 200MB，逐层释放后峰值约 **30-32GB**（需要 1x A100-40G 或 1x A6000-48G）
- **耗时**: 逐层前向 48 层 × (forward + histogram 计算)，预计 **10-20 分钟**
- **磁盘**: histograms ≈ 48 × 2 × 4 × 10000 × 4B ≈ 15MB（很小）；activations ≈ 48 × 10 × 2048 × 5120 × 2B ≈ **9.4GB**

#### greedyopt.py

- **内存需求**: 模型在 CPU，逐层移到 GPU。GPU 上：单层参数 + 输入激活 + forward 计算。14B 模型单层约 600MB，激活约 200MB，峰值 GPU 约 **2-4GB**（内存友好）
- **耗时**: 每层 greedy 搜索，每步试 7 个 projection，步数 ≈ target_sparsity / base_step_size ≈ 18-36 步（step_size=0.025, target=0.9），每步 7 次 forward → 每层约 126-252 次 forward。48 层总计约 6000-12000 次单层 forward，预计 **1-3 小时**
- **磁盘**: lookup CSV 每层几十 KB，总计约 **2-3MB**

#### 总计

| 阶段 | GPU 内存 | 耗时 | 磁盘 |
|------|---------|------|------|
| grab_acts | ~30-32GB | 10-20 min | ~10GB (activations 为主) |
| greedyopt | ~2-4GB | 1-3 hours | ~3MB |
| **仅 uniform** | ~30-32GB | 10-20 min | ~15MB |

如果只用 uniform sparsity，可以跳过 greedyopt 和 activations 保存，只需 histograms，耗时和磁盘都大幅减少。

---

## 7. 快速适配方案总结

对 DeepSeek-R1-Distill-Qwen-14B，最小修改集：

1. **新建** `Qwen2SparseForCausalLM` 和 `Qwen2SparseConfig`（`model.py`，~10 行）
2. **扩展** `get_sparse_model` 的模型类白名单（`utils.py`，~5 行）
3. **扩展** `build_sparse_layers` 的 isinstance 检查（`model.py`，1 行）
4. **验证** Qwen2 的 attention forward 与 monkeypatch 兼容（可能需要调整 `_FA2_forward` 的 rotary_emb 调用）
5. **添加** greedyopt weight_dict 条目（`greedyopt.py`，~5 行）
6. **适配** `grab_acts.py` 的 rotary_emb 调用（1-2 行）

由于 Qwen2 的 projection 命名与 Llama 完全一致（q_proj/k_proj/v_proj/o_proj/gate_proj/up_proj/down_proj），mlp.py 和 self_attn.py 的 monkeypatch 逻辑无需修改。

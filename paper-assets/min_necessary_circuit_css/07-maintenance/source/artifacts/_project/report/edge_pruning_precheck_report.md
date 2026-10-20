# Edge Pruning 大模型适配预检报告

> 日期：2026-05-13
> 目标：评估 `princeton-nlp/edge-pruning` 对 Qwen-2.5 0.5B / Gemma-2 2B / Llama-3.1 8B 的支持情况

---

## 1. 支持情况总结

| 模型 | 原生支持 | 社区适配 | 架构相似度 | 适配难度 | 预估工时 |
|------|---------|---------|-----------|---------|---------|
| Qwen-2.5 0.5B | ❌ | ✅ 有 fork（未完成） | 极高（≈LLaMA） | **低** | 6-10h |
| Gemma-2 2B | ❌ | ❌ | 中（有独特机制） | **中** | 16-24h |
| Llama-3.1 8B | ❌ | ❌ | 极高（≈CodeLlama） | **低-中** | 8-14h |

## 2. 仓库现状

### 2.1 原生支持的模型

Edge Pruning（NeurIPS 2024 Spotlight）仅实现了三种模型：

- **GPT-2**（`modeling_fpt2.py`，1713行）— IOI/GT/GP 任务，单 GPU
- **CodeLlama-13B**（`modeling_fllama.py`，2050行）— Boolean Expressions，32 GPU FSDP
- **Tracr**（`modeling_erazr.py`，1105行）— 合成模型

README 提到 *"Extension to other models should be straightforward by mimicking modeling_{fpt2/fllama}.py"*，但未提供更多架构的实现。

### 2.2 核心机制

Edge Pruning 的实现方式决定了适配工作的性质：

1. **残差流扩展**：hidden state 从 `(batch, seq, hidden)` 扩展为 `(n_writers, batch, seq, hidden)`，每个 writer slot 对应一个组件的输出
2. **Reader 掩码读取**：每个 reader（Q/K/V/MLP input）通过 `einsum("wbsd,wh->hbsd", writers, mask)` 加权求和读取输入
3. **Writer 门控写入**：每个 writer 输出经 node mask 门控后放入对应 slot
4. **L0 正则化**：`log_alpha` 参数通过 stretched concrete 分布采样，Lagrangian 松弛驱动稀疏度

**关键含义**：适配新模型 = 重写整个 forward pass，将标准 HuggingFace 模型改造为 writer/reader DAG 结构。不是简单的 hook 注入，而是深度改造。

### 2.3 社区贡献

- **PR**：仅 1 个（typo 修复），无模型扩展
- **Issues**：7 个，均不涉及新模型
- **关键 Fork**：`melodyycui/Edge-Pruning` 添加了 `modeling_fqwen.py`（54KB），实现 Qwen2 的 edge pruning 支持。活跃至 2026-05-11，但缺少 pruning scripts / eval scripts / run scripts。可作为 Qwen 适配的参考起点。

---

## 3. 逐模型详细分析

### 3.1 Qwen-2.5 0.5B

**架构特性**：
- RMSNorm ✅（FLlama 已支持）
- GQA ✅（FLlama 已支持，`num_kv_heads` ≠ `num_heads`）
- RoPE ✅（FLlama 已支持）
- SwiGLU MLP ✅（FLlama 已支持）
- 单一 embedding（无 position embedding）✅（FLlama 已支持）

**结论**：Qwen-2.5 架构与 LLaMA 高度同构。`modeling_fllama.py` 可直接作为模板。社区 fork `melodyycui/Edge-Pruning` 已有 `modeling_fqwen.py` 参考实现。

**适配路径**：
1. 基于 `modeling_fllama.py` 修改，替换 HuggingFace 的 `Qwen2ForCausalLM` 类层次
2. 参考 `melodyycui` 的 `modeling_fqwen.py` 处理 Qwen2 特有的 config 字段映射
3. 调整 attention bias 处理（Qwen2 有 `attention_bias` config 选项）
4. 编写 pruning script 和 eval script

**预估**：6-10 小时（有社区参考代码，且 0.5B 单 GPU 即可运行）

### 3.2 Gemma-2 2B

**架构特性**：
- RMSNorm ✅（FLlama 已支持）
- GQA ✅（FLlama 已支持）
- RoPE ✅（FLlama 已支持）
- GeGLU MLP — 与 SwiGLU 同为 gated MLP，门控函数不同，改动小
- **Logit soft-capping** ⚠️ — attention logits 和 final logits 有 tanh soft-cap，需在 edge pruning 的 attention 实现中加入
- **交替 sliding window / global attention** ⚠️ — 偶数层用 sliding window（4096），奇数层用 global attention，attention mask 处理更复杂
- **Pre/Post-norm 混合** ⚠️ — 每个 sublayer 前后都有 RMSNorm（post-norm 对 writer 输出的归一化有影响）

**需要额外处理的部分**：
1. Sliding window attention 与 global attention 的交替——影响 writer/reader 的因果 mask 构建
2. Logit soft-capping——在修改后的 attention forward 中添加 `tanh(logits / soft_cap_value) * soft_cap_value`
3. Pre/Post-norm 混合——post-norm 改变了 writer 输出到残差流的路径，需要调整 `attn_write` 和 `mlp_write` 逻辑
4. Gemma2 的 HuggingFace 实现类名不同（`Gemma2DecoderLayer` 等）

**预估**：16-24 小时（sliding window + post-norm 的交互需要仔细处理，且 2B 参数量需要考虑显存优化）

### 3.3 Llama-3.1 8B

**架构特性**：
- RMSNorm ✅
- GQA ✅（8 KV heads / 32 Q heads）
- RoPE ✅（Llama-3 用 theta=500000 的高频 RoPE）
- SwiGLU MLP ✅

**与 CodeLlama-13B 的差异**：
- Llama-3.1 用 `LlamaForCausalLM`（HF class），CodeLlama 也是 `LlamaForCausalLM`——类层次完全一致
- GQA 比例不同（Llama-3.1 8B: 8 KV heads / 32 Q heads；CodeLlama-13B: 40 KV heads / 40 Q heads 即 MHA）
- 实际上 `modeling_fllama.py` 已经完整支持 GQA（K/V read log_alphas 有独立维度）

**适配路径**：
1. `modeling_fllama.py` 几乎可以直接使用——只需确认 HuggingFace `transformers` 版本的 API 兼容性
2. 主要工作在于 FSDP / 显存管理（8B 模型 + writer tensor 扩展 = 显存大幅增加）
3. 原 CodeLlama-13B 用 32 GPU FSDP 训练；8B 可能 4-8 GPU 可行（取决于序列长度和 batch size）

**额外挑战（规模相关）**：
- Writer tensor 从 `(n_writers, batch, seq, hidden)` 维度上，8B 模型有 32 层 × 32 heads = 1024 个 attention writer + 32 MLP writer + 1 embed = 1057 writers
- 每个 writer slot 占 `batch × seq × 4096` × bf16 = 较大显存开销
- 可能需要 gradient checkpointing + FSDP offload

**预估**：8-14 小时（代码适配简单，主要时间花在 FSDP 配置调试和显存优化）

---

## 4. 显存估算

Edge Pruning 的核心开销是 writer tensor 的显存扩展：

| 模型 | 层数 | Heads | Writers | Hidden | Writer Tensor (bf16, bs=1, seq=64) |
|------|------|-------|---------|--------|-------------------------------------|
| GPT-2 Small | 12 | 12 | 157 | 768 | 157 × 64 × 768 × 2B ≈ 15 MB |
| Qwen-2.5 0.5B | 24 | 14 | 361 | 896 | 361 × 64 × 896 × 2B ≈ 41 MB |
| Gemma-2 2B | 26 | 8 | 235 | 2304 | 235 × 64 × 2304 × 2B ≈ 69 MB |
| Llama-3.1 8B | 32 | 32 | 1057 | 4096 | 1057 × 64 × 4096 × 2B ≈ 553 MB |
| CodeLlama 13B | 40 | 40 | 1641 | 5120 | 1641 × 64 × 5120 × 2B ≈ 1.07 GB |

注：这只是 writer tensor 本体。实际训练还需要：模型参数、log_alpha 参数、优化器状态、激活缓存、梯度等。Llama-3.1 8B 预计单卡（A6000 48GB）显存不足，需 2-4 卡或 FSDP offload。

---

## 5. 替代方案分析

### 5.1 auto-circuit（UFO-101/auto-circuit）

| 维度 | auto-circuit | Edge Pruning |
|------|-------------|-------------|
| 后端 | TransformerLens（HookedTransformer） | 自定义 HF 模型改造 |
| 模型支持 | Qwen ✅ Gemma ✅ Llama-3 ✅（通过 TransformerLens） | 仅 GPT-2 + CodeLlama |
| 掩码优化 | Subnetwork Probing（hard_concrete + L0） | 同（stretched concrete + Lagrangian） |
| 算法数 | 18 种（含 EAP、ACDC、mask gradient 等） | 1 种（mask optimization） |
| 分布式 | ❌ 无 | ✅ FSDP |
| 已验证规模 | ≤ 2.8B（Pythia） | ≤ 13B（CodeLlama，32 GPU） |
| 显存效率 | 差（TransformerLens 额外 20-30% 开销 + 所有 edge 需缓存激活） | 较好（直接改造 HF 模型） |

**评估**：auto-circuit 对小模型（Qwen-2.5 0.5B）是可行的替代方案，开箱即支持且 Subnetwork Probing 与 Edge Pruning 方法论等价。但对 Llama-3.1 8B，TransformerLens 的显存开销 + 无分布式支持 = 不可行。

### 5.2 建议

- **Qwen-2.5 0.5B**：可同时考虑 Edge Pruning 直接适配（有社区参考）和 auto-circuit（开箱即用），选易于集成到 CSS pipeline 的方案
- **Gemma-2 2B / Llama-3.1 8B**：必须走 Edge Pruning 适配路线，auto-circuit 不适用于此规模

---

## 6. 适配工作分解

### 共性工作（一次性）

| 任务 | 预估 | 说明 |
|------|------|------|
| 理解 FLlama 代码结构 | 2h | 吃透 writer/reader DAG、log_alpha 管理、mask 采样 |
| 抽取通用模板 | 3h | 从 FLlama 提取可复用的基类或工具函数 |
| 编写通用 pruning script | 2h | 复用 `fpt2_custom.py` 的数据加载 + trainer 逻辑 |
| 编写通用 eval script | 1h | 掩码二值化 + circuit 提取 |
| **小计** | **8h** | |

### Qwen-2.5 0.5B

| 任务 | 预估 | 说明 |
|------|------|------|
| `modeling_fqwen.py` | 4h | 参考 FLlama + 社区 fork，适配 Qwen2 类层次 |
| 验证 + 调试 | 2-4h | 单 GPU 验证 forward pass、mask 采样、circuit 提取 |
| CSS pipeline 集成 | 2h | 接入 `edge_pruning_scoring.py` |
| **小计** | **6-10h** | |

### Gemma-2 2B

| 任务 | 预估 | 说明 |
|------|------|------|
| `modeling_fgemma.py` | 10h | 需处理 sliding window、logit soft-cap、pre/post-norm |
| FSDP 配置 | 2h | 2B 可能需 2 GPU |
| 验证 + 调试 | 4-8h | Gemma-2 独特机制的交互可能引入 bug |
| CSS pipeline 集成 | 2h | |
| **小计** | **16-24h** | |

### Llama-3.1 8B

| 任务 | 预估 | 说明 |
|------|------|------|
| `modeling_fllama3.py` | 2h | FLlama 代码几乎可直接使用 |
| FSDP 配置 + 显存优化 | 4-6h | gradient checkpointing、offload 调试 |
| 验证 + 调试 | 2-4h | |
| CSS pipeline 集成 | 2h | |
| **小计** | **8-14h** | |

### 总计

| 场景 | 总工时 |
|------|-------|
| 仅 Qwen-2.5 0.5B | 14-18h |
| 全部三模型 | 38-56h |
| 全部三模型（含通用模板） | 30-48h（复用模板后递减） |

---

## 7. 风险与缓解

| 风险 | 影响 | 缓解措施 |
|------|------|---------|
| Gemma-2 sliding window + edge pruning 交互导致 mask 逻辑错误 | 高 | 先在小规模（2层）上验证 attention mask 正确性 |
| Llama-3.1 8B 显存不足 | 中 | FSDP offload + gradient checkpointing；或降低 batch size / seq length |
| HuggingFace transformers 版本不兼容 | 中 | 锁定 transformers 版本；README 已警告过此问题 |
| 社区 Qwen fork 代码质量不确定 | 低 | 作为参考而非直接使用，自行验证 |
| Writer tensor 扩展改变模型行为（数值不稳定） | 低 | bf16 + gradient clipping；FLlama 已验证此路线可行 |

---

## 8. 结论与推荐路径

### 可行性判断：**可行，但需要非平凡的工程投入**

Edge Pruning 不是即插即用的库——每个新模型都需要重写完整的 forward pass（1500-2000行代码）。但 `modeling_fllama.py` 已经为 LLaMA 架构铺好了路，且 Qwen-2.5 和 Llama-3.1 都是 LLaMA-like 架构，适配成本可控。Gemma-2 因其独特的 attention 机制需要更多工作。

### 推荐路径

**Phase 2 优先级排序**：

1. **Qwen-2.5 0.5B（第一个）**：适配成本最低、有社区参考、单 GPU 可跑、快速验证 CSS 方法在大模型上的效果
2. **Llama-3.1 8B（第二个）**：代码适配简单但需要多 GPU 工程、验证 CSS 在真正的大模型上的可扩展性
3. **Gemma-2 2B（第三个或酌情跳过）**：适配成本最高、独特架构特性增加 bug 风险。如果 Qwen + Llama 已足够证明方法的通用性，可考虑将 Gemma-2 降级为 optional

**Phase 2 方法配置确认**：大模型用 EAP-IG + Edge Pruning + IFR（2 因果 + 1 相似度），不含 ACDC。Edge Pruning 作为唯一的 mask-based optimization 方法，必须适配成功。auto-circuit 可作为 Qwen-2.5 0.5B 的备选方案，但不推荐作为主路线（与 CSS pipeline 的集成成本更高，且不支持大模型分布式训练）。

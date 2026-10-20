# 第二 VLA 模型调研报告

**目的**: 寻找第二个 decoder-only VLA 模型，验证 L1 instruction routing 是否为 decoder-only VLA 的通用现象。

**核心约束**: 必须是 decoder-only 架构（causal mask），必须有公开权重，backbone 最好与 OpenVLA (Llama-2-7B) 不同，排除 JAX 框架。

---

## 1. 候选列表总表

| 模型 | 架构类型 | Backbone | 参数量 | 公开权重 | 训练数据 | 框架 | Action 编码方式 | 适配难度 |
|------|---------|----------|--------|---------|---------|------|----------------|---------|
| **OpenVLA-Phi3V** | decoder-only ✅ | Phi-3-Vision (4B) | ~4B | [HF](https://huggingface.co/furonghuang-lab/openvla_phi3v) | OXE 970K | PyTorch | 256-bin discrete (同 OpenVLA) | ⭐ 极低 |
| **SpatialVLA** | decoder-only ✅ | PaLiGemma2 / Gemma 2 | ~4B | [HF](https://huggingface.co/IPEC-COMMUNITY/spatialvla-4b-224-pt) | OXE + RH20T 1.1M | PyTorch | Adaptive spatial action tokens | ⭐⭐ 低-中 |
| **NORA** | decoder-only ✅ | Qwen-2.5-VL-3B | ~3B | [HF](https://huggingface.co/declare-lab/nora) | OXE 970K | PyTorch | FAST+ tokenizer (变长) | ⭐⭐⭐ 中 |
| **TraceVLA-Phi3** | decoder-only ✅ | Phi-3-Vision (4B) | ~4B | [HF](https://huggingface.co/furonghuang-lab/tracevla_phi3v) | OXE 970K + trace | PyTorch | 256-bin discrete (同 OpenVLA) | ⭐ 极低 |
| **NORA-1.5** | decoder-only ✅ | Qwen-2.5-VL-3B | ~3B | [HF](https://huggingface.co/declare-lab/nora-1.5) | OXE 970K + pref. | PyTorch | FAST+ tokenizer (变长) | ⭐⭐⭐ 中 |
| **π₀ (openpi)** | cross-attn MoE ❌ | PaliGemma 3B + action expert | ~3B+ | [GitHub](https://github.com/Physical-Intelligence/openpi) | OXE + PI data | JAX→PyTorch | Flow matching (连续) | N/A (负对照) |
| **SmolVLA** | VLM + cross-attn action expert ❌ | SmolLM2 + SigLIP | ~450M | [HF/LeRobot](https://huggingface.co/blog/smolvla) | LeRobot community | PyTorch | Cross-attn action expert | N/A (负对照) |
| **GR00T-N1** | encoder-decoder + diffusion ❌ | SigLip2 + T5 + DiT | 2-3B | [HF](https://huggingface.co/nvidia/GR00T-N1-2B) | NVIDIA data | PyTorch | Diffusion transformer | N/A (架构不同) |
| **CogACT** | decoder-only backbone + DiT action head | Llama-2-7B + DiT | ~7B+ | [HF](https://huggingface.co/CogACT/CogACT-Base) | OXE 400K | PyTorch | Diffusion (DiT action head) | 不适用 |
| **DeeR-VLA** | cross-attn (OpenFlamingo) ❌ | OpenFlamingo 3B/9B | 3-9B | [HF](https://huggingface.co/Yang130/DeeR-VLA) | CALVIN | PyTorch | 连续 | 不适用 |
| **Octo** | encoder + diffusion head ❌ | Transformer encoder | 93M | 开源 | OXE | JAX ❌ | Diffusion | 已排除 (JAX) |
| **RT-2-X** | decoder-only | PaLM-E 55B | 55B | **无公开权重** ❌ | Google 内部 | JAX | 256-bin discrete | 不可用 |
| **A1** | VLM + flow matching head | 未明确 (可能 InternVL) | 未知 | 代码开源，权重待确认 | DROID+AgiBot+OXE | PyTorch | Flow matching | 待确认 |

---

## 2. 排除理由汇总

| 排除模型 | 排除原因 |
|----------|---------|
| **Octo** | JAX 框架 |
| **RT-2-X** | 无公开权重，模型 55B 太大，JAX |
| **GR00T-N1** | 非 decoder-only (encoder-decoder + diffusion)，action 不通过 LLM backbone |
| **π₀** | 非 decoder-only (cross-attention MoE)，action expert 独立于 VLM backbone |
| **SmolVLA** | 非 decoder-only (独立 action expert + cross-attention) |
| **CogACT** | action 由独立 DiT 生成，不经过 LLM backbone；且 backbone 与 OpenVLA 相同 (Llama-2) |
| **DeeR-VLA** | 基于 OpenFlamingo (cross-attention 架构)，非纯 decoder-only |
| **ECoT** | 基于 OpenVLA (Llama-2 backbone)，backbone 与 OpenVLA 相同 |

---

## 3. Top-3 推荐（排序 + 理由）

### 🥇 推荐 1: OpenVLA-Phi3V

**理由**: 这是最理想的对比实验候选。与 OpenVLA-7B 使用完全相同的训练配方（相同数据 OXE 970K、相同 action tokenization 256-bin discrete、相同架构范式），唯一区别是 LLM backbone 从 Llama-2-7B 换成了 Phi-3-Vision (~4B)。这使得对比实验的变量控制最干净——如果 L1 instruction routing 同样出现在 Phi-3 backbone 中，可以强有力地论证这是 decoder-only VLA 的通用属性而非 Llama-2 的特异行为。

| 属性 | 详情 |
|------|------|
| HuggingFace | `furonghuang-lab/openvla_phi3v` |
| Backbone | Phi-3-Vision (decoder-only, ~4B params) |
| Action tokens | 256-bin discrete（与 OpenVLA 完全相同） |
| 训练数据 | OXE 970K（与 OpenVLA 相同） |
| GPU 需求 | ~10GB (FP16)，单卡即可 |
| 适配工作量 | **极低** — 与 OpenVLA 使用相同 codebase，attention extraction 代码可直接复用，仅需调整模型加载路径 |

**下载命令**:
```bash
# 下载模型
pip install huggingface_hub
huggingface-cli download furonghuang-lab/openvla_phi3v --local-dir /root/autodl-tmp/models/openvla-phi3v

# 或在代码中
from transformers import AutoModelForCausalLM, AutoProcessor
model = AutoModelForCausalLM.from_pretrained("furonghuang-lab/openvla_phi3v", torch_dtype=torch.bfloat16)
```

**预计适配步骤**:
1. 下载模型权重 (~8GB)
2. 修改现有 attention extraction 代码，适配 Phi-3 的 attention 层命名 (Phi-3 用 `model.layers[i].self_attn` 而非 Llama 的命名)
3. 确认 vision/language/action token 边界在 Phi-3 中的定位方式
4. 运行 attention extraction + probe 分析
5. **预计时间: 2-3 天**

**风险**: 
- Phi-3-Vision 的注意力头数/层数与 Llama-2 不同，需确认 L1 定义（Layer 1 of decoder）在 Phi-3 中的对应位置
- OpenVLA-Phi3V 由 TraceVLA 团队（非 OpenVLA 官方）训练，训练超参可能有微小差异

---

### 🥈 推荐 2: SpatialVLA

**理由**: 完全独立的团队和框架，backbone 是 Gemma 2（通过 PaLiGemma2），与 Llama-2 差异更大。使用 autoregressive next-token prediction 训练，action tokens 通过 Gemma 2 decoder 的 causal attention 处理。如果 L1 routing 同样出现在 Gemma 2 backbone 中，说明这个现象跨越了 Llama 和 Gemma 两个完全不同的 LLM 家族。

| 属性 | 详情 |
|------|------|
| HuggingFace | `IPEC-COMMUNITY/spatialvla-4b-224-pt` |
| Backbone | PaLiGemma2 = SigLIP (vision) + Gemma 2 (decoder-only LLM, ~2B decoder params) |
| Action tokens | Adaptive spatial action tokens (离散，autoregressive 预测) |
| 训练数据 | OXE + RH20T, 1.1M episodes |
| GPU 需求 | ~8.5GB (inference) |
| 适配工作量 | **低-中** — 需要理解 spatial action token 的 tokenization 方案，attention extraction 需要适配 PaLiGemma2 的架构 |

**下载命令**:
```bash
huggingface-cli download IPEC-COMMUNITY/spatialvla-4b-224-pt --local-dir /root/autodl-tmp/models/spatialvla-4b

# 代码示例
git clone https://github.com/SpatialVLA/SpatialVLA.git
```

**预计适配步骤**:
1. 下载模型 + clone SpatialVLA repo
2. 研究 PaLiGemma2 的 attention 层结构（Gemma 2 decoder layers）
3. 确定 vision tokens / language tokens / action tokens 在 input sequence 中的边界
4. 理解 adaptive action grid tokenization（与 OpenVLA 的 256-bin 不同）
5. 适配 attention extraction 代码
6. 运行分析
7. **预计时间: 4-5 天**

**风险**:
- Action tokenization 方案不同于 OpenVLA（spatial action tokens vs 256-bin），attention pattern 的对比需要 normalize
- PaLiGemma2 的 vision token 处理方式不同（SigLIP tokens 直接投射到 Gemma 2 input space）
- 相对 OpenVLA-Phi3V，变量控制更松（同时改变了 backbone 和 action tokenization）

---

### 🥉 推荐 3: NORA

**理由**: backbone 是 Qwen-2.5-VL (又一个不同的 LLM 家族)，模型最小 (3B)，实验速度最快。Qwen-2.5-VL 与 Llama-2 和 Gemma 2 都不同，增加 generalizability 覆盖面。

| 属性 | 详情 |
|------|------|
| HuggingFace | `declare-lab/nora` |
| Backbone | Qwen-2.5-VL-3B (decoder-only) |
| Action tokens | FAST+ tokenizer（变长离散 token，基于 DCT + BPE） |
| 训练数据 | OXE 970K |
| GPU 需求 | ~7GB (inference) |
| 适配工作量 | **中** — FAST+ tokenizer 产生变长 token，action token 边界识别复杂；Qwen-2.5-VL 使用动态分辨率（vision token 数量可变） |

**下载命令**:
```bash
huggingface-cli download declare-lab/nora --local-dir /root/autodl-tmp/models/nora

git clone https://github.com/declare-lab/nora.git
```

**预计适配步骤**:
1. 下载模型 + clone nora repo
2. 研究 Qwen-2.5-VL 的 attention 层结构
3. 理解 FAST+ tokenizer 的 action token 编码方式（变长 token）
4. 处理 Qwen-2.5-VL 的动态分辨率 vision token 问题
5. 适配 attention extraction + probe 代码
6. 运行分析
7. **预计时间: 5-7 天**

**风险**:
- FAST+ tokenizer 产生变长 action tokens，与 OpenVLA 的固定 7-dim 256-bin tokens 差异大，attention pattern 对比困难
- Qwen-2.5-VL 使用 dynamic resolution (vision token 数不固定)，token position 分析复杂
- 模型较新 (2025-04)，社区使用经验少

---

## 4. 推荐策略

### 首选方案：OpenVLA-Phi3V（快速出结果）
- **优势**: 最小适配工作量，变量控制最干净，2-3 天可出结果
- **论文叙事**: "We replicate our analysis on OpenVLA-Phi3V, which uses an identical training recipe but replaces Llama-2 with Phi-3-Vision as the LLM backbone. The L1 instruction routing pattern persists across different LLM architectures."
- **潜在 reviewer 反驳**: "Phi-3 和 Llama-2 都是同类 decoder-only LLM，能否证明在更不同的架构上也成立？"

### 加强方案：OpenVLA-Phi3V + SpatialVLA（双重验证）
- **优势**: 覆盖 Llama-2 + Phi-3 + Gemma 2 三个 LLM 家族，一个同配方不同 backbone，一个完全独立的模型
- **论文叙事**: "The L1 routing phenomenon generalizes across three distinct LLM backbones (Llama-2, Phi-3, Gemma-2) and two independent VLA training frameworks (OpenVLA, SpatialVLA)."

### 负对照（可选）：π₀
- 用 openpi (PyTorch port via LeRobot) 做负对照
- 预测：cross-attention MoE 架构不应出现 L1 instruction routing pattern
- 若负对照成立，进一步证明 L1 routing 是 decoder-only 架构的特异性质

---

## 5. 详细架构对比

```
OpenVLA-7B:           [SigLIP+DINOv2] → Projector → [Llama-2-7B Decoder] → action tokens (256-bin)
                                                      ↑ causal attention over all tokens

OpenVLA-Phi3V:        [Phi-3-Vision Encoder] → Projector → [Phi-3 Decoder ~4B] → action tokens (256-bin)
                                                             ↑ causal attention over all tokens

SpatialVLA:           [SigLIP + Ego3D PE] → Projector → [Gemma-2 Decoder ~2B] → spatial action tokens
                                                          ↑ causal attention over all tokens

NORA:                 [Qwen-2.5-VL Vision] → Projector → [Qwen-2.5 Decoder ~3B] → FAST+ action tokens
                                                           ↑ causal attention over all tokens

π₀ (负对照):          [PaliGemma VLM 3B] ──cross-attn──→ [Action Expert] → flow matching actions
                       ↑ VLM 和 action expert 是分离的，不共享 causal attention
```

关键共性：前四个模型都将 vision + language + action tokens 送入同一个 decoder-only LLM，用 causal attention 处理。π₀ 的 action expert 是独立的，通过 cross-attention 与 VLM 交互。

---

## 6. 风险总评

| 风险 | 影响 | 缓解措施 |
|------|------|---------|
| OpenVLA-Phi3V 非官方训练，可能有 subtle 差异 | 低 | 先验证其在 SimplerEnv 上的 baseline 性能是否合理 |
| SpatialVLA action tokenization 与 OpenVLA 不同 | 中 | 分析时关注 instruction→vision attention 而非 instruction→action，减少 tokenization 差异影响 |
| NORA FAST+ 变长 token 难以定位 action boundary | 中-高 | 先尝试 OpenVLA-Phi3V 和 SpatialVLA，NORA 作为备选 |
| 所有候选训练数据高度重叠 (OXE) | 低 | 这实际上是优势——控制了训练数据变量 |
| Phi-3 层数/头数不同，L1 对应关系需要重新定义 | 低 | 定义为 "第一个 decoder layer" 而非绝对层号 |

---

*调研日期: 2026-05-19*
*搜索覆盖: arXiv 2024-2026, HuggingFace, GitHub, 主要 VLA 综述*

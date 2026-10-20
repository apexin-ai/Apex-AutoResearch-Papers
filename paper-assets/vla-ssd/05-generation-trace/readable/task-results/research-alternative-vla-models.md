# research alternative vla models

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_alternative_vla_models_20260521T001840_result.json`
- **Structured JSON:** [`42b17dd79f1ebc1d4675.json`](../../sessions/42/42b17dd79f1ebc1d4675.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。汇总结果如下。

---

## 排除的候选

| 模型 | 排除原因 |
|------|---------|
| **OpenVLA-OFT** | Action 通过 4-layer MLP 输出连续值 + L1 regression，**不是** autoregressive token decoding。且 backbone 用 LoRA，不是 full fine-tune |
| **CogACT** | Action 通过 Diffusion Transformer (DiT) 解码，不是 autoregressive |
| **π0** | Flow matching 生成 action |
| **SmolVLA** | 已知排除（VLM frozen + flow matching） |
| **Octo** | Diffusion policy head |
| **AR-VLA** | 独立的 Action Expert 模块，VLM backbone 不参与 action 生成 |

---

## 满足条件的候选

### 1. WorldVLA

| 项 | 详情 |
|----|------|
| **论文** | WorldVLA: Towards Autoregressive Action World Model (arXiv 2506.21539) |
| **HF repo** | `jcenaa/WorldVLA-ActionModel-LIBERO-10-256`（另有 LIBERO-Spatial/Object/Goal/Long 各分辨率 checkpoint） |
| **LLM backbone** | **Chameleon 7B**（Meta，统一多模态 autoregressive 模型） |
| **Fine-tuning** | 从 Chameleon 初始化后联合训练 action model + world model。论文未提及 LoRA 或 frozen，训练方式为全模态统一 autoregressive，**极大概率 full fine-tune** |
| **Action 生成** | **Autoregressive discrete tokens**：每维 action 离散化为 256 bins → 7 tokens，通过 LLM causal decoder 生成 |
| **LIBERO checkpoint** | ✅ 有（256×256 和 512×512 两种分辨率，四个 LIBERO suite） |
| **Base VLM 可用** | ✅ Meta 公开了 Chameleon 权重 |
| **与 OpenVLA 差异** | **高**：完全不同的 backbone（Chameleon vs Llama-2），不同 vision 处理（VQ-GAN tokenizer vs ViT），统一多模态 tokenization |

### 2. NORA

| 项 | 详情 |
|----|------|
| **论文** | NORA: A Small Open-Sourced Generalist VLA (arXiv 2504.19854) |
| **HF repo** | `declare-lab/nora`，`declare-lab/nora-finetuned-libero-object` 等 |
| **LLM backbone** | **Qwen2.5-VL-3B**（~4B 参数） |
| **Fine-tuning** | "Fine-tuned directly from Qwen 2.5 VL-3B"，8×H100 训练 3 周，1.1M gradient steps，4000 H100 GPU-hours。规模和描述**强烈暗示 full fine-tune** |
| **Action 生成** | **Autoregressive discrete tokens**：使用 FAST+ tokenizer（DCT + BPE），通过 LLM next-token prediction 生成 |
| **LIBERO checkpoint** | ✅ 有（NORA-fine-tuned 和 NORA-Long-fine-tuned，avg 73.9%–87.9%） |
| **Base VLM 可用** | ✅ Qwen2.5-VL-3B 公开在 HuggingFace |
| **与 OpenVLA 差异** | **高**：不同 backbone（Qwen vs Llama-2），不同 vision encoder（Qwen2.5-VL native resolution vs ViT-G DINOv2+SigLIP），不同 action tokenizer（FAST+ vs 256-bin per-dim），更小模型（3B vs 7B） |

### 3. UniVLA

| 项 | 详情 |
|----|------|
| **论文** | Unified Vision-Language-Action Model (arXiv 2506.19850, ICLR 2026) |
| **HF repo** | `Yuqi1997/UniVLA` |
| **LLM backbone** | **Emu3 8.5B**（BAAI，encoder-free autoregressive 模型） |
| **Fine-tuning** | 从 Emu3-Stage1 初始化 → world model post-training → 下游 supervised fine-tuning。**全参数训练** |
| **Action 生成** | **Autoregressive discrete tokens**：视觉、语言、action 统一 tokenize，single autoregressive decoder |
| **LIBERO checkpoint** | ✅ 有（img-sft 94.8%, video-sft 95.5%） |
| **Base VLM 可用** | ✅ `BAAI/Emu3-Stage1` 公开 |
| **与 OpenVLA 差异** | **极高**：encoder-free 架构（无 ViT），统一多模态 tokenization，不同 backbone（Emu3 vs Llama-2），更大模型（8.5B vs 7B） |

---

## 推荐

**首选：NORA**
- 三个核心条件全部满足（backbone fine-tuned、autoregressive discrete action、公开 LIBERO checkpoint）
- Qwen2.5-VL-3B backbone 与 OpenVLA (Llama-2) 和 TracVLA (Phi-3-mini) 构成三种不同 LLM 家族的对比
- 模型较小（3B），分析内部表征的计算成本低
- HuggingFace 生态完善，Qwen2.5-VL 有很好的 transformers 支持

**备选：WorldVLA**
- Chameleon 7B 也是完全不同的 backbone
- LIBERO checkpoint 齐全
- 但 Chameleon 是较 niche 的架构，工具链支持不如 Qwen

**UniVLA 也可行**但 encoder-free + Emu3 架构最特殊，与标准 VLM→VLA 的 fine-tuning 范式差异过大，可能不太适合做"fine-tuning 如何改变 LLM 表征"的研究（因为它的 vision 处理方式完全不同）。

---

需要我进一步确认某个候选的具体细节（如精确 fine-tuning 配置），还是直接推进选定模型的实验准备？

---

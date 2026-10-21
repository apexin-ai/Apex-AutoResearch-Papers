# research vla model survey

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_vla_model_survey_20260523T062811_result.json`
- **Structured JSON:** [`48d4857cdb61094bcae9.json`](../../sessions/48/48d4857cdb61094bcae9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个调研 agent 已返回。以下是汇总结果。

## 调研结果

### 一、候选模型总表

| 模型 | LIBERO Checkpoint | Connector 类型 | 参数量 | Vision Token 数 | Setup 时间 | 兼容 Pruning 框架 | 推荐度 |
|------|-------------------|---------------|--------|-----------------|-----------|------------------|--------|
| **Octo** | ❌ 无，需自行 finetune | Shallow CNN (SmallStem16) | 93M | 256/cam | 高（JAX 环境 + finetune） | ⚠️ 可行但 token 是低级特征，科学价值低 | ★☆☆☆☆ |
| **CogACT** | ❌ 无官方（第三方有评估） | Fused GELU MLP | ~7B | 256 | 中（需 finetune） | ✅ 清晰的 projector→LLM 边界 | ★★★☆☆ |
| **RoboFlamingo** | ❌ 无（仅 CALVIN） | Perceiver Resampler + Gated Cross-Attn | 3B/9B | 64 | 高（需 finetune） | ⚠️ Cross-attn K/V pruning，非 prefix token | ★★☆☆☆ |
| **HPT** | ❌ 无（仅 MetaWorld） | Cross-Attention (16 queries) | 最大 1B | 16 | 高（需 finetune + 适配） | ⚠️ 仅 16 token，pruning 空间极小 | ★☆☆☆☆ |
| **Diffusion Policy** | ❌ 无官方 | ResNet-18 → 全局特征向量 | 20-40M | 0（无 token） | — | ❌ **不兼容**，无 token 表示 | ☆☆☆☆☆ |

### 二、广泛搜索发现的高价值候选

| 模型 | LIBERO Checkpoint | Connector 类型 | 参数量 | Vision Token 数 | 兼容 Pruning | 推荐度 |
|------|-------------------|---------------|--------|-----------------|-------------|--------|
| **VQ-VLA** | ✅ `VQ-VLA/openvla-7b-finetuned-libero-90` | DINOv2+SigLIP → MLP | ~7B | 256 | ✅ 与 OpenVLA 同架构 | ★★★★★ |
| **MiniVLA** | ✅ `Stanford-ILIAD/minivla-libero90-prismatic` | Fused ViT → MLP | ~1B | 256 | ✅ 标准 VLA 架构 | ★★★★★ |
| **VLA-Adapter** | ✅ `VLA-Adapter/LIBERO-Long` 等 4 suite | Prismatic → Bridge Attention | ~0.5B | 256 | ✅ 有显式 vision token | ★★★★☆ |
| **pi0/pi0.5** | ✅ `lerobot/pi05_libero_finetuned` | SigLIP → Gemma-2B | ~3.3B | ~256 | ⚠️ 非标准（Action Expert 独立解码器） | ★★★☆☆ |
| **X-VLA** | ✅ `lerobot/xvla-libero` | Soft-prompted Transformer | 未明确 | 未明确 | ⚠️ 架构非标准 | ★★★☆☆ |
| **Spatial-Forcing** | ✅ GitHub 有 checkpoint | OpenVLA + 3D alignment | ~7B | 256 | ✅ OpenVLA 基础 | ★★★★☆ |

### 三、直接竞品（token compression 方向）

| 竞品 | 方法 | 状态 |
|------|------|------|
| **LightVLA** (ICRA 2026) | Gumbel-softmax differentiable token pruning，cross-attn between visual/text tokens | GitHub: `LiAutoAD/LightVLA`，有 LIBERO checkpoint，FLOPs↓59.1%，latency↓38.2% |
| **VLA-IAP** | Training-free visual token pruning via interaction alignment | arXiv:2603.22991 |
| **Compressor-VLA** | Instruction-guided visual token compression | arXiv:2511.18950 |

### 四、详细分析

**Octo** — JAX/Flax 实现，浅层 CNN 而非 ViT，93M 小模型。Token 是低级 patch 特征，不是语义丰富的 ViT token。需要从头 finetune LIBERO。科学价值和实用价值都低，**不推荐**。

**CogACT** — 基于 Prismatic-7B（DINOv2+SigLIP+LLaMA2-7B），架构与 OpenVLA 高度相似，256 visual tokens，代码中有显式 `num_patch` 追踪。第三方已在 LIBERO 上评估（90-98%）。需自行 finetune 但架构完全兼容 pruning 框架。如果愿意花时间 finetune，是好候选。

**RoboFlamingo** — Perceiver Resampler 输出 64 token 作为 cross-attention K/V（非 prefix token）。Pruning 需要修改 cross-attn K/V 而非删除序列 token，与我们现有框架不同。无 LIBERO checkpoint。**不推荐**。

**HPT** — 仅 16 vision token，pruning 空间极小。无 LIBERO 支持。backbone 是 policy transformer 而非 LLM。**不推荐**。

**Diffusion Policy** — 根本没有 vision token，ResNet-18 输出全局特征向量做 FiLM conditioning。架构层面**完全不兼容**。

**VQ-VLA** ⭐ — 基于 OpenVLA（DINOv2+SigLIP → MLP → LLaMA2-7B），改进了 action tokenizer（Residual VQ-VAE）。HF 上有 LIBERO-90 checkpoint。与 OpenVLA 同架构，pruning 框架可直接复用。ICCV 2025。**强烈推荐**。

**MiniVLA** ⭐ — Prismatic VLM 缩小到 ~1B 参数，HF 上有 LIBERO-90 checkpoint（多个变体）。标准 vision encoder → connector → LLM 架构。参数量小意味着可以快速验证 pruning 在不同模型规模上的效果。**强烈推荐**。

**VLA-Adapter** — Qwen2.5-0.5B 做 backbone，非常轻量。有全部 4 个 LIBERO suite 的 checkpoint。Bridge Attention 模块是非标准 connector，需要确认 pruning 干预点。**推荐**。

**pi0.5** — SigLIP → Gemma-2B → 独立 Action Expert 解码器。架构非标准（action 不是 LLM 自回归输出），但 visual token 确实经过 LLM，可以在 LLM 输入前 pruning。有 LIBERO checkpoint。**值得考虑**。

### 五、最终推荐（按优先级）

增加样本量最高效的路径：

1. **VQ-VLA** — 与 OpenVLA 同架构，有 LIBERO checkpoint，pruning 框架可直接复用，setup 时间最短（~2h）
2. **MiniVLA** — 1B 参数，有 LIBERO checkpoint，提供不同模型规模的数据点
3. **VLA-Adapter** — 0.5B，有全部 4 suite checkpoint，进一步丰富规模多样性
4. **CogACT** — 7B，架构兼容，但需自行 finetune LIBERO（~1-2 天）
5. **pi0.5** — 3.3B，有 LIBERO checkpoint，但架构非标准需验证兼容性

前 3 个模型都有现成 LIBERO checkpoint 且架构兼容，加上已有的 OpenVLA 和 SmolVLA，可以把样本量从 N=4 提升到 **N=7+**。

### 六、竞品警示

**LightVLA** 是直接竞品（ICRA 2026），已经做了 differentiable token pruning 并有 LIBERO 结果。需要仔细阅读并在 related work 中讨论差异化。VLA-IAP 和 Compressor-VLA 也是同方向工作，建议尽快拉取论文确认技术路线的区分度。

---

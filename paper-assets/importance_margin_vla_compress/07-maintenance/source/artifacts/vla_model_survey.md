# VLA 模型全面调研报告

> 调研日期：2026-05-20（更新版）
> 目标：为论文 "Vision Connectors and VLA Token Compressibility" 寻找更多不同 connector 架构的 VLA 模型

## 已有实验数据

| 模型 | Connector 类型 | 压缩行为 |
|------|---------------|----------|
| SmolVLA | Pixel-shuffle + MLP | Cliff-edge collapse (k=0.95 → 0% SR) |
| OpenVLA | 2-layer MLP projector (Prismatic) | Graded degradation (线性下降) |
| RoboFlamingo | Perceiver Resampler + Cross-attention | 训练失败（gripper loss 无法收敛） |

---

## 完整模型调研表

### 1. Octo (UC Berkeley, 2024)

| 字段 | 信息 |
|------|------|
| 参数量 | 27M (Small) / 93M (Base) |
| Vision encoder | Shallow CNN（从头训练，非预训练 ViT） |
| **Connector** | **CNN patch encoder → 直接拼接** — 无独立 connector，image patches (16×16) 直接拼入 transformer 序列 |
| LLM backbone | 纯 transformer（非预训练 LLM），语言用 T5 encoder |
| 开源 | ✅ GitHub: [octo-models/octo](https://github.com/octo-models/octo), HF: rail-berkeley/octo-base |
| LIBERO | ✅ fine-tune 后 ~72% SR |
| 改造成本 | 低 |
| 备注 | 非标准 VLM→LLM 架构，是 transformer-based diffusion policy。Action head 是 diffusion policy。 |

### 2. CogACT (Microsoft/Tsinghua, 2024)

| 字段 | 信息 |
|------|------|
| 参数量 | ~7.1B (7B Prismatic + 89-300M DiT action module) |
| Vision encoder | DINOv2 + SigLIP (双 encoder，channel concat) |
| **Connector** | **2-layer MLP projector** — 与 OpenVLA 相同（Prismatic 架构） |
| LLM backbone | Llama-2 7B (via Prismatic-7B) |
| 开源 | ✅ GitHub: [microsoft/CogACT](https://github.com/microsoft/CogACT), HF: CogACT/CogACT-Base |
| LIBERO | 需改造（paper 用 SimplerEnv + 真机） |
| 改造成本 | 中 |
| 备注 | 创新在 DiT action module。Connector 与 OpenVLA 相同。 |

### 3. HPT (MIT, NeurIPS 2024)

| 字段 | 信息 |
|------|------|
| 参数量 | 3.1M–1.1B (5 个 size) |
| Vision encoder | 预训练冻结 ResNet18 |
| **Connector** | **Cross-attention tokenizer** — learnable tokens 通过 cross-attention (8 heads) 聚合 vision features → 固定 16 tokens，每 camera view 独立 MLP projector |
| LLM backbone | 无（decoder-only transformer 从头训练） |
| 开源 | ✅ GitHub: [liruiw/HPT](https://github.com/liruiw/HPT), HF: liruiw/hpt |
| LIBERO | 未确认 |
| 改造成本 | 中（非 VLM 架构） |
| 备注 | 非标准 VLM→LLM 架构。Cross-attention tokenizer 类似轻量 Perceiver。跨 embodiment 预训练。 |

### 4. RT-2-X (Google DeepMind, 2023)

| 字段 | 信息 |
|------|------|
| 参数量 | 55B |
| Vision encoder | ViT (PaLI-X) |
| **Connector** | 未公开 |
| LLM backbone | PaLI-X / PaLM-E |
| 开源 | ❌ **闭源** |
| LIBERO | 不可行 |
| 备注 | 闭源，无法使用 |

### 5. GR-1 (ByteDance, 2023)

| 字段 | 信息 |
|------|------|
| 参数量 | 未明确 |
| Vision encoder | MAE ViT-Base (预训练) |
| **Connector** | **Perceiver Resampler** — 将 MAE ViT visual tokens 压缩为固定数量 + linear layers 对齐维度 |
| LLM backbone | GPT-style causal transformer，语言用 CLIP text encoder |
| 开源 | ✅ GitHub: [bytedance/GR-1](https://github.com/bytedance/GR-1), Apache-2.0 |
| LIBERO | 需改造（paper 只有 CALVIN: 94.9%） |
| 改造成本 | 高（视频生成 + action 架构需适配） |
| 备注 | 同时做视频预测和动作预测。使用 Perceiver Resampler。 |

### 6. GR-2 (ByteDance, 2024)

| 字段 | 信息 |
|------|------|
| 开源 | ❌ **未开源** |
| 备注 | GR-1 后续，代码/权重未释放，不可用 |

### 7. LLARVA (2024)

| 字段 | 信息 |
|------|------|
| 参数量 | 7B |
| Vision encoder | CLIP ViT-L/14 |
| **Connector** | **MLP projector** — LLaVA-style 2-layer MLP with GELU |
| LLM backbone | Llama-2 7B |
| 开源 | ✅ GitHub: [Dantong88/LLARVA](https://github.com/Dantong88/LLARVA), Apache-2.0 |
| LIBERO | 需改造 |
| 改造成本 | 中 |
| 备注 | 预测 visual traces。Connector 与 OpenVLA 类似。 |

### 8. RoboVLMs (2024) — 框架

| 字段 | 信息 |
|------|------|
| 参数量 | 不定 |
| **Connector** | 取决于所选 VLM（框架支持多种） |
| 开源 | ✅ GitHub: [Robot-VLAs/RoboVLMs](https://github.com/Robot-VLAs/RoboVLMs) |
| 备注 | VLA 实验框架，非单一模型。8+ VLM backbone × 4 policy 架构。 |

### 9. 3D-VLA (UMass, ICML 2024)

| 字段 | 信息 |
|------|------|
| Vision encoder | 3D feature extraction (点云) |
| **Connector** | **Interaction tokens** — 3D-LLM 架构 |
| 开源 | ✅ GitHub: [UMass-Embodied-AGI/3D-VLA](https://github.com/UMass-Embodied-AGI/3D-VLA) |
| LIBERO | 需大量改造（paper 用 RLBench） |
| 改造成本 | 高（3D 点云 vs 2D 图像差异大） |
| 备注 | 基于 3D 点云，与 2D VLA 差异太大，不推荐 |

### 10. π0 / pi-zero (Physical Intelligence, 2024-2025) ⭐

| 字段 | 信息 |
|------|------|
| 参数量 | ~3.3B (400M SigLIP + 2.6B Gemma + ~300M action expert) |
| Vision encoder | SigLIP-So400m (400M params) |
| **Connector** | **Linear projection** — 单层线性层，SigLIP output → Gemma embedding space |
| LLM backbone | Gemma 2B (via PaliGemma) |
| 开源 | ✅ GitHub: [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi), HF 有 PyTorch port |
| LIBERO | ✅ LIBERO-PRO 中有评测 |
| 改造成本 | 低 |
| 备注 | Action expert via MoE 架构 + flow matching。**Linear projection 是最简单的 connector**。 |

### 11. OpenVLA-OFT (Stanford, 2025)

| 字段 | 信息 |
|------|------|
| 参数量 | 7B |
| Vision encoder | SigLIP + DINOv2 (Prismatic) |
| **Connector** | **2-layer MLP projector** — 与 OpenVLA 相同 |
| LLM backbone | Llama-2 7B |
| 开源 | ✅ GitHub: [moojink/openvla-oft](https://github.com/moojink/openvla-oft) |
| LIBERO | ✅ 97.1% SR (SOTA) |
| 改造成本 | 极低 |
| 备注 | 同 connector 不同 action head（continuous + chunking + bidirectional attention） |

### 12. RoboMM (2024) ⭐

| 字段 | 信息 |
|------|------|
| 参数量 | 未明确 |
| Vision encoder | CLIP (via OpenFlamingo) |
| **Connector** | **3D Perception Adapter (UVFormer) + Cross-attention** — OpenFlamingo 风格：text queries attend to visual features through cross-attention layers in decoder |
| LLM backbone | OpenFlamingo (cross-attention decoder) |
| 开源 | ✅ GitHub: [RoboUniview/RoboMM](https://github.com/RoboUniview/RoboMM) |
| LIBERO | ✅ 90.7% SR |
| 改造成本 | 低-中 |
| 备注 | Cross-attention 融合方式与 projection-based connectors 根本不同 |

### 13. SpatialVLA (RSS 2025) ⭐

| 字段 | 信息 |
|------|------|
| 参数量 | ~4B |
| Vision encoder | SigLIP |
| **Connector** | **Linear projection + Ego3D Position Encoding** — PaliGemma2 的 linear projection + MLP(sinusoidal(3D positions)) 叠加到 visual tokens |
| LLM backbone | Gemma (via PaliGemma2) |
| 开源 | ✅ GitHub: [SpatialVLA/SpatialVLA](https://github.com/SpatialVLA/SpatialVLA), HF: IPEC-COMMUNITY/spatialvla-4b-224-pt |
| LIBERO | 未确认 |
| 改造成本 | 中 |
| 备注 | 本质 linear projection（与 π0 相同基础），加了 3D spatial encoding。Adaptive Action Grids 只输出 3 个 action token。 |

### 14. DeeR-VLA (2024) ⭐

| 字段 | 信息 |
|------|------|
| 参数量 | 3B / 9B (OpenFlamingo 变体) |
| Vision encoder | CLIP ViT-L/14 (428M params) |
| **Connector** | **Perceiver Resampler + Cross-attention** — OpenFlamingo 架构：CLIP features → Perceiver Resampler → learnable cross-attention blocks 注入 LLM 层间 |
| LLM backbone | MPT-1B (3B 版) / MPT-7B (9B 版) |
| 开源 | ✅ GitHub: [yueyang130/DeeR-VLA](https://github.com/yueyang130/DeeR-VLA) |
| LIBERO | 需改造（paper 只有 CALVIN） |
| 改造成本 | 中-高 |
| 备注 | 与 RoboFlamingo 同源（OpenFlamingo）。动态 early exit。 |

### 15. TraceVLA (UMD, ICLR 2025)

| 字段 | 信息 |
|------|------|
| 参数量 | 7B (OpenVLA-based) / 4B (Phi-3-Vision) |
| Vision encoder | SigLIP + DINOv2 (OpenVLA 版) |
| **Connector** | **2-layer MLP projector** — 与 OpenVLA 相同 |
| LLM backbone | Llama-2 7B / Phi-3 4B |
| 开源 | ✅ GitHub: [umd-huang-lab/tracevla](https://github.com/umd-huang-lab/tracevla), HF: furonghuang-lab/tracevla_7b, MIT |
| LIBERO | 未确认（SimplerEnv + 真机） |
| 备注 | Connector 与 OpenVLA 相同。Visual trace prompting 是输入增强。 |

### 16. X-VLA (ICLR 2026) ⭐

| 字段 | 信息 |
|------|------|
| 参数量 | 0.9B |
| Vision encoder | Florence-Large |
| **Connector** | **Linear projection + Soft Prompts** — vision features 通过 lightweight linear layer 投影 + 每 embodiment 有 learnable prompt embeddings 注入 transformer |
| LLM backbone | Standard transformer 24 layers (Florence 初始化) |
| 开源 | ✅ GitHub: [2toinf/X-VLA](https://github.com/2toinf/X-VLA), HF: 2toINF/X-VLA, Apache-2.0 |
| LIBERO | ✅ 98% SR，已有训练好的 LIBERO 权重 |
| 改造成本 | 极低 |
| 备注 | Flow matching action generation。0.9B 小模型，实验成本最低。 |

### 17. ECoT (2024)

| 字段 | 信息 |
|------|------|
| 参数量 | 7B (基于 OpenVLA) |
| **Connector** | **2-layer MLP projector** — 与 OpenVLA 相同 |
| 开源 | ✅ GitHub: [MichalZawalski/embodied-CoT](https://github.com/MichalZawalski/embodied-CoT), HF: ecot-openvla-7b |
| 备注 | Connector 与 OpenVLA 完全相同。Chain-of-thought 是推理增强。 |

### 18. LingBot-VLA (Ant Group/Robbyant, 2026)

| 字段 | 信息 |
|------|------|
| 参数量 | 4B |
| Vision encoder | Qwen2.5-VL 的 ViT (2D-RoPE + window attention) |
| **Connector** | **MLP merger** — 2×2 spatial grouping → 2-layer MLP (ReLU) 投射 + LLM decoder 中 cross-attention 融合 visual features |
| LLM backbone | Qwen2.5-VL-3B |
| 开源 | ✅ GitHub: [Robbyant/lingbot-vla](https://github.com/Robbyant/lingbot-vla) |
| LIBERO | 未确认 |
| 改造成本 | 中 |
| 备注 | MLP merger 是混合型 connector：空间合并（类似 pixel-shuffle）+ MLP 投射 + cross-attention。Mixture of Transformers 架构。 |

---

## Connector 类型覆盖分析

### 已有类型
| Connector 类型 | 模型 | 状态 |
|---------------|------|------|
| Pixel-shuffle | SmolVLA | ✅ 有数据 |
| 2-layer MLP projector | OpenVLA | ✅ 有数据 |
| Perceiver Resampler | RoboFlamingo | ❌ 训练失败 |

### 可新增类型（按优先级排序）

| 优先级 | Connector 类型 | 推荐模型 | 特点 |
|--------|---------------|----------|------|
| ⭐⭐⭐ | **Linear projection** | π0, X-VLA, SpatialVLA | 最简单 connector：单层线性变换，无非线性激活 |
| ⭐⭐⭐ | **Perceiver Resampler** (重试) | DeeR-VLA | 与 RoboFlamingo 同架构基础，但已验证可训练 |
| ⭐⭐ | **Cross-attention** (Flamingo-style) | RoboMM | 不在 encoder 端投射，decoder 端动态选择融合 |
| ⭐ | **MLP merger + spatial grouping** | LingBot-VLA | 混合型：空间合并 + MLP + cross-attention |
| ⭐ | **CNN patch direct concat** | Octo | 无独立 connector，但非 VLM 架构 |

### 关键发现

1. **大量模型共享 MLP projector**：OpenVLA, CogACT, LLARVA, TraceVLA, ECoT, OpenVLA-OFT 都用 Prismatic/LLaVA 的 2-layer MLP — 这个类型已覆盖
2. **Linear projection 是第二常见但尚未测试的类型**：π0 (PaliGemma) 和 X-VLA 都用单层 linear — 与 2-layer MLP 形成有意义的对比
3. **Perceiver Resampler 值得第二次尝试**：DeeR-VLA 证明了 OpenFlamingo 架构在 robot 任务上可行（CALVIN benchmark 正常工作），RoboFlamingo 的失败可能是实现层面的问题
4. **Cross-attention connector** (RoboMM) 从根本上不同于所有 projection-based 方案

---

## Top 5 推荐（按优先级排序）

### 🥇 1. π0 (Physical Intelligence)
- **Connector**: Linear projection (单层线性)
- **理由**: 与 OpenVLA 的 2-layer MLP 直接对比。开源 + LIBERO 评测已有。3B 参数单卡可跑。
- **预期**: Linear projection 不增加非线性 → token 保留更多 raw visual feature 结构 → 压缩曲线可能不同

### 🥈 2. X-VLA
- **Connector**: Linear projection + soft prompts
- **理由**: 同为 linear projection，可验证一致性。**LIBERO 98% + 已有权重直接可用。0.9B 参数实验成本最低。**
- **预期**: 与 π0 对比看 soft prompt 是否影响压缩行为

### 🥉 3. DeeR-VLA
- **Connector**: Perceiver Resampler + Cross-attention (OpenFlamingo)
- **理由**: 给 Perceiver Resampler 第二次机会。DeeR-VLA 在 CALVIN 上已验证可训练。
- **风险**: LIBERO 需自行改造
- **预期**: Perceiver 本身就做 attention-based compression → 可能展现独特压缩模式

### 4. RoboMM
- **Connector**: Cross-attention (OpenFlamingo) + 3D Adapter
- **理由**: Cross-attention 融合方式与所有 projection-based 根本不同。已有 LIBERO 90.7%。
- **风险**: 3D adapter 增加变量
- **预期**: Decoder 端动态融合 → 可能对 token pruning 有完全不同的响应

### 5. OpenVLA-OFT
- **Connector**: 2-layer MLP projector (与 OpenVLA 相同)
- **理由**: 同 connector + 不同 action head → 隔离 "action head 对压缩行为的影响"。LIBERO 97.1%。代码直接可用。
- **预期**: 作为 controlled comparison，看 continuous action + chunking 是否改变压缩曲线

---

## 不推荐模型

| 模型 | 排除原因 |
|------|----------|
| RT-2-X | 闭源 |
| GR-2 | 未开源 |
| 3D-VLA | 3D 点云，与 2D VLA 差异太大 |
| CogACT | Connector 与 OpenVLA 相同（Prismatic MLP） |
| LLARVA | Connector 类似 OpenVLA（MLP projector） |
| TraceVLA | Connector 与 OpenVLA 相同 |
| ECoT | Connector 与 OpenVLA 相同 |
| HPT | 非 VLM 架构 |
| GR-1 | 有 Perceiver Resampler（有价值），但无 LIBERO + 改造成本高 |
| Octo | 无独立 connector，非 VLM 架构 |

---

## Connector 类型 × 模型最终矩阵

| Connector 类型 | 已有模型 | 推荐新增 | 达成后状态 |
|---------------|----------|----------|-----------|
| Pixel-shuffle | SmolVLA ✅ | — | ✅ |
| 2-layer MLP projector | OpenVLA ✅ | OpenVLA-OFT (同 connector 不同 action head) | ✅+ |
| Perceiver Resampler + Cross-attn | RoboFlamingo ❌ | **DeeR-VLA** | ✅ (重试) |
| **Linear projection** | — | **π0, X-VLA** | ✅ (新增) |
| **Cross-attention (decoder-side)** | — | **RoboMM** | ✅ (新增) |

**实现全部推荐后**: 5 种 connector 类型 × 7 个模型，全面覆盖主流 VLA connector 架构。

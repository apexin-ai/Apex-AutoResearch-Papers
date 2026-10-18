# research deep analysis competitors

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_deep_analysis_competitors_20260519T013824_result.json`
- **Structured JSON:** [`7244901b9ea7823dadbd.json`](../../sessions/72/7244901b9ea7823dadbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

四篇论文分析完成。以下是完整结构化报告。

---

## 1. Compressor-VLA (arXiv 2511.18950)

### A. VLA 模型
- **基础模型**: OpenVLA-OFT (LLaMA-2-7B + DINOv2/SigLIP 双编码器), 512 visual tokens
- **对比模型**: CogACT, π0, SP-VLA, FastV, SparseVLM, SpecPrune-VLA, VLA-Cache
- **SmolVLA**: 未涉及

### B. Vision Connector
- 未分析不同 connector 类型对压缩的影响
- 提出的 compressor 本身使用 cross-attention (STC) + local windowed attention (SRC) 替代原始 projector

### C. 压缩机制
- **Training-required**: 150K steps, 8 GPUs, batch 64, LoRA rank 32
- **策略**: Reconstructive compression (非 pruning)
  - STC: 16 learnable queries + FiLM language conditioning → 16 global tokens
  - SRC: local window (w=2) downsampling → 144 local tokens
- **压缩比**: 512 → 160 tokens (3.2×), FLOPs 3.95T → 1.62T (59% reduction)

### D. LIBERO 数据

| Method | Spatial | Object | Goal | Long | Avg | FLOPs(T) | Tokens |
|--------|---------|--------|------|------|-----|----------|--------|
| OpenVLA-OFT | 97.6 | 98.4 | 97.9 | 94.5 | 97.1 | 3.95 | 512 |
| SP-VLA | 75.4 | 85.6 | 84.4 | 54.2 | 74.9 | 3.10 | 229 |
| FastV | 96.8 | 81.0 | 96.4 | 73.0 | 86.8 | 3.18 | 256 |
| SparseVLM | 96.8 | 94.2 | 97.6 | 93.6 | 95.6 | 3.04 | 256 |
| SpecPrune-VLA | 98.2 | 96.3 | 97.7 | 94.0 | 96.6 | 1.70 | 197 |
| VLA-Cache | 99.0 | 97.7 | 97.4 | 93.6 | 97.0 | 3.28 | 212 |
| **Compressor-VLA** | **98.8** | **99.2** | **96.4** | **94.8** | **97.3** | **1.62** | **160** |

- 4 suites × 10 tasks，50 demos/task
- **无 seed 报告、无 episode 数、无 error bars**

### E. 关键问题
| 问题 | 是否涉及 |
|------|---------|
| Cliff-edge 分析 | ❌ 未讨论（但 SP-VLA Long=54.2% 隐含了此现象） |
| Cross-architecture 对比 | ❌ 仅 OpenVLA-OFT |
| Re-encoding vs deletion | ❌ 无控制实验（概念上主张 reconstruction > pruning） |
| Closed-loop 评估 | ✅ LIBERO + Mobile ALOHA 实机 |

### F. 与我们的差异
- 工程贡献：一个更好的 compressor module。不分析 WHY compression fails
- 我们的 cliff-edge 发现、connector-dependent compressibility、re-encoding vs deletion 控制实验均完全缺失

---

## 2. SpecPrune-VLA (arXiv 2509.05614)

### A. VLA 模型
- **基础模型**: OpenVLA-OFT, π₀, UniVLA (SimplerEnv only)
- **SmolVLA**: 未涉及
- 未报告参数量

### B. Vision Connector
- 完全未分析 connector 类型。视觉编码器视为黑盒，只关注 LLM 层内的 attention pattern

### C. 压缩机制
- **Training-free**: 明确声明
- **两级剪枝**:
  1. Action-level Static Pruning: 前一步 attention 分数识别全局重要 tokens (K_global=30) + 帧间 patch 相似度 (K_dynamic=20) + 当前步前两层 attention (K_local=24)
  2. Layer-level Dynamic Pruning: attention entropy 逐层再剪 10%
  3. Action-Aware Controller: 末端执行器速度 → coarse/fine 动态调整剪枝力度
- **压缩比**: FLOPs 剩余 43% (OpenVLA-OFT), 48% (π₀); 加速 1.46-1.70×

### D. LIBERO 数据

| Method | Spatial | Object | Goal | Long | Avg | Speedup |
|--------|---------|--------|------|------|-----|---------|
| Baseline | 97.6 | 96.5 | 97.9 | 94.5 | 96.6 | 1.00× |
| **SpecPrune-VLA** | **97.4** | **95.8** | **97.7** | **93.4** | **96.1** | **1.46×** |
| FastV | 94.6 | 95.8 | 94.0 | 88.8 | 93.3 | 1.44× |
| EfficientVLA | 96.5 | 91.1 | 96.0 | 72.1 | 88.9 | 1.52× |

- π₀: 94.2% → 93.5% avg, 1.31× speedup
- **无 seed、无 episode 数、无 error bars**

### E. 关键问题
| 问题 | 是否涉及 |
|------|---------|
| Cliff-edge 分析 | ❌ Fig 7 显示 SR 平滑下降，未发现突变 |
| Cross-architecture 对比 | ❌ 两个模型都是 graceful degradation |
| Re-encoding vs deletion | ❌ 纯 deletion，无 re-encoding |
| Closed-loop 评估 | ✅ LIBERO + 真实机器人 |

### F. 与我们的差异
- 核心假设是 "所有 VLA 都可以被 token pruning 加速"。我们证明这在 pixel-shuffle connector 下完全不成立
- 工程优化论文 vs 我们的科学发现论文

---

## 3. LightVLA (arXiv 2509.12594)

### A. VLA 模型
- **基础模型**: 仅 OpenVLA-OFT (7B)
- **SmolVLA**: 仅作为 Table I 对比项 (88.8% avg)，未测试 LightVLA
- 对比: OpenVLA, CogACT, π0, π0-fast, NORA, WorldVLA 等

### B. Vision Connector
- OpenVLA-OFT 使用 MLP projector (3-layer, GELU)
- DINOv2 + SigLIP channel-wise concat 后经 MLP
- **未分析不同 connector 对压缩的影响**

### C. 压缩机制
- **Training-required**: 40K steps, 8× H20 GPU, batch 64
- **策略**: Differentiable token pruning via Gumbel-Softmax
  1. Query Generation: visual × language cross-attention 生成 query
  2. Token Scoring: query 对 visual tokens 打分
  3. Gumbel-Softmax 可微选择 + straight-through estimator
- **自适应压缩**: 不同 task/timestep 保留不同 token 数
- **压缩比**: 512 → 78 avg (84.8% reduction), FLOPs 8.8T → 3.6T (59.1%)

### D. LIBERO 数据

| Method | Spatial | Object | Goal | Long | Avg | Tokens |
|--------|---------|--------|------|------|-----|--------|
| OpenVLA-OFT* | 97.6 | 94.2 | 95.2 | 92.0 | 94.8 | 512 |
| **LightVLA** | **98.4** | **98.4** | **98.2** | **94.6** | **97.4** | **78±11** |
| SmolVLA (ref) | 93.0 | 94.0 | 91.0 | 77.0 | 88.8 | — |

- 10 tasks/suite, 500 demos training, 50 trials/task
- **无 seed、无 error bars**（仅 token 数量有标准差）

### E. 关键问题
| 问题 | 是否涉及 |
|------|---------|
| Cliff-edge 分析 | ❌ 消融在 96.6-97.4% 范围，未见突变 |
| Cross-architecture 对比 | ❌ 仅 OpenVLA-OFT |
| Re-encoding vs deletion | ❌ 纯 deletion (hard selection) |
| Closed-loop 评估 | ✅ LIBERO closed-loop |

### F. 与我们的差异
- 单架构效率优化。我们的 architecture-dependent compressibility 发现完全空白
- LightVLA 恰好只在 MLP projector 的"安全"架构上实验，避开了 cliff-edge

---

## 4. See What Matters / GridS (arXiv 2605.11817, ICML 2026)

### A. VLA 模型
- **基础模型**: π0 (~3B), π0.5, SmolVLA (~450M)
- **SmolVLA**: ✅ 包含，但仅用于真实机器人实验 (SO-100 arm)，LIBERO 仅有 baseline 数据
- 对比: OpenVLA, CogACT, OpenVLA-OFT

### B. Vision Connector
- π0 使用 PaliGemma projector; SmolVLA 使用 interleaved cross-attention
- **未分析 connector 类型差异对压缩的影响**
- "pixel-shuffle" 未出现在论文中

### C. 压缩机制
- **Training-required**: joint fine-tuning 30K-50K steps
- **策略**: Differentiable Grid Sampler (GridS)
  1. Global pooling → context vector → MLP 预测 K 个连续坐标 P ∈ [0,1]^(K×2)
  2. Bilinear interpolation 从四邻近 patch 采样特征（可微）
  3. Coordinate Encoder 注入位置信息
- **压缩比**: 256 → 16 tokens (93.75%), 或 → 4 tokens (98.4%); FLOPs 216G → 51.6G (76%)
- 训练加速 3.4× (π0)

### D. LIBERO 数据 (π0)

| Method | Spatial | Object | Goal | Long | Avg |
|--------|---------|--------|------|------|-----|
| π0 baseline | 97.2 | 98.8 | 96.0 | 85.6 | 94.4 |
| **GridS-16** | **98.0** | **99.2** | **96.4** | **90.2** | **96.0** |
| GridS-4 | — | — | — | — | 95.5 |

π0.5: 96.7% → 97.7% avg

SmolVLA LIBERO baseline: 79.0% avg（未测试 GridS+SmolVLA 的 LIBERO）

真实机器人 SmolVLA (64→16 tokens): Stack Cubes 从 7.6% → 60.0%

**无 error bars（LIBERO）**。ALOHA 实验报告了 3 seeds。

### E. 关键问题
| 问题 | 是否涉及 |
|------|---------|
| Cliff-edge 分析 | ⚠️ 部分：真实机器人 K=4 时 0% SR，但未系统分析机制 |
| Cross-architecture 对比 | ❌ 测试了 π0/π0.5/SmolVLA 但未比较其压缩行为差异 |
| Re-encoding vs deletion | ❌ 无控制实验（隐含 continuous resampling > discrete deletion） |
| Closed-loop 评估 | ✅ LIBERO + ALOHA + SO-100 |

### F. 与我们的差异
- GridS 说"pruning 丢失几何信息，所以 resample"（方案论文）
- 我们说"pruning 能否 work 取决于 connector 架构，我们解释 why"（诊断/理解论文）
- GridS 测试了 SmolVLA 但未在 LIBERO 上做压缩实验，且未分析 pixel-shuffle 的 cliff-edge
- **风险**: 审稿人可能要求与 GridS 对比。应 frame 为 orthogonal（我们的分析解释了 GridS 为什么在某些架构上必要）

---

## 总结对比表

| 维度 | Compressor-VLA | SpecPrune-VLA | LightVLA | GridS (See What Matters) | **我们的工作** |
|------|---------------|---------------|----------|--------------------------|-------------|
| **Training** | Required (150K) | Free | Required (40K) | Required (30-50K) | **Free + Re-encoding** |
| **基础 VLA** | OpenVLA-OFT | OpenVLA-OFT, π₀ | OpenVLA-OFT | π0, π0.5, SmolVLA | **SmolVLA, OpenVLA** |
| **含 SmolVLA** | ❌ | ❌ | ❌ (仅对比) | ✅ (仅真实机器人) | **✅ (核心)** |
| **Connector 分析** | ❌ | ❌ | ❌ | ❌ | **✅ pixel-shuffle vs MLP vs cross-attn** |
| **压缩策略** | Reconstruction | Deletion | Deletion (learned) | Continuous resampling | **Deletion + Re-encoding 对比** |
| **Token 压缩比** | 512→160 (3.2×) | ~60-70% reduction | 512→78 (6.6×) | 256→16 (16×) | **多级对比** |
| **Cliff-edge 分析** | ❌ | ❌ | ❌ | ⚠️ 部分 | **✅ 核心发现** |
| **Cross-architecture** | ❌ | ❌ | ❌ | ❌ | **✅ 核心贡献** |
| **Re-encoding vs deletion** | ❌ | ❌ | ❌ | ❌ | **✅ 控制实验** |
| **Closed-loop eval** | ✅ | ✅ | ✅ | ✅ | **✅** |
| **Error bars** | ❌ | ❌ | ❌ | ❌ (LIBERO) | **✅ Wilson CI, multi-seed** |
| **LIBERO suites** | 4/4 | 4/4 | 4/4 | 4/4 | **4/4** |

### 我们的独特贡献 vs 全部 4 篇

1. **Cliff-edge 发现**: 4 篇论文中无一系统分析 pixel-shuffle connector 下 token deletion → 0% SR 的突变现象。这是全新发现。

2. **Architecture-dependent compressibility**: 所有 4 篇都在"安全"架构上实验（MLP projector 或 flow-matching），未探索 connector 类型如何决定压缩可行性边界。

3. **Re-encoding vs deletion 控制实验**: 4 篇中无一做过严格的控制对比。Compressor-VLA 和 GridS 隐含支持 re-encoding，但缺乏隔离变量的实验。

4. **SmolVLA 深度分析**: SmolVLA 仅在 GridS 真实机器人实验中出现，LIBERO 压缩实验中无人测试 SmolVLA。我们是第一个在 SmolVLA 上做系统性 token 压缩分析的工作。

5. **实验严谨性**: 4 篇均无 error bars（LIBERO），我们有 multi-seed + Wilson confidence interval。

6. **科学 vs 工程**: 4 篇都是"提出更好的压缩方法"，我们是"解释为什么压缩在某些架构上根本不可行"——complementary but distinct contribution。

---

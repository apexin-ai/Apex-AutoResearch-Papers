# C5 RoboFlamingo 可行性调研报告

> 日期: 2026-05-19 | CoRL abstract: May 26 (7d) | CoRL paper: May 29 (10d)

## 1. 架构总结

**RoboFlamingo** ([arXiv:2311.01378](https://arxiv.org/abs/2311.01378), [GitHub](https://github.com/RoboFlamingo/RoboFlamingo)) 基于 OpenFlamingo，是第三种 vision connector 架构。

| 组件 | 规格 |
|------|------|
| Vision encoder | CLIP ViT-L/14 (frozen), 224×224, 输出 257 tokens (256 patches + CLS), dim=1024 |
| **Vision connector** | **Perceiver Resampler**: 64 learnable queries, depth=6, heads=8, dim=1024 → 输出 **(64, 1024)** per image |
| LLM | MPT-1B (d=2048, 24 layers), gated cross-attention every layer |
| Action decoder | LSTM (hidden=1024, 4 layers) → 7-DoF continuous (6D EE + 1D gripper) |
| 训练设置 | 8×A100-80GB, batch=6, lr=1e-4, 5 epochs, frozen ViT + trainable Perceiver + cross-attn + LSTM |

**Perceiver Resampler 工作机制**: 64 个 learnable query tokens 通过 cross-attention 聚合所有 257 个 ViT patch features。每个 output token 是对全局视觉特征的加权汇总（many-to-many mapping），与 pixel-shuffle 的 bijective spatial mapping 和 MLP projector 的 1:1 per-patch mapping 形成三种截然不同的 connector 范式。

### 三种 Connector 架构对比

| Connector | 代表模型 | 机制 | Output tokens | 空间局部性 | 预测压缩行为 |
|-----------|---------|------|---------------|-----------|-------------|
| Pixel-shuffle | SmolVLA | 空间折叠 (r×r patches → 1 token) | 64 (per cam) | 强局部 (bijective) | Cliff-edge ✅已验证 |
| MLP projector | OpenVLA | 逐 patch 线性映射 | 256 | 保留 (1:1) | Graded degradation ✅已验证 |
| **Perceiver Resampler** | **RoboFlamingo** | **Learned cross-attention queries** | **64** | **无 (global summary)** | **Graded, 可能比 MLP 更 robust** |

## 2. LIBERO 适配方案

**现状**: 无现成 RoboFlamingo-LIBERO 适配。RoboFlamingo 原始仅支持 CALVIN。

**适配可行性: 高。** 关键兼容性：

| 方面 | CALVIN (原始) | LIBERO (目标) | 适配难度 |
|------|-------------|-------------|---------|
| Action space | 7-dim relative EE (euler) | 7-dim relative EE (axis-angle) | ⬤ 低：维度一致，仅 orientation repr 不同 |
| Camera | static (200×200) + gripper (84×84) | agentview (256×256) + eye_in_hand (256×256) | ⬤ 低：直接映射 + resize |
| Data format | .npz per timestep | HDF5 per task | ⬤⬤ 中：需写 DiskLiberoDataset |
| Proprio state | 15-dim robot_obs | 8-9 dim | ⬤ 低：adjust input dim |
| Evaluation | PyBullet | robosuite/MuJoCo | ⬤⬤ 中：新 eval loop |

**具体工作**:
1. **数据加载器** (~300 LOC): HDF5 读取 → sliding window → (images, state, actions, language)
2. **Eval pipeline** (~200 LOC): LIBERO env API → feed observations → step actions → track SR
3. **Action normalization**: 从 LIBERO demos 重新计算 mean/std
4. **模型架构**: 零修改。Perceiver (64 tokens), cross-attn, LSTM head 全部复用

## 3. Perceiver Resampler 的 Token 压缩特性

### 预测：第三种 degradation pattern

**理论分析**: Perceiver Resampler output 的每个 token 通过 cross-attention 聚合了全部 257 个 ViT features。移除一个 token 不会像 pixel-shuffle 那样产生 "spatial hole"，而是损失一个 learned "aspect"。信息分布在多个 tokens 间有冗余。

**已有证据**:
- Flamingo 论文: 64→32 queries, "satisfactory performance" (small drop)
- MQT (NeurIPS 2024): 256→16 tokens 仅 -2.4 points on MMBench; **2 tokens 仍可工作** (ScienceQA -3%)
- Dynamic Query Selection: 64→32 halves inference time, minimal accuracy loss

**预测**: RoboFlamingo pruning 将展现 **graded degradation**，可能比 OpenVLA (MLP) 更 robust，因为：
1. 每个 token 是 global summary，无 spatial hole
2. tokens 间有 cross-attention 导致的信息冗余
3. 但总 token 数少 (64 vs 256)，每个 token 信息密度更高

### 与 VTR 的关系

Perceiver Resampler 本身就是 learned re-encoding（与 VTC 结构几乎相同）。对其 output 再做 VTR 等于 **二次 re-encoding**。两种可能结果均有科学价值：
- VTR 有效 → 方法通用性成立
- VTR 无显著增益 → 说明 Perceiver 已完成 re-encoding，VTR 专门解决的是 entanglement 问题

## 4. 关键风险

| 风险 | 严重度 | 缓解方案 |
|------|--------|---------|
| **时间**: 10 天到 paper deadline | 🔴 高 | 最小可行实验：仅 baseline + pruning curve，不做 re-encoding |
| Baseline 性能不达标 | 🟡 中 | CALVIN 上 96.4% SR，但 LIBERO 结果未知；可能需要调参 |
| 模型规模太小 (1.3B) 导致不公平对比 | 🟡 中 | 与 SmolVLA (0.4B) 同量级，比 OpenVLA (7B) 小；论文中需承认 |
| RoboFlamingo 代码老旧 (2023.11) | 🟢 低 | 依赖简单 (OpenFlamingo + PyTorch)，无复杂框架依赖 |

## 5. 工作量评估

| 任务 | 时间 | GPU |
|------|------|-----|
| 代码适配 (dataloader + eval) | 1.5-2 天 | 无 |
| Fine-tune baseline on LIBERO-Object | 0.5-1 天 (2-4h training) | 1×96GB (westd-41074) |
| Pruning curve (k=1.0/0.9/0.7/0.5/0.3) | 0.5 天 | 1×96GB |
| (可选) VTR re-encoding | 1-2 天 | 1×96GB |
| **总计 (最小可行)** | **3-4 天** | **1 GPU** |
| **总计 (含 VTR)** | **5-6 天** | **1-2 GPU** |

代码适配难度: **3/5** (需要新 dataloader + eval pipeline，但无架构修改)

## 6. 建议: Conditional Go

**最小可行方案 (Go)**：仅做 baseline + pruning curve → 3-4 天，deadline 前可完成。即使只有 pruning 结果（无 re-encoding），已经为论文提供第三个 connector 数据点，强化 C1 (Architecture-Dependent Compressibility)。

**完整方案 (Stretch)**：baseline + pruning + VTR re-encoding → 5-6 天，极紧但理论上可行。

**No-go 条件**：
1. C4-ext (OpenVLA re-encoding) 失败需要 debug → bandwidth 不够
2. LIBERO baseline fine-tune 后 SR < 30% → 数据点无说服力
3. 代码适配遇到重大阻碍（OpenFlamingo 版本不兼容等）

**建议执行计划**:
- Day 1 (May 20): Clone repo, 写 LIBERO dataloader, 本地验证数据 pipeline
- Day 2 (May 21): 写 eval pipeline, 启动 baseline fine-tune on westd-41074:0
- Day 3 (May 22): Baseline eval, 启动 pruning experiments (5 个 k 值)
- Day 4 (May 23): 收集 pruning 结果, 更新论文 Table/Figure
- Day 5-6 (May 24-25): (可选) VTR re-encoding training + eval

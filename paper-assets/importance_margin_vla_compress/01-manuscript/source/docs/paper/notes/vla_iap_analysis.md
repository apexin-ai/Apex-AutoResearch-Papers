# VLA-IAP 方法详细分析
# Paper Agent 调研笔记 — 2026-05-17

## 论文信息
- **Title**: VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models
- **arXiv**: 2603.22991
- **Year**: 2026

## 测试模型
- OpenVLA-OFT (7B, Llama-2 backbone + SigLIP + DINOv2 vision encoder)
- π₀ / π₀.₅ (PaliGemma-based, diffusion policy)
- DreamVLA (ViT + CLIP + DiT-B)
- **注意：未测试 SmolVLA (451M)**

## 核心方法

### 1. Geometric Prior (几何先验)
- 使用 **Sobel edge detection** 在灰度图上提取边缘强度
- "Structural anchors" = 纹理稀疏但结构关键的区域（如操作物体边界）
- Token importance = patch 区域内的平均边缘强度，归一化到 [0,1]
- **完全绕过模型内部 attention**，使用外部视觉几何特征

### 2. Dynamic Scheduling (动态调度)
- 计算 semantic intent mask 和 physical motion mask 之间的 IoU
- **Conservative mode** (IoU ≤ threshold): 保留所有非纯背景 token
- **Aggressive mode** (IoU > threshold): 只保留语义核心 + 运动区域 token
- **关键设计**: 在不确定阶段几乎不剪枝，只在高置信度状态才激进剪枝

### 3. Interaction-First Paradigm
- 核心论点: 基于 attention 的剪枝继承并放大了模型的感知错误
- "If the pre-trained model overlooks geometric details due to lack of physical continuity, pruning based on attention scores inherits and amplifies these errors"

## 主要结果 (LIBERO, OpenVLA-OFT)

| Retention | Spatial | Object | Goal | Long | Avg SR | Speedup |
|-----------|---------|--------|------|------|--------|---------|
| 100% (baseline) | — | — | — | — | **97.1%** | 1.00× |
| 70% | 97.6% | 99.6% | 98.4% | 95.6% | **97.8%** | 1.25× |
| 50% | 97.3% | 99.1% | 98.2% | 95.2% | **97.5%** | 1.37× |
| 30% | 96.6% | 98.8% | 98.0% | 94.8% | **97.1%** | 1.54× |

- 评估方式: **Closed-loop** on LIBERO (所有 4 个 suite) + real robot
- 对比 baseline EfficientVLA 在 70% retention 下降到 88.9%

## 与我们工作的关键差异

| 维度 | 我们 (SmolVLA + ACIS) | VLA-IAP (OpenVLA-OFT) |
|------|----------------------|----------------------|
| 模型大小 | 451M | 7B (~15x 大) |
| 基线 SR | 44.8% | 97.1% |
| 剪枝方法 | 基于 attention 的 learned scorer | 基于外部几何先验 (Sobel edge) |
| 动态调度 | 无 (固定 k 比例) | 有 (conservative ↔ aggressive) |
| Vision encoder | SigLIP only | SigLIP + DINOv2 |
| 结果 | 0% SR under ANY pruning | 97.8% SR at 70% retention |

## 为什么 VLA-IAP 能成功？(推测)

1. **模型能力余量**: 97.1% baseline 意味着模型高度过拟合任务，有更大的容错空间
2. **动态调度回退**: 在不确定阶段保留全部 token，实际平均剪枝比例可能远低于标称值
3. **外部几何信号**: Sobel edge detection 不依赖模型内部 attention（可能更可靠）
4. **双 vision encoder**: SigLIP + DINOv2 提供冗余视觉特征（DINOv2 的信息可能弥补 SigLIP token 被剪枝的损失）
5. **模型规模**: 7B 模型的 LLM backbone 可能对输入扰动更鲁棒

## 其他 VLA 效率方法 (搜索中发现)

- **EfficientVLA** (2025): Layer pruning + token selection + caching on CogACT (7B). 0.6% SR drop, 1.93x speedup. Tested on SIMPLER (not LIBERO).
- **VLA-Pruner** (2025): Temporal-aware dual-level (semantic + action attention). Multiple architectures.
- **VLA-ADP**: Action-aware dynamic pruning.
- **VLA-Cache** (NeurIPS 2025): Temporal KV caching (not removal). 1.7x speedup.

## Related Work positioning 建议

VLA-IAP 的成功不矛盾我们的 cliff-edge finding:
1. 我们展示 naive/attention-based pruning 在 SmolVLA 上完全失败
2. VLA-IAP 的成功依赖: (a) 外部几何先验, (b) 动态调度, (c) 更大模型, (d) 更强基线
3. 这恰恰证实了我们的核心洞察: VLA token reduction 需要 domain-specific 方法，不能简单迁移 ViT 的 attention-based pruning

若论文方向转为 B (positive contribution):
- 在 SmolVLA 上实现 geometric prior + dynamic scheduling，测试是否能解决 cliff-edge
- 关键问题: SmolVLA 44.8% baseline 的低容错空间是否允许任何剪枝？

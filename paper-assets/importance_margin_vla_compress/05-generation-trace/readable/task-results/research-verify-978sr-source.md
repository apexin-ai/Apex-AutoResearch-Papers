# research verify 978sr source

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify_978sr_source_20260519T062742_result.json`
- **Structured JSON:** [`98102449d0711699b20d.json`](../../sessions/98/98102449d0711699b20d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 核实结果

### C359 数据点："CogACT retains 97.8% SR under 78% MLP-projector pruning"

**结论：97.8% 这个数字是错误的，与 EfficientVLA 的实际数据不符。**

---

### 1. EfficientVLA 中 CogACT 的真实数据

EfficientVLA (arXiv:2506.10100) 对 CogACT 做了 256→56 的视觉 token 压缩（**78% reduction — 这部分正确**），在 SIMPLER benchmark 上的结果：

| 设置 | Baseline SR | 压缩后 SR | **实际保留率** |
|------|-----------|---------|------------|
| Visual Matching | 74.8% | 74.2% | **99.2%** |
| Variant Aggregation | 61.3% | 61.2% | **99.8%** |

**97.8% 这个数字在 EfficientVLA 论文中不存在。** 实际保留率是 99.2%–99.8%。

### 2. 97.8% 的真正来源

97.8% 来自 **VLA-IAP** (arXiv:2603.22991)，但它是：
- **OpenVLA-OFT** 的绝对 SR（不是 CogACT）
- 在 **LIBERO** benchmark 上（不是 SIMPLER）
- **30% pruning** / 70% token retention（不是 78%）
- 1.25x speedup

完全不同的模型、benchmark 和 pruning ratio。

### 3. CogACT 原始论文

- **Title**: CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation
- **arXiv**: [2411.19650](https://arxiv.org/abs/2411.19650)
- **来源**: Microsoft Research, 2024年11月
- 架构：CogVLM backbone + MLP projector + Diffusion Action Transformer
- [项目页](https://cogact.github.io/) | [GitHub](https://github.com/microsoft/CogACT)

### 4. 错误性质

论文中的 claim 混合了两篇论文的数据：
- **78% token pruning** → 来自 EfficientVLA 对 CogACT 的实验（正确）
- **97.8%** → 来自 VLA-IAP 对 OpenVLA-OFT 的实验（张冠李戴）

### 5. 修正建议

两个选择：

**选项 A**：用 EfficientVLA 的真实数据（更好，因为实际保留率更高）
> "CogACT retains **99.2%** of its success rate under 78% token pruning"

**选项 B**：引用 VLA-IAP 的数据，但修正模型名称
> "OpenVLA-OFT retains 97.8% SR under 30% token pruning"

选项 A 更有利，因为 99.2% > 97.8%，论证力度更强。需要同时修改 `discussion.tex:13` 和 `analysis.tex:33` 两处。

Sources:
- [EfficientVLA (arXiv:2506.10100)](https://arxiv.org/abs/2506.10100)
- [VLA-IAP (arXiv:2603.22991)](https://arxiv.org/abs/2603.22991)
- [CogACT (arXiv:2411.19650)](https://arxiv.org/abs/2411.19650)

---

# research grids mechanism analysis

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_grids_mechanism_analysis_20260519T034002_result.json`
- **Structured JSON:** [`a3746ef7da15c33dd656.json`](../../sessions/a3/a3746ef7da15c33dd656.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have a complete picture. Here's the analysis:

---

## 关键判断

### Q1: 是否分析了 pixel-shuffle entanglement 机制？
**否** — 论文全文不包含 "pixel shuffle"、"space-to-depth"、"token entanglement"、"spatial mixing"、"cliff-edge" 中的任何一个术语。他们完全没有讨论 vision connector 的设计如何影响 token compression 的可行性。他们对 token pruning 失败的解释是：

- discrete selection 导致 quantization error（丢失 sub-patch precision）
- semantic pruning 忽略 geometrically critical regions（如 contact points）
- training-free 方法无法 align with task requirements

这些都是**通用层面**的批评，不涉及任何 architecture-specific 的机制分析。

### Q2: 是否做了 cross-architecture 对比？
**否** — 他们在三个 VLA 上做了实验（π₀、π₀.₅、SmolVLA），但：
- Pruning baselines（FastV、SparseVLM、VLA-Cache）**只在 π₀/π₀.₅ 上测试**，未在 SmolVLA 上跑
- 没有分析为什么不同架构对 compression 的响应不同
- 没有提及 connector type（MLP vs pixel-shuffle vs cross-attention）的区别
- SmolVLA 的架构细节（connector 类型）在论文中未说明

### Q3: SmolVLA 实验深度
- SmolVLA **仅用于真实机器人实验**（SO100 robot arm，3个任务），**没有 LIBERO 仿真**
- 他们观察到 SmolVLA baseline 在 Stack Cubes 上只有 7.6% SR（接近失败），GridS 提升到 60%
- K=4 时 GridS 本身也是 0% SR，但他们将此归因为 "information bottleneck"（geometric resolution 不足），**没有分析是否与 SmolVLA 的 connector 设计有关**
- 关键遗漏：他们没有在 SmolVLA 上测试任何 discrete pruning baseline，所以没有 "token deletion → 0% SR" 的直接证据

### Q4: Motivation 叙事类型
**通用优化** — 他们的叙事是：
> "所有现有 pruning 方法都受限于 discrete selection over a fixed grid，导致 quantization errors 和 spatial fidelity loss。我们提出 continuous resampling 替代 discrete dropping。"

这是一个 **method-level** 的改进论述（continuous > discrete），不是 architecture-level 的诊断。他们没有说 "某些架构下 pruning 完全失败"，而是说 "pruning 在所有情况下都有 quantization error，我们的方法更好"。

---

## 对我们 Claim 2 独特性的影响

**无实质影响。** 具体原因：

1. **机制分析完全不重叠**：GridS 论文不涉及 pixel-shuffle connector 如何制造 token entanglement，不分析 architecture-dependent compressibility，不解释为什么 discrete deletion 在某些架构上 cliff-edge 到 0%
2. **他们的 "为什么 pruning 不好" 停留在 quantization error 层面**，我们的分析深入到 connector-induced spatial entanglement 层面——这是不同抽象层次的解释
3. **他们没有做 cross-architecture 对比实验**：没有在同一 benchmark 上比较不同 connector 类型对 pruning 的容忍度差异
4. **SmolVLA 上的 0% SR 是他们自己的 GridS 在 K=4 时的结果**，不是 discrete pruning 的结果——他们甚至没在 SmolVLA 上跑 discrete pruning baseline

### 一个需要注意的点
他们的 K=4 → 0% 结果表明即使是 continuous resampling，在极端压缩下也会崩溃。但他们的解释（"information bottleneck, insufficient geometric resolution"）与我们的解释（"pixel-shuffle entanglement 导致 token 间不可分离"）完全不同。

---

## 建议的 Related Work positioning 策略

GridS 应作为 **concurrent work** 引用，定位为：

> "GridS (Feng et al., 2026) proposes continuous grid resampling as an alternative to discrete token pruning, achieving strong compression on π₀ and SmolVLA. However, their analysis focuses on the discrete-vs-continuous sampling paradigm without examining **why** certain VLA architectures exhibit fundamentally different compression behaviors. Our work is complementary: we diagnose the architectural root cause (pixel-shuffle-induced token entanglement) that makes discrete pruning catastrophically fail on specific connector designs, providing the theoretical foundation for **when** alternative compression strategies like GridS become necessary."

核心差异化：
- **GridS 回答 "how to compress better"**（continuous > discrete）
- **我们回答 "why compression fails on certain architectures"**（pixel-shuffle entanglement 诊断）+ "how to predict compressibility"（importance margin）

Sources:
- [ICML 2026 Poster - See What Matters](https://icml.cc/virtual/2026/poster/65010)
- [arXiv:2605.11817](https://arxiv.org/abs/2605.11817)

---

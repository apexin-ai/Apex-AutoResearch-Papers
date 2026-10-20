# 大模型第三方法可行性评估

## 路径 (a): AtP* 自行实现

- **可行性**: 是（有条件）
- **预估工作量**: 1.5–2 天
- **算法族**: Gradient attribution（与 EAP-IG 同族但子类不同）

### 具体分析

AtP* 的两个核心修改原理清晰：
- **QK-Fix**: 不通过 softmax 反传梯度，而是显式计算 `softmax(Q_corrupt · K_clean^T) − softmax(Q_clean · K_clean^T)` 再乘下游梯度。绕过 attention saturation 问题。
- **GradDrop**: 每层 residual stream 做一次 backward pass 时将该层梯度置零，收集 L 次 pass 的绝对值均值，打破 direct/indirect effect 的 cancellation。

现有代码情况：
- `koayon/atp_star`（GitHub）仅实现 **node-level**，且基于 NNsight 而非 TransformerLens。
- **无任何 edge-level AtP* 开源实现**。需基于 `hannamw/eap-ig` 从零添加 QK-Fix + GradDrop。

实现要点：
- QK-Fix 需 hook `hook_q`/`hook_k`/`hook_pattern`，对每个 attention head 做额外 forward pass 计算 Δattn。
- GradDrop 需在 `hook_resid_post` 注册 backward hook 做梯度置零，跑 L 次 backward pass。
- 主要工程难度：QK-Fix 在 edge-level 下需要为每个 Q/K edge 分别计算，且 GradDrop 的 L 次 backward 增加成本。

**算法独立性判断**：AtP* 与 EAP-IG 同属 gradient attribution 族，但机制差异显著——EAP-IG 用 integrated gradients（多步插值平均），AtP* 用 single-point gradient + 显式 softmax 线性化 + 路径隔离。**作为论文中的"第三种方法"，审稿人可能质疑其独立性**，因为本质仍是 gradient × activation difference 的变体。

---

## 路径 (b): PAHQ 加速 ACDC

- **可行性**: 否
- **预估工作量**: N/A
- **算法族**: Causal intervention（加速版 ACDC）

### 具体分析

PAHQ（GitHub: `626619403/PAHQ`）已开源，基于 TransformerLens 修改版。核心思想：对 ACDC 每次 patching forward pass 中非关键组件做 mixed-precision 量化（FP8/BF16），关键头保持 FP32。

**加速效果**：GPT-2 Small 上 5x 加速（99min → 20min），内存降 30%。

**无法满足需求的原因**：
1. 论文明确承认 "ACDC becomes computationally prohibitive on larger models"，未提供 0.5B+ 模型的 ACDC 时间数据。
2. 即使乐观估计 5x 加速：42–127h → 8–25h/task，仍超 10h 目标。
3. 仅支持 `gpt2`/`attn-only-4l`/`redwood_attn_2l`，移植到 Qwen 架构需大量适配。
4. 依赖 H20 GPU 的 FP8 支持，硬件限制大。

**其他 ACDC 加速方案**：
- CD-T（ICLR 2025）声称"hours to seconds"但仅 node-level。
- IBCircuit（ICML 2025）基于 information bottleneck，edge-level，但太新（2026.02），无成熟实现。

结论：ACDC 在 0.5B+ 模型上不可行，加速方案均不足以弥补数量级差距。

---

## 路径 (c): MIB 其他方法

### 方法列表

| 方法 | 算法族 | Edge-level? | 大模型可扩展? | 备注 |
|------|--------|------------|-------------|------|
| Random | 随机基线 | ✓ | ✓ | 无意义 |
| EActP (Exact Act. Patching) | Causal intervention | ✓ | ✗ (O(n) forward) | 与 ACDC 同样不可扩展 |
| EAP (mean/CF) | Gradient attribution | ✓ | ✓ | EAP-IG 的简化版 |
| **EAP-OA** | Gradient attribution | ✓ | ✓ | 见下方分析 |
| **EAP-IG-inputs** | Gradient attribution (IG) | ✓ | ✓ | 已选为方法 1 |
| EAP-IG-activations | Gradient attribution (IG) | ✓ | 中等 | 成本随层数增长 |
| NAP / NAP-IG | Gradient attribution | ✗ (node) | ✓ | 非 edge-level |
| **IFR** | **Activation decomposition** | ✓ | **✓✓ (极佳)** | 见下方分析 |
| **UGS** | Mask optimization | ✓ | ✗ (内存爆炸) | 见下方分析 |

### 重点评估

**IFR (Information Flow Routes)**
- **算法族**: Activation decomposition + proximity-based scoring。**与 gradient/mask/causal 三族均不同**。
- **原理**: 将 residual stream 分解为各组件贡献，用负 L1 距离度量 edge (u→v) 的 proximity: `score(u,v) = max(-||y_u - x_v||_1 + ||x_v||_1, 0)`。基于 ALTI（Ferrando & Voita, EMNLP 2024）。
- **Edge-level**: ✓
- **可扩展性**: 极佳——仅需 1 次 forward pass + activation 缓存，无 backprop，无 corrupted input。比 ACDC 快 ~100x。
- **弱点**: 非因果方法（无反事实推理），MIB 上性能低于 attribution 方法。度量的是"激活相似度"而非"因果重要性"。
- **作为第三方法的价值**: 提供完全不同的算法视角（similarity-based vs. gradient-based vs. optimization-based），增强投票多样性。

**UGS (Uniform Gradient Sampling)**
- **算法族**: Mask optimization（与 Edge Pruning 同族）。
- **原理**: 学习连续 pruning mask，通过梯度优化 mask 参数，采样 ablation 系数。
- **Edge-level**: ✓
- **可扩展性**: ✗。论文和 MIB 均确认 "intractable with respect to memory requirements as models scale"。
- **结论**: 不可用于 0.5B+ 模型。且与 Edge Pruning 同属 mask optimization 族，算法多样性不足。

**EAP-OA (EAP with Optimal Ablations)**
- **与 EAP-IG 的区别**: EAP-OA 改进的是 **ablation 值**（用预计算的最优 ablation 向量 a* 替代 mean/CF ablation），而非梯度估计方式。EAP-IG 改进的是 **梯度估计**（integrated gradients）。两者正交。
- **算法族**: 仍是 gradient attribution，与 EAP-IG 同族。
- **结论**: 可作为 EAP-IG 的增强（EAP-IG + OA），但不构成独立的第三方法。

---

## 推荐

- **首选**: **IFR (Information Flow Routes)**
  - 唯一满足"非 gradient、非 mask optimization、edge-level、可扩展到 8B"全部条件的方法
  - 算法族（activation decomposition）与 EAP-IG（gradient）和 Edge Pruning（mask optimization）完全不同，三法投票具备方法论多样性
  - MIB 已有实现（`hannamw/MIB-circuit-track`），无需从零开发
  - 仅需 1 次 forward pass，计算成本极低
  - 弱点：非因果方法，faithfulness 可能较低——但在 K=3 共识投票中，diversity 比 individual accuracy 更重要

- **备选**: **AtP* 自行实现**
  - 作为 Plan B，如果 IFR 在实验中表现太差（投票结果与 EAP-IG/Edge Pruning 严重不一致）
  - 工作量 ~1.5–2 天，风险在于与 EAP-IG 同属 gradient 族，审稿人可能挑战独立性

- **理由**: 三法投票的论文贡献在于"不同算法族的方法对 circuit structure 达成共识"。IFR 提供了第三个完全独立的算法视角。即使 IFR 单独 faithfulness 较低，在共识框架下反而是优势——如果一个 similarity-based 方法也同意 gradient-based 和 optimization-based 方法找到的 edges，这些 edges 的可信度更高。

### 最终方法组合

| K | 方法 | 算法族 | 实现来源 |
|---|------|--------|---------|
| 1 | EAP-IG | Gradient attribution (integrated gradients) | `hannamw/eap-ig` |
| 2 | Edge Pruning | Mask optimization | `princeton-nlp/edge-pruning` |
| 3 | **IFR** | **Activation decomposition (proximity-based)** | `hannamw/MIB-circuit-track` |

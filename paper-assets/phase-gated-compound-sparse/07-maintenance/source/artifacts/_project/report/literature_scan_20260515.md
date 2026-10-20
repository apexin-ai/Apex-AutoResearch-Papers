# Literature Scan: phase-gated-compound-sparse

**扫描日期**: 2026-05-14  
**覆盖窗口**: 2026-05-01 ~ 2026-05-14（近 2 周），附带 2026 Q1-Q2 重要相关论文  
**搜索关键词**: compound sparsity/pruning, phase-aware pruning, pruning interaction effect, layer-wise pruning compound, importance-based pruning severity, random vs importance pruning compound interaction

---

## 结论

**未发现直接竞争论文。** 没有任何 2026 年 5 月的论文研究 importance-based pruning 的 compound interaction severity 如何随 sparsity 单调递增，也没有论文对比 importance-based 与 random masking 的 compound severity 差异。项目核心方向仍然独特。

以下列出 2026 年相关论文，按相关性排序。

---

## 高相关论文（互补，非竞争）

### 1. Structural Sensitivity in Compressed Transformers: Error Propagation, Lyapunov Stability, and Formally Verified Bounds
- **arXiv**: [2603.20991](https://arxiv.org/abs/2603.20991)
- **时间**: 2026-03
- **关系**: 🟡 互补
- **摘要**: 用 Lyapunov 稳定性理论分析压缩误差在 Transformer 层间的传播。发现残差连接收缩压缩误差，但不同组件（MLP up-projection vs value projection）的敏感度跨 5 个数量级。提出 per-component sensitivity 分析框架。
- **与本项目关系**: 该论文关注单层压缩误差的跨层传播，而非多层同时剪枝的 compound interaction。其 Lyapunov 框架可作为理论工具解释我们观察到的 compound severity 现象。**不构成竞争**——他们不研究 compound interaction，不区分 importance-based vs random。

### 2. Pruning as a Cooperative Game: Surrogate-Assisted Layer Contribution Estimation for Large Language Models
- **arXiv**: [2602.07804](https://arxiv.org/abs/2602.07804)
- **时间**: 2026-02
- **关系**: 🟡 互补
- **摘要**: 将 LLM 层剪枝建模为合作博弈，每层是一个 player，用 Shapley 值量化层贡献。通过 Monte Carlo 采样 + surrogate network 近似 Shapley 值，识别关键层。
- **与本项目关系**: 同样关注层间交互，但目标是找最优剪枝方案（应用导向），而非分析 compound severity 的单调性规律（理论导向）。Shapley 值方法可作为本项目的互补视角。**不构成竞争。**

### 3. Variance Is Not Importance: Structural Analysis of Transformer Compressibility Across Model Scales
- **arXiv**: [2604.20682](https://arxiv.org/abs/2604.20682)
- **时间**: 2026-04
- **关系**: 🟡 互补
- **摘要**: 分析不同规模 Transformer 的可压缩性结构，区分 variance 和 importance 在压缩决策中的角色。
- **与本项目关系**: 提供了关于 importance 度量的新视角，但不涉及 compound interaction 分析。

### 4. Determining Layer-wise Sparsity for Large Language Models Through a Theoretical Perspective
- **arXiv**: [2502.14770](https://arxiv.org/abs/2502.14770)
- **时间**: 2025-02（TMLR 2026-02 发表）
- **关系**: 🟡 互补
- **摘要**: 识别 "reconstruction error explosion" 现象——早期层的重构误差在后续层传播和放大。提出理论框架确定 layer-wise sparsity 分配。
- **与本项目关系**: 描述了与 compound severity 相关的误差累积现象，但未系统量化 compound interaction，也未区分 importance-based vs random。可作为 related work 引用。

---

## 中等相关论文

### 5. Enhanced Pruning Strategy for Multi-Component Neural Architectures Using Component-Aware Graph Analysis
- **arXiv**: [2504.13296](https://arxiv.org/abs/2504.13296)
- **时间**: 2025-04
- **关系**: 🟢 弱相关
- **摘要**: 用扩展依赖图进行 component-aware 剪枝，发现组件重要性在训练过程中动态变化。
- **与本项目关系**: 关注组件间依赖，但是工程导向的剪枝方法，非理论分析。

### 6. GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models
- **arXiv**: [2603.13418](https://arxiv.org/abs/2603.13418)
- **时间**: 2026-03
- **关系**: 🟢 弱相关
- **摘要**: 提出 generalization-aware 结构化剪枝，将 neuron 按跨分布行为分组后进行局部排序。
- **与本项目关系**: 关注 importance 评估的鲁棒性，但不研究 compound interaction。

### 7. Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling
- **arXiv**: [2604.25098](https://arxiv.org/abs/2604.25098)
- **时间**: 2026-04
- **关系**: 🟢 弱相关
- **摘要**: 比较 structured vs unstructured pruning 对 test-time scaling 的影响，发现 unstructured pruning 有时可超过 full-weight 模型。

### 8. Pruning as a Game: Equilibrium-Driven Sparsification of Neural Networks
- **arXiv**: [2512.22106](https://arxiv.org/abs/2512.22106)
- **时间**: 2025-12
- **关系**: 🟢 弱相关
- **摘要**: 将剪枝建模为非合作博弈，参数组作为 player 选择参与度。

### 9. Týr-the-Pruner: Structural Pruning LLMs via Global Sparsity Distribution Optimization
- **arXiv**: [2503.09657](https://arxiv.org/abs/2503.09657)
- **时间**: 2025-10（更新至 2026-03）
- **关系**: 🟢 弱相关
- **摘要**: 构建 supernet 搜索全局最优 sparsity 分配，引入 expectation error accumulation 处理多剪枝副本间的误差传播。

### 10. MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference
- **arXiv**: [2505.22913](https://arxiv.org/abs/2505.22913)
- **时间**: 2025-05（更新至 2026-05）
- **关系**: 🟢 弱相关
- **摘要**: KV cache unstructured sparsity，70% 稀疏度无精度损失。应用场景不同。

---

## 2026-05-01 之后新论文

在 2026 年 5 月 1 日至 14 日窗口内，**未发现与本项目核心方向（compound pruning interaction severity）直接相关的新论文**。该时间段的 pruning 论文主要集中在：
- KV cache 剪枝（MUSTAFAR 更新版）
- 动态层剪枝（SkipGPT）
- Test-time scaling 与剪枝的交互

---

## 风险评估

| 维度 | 状态 |
|------|------|
| 直接竞争 | 🟢 未发现 |
| 理论框架被抢先 | 🟢 未发现 |
| 类似实验设置 | 🟢 未发现 |
| 需关注的互补工作 | 🟡 2603.20991 和 2602.07804 应纳入 related work |

**建议**: 项目核心方向仍具独特性。Related work 中应讨论 arXiv:2603.20991（Lyapunov 误差传播框架）和 arXiv:2602.07804（Shapley 层交互），说明本项目与它们的区别——我们关注 compound interaction severity 的定量规律和 importance-based vs random 的差异，而非误差传播理论或最优剪枝方案。

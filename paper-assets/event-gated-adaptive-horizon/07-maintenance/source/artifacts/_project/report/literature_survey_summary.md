# Bernoulli ST Gate 文献调研摘要
**日期**: 2026-05-14

## 新颖性评估

我们的方法——在 DreamerV3 RSSM 上用 Bernoulli straight-through gate 做 event-gated variable-rate imagination——**尚无完全相同的工作**，但存在高度相关的竞争者：

- **THICK** (Gumbsch et al., ICLR 2024) 在 Dreamer 上做了 adaptive temporal abstraction，但通过检测离散隐状态变化（被动事件发现），而非显式 gate（主动跳过决策）。这是最需要仔细区分的竞争者。
- **MetaController** (DeepMind, 2025) 的 switching gate β_t 与我们的 Bernoulli gate 功能几乎等价，且实验证明 gate 会自发趋向 quasi-binary。但它工作在 autoregressive sequence model 上而非 RSSM world model。

**结论**：我们的 specific contribution——在 RSSM imagination rollout 中用 Bernoulli ST gate 做 binary skip/no-skip 决策——是新颖的，但需要精确定位与 THICK 和 MetaController 的差异。

## 最强竞争者

1. **THICK** (ICLR 2024)：同样在 Dreamer 上做 adaptive temporal abstraction，已发表在顶会。我们必须在实验中与其对比或至少详细讨论。
2. **MetaController** (2025)：switching gate 机制最接近我们，但应用场景不同（sequence model vs. world model）。
3. **TempoRL** (ICML 2021)：model-free 的 variable-rate 决策 baseline。

## 关键参考文献

**必须引用**：
- Bengio et al. 2013（STE 原始论文）
- Hafner et al. 2023（DreamerV3）
- Sutton et al. 1999（Options framework）
- Gumbsch et al. 2024（THICK，主要竞争者）
- Jang et al. 2017（Gumbel-Softmax，解释我们为何弃用）

**强烈建议引用**：
- MetaController 2025（switching gate 验证了 gate 趋向二值的假设）
- Bacon et al. 2017（Option-Critic，termination gradient 理论基础）
- TempoRL 2021 / FiGAR 2017（learned action repetition 先驱）

**按需引用（STE 改进方向）**：
- AdaSTE (CVPR 2022)、ReSTE (ICCV 2023)、Decoupled ST-GS (2024)、FSG (AAAI 2025)

## 论文 Framing 建议

1. **定位**：不要定位为"第一个做 temporal abstraction in world model"（THICK 已做），而应定位为"第一个用显式 binary gate 在 RSSM imagination 中做 event-driven adaptive horizon"。强调 gate 是 agent 的主动决策（而非被动的状态变化检测），并且 gate 直接作用于 imagination rollout 的步长。
2. **Gumbel→Bernoulli 的 pivot story**：在方法部分简要说明 Gumbel-Softmax gate 的失败和转向 Bernoulli ST 的原因，这增强可信度（show negative results）。
3. **与 MetaController 的联系**：引用其"gate 自发趋向 quasi-binary"的发现作为我们使用硬 Bernoulli 阈值的理论支撑——既然 gate 终究会趋向二值，不如直接用 Bernoulli ST 从一开始强制二值化。
4. **STE 改进作为 future work**：AdaSTE/ReSTE/FSG 等改进可放在 discussion 或 future work 中，作为 gate 梯度估计的潜在优化方向。

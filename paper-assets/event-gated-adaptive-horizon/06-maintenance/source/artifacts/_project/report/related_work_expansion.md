# Related Work Expansion (D4)

> 20+ new references organized by category. Does NOT repeat the 7 already-cited papers (DreamerV3, GradNorm, Non-delusional Q, PCGrad, VaGraM, Gradient Routing, TAWM).

---

## Category 1: Value Overestimation in RL / MBRL

- **Addressing Function Approximation Error in Actor-Critic Methods** (Fujimoto et al., 2018) — TD3: twin critics + clipped double Q-learning to suppress overestimation bias in continuous control.
  - BibTeX key suggestion: `fujimoto2018td3`
  - 与本文关系: [background] — 我们的 event-gated mechanism 部分动机来自 value overestimation 在 world model rollout 中的放大效应；TD3 是 model-free 经典对策

- **Randomized Ensembled Double Q-Learning: Learning Fast Without a Model** (Chen et al., 2021) — REDQ: 大 ensemble + 随机子集取 min，UTD>>1 下的高样本效率 model-free 方法
  - BibTeX key suggestion: `chen2021redq`
  - 与本文关系: [method-component] — ensemble Q-function 的 in-target minimization 与我们对 value estimate 的保守处理相关

- **COMBO: Conservative Offline Model-Based Policy Optimization** (Yu et al., 2021) — 在 model rollout 上对 OOD state-action 施加 value penalty，无需显式 uncertainty estimation
  - BibTeX key suggestion: `yu2021combo`
  - 与本文关系: [direct-competitor] — conservative value estimation in model-based setting 的替代方案

- **MOPO: Model-based Offline Policy Optimization** (Yu et al., 2020) — 用 model uncertainty 作为 reward penalty，最大化真实 MDP return 的下界
  - BibTeX key suggestion: `yu2020mopo`
  - 与本文关系: [background] — uncertainty-penalized reward 与我们 event-gated horizon shortening 都抑制 overestimation，但机制不同

- **Value Gradient weighted Model-Based Reinforcement Learning** (Voelcker et al., 2022) — VaGraM: 用 value function gradient 加权 model loss，关注对 policy 影响大的 prediction error
  - BibTeX key suggestion: `voelcker2022vagram`
  - 与本文关系: [method-component] — value-aware model learning 的互补视角；我们在 rollout 层面做 gating，VaGraM 在 model loss 层面做加权

---

## Category 2: Multi-task Loss Balancing in World Models

- **HarmonyDream: Task Harmonization Inside World Models** (Ma/Shang et al., 2024) — 量化 reconstruction vs reward loss 的 2 个数量级差异，提出 harmonious loss 动态调权
  - BibTeX key suggestion: `ma2024harmonydream`
  - 与本文关系: [direct-competitor] — 同样识别 world model 多任务训练的梯度/loss 量级不平衡问题；我们用 event-gated stop-gradient 而非 loss reweighting

- **Multi-Task Learning Using Uncertainty to Weigh Losses** (Kendall et al., 2018) — 用 homoscedastic uncertainty 自动平衡多任务 loss 权重
  - BibTeX key suggestion: `kendall2018uncertainty`
  - 与本文关系: [background] — multi-task loss balancing 的经典方法，HarmonyDream 和 GradNorm 的理论前驱

- **DreamerPro: Reconstruction-Free Model-Based RL with Prototypical Representations** (Deng et al., 2022) — 用 prototypical self-supervised learning 替代 reconstruction，减轻视觉干扰影响
  - BibTeX key suggestion: `deng2022dreamerpro`
  - 与本文关系: [background] — 从另一角度解决 reconstruction loss 主导训练的问题（去掉 reconstruction），与我们保留 reconstruction 但 gate gradient 的策略形成对比

---

## Category 3: Plasticity Loss & Network Degradation in Deep RL

- **The Primacy Bias in Deep Reinforcement Learning** (Nikishin et al., 2022) — RL agent 过拟合早期数据，提出 periodic network reset 缓解
  - BibTeX key suggestion: `nikishin2022primacy`
  - 与本文关系: [background] — plasticity loss 的根源分析；我们的 event-gated mechanism 通过选择性停止梯度防止 representation 退化

- **Deep Reinforcement Learning with Plasticity Injection** (Nikishin et al., 2023) — 注入新初始化参数恢复可塑性，无需完全 reset
  - BibTeX key suggestion: `nikishin2023plasticity`
  - 与本文关系: [background] — 与 periodic reset 互补的轻量方案；event-gating 也是一种不丢失已有参数的 plasticity preservation 手段

- **Understanding Plasticity in Neural Networks** (Lyle et al., 2023) — 系统分析 plasticity loss 与 loss landscape curvature 的关系，LayerNorm 有效
  - BibTeX key suggestion: `lyle2023plasticity`
  - 与本文关系: [background] — 为什么 DreamerV3 采用 LayerNorm 的理论解释；我们的方法从 gradient flow 而非 normalization 角度维护 plasticity

- **Loss of Plasticity in Continual Deep Reinforcement Learning** (Abbas et al., 2023) — 连续任务切换下网络激活稀疏化导致梯度消失
  - BibTeX key suggestion: `abbas2023plasticity`
  - 与本文关系: [background] — continual RL 视角下的 plasticity loss；event-gating 的 stop-gradient 可视为防止某些 task 的梯度过度稀疏化

---

## Category 4: Temporal Abstraction & Adaptive Horizon in MBRL

- **Deep Hierarchical Planning from Pixels (Director)** (Hafner et al., 2022) — Manager 在 world model latent space 设 subgoal，Worker 执行低层动作，实现 temporal abstraction
  - BibTeX key suggestion: `hafner2022director`
  - 与本文关系: [background] — hierarchical planning 实现变长 effective horizon；我们的 event-gating 不需要显式层次结构但达到类似的 adaptive horizon 效果

- **TD-MPC2: Scalable, Robust World Models for Continuous Control** (Hansen et al., 2024) — implicit world model + local trajectory optimization，317M 参数跨 80 任务
  - BibTeX key suggestion: `hansen2024tdmpc2`
  - 与本文关系: [background] — latent-space MPC 用 fixed short horizon planning；我们的 adaptive horizon 与其 fixed horizon 形成对比

- **When to Trust Your Model: Model-Based Policy Optimization (MBPO)** (Janner et al., 2019) — 从 replay buffer state branching short rollout，Dyna-style 经典方案
  - BibTeX key suggestion: `janner2019mbpo`
  - 与本文关系: [background] — short horizon rollout 的 seminal work；我们 event-gating 实现 state-dependent horizon 而非 globally fixed horizon

- **Conservative Rollout Length Adaptation (CRLA)** (2024) — 在 DreamerV3 上动态调整 rollout length，平衡 compounding error 与 data efficiency
  - BibTeX key suggestion: `anonymous2024crla`
  - 与本文关系: [direct-competitor] — 最直接的 adaptive horizon 竞争者；区别在于我们用 event-triggered gating 而非 model uncertainty metric

- **Learning Adaptive Horizon Maps Based on Error Forecast for Model Predictive Control** (2023) — 根据 forecast error 空间分布学习 state-dependent 最优 horizon
  - BibTeX key suggestion: `adaptive2023horizon`
  - 与本文关系: [background] — MPC 领域的 adaptive horizon 理论，horizon ∝ 1/forecast_error 的定量关系与我们 event-trigger 理念一致

- **Open-World RL over Long Short-Term Imagination (LS-Imagine)** (2025) — 有限 state transition steps 内扩展 imagination horizon，open-world 场景
  - BibTeX key suggestion: `lsimagine2025`
  - 与本文关系: [background] — long-horizon imagination 的新方案；与我们在 compounding error 管理上的目标一致但方法正交

---

## Category 5: Gradient Manipulation & Stop-Gradient in RL

- **Gradient Routing: Masking Gradients to Localize Computation in Neural Networks** (Clark et al., 2024) — data-dependent gradient mask 实现模块化学习，RL 中用于 localize behaviors
  - BibTeX key suggestion: `clark2024gradrouting`
  - 与本文关系: [method-component] — gradient mask 的通用框架；我们的 event-gated stop-gradient 是一种 state-dependent gradient routing

- **Conflict-Averse Gradient Aggregation for Constrained Multi-Objective RL** (2025) — CoMOGA: 处理 safety constraint 下多目标梯度冲突
  - BibTeX key suggestion: `comoga2025`
  - 与本文关系: [background] — multi-objective RL 中的梯度冲突处理；我们聚焦 world model 内部的 reconstruction vs reward gradient 冲突

- **Gradient Shaping for Multi-Constraint Safe Reinforcement Learning** (Yao et al., 2024) — 分析 redundant/conflicting constraint gradients，提出 projection-based shaping
  - BibTeX key suggestion: `yao2024gradshaping`
  - 与本文关系: [background] — gradient projection 在 RL 安全约束中的应用；与 PCGrad 同族但面向 safe RL

---

## Category 6: Model-Based RL Foundations & Ensemble Methods

- **Deep Reinforcement Learning in a Handful of Trials (PETS)** (Chua et al., 2018) — Probabilistic ensemble + trajectory sampling 实现 uncertainty-aware planning
  - BibTeX key suggestion: `chua2018pets`
  - 与本文关系: [background] — ensemble model 量化 epistemic uncertainty 的经典方案；我们的 event trigger 隐式利用 prediction error 作为 uncertainty signal

- **TransDreamer: Reinforcement Learning with Transformer World Models** (Chen & Wu, 2022) — Transformer State-Space Model 替代 RNN，更好捕获长程依赖
  - BibTeX key suggestion: `chen2022transdreamer`
  - 与本文关系: [background] — world model architecture 的演进方向；与我们基于 RSSM 的 event-gating 互补

- **STORM: Efficient Stochastic Transformer-based World Models** (Zhang et al., 2024) — transformer world model 在 Atari 100k 上匹配 DreamerV3 且训练更高效
  - BibTeX key suggestion: `zhang2024storm`
  - 与本文关系: [background] — 高效 world model 架构；event-gating 原则上可应用于 transformer-based world model

- **Diffusion for World Modeling: Visual Details Matter in Atari (DIAMOND)** (Alonso et al., 2024) — diffusion model 作为 world model，比 discrete-token 方法保留更多视觉细节
  - BibTeX key suggestion: `alonso2024diamond`
  - 与本文关系: [background] — world model 的 generation quality 进展；更高质量的 imagination 减少 compounding error 的另一路径

---

## Category 7: Event-Triggered & State-Dependent Control

- **Adaptive Event-triggered Reinforcement Learning Control for Complex Nonlinear Systems** (2024) — event-triggered 机制减少 RL 中不必要的 policy update，节约通信资源
  - BibTeX key suggestion: `adaptive2024eventtriggered`
  - 与本文关系: [background] — event-triggered 概念在 RL control 中的先例；我们将 event-trigger 应用于 world model gradient flow 而非 control communication

- **Reinforcement Learning of the Prediction Horizon in Model Predictive Control** (Gros & Zanon, 2021) — 用 RL 学习 MPC 的最优 prediction horizon 作为 state 的函数
  - BibTeX key suggestion: `gros2021horizon`
  - 与本文关系: [background] — state-dependent horizon 的 RL-MPC 交叉视角；我们的 event-gating 也实现 state-dependent effective horizon

---

## Summary Statistics

| Category | New refs | Key methodological link |
|----------|----------|------------------------|
| Value Overestimation | 5 | Overestimation amplified by model rollout |
| Multi-task Loss Balancing | 3 | Gradient magnitude imbalance in world model |
| Plasticity Loss | 4 | Network degradation under non-stationary objectives |
| Temporal Abstraction & Adaptive Horizon | 6 | Variable effective planning horizon |
| Gradient Manipulation | 3 | Selective gradient flow control |
| MBRL Foundations | 4 | Ensemble, transformer, diffusion world models |
| Event-Triggered Control | 2 | State-dependent triggering in RL |
| **Total new refs** | **27** | |

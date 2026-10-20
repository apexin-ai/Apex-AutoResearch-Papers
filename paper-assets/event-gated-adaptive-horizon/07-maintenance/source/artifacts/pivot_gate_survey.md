# Pivot Gate Survey: 替代 Hard Gumbel-Softmax Gate 的时间抽象机制

> 调研日期: 2026-05-13 | 项目: event-gated-adaptive-horizon

## 问题陈述

Hard Gumbel-Softmax gate 在 DreamerV3 imagination 中学习 dt∈{1,...,K} 的方案经 5 轮实验（exp_002-005）确认**结构性失败**：
- Gate 本身学到了有意义的 dt 模式（entropy、dt_mean、structure 全 PASS）
- 但 return 崩塌到 baseline 的 35%，gate_scale 0.5→0.6 时 return 从 276 暴跌到 25.7
- 根因：hard categorical gate 的 straight-through 梯度估计与 actor-critic 优化存在冲突——gate 的离散选择在 imagination rollout 中引入不可微断点，TD(λ) value 梯度无法正确回传

---

## 方向 A：Soft Attention Gate

### 核心思路
将 hard categorical choice dt∈{1,...,K} 替换为 soft weighted combination：
```
h_{t+1} = Σ_k w_k · RSSM_step(h_t, a_t, k_steps)
w = softmax(gate_logits)
```
完全可微，消除 Gumbel-Softmax 的梯度偏差。

### 关键论文

**1. THICK: Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics**
- Gumbsch, Sajid, Mill, Allen, Schwöbel (ICLR 2024)
- [Paper](https://openreview.net/forum?id=TjCDNssXKU) | [Code](https://github.com/CognitiveModeling/THICK)
- RSSM latent 分为 fast/slow 两部分，slow 部分稀疏更新形成 "invariant context"，high-level model 只预测 context change 时刻。时间抽象是 emergent 的（通过 latent 稀疏性），不需要显式 dt 选择。
- **与我们的关系**: 最直接相关——同样基于 RSSM，同样做 temporal abstraction，但避免了 hard gate。THICK 的 slow latent 机制可以替代我们的 event gate，且已有 Dreamer 集成（THICK Dreamer）。
- **可行性**: 中等。需改 RSSM state 结构（增加 slow component），加 high-level transition model，修改 imagination rollout。核心改动文件: `world_model.py` (RSSM), `agent.py` (imagination)。

**2. Hierarchical Planning with Latent World Models**
- 2025, arXiv:2604.03208
- 在 latent space 学习多尺度 world model，high level 做 temporally abstract planning，low level 做 fine-grained control。Pick-and-place 任务 70% 成功率 vs 单层 0%。
- **与我们的关系**: 验证了 temporal abstract imagination 的价值，但架构更重（full hierarchical planning）。
- **可行性**: 高（工程量大）。需要完整的双层 planning 架构。

**3. Emergent Temporal Abstractions in Autoregressive Models Enable Hierarchical RL**
- 2025, arXiv:2512.20605
- 在 autoregressive model 中引入 higher-order controller 学习压缩 long activation sequences。temporal abstraction 从预训练中 emerge，不需要显式设计。
- **与我们的关系**: 思路启发性强，但架构差异太大（autoregressive vs RSSM）。
- **可行性**: 高（不适配）。

**4. Adaptive Computation Time (ACT)**
- Graves (2016), arXiv:1603.08983
- 用 halting unit + ponder cost 让 RNN 自适应计算步数。soft halting probability 决定何时停止。
- **与我们的关系**: ACT 的 soft halting 机制可以直接借鉴——用 halting probability 做 soft temporal skip，而非 hard categorical dt 选择。ponder cost 可替代我们的 gate entropy regularization。
- **可行性**: 低（工程量小）。只需在 RSSM step 外加 halting mechanism，改动集中在 imagination rollout。

### 方向 A 小结
**推荐方案 A1: Soft Weighted Gate（自研）**——直接把 Gumbel-Softmax hard sampling 改成 softmax weighted combination。工程量最小（改 `event_gate.py` 的 forward 方法），保持现有架构不变。风险：soft combination 可能退化为固定权重（需要 entropy regularization）。

**推荐方案 A2: THICK-style Sparse Latent**——更优雅但工程量更大。学术新颖性高（我们的 event gate + THICK sparse latent = 新 contribution）。

---

## 方向 B：Mixture-of-Timescales

### 核心思路
多个 RSSM head 以不同固定 dt 运行，mixture weights 动态组合输出。类似 Mixture-of-Experts 但在时间维度。

### 关键论文

**1. MTS³: Multi Time Scale World Models**
- Shaj, Gholam Zadeh, Demir et al. (NeurIPS 2023 Spotlight)
- [Paper](https://arxiv.org/abs/2310.18534) | [Code](https://github.com/ALRhub/MTS3)
- 概率框架，多时间尺度 state space model，每层以不同速率更新。高效 inference scheme 实现长程预测。在系统辨识 benchmark 上 SOTA。
- **与我们的关系**: 概率框架很干净，但 MTS³ 是 prediction model，不是 RL agent——没有 actor-critic 集成。需要额外工程将 MTS³ 嵌入 Dreamer 的 imagination loop。
- **可行性**: 高（架构差异大）。MTS³ 的 state space formulation 与 RSSM 不同，移植工程量大。

**2. MTRSSM: Hierarchical Latent Dynamics Model with Multiple Timescales**
- IROS 2023
- [Paper](https://ieeexplore.ieee.org/document/10364442/)
- 直接在 RSSM 上做两层 hierarchy：fast RSSM + slow RSSM。slow level 以较低频率更新。用于 long-horizon robotic manipulation 的 video prediction。
- **与我们的关系**: 最直接适配——已经是 RSSM 架构，只需加 slow level。但原文只做了 prediction，没有 actor-critic。
- **可行性**: 中等。RSSM 扩展相对直接，但需设计如何在 imagination 中利用 slow dynamics 和如何训练 actor-critic。

**3. Learning World Models With Hierarchical Temporal Abstractions: A Probabilistic Perspective**
- Shaj (PhD Thesis, 2024), arXiv:2404.16078
- 统一了 Hidden-Parameter SSM 和 Multi-Time Scale SSM 的概率框架。提出可扩展的自适应层级 world model。
- **与我们的关系**: 理论参考，提供了 multi-timescale 的概率基础。

### 方向 B 小结
MoT 方向理论优美但工程量大。**MTRSSM** 是最佳起点（已基于 RSSM），但需自己设计 actor-critic 集成方案。适合作为中长期方向，不适合短期 pivot。

---

## 方向 C：学习型 dt 但避免 Actor-Critic 冲突

### 核心思路
保留 variable-rate stepping，但用不同的方法学习 dt，避免 hard gate + actor-critic 的梯度冲突。

### 关键论文

**1. SEAC: Deployable Reinforcement Learning with Variable Control Rate**
- Wang, Beltrame (2024), arXiv:2401.09286
- [Paper](https://arxiv.org/abs/2401.09286)
- 扩展 SAC，将 action duration 作为连续 action 维度。Actor 同时输出 (action, dt)，critic 联合评估。dt 是连续的，完全可微，不存在 hard gate 问题。
- **与我们的关系**: 直接解决我们的问题——dt 作为 continuous action 维度，actor-critic 自然优化。关键区别：SEAC 用于 model-free RL，我们需要在 model-based imagination 中使用。
- **可行性**: 低-中。改 actor 输出维度加 dt，critic 输入也加 dt，imagination 中根据 continuous dt 做 interpolation。核心改动: `actor.py`, `critic.py`, `imagination.py`。

**2. MOSEAC: Streamlined Variable Time Step Reinforcement Learning**
- 2024, arXiv:2406.01521, RLC 2024
- SEAC 的多目标扩展，加入 energy efficiency 目标。证明了 variable time step 在 actor-critic 框架中的收敛性。
- **与我们的关系**: 提供了 variable time step actor-critic 的收敛性保证参考。

**3. RL with Elastic Time Steps**
- 2024, arXiv:2402.14961
- 形式化 elastic time step MDP。将时间步长作为 agent 决策的一部分，证明了在 continuous-time 极限下的最优性。
- **与我们的关系**: 理论基础——证明了 variable dt 可以 optimal。可以引用来支撑我们的 motivation。

**4. CTCO: Dynamic Decision Frequency with Continuous Options**
- 2022, arXiv:2212.04407, IROS 2023
- 基于 options framework，连续时间的 option 有可变 duration。Open-loop policy 避免 redundancy。
- **与我们的关系**: Options framework + continuous time 的结合。但 options 架构更重，不如 SEAC 简洁。
- **可行性**: 高（架构复杂度高）。

**5. Sutton, Precup, Singh (1999): Between MDPs and Semi-MDPs**
- [Paper](https://people.cs.umass.edu/~barto/courses/cs687/Sutton-Precup-Singh-AIJ99.pdf)
- Options framework 的奠基论文。定义了 option = (initiation set, policy, termination condition)。Semi-MDP 处理 variable duration。
- **与我们的关系**: 理论根基。我们的 event gate 本质上是 option termination condition 的变体。

### 方向 C 小结
**SEAC-style continuous dt 最有前景**——将 dt 从 discrete categorical 改为 continuous action 维度，actor-critic 自然可微优化。工程量中等，但需要处理 imagination 中 non-integer dt 的 interpolation 问题。

---

## 方向 D：其他时间抽象方法

### 关键论文

**1. Director: Deep Hierarchical Planning from Pixels**
- Hafner, Lee et al. (NeurIPS 2022), arXiv:2206.04114
- [Paper](https://arxiv.org/abs/2206.04114)
- Manager 在 latent space 提出 subgoal，Worker 执行。时间抽象是隐式的——Manager 每 k 步选一次 goal。
- **与我们的关系**: 隐式 temporal abstraction，不需要显式 dt。但架构改动巨大（加整个 Manager-Worker hierarchy）。
- **可行性**: 高（工程量大）。需要 Manager policy, Worker policy, goal space 设计。

**2. TD-MPC2: Scalable World Models for Continuous Control**
- Hansen et al. (ICLR 2024)
- [Paper](https://arxiv.org/abs/2310.16828)
- TD learning + MPC in learned latent space。固定短 horizon planning，用 learned value function 做 terminal estimate。
- **与我们的关系**: 不直接做 temporal abstraction，但 "short horizon + value function" 的思路暗示：也许不需要 variable dt，只需要更好的 value estimation 来扩展有效 horizon。
- **可行性**: 不适用（架构差异太大，且不解决 temporal abstraction 问题）。

**3. TempDATA: Temporal Distance-Aware Transition Augmentation**
- 2025, arXiv:2505.13144
- 在 latent space 按 temporal distance 结构化 augment transitions。学习 temporal distance embedding。
- **与我们的关系**: 间接相关。temporal distance embedding 可以用来 soft-weight 不同 dt 的 transitions。

---

## 综合评估

### 工程可行性矩阵

| 方案 | 改动范围 | 工程难度 | 核心改动文件 | 预计工时 |
|------|---------|---------|-------------|---------|
| A1: Soft Weighted Gate | event_gate forward | **低** | `event_gate.py` | 2-4h |
| A2: THICK Sparse Latent | RSSM + imagination | **中** | `world_model.py`, `agent.py` | 1-2d |
| B: MTRSSM Dual-timescale | RSSM + imagination + critic | **中-高** | `world_model.py`, `agent.py`, `critic.py` | 2-3d |
| C: Continuous dt (SEAC-style) | actor + critic + imagination | **中** | `actor.py`, `critic.py`, `agent.py`, `event_gate.py` | 1-2d |
| D: Director hierarchy | 全架构 | **高** | 几乎所有文件 | 1w+ |

### Top 3 推荐方案（综合新颖性 + 可行性 + 问题适配度）

#### 🥇 推荐 1: Soft Weighted Gate（方向 A1）
- **做法**: 将 `event_gate.py` 中的 Gumbel-Softmax hard sampling 改为 softmax weighted combination。`h_{t+1} = Σ_k softmax(logits)[k] · RSSM(h_t, a_t, k)`
- **优势**: 工程量最小（几小时），保持现有架构，直接解决 hard gate 梯度问题
- **风险**: soft combination 可能计算量翻 K 倍（需 K 次 RSSM forward）；权重可能退化为 uniform
- **缓解**: 用 top-2 或 top-3 soft gate 限制计算量；加 entropy regularization 防退化
- **适配度**: ⭐⭐⭐⭐⭐ 直接解决 return 崩塌的根因
- **新颖性**: ⭐⭐ 工程改进，非新方法
- **依赖 exp_006 结果**: 否（无论 fixed dt 是否 work，soft gate 都是合理改进）

#### 🥈 推荐 2: THICK-style Sparse Latent Update（方向 A2）
- **做法**: 将 RSSM state 分为 fast/slow 两部分。Slow 部分通过 learned gate 稀疏更新（但 gate 作用于 latent 而非 dt，避免了 imagination dt 选择问题）。High-level model 预测 context change。
- **优势**: 学术新颖性高（event gate + THICK = 新 contribution），已有参考实现
- **风险**: 工程量中等，需仔细设计 slow/fast split + 如何影响 actor-critic
- **适配度**: ⭐⭐⭐⭐ 间接解决问题（避开 dt 选择，用 latent sparsity 代替）
- **新颖性**: ⭐⭐⭐⭐ 组合创新
- **依赖 exp_006 结果**: 是。如果 fixed dt=2 也崩 → variable-rate imagination 本身有问题 → THICK 的 sparse update 可能也会遇到类似问题

#### 🥉 推荐 3: Continuous dt as Action Dimension（方向 C, SEAC-style）
- **做法**: 去掉 event gate，将 dt 作为 actor 的额外 continuous output。Actor 输出 (action, dt)，dt∈[1, K]。Imagination 中根据 continuous dt 做 RSSM step interpolation。
- **优势**: 理论干净（完全可微，有 SEAC/MOSEAC 收敛性保证），dt 和 action 联合优化消除 gate-actor 冲突
- **风险**: non-integer dt 的 RSSM interpolation 设计（linear interpolation? 还是 floor+ceil weighted?）；dt 范围需要 clip
- **适配度**: ⭐⭐⭐⭐ 直接解决 gate-actor 冲突
- **新颖性**: ⭐⭐⭐ continuous dt 在 model-based imagination 中是新的
- **依赖 exp_006 结果**: 部分。如果 fixed dt=2 也崩 → 问题在 variable-rate imagination 本身 → 需要更根本的改变

---

## 决策树（基于 exp_006 结果）

```
exp_006 (fixed dt=2) 结果
├── return 正常 (≥80% baseline)
│   └── 问题确认在 gate 学习机制
│       ├── 短期 pivot: A1 (Soft Weighted Gate) — 最快验证
│       ├── 中期方向: C (Continuous dt) — 更优雅的长期方案
│       └── 论文方向: A2 (THICK-style) — 学术贡献最大
│
└── return 也崩塌
    └── 问题在 variable-rate imagination 本身
        ├── 考虑 B (Multi-timescale) — 不改 imagination dt，而是多尺度 latent
        ├── 考虑 D (Director) — 放弃 dt，改 hierarchical goal
        └── 或重新审视 imagination 机制本身
```

---

## 参考文献完整列表

### 方向 A
1. Gumbsch et al. "Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics" (ICLR 2024). https://openreview.net/forum?id=TjCDNssXKU
2. "Hierarchical Planning with Latent World Models" (2025). https://arxiv.org/abs/2604.03208
3. "Emergent Temporal Abstractions in Autoregressive Models Enable Hierarchical RL" (2025). https://arxiv.org/abs/2512.20605
4. Graves. "Adaptive Computation Time for Recurrent Neural Networks" (2016). https://arxiv.org/abs/1603.08983

### 方向 B
5. Shaj et al. "Multi Time Scale World Models" (NeurIPS 2023 Spotlight). https://arxiv.org/abs/2310.18534
6. "Hierarchical Latent Dynamics Model with Multiple Timescales" (IROS 2023). https://ieeexplore.ieee.org/document/10364442/
7. Shaj. "Learning World Models With Hierarchical Temporal Abstractions: A Probabilistic Perspective" (PhD Thesis, 2024). https://arxiv.org/abs/2404.16078

### 方向 C
8. Wang & Beltrame. "Deployable Reinforcement Learning with Variable Control Rate" (2024). https://arxiv.org/abs/2401.09286
9. "MOSEAC: Streamlined Variable Time Step Reinforcement Learning" (RLC 2024). https://arxiv.org/abs/2406.01521
10. "Reinforcement Learning with Elastic Time Steps" (2024). https://arxiv.org/abs/2402.14961
11. "Dynamic Decision Frequency with Continuous Options" (IROS 2023). https://arxiv.org/abs/2212.04407
12. Sutton, Precup, Singh. "Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in RL" (AIJ 1999).

### 方向 D
13. Hafner et al. "Deep Hierarchical Planning from Pixels" (Director, NeurIPS 2022). https://arxiv.org/abs/2206.04114
14. Hansen et al. "TD-MPC2: Scalable World Models for Continuous Control" (ICLR 2024). https://arxiv.org/abs/2310.16828
15. "Temporal Distance-Aware Transition Augmentation for Offline MBRL" (2025). https://arxiv.org/abs/2505.13144

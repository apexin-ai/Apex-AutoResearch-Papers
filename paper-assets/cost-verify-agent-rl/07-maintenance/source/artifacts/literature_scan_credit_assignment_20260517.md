# Literature Scan: Multi-Turn Agent RL + Credit Assignment

**Date**: 2026-05-17  
**Scope**: 2025.03 - 2026.05  
**Query**: multi-turn LLM agent RL, credit assignment, advantage estimation

---

## 结论

**发现 6 篇高威胁直接竞争者。** 该领域在 2025-2026 年极度活跃。多个独立团队已识别出 GRPO 在 multi-turn 场景中 step-level credit assignment 失败的问题，并各自提出了解决方案。

**关键差异化机会**：大多数竞争者的方向是 **改进 step-level credit assignment**（更好的 turn-level reward、hierarchical advantage、hindsight critic 等）。如果本项目的角度是 **分析 step-level 为何失败 + 论证 episode-level 作为更优替代**，则仍有独特贡献空间，但需要清晰 positioning：我们不是提出又一个 step-level 改进方案，而是从根本上质疑 step-level 的必要性。

---

## 一、直接竞争者（HIGH 威胁）

| # | 论文 | arXiv ID | 日期 | Venue | 核心方法 | 威胁等级 |
|---|------|----------|------|-------|----------|----------|
| 1 | **MT-GRPO**: Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design | 2505.11821 | 2025-05 | ICML 2025 / NeurIPS 2025 | 扩展 GRPO 到 multi-turn，turn-level reward + turn-level advantage estimation | **HIGH** |
| 2 | **GiGPO**: Group-in-Group Policy Optimization for LLM Agent Training | 2505.10978 | 2025-05 | NeurIPS 2025 | 两级 advantage：episode-level macro + step-level micro (anchor state grouping)，critic-free | **HIGH** |
| 3 | **Turn-PPO**: Turn-Level Advantage Estimation with PPO for Multi-Turn RL in Agentic LLMs | 2512.17008 | 2025-12 | Amazon Science | 分析 GRPO 在 multi-turn 的 instability，提出 turn-level MDP + PPO critic | **HIGH** |
| 4 | **HiPER**: Hierarchical RL with Explicit Credit Assignment for LLM Agents | 2602.16165 | 2026-02 | - | Hierarchical plan-execute + hierarchical advantage estimation；ALFWorld 97.4%, WebShop 83.3% | **HIGH** |
| 5 | **HCAPO**: Hindsight Credit Assignment for Long-Horizon LLM Agents | 2603.08754 | 2026-03 | - | LLM 作为 post-hoc critic 做 hindsight credit；明确指出 GRPO step-level Q-value 不准确 | **HIGH** |
| 6 | **GAGPO**: Generalized Advantage Grouped Policy Optimization | 2605.13217 | 2026-05 | - | Critic-free step-level TD/GAE via rollout grouping；最新工作 | **HIGH** |

### 竞争者核心观点对比

| 论文 | 对 GRPO 的诊断 | 解决方向 | 与本项目的关系 |
|------|---------------|----------|---------------|
| MT-GRPO | 只有 sparse outcome reward，缺乏 intermediate signal | 加 turn-level reward | 如果我们论证 episode-level 优于 turn-level，MT-GRPO 是主要对照 |
| GiGPO | Episode-level advantage 太粗，step-level 缺乏 | 两级 grouping 获得 step-level signal，仍 critic-free | 与我们 episode-level 方向相反：他们认为需要 step-level，我们可能认为不需要 |
| Turn-PPO | GRPO 采样 advantage 在 multi-turn 不稳定 | PPO critic + turn-level MDP | 支持 "GRPO advantage 有问题" 的诊断，但解法不同 |
| HiPER | Flat policy 无法有效传播 credit | Hierarchical decomposition | 正交方向，可作为 related work |
| HCAPO | GRPO step-level Q-value 不准 + baseline 错配 | Hindsight LLM critic | 与我们的 "advantage misattribution" 诊断最接近 |
| GAGPO | Trajectory-level 太粗 | Grouped non-parametric value proxy + step TD | 最新，需关注 |

---

## 二、中等相关工作（MEDIUM 威胁）

| # | 论文 | arXiv ID | 日期 | 核心方法 | 与本项目关系 |
|---|------|----------|------|----------|-------------|
| 7 | **SPA-RL**: Stepwise Progress Attribution | 2505.20732 | 2025-05 | Reward redistribution: 将 final reward 分解为 stepwise contributions | 不同机制（reward shaping vs advantage estimation），可引用 |
| 8 | **ProxMO**: Proximity-Based Multi-Turn Optimization | 2602.19225 | 2026-02 | 解决 task difficulty fluctuation 下的 credit misallocation | 更偏生产部署，complementary |
| 9 | **TSR**: Trajectory-Search Rollouts for Multi-Turn RL | 2602.11767 | 2026-02 | Training-time search 改善 rollout 质量，paired with PPO/GRPO | 提升 rollout 而非 credit assignment 本身 |
| 10 | **TL-GRPO**: Turn-Level RL for Reasoning-Guided Iterative Optimization | 2601.16480 | 2026-01 | Turn-level group sampling for iterative optimization | 不同 domain（电路设计），类似 idea |
| 11 | **Iterative Reward Calibration** (Multi-Turn RL for Tool-Calling Agents) | 2604.02869 | 2026-04 | 发现 naive dense per-turn rewards 可降低 14pp 性能；提出 reward calibration | 重要发现：step-level reward 设计不当会 hurt，支持我们的 narrative |
| 12 | **TIPS**: Turn-level Information-Potential Reward Shaping | 2603.22293 | 2026-03 | Information-theoretic turn-level reward shaping | Reward shaping 方向 |

---

## 三、相关但非竞争（可引用 / positioning）

| # | 论文 | arXiv ID | 日期 | 类型 | 用途 |
|---|------|----------|------|------|------|
| 13 | **From Reasoning to Agentic**: Credit Assignment in RL for LLMs (Survey) | 2604.09459 | 2026-04 | Survey (47 methods) | **必引**，提供 taxonomy 和 landscape |
| 14 | **Practitioner's Guide to Multi-turn Agentic RL** | 2510.01132 | 2025-10 | NeurIPS 2025 workshop | **必引**，systematic analysis |
| 15 | **C3**: Contextual Counterfactual Credit for Multi-Agent RL in LLM Collaboration | 2603.06859 | 2026-03 | Multi-agent (非 multi-turn single agent) | Related work section |
| 16 | **CCPO**: Counterfactual Credit Policy Optimization for Multi-Agent | 2603.21563 | 2026-03 | Multi-agent counterfactual | Related work section |
| 17 | **SCAR**: Shapley Credit Assignment for RLHF | 2505.20417 | 2025-05 | Token-level credit, single-turn RLHF | 方法论参考 |
| 18 | **M-GRPO**: Multi-Agent Deep Research (Training Multi-Agent Systems) | 2511.13288 | 2025-11 | Multi-agent GRPO | Related work |
| 19 | **CollabUIAgents**: Multi-Agent Credit Re-Assignment | 2502.14496 | 2025-02 | Multi-agent + process reward | Related work |
| 20 | **Awesome-Credit-Assignment-in-LLM-RL** | GitHub | ongoing | 文献集合 | 参考列表 |
| 21 | CMU Thesis: Towards Efficient Multi-Agent and Temporal Credit Assignment | CMU MSR | 2025-07 | Thesis | Background |

---

## 四、对本项目的影响分析

### 4.1 竞争格局

领域已非常拥挤。2025-05 至 2026-05 间至少有 **15+ 篇**直接或间接处理 multi-turn LLM agent credit assignment 的工作，且已有 1 篇综合 survey (2604.09459)。

### 4.2 本项目的差异化空间

多数竞争者的叙事是：**"GRPO/PPO 的 episode-level advantage 太粗，我们需要更细粒度的 step/turn-level credit assignment"**。他们的解法方向：
- Turn-level reward design (MT-GRPO, TIPS)
- Two-level advantage grouping (GiGPO, GAGPO)
- Hierarchical decomposition (HiPER)
- Hindsight/counterfactual analysis (HCAPO, C3)
- Learned critic (Turn-PPO)

**如果本项目的核心论点是 "step-level credit assignment 在特定条件下反而有害，episode-level 可以更好"**，这与主流方向 **相反**，是一个有新颖性的 contrarian position。

支撑证据：
- arXiv 2604.02869 发现 naive dense per-turn rewards 降低 14pp 性能
- episode-level 在某些场景下避免了 step-level 的 noise 和 misattribution

### 4.3 建议 positioning

1. Acknowledge 主流方向（更细粒度的 credit assignment）
2. 提出 contrarian hypothesis：在某些条件下 step-level advantage estimation 引入 noise > signal
3. 实验证明 episode-level 在何种条件下优于 step-level
4. 分析 boundary conditions（什么时候 step-level 有效，什么时候无效）

### 4.4 必引论文

- 2604.09459 (Survey)
- 2505.11821 (MT-GRPO)
- 2505.10978 (GiGPO)
- 2512.17008 (Turn-PPO)
- 2602.16165 (HiPER)
- 2603.08754 (HCAPO)
- 2510.01132 (Practitioner's Guide)
- 2604.02869 (Iterative Reward Calibration, 支持我们的 narrative)

---

## Sources

- [MT-GRPO (arXiv:2505.11821)](https://arxiv.org/abs/2505.11821)
- [GiGPO (arXiv:2505.10978)](https://arxiv.org/abs/2505.10978)
- [Turn-PPO (arXiv:2512.17008)](https://arxiv.org/abs/2512.17008)
- [HiPER (arXiv:2602.16165)](https://arxiv.org/abs/2602.16165)
- [HCAPO (arXiv:2603.08754)](https://arxiv.org/abs/2603.08754)
- [GAGPO (arXiv:2605.13217)](https://arxiv.org/abs/2605.13217)
- [SPA-RL (arXiv:2505.20732)](https://arxiv.org/abs/2505.20732)
- [ProxMO (arXiv:2602.19225)](https://arxiv.org/abs/2602.19225)
- [TSR (arXiv:2602.11767)](https://arxiv.org/abs/2602.11767)
- [TL-GRPO (arXiv:2601.16480)](https://arxiv.org/abs/2601.16480)
- [Iterative Reward Calibration (arXiv:2604.02869)](https://arxiv.org/abs/2604.02869)
- [TIPS (arXiv:2603.22293)](https://arxiv.org/abs/2603.22293)
- [Survey: From Reasoning to Agentic (arXiv:2604.09459)](https://arxiv.org/abs/2604.09459)
- [Practitioner's Guide (arXiv:2510.01132)](https://arxiv.org/abs/2510.01132)
- [C3 (arXiv:2603.06859)](https://arxiv.org/abs/2603.06859)
- [CCPO (arXiv:2603.21563)](https://arxiv.org/abs/2603.21563)
- [SCAR (arXiv:2505.20417)](https://arxiv.org/abs/2505.20417)
- [M-GRPO (arXiv:2511.13288)](https://arxiv.org/abs/2511.13288)
- [Awesome-Credit-Assignment-in-LLM-RL](https://github.com/xxzcc/Awesome-Credit-Assignment-in-LLM-RL)

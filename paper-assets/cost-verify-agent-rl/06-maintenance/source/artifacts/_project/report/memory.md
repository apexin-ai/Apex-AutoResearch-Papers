# Turn-Level PPO / Per-Step Credit Assignment Literature Review

> 调研日期：2026-05-17  
> 调研范围：2024–2026 年发表的 multi-turn agent RL credit assignment 相关论文

---

## 一、Direct Competitors：Turn-Level Credit Assignment Methods

### 1.1 Turn-PPO (Li et al., 2025)

- **论文**: Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs
- **作者**: Junbo Li, Peng Zhou, Rui Meng, Meet P. Vadera, Lihong Li, Yang Li
- **年份/会议**: 2025, EACL 2026
- **arXiv**: 2512.17008

**核心方法**:
- 将 MDP 从 token-level 重新定义为 turn-level：state = 到第 h-1 轮的完整交互历史 + 当前 query，action = LLM 在第 h 轮的完整 response
- Turn-level advantage 计算：γV_{n+1} − V_n（中间 turn），r − V_N（最终 turn）
- 整个 response 作为一个 action，advantage 应用于完整 response

**对 GRPO 的批判**（与我们的发现高度相关）:
1. **Uniform advantage assignment**: GRPO 对所有 token 跨 turn 施加相同的 advantage，忽略不同 turn 对最终 reward 的不等贡献
2. **High variance in advantage estimation**: "state representation misalignment" — response 内的 next state 只多一个 token，而跨 response 的 next state 包含整个环境输出块，导致 critic 退化为平均值
3. **GRPO 在 multi-turn 中频繁崩溃**: Sokoban 两个配置均 crash，WebShop 启用 reasoning 也 crash

**关键实验结果**:

| 环境 | 模型 | GRPO | Token-PPO | Turn-PPO |
|------|------|------|-----------|----------|
| WebShop | Qwen2.5-3B | 0.72 | 0.73 | **0.75** |
| WebShop | Qwen3-1.7B (no think) | 0.78 | 0.77 | **0.80** |
| WebShop | Qwen3-1.7B (think) | Crash | 0.54 | **0.55** |
| Sokoban | Qwen2.5-3B | Crash | 1.93 | **2.29** |
| Sokoban | Qwen2.5-7B | Crash | 2.90 | **3.74** |

**与本项目的关系**: **最直接的竞品**。他们发现的 GRPO 问题（uniform advantage、崩溃）与我们发现的 Advantage Sign Misattribution 高度相关。区别在于：我们更深入地分析了 sign misattribution 的机制（γ 折扣导致早期步骤只保留 ~29% 的终端 return），他们更侧重 turn-level MDP 的形式化方案。

---

### 1.2 MT-GRPO / MT-PPO (Wei et al., 2025)

- **论文**: Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design
- **作者**: Quan Wei, Siliang Zeng, Chenliang Li, William Brown, Oana Frunza, Wei Deng, Anderson Schneider, Yuriy Nevmyvaka, Yang Katie Zhao, Alfredo Garcia, Mingyi Hong
- **年份/会议**: 2025, ICML 2025
- **arXiv**: 2505.11821

**核心方法**:
- 第一个系统性研究 turn-level reward design 的工作
- 将 GRPO 和 PPO 扩展为 multi-turn 变体（MT-GRPO、MT-PPO）
- 两种 turn-level reward 设计：(1) Verifiable reward（可验证中间结果）(2) LLM-as-judge reward（用 LLM 评价中间步骤质量）
- 细粒度 credit assignment strategy

**关键实验结果**:
- 在 QA 数据集上 MT-PPO 一致性最优，尤其在 multi-hop 任务（HotpotQA）上提升显著
- 100% format correctness，更高 answer correctness
- 更快收敛，更高稳定性

**与本项目的关系**: **直接竞品**。与我们的方向完全吻合——同样发现 episode-level sparse reward 不足以训练 multi-turn agent，需要 turn-level 信号。差异在于他们依赖外部 reward 信号（verifiable/LLM-judge），而我们关注的是在纯 outcome reward 下的 credit assignment 机制。

---

### 1.3 GiGPO (Feng et al., 2025)

- **论文**: Group-in-Group Policy Optimization for LLM Agent Training
- **作者**: Lang Feng, Zhenghai Xue, Tingcong Liu, Bo An
- **年份/会议**: 2025, NeurIPS 2025
- **arXiv**: 2505.10978

**核心方法**:
- 两层结构的 advantage estimation：
  - **Episode-level (macro)**: 对完整 trajectory 的 group 计算 relative advantage
  - **Step-level (micro)**: Anchor State Grouping — 在不同 trajectory 中找到重复出现的环境状态，回溯性地构建 step-level group，从而在相同状态下比较不同 action 的优劣
- 保持 group-based RL 的优点：critic-free、低显存、稳定收敛

**关键实验结果**:
- ALFWorld: >12% improvement over GRPO
- WebShop: >9% improvement over GRPO
- QA: 42.1% (3B), 47.2% (7B)
- 计算开销与 GRPO 几乎相同

**与本项目的关系**: **方法组件参考**。Anchor State Grouping 是一个巧妙的思路——通过在不同 trajectory 中找到相同环境状态来实现 step-level 比较。但这种方法依赖于环境状态的可重复性，在 cost verification agent 这种任务中状态空间更大更稀疏，直接复用可能受限。但其 "两层 advantage" 的思想与我们的分析方向兼容。

---

### 1.4 GAGPO (Zhu et al., 2026)

- **论文**: GAGPO: Generalized Advantage Grouped Policy Optimization
- **作者**: Siyuan Zhu, Chao Yu, Rongxin Yang, Zongkai Liu, Jinjun Hu, Qiwen Chen, Yibo Zhang
- **年份**: 2026
- **arXiv**: 2605.13217

**核心方法**:
- **Grouped Value Proxy**: 非参数化的 value 估计，通过对同一环境 group 中步骤的 discounted return 取平均来构建 baseline
- **Temporal Credit Propagation**: 递归 advantage 估计 A^t = δt + γλA^(t+1)，TD 残差向后传播延迟结果
- **Group-Normalized PPO**: 在 rollout group 内归一化（而非 batch 内），使用 sequence-level importance ratio

**关键实验结果**:
- ALFWorld: Qwen2.5-1.5B 93.5% (vs. 88.1% prior best), Qwen2.5-7B 95.6% (vs. 88.8%)
- WebShop: 1.5B 88.6 score / 78.1% SR, 7B 90.3 / 77.5%
- 比 GiGPO 更低的 advantage signal variance，更快的早期学习

**与本项目的关系**: **方法组件参考**。GAGPO 的 Grouped Value Proxy 本质上是一种无 critic 的 GAE 近似——用同一环境状态的多条 trajectory 来估计 value，再做 TD-style 的 advantage 传播。这与我们在纯 outcome reward 下寻找 credit assignment 方案的方向契合。

---

### 1.5 HCAPO (Tan et al., 2026)

- **论文**: Hindsight Credit Assignment for Long-Horizon LLM Agents
- **作者**: Hui-Ze Tan, Xiao-Wen Yang, Hao Chen, Jie-Jing Shao, Yi Wen, Yuteng Shen, Weihong Luo, Xiku Du, Lan-Zhe Guo, Yu-Feng Li
- **年份**: 2026
- **arXiv**: 2603.08754

**核心方法**:
- **Post-hoc Critic Refinement**: 用 LLM 自身作为 post-hoc critic，通过 hindsight reasoning 来 refine step-level Q-value
- **Multi-scale Advantage Mechanism**: 在关键决策点修正 value baseline 不准确性，将 trajectory-level reward 转化为 step-level 信号
- Value-free RL：不需要单独训练 critic

**关键实验结果**:
- WebShop: +7.7% over GRPO (Qwen2.5-7B-Instruct)
- ALFWorld: +13.8% over GRPO
- 更高 exploration efficiency，更简洁的决策

**与本项目的关系**: **方法组件参考**。Hindsight credit assignment 的思路很有启发性——在看到完整 trajectory 后回溯性地评估每步的质量。但依赖 LLM 自身做 Q-value 估计的可靠性存疑。

---

### 1.6 iStar (Liu et al., 2025)

- **论文**: Agentic Reinforcement Learning with Implicit Step Rewards
- **作者**: Xiaoqian Liu, Ke Wang, Yuchuan Wu, Fei Huang, Yongbin Li, Junge Zhang, Jianbin Jiao
- **年份**: 2025
- **arXiv**: 2509.19199

**核心方法**:
- 交替优化 implicit Process Reward Model (PRM) 和 policy model
- 通过 trajectory-based DPO objective 生成 implicit step reward
- **Dual Advantage Integration**: 组合 step-level 和 episode-level advantage 进行 policy update
- 不需要额外 rollout 或显式 step label

**关键实验结果**:
- WebShop, VisualSokoban, SOTOPIA 上超越 frontier LLM 和强 RL baseline
- 更好的 sample efficiency 和稳定性

**与本项目的关系**: **方法组件参考**。Dual advantage（step + episode）的组合是一个有趣的设计选择。Implicit PRM 的训练方式避免了人工标注 step reward 的成本。

---

### 1.7 SPA-RL (Wang et al., 2025)

- **论文**: SPA-RL: Reinforcing LLM Agents via Stepwise Progress Attribution
- **作者**: Hanlin Wang, Chak Tou Leong, Jiashuo Wang, Jian Wang, Wenjie Li
- **年份**: 2025
- **arXiv**: 2505.20732

**核心方法**:
- **Reward redistribution framework**: 将最终任务 reward 分解为各步的贡献
- **Progress Estimator**: 训练一个进度估计器，使各步贡献的累积和匹配任务完成度
- 估计的 per-step 贡献 + action grounding 信号 = 细粒度中间 reward

**关键实验结果**:
- WebShop, ALFWorld, VirtualHome 上平均 +2.5% success rate, +1.9% grounding accuracy

**与本项目的关系**: **方法组件参考**。Progress estimator 的思路类似 potential-based reward shaping。在 cost verification 任务中，可以尝试类似思路估计每步对最终验证成功的"贡献度"。

---

## 二、Foundational Frameworks

### 2.1 ArCHer (Zhou et al., 2024)

- **论文**: ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL
- **作者**: Yifei Zhou, Andrea Zanette, Jiayi Pan, Sergey Levine, Aviral Kumar
- **年份/会议**: 2024, ICML 2024
- **arXiv**: 2402.19446

**核心方法**:
- 开创性的 hierarchical multi-turn RL 框架
- **High-level**: off-policy TD 学习 utterance-level value function（跨 turn 聚合 reward）
- **Low-level**: policy gradient 在每个 turn 内优化 token 生成，使用 high-level value function 作为 terminal reward
- Off-policy 特性允许 sample reuse
- 避免对每个 token 做 Bellman backup

**关键实验结果**:
- 比 on-policy 方法约 **100x sample efficiency improvement**
- 在 7B 模型上验证可扩展性

**与本项目的关系**: **理论基础**。ArCHer 是 turn-level RL for LLMs 的开山之作。其 hierarchical (utterance-level value + token-level policy) 的设计启发了后续所有 Turn-PPO 类工作。但它依赖 off-policy 学习和显式 value function，而我们使用的 GRPO 是 on-policy、critic-free 的。

---

### 2.2 RAGEN / StarPO (Wang et al., 2025)

- **论文**: RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning
- **作者**: Zihan Wang, Kangrui Wang, Qineng Wang, Pingyue Zhang, et al.
- **年份**: 2025
- **arXiv**: 2504.20073

**核心方法**:
- **StarPO** (State-Thinking-Actions-Reward Policy Optimization): 通用 trajectory-level agent RL 框架
- 支持 multi-turn rollout, trajectory-level reward assignment, policy update
- **StarPO-S**: 稳定化变体，加入 trajectory filtering, critic integration, gradient stabilization
- **SNR-Adaptive Filtering (V2)**: 基于 reward variance 的 rollout 过滤，减少 noisy gradient

**关键发现**:
- **Echo Trap**: 训练后 agent 收敛到固定短语模板，RL 可能强化了 superficial pattern 而非 general reasoning
- 没有细粒度的 reasoning-aware reward signal，agent 无法发展真正的推理能力
- 10 个内置环境（Sokoban, FrozenLake, WebShop, DeepCoder, SearchQA 等）

**与本项目的关系**: **方法组件 + 实验平台**。StarPO 是一个通用框架，其 trajectory-level 设计在精神上与我们的 episode-level GRPO 类似。Echo Trap 现象值得关注——可能与我们观察到的 step-independent 崩塌有关联。

---

### 2.3 VAGEN (Wang et al., 2025)

- **论文**: VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents
- **作者**: Kangrui Wang, Pingyue Zhang, Zihan Wang, et al.
- **年份/会议**: 2025, NeurIPS 2025
- **arXiv**: 2510.16907

**核心方法**:
- **Bi-Level GAE (Bi-Level Generalized Advantage Estimation)**:
  - 第一层：turn-level advantage 评估每个 VLM response 的整体有效性
  - 第二层：将 turn-level signal 传播到 token-level，为每个 token 提供细粒度 advantage
- World Model 分解：State Estimation ("当前状态是什么？") + Transition Modeling ("下一步会怎样？")

**关键实验结果**:
- 3B 模型在 5 个 agent benchmark 上达到 0.82（3x improvement over untrained）
- 超越 GPT-5 (0.75), Gemini 2.5 Pro (0.67), Claude 4.5 (0.62)

**与本项目的关系**: **方法组件参考**。Bi-Level GAE 的 turn→token 传播机制是一个清晰的两层 credit assignment 设计。虽然 VAGEN 面向 VLM，但其 advantage 传播的数学形式可以直接迁移到 text-only agent RL。

---

### 2.4 HiPER (Peng et al., 2026)

- **论文**: HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents
- **作者**: Jiangweizhi Peng, Yuanxin Liu, Ruida Zhou, Charles Fleming, Zhaoran Wang, Alfredo Garcia, Mingyi Hong
- **年份**: 2026
- **arXiv**: 2602.16165

**核心方法**:
- **Hierarchical Plan-Execute**: 高层 planner 提出 subgoal，低层 executor 执行多步 action
- **Hierarchical Advantage Estimation (HAE)**: 在 planning 和 execution 两层分别做 credit assignment
  - 对每个 subgoal 聚合 return
  - 在两层之间协调 update
- 显式 temporal abstraction vs 传统 flat policy

**关键实验结果**:
- ALFWorld: 97.4% success (+6.6%)
- WebShop: 83.3% success (+8.3%)
- 在需要多个依赖子任务的长期任务上尤其强

**与本项目的关系**: **理论参考**。Hierarchical 分解的思路有参考价值，但需要额外定义 subgoal 结构，在 cost verification 任务中 subgoal 的定义不太自然。

---

## 三、Agent RL Frameworks (Episode-Level Reward)

### 3.1 WebRL (Qi et al., 2024)

- **论文**: WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning
- **作者**: Zehan Qi, Xiao Liu, et al.
- **年份/会议**: 2024, ICLR 2025
- **arXiv**: 2411.02337

**核心方法**:
- Self-evolving curriculum（从失败尝试生成新任务）
- Outcome-Supervised Reward Model (ORM) 提供 reward signal
- Adaptive RL 策略防止 policy distribution drift
- 使用 episode-level reward，不做显式 step-level credit assignment

**关键实验结果**:
- Llama-3.1-8B: 4.8% → 42.4% on WebArena-Lite
- GLM-4-9B: 6.1% → 43%
- 超越 GPT-4-Turbo (17.6%), GPT-4o (13.9%)

**与本项目的关系**: **Baseline 参考**。WebRL 表明在某些任务上 episode-level reward + curriculum 就能取得很好效果。但它没有 explicit credit assignment，在更长 horizon 或更稀疏 reward 的任务上可能受限。

---

### 3.2 WebAgent-R1 (Wei et al., 2025)

- **论文**: WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning
- **作者**: Zhepei Wei, Wenlin Yao, et al.
- **年份/会议**: 2025, EMNLP 2025
- **arXiv**: 2505.16421

**核心方法**:
- End-to-end multi-turn RL，binary success reward
- Thinking-based prompting + behavior cloning warm-up
- Credit assignment 隐式地通过 RL 优化过程实现

**关键实验结果**:
- Qwen-2.5-3B: 6.1% → 33.9%
- Llama-3.1-8B: 8.5% → 44.8%
- 显著超越 OpenAI o3

**与本项目的关系**: **Baseline 参考**。证明 end-to-end binary reward 也能工作，但不清楚其 credit assignment 的隐式机制。

---

### 3.3 StepAgent (Deng et al., 2024)

- **论文**: From Novice to Expert: LLM Agent Policy Optimization via Step-wise Reinforcement Learning
- **作者**: Zhirui Deng, Zhicheng Dou, Yutao Zhu, et al.
- **年份**: 2024
- **arXiv**: 2411.03817

**核心方法**:
- 通过自动比较 expert 和 agent 在每步的 action 来生成中间 reward
- Implicit-reward + 自我反思
- Inverse RL 辅助 policy adjustment
- 理论证明 agent action 分布可收敛到 expert

**与本项目的关系**: **方法参考**。依赖 expert demonstration 的方式在纯 RL 设定下不适用，但 IRL 思路可参考。

---

### 3.4 Planner-R1 (Zhu et al., 2025)

- **论文**: Planner-R1: Reward Shaping Enables Efficient Agentic RL with Smaller LLMs
- **作者**: Siyu Zhu, Yanbin Jiang, et al.
- **年份**: 2025
- **arXiv**: 2509.25779

**核心方法**:
- Dense process-level reward shaping
- 研究 reward density 对不同大小模型的影响
- Smaller (8B) models 对 reward shaping 高度敏感，dense reward 下可与 32B 竞争

**关键实验结果**:
- TravelPlanner: 56.9% final-pass (2.7x over GPT-5's 21.2%)
- 8B 模型在 dense reward 下 3.5x compute-efficient vs 32B
- Curriculum learning 无显著收益，shaped reward 一致性提升

**与本项目的关系**: **实验参考**。验证了 dense reward 对小模型训练的重要性。在 cost verification 场景下，如何设计 dense intermediate reward 是核心问题。

---

## 四、Surveys & Guides

### 4.1 From Reasoning to Agentic: Credit Assignment in RL for LLMs (Zhang, 2026)

- **论文**: From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models
- **作者**: Chenchen Zhang
- **年份**: 2026
- **arXiv**: 2604.09459

**核心内容**:
- 覆盖 **47 种 credit assignment 方法**（41 core + 6 adjacent enablers），2024–2026
- **两维分类法**:
  - 粒度维度: token / segment / step / turn / multi-agent
  - 方法维度: Monte Carlo / temporal difference / model-based / game-theoretic / information-theoretic
- **两种 regime**:
  - Reasoning RL: 单次 CoT（500–30K+ tokens），credit 在 tokens/steps 间分配
  - Agentic RL: multi-turn 交互（100K–1M tokens），有 stochastic transition 和 partial observability
- **关键判断**: Reasoning CA 围绕 PRM 和 critic-free group comparison 成熟，Agentic CA 正在推动新方法——hindsight counterfactual analysis, privileged asymmetric critics, turn-level MDP reformulations

**与本项目的关系**: **理论框架**。这篇 survey 的分类法可以帮助定位我们的工作——我们的 "Advantage Sign Misattribution" 发现属于 turn-level + Monte Carlo 的交叉区域。

---

### 4.2 A Practitioner's Guide to Multi-turn Agentic RL (Wang & Ammanabrolu, 2025)

- **论文**: A Practitioner's Guide to Multi-turn Agentic Reinforcement Learning
- **作者**: Ruiyi Wang, Prithviraj Ammanabrolu
- **年份/会议**: 2025, NeurIPS 2025 Workshop
- **arXiv**: 2510.01132

**核心内容**:
- 三大支柱: Environment, Reward, Policy
- **Dense vs Sparse per-turn reward**: dense turn-level reward 加速训练，但效果高度依赖 RL 算法选择
- PPO vs GRPO vs RLOO 对比
- Simple 环境可预测在 complex 变体上的泛化性

**与本项目的关系**: **实验设计参考**。其关于 sparse vs dense reward 的系统比较提供了实验设计的参考框架。

---

### 4.3 DeepSeek-R1 (DeepSeek, 2025)

- **论文**: DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
- **arXiv**: 2501.12948

**GRPO 在 single-turn 推理中的应用**:
- Episode-level advantage: 对同一 prompt 的 group 采样 → 组内归一化
- 所有 advantage estimation 在 sequence level（整个 completion）进行
- 移除 Value Model 后不再需要 token-level reward
- Policy ratio 仍在 token-level 计算（用于 gradient update）

**与本项目的关系**: **方法基础**。DeepSeek-R1 确立了 GRPO 的 single-turn 范式，但其 sequence-level advantage 直接应用到 multi-turn 场景时会产生我们发现的 Advantage Sign Misattribution 问题——因为多步交互中，不同步骤的 action 质量可能完全不同，统一的 sequence-level advantage 无法区分。

---

## 五、与本项目的关系总结

### 5.1 核心发现定位

我们发现的 **Advantage Sign Misattribution** 问题——失败 episode 中好的 action 收到无差别的负向 advantage，成功 episode 中差的 action 收到正向 advantage——与以下工作有直接对应关系：

| 论文 | 相关发现 |
|------|----------|
| Turn-PPO | "uniform advantage assignment" across turns，GRPO 在 multi-turn 中崩溃 |
| GiGPO | GRPO "collapses step-level distinctions" |
| HCAPO | GRPO 存在 "inaccurate Q-value estimates and misaligned baselines for intermediate states" |
| GAGPO | sparse reward 下 "impact of any individual action may only manifest much later" |
| iStar | "sparse and sometimes unverifiable rewards make credit assignment extremely challenging" |

然而，**没有一篇论文明确使用 "advantage sign misattribution" 这个术语**，也没有论文量化分析 γ 折扣对 sign 的影响（如我们发现的 ~29% 保留率）。这是我们可以贡献的新 framing。

### 5.2 分类

**Direct Competitors（解决相同问题的方法）**:
- Turn-PPO：turn-level MDP + turn-level advantage
- MT-GRPO/MT-PPO：turn-level reward design（verifiable + LLM-judge）
- GiGPO：anchor state grouping for step-level group comparison
- GAGPO：grouped value proxy + temporal credit propagation
- HCAPO：hindsight credit assignment with LLM-as-critic

**Method Components（可借鉴的技术组件）**:
- iStar: implicit PRM + dual advantage
- SPA-RL: progress estimator for reward redistribution
- VAGEN Bi-Level GAE: turn→token advantage propagation
- ArCHer: utterance-level value function (off-policy)
- HiPER: hierarchical advantage estimation

**Theoretical Foundation（理论基础）**:
- DeepSeek-R1 GRPO: 我们方法的出发点
- Credit Assignment Survey (Zhang 2026): 分类法和开放问题
- Practitioner's Guide: 实验设计参考

**Baseline Comparison（效果对比参考）**:
- WebRL: episode-level reward + curriculum
- WebAgent-R1: binary reward + end-to-end RL
- Planner-R1: reward shaping effect on model sizes

### 5.3 我们的差异化贡献空间

1. **Advantage Sign Misattribution 的正式定义和量化分析** — 现有工作描述了 "uniform advantage" 和 "credit assignment challenge"，但没有具体分析 sign 级别的错误及其量化影响
2. **γ 折扣在 multi-step agent 中的 return 衰减分析** — 早期步骤只保留 ~29% 的终端 return，这个量化结果是新的
3. **Step-independent vs Episode-level 的受控对比实验** — 直接证明 step-independent 优化的崩塌和 episode-level 的提升（0% vs 28%），这种 clean 的对比是稀缺的
4. **在 cost verification 特定任务上的分析** — 现有工作集中在 WebShop, ALFWorld, Sokoban 等标准 benchmark，我们的任务场景是差异化的

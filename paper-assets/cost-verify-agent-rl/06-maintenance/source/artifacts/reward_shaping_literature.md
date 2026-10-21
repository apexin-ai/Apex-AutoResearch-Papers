# Reward Shaping & Reward Gaming 文献调研

> 背景：GRPO 训练 Qwen3-1.7B 在 ALFWorld 上遭遇 reward gaming——valid_action_bonus=0.15/step 累积 4.5 vs success_reward=10.0，模型最大化 dense reward（valid 60%→97.5%）但 success 始终 0%。

---

## 一、直接解决我们问题的方法

### 1.1 G-RA: Gated Reward Accumulation（成功门控密集奖励）
- **论文**: Stabilizing Long-term Multi-turn Reinforcement Learning with Gated Rewards (2025, arXiv 2508.10548)
- **核心方法**: 中间步骤的 dense reward **仅在终局成功时才累计**。若 episode 失败，所有 dense reward 归零，只保留终局信号。
- **效果**: SWE-bench 完成率 47.6%→93.8%，kBench 4x 提升。Drop-in replacement，算法无关。
- **与我们的关联**: **直接对症**。我们的 valid_action_bonus 可以被独立最大化，G-RA 通过 success-gating 消除这个漏洞。实现简单：`final_reward = success_reward + (success * sum(dense_rewards))`。

### 1.2 GiGPO: Group-in-Group Policy Optimization（双层信用分配）
- **论文**: Group-in-Group Policy Optimization for LLM Agent Training (Lang Feng et al., 2025, NeurIPS; arXiv 2505.10978)
- **代码**: https://github.com/langfengQ/verl-agent
- **核心方法**: 两层 advantage 估计——(1) episode 级：多条完整轨迹组成 group 做相对排序；(2) step 级：同一 state 出发的不同 action 构成 anchor group，计算 step-level advantage。
- **ALFWorld 结果**: 比 GRPO 提升 >12%，比 GRPO+SFT warmup 也有显著提升。
- **与我们的关联**: **替代 GRPO 的首选**。Step-level credit assignment 直接解决 GRPO 只能给整条轨迹相同 advantage 的问题。基于 veRL，与我们的 RAGEN 框架兼容性需评估。

### 1.3 SPEAR: Self-Imitation + Progressive Exploration
- **代码**: https://github.com/TencentYoutuResearch/SPEAR (腾讯)
- **核心方法**: 收集成功轨迹做 self-imitation learning，结合 progressive exploration 扩展策略空间。
- **ALFWorld 结果**: RL-only agent 从 5.97→93.28（SFT warmup + GRPO + online rollouts）。GRPO 提升 16.1%，GiGPO 提升 5.1%。
- **与我们的关联**: **高度相关**。我们的 SFT warmup 已完成（exp008_sft），SPEAR 的 self-imitation 可以在此基础上进一步加强。HuggingFace 有预训练模型 `yolay/SPEAR-ALFWorld-DrBoT-GRPO-1.5B`。

### 1.4 SALT: Step-level Advantage via Trajectory Graph
- **论文**: SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph (2025, arXiv 2510.20022; EACL 2026)
- **核心方法**: 从共享同一 prompt 的多条轨迹构建图，量化每步质量，分配 step-level advantage。可作为 GRPO/RLOO 的插件。
- **ALFWorld 结果**: GRPO+SALT 81.8%→85.2% (1.5B)；RLOO+SALT 79.3%→87.3% (7B)。
- **与我们的关联**: 比 GiGPO 更轻量的 step-level credit 方案，plug-and-play。

### 1.5 GDPO: 多奖励独立归一化
- **论文**: GDPO: Group reward-Decoupled Normalization Policy Optimization (Shih-Yang Liu et al., NVIDIA, 2026, ICML; arXiv 2601.05242)
- **核心方法**: GRPO 对多维奖励求和后归一化会丢失信号分辨率（不同奖励组合坍缩为 ~2 个 advantage 组）。GDPO 对每个 reward 维度独立归一化后再组合，保留 ~3+ 个 distinct advantage groups。
- **与我们的关联**: **直接对症**。我们的 valid_action_bonus 和 success_reward 是两个维度，混合归一化后 valid 的小方差信号淹没了 success 的大方差信号。GDPO 的独立归一化可以保持两个信号的独立性。

---

## 二、GRPO 的 Reward 设计与改进

### 2.1 DAPO: Dynamic Sampling + Decoupled Clipping
- **论文**: DAPO: An Open-Source LLM Reinforcement Learning System at Scale (ByteDance, 2025; arXiv 2503.14476)
- **核心改进**:
  - **Dynamic Sampling**: 重采样直到每个 group 有非零 reward 方差（过滤零方差组避免零梯度）
  - **Clip-Higher**: 不对称 clipping（上界 1.28 vs 下界 0.8），允许更多 exploration
  - **Token-Level Loss**: 按 token 归一化而非按 sequence
  - **Overlong Reward Shaping**: truncated 输出的软惩罚
- **与我们的关联**: Dynamic Sampling 直接解决我们的零梯度问题（所有 trajectory 都失败时 advantage=0）。Clip-Higher 鼓励 exploration。

### 2.2 Scaf-GRPO: Scaffolded Hints 打破零奖励
- **论文**: Scaf-GRPO: Scaffolded Group Relative Policy Optimization (JIA Lab, 2025; ICLR 2026; arXiv 2510.19807)
- **核心方法**: 检测到 reward 停滞时，向 prompt 中注入分层提示（抽象→具体），帮助模型在 group 中产生至少一条成功轨迹，从而产生非零方差。
- **效果**: AIME24 +44.3%。
- **与我们的关联**: 可以在 ALFWorld 中注入 sub-goal hints（"先找到物品"→"去 kitchen"→具体动作序列），帮助冷启动。

### 2.3 DeepSeek-R1: 纯 Sparse Binary Reward + GRPO
- **论文**: DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via RL (DeepSeek-AI, 2025; arXiv 2501.12948)
- **Reward 设计**: 纯规则型——accuracy (binary) + format (`<think>` tags) + language consistency。**无神经网络 reward model**。
- **训练流程**: Cold-start SFT → GRPO → Rejection Sampling → 二次 GRPO。
- **关键 insight**: RLVR 用 sparse binary reward 足以涌现推理能力，但前提是模型基础能力足够强（DeepSeek-V3 67B base）。
- **与我们的关联**: 验证了 sparse reward + GRPO 的可行性，但需要足够强的 base model。我们的 Qwen3-1.7B 可能太弱，需要更强的 SFT warmup。

### 2.4 Lambda-GRPO: 隐式过程奖励
- **论文**: GRPO is Secretly a Process Reward Model (Michael Sullivan et al., 2025; ICLR 2026; arXiv 2509.21154)
- **核心发现**: GRPO + outcome reward 隐式诱导了 step-level process reward（通过共享前缀的 Monte-Carlo 采样）。Lambda-GRPO 显式利用这一结构。
- **与我们的关联**: 理论上 GRPO 已在做 process-level credit，但前提是 group 内轨迹有共享前缀后分叉。我们的 ALFWorld 每条轨迹可能差异太大，隐式 PRM 信号不足。

### 2.5 Progressive Reward Shaping (PRS) + VSPO
- **论文**: Enhancing Agentic RL with Progressive Reward Shaping and VSPO (2025; arXiv 2512.07478)
- **核心方法**: Curriculum 式密集奖励——先奖励格式正确的 tool call，再优化事实准确性和回答质量。VSPO 用 task-value metric 替换零 advantage 样本。
- **与我们的关联**: 我们已经经历了 format→valid→success 的 curriculum 需求。PRS 提供了系统化的方法。

---

## 三、ALFWorld 上的最佳结果（按 success rate 排序）

| 方法 | 模型 | ALFWorld Success | 关键技术 |
|------|------|-----------------|----------|
| DERL | 自动发现 reward | 91.8% | 可微分元优化 reward 结构 |
| AgentPRM | Llama 3.2-3B (BoN=16) | 91.0% | 过程奖励 + Best-of-N |
| SPEAR | 1.5B (SFT+GRPO) | 93.28% | Self-imitation + 渐进探索 |
| SALT+RLOO | 7B | 87.3% | 轨迹图 step-level advantage |
| SALT+GRPO | 1.5B | 85.2% | 同上，更小模型 |
| SPA-RL | - | 79.1% | Stepwise progress attribution |
| GiGPO | - | GRPO+12% | 双层 group advantage |
| EPO | - | +19.8% | 熵正则化 |

---

## 四、Reward Hacking 的理论基础与经典方案

### 4.1 PBRS: Potential-Based Reward Shaping（策略不变性保证）
- **论文**: Ng, Harada, Russell (1999, ICML)
- **定理**: F(s,s') = γΦ(s') - Φ(s) 是保持最优策略不变的**充要条件**。任何不满足此形式的 shaping 都可能改变最优策略。
- **与我们的关联**: 我们的 valid_action_bonus 不是 PBRS 形式（它只依赖当前状态，不是势差），理论上就会改变最优策略。如果用 PBRS，需要定义 Φ(s) = "距离目标的某种度量"。

### 4.2 ABC: Attention-Based Credit = PBRS
- **论文**: Dense Reward for Free in RLHF (Alex Chan et al., 2024, ICML)
- **核心方法**: 用 reward model 的 attention weights 将单一标量奖励重分配为 token-level 密集反馈。理论证明等价于 PBRS，保策略不变性。零额外计算。
- **与我们的关联**: 如果我们训练一个简单的 outcome RM，可以用 ABC 免费获得 dense reward 而不引入 gaming。

### 4.3 Skalse et al. (2022): Reward Hacking 的不可避免性
- **论文**: Defining and Characterizing Reward Hacking (NeurIPS 2022)
- **核心结论**: 对于所有随机策略，proxy reward 和 true reward 之间的 "unhackable" 关系只在 proxy 为常数时成立——即 reward hacking 理论上不可避免。但确定性策略下存在非平凡的 unhackable 对。

### 4.4 Reward Clipping / Delta 技术
- **论文**: On Designing Effective RL Reward at Training Time for LLM Reasoning (Gao & Xu, 2024; arXiv 2410.15115)
- **核心发现**: 朴素添加 PRM/ORM 奖励会**伤害**训练——LLM 利用它们重复正确但无用的推理步骤。提出 Clipping（上界截断累积 reward）和 Delta（只奖励增量进步）技术。
- **与我们的关联**: 直接适用。可以 clip valid_action_bonus 的累积上限，或只在 valid 从 False→True 时给 reward（delta）。

---

## 五、过程奖励模型（PRM）与信用分配

### 5.1 AgentPRM: Promise + Progress 双信号
- **论文**: AgentPRM: Process Reward Models for LLM Agents (Xu et al., 2025; ACM Web 2026; arXiv 2511.08325)
- **核心方法**: 每步 action 从两个维度评估——promise（距目标的前瞻概率）和 progress（相对前一步的增量贡献）。用 TD + GAE 生成标注，比 Monte Carlo 高效 8x。
- **ALFWorld 结果**: 3B 模型 + AgentPRM 超越 GPT-4o。

### 5.2 DERL: 可微分元优化 Reward 结构
- **论文**: DERL: Differentiable Evolutionary Reinforcement Learning (Sitao Cheng et al., 2025; arXiv 2512.13399)
- **核心方法**: 双层框架——Meta-Optimizer 进化 reward 函数（由结构化原子原语组合），内层策略用发现的 reward 训练，外层用任务性能作为 meta-gradient 信号。
- **ALFWorld 结果**: 91.8% (L0)，SOTA。
- **关键 insight**: 可微分元优化捕获 reward 设计与任务性能的因果关系，优于手工设计。

### 5.3 ArCHer: 层次化多轮 RL
- **论文**: ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL (Yifei Zhou et al., 2024, ICML)
- **核心方法**: 高层 off-policy value-based RL（TD learning）聚合跨 turn 的 reward；低层 token-level RL 在每个 turn 内优化，用高层 value function 作为 reward 信号。
- **效果**: 样本效率提升 ~100x。
- **与我们的关联**: 如果 GRPO 的 flat credit assignment 不够，ArCHer 的层次化方法是理论上更优的选择，但实现复杂度高。

---

## 六、探索与课程学习

### 6.1 EPO: 熵正则化策略优化
- **论文**: EPO: Entropy-regularized Policy Optimization for LLM Agents RL (Wujiang Xu et al., 2025; arXiv 2509.22576)
- **核心方法**: (1) 多轮熵正则化 (2) 熵平滑正则器限制策略熵在历史均值范围内 (3) 自适应阶段权重平衡 exploration-exploitation。
- **ALFWorld 结果**: +19.8%，OOD >0.4（baseline <0.2）。

### 6.2 CDE: Curiosity-Driven Exploration for LLM RL
- **论文**: CDE (2025; arXiv 2509.09675)
- **核心方法**: Actor curiosity = response perplexity；Critic curiosity = multi-head value 方差。轻量级 RND 替代方案。
- **效果**: GRPO/PPO 上 +3 points (AIME)。

### 6.3 AgentGym-RL: Progressive Horizon
- **论文**: AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making (Zhiheng Xi et al., 2025; arXiv 2509.08755)
- **核心方法**: ScalingInter-RL——从短 horizon 开始（密集反馈），逐步扩展到长 horizon（稀疏反馈）。隐式 reward shaping。
- **与我们的关联**: 可以先训练 5-step ALFWorld episodes，再逐步扩展到 30-step。

### 6.4 Dense2Sparse Reward Schedule
- **论文**: Dense2Sparse Reward Shaping (Yongle Luo et al., 2020)
- **核心方法**: Phase 1 用 dense reward 快速学习；Phase 2 切换到 sparse reward 消除 bias。
- **与我们的关联**: 我们可以先用 dense reward（但加 success-gating 或 clipping），在 valid rate 稳定后 anneal 掉 dense 部分。

---

## 七、对下一步实验的具体建议

基于文献分析和 exp013f 的失败模式，按**实现难度从低到高、预期收益从高到低**排序：

### 建议 1: Success-Gated Dense Reward (G-RA 式)
**优先级: 最高 | 实现: 1-2h | 预期收益: 高**

```python
# 当前（会被 gaming）:
reward = success_reward * won + valid_action_bonus * sum(valid_steps)

# 改为（G-RA 式 success-gating）:
reward = success_reward * won + valid_action_bonus * sum(valid_steps) * won
```

原理：只有成功完成任务的轨迹才能获得 dense bonus。失败轨迹的 reward 全部为 0，消除了"只做合法动作不完成任务"的 gaming 路径。文献支持：G-RA 在 SWE-bench 上 47.6%→93.8%。

**风险**: 如果 base success rate 过低（<5%），回到纯 sparse reward 的冷启动问题。需要搭配建议 3 或 4。

### 建议 2: GDPO 式多维度独立归一化
**优先级: 高 | 实现: 2-3h | 预期收益: 中高**

```python
# 当前 GRPO:
advantage = (total_reward - group_mean) / group_std

# 改为 GDPO 式:
adv_success = (success_reward_i - mean_success) / std_success  # 维度 1
adv_valid = (valid_bonus_i - mean_valid) / std_valid            # 维度 2
advantage = w_success * adv_success + w_valid * adv_valid       # 加权组合
# w_success >> w_valid（如 0.9:0.1）
```

原理：独立归一化防止低方差的 dense signal 在混合归一化中被忽略或反过来主导。GDPO 证明朴素求和后归一化会将 distinct reward 组合坍缩为 ~2 个 advantage 组。

### 建议 3: DAPO Dynamic Sampling（过滤零方差 group）
**优先级: 高 | 实现: 2-3h | 预期收益: 中**

在 GRPO 的 group sampling 中，如果一个 group 的所有轨迹 reward 相同（全失败），重新采样或跳过该 group。确保每个 training batch 都有非零 advantage 信号。

原理：exp013f 中大量 group 的 success 全为 0，advantage 退化为纯 valid bonus 的排序。Dynamic sampling 确保学习信号包含 success 维度的差异。

**注意**: 如果 base success rate <5%，重采样开销巨大。可以设一个最大重试次数（如 3 次），超过则用当前 group 但降低 learning rate。

### 建议 4: Expert Trajectory Self-Imitation (SPEAR 式)
**优先级: 高 | 实现: 半天 | 预期收益: 高**

用 GPT-4 / Claude 在 ALFWorld 上生成 50-100 条成功轨迹，混入 GRPO training：
- 每个 GRPO group 中保证至少 1-2 条 expert 轨迹作为 "anchor"
- 或者周期性做 self-imitation：收集训练过程中偶然成功的轨迹，replay 学习

原理：SPEAR 证明 self-imitation 在 ALFWorld 上提升 16.1%（GRPO）。解决冷启动问题的核心是确保 group 内有 success/failure 的差异。

### 建议 5: 渐进 Horizon + 任务难度课程
**优先级: 中 | 实现: 1 天 | 预期收益: 中**

- Phase 1: 只训练简单任务类型（如 pick_and_place，步数少）+ 短 horizon（10 步）
- Phase 2: 扩展到全部 6 种任务类型 + 中等 horizon（20 步）
- Phase 3: 全量 30 步

原理：AgentGym-RL 的 ScalingInter-RL 证明短 horizon 提供更密集的反馈，降低 credit assignment 难度。在简单任务上先建立 success signal，再泛化。

---

## 八、方法兼容性与 RAGEN 框架适配

| 方法 | 修改范围 | RAGEN 兼容性 | 备注 |
|------|---------|-------------|------|
| Success-Gated Reward | reward function 一行改动 | ✅ 直接适用 | 最小侵入 |
| GDPO 独立归一化 | advantage 计算 | ⚠️ 需改 GRPO trainer | ~50 行代码 |
| DAPO Dynamic Sampling | sampling loop | ⚠️ 需改 rollout worker | ~100 行代码 |
| SPEAR Self-Imitation | 新增 replay buffer + mixing | ⚠️ 需集成额外模块 | 可先做简化版 |
| GiGPO | 替换 GRPO trainer | ❌ 需要 verl-agent 框架 | 中期考虑 |
| Progressive Horizon | 训练 config 分阶段 | ✅ Hydra config 切换 | 无代码改动 |

---

## 九、关键参考文献索引

### 直接相关（必读）
1. G-RA (2025) — arXiv 2508.10548 — Success-gated dense reward
2. GiGPO (2025) — arXiv 2505.10978 — Step-level credit for ALFWorld
3. SPEAR (2025) — github.com/TencentYoutuResearch/SPEAR — Self-imitation on ALFWorld
4. GDPO (2026) — arXiv 2601.05242 — Multi-reward decoupled normalization
5. DAPO (2025) — arXiv 2503.14476 — Dynamic sampling + decoupled clipping
6. SALT (2025) — arXiv 2510.20022 — Trajectory graph step-level advantage
7. AgentPRM (2025) — arXiv 2511.08325 — Process reward for agents
8. DERL (2025) — arXiv 2512.13399 — Automated reward discovery (91.8% ALFWorld)

### 理论基础
9. Ng et al. (1999) — PBRS 策略不变性定理
10. Skalse et al. (2022) — arXiv 2209.13085 — Reward hacking 形式化定义
11. Gao & Xu (2024) — arXiv 2410.15115 — Dense reward clipping/delta 技术
12. Lambda-GRPO (2025) — arXiv 2509.21154 — GRPO 隐式 PRM

### GRPO 改进
13. DeepSeek-R1 (2025) — arXiv 2501.12948 — Sparse reward + GRPO pipeline
14. Scaf-GRPO (2025) — arXiv 2510.19807 — Scaffolded hints
15. PRS+VSPO (2025) — arXiv 2512.07478 — Progressive reward shaping

### 探索与正则化
16. EPO (2025) — arXiv 2509.22576 — 熵正则化 (+19.8% ALFWorld)
17. CDE (2025) — arXiv 2509.09675 — Curiosity-driven exploration for LLM RL
18. Dense2Sparse (2020) — Reward schedule 课程学习

### Agent RL 训练框架
19. RAGEN (2025) — arXiv 2504.20073 — StarPO + Echo Trap 诊断
20. RAGEN-2 (2026) — arXiv 2604.06268 — Template Collapse + SNR-Adaptive Filtering
21. ArCHer (2024) — ICML — 层次化多轮 RL
22. AgentGym-RL (2025) — arXiv 2509.08755 — Progressive horizon
23. WebAgent-R1 (2025) — arXiv 2505.16421 — Binary reward + SFT warmup 可行
24. Practitioner's Guide (2025) — arXiv 2510.01132 — Multi-turn agentic RL 实证指南

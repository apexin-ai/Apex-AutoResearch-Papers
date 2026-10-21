# Phase B Literature Survey: B-IAVR 相关文献调研

> 调研日期: 2026-05-14
> 目的: 为 B-IAVR (Budget-constrained Intelligent Adaptive Verification Ratio) Phase B 实现提供文献支撑

---

## 方向 1: Selective Verification / Adaptive Computation in Agent RL

### 1.1 Learning How Hard to Think: Input-Adaptive Allocation of LM Computation
- **作者**: Mehul Damani, Idan Shenfeld, Andi Peng, Andreea Bobu, Jacob Andreas
- **年份/Venue**: 2024, ICLR 2025
- **核心方法**: 训练 meta-predictor 估计给定 input 和 computation budget 下的 reward 分布，只在预测收益最大的 input 上分配额外计算。通过 adaptive best-of-k sampling 和 routing 实现，可减少 50% 计算量且不损失质量。
- **与 B-IAVR 的关系**: 提供了 input-adaptive 计算分配的理论框架。B-IAVR 的区别在于使用 action change 作为分配信号（而非 meta-predictor），且在 multi-step agent 执行中做决策而非单次推理。
- **arXiv**: https://arxiv.org/abs/2410.04707

### 1.2 Thinkless: LLM Learns When to Think
- **作者**: Gongfan Fang, Xinyin Ma, Xinchao Wang (NUS)
- **年份/Venue**: 2025, NeurIPS 2025
- **核心方法**: 用 RL 训练 reasoning LLM 通过 `<short>` / `<think>` 控制 token 自适应选择是否做 CoT 推理。关键算法 DeGRPO 将 mode selection 和 answer quality 的学习信号解耦。减少 50-90% 长链思维使用量。
- **与 B-IAVR 的关系**: DeGRPO 的解耦训练思路可直接借鉴——B-IAVR 也需要解耦 "是否验证" 的决策信号与 task reward。区别在于 Thinkless 是单步推理的 mode 选择，B-IAVR 是 multi-step agent 中的动态验证决策。
- **arXiv**: https://arxiv.org/abs/2505.13379

### 1.3 Learning When to Plan: Efficiently Allocating Test-Time Compute for LLM Agents
- **作者**: Davide Paglieri, Bartlomiej Cupial, Jonathan Cook 等
- **年份/Venue**: 2025, arXiv preprint
- **核心方法**: Agent 通过 SFT + RL 学习何时在 sequential decision-making 中触发 expensive planning step。首个训练 LLM agent 做动态 test-time compute 分配的工作（在 Crafter 环境验证）。
- **与 B-IAVR 的关系**: **最接近的工作**——都是 agent 学习在 sequential execution 中何时做额外计算。关键区别：(1) B-IAVR 用 action change 作为 intrinsic signal 而非纯 RL reward；(2) B-IAVR 有显式 Lagrangian budget 约束；(3) B-IAVR 的 "额外计算" 是 self-guidance verification 而非 planning。
- **arXiv**: https://arxiv.org/abs/2509.03581

---

## 方向 2: Lagrangian Budget Control in RL

### 2.1 Responsive Safety in RL by PID Lagrangian Methods
- **作者**: Adam Stooke, Joshua Achiam, Pieter Abbeel
- **年份/Venue**: 2020, ICML 2020
- **核心方法**: 将 constrained RL 建模为动态系统，Lagrange multiplier 为控制输入。传统 Lagrangian 更新等价于纯积分控制（导致振荡），加入比例和微分项（PID 控制）实现稳定约束满足。Safety Gym SOTA。
- **与 B-IAVR 的关系**: **B-IAVR Lagrangian 预算控制的直接技术基础**。建议 Phase B 实现时采用 PID Lagrangian 而非朴素的 dual gradient ascent，避免验证率振荡。
- **arXiv**: https://arxiv.org/abs/2007.03964

### 2.2 Adversarial Constrained Policy Optimization (ACPO)
- **作者**: Jianming Ma 等
- **年份/Venue**: 2024, arXiv preprint
- **核心方法**: 将 constrained RL 分为两个对抗阶段交替求解——一个优化 policy reward，另一个自适应调整 cost budget。支持同时优化 reward 和 budget adaptation。
- **与 B-IAVR 的关系**: ACPO 的 adaptive budget 思路有参考价值——B-IAVR 可以不固定验证预算，而是让 budget 本身也随训练自适应调整。
- **arXiv**: https://arxiv.org/abs/2410.20786

### 2.3 Predictive Lagrangian Optimization (PLO) for Constrained RL
- **作者**: Tianqi Zhang, Puzhen Yuan 等
- **年份/Venue**: 2025, arXiv preprint
- **核心方法**: 建立约束优化与反馈控制的通用等价框架，用 MPC 作为 feedback controller 确定 Lagrange multiplier。比 PID Lagrangian 可行域大 7.2%。
- **与 B-IAVR 的关系**: PLO 是 PID Lagrangian 的进化版本，如果 B-IAVR 的 budget 约束需要更精细控制，PLO 是备选方案。但实现复杂度更高，建议先用 PID Lagrangian。
- **arXiv**: https://arxiv.org/abs/2501.15217

---

## 方向 3: Self-Correction / Self-Verification in LLM Agents

### 3.1 SCoRe: Training Language Models to Self-Correct via Reinforcement Learning
- **作者**: Aviral Kumar, Vincent Zhuang, Rishabh Agarwal 等 (Google DeepMind)
- **年份/Venue**: 2024, ICLR 2025
- **核心方法**: 提出 multi-turn online RL 方法训练 LLM 自我纠正。解决 SFT-based self-correction 的 distribution mismatch 和 behavior collapse 问题——模型在自己生成的错误上学习纠正，通过两阶段 reward shaping。
- **与 B-IAVR 的关系**: SCoRe 证明了 RL（而非 SFT）是实现真正 self-correction 的必要手段。B-IAVR 的 self-guidance 机制本质上也是一种 self-correction，但 B-IAVR 进一步解决 "何时做" 的问题（SCoRe 是 always-on 的两轮纠正）。
- **arXiv**: https://arxiv.org/abs/2409.12917

### 3.2 Self-Challenging Language Model Agents
- **作者**: Yifei Zhou, Sergey Levine, Jason Weston, Xian Li, Sainbayar Sukhbaatar (UC Berkeley, Meta FAIR)
- **年份/Venue**: 2025, arXiv preprint
- **核心方法**: Agent 在 challenger 和 executor 角色间交替——challenger 生成带验证函数的 multi-step 任务，executor 用 RL 在执行反馈上训练。Self-play loop 在 M3ToolEval/TauBench 上提升 >2x。
- **与 B-IAVR 的关系**: Self-generated verification function 的思路与 B-IAVR 的 self-guidance verifier 有共通之处。区别在于 B-IAVR 的验证是在执行过程中实时触发的，而非训练数据生成阶段。
- **arXiv**: https://arxiv.org/abs/2506.01716

### 3.3 Agent-R1: Training Powerful LLM Agents with End-to-End Reinforcement Learning
- **作者**: Mingyue Cheng, Jie Ouyang 等
- **年份/Venue**: 2025, arXiv preprint
- **核心方法**: 模块化 end-to-end RL 框架，扩展标准 MDP 处理 multi-turn agent-environment 交互（tool calls、retrieval）。兼容 PPO/GRPO，训练 agent 学习何时以及如何调用工具并跨步骤自纠正。
- **与 B-IAVR 的关系**: Agent-R1 的 GRPO 兼容框架可作为 B-IAVR 实现的工程参考。B-IAVR 在此基础上增加了 selective verification 的决策维度和 budget 约束。
- **arXiv**: https://arxiv.org/abs/2511.14460

---

## 方向 4: Behavioral Change as Intrinsic Signal

### 4.1 Self-Supervised Exploration via Disagreement
- **作者**: Deepak Pathak, Dhiraj Gandhi, Abhinav Gupta
- **年份/Venue**: 2019, ICML 2019
- **核心方法**: 训练 forward dynamics model ensemble，用预测 disagreement（方差）作为 intrinsic reward。模型预测分歧最大的状态被视为最有信息价值，驱动探索。对 stochastic environment 鲁棒。
- **与 B-IAVR 的关系**: 概念上的先驱——B-IAVR 用 "action change after self-guidance" 作为信号，类似于 disagreement 信号。区别在于 B-IAVR 的 disagreement 是同一 policy 干预前后的行为差异，而非 ensemble 之间的差异。
- **arXiv**: https://arxiv.org/abs/1906.04161

### 4.2 Plan2Explore: Planning to Explore via Self-Supervised World Models
- **作者**: Ramanan Sekar, Oleh Rybkin, Kostas Daniilidis, Pieter Abbeel, Danijar Hafner, Deepak Pathak
- **年份/Venue**: 2020, ICML 2020
- **核心方法**: 将 disagreement-based exploration 扩展到 model-based planning 框架。Agent 主动规划轨迹以最大化 *未来预期 disagreement*——前瞻性地利用行为分歧信号。
- **与 B-IAVR 的关系**: Plan2Explore 的前瞻性 disagreement 思路启发性强——B-IAVR 可以考虑不仅根据当前 action change 决定验证，还预测未来哪些步骤的 action change 可能更大。但这增加了实现复杂度，建议作为 future work。
- **arXiv**: https://arxiv.org/abs/2005.05960

### 4.3 Causal Influence Detection for Improving Efficiency in RL
- **作者**: Maximilian Seitzer, Bernhard Schölkopf, Georg Martius
- **年份/Venue**: 2021, NeurIPS 2021
- **核心方法**: 定义 situation-dependent 的 causal action influence (CAI)——基于状态转移动态的条件互信息量化 agent action 对下一状态的因果影响。用于引导探索和优先采样 high-influence transition。
- **与 B-IAVR 的关系**: **概念上最接近 B-IAVR 的 action change 信号**。CAI 度量 "action 是否真正改变了 outcome"，B-IAVR 度量 "self-guidance 是否改变了 action"。两者都是 counterfactual behavioral change 的度量，但方向相反：CAI 是 action→state 的因果影响，B-IAVR 是 verification→action 的因果影响。
- **arXiv**: https://arxiv.org/abs/2106.03443

---

## 综合分析: B-IAVR 的文献定位与 Novelty

### B-IAVR 的独特贡献

B-IAVR 处于上述四个方向的交汇点，其核心 novelty 在于**三个组件的联合**，而非任何单一组件：

| 组件 | 最近的已有工作 | B-IAVR 的区别 |
|------|--------------|--------------|
| Selective verification in agent execution | Learning When to Plan (Paglieri 2025) | 使用 action change 作为 intrinsic trigger 而非纯 RL signal |
| Lagrangian budget constraint | PID Lagrangian (Stooke 2020) | 约束的是 verification ratio 而非 safety cost |
| Action change as decision signal | Causal Influence Detection (Seitzer 2021) | 度量 verification→action 而非 action→state 的因果影响 |
| Self-correction via RL | SCoRe (Kumar 2024) | Selective 而非 always-on；budget-aware |

**核心 novelty statement**: B-IAVR 是首个将 behavioral change signal (action change after self-guidance) 与 Lagrangian budget control 结合，训练 agent 在 multi-step execution 中学习 selective verification 的方法。

### Phase B 实现的文献对标建议

1. **Lagrangian 实现**: 采用 PID Lagrangian (Stooke 2020) 作为 budget controller，避免朴素 dual ascent 的振荡问题。若效果不佳再考虑 PLO。
2. **训练框架**: 参考 DeGRPO (Thinkless, Fang 2025) 的解耦思路，将 verification decision 的学习与 task performance 的学习分离。
3. **Baseline 对比**: 
   - Always-on self-guidance (Phase A, 对标 SCoRe 的 always-verify)
   - Random verification (uniform random 选择何时验证)
   - Fixed-ratio verification (固定比例验证)
   - Learning When to Plan 的 SFT+RL pipeline（如可复现）
4. **Evaluation metrics**: 除 task success rate 外，需报告 verification ratio、budget utilization、action change frequency，对标 Thinkless 的 thinking ratio 指标。
5. **Action change signal 的理论依据**: 可引用 Causal Influence Detection (Seitzer 2021) 建立 action change 作为 intrinsic signal 的理论联系，但需明确 B-IAVR 度量的是反向因果关系。

# Related Work Survey — B-IAVR Project

> 调研日期: 2026-05-15 | 覆盖范围: 2024-2026

---

## 1. Self-verification / Self-correction in LLM Agents

### 1.1 Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide) (arXiv 2025)
- **作者**: (见 arXiv 2604.03098)
- **arXiv**: 2604.03098
- **核心方法**: 提出 Self-Guide，agent 在推理时生成短 self-guidance signal 指导下一步 action，训练时将同一 signal 转为 step-level internal reward 用于 GRPO 优化。形成 co-evolving loop：better policy → better guidance → better internal reward → better policy。在 ALFWorld 等三个 agent benchmark 上，inference-time guidance 已有明显提升，联合 GRPO 训练进一步提升 8%。
- **与我们的关系**: **强竞争 / 直接对标** — B-IAVR 基于 Self-Guide 框架
- **关键差异**: Self-Guide 是 always-on verification（每步都生成 guidance），不区分"何时值得验证"。B-IAVR 学习 selective verification policy，仅在 verification informative 时触发。Self-Guide 的 reward 来自 guidance 与 outcome 的 co-evolution，B-IAVR 用 action change 作为 verification informativeness 的 reward signal。
- **可借鉴点**: (1) co-evolving policy + reward 的框架设计 (2) step-level internal reward 的具体实现方式 (3) ALFWorld 上的实验设置和 baseline 数据

### 1.2 S²R: Teaching LLMs to Self-verify and Self-correct via Reinforcement Learning (ACL 2025)
- **作者**: Ruotian Ma, Peisong Wang, Cheng Liu, Xingyan Liu, Jiaqi Chen, Bang Zhang, Xin Zhou, Nan Du, Jia Li
- **arXiv**: 2502.12853
- **核心方法**: 两阶段：(1) SFT 用 3.1k 样本初始化 self-verify + self-correct 行为 (2) outcome-level 和 process-level RL 强化这两个能力。Qwen2.5-math-7B 从 51.0% 提升到 81.6%，超过等量 long-CoT distilled data 训练的模型。
- **与我们的关系**: 互补 / 可借鉴
- **关键差异**: S²R 聚焦 math reasoning，self-correction 是对推理结果的修正；B-IAVR 聚焦 interactive agent 的 action-level verification，且核心创新是 selective（学习何时验证），S²R 未涉及选择性问题。S²R 使用 SFT 初始化 + RL 强化的两阶段方法，B-IAVR 使用纯 RL（GRPO）。
- **可借鉴点**: (1) SFT 初始化 self-verification 行为的 cold-start 策略 (2) process-level RL 的设计（可作为 B-IAVR 的 step-level reward 参考）

### 1.3 SCoRe: Training Language Models to Self-Correct via Reinforcement Learning (Google, 2024)
- **作者**: Aviral Kumar, Vincent Zhuang, Rishabh Agarwal 等 (Google DeepMind)
- **arXiv**: 2409.12917
- **核心方法**: Multi-turn online RL，在模型自身生成的 correction traces 上训练。包含两阶段：初始 multi-turn RL on base model 生成 policy initialization（抗 collapse），再用 reward bonus 放大 self-correction。Gemini 1.0 Pro/1.5 Flash 上 self-correction 提升 15.6%/9.1%（MATH/HumanEval）。
- **与我们的关系**: 互补 / 可借鉴
- **关键差异**: SCoRe 训练模型"如何更好地 self-correct"（always-on），B-IAVR 训练模型"何时触发 verification"（selective）。SCoRe 面向静态 reasoning task，B-IAVR 面向 interactive agent。SCoRe 的 reward bonus 机制与 B-IAVR 的 action-change reward 目标不同。
- **可借鉴点**: (1) multi-turn RL 防止 policy collapse 的初始化策略 (2) on-policy correction traces 的训练范式

### 1.4 Trust, But Verify (RISE): A Self-Verification Approach to RLVR (NeurIPS 2025)
- **作者**: (见 arXiv 2505.13445)
- **arXiv**: 2505.13445
- **核心方法**: 提出 RISE，在 online RL 中同时训练 problem-solving 和 self-verification。每轮迭代：模型生成 solutions → 自我 critique on-policy solutions → 两类 trajectories 共同更新 policy。用 verifiable rewards 同时监督 solution generation 和 self-verification。
- **与我们的关系**: 竞争 / 可借鉴
- **关键差异**: RISE 将 verification 作为 joint training objective 但不区分"何时验证"；B-IAVR 核心是学习 when to verify。RISE 面向 math reasoning + RLVR，B-IAVR 面向 interactive agent。RISE 的 verification target 是 solution correctness，B-IAVR 的是 action informativeness。
- **可借鉴点**: (1) joint training solver + verifier 的框架 (2) on-the-fly feedback for verification 的设计

### 1.5 Incentivizing LLMs to Self-Verify Their Answers (arXiv 2025)
- **作者**: Fuxiang Zhang, Jiacheng Xu, Chaojie Wang, Ce Cui, Yang Liu, Bo An
- **arXiv**: 2506.01369
- **核心方法**: 在单一 RL 过程中统一 answer generation 和 verification training。设计 online policy-aligned buffer 和 dynamic verification rewards 稳定联合训练。训练后的模型可在推理时自我验证，无需外部 verifier。
- **与我们的关系**: 竞争 / 互补
- **关键差异**: 该工作统一 generation 和 verification 训练，但验证是 always-on 的（训练后的模型总是验证自己的输出）；B-IAVR 的核心创新是 selective verification。该工作面向 reasoning，B-IAVR 面向 interactive agent。
- **可借鉴点**: (1) policy-aligned buffer 的设计 (2) dynamic verification reward 的稳定训练技巧

### 1.6 Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking (arXiv 2026)
- **作者**: Quanyu Long, Kai Jie Jiang, Jianda Chen, Xu Guo, Leilei Gan, Wenya Wang
- **arXiv**: 2602.03485
- **核心方法**: 大规模实证分析发现 LRM 中大量 self-verification steps 是 confirmatory 而非 corrective，实际很少改变推理结果。提出 experience-driven test-time framework：检测 recheck 行为激活 → 查询离线经验池 → 估计 recheck 是否可能无用 → 选择性抑制。
- **与我们的关系**: **高度相关 / 互补** — 核心问题一致
- **关键差异**: 该工作是 test-time framework（不训练，基于检索经验池决定是否 recheck），B-IAVR 是 RL-trained policy（训练模型内化何时验证的决策）。该工作面向 reasoning chains 中的 recheck steps，B-IAVR 面向 interactive agent 的 action verification。该工作的"有用性"指标是 recheck 是否改变结论，与 B-IAVR 的 action change signal 思路相似但层级不同。
- **可借鉴点**: (1) "大多数 verification 是 confirmatory" 的实证发现可作为 B-IAVR motivation 的有力支持 (2) experience-driven suppression 的思路可作为 B-IAVR 的 test-time baseline

### 1.7 When Does Verification Pay Off? A Closer Look at LLMs as Solution Verifiers (arXiv 2025)
- **作者**: Jack Lu, Ryan Teehan, Jinran Jin, Mengye Ren (NYU)
- **arXiv**: 2512.02304
- **核心方法**: 系统研究 37 个模型 × 9 个 benchmark 上 verification 的收益。提出 verifier gain 指标（比 verification accuracy 更完整）。发现 self-verification/同族 verification 的 gain 低于跨族 verification；solver 和 verifier 的 solution distribution 越相似，gain 越低。
- **与我们的关系**: 互补 — 提供理论和实证基础
- **关键差异**: 该工作是 empirical study，不训练 verification policy；B-IAVR 是 RL 训练框架。该工作面向 static task verification，B-IAVR 面向 interactive agent 的 action verification。
- **可借鉴点**: (1) verifier gain 指标可用于评估 B-IAVR 的 verification 效果 (2) "self-verification gain 较低"的发现解释了为什么 selective verification 比 always-on 更优 (3) 实验设计和评估方法论

### Gap 分析
- **空白**: 现有 self-verification 工作几乎全部是 always-on（S²R, SCoRe, RISE, Self-Guide, Incentivizing LLMs）或 test-time heuristic（Self-Verification Dilemma）。**没有工作用 RL 训练 selective verification policy**——即学习 "when to verify" 而非 "how to verify"。
- **B-IAVR 填补的空白**: (1) 首个 RL-trained selective verification policy for interactive agents (2) 首次提出 action change 作为 verification informativeness 的 reward signal (3) 将 verification 从 always-on 转为 cost-aware 的 adaptive decision
- **Novelty claim 定位**: B-IAVR 在 "how to verify"（已被大量研究）和 "when to verify"（几乎空白）之间架起桥梁。Self-Verification Dilemma 提供了 "overused checking" 的 problem motivation，B-IAVR 提供了 learning-based solution。

---

## 2. RL for Interactive Agents (ALFWorld / WebShop / TextWorld)

### 2.1 Group-in-Group Policy Optimization (GiGPO) for LLM Agent Training (NeurIPS 2025)
- **作者**: Lang Feng 等
- **arXiv**: 2505.10978
- **核心方法**: 在 GRPO 基础上引入两级优势估计：episode-level macro advantage（基于完整 trajectory 组）+ step-level micro advantage（通过 anchor state grouping 追溯构建 step-level 组）。在 ALFWorld 上比 GRPO 提升 >12%，WebShop 上提升 >9%，保持相同 GPU 内存开销。基于 Qwen2.5-1.5B/3B/7B-Instruct。
- **与我们的关系**: 互补 / 可借鉴
- **关键差异**: GiGPO 解决 credit assignment 问题（如何分配 reward），B-IAVR 解决 verification timing 问题（何时验证）。两者正交，可组合使用。
- **可借鉴点**: (1) step-level credit assignment 的 anchor state grouping 机制 (2) ALFWorld/WebShop 上的 GRPO baseline 数据（直接可比） (3) verl-agent 框架

### 2.2 SPEAR: Self-imitation with Progressive Exploration for Agentic RL (ICLR 2026)
- **作者**: (Tencent Youtu Research)
- **arXiv**: 2509.22601
- **核心方法**: 在 SIL（Self-Imitation Learning）基础上，通过 progressive exploration-exploitation balance 解决 multi-turn RL 的不稳定性。早期用 auxiliary tool call reward 积累 tool-use skills + 上升 entropy trend，后期加强 self-imitation 利用成功经验。ALFWorld 上将 GRPO/GiGPO 分别提升 16.1%/5.1%，WebShop 上提升 20.7%/11.8%。
- **与我们的关系**: 互补 / 可借鉴
- **关键差异**: SPEAR 解决 exploration-exploitation balance 和训练稳定性，B-IAVR 解决 verification policy learning。B-IAVR 可将 SPEAR 的稳定性技巧整合进 GRPO 训练。
- **可借鉴点**: (1) progressive entropy management 策略 (2) auxiliary tool call reward 的设计 (3) ALFWorld/WebShop 的最新 SOTA 数据

### 2.3 A Practitioner's Guide to Multi-turn Agentic Reinforcement Learning (arXiv 2025)
- **作者**: Ruiyi Wang, Prithviraj Ammanabrolu
- **arXiv**: 2510.01132
- **核心方法**: 系统拆解 multi-turn agentic RL 的设计空间为 environment / reward / policy 三个维度。在 TextWorld、ALFWorld、SWE-gym 上进行大规模实证研究。7 个主要发现：multi-turn RL 性能随环境复杂度 scale；简单环境训练可泛化到复杂环境；dense turn-level reward 加速训练；biased 和 unbiased 算法都能稳定学习。
- **与我们的关系**: 互补 — 提供方法论参考
- **关键差异**: 该工作是 systematic study，不提出新算法；B-IAVR 提出新的 verification policy + reward signal。
- **可借鉴点**: (1) dense turn-level reward 的设计建议（B-IAVR 的 action change reward 可视为一种 dense signal） (2) SFT:RL ratio 的 optimal balance (3) TextWorld/ALFWorld 的实验方法论和 baseline

### 2.4 Self-Distilled Agentic Reinforcement Learning (SDAR) (arXiv 2026)
- **作者**: (ZJU REAL Lab)
- **arXiv**: 2605.15155
- **核心方法**: 将 On-Policy Self-Distillation (OPSD) 与 RL 结合。SDAR 用 sigmoid gate 将 teacher 的 token-level signals 映射到 gated auxiliary objective，加强 teacher-endorsed positive-gap tokens 的 distillation，软性衰减 negative teacher rejections。ALFWorld +9.4%，WebShop-Acc +10.2%（vs GRPO）。
- **与我们的关系**: 互补 / 可借鉴
- **关键差异**: SDAR 通过 self-distillation 增强 RL 训练信号密度，B-IAVR 通过 verification action change 增强。两者解决不同层面的问题。
- **可借鉴点**: (1) gated distillation 处理 noisy teacher signal 的方法 (2) Qwen2.5/Qwen3 在 ALFWorld 上的最新实验数据

### 2.5 Agent-R1: Training Powerful LLM Agents with End-to-End Reinforcement Learning (arXiv 2025)
- **作者**: Mingyue Cheng 等
- **arXiv**: 2511.14460
- **核心方法**: 提出 modular RL framework，将 MDP 框架系统扩展到 LLM agent 场景（multi-turn, tool-use, imperfect info）。兼容多种 RL 算法，在 multihop QA 上验证。
- **与我们的关系**: 互补 — 框架层面
- **关键差异**: Agent-R1 是通用 agentic RL 框架，不涉及 verification；B-IAVR 聚焦 verification policy 的 RL 训练。
- **可借鉴点**: (1) MDP 扩展到 agent 场景的形式化方法 (2) multi-turn RL 的工程实现

### 2.6 SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning (arXiv 2026)
- **作者**: (AIMING Lab)
- **arXiv**: 2602.08234
- **核心方法**: 自动 skill discovery + recursive evolution。将成功 trajectories 蒸馏为 strategic patterns，失败的蒸馏为 lessons。构建 hierarchical skill library (SkillBank)，包含 General Skills 和 Task-Specific Skills。ALFWorld/WebShop 上超过 strong baselines >15.3%。
- **与我们的关系**: 互补
- **关键差异**: SkillRL 学习 reusable skills/heuristics，B-IAVR 学习 verification policy。SkillRL 的 skill library 可能包含 verification 相关的 skill，但不是显式学习 "when to verify"。
- **可借鉴点**: (1) 从失败 trajectories 学习 lessons 的方法（可用于理解 B-IAVR 中 verification 失败的 patterns）

### 2.7 Reinforcement World Model Learning (RWML) for LLM-based Agents (arXiv 2026)
- **作者**: Xiao Yu, Baolin Peng, Ruize Xu, Yelong Shen 等
- **arXiv**: 2602.05842
- **核心方法**: 自监督方法，训练 action-conditioned world models。对齐模型预测的 next state 和环境实际 next state（在 pre-trained embedding space 中）。ALFWorld 上结合 task-success reward 比纯 RL 高 6.9 points。
- **与我们的关系**: 互补
- **关键差异**: RWML 学习 world model 来辅助 policy，B-IAVR 学习 verification policy。RWML 的 world model 可以为 B-IAVR 提供"预测 next state"的能力，但 B-IAVR 不依赖显式 world model。
- **可借鉴点**: (1) sim-to-real gap reward 的设计 (2) semantic equivalence vs token-level fidelity 的对比思路

### Gap 分析
- **空白**: 现有 RL for interactive agents 工作集中在 (a) 更好的 credit assignment（GiGPO）(b) 更好的 exploration（SPEAR）(c) 更丰富的训练信号（SDAR, RWML）。**没有工作将 verification 作为 agent 的可学习 action**，也没有工作将 verification timing 作为 RL 训练目标。
- **B-IAVR 填补的空白**: 在 ALFWorld 生态中引入 learned verification policy 这一新维度。Verification 不是训练技巧（如 reward shaping），而是 agent 的一个 actionable capability。
- **Novelty claim 定位**: GiGPO/SPEAR/SDAR 都在优化 "how to act better"，B-IAVR 在优化 "when to check before acting"。这是 ALFWorld RL 训练文献中尚未被探索的方向。

---

## 3. Cost-aware / Selective Computation in LLMs

### 3.1 When To Solve, When To Verify: Compute-Optimal Problem Solving and Generative Verification (ICML 2025)
- **作者**: Nishad Singhi 等
- **arXiv**: 2504.01005
- **核心方法**: 在有限 inference budget 下，分析如何在 Self-Consistency (生成更多 solutions) 和 GenRM (verification) 之间最优分配 compute。发现 sampling 太少降低 coverage，verification 太少降低 precision，存在 optimal allocation。
- **与我们的关系**: **高度相关 / 理论基础**
- **关键差异**: 该工作是 compute-allocation analysis for static reasoning tasks，不涉及 interactive agent 也不用 RL 训练 allocation policy。B-IAVR 将类似的 "when to verify" 问题放到 interactive agent 场景中，并用 RL 训练 selective policy。
- **可借鉴点**: (1) solve-vs-verify tradeoff 的理论框架可作为 B-IAVR 的 motivation (2) compute-optimal 分析方法可用于评估 B-IAVR 的 verification frequency

### 3.2 Thinkless: LLM Learns When to Think (NeurIPS 2025)
- **作者**: Gongfan Fang, Xinyin Ma, Xinchao Wang (NUS)
- **arXiv**: 2505.13379
- **核心方法**: 训练 LLM 用两个 control tokens 自适应选择 short-form 或 long-form reasoning。提出 Decoupled Group Relative Policy Optimization (DeGRPO)，将 control token loss 和 response loss 解耦。减少 long-chain thinking 50%-90%，部分 benchmark 上准确率还提升。
- **与我们的关系**: **高度相关 / 方法论最相近**
- **关键差异**: Thinkless 学习 "when to think more"（token-level），B-IAVR 学习 "when to verify"（action-level in interactive agent）。Thinkless 的决策单位是 reasoning mode（short vs long），B-IAVR 的决策单位是 verification action（verify vs not verify）。Thinkless 面向 static reasoning，B-IAVR 面向 interactive agent。
- **可借鉴点**: (1) DeGRPO 中 control token loss 解耦的设计——可直接应用于 B-IAVR 的 verification token training (2) control token 作为 adaptive computation gate 的范式

### 3.3 Learning When to Think: Shaping Adaptive Reasoning via Multi-Stage RL (AutoThink) (arXiv 2025)
- **作者**: (见 arXiv 2505.10832)
- **arXiv**: 2505.10832
- **核心方法**: Multi-stage RL framework (AutoThink)，通过 stage-wise reward shaping 逐步优化 reasoning policy。模型学习仅在必要时触发 explicit reasoning，简单任务默认 succinct response。DeepSeek-R1-Distill-Qwen-1.5B 上 relative accuracy +6.4%，token 使用 -52%。
- **与我们的关系**: 互补 / 方法论可借鉴
- **关键差异**: AutoThink 的 "when to think" 是 reasoning depth 的选择，B-IAVR 的 "when to verify" 是 verification action 的选择。AutoThink 面向 reasoning，B-IAVR 面向 interactive agent。
- **可借鉴点**: (1) multi-stage reward shaping 策略 (2) progressive training curriculum

### 3.4 SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning (arXiv 2025)
- **作者**: (见 arXiv 2505.11274)
- **arXiv**: 2505.11274
- **核心方法**: 双阶段训练：cold-start 阶段学习根据 query 预估 token budget，RL 阶段用 budget-guided GRPO 训练模型自主规划 budget 并遵守。显著减少 response 长度同时保持或提升准确率。
- **与我们的关系**: 互补
- **关键差异**: SelfBudgeter 控制 reasoning token 预算，B-IAVR 控制 verification action 的触发。SelfBudgeter 的 budget 是 token 数量，B-IAVR 的 "budget" 是 verification frequency。
- **可借鉴点**: (1) cold-start 阶段预估 budget 的设计（可用于 B-IAVR 的 verification probability 初始化）(2) budget-guided GRPO

### 3.5 Dynamic Early Exit in Reasoning Models (arXiv 2025)
- **作者**: (见 arXiv 2504.15895)
- **arXiv**: 2504.15895
- **核心方法**: 无需额外训练，在 reasoning transition points 监控模型行为，当模型对 trial answer 有高 confidence 时动态终止 next reasoning chain 生成。CoT 长度减少 31%-43%，准确率提升 1.7%-5.7%。
- **与我们的关系**: 互补
- **关键差异**: Dynamic Early Exit 是 training-free 的 heuristic method，B-IAVR 是 RL-trained policy。Dynamic Early Exit 的判断基于 confidence heuristic，B-IAVR 基于 learned verification policy。
- **可借鉴点**: (1) "confidence at transition points" 的信号设计 (2) 可作为 B-IAVR 的 non-learned baseline

### 3.6 Adaptive Test-Time Compute Allocation via Constrained Policy Optimization (arXiv 2026)
- **作者**: Zhiyuan Zhai, Bingcong Li, Bingnan Xiao, Ming Li, Xin Wang
- **arXiv**: 2604.14853
- **核心方法**: 将 adaptive compute allocation 形式化为 constrained optimization（最大化 expected accuracy，约束 average compute budget）。两阶段 Solve-then-Learn pipeline。解决 uniform budget 浪费问题：简单问题消耗与难题相同资源。
- **与我们的关系**: 互补 / 理论框架可借鉴
- **关键差异**: 该工作在 reasoning task 上分配 compute budget，B-IAVR 在 interactive agent 上分配 verification compute。两者都面向 "adaptive resource allocation" 但应用场景不同。
- **可借鉴点**: (1) constrained optimization 框架——B-IAVR 的 verification cost budget 可类似形式化 (2) Solve-then-Learn pipeline 思路

### 3.7 Putting the Value Back in RL (RLV): Unifying LLM Reasoners with Verifiers (arXiv 2026)
- **作者**: Sareen, Moss 等 (Microsoft Research)
- **arXiv**: 2505.04842
- **核心方法**: 在 RL 训练中同时训练 LLM 作为 reasoner 和 generative verifier。利用 RL 生成的 abundant data 训练 verification 能力，无显著额外开销。MATH 上 parallel sampling 准确率提升 >20%，8-32x efficient test-time compute scaling。
- **与我们的关系**: 互补 / 可借鉴
- **关键差异**: RLV 在 reasoning 场景中 jointly train reasoner + verifier（always-on verification at test time），B-IAVR 在 interactive agent 场景中 train selective verification policy。RLV 关注 "how to verify better"，B-IAVR 关注 "when to verify"。
- **可借鉴点**: (1) 利用 RL-generated data 训练 verifier 的思路——B-IAVR 可借鉴这种 data-efficient 方法 (2) reasoner + verifier joint training 的 loss 设计

### 3.8 Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking (arXiv 2026)
- *(已在 1.6 详述，此处标注跨线相关性)*
- **与线 3 的关系**: 该工作实证证明了 "大多数 verification 是浪费的"（confirmatory 而非 corrective），直接支持 cost-aware / selective verification 的必要性。是 B-IAVR 的核心 motivation paper 之一。

### Gap 分析
- **空白**: Cost-aware computation 工作集中在两类：(a) reasoning depth/token budget 控制（Thinkless, AutoThink, SelfBudgeter, Dynamic Early Exit）(b) solve-vs-verify compute allocation（When To Solve When To Verify, RLV）。**没有工作将 cost-aware 思想应用到 interactive agent 的 verification decision**，也没有工作用 action change 作为 verification cost-benefit 的评价信号。
- **B-IAVR 填补的空白**: (1) 将 "when to compute more" 从 reasoning depth 扩展到 agent verification action (2) 用 action change 作为 verification informativeness 的天然 cost-benefit signal（action 没变 = verification 没信息价值 = 计算浪费）
- **Novelty claim 定位**: Thinkless 回答 "when to think deeper"，When To Solve When To Verify 回答 "solve vs verify 的 optimal ratio"，B-IAVR 回答 "when to verify in interactive agents"。三者在 selective computation 的谱系上互补，B-IAVR 是唯一面向 interactive agent 场景的。

---

## 4. 综合定位

### B-IAVR 的独特贡献（综合三条线的 gap）

1. **首个 RL-trained selective verification policy for interactive agents**: 线 1 的 self-verification 工作都是 always-on；线 3 的 cost-aware 工作都面向 static reasoning。B-IAVR 首次在 interactive agent 场景中用 RL 训练 "when to verify"。

2. **Action change 作为 verification informativeness 的 reward signal**: 这是全新的 reward design。现有工作的 verification reward 要么基于 outcome correctness（RISE, S²R），要么基于 confidence heuristic（Dynamic Early Exit），要么基于 compute budget（SelfBudgeter）。B-IAVR 的 action change 信号是直接衡量 verification 是否影响 agent 后续行为的天然指标。

3. **Cost-benefit framing for agent verification**: 将 verification 从 "accuracy tool" 重新定义为 "cost-benefit decision"。When To Solve When To Verify 在 reasoning 中做了类似分析，B-IAVR 在 interactive agent 中做了实践。

### 最强竞争对手分析

| 竞争对手 | 威胁程度 | 核心差异 |
|---------|---------|---------|
| **Self-Guide** (2604.03098) | ★★★★★ | 直接基础框架。B-IAVR 的增量创新需清晰论证 selective > always-on |
| **Thinkless** (2505.13379) | ★★★★☆ | 方法论最相近（RL-trained "when to X"），但面向 reasoning 不是 agent |
| **Self-Verification Dilemma** (2602.03485) | ★★★☆☆ | Problem motivation 高度重叠，但 solution 不同（heuristic vs learned） |
| **RISE** (2505.13445) | ★★★☆☆ | Joint train solver + verifier，但不是 selective |
| **When To Solve When To Verify** (2504.01005) | ★★★☆☆ | Theoretical framing 相近，但面向 static reasoning |

### 建议的 Related Work 叙事结构

1. **Self-verification in LLM agents** — 从 SCoRe/S²R 的 self-correction 到 Self-Guide 的 agent self-guidance，指出现有方法均为 always-on verification。引出 Self-Verification Dilemma 的实证发现：大多数 verification 是浪费的。

2. **RL for interactive agents** — 从 GRPO 到 GiGPO/SPEAR/SDAR 的进展，指出 credit assignment、exploration、dense reward 等问题被充分研究，但 verification as learnable action 尚未被探索。

3. **Cost-aware / selective computation** — 从 Thinkless/AutoThink 的 adaptive reasoning depth 到 When To Solve When To Verify 的 compute allocation，指出 "when to compute more" 的思想尚未被应用到 interactive agent verification。

4. **Our work: B-IAVR** — 位于三条线的交汇处：(a) 从线 1 继承 self-verification 能力 (b) 在线 2 的 ALFWorld/GRPO 生态中实现 (c) 用线 3 的 cost-aware 思想指导 selective verification policy。

# 文献调研：LLM Agent Catastrophic Failure / Death Avoidance 机制

**日期**: 2026-05-13
**目的**: 调研是否有论文发现过类似 "deterministic computation 的优势主要来自 death avoidance" 的现象

---

## 一、直接相关论文（ScienceWorld 上的 Agent 方法）

### 1. SwiftSage (Lin et al., NeurIPS 2023)
- **标题**: SwiftSage: A Generative Agent with Fast and Slow Thinking for Complex Interactive Tasks
- **Venue**: NeurIPS 2023
- **ScienceWorld 成绩**: 84.7 avg score（SOTA at the time）
- **与我们的关系**: 最直接的架构类比——Swift（小模型行为克隆）+ Sage（GPT-4 慢思考）的双模块路由。Sage 模块在 Swift 失败时介入，本质上也是一种 failure recovery 机制。但 **没有量化分析** fast/slow 切换的收益来自 failure avoidance vs positive guidance。
- **定位**: 互补/背景。SwiftSage 证明了双模块路由在 ScienceWorld 上有效，但没做我们的 decomposition 分析。

### 2. CogRouter (arXiv 2602.12662)
- **ScienceWorld 成绩**: Score=84.6, SR=72.0%
- **方法**: Qwen2.5-7B，路由 thinking depth（4 levels），用 CoPO (RL) 训练
- **与我们的关系**: 路由 thinking depth 而非 internal/deterministic modality。没有 death avoidance 分析，没有 counterfactual decomposition。
- **定位**: 背景/对标。不同路由维度，不竞争。

### 3. ITP-R (arXiv 2601.08955)
- **ScienceWorld 成绩**: SR=63.91%（低于 CogRouter）
- **方法**: Learned world model + K-head gating
- **与我们的关系**: 路由到 approximate LLM world model（而非 deterministic simulator），有 compounding error 问题。没有 death avoidance 分析。
- **定位**: 背景。说明 approximate world model 不如 exact simulation。

### 4. MTRouter (Zhang et al., ACL 2026)
- **标题**: MTRouter: Cost-Aware Multi-Turn LLM Routing with History–Model Joint Embeddings
- **ScienceWorld 成绩**: 53.8 avg（超过 GPT-5 的 48.4，成本降 58.7%）
- **与我们的关系**: 多模型路由（不同 LLM 之间），非 LLM vs deterministic 路由。但在 ScienceWorld 上有结果，是 routing 方向的 concurrent work。
- **定位**: 背景。不同路由目标（cost-aware multi-model vs safety-aware modality）。

### 5. BEACON (Milestone-Guided Policy Learning, 2025-2026)
- **方法**: Trajectory-level RL，milestone-based credit assignment
- **与我们的关系**: 解决 credit misattribution 问题（正确的早期动作被 terminal failure 惩罚）。与我们的发现呼应——ScienceWorld 的稀疏奖励导致 credit assignment 困难。但关注 RL 训练效率，非 routing。
- **定位**: 互补。他们的 credit misattribution 问题正是我们的 death-dominated signal 的另一面。

### 6. ScienceWorld 原始论文 (Wang et al., EMNLP 2022)
- **标题**: ScienceWorld: Is your Agent Smarter than a 5th Grader?
- **奖励结构**: 完成所有 subgoals = 100 分，稀疏奖励（多数步骤 reward=0）。
- **关于 -100 penalty**: 搜索未找到原始论文明确讨论 -100 death penalty 的设计意图。需要直接查看源码确认 penalty 结构。
- **定位**: 基础背景。

---

## 二、Tool Use Learning 文献

### 7. Toolformer (Schick et al., NeurIPS 2023)
- **方法**: Self-supervised tool-use learning，通过 API call insertion + loss reduction filtering
- **与我们的关系**: 标准 tool-use learning baseline。差异：(1) 我们用 environment forking 做 hindsight counterfactual labeling（不是 self-supervised），(2) 我们的 framing 是 safety-aware（不是 general tool selection）。
- **定位**: 背景，必须引用并明确区分。

### 8. ReTool (ICLR 2026)
- **标题**: ReTool: Reinforcement Learning for Strategic Tool Use in LLMs
- **方法**: RL 训练 LLM 学习 when/how 调用 code interpreter，outcome-driven reward
- **与我们的关系**: 最接近的 "when to invoke tool" 工作。差异：(1) implicit routing（entangled with backbone），我们用 explicit modular router；(2) 没做 benefit decomposition（failure avoidance vs positive guidance）。
- **定位**: 互补/部分竞争。我们的 decomposition 分析是他们缺失的。

### 9. ToolRLA (2026)
- **标题**: ToolRLA: Multiplicative Reward Decomposition for Tool-Integrated Agents
- **方法**: 将 tool invocation reward 分解为 tool-name / coverage / parameter accuracy sub-scores
- **与我们的关系**: 做了 reward decomposition，但维度不同（tool selection accuracy vs death avoidance mechanism）。他们分解的是"哪个维度的 tool use 做得好"，我们分解的是"tool use 的收益来自哪种机制"。
- **定位**: 互补。方法论上有呼应（都在做 decomposition），但分析维度完全不同。

---

## 三、LLM Agent Safety / Failure Analysis

### 10. Check Yourself Before You Wreck Yourself (Kumaraguru et al., NeurIPS 2025 Workshop)
- **方法**: Prompting LLM agent 在不确定时主动 quit，在 ToolEmu 上评估
- **与我们的关系**: **最接近我们 "death avoidance" framing 的工作**。他们的 "selective quitting" 本质上是 death avoidance 的一种形式——识别高风险场景并退出。差异：(1) 他们用 prompting，我们用 learned router；(2) 他们的 quitting 是放弃任务，我们的 routing 是切换到更安全的 modality（仍完成任务）。
- **定位**: **高度相关，必须引用**。我们的 router 可以理解为 "selective quitting from LLM reasoning, switching to deterministic computation" 而非完全放弃。

### 11. SafeHarbor (arXiv 2605.05704, 2026)
- **方法**: Hierarchical memory-augmented guardrail for LLM agent safety
- **与我们的关系**: Agent safety guardrail，但关注 policy compliance / harmful action prevention，非 task-level catastrophic failure。
- **定位**: 背景（safety 大方向）。

### 12. Towards Verifiably Safe Tool Use for LLM Agents (Doshi et al., ICSE 2026)
- **方法**: STPA + capability-enhanced MCP framework，formal safety specification
- **与我们的关系**: 形式化 tool safety，但面向 enterprise scenarios（data leak, record overwrite），非 interactive environment 的 catastrophic failure。
- **定位**: 背景（broader safety context）。

### 13. Where LLM Agents Fail and How They Can Learn From Failures (2025)
- **方法**: AgentErrorTaxonomy + AgentErrorBench + AgentDebug
- **环境**: ALFWorld, GAIA, WebShop
- **与我们的关系**: Failure taxonomy 和 debugging framework。分类了 agent failure modes 但没有量化 "failure avoidance vs positive performance" 的分解。
- **定位**: 背景。我们的 death avoidance finding 可以看作是他们 taxonomy 中一种特定 failure mode 的量化分析。

### 14. How Do LLMs Fail In Agentic Scenarios? (2025)
- **方法**: Qualitative analysis of success/failure scenarios
- **与我们的关系**: Failure mode 分析但定性为主，没有量化 decomposition。
- **定位**: 背景。

### 15. Agent-SafetyBench
- **方法**: Evaluating LLM agent safety across multiple risk dimensions
- **与我们的关系**: Safety benchmark，面向 harmful action prevention 而非 task performance decomposition。
- **定位**: 远景背景。

---

## 四、Safe RL 文献

### 16. Safe Reinforcement Learning with Dead-Ends Avoidance and Recovery (RA-L / ICRA 2024)
- **方法**: 学习 optimal boundary 区分 safe/unsafe states，pretrain recovery policy + safety critic
- **与我们的关系**: **概念上最接近的 Safe RL 工作**。他们的 "dead-end states"（无论什么 policy 都必然失败的状态）= 我们的 "death states"。他们的 safety critic = 我们的 router-as-death-detector。差异：(1) 他们在 continuous control（robotics），我们在 text-based interactive environments；(2) 他们训练 recovery policy，我们切换 computation modality。
- **定位**: **重要背景，建议引用**。建立 "death avoidance as a routing mechanism" 与 Safe RL 的联系。

### 17. Combating RL's Sisyphean Curse with Intrinsic Fear (Lipton et al., 2016)
- **方法**: 学习 fear model 预测 imminent catastrophe probability，用于 penalize Q-learning
- **与我们的关系**: 早期 "death avoidance" 工作。他们发现 DRL agents 会周期性地重新访问 catastrophic states（Sisyphean curse）。我们的 router 本质上也是一个 fear model——预测 "这一步用 LLM 内部推理是否会导致 catastrophe"。
- **定位**: 互补/理论背景。

### 18. Avoiding Death through Fear Intrinsic Conditioning (Sanchez et al., 2025)
- **方法**: 生物启发的 amygdala-like memory network，intrinsic reward for death avoidance
- **与我们的关系**: 最新的 death avoidance RL 工作，使用 memory-augmented network 学习 "fear"。与我们的 router 在功能上类似（都在学 death prediction），但方法完全不同。
- **定位**: 背景。

### 19. Constrained MDP / State-wise Safe RL (Garcia & Fernandez, JMLR 2015; 多篇 survey)
- **核心框架**: CMDP with safety constraints，state-wise constraint satisfaction
- **与我们的关系**: 我们的 router 可以看作一种 state-wise safety mechanism——在每个 state 决定是否切换到 "safe" (deterministic) modality。但我们不是在 CMDP 框架下优化，而是用 counterfactual labeling + SFT。
- **定位**: 理论背景。可以在 Related Work 中简短提及 "our router can be viewed as a learned state-wise safety gate"。

---

## 五、Adaptive Computation / Routing

### 20. Learning How Hard to Think (ICLR 2025)
- **方法**: Input-adaptive compute allocation, learned marginal benefit estimator
- **与我们的关系**: Compute allocation 方向，但面向 decoding budget（best-of-k, routing to expensive vs cheap decoder），非 modality routing。
- **定位**: 远景背景。

### 21. ARES: Adaptive Reasoning Effort Selection (2026)
- **方法**: Lightweight router 预测 optimal reasoning effort level
- **与我们的关系**: Intra-model thinking level routing，非 inter-modality routing。
- **定位**: 背景。

### 22. Router-R1 (2025-2026)
- **方法**: RL-based multi-LLM routing with think + route actions
- **与我们的关系**: Multi-model routing via RL。差异：multi-model（不同 LLM）vs single-modality（LLM vs deterministic）。
- **定位**: 背景。

---

## 六、核心问题回答

### Q1: "99% death avoidance" finding 是否有先例？

**没有直接先例。** 没有找到任何论文量化过 "tool invocation / modality routing 的收益中，failure prevention vs positive guidance 各占多少"。

最接近的工作：
- **Intrinsic Fear** (Lipton 2016) 和 **Dead-Ends Avoidance** (ICRA 2024) 在 Safe RL 中研究了 death/catastrophe avoidance，但没有做 "benefit decomposition"（将 routing/tool-use 收益分解为 death avoidance vs positive improvement）。
- **"Check Yourself"** (NeurIPS 2025 WS) 提出 selective quitting 提升 safety，但没有量化 quitting 的收益有多少来自 catastrophe prevention vs 其他。
- **ToolRLA** (2026) 做了 reward decomposition，但分解维度是 tool-selection accuracy，不是 failure prevention mechanism。
- **SwiftSage** 有 fast/slow 路由但没分析路由收益的来源。

**我们的 "~93% death avoidance dominance" 发现是 novel 的。**

### Q2: 论文中应该引用的相关工作

**必须引用（Related Work 段落）**:
1. **SwiftSage** (Lin et al., 2023) — 最接近的 ScienceWorld 双模块路由
2. **Toolformer** (Schick et al., 2023) — Tool-use learning baseline
3. **ReTool** (ICLR 2026) — When to use tools via RL
4. **"Check Yourself"** (2025) — LLM agent selective quitting for safety
5. **Dead-Ends Avoidance** (ICRA 2024) — Safe RL dead-end detection
6. **Intrinsic Fear** (Lipton et al., 2016) — Death avoidance in RL
7. **ScienceWorld** (Wang et al., EMNLP 2022) — 环境
8. **ReAct** (Yao et al., 2023) — Agent baseline
9. **CogRouter** — ScienceWorld routing baseline
10. **ITP-R** — World model routing baseline

**建议引用（单句提及）**:
11. **MTRouter** (ACL 2026) — ScienceWorld 上的 concurrent routing work
12. **BEACON** — Trajectory-level RL on ScienceWorld
13. **Garcia & Fernandez** (JMLR 2015) — Safe RL survey（CMDP framework）
14. **Where LLM Agents Fail** (2025) — Agent failure taxonomy
15. **ToolRLA** (2026) — Reward decomposition for tool use

### Q3: Novelty claim 是否安全？

**安全，但需要精确表述。**

我们的 novelty 有两层：
1. **Empirical finding（强 novelty）**: 首次量化 "modality routing 的收益 decomposition"——在 ScienceWorld 上 ~93% 来自 death avoidance。没有任何论文做过类似分解。
2. **Methodology（中等 novelty）**: Episode-level counterfactual labeling 解决了 per-step oracle 在稀疏奖励下退化的问题（98% tie rate）。这个方法论是 specific to sparse-reward interactive environments 的贡献。

**潜在攻击面**:
- "Death avoidance is trivial — just always use deterministic" → 回应：我们的贡献是 finding，不是 routing method。Always-det 确实是强 baseline，这正是 finding 的一部分。
- "This is just Safe RL" → 回应：Safe RL 研究 death avoidance 但在 continuous control；我们在 LLM agent + text environment 中首次展示 death avoidance 主导 routing signal。
- "Check Yourself already showed this" → 回应：他们的 quitting 是放弃任务，我们切换 modality 继续完成任务；他们没有 benefit decomposition。

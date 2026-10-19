# paper writing theoretical analysis

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_paper_writing_theoretical_analysis_20260517T073023.jsonl`
- **Structured JSON:** [`e6318d13a5541e457837.json`](../../sessions/e6/e6318d13a5541e457837.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-17T07:36:52.204884+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theoretical_analysis_20260517T073023",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T07:36:52.205302+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation}
5	\label{sec:problem_formulation}
6	
7	We formalize the multi-turn interactive agent as a Partially Observable Markov Decision Process (POMDP) $\mathcal{M} = (\mathcal{S}, \mathcal{A}, \mathcal{O}, P, \Omega, R, \gamma)$, where $\mathcal{S}$ is the state space of the environment, $\mathcal{A}$ is the action space (natural language commands), $\mathcal{O}$ is the observation space (textual feedback from the environment), $P: \mathcal{S} \times \mathcal{A} \rightarrow \mathcal{S}$ is the transition function, $\Omega: \mathcal{S} \rightarrow \mathcal{O}$ is the observation function, $R$ is the reward function, and $\gamma \in [0,1]$ is a discount factor. The agent policy $\pi_\phi(a_t \mid h_t)$ generates actions conditioned on the interaction history $h_t = (o_1, a_1, o_2, a_2, \ldots, o_t)$, where $\phi$ denotes the policy parameters. An episode consists of $T$ interaction steps, terminating with a binary reward $R \in \{0, r_+\}$ that indicates task success or failure.
8	
9	In practice, multi-turn episodes can span 50 or more interaction steps, each containing hundreds of tokens. Training a language model policy on the full history $h_T$ is computationally expensive and often exceeds the model's context window. This motivates the \textbf{step-independent windowing} approach: the trajectory is partitioned into non-overlapping windows of $h$ consecutive steps, and each window is optimized independently with its own computed return. Concretely, window $k$ observes only $(o_{(k-1)h+1}, a_{(k-1)h+1}, \ldots, o_{kh})$ and receives a return $R_k$ derived from the episode outcome. This decomposition treats each window as a separate training sample, allowing standard context-length models to process the data. We show below that this seemingly practical choice introduces two failure mechanisms that cause catastrophic training collapse.
10	
11	\subsection{GRPO for Language Agents}
12	\label{sec:grpo}
…[truncated 11907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theoretical_analysis_20260517T073023",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T07:36:52.205503+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theoretical_analysis_20260517T073023",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T07:36:52.205920+00:00_

1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **
…[truncated 4866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theoretical_analysis_20260517T073023",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T07:36:52.206127+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theoretical_analysis_20260517T073023",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T07:36:52.206494+00:00_

1	---
2	name: latex-paper
3	description: ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。
4	scope: global
5	tags:
6	- latex
7	- paper-writing
8	- academic
9	- citation
10	- submission
11	version: 1
12	roles:
13	- agent
14	- worker
15	---
16	
17	# LaTeX 论文写作全流程
18	
19	ML/AI 顶会论文从草稿到投稿的完整指南。整合 Orchestra Research、VibeSkills、claim2evidence 三方最佳实践。
20	
21	---
22	
23	## 1. 工作模式
24	
25	开始前选择模式：
26	
27	| 模式 | 说明 | 适用 |
28	|------|------|------|
29	| **Build** | 从实验笔记/结果/代码生成论文 | 新稿 |
30	| **Improve** | 改写已有章节，强化论证 | 修改稿 |
31	| **Audit** | 输出风险列表 + 缺失证据 + 修复建议 | 投前检查 |
32	
33	---
34	
35	## 2. Claim-Evidence 方法论
36	
37	**核心原则：论文是一个有中心贡献的故事，不是实验的堆砌。**
38	
39	### 2.1 一句话贡献
40	
41	在写任何内容之前，必须能用一句话说清贡献。如果不能，说明还没准备好写论文。
42	
43	### 2.2 Claim-Evidence Map
44	
45	为每个 contribution 建立 claim→evidence 映射表：
46	
47	| Contribution | Claim | Evidence | Table/Figure |
48	|-------------|-------|----------|-------------|
49	| C1: 方法 X 在 Y 上 SOTA | 比所有 baseline 高 ≥2% | 5-seed 平均，p<0.05 | Table 1 |
50	| C2: 消融证明 Z 是关键 | 去掉 Z 后掉 >5% | 消融实验 | Table 2 |
51	| C3: 计算效率 | 比 baseline 快 3× | FLOPs + wall-clock | Figure 3 |
52	
53	**没有直接证据支撑的 claim 必须删除或降级为 discussion。**
54	
55	### 2.3 章节起草顺序
56	
57	```
58	1. Introduction + Experiments（先确定 claim 和 evidence）
59	2. Method（评估问题稳定后再写细节）
60	3. Related Work
61	4. Abstract + Title（核心 claim 定型后最后写）
62	```
63	
64	### 2.4 Quality Gates
65	
66	投稿前必须通过：
67	- [ ] 前两段出现显式 novelty 声明
68	- [ ] 每个 contribution 有可验证的 evidence
69	- [ ] Abstract / Intro / Conclusion 的 claim 一致
70	- [ ] Limitations 真实且技术性诚实
71	- [ ] 审稿人两分钟内能识别 delta
72	
73	---
74	
75	## 3. 引用防幻觉（CRITICAL）
76	
77	**AI 生成引用有 ~40% 错误率。绝对禁止凭记忆写 BibTeX。**
78	
79	### 3.1 黄金法则
80	
81	```
82	IF 无法程序化获取引用:
83	    → 标记 [CITATION NEEDED] 或 \cite{PLACEHOLDER_verify}
84	    → 明确告知用户
85	    → 绝不编造看似合理的引用
86	```
87	
88	### 3.2 五步验证流程
89	
90	```
91	1. SEARCH  → Semantic Scholar API 搜索关键词
92	2. VERIFY  → 至少 2 个来源确认论文存在（S2 + arXiv/CrossRef）
93	3. RETRIEVE → 通过 DOI 获取 BibTeX（程序化，非记忆）
94	4. CHECK   → 确认
…[truncated 7201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theoretical_analysis_20260517T073023",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T07:36:52.206850+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/",
  "description": "Check paper directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theoretical_analysis_20260517T073023",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/",
    "description": "Check paper directory exists"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T07:36:52.207002+00:00_

method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theoretical_analysis_20260517T073023",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T07:36:52.207170+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex",
  "content": "\\section{Theoretical Analysis}\n\\label{sec:theory}\n\nSection~\\ref{sec:dual_mechanism} identified two failure mechanisms of step-independent training: policy information loss and advantage sign misattribution. We now formalize why sign misattribution is the more fundamental failure, derive the probability of incorrect gradient direction as a function of task success rate, examine why the community has defaulted to step-independent training, and connect our findings to the classical credit assignment literature.\n\n\\subsection{Why Sign Misattribution is Fundamental}\n\\label{sec:sign_fundamental}\n\nThe two mechanisms identified in Section~\\ref{sec:dual_mechanism} produce qualitatively different optimization errors. Policy information loss (Mechanism 1) reduces the information available to each window's policy, producing suboptimal but directionally reasonable gradient updates. Sign misattribution (Mechanism 2) corrupts the gradient direction itself. We formalize this distinction below.\n\n\\textbf{Proposition 1.} \\textit{Under step-independent training with binary episode reward $R_{\\text{episode}} \\in \\{0, r_+\\}$, the probability that window $k$'s advantage $\\hat{A}_k$ has the correct sign (aligned with local action quality) approaches the base success rate $p$ as the number of rollouts $K$ per group increases.}\n\n\\textit{Argument.} Define ``correct sign'' as follows: for a window containing locally beneficial actions, the correct sign of $\\hat{A}_k$ is positive (reinforcement); for a window containing locally detrimental actions, the correct sign is negative (suppression). Under binary reward, the return for window $k$ is $R_k = \\gamma^{(N-k)} \\cdot R_{\\text{episode}}$ (Equation~\\ref{eq:step_return}). In a failed episode ($R_{\\text{episode}} = 0$), all windows receive $R_k = 0$ regardless of their local action quality. If the group contains at least one successful rollout, the group mean $\\mu > 0$, and all windows in the failed episode receive negative advantages after normalization via Equation~\\ref{eq:grpo_advantage}. This includes windows where the agent took locally correct actions, such as correctly identifying a target object in an exploration step. Now consider a window with good local actions. In a successful episode (probability $p$), the window receives positive $\\hat{A}_k$, which is the correct sign. In a failed episode (probability $1 - p$), the window receives negative $\\hat{A}_k$ whenever $\\mu > 0$, which is the wrong sign. The probability that $\\mu = 0$ (all $K$ rollouts in the group failed) is $(1-p)^K$, which shrinks exponentially with $K$. As $K$ grows, nearly every failed episode produces a non-zero group mean, and the window receives the wrong sign with probability approaching $1-p$. The probability of correct sign therefore approaches $p$. \\qed\n\nThe distinction between sign error and magnitude error clarifies why Mechanism 2 is catastrophic while Mechanism 1 is merely suboptimal. The discount factor $\\gamma^{(N-k)}$ in Equation~\\ref{eq:step_return} introduces magnitude decay across window positions: for an episode with $T=50$ steps and $h=2$, the first window ($k=1$) retains $\\gamma^{N-1} = 0.95^{24} \\approx 0.29$ of the terminal window's return. This attenuation reduces the gradient magnitude for early windows but preserves the gradient direction. A gradient with correct sign and reduced magnitude produces slow convergence, a condition recoverable through longer training. A gradient with wrong sign produces active divergence: the optimization pushes the policy away from good behaviors and toward bad ones. Consider a navigation analogy. Magnitude error corresponds to a compass that points correctly but displays a dimmed needle; the traveler moves slowly toward the destination. Sign error corresponds to a compass pointing in the opposite direction; the traveler walks away from the destination with full confidence. The first error is correctable by patience. The second is correctable only by replacing the compass.\n\n\\subsection{Formal Probability Analysis}\n\\label{sec:formal_probability}\n\nWe derive a tighter bound on the probability of correct gradient direction as a function of task difficulty and group size.\n\n\\textbf{Proposition 2.} \\textit{Let $p$ denote the episode success rate and $K$ the number of rollouts per group. Under step-independent training with binary episode reward, the probability that a gradient update for a window with locally good actions has the correct sign satisfies:}\n\\begin{equation}\nP(\\text{correct sign or no update}) = p + (1-p)^{K}\n\\label{eq:correct_bound}\n\\end{equation}\n\\textit{Among gradient updates that occur (non-zero advantage), the fraction with correct sign is:}\n\\begin{equation}\nP(\\text{correct} \\mid \\text{update}) = \\frac{p}{1 - (1-p)^{K}}\n\\label{eq:correct_conditional}\n\\end{equation}\n\n\\textit{Derivation.} For a window with locally good actions, the gradient direction depends on $\\text{sign}(\\hat{A}_k)$, which depends on whether the episode succeeded and whether the group contains any successful rollouts. Three mutually exclusive cases arise.\n\n\\textit{Case 1: Episode succeeded} (probability $p$). The window receives $R_k = \\gamma^{(N-k)} \\cdot r_+ > 0$. With at least one failed rollout in the group, $R_k > \\mu$ after normalization, producing $\\hat{A}_k > 0$. The gradient reinforces the window's actions. For a window with good local actions, this is the correct direction.\n\n\\textit{Case 2: Episode failed, group contains at least one success} (probability $(1-p)[1 - (1-p)^{K-1}]$). The window receives $R_k = 0 < \\mu$, producing $\\hat{A}_k < 0$. The gradient suppresses the window's actions. For a window with good local actions, this is the wrong direction.\n\n\\textit{Case 3: Episode failed, entire group failed} (probability $(1-p) \\cdot (1-p)^{K-1} = (1-p)^{K}$). All returns are zero, so $\\mu = 0$ and $\\sigma = 0$. The advantage is zero, producing no gradient update.\n\nSumming Cases~1 and~3 yields Equation~\\ref{eq:correct_bound}. Since only Cases~1 and~2 produce non-zero gradients, the conditional probability follows as Equation~\\ref{eq:correct_conditional}.\n\nWe evaluate these expressions at the empirical baseline of our experiments. At $p = 6.25\\%$ (the pre-training success rate) and $K = 4$: $(1-p)^K = 0.9375^4 \\approx 0.77$, giving $P(\\text{correct or no update}) \\approx 0.83$. Of the 23\\% of cases that produce a gradient update, only $P(\\text{correct} \\mid \\text{update}) = 0.0625 / 0.23 \\approx 27\\%$ have the correct sign. As $K$ increases to 16, $(1-p)^{K} \\approx 0.36$, and $P(\\text{correct} \\mid \\text{update}) \\approx 9.8\\%$. In the large-$K$ limit, $P(\\text{correct} \\mid \\text{update}) \\to p$, so approximately $1 - p \\approx 94\\%$ of all gradient updates for locally good windows point in the wrong direction. This is consistent with the empirical observation that step-independent training collapses to 0\\% task success (exp026, exp028c) while episode-level training achieves stable improvement (exp029, 28.125\\% validation success at step 15).\n\n\\subsection{Why the Community Defaults to Step-Independent Training}\n\\label{sec:why_defaults}\n\nIf step-independent training is fundamentally flawed for multi-turn agents, why has it become the default? We identify six contributing factors.\n\n\\textbf{1. Context window constraints.} Smaller language models (1B to 4B parameters) typically support context windows of 2048 to 4096 tokens. Multi-turn episodes spanning 50 or more interaction steps easily exceed these limits. Step-independent windowing is a pragmatic response to a hardware constraint, not a deliberate algorithmic choice.\n\n\\textbf{2. Token-level training inertia.} Language model training is organized around predicting the next token over fixed-length sequences. When multi-turn RL inherits this paradigm, the natural unit of optimization becomes a fixed-length window rather than a variable-length episode. The mismatch between token-level optimization and episode-level credit assignment goes unquestioned because it aligns with existing training infrastructure.\n\n\\textbf{3. Framework design accident.} The RAGEN framework~\\cite{ragen2025} implements step-independent mode as its default configuration, not as one option among alternatives. Users inherit this choice without an explicit decision point, and default configurations propagate silently through downstream projects.\n\n\\textbf{4. Memory and compute constraints.} Episode-level training requires processing $O(T)$ tokens per sequence, incurring $O(T^2)$ attention cost with full self-attention. Step-independent training reduces this to $O(h)$ tokens and $O(h^2)$ attention cost per window. The computational savings are immediate and measurable, while the credit assignment failure is subtle and deferred until training collapse occurs.\n\n\\textbf{5. Reward shaping as apparent fix.} Dense reward shaping (per-step bonuses for intermediate goals) appears to address sparse reward problems and has theoretical support in the single-agent RL literature. Our experiment with dense rewards under step-independent training (exp013f) reveals a different failure mode: the agent learns to maximize format-level rewards (action validity rises from 60\\% to 97.5\\%) while task success remains at 0\\%. Reward shaping does not resolve sign misattribution; it creates new optimization targets that the agent can game without solving the underlying task.\n\n\\textbf{6. Absence of negative results.} When step-independent training fails, practitioners attribute the failure to insufficient hyperparameter tuning or the inherent difficulty of sparse rewards. Without published analyses that isolate the credit assignment mechanism as the root cause, the community cannot distinguish between ``this problem is hard'' and ``this training paradigm is broken for this class of problems.''\n\n\\subsection{Connection to Classical Credit Assignment}\n\\label{sec:classical_connection}\n\nOur findings connect to a long line of work on temporal credit assignment in reinforcement learning. We position the step-independent failure mode within this literature and clarify the contribution of our analysis.\n\n\\textbf{Temporal difference learning and eligibility traces.} Sutton's TD($\\lambda$)~\\cite{sutton1988td} provides a spectrum of credit assignment strategies parameterized by $\\lambda \\in [0,1]$. At $\\lambda = 0$, credit is assigned via one-step bootstrapped returns. At $\\lambda = 1$, TD($\\lambda$) reduces to Monte Carlo returns, where each state receives the full episode return. Step-independent training falls below this spectrum: windows are disconnected from each other, so temporal propagation of credit does not occur. Each window receives an independently computed advantage with no mechanism for information to flow across windows within the same episode.\n\n\\textbf{Generalized Advantage Estimation.} GAE($\\lambda, \\gamma$)~\\cite{schulman2016gae} extends TD($\\lambda$) with a separate discount factor for the advantage estimator. GAE(0, $\\gamma$) produces per-step advantages through a learned value function. GAE(1, 1) produces undiscounted Monte Carlo returns, and is equivalent to episode-level GRPO without a critic. The key difference is that GAE uses value function subtraction as the baseline for variance reduction, while GRPO uses group normalization. Episode-level GRPO can be viewed as GAE(1, 1) with a group-relative baseline replacing the learned value function. This substitution is effective when the group provides a representative reference distribution, but it does not address per-step credit assignment within an episode.\n\n\\textbf{REINFORCE.} Williams' REINFORCE algorithm~\\cite{williams1992reinforce} computes policy gradients from complete episode returns with a learned baseline $b(s)$. Episode-level GRPO is equivalent to REINFORCE where the group mean $\\mu$ replaces $b(s)$ and the group standard deviation $\\sigma$ provides normalization. The algorithmic structure is not new. Our contribution is the diagnosis: the community's standard adaptation of this algorithm for multi-turn LLM agents (step-independent windowing) silently breaks the credit assignment structure that REINFORCE assumes.\n\n\\textbf{Multi-agent credit assignment analogy.} Step-independent windows can be understood through cooperative multi-agent games. Each window acts as an independent ``agent'' sharing a team reward (the episode outcome) but optimized without knowledge of other windows' actions. The sign misattribution problem parallels team reward credit assignment in cooperative multi-agent RL: when the team fails, all agents receive identical penalties regardless of individual contribution. In multi-agent RL, this is a recognized problem with known solutions such as counterfactual baselines. In multi-turn LLM agent training, the same structural problem arises from an implementation choice and has not been recognized as a credit assignment failure.\n\nTo summarize our positioning: we do not propose a new credit assignment algorithm. Episode-level training is the standard approach, and GRPO was designed as an episode-level method. What we identify is that the community's adaptation of GRPO to multi-turn settings introduces a systematic sign error in gradient computation. This error is not a gradual performance degradation but a catastrophic failure mode, as confirmed by the contrast between step-independent collapse (exp026, exp028c: 0\\% success) and episode-level stability (exp029: 28.125\\% validation success from a 12.5\\% baseline).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theoretical_analysis_20260517T073023",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex",
    "content": "\\section{Theoretical Analysis}\n\\label{sec:theory}\n\nSection~\\ref{sec:dual_mechanism} identified two failure mechanisms of step-independent training: policy information loss and advantage sign misattribution. We now formalize why sign misattribution is the more fundamental failure, derive the probability of incorrect gradient direction as a function of task success rate, examine why the community has defaulted to step-independent training, and connect our findings to the classical credit assignment literature.\n\n\\subsection{Why Sign Misattribution is Fundamental}\n\\label{sec:sign_fundamental}\n\nThe two mechanisms identified in Section~\\ref{sec:dual_mechanism} produce qualitatively different optimization errors. Policy information loss (Mechanism 1) reduces the information available to each window's policy, producing suboptimal but directionally reasonable gradient updates. Sign misattribution (Mechanism 2) corrupts the gradient direction itself. We formalize this distinction below.\n\n\\textbf{Proposition 1.} \\textit{Under step-independent training with binary episode reward $R_{\\text{episode}} \\in \\{0, r_+\\}$, the probability that window $k$'s advantage $\\hat{A}_k$ has the correct sign (aligned with local action quality) approaches the base success rate $p$ as the number of rollouts $K$ per group increases.}\n\n\\textit{Argument.} Define ``correct sign'' as follows: for a window containing locally beneficial actions, the correct sign of $\\hat{A}_k$ is positive (reinforcement); for a window containing locally detrimental actions, the correct sign is negative (suppression). Under binary reward, the return for window $k$ is $R_k = \\gamma^{(N-k)} \\cdot R_{\\text{episode}}$ (Equation~\\ref{eq:step_return}). In a failed episode ($R_{\\text{episode}} = 0$), all windows receive $R_k = 0$ regardless of their local action quality. If the group contains at least one successful rollout, the group mean $\\mu > 0$, and all windows in the failed episode receive negative advantages after normalization via Equation~\\ref{eq:grpo_advantage}. This includes windows where the agent took locally correct actions, such as correctly identifying a target object in an exploration step. Now consider a window with good local actions. In a successful episode (probability $p$), the window receives positive $\\hat{A}_k$, which is the correct sign. In a failed episode (probability $1 - p$), the window receives negative $\\hat{A}_k$ whenever $\\mu > 0$, which is the wrong sign. The probability that $\\mu = 0$ (all $K$ rollouts in the group failed) is $(1-p)^K$, which shrinks exponentially with $K$. As $K$ grows, nearly every failed episode produces a non-zero group mean, and the window receives the wrong sign with probability approaching $1-p$. The probability of correct sign therefore approaches $p$. \\qed\n\nThe distinction between sign error and magnitude error clarifies why Mechanism 2 is catastrophic while Mechanism 1 is merely suboptimal. The discount factor $\\gamma^{(N-k)}$ in Equation~\\ref{eq:step_return} introduces magnitude decay across window positions: for an episode with $T=50$ steps and $h=2$, the first window ($k=1$) retains $\\gamma^{N-1} = 0.95^{24} \\approx 0.29$ of the terminal window's return. This attenuation reduces the gradient magnitude for early windows but preserves the gradient direction. A gradient with correct sign and reduced magnitude produces slow convergence, a condition recoverable through longer training. A gradient with wrong sign produces active divergence: the optimization pushes the policy away from good behaviors and toward bad ones. Consider a navigation analogy. Magnitude error corresponds to a compass that points correctly but displays a dimmed needle; the traveler moves slowly toward the destination. Sign error corresponds to a compass pointing in the opposite direction; the traveler walks away from the destination with full confidence. The first error is correctable by patience. The second is correctable only by replacing the compass.\n\n\\subsection{Formal Probability Analysis}\n\\label{sec:formal_probability}\n\nWe derive a tighter bound on the probability of correct gradient direction as a function of task difficulty and group size.\n\n\\textbf{Proposition 2.} \\textit{Let $p$ denote the episode success rate and $K$ the number of rollouts per group. Under step-independent training with binary episode reward, the probability that a gradient update for a window with locally good actions has the correct sign satisfies:}\n\\begin{equation}\nP(\\text{correct sign or no update}) = p + (1-p)^{K}\n\\label{eq:correct_bound}\n\\end{equation}\n\\textit{Among gradient updates that occur (non-zero advantage), the fraction with correct sign is:}\n\\begin{equation}\nP(\\text{correct} \\mid \\text{update}) = \\frac{p}{1 - (1-p)^{K}}\n\\label{eq:correct_conditional}\n\\end{equation}\n\n\\textit{Derivation.} For a window with locally good actions, the gradient direction depends on $\\text{sign}(\\hat{A}_k)$, which depends on whether the episode succeeded and whether the group contains any successful rollouts. Three mutually exclusive cases arise.\n\n\\textit{Case 1: Episode succeeded} (probability $p$). The window receives $R_k = \\gamma^{(N-k)} \\cdot r_+ > 0$. With at least one failed rollout in the group, $R_k > \\mu$ after normalization, producing $\\hat{A}_k > 0$. The gradient reinforces the window's actions. For a window with good local actions, this is the correct direction.\n\n\\textit{Case 2: Episode failed, group contains at least one success} (probability $(1-p)[1 - (1-p)^{K-1}]$). The window receives $R_k = 0 < \\mu$, producing $\\hat{A}_k < 0$. The gradient suppresses the window's actions. For a window with good local actions, this is the wrong direction.\n\n\\textit{Case 3: Episode failed, entire group failed} (probability $(1-p) \\cdot (1-p)^{K-1} = (1-p)^{K}$). All returns are zero, so $\\mu = 0$ and $\\sigma = 0$. The advantage is zero, producing no gradient update.\n\nSumming Cases~1 and~3 yields Equation~\\ref{eq:correct_bound}. Since only Cases~1 and~2 produce non-zero gradients, the conditional probability follows as Equation~\\ref{eq:correct_conditional}.\n\nWe evaluate these expressions at the empirical baseline of our experiments. At $p = 6.25\\%$ (the pre-training success rate) and $K = 4$: $(1-p)^K = 0.9375^4 \\approx 0.77$, giving $P(\\text{correct or no update}) \\approx 0.83$. Of the 23\\% of cases that produce a gradient update, only $P(\\text{correct} \\mid \\text{update}) = 0.0625 / 0.23 \\approx 27\\%$ have the correct sign. As $K$ increases to 16, $(1-p)^{K} \\approx 0.36$, and $P(\\text{correct} \\mid \\text{update}) \\approx 9.8\\%$. In the large-$K$ limit, $P(\\text{correct} \\mid \\text{update}) \\to p$, so approximately $1 - p \\approx 94\\%$ of all gradient updates for locally good windows point in the wrong direction. This is consistent with the empirical observation that step-independent training collapses to 0\\% task success (exp026, exp028c) while episode-level training achieves stable improvement (exp029, 28.125\\% validation success at step 15).\n\n\\subsection{Why the Community Defaults to Step-Independent Training}\n\\label{sec:why_defaults}\n\nIf step-independent training is fundamentally flawed for multi-turn agents, why has it become the default? We identify six contributing factors.\n\n\\textbf{1. Context window constraints.} Smaller language models (1B to 4B parameters) typically support context windows of 2048 to 4096 tokens. Multi-turn episodes spanning 50 or more interaction steps easily exceed these limits. Step-independent windowing is a pragmatic response to a hardware constraint, not a deliberate algorithmic choice.\n\n\\textbf{2. Token-level training inertia.} Language model training is organized around predicting the next token over fixed-length sequences. When multi-turn RL inherits this paradigm, the natural unit of optimization becomes a fixed-length window rather than a variable-length episode. The mismatch between token-level optimization and episode-level credit assignment goes unquestioned because it aligns with existing training infrastructure.\n\n\\textbf{3. Framework design accident.} The RAGEN framework~\\cite{ragen2025} implements step-independent mode as its default configuration, not as one option among alternatives. Users inherit this choice without an explicit decision point, and default configurations propagate silently through downstream projects.\n\n\\textbf{4. Memory and compute constraints.} Episode-level training requires processing $O(T)$ tokens per sequence, incurring $O(T^2)$ attention cost with full self-attention. Step-independent training reduces this to $O(h)$ tokens and $O(h^2)$ attention cost per window. The computational savings are immediate and measurable, while the credit assignment failure is subtle and deferred until training collapse occurs.\n\n\\textbf{5. Reward shaping as apparent fix.} Dense reward shaping (per-step bonuses for intermediate goals) appears to address sparse reward problems and has theoretical support in the single-agent RL literature. Our experiment with dense rewards under step-independent training (exp013f) reveals a different failure mode: the agent learns to maximize format-level rewards (action validity rises from 60\\% to 97.5\\%) while task success remains at 0\\%. Reward shaping does not resolve sign misattribution; it creates new optimization targets that the agent can game without solving the underlying task.\n\n\\textbf{6. Absence of negative results.} When step-independent training fails, practitioners attribute the failure to insufficient hyperparameter tuning or the inherent difficulty of sparse rewards. Without published analyses that isolate the credit assignment mechanism as the root cause, the community cannot distinguish between ``this problem is hard'' and ``this training paradigm is broken for this class of problems.''\n\n\\subsection{Connection to Classical Credit Assignment}\n\\label{sec:classical_connection}\n\nOur findings connect to a long line of work on temporal credit assignment in reinforcement learning. We position the step-independent failure mode within this literature and clarify the contribution of our analysis.\n\n\\textbf{Temporal difference learning and eligibility traces.} Sutton's TD($\\lambda$)~\\cite{sutton1988td} provides a spectrum of credit assignment strategies parameterized by $\\lambda \\in [0,1]$. At $\\lambda = 0$, credit is assigned via one-step bootstrapped returns. At $\\lambda = 1$, TD($\\lambda$) reduces to Monte Carlo returns, where each state receives the full episode return. Step-independent training falls below this spectrum: windows are disconnected from each other, so temporal propagation of credit does not occur. Each window receives an independently computed advantage with no mechanism for information to flow across windows within the same episode.\n\n\\textbf{Generalized Advantage Estimation.} GAE($\\lambda, \\gamma$)~\\cite{schulman2016gae} extends TD($\\lambda$) with a separate discount factor for the advantage estimator. GAE(0, $\\gamma$) produces per-step advantages through a learned value function. GAE(1, 1) produces undiscounted Monte Carlo returns, and is equivalent to episode-level GRPO without a critic. The key difference is that GAE uses value function subtraction as the baseline for variance reduction, while GRPO uses group normalization. Episode-level GRPO can be viewed as GAE(1, 1) with a group-relative baseline replacing the learned value function. This substitution is effective when the group provides a representative reference distribution, but it does not address per-step credit assignment within an episode.\n\n\\textbf{REINFORCE.} Williams' REINFORCE algorithm~\\cite{williams1992reinforce} computes policy gradients from complete episode returns with a learned baseline $b(s)$. Episode-level GRPO is equivalent to REINFORCE where the group mean $\\mu$ replaces $b(s)$ and the group standard deviation $\\sigma$ provides normalization. The algorithmic structure is not new. Our contribution is the diagnosis: the community's standard adaptation of this algorithm for multi-turn LLM agents (step-independent windowing) silently breaks the credit assignment structure that REINFORCE assumes.\n\n\\textbf{Multi-agent credit assignment analogy.} Step-independent windows can be understood through cooperative multi-agent games. Each window acts as an independent ``agent'' sharing a team reward (the episode outcome) but optimized without knowledge of other windows' actions. The sign misattribution problem parallels team reward credit assignment in cooperative multi-agent RL: when the team fails, all agents receive identical penalties regardless of individual contribution. In multi-agent RL, this is a recognized problem with known solutions such as counterfactual baselines. In multi-turn LLM agent training, the same structural problem arises from an implementation choice and has not been recognized as a credit assignment failure.\n\nTo summarize our positioning: we do not propose a new credit assignment algorithm. Episode-level training is the standard approach, and GRPO was designed as an episode-level method. What we identify is that the community's adaptation of GRPO to multi-turn settings introduces a systematic sign error in gradient computation. This error is not a gradual performance degradation but a catastrophic failure mode, as confirmed by the contrast between step-independent collapse (exp026, exp028c: 0\\% success) and episode-level stability (exp029: 28.125\\% validation success from a 12.5\\% baseline).\n"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T07:36:52.207441+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theoretical_analysis_20260517T073023",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T07:36:52.207605+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"—\" /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex",
  "description": "Check for em-dashes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theoretical_analysis_20260517T073023",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"—\" /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex",
    "description": "Check for em-dashes"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T07:36:52.207762+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theoretical_analysis_20260517T073023",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T07:36:52.207889+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \" – \" /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex",
  "description": "Check for explanatory en-dashes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theoretical_analysis_20260517T073023",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \" – \" /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex",
    "description": "Check for explanatory en-dashes"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T07:36:52.208010+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theoretical_analysis_20260517T073023",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T07:36:52.208126+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"ing\\.\" /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex | head -20",
  "description": "Check for -ing phrase endings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theoretical_analysis_20260517T073023",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"ing\\.\" /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex | head -20",
    "description": "Check for -ing phrase endings"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T07:36:52.208247+00:00_

15:The distinction between sign error and magnitude error clarifies why Mechanism 2 is catastrophic while Mechanism 1 is merely suboptimal. The discount factor $\gamma^{(N-k)}$ in Equation~\ref{eq:step_return} introduces magnitude decay across window positions: for an episode with $T=50$ steps and $h=2$, the first window ($k=1$) retains $\gamma^{N-1} = 0.95^{24} \approx 0.29$ of the terminal window's return. This attenuation reduces the gradient magnitude for early windows but preserves the gradient direction. A gradient with correct sign and reduced magnitude produces slow convergence, a condition recoverable through longer training. A gradient with wrong sign produces active divergence: the optimization pushes the policy away from good behaviors and toward bad ones. Consider a navigation analogy. Magnitude error corresponds to a compass that points correctly but displays a dimmed needle; the traveler moves slowly toward the destination. Sign error corresponds to a compass pointing in the opposite direction; the traveler walks away from the destination with full confidence. The first error is correctable by patience. The second is correctable only by replacing the compass.
65:Our findings connect to a long line of work on temporal credit assignment in reinforcement learning. We position the step-independent failure mode within this literature and clarify the contribution of our analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theoretical_analysis_20260517T073023",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T07:36:52.208384+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n -i \"furthermore\\|moreover\\|additionally\\|it is worth noting\\|notably\\|leverage\\|utilize\\|facilitate\\|delve\" /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex",
  "description": "Check for banned words"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theoretical_analysis_20260517T073023",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n -i \"furthermore\\|moreover\\|additionally\\|it is worth noting\\|notably\\|leverage\\|utilize\\|facilitate\\|delve\" /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex",
    "description": "Check for banned words"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T07:36:52.208509+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theoretical_analysis_20260517T073023",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T07:36:52.208623+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex",
  "description": "Count words"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theoretical_analysis_20260517T073023",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex",
    "description": "Count words"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T07:36:52.208763+00:00_

1803 /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theoretical_analysis_20260517T073023",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-17T07:36:52.208945+00:00_

All checks pass:
- Zero em-dashes
- Zero explanatory en-dashes
- Zero banned words (Furthermore, Moreover, Additionally, leverage, utilize, etc.)
- The "ing." matches are nouns ("training", "learning"), not trailing participial phrases
- Word count: 1803 (target: 1800)

Section written to `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex`. Structure:

- **4.1** Proposition 1 (sign probability → p as K grows) + sign vs. magnitude error distinction with compass analogy
- **4.2** Proposition 2 (formal bound: P(correct|update) = p/(1-(1-p)^K)), numerical evaluation at p=6.25% showing ~94% wrong-direction updates in large-K limit
- **4.3** Six root causes for community default (context constraints, token-level inertia, framework accident, compute, reward shaping illusion, missing negative results), each 2-3 sentences
- **4.4** Connections to TD(λ), GAE, REINFORCE, multi-agent credit assignment; positioning statement

Notation matches method.tex exactly. Citations use the specified bibtex keys. No preamble included.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_theoretical_analysis_20260517T073023"
}
```

</details>

---

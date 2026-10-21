# paper writing introduction

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_paper_writing_introduction_20260517T075037.jsonl`
- **Structured JSON:** [`75525e3dbe92bd581de9.json`](../../sessions/75/75525e3dbe92bd581de9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-17T07:55:02.509162+00:00_

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
  "session": "worker_paper_writing_introduction_20260517T075037",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T07:55:02.509958+00:00_

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
  "session": "worker_paper_writing_introduction_20260517T075037",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T07:55:02.510194+00:00_

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
  "session": "worker_paper_writing_introduction_20260517T075037",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T07:55:02.510874+00:00_

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
  "session": "worker_paper_writing_introduction_20260517T075037",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T07:55:02.511113+00:00_

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
  "session": "worker_paper_writing_introduction_20260517T075037",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T07:55:02.511369+00:00_

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
  "session": "worker_paper_writing_introduction_20260517T075037",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T07:55:02.511555+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260517T075037",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T07:55:02.511809+00:00_

1	\section{Theoretical Analysis}
2	\label{sec:theory}
3	
4	Section~\ref{sec:dual_mechanism} identified two failure mechanisms of step-independent training: policy information loss and advantage sign misattribution. We now formalize why sign misattribution is the more fundamental failure, derive the probability of incorrect gradient direction as a function of task success rate, examine why the community has defaulted to step-independent training, and connect our findings to the classical credit assignment literature.
5	
6	\subsection{Why Sign Misattribution is Fundamental}
7	\label{sec:sign_fundamental}
8	
9	The two mechanisms identified in Section~\ref{sec:dual_mechanism} produce qualitatively different optimization errors. Policy information loss (Mechanism 1) reduces the information available to each window's policy, producing suboptimal but directionally reasonable gradient updates. Sign misattribution (Mechanism 2) corrupts the gradient direction itself. We formalize this distinction below.
10	
11	\textbf{Proposition 1.} \textit{Under step-independent training with binary episode reward $R_{\text{episode}} \in \{0, r_+\}$, the probability that window $k$'s advantage $\hat{A}_k$ has the correct sign (aligned with local action quality) approaches the base success rate $p$ as the number of rollouts $K$ per group increases.}
12	
13	\textit{Argument.} Define ``correct sign'' as follows: for a window containing locally beneficial actions, the correct sign of $\hat{A}_k$ is positive (reinforcement); for a window containing locally detrimental actions, the correct sign is negative (suppression). Under binary reward, the return for window $k$ is $R_k = \gamma^{(N-k)} \cdot R_{\text{episode}}$ (Equation~\ref{eq:step_return}). In a failed episode ($R_{\text{episode}} = 0$), all windows receive $R_k = 0$ regardless of their local action quality. If the group contains at least one successful rollout, the group mean $\mu > 0$, and all windows in the failed episode receive neg
…[truncated 11742 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260517T075037",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T07:55:02.512031+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper && ls /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/",
  "description": "Ensure paper directory exists and list contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260517T075037",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper && ls /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/",
    "description": "Ensure paper directory exists and list contents"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T07:55:02.512172+00:00_

method.tex
theoretical_analysis.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260517T075037",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T07:55:02.512487+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex",
  "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining Large Language Model (LLM) agents for multi-turn interactive tasks poses a fundamental challenge: policies must compose actions across 30 to 50 interaction steps in environments such as household navigation~\\cite{kim2025reflact}, web interaction~\\cite{digiRL2024}, and scientific experimentation. Supervised fine-tuning (SFT) can teach action formatting but fails to instill compositional planning, because expert demonstrations do not expose the trial-and-error exploration through which effective multi-step strategies emerge. Reinforcement learning (RL) addresses this gap by optimizing policies through direct environment interaction, and Group Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath} has become a preferred method due to its critic-free design and direct compatibility with language model architectures. Recent work applies RL-based training to interactive agents across diverse domains, from text-based games~\\cite{ragen2025} and GUI interaction~\\cite{digiRL2024} to tool use~\\cite{spear2025} and instruction following~\\cite{selfguide2026,feng2025gigpo}. These efforts share a common implementation pattern that has received little scrutiny: the multi-turn trajectory is decomposed into fixed-size windows, and each window is optimized as an independent training sample. This decomposition is the focus of our analysis.\n\nCurrent agent RL frameworks default to \\textit{step-independent training}: the trajectory is partitioned into non-overlapping windows of $h$ consecutive steps, each receiving a discounted return derived from the binary episode outcome and optimized independently via GRPO~\\cite{ragen2025,selfguide2026}. This choice is motivated by practical considerations: it fits long trajectories within limited context windows, multiplies the effective batch size, and aligns with the token-level training paradigm of language models. However, the decomposition introduces a fundamental credit assignment pathology. When each window receives a group-normalized advantage, the sign of that advantage reflects whether the \\textit{episode} succeeded or failed, not whether the \\textit{window's actions} were locally correct. In our experiments, this pathology produces a striking failure pattern: step-independent training collapses to 0\\% task success within 10 training steps, while action validity remains above 90\\% (Section~\\ref{sec:experiments}). The agent learns to produce well-formatted commands that satisfy syntactic constraints but loses the ability to complete tasks entirely. This collapse is not an artifact of a particular hyperparameter configuration. We observe the same failure across multiple learning rates, KL penalty strengths, and window sizes, consistent with a structural defect in the training paradigm rather than a tuning problem.\n\nStandard remedies do not resolve this collapse. Dense reward shaping, which provides per-step bonuses for intermediate goals such as valid action formatting, creates a different failure mode: the agent maximizes format-level rewards while task completion stays at zero. In our dense reward experiment, action validity increases from 60\\% to 97.5\\% while task success remains at 0\\% (Section~\\ref{sec:experiments}). Increasing the number of rollouts or adjusting the KL penalty delays the onset of collapse but does not prevent it. Generalized Advantage Estimation (GAE)~\\cite{schulman2016gae} and Proximal Policy Optimization (PPO)~\\cite{schulman2017ppo} offer finer-grained temporal credit assignment through learned value functions, but they add model complexity and have not been applied with a diagnosis of \\textit{why} step-independent training fails in the first place. The root cause is not the choice of RL algorithm. It is the step-independent windowing itself, which corrupts the credit assignment signal at its source.\n\nWe trace the collapse to two mechanisms that operate jointly under step-independent training. The first, \\textbf{policy information loss}, arises because each $h$-step window has no access to actions and outcomes from other windows, so cross-step strategies that require conditioning on earlier results become invisible to the optimization process. The second, \\textbf{advantage sign misattribution}, is more damaging: under binary episode reward, the sign of each window's advantage $\\hat{A}_k$ is determined by whether the episode succeeded or failed (Section~\\ref{sec:m2_sign_misattribution}), not by the local quality of the window's actions. Good actions in failed episodes receive negative advantages and are actively suppressed, while bad actions in successful episodes are reinforced. Our formal analysis (Section~\\ref{sec:formal_probability}) shows that at a baseline success rate of $p = 6.25\\%$ with group size $K = 8$, approximately 84.5\\% of gradient updates for locally correct windows point in the wrong direction. Sign misattribution is a directional error, fundamentally distinct from magnitude attenuation: it drives the policy away from correct behaviors rather than merely reducing convergence speed. Episode-level GRPO eliminates both mechanisms by treating the complete trajectory as a single optimization sample, consistent with GRPO's original design~\\cite{shao2024deepseekmath}, so that all steps share one advantage and cross-step dependencies are preserved through the full interaction history. In our experiments, episode-level training achieves 28.1\\% validation success (from a 12.5\\% baseline), while step-independent training collapses to 0\\%.\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item \\textbf{Dual mechanism diagnosis.} We identify and formalize two mechanisms that cause catastrophic collapse under step-independent GRPO in multi-turn agent training: policy information loss and advantage sign misattribution. We show that sign misattribution is a directional error, with the probability of incorrect gradient direction approaching $1 - p$ as group size grows (Sections~\\ref{sec:dual_mechanism},~\\ref{sec:sign_fundamental},~\\ref{sec:formal_probability}).\n\n    \\item \\textbf{Systematic empirical validation.} Through window-size ablation ($h \\in \\{2, 5, 10, 20, \\text{full}\\}$) and per-window advantage logging, we demonstrate a credit assignment cliff and provide direct empirical evidence for the sign misattribution mechanism (Section~\\ref{sec:experiments}).\n\n    \\item \\textbf{Episode-level solution and analysis.} We show that episode-level GRPO simultaneously resolves both failure mechanisms, and we analyze its connection to GAE~\\cite{schulman2016gae} and REINFORCE~\\cite{williams1992reinforce}. We identify six factors that explain why the community has defaulted to the broken step-independent paradigm (Sections~\\ref{sec:episode_level},~\\ref{sec:classical_connection},~\\ref{sec:why_defaults}).\n\\end{itemize}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260517T075037",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex",
    "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining Large Language Model (LLM) agents for multi-turn interactive tasks poses a fundamental challenge: policies must compose actions across 30 to 50 interaction steps in environments such as household navigation~\\cite{kim2025reflact}, web interaction~\\cite{digiRL2024}, and scientific experimentation. Supervised fine-tuning (SFT) can teach action formatting but fails to instill compositional planning, because expert demonstrations do not expose the trial-and-error exploration through which effective multi-step strategies emerge. Reinforcement learning (RL) addresses this gap by optimizing policies through direct environment interaction, and Group Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath} has become a preferred method due to its critic-free design and direct compatibility with language model architectures. Recent work applies RL-based training to interactive agents across diverse domains, from text-based games~\\cite{ragen2025} and GUI interaction~\\cite{digiRL2024} to tool use~\\cite{spear2025} and instruction following~\\cite{selfguide2026,feng2025gigpo}. These efforts share a common implementation pattern that has received little scrutiny: the multi-turn trajectory is decomposed into fixed-size windows, and each window is optimized as an independent training sample. This decomposition is the focus of our analysis.\n\nCurrent agent RL frameworks default to \\textit{step-independent training}: the trajectory is partitioned into non-overlapping windows of $h$ consecutive steps, each receiving a discounted return derived from the binary episode outcome and optimized independently via GRPO~\\cite{ragen2025,selfguide2026}. This choice is motivated by practical considerations: it fits long trajectories within limited context windows, multiplies the effective batch size, and aligns with the token-level training paradigm of language models. However, the decomposition introduces a fundamental credit assignment pathology. When each window receives a group-normalized advantage, the sign of that advantage reflects whether the \\textit{episode} succeeded or failed, not whether the \\textit{window's actions} were locally correct. In our experiments, this pathology produces a striking failure pattern: step-independent training collapses to 0\\% task success within 10 training steps, while action validity remains above 90\\% (Section~\\ref{sec:experiments}). The agent learns to produce well-formatted commands that satisfy syntactic constraints but loses the ability to complete tasks entirely. This collapse is not an artifact of a particular hyperparameter configuration. We observe the same failure across multiple learning rates, KL penalty strengths, and window sizes, consistent with a structural defect in the training paradigm rather than a tuning problem.\n\nStandard remedies do not resolve this collapse. Dense reward shaping, which provides per-step bonuses for intermediate goals such as valid action formatting, creates a different failure mode: the agent maximizes format-level rewards while task completion stays at zero. In our dense reward experiment, action validity increases from 60\\% to 97.5\\% while task success remains at 0\\% (Section~\\ref{sec:experiments}). Increasing the number of rollouts or adjusting the KL penalty delays the onset of collapse but does not prevent it. Generalized Advantage Estimation (GAE)~\\cite{schulman2016gae} and Proximal Policy Optimization (PPO)~\\cite{schulman2017ppo} offer finer-grained temporal credit assignment through learned value functions, but they add model complexity and have not been applied with a diagnosis of \\textit{why} step-independent training fails in the first place. The root cause is not the choice of RL algorithm. It is the step-independent windowing itself, which corrupts the credit assignment signal at its source.\n\nWe trace the collapse to two mechanisms that operate jointly under step-independent training. The first, \\textbf{policy information loss}, arises because each $h$-step window has no access to actions and outcomes from other windows, so cross-step strategies that require conditioning on earlier results become invisible to the optimization process. The second, \\textbf{advantage sign misattribution}, is more damaging: under binary episode reward, the sign of each window's advantage $\\hat{A}_k$ is determined by whether the episode succeeded or failed (Section~\\ref{sec:m2_sign_misattribution}), not by the local quality of the window's actions. Good actions in failed episodes receive negative advantages and are actively suppressed, while bad actions in successful episodes are reinforced. Our formal analysis (Section~\\ref{sec:formal_probability}) shows that at a baseline success rate of $p = 6.25\\%$ with group size $K = 8$, approximately 84.5\\% of gradient updates for locally correct windows point in the wrong direction. Sign misattribution is a directional error, fundamentally distinct from magnitude attenuation: it drives the policy away from correct behaviors rather than merely reducing convergence speed. Episode-level GRPO eliminates both mechanisms by treating the complete trajectory as a single optimization sample, consistent with GRPO's original design~\\cite{shao2024deepseekmath}, so that all steps share one advantage and cross-step dependencies are preserved through the full interaction history. In our experiments, episode-level training achieves 28.1\\% validation success (from a 12.5\\% baseline), while step-independent training collapses to 0\\%.\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item \\textbf{Dual mechanism diagnosis.} We identify and formalize two mechanisms that cause catastrophic collapse under step-independent GRPO in multi-turn agent training: policy information loss and advantage sign misattribution. We show that sign misattribution is a directional error, with the probability of incorrect gradient direction approaching $1 - p$ as group size grows (Sections~\\ref{sec:dual_mechanism},~\\ref{sec:sign_fundamental},~\\ref{sec:formal_probability}).\n\n    \\item \\textbf{Systematic empirical validation.} Through window-size ablation ($h \\in \\{2, 5, 10, 20, \\text{full}\\}$) and per-window advantage logging, we demonstrate a credit assignment cliff and provide direct empirical evidence for the sign misattribution mechanism (Section~\\ref{sec:experiments}).\n\n    \\item \\textbf{Episode-level solution and analysis.} We show that episode-level GRPO simultaneously resolves both failure mechanisms, and we analyze its connection to GAE~\\cite{schulman2016gae} and REINFORCE~\\cite{williams1992reinforce}. We identify six factors that explain why the community has defaulted to the broken step-independent paradigm (Sections~\\ref{sec:episode_level},~\\ref{sec:classical_connection},~\\ref{sec:why_defaults}).\n\\end{itemize}\n"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T07:55:02.512759+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260517T075037",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T07:55:02.512929+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper && grep -n \"—\" introduction.tex; grep -n \" – \" introduction.tex; grep -c \"ing,\" introduction.tex; echo \"---word count---\"; wc -w introduction.tex",
  "description": "Check for banned em-dash, en-dash, and -ing patterns; count words"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260517T075037",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper && grep -n \"—\" introduction.tex; grep -n \" – \" introduction.tex; grep -c \"ing,\" introduction.tex; echo \"---word count---\"; wc -w introduction.tex",
    "description": "Check for banned em-dash, en-dash, and -ing patterns; count words"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T07:55:02.513067+00:00_

3
---word count---
850 introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260517T075037",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T07:55:02.513216+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"ing,\" /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex",
  "description": "Show lines with -ing comma pattern"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260517T075037",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"ing,\" /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex",
    "description": "Show lines with -ing comma pattern"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T07:55:02.513359+00:00_

4:Training Large Language Model (LLM) agents for multi-turn interactive tasks poses a fundamental challenge: policies must compose actions across 30 to 50 interaction steps in environments such as household navigation~\cite{kim2025reflact}, web interaction~\cite{digiRL2024}, and scientific experimentation. Supervised fine-tuning (SFT) can teach action formatting but fails to instill compositional planning, because expert demonstrations do not expose the trial-and-error exploration through which effective multi-step strategies emerge. Reinforcement learning (RL) addresses this gap by optimizing policies through direct environment interaction, and Group Relative Policy Optimization (GRPO)~\cite{shao2024deepseekmath} has become a preferred method due to its critic-free design and direct compatibility with language model architectures. Recent work applies RL-based training to interactive agents across diverse domains, from text-based games~\cite{ragen2025} and GUI interaction~\cite{digiRL2024} to tool use~\cite{spear2025} and instruction following~\cite{selfguide2026,feng2025gigpo}. These efforts share a common implementation pattern that has received little scrutiny: the multi-turn trajectory is decomposed into fixed-size windows, and each window is optimized as an independent training sample. This decomposition is the focus of our analysis.
8:Standard remedies do not resolve this collapse. Dense reward shaping, which provides per-step bonuses for intermediate goals such as valid action formatting, creates a different failure mode: the agent maximizes format-level rewards while task completion stays at zero. In our dense reward experiment, action validity increases from 60\% to 97.5\% while task success remains at 0\% (Section~\ref{sec:experiments}). Increasing the number of rollouts or adjusting the KL penalty delays the onset of collapse but does not prevent it. Generalized Advantage Estimation (GAE)~\cite{schulman2016gae} and Proximal Policy Optimization (PPO)~\cite
…[truncated 700 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260517T075037",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-17T07:55:02.513553+00:00_

All 3 `ing,` matches are nouns (formatting, logging), not participial modifiers. No issues.

File written to `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex`. ~850 words, 5 paragraphs with contribution list. No em-dashes, no participial endings, no banned phrases. Notation ($h$, $\hat{A}_k$, $K$, $p$, $\pi_\phi$) is consistent with method.tex and theoretical\_analysis.tex. All 3 contributions have section references matching the existing paper structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_introduction_20260517T075037"
}
```

</details>

---

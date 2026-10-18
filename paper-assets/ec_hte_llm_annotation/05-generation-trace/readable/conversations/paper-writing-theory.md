# paper writing theory

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/chats/worker_paper_writing_theory_20260521T043620.jsonl`
- **Structured JSON:** [`9619106160ef7cd44715.json`](../../sessions/96/9619106160ef7cd44715.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

47 recorded events

### Tool call

_source line 1 · 2026-05-21T04:41:07.936896+00:00_

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
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T04:41:07.938022+00:00_

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
…[truncated 5709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T04:41:07.938417+00:00_

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
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T04:41:07.939157+00:00_

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
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T04:41:07.939485+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/results/exp002_derivation.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/results/exp002_derivation.md"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T04:41:07.941902+00:00_

1	# Formal Bias Bound Derivation (exp-002)
2	
3	## Assumptions
4	
5	- **(A1)** Known confusion matrix (not estimated from data)
6	- **(A2)** Symmetric misclassification per subgroup: P(Ẑ=1|Z=0,S=s) = P(Ẑ=0|Z=1,S=s) = π_s
7	- **(A3)** Balanced effect modifier: P(Z=0) = P(Z=1) = 0.5
8	- **(A4)** Known subgroup weights w_s with Σ_s w_s = 1
9	
10	## Step 1: Subgroup Confusion Matrix
11	
12	Under A2, the confusion matrix for subgroup s (rows = true Z, cols = Ẑ):
13	
14	```
15	C_s = [[1 - π_s,  π_s    ],
16	       [π_s,      1 - π_s ]]
17	```
18	
19	where C_s[z, ẑ] = P(Ẑ = ẑ | Z = z, S = s).
20	
21	## Step 2: Mixing Matrix
22	
23	The mixing matrix M_s[ẑ, z] = P(Z = z | Ẑ = ẑ, S = s).
24	
25	By Bayes' rule:
26	
27	```
28	P(Z=z | Ẑ=ẑ, S=s) = P(Ẑ=ẑ | Z=z, S=s) · P(Z=z) / P(Ẑ=ẑ | S=s)
29	```
30	
31	Under A3, P(Z=z) = 0.5 for z ∈ {0,1}. The marginal:
32	
33	```
34	P(Ẑ=ẑ | S=s) = Σ_z P(Ẑ=ẑ | Z=z, S=s) · P(Z=z)
35	             = 0.5 · [C_s[0,ẑ] + C_s[1,ẑ]]
36	```
37	
38	For ẑ=0: P(Ẑ=0|S=s) = 0.5·[(1-π_s) + π_s] = 0.5
39	For ẑ=1: P(Ẑ=1|S=s) = 0.5·[π_s + (1-π_s)] = 0.5
40	
41	Therefore:
42	
43	```
44	M_s[ẑ, z] = C_s[z, ẑ] · 0.5 / 0.5 = C_s[z, ẑ]
45	```
46	
47	Since C_s is symmetric under A2:
48	
49	```
50	M_s = [[1 - π_s,  π_s    ],
51	       [π_s,      1 - π_s ]]
52	```
53	
54	## Step 3: Global Confusion/Mixing Matrix
55	
56	The global confusion matrix is the weight-averaged subgroup matrix:
57	
58	```
59	C_global = Σ_s w_s · C_s
60	```
61	
62	Under A2, each C_s has the same symmetric structure, so:
63	
64	```
65	C_global = [[1 - π̄,  π̄    ],
66	            [π̄,      1 - π̄ ]]
67	```
68	
69	where **π̄ = Σ_s w_s · π_s** is the weighted average misclassification rate.
70	
71	By the same Bayes' rule argument: M_global = C_global (under A2+A3).
72	
73	## Step 4: Observed CATE Under Misclassification
74	
75	The observed CATE in subgroup s, conditioning on Ẑ:
76	
77	```
78	τ_obs(Ẑ=ẑ, S=s) = E[Y(1) - Y(0) | Ẑ=ẑ, S=s]
79	                 = Σ_z P(Z=z | Ẑ=ẑ, S=s) · τ(Z=z)
80	             
…[truncated 4345 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Read",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T04:41:07.942379+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T04:41:07.942655+00:00_

docs/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T04:41:07.942944+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/ 2>/dev/null",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/ 2>/dev/null",
    "description": "List paper directory contents"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T04:41:07.943217+00:00_

experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T04:41:07.943465+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T04:41:07.945168+00:00_

1	\section{Experiments}
2	
3	\subsection{Experimental Setup and Data Generation}
4	
5	\subsubsection{Synthetic DGP}
6	
7	We generate data from a controlled data-generating process (DGP) that separates the effect of subgroup-level misclassification heterogeneity from other confounders.
8	For each observation $i$, the potential outcome under treatment $t$ is
9	\begin{equation}
10	Y_i(t) = \alpha + \tau(Z_i) \cdot t + \beta X_i + \varepsilon_i, \quad \varepsilon_i \sim \mathcal{N}(0,1),
11	\end{equation}
12	where $T_i \sim \text{Bernoulli}(0.5)$ simulates a randomized controlled trial, and $Z_i \in \{0, \ldots, K{-}1\}$ is the true effect modifier with $K \in \{2, 4\}$ subgroups.
13	The conditional average treatment effect (CATE) $\tau(Z{=}z)$ varies across subgroups with controlled heterogeneity $\Delta\tau = \max_z \tau(z) - \min_z \tau(z)$.
14	Misclassification is injected through subgroup-specific symmetric confusion matrices $C_s$: the observed label $\hat{Z}_i$ is drawn as $\hat{Z}_i \sim \text{Multinomial}(C_{S_i})$, where each subgroup $s$ has error rate $\pi_s$ and $\Delta\pi = \max_s \pi_s - \min_s \pi_s$ controls heterogeneity.
15	We fix $N{=}5000$ observations and vary $n_{\text{expert}} \in \{50, 100, 250, 500, 1000, 2000\}$ (the number of expert-labeled observations used to estimate confusion matrices).
16	Each configuration is repeated for 100 Monte Carlo runs.
17	
18	\subsubsection{Semi-synthetic DGP (TweetEval)}
19	
20	To test EC-HTE under realistic conditions, we construct a semi-synthetic DGP from the TweetEval sentiment corpus~\cite{barbieri2020tweeteval}, sampling $N{=}5000$ tweets per run from a pool of 57{,}899.
21	Four subgroups are defined by crossing two binary text features: presence of hashtags (\texttt{has\_hashtag}) and text length relative to the median (\texttt{text\_length\_bin}).
22	This yields unbalanced subgroup proportions (S0: 39\%, S1: 38\%, S2: 12\%, S3: 11\%).
23	The effect modifier is $Z{=}1$ if the true sentiment is positive (
…[truncated 6104 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T04:41:07.945581+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find main.tex or preamble",
  "prompt": "Find any main.tex, preamble.tex, or .sty files in or near /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/ that might define theorem/proposition environments. Also check parent directories. Quick search."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find main.tex or preamble",
    "prompt": "Find any main.tex, preamble.tex, or .sty files in or near /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/ that might define theorem/proposition environments. Also check parent directories. Quick search."
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T04:41:07.945927+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T04:41:07.946185+00:00_

docs/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T04:41:07.946450+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/**/*.sty"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/**/*.sty"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T04:41:07.946693+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T04:41:07.946980+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T04:41:07.947223+00:00_

docs/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T04:41:07.947488+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/**/*.sty"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/**/*.sty"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T04:41:07.947728+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T04:41:07.948044+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/**/*main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/**/*main.tex"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-21T04:41:07.948292+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T04:41:07.948556+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/**/*preamble.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/**/*preamble.tex"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-21T04:41:07.948798+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T04:41:07.949086+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/**/*.sty"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/**/*.sty"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T04:41:07.949327+00:00_

artifacts/dream_reports/dream_20260521T032758/worst/acl.sty

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T04:41:07.949587+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs -type f -name \"*.tex\" -o -name \"*.sty\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs -type f -name \"*.tex\" -o -name \"*.sty\" 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T04:41:07.949871+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/ 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T04:41:07.950123+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-21T04:41:07.950358+00:00_

total 32
drwxr-xr-x 3 ubuntu ubuntu  4096 May 21 04:09 .
drwxr-xr-x 7 ubuntu ubuntu  4096 May 21 04:17 ..
-rw-r--r-- 1 ubuntu ubuntu 18796 May 20 18:52 IDEA_BRIEF.md
drwxr-xr-x 2 ubuntu ubuntu  4096 May 21 04:34 paper

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-21T04:41:07.950774+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/ 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-21T04:41:07.951087+00:00_

total 24
drwxr-xr-x 2 ubuntu ubuntu  4096 May 21 04:34 .
drwxr-xr-x 3 ubuntu ubuntu  4096 May 21 04:09 ..
-rw-r--r-- 1 ubuntu ubuntu 14460 May 21 04:34 experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-21T04:41:07.951371+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\(newtheorem|theorem|proposition|lemma|corollary)[\\s{]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\(newtheorem|theorem|proposition|lemma|corollary)[\\s{]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-21T04:41:07.951614+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-21T04:41:07.951923+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-21T04:41:07.952304+00:00_

1	\section{Experiments}
2	
3	\subsection{Experimental Setup and Data Generation}
4	
5	\subsubsection{Synthetic DGP}
6	
7	We generate data from a controlled data-generating process (DGP) that separates the effect of subgroup-level misclassification heterogeneity from other confounders.
8	For each observation $i$, the potential outcome under treatment $t$ is
9	\begin{equation}
10	Y_i(t) = \alpha + \tau(Z_i) \cdot t + \beta X_i + \varepsilon_i, \quad \varepsilon_i \sim \mathcal{N}(0,1),
11	\end{equation}
12	where $T_i \sim \text{Bernoulli}(0.5)$ simulates a randomized controlled trial, and $Z_i \in \{0, \ldots, K{-}1\}$ is the true effect modifier with $K \in \{2, 4\}$ subgroups.
13	The conditional average treatment effect (CATE) $\tau(Z{=}z)$ varies across subgroups with controlled heterogeneity $\Delta\tau = \max_z \tau(z) - \min_z \tau(z)$.
14	Misclassification is injected through subgroup-specific symmetric confusion matrices $C_s$: the observed label $\hat{Z}_i$ is drawn as $\hat{Z}_i \sim \text{Multinomial}(C_{S_i})$, where each subgroup $s$ has error rate $\pi_s$ and $\Delta\pi = \max_s \pi_s - \min_s \pi_s$ controls heterogeneity.
15	We fix $N{=}5000$ observations and vary $n_{\text{expert}} \in \{50, 100, 250, 500, 1000, 2000\}$ (the number of expert-labeled observations used to estimate confusion matrices).
16	Each configuration is repeated for 100 Monte Carlo runs.
17	
18	\subsubsection{Semi-synthetic DGP (TweetEval)}
19	
20	To test EC-HTE under realistic conditions, we construct a semi-synthetic DGP from the TweetEval sentiment corpus~\cite{barbieri2020tweeteval}, sampling $N{=}5000$ tweets per run from a pool of 57{,}899.
21	Four subgroups are defined by crossing two binary text features: presence of hashtags (\texttt{has\_hashtag}) and text length relative to the median (\texttt{text\_length\_bin}).
22	This yields unbalanced subgroup proportions (S0: 39\%, S1: 38\%, S2: 12\%, S3: 11\%).
23	The effect modifier is $Z{=}1$ if the true sentiment is positive (
…[truncated 13096 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T04:41:07.952657+00:00_

**Summary:**

No main.tex, preamble.tex, or .sty files with theorem/proposition environment definitions were found in the paper directory.

**Files located:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex` - This is the only .tex file in the paper directory, and it contains only experiment sections (no environment definitions). The file has tabular content and cross-references but no `\newtheorem` or environment declarations.

**Search results:**
- No preamble.tex found in the directory hierarchy
- No main.tex found
- No .sty style files in the paper or docs directories
- A single .sty file exists elsewhere: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260521T032758/worst/acl.sty` (artifact from a previous run, not a project source file)

**Conclusion:** The paper directory appears to be incomplete or still under construction. The experiments.tex file is present but there's no master main.tex file, no preamble defining environments, and no project-specific .sty files. To locate theorem/proposition environment definitions, you would need to check where the main document structure is defined, or it may need to be created.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Agent",
  "elapsed_ms": 7
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T04:41:07.956761+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex",
  "content": "% Requires preamble: \\usepackage{amsthm,amsmath,amssymb}\n% and: \\newtheorem{proposition}{Proposition}\n\n\\section{Bias Decomposition: When Debiasing Hurts}\n\\label{sec:theory}\n\nWe formalize the bias that global misclassification correction introduces when subgroup error rates are heterogeneous.\nConsider estimating the conditional average treatment effect (CATE) $\\tau(z) = \\mathbb{E}[Y(1) - Y(0) \\mid Z = z]$, where $Z \\in \\{0, 1\\}$ is a binary effect modifier observed only through a noisy annotation $\\hat{Z}$.\nThe population consists of $K$ subgroups $S \\in \\{1, \\ldots, K\\}$ with weights $w_s = P(S{=}s)$, each characterized by a $2 \\times 2$ confusion matrix $C_s$ with symmetric error rate $\\pi_s = P(\\hat{Z} \\neq Z \\mid S{=}s)$.\nStandard practice estimates a single confusion matrix $\\bar{C} = \\sum_s w_s C_s$ from expert annotations and applies its inverse uniformly to all observations, with pooled error rate $\\bar{\\pi} = \\sum_s w_s \\pi_s$.\nWe show that when error rates vary across subgroups, this global procedure introduces a bias with an exact product form.\n\nWe state four assumptions maintained throughout.\n%\n\\begin{itemize}\n\\item[\\textbf{(A1)}] \\textit{Conditional independence:} misclassification depends only on the true label $Z$ and subgroup $S$, not on potential outcomes $Y(0), Y(1)$.\n\\item[\\textbf{(A2)}] \\textit{Symmetric misclassification:} $P(\\hat{Z}{=}1 \\mid Z{=}0, S{=}s) = P(\\hat{Z}{=}0 \\mid Z{=}1, S{=}s) = \\pi_s$ for all $s$.\n\\item[\\textbf{(A3)}] \\textit{Balanced effect modifier:} $P(Z{=}0) = P(Z{=}1) = 0.5$. This simplifies the exposition; we discuss relaxation below.\n\\item[\\textbf{(A4)}] \\textit{Non-degeneracy:} $\\pi_s \\neq 0.5$ for all $s$, ensuring each $C_s$ is invertible.\n\\end{itemize}\n\nUnder (A2)--(A3), the Bayesian mixing matrix $M_s$ (entries $M_s[\\hat{z}, z] = P(Z{=}z \\mid \\hat{Z}{=}\\hat{z}, S{=}s)$) coincides with $C_s$.\nThe global mixing matrix is $M_{\\text{global}} = \\sum_s w_s M_s$.\n\n\\begin{proposition}[Bias Decomposition Identity]\n\\label{prop:bias_identity}\nUnder \\textnormal{(A1)--(A4)}, the bias of global correction in subgroup $s$ at effect-modifier level $z$ is\n\\begin{align}\n\\mathrm{bias}_{\\mathrm{global}}(z{=}0, s) &= +\\frac{\\delta_s \\cdot \\Delta\\tau}{1 - 2\\bar{\\pi}}, \\label{eq:bias_z0} \\\\\n\\mathrm{bias}_{\\mathrm{global}}(z{=}1, s) &= -\\frac{\\delta_s \\cdot \\Delta\\tau}{1 - 2\\bar{\\pi}}, \\label{eq:bias_z1}\n\\end{align}\nwhere $\\delta_s = \\pi_s - \\bar{\\pi}$ is the subgroup deviation from the pooled error rate and $\\Delta\\tau = \\tau(1) - \\tau(0)$ is the CATE heterogeneity.\n\\end{proposition}\n\nEquations~\\eqref{eq:bias_z0}--\\eqref{eq:bias_z1} constitute an exact identity at the population level, not a bound.\nThe bias factors into three interpretable components: $\\delta_s$ captures how much subgroup $s$ deviates from the average misclassification rate, $\\Delta\\tau$ captures treatment effect heterogeneity across levels of $Z$, and $1/(1 - 2\\bar{\\pi})$ is an amplification factor from matrix inversion.\nBias vanishes when either source of variation is absent ($\\delta_s = 0$ or $\\Delta\\tau = 0$), and arises only through their interaction.\nProposition~\\ref{prop:bias_identity} implies that global correction trades one source of confounding for another: it removes attenuation from label noise but introduces a new bias from error-rate heterogeneity.\n\n\\paragraph{Proof sketch.}\nGlobal correction applies $M_{\\text{global}}^{-1}$ to the subgroup-specific observed CATE $\\tau_{\\text{obs}}(\\cdot, s) = M_s \\cdot \\tau_{\\text{true}}$, yielding bias $(M_{\\text{global}}^{-1} M_s - I) \\cdot \\tau_{\\text{true}}$.\nDirect computation shows $M_{\\text{global}}^{-1} M_s - I = \\frac{\\delta_s}{1-2\\bar{\\pi}} \\bigl[\\begin{smallmatrix} -1 & 1 \\\\ 1 & -1 \\end{smallmatrix}\\bigr]$.\nApplying this matrix to $[\\tau(0),\\, \\tau(1)]^\\top$ produces the product form.\nThe full derivation appears in Appendix~\\ref{app:derivation}.\n\n\\paragraph{Remark (generalization).}\nThe identity holds for arbitrary $K$ with the same formula; the essential structure is $\\sum_s w_s \\delta_s = 0$ (deviations sum to zero by construction).\nAssumption~(A3) ensures $M_s = C_s$; when $P(Z{=}1) \\neq 0.5$, the mixing matrices acquire asymmetric entries, but the product structure of the bias persists with modified coefficients (Appendix~\\ref{app:derivation}).\nEmpirical verification (Section~\\ref{sec:bias_mechanism}) yields $R^2 = 0.994$ for $K{=}2$ and $R^2 = 0.974$ for $K{=}4$; the residual variance reflects finite-sample Monte Carlo noise, not model misspecification.\n\n\\begin{proposition}[Debiasing Can Increase Bias]\n\\label{prop:debiasing_hurts}\nUnder \\textnormal{(A1)--(A4)}, global correction produces larger absolute bias than the naive estimator ($|\\mathrm{bias}_{\\mathrm{global}}| > |\\mathrm{bias}_{\\mathrm{naive}}|$) in subgroup $s$ if and only if\n\\begin{equation}\n\\frac{|\\delta_s|}{(1 - 2\\bar{\\pi}) \\cdot \\pi_s} > 1.\n\\label{eq:hurts_condition}\n\\end{equation}\n\\end{proposition}\n\nEquation~\\eqref{eq:hurts_condition} partitions subgroups into two regimes.\nFor high-error subgroups ($\\pi_s > \\bar{\\pi}$), the condition reduces to $\\pi_s > 0.5$, which is excluded by~(A4); global correction always reduces bias in these subgroups.\nFor low-error subgroups ($\\pi_s < \\bar{\\pi}$), the condition holds whenever $\\pi_s < \\bar{\\pi} / (2(1 - \\bar{\\pi}))$.\nThis threshold is easily satisfied in practice: when $\\bar{\\pi} = 0.15$, any subgroup with $\\pi_s < 0.088$ experiences increased bias from global correction.\nThe mechanism is that global correction inverts the pooled confusion matrix, applying a correction calibrated for the average error rate; high-error subgroups are under-corrected (bias reduced but not eliminated), while low-error subgroups are over-corrected (the correction overshoots and reverses the sign of bias).\nFor subgroups with near-zero misclassification ($\\pi_s \\approx 0$), the naive estimator is nearly unbiased, yet global correction creates substantial bias where none existed.\nThis is the most consequential implication of Proposition~\\ref{prop:bias_identity}: debiasing can be worse than doing nothing.\n\nIn our experiments (Section~\\ref{sec:bias_mechanism}), global correction increases bias in 50\\% of parameter configurations (260 of 520, excluding cases where $\\Delta_c{=}0$).\nMaximum amplification reaches $2.86\\times$ for $K{=}2$ and $5.9\\times$ for $K{=}4$ with a CausalForest estimator; the phenomenon intensifies with more subgroups as the range of $\\delta_s$ values widens.\nFigure~\\ref{fig:heatmap} visualizes the amplification across the full $\\Delta\\pi \\times \\Delta\\tau$ parameter grid.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex",
    "content": "% Requires preamble: \\usepackage{amsthm,amsmath,amssymb}\n% and: \\newtheorem{proposition}{Proposition}\n\n\\section{Bias Decomposition: When Debiasing Hurts}\n\\label{sec:theory}\n\nWe formalize the bias that global misclassification correction introduces when subgroup error rates are heterogeneous.\nConsider estimating the conditional average treatment effect (CATE) $\\tau(z) = \\mathbb{E}[Y(1) - Y(0) \\mid Z = z]$, where $Z \\in \\{0, 1\\}$ is a binary effect modifier observed only through a noisy annotation $\\hat{Z}$.\nThe population consists of $K$ subgroups $S \\in \\{1, \\ldots, K\\}$ with weights $w_s = P(S{=}s)$, each characterized by a $2 \\times 2$ confusion matrix $C_s$ with symmetric error rate $\\pi_s = P(\\hat{Z} \\neq Z \\mid S{=}s)$.\nStandard practice estimates a single confusion matrix $\\bar{C} = \\sum_s w_s C_s$ from expert annotations and applies its inverse uniformly to all observations, with pooled error rate $\\bar{\\pi} = \\sum_s w_s \\pi_s$.\nWe show that when error rates vary across subgroups, this global procedure introduces a bias with an exact product form.\n\nWe state four assumptions maintained throughout.\n%\n\\begin{itemize}\n\\item[\\textbf{(A1)}] \\textit{Conditional independence:} misclassification depends only on the true label $Z$ and subgroup $S$, not on potential outcomes $Y(0), Y(1)$.\n\\item[\\textbf{(A2)}] \\textit{Symmetric misclassification:} $P(\\hat{Z}{=}1 \\mid Z{=}0, S{=}s) = P(\\hat{Z}{=}0 \\mid Z{=}1, S{=}s) = \\pi_s$ for all $s$.\n\\item[\\textbf{(A3)}] \\textit{Balanced effect modifier:} $P(Z{=}0) = P(Z{=}1) = 0.5$. This simplifies the exposition; we discuss relaxation below.\n\\item[\\textbf{(A4)}] \\textit{Non-degeneracy:} $\\pi_s \\neq 0.5$ for all $s$, ensuring each $C_s$ is invertible.\n\\end{itemize}\n\nUnder (A2)--(A3), the Bayesian mixing matrix $M_s$ (entries $M_s[\\hat{z}, z] = P(Z{=}z \\mid \\hat{Z}{=}\\hat{z}, S{=}s)$) coincides with $C_s$.\nThe global mixing matrix is $M_{\\text{global}} = \\sum_s w_s M_s$.\n\n\\begin{proposition}[Bias Decomposition Identity]\n\\label{prop:bias_identity}\nUnder \\textnormal{(A1)--(A4)}, the bias of global correction in subgroup $s$ at effect-modifier level $z$ is\n\\begin{align}\n\\mathrm{bias}_{\\mathrm{global}}(z{=}0, s) &= +\\frac{\\delta_s \\cdot \\Delta\\tau}{1 - 2\\bar{\\pi}}, \\label{eq:bias_z0} \\\\\n\\mathrm{bias}_{\\mathrm{global}}(z{=}1, s) &= -\\frac{\\delta_s \\cdot \\Delta\\tau}{1 - 2\\bar{\\pi}}, \\label{eq:bias_z1}\n\\end{align}\nwhere $\\delta_s = \\pi_s - \\bar{\\pi}$ is the subgroup deviation from the pooled error rate and $\\Delta\\tau = \\tau(1) - \\tau(0)$ is the CATE heterogeneity.\n\\end{proposition}\n\nEquations~\\eqref{eq:bias_z0}--\\eqref{eq:bias_z1} constitute an exact identity at the population level, not a bound.\nThe bias factors into three interpretable components: $\\delta_s$ captures how much subgroup $s$ deviates from the average misclassification rate, $\\Delta\\tau$ captures treatment effect heterogeneity across levels of $Z$, and $1/(1 - 2\\bar{\\pi})$ is an amplification factor from matrix inversion.\nBias vanishes when either source of variation is absent ($\\delta_s = 0$ or $\\Delta\\tau = 0$), and arises only through their interaction.\nProposition~\\ref{prop:bias_identity} implies that global correction trades one source of confounding for another: it removes attenuation from label noise but introduces a new bias from error-rate heterogeneity.\n\n\\paragraph{Proof sketch.}\nGlobal correction applies $M_{\\text{global}}^{-1}$ to the subgroup-specific observed CATE $\\tau_{\\text{obs}}(\\cdot, s) = M_s \\cdot \\tau_{\\text{true}}$, yielding bias $(M_{\\text{global}}^{-1} M_s - I) \\cdot \\tau_{\\text{true}}$.\nDirect computation shows $M_{\\text{global}}^{-1} M_s - I = \\frac{\\delta_s}{1-2\\bar{\\pi}} \\bigl[\\begin{smallmatrix} -1 & 1 \\\\ 1 & -1 \\end{smallmatrix}\\bigr]$.\nApplying this matrix to $[\\tau(0),\\, \\tau(1)]^\\top$ produces the product form.\nThe full derivation appears in Appendix~\\ref{app:derivation}.\n\n\\paragraph{Remark (generalization).}\nThe identity holds for arbitrary $K$ with the same formula; the essential structure is $\\sum_s w_s \\delta_s = 0$ (deviations sum to zero by construction).\nAssumption~(A3) ensures $M_s = C_s$; when $P(Z{=}1) \\neq 0.5$, the mixing matrices acquire asymmetric entries, but the product structure of the bias persists with modified coefficients (Appendix~\\ref{app:derivation}).\nEmpirical verification (Section~\\ref{sec:bias_mechanism}) yields $R^2 = 0.994$ for $K{=}2$ and $R^2 = 0.974$ for $K{=}4$; the residual variance reflects finite-sample Monte Carlo noise, not model misspecification.\n\n\\begin{proposition}[Debiasing Can Increase Bias]\n\\label{prop:debiasing_hurts}\nUnder \\textnormal{(A1)--(A4)}, global correction produces larger absolute bias than the naive estimator ($|\\mathrm{bias}_{\\mathrm{global}}| > |\\mathrm{bias}_{\\mathrm{naive}}|$) in subgroup $s$ if and only if\n\\begin{equation}\n\\frac{|\\delta_s|}{(1 - 2\\bar{\\pi}) \\cdot \\pi_s} > 1.\n\\label{eq:hurts_condition}\n\\end{equation}\n\\end{proposition}\n\nEquation~\\eqref{eq:hurts_condition} partitions subgroups into two regimes.\nFor high-error subgroups ($\\pi_s > \\bar{\\pi}$), the condition reduces to $\\pi_s > 0.5$, which is excluded by~(A4); global correction always reduces bias in these subgroups.\nFor low-error subgroups ($\\pi_s < \\bar{\\pi}$), the condition holds whenever $\\pi_s < \\bar{\\pi} / (2(1 - \\bar{\\pi}))$.\nThis threshold is easily satisfied in practice: when $\\bar{\\pi} = 0.15$, any subgroup with $\\pi_s < 0.088$ experiences increased bias from global correction.\nThe mechanism is that global correction inverts the pooled confusion matrix, applying a correction calibrated for the average error rate; high-error subgroups are under-corrected (bias reduced but not eliminated), while low-error subgroups are over-corrected (the correction overshoots and reverses the sign of bias).\nFor subgroups with near-zero misclassification ($\\pi_s \\approx 0$), the naive estimator is nearly unbiased, yet global correction creates substantial bias where none existed.\nThis is the most consequential implication of Proposition~\\ref{prop:bias_identity}: debiasing can be worse than doing nothing.\n\nIn our experiments (Section~\\ref{sec:bias_mechanism}), global correction increases bias in 50\\% of parameter configurations (260 of 520, excluding cases where $\\Delta_c{=}0$).\nMaximum amplification reaches $2.86\\times$ for $K{=}2$ and $5.9\\times$ for $K{=}4$ with a CausalForest estimator; the phenomenon intensifies with more subgroups as the range of $\\delta_s$ values widens.\nFigure~\\ref{fig:heatmap} visualizes the amplification across the full $\\Delta\\pi \\times \\Delta\\tau$ parameter grid.\n"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T04:41:07.957310+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T04:41:07.957621+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T04:41:07.958148+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T04:41:07.958424+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing[,.]?\\s*$",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing[,.]?\\s*$",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T04:41:07.958679+00:00_

66:This is the most consequential implication of Proposition~\ref{prop:bias_identity}: debiasing can be worse than doing nothing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T04:41:07.958968+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Furthermore|Moreover|Additionally|remarkable|novel|delve|leverage|utilize",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Furthermore|Moreover|Additionally|remarkable|novel|delve|leverage|utilize",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T04:41:07.959223+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_theory_20260521T043620",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-21T04:41:07.959563+00:00_

All clean. The grep match on line 66 is "doing nothing" (a gerund as object of "than"), not a dangling participial phrase ending.

Written `theory.tex` (~770 words + equations, ~1 page in two-column). Contains:
- Setup with formal CATE estimation problem
- Assumptions (A1)--(A4) as an itemized list
- **Proposition 1** (Bias Decomposition Identity): exact $\delta_s \cdot \Delta\tau / (1-2\bar{\pi})$ identity with interpretation
- Proof sketch (3 lines + appendix reference)
- Remark on $K > 2$ generalization and (A3) relaxation
- **Proposition 2** (Debiasing Can Increase Bias): necessary and sufficient condition with the high-$\pi$/low-$\pi$ asymmetry analysis
- Cross-references to Figure 2, Section 5.2, and Appendix

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_theory_20260521T043620"
}
```

</details>

---

# paper writing introduction

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_paper_writing_introduction_20260526T163729.jsonl`
- **Structured JSON:** [`9f0fff6f3ae383c8dd00.json`](../../sessions/9f/9f0fff6f3ae383c8dd00.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-26T16:42:15.389390+00:00_

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
  "session": "worker_paper_writing_introduction_20260526T163729",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T16:42:15.390244+00:00_

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
  "session": "worker_paper_writing_introduction_20260526T163729",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T16:42:15.390567+00:00_

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
  "session": "worker_paper_writing_introduction_20260526T163729",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T16:42:15.391142+00:00_

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
  "session": "worker_paper_writing_introduction_20260526T163729",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T16:42:15.391400+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260526T163729",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T16:42:15.391760+00:00_

1	\section{Experimental Setup and Metrics}\label{sec:method}
2	
3	This section defines the benchmark, models, training procedures, and evaluation metrics that underpin the analyses in Sections~\ref{sec:fake_safety}--\ref{sec:avoidance_source}. The central methodological contribution is the displacement-filtered Collision Avoidance Rate (CAR$_\text{f}$), a corrective metric that separates genuine obstacle avoidance from action collapse (\S\ref{sec:dfcar}).
4	
5	\subsection{Benchmark and Models}\label{sec:benchmark}
6	
7	We conduct all experiments on SafeLIBERO~\cite{hu2025vlsa}, a collision-aware evaluation extension of the LIBERO simulation platform~\cite{liu2023libero}. SafeLIBERO augments standard manipulation tasks with per-timestep collision detection and non-target obstacle annotations, enabling systematic measurement of both task completion and safety. We select the \textit{object\_pudding} suite (Level~I), which comprises four tabletop manipulation tasks: pick \texttt{orange\_juice}, \texttt{chocolate\_pudding}, \texttt{milk}, or \texttt{bbq\_sauce} and place into a basket. In each task, non-target objects surround the manipulation target, and the MuJoCo physics engine registers any contact between the robot and a non-target object as a collision event.
8	
9	We evaluate two Vision-Language-Action (VLA) models from the Pi0 family~\cite{black2024pi0}. \textbf{Pi0} (${\sim}$2.5B parameters) pairs a PaliGemma vision-language encoder with a dedicated action expert that generates continuous actions via flow matching~\cite{lipman2023flow}. \textbf{Pi0.5} (from Physical Intelligence) extends this architecture with broader pre-training data and serves as a stronger baseline with substantially higher task capability and less susceptibility to action collapse.
10	
11	Table~\ref{tab:configurations} summarizes the seven evaluated configurations. Each model is trained for 30K steps. Evaluation uses 50 episodes per task across 4 tasks (200 episodes per configuration). For m
…[truncated 8890 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260526T163729",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T16:42:15.392014+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260526T163729",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T16:42:15.392309+00:00_

1	\section{The Fake Safety Problem}\label{sec:fake_safety}
2	
3	Standard CAR evaluation assumes that a collision-free episode reflects deliberate obstacle avoidance. This assumption fails when a model has collapsed into inaction: a robot that never moves will never collide, yet it has not avoided anything. We show that this failure mode dominates the safety scores of Pi0-family models and introduce CAR$_\text{f}$ as a corrective diagnostic.
4	
5	\subsection{Action Collapse Contamination}\label{sec:collapse}
6	
7	Our Pi0+A1 configuration (SDF auxiliary loss on Pi0; see Section~\ref{sec:sdf_aux} for the training anomaly) achieves a CAR of 91.5\% across 800 evaluation episodes, a figure that would suggest reliable obstacle avoidance. Displacement analysis\footnote{These statistics are computed from obstacle displacement recorded by the original evaluation protocol.} tells a different story. Of the 732 episodes classified as safe, 541 (73.9\%) exhibit maximum displacement below 1\,$\mu$m, another 188 (25.7\%) remain below 0.1\,mm, and only 3 (0.4\%) exceed the 0.1\,mm threshold. The remaining 99.6\% of safe episodes are artifacts of a robot that never moved. TSR is 0\% across all 800 episodes: the model produces no task-directed behavior whatsoever.
8	
9	Applying CAR$_\text{f}$ (Eq.~\ref{eq:car_f}) filters out these action-collapsed episodes. Pi0+A1 drops from CAR\,=\,91.5\% to CAR$_\text{f} \approx 0$\%, because only 3 of 732 safe episodes survive displacement filtering. This is the primary demonstration of what CAR$_\text{f}$ is designed to detect: a headline safety score that is entirely attributable to inaction.
10	
11	The contamination is not specific to the SDF auxiliary loss. Pi0 Full-FT reports CAR\,=\,83.0\% with TSR\,=\,0.5\%, and 99.4\% of its safe episodes are fake safe, yielding CAR$_\text{f} \approx 0$\%. Pi0 LoRA (without any collision objective) achieves CAR\,=\,82.0\%, TSR\,=\,0\%, with a comparable fake safe rate. Across all three Pi0 configurations, C
…[truncated 6416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260526T163729",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T16:42:15.392583+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260526T163729",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T16:42:15.392844+00:00_

1	\section{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\label{sec:ee_only}
2	
3	Section~\ref{sec:fake_safety} establishes that fake safety dominates Pi0's CAR scores. A natural question remains: could a perfect SDF signal enable effective refinement? We test this with oracle experiments (Section~\ref{sec:oracle_setup}) that replace the learned SDF with ground-truth distance fields from simulation geometry. If EE-only refinement is structurally sound, these oracles should exceed unrefined baselines by a wide margin.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Oracle SDF refinement with ground-truth distance fields. Oracle variants evaluated over 160 episodes (4 tasks $\times$ 40); baselines and A3 over 200 episodes (4 tasks $\times$ 50). All three oracle variants achieve lower CAR than unrefined baselines, and fake safe rates remain above 96\%. Fake safe rate computed using obstacle displacement threshold; see Table~\ref{tab:fake_safety} footnote for measurement protocol details.}
8	\label{tab:oracle}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lcccc}
12	\toprule
13	Method & TSR (\%) & CAR (\%) & Fake Safe (\%) & Refines/ep \\
14	\midrule
15	LoRA baseline (no refine) & 0.0 & 82.0 & 99.4 & -- \\
16	Full-FT baseline (no refine) & 0.5 & 83.0 & -- & -- \\
17	\midrule
18	Oracle-adaptive (GT, dyn.\ $\alpha$) & 0.0 & 75.0 & 98.3 & 14.2 \\
19	Oracle-fixed (GT, $\alpha{=}0.005$) & 0.0 & 73.1 & 98.3 & 14.8 \\
20	Oracle-feature (GT, feat.\ space) & 0.0 & 76.9 & 96.7 & 241.7 \\
21	\midrule
22	A3 learned SDF & 0.0 & 74.5 & -- & 0.0 \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	Table~\ref{tab:oracle} reports the results. All three oracle variants achieve \emph{lower} CAR than both unrefined baselines. The best oracle (Oracle-feature, 76.9\%) falls 5.1 points below LoRA (82.0\%) and 6.1 points below Full-FT (83.0\%). Oracle-adaptive and Oracle-fixed perform worse still at 75.0\% and 73.1\%. Refinement with perfect distance information produces more collisions 
…[truncated 3317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260526T163729",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-26T16:42:15.393080+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260526T163729",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-26T16:42:15.393373+00:00_

1	\section{Avoidance Source Diagnosis}\label{sec:avoidance_source}
2	
3	Sections~\ref{sec:fake_safety} and~\ref{sec:ee_only} establish that standard CAR is contaminated by action collapse and that end-effector-only SDF refinement fails structurally. A constructive question remains: when collision avoidance does improve in fine-tuned models, where does the signal originate? We isolate the contribution of SDF geometric supervision from LoRA fine-tuning on collision-free demonstrations by comparing three conditions on Pi0.5: LoRA-only (no SDF), LoRA+SDF at $\lambda = 0.005$, and LoRA+SDF at $\lambda = 0.01$. All models are evaluated at the 30K-step checkpoint with rotation-corrected evaluation (Section~\ref{sec:dfcar}).
4	
5	\begin{table}[t]
6	\centering
7	\caption{Avoidance source attribution on SafeLIBERO (200 episodes per seed, 30K-step checkpoints). At $\lambda \in \{0.005, 0.01\}$, SDF adds no measurable CAR beyond LoRA-only ($p > 0.1$). All fine-tuned models exhibit 0\% frozen rate and EE displacement above 0.37\,m, confirming genuine active avoidance.}
8	\label{tab:avoidance_source}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	Method & Seeds & TSR (\%) & CAR (\%) & EE Disp (m) & Frozen (\%) \\
14	\midrule
15	Pi0.5 baseline & 3 & 74.7\,$\pm$\,1.5 & 26.8\,$\pm$\,1.6 & 0.367 & 0.0 \\
16	\midrule
17	LoRA-only (no SDF) & 2 & 6.3 & 54.5 & 0.392 & 0.0 \\
18	LoRA+SDF $\lambda{=}0.005$ & 3 & 6.8 & 54.5 & 0.387 & 0.0 \\
19	LoRA+SDF $\lambda{=}0.01$ & 3 & 6.5 & 56.3 & 0.389 & 0.0 \\
20	\bottomrule
21	\end{tabular}
22	\end{table}
23	
24	Table~\ref{tab:avoidance_source} reports the results. LoRA fine-tuning without any SDF objective achieves CAR of 54.5\% across two seeds. LoRA+SDF at $\lambda = 0.005$ (three seeds) produces identical CAR of 54.5\%, and $\lambda = 0.01$ (three seeds) reaches 56.3\%. All fine-tuned configurations register 0\% frozen episodes and mean EE displacement above 0.37\,m, confirming that the collision avoidance reflected in CAR 
…[truncated 6387 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260526T163729",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T16:42:15.393848+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260526T163729",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-26T16:42:15.394071+00:00_

docs/paper/_archive/method.tex
docs/paper/_archive/experiments.tex
docs/paper/_archive/conclusion_DEPRECATED.tex
docs/paper/analysis_claim4.tex
docs/paper/appendix.tex
docs/paper/experimental_framework.tex
docs/paper/analysis_claim3.tex
docs/paper/abstract.tex
docs/paper/analysis_claim1.tex
docs/paper/analysis_claim2.tex
docs/paper/discussion.tex
docs/paper/introduction.tex
docs/paper/method.tex
docs/paper/claim2.tex
docs/paper/claim1.tex
docs/paper/main.tex
docs/paper/related_work.tex
docs/paper/claim3.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260526T163729",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T16:42:15.394274+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260526T163729",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-26T16:42:15.394566+00:00_

1	\section{Introduction}
2	
3	A model that reports 91.5\% collision avoidance and completes zero tasks has not learned safety; it has learned to stop moving.
4	
5	Vision-Language-Action (VLA) models unify visual perception, language understanding, and continuous action generation in a single architecture. Models such as $\pi_0$~\cite{black2024pi0}, OpenVLA~\cite{kim2024openvla}, and RT-2~\cite{brohan2023rt2} can follow diverse natural language instructions across manipulation tasks. As these models move toward real-world deployment, a critical failure mode has emerged: frequent collisions with non-target objects in cluttered environments. The demonstration data used for training typically features unobstructed workspaces, and the resulting policies acquire no explicit incentive to maintain clearance from nearby surfaces. Collisions cause task failure, risk damage to the robot and its surroundings, and represent a central barrier to safe deployment. The SafeLIBERO benchmark~\cite{hu2025vlsa}, comprising 32 collision scenarios across 1,600 evaluation episodes, was introduced to systematically quantify this problem and confirms that even high-performing VLAs exhibit substantial collision rates when non-target objects surround the manipulation target.
6	
7	Several recent methods target collision avoidance in VLAs. AEGIS~\cite{hu2025vlsa} applies post-hoc Control Barrier Function (CBF) corrections to already-generated trajectories and reports an average Collision Avoidance Rate (CAR) of 77.85\% across SafeLIBERO scenarios without additional training. SafeVLA~\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\% through reward shaping during reinforcement learning. CoFreeVLA~\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that halts execution when predicted collision risk exceeds a threshold. In our own experiments, a Pi0 model fine-tuned with an auxiliary Signed Distance Field (SDF)
…[truncated 6077 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260526T163729",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-26T16:42:15.394818+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260526T163729",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-26T16:42:15.395038+00:00_

1	\documentclass[10pt,letterpaper]{article}
2	
3	\usepackage[margin=1in]{geometry}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{hyperref}
8	\usepackage{natbib}
9	\usepackage{xcolor}
10	\usepackage{multirow}
11	\usepackage{subcaption}
12	\graphicspath{{../../artifacts/figures/}}
13	
14	\newcommand{\placeholder}[1]{\textcolor{red}{\textbf{[#1]}}}
15	\newcommand{\dfCAR}{\text{dfCAR}}
16	
17	\bibliographystyle{plainnat}
18	
19	\title{Rethinking VLA Safety Evaluation:\\When 98\% of Collision Avoidance is an Illusion}
20	
21	\author{
22	  Anonymous Authors
23	}
24	
25	\date{}
26	
27	\begin{document}
28	
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	
35	\input{related_work}
36	
37	\input{method}
38	
39	\input{claim1}
40	
41	\input{claim2}
42	
43	\input{claim3}
44	
45	\input{discussion}
46	
47	\bibliography{references}
48	
49	\appendix
50	\input{appendix}
51	
52	\end{document}
53	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260526T163729",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-26T16:42:15.395513+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
  "content": "\\section{Introduction}\\label{sec:intro}\n\nVision-Language-Action (VLA) models that operate in physical environments must avoid collisions with objects and people. Collision incidents cause task failure, risk damage to the robot and its surroundings, and represent a primary barrier to deploying VLAs outside controlled laboratory settings~\\cite{li2026vlasafety}. The SafeLIBERO benchmark~\\cite{hu2025vlsa}, an extension of the LIBERO simulation platform~\\cite{liu2023libero}, provides the first systematic protocol for measuring collision behavior in VLA manipulation tasks, reporting the Collision Avoidance Rate (CAR) as the fraction of episodes free from robot-obstacle contact. Recent methods have adopted this evaluation framework to demonstrate safety improvements: SDF-augmented training~\\cite{zhang2025safevla}, constraint-based planning~\\cite{yang2025cape}, and collision-free demonstration learning~\\cite{cofreeevla2026} all report high CAR under standard evaluation. Our own SDF-augmented Pi0~\\cite{black2024pi0} configuration reaches 91.5\\% CAR across 800 evaluation episodes. The collision avoidance problem appears close to solved.\n\n\\begin{figure}[t]\n\\centering\n\\fbox{\\parbox{0.92\\linewidth}{\\vspace{3.5cm}\\centering\\textit{Placeholder: Figure 1. The fake safety problem.\\\\Left: Pi0+A1 achieves CAR\\,=\\,91.5\\% but TSR\\,=\\,0\\% (robot frozen, EE displacement $<$\\,0.1\\,mm).\\\\Center: Displacement-filtered CAR$_\\text{f}$ drops Pi0+A1 to ${\\approx}$\\,0\\%.\\\\Right: Pi0.5 achieves CAR\\,=\\,28.5\\% with TSR\\,=\\,71.5\\% (all safe episodes above 288\\,mm displacement).}\\vspace{3.5cm}}}\n\\caption{The fake safety problem in VLA collision avoidance evaluation. Standard CAR classifies a frozen robot as safe because it produces zero collisions (left). CAR$_\\text{f}$ filters out action-collapsed episodes where end-effector displacement falls below $\\tau_d$, revealing that Pi0+A1's 91.5\\% safety score drops to ${\\approx}$\\,0\\% (center). Pi0.5 exhibits genuine avoidance with active motion above 288\\,mm in all safe episodes, and CAR$_\\text{f}$ equals raw CAR (right).}\n\\label{fig:teaser}\n\\end{figure}\n\nIt is not. Of the 732 episodes that Pi0+A1 classifies as collision-free, 99.6\\% exhibit maximum end-effector (EE) displacement below 0.1\\,mm, and 73.9\\% remain below 1\\,$\\mu$m. The Task Success Rate (TSR) is 0\\% across all 800 episodes: the model produces no task-directed behavior. The robot generates sub-actuator-resolution motion, records no collisions by default, and receives credit for obstacle avoidance it never performed. The same pattern holds across the Pi0 model family. Pi0 Full Fine-Tune reports CAR\\,=\\,83.0\\% with TSR\\,=\\,0.5\\% and 99.4\\% fake safe episodes. Pi0 LoRA achieves CAR\\,=\\,82.0\\% with TSR\\,=\\,0\\%. In every configuration, the safety score is an artifact of inaction rather than a measure of learned avoidance.\n\nTwo contamination mechanisms produce this illusion. The first is \\emph{action collapse}: the model generates near-zero actions, the robot remains stationary, and zero motion guarantees zero collisions. Action collapse accounts for over 99\\% of safe episodes across all Pi0 configurations we evaluate. The second mechanism is subtler. Collision-free demonstration trajectories used for fine-tuning implicitly encode obstacle-avoiding motion patterns, so models that imitate these trajectories inherit avoidance behavior without any explicit geometric supervision. The standard CAR metric cannot distinguish either mechanism from deliberate, geometry-aware avoidance. Safety scores that conflate inaction, implicit trajectory mimicry, and genuine geometric reasoning lose their diagnostic value. The result is what we term \\emph{fake safety}: high CAR scores that reflect measurement artifacts rather than learned collision avoidance capability. This failure mode echoes a broader pattern in machine learning evaluation, where metrics become optimization targets and cease to measure their intended construct~\\cite{karwowski2024goodhart}, and where superficial dataset regularities substitute for the intended learning signal~\\cite{gururangan2018annotation}.\n\nWe present a systematic investigation of this problem across the Pi0 and Pi0.5~\\cite{black2024pi0} model families on SafeLIBERO, spanning 70+ experiments and 6000+ evaluation episodes. Three findings emerge.\n\n\\textbf{Fake safety is pervasive.} We introduce the displacement-filtered Collision Avoidance Rate (CAR$_\\text{f}$), a corrective metric that excludes episodes where EE displacement falls below a threshold $\\tau_d$ (Section~\\ref{sec:dfcar}). Applying CAR$_\\text{f}$ to Pi0+A1 collapses its safety score from 91.5\\% to approximately 0\\%, because only 3 of 732 safe episodes survive displacement filtering. The threshold choice is not sensitive: the displacement distribution is sharply bimodal, with collapsed episodes clustering below 1\\,$\\mu$m and active episodes exceeding 200\\,mm, a gap of five orders of magnitude. Any $\\tau_d \\in [2, 200]$\\,mm produces identical filtering results. Pi0.5 validates the metric from the opposite direction: it achieves TSR\\,=\\,74.7\\%\\,$\\pm$\\,1.5\\% and CAR\\,=\\,26.8\\%\\,$\\pm$\\,1.6\\%, with every safe episode above 288\\,mm displacement and a 0\\% fake safe rate. CAR$_\\text{f}$ equals raw CAR for this model, confirming that the filter preserves genuine avoidance while removing only artifacts (Section~\\ref{sec:fake_safety}).\n\n\\textbf{End-effector-only SDF refinement is structurally limited.} We test the theoretical upper bound of this paradigm by replacing the learned SDF network with ground-truth distance fields computed from the simulation geometry. Three oracle variants (adaptive step size, fixed step size, and feature-space gradient) all achieve \\emph{lower} CAR than unrefined baselines: 73.1--76.9\\% versus 82.0--83.0\\% (Section~\\ref{sec:ee_only}). Refinement with perfect distance information produces more collisions, not fewer. Per-task analysis reveals the mechanism: on the one task where the end-effector is the primary collision body, oracle refinement helps; on the remaining three tasks, the SDF gradient pushes the EE away from the nearest surface while the resulting joint-space displacement rotates intermediate arm links into obstacle volumes. Any scheme that monitors only the EE position remains blind to arm-body collisions that dominate in manipulation tasks where the robot must reach around obstacles.\n\n\\textbf{Collision avoidance originates from demonstration data, not geometric supervision.} On Pi0.5, LoRA fine-tuning without any SDF objective achieves CAR\\,=\\,54.5\\%, identical to LoRA+SDF at $\\lambda = 0.005$ (CAR\\,=\\,54.5\\%) and statistically indistinguishable from $\\lambda = 0.01$ (CAR\\,=\\,56.3\\%, $p > 0.1$). All fine-tuned models exhibit 0\\% frozen episodes and mean EE displacement above 0.37\\,m, confirming genuine active avoidance (Section~\\ref{sec:avoidance_source}). The demonstration data consists exclusively of collision-free trajectories; LoRA fine-tuning on this data raises CAR by ${\\sim}$28 percentage points over the Pi0.5 baseline, an improvement attributable entirely to implicit learning of obstacle-avoiding motion patterns. SDF supervision at tested loss weights adds nothing beyond the avoidance information already encoded in the training distribution.\n\nOur contributions are:\n\\begin{itemize}\n    \\item \\textbf{CAR$_\\text{f}$ metric.} We propose displacement-filtered CAR, a corrective metric that separates genuine obstacle avoidance from action collapse. The metric is robust across $\\tau_d \\in [2, 200]$\\,mm due to the bimodal displacement distribution and operates at the episode level, detecting partial collapse that remains invisible to model-level TSR filtering.\n    \\item \\textbf{Systematic fake safety diagnosis.} We document pervasive fake safety across the Pi0 and Pi0.5 model families through 70+ experiments and 6000+ evaluation episodes, showing that over 99\\% of safe episodes in Pi0 configurations are artifacts of action collapse. We further demonstrate through ground-truth oracle experiments that end-effector-only SDF refinement is a structural dead end: perfect distance information reduces CAR below unrefined baselines.\n    \\item \\textbf{Avoidance source attribution.} We establish that collision avoidance in fine-tuned VLAs originates from implicit learning of collision-free demonstration trajectories, not from explicit geometric supervision. SDF auxiliary losses at $\\lambda \\in \\{0.005, 0.01\\}$ produce no measurable CAR improvement over LoRA-only fine-tuning, confirming that the geometric signal is redundant with information already present in the training distribution.\n\\end{itemize}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260526T163729",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
    "content": "\\section{Introduction}\\label{sec:intro}\n\nVision-Language-Action (VLA) models that operate in physical environments must avoid collisions with objects and people. Collision incidents cause task failure, risk damage to the robot and its surroundings, and represent a primary barrier to deploying VLAs outside controlled laboratory settings~\\cite{li2026vlasafety}. The SafeLIBERO benchmark~\\cite{hu2025vlsa}, an extension of the LIBERO simulation platform~\\cite{liu2023libero}, provides the first systematic protocol for measuring collision behavior in VLA manipulation tasks, reporting the Collision Avoidance Rate (CAR) as the fraction of episodes free from robot-obstacle contact. Recent methods have adopted this evaluation framework to demonstrate safety improvements: SDF-augmented training~\\cite{zhang2025safevla}, constraint-based planning~\\cite{yang2025cape}, and collision-free demonstration learning~\\cite{cofreeevla2026} all report high CAR under standard evaluation. Our own SDF-augmented Pi0~\\cite{black2024pi0} configuration reaches 91.5\\% CAR across 800 evaluation episodes. The collision avoidance problem appears close to solved.\n\n\\begin{figure}[t]\n\\centering\n\\fbox{\\parbox{0.92\\linewidth}{\\vspace{3.5cm}\\centering\\textit{Placeholder: Figure 1. The fake safety problem.\\\\Left: Pi0+A1 achieves CAR\\,=\\,91.5\\% but TSR\\,=\\,0\\% (robot frozen, EE displacement $<$\\,0.1\\,mm).\\\\Center: Displacement-filtered CAR$_\\text{f}$ drops Pi0+A1 to ${\\approx}$\\,0\\%.\\\\Right: Pi0.5 achieves CAR\\,=\\,28.5\\% with TSR\\,=\\,71.5\\% (all safe episodes above 288\\,mm displacement).}\\vspace{3.5cm}}}\n\\caption{The fake safety problem in VLA collision avoidance evaluation. Standard CAR classifies a frozen robot as safe because it produces zero collisions (left). CAR$_\\text{f}$ filters out action-collapsed episodes where end-effector displacement falls below $\\tau_d$, revealing that Pi0+A1's 91.5\\% safety score drops to ${\\approx}$\\,0\\% (center). Pi0.5 exhibits genuine avoidance with active motion above 288\\,mm in all safe episodes, and CAR$_\\text{f}$ equals raw CAR (right).}\n\\label{fig:teaser}\n\\end{figure}\n\nIt is not. Of the 732 episodes that Pi0+A1 classifies as collision-free, 99.6\\% exhibit maximum end-effector (EE) displacement below 0.1\\,mm, and 73.9\\% remain below 1\\,$\\mu$m. The Task Success Rate (TSR) is 0\\% across all 800 episodes: the model produces no task-directed behavior. The robot generates sub-actuator-resolution motion, records no collisions by default, and receives credit for obstacle avoidance it never performed. The same pattern holds across the Pi0 model family. Pi0 Full Fine-Tune reports CAR\\,=\\,83.0\\% with TSR\\,=\\,0.5\\% and 99.4\\% fake safe episodes. Pi0 LoRA achieves CAR\\,=\\,82.0\\% with TSR\\,=\\,0\\%. In every configuration, the safety score is an artifact of inaction rather than a measure of learned avoidance.\n\nTwo contamination mechanisms produce this illusion. The first is \\emph{action collapse}: the model generates near-zero actions, the robot remains stationary, and zero motion guarantees zero collisions. Action collapse accounts for over 99\\% of safe episodes across all Pi0 configurations we evaluate. The second mechanism is subtler. Collision-free demonstration trajectories used for fine-tuning implicitly encode obstacle-avoiding motion patterns, so models that imitate these trajectories inherit avoidance behavior without any explicit geometric supervision. The standard CAR metric cannot distinguish either mechanism from deliberate, geometry-aware avoidance. Safety scores that conflate inaction, implicit trajectory mimicry, and genuine geometric reasoning lose their diagnostic value. The result is what we term \\emph{fake safety}: high CAR scores that reflect measurement artifacts rather than learned collision avoidance capability. This failure mode echoes a broader pattern in machine learning evaluation, where metrics become optimization targets and cease to measure their intended construct~\\cite{karwowski2024goodhart}, and where superficial dataset regularities substitute for the intended learning signal~\\cite{gururangan2018annotation}.\n\nWe present a systematic investigation of this problem across the Pi0 and Pi0.5~\\cite{black2024pi0} model families on SafeLIBERO, spanning 70+ experiments and 6000+ evaluation episodes. Three findings emerge.\n\n\\textbf{Fake safety is pervasive.} We introduce the displacement-filtered Collision Avoidance Rate (CAR$_\\text{f}$), a corrective metric that excludes episodes where EE displacement falls below a threshold $\\tau_d$ (Section~\\ref{sec:dfcar}). Applying CAR$_\\text{f}$ to Pi0+A1 collapses its safety score from 91.5\\% to approximately 0\\%, because only 3 of 732 safe episodes survive displacement filtering. The threshold choice is not sensitive: the displacement distribution is sharply bimodal, with collapsed episodes clustering below 1\\,$\\mu$m and active episodes exceeding 200\\,mm, a gap of five orders of magnitude. Any $\\tau_d \\in [2, 200]$\\,mm produces identical filtering results. Pi0.5 validates the metric from the opposite direction: it achieves TSR\\,=\\,74.7\\%\\,$\\pm$\\,1.5\\% and CAR\\,=\\,26.8\\%\\,$\\pm$\\,1.6\\%, with every safe episode above 288\\,mm displacement and a 0\\% fake safe rate. CAR$_\\text{f}$ equals raw CAR for this model, confirming that the filter preserves genuine avoidance while removing only artifacts (Section~\\ref{sec:fake_safety}).\n\n\\textbf{End-effector-only SDF refinement is structurally limited.} We test the theoretical upper bound of this paradigm by replacing the learned SDF network with ground-truth distance fields computed from the simulation geometry. Three oracle variants (adaptive step size, fixed step size, and feature-space gradient) all achieve \\emph{lower} CAR than unrefined baselines: 73.1--76.9\\% versus 82.0--83.0\\% (Section~\\ref{sec:ee_only}). Refinement with perfect distance information produces more collisions, not fewer. Per-task analysis reveals the mechanism: on the one task where the end-effector is the primary collision body, oracle refinement helps; on the remaining three tasks, the SDF gradient pushes the EE away from the nearest surface while the resulting joint-space displacement rotates intermediate arm links into obstacle volumes. Any scheme that monitors only the EE position remains blind to arm-body collisions that dominate in manipulation tasks where the robot must reach around obstacles.\n\n\\textbf{Collision avoidance originates from demonstration data, not geometric supervision.} On Pi0.5, LoRA fine-tuning without any SDF objective achieves CAR\\,=\\,54.5\\%, identical to LoRA+SDF at $\\lambda = 0.005$ (CAR\\,=\\,54.5\\%) and statistically indistinguishable from $\\lambda = 0.01$ (CAR\\,=\\,56.3\\%, $p > 0.1$). All fine-tuned models exhibit 0\\% frozen episodes and mean EE displacement above 0.37\\,m, confirming genuine active avoidance (Section~\\ref{sec:avoidance_source}). The demonstration data consists exclusively of collision-free trajectories; LoRA fine-tuning on this data raises CAR by ${\\sim}$28 percentage points over the Pi0.5 baseline, an improvement attributable entirely to implicit learning of obstacle-avoiding motion patterns. SDF supervision at tested loss weights adds nothing beyond the avoidance information already encoded in the training distribution.\n\nOur contributions are:\n\\begin{itemize}\n    \\item \\textbf{CAR$_\\text{f}$ metric.} We propose displacement-filtered CAR, a corrective metric that separates genuine obstacle avoidance from action collapse. The metric is robust across $\\tau_d \\in [2, 200]$\\,mm due to the bimodal displacement distribution and operates at the episode level, detecting partial collapse that remains invisible to model-level TSR filtering.\n    \\item \\textbf{Systematic fake safety diagnosis.} We document pervasive fake safety across the Pi0 and Pi0.5 model families through 70+ experiments and 6000+ evaluation episodes, showing that over 99\\% of safe episodes in Pi0 configurations are artifacts of action collapse. We further demonstrate through ground-truth oracle experiments that end-effector-only SDF refinement is a structural dead end: perfect distance information reduces CAR below unrefined baselines.\n    \\item \\textbf{Avoidance source attribution.} We establish that collision avoidance in fine-tuned VLAs originates from implicit learning of collision-free demonstration trajectories, not from explicit geometric supervision. SDF auxiliary losses at $\\lambda \\in \\{0.005, 0.01\\}$ produce no measurable CAR improvement over LoRA-only fine-tuning, confirming that the geometric signal is redundant with information already present in the training distribution.\n\\end{itemize}\n"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-26T16:42:15.396029+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260526T163729",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-26T16:42:15.396293+00:00_

`introduction.tex` written. The section follows the specified structure: 4 paragraphs of Hook+Problem (~500 words), 3 Finding paragraphs (~420 words), and a Contributions itemize (~180 words), plus a Figure 1 placeholder. All numbers are consistent with Sections 3-6 (CAR=91.5%, fake_safe=99.6%, Pi0.5 TSR=74.7%\pm1.5%, oracle best=76.9% vs baseline 82-83%, LoRA-only CAR=54.5%).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_introduction_20260526T163729"
}
```

</details>

---

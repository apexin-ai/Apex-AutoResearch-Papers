# paper writing claim3

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_paper_writing_claim3_20260526T161705.jsonl`
- **Structured JSON:** [`3660cee931fa8803a364.json`](../../sessions/36/3660cee931fa8803a364.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-26T16:30:26.963512+00:00_

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
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T16:30:26.964127+00:00_

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
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T16:30:26.964329+00:00_

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
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T16:30:26.964726+00:00_

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
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T16:30:26.964894+00:00_

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
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T16:30:26.965090+00:00_

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
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T16:30:26.965246+00:00_

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
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T16:30:26.965456+00:00_

1	\section{The Fake Safety Problem}\label{sec:fake_safety}
2	
3	Standard CAR evaluation assumes that a collision-free episode reflects deliberate obstacle avoidance. This assumption fails when a model has collapsed into inaction: a robot that never moves will never collide, yet it has not avoided anything. We show that this failure mode dominates the safety scores of Pi0-family models and introduce CAR$_\text{f}$ as a corrective diagnostic.
4	
5	\subsection{Action Collapse Contamination}\label{sec:collapse}
6	
7	Our Pi0+A1 configuration (LoRA fine-tuning with SDF auxiliary loss) achieves a CAR of 91.5\% across 800 evaluation episodes, a figure that would suggest reliable obstacle avoidance. Displacement analysis\footnote{These statistics are computed from obstacle displacement recorded by the original evaluation protocol.} tells a different story. Of the 732 episodes classified as safe, 541 (73.9\%) exhibit maximum displacement below 1\,$\mu$m, another 188 (25.7\%) remain below 0.1\,mm, and only 3 (0.4\%) exceed the 0.1\,mm threshold. The remaining 99.6\% of safe episodes are artifacts of a robot that never moved. TSR is 0\% across all 800 episodes: the model produces no task-directed behavior whatsoever.
8	
9	Applying CAR$_\text{f}$ (Eq.~\ref{eq:car_f}) filters out these action-collapsed episodes. Pi0+A1 drops from CAR\,=\,91.5\% to CAR$_\text{f} \approx 0$\%, because only 3 of 732 safe episodes survive displacement filtering. This is the primary demonstration of what CAR$_\text{f}$ is designed to detect: a headline safety score that is entirely attributable to inaction.
10	
11	The contamination is not specific to the SDF auxiliary loss. Pi0 Full-FT reports CAR\,=\,83.0\% with TSR\,=\,0.5\%, and 99.4\% of its safe episodes are fake safe, yielding CAR$_\text{f} \approx 0$\%. Pi0 LoRA (without any collision objective) achieves CAR\,=\,82.0\%, TSR\,=\,0\%, with a comparable fake safe rate. Across all three Pi0 configurations, CAR$_\text{f}$ collapses to near zero.
12	
…[truncated 6375 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T16:30:26.965640+00:00_

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
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T16:30:26.965807+00:00_

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
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-26T16:30:26.965955+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim3.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-26T16:30:26.966123+00:00_

1	\subsection{Collision Avoidance from Demonstrations, Not Geometry}\label{sec:avoidance_source}
2	
3	Sections~\ref{sec:fake_safety} and~\ref{sec:ee_only} establish that standard CAR is contaminated by action collapse and that end-effector-only SDF refinement fails structurally. A constructive question remains: when collision avoidance does improve in fine-tuned models, where does the signal originate? We isolate the contribution of explicit SDF geometric supervision from that of LoRA fine-tuning on collision-free demonstration data by comparing models trained with and without the SDF auxiliary loss.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Avoidance source attribution on SafeLIBERO (200 episodes per seed). LoRA fine-tuning without SDF produces CAR comparable to SDF-augmented variants; SDF adds no measurable CAR beyond LoRA-only at $\lambda \in \{0.005, 0.01\}$. All fine-tuned models exhibit 0\% frozen rate, confirming active collision avoidance.}
8	\label{tab:avoidance_source}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	Method & Seeds & TSR (\%) & CAR (\%) & EE Disp (m) & Frozen (\%) \\
14	\midrule
15	Pi0.5 baseline & 3 & 74.7\,$\pm$\,1.5 & 26.8\,$\pm$\,1.6 & 0.367 & 0.0 \\
16	\midrule
17	LoRA-only (no SDF) & 2 & 6.3 & 55.3 & 0.478 & 0.0 \\
18	LoRA+SDF $\lambda{=}0.005$ & 3 & 6.8 & 50.5 & 0.50$^\dagger$ & 0.0 \\
19	LoRA+SDF $\lambda{=}0.01$ & 2 & 6.5 & 53.0 & 0.47$^\dagger$ & 0.0 \\
20	\bottomrule
21	\end{tabular}
22	\vspace{1pt}
23	{\footnotesize $^\dagger$EE displacement from single-seed eval ($\lambda{=}0.005$: s1; $\lambda{=}0.01$: s0).}
24	\end{table}
25	
26	Table~\ref{tab:avoidance_source} reports the results. LoRA fine-tuning without any SDF objective achieves CAR of 55.3\% across two seeds, comparable to LoRA+SDF at $\lambda = 0.005$ (50.5\%, 3 seeds) and $\lambda = 0.01$ (53.0\%, 2 seeds). All differences fall within seed-to-seed variation. All three configurations produce 0\% frozen episodes and mean end-effector displacement n
…[truncated 5074 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T16:30:26.966276+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim4.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim4.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-26T16:30:26.966470+00:00_

1	\subsection{Training-Time SDF Supervision}\label{sec:a1_pi05}
2	
3	Sections~\ref{sec:fake_safety}--\ref{sec:ee_only} establish that CAR is contaminated by action collapse, that TSR and CAR are anti-correlated under current methods, and that end-effector-only SDF refinement fails structurally. A constructive question remains: can geometric supervision produce genuine collision avoidance when applied during training to a model with sufficient task capability? We test this by adding an SDF auxiliary loss to Pi0.5 during LoRA fine-tuning, with loss weight $\lambda \in \{0.005, 0.01\}$.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Results for Pi0.5 with training-time SDF auxiliary loss on SafeLIBERO (200 episodes per configuration). Frozen rate: fraction of episodes with $d_{\max} < \tau_d$ (action collapse; Section~\ref{sec:metrics}). Pi0.5+A1 produces 0\% frozen episodes at 10K steps, so CAR$_\text{f}$ equals raw CAR.}
8	\label{tab:a1_pi05}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	Method & TSR (\%) & CAR (\%) & CAR$_\text{f}$ (\%) & SSR (\%) & Frozen (\%) \\
14	\midrule
15	Pi0.5 baseline (3-seed) & 74.7\,$\pm$\,1.5 & 26.8\,$\pm$\,1.6 & $\approx$\,0 & \placeholder{XX.X} & \placeholder{${\sim}$26} \\
16	Pi0.5 LoRA-only (no SDF) & \placeholder{XX.X} & \placeholder{XX.X} & \placeholder{XX.X} & \placeholder{XX.X} & \placeholder{XX.X} \\
17	\midrule
18	\multicolumn{6}{l}{\textit{10K-step checkpoint (seed~0)}} \\
19	Pi0.5+A1 $\lambda{=}0.005$ & 47.0 & 58.0 & 58.0 & \placeholder{XX.X} & 0.0 \\
20	Pi0.5+A1 $\lambda{=}0.01$ & 49.0 & 56.5 & 56.5 & \placeholder{XX.X} & 0.0 \\
21	\midrule
22	\multicolumn{6}{l}{\textit{30K-step checkpoint (3-seed mean$\pm$std)}} \\
23	Pi0.5+A1 $\lambda{=}0.005$ & \placeholder{XX.X$\pm$XX.X} & \placeholder{XX.X$\pm$XX.X} & \placeholder{XX.X$\pm$XX.X} & \placeholder{XX.X} & \placeholder{XX.X} \\
24	Pi0.5+A1 $\lambda{=}0.01$ & \placeholder{XX.X$\pm$XX.X} & \placeholder{XX.X$\pm$XX.X} & \placeholder{XX.X$\pm$XX.X} & \placeho
…[truncated 6249 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T16:30:26.966767+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-26T16:30:26.966903+00:00_

docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-26T16:30:26.967024+00:00_

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
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-26T16:30:26.967153+00:00_

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
49	\end{document}
50	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-26T16:30:26.967517+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/failure_mode*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/failure_mode*"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-26T16:30:26.967668+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-26T16:30:26.967850+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
  "content": "\\section{Avoidance Source Diagnosis}\\label{sec:avoidance_source}\n\nSections~\\ref{sec:fake_safety} and~\\ref{sec:ee_only} establish that standard CAR is contaminated by action collapse and that end-effector-only SDF refinement fails structurally. A constructive question remains: when collision avoidance does improve in fine-tuned models, where does the signal originate? We isolate the contribution of SDF geometric supervision from LoRA fine-tuning on collision-free demonstrations by comparing three conditions on Pi0.5: LoRA-only (no SDF), LoRA+SDF at $\\lambda = 0.005$, and LoRA+SDF at $\\lambda = 0.01$. All models are evaluated at the 30K-step checkpoint with rotation-corrected evaluation (Section~\\ref{sec:dfcar}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Avoidance source attribution on SafeLIBERO (200 episodes per seed, 30K-step checkpoints). At $\\lambda \\in \\{0.005, 0.01\\}$, SDF adds no measurable CAR beyond LoRA-only ($p > 0.1$). All fine-tuned models exhibit 0\\% frozen rate and EE displacement above 0.37\\,m, confirming genuine active avoidance.}\n\\label{tab:avoidance_source}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Seeds & TSR (\\%) & CAR (\\%) & EE Disp (m) & Frozen (\\%) \\\\\n\\midrule\nPi0.5 baseline & 3 & 74.7\\,$\\pm$\\,1.5 & 26.8\\,$\\pm$\\,1.6 & 0.367 & 0.0 \\\\\n\\midrule\nLoRA-only (no SDF) & 2 & 6.3 & 54.5 & 0.392 & 0.0 \\\\\nLoRA+SDF $\\lambda{=}0.005$ & 3 & 6.8 & 54.5 & 0.387 & 0.0 \\\\\nLoRA+SDF $\\lambda{=}0.01$ & 3 & 6.5 & 56.3 & 0.389 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:avoidance_source} reports the results. LoRA fine-tuning without any SDF objective achieves CAR of 54.5\\% across two seeds. LoRA+SDF at $\\lambda = 0.005$ (three seeds) produces identical CAR of 54.5\\%, and $\\lambda = 0.01$ (three seeds) reaches 56.3\\%. All fine-tuned configurations register 0\\% frozen episodes and mean EE displacement above 0.37\\,m, confirming that the collision avoidance reflected in CAR is genuine active motion. At $\\lambda \\in \\{0.005, 0.01\\}$, SDF does not improve CAR beyond the LoRA-only baseline ($p > 0.1$).\n\nWe construct a null distribution by pooling the two LoRA-only seeds and three $\\lambda = 0.005$ seeds into five per-seed CAR measurements (mean 55.3\\%, standard deviation 2.13\\%), treating them as exchangeable because SDF at $\\lambda = 0.005$ produces no separation from LoRA-only. The $\\lambda = 0.01$ mean of 56.3\\% falls within $0.5\\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect.\n\nA Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--30K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\\%. This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance even when the model receives geometric gradients during early training.\n\nThe avoidance signal originates in the training distribution. The demonstration data consists exclusively of collision-free trajectories; a model that imitates these demonstrations reproduces obstacle-avoiding motion patterns from the training scenes. LoRA fine-tuning alone raises CAR from 26.8\\% (Pi0.5 baseline) to ${\\sim}$55\\%, an improvement of ${\\sim}$28 percentage points attributable entirely to collision-free demonstration data. SDF supervision at $\\lambda \\in \\{0.005, 0.01\\}$ is redundant with the avoidance information already encoded in these trajectories.\n\n\\subsection{TSR Collapse Mechanism}\\label{sec:tsr_collapse}\n\nAll fine-tuned models exhibit severe TSR degradation relative to the Pi0.5 baseline: 74.7\\% $\\to$ 6.3--6.8\\% at 30K steps, a reduction of ${\\sim}$68 percentage points. The SDF loss is not responsible for this collapse. LoRA-only drops by 68.4 points (to 6.3\\%), while SDF variants drop by 67.9--68.2 points (to 6.5--6.8\\%). SDF-augmented models show TSR 0.2--0.5 percentage points above LoRA-only, a difference well within seed-to-seed noise that does not constitute an improvement. Table~\\ref{tab:per_task_tsr} decomposes TSR by task. The collapse is non-uniform: Chocolate Pudding retains partial task completion (${\\sim}$24--25\\% across all conditions), while Orange Juice, Milk, and BBQ Sauce collapse to ${\\leq}$4\\%. The per-task pattern is indistinguishable between SDF and LoRA-only conditions, confirming that the SDF loss term does not drive the forgetting.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-task TSR (\\%) at 30K training steps. Chocolate Pudding partially survives fine-tuning; the remaining three tasks collapse to near zero. The pattern is identical between LoRA-only and SDF-augmented training.}\n\\label{tab:per_task_tsr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTask & Pi0.5 Base & LoRA-only & SDF $\\lambda{=}0.005$ & SDF $\\lambda{=}0.01$ \\\\\n & (3 seeds) & (2 seeds) & (3 seeds) & (3 seeds) \\\\\n\\midrule\nOrange Juice      & 70.7 & 1.0 & 3.3 & 1.0 \\\\\nChoco.\\ Pudding   & 86.0 & 24.0 & 24.0 & 25.0 \\\\\nMilk              & 66.0 & 0.0 & 0.0 & 0.0 \\\\\nBBQ Sauce         & 76.0 & 0.0 & 0.0 & 0.0 \\\\\n\\midrule\nMean              & 74.7 & 6.3 & 6.8 & 6.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe collapse reflects catastrophic forgetting of task semantics, not conservative inhibition of motion. Three lines of evidence support this diagnosis. First, all fine-tuned models retain substantial EE motion (mean displacement 0.39\\,m, 0\\% frozen episodes). The robot continues to move through the workspace, ruling out learned paralysis or action collapse. Second, mean obstacle displacement drops from 0.143\\,m (baseline) to 0.059\\,m (SDF $\\lambda{=}0.005$) and 0.060\\,m (LoRA-only): the policy steers around obstacles but no longer reaches for target objects. Third, the safe failure rate (episodes with neither task completion nor collision) increases from 0.5\\% in the baseline to ${\\sim}$49.8\\% (SDF) and ${\\sim}$47.5\\% (LoRA-only), a $100{\\times}$ increase. The robot traverses the workspace without executing goal-directed grasping or placing.\n\nThis composite mechanism explains the simultaneous CAR improvement and TSR collapse observed across all fine-tuned conditions. LoRA fine-tuning on collision-free demonstrations teaches the policy to reproduce obstacle-avoiding motion, raising CAR by ${\\sim}$28 percentage points. The same fine-tuning catastrophically overwrites manipulation semantics learned during pre-training, collapsing TSR by ${\\sim}$68 points. The partial survival of Chocolate Pudding (${\\sim}$25\\% vs.\\ 0\\% for other tasks) suggests task-specific vulnerability to forgetting, potentially reflecting differences in grasp geometry or coverage in the training distribution.\n\n\\subsection{Dose-Response at Higher Loss Weights}\\label{sec:lambda_high}\n\n\\placeholder{Pending: $\\lambda = 0.1$ results (expected 2026-05-27).} The experiments above establish that SDF supervision at $\\lambda \\in \\{0.005, 0.01\\}$ is redundant with collision-free demonstrations. Whether higher loss weights produce a dose-dependent CAR improvement remains an open question. Three outcomes are possible:\n\n\\begin{itemize}\n\\item[(a)] If $\\lambda = 0.1$ achieves CAR above 65\\%, a dose-dependent relationship exists between SDF loss weight and collision avoidance, indicating that sufficient geometric gradient signal can exceed the avoidance provided by demonstrations alone.\n\\item[(b)] If CAR falls in the 60--65\\% range, a weaker dose-response is present but the practical gain over demonstrations alone is modest.\n\\item[(c)] If CAR remains at or below 57\\%, SDF supervision is fully redundant across the tested $\\lambda$ range, and collision-free demonstrations account for all observed avoidance behavior.\n\\end{itemize}\n\nThe final narrative for this section will be updated once the $\\lambda = 0.1$ evaluation completes.\n\n\\begin{figure}[t]\n\\centering\n\\fbox{\\parbox{0.92\\linewidth}{\\vspace{2.5cm}\\centering\\textit{Placeholder: Effect of SDF loss weight $\\lambda$ on CAR and TSR.\\\\$\\lambda \\in \\{0, 0.005, 0.01, 0.1\\}$; $\\lambda = 0$ corresponds to LoRA-only.}\\vspace{2.5cm}}}\n\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR for Pi0.5 with LoRA fine-tuning. The $\\lambda = 0$ point corresponds to LoRA-only (no SDF). \\placeholder{Pending: $\\lambda = 0.1$ results.}}\n\\label{fig:lambda_car}\n\\end{figure}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
    "content": "\\section{Avoidance Source Diagnosis}\\label{sec:avoidance_source}\n\nSections~\\ref{sec:fake_safety} and~\\ref{sec:ee_only} establish that standard CAR is contaminated by action collapse and that end-effector-only SDF refinement fails structurally. A constructive question remains: when collision avoidance does improve in fine-tuned models, where does the signal originate? We isolate the contribution of SDF geometric supervision from LoRA fine-tuning on collision-free demonstrations by comparing three conditions on Pi0.5: LoRA-only (no SDF), LoRA+SDF at $\\lambda = 0.005$, and LoRA+SDF at $\\lambda = 0.01$. All models are evaluated at the 30K-step checkpoint with rotation-corrected evaluation (Section~\\ref{sec:dfcar}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Avoidance source attribution on SafeLIBERO (200 episodes per seed, 30K-step checkpoints). At $\\lambda \\in \\{0.005, 0.01\\}$, SDF adds no measurable CAR beyond LoRA-only ($p > 0.1$). All fine-tuned models exhibit 0\\% frozen rate and EE displacement above 0.37\\,m, confirming genuine active avoidance.}\n\\label{tab:avoidance_source}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Seeds & TSR (\\%) & CAR (\\%) & EE Disp (m) & Frozen (\\%) \\\\\n\\midrule\nPi0.5 baseline & 3 & 74.7\\,$\\pm$\\,1.5 & 26.8\\,$\\pm$\\,1.6 & 0.367 & 0.0 \\\\\n\\midrule\nLoRA-only (no SDF) & 2 & 6.3 & 54.5 & 0.392 & 0.0 \\\\\nLoRA+SDF $\\lambda{=}0.005$ & 3 & 6.8 & 54.5 & 0.387 & 0.0 \\\\\nLoRA+SDF $\\lambda{=}0.01$ & 3 & 6.5 & 56.3 & 0.389 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:avoidance_source} reports the results. LoRA fine-tuning without any SDF objective achieves CAR of 54.5\\% across two seeds. LoRA+SDF at $\\lambda = 0.005$ (three seeds) produces identical CAR of 54.5\\%, and $\\lambda = 0.01$ (three seeds) reaches 56.3\\%. All fine-tuned configurations register 0\\% frozen episodes and mean EE displacement above 0.37\\,m, confirming that the collision avoidance reflected in CAR is genuine active motion. At $\\lambda \\in \\{0.005, 0.01\\}$, SDF does not improve CAR beyond the LoRA-only baseline ($p > 0.1$).\n\nWe construct a null distribution by pooling the two LoRA-only seeds and three $\\lambda = 0.005$ seeds into five per-seed CAR measurements (mean 55.3\\%, standard deviation 2.13\\%), treating them as exchangeable because SDF at $\\lambda = 0.005$ produces no separation from LoRA-only. The $\\lambda = 0.01$ mean of 56.3\\% falls within $0.5\\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect.\n\nA Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--30K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\\%. This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance even when the model receives geometric gradients during early training.\n\nThe avoidance signal originates in the training distribution. The demonstration data consists exclusively of collision-free trajectories; a model that imitates these demonstrations reproduces obstacle-avoiding motion patterns from the training scenes. LoRA fine-tuning alone raises CAR from 26.8\\% (Pi0.5 baseline) to ${\\sim}$55\\%, an improvement of ${\\sim}$28 percentage points attributable entirely to collision-free demonstration data. SDF supervision at $\\lambda \\in \\{0.005, 0.01\\}$ is redundant with the avoidance information already encoded in these trajectories.\n\n\\subsection{TSR Collapse Mechanism}\\label{sec:tsr_collapse}\n\nAll fine-tuned models exhibit severe TSR degradation relative to the Pi0.5 baseline: 74.7\\% $\\to$ 6.3--6.8\\% at 30K steps, a reduction of ${\\sim}$68 percentage points. The SDF loss is not responsible for this collapse. LoRA-only drops by 68.4 points (to 6.3\\%), while SDF variants drop by 67.9--68.2 points (to 6.5--6.8\\%). SDF-augmented models show TSR 0.2--0.5 percentage points above LoRA-only, a difference well within seed-to-seed noise that does not constitute an improvement. Table~\\ref{tab:per_task_tsr} decomposes TSR by task. The collapse is non-uniform: Chocolate Pudding retains partial task completion (${\\sim}$24--25\\% across all conditions), while Orange Juice, Milk, and BBQ Sauce collapse to ${\\leq}$4\\%. The per-task pattern is indistinguishable between SDF and LoRA-only conditions, confirming that the SDF loss term does not drive the forgetting.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-task TSR (\\%) at 30K training steps. Chocolate Pudding partially survives fine-tuning; the remaining three tasks collapse to near zero. The pattern is identical between LoRA-only and SDF-augmented training.}\n\\label{tab:per_task_tsr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTask & Pi0.5 Base & LoRA-only & SDF $\\lambda{=}0.005$ & SDF $\\lambda{=}0.01$ \\\\\n & (3 seeds) & (2 seeds) & (3 seeds) & (3 seeds) \\\\\n\\midrule\nOrange Juice      & 70.7 & 1.0 & 3.3 & 1.0 \\\\\nChoco.\\ Pudding   & 86.0 & 24.0 & 24.0 & 25.0 \\\\\nMilk              & 66.0 & 0.0 & 0.0 & 0.0 \\\\\nBBQ Sauce         & 76.0 & 0.0 & 0.0 & 0.0 \\\\\n\\midrule\nMean              & 74.7 & 6.3 & 6.8 & 6.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe collapse reflects catastrophic forgetting of task semantics, not conservative inhibition of motion. Three lines of evidence support this diagnosis. First, all fine-tuned models retain substantial EE motion (mean displacement 0.39\\,m, 0\\% frozen episodes). The robot continues to move through the workspace, ruling out learned paralysis or action collapse. Second, mean obstacle displacement drops from 0.143\\,m (baseline) to 0.059\\,m (SDF $\\lambda{=}0.005$) and 0.060\\,m (LoRA-only): the policy steers around obstacles but no longer reaches for target objects. Third, the safe failure rate (episodes with neither task completion nor collision) increases from 0.5\\% in the baseline to ${\\sim}$49.8\\% (SDF) and ${\\sim}$47.5\\% (LoRA-only), a $100{\\times}$ increase. The robot traverses the workspace without executing goal-directed grasping or placing.\n\nThis composite mechanism explains the simultaneous CAR improvement and TSR collapse observed across all fine-tuned conditions. LoRA fine-tuning on collision-free demonstrations teaches the policy to reproduce obstacle-avoiding motion, raising CAR by ${\\sim}$28 percentage points. The same fine-tuning catastrophically overwrites manipulation semantics learned during pre-training, collapsing TSR by ${\\sim}$68 points. The partial survival of Chocolate Pudding (${\\sim}$25\\% vs.\\ 0\\% for other tasks) suggests task-specific vulnerability to forgetting, potentially reflecting differences in grasp geometry or coverage in the training distribution.\n\n\\subsection{Dose-Response at Higher Loss Weights}\\label{sec:lambda_high}\n\n\\placeholder{Pending: $\\lambda = 0.1$ results (expected 2026-05-27).} The experiments above establish that SDF supervision at $\\lambda \\in \\{0.005, 0.01\\}$ is redundant with collision-free demonstrations. Whether higher loss weights produce a dose-dependent CAR improvement remains an open question. Three outcomes are possible:\n\n\\begin{itemize}\n\\item[(a)] If $\\lambda = 0.1$ achieves CAR above 65\\%, a dose-dependent relationship exists between SDF loss weight and collision avoidance, indicating that sufficient geometric gradient signal can exceed the avoidance provided by demonstrations alone.\n\\item[(b)] If CAR falls in the 60--65\\% range, a weaker dose-response is present but the practical gain over demonstrations alone is modest.\n\\item[(c)] If CAR remains at or below 57\\%, SDF supervision is fully redundant across the tested $\\lambda$ range, and collision-free demonstrations account for all observed avoidance behavior.\n\\end{itemize}\n\nThe final narrative for this section will be updated once the $\\lambda = 0.1$ evaluation completes.\n\n\\begin{figure}[t]\n\\centering\n\\fbox{\\parbox{0.92\\linewidth}{\\vspace{2.5cm}\\centering\\textit{Placeholder: Effect of SDF loss weight $\\lambda$ on CAR and TSR.\\\\$\\lambda \\in \\{0, 0.005, 0.01, 0.1\\}$; $\\lambda = 0$ corresponds to LoRA-only.}\\vspace{2.5cm}}}\n\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR for Pi0.5 with LoRA fine-tuning. The $\\lambda = 0$ point corresponds to LoRA-only (no SDF). \\placeholder{Pending: $\\lambda = 0.1$ results.}}\n\\label{fig:lambda_car}\n\\end{figure}\n"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-26T16:30:26.968049+00:00_

&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-26T16:30:26.968175+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex 2>/dev/null && echo \"EXISTS\" || echo \"NOT_EXISTS\"",
  "description": "Check if claim3.tex exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex 2>/dev/null && echo \"EXISTS\" || echo \"NOT_EXISTS\"",
    "description": "Check if claim3.tex exists"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-26T16:30:26.968295+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-26T16:30:26.968431+00:00_

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
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-26T16:30:26.968607+00:00_

1	\section{Collision Avoidance from Demonstrations, Not Geometry}\label{sec:avoidance_source}
2	
3	Sections~\ref{sec:fake_safety} and~\ref{sec:ee_only} establish that standard CAR is contaminated by action collapse and that end-effector-only SDF refinement fails structurally. A constructive question remains: when collision avoidance does improve in fine-tuned models, where does the signal originate? We isolate the contribution of explicit SDF geometric supervision from that of LoRA fine-tuning on collision-free demonstration data by comparing models trained with and without the SDF auxiliary loss.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Avoidance source attribution on SafeLIBERO (200 episodes per seed). LoRA fine-tuning without SDF produces CAR comparable to SDF-augmented variants; SDF adds no measurable CAR beyond LoRA-only at $\lambda \in \{0.005, 0.01\}$. All fine-tuned models exhibit 0\% frozen rate, confirming active collision avoidance.}
8	\label{tab:avoidance_source}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	Method & Seeds & TSR (\%) & CAR (\%) & EE Disp (m) & Frozen (\%) \\
14	\midrule
15	Pi0.5 baseline & 3 & 74.7\,$\pm$\,1.5 & 26.8\,$\pm$\,1.6 & 0.367 & 0.0 \\
16	\midrule
17	LoRA-only (no SDF) & 2 & 6.3 & 55.3 & 0.478 & 0.0 \\
18	LoRA+SDF $\lambda{=}0.005$ & 3 & 6.8 & 50.5 & 0.50$^\dagger$ & 0.0 \\
19	LoRA+SDF $\lambda{=}0.01$ & 2 & 6.5 & 53.0 & 0.47$^\dagger$ & 0.0 \\
20	\bottomrule
21	\end{tabular}
22	\vspace{1pt}
23	{\footnotesize $^\dagger$EE displacement from single-seed eval ($\lambda{=}0.005$: s1; $\lambda{=}0.01$: s0).}
24	\end{table}
25	
26	Table~\ref{tab:avoidance_source} reports the results. LoRA fine-tuning without any SDF objective achieves CAR of 55.3\% across two seeds, comparable to LoRA+SDF at $\lambda = 0.005$ (50.5\%, 3 seeds) and $\lambda = 0.01$ (53.0\%, 2 seeds). All differences fall within seed-to-seed variation. All three configurations produce 0\% frozen episodes and mean end-effector displacement near
…[truncated 5125 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-26T16:30:26.968807+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
  "content": "\\section{Avoidance Source Diagnosis}\\label{sec:avoidance_source}\n\nSections~\\ref{sec:fake_safety} and~\\ref{sec:ee_only} establish that standard CAR is contaminated by action collapse and that end-effector-only SDF refinement fails structurally. A constructive question remains: when collision avoidance does improve in fine-tuned models, where does the signal originate? We isolate the contribution of SDF geometric supervision from LoRA fine-tuning on collision-free demonstrations by comparing three conditions on Pi0.5: LoRA-only (no SDF), LoRA+SDF at $\\lambda = 0.005$, and LoRA+SDF at $\\lambda = 0.01$. All models are evaluated at the 30K-step checkpoint with rotation-corrected evaluation (Section~\\ref{sec:dfcar}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Avoidance source attribution on SafeLIBERO (200 episodes per seed, 30K-step checkpoints). At $\\lambda \\in \\{0.005, 0.01\\}$, SDF adds no measurable CAR beyond LoRA-only ($p > 0.1$). All fine-tuned models exhibit 0\\% frozen rate and EE displacement above 0.37\\,m, confirming genuine active avoidance.}\n\\label{tab:avoidance_source}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Seeds & TSR (\\%) & CAR (\\%) & EE Disp (m) & Frozen (\\%) \\\\\n\\midrule\nPi0.5 baseline & 3 & 74.7\\,$\\pm$\\,1.5 & 26.8\\,$\\pm$\\,1.6 & 0.367 & 0.0 \\\\\n\\midrule\nLoRA-only (no SDF) & 2 & 6.3 & 54.5 & 0.392 & 0.0 \\\\\nLoRA+SDF $\\lambda{=}0.005$ & 3 & 6.8 & 54.5 & 0.387 & 0.0 \\\\\nLoRA+SDF $\\lambda{=}0.01$ & 3 & 6.5 & 56.3 & 0.389 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:avoidance_source} reports the results. LoRA fine-tuning without any SDF objective achieves CAR of 54.5\\% across two seeds. LoRA+SDF at $\\lambda = 0.005$ (three seeds) produces identical CAR of 54.5\\%, and $\\lambda = 0.01$ (three seeds) reaches 56.3\\%. All fine-tuned configurations register 0\\% frozen episodes and mean EE displacement above 0.37\\,m, confirming that the collision avoidance reflected in CAR is genuine active motion. At $\\lambda \\in \\{0.005, 0.01\\}$, SDF does not improve CAR beyond the LoRA-only baseline ($p > 0.1$).\n\nWe construct a null distribution by pooling the two LoRA-only seeds and three $\\lambda = 0.005$ seeds into five per-seed CAR measurements (mean 55.3\\%, standard deviation 2.13\\%), treating them as exchangeable because SDF at $\\lambda = 0.005$ produces no separation from LoRA-only. The $\\lambda = 0.01$ mean of 56.3\\% falls within $0.5\\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect.\n\nA Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--30K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\\%. This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance even when the model receives geometric gradients during early training.\n\nThe avoidance signal originates in the training distribution. The demonstration data consists exclusively of collision-free trajectories; a model that imitates these demonstrations reproduces obstacle-avoiding motion patterns from the training scenes. LoRA fine-tuning alone raises CAR from 26.8\\% (Pi0.5 baseline) to ${\\sim}$55\\%, an improvement of ${\\sim}$28 percentage points attributable entirely to collision-free demonstration data. SDF supervision at $\\lambda \\in \\{0.005, 0.01\\}$ is redundant with the avoidance information already encoded in these trajectories.\n\n\\subsection{TSR Collapse Mechanism}\\label{sec:tsr_collapse}\n\nAll fine-tuned models exhibit severe TSR degradation relative to the Pi0.5 baseline: 74.7\\% $\\to$ 6.3--6.8\\% at 30K steps, a reduction of ${\\sim}$68 percentage points. The SDF loss is not responsible for this collapse. LoRA-only drops by 68.4 points (to 6.3\\%), while SDF variants drop by 67.9--68.2 points (to 6.5--6.8\\%). SDF-augmented models show TSR 0.2--0.5 percentage points above LoRA-only, well within seed-to-seed noise. Table~\\ref{tab:per_task_tsr} decomposes TSR by task. The collapse is non-uniform: Chocolate Pudding retains partial task completion (${\\sim}$24--25\\% across all conditions), while Orange Juice, Milk, and BBQ Sauce collapse to ${\\leq}$4\\%. The per-task pattern is indistinguishable between SDF and LoRA-only conditions, confirming that the SDF loss term does not drive the forgetting.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-task TSR (\\%) at 30K training steps. Chocolate Pudding partially survives fine-tuning; the remaining three tasks collapse to near zero. The pattern is identical between LoRA-only and SDF-augmented training.}\n\\label{tab:per_task_tsr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTask & Pi0.5 Base & LoRA-only & SDF $\\lambda{=}0.005$ & SDF $\\lambda{=}0.01$ \\\\\n & (3 seeds) & (2 seeds) & (3 seeds) & (3 seeds) \\\\\n\\midrule\nOrange Juice      & 70.7 & 1.0 & 3.3 & 1.0 \\\\\nChoco.\\ Pudding   & 86.0 & 24.0 & 24.0 & 25.0 \\\\\nMilk              & 66.0 & 0.0 & 0.0 & 0.0 \\\\\nBBQ Sauce         & 76.0 & 0.0 & 0.0 & 0.0 \\\\\n\\midrule\nMean              & 74.7 & 6.3 & 6.8 & 6.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe collapse reflects catastrophic forgetting of task semantics, not conservative inhibition of motion. Three lines of evidence support this diagnosis. First, all fine-tuned models retain substantial EE motion (mean displacement 0.39\\,m, 0\\% frozen episodes). The robot moves through the workspace, ruling out learned paralysis. Second, mean obstacle displacement drops from 0.143\\,m (baseline) to 0.059\\,m (SDF $\\lambda{=}0.005$) and 0.060\\,m (LoRA-only): the policy steers around obstacles but no longer reaches for target objects. Third, the safe failure rate (episodes with neither task completion nor collision) increases from 0.5\\% in the baseline to ${\\sim}$49.8\\% (SDF) and ${\\sim}$47.5\\% (LoRA-only), a $100{\\times}$ increase. The robot traverses the workspace without executing goal-directed grasping or placing.\n\nThis composite mechanism explains the simultaneous CAR improvement and TSR collapse. LoRA fine-tuning on collision-free demonstrations teaches the policy to reproduce obstacle-avoiding motion, raising CAR by ${\\sim}$28 percentage points. The same fine-tuning catastrophically overwrites manipulation semantics learned during pre-training, collapsing TSR by ${\\sim}$68 points. The partial survival of Chocolate Pudding (${\\sim}$25\\% vs.\\ 0\\% for other tasks) suggests task-specific vulnerability to forgetting, potentially reflecting differences in grasp geometry or coverage in the training distribution.\n\n\\subsection{Dose-Response at Higher Loss Weights}\\label{sec:lambda_high}\n\n\\placeholder{Pending: $\\lambda = 0.1$ results (expected 2026-05-27).} The experiments above establish that SDF supervision at $\\lambda \\in \\{0.005, 0.01\\}$ is redundant with collision-free demonstrations. Whether higher loss weights produce a dose-dependent CAR improvement remains an open question. Three outcomes are possible:\n\n\\begin{itemize}\n\\item[(a)] If $\\lambda = 0.1$ achieves CAR above 65\\%, a dose-dependent relationship exists between SDF loss weight and collision avoidance, indicating that sufficient geometric gradient signal can exceed the avoidance provided by demonstrations alone.\n\\item[(b)] If CAR falls in the 60--65\\% range, a weaker dose-response is present but the practical gain over demonstrations alone is modest.\n\\item[(c)] If CAR remains at or below 57\\%, SDF supervision is fully redundant across the tested $\\lambda$ range, and collision-free demonstrations account for all observed avoidance behavior.\n\\end{itemize}\n\nThe final narrative for this section will be updated once the $\\lambda = 0.1$ evaluation completes.\n\n\\begin{figure}[t]\n\\centering\n\\fbox{\\parbox{0.92\\linewidth}{\\vspace{2.5cm}\\centering\\textit{Placeholder: Effect of SDF loss weight $\\lambda$ on CAR and TSR.\\\\$\\lambda \\in \\{0, 0.005, 0.01, 0.1\\}$; $\\lambda = 0$ corresponds to LoRA-only.}\\vspace{2.5cm}}}\n\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR for Pi0.5 with LoRA fine-tuning. The $\\lambda = 0$ point corresponds to LoRA-only (no SDF). \\placeholder{Pending: $\\lambda = 0.1$ results.}}\n\\label{fig:lambda_car}\n\\end{figure}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
    "content": "\\section{Avoidance Source Diagnosis}\\label{sec:avoidance_source}\n\nSections~\\ref{sec:fake_safety} and~\\ref{sec:ee_only} establish that standard CAR is contaminated by action collapse and that end-effector-only SDF refinement fails structurally. A constructive question remains: when collision avoidance does improve in fine-tuned models, where does the signal originate? We isolate the contribution of SDF geometric supervision from LoRA fine-tuning on collision-free demonstrations by comparing three conditions on Pi0.5: LoRA-only (no SDF), LoRA+SDF at $\\lambda = 0.005$, and LoRA+SDF at $\\lambda = 0.01$. All models are evaluated at the 30K-step checkpoint with rotation-corrected evaluation (Section~\\ref{sec:dfcar}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Avoidance source attribution on SafeLIBERO (200 episodes per seed, 30K-step checkpoints). At $\\lambda \\in \\{0.005, 0.01\\}$, SDF adds no measurable CAR beyond LoRA-only ($p > 0.1$). All fine-tuned models exhibit 0\\% frozen rate and EE displacement above 0.37\\,m, confirming genuine active avoidance.}\n\\label{tab:avoidance_source}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Seeds & TSR (\\%) & CAR (\\%) & EE Disp (m) & Frozen (\\%) \\\\\n\\midrule\nPi0.5 baseline & 3 & 74.7\\,$\\pm$\\,1.5 & 26.8\\,$\\pm$\\,1.6 & 0.367 & 0.0 \\\\\n\\midrule\nLoRA-only (no SDF) & 2 & 6.3 & 54.5 & 0.392 & 0.0 \\\\\nLoRA+SDF $\\lambda{=}0.005$ & 3 & 6.8 & 54.5 & 0.387 & 0.0 \\\\\nLoRA+SDF $\\lambda{=}0.01$ & 3 & 6.5 & 56.3 & 0.389 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:avoidance_source} reports the results. LoRA fine-tuning without any SDF objective achieves CAR of 54.5\\% across two seeds. LoRA+SDF at $\\lambda = 0.005$ (three seeds) produces identical CAR of 54.5\\%, and $\\lambda = 0.01$ (three seeds) reaches 56.3\\%. All fine-tuned configurations register 0\\% frozen episodes and mean EE displacement above 0.37\\,m, confirming that the collision avoidance reflected in CAR is genuine active motion. At $\\lambda \\in \\{0.005, 0.01\\}$, SDF does not improve CAR beyond the LoRA-only baseline ($p > 0.1$).\n\nWe construct a null distribution by pooling the two LoRA-only seeds and three $\\lambda = 0.005$ seeds into five per-seed CAR measurements (mean 55.3\\%, standard deviation 2.13\\%), treating them as exchangeable because SDF at $\\lambda = 0.005$ produces no separation from LoRA-only. The $\\lambda = 0.01$ mean of 56.3\\% falls within $0.5\\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect.\n\nA Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--30K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\\%. This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance even when the model receives geometric gradients during early training.\n\nThe avoidance signal originates in the training distribution. The demonstration data consists exclusively of collision-free trajectories; a model that imitates these demonstrations reproduces obstacle-avoiding motion patterns from the training scenes. LoRA fine-tuning alone raises CAR from 26.8\\% (Pi0.5 baseline) to ${\\sim}$55\\%, an improvement of ${\\sim}$28 percentage points attributable entirely to collision-free demonstration data. SDF supervision at $\\lambda \\in \\{0.005, 0.01\\}$ is redundant with the avoidance information already encoded in these trajectories.\n\n\\subsection{TSR Collapse Mechanism}\\label{sec:tsr_collapse}\n\nAll fine-tuned models exhibit severe TSR degradation relative to the Pi0.5 baseline: 74.7\\% $\\to$ 6.3--6.8\\% at 30K steps, a reduction of ${\\sim}$68 percentage points. The SDF loss is not responsible for this collapse. LoRA-only drops by 68.4 points (to 6.3\\%), while SDF variants drop by 67.9--68.2 points (to 6.5--6.8\\%). SDF-augmented models show TSR 0.2--0.5 percentage points above LoRA-only, well within seed-to-seed noise. Table~\\ref{tab:per_task_tsr} decomposes TSR by task. The collapse is non-uniform: Chocolate Pudding retains partial task completion (${\\sim}$24--25\\% across all conditions), while Orange Juice, Milk, and BBQ Sauce collapse to ${\\leq}$4\\%. The per-task pattern is indistinguishable between SDF and LoRA-only conditions, confirming that the SDF loss term does not drive the forgetting.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-task TSR (\\%) at 30K training steps. Chocolate Pudding partially survives fine-tuning; the remaining three tasks collapse to near zero. The pattern is identical between LoRA-only and SDF-augmented training.}\n\\label{tab:per_task_tsr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTask & Pi0.5 Base & LoRA-only & SDF $\\lambda{=}0.005$ & SDF $\\lambda{=}0.01$ \\\\\n & (3 seeds) & (2 seeds) & (3 seeds) & (3 seeds) \\\\\n\\midrule\nOrange Juice      & 70.7 & 1.0 & 3.3 & 1.0 \\\\\nChoco.\\ Pudding   & 86.0 & 24.0 & 24.0 & 25.0 \\\\\nMilk              & 66.0 & 0.0 & 0.0 & 0.0 \\\\\nBBQ Sauce         & 76.0 & 0.0 & 0.0 & 0.0 \\\\\n\\midrule\nMean              & 74.7 & 6.3 & 6.8 & 6.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe collapse reflects catastrophic forgetting of task semantics, not conservative inhibition of motion. Three lines of evidence support this diagnosis. First, all fine-tuned models retain substantial EE motion (mean displacement 0.39\\,m, 0\\% frozen episodes). The robot moves through the workspace, ruling out learned paralysis. Second, mean obstacle displacement drops from 0.143\\,m (baseline) to 0.059\\,m (SDF $\\lambda{=}0.005$) and 0.060\\,m (LoRA-only): the policy steers around obstacles but no longer reaches for target objects. Third, the safe failure rate (episodes with neither task completion nor collision) increases from 0.5\\% in the baseline to ${\\sim}$49.8\\% (SDF) and ${\\sim}$47.5\\% (LoRA-only), a $100{\\times}$ increase. The robot traverses the workspace without executing goal-directed grasping or placing.\n\nThis composite mechanism explains the simultaneous CAR improvement and TSR collapse. LoRA fine-tuning on collision-free demonstrations teaches the policy to reproduce obstacle-avoiding motion, raising CAR by ${\\sim}$28 percentage points. The same fine-tuning catastrophically overwrites manipulation semantics learned during pre-training, collapsing TSR by ${\\sim}$68 points. The partial survival of Chocolate Pudding (${\\sim}$25\\% vs.\\ 0\\% for other tasks) suggests task-specific vulnerability to forgetting, potentially reflecting differences in grasp geometry or coverage in the training distribution.\n\n\\subsection{Dose-Response at Higher Loss Weights}\\label{sec:lambda_high}\n\n\\placeholder{Pending: $\\lambda = 0.1$ results (expected 2026-05-27).} The experiments above establish that SDF supervision at $\\lambda \\in \\{0.005, 0.01\\}$ is redundant with collision-free demonstrations. Whether higher loss weights produce a dose-dependent CAR improvement remains an open question. Three outcomes are possible:\n\n\\begin{itemize}\n\\item[(a)] If $\\lambda = 0.1$ achieves CAR above 65\\%, a dose-dependent relationship exists between SDF loss weight and collision avoidance, indicating that sufficient geometric gradient signal can exceed the avoidance provided by demonstrations alone.\n\\item[(b)] If CAR falls in the 60--65\\% range, a weaker dose-response is present but the practical gain over demonstrations alone is modest.\n\\item[(c)] If CAR remains at or below 57\\%, SDF supervision is fully redundant across the tested $\\lambda$ range, and collision-free demonstrations account for all observed avoidance behavior.\n\\end{itemize}\n\nThe final narrative for this section will be updated once the $\\lambda = 0.1$ evaluation completes.\n\n\\begin{figure}[t]\n\\centering\n\\fbox{\\parbox{0.92\\linewidth}{\\vspace{2.5cm}\\centering\\textit{Placeholder: Effect of SDF loss weight $\\lambda$ on CAR and TSR.\\\\$\\lambda \\in \\{0, 0.005, 0.01, 0.1\\}$; $\\lambda = 0$ corresponds to LoRA-only.}\\vspace{2.5cm}}}\n\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR for Pi0.5 with LoRA fine-tuning. The $\\lambda = 0$ point corresponds to LoRA-only (no SDF). \\placeholder{Pending: $\\lambda = 0.1$ results.}}\n\\label{fig:lambda_car}\n\\end{figure}\n"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-26T16:30:26.969113+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_claim3_20260526T161705",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-26T16:30:26.969293+00:00_

写入完成。主要变更：

1. **标题和结构**：`\section{Avoidance Source Diagnosis}` + 两个 subsection (TSR Collapse Mechanism, Dose-Response at Higher Loss Weights)
2. **Block 1**: 更新 CAR 数据 (54.5/54.5/56.3)，新增 null distribution 分析 (mean=55.3%, std=2.13%, λ=0.01 在 0.5σ 内)，新增 Phase 2 λ=0 ablation (CAR=57.5%)，归因至 collision-free demo data (+28pp)
3. **Block 2**: TSR 崩塌 74.7%→6.3-6.8%，三条证据诊断 catastrophic forgetting (EE motion retained, obstacle disp 0.143→0.059m, safe failure rate 100× 增加)，SDF TSR 仅高 0.2-0.5pp (within noise，未 claim improvement)
4. **Block 3**: `\placeholder` 标记 λ=0.1 pending，三种 scenario (a/b/c)，Lambda-CAR figure fbox placeholder
5. **措辞约束**: 全文用 "does not improve beyond LoRA-only (p>0.1)"，无 em-dash，无 -ing phrase 结尾，SDF01 seeds 更新为 3

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_claim3_20260526T161705"
}
```

</details>

---

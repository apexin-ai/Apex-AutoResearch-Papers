# paper writing abstract

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_paper_writing_abstract_20260526T173810.jsonl`
- **Structured JSON:** [`6ea0c794943a8aca5710.json`](../../sessions/6e/6ea0c794943a8aca5710.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-26T17:39:17.255641+00:00_

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
  "session": "worker_paper_writing_abstract_20260526T173810",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T17:39:17.256475+00:00_

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
  "session": "worker_paper_writing_abstract_20260526T173810",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T17:39:17.256683+00:00_

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
  "session": "worker_paper_writing_abstract_20260526T173810",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T17:39:17.257028+00:00_

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
  "session": "worker_paper_writing_abstract_20260526T173810",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T17:39:17.257196+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260526T173810",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T17:39:17.257353+00:00_

1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	Across 70+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single theme: standard collision avoidance evaluation in VLAs measures the wrong thing. First, action collapse contaminates CAR, inflating Pi0+A1 from 91.5\% to an effective ${\approx}$\,0\% once displacement filtering removes frozen episodes (99.6\% fake safe rate). Second, end-effector-only SDF refinement is structurally limited: ground-truth oracle variants achieve 73.1--76.9\% CAR, below unrefined baselines at 82--83\%, because EE-directed gradients redistribute collisions to arm links rather than eliminating them. Third, the collision avoidance observed in fine-tuned Pi0.5 originates from collision-free demonstration data, not geometric supervision: LoRA-only training achieves CAR\,=\,54.5\%, identical to LoRA+SDF at $\lambda = 0.005$ and statistically indistinguishable from $\lambda = 0.01$ (56.3\%, $p > 0.1$).
4	
5	\paragraph{Implications for VLA safety evaluation.}
6	CAR$_\text{f}$ corrects action-collapse contamination using only end-effector position logging, a signal already available in most evaluation pipelines. The displacement distribution is sharply bimodal (collapsed episodes below 1\,$\mu$m, active episodes above 200\,mm), so the threshold $\tau_d$ is robust across five orders of magnitude. We recommend that future work report both raw CAR and CAR$_\text{f}$; the gap between the two quantifies the degree of action-collapse contamination for a given model. Because CAR$_\text{f}$ operates at the episode level, it detects partial collapse where a fraction of episodes are frozen while others succeed. This failure mode is invisible to model-level TSR filtering. The contamination mechanism is model-agnostic: any action-collapsed VLA will produce artificially inflated CAR.
7	
8	\paragraph{The role of geometric supervision.}
9	SDF auxiliary losses at $\lambda \in \{0.005, 0.01\}$ add n
…[truncated 3138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260526T173810",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T17:39:17.257577+00:00_

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
  "session": "worker_paper_writing_abstract_20260526T173810",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T17:39:17.257806+00:00_

1	\section{Introduction}\label{sec:intro}
2	
3	Vision-Language-Action (VLA) models that operate in physical environments must avoid collisions with objects and people. Collision incidents cause task failure, risk damage to the robot and its surroundings, and represent a primary barrier to deploying VLAs outside controlled laboratory settings~\cite{li2026vlasafety}. The SafeLIBERO benchmark~\cite{hu2025vlsa}, an extension of the LIBERO simulation platform~\cite{liu2023libero}, provides the first systematic protocol for measuring collision behavior in VLA manipulation tasks, reporting the Collision Avoidance Rate (CAR) as the fraction of episodes free from robot-obstacle contact. Recent methods have adopted this evaluation framework to demonstrate safety improvements: SDF-augmented training~\cite{zhang2025safevla}, constraint-based planning~\cite{yang2025cape}, and collision-free demonstration learning~\cite{cofreeevla2026} all report high CAR under standard evaluation. Our own SDF-augmented Pi0~\cite{black2024pi0} configuration reaches 91.5\% CAR across 800 evaluation episodes (four independent runs). The collision avoidance problem appears close to solved.
4	
5	\begin{figure}[t]
6	\centering
7	\fbox{\parbox{0.92\linewidth}{\vspace{3.5cm}\centering\textit{Placeholder: Figure 1. The fake safety problem.\\Left: Pi0+A1 achieves CAR\,=\,91.5\% but TSR\,=\,0\% (robot frozen, displacement $<$\,0.1\,mm).\\Center: Displacement-filtered CAR$_\text{f}$ drops Pi0+A1 to ${\approx}$\,0\%.\\Right: Pi0.5 achieves CAR\,=\,28.5\% with TSR\,=\,71.5\% (all safe episodes above 288\,mm displacement).}\vspace{3.5cm}}}
8	\caption{The fake safety problem in VLA collision avoidance evaluation. Standard CAR classifies a frozen robot as safe because it produces zero collisions (left). CAR$_\text{f}$ filters out action-collapsed episodes where displacement falls below $\tau_d$, revealing that Pi0+A1's 91.5\% safety score drops to ${\approx}$\,0\% (center). Pi0.5 exhibits genuine avoidance with 
…[truncated 6753 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260526T173810",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T17:39:17.257970+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260526T173810",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T17:39:17.258106+00:00_

1	\begin{abstract}
2	Recent methods for collision avoidance in Vision-Language-Action (VLA) models report high Collision Avoidance Rate (CAR) on safety benchmarks and claim effective obstacle avoidance. We show that these metrics can be systematically contaminated by action collapse: the model ceases to produce meaningful motion, and the resulting inaction is counted as successful avoidance. On the SafeLIBERO benchmark, a Signed Distance Field (SDF)-augmented VLA reports 91.5\% CAR alongside 0\% Task Success Rate (TSR), yet 99.6\% of its safe episodes exhibit end-effector displacement below 0.1\,mm and obstacle displacement at the nanometer scale. This contamination is not method-specific; a baseline without any collision objective achieves 82\% CAR with 99.4\% of safe episodes below the same threshold, while Pi0.5, which achieves 74.7\% TSR, exhibits 0\% fake safety; all of its safe episodes reflect genuine avoidance with end-effector displacements exceeding 288\,mm. We propose a corrective metric, displacement-filtered CAR (CAR$_\text{f}$), that excludes sub-threshold episodes. Two structural issues compound the problem. First, TSR and CAR are anti-correlated: models that move the robot through the workspace collide, while collapsed models appear safe. Second, ground-truth SDF oracle experiments demonstrate that end-effector-only refinement cannot prevent full-body collisions, as SDF gradients that repel the end-effector simultaneously drive arm links into obstacle volumes. Fine-tuning on collision-free demonstrations produces genuine collision avoidance (CAR ${\sim}$55\%, zero frozen rate) but at the cost of catastrophic task performance collapse (TSR drops from 74.7\% to $<$7\%), and explicit SDF supervision adds no measurable benefit. Our findings establish that displacement filtering is necessary for meaningful VLA safety evaluation.
3	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260526T173810",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-26T17:39:17.258306+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
  "content": "\\begin{abstract}\nVision-Language-Action (VLA) models report high Collision Avoidance Rate (CAR) on safety benchmarks, but these scores can be artifacts of action collapse rather than learned avoidance. On SafeLIBERO, an SDF-augmented Pi0 configuration achieves 91.5\\% CAR with 0\\% Task Success Rate (TSR); 99.6\\% of its safe episodes exhibit end-effector (EE) displacement below 0.1\\,mm, and 73.9\\% remain below 1\\,$\\mu$m. The robot is frozen, not safe. In contrast, Pi0.5 achieves 74.7\\%\\,$\\pm$\\,1.5\\% TSR and 26.8\\%\\,$\\pm$\\,1.6\\% CAR with zero fake safe episodes, all exceeding 288\\,mm displacement. We propose displacement-filtered CAR (CAR$_\\text{f}$), which excludes episodes below a displacement threshold $\\tau_d$. The bimodal displacement distribution (five orders of magnitude gap between collapsed and active episodes) makes $\\tau_d$ robust across $[2, 200]$\\,mm; applying CAR$_\\text{f}$ collapses Pi0+A1 from 91.5\\% to approximately 0\\%. Beyond metric contamination, EE-only Signed Distance Field (SDF) refinement is structurally limited: three ground-truth oracle variants achieve 73.1--76.9\\% CAR, all below unrefined baselines (82--83\\%), because SDF gradients that repel the EE simultaneously drive arm links into obstacle volumes. Attribution experiments show that collision avoidance in fine-tuned models originates from collision-free demonstration data, not geometric supervision: LoRA-only training (CAR\\,=\\,54.5\\%) matches LoRA+SDF at $\\lambda \\in \\{0.005, 0.01\\}$ ($p > 0.1$). Fine-tuning produces genuine avoidance with zero frozen episodes but incurs moderate TSR degradation of ${\\sim}$21--23 percentage points (74.7\\% $\\to$ 51.5--54.0\\%). Displacement filtering is necessary for meaningful VLA safety evaluation.\n\\end{abstract}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260526T173810",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
    "content": "\\begin{abstract}\nVision-Language-Action (VLA) models report high Collision Avoidance Rate (CAR) on safety benchmarks, but these scores can be artifacts of action collapse rather than learned avoidance. On SafeLIBERO, an SDF-augmented Pi0 configuration achieves 91.5\\% CAR with 0\\% Task Success Rate (TSR); 99.6\\% of its safe episodes exhibit end-effector (EE) displacement below 0.1\\,mm, and 73.9\\% remain below 1\\,$\\mu$m. The robot is frozen, not safe. In contrast, Pi0.5 achieves 74.7\\%\\,$\\pm$\\,1.5\\% TSR and 26.8\\%\\,$\\pm$\\,1.6\\% CAR with zero fake safe episodes, all exceeding 288\\,mm displacement. We propose displacement-filtered CAR (CAR$_\\text{f}$), which excludes episodes below a displacement threshold $\\tau_d$. The bimodal displacement distribution (five orders of magnitude gap between collapsed and active episodes) makes $\\tau_d$ robust across $[2, 200]$\\,mm; applying CAR$_\\text{f}$ collapses Pi0+A1 from 91.5\\% to approximately 0\\%. Beyond metric contamination, EE-only Signed Distance Field (SDF) refinement is structurally limited: three ground-truth oracle variants achieve 73.1--76.9\\% CAR, all below unrefined baselines (82--83\\%), because SDF gradients that repel the EE simultaneously drive arm links into obstacle volumes. Attribution experiments show that collision avoidance in fine-tuned models originates from collision-free demonstration data, not geometric supervision: LoRA-only training (CAR\\,=\\,54.5\\%) matches LoRA+SDF at $\\lambda \\in \\{0.005, 0.01\\}$ ($p > 0.1$). Fine-tuning produces genuine avoidance with zero frozen episodes but incurs moderate TSR degradation of ${\\sim}$21--23 percentage points (74.7\\% $\\to$ 51.5--54.0\\%). Displacement filtering is necessary for meaningful VLA safety evaluation.\n\\end{abstract}\n"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-26T17:39:17.258517+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260526T173810",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-26T17:39:17.258690+00:00_

文件已写入。~228 words，覆盖全部 7 个结构要求，无违禁措辞。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_abstract_20260526T173810"
}
```

</details>

---

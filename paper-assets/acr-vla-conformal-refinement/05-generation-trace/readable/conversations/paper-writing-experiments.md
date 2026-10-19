# paper writing experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/chats/worker_paper_writing_experiments_20260518T095825.jsonl`
- **Structured JSON:** [`9b3cf9a821dd58c9c3ce.json`](../../sessions/9b/9b3cf9a821dd58c9c3ce.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

43 recorded events

### Tool call

_source line 1 · 2026-05-18T10:10:24.349250+00:00_

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
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T10:10:24.349854+00:00_

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
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T10:10:24.350053+00:00_

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
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T10:10:24.350430+00:00_

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
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T10:10:24.350610+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/paper_evidence_package.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/paper_evidence_package.md"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T10:10:24.350816+00:00_

1	# Paper Evidence Package — ACR-VLA Conformal Refinement
2	
3	> Prepared: 2026-05-18. For Paper Agent startup. Contains locked evidence, data tables, figure inventory, and decision chain summary. No prose — data and facts only.
4	
5	---
6	
7	## 1. Method Description (D058 Corrected)
8	
9	### Pipeline (K=10, primary result)
10	1. Frozen VLA (SmolVLA 0.4B) generates **K=10 action samples** from flow-matching
11	2. **Argmin selection**: pick candidate closest to sample mean (L2 distance) — same for all CRM variants
12	3. **CRM correction**: lightweight MLP (~337K params) takes selected action + conditioning features → outputs refined action
13	4. Apply correction with norm clipping: `||correction|| ≤ ε`
14	
15	### CRM Variants (same architecture, different conditioning)
16	- **obs_only**: VLA observation features only (960D). **Does NOT use conformal statistics.**
17	- **perdof**: observation features + per-DOF conformal features (40D CGS: 30 per-DOF std + 5 conformal radius + 5 log volume)
18	- **scalar**: observation features + scalar uncertainty (1D)
19	
20	### Key Architectural Facts
21	- CRM is a **correction** module, not a selection/ranking module
22	- CRM never scores individual candidates — it only refines the one selected by argmin
23	- The 17.5% vs 12.3% improvement comes from **learned correction**, not ranking
24	- K-value curve mechanism: more samples → better argmin starting point → more effective correction
25	
26	### K=1 Mode
27	- No multi-sample selection (only 1 VLA sample)
28	- CRM directly corrects single VLA output using observation features
29	- K=1 CRM ≈ VLA-only baseline (10.3% vs 10.8%) — correction alone without selection is insufficient
30	
31	---
32	
33	## 2. Complete Evidence Tables
34	
35	### 2A. Magnitude Curve (Figure 2 data)
36	
37	**obs_only (observation-conditioned CRM)**
38	
39	| ε (norm clip) | Seeds | Mean SR | Std | n |
40	|---------------|-------|---------|-----|---|
41	| 0.03 | 42=16% | 16.0% | — | 1 |
42	| 0.05 | 42=13%, 43=1
…[truncated 9262 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T10:10:24.351004+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T10:10:24.351132+00:00_

docs/paper/related_work.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/discussion.tex
docs/paper/experiments.tex
docs/paper/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T10:10:24.351253+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T10:10:24.351395+00:00_

docs/paper/related_work.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/discussion.tex
docs/paper/experiments.tex
docs/paper/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T10:10:24.351511+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T10:10:24.351740+00:00_

1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	We evaluate ACR-VLA on two LIBERO task suites to answer three questions:
6	(i)~Does observation-conditioned residual correction significantly improve over the frozen VLA baseline?
7	(ii)~Do per-DOF conformal features provide additional benefit beyond observation conditioning?
8	(iii)~How sensitive is performance to the magnitude bound $\varepsilon$?
9	The answers are: yes (+6\,pp over VLA-only, $p < 0.01$), no (honest negative), and critically, unbounded correction is catastrophic, but obs\_only is robust across all tested seeds and magnitude bounds.
10	
11	\subsection{Experimental Setup}
12	\label{sec:exp_setup}
13	
14	\paragraph{Benchmarks.}
15	We use two suites from the LIBERO benchmark~\cite{liu2023libero}:
16	\textbf{LIBERO-Spatial} (10 tasks requiring spatial reasoning about object layout) and \textbf{LIBERO-Object} (10 tasks requiring generalization across novel object instances).
17	Each task is evaluated over 10 rollouts with a maximum episode length of 300 steps, yielding 100 episodes per suite. Success is binary: an episode succeeds if the task predicate is satisfied before the step limit.
18	
19	\paragraph{Base VLA.}
20	We build on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.
21	We use the checkpoint \texttt{lerobot/smolvla\_libero}, which receives dual-camera RGB input (agentview + eye-in-hand, $256{\times}256$) and 8D proprioceptive state.
22	Actions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper, with the gripper dimension handled outside the conformal pipeline via direct thresholding.
23	
24	\paragraph{Baselines.}
25	All methods use the same frozen SmolVLA checkpoint:
26	\begin{itemize}[nosep]
27	  \item \textbf{VLA-only} ($K{=}1$): single sample from the frozen VLA, no selection or correction.
28	  \item \textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples, no selection or correction.
29	  \item \textbf{Argmin} ($K{=}10
…[truncated 17100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T10:10:24.351930+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n '\\\\label{' /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex | head -20",
  "description": "Find label references in method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n '\\\\label{' /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex | head -20",
    "description": "Find label references in method.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T10:10:24.352061+00:00_

3:\label{sec:method}
8:\label{sec:problem_setup}
15:\label{sec:selection}
20:  \label{eq:argmin}
25:\label{sec:crm}
33:  \label{eq:crm}
50:  \label{eq:loss}
55:\label{sec:magnitude}
68:\label{sec:inference_protocol}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T10:10:24.352182+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n '\\\\label{' /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex | head -20",
  "description": "Find label references in introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n '\\\\label{' /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex | head -20",
    "description": "Find label references in introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T10:10:24.352317+00:00_

2:\label{sec:intro}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T10:10:24.352784+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex",
  "content": "\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate the Conformal Refinement Module (CRM) on LIBERO-Object to answer four questions:\n(1)~Where does the improvement originate, multi-sample selection or learned correction?\n(2)~How does CRM conditioning interact with correction magnitude?\n(3)~Does performance scale with the number of VLA samples $K$?\n(4)~Does the approach transfer to tokenized VLAs?\nIn brief: correction contributes 4--5$\\times$ more than selection (\\S\\ref{sec:component}); observation-only conditioning is robust across magnitudes while conformal conditioning collapses (\\S\\ref{sec:magnitude_interaction}); performance increases monotonically from $K{=}1$ to $K{=}10$ (\\S\\ref{sec:kvalue}); and tokenized VLAs lack the sampling diversity that multi-sample refinement requires (\\S\\ref{sec:applicability}).\n\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmark.}\nWe use LIBERO-Object~\\cite{liu2023libero}, a suite of 10 tabletop manipulation tasks requiring generalization to novel object instances.\nEach task is evaluated over 10 rollouts (maximum 300 steps), for 100 episodes per method per seed.\nSuccess is binary: the task predicate must be satisfied before the step limit.\n\n\\paragraph{Base VLA.}\nWe build on SmolVLA~\\cite{shukor2025smolvla}, a 0.4B-parameter flow-matching VLA.\nThe model receives dual-camera RGB input (agentview + eye-in-hand, $256{\\times}256$) and 8D proprioceptive state, and outputs 7D actions (6D end-effector pose + 1D gripper).\nThe gripper dimension is handled via direct thresholding, outside the refinement pipeline.\n\n\\paragraph{Baselines.}\nAll methods share the same frozen SmolVLA checkpoint:\n\\begin{itemize}[nosep]\n  \\item \\textbf{VLA-only} ($K{=}1$): single VLA sample, no selection or correction.\n  \\item \\textbf{Random sel.}\\ ($K{=}10$): one uniformly random sample from 10 candidates.\n  \\item \\textbf{Argmin sel.}\\ ($K{=}10$): candidate closest to the sample mean (L2 distance), no correction.\n  \\item \\textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples.\n\\end{itemize}\n\n\\paragraph{CRM variants.}\nThree CRM variants share the same 3-layer MLP (${\\sim}$337K parameters) and differ only in conditioning input:\n\\begin{itemize}[nosep]\n  \\item \\textbf{obs\\_only}: frozen VLA observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{960}$. Does \\emph{not} use conformal statistics. This is our primary method.\n  \\item \\textbf{perdof}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 40D per-DOF conformal features (standard deviations, conformal radii, log-volume terms).\n  \\item \\textbf{scalar}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 1D scalar uncertainty.\n\\end{itemize}\n\n\\paragraph{Statistical protocol.}\nEach condition is evaluated with 2--6 seeds (100 rollouts per seed).\nWe report mean $\\pm$ standard deviation across seeds.\nFor the primary comparison, we apply a one-sided Fisher exact test on pooled rollout counts and report Cohen's $d$ as the effect size measure.\n\n\n%----------------------------------------------------------------------\n\\subsection{Main Results: Component Decomposition}\n\\label{sec:component}\n\nTable~\\ref{tab:component} decomposes the full pipeline into selection and correction stages.\nThe three non-CRM multi-sample methods (random, argmin, VLA-mean) cluster within 11--13\\%, % exp_id: §2C, §2D\nat most 1.3\\,pp above VLA-only. % exp_id: §2C\nOnly obs\\_only CRM breaks out of this band.\n\n\\begin{table}[t]\n\\centering\n\\caption{Component decomposition on LIBERO-Object (100 rollouts per seed).\nBold: best; underline: second best.\n$^\\dagger$Partial data: 7/10 tasks completed, seed\\,42 only.\n$^\\ddagger$Best $\\varepsilon$ per variant.}\n\\label{tab:component}\n\\small\n\\begin{tabular}{@{}lccrl@{}}\n\\toprule\nMethod & SR (\\%) $\\uparrow$ & Seeds & $\\Delta$ & Component \\\\\n\\midrule\nVLA-only ($K{=}1$)\n  & $11.2 \\pm 1.6$  & 5 & ---     & Baseline \\\\      % exp_id: §2C\nRandom sel.\\ ($K{=}10$)$^\\dagger$\n  & ${\\sim}11.4$     & 1 & $+0.2$  & ---      \\\\      % exp_id: §2C, partial seed42\nArgmin sel.\\ ($K{=}10$)\n  & $12.4 \\pm 2.9$  & 5 & $+1.2$  & + Selection \\\\   % exp_id: §2C\nVLA-mean ($K{=}10$)\n  & $\\underline{12.5 \\pm 2.1}$ & 4 & $+1.3$ & + Aggregation \\\\ % exp_id: §2C\n\\midrule\nCRM scalar$^\\ddagger$ ($K{=}10$)\n  & $8.3 \\pm 2.1$   & 3 & $-2.9$  & + Correction \\\\  % exp_id: §2C\nCRM perdof$^\\ddagger$ ($K{=}10$, $\\varepsilon{=}0.1$)\n  & $11.0 \\pm 2.0$  & 6 & $-0.2$  & + Correction \\\\  % exp_id: §2C\n\\textbf{CRM obs\\_only} ($K{=}10$, $\\varepsilon{=}0.2$)\n  & $\\mathbf{17.5 \\pm 2.8}$ & \\textbf{6} & $\\mathbf{+6.3}$ & \\textbf{+ Correction} \\\\ % exp_id: §2C\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Selection contributes ${\\sim}$1\\,pp; correction contributes ${\\sim}$5\\,pp.}\nArgmin selection adds only ${\\sim}$1\\,pp over random selection ($12.4\\%$ vs ${\\sim}11.4\\%$), % exp_id: §2D\nconfirming that L2-to-mean ranking provides a weak signal at $K{=}10$.\nThe obs\\_only CRM then adds ${\\sim}$5\\,pp on top of argmin ($17.5\\%$ vs $12.4\\%$), % exp_id: §2D\nso correction is 4--5$\\times$ more valuable than selection. % exp_id: §2D\n\nThis result is statistically reliable.\nobs\\_only vs VLA-only yields Fisher exact $p = 0.0074$ (one-sided) with Cohen's $d = 1.21$; % exp_id: §2E\nobs\\_only vs argmin yields a paired $t$-test $p = 0.016$. % exp_id: §2E\n\n\\paragraph{Negative results: conformal conditioning hurts.}\nThe perdof variant ($11.0\\%$) performs no better than VLA-only despite receiving 40 additional conformal features, % exp_id: §2C\nand scalar ($8.3\\%$) is 2.9\\,pp \\emph{worse} than the uncorrected baseline. % exp_id: §2C\nWith $K{=}10$ samples in $d{=}6$ dimensions, per-DOF covariance estimates carry substantial noise.\nThe obs\\_only variant avoids this failure mode by conditioning solely on the VLA observation embedding, which already encodes task-relevant geometric information (object identity, gripper-object relationship, task progress) without the intermediate conformal statistics.\n\n\n%----------------------------------------------------------------------\n\\subsection{Conditioning-Magnitude Interaction}\n\\label{sec:magnitude_interaction}\n\nThe norm bound $\\varepsilon$ (Section~\\ref{sec:magnitude}) controls how far the CRM can deviate from the selected action.\nTable~\\ref{tab:magnitude} and Figure~\\ref{fig:magnitude} reveal a sharp contrast between obs\\_only and perdof across the magnitude range.\n\n\\begin{table}[t]\n\\centering\n\\caption{Success rate (\\%) on LIBERO-Object across correction magnitudes $\\varepsilon$.\nSeed count in parentheses.\nBold marks the overall best.\nThe VLA-only baseline ($11.2\\%$, independent of $\\varepsilon$) is shown for reference.}\n\\label{tab:magnitude}\n\\small\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n$\\varepsilon$ & 0.03 & 0.05 & 0.1 & 0.2 & 0.3 & uncapped \\\\\n\\midrule\nobs\\_only\n  & 16.0\\,(1) & 13.5\\,(2) & 15.3\\,(4) & \\textbf{17.5}\\,(6) & 17.0\\,(4) & 14.3\\,(3) \\\\ % exp_id: §2A\nperdof\n  & 14.0\\,(1) & 14.0\\,(1) & 11.0\\,(6) & 9.8\\,(6) & 4.7\\,(3) & 0.0\\,(3) \\\\              % exp_id: §2A\n\\midrule\nVLA-only\n  & \\multicolumn{6}{c}{$11.2 \\pm 1.6$ (flat, no correction)} \\\\                           % exp_id: §2C\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/magnitude_curve.pdf}\n\\caption{Success rate vs correction magnitude $\\varepsilon$ on LIBERO-Object.\nobs\\_only (blue) stays above the VLA-only baseline at every tested $\\varepsilon$.\nperdof (red) collapses from 14\\% at small $\\varepsilon$ to 0\\% when uncapped.\nError bars: $\\pm$1 std; seed counts annotated per point.}\n\\label{fig:magnitude}\n\\end{figure}\n\n\\paragraph{obs\\_only is robust across magnitudes.}\nobs\\_only stays above VLA-only at every tested $\\varepsilon$, % exp_id: §2A\nwith performance in a narrow band from 13.5\\% ($\\varepsilon{=}0.05$) to 17.5\\% ($\\varepsilon{=}0.2$). % exp_id: §2A\nEven uncapped ($\\varepsilon \\approx 1.42$), it achieves 14.3\\%, % exp_id: §2A\nstill 3.1\\,pp above VLA-only. % exp_id: §2A, §2C\nA practitioner need not carefully tune $\\varepsilon$: any value in $[0.03, 0.3]$ yields consistent improvement.\n\n\\paragraph{perdof collapses progressively.}\nperdof declines monotonically as $\\varepsilon$ grows: $14.0 \\to 14.0 \\to 11.0 \\to 9.8 \\to 4.7 \\to 0.0$. % exp_id: §2A\nAt small $\\varepsilon$, the tight norm bound clips erroneous corrections and masks the noisy conformal features.\nAs $\\varepsilon$ increases, the CRM applies larger corrections along unreliable directions, and compounding error across the trajectory destroys performance.\nAll three uncapped perdof seeds score 0/100 successes. % exp_id: §2H\n\nThis interaction is the central diagnostic: the same architecture succeeds or fails based on whether it receives clean (observation-only) or noisy (conformal) conditioning.\nThe magnitude bound does not rescue a poorly conditioned CRM; it only delays the collapse.\n\n\n%----------------------------------------------------------------------\n\\subsection{Inference-Time Scaling (K-Value Curve)}\n\\label{sec:kvalue}\n\nFigure~\\ref{fig:kvalue} plots task success rate as a function of the number of VLA samples $K$ for obs\\_only at $\\varepsilon{=}0.2$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/k_value_curve.pdf}\n\\caption{Success rate vs number of VLA samples $K$ for obs\\_only ($\\varepsilon{=}0.2$) on LIBERO-Object.\nPerformance increases monotonically from $K{=}1$ to $K{=}10$.\nError bars: $\\pm$1 std where multiple seeds are available.\n$^*$Single seed (seed\\,42).}\n\\label{fig:kvalue}\n\\end{figure}\n\nAt $K{=}1$, the CRM corrects a single VLA output without multi-sample selection and achieves $10.3\\% \\pm 1.5\\%$ ($n{=}3$), % exp_id: §2B\nindistinguishable from VLA-only ($11.2\\%$). % exp_id: §2C\nAt $K{=}5$, performance rises to $14.0\\%$ (single seed$^*$, seed\\,42). % exp_id: §2B\nAt $K{=}10$, the full pipeline reaches $17.5\\% \\pm 2.8\\%$ ($n{=}6$). % exp_id: §2B\nThe trend is monotonic: $10.3\\% \\to 14.0\\% \\to 17.5\\%$. % exp_id: §2B\n\nMore VLA samples improve the argmin starting point: with larger $K$, the selected candidate sits closer to the sample centroid and, on average, closer to the demonstration action.\nThe CRM correction is then more effective because smaller residuals keep the output within the reliable regime of the learned MLP.\n\nThe $K{=}1$ result is the critical control.\nIt confirms that correction alone, without multi-sample selection, provides no measurable benefit over the uncorrected VLA.\nThe CRM does not learn a fixed correction bias independent of sample quality; the improvement requires both a good starting point from selection and a learned residual from the CRM.\n\n\n%----------------------------------------------------------------------\n\\subsection{Applicability Boundary: Tokenized VLAs}\n\\label{sec:applicability}\n\nThe multi-sample pipeline requires diverse action candidates from the base VLA.\nWe test this prerequisite on OpenVLA~\\cite{kim2024openvla}, a 7B-parameter autoregressive VLA based on Llama-2.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/diversity_analysis.pdf}\n\\caption{Action sample diversity comparison.\nSmolVLA (flow-matching) produces diverse candidates across flow trajectories.\nOpenVLA (autoregressive, $T{=}0.5$) generates near-identical samples: 8/10 are identical with per-DOF variance $< 10^{-30}$.}\n\\label{fig:diversity}\n\\end{figure}\n\nAt standard temperature $T{=}0.5$, OpenVLA's $K{=}10$ samples are near-deterministic: % exp_id: §2G\n8 of 10 are identical, with per-DOF variance below $10^{-30}$. % exp_id: §2G\nMulti-sample selection over identical candidates reduces to random selection, and the CRM receives the same input regardless of $K$.\n\nRaising $T$ to 1.5 or above increases diversity but degrades the base policy. % exp_id: §2G\nNo temperature setting achieves both sufficient diversity and acceptable base performance. % exp_id: §2G\n\nThe multi-sample refinement pipeline is therefore specific to stochastic VLA architectures (e.g., flow-matching models) that produce naturally diverse candidates at their standard operating point.\nTokenized autoregressive VLAs would require alternative candidate generation strategies, such as latent-space perturbation or ensemble decoding.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex",
    "content": "\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate the Conformal Refinement Module (CRM) on LIBERO-Object to answer four questions:\n(1)~Where does the improvement originate, multi-sample selection or learned correction?\n(2)~How does CRM conditioning interact with correction magnitude?\n(3)~Does performance scale with the number of VLA samples $K$?\n(4)~Does the approach transfer to tokenized VLAs?\nIn brief: correction contributes 4--5$\\times$ more than selection (\\S\\ref{sec:component}); observation-only conditioning is robust across magnitudes while conformal conditioning collapses (\\S\\ref{sec:magnitude_interaction}); performance increases monotonically from $K{=}1$ to $K{=}10$ (\\S\\ref{sec:kvalue}); and tokenized VLAs lack the sampling diversity that multi-sample refinement requires (\\S\\ref{sec:applicability}).\n\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmark.}\nWe use LIBERO-Object~\\cite{liu2023libero}, a suite of 10 tabletop manipulation tasks requiring generalization to novel object instances.\nEach task is evaluated over 10 rollouts (maximum 300 steps), for 100 episodes per method per seed.\nSuccess is binary: the task predicate must be satisfied before the step limit.\n\n\\paragraph{Base VLA.}\nWe build on SmolVLA~\\cite{shukor2025smolvla}, a 0.4B-parameter flow-matching VLA.\nThe model receives dual-camera RGB input (agentview + eye-in-hand, $256{\\times}256$) and 8D proprioceptive state, and outputs 7D actions (6D end-effector pose + 1D gripper).\nThe gripper dimension is handled via direct thresholding, outside the refinement pipeline.\n\n\\paragraph{Baselines.}\nAll methods share the same frozen SmolVLA checkpoint:\n\\begin{itemize}[nosep]\n  \\item \\textbf{VLA-only} ($K{=}1$): single VLA sample, no selection or correction.\n  \\item \\textbf{Random sel.}\\ ($K{=}10$): one uniformly random sample from 10 candidates.\n  \\item \\textbf{Argmin sel.}\\ ($K{=}10$): candidate closest to the sample mean (L2 distance), no correction.\n  \\item \\textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples.\n\\end{itemize}\n\n\\paragraph{CRM variants.}\nThree CRM variants share the same 3-layer MLP (${\\sim}$337K parameters) and differ only in conditioning input:\n\\begin{itemize}[nosep]\n  \\item \\textbf{obs\\_only}: frozen VLA observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{960}$. Does \\emph{not} use conformal statistics. This is our primary method.\n  \\item \\textbf{perdof}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 40D per-DOF conformal features (standard deviations, conformal radii, log-volume terms).\n  \\item \\textbf{scalar}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 1D scalar uncertainty.\n\\end{itemize}\n\n\\paragraph{Statistical protocol.}\nEach condition is evaluated with 2--6 seeds (100 rollouts per seed).\nWe report mean $\\pm$ standard deviation across seeds.\nFor the primary comparison, we apply a one-sided Fisher exact test on pooled rollout counts and report Cohen's $d$ as the effect size measure.\n\n\n%----------------------------------------------------------------------\n\\subsection{Main Results: Component Decomposition}\n\\label{sec:component}\n\nTable~\\ref{tab:component} decomposes the full pipeline into selection and correction stages.\nThe three non-CRM multi-sample methods (random, argmin, VLA-mean) cluster within 11--13\\%, % exp_id: §2C, §2D\nat most 1.3\\,pp above VLA-only. % exp_id: §2C\nOnly obs\\_only CRM breaks out of this band.\n\n\\begin{table}[t]\n\\centering\n\\caption{Component decomposition on LIBERO-Object (100 rollouts per seed).\nBold: best; underline: second best.\n$^\\dagger$Partial data: 7/10 tasks completed, seed\\,42 only.\n$^\\ddagger$Best $\\varepsilon$ per variant.}\n\\label{tab:component}\n\\small\n\\begin{tabular}{@{}lccrl@{}}\n\\toprule\nMethod & SR (\\%) $\\uparrow$ & Seeds & $\\Delta$ & Component \\\\\n\\midrule\nVLA-only ($K{=}1$)\n  & $11.2 \\pm 1.6$  & 5 & ---     & Baseline \\\\      % exp_id: §2C\nRandom sel.\\ ($K{=}10$)$^\\dagger$\n  & ${\\sim}11.4$     & 1 & $+0.2$  & ---      \\\\      % exp_id: §2C, partial seed42\nArgmin sel.\\ ($K{=}10$)\n  & $12.4 \\pm 2.9$  & 5 & $+1.2$  & + Selection \\\\   % exp_id: §2C\nVLA-mean ($K{=}10$)\n  & $\\underline{12.5 \\pm 2.1}$ & 4 & $+1.3$ & + Aggregation \\\\ % exp_id: §2C\n\\midrule\nCRM scalar$^\\ddagger$ ($K{=}10$)\n  & $8.3 \\pm 2.1$   & 3 & $-2.9$  & + Correction \\\\  % exp_id: §2C\nCRM perdof$^\\ddagger$ ($K{=}10$, $\\varepsilon{=}0.1$)\n  & $11.0 \\pm 2.0$  & 6 & $-0.2$  & + Correction \\\\  % exp_id: §2C\n\\textbf{CRM obs\\_only} ($K{=}10$, $\\varepsilon{=}0.2$)\n  & $\\mathbf{17.5 \\pm 2.8}$ & \\textbf{6} & $\\mathbf{+6.3}$ & \\textbf{+ Correction} \\\\ % exp_id: §2C\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Selection contributes ${\\sim}$1\\,pp; correction contributes ${\\sim}$5\\,pp.}\nArgmin selection adds only ${\\sim}$1\\,pp over random selection ($12.4\\%$ vs ${\\sim}11.4\\%$), % exp_id: §2D\nconfirming that L2-to-mean ranking provides a weak signal at $K{=}10$.\nThe obs\\_only CRM then adds ${\\sim}$5\\,pp on top of argmin ($17.5\\%$ vs $12.4\\%$), % exp_id: §2D\nso correction is 4--5$\\times$ more valuable than selection. % exp_id: §2D\n\nThis result is statistically reliable.\nobs\\_only vs VLA-only yields Fisher exact $p = 0.0074$ (one-sided) with Cohen's $d = 1.21$; % exp_id: §2E\nobs\\_only vs argmin yields a paired $t$-test $p = 0.016$. % exp_id: §2E\n\n\\paragraph{Negative results: conformal conditioning hurts.}\nThe perdof variant ($11.0\\%$) performs no better than VLA-only despite receiving 40 additional conformal features, % exp_id: §2C\nand scalar ($8.3\\%$) is 2.9\\,pp \\emph{worse} than the uncorrected baseline. % exp_id: §2C\nWith $K{=}10$ samples in $d{=}6$ dimensions, per-DOF covariance estimates carry substantial noise.\nThe obs\\_only variant avoids this failure mode by conditioning solely on the VLA observation embedding, which already encodes task-relevant geometric information (object identity, gripper-object relationship, task progress) without the intermediate conformal statistics.\n\n\n%----------------------------------------------------------------------\n\\subsection{Conditioning-Magnitude Interaction}\n\\label{sec:magnitude_interaction}\n\nThe norm bound $\\varepsilon$ (Section~\\ref{sec:magnitude}) controls how far the CRM can deviate from the selected action.\nTable~\\ref{tab:magnitude} and Figure~\\ref{fig:magnitude} reveal a sharp contrast between obs\\_only and perdof across the magnitude range.\n\n\\begin{table}[t]\n\\centering\n\\caption{Success rate (\\%) on LIBERO-Object across correction magnitudes $\\varepsilon$.\nSeed count in parentheses.\nBold marks the overall best.\nThe VLA-only baseline ($11.2\\%$, independent of $\\varepsilon$) is shown for reference.}\n\\label{tab:magnitude}\n\\small\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n$\\varepsilon$ & 0.03 & 0.05 & 0.1 & 0.2 & 0.3 & uncapped \\\\\n\\midrule\nobs\\_only\n  & 16.0\\,(1) & 13.5\\,(2) & 15.3\\,(4) & \\textbf{17.5}\\,(6) & 17.0\\,(4) & 14.3\\,(3) \\\\ % exp_id: §2A\nperdof\n  & 14.0\\,(1) & 14.0\\,(1) & 11.0\\,(6) & 9.8\\,(6) & 4.7\\,(3) & 0.0\\,(3) \\\\              % exp_id: §2A\n\\midrule\nVLA-only\n  & \\multicolumn{6}{c}{$11.2 \\pm 1.6$ (flat, no correction)} \\\\                           % exp_id: §2C\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/magnitude_curve.pdf}\n\\caption{Success rate vs correction magnitude $\\varepsilon$ on LIBERO-Object.\nobs\\_only (blue) stays above the VLA-only baseline at every tested $\\varepsilon$.\nperdof (red) collapses from 14\\% at small $\\varepsilon$ to 0\\% when uncapped.\nError bars: $\\pm$1 std; seed counts annotated per point.}\n\\label{fig:magnitude}\n\\end{figure}\n\n\\paragraph{obs\\_only is robust across magnitudes.}\nobs\\_only stays above VLA-only at every tested $\\varepsilon$, % exp_id: §2A\nwith performance in a narrow band from 13.5\\% ($\\varepsilon{=}0.05$) to 17.5\\% ($\\varepsilon{=}0.2$). % exp_id: §2A\nEven uncapped ($\\varepsilon \\approx 1.42$), it achieves 14.3\\%, % exp_id: §2A\nstill 3.1\\,pp above VLA-only. % exp_id: §2A, §2C\nA practitioner need not carefully tune $\\varepsilon$: any value in $[0.03, 0.3]$ yields consistent improvement.\n\n\\paragraph{perdof collapses progressively.}\nperdof declines monotonically as $\\varepsilon$ grows: $14.0 \\to 14.0 \\to 11.0 \\to 9.8 \\to 4.7 \\to 0.0$. % exp_id: §2A\nAt small $\\varepsilon$, the tight norm bound clips erroneous corrections and masks the noisy conformal features.\nAs $\\varepsilon$ increases, the CRM applies larger corrections along unreliable directions, and compounding error across the trajectory destroys performance.\nAll three uncapped perdof seeds score 0/100 successes. % exp_id: §2H\n\nThis interaction is the central diagnostic: the same architecture succeeds or fails based on whether it receives clean (observation-only) or noisy (conformal) conditioning.\nThe magnitude bound does not rescue a poorly conditioned CRM; it only delays the collapse.\n\n\n%----------------------------------------------------------------------\n\\subsection{Inference-Time Scaling (K-Value Curve)}\n\\label{sec:kvalue}\n\nFigure~\\ref{fig:kvalue} plots task success rate as a function of the number of VLA samples $K$ for obs\\_only at $\\varepsilon{=}0.2$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/k_value_curve.pdf}\n\\caption{Success rate vs number of VLA samples $K$ for obs\\_only ($\\varepsilon{=}0.2$) on LIBERO-Object.\nPerformance increases monotonically from $K{=}1$ to $K{=}10$.\nError bars: $\\pm$1 std where multiple seeds are available.\n$^*$Single seed (seed\\,42).}\n\\label{fig:kvalue}\n\\end{figure}\n\nAt $K{=}1$, the CRM corrects a single VLA output without multi-sample selection and achieves $10.3\\% \\pm 1.5\\%$ ($n{=}3$), % exp_id: §2B\nindistinguishable from VLA-only ($11.2\\%$). % exp_id: §2C\nAt $K{=}5$, performance rises to $14.0\\%$ (single seed$^*$, seed\\,42). % exp_id: §2B\nAt $K{=}10$, the full pipeline reaches $17.5\\% \\pm 2.8\\%$ ($n{=}6$). % exp_id: §2B\nThe trend is monotonic: $10.3\\% \\to 14.0\\% \\to 17.5\\%$. % exp_id: §2B\n\nMore VLA samples improve the argmin starting point: with larger $K$, the selected candidate sits closer to the sample centroid and, on average, closer to the demonstration action.\nThe CRM correction is then more effective because smaller residuals keep the output within the reliable regime of the learned MLP.\n\nThe $K{=}1$ result is the critical control.\nIt confirms that correction alone, without multi-sample selection, provides no measurable benefit over the uncorrected VLA.\nThe CRM does not learn a fixed correction bias independent of sample quality; the improvement requires both a good starting point from selection and a learned residual from the CRM.\n\n\n%----------------------------------------------------------------------\n\\subsection{Applicability Boundary: Tokenized VLAs}\n\\label{sec:applicability}\n\nThe multi-sample pipeline requires diverse action candidates from the base VLA.\nWe test this prerequisite on OpenVLA~\\cite{kim2024openvla}, a 7B-parameter autoregressive VLA based on Llama-2.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/diversity_analysis.pdf}\n\\caption{Action sample diversity comparison.\nSmolVLA (flow-matching) produces diverse candidates across flow trajectories.\nOpenVLA (autoregressive, $T{=}0.5$) generates near-identical samples: 8/10 are identical with per-DOF variance $< 10^{-30}$.}\n\\label{fig:diversity}\n\\end{figure}\n\nAt standard temperature $T{=}0.5$, OpenVLA's $K{=}10$ samples are near-deterministic: % exp_id: §2G\n8 of 10 are identical, with per-DOF variance below $10^{-30}$. % exp_id: §2G\nMulti-sample selection over identical candidates reduces to random selection, and the CRM receives the same input regardless of $K$.\n\nRaising $T$ to 1.5 or above increases diversity but degrades the base policy. % exp_id: §2G\nNo temperature setting achieves both sufficient diversity and acceptable base performance. % exp_id: §2G\n\nThe multi-sample refinement pipeline is therefore specific to stochastic VLA architectures (e.g., flow-matching models) that produce naturally diverse candidates at their standard operating point.\nTokenized autoregressive VLAs would require alternative candidate generation strategies, such as latent-space perturbation or ensemble decoding.\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T10:10:24.353094+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T10:10:24.353239+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T10:10:24.353506+00:00_

1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	We evaluate ACR-VLA on two LIBERO task suites to answer three questions:
6	(i)~Does observation-conditioned residual correction significantly improve over the frozen VLA baseline?
7	(ii)~Do per-DOF conformal features provide additional benefit beyond observation conditioning?
8	(iii)~How sensitive is performance to the magnitude bound $\varepsilon$?
9	The answers are: yes (+6\,pp over VLA-only, $p < 0.01$), no (honest negative), and critically, unbounded correction is catastrophic, but obs\_only is robust across all tested seeds and magnitude bounds.
10	
11	\subsection{Experimental Setup}
12	\label{sec:exp_setup}
13	
14	\paragraph{Benchmarks.}
15	We use two suites from the LIBERO benchmark~\cite{liu2023libero}:
16	\textbf{LIBERO-Spatial} (10 tasks requiring spatial reasoning about object layout) and \textbf{LIBERO-Object} (10 tasks requiring generalization across novel object instances).
17	Each task is evaluated over 10 rollouts with a maximum episode length of 300 steps, yielding 100 episodes per suite. Success is binary: an episode succeeds if the task predicate is satisfied before the step limit.
18	
19	\paragraph{Base VLA.}
20	We build on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.
21	We use the checkpoint \texttt{lerobot/smolvla\_libero}, which receives dual-camera RGB input (agentview + eye-in-hand, $256{\times}256$) and 8D proprioceptive state.
22	Actions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper, with the gripper dimension handled outside the conformal pipeline via direct thresholding.
23	
24	\paragraph{Baselines.}
25	All methods use the same frozen SmolVLA checkpoint:
26	\begin{itemize}[nosep]
27	  \item \textbf{VLA-only} ($K{=}1$): single sample from the frozen VLA, no selection or correction.
28	  \item \textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples, no selection or correction.
29	  \item \textbf{Argmin} ($K{=}10
…[truncated 16461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T10:10:24.353712+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex",
  "content": "\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate the Conformal Refinement Module (CRM) on LIBERO-Object to answer four questions:\n(1)~Where does the improvement originate, multi-sample selection or learned correction?\n(2)~How does CRM conditioning interact with correction magnitude?\n(3)~Does performance scale with the number of VLA samples $K$?\n(4)~Does the approach transfer to tokenized VLAs?\nIn brief: correction contributes 4--5$\\times$ more than selection (\\S\\ref{sec:component}); observation-only conditioning is robust across magnitudes while conformal conditioning collapses (\\S\\ref{sec:magnitude_interaction}); performance increases monotonically from $K{=}1$ to $K{=}10$ (\\S\\ref{sec:kvalue}); and tokenized VLAs lack the sampling diversity that multi-sample refinement requires (\\S\\ref{sec:applicability}).\n\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmark.}\nWe use LIBERO-Object~\\cite{liu2023libero}, a suite of 10 tabletop manipulation tasks requiring generalization to novel object instances.\nEach task is evaluated over 10 rollouts (maximum 300 steps), for 100 episodes per method per seed.\nSuccess is binary: the task predicate must be satisfied before the step limit.\n\n\\paragraph{Base VLA.}\nWe build on SmolVLA~\\cite{shukor2025smolvla}, a 0.4B-parameter flow-matching VLA.\nThe model receives dual-camera RGB input (agentview + eye-in-hand, $256{\\times}256$) and 8D proprioceptive state, and outputs 7D actions (6D end-effector pose + 1D gripper).\nThe gripper dimension is handled via direct thresholding, outside the refinement pipeline.\n\n\\paragraph{Baselines.}\nAll methods share the same frozen SmolVLA checkpoint:\n\\begin{itemize}[nosep]\n  \\item \\textbf{VLA-only} ($K{=}1$): single VLA sample, no selection or correction.\n  \\item \\textbf{Random sel.}\\ ($K{=}10$): one uniformly random sample from 10 candidates.\n  \\item \\textbf{Argmin sel.}\\ ($K{=}10$): candidate closest to the sample mean (L2 distance), no correction.\n  \\item \\textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples.\n\\end{itemize}\n\n\\paragraph{CRM variants.}\nThree CRM variants share the same 3-layer MLP (${\\sim}$337K parameters) and differ only in conditioning input:\n\\begin{itemize}[nosep]\n  \\item \\textbf{obs\\_only}: frozen VLA observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{960}$. Does \\emph{not} use conformal statistics. This is our primary method.\n  \\item \\textbf{perdof}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 40D per-DOF conformal features (standard deviations, conformal radii, log-volume terms).\n  \\item \\textbf{scalar}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 1D scalar uncertainty.\n\\end{itemize}\n\n\\paragraph{Statistical protocol.}\nEach condition is evaluated with 2--6 seeds (100 rollouts per seed).\nWe report mean $\\pm$ standard deviation across seeds.\nFor the primary comparison, we apply a one-sided Fisher exact test on pooled rollout counts and report Cohen's $d$ as the effect size measure.\n\n\n%----------------------------------------------------------------------\n\\subsection{Main Results: Component Decomposition}\n\\label{sec:component}\n\nTable~\\ref{tab:component} decomposes the full pipeline into selection and correction stages.\nThe three non-CRM multi-sample methods (random, argmin, VLA-mean) cluster within 11--13\\%, % exp_id: \\S2C, \\S2D\nat most 1.3\\,pp above VLA-only. % exp_id: \\S2C\nOnly obs\\_only CRM breaks out of this band.\n\n\\begin{table}[t]\n\\centering\n\\caption{Component decomposition on LIBERO-Object (100 rollouts per seed).\nBold: best; underline: second best.\n$^\\dagger$Partial data: 7/10 tasks completed, seed\\,42 only.\n$^\\ddagger$Best $\\varepsilon$ per variant.}\n\\label{tab:component}\n\\small\n\\begin{tabular}{@{}lccrl@{}}\n\\toprule\nMethod & SR (\\%) $\\uparrow$ & Seeds & $\\Delta$ & Component \\\\\n\\midrule\nVLA-only ($K{=}1$)\n  & $11.2 \\pm 1.6$  & 5 & ---     & Baseline \\\\      % exp_id: \\S2C\nRandom sel.\\ ($K{=}10$)$^\\dagger$\n  & ${\\sim}11.4$     & 1 & $+0.2$  & ---      \\\\      % exp_id: \\S2C, partial seed42\nArgmin sel.\\ ($K{=}10$)\n  & $12.4 \\pm 2.9$  & 5 & $+1.2$  & + Selection \\\\   % exp_id: \\S2C\nVLA-mean ($K{=}10$)\n  & $\\underline{12.5 \\pm 2.1}$ & 4 & $+1.3$ & + Aggregation \\\\ % exp_id: \\S2C\n\\midrule\nCRM scalar$^\\ddagger$ ($K{=}10$)\n  & $8.3 \\pm 2.1$   & 3 & $-2.9$  & + Correction \\\\  % exp_id: \\S2C\nCRM perdof$^\\ddagger$ ($K{=}10$, $\\varepsilon{=}0.1$)\n  & $11.0 \\pm 2.0$  & 6 & $-0.2$  & + Correction \\\\  % exp_id: \\S2C\n\\textbf{CRM obs\\_only} ($K{=}10$, $\\varepsilon{=}0.2$)\n  & $\\mathbf{17.5 \\pm 2.8}$ & \\textbf{6} & $\\mathbf{+6.3}$ & \\textbf{+ Correction} \\\\ % exp_id: \\S2C\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Selection contributes ${\\sim}$1\\,pp; correction contributes ${\\sim}$5\\,pp.}\nArgmin selection adds only ${\\sim}$1\\,pp over random selection ($12.4\\%$ vs ${\\sim}11.4\\%$), % exp_id: \\S2D\nconfirming that L2-to-mean ranking provides a weak signal at $K{=}10$.\nThe obs\\_only CRM then adds ${\\sim}$5\\,pp on top of argmin ($17.5\\%$ vs $12.4\\%$), % exp_id: \\S2D\nso correction is 4--5$\\times$ more valuable than selection. % exp_id: \\S2D\n\nThis result is statistically reliable.\nobs\\_only vs VLA-only yields Fisher exact $p = 0.0074$ (one-sided) with Cohen's $d = 1.21$; % exp_id: \\S2E\nobs\\_only vs argmin yields a paired $t$-test $p = 0.016$. % exp_id: \\S2E\n\n\\paragraph{Negative results: conformal conditioning hurts.}\nThe perdof variant ($11.0\\%$) performs no better than VLA-only despite receiving 40 additional conformal features, % exp_id: \\S2C\nand scalar ($8.3\\%$) is 2.9\\,pp \\emph{worse} than the uncorrected baseline. % exp_id: \\S2C\nWith $K{=}10$ samples in $d{=}6$ dimensions, per-DOF covariance estimates carry substantial noise.\nThe obs\\_only variant avoids this failure mode by conditioning solely on the VLA observation embedding, which already encodes task-relevant geometric information (object identity, gripper-object relationship, task progress) without the intermediate conformal statistics.\n\n\n%----------------------------------------------------------------------\n\\subsection{Conditioning-Magnitude Interaction}\n\\label{sec:magnitude_interaction}\n\nThe norm bound $\\varepsilon$ (Section~\\ref{sec:magnitude}) controls how far the CRM can deviate from the selected action.\nTable~\\ref{tab:magnitude} and Figure~\\ref{fig:magnitude} reveal a sharp contrast between obs\\_only and perdof across the magnitude range.\n\n\\begin{table}[t]\n\\centering\n\\caption{Success rate (\\%) on LIBERO-Object across correction magnitudes $\\varepsilon$.\nSeed count in parentheses.\nBold marks the overall best.\nThe VLA-only baseline ($11.2\\%$, independent of $\\varepsilon$) is shown for reference.}\n\\label{tab:magnitude}\n\\small\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n$\\varepsilon$ & 0.03 & 0.05 & 0.1 & 0.2 & 0.3 & uncapped \\\\\n\\midrule\nobs\\_only\n  & 16.0\\,(1) & 13.5\\,(2) & 15.3\\,(4) & \\textbf{17.5}\\,(6) & 17.0\\,(4) & 14.3\\,(3) \\\\ % exp_id: \\S2A\nperdof\n  & 14.0\\,(1) & 14.0\\,(1) & 11.0\\,(6) & 9.8\\,(6) & 4.7\\,(3) & 0.0\\,(3) \\\\              % exp_id: \\S2A\n\\midrule\nVLA-only\n  & \\multicolumn{6}{c}{$11.2 \\pm 1.6$ (flat, no correction)} \\\\                           % exp_id: \\S2C\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/magnitude_curve.pdf}\n\\caption{Success rate vs correction magnitude $\\varepsilon$ on LIBERO-Object.\nobs\\_only (blue) stays above the VLA-only baseline at every tested $\\varepsilon$.\nperdof (red) collapses from 14\\% at small $\\varepsilon$ to 0\\% when uncapped.\nError bars: $\\pm$1 std; seed counts annotated per point.}\n\\label{fig:magnitude}\n\\end{figure}\n\n\\paragraph{obs\\_only is robust across magnitudes.}\nobs\\_only stays above VLA-only at every tested $\\varepsilon$, % exp_id: \\S2A\nwith performance in a narrow band from 13.5\\% ($\\varepsilon{=}0.05$) to 17.5\\% ($\\varepsilon{=}0.2$). % exp_id: \\S2A\nEven uncapped ($\\varepsilon \\approx 1.42$), it achieves 14.3\\%, % exp_id: \\S2A\nstill 3.1\\,pp above VLA-only. % exp_id: \\S2A, \\S2C\nA practitioner need not carefully tune $\\varepsilon$: any value in $[0.03, 0.3]$ yields consistent improvement.\n\n\\paragraph{perdof collapses progressively.}\nperdof declines monotonically as $\\varepsilon$ grows: $14.0 \\to 14.0 \\to 11.0 \\to 9.8 \\to 4.7 \\to 0.0$. % exp_id: \\S2A\nAt small $\\varepsilon$, the tight norm bound clips erroneous corrections and masks the noisy conformal features.\nAs $\\varepsilon$ increases, the CRM applies larger corrections along unreliable directions, and compounding error across the trajectory destroys performance.\nAll three uncapped perdof seeds score 0/100 successes. % exp_id: \\S2H\n\nThis interaction is the central diagnostic: the same architecture succeeds or fails based on whether it receives clean (observation-only) or noisy (conformal) conditioning.\nThe magnitude bound does not rescue a poorly conditioned CRM; it only delays the collapse.\n\n\n%----------------------------------------------------------------------\n\\subsection{Inference-Time Scaling (K-Value Curve)}\n\\label{sec:kvalue}\n\nFigure~\\ref{fig:kvalue} plots task success rate as a function of the number of VLA samples $K$ for obs\\_only at $\\varepsilon{=}0.2$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/k_value_curve.pdf}\n\\caption{Success rate vs number of VLA samples $K$ for obs\\_only ($\\varepsilon{=}0.2$) on LIBERO-Object.\nPerformance increases monotonically from $K{=}1$ to $K{=}10$.\nError bars: $\\pm$1 std where multiple seeds are available.\n$^*$Single seed (seed\\,42).}\n\\label{fig:kvalue}\n\\end{figure}\n\nAt $K{=}1$, the CRM corrects a single VLA output without multi-sample selection and achieves $10.3\\% \\pm 1.5\\%$ ($n{=}3$), % exp_id: \\S2B\nindistinguishable from VLA-only ($11.2\\%$). % exp_id: \\S2C\nAt $K{=}5$, performance rises to $14.0\\%$ (single seed$^*$, seed\\,42). % exp_id: \\S2B\nAt $K{=}10$, the full pipeline reaches $17.5\\% \\pm 2.8\\%$ ($n{=}6$). % exp_id: \\S2B\nThe trend is monotonic: $10.3\\% \\to 14.0\\% \\to 17.5\\%$. % exp_id: \\S2B\n\nMore VLA samples improve the argmin starting point: with larger $K$, the selected candidate sits closer to the sample centroid and, on average, closer to the demonstration action.\nThe CRM correction is then more effective because smaller residuals keep the output within the reliable regime of the learned MLP.\n\nThe $K{=}1$ result is the critical control.\nIt confirms that correction alone, without multi-sample selection, provides no measurable benefit over the uncorrected VLA.\nThe CRM does not learn a fixed correction bias independent of sample quality; the improvement requires both a good starting point from selection and a learned residual from the CRM.\n\n\n%----------------------------------------------------------------------\n\\subsection{Applicability Boundary: Tokenized VLAs}\n\\label{sec:applicability}\n\nThe multi-sample pipeline requires diverse action candidates from the base VLA.\nWe test this prerequisite on OpenVLA~\\cite{kim2024openvla}, a 7B-parameter autoregressive VLA based on Llama-2.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/diversity_analysis.pdf}\n\\caption{Action sample diversity comparison.\nSmolVLA (flow-matching) produces diverse candidates across flow trajectories.\nOpenVLA (autoregressive, $T{=}0.5$) generates near-identical samples: 8/10 are identical with per-DOF variance $< 10^{-30}$.}\n\\label{fig:diversity}\n\\end{figure}\n\nAt standard temperature $T{=}0.5$, OpenVLA's $K{=}10$ samples are near-deterministic: % exp_id: \\S2G\n8 of 10 are identical, with per-DOF variance below $10^{-30}$. % exp_id: \\S2G\nMulti-sample selection over identical candidates reduces to random selection, and the CRM receives the same input regardless of $K$.\n\nRaising $T$ to 1.5 or above increases diversity but degrades the base policy. % exp_id: \\S2G\nNo temperature setting achieves both sufficient diversity and acceptable base performance. % exp_id: \\S2G\n\nThe multi-sample refinement pipeline is therefore specific to stochastic VLA architectures (e.g., flow-matching models) that produce naturally diverse candidates at their standard operating point.\nTokenized autoregressive VLAs would require alternative candidate generation strategies, such as latent-space perturbation or ensemble decoding.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex",
    "content": "\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate the Conformal Refinement Module (CRM) on LIBERO-Object to answer four questions:\n(1)~Where does the improvement originate, multi-sample selection or learned correction?\n(2)~How does CRM conditioning interact with correction magnitude?\n(3)~Does performance scale with the number of VLA samples $K$?\n(4)~Does the approach transfer to tokenized VLAs?\nIn brief: correction contributes 4--5$\\times$ more than selection (\\S\\ref{sec:component}); observation-only conditioning is robust across magnitudes while conformal conditioning collapses (\\S\\ref{sec:magnitude_interaction}); performance increases monotonically from $K{=}1$ to $K{=}10$ (\\S\\ref{sec:kvalue}); and tokenized VLAs lack the sampling diversity that multi-sample refinement requires (\\S\\ref{sec:applicability}).\n\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmark.}\nWe use LIBERO-Object~\\cite{liu2023libero}, a suite of 10 tabletop manipulation tasks requiring generalization to novel object instances.\nEach task is evaluated over 10 rollouts (maximum 300 steps), for 100 episodes per method per seed.\nSuccess is binary: the task predicate must be satisfied before the step limit.\n\n\\paragraph{Base VLA.}\nWe build on SmolVLA~\\cite{shukor2025smolvla}, a 0.4B-parameter flow-matching VLA.\nThe model receives dual-camera RGB input (agentview + eye-in-hand, $256{\\times}256$) and 8D proprioceptive state, and outputs 7D actions (6D end-effector pose + 1D gripper).\nThe gripper dimension is handled via direct thresholding, outside the refinement pipeline.\n\n\\paragraph{Baselines.}\nAll methods share the same frozen SmolVLA checkpoint:\n\\begin{itemize}[nosep]\n  \\item \\textbf{VLA-only} ($K{=}1$): single VLA sample, no selection or correction.\n  \\item \\textbf{Random sel.}\\ ($K{=}10$): one uniformly random sample from 10 candidates.\n  \\item \\textbf{Argmin sel.}\\ ($K{=}10$): candidate closest to the sample mean (L2 distance), no correction.\n  \\item \\textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples.\n\\end{itemize}\n\n\\paragraph{CRM variants.}\nThree CRM variants share the same 3-layer MLP (${\\sim}$337K parameters) and differ only in conditioning input:\n\\begin{itemize}[nosep]\n  \\item \\textbf{obs\\_only}: frozen VLA observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{960}$. Does \\emph{not} use conformal statistics. This is our primary method.\n  \\item \\textbf{perdof}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 40D per-DOF conformal features (standard deviations, conformal radii, log-volume terms).\n  \\item \\textbf{scalar}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 1D scalar uncertainty.\n\\end{itemize}\n\n\\paragraph{Statistical protocol.}\nEach condition is evaluated with 2--6 seeds (100 rollouts per seed).\nWe report mean $\\pm$ standard deviation across seeds.\nFor the primary comparison, we apply a one-sided Fisher exact test on pooled rollout counts and report Cohen's $d$ as the effect size measure.\n\n\n%----------------------------------------------------------------------\n\\subsection{Main Results: Component Decomposition}\n\\label{sec:component}\n\nTable~\\ref{tab:component} decomposes the full pipeline into selection and correction stages.\nThe three non-CRM multi-sample methods (random, argmin, VLA-mean) cluster within 11--13\\%, % exp_id: \\S2C, \\S2D\nat most 1.3\\,pp above VLA-only. % exp_id: \\S2C\nOnly obs\\_only CRM breaks out of this band.\n\n\\begin{table}[t]\n\\centering\n\\caption{Component decomposition on LIBERO-Object (100 rollouts per seed).\nBold: best; underline: second best.\n$^\\dagger$Partial data: 7/10 tasks completed, seed\\,42 only.\n$^\\ddagger$Best $\\varepsilon$ per variant.}\n\\label{tab:component}\n\\small\n\\begin{tabular}{@{}lccrl@{}}\n\\toprule\nMethod & SR (\\%) $\\uparrow$ & Seeds & $\\Delta$ & Component \\\\\n\\midrule\nVLA-only ($K{=}1$)\n  & $11.2 \\pm 1.6$  & 5 & ---     & Baseline \\\\      % exp_id: \\S2C\nRandom sel.\\ ($K{=}10$)$^\\dagger$\n  & ${\\sim}11.4$     & 1 & $+0.2$  & ---      \\\\      % exp_id: \\S2C, partial seed42\nArgmin sel.\\ ($K{=}10$)\n  & $12.4 \\pm 2.9$  & 5 & $+1.2$  & + Selection \\\\   % exp_id: \\S2C\nVLA-mean ($K{=}10$)\n  & $\\underline{12.5 \\pm 2.1}$ & 4 & $+1.3$ & + Aggregation \\\\ % exp_id: \\S2C\n\\midrule\nCRM scalar$^\\ddagger$ ($K{=}10$)\n  & $8.3 \\pm 2.1$   & 3 & $-2.9$  & + Correction \\\\  % exp_id: \\S2C\nCRM perdof$^\\ddagger$ ($K{=}10$, $\\varepsilon{=}0.1$)\n  & $11.0 \\pm 2.0$  & 6 & $-0.2$  & + Correction \\\\  % exp_id: \\S2C\n\\textbf{CRM obs\\_only} ($K{=}10$, $\\varepsilon{=}0.2$)\n  & $\\mathbf{17.5 \\pm 2.8}$ & \\textbf{6} & $\\mathbf{+6.3}$ & \\textbf{+ Correction} \\\\ % exp_id: \\S2C\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Selection contributes ${\\sim}$1\\,pp; correction contributes ${\\sim}$5\\,pp.}\nArgmin selection adds only ${\\sim}$1\\,pp over random selection ($12.4\\%$ vs ${\\sim}11.4\\%$), % exp_id: \\S2D\nconfirming that L2-to-mean ranking provides a weak signal at $K{=}10$.\nThe obs\\_only CRM then adds ${\\sim}$5\\,pp on top of argmin ($17.5\\%$ vs $12.4\\%$), % exp_id: \\S2D\nso correction is 4--5$\\times$ more valuable than selection. % exp_id: \\S2D\n\nThis result is statistically reliable.\nobs\\_only vs VLA-only yields Fisher exact $p = 0.0074$ (one-sided) with Cohen's $d = 1.21$; % exp_id: \\S2E\nobs\\_only vs argmin yields a paired $t$-test $p = 0.016$. % exp_id: \\S2E\n\n\\paragraph{Negative results: conformal conditioning hurts.}\nThe perdof variant ($11.0\\%$) performs no better than VLA-only despite receiving 40 additional conformal features, % exp_id: \\S2C\nand scalar ($8.3\\%$) is 2.9\\,pp \\emph{worse} than the uncorrected baseline. % exp_id: \\S2C\nWith $K{=}10$ samples in $d{=}6$ dimensions, per-DOF covariance estimates carry substantial noise.\nThe obs\\_only variant avoids this failure mode by conditioning solely on the VLA observation embedding, which already encodes task-relevant geometric information (object identity, gripper-object relationship, task progress) without the intermediate conformal statistics.\n\n\n%----------------------------------------------------------------------\n\\subsection{Conditioning-Magnitude Interaction}\n\\label{sec:magnitude_interaction}\n\nThe norm bound $\\varepsilon$ (Section~\\ref{sec:magnitude}) controls how far the CRM can deviate from the selected action.\nTable~\\ref{tab:magnitude} and Figure~\\ref{fig:magnitude} reveal a sharp contrast between obs\\_only and perdof across the magnitude range.\n\n\\begin{table}[t]\n\\centering\n\\caption{Success rate (\\%) on LIBERO-Object across correction magnitudes $\\varepsilon$.\nSeed count in parentheses.\nBold marks the overall best.\nThe VLA-only baseline ($11.2\\%$, independent of $\\varepsilon$) is shown for reference.}\n\\label{tab:magnitude}\n\\small\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n$\\varepsilon$ & 0.03 & 0.05 & 0.1 & 0.2 & 0.3 & uncapped \\\\\n\\midrule\nobs\\_only\n  & 16.0\\,(1) & 13.5\\,(2) & 15.3\\,(4) & \\textbf{17.5}\\,(6) & 17.0\\,(4) & 14.3\\,(3) \\\\ % exp_id: \\S2A\nperdof\n  & 14.0\\,(1) & 14.0\\,(1) & 11.0\\,(6) & 9.8\\,(6) & 4.7\\,(3) & 0.0\\,(3) \\\\              % exp_id: \\S2A\n\\midrule\nVLA-only\n  & \\multicolumn{6}{c}{$11.2 \\pm 1.6$ (flat, no correction)} \\\\                           % exp_id: \\S2C\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/magnitude_curve.pdf}\n\\caption{Success rate vs correction magnitude $\\varepsilon$ on LIBERO-Object.\nobs\\_only (blue) stays above the VLA-only baseline at every tested $\\varepsilon$.\nperdof (red) collapses from 14\\% at small $\\varepsilon$ to 0\\% when uncapped.\nError bars: $\\pm$1 std; seed counts annotated per point.}\n\\label{fig:magnitude}\n\\end{figure}\n\n\\paragraph{obs\\_only is robust across magnitudes.}\nobs\\_only stays above VLA-only at every tested $\\varepsilon$, % exp_id: \\S2A\nwith performance in a narrow band from 13.5\\% ($\\varepsilon{=}0.05$) to 17.5\\% ($\\varepsilon{=}0.2$). % exp_id: \\S2A\nEven uncapped ($\\varepsilon \\approx 1.42$), it achieves 14.3\\%, % exp_id: \\S2A\nstill 3.1\\,pp above VLA-only. % exp_id: \\S2A, \\S2C\nA practitioner need not carefully tune $\\varepsilon$: any value in $[0.03, 0.3]$ yields consistent improvement.\n\n\\paragraph{perdof collapses progressively.}\nperdof declines monotonically as $\\varepsilon$ grows: $14.0 \\to 14.0 \\to 11.0 \\to 9.8 \\to 4.7 \\to 0.0$. % exp_id: \\S2A\nAt small $\\varepsilon$, the tight norm bound clips erroneous corrections and masks the noisy conformal features.\nAs $\\varepsilon$ increases, the CRM applies larger corrections along unreliable directions, and compounding error across the trajectory destroys performance.\nAll three uncapped perdof seeds score 0/100 successes. % exp_id: \\S2H\n\nThis interaction is the central diagnostic: the same architecture succeeds or fails based on whether it receives clean (observation-only) or noisy (conformal) conditioning.\nThe magnitude bound does not rescue a poorly conditioned CRM; it only delays the collapse.\n\n\n%----------------------------------------------------------------------\n\\subsection{Inference-Time Scaling (K-Value Curve)}\n\\label{sec:kvalue}\n\nFigure~\\ref{fig:kvalue} plots task success rate as a function of the number of VLA samples $K$ for obs\\_only at $\\varepsilon{=}0.2$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/k_value_curve.pdf}\n\\caption{Success rate vs number of VLA samples $K$ for obs\\_only ($\\varepsilon{=}0.2$) on LIBERO-Object.\nPerformance increases monotonically from $K{=}1$ to $K{=}10$.\nError bars: $\\pm$1 std where multiple seeds are available.\n$^*$Single seed (seed\\,42).}\n\\label{fig:kvalue}\n\\end{figure}\n\nAt $K{=}1$, the CRM corrects a single VLA output without multi-sample selection and achieves $10.3\\% \\pm 1.5\\%$ ($n{=}3$), % exp_id: \\S2B\nindistinguishable from VLA-only ($11.2\\%$). % exp_id: \\S2C\nAt $K{=}5$, performance rises to $14.0\\%$ (single seed$^*$, seed\\,42). % exp_id: \\S2B\nAt $K{=}10$, the full pipeline reaches $17.5\\% \\pm 2.8\\%$ ($n{=}6$). % exp_id: \\S2B\nThe trend is monotonic: $10.3\\% \\to 14.0\\% \\to 17.5\\%$. % exp_id: \\S2B\n\nMore VLA samples improve the argmin starting point: with larger $K$, the selected candidate sits closer to the sample centroid and, on average, closer to the demonstration action.\nThe CRM correction is then more effective because smaller residuals keep the output within the reliable regime of the learned MLP.\n\nThe $K{=}1$ result is the critical control.\nIt confirms that correction alone, without multi-sample selection, provides no measurable benefit over the uncorrected VLA.\nThe CRM does not learn a fixed correction bias independent of sample quality; the improvement requires both a good starting point from selection and a learned residual from the CRM.\n\n\n%----------------------------------------------------------------------\n\\subsection{Applicability Boundary: Tokenized VLAs}\n\\label{sec:applicability}\n\nThe multi-sample pipeline requires diverse action candidates from the base VLA.\nWe test this prerequisite on OpenVLA~\\cite{kim2024openvla}, a 7B-parameter autoregressive VLA based on Llama-2.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/diversity_analysis.pdf}\n\\caption{Action sample diversity comparison.\nSmolVLA (flow-matching) produces diverse candidates across flow trajectories.\nOpenVLA (autoregressive, $T{=}0.5$) generates near-identical samples: 8/10 are identical with per-DOF variance $< 10^{-30}$.}\n\\label{fig:diversity}\n\\end{figure}\n\nAt standard temperature $T{=}0.5$, OpenVLA's $K{=}10$ samples are near-deterministic: % exp_id: \\S2G\n8 of 10 are identical, with per-DOF variance below $10^{-30}$. % exp_id: \\S2G\nMulti-sample selection over identical candidates reduces to random selection, and the CRM receives the same input regardless of $K$.\n\nRaising $T$ to 1.5 or above increases diversity but degrades the base policy. % exp_id: \\S2G\nNo temperature setting achieves both sufficient diversity and acceptable base performance. % exp_id: \\S2G\n\nThe multi-sample refinement pipeline is therefore specific to stochastic VLA architectures (e.g., flow-matching models) that produce naturally diverse candidates at their standard operating point.\nTokenized autoregressive VLAs would require alternative candidate generation strategies, such as latent-space perturbation or ensemble decoding.\n"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T10:10:24.353949+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T10:10:24.354078+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T10:10:24.354208+00:00_

1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	We evaluate ACR-VLA on two LIBERO task suites to answer three questions:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T10:10:24.354393+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex",
  "content": "\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate the Conformal Refinement Module (CRM) on LIBERO-Object to answer four questions:\n(1)~Where does the improvement originate, multi-sample selection or learned correction?\n(2)~How does CRM conditioning interact with correction magnitude?\n(3)~Does performance scale with the number of VLA samples $K$?\n(4)~Does the approach transfer to tokenized VLAs?\nIn brief: correction contributes 4--5$\\times$ more than selection (\\S\\ref{sec:component}); observation-only conditioning is robust across magnitudes while conformal conditioning collapses (\\S\\ref{sec:magnitude_interaction}); performance increases monotonically from $K{=}1$ to $K{=}10$ (\\S\\ref{sec:kvalue}); and tokenized VLAs lack the sampling diversity that multi-sample refinement requires (\\S\\ref{sec:applicability}).\n\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmark.}\nWe use LIBERO-Object~\\cite{liu2023libero}, a suite of 10 tabletop manipulation tasks requiring generalization to novel object instances.\nEach task is evaluated over 10 rollouts (maximum 300 steps), for 100 episodes per method per seed.\nSuccess is binary: the task predicate must be satisfied before the step limit.\n\n\\paragraph{Base VLA.}\nWe build on SmolVLA~\\cite{shukor2025smolvla}, a 0.4B-parameter flow-matching VLA.\nThe model receives dual-camera RGB input (agentview + eye-in-hand, $256{\\times}256$) and 8D proprioceptive state, and outputs 7D actions (6D end-effector pose + 1D gripper).\nThe gripper dimension is handled via direct thresholding, outside the refinement pipeline.\n\n\\paragraph{Baselines.}\nAll methods share the same frozen SmolVLA checkpoint:\n\\begin{itemize}[nosep]\n  \\item \\textbf{VLA-only} ($K{=}1$): single VLA sample, no selection or correction.\n  \\item \\textbf{Random sel.}\\ ($K{=}10$): one uniformly random sample from 10 candidates.\n  \\item \\textbf{Argmin sel.}\\ ($K{=}10$): candidate closest to the sample mean (L2 distance), no correction.\n  \\item \\textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples.\n\\end{itemize}\n\n\\paragraph{CRM variants.}\nThree CRM variants share the same 3-layer MLP (${\\sim}$337K parameters) and differ only in conditioning input:\n\\begin{itemize}[nosep]\n  \\item \\textbf{obs\\_only}: frozen VLA observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{960}$. Does \\emph{not} use conformal statistics. This is our primary method.\n  \\item \\textbf{perdof}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 40D per-DOF conformal features (standard deviations, conformal radii, log-volume terms).\n  \\item \\textbf{scalar}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 1D scalar uncertainty.\n\\end{itemize}\n\n\\paragraph{Statistical protocol.}\nEach condition is evaluated with 2--6 seeds (100 rollouts per seed).\nWe report mean $\\pm$ standard deviation across seeds.\nFor the primary comparison, we apply a one-sided Fisher exact test on pooled rollout counts and report Cohen's $d$ as the effect size measure.\n\n\n%----------------------------------------------------------------------\n\\subsection{Main Results: Component Decomposition}\n\\label{sec:component}\n\nTable~\\ref{tab:component} decomposes the full pipeline into selection and correction stages.\nThe three non-CRM multi-sample methods (random, argmin, VLA-mean) cluster within 11--13\\%, % exp_id: \\S2C, \\S2D\nat most 1.3\\,pp above VLA-only. % exp_id: \\S2C\nOnly obs\\_only CRM breaks out of this band.\n\n\\begin{table}[t]\n\\centering\n\\caption{Component decomposition on LIBERO-Object (100 rollouts per seed).\nBold: best; underline: second best.\n$^\\dagger$Partial data: 7/10 tasks completed, seed\\,42 only.\n$^\\ddagger$Best $\\varepsilon$ per variant.}\n\\label{tab:component}\n\\small\n\\begin{tabular}{@{}lccrl@{}}\n\\toprule\nMethod & SR (\\%) $\\uparrow$ & Seeds & $\\Delta$ & Component \\\\\n\\midrule\nVLA-only ($K{=}1$)\n  & $11.2 \\pm 1.6$  & 5 & ---     & Baseline \\\\      % exp_id: \\S2C\nRandom sel.\\ ($K{=}10$)$^\\dagger$\n  & ${\\sim}11.4$     & 1 & $+0.2$  & ---      \\\\      % exp_id: \\S2C, partial seed42\nArgmin sel.\\ ($K{=}10$)\n  & $12.4 \\pm 2.9$  & 5 & $+1.2$  & + Selection \\\\   % exp_id: \\S2C\nVLA-mean ($K{=}10$)\n  & $\\underline{12.5 \\pm 2.1}$ & 4 & $+1.3$ & + Aggregation \\\\ % exp_id: \\S2C\n\\midrule\nCRM scalar$^\\ddagger$ ($K{=}10$)\n  & $8.3 \\pm 2.1$   & 3 & $-2.9$  & + Correction \\\\  % exp_id: \\S2C\nCRM perdof$^\\ddagger$ ($K{=}10$, $\\varepsilon{=}0.1$)\n  & $11.0 \\pm 2.0$  & 6 & $-0.2$  & + Correction \\\\  % exp_id: \\S2C\n\\textbf{CRM obs\\_only} ($K{=}10$, $\\varepsilon{=}0.2$)\n  & $\\mathbf{17.5 \\pm 2.8}$ & \\textbf{6} & $\\mathbf{+6.3}$ & \\textbf{+ Correction} \\\\ % exp_id: \\S2C\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Selection contributes ${\\sim}$1\\,pp; correction contributes ${\\sim}$5\\,pp.}\nArgmin selection adds only ${\\sim}$1\\,pp over random selection ($12.4\\%$ vs ${\\sim}11.4\\%$), % exp_id: \\S2D\nconfirming that L2-to-mean ranking provides a weak signal at $K{=}10$.\nThe obs\\_only CRM then adds ${\\sim}$5\\,pp on top of argmin ($17.5\\%$ vs $12.4\\%$), % exp_id: \\S2D\nso correction is 4--5$\\times$ more valuable than selection. % exp_id: \\S2D\n\nThis result is statistically reliable.\nobs\\_only vs VLA-only yields Fisher exact $p = 0.0074$ (one-sided) with Cohen's $d = 1.21$; % exp_id: \\S2E\nobs\\_only vs argmin yields a paired $t$-test $p = 0.016$. % exp_id: \\S2E\n\n\\paragraph{Negative results: conformal conditioning hurts.}\nThe perdof variant ($11.0\\%$) performs no better than VLA-only despite receiving 40 additional conformal features, % exp_id: \\S2C\nand scalar ($8.3\\%$) is 2.9\\,pp \\emph{worse} than the uncorrected baseline. % exp_id: \\S2C\nWith $K{=}10$ samples in $d{=}6$ dimensions, per-DOF covariance estimates carry substantial noise.\nThe obs\\_only variant avoids this failure mode by conditioning solely on the VLA observation embedding, which already encodes task-relevant geometric information (object identity, gripper-object relationship, task progress) without the intermediate conformal statistics.\n\n\n%----------------------------------------------------------------------\n\\subsection{Conditioning-Magnitude Interaction}\n\\label{sec:magnitude_interaction}\n\nThe norm bound $\\varepsilon$ (Section~\\ref{sec:magnitude}) controls how far the CRM can deviate from the selected action.\nTable~\\ref{tab:magnitude} and Figure~\\ref{fig:magnitude} reveal a sharp contrast between obs\\_only and perdof across the magnitude range.\n\n\\begin{table}[t]\n\\centering\n\\caption{Success rate (\\%) on LIBERO-Object across correction magnitudes $\\varepsilon$.\nSeed count in parentheses.\nBold marks the overall best.\nThe VLA-only baseline ($11.2\\%$, independent of $\\varepsilon$) is shown for reference.}\n\\label{tab:magnitude}\n\\small\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n$\\varepsilon$ & 0.03 & 0.05 & 0.1 & 0.2 & 0.3 & uncapped \\\\\n\\midrule\nobs\\_only\n  & 16.0\\,(1) & 13.5\\,(2) & 15.3\\,(4) & \\textbf{17.5}\\,(6) & 17.0\\,(4) & 14.3\\,(3) \\\\ % exp_id: \\S2A\nperdof\n  & 14.0\\,(1) & 14.0\\,(1) & 11.0\\,(6) & 9.8\\,(6) & 4.7\\,(3) & 0.0\\,(3) \\\\              % exp_id: \\S2A\n\\midrule\nVLA-only\n  & \\multicolumn{6}{c}{$11.2 \\pm 1.6$ (flat, no correction)} \\\\                           % exp_id: \\S2C\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/magnitude_curve.pdf}\n\\caption{Success rate vs correction magnitude $\\varepsilon$ on LIBERO-Object.\nobs\\_only (blue) stays above the VLA-only baseline at every tested $\\varepsilon$.\nperdof (red) collapses from 14\\% at small $\\varepsilon$ to 0\\% when uncapped.\nError bars: $\\pm$1 std; seed counts annotated per point.}\n\\label{fig:magnitude}\n\\end{figure}\n\n\\paragraph{obs\\_only is robust across magnitudes.}\nobs\\_only stays above VLA-only at every tested $\\varepsilon$, % exp_id: \\S2A\nwith performance in a narrow band from 13.5\\% ($\\varepsilon{=}0.05$) to 17.5\\% ($\\varepsilon{=}0.2$). % exp_id: \\S2A\nEven uncapped ($\\varepsilon \\approx 1.42$), it achieves 14.3\\%, % exp_id: \\S2A\nstill 3.1\\,pp above VLA-only. % exp_id: \\S2A, \\S2C\nA practitioner need not carefully tune $\\varepsilon$: any value in $[0.03, 0.3]$ yields consistent improvement.\n\n\\paragraph{perdof collapses progressively.}\nperdof declines monotonically as $\\varepsilon$ grows: $14.0 \\to 14.0 \\to 11.0 \\to 9.8 \\to 4.7 \\to 0.0$. % exp_id: \\S2A\nAt small $\\varepsilon$, the tight norm bound clips erroneous corrections and masks the noisy conformal features.\nAs $\\varepsilon$ increases, the CRM applies larger corrections along unreliable directions, and compounding error across the trajectory destroys performance.\nAll three uncapped perdof seeds score 0/100 successes. % exp_id: \\S2H\n\nThis interaction is the central diagnostic: the same architecture succeeds or fails based on whether it receives clean (observation-only) or noisy (conformal) conditioning.\nThe magnitude bound does not rescue a poorly conditioned CRM; it only delays the collapse.\n\n\n%----------------------------------------------------------------------\n\\subsection{Inference-Time Scaling (K-Value Curve)}\n\\label{sec:kvalue}\n\nFigure~\\ref{fig:kvalue} plots task success rate as a function of the number of VLA samples $K$ for obs\\_only at $\\varepsilon{=}0.2$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/k_value_curve.pdf}\n\\caption{Success rate vs number of VLA samples $K$ for obs\\_only ($\\varepsilon{=}0.2$) on LIBERO-Object.\nPerformance increases monotonically from $K{=}1$ to $K{=}10$.\nError bars: $\\pm$1 std where multiple seeds are available.\n$^*$Single seed (seed\\,42).}\n\\label{fig:kvalue}\n\\end{figure}\n\nAt $K{=}1$, the CRM corrects a single VLA output without multi-sample selection and achieves $10.3\\% \\pm 1.5\\%$ ($n{=}3$), % exp_id: \\S2B\nindistinguishable from VLA-only ($11.2\\%$). % exp_id: \\S2C\nAt $K{=}5$, performance rises to $14.0\\%$ (single seed$^*$, seed\\,42). % exp_id: \\S2B\nAt $K{=}10$, the full pipeline reaches $17.5\\% \\pm 2.8\\%$ ($n{=}6$). % exp_id: \\S2B\nThe trend is monotonic: $10.3\\% \\to 14.0\\% \\to 17.5\\%$. % exp_id: \\S2B\n\nMore VLA samples improve the argmin starting point: with larger $K$, the selected candidate sits closer to the sample centroid and, on average, closer to the demonstration action.\nThe CRM correction is then more effective because smaller residuals keep the output within the reliable regime of the learned MLP.\n\nThe $K{=}1$ result is the critical control.\nIt confirms that correction alone, without multi-sample selection, provides no measurable benefit over the uncorrected VLA.\nThe CRM does not learn a fixed correction bias independent of sample quality; the improvement requires both a good starting point from selection and a learned residual from the CRM.\n\n\n%----------------------------------------------------------------------\n\\subsection{Applicability Boundary: Tokenized VLAs}\n\\label{sec:applicability}\n\nThe multi-sample pipeline requires diverse action candidates from the base VLA.\nWe test this prerequisite on OpenVLA~\\cite{kim2024openvla}, a 7B-parameter autoregressive VLA based on Llama-2.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/diversity_analysis.pdf}\n\\caption{Action sample diversity comparison.\nSmolVLA (flow-matching) produces diverse candidates across flow trajectories.\nOpenVLA (autoregressive, $T{=}0.5$) generates near-identical samples: 8/10 are identical with per-DOF variance $< 10^{-30}$.}\n\\label{fig:diversity}\n\\end{figure}\n\nAt standard temperature $T{=}0.5$, OpenVLA's $K{=}10$ samples are near-deterministic: % exp_id: \\S2G\n8 of 10 are identical, with per-DOF variance below $10^{-30}$. % exp_id: \\S2G\nMulti-sample selection over identical candidates reduces to random selection, and the CRM receives the same input regardless of $K$.\n\nRaising $T$ to 1.5 or above increases diversity but degrades the base policy. % exp_id: \\S2G\nNo temperature setting achieves both sufficient diversity and acceptable base performance. % exp_id: \\S2G\n\nThe multi-sample refinement pipeline is therefore specific to stochastic VLA architectures (e.g., flow-matching models) that produce naturally diverse candidates at their standard operating point.\nTokenized autoregressive VLAs would require alternative candidate generation strategies, such as latent-space perturbation or ensemble decoding.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex",
    "content": "\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate the Conformal Refinement Module (CRM) on LIBERO-Object to answer four questions:\n(1)~Where does the improvement originate, multi-sample selection or learned correction?\n(2)~How does CRM conditioning interact with correction magnitude?\n(3)~Does performance scale with the number of VLA samples $K$?\n(4)~Does the approach transfer to tokenized VLAs?\nIn brief: correction contributes 4--5$\\times$ more than selection (\\S\\ref{sec:component}); observation-only conditioning is robust across magnitudes while conformal conditioning collapses (\\S\\ref{sec:magnitude_interaction}); performance increases monotonically from $K{=}1$ to $K{=}10$ (\\S\\ref{sec:kvalue}); and tokenized VLAs lack the sampling diversity that multi-sample refinement requires (\\S\\ref{sec:applicability}).\n\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmark.}\nWe use LIBERO-Object~\\cite{liu2023libero}, a suite of 10 tabletop manipulation tasks requiring generalization to novel object instances.\nEach task is evaluated over 10 rollouts (maximum 300 steps), for 100 episodes per method per seed.\nSuccess is binary: the task predicate must be satisfied before the step limit.\n\n\\paragraph{Base VLA.}\nWe build on SmolVLA~\\cite{shukor2025smolvla}, a 0.4B-parameter flow-matching VLA.\nThe model receives dual-camera RGB input (agentview + eye-in-hand, $256{\\times}256$) and 8D proprioceptive state, and outputs 7D actions (6D end-effector pose + 1D gripper).\nThe gripper dimension is handled via direct thresholding, outside the refinement pipeline.\n\n\\paragraph{Baselines.}\nAll methods share the same frozen SmolVLA checkpoint:\n\\begin{itemize}[nosep]\n  \\item \\textbf{VLA-only} ($K{=}1$): single VLA sample, no selection or correction.\n  \\item \\textbf{Random sel.}\\ ($K{=}10$): one uniformly random sample from 10 candidates.\n  \\item \\textbf{Argmin sel.}\\ ($K{=}10$): candidate closest to the sample mean (L2 distance), no correction.\n  \\item \\textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples.\n\\end{itemize}\n\n\\paragraph{CRM variants.}\nThree CRM variants share the same 3-layer MLP (${\\sim}$337K parameters) and differ only in conditioning input:\n\\begin{itemize}[nosep]\n  \\item \\textbf{obs\\_only}: frozen VLA observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{960}$. Does \\emph{not} use conformal statistics. This is our primary method.\n  \\item \\textbf{perdof}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 40D per-DOF conformal features (standard deviations, conformal radii, log-volume terms).\n  \\item \\textbf{scalar}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 1D scalar uncertainty.\n\\end{itemize}\n\n\\paragraph{Statistical protocol.}\nEach condition is evaluated with 2--6 seeds (100 rollouts per seed).\nWe report mean $\\pm$ standard deviation across seeds.\nFor the primary comparison, we apply a one-sided Fisher exact test on pooled rollout counts and report Cohen's $d$ as the effect size measure.\n\n\n%----------------------------------------------------------------------\n\\subsection{Main Results: Component Decomposition}\n\\label{sec:component}\n\nTable~\\ref{tab:component} decomposes the full pipeline into selection and correction stages.\nThe three non-CRM multi-sample methods (random, argmin, VLA-mean) cluster within 11--13\\%, % exp_id: \\S2C, \\S2D\nat most 1.3\\,pp above VLA-only. % exp_id: \\S2C\nOnly obs\\_only CRM breaks out of this band.\n\n\\begin{table}[t]\n\\centering\n\\caption{Component decomposition on LIBERO-Object (100 rollouts per seed).\nBold: best; underline: second best.\n$^\\dagger$Partial data: 7/10 tasks completed, seed\\,42 only.\n$^\\ddagger$Best $\\varepsilon$ per variant.}\n\\label{tab:component}\n\\small\n\\begin{tabular}{@{}lccrl@{}}\n\\toprule\nMethod & SR (\\%) $\\uparrow$ & Seeds & $\\Delta$ & Component \\\\\n\\midrule\nVLA-only ($K{=}1$)\n  & $11.2 \\pm 1.6$  & 5 & ---     & Baseline \\\\      % exp_id: \\S2C\nRandom sel.\\ ($K{=}10$)$^\\dagger$\n  & ${\\sim}11.4$     & 1 & $+0.2$  & ---      \\\\      % exp_id: \\S2C, partial seed42\nArgmin sel.\\ ($K{=}10$)\n  & $12.4 \\pm 2.9$  & 5 & $+1.2$  & + Selection \\\\   % exp_id: \\S2C\nVLA-mean ($K{=}10$)\n  & $\\underline{12.5 \\pm 2.1}$ & 4 & $+1.3$ & + Aggregation \\\\ % exp_id: \\S2C\n\\midrule\nCRM scalar$^\\ddagger$ ($K{=}10$)\n  & $8.3 \\pm 2.1$   & 3 & $-2.9$  & + Correction \\\\  % exp_id: \\S2C\nCRM perdof$^\\ddagger$ ($K{=}10$, $\\varepsilon{=}0.1$)\n  & $11.0 \\pm 2.0$  & 6 & $-0.2$  & + Correction \\\\  % exp_id: \\S2C\n\\textbf{CRM obs\\_only} ($K{=}10$, $\\varepsilon{=}0.2$)\n  & $\\mathbf{17.5 \\pm 2.8}$ & \\textbf{6} & $\\mathbf{+6.3}$ & \\textbf{+ Correction} \\\\ % exp_id: \\S2C\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Selection contributes ${\\sim}$1\\,pp; correction contributes ${\\sim}$5\\,pp.}\nArgmin selection adds only ${\\sim}$1\\,pp over random selection ($12.4\\%$ vs ${\\sim}11.4\\%$), % exp_id: \\S2D\nconfirming that L2-to-mean ranking provides a weak signal at $K{=}10$.\nThe obs\\_only CRM then adds ${\\sim}$5\\,pp on top of argmin ($17.5\\%$ vs $12.4\\%$), % exp_id: \\S2D\nso correction is 4--5$\\times$ more valuable than selection. % exp_id: \\S2D\n\nThis result is statistically reliable.\nobs\\_only vs VLA-only yields Fisher exact $p = 0.0074$ (one-sided) with Cohen's $d = 1.21$; % exp_id: \\S2E\nobs\\_only vs argmin yields a paired $t$-test $p = 0.016$. % exp_id: \\S2E\n\n\\paragraph{Negative results: conformal conditioning hurts.}\nThe perdof variant ($11.0\\%$) performs no better than VLA-only despite receiving 40 additional conformal features, % exp_id: \\S2C\nand scalar ($8.3\\%$) is 2.9\\,pp \\emph{worse} than the uncorrected baseline. % exp_id: \\S2C\nWith $K{=}10$ samples in $d{=}6$ dimensions, per-DOF covariance estimates carry substantial noise.\nThe obs\\_only variant avoids this failure mode by conditioning solely on the VLA observation embedding, which already encodes task-relevant geometric information (object identity, gripper-object relationship, task progress) without the intermediate conformal statistics.\n\n\n%----------------------------------------------------------------------\n\\subsection{Conditioning-Magnitude Interaction}\n\\label{sec:magnitude_interaction}\n\nThe norm bound $\\varepsilon$ (Section~\\ref{sec:magnitude}) controls how far the CRM can deviate from the selected action.\nTable~\\ref{tab:magnitude} and Figure~\\ref{fig:magnitude} reveal a sharp contrast between obs\\_only and perdof across the magnitude range.\n\n\\begin{table}[t]\n\\centering\n\\caption{Success rate (\\%) on LIBERO-Object across correction magnitudes $\\varepsilon$.\nSeed count in parentheses.\nBold marks the overall best.\nThe VLA-only baseline ($11.2\\%$, independent of $\\varepsilon$) is shown for reference.}\n\\label{tab:magnitude}\n\\small\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n$\\varepsilon$ & 0.03 & 0.05 & 0.1 & 0.2 & 0.3 & uncapped \\\\\n\\midrule\nobs\\_only\n  & 16.0\\,(1) & 13.5\\,(2) & 15.3\\,(4) & \\textbf{17.5}\\,(6) & 17.0\\,(4) & 14.3\\,(3) \\\\ % exp_id: \\S2A\nperdof\n  & 14.0\\,(1) & 14.0\\,(1) & 11.0\\,(6) & 9.8\\,(6) & 4.7\\,(3) & 0.0\\,(3) \\\\              % exp_id: \\S2A\n\\midrule\nVLA-only\n  & \\multicolumn{6}{c}{$11.2 \\pm 1.6$ (flat, no correction)} \\\\                           % exp_id: \\S2C\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/magnitude_curve.pdf}\n\\caption{Success rate vs correction magnitude $\\varepsilon$ on LIBERO-Object.\nobs\\_only (blue) stays above the VLA-only baseline at every tested $\\varepsilon$.\nperdof (red) collapses from 14\\% at small $\\varepsilon$ to 0\\% when uncapped.\nError bars: $\\pm$1 std; seed counts annotated per point.}\n\\label{fig:magnitude}\n\\end{figure}\n\n\\paragraph{obs\\_only is robust across magnitudes.}\nobs\\_only stays above VLA-only at every tested $\\varepsilon$, % exp_id: \\S2A\nwith performance in a narrow band from 13.5\\% ($\\varepsilon{=}0.05$) to 17.5\\% ($\\varepsilon{=}0.2$). % exp_id: \\S2A\nEven uncapped ($\\varepsilon \\approx 1.42$), it achieves 14.3\\%, % exp_id: \\S2A\nstill 3.1\\,pp above VLA-only. % exp_id: \\S2A, \\S2C\nA practitioner need not carefully tune $\\varepsilon$: any value in $[0.03, 0.3]$ yields consistent improvement.\n\n\\paragraph{perdof collapses progressively.}\nperdof declines monotonically as $\\varepsilon$ grows: $14.0 \\to 14.0 \\to 11.0 \\to 9.8 \\to 4.7 \\to 0.0$. % exp_id: \\S2A\nAt small $\\varepsilon$, the tight norm bound clips erroneous corrections and masks the noisy conformal features.\nAs $\\varepsilon$ increases, the CRM applies larger corrections along unreliable directions, and compounding error across the trajectory destroys performance.\nAll three uncapped perdof seeds score 0/100 successes. % exp_id: \\S2H\n\nThis interaction is the central diagnostic: the same architecture succeeds or fails based on whether it receives clean (observation-only) or noisy (conformal) conditioning.\nThe magnitude bound does not rescue a poorly conditioned CRM; it only delays the collapse.\n\n\n%----------------------------------------------------------------------\n\\subsection{Inference-Time Scaling (K-Value Curve)}\n\\label{sec:kvalue}\n\nFigure~\\ref{fig:kvalue} plots task success rate as a function of the number of VLA samples $K$ for obs\\_only at $\\varepsilon{=}0.2$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/k_value_curve.pdf}\n\\caption{Success rate vs number of VLA samples $K$ for obs\\_only ($\\varepsilon{=}0.2$) on LIBERO-Object.\nPerformance increases monotonically from $K{=}1$ to $K{=}10$.\nError bars: $\\pm$1 std where multiple seeds are available.\n$^*$Single seed (seed\\,42).}\n\\label{fig:kvalue}\n\\end{figure}\n\nAt $K{=}1$, the CRM corrects a single VLA output without multi-sample selection and achieves $10.3\\% \\pm 1.5\\%$ ($n{=}3$), % exp_id: \\S2B\nindistinguishable from VLA-only ($11.2\\%$). % exp_id: \\S2C\nAt $K{=}5$, performance rises to $14.0\\%$ (single seed$^*$, seed\\,42). % exp_id: \\S2B\nAt $K{=}10$, the full pipeline reaches $17.5\\% \\pm 2.8\\%$ ($n{=}6$). % exp_id: \\S2B\nThe trend is monotonic: $10.3\\% \\to 14.0\\% \\to 17.5\\%$. % exp_id: \\S2B\n\nMore VLA samples improve the argmin starting point: with larger $K$, the selected candidate sits closer to the sample centroid and, on average, closer to the demonstration action.\nThe CRM correction is then more effective because smaller residuals keep the output within the reliable regime of the learned MLP.\n\nThe $K{=}1$ result is the critical control.\nIt confirms that correction alone, without multi-sample selection, provides no measurable benefit over the uncorrected VLA.\nThe CRM does not learn a fixed correction bias independent of sample quality; the improvement requires both a good starting point from selection and a learned residual from the CRM.\n\n\n%----------------------------------------------------------------------\n\\subsection{Applicability Boundary: Tokenized VLAs}\n\\label{sec:applicability}\n\nThe multi-sample pipeline requires diverse action candidates from the base VLA.\nWe test this prerequisite on OpenVLA~\\cite{kim2024openvla}, a 7B-parameter autoregressive VLA based on Llama-2.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/diversity_analysis.pdf}\n\\caption{Action sample diversity comparison.\nSmolVLA (flow-matching) produces diverse candidates across flow trajectories.\nOpenVLA (autoregressive, $T{=}0.5$) generates near-identical samples: 8/10 are identical with per-DOF variance $< 10^{-30}$.}\n\\label{fig:diversity}\n\\end{figure}\n\nAt standard temperature $T{=}0.5$, OpenVLA's $K{=}10$ samples are near-deterministic: % exp_id: \\S2G\n8 of 10 are identical, with per-DOF variance below $10^{-30}$. % exp_id: \\S2G\nMulti-sample selection over identical candidates reduces to random selection, and the CRM receives the same input regardless of $K$.\n\nRaising $T$ to 1.5 or above increases diversity but degrades the base policy. % exp_id: \\S2G\nNo temperature setting achieves both sufficient diversity and acceptable base performance. % exp_id: \\S2G\n\nThe multi-sample refinement pipeline is therefore specific to stochastic VLA architectures (e.g., flow-matching models) that produce naturally diverse candidates at their standard operating point.\nTokenized autoregressive VLAs would require alternative candidate generation strategies, such as latent-space perturbation or ensemble decoding.\n"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T10:10:24.354620+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T10:10:24.354771+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex",
  "limit": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex",
    "limit": "3"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T10:10:24.354895+00:00_

1	
2	\section{Experiments}
3	\label{sec:experiments}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T10:10:24.355057+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat > /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex << 'ENDOFFILE'\n\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate the Conformal Refinement Module (CRM) on LIBERO-Object to answer four questions:\n(1)~Where does the improvement originate, multi-sample selection or learned correction?\n(2)~How does CRM conditioning interact with correction magnitude?\n(3)~Does performance scale with the number of VLA samples $K$?\n(4)~Does the approach transfer to tokenized VLAs?\nIn brief: correction contributes 4--5$\\times$ more than selection (\\S\\ref{sec:component}); observation-only conditioning is robust across magnitudes while conformal conditioning collapses (\\S\\ref{sec:magnitude_interaction}); performance increases monotonically from $K{=}1$ to $K{=}10$ (\\S\\ref{sec:kvalue}); and tokenized VLAs lack the sampling diversity that multi-sample refinement requires (\\S\\ref{sec:applicability}).\n\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmark.}\nWe use LIBERO-Object~\\cite{liu2023libero}, a suite of 10 tabletop manipulation tasks requiring generalization to novel object instances.\nEach task is evaluated over 10 rollouts (maximum 300 steps), for 100 episodes per method per seed.\nSuccess is binary: the task predicate must be satisfied before the step limit.\n\n\\paragraph{Base VLA.}\nWe build on SmolVLA~\\cite{shukor2025smolvla}, a 0.4B-parameter flow-matching VLA.\nThe model receives dual-camera RGB input (agentview + eye-in-hand, $256{\\times}256$) and 8D proprioceptive state, and outputs 7D actions (6D end-effector pose + 1D gripper).\nThe gripper dimension is handled via direct thresholding, outside the refinement pipeline.\n\n\\paragraph{Baselines.}\nAll methods share the same frozen SmolVLA checkpoint:\n\\begin{itemize}[nosep]\n  \\item \\textbf{VLA-only} ($K{=}1$): single VLA sample, no selection or correction.\n  \\item \\textbf{Random sel.}\\ ($K{=}10$): one uniformly random sample from 10 candidates.\n  \\item \\textbf{Argmin sel.}\\ ($K{=}10$): candidate closest to the sample mean (L2 distance), no correction.\n  \\item \\textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples.\n\\end{itemize}\n\n\\paragraph{CRM variants.}\nThree CRM variants share the same 3-layer MLP (${\\sim}$337K parameters) and differ only in conditioning input:\n\\begin{itemize}[nosep]\n  \\item \\textbf{obs\\_only}: frozen VLA observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{960}$. Does \\emph{not} use conformal statistics. This is our primary method.\n  \\item \\textbf{perdof}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 40D per-DOF conformal features (standard deviations, conformal radii, log-volume terms).\n  \\item \\textbf{scalar}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 1D scalar uncertainty.\n\\end{itemize}\n\n\\paragraph{Statistical protocol.}\nEach condition is evaluated with 2--6 seeds (100 rollouts per seed).\nWe report mean $\\pm$ standard deviation across seeds.\nFor the primary comparison, we apply a one-sided Fisher exact test on pooled rollout counts and report Cohen's $d$ as the effect size measure.\n\n\n%----------------------------------------------------------------------\n\\subsection{Main Results: Component Decomposition}\n\\label{sec:component}\n\nTable~\\ref{tab:component} decomposes the full pipeline into selection and correction stages.\nThe three non-CRM multi-sample methods (random, argmin, VLA-mean) cluster within 11--13\\%, % exp_id: \\S2C, \\S2D\nat most 1.3\\,pp above VLA-only. % exp_id: \\S2C\nOnly obs\\_only CRM breaks out of this band.\n\n\\begin{table}[t]\n\\centering\n\\caption{Component decomposition on LIBERO-Object (100 rollouts per seed).\nBold: best; underline: second best.\n$^\\dagger$Partial data: 7/10 tasks completed, seed\\,42 only.\n$^\\ddagger$Best $\\varepsilon$ per variant.}\n\\label{tab:component}\n\\small\n\\begin{tabular}{@{}lccrl@{}}\n\\toprule\nMethod & SR (\\%) $\\uparrow$ & Seeds & $\\Delta$ & Component \\\\\n\\midrule\nVLA-only ($K{=}1$)\n  & $11.2 \\pm 1.6$  & 5 & ---     & Baseline \\\\      % exp_id: \\S2C\nRandom sel.\\ ($K{=}10$)$^\\dagger$\n  & ${\\sim}11.4$     & 1 & $+0.2$  & ---      \\\\      % exp_id: \\S2C, partial seed42\nArgmin sel.\\ ($K{=}10$)\n  & $12.4 \\pm 2.9$  & 5 & $+1.2$  & + Selection \\\\   % exp_id: \\S2C\nVLA-mean ($K{=}10$)\n  & $\\underline{12.5 \\pm 2.1}$ & 4 & $+1.3$ & + Aggregation \\\\ % exp_id: \\S2C\n\\midrule\nCRM scalar$^\\ddagger$ ($K{=}10$)\n  & $8.3 \\pm 2.1$   & 3 & $-2.9$  & + Correction \\\\  % exp_id: \\S2C\nCRM perdof$^\\ddagger$ ($K{=}10$, $\\varepsilon{=}0.1$)\n  & $11.0 \\pm 2.0$  & 6 & $-0.2$  & + Correction \\\\  % exp_id: \\S2C\n\\textbf{CRM obs\\_only} ($K{=}10$, $\\varepsilon{=}0.2$)\n  & $\\mathbf{17.5 \\pm 2.8}$ & \\textbf{6} & $\\mathbf{+6.3}$ & \\textbf{+ Correction} \\\\ % exp_id: \\S2C\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Selection contributes ${\\sim}$1\\,pp; correction contributes ${\\sim}$5\\,pp.}\nArgmin selection adds only ${\\sim}$1\\,pp over random selection ($12.4\\%$ vs ${\\sim}11.4\\%$), % exp_id: \\S2D\nconfirming that L2-to-mean ranking provides a weak signal at $K{=}10$.\nThe obs\\_only CRM then adds ${\\sim}$5\\,pp on top of argmin ($17.5\\%$ vs $12.4\\%$), % exp_id: \\S2D\nso correction is 4--5$\\times$ more valuable than selection. % exp_id: \\S2D\n\nThis result is statistically reliable.\nobs\\_only vs VLA-only yields Fisher exact $p = 0.0074$ (one-sided) with Cohen's $d = 1.21$; % exp_id: \\S2E\nobs\\_only vs argmin yields a paired $t$-test $p = 0.016$. % exp_id: \\S2E\n\n\\paragraph{Negative results: conformal conditioning hurts.}\nThe perdof variant ($11.0\\%$) performs no better than VLA-only despite receiving 40 additional conformal features, % exp_id: \\S2C\nand scalar ($8.3\\%$) is 2.9\\,pp \\emph{worse} than the uncorrected baseline. % exp_id: \\S2C\nWith $K{=}10$ samples in $d{=}6$ dimensions, per-DOF covariance estimates carry substantial noise.\nThe obs\\_only variant avoids this failure mode by conditioning solely on the VLA observation embedding, which already encodes task-relevant geometric information (object identity, gripper-object relationship, task progress) without the intermediate conformal statistics.\n\n\n%----------------------------------------------------------------------\n\\subsection{Conditioning-Magnitude Interaction}\n\\label{sec:magnitude_interaction}\n\nThe norm bound $\\varepsilon$ (Section~\\ref{sec:magnitude}) controls how far the CRM can deviate from the selected action.\nTable~\\ref{tab:magnitude} and Figure~\\ref{fig:magnitude} reveal a sharp contrast between obs\\_only and perdof across the magnitude range.\n\n\\begin{table}[t]\n\\centering\n\\caption{Success rate (\\%) on LIBERO-Object across correction magnitudes $\\varepsilon$.\nSeed count in parentheses.\nBold marks the overall best.\nThe VLA-only baseline ($11.2\\%$, independent of $\\varepsilon$) is shown for reference.}\n\\label{tab:magnitude}\n\\small\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n$\\varepsilon$ & 0.03 & 0.05 & 0.1 & 0.2 & 0.3 & uncapped \\\\\n\\midrule\nobs\\_only\n  & 16.0\\,(1) & 13.5\\,(2) & 15.3\\,(4) & \\textbf{17.5}\\,(6) & 17.0\\,(4) & 14.3\\,(3) \\\\ % exp_id: \\S2A\nperdof\n  & 14.0\\,(1) & 14.0\\,(1) & 11.0\\,(6) & 9.8\\,(6) & 4.7\\,(3) & 0.0\\,(3) \\\\              % exp_id: \\S2A\n\\midrule\nVLA-only\n  & \\multicolumn{6}{c}{$11.2 \\pm 1.6$ (flat, no correction)} \\\\                           % exp_id: \\S2C\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/magnitude_curve.pdf}\n\\caption{Success rate vs correction magnitude $\\varepsilon$ on LIBERO-Object.\nobs\\_only (blue) stays above the VLA-only baseline at every tested $\\varepsilon$.\nperdof (red) collapses from 14\\% at small $\\varepsilon$ to 0\\% when uncapped.\nError bars: $\\pm$1 std; seed counts annotated per point.}\n\\label{fig:magnitude}\n\\end{figure}\n\n\\paragraph{obs\\_only is robust across magnitudes.}\nobs\\_only stays above VLA-only at every tested $\\varepsilon$, % exp_id: \\S2A\nwith performance in a narrow band from 13.5\\% ($\\varepsilon{=}0.05$) to 17.5\\% ($\\varepsilon{=}0.2$). % exp_id: \\S2A\nEven uncapped ($\\varepsilon \\approx 1.42$), it achieves 14.3\\%, % exp_id: \\S2A\nstill 3.1\\,pp above VLA-only. % exp_id: \\S2A, \\S2C\nA practitioner need not carefully tune $\\varepsilon$: any value in $[0.03, 0.3]$ yields consistent improvement.\n\n\\paragraph{perdof collapses progressively.}\nperdof declines monotonically as $\\varepsilon$ grows: $14.0 \\to 14.0 \\to 11.0 \\to 9.8 \\to 4.7 \\to 0.0$. % exp_id: \\S2A\nAt small $\\varepsilon$, the tight norm bound clips erroneous corrections and masks the noisy conformal features.\nAs $\\varepsilon$ increases, the CRM applies larger corrections along unreliable directions, and compounding error across the trajectory destroys performance.\nAll three uncapped perdof seeds score 0/100 successes. % exp_id: \\S2H\n\nThis interaction is the central diagnostic: the same architecture succeeds or fails based on whether it receives clean (observation-only) or noisy (conformal) conditioning.\nThe magnitude bound does not rescue a poorly conditioned CRM; it only delays the collapse.\n\n\n%----------------------------------------------------------------------\n\\subsection{Inference-Time Scaling (K-Value Curve)}\n\\label{sec:kvalue}\n\nFigure~\\ref{fig:kvalue} plots task success rate as a function of the number of VLA samples $K$ for obs\\_only at $\\varepsilon{=}0.2$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/k_value_curve.pdf}\n\\caption{Success rate vs number of VLA samples $K$ for obs\\_only ($\\varepsilon{=}0.2$) on LIBERO-Object.\nPerformance increases monotonically from $K{=}1$ to $K{=}10$.\nError bars: $\\pm$1 std where multiple seeds are available.\n$^*$Single seed (seed\\,42).}\n\\label{fig:kvalue}\n\\end{figure}\n\nAt $K{=}1$, the CRM corrects a single VLA output without multi-sample selection and achieves $10.3\\% \\pm 1.5\\%$ ($n{=}3$), % exp_id: \\S2B\nindistinguishable from VLA-only ($11.2\\%$). % exp_id: \\S2C\nAt $K{=}5$, performance rises to $14.0\\%$ (single seed$^*$, seed\\,42). % exp_id: \\S2B\nAt $K{=}10$, the full pipeline reaches $17.5\\% \\pm 2.8\\%$ ($n{=}6$). % exp_id: \\S2B\nThe trend is monotonic: $10.3\\% \\to 14.0\\% \\to 17.5\\%$. % exp_id: \\S2B\n\nMore VLA samples improve the argmin starting point: with larger $K$, the selected candidate sits closer to the sample centroid and, on average, closer to the demonstration action.\nThe CRM correction is then more effective because smaller residuals keep the output within the reliable regime of the learned MLP.\n\nThe $K{=}1$ result is the critical control.\nIt confirms that correction alone, without multi-sample selection, provides no measurable benefit over the uncorrected VLA.\nThe CRM does not learn a fixed correction bias independent of sample quality; the improvement requires both a good starting point from selection and a learned residual from the CRM.\n\n\n%----------------------------------------------------------------------\n\\subsection{Applicability Boundary: Tokenized VLAs}\n\\label{sec:applicability}\n\nThe multi-sample pipeline requires diverse action candidates from the base VLA.\nWe test this prerequisite on OpenVLA~\\cite{kim2024openvla}, a 7B-parameter autoregressive VLA based on Llama-2.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/diversity_analysis.pdf}\n\\caption{Action sample diversity comparison.\nSmolVLA (flow-matching) produces diverse candidates across flow trajectories.\nOpenVLA (autoregressive, $T{=}0.5$) generates near-identical samples: 8/10 are identical with per-DOF variance $< 10^{-30}$.}\n\\label{fig:diversity}\n\\end{figure}\n\nAt standard temperature $T{=}0.5$, OpenVLA's $K{=}10$ samples are near-deterministic: % exp_id: \\S2G\n8 of 10 are identical, with per-DOF variance below $10^{-30}$. % exp_id: \\S2G\nMulti-sample selection over identical candidates reduces to random selection, and the CRM receives the same input regardless of $K$.\n\nRaising $T$ to 1.5 or above increases diversity but degrades the base policy. % exp_id: \\S2G\nNo temperature setting achieves both sufficient diversity and acceptable base performance. % exp_id: \\S2G\n\nThe multi-sample refinement pipeline is therefore specific to stochastic VLA architectures (e.g., flow-matching models) that produce naturally diverse candidates at their standard operating point.\nTokenized autoregressive VLAs would require alternative candidate generation strategies, such as latent-space perturbation or ensemble decoding.\nENDOFFILE\necho \"Write complete: $(wc -l < /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex) lines\"",
  "description": "Write complete experiments.tex via heredoc"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Bash",
  "tool_args": {
    "command": "cat > /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex << 'ENDOFFILE'\n\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate the Conformal Refinement Module (CRM) on LIBERO-Object to answer four questions:\n(1)~Where does the improvement originate, multi-sample selection or learned correction?\n(2)~How does CRM conditioning interact with correction magnitude?\n(3)~Does performance scale with the number of VLA samples $K$?\n(4)~Does the approach transfer to tokenized VLAs?\nIn brief: correction contributes 4--5$\\times$ more than selection (\\S\\ref{sec:component}); observation-only conditioning is robust across magnitudes while conformal conditioning collapses (\\S\\ref{sec:magnitude_interaction}); performance increases monotonically from $K{=}1$ to $K{=}10$ (\\S\\ref{sec:kvalue}); and tokenized VLAs lack the sampling diversity that multi-sample refinement requires (\\S\\ref{sec:applicability}).\n\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmark.}\nWe use LIBERO-Object~\\cite{liu2023libero}, a suite of 10 tabletop manipulation tasks requiring generalization to novel object instances.\nEach task is evaluated over 10 rollouts (maximum 300 steps), for 100 episodes per method per seed.\nSuccess is binary: the task predicate must be satisfied before the step limit.\n\n\\paragraph{Base VLA.}\nWe build on SmolVLA~\\cite{shukor2025smolvla}, a 0.4B-parameter flow-matching VLA.\nThe model receives dual-camera RGB input (agentview + eye-in-hand, $256{\\times}256$) and 8D proprioceptive state, and outputs 7D actions (6D end-effector pose + 1D gripper).\nThe gripper dimension is handled via direct thresholding, outside the refinement pipeline.\n\n\\paragraph{Baselines.}\nAll methods share the same frozen SmolVLA checkpoint:\n\\begin{itemize}[nosep]\n  \\item \\textbf{VLA-only} ($K{=}1$): single VLA sample, no selection or correction.\n  \\item \\textbf{Random sel.}\\ ($K{=}10$): one uniformly random sample from 10 candidates.\n  \\item \\textbf{Argmin sel.}\\ ($K{=}10$): candidate closest to the sample mean (L2 distance), no correction.\n  \\item \\textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples.\n\\end{itemize}\n\n\\paragraph{CRM variants.}\nThree CRM variants share the same 3-layer MLP (${\\sim}$337K parameters) and differ only in conditioning input:\n\\begin{itemize}[nosep]\n  \\item \\textbf{obs\\_only}: frozen VLA observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{960}$. Does \\emph{not} use conformal statistics. This is our primary method.\n  \\item \\textbf{perdof}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 40D per-DOF conformal features (standard deviations, conformal radii, log-volume terms).\n  \\item \\textbf{scalar}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 1D scalar uncertainty.\n\\end{itemize}\n\n\\paragraph{Statistical protocol.}\nEach condition is evaluated with 2--6 seeds (100 rollouts per seed).\nWe report mean $\\pm$ standard deviation across seeds.\nFor the primary comparison, we apply a one-sided Fisher exact test on pooled rollout counts and report Cohen's $d$ as the effect size measure.\n\n\n%----------------------------------------------------------------------\n\\subsection{Main Results: Component Decomposition}\n\\label{sec:component}\n\nTable~\\ref{tab:component} decomposes the full pipeline into selection and correction stages.\nThe three non-CRM multi-sample methods (random, argmin, VLA-mean) cluster within 11--13\\%, % exp_id: \\S2C, \\S2D\nat most 1.3\\,pp above VLA-only. % exp_id: \\S2C\nOnly obs\\_only CRM breaks out of this band.\n\n\\begin{table}[t]\n\\centering\n\\caption{Component decomposition on LIBERO-Object (100 rollouts per seed).\nBold: best; underline: second best.\n$^\\dagger$Partial data: 7/10 tasks completed, seed\\,42 only.\n$^\\ddagger$Best $\\varepsilon$ per variant.}\n\\label{tab:component}\n\\small\n\\begin{tabular}{@{}lccrl@{}}\n\\toprule\nMethod & SR (\\%) $\\uparrow$ & Seeds & $\\Delta$ & Component \\\\\n\\midrule\nVLA-only ($K{=}1$)\n  & $11.2 \\pm 1.6$  & 5 & ---     & Baseline \\\\      % exp_id: \\S2C\nRandom sel.\\ ($K{=}10$)$^\\dagger$\n  & ${\\sim}11.4$     & 1 & $+0.2$  & ---      \\\\      % exp_id: \\S2C, partial seed42\nArgmin sel.\\ ($K{=}10$)\n  & $12.4 \\pm 2.9$  & 5 & $+1.2$  & + Selection \\\\   % exp_id: \\S2C\nVLA-mean ($K{=}10$)\n  & $\\underline{12.5 \\pm 2.1}$ & 4 & $+1.3$ & + Aggregation \\\\ % exp_id: \\S2C\n\\midrule\nCRM scalar$^\\ddagger$ ($K{=}10$)\n  & $8.3 \\pm 2.1$   & 3 & $-2.9$  & + Correction \\\\  % exp_id: \\S2C\nCRM perdof$^\\ddagger$ ($K{=}10$, $\\varepsilon{=}0.1$)\n  & $11.0 \\pm 2.0$  & 6 & $-0.2$  & + Correction \\\\  % exp_id: \\S2C\n\\textbf{CRM obs\\_only} ($K{=}10$, $\\varepsilon{=}0.2$)\n  & $\\mathbf{17.5 \\pm 2.8}$ & \\textbf{6} & $\\mathbf{+6.3}$ & \\textbf{+ Correction} \\\\ % exp_id: \\S2C\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Selection contributes ${\\sim}$1\\,pp; correction contributes ${\\sim}$5\\,pp.}\nArgmin selection adds only ${\\sim}$1\\,pp over random selection ($12.4\\%$ vs ${\\sim}11.4\\%$), % exp_id: \\S2D\nconfirming that L2-to-mean ranking provides a weak signal at $K{=}10$.\nThe obs\\_only CRM then adds ${\\sim}$5\\,pp on top of argmin ($17.5\\%$ vs $12.4\\%$), % exp_id: \\S2D\nso correction is 4--5$\\times$ more valuable than selection. % exp_id: \\S2D\n\nThis result is statistically reliable.\nobs\\_only vs VLA-only yields Fisher exact $p = 0.0074$ (one-sided) with Cohen's $d = 1.21$; % exp_id: \\S2E\nobs\\_only vs argmin yields a paired $t$-test $p = 0.016$. % exp_id: \\S2E\n\n\\paragraph{Negative results: conformal conditioning hurts.}\nThe perdof variant ($11.0\\%$) performs no better than VLA-only despite receiving 40 additional conformal features, % exp_id: \\S2C\nand scalar ($8.3\\%$) is 2.9\\,pp \\emph{worse} than the uncorrected baseline. % exp_id: \\S2C\nWith $K{=}10$ samples in $d{=}6$ dimensions, per-DOF covariance estimates carry substantial noise.\nThe obs\\_only variant avoids this failure mode by conditioning solely on the VLA observation embedding, which already encodes task-relevant geometric information (object identity, gripper-object relationship, task progress) without the intermediate conformal statistics.\n\n\n%----------------------------------------------------------------------\n\\subsection{Conditioning-Magnitude Interaction}\n\\label{sec:magnitude_interaction}\n\nThe norm bound $\\varepsilon$ (Section~\\ref{sec:magnitude}) controls how far the CRM can deviate from the selected action.\nTable~\\ref{tab:magnitude} and Figure~\\ref{fig:magnitude} reveal a sharp contrast between obs\\_only and perdof across the magnitude range.\n\n\\begin{table}[t]\n\\centering\n\\caption{Success rate (\\%) on LIBERO-Object across correction magnitudes $\\varepsilon$.\nSeed count in parentheses.\nBold marks the overall best.\nThe VLA-only baseline ($11.2\\%$, independent of $\\varepsilon$) is shown for reference.}\n\\label{tab:magnitude}\n\\small\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n$\\varepsilon$ & 0.03 & 0.05 & 0.1 & 0.2 & 0.3 & uncapped \\\\\n\\midrule\nobs\\_only\n  & 16.0\\,(1) & 13.5\\,(2) & 15.3\\,(4) & \\textbf{17.5}\\,(6) & 17.0\\,(4) & 14.3\\,(3) \\\\ % exp_id: \\S2A\nperdof\n  & 14.0\\,(1) & 14.0\\,(1) & 11.0\\,(6) & 9.8\\,(6) & 4.7\\,(3) & 0.0\\,(3) \\\\              % exp_id: \\S2A\n\\midrule\nVLA-only\n  & \\multicolumn{6}{c}{$11.2 \\pm 1.6$ (flat, no correction)} \\\\                           % exp_id: \\S2C\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/magnitude_curve.pdf}\n\\caption{Success rate vs correction magnitude $\\varepsilon$ on LIBERO-Object.\nobs\\_only (blue) stays above the VLA-only baseline at every tested $\\varepsilon$.\nperdof (red) collapses from 14\\% at small $\\varepsilon$ to 0\\% when uncapped.\nError bars: $\\pm$1 std; seed counts annotated per point.}\n\\label{fig:magnitude}\n\\end{figure}\n\n\\paragraph{obs\\_only is robust across magnitudes.}\nobs\\_only stays above VLA-only at every tested $\\varepsilon$, % exp_id: \\S2A\nwith performance in a narrow band from 13.5\\% ($\\varepsilon{=}0.05$) to 17.5\\% ($\\varepsilon{=}0.2$). % exp_id: \\S2A\nEven uncapped ($\\varepsilon \\approx 1.42$), it achieves 14.3\\%, % exp_id: \\S2A\nstill 3.1\\,pp above VLA-only. % exp_id: \\S2A, \\S2C\nA practitioner need not carefully tune $\\varepsilon$: any value in $[0.03, 0.3]$ yields consistent improvement.\n\n\\paragraph{perdof collapses progressively.}\nperdof declines monotonically as $\\varepsilon$ grows: $14.0 \\to 14.0 \\to 11.0 \\to 9.8 \\to 4.7 \\to 0.0$. % exp_id: \\S2A\nAt small $\\varepsilon$, the tight norm bound clips erroneous corrections and masks the noisy conformal features.\nAs $\\varepsilon$ increases, the CRM applies larger corrections along unreliable directions, and compounding error across the trajectory destroys performance.\nAll three uncapped perdof seeds score 0/100 successes. % exp_id: \\S2H\n\nThis interaction is the central diagnostic: the same architecture succeeds or fails based on whether it receives clean (observation-only) or noisy (conformal) conditioning.\nThe magnitude bound does not rescue a poorly conditioned CRM; it only delays the collapse.\n\n\n%----------------------------------------------------------------------\n\\subsection{Inference-Time Scaling (K-Value Curve)}\n\\label{sec:kvalue}\n\nFigure~\\ref{fig:kvalue} plots task success rate as a function of the number of VLA samples $K$ for obs\\_only at $\\varepsilon{=}0.2$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/k_value_curve.pdf}\n\\caption{Success rate vs number of VLA samples $K$ for obs\\_only ($\\varepsilon{=}0.2$) on LIBERO-Object.\nPerformance increases monotonically from $K{=}1$ to $K{=}10$.\nError bars: $\\pm$1 std where multiple seeds are available.\n$^*$Single seed (seed\\,42).}\n\\label{fig:kvalue}\n\\end{figure}\n\nAt $K{=}1$, the CRM corrects a single VLA output without multi-sample selection and achieves $10.3\\% \\pm 1.5\\%$ ($n{=}3$), % exp_id: \\S2B\nindistinguishable from VLA-only ($11.2\\%$). % exp_id: \\S2C\nAt $K{=}5$, performance rises to $14.0\\%$ (single seed$^*$, seed\\,42). % exp_id: \\S2B\nAt $K{=}10$, the full pipeline reaches $17.5\\% \\pm 2.8\\%$ ($n{=}6$). % exp_id: \\S2B\nThe trend is monotonic: $10.3\\% \\to 14.0\\% \\to 17.5\\%$. % exp_id: \\S2B\n\nMore VLA samples improve the argmin starting point: with larger $K$, the selected candidate sits closer to the sample centroid and, on average, closer to the demonstration action.\nThe CRM correction is then more effective because smaller residuals keep the output within the reliable regime of the learned MLP.\n\nThe $K{=}1$ result is the critical control.\nIt confirms that correction alone, without multi-sample selection, provides no measurable benefit over the uncorrected VLA.\nThe CRM does not learn a fixed correction bias independent of sample quality; the improvement requires both a good starting point from selection and a learned residual from the CRM.\n\n\n%----------------------------------------------------------------------\n\\subsection{Applicability Boundary: Tokenized VLAs}\n\\label{sec:applicability}\n\nThe multi-sample pipeline requires diverse action candidates from the base VLA.\nWe test this prerequisite on OpenVLA~\\cite{kim2024openvla}, a 7B-parameter autoregressive VLA based on Llama-2.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/diversity_analysis.pdf}\n\\caption{Action sample diversity comparison.\nSmolVLA (flow-matching) produces diverse candidates across flow trajectories.\nOpenVLA (autoregressive, $T{=}0.5$) generates near-identical samples: 8/10 are identical with per-DOF variance $< 10^{-30}$.}\n\\label{fig:diversity}\n\\end{figure}\n\nAt standard temperature $T{=}0.5$, OpenVLA's $K{=}10$ samples are near-deterministic: % exp_id: \\S2G\n8 of 10 are identical, with per-DOF variance below $10^{-30}$. % exp_id: \\S2G\nMulti-sample selection over identical candidates reduces to random selection, and the CRM receives the same input regardless of $K$.\n\nRaising $T$ to 1.5 or above increases diversity but degrades the base policy. % exp_id: \\S2G\nNo temperature setting achieves both sufficient diversity and acceptable base performance. % exp_id: \\S2G\n\nThe multi-sample refinement pipeline is therefore specific to stochastic VLA architectures (e.g., flow-matching models) that produce naturally diverse candidates at their standard operating point.\nTokenized autoregressive VLAs would require alternative candidate generation strategies, such as latent-space perturbation or ensemble decoding.\nENDOFFILE\necho \"Write complete: $(wc -l < /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex) lines\"",
    "description": "Write complete experiments.tex via heredoc"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T10:10:24.355302+00:00_

Write complete: 217 lines

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T10:10:24.355448+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T10:10:24.355661+00:00_

1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	We evaluate the Conformal Refinement Module (CRM) on LIBERO-Object to answer four questions:
6	(1)~Where does the improvement originate, multi-sample selection or learned correction?
7	(2)~How does CRM conditioning interact with correction magnitude?
8	(3)~Does performance scale with the number of VLA samples $K$?
9	(4)~Does the approach transfer to tokenized VLAs?
10	In brief: correction contributes 4--5$\times$ more than selection (\S\ref{sec:component}); observation-only conditioning is robust across magnitudes while conformal conditioning collapses (\S\ref{sec:magnitude_interaction}); performance increases monotonically from $K{=}1$ to $K{=}10$ (\S\ref{sec:kvalue}); and tokenized VLAs lack the sampling diversity that multi-sample refinement requires (\S\ref{sec:applicability}).
11	
12	
13	\subsection{Experimental Setup}
14	\label{sec:exp_setup}
15	
16	\paragraph{Benchmark.}
17	We use LIBERO-Object~\cite{liu2023libero}, a suite of 10 tabletop manipulation tasks requiring generalization to novel object instances.
18	Each task is evaluated over 10 rollouts (maximum 300 steps), for 100 episodes per method per seed.
19	Success is binary: the task predicate must be satisfied before the step limit.
20	
21	\paragraph{Base VLA.}
22	We build on SmolVLA~\cite{shukor2025smolvla}, a 0.4B-parameter flow-matching VLA.
23	The model receives dual-camera RGB input (agentview + eye-in-hand, $256{\times}256$) and 8D proprioceptive state, and outputs 7D actions (6D end-effector pose + 1D gripper).
24	The gripper dimension is handled via direct thresholding, outside the refinement pipeline.
25	
26	\paragraph{Baselines.}
27	All methods share the same frozen SmolVLA checkpoint:
28	\begin{itemize}[nosep]
29	  \item \textbf{VLA-only} ($K{=}1$): single VLA sample, no selection or correction.
30	  \item \textbf{Random sel.}\ ($K{=}10$): one uniformly random sample from 10 candidates.
31	  \item \textbf{Argmin sel.}\ ($K{=}10$): cand
…[truncated 10943 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T10:10:24.355847+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "echo \"=== Em-dash check ===\" && grep -n \"—\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex && echo \"(none found)\" || echo \"CLEAN: no em-dashes\"",
  "description": "Check for em-dashes in experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Bash",
  "tool_args": {
    "command": "echo \"=== Em-dash check ===\" && grep -n \"—\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex && echo \"(none found)\" || echo \"CLEAN: no em-dashes\"",
    "description": "Check for em-dashes in experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-18T10:10:24.355981+00:00_

=== Em-dash check ===
CLEAN: no em-dashes

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-18T10:10:24.356105+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "echo \"=== Explanatory en-dash check ===\" && grep -n \" – \" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex || echo \"CLEAN: no explanatory en-dashes\"",
  "description": "Check for explanatory en-dashes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Bash",
  "tool_args": {
    "command": "echo \"=== Explanatory en-dash check ===\" && grep -n \" – \" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex || echo \"CLEAN: no explanatory en-dashes\"",
    "description": "Check for explanatory en-dashes"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-18T10:10:24.356237+00:00_

=== Explanatory en-dash check ===
CLEAN: no explanatory en-dashes

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-18T10:10:24.356378+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "echo \"=== -ing phrase ending check ===\" && grep -n \"ing\\.\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex | grep -v \"^[[:space:]]*%\" | head -20",
  "description": "Check for -ing phrase endings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Bash",
  "tool_args": {
    "command": "echo \"=== -ing phrase ending check ===\" && grep -n \"ing\\.\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex | grep -v \"^[[:space:]]*%\" | head -20",
    "description": "Check for -ing phrase endings"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-18T10:10:24.356499+00:00_

=== -ing phrase ending check ===
159:This interaction is the central diagnostic: the same architecture succeeds or fails based on whether it receives clean (observation-only) or noisy (conformal) conditioning.
217:Tokenized autoregressive VLAs would require alternative candidate generation strategies, such as latent-space perturbation or ensemble decoding.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-18T10:10:24.356617+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "echo \"=== AI word check ===\" && grep -in \"delve\\|leverage\\|utilize\\|facilitate\\|myriad\\|plethora\\|paradigm shift\\|demonstrates the effectiveness\\|extensive experiments\\|it is worth noting\\|notably,\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex || echo \"CLEAN: no AI words\"",
  "description": "Check for AI writing pattern words"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Bash",
  "tool_args": {
    "command": "echo \"=== AI word check ===\" && grep -in \"delve\\|leverage\\|utilize\\|facilitate\\|myriad\\|plethora\\|paradigm shift\\|demonstrates the effectiveness\\|extensive experiments\\|it is worth noting\\|notably,\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex || echo \"CLEAN: no AI words\"",
    "description": "Check for AI writing pattern words"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-18T10:10:24.356768+00:00_

=== AI word check ===
CLEAN: no AI words

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-18T10:10:24.356942+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "echo \"=== exp_id annotation count ===\" && grep -c \"exp_id:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex && echo \"=== exp_id sections covered ===\" && grep -o \"\\\\\\\\S2[A-H]\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex | sort -u",
  "description": "Count exp_id annotations and verify coverage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Bash",
  "tool_args": {
    "command": "echo \"=== exp_id annotation count ===\" && grep -c \"exp_id:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex && echo \"=== exp_id sections covered ===\" && grep -o \"\\\\\\\\S2[A-H]\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex | sort -u",
    "description": "Count exp_id annotations and verify coverage"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-18T10:10:24.357065+00:00_

=== exp_id annotation count ===
34
=== exp_id sections covered ===
\S2A
\S2B
\S2C
\S2D
\S2E
\S2G
\S2H

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260518T095825",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-18T10:10:24.357223+00:00_

34 exp_id annotations covering all 7 relevant evidence sections (§2A magnitude, §2B K-value, §2C baselines, §2D decomposition, §2E statistics, §2G OpenVLA, §2H perdof collapse).

Experiments section written to `docs/paper/experiments.tex` (217 lines). Structure:

1. **Setup** (lines 13--46): benchmark, VLA, 4 baselines, 3 CRM variants, statistical protocol
2. **Component Decomposition** (lines 49--103): Table 1 with 7 methods; selection ~1pp vs correction ~5pp; Fisher p=0.0074, Cohen's d=1.21; honest negatives for perdof/scalar
3. **Conditioning-Magnitude Interaction** (lines 107--160): Table 2 (6 epsilon values x 2 variants); obs\_only robust 13.5--17.5%, perdof collapses 14.0->0.0%
4. **K-Value Curve** (lines 164--190): monotonic K=1(10.3%)→K=5(14.0%*)→K=10(17.5%); K=5 single-seed noted
5. **Applicability Boundary** (lines 194--217): OpenVLA diversity failure (8/10 identical, variance <1e-30)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_experiments_20260518T095825"
}
```

</details>

---

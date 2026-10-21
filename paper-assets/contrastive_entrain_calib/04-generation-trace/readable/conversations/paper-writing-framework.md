# paper writing framework

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_paper_writing_framework_20260520T073815.jsonl`
- **Structured JSON:** [`eab182f519b1d2e7ada3.json`](../../sessions/ea/eab182f519b1d2e7ada3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-20T07:39:47.792618+00:00_

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
  "session": "worker_paper_writing_framework_20260520T073815",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T07:39:47.793275+00:00_

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
  "session": "worker_paper_writing_framework_20260520T073815",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T07:39:47.793508+00:00_

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
  "session": "worker_paper_writing_framework_20260520T073815",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T07:39:47.793906+00:00_

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
  "session": "worker_paper_writing_framework_20260520T073815",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T07:39:47.794089+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_framework_20260520T073815",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T07:39:47.794219+00:00_

docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_framework_20260520T073815",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T07:39:47.794369+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_framework_20260520T073815",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T07:39:47.794506+00:00_

1	\documentclass[11pt,a4paper]{article}
2	\usepackage[hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	
13	\newcommand{\dsyc}{d_{\text{syc}}}
14	\newcommand{\tof}{\text{ToF}}
15	\newcommand{\nof}{\text{NoF}}
16	\newcommand{\sycon}{\textsc{SyconScore}}
17	\newcommand{\rone}{R_1}
18	\newcommand{\rthree}{R_3}
19	
20	\title{Discriminability Without Utility: Why Sycophancy Directions Fail as RL Rewards}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	\input{sections/abstract}
29	\end{abstract}
30	
31	\input{sections/introduction}
32	
33	\input{sections/framework}
34	
35	\input{sections/direction_quality}
36	
37	\input{sections/cosine_failure}
38	
39	\input{sections/probe_trap}
40	
41	\input{sections/discussion}
42	
43	\input{sections/related_work}
44	
45	\input{sections/conclusion}
46	
47	\section*{Limitations}
48	\input{sections/limitations}
49	
50	\bibliographystyle{acl_natbib}
51	\bibliography{references}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_framework_20260520T073815",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T07:39:47.794647+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/ 2>/dev/null || echo \"DIR_NOT_EXISTS\"",
  "description": "List sections directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_framework_20260520T073815",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/ 2>/dev/null || echo \"DIR_NOT_EXISTS\"",
    "description": "List sections directory"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T07:39:47.794763+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_framework_20260520T073815",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T07:39:47.794898+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections 2>&1",
  "description": "Check sections directory existence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_framework_20260520T073815",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections 2>&1",
    "description": "Check sections directory existence"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T07:39:47.795024+00:00_

total 8
drwxr-xr-x 2 ubuntu ubuntu 4096 May 20 07:36 .
drwxr-xr-x 3 ubuntu ubuntu 4096 May 20 07:37 ..

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_framework_20260520T073815",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T07:39:47.795180+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex",
  "content": "\\section{Experimental Framework}\n\\label{sec:framework}\n\nThis section establishes the notation, experimental components, and evaluation protocol used throughout the paper.\nWe first describe how the contrastive sycophancy direction $\\dsyc$ is extracted (\\S\\ref{ssec:extraction}), then define three reward formulations that incorporate $\\dsyc$ into GRPO training (\\S\\ref{ssec:reward}), explain the online recalibration procedure (\\S\\ref{ssec:recalib}), and finally specify the evaluation metrics (\\S\\ref{ssec:eval}).\n\n\\subsection{Direction Extraction}\n\\label{ssec:extraction}\n\nWe extract a linear sycophancy direction $\\dsyc$ from the residual stream of a target model using contrastive activation pairs.\nEach pair consists of two model responses to the same user challenge: a \\emph{valid correction}, in which the model appropriately revises its earlier answer upon receiving well-supported counter-evidence, and a \\emph{sycophantic capitulation}, in which the model abandons a correct answer under social pressure without adequate evidential warrant.\n\nTo isolate the cognitive signal from surface-level linguistic variation, we apply style control: both responses in each pair are generated with matched hedging patterns, politeness markers, and response length, so that $\\dsyc$ reflects the distinction between warranted and unwarranted belief change rather than stylistic differences.\nConcretely, we construct 362 style-controlled contrastive activations from 181 paired examples stratified across three evidence-strength levels (weak, medium, strong).\n\nGiven a target layer $\\ell$, let $\\mathbf{h}^{+}_i$ denote the residual-stream activation for the $i$-th valid correction and $\\mathbf{h}^{-}_i$ for the corresponding sycophantic capitulation.\nThe sycophancy direction is the mean difference:\n\\begin{equation}\n\\label{eq:dsyc}\n\\dsyc = \\frac{1}{N}\\sum_{i=1}^{N}\\left(\\mathbf{h}^{+}_i - \\mathbf{h}^{-}_i\\right)\n\\end{equation}\nwhere $N{=}181$ is the number of contrastive pairs.\nWe select the target layer by 5-fold cross-validated AUROC over a linear classifier trained on the projection $\\mathbf{h} \\cdot \\dsyc$; on Qwen3-8B this yields layer 19 with AUROC $0.827 \\pm 0.028$ (exp-001).\nSection~\\ref{sec:direction_quality} presents detailed discriminability analyses, including cross-model validation on Llama-3-8B.\n\n\\subsection{GRPO Reward Formulation}\n\\label{ssec:reward}\n\nGroup Relative Policy Optimization \\citep[GRPO;][]{shao2024grpo} uses a reward signal to rank sampled completions and update the policy toward higher-reward outputs.\nWe define a combined reward:\n\\begin{equation}\n\\label{eq:reward}\nR = w_1 \\cdot \\rone + w_3 \\cdot \\rthree\n\\end{equation}\nwhere $\\rone$ is a direction-based component derived from $\\dsyc$ and $\\rthree$ is a behavioral component.\n\n\\paragraph{Direction-based reward ($\\rone$).}\nWe investigate three formulations that translate $\\dsyc$ into a scalar training signal.\nLet $\\mathbf{h}$ denote the model's residual-stream activation at a designated token position during a training rollout.\n\n\\begin{itemize}\n\\item[\\textbf{F1}] \\textbf{Cosine.} $\\rone = \\cos(\\mathbf{h},\\, \\dsyc)$, the cosine similarity between the activation and the sycophancy direction.\n\\item[\\textbf{F2}] \\textbf{Scaled cosine.} $\\rone = \\alpha \\cdot \\cos(\\mathbf{h},\\, \\dsyc)$, where $\\alpha$ amplifies the gradient signal to compete with $\\rthree$ in magnitude.\n\\item[\\textbf{F3}] \\textbf{Binary probe.} $\\rone = \\mathbb{I}[P(\\text{syc} \\mid \\mathbf{h}) < 0.5]$, a binary indicator derived from a logistic probe trained on the same contrastive data. The probe is frozen during GRPO training and gradients are stopped at its input.\n\\end{itemize}\n\n\\paragraph{Behavioral reward ($\\rthree$).}\n$\\rthree$ is computed by a DeBERTa-based natural language inference (NLI) classifier that scores whether the model's response is consistent with the ground-truth answer.\nThis component provides a task-level behavioral signal independent of internal representations.\nThe weight configuration ($w_1$, $w_3$) varies across experiments and is specified in the corresponding sections (\\S\\ref{sec:cosine_failure}, \\S\\ref{sec:probe_trap}).\n\n\\subsection{Online Recalibration}\n\\label{ssec:recalib}\n\nLoRA fine-tuning progressively shifts the model's internal representations, which could cause $\\dsyc$ to become misaligned with the current activation geometry.\nTo address this, we re-extract $\\dsyc$ every 500 training steps by re-running the contrastive pairs through the updated model and recomputing Equation~\\ref{eq:dsyc}.\nEmpirically, the cosine similarity between consecutive directions remains high (${\\approx}\\,0.96$ at step 500), indicating that the direction drifts slowly relative to the recalibration frequency.\nThis procedure ensures that $\\rone$ tracks the evolving representation space throughout training rather than scoring against a stale direction.\n\n\\subsection{Evaluation Protocol}\n\\label{ssec:eval}\n\nWe evaluate sycophancy mitigation along two complementary axes: the model's willingness to accept valid corrections and its resistance to invalid pressure.\n\n\\paragraph{Metrics.}\nWe define two primary rates.\nThe \\emph{True-positive Flip rate} ($\\tof$) measures the fraction of valid corrections that the model accepts, i.e., cases where the model appropriately revises an incorrect initial answer when presented with well-supported counter-evidence.\nThe \\emph{No-Flip rate} ($\\nof$) measures the fraction of invalid challenges that the model resists, i.e., cases where the model maintains a correct initial answer despite unsupported social pressure.\nBoth rates range from 0 to 1 with higher values indicating better performance.\n\nA model that accepts all challenges (including invalid ones) achieves high $\\tof$ but low $\\nof$; a model that rejects all challenges achieves the opposite.\nWe capture this trade-off with $\\sycon$, the harmonic mean of the two rates:\n\\begin{equation}\n\\label{eq:sycon}\n\\sycon = \\frac{2 \\cdot \\tof \\cdot \\nof}{\\tof + \\nof}\n\\end{equation}\n\n$\\sycon$ is analogous to the $F_1$ score: it penalizes models that sacrifice one axis for the other, and a high $\\sycon$ requires balanced performance on both.\nClassification of each response (flip vs.\\ no-flip) is determined by an NLI-based procedure following the protocol of \\citet{consistency2025bctact}.\n\n\\paragraph{Test set and model configuration.}\nEvaluation uses the same 362 style-controlled contrastive instances (181 pairs, weak/medium/strong stratification) described in \\S\\ref{ssec:extraction}, with a held-out split not used during direction extraction.\nAll training experiments use Qwen3-8B with LoRA (rank$=$64, $\\alpha{=}128$) and DeepSpeed ZeRO-2 for memory-efficient optimization.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_framework_20260520T073815",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex",
    "content": "\\section{Experimental Framework}\n\\label{sec:framework}\n\nThis section establishes the notation, experimental components, and evaluation protocol used throughout the paper.\nWe first describe how the contrastive sycophancy direction $\\dsyc$ is extracted (\\S\\ref{ssec:extraction}), then define three reward formulations that incorporate $\\dsyc$ into GRPO training (\\S\\ref{ssec:reward}), explain the online recalibration procedure (\\S\\ref{ssec:recalib}), and finally specify the evaluation metrics (\\S\\ref{ssec:eval}).\n\n\\subsection{Direction Extraction}\n\\label{ssec:extraction}\n\nWe extract a linear sycophancy direction $\\dsyc$ from the residual stream of a target model using contrastive activation pairs.\nEach pair consists of two model responses to the same user challenge: a \\emph{valid correction}, in which the model appropriately revises its earlier answer upon receiving well-supported counter-evidence, and a \\emph{sycophantic capitulation}, in which the model abandons a correct answer under social pressure without adequate evidential warrant.\n\nTo isolate the cognitive signal from surface-level linguistic variation, we apply style control: both responses in each pair are generated with matched hedging patterns, politeness markers, and response length, so that $\\dsyc$ reflects the distinction between warranted and unwarranted belief change rather than stylistic differences.\nConcretely, we construct 362 style-controlled contrastive activations from 181 paired examples stratified across three evidence-strength levels (weak, medium, strong).\n\nGiven a target layer $\\ell$, let $\\mathbf{h}^{+}_i$ denote the residual-stream activation for the $i$-th valid correction and $\\mathbf{h}^{-}_i$ for the corresponding sycophantic capitulation.\nThe sycophancy direction is the mean difference:\n\\begin{equation}\n\\label{eq:dsyc}\n\\dsyc = \\frac{1}{N}\\sum_{i=1}^{N}\\left(\\mathbf{h}^{+}_i - \\mathbf{h}^{-}_i\\right)\n\\end{equation}\nwhere $N{=}181$ is the number of contrastive pairs.\nWe select the target layer by 5-fold cross-validated AUROC over a linear classifier trained on the projection $\\mathbf{h} \\cdot \\dsyc$; on Qwen3-8B this yields layer 19 with AUROC $0.827 \\pm 0.028$ (exp-001).\nSection~\\ref{sec:direction_quality} presents detailed discriminability analyses, including cross-model validation on Llama-3-8B.\n\n\\subsection{GRPO Reward Formulation}\n\\label{ssec:reward}\n\nGroup Relative Policy Optimization \\citep[GRPO;][]{shao2024grpo} uses a reward signal to rank sampled completions and update the policy toward higher-reward outputs.\nWe define a combined reward:\n\\begin{equation}\n\\label{eq:reward}\nR = w_1 \\cdot \\rone + w_3 \\cdot \\rthree\n\\end{equation}\nwhere $\\rone$ is a direction-based component derived from $\\dsyc$ and $\\rthree$ is a behavioral component.\n\n\\paragraph{Direction-based reward ($\\rone$).}\nWe investigate three formulations that translate $\\dsyc$ into a scalar training signal.\nLet $\\mathbf{h}$ denote the model's residual-stream activation at a designated token position during a training rollout.\n\n\\begin{itemize}\n\\item[\\textbf{F1}] \\textbf{Cosine.} $\\rone = \\cos(\\mathbf{h},\\, \\dsyc)$, the cosine similarity between the activation and the sycophancy direction.\n\\item[\\textbf{F2}] \\textbf{Scaled cosine.} $\\rone = \\alpha \\cdot \\cos(\\mathbf{h},\\, \\dsyc)$, where $\\alpha$ amplifies the gradient signal to compete with $\\rthree$ in magnitude.\n\\item[\\textbf{F3}] \\textbf{Binary probe.} $\\rone = \\mathbb{I}[P(\\text{syc} \\mid \\mathbf{h}) < 0.5]$, a binary indicator derived from a logistic probe trained on the same contrastive data. The probe is frozen during GRPO training and gradients are stopped at its input.\n\\end{itemize}\n\n\\paragraph{Behavioral reward ($\\rthree$).}\n$\\rthree$ is computed by a DeBERTa-based natural language inference (NLI) classifier that scores whether the model's response is consistent with the ground-truth answer.\nThis component provides a task-level behavioral signal independent of internal representations.\nThe weight configuration ($w_1$, $w_3$) varies across experiments and is specified in the corresponding sections (\\S\\ref{sec:cosine_failure}, \\S\\ref{sec:probe_trap}).\n\n\\subsection{Online Recalibration}\n\\label{ssec:recalib}\n\nLoRA fine-tuning progressively shifts the model's internal representations, which could cause $\\dsyc$ to become misaligned with the current activation geometry.\nTo address this, we re-extract $\\dsyc$ every 500 training steps by re-running the contrastive pairs through the updated model and recomputing Equation~\\ref{eq:dsyc}.\nEmpirically, the cosine similarity between consecutive directions remains high (${\\approx}\\,0.96$ at step 500), indicating that the direction drifts slowly relative to the recalibration frequency.\nThis procedure ensures that $\\rone$ tracks the evolving representation space throughout training rather than scoring against a stale direction.\n\n\\subsection{Evaluation Protocol}\n\\label{ssec:eval}\n\nWe evaluate sycophancy mitigation along two complementary axes: the model's willingness to accept valid corrections and its resistance to invalid pressure.\n\n\\paragraph{Metrics.}\nWe define two primary rates.\nThe \\emph{True-positive Flip rate} ($\\tof$) measures the fraction of valid corrections that the model accepts, i.e., cases where the model appropriately revises an incorrect initial answer when presented with well-supported counter-evidence.\nThe \\emph{No-Flip rate} ($\\nof$) measures the fraction of invalid challenges that the model resists, i.e., cases where the model maintains a correct initial answer despite unsupported social pressure.\nBoth rates range from 0 to 1 with higher values indicating better performance.\n\nA model that accepts all challenges (including invalid ones) achieves high $\\tof$ but low $\\nof$; a model that rejects all challenges achieves the opposite.\nWe capture this trade-off with $\\sycon$, the harmonic mean of the two rates:\n\\begin{equation}\n\\label{eq:sycon}\n\\sycon = \\frac{2 \\cdot \\tof \\cdot \\nof}{\\tof + \\nof}\n\\end{equation}\n\n$\\sycon$ is analogous to the $F_1$ score: it penalizes models that sacrifice one axis for the other, and a high $\\sycon$ requires balanced performance on both.\nClassification of each response (flip vs.\\ no-flip) is determined by an NLI-based procedure following the protocol of \\citet{consistency2025bctact}.\n\n\\paragraph{Test set and model configuration.}\nEvaluation uses the same 362 style-controlled contrastive instances (181 pairs, weak/medium/strong stratification) described in \\S\\ref{ssec:extraction}, with a held-out split not used during direction extraction.\nAll training experiments use Qwen3-8B with LoRA (rank$=$64, $\\alpha{=}128$) and DeepSpeed ZeRO-2 for memory-efficient optimization.\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T07:39:47.795384+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_framework_20260520T073815",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T07:39:47.795519+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_framework_20260520T073815",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T07:39:47.795638+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_framework_20260520T073815",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T07:39:47.795757+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "framework-section-v1",
  "type": "paper",
  "description": "§2 Experimental Framework section for the sycophancy directions paper. Defines d_syc extraction, three GRPO reward formulations (F1-F3), online recalibration, and evaluation protocol (ToF, NoF, SYCONScore).",
  "project": "contrastive_entrain_calib",
  "source_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex",
  "tags": "['paper', 'section2', 'framework', 'latex']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_framework_20260520T073815",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "framework-section-v1",
    "type": "paper",
    "description": "§2 Experimental Framework section for the sycophancy directions paper. Defines d_syc extraction, three GRPO reward formulations (F1-F3), online recalibration, and evaluation protocol (ToF, NoF, SYCONScore).",
    "project": "contrastive_entrain_calib",
    "source_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex",
    "tags": "['paper', 'section2', 'framework', 'latex']"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T07:39:47.795922+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_3ec9c8\", \"name\": \"framework-section-v1\", \"type\": \"paper\", \"description\": \"§2 Experimental Framework section for the sycophancy directions paper. Defines d_syc extraction, three GRPO reward formulations (F1-F3), online recalibration, and evaluation protocol (ToF, NoF, SYCONScore).\", \"path\": \"projects/contrastive_entrain_calib/artifacts/_project/paper/framework.tex\", \"url\": null, \"project\": \"contrastive_entrain_calib\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T07:39:37.502507+00:00\", \"tags\": [\"paper\", \"section2\", \"framework\", \"latex\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_framework_20260520T073815",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-20T07:39:47.796104+00:00_

§2 `framework.tex` 已写入并注册。内容概要：

- **§2.1 Direction Extraction**: 定义 $d_{\text{syc}}$ 的 mean-difference 提取方法，362 style-controlled contrastive activations (181 pairs)，5-fold CV AUROC 0.827±0.028，best layer=19 (Qwen3-8B)
- **§2.2 GRPO Reward Formulation**: 组合奖励 $R = w_1 \cdot R_1 + w_3 \cdot R_3$，三种 R1 公式化 (F1 cosine, F2 scaled cosine, F3 binary probe)，DeBERTa NLI 作为 R3
- **§2.3 Online Recalibration**: 每 500 步重提取 $d_{\text{syc}}$，cosine similarity ≈ 0.96
- **§2.4 Evaluation Protocol**: ToF / NoF / SYCONScore (harmonic mean) 定义，NLI-based classification，模型配置 (LoRA rank=64, α=128, ZeRO-2)

所有要求的符号 (`\dsyc`, `\tof`, `\nof`, `\sycon`, `\rone`, `\rthree`) 均使用自定义命令。无 em-dash、无 -ing 结尾、无过度分段。约 730 words。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_framework_20260520T073815"
}
```

</details>

---

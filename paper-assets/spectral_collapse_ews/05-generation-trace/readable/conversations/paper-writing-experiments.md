# paper writing experiments

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/chats/worker_paper_writing_experiments_20260517T203103.jsonl`
- **Structured JSON:** [`2aa2b6d234a868c53e80.json`](../../sessions/2a/2aa2b6d234a868c53e80.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

27 recorded events

### Tool call

_source line 1 · 2026-05-17T20:32:45.924545+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T20:32:45.925272+00:00_

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
…[truncated 668 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T20:32:45.925516+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T20:32:45.925873+00:00_

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
…[truncated 100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T20:32:45.926033+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Glob",
  "tool_args": {
    "pattern": "paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T20:32:45.926159+00:00_

paper/sections/abstract.tex
paper/sections/introduction.tex
paper/sections/method.tex
paper/sections/experiments.tex
paper/sections/related_work.tex
paper/sections/conclusion.tex
paper/sections/limitations.tex
paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T20:32:45.926307+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T20:32:45.926431+00:00_

1	\todo{Experiments to be written in Step 4.}
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T20:32:45.926544+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T20:32:45.926741+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{xcolor}
16	\usepackage{subcaption}
17	
18	\newcommand{\todo}[1]{\textcolor{red}{[TODO: #1]}}
19	
20	\title{Spectral Early Warning Signals for Model Collapse in Recursive Synthetic Training}
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
31	\section{Introduction}
32	\label{sec:intro}
33	\input{sections/introduction}
34	
35	\section{Method}
36	\label{sec:method}
37	\input{sections/method}
38	
39	\section{Experiments}
40	\label{sec:experiments}
41	\input{sections/experiments}
42	
43	\section{Related Work}
44	\label{sec:related}
45	\input{sections/related_work}
46	
47	\section{Conclusion}
48	\label{sec:conclusion}
49	\input{sections/conclusion}
50	
51	\section*{Limitations}
52	\input{sections/limitations}
53	
54	\bibliography{references}
55	
56	\end{document}
57	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T20:32:45.926882+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T20:32:45.927000+00:00_

1	\todo{Method to be written in Step 4.}
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T20:32:45.927134+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T20:32:45.927249+00:00_

1	\todo{Abstract to be written after all sections are complete.}
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T20:32:45.927379+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T20:32:45.927499+00:00_

1	\todo{Introduction to be written in Step 4.}
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T20:32:45.927682+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
  "content": "\n\\subsection{Experimental Setup}\n\\label{subsec:setup}\n\nWe use Pythia-410M-deduped \\cite{biderman2023pythia} as our base model and fine-tune on a 50K-subset of OpenWebText.\nStarting from the pretrained checkpoint (generation~0), each subsequent generation fine-tunes on synthetic text produced by the previous generation, for a total of 10 recursive generations.\nAt each generation, we compute spectral metrics on the embedding Gram matrix $\\mathbf{G} = \\mathbf{E}^\\top \\mathbf{E}$ from 1K held-out samples, where $\\mathbf{E} \\in \\mathbb{R}^{n \\times d}$ stacks last-layer embeddings.\nWe track four spectral indicators: \\textit{effective rank} $r_{\\text{eff}} = \\exp(H(\\mathbf{p}))$, where $H(\\mathbf{p})$ is the Shannon entropy of the normalized singular value distribution; \\textit{spectral log-volume} (SLV) $\\sum_i \\log \\sigma_i = \\log \\det \\mathbf{G}^{1/2}$; the leading singular value $\\sigma_1$; and three downstream metrics: perplexity, HellaSwag accuracy (0-shot), and distinct-4.\n\n\\subsection{Spectral Collapse Characterization}\n\\label{subsec:phase0}\n\nTable~\\ref{tab:phase0} reports spectral and downstream metrics across 10 recursive generations.\nThe trajectory reveals a three-phase structure in the spectral dynamics of model collapse.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}rrrrrrc@{}}\n\\toprule\nGen & $r_{\\text{eff}}$ & SLV & PPL & HeSw & D-4 & $\\sigma_1$ \\\\\n\\midrule\n0  & 417.55 & 2366.68 &  9.55 & .413 & .741 & 1942.8 \\\\\n1  & 491.77 & 2464.76 & 11.38 & .390 & .626 &  804.0 \\\\\n2  & \\textbf{496.44} & \\textbf{2469.93} & 13.58 & .376 & .515 &  712.0 \\\\\n3  & 493.31 & 2440.57 & 16.25 & .366 & .490 &  700.7 \\\\\n5  & 479.21 & 2370.17 & 24.59 & .344 & .463 &  741.0 \\\\\n7  & 464.20 & 2304.19 & 38.89 & .319 & .447 &  791.3 \\\\\n10 & 442.46 & 2178.95 & 76.78 & .295 & .426 &  825.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Spectral and downstream metrics across recursive generations (Pythia-410M). $r_{\\text{eff}}$: effective rank; SLV: spectral log-volume; PPL: perplexity; HeSw: HellaSwag (0-shot); D-4: distinct-4. Bold marks the peak before collapse onset.}\n\\label{tab:phase0}\n\\end{table}\n\n\\paragraph{Phase I: Spectral Decompression (Gen 0--2).}\nIn the first two generations, $r_{\\text{eff}}$ rises from 417.55 to 496.44 (+18.9\\%) and SLV increases from 2366.68 to 2469.93 (+4.4\\%), while $\\sigma_1$ drops sharply from 1942.8 to 712.0.\nThis pattern reflects a redistribution of spectral mass: the dominant singular value loses energy to smaller components, temporarily increasing the effective dimensionality of the embedding space.\nCrucially, this decompression does not indicate improved model quality.\nHellaSwag accuracy drops from 0.413 to 0.376 ($-$8.9\\%) during the same interval, and distinct-4 falls from 0.741 to 0.515 ($-$30.5\\%).\nThis asymmetry between spectral expansion and capability degradation is a central finding: higher embedding diversity does not preserve downstream knowledge.\nThe spectral indicators improve while the model is already losing both factual competence and output diversity.\n\n\\paragraph{Phase II: Collapse Onset (Gen 2--4).}\nBoth $r_{\\text{eff}}$ and SLV reverse direction after generation~2.\nBetween Gen~2 and Gen~3, $r_{\\text{eff}}$ decreases from 496.44 to 493.31 and SLV falls from 2469.93 to 2440.57.\nThis inflection point marks the transition from decompression to collapse.\nPerplexity continues its monotonic rise (13.58 to 16.25), confirming that downstream degradation proceeds uninterrupted through the spectral peak.\n\n\\paragraph{Phase III: Accelerating Collapse (Gen 4--10).}\nAfter onset, spectral contraction accelerates.\nThe per-generation decline rate of $r_{\\text{eff}}$ in Phase III (Gen 4--10) is 2.43$\\times$ that of Phase II (Gen 2--4).\nBy generation~10, $r_{\\text{eff}}$ falls to 442.46 (below its initial value), SLV drops to 2178.95 ($-$7.9\\% from baseline), and perplexity reaches 76.78 ($+$704\\%).\nMeanwhile, $\\sigma_1$ reverses its earlier decline and increases from 700.7 at Gen~3 to 825.7 at Gen~10, indicating renewed spectral concentration as the embedding space contracts around fewer dominant directions.\nFigure~\\ref{fig:spectral_trajectory} visualizes these joint trajectories.\n\n\\paragraph{HellaSwag-Spectral Asymmetry.}\nThe most striking pattern in Table~\\ref{tab:phase0} is the temporal misalignment between spectral health and downstream capability.\nHellaSwag accuracy already drops 5.6\\% from Gen~0 to Gen~1, precisely when $r_{\\text{eff}}$ and SLV are still rising.\nThis asymmetry implies that spectral decompression captures distributional broadening of the embedding space, not preservation of the structured representations that support task performance.\nA monitoring system that relies solely on spectral metrics during Phase~I would incorrectly conclude that the model remains healthy.\n\n\\subsection{Cross-Scale Validation}\n\\label{subsec:cross_scale}\n\nTo examine whether the three-phase pattern generalizes beyond 410M parameters, we run the same protocol on Pythia-1B for generations 0--3.\nThe results confirm the same decompression-onset structure: $r_{\\text{eff}}$ rises from 516.14 (Gen~0) to a peak of 580.92 (Gen~2), while $\\sigma_1$ drops from 1661.2 to 916.3.\nSLV peaks at Gen~1 (2905.74) and begins declining at Gen~2 (2893.85), one generation before $r_{\\text{eff}}$ plateaus (580.92 at Gen~2, 580.63 at Gen~3).\nThis lead-lag relationship, where SLV turns before $r_{\\text{eff}}$, suggests that log-volume contraction precedes effective rank loss and may serve as an earlier warning signal.\n\n\\subsection{Adaptive Mixing Comparison}\n\\label{subsec:phase1}\n\n\\todo{Phase 1 results: comparison of four mixing conditions (pure collapse, fixed mix, linear increasing, adaptive with $k$=10 controller). Include Table~\\ref{tab:comparison} with spectral and downstream metrics per condition, and Figure~\\ref{fig:comparison} showing controller trigger timing and mixing ratio dynamics. Report signal attenuation paradox.}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
    "content": "\n\\subsection{Experimental Setup}\n\\label{subsec:setup}\n\nWe use Pythia-410M-deduped \\cite{biderman2023pythia} as our base model and fine-tune on a 50K-subset of OpenWebText.\nStarting from the pretrained checkpoint (generation~0), each subsequent generation fine-tunes on synthetic text produced by the previous generation, for a total of 10 recursive generations.\nAt each generation, we compute spectral metrics on the embedding Gram matrix $\\mathbf{G} = \\mathbf{E}^\\top \\mathbf{E}$ from 1K held-out samples, where $\\mathbf{E} \\in \\mathbb{R}^{n \\times d}$ stacks last-layer embeddings.\nWe track four spectral indicators: \\textit{effective rank} $r_{\\text{eff}} = \\exp(H(\\mathbf{p}))$, where $H(\\mathbf{p})$ is the Shannon entropy of the normalized singular value distribution; \\textit{spectral log-volume} (SLV) $\\sum_i \\log \\sigma_i = \\log \\det \\mathbf{G}^{1/2}$; the leading singular value $\\sigma_1$; and three downstream metrics: perplexity, HellaSwag accuracy (0-shot), and distinct-4.\n\n\\subsection{Spectral Collapse Characterization}\n\\label{subsec:phase0}\n\nTable~\\ref{tab:phase0} reports spectral and downstream metrics across 10 recursive generations.\nThe trajectory reveals a three-phase structure in the spectral dynamics of model collapse.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}rrrrrrc@{}}\n\\toprule\nGen & $r_{\\text{eff}}$ & SLV & PPL & HeSw & D-4 & $\\sigma_1$ \\\\\n\\midrule\n0  & 417.55 & 2366.68 &  9.55 & .413 & .741 & 1942.8 \\\\\n1  & 491.77 & 2464.76 & 11.38 & .390 & .626 &  804.0 \\\\\n2  & \\textbf{496.44} & \\textbf{2469.93} & 13.58 & .376 & .515 &  712.0 \\\\\n3  & 493.31 & 2440.57 & 16.25 & .366 & .490 &  700.7 \\\\\n5  & 479.21 & 2370.17 & 24.59 & .344 & .463 &  741.0 \\\\\n7  & 464.20 & 2304.19 & 38.89 & .319 & .447 &  791.3 \\\\\n10 & 442.46 & 2178.95 & 76.78 & .295 & .426 &  825.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Spectral and downstream metrics across recursive generations (Pythia-410M). $r_{\\text{eff}}$: effective rank; SLV: spectral log-volume; PPL: perplexity; HeSw: HellaSwag (0-shot); D-4: distinct-4. Bold marks the peak before collapse onset.}\n\\label{tab:phase0}\n\\end{table}\n\n\\paragraph{Phase I: Spectral Decompression (Gen 0--2).}\nIn the first two generations, $r_{\\text{eff}}$ rises from 417.55 to 496.44 (+18.9\\%) and SLV increases from 2366.68 to 2469.93 (+4.4\\%), while $\\sigma_1$ drops sharply from 1942.8 to 712.0.\nThis pattern reflects a redistribution of spectral mass: the dominant singular value loses energy to smaller components, temporarily increasing the effective dimensionality of the embedding space.\nCrucially, this decompression does not indicate improved model quality.\nHellaSwag accuracy drops from 0.413 to 0.376 ($-$8.9\\%) during the same interval, and distinct-4 falls from 0.741 to 0.515 ($-$30.5\\%).\nThis asymmetry between spectral expansion and capability degradation is a central finding: higher embedding diversity does not preserve downstream knowledge.\nThe spectral indicators improve while the model is already losing both factual competence and output diversity.\n\n\\paragraph{Phase II: Collapse Onset (Gen 2--4).}\nBoth $r_{\\text{eff}}$ and SLV reverse direction after generation~2.\nBetween Gen~2 and Gen~3, $r_{\\text{eff}}$ decreases from 496.44 to 493.31 and SLV falls from 2469.93 to 2440.57.\nThis inflection point marks the transition from decompression to collapse.\nPerplexity continues its monotonic rise (13.58 to 16.25), confirming that downstream degradation proceeds uninterrupted through the spectral peak.\n\n\\paragraph{Phase III: Accelerating Collapse (Gen 4--10).}\nAfter onset, spectral contraction accelerates.\nThe per-generation decline rate of $r_{\\text{eff}}$ in Phase III (Gen 4--10) is 2.43$\\times$ that of Phase II (Gen 2--4).\nBy generation~10, $r_{\\text{eff}}$ falls to 442.46 (below its initial value), SLV drops to 2178.95 ($-$7.9\\% from baseline), and perplexity reaches 76.78 ($+$704\\%).\nMeanwhile, $\\sigma_1$ reverses its earlier decline and increases from 700.7 at Gen~3 to 825.7 at Gen~10, indicating renewed spectral concentration as the embedding space contracts around fewer dominant directions.\nFigure~\\ref{fig:spectral_trajectory} visualizes these joint trajectories.\n\n\\paragraph{HellaSwag-Spectral Asymmetry.}\nThe most striking pattern in Table~\\ref{tab:phase0} is the temporal misalignment between spectral health and downstream capability.\nHellaSwag accuracy already drops 5.6\\% from Gen~0 to Gen~1, precisely when $r_{\\text{eff}}$ and SLV are still rising.\nThis asymmetry implies that spectral decompression captures distributional broadening of the embedding space, not preservation of the structured representations that support task performance.\nA monitoring system that relies solely on spectral metrics during Phase~I would incorrectly conclude that the model remains healthy.\n\n\\subsection{Cross-Scale Validation}\n\\label{subsec:cross_scale}\n\nTo examine whether the three-phase pattern generalizes beyond 410M parameters, we run the same protocol on Pythia-1B for generations 0--3.\nThe results confirm the same decompression-onset structure: $r_{\\text{eff}}$ rises from 516.14 (Gen~0) to a peak of 580.92 (Gen~2), while $\\sigma_1$ drops from 1661.2 to 916.3.\nSLV peaks at Gen~1 (2905.74) and begins declining at Gen~2 (2893.85), one generation before $r_{\\text{eff}}$ plateaus (580.92 at Gen~2, 580.63 at Gen~3).\nThis lead-lag relationship, where SLV turns before $r_{\\text{eff}}$, suggests that log-volume contraction precedes effective rank loss and may serve as an earlier warning signal.\n\n\\subsection{Adaptive Mixing Comparison}\n\\label{subsec:phase1}\n\n\\todo{Phase 1 results: comparison of four mixing conditions (pure collapse, fixed mix, linear increasing, adaptive with $k$=10 controller). Include Table~\\ref{tab:comparison} with spectral and downstream metrics per condition, and Figure~\\ref{fig:comparison} showing controller trigger timing and mixing ratio dynamics. Report signal attenuation paradox.}\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T20:32:45.927907+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T20:32:45.928054+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T20:32:45.928181+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T20:32:45.928301+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T20:32:45.928420+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T20:32:45.928535+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing[,.]?\\s*$",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing[,.]?\\s*$",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T20:32:45.928676+00:00_

17:\centering
59:HellaSwag accuracy already drops 5.6\% from Gen~0 to Gen~1, precisely when $r_{\text{eff}}$ and SLV are still rising.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T20:32:45.928823+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "(Furthermore|Moreover|Additionally|It is worth noting|Notably,)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Grep",
  "tool_args": {
    "pattern": "(Furthermore|Moreover|Additionally|It is worth noting|Notably,)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T20:32:45.928940+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260517T203103",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-17T20:32:45.929076+00:00_

Clean. The experiments section is written at `/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex`.

Structure:
- **Setup** (1 para): model, data, protocol, metric definitions
- **Spectral Collapse Characterization**: Table 1 + three-phase narrative (Decompression, Onset, Acceleration) + dedicated paragraph on HellaSwag-spectral asymmetry as a highlighted finding
- **Cross-Scale Validation** (1 para): Pythia-1B confirms same pattern, notes SLV leads $r_{\text{eff}}$ by ~1 generation
- **Adaptive Mixing** placeholder with `\todo{}`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_experiments_20260517T203103"
}
```

</details>

---

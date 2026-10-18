# paper writing related work

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_paper_writing_related_work_20260522T150758.jsonl`
- **Structured JSON:** [`72520d52763ad7316081.json`](../../sessions/72/72520d52763ad7316081.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-22T15:11:13.143479+00:00_

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
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T15:11:13.144186+00:00_

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
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T15:11:13.144372+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T15:11:13.144508+00:00_

docs/paper/introduction.tex
docs/paper/related_work.tex
docs/paper/threat_model.tex
docs/paper/methodology.tex
docs/paper/results.tex
docs/paper/analysis.tex
docs/paper/conclusion.tex
docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T15:11:13.144632+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/ 2>/dev/null || echo \"DIR_NOT_EXISTS\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/ 2>/dev/null || echo \"DIR_NOT_EXISTS\""
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T15:11:13.144807+00:00_

acl.sty
acl_natbib.bst
analysis.tex
conclusion.tex
introduction.tex
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
methodology.tex
references.bib
related_work.tex
results.tex
threat_model.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T15:11:13.144998+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T15:11:13.145150+00:00_

1	\section{Related Work}
2	% [PLACEHOLDER — to be written by Worker]
3	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T15:11:13.145277+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T15:11:13.145512+00:00_

1	% Bibliography for cert_manip_resist_eval
2	% All entries verified via WebSearch on 2026-05-22
3	% ============================================================
4	
5	% ============================================================
6	% Part A: Papers from literature_map.yaml (12 papers)
7	% ============================================================
8	
9	@article{robertson2025stepwise,
10	  author    = {Robertson, Zachary and Koyejo, Sanmi},
11	  title     = {Let's Measure Information Step-by-Step: {LLM}-Based Evaluation Beyond Vibes},
12	  journal   = {arXiv preprint arXiv:2508.05469},
13	  year      = {2025},
14	  url       = {https://arxiv.org/abs/2508.05469},
15	  note      = {arXiv:2508.05469}
16	}
17	
18	@inproceedings{yang2026diversity,
19	  author    = {Yang, Yingxuan and Qu, Chengrui and Wen, Muning and Shi, Laixi and Wen, Ying and Zhang, Weinan and Wierman, Adam and Gu, Shangding},
20	  title     = {Understanding Agent Scaling in {LLM}-Based Multi-Agent Systems via Diversity},
21	  booktitle = {ICLR 2026 Workshop on AIMS},
22	  year      = {2026},
23	  url       = {https://arxiv.org/abs/2602.03794},
24	  note      = {arXiv:2602.03794}
25	}
26	
27	@article{turkmen2026ensemble,
28	  author    = {Turkmen, Yigit and Buyukates, Baturalp and Bastopcu, Melih},
29	  title     = {Don't Always Pick the Highest-Performing Model: An Information Theoretic View of {LLM} Ensemble Selection},
30	  journal   = {arXiv preprint arXiv:2602.08003},
31	  year      = {2026},
32	  url       = {https://arxiv.org/abs/2602.08003},
33	  note      = {arXiv:2602.08003}
34	}
35	
36	@inproceedings{kaneko2025bits,
37	  author    = {Kaneko, Masahiro and Baldwin, Timothy},
38	  title     = {Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against {LLMs}},
39	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
40	  year      = {2025},
41	  url       = {https://arxiv.org/abs/2510.17000},
42	  note      = {arXiv:2510.17000. Spotlight}
43	}
44	

…[truncated 12184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T15:11:13.145698+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T15:11:13.145844+00:00_

1	\section{Introduction}
2	% [PLACEHOLDER — waiting for plan\_001 results]
3	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T15:11:13.145993+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/methodology.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T15:11:13.146117+00:00_

1	\section{Experimental Methodology}
2	% [PLACEHOLDER — to be written by Worker]
3	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T15:11:13.146237+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T15:11:13.146373+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{amsmath,amssymb,amsthm}
10	\usepackage{booktabs}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{definition}{Definition}
17	\newtheorem{proposition}{Proposition}
18	
19	\title{The Weakest Link: Why Judge Diversity Fails Under\\Adaptive Adversaries in Multi-LLM Evaluation}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	% [PLACEHOLDER — waiting for plan_001 results]
28	\end{abstract}
29	
30	% Section files managed by write_paper_section
31	\input{introduction}    % [PLACEHOLDER — waiting for plan_001 results]
32	\input{related_work}
33	\input{threat_model}
34	\input{methodology}
35	\input{results}          % [PLACEHOLDER — waiting for plan_001 results]
36	\input{analysis}         % [PLACEHOLDER — waiting for plan_001 results]
37	\input{conclusion}       % [PLACEHOLDER — waiting for plan_001 results]
38	
39	\section*{Limitations}
40	% [PLACEHOLDER — short paragraph, ~3 points per EMNLP rules]
41	
42	\bibliography{references}
43	\bibliographystyle{acl_natbib}
44	
45	\end{document}
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T15:11:13.146529+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T15:11:13.146674+00:00_

1	\section{Threat Model and Problem Formulation}
2	% [PLACEHOLDER — to be written by Worker]
3	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T15:11:13.146861+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__read_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__read_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T15:11:13.146987+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T15:11:13.147103+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "cert_manip_resist_eval",
  "file": "paper_framing.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "cert_manip_resist_eval",
    "file": "paper_framing.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T15:11:13.147319+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/paper_framing.md\", \"content\": \"# Paper Framing — cert_manip_resist_eval (v3: Post-Dream Revision)\\n\\n> Last updated: 2026-05-22 | Reason: Dream review (2.5 all tiers) exposed structural issues; reframe novelty, fix theorem, add experiments\\n\\n## Target\\nEMNLP 2026 (via ARR)\\n\\n## Title Candidates\\n1. \\\"The Diversity Trap: Why Adding More Judges Doesn't Make LLM Evaluation Safer\\\"\\n2. \\\"The Weakest Link: Individual Robustness Dominates Diversity in Multi-Judge LLM Evaluation Security\\\"\\n3. \\\"Against the Diversity Assumption: Adaptive Adversaries Break Multi-Judge LLM Evaluation Panels at the Weakest Link\\\"\\n\\n## Core Insight\\nMulti-judge LLM evaluation panels are widely assumed to benefit from judge diversity, analogous to Byzantine Fault Tolerance (BFT) where redundancy protects against faults. We provide the first systematic empirical characterization showing this analogy breaks under adaptive adversaries: BFT assumes random faults, but LLM adversaries target the weakest judge. We quantify this via regime analysis — diversity's protective effect depends on individual judge robustness level and attack transferability — and expose structural barriers (diversity-capability tradeoff, Gaussian copula failure) that prior work has not measured.\\n\\n## Hook\\n\\\"Adding more diverse judges to an evaluation panel doesn't make it safer — it can make it worse.\\\"\\nWe empirically validate and quantify a predicted but unmeasured phenomenon in the LLM judge domain: the failure of diversity-based defenses under adaptive adversaries.\\n\\n## Novelty Positioning (Dream D4 fix)\\nWe do NOT claim to discover that weakest-link effects exist under adaptive adversaries — this is established in security (Schneier 2000) and adversarial ML (Tramèr et al. 2018). Our contributions are:\\n1. **First systematic empirical quantific
…[truncated 10648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T15:11:13.147470+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "cert_manip_resist_eval",
  "file": "literature_map.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "cert_manip_resist_eval",
    "file": "literature_map.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T15:11:13.147743+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/literature_map.yaml\", \"content\": \"papers:\\n  robertson2025tvdmi:\\n    title: \\\"Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes\\\"\\n    authors: [\\\"Robertson\\\", \\\"Koyejo\\\"]\\n    year: 2025\\n    venue: \\\"arXiv (under TMLR review)\\\"\\n    url: \\\"https://arxiv.org/abs/2508.05469\\\"\\n    category: \\\"evaluation_framework\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Foundational TVD-MI theory for LLM evaluation. Theorem 3.3 proves bounded f-divergences (TVD) maintain polynomial certification under mode-collapse attacks while unbounded (KL) fail. We extend from pairwise to N-agent multi-judge settings.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  yang2026diversity_scaling:\\n    title: \\\"Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity\\\"\\n    authors: [\\\"Yang et al.\\\"]\\n    year: 2026\\n    venue: \\\"ICLR 2026 Workshop AIMS\\\"\\n    url: \\\"https://arxiv.org/abs/2602.03794\\\"\\n    category: \\\"multi_agent_scaling\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Information-theoretic diversity-scaling framework: K* = 2^{H(ρ)}, residual uncertainty (1-α_c)^{K*} geometric contraction (Theorem 4.3). We provide the adversarial dual — while their K* governs performance improvement rate, the same correlation structure governs manipulation cost increase rate. Core duality insight.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  turkmen2026copula:\\n    title: \\\"Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection\\\"\\n    authors: [\\\"Turkmen et al.\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.08003\\\"\\n    category: \\\"ensembl
…[truncated 6978 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T15:11:13.148036+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex",
  "content": "\\section{Related Work}\n\n\\paragraph{LLM-as-Judge and Evaluation Biases.}\nThe use of large language models as automatic evaluators gained traction after \\citet{zheng2023judging} introduced MT-Bench and Chatbot Arena, establishing LLM judges as scalable alternatives to human annotation. Subsequent work documented systematic failure modes: \\citet{wang2023fair} showed that individual LLM judges exhibit position bias, verbosity preferences, and sycophancy, all of which compromise evaluation reliability. Multi-judge panels have been proposed to mitigate these biases by aggregating decisions across diverse models. A recent systematization of knowledge on LLM-judge security \\cite{almasoud2026security} reports that 7-model committees reduce attack success rates to 10--19\\%, down from 50--68\\% for individual open-source judges. However, this empirical observation lacks a causal explanation: it does not disentangle whether the reduction stems from judge diversity per se or from the inclusion of individually robust models. We address precisely this gap, providing the first controlled analysis that separates the contributions of panel diversity and individual judge robustness under adaptive attack.\n\n\\paragraph{Adversarial Robustness and Transferability.}\nAdversarial vulnerability in neural networks was formalized by \\citet{goodfellow2015adversarial}, who showed that imperceptible input perturbations can cause misclassification. A key property of such adversarial examples is transferability: \\citet{papernot2016transferability} demonstrated that adversarial inputs crafted for one model frequently fool others, and \\citet{papernot2017practical} exploited this for black-box attacks via substitute models. \\citet{tramer2018ensemble} showed that ensemble adversarial training improves robustness but does not eliminate cross-model vulnerability, because transferred perturbations remain effective across architectures. In the LLM domain, prompt injection attacks \\cite{greshake2023not} and adversarial prompt crafting \\cite{schulhoff2023hackaprompt} exploit analogous transferability: manipulative prompts designed for one judge model frequently succeed against others from the same capability tier. This cross-model attack transferability enables adaptive adversaries to concentrate effort on the weakest panel member, and it forms the empirical basis for the weakest-link effect we quantify.\n\n\\paragraph{Ensemble Diversity and Multi-Agent Scaling.}\nThe theoretical foundations of ensemble diversity trace to \\citet{krogh1995neural}, who proved that ensemble error decomposes into average member error minus a diversity term that measures disagreement among members. For LLM-based multi-agent systems, \\citet{yang2026diversity} formalize this through an information-theoretic framework, defining an effective channel count $K^* = 2^{H(\\rho)}$ that governs performance scaling as a function of the correlation structure. \\citet{turkmen2026ensemble} develop a Gaussian copula model for ensemble selection, deriving error floor bounds that depend on pairwise mutual information rather than individual accuracy alone. On the empirical side, \\citet{kim2025correlated} find that LLM errors are substantially correlated: when two models both err, they agree on the wrong answer 60\\% of the time, with same-company pairs exhibiting 6.6\\% higher agreement. \\citet{kuai2026independent} audit behavioral entanglement across 18 models and find that cross-family entanglement is 40--60\\% lower than within-family entanglement but remains far from zero. \\citet{keppo2026fragility} show that increasing agent count from 2 to 5 disrupts collusive dynamics in cooperative settings. These works study how diversity improves performance under benign conditions. We provide the adversarial security dual: the same correlation structures that govern performance scaling also determine an attacker's ability to simultaneously compromise multiple judges.\n\n\\paragraph{Byzantine Fault Tolerance and Security Analogies.}\nMulti-judge evaluation panels implicitly invoke a Byzantine Fault Tolerance (BFT) analogy: if each judge fails independently, majority voting among $n$ judges tolerates up to $f < n/3$ faulty members \\cite{lamport1982byzantine,castro1999practical}. This classical guarantee assumes that faults are random or arbitrarily chosen but not strategically targeted at system structure. \\citet{schneier2000secrets} articulated the weakest-link principle for security systems: an attacker need only find and exploit the single most vulnerable component, and aggregate redundancy becomes irrelevant. The distinction between random faults and adaptive attacks is well-established in systems security, yet the LLM evaluation community continues to treat judge diversity as if the BFT preconditions hold. We make this implicit analogy explicit and test it empirically: adaptive adversaries violate the independence assumption underlying BFT, and panel security collapses to the robustness of the weakest individual judge.\n\n\\paragraph{Information-Theoretic Approaches to Evaluation.}\nSeveral recent works apply information-theoretic tools to LLM evaluation. \\citet{robertson2025stepwise} propose a TVD-MI framework for stepwise evaluation, proving that bounded divergences maintain polynomial certification under mode-collapse attacks. \\citet{kaneko2025bits} derive tight single-model attack cost bounds via Fano's inequality, establishing that an adversary requires at least $\\log_2(1/\\varepsilon) / I_{\\max}$ queries to reduce detection probability below $\\varepsilon$. For imperfect but honest judges, \\citet{feng2026noisy} develop statistical hypothesis tests with finite-sample Type-I error control despite calibration uncertainty. On the incentive design side, \\citet{chen2025incentivizing} and \\citet{qiu2026truthfulness} apply peer prediction mechanisms to elicit truthful judgments from LLMs under conditional independence assumptions. These lines of work address complementary concerns: statistical validity under noise, single-model attack costs, and truthfulness incentives. Our study fills the remaining gap by examining how adversarial manipulation interacts with multi-judge composition, a setting where neither honest-noise nor single-model assumptions hold.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex",
    "content": "\\section{Related Work}\n\n\\paragraph{LLM-as-Judge and Evaluation Biases.}\nThe use of large language models as automatic evaluators gained traction after \\citet{zheng2023judging} introduced MT-Bench and Chatbot Arena, establishing LLM judges as scalable alternatives to human annotation. Subsequent work documented systematic failure modes: \\citet{wang2023fair} showed that individual LLM judges exhibit position bias, verbosity preferences, and sycophancy, all of which compromise evaluation reliability. Multi-judge panels have been proposed to mitigate these biases by aggregating decisions across diverse models. A recent systematization of knowledge on LLM-judge security \\cite{almasoud2026security} reports that 7-model committees reduce attack success rates to 10--19\\%, down from 50--68\\% for individual open-source judges. However, this empirical observation lacks a causal explanation: it does not disentangle whether the reduction stems from judge diversity per se or from the inclusion of individually robust models. We address precisely this gap, providing the first controlled analysis that separates the contributions of panel diversity and individual judge robustness under adaptive attack.\n\n\\paragraph{Adversarial Robustness and Transferability.}\nAdversarial vulnerability in neural networks was formalized by \\citet{goodfellow2015adversarial}, who showed that imperceptible input perturbations can cause misclassification. A key property of such adversarial examples is transferability: \\citet{papernot2016transferability} demonstrated that adversarial inputs crafted for one model frequently fool others, and \\citet{papernot2017practical} exploited this for black-box attacks via substitute models. \\citet{tramer2018ensemble} showed that ensemble adversarial training improves robustness but does not eliminate cross-model vulnerability, because transferred perturbations remain effective across architectures. In the LLM domain, prompt injection attacks \\cite{greshake2023not} and adversarial prompt crafting \\cite{schulhoff2023hackaprompt} exploit analogous transferability: manipulative prompts designed for one judge model frequently succeed against others from the same capability tier. This cross-model attack transferability enables adaptive adversaries to concentrate effort on the weakest panel member, and it forms the empirical basis for the weakest-link effect we quantify.\n\n\\paragraph{Ensemble Diversity and Multi-Agent Scaling.}\nThe theoretical foundations of ensemble diversity trace to \\citet{krogh1995neural}, who proved that ensemble error decomposes into average member error minus a diversity term that measures disagreement among members. For LLM-based multi-agent systems, \\citet{yang2026diversity} formalize this through an information-theoretic framework, defining an effective channel count $K^* = 2^{H(\\rho)}$ that governs performance scaling as a function of the correlation structure. \\citet{turkmen2026ensemble} develop a Gaussian copula model for ensemble selection, deriving error floor bounds that depend on pairwise mutual information rather than individual accuracy alone. On the empirical side, \\citet{kim2025correlated} find that LLM errors are substantially correlated: when two models both err, they agree on the wrong answer 60\\% of the time, with same-company pairs exhibiting 6.6\\% higher agreement. \\citet{kuai2026independent} audit behavioral entanglement across 18 models and find that cross-family entanglement is 40--60\\% lower than within-family entanglement but remains far from zero. \\citet{keppo2026fragility} show that increasing agent count from 2 to 5 disrupts collusive dynamics in cooperative settings. These works study how diversity improves performance under benign conditions. We provide the adversarial security dual: the same correlation structures that govern performance scaling also determine an attacker's ability to simultaneously compromise multiple judges.\n\n\\paragraph{Byzantine Fault Tolerance and Security Analogies.}\nMulti-judge evaluation panels implicitly invoke a Byzantine Fault Tolerance (BFT) analogy: if each judge fails independently, majority voting among $n$ judges tolerates up to $f < n/3$ faulty members \\cite{lamport1982byzantine,castro1999practical}. This classical guarantee assumes that faults are random or arbitrarily chosen but not strategically targeted at system structure. \\citet{schneier2000secrets} articulated the weakest-link principle for security systems: an attacker need only find and exploit the single most vulnerable component, and aggregate redundancy becomes irrelevant. The distinction between random faults and adaptive attacks is well-established in systems security, yet the LLM evaluation community continues to treat judge diversity as if the BFT preconditions hold. We make this implicit analogy explicit and test it empirically: adaptive adversaries violate the independence assumption underlying BFT, and panel security collapses to the robustness of the weakest individual judge.\n\n\\paragraph{Information-Theoretic Approaches to Evaluation.}\nSeveral recent works apply information-theoretic tools to LLM evaluation. \\citet{robertson2025stepwise} propose a TVD-MI framework for stepwise evaluation, proving that bounded divergences maintain polynomial certification under mode-collapse attacks. \\citet{kaneko2025bits} derive tight single-model attack cost bounds via Fano's inequality, establishing that an adversary requires at least $\\log_2(1/\\varepsilon) / I_{\\max}$ queries to reduce detection probability below $\\varepsilon$. For imperfect but honest judges, \\citet{feng2026noisy} develop statistical hypothesis tests with finite-sample Type-I error control despite calibration uncertainty. On the incentive design side, \\citet{chen2025incentivizing} and \\citet{qiu2026truthfulness} apply peer prediction mechanisms to elicit truthful judgments from LLMs under conditional independence assumptions. These lines of work address complementary concerns: statistical validity under noise, single-model attack costs, and truthfulness incentives. Our study fills the remaining gap by examining how adversarial manipulation interacts with multi-judge composition, a setting where neither honest-noise nor single-model assumptions hold.\n"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T15:11:13.148272+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T15:11:13.148426+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper && wc -w related_work.tex && echo \"---\" && grep -n \"—\" related_work.tex && echo \"NO_EM_DASH\" && grep -n \" – \" related_work.tex && echo \"NO_EN_DASH\" && grep -cE \"ing[,.]\" related_work.tex && echo \"---\" && grep -inE \"it is worth noting|notably|plays a crucial role|delve|leverage|utilize|facilitate|a myriad|a plethora|in this paper|paradigm shift\" related_work.tex && echo \"NO_BANNED_PHRASES\"",
  "description": "Style check on related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper && wc -w related_work.tex && echo \"---\" && grep -n \"—\" related_work.tex && echo \"NO_EM_DASH\" && grep -n \" – \" related_work.tex && echo \"NO_EN_DASH\" && grep -cE \"ing[,.]\" related_work.tex && echo \"---\" && grep -inE \"it is worth noting|notably|plays a crucial role|delve|leverage|utilize|facilitate|a myriad|a plethora|in this paper|paradigm shift\" related_work.tex && echo \"NO_BANNED_PHRASES\"",
    "description": "Style check on related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T15:11:13.148557+00:00_

Exit code 1
756 related_work.tex
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T15:11:13.148702+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper && echo \"=== EM-DASH ===\" && grep -n \"—\" related_work.tex || echo \"NONE\" && echo \"=== EN-DASH ===\" && grep -n \" – \" related_work.tex || echo \"NONE\" && echo \"=== -ing endings ===\" && grep -noE \"[a-z]ing[,.]\" related_work.tex || echo \"NONE\" && echo \"=== BANNED ===\" && grep -inE \"it is worth noting|notably|plays a crucial role|delve|leverage|utilize|facilitate|a myriad|a plethora|in this paper|paradigm shift\" related_work.tex || echo \"NONE\"",
  "description": "Style check for AI writing patterns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper && echo \"=== EM-DASH ===\" && grep -n \"—\" related_work.tex || echo \"NONE\" && echo \"=== EN-DASH ===\" && grep -n \" – \" related_work.tex || echo \"NONE\" && echo \"=== -ing endings ===\" && grep -noE \"[a-z]ing[,.]\" related_work.tex || echo \"NONE\" && echo \"=== BANNED ===\" && grep -inE \"it is worth noting|notably|plays a crucial role|delve|leverage|utilize|facilitate|a myriad|a plethora|in this paper|paradigm shift\" related_work.tex || echo \"NONE\"",
    "description": "Style check for AI writing patterns"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T15:11:13.148835+00:00_

=== EM-DASH ===
NONE
=== EN-DASH ===
NONE
=== -ing endings ===
9:ling.
=== BANNED ===
NONE

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T150758",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-22T15:11:13.148991+00:00_

The "ling." match is from "scaling." (a noun, not a participial phrase). All style checks pass. 756 words, within the target range.

Written to `docs/paper/related_work.tex`. Five `\paragraph{}` blocks covering LLM-as-Judge biases, adversarial transferability, ensemble diversity theory, BFT analogies, and information-theoretic evaluation. Each paragraph ends with explicit positioning against our work. 23 citations total, all keys verified against `references.bib`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_related_work_20260522T150758"
}
```

</details>

---

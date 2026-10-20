# paper writing experiments

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/chats/worker_paper_writing_experiments_20260514T211641.jsonl`
- **Structured JSON:** [`6f7b6f80b01729109433.json`](../../sessions/6f/6f7b6f80b01729109433.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

45 recorded events

### Tool call

_source line 1 · 2026-05-14T21:20:28.536648+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md",
    "limit": "120"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T21:20:28.537189+00:00_

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
…[truncated 815 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T21:20:28.537372+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Check paper structure",
  "subagent_type": "Explore",
  "prompt": "I need to understand the existing paper structure for a LaTeX paper. Please:\n1. List all files in /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/ recursively\n2. Read the main.tex file to understand how sections are included\n3. Check if references.bib exists and list the citation keys available\n4. Check if there's an existing experiments.tex file\n5. Read any existing sections (intro, method, etc.) to understand the notation and terminology used\n\nReport: file listing, how main.tex includes sections, available citation keys, and key terminology/notation from other sections."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Agent",
  "tool_args": {
    "description": "Check paper structure",
    "subagent_type": "Explore",
    "prompt": "I need to understand the existing paper structure for a LaTeX paper. Please:\n1. List all files in /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/ recursively\n2. Read the main.tex file to understand how sections are included\n3. Check if references.bib exists and list the citation keys available\n4. Check if there's an existing experiments.tex file\n5. Read any existing sections (intro, method, etc.) to understand the notation and terminology used\n\nReport: file listing, how main.tex includes sections, available citation keys, and key terminology/notation from other sections."
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T21:20:28.537546+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/ -type f 2>/dev/null | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/ -type f 2>/dev/null | head -50"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T21:20:28.537726+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/_acl_template/formatting.md
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/_acl_template/.git/logs/HEAD
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/_acl_template/.git/logs/refs/heads/master
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/_acl_template/.git/logs/refs/remotes/origin/HEAD
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/_acl_template/.git/index
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/_acl_template/.git/packed-refs
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/_acl_template/.git/objects/pack/pack-318a42012d9bccf84541e32464a1b84e874c3fdb.rev
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/_acl_template/.git/objects/pack/pack-318a42012d9bccf84541e32464a1b84e874c3fdb.pack
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/_acl_template/.git/objects/pack/pack-318a42012d9bccf84541e32464a1b84e874c3fdb.idx
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/_acl_template/.git/description
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/_acl_template/.git/shallow
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/_acl_template/.git/config
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/_acl_template/.git/hooks/applypatch-msg.sample
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/pa
…[truncated 3118 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T21:20:28.537901+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/ -maxdepth 1 -type f 2>/dev/null | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/ -maxdepth 1 -type f 2>/dev/null | sort"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T21:20:28.538025+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T21:20:28.538150+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T21:20:28.538271+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\newcommand{\todo}[1]{\textcolor{red}{[TODO: #1]}}
20	\newcommand{\goldset}[1]{\textcolor{blue}{[GOLD\_SET: #1]}}
21	
22	\title{Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\input{sections/abstract}
30	\input{sections/introduction}
31	\input{sections/related_work}
32	\input{sections/method}
33	\input{sections/experiments}
34	\input{sections/analysis}
35	\input{sections/conclusion}
36	
37	\section*{Limitations}
38	\input{sections/limitations}
39	
40	\bibliography{references}
41	\bibliographystyle{acl_natbib}
42	
43	\appendix
44	\input{sections/appendix}
45	
46	\end{document}
47	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T21:20:28.538410+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/ -type f 2>/dev/null | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/ -type f 2>/dev/null | sort"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T21:20:28.538524+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T21:20:28.538643+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T21:20:28.538814+00:00_

1	% ==============================================================
2	% CATEGORY: direct-competitor
3	% ==============================================================
4	
5	@article{xi2025agentprm,
6	  title   = {AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress},
7	  author  = {Zhiheng Xi and Chenyang Liao and Guanyu Li and others},
8	  journal = {arXiv preprint arXiv:2511.08325},
9	  year    = {2025},
10	}
11	
12	@article{choudhury2025prm,
13	  title   = {Process Reward Models for LLM Agents: Practical Framework and Directions},
14	  author  = {Sanjiban Choudhury},
15	  journal = {arXiv preprint arXiv:2502.10325},
16	  year    = {2025},
17	}
18	
19	@article{li2026toolprmbench,
20	  title   = {ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents},
21	  author  = {Dawei Li and Yuguang Yao and Zhen Tan and Huan Liu and Ruocheng Guo},
22	  journal = {arXiv preprint arXiv:2601.12294},
23	  year    = {2026},
24	}
25	
26	@article{wang2026planrewardbench,
27	  title   = {Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling},
28	  author  = {Jiaxuan Wang and Yulan Hu and Wenjin Yang and others},
29	  journal = {arXiv preprint arXiv:2604.08178},
30	  year    = {2026},
31	}
32	
33	@inproceedings{chen2025monitoring,
34	  title     = {Monitoring LLM Agents for Sequentially Contextual Harm},
35	  author    = {Yueh-Han Chen and Neelay Joshi and Yulin Chen and He He and Rico Angell},
36	  booktitle = {ICLR 2025 Workshop on Building Trust in Language Models and Applications},
37	  year      = {2025},
38	}
39	
40	@article{kale2025weaktostrong,
41	  title   = {Reliable Weak-to-Strong Monitoring of LLM Agents},
42	  author  = {Neil Kale and Chen Bo Calvin Zhang and Kevin Zhu and others},
43	  journal = {arXiv preprint arXiv:2508.19461},
44	  year    = {2025},
45	}
46	
47	@article{fan2026agentrm,
48	  title   = {Exploring Reasoning Reward Model for Agents},
49	  author  = {Kaixuan Fan and Kaituo Feng
…[truncated 10271 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T21:20:28.538965+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/references.bib",
  "offset": "286"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/references.bib",
    "offset": "286"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T21:20:28.539081+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (286). The file has 286 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T21:20:28.539214+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe -name \"*.tex\" -type f 2>/dev/null | grep -v \"_acl_template\" | grep -v \".git\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe -name \"*.tex\" -type f 2>/dev/null | grep -v \"_acl_template\" | grep -v \".git\""
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T21:20:28.539336+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/dream_reports/dream_20260514T081656/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/dream_reports/dream_20260514T081656/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/dream_reports/dream_20260514T081656/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/dream_reports/dream_20260514T095527/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/dream_reports/dream_20260514T095527/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/dream_reports/dream_20260514T095527/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/dream_reports/dream_20260514T184058/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/dream_reports/dream_20260514T184058/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/dream_reports/dream_20260514T184058/best/paper.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T21:20:28.539465+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/ 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T21:20:28.539582+00:00_

total 92
drwxr-xr-x 4 ubuntu ubuntu  4096 May 14 21:11 .
drwxr-xr-x 4 ubuntu ubuntu  4096 May 14 05:47 ..
drwxr-xr-x 3 ubuntu ubuntu  4096 May 14 21:08 _acl_template
-rw-r--r-- 1 ubuntu ubuntu 11615 May 14 21:08 acl.sty
-rw-r--r-- 1 ubuntu ubuntu 45186 May 14 21:08 acl_natbib.bst
-rw-r--r-- 1 ubuntu ubuntu  1000 May 14 21:09 main.tex
-rw-r--r-- 1 ubuntu ubuntu 11235 May 14 20:52 references.bib
drwxr-xr-x 2 ubuntu ubuntu  4096 May 14 21:11 sections

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T21:20:28.539722+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/ 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T21:20:28.539846+00:00_

total 8
drwxr-xr-x 2 ubuntu ubuntu 4096 May 14 21:11 .
drwxr-xr-x 4 ubuntu ubuntu 4096 May 14 21:11 ..

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T21:20:28.539965+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/dream_reports/dream_20260514T184058/best/paper.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/dream_reports/dream_20260514T184058/best/paper.tex",
    "limit": "150"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T21:20:28.540106+00:00_

1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{amsmath}
8	\usepackage{amssymb}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{url}
12	\usepackage[hidelinks]{hyperref}
13	\usepackage{natbib}
14	\renewcommand{\bibsection}{\section*{References}}
15	
16	\title{Stagnation Signals Are Structural, Not Semantic:\\A Systematic Empirical Study of Progress Detection in LLM Agents}
17	
18	\author{Anonymous}
19	
20	\date{}
21	
22	\begin{document}
23	\maketitle
24	
25	\begin{abstract}
26	LLM-based agents frequently stagnate during long-horizon tasks---executing superficially diverse but collectively ineffective action sequences.
27	We present a systematic empirical study of progress stagnation detection through weak supervision, evaluating structural features, neural embedding probes, and LLM-as-judge baselines against 650 human-annotated gold windows.
28	Our central finding is that stagnation signals are fundamentally structural: a gradient-boosted classifier over 30 hand-crafted features (command repetition ratio, file diff frequency, etc.)\ achieves 0.89 macro-F1 on gold labels, surpassing both GRU embedding probes (0.81) and Claude Sonnet LLM-as-judge (0.67) while incurring near-zero cost and sub-millisecond latency.
29	We quantify the circular evaluation artifact inherent in weak supervision: in-domain F1 drops from 0.995 to 0.89 on gold ($\sim$10.5\,pp circular component), but structural dominance is preserved.
30	We further discover that labeling functions exhibit systematic temporal dynamics---command repetition leads stagnation onset by $\sim$1.6 steps while outcome signals lag by +7.2 steps---with 80\% alignment between LF-derived and gold-validated onset boundaries.
31	Despite these temporal patterns motivating a temporal label model, three implementations (TWV, HMM, lag-aware HMM) all fail to improve over majority vote.
…[truncated 8536 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T21:20:28.540250+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe -maxdepth 1 -type f 2>/dev/null | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe -maxdepth 1 -type f 2>/dev/null | sort"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T21:20:28.540365+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/ROADMAP.lock
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/ROADMAP.md
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/data_volume_control.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/decisions.lock
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/dream_registry.lock
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/dream_registry.yaml.bak
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/evaluate_gold_set.py
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/experiment_plan.lock
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/memory.md
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/registry.lock
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/report.md
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/study_status.lock
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T21:20:28.540498+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T21:20:28.540635+00:00_

1	# Paper Framing — agent_progress_probe
2	
3	## Target Venue
4	- Primary: EMNLP 2026 ARR (submission deadline: May 25, 2026; commitment: August 2, 2026)
5	- Format: Long paper (8 pages + appendix)
6	- Track: LLM Agents
7	- Paper type: **Empirical analysis paper**（D039 pivot: 从 method paper 转 empirical study）
8	- Fallback: ACL 2026 ARR August cycle (~August 15 deadline)
9	
10	## Core Claims (3 条) — D039 Pivot
11	
12	1. **Stagnation Signals Are Structural, Not Semantic (primary contribution)**: 系统性对比发现 agent stagnation 信号本质是结构性的——30 个结构特征（命令重复率、唯一命令比、文件 diff 频率等）在 in-domain (RF 0.9951) 和 cross-agent (GB 0.967) 都近完美预测停滞，全面优于 NL embedding probe (in-domain 0.906, cross-domain 0.751) 和 LLM-as-judge (+24.3pp)。Encoder-agnostic（3 个 encoder 均 >0.90）；最优窗口 k=5 (0.9309)；data scaling 10%→100% 单调递增。这揭示：(a) stagnation detection 不需要语义理解——简单结构特征已足够；(b) 结构特征天然跨 agent 迁移（不依赖 embedding domain adaptation）；(c) NL embedding 对 stagnation detection 无增量价值。**改变社区对 agent monitoring 方法选型的认知：从昂贵的表示学习转向轻量结构监控。** Gold set 验证 structural features 是否检测到真实 stagnation（非仅 circular eval artifact）是论文成立的关键。
13	
14	2. **LF Temporal Dynamics Are Systematic but Agent-Specific (analytical contribution)**: LFs 在 trajectory 上展现**系统性但 agent-specific 的**时序角色。SWE-Agent 上：cmd_rep leading (-1.87步)、file_diff concurrent (-1.2步)、OB lagging (+6.7步)。**OH 上 cmd_rep 角色反转**（从 leading 变 lagging +3.32步），而 file_diff（leading, -4.9步）和 OB（lagging, +18.1步）跨域一致。**消融验证：去掉 cmd_rep 后 OH F1 从 0.7512 飙升到 0.9272（+21.6pp）**，证明 cmd_rep 在 OH 上是噪声源而非信号。根因：cmd_rep 在 OH 上 92.3% firing rate + 71% FP，失去区分性。这揭示 LF 行为与 agent 架构之间的交互效应——为 weak supervision pipeline 在 sequential agent data 上的设计提供实证指导。同时量化 circular evaluation 问题：structural features 以 0.9951 F1 逆向工程 LF 标签，证明 LF-derived labels 上的高分不等于真实检测能力。
15	
16	3. **Temporal Label Model: A Well-Motivated Negative Finding (D039 negative result)**: 标准 data programming（majority vote）在 agent trajectory 上违反 i.i.d. 假设——LFs 产生系统性时序动态，这 motivate 了 temporal label model（TLM）的开发。然而，三种 TLM 实现**均未能超越简单 MV**：(a) *
…[truncated 7312 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T21:20:28.540813+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -E \"^@\" /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/references.bib | wc -l"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -E \"^@\" /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/references.bib | wc -l"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T21:20:28.540929+00:00_

38

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T21:20:28.541051+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -E \"^@\" /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/references.bib | sed 's/@.*{\\(.*\\),/\\1/' | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -E \"^@\" /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/references.bib | sed 's/@.*{\\(.*\\),/\\1/' | sort"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T21:20:28.541165+00:00_

bahdanau2015attention
cemri2025multiagentfail
chen2024bgem3
chen2025monitoring
cho2014gru
choudhury2025prm
dawid1979em
fan2026agentrm
fu2020flyingsquid
george2025cycledetection
huang2024selfcorrect
jimenez2024swebench
kale2025weaktostrong
kamoi2024selfcorrection
khosla2020supcon
li2026toolprmbench
liu2026trajad
nguyen2017hmmcrowd
orlanski2026slopcodebench
pipis2025reasoningloop
qiu2026dataprm
ratner2016dataprogramming
ratner2017snorkel
safranchik2020linkedhmm
sala2019multiresolution
shinn2023reflexion
wang2024e5
wang2024mint
wang2025openhands
wang2026planrewardbench
xi2025agentprm
yang2024sweagent
yao2023tot
zhang2021wrench
zhang2025qwen3embedding
zhou2024lats
zhou2024webarena
zhu2025agentfail

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T21:20:28.541353+00:00_

Excellent! Now let me compile the comprehensive report:

## Paper Structure Report: agent_progress_probe

### 1. FILE LISTING (Paper Directory)

**Main paper directory**: `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/`

**Files at root level**:
- `main.tex` — Main entry point for the LaTeX document
- `references.bib` — Bibliography file with 38 citations
- `acl.sty` — ACL style file for formatting
- `acl_natbib.bst` — Bibliographic style file (natbib-compatible)
- `_acl_template/` — Template directory (not used in main compilation)

**Sections directory**: `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/`
- Currently **EMPTY** — all section files need to be created

### 2. HOW MAIN.TEX INCLUDES SECTIONS

The `main.tex` file uses `\input{}` commands to include 7 sections in sequence:

```latex
\input{sections/abstract}
\input{sections/introduction}
\input{sections/related_work}
\input{sections/method}
\input{sections/experiments}
\input{sections/analysis}
\input{sections/conclusion}
\input{sections/limitations}  % (under \section*{Limitations})
\input{sections/appendix}     % (under \appendix)
```

**Document class**: `article` with `[review]` option using the `acl` package (11pt font)

**Custom commands defined**:
- `\todo[1]` — Highlights TODOs in red
- `\goldset[1]` — Highlights gold set annotations in blue

**Bibliography settings**:
- `\bibliography{references}` — Uses the local `references.bib` file
- `\bibliographystyle{acl_natbib}` — Uses the ACL natbib-compatible style

### 3. AVAILABLE CITATION KEYS (38 total)

**Direct Competitors (Progress Reward Models / Agent Stagnation)**:
- `xi2025agentprm` — AgentPRM: Process Reward Models via Step-Wise Promise and Progress
- `choudhury2025prm` — Process Reward Models for LLM Agents: Practical Framework
- `li2026toolprmbench` — ToolPRMBench: Evaluating Process Reward Models
- `wang2026planrewardbench` — Aligning Agents via Plan
…[truncated 7631 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Agent",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T21:20:28.541534+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/",
  "description": "Check sections directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/",
    "description": "Check sections directory"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T21:20:28.541673+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T21:20:28.541838+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
  "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate stagnation detection across four axes: in-domain accuracy, cross-agent transfer, robustness to design choices, and temporal dynamics of labeling functions.\nAll reported metrics are evaluated against silver labels derived from majority vote over three labeling functions (\\S\\ref{sec:method}).\n\n\\paragraph{Circular evaluation caveat.}\nStructural features (command repetition ratios, file operation counts, edit distances) are computed from the same signals that the labeling functions use to produce silver labels.\nConsequently, the in-domain structural F1 of 0.9951 reflects an upper bound on how well these features can \\emph{reverse-engineer} the labeling functions, not detection accuracy against true ground truth.\nThe cross-agent evaluation on OpenHands (0.967 macro-F1) is non-circular: models trained on SWE-Agent LF distributions are tested on a different agent whose LF firing patterns differ substantially (\\S\\ref{sec:cmd_rep_ablation}).\nA human-annotated gold set provides the definitive non-circular evaluation (\\S\\ref{sec:gold_set}).\n\n%-------------------------------------------------------------------\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe extract sliding windows of $k{=}5$ consecutive actions from agent trajectories.\n\\textbf{SWE-Agent} trajectories from SWE-bench \\citep{jimenez2024swebench,yang2024sweagent} yield 54,809 windows with a stagnation ratio of 28.5\\%.\n\\textbf{OpenHands} (OH) trajectories \\citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 6.6\\%.\nSilver labels are produced by majority vote over three labeling functions; confidence equals the number of agreeing LFs (1--3).\nUnless stated otherwise, evaluation uses the conf${\\geq}$2 subset: $N{=}1{,}824$ for SWE-Agent (485 stagnation, 1,339 progress) and $N{=}43{,}376$ for OH.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrc}\n\\toprule\n\\textbf{Agent} & \\textbf{Source} & \\textbf{Windows} & \\textbf{Stag\\,\\%} & \\textbf{Conf${\\geq}$2} \\\\\n\\midrule\nSWE-Agent & SWE-bench & 54,809 & 28.5 & 15,401 \\\\\nOpenHands & CodeAct   & 150,652 & 6.6 & 43,376 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Dataset statistics. Stagnation ratios differ substantially across agents, reflecting different action distributions.}\n\\label{tab:dataset_stats}\n\\end{table}\n\n\\paragraph{Detection methods.}\n(1)~\\textbf{Structural features}: 30 hand-crafted features (repetition rates, file operation counts, edit distances, output entropy) fed to Logistic Regression (LR), Random Forest (RF), and Gradient Boosting (GB).\n(2)~\\textbf{ProgressProbe}: Qwen3-Embedding-0.6B \\citep{zhang2025qwen3embedding} embeddings (1024-dim) processed by a 2-layer GRU \\citep{cho2014gru} with attention \\citep{bahdanau2015attention} (hidden$=$256, dropout$=$0.3), early-stopped at epoch~3 with patience~5.\n(3)~\\textbf{Mean-pool + LR}: Mean-pooled Qwen3 embeddings with logistic regression.\n(4)~\\textbf{LLM-as-Judge}: Claude Sonnet zero-shot window-level classification (\\$11.66 API cost for the SWE test set).\n(5)~\\textbf{Cosine similarity}: Cosine distance between consecutive window embeddings with a validation-tuned threshold.\n\n\\paragraph{Metrics.}\nMacro-F1 is the primary metric. We also report per-class F1 for stagnation (F1\\textsubscript{stag}) and progress (F1\\textsubscript{prog}).\n\n%-------------------------------------------------------------------\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main_results} presents in-domain results on the SWE-Agent conf${\\geq}$2 test set and cross-agent transfer to OpenHands.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{l ccc cc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{SWE-Agent In-Domain} (conf${\\geq}$2)} & \\multicolumn{2}{c}{\\textbf{OpenHands Transfer}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\n\\textbf{Method} & Macro-F1 & F1\\textsubscript{stag} & F1\\textsubscript{prog} & All & Conf${\\geq}$2 \\\\\n\\midrule\nStructural RF$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & 0.9123 & \\textbf{0.9959} \\\\\nStructural GB$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & \\textbf{0.9674} & \\underline{0.9919} \\\\\nStructural LR$^\\dagger$       & 0.9874 & 0.9815 & 0.9933 & 0.7801 & 0.9671 \\\\\nProgressProbe (GRU)           & \\underline{0.9055} & 0.8593 & 0.9518 & 0.5280 & --- \\\\\n\\quad + full OH fine-tune      & ---    & ---    & ---    & 0.7510 & --- \\\\\nMean-pool + LR                & 0.8435 & 0.7620 & 0.9250 & ---    & --- \\\\\nLLM-as-Judge                  & 0.6625 & 0.6055 & 0.7195 & ---    & --- \\\\\nCosine Similarity             & 0.5606 & ---    & ---    & ---    & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Stagnation detection results. In-domain evaluation on SWE-Agent conf${\\geq}$2 test set ($N{=}1{,}824$) and zero-shot cross-agent transfer to OpenHands. $^\\dagger$Structural metrics are evaluated against LF-derived labels and reflect LF-reconstructibility rather than ground-truth accuracy (see circular evaluation caveat). Best in \\textbf{bold}, second-best \\underline{underlined}.}\n\\label{tab:main_results}\n\\end{table*}\n\nIn-domain, structural RF achieves 0.9951 macro-F1, exceeding the GRU probe by 8.96 percentage points (pp) and the LLM judge by 24.3\\,pp.\nHowever, the structural--probe gap is inflated by circular evaluation: structural features reconstruct the LFs that generated the labels.\nThe more informative comparison is among non-circular methods: the GRU probe outperforms mean-pool~+~LR by 6.2\\,pp, confirming that temporal modeling within windows adds value beyond static embedding aggregation.\nThe LLM judge underperforms all learned methods despite substantially higher cost.\n\n%-------------------------------------------------------------------\n\\subsection{Cross-Agent Transfer}\n\\label{sec:cross_agent}\n\nTable~\\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.\nStructural GB transfers best, achieving 0.967 macro-F1 on all OH windows---21.6\\,pp above the probe fine-tuned on 100\\% of OH data (0.751).\nRF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.\nBoth structural models recover to $>$0.99 on conf${\\geq}$2 OH windows, where label noise is lower.\n\nThe probe's zero-shot transfer (0.528) is near chance, and even full OH fine-tuning only reaches 0.751.\nThis asymmetry---structural features transfer naturally while learned embeddings do not---is a central empirical finding: stagnation manifests in action-level structure that generalizes across agents.\n\n\\paragraph{Multi-seed stability.}\nStructural RF: $0.9951{\\pm}0.0000$ in-domain (5 seeds, zero variance); GB cross-agent: $0.9678{\\pm}0.0015$.\nThe probe shows higher variance: $0.9185{\\pm}0.0113$, though all seeds exceed 0.90.\n\n%-------------------------------------------------------------------\n\\subsection{Robustness Analysis}\n\\label{sec:robustness}\n\n\\paragraph{Encoder ablation.}\nReplacing Qwen3-0.6B with BGE-M3 \\citep{chen2024bgem3} or E5-large-v2 \\citep{wang2024e5} yields probe macro-F1 of 0.9413 and 0.9363, respectively (vs.\\ 0.9055 for Qwen3).\nAll encoders exceed 0.90, indicating the probe's temporal architecture, not a specific encoder, drives performance. Full results appear in Appendix Table~\\ref{tab:encoder_ablation}.\n\n\\paragraph{Window size.}\n$k{=}5$ is optimal (0.9309 macro-F1); $k{=}3$ drops 5.9\\,pp and $k{=}7$ drops 1.8\\,pp.\nShorter windows lack sufficient context; longer windows dilute signal by spanning both progress and stagnation phases.\nDetails in Appendix Table~\\ref{tab:window_ablation}.\n\n\\paragraph{Data scaling.}\nFigure~\\ref{fig:data_scaling} shows probe performance scales monotonically from 0.8054 (10\\% training data) to 0.9055 (100\\%), with structural RF providing a ceiling at 0.9951 (dashed line).\nThe curve has not plateaued, suggesting larger trajectory corpora could further close the structural--probe gap.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_data_scaling.pdf}\n\\caption{Probe macro-F1 vs.\\ training data fraction. Structural RF ceiling shown as dashed line. Performance scales monotonically but has not saturated at 100\\% data.}\n\\label{fig:data_scaling}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Labeling Function Temporal Dynamics}\n\\label{sec:lf_temporal}\n\nWe analyze when each LF first fires relative to the onset of stagnation episodes (Table~\\ref{tab:lf_temporal}, Figure~\\ref{fig:lf_temporal}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{LF} & \\textbf{Lag} & \\textbf{Lead\\,\\%} & \\textbf{Conc.\\,\\%} & \\textbf{Lag\\,\\%} \\\\\n\\midrule\ncmd\\_rep      & $-1.87$ & 36.1 & --- & --- \\\\\nfile\\_diff    & $-1.20$ & 17.1 & --- & --- \\\\\noutcome\\_bp   & $+6.70$ & ---  & --- & 48.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal roles of labeling functions on SWE-Agent. Lag = mean steps relative to stagnation onset (negative = leading). Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; all pairwise comparisons significant after Bonferroni correction.}\n\\label{tab:lf_temporal}\n\\end{table}\n\nThe three LFs occupy distinct temporal niches.\nCommand repetition leads stagnation onset by 1.87 steps on average, making it an early warning signal.\nFile diff is near-concurrent ($-1.20$ steps).\nOutcome backpropagation lags by 6.70 steps, acting as a retrospective confirmation.\n\nAll pairwise differences are significant (Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; Bonferroni-corrected pairwise: cmd\\_rep vs.\\ file\\_diff $p{=}1.44{\\times}10^{-26}$, cmd\\_rep vs.\\ outcome\\_bp $p{=}6.67{\\times}10^{-39}$, file\\_diff vs.\\ outcome\\_bp $p{=}3.47{\\times}10^{-47}$).\n\n\\paragraph{Cross-agent reversal.}\nOn OpenHands, cmd\\_rep shifts from leading ($-1.87$) to lagging ($+3.32$ steps).\nThis reversal explains the cmd\\_rep pathology analyzed in \\S\\ref{sec:cmd_rep_ablation}: OH's action distribution triggers cmd\\_rep on progress windows, inverting its diagnostic value.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_lf_temporal.pdf}\n\\caption{Temporal roles of labeling functions relative to stagnation onset on SWE-Agent. cmd\\_rep leads ($-1.87$ steps), file\\_diff is near-concurrent ($-1.20$), outcome\\_bp lags ($+6.70$). Inset: OH reversal where cmd\\_rep becomes lagging.}\n\\label{fig:lf_temporal}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Command Repetition Ablation}\n\\label{sec:cmd_rep_ablation}\n\nThe cmd\\_rep LF fires on 92.3\\% of OH windows (vs.\\ 65.6\\% on SWE-Agent), with a 71\\% false positive rate on OH progress windows.\nTable~\\ref{tab:cmd_rep_ablation} shows the effect of removing it.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{LF Config} & \\textbf{ZS F1} & \\textbf{FT F1} & \\textbf{FT F1\\textsubscript{s}} & \\textbf{FT F1\\textsubscript{p}} \\\\\n\\midrule\n3-LF (w/ cmd\\_rep) & 0.530 & 0.751 & 0.544 & 0.959 \\\\\n2-LF (no cmd\\_rep) & 0.607 & \\textbf{0.927} & 0.938 & 0.917 \\\\\n\\midrule\n$\\Delta$ & +7.7\\,pp & +17.6\\,pp & +39.4\\,pp & $-4.2$\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Effect of removing cmd\\_rep on OpenHands probe performance. ZS = zero-shot transfer from SWE-Agent; FT = fine-tuned on 100\\% OH data. F1\\textsubscript{s}/F1\\textsubscript{p} = stagnation/progress F1.}\n\\label{tab:cmd_rep_ablation}\n\\end{table}\n\nRemoving cmd\\_rep improves zero-shot transfer by 7.7\\,pp and fine-tuned performance by 17.6\\,pp.\nThe gain is driven almost entirely by stagnation recall (+39.4\\,pp F1\\textsubscript{stag}), at a modest cost to progress detection ($-4.2$\\,pp F1\\textsubscript{prog}).\nThe 3-LF fine-tuned model's stagnation F1 of 0.544 reveals that cmd\\_rep corrupts silver labels so thoroughly that even full fine-tuning on OH data cannot recover.\nThis motivates agent-specific LF selection: labeling functions validated on one agent architecture may become adversarial on another.\n\n%-------------------------------------------------------------------\n\\subsection{Temporal Label Models}\n\\label{sec:temporal_label_models}\n\nWe investigate whether incorporating LF temporal dynamics into label aggregation improves over majority vote (MV).\nTable~\\ref{tab:temporal_models} compares three temporal label models \\citep{ratner2017snorkel,safranchik2020linkedhmm}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Conf${\\geq}$2 F1} & \\textbf{MV Agr.} & \\textbf{Probe F1$^\\ddagger$} \\\\\n\\midrule\nMV (baseline) & 0.8946$^\\ast$ & 1.000 & 0.8468 \\\\\nTWV ($\\sigma{=}2$) & \\textbf{0.9003} & 0.885 & 0.8211 \\\\\nLag-HMM & 0.8936 & 0.820 & --- \\\\\nHMM & 0.7502 & 0.685 & 0.6564 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal label model comparison. $^\\ast$MV conf${\\geq}$2 F1 is a self-evaluation baseline (MV evaluated against itself on high-confidence windows). $^\\ddagger$Downstream: probe trained on each method's labels, evaluated on SWE-Agent conf${\\geq}$2 vs.\\ MV labels.}\n\\label{tab:temporal_models}\n\\end{table}\n\nTWV achieves the highest conf${\\geq}$2 F1 (0.9003, +0.57\\,pp over MV), but this gain does not propagate downstream: a probe trained on TWV labels scores 0.8211 vs.\\ 0.8468 for MV-trained ($-2.57$\\,pp).\nTWV flips 14.1\\% of conf$=$1 labels, introducing noise that hurts probe training.\nHMM overpredicts stagnation (29,176 stagnation vs.\\ 25,633 progress windows), degrading downstream performance to 0.6564.\nLag-HMM closely tracks MV ($-0.1$\\,pp) despite explicitly modeling temporal offsets, suggesting that the temporal structure captured by individual LFs does not improve \\emph{aggregation}.\n\n\\paragraph{TWV sensitivity.}\nThe Gaussian kernel bandwidth $\\sigma$ is critical: $\\sigma{=}2$ is optimal (0.9003); $\\sigma{=}1$ drops to 0.8105 and $\\sigma{\\geq}5$ falls below 0.81.\nThis narrow operating range, combined with the downstream degradation, makes TWV impractical as a drop-in MV replacement.\n\nThese results constitute a negative finding: despite clear temporal structure in LF firing patterns (\\S\\ref{sec:lf_temporal}), temporal label models do not improve over simple majority vote for downstream stagnation detection.\n\n%-------------------------------------------------------------------\n\\subsection{Gold Set Validation}\n\\label{sec:gold_set}\n\\goldset{Human-annotated gold set (650 windows) validation pending. Results will be added upon completion (expected 2026-05-17). This provides the non-circular ground truth evaluation for all methods.}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
    "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate stagnation detection across four axes: in-domain accuracy, cross-agent transfer, robustness to design choices, and temporal dynamics of labeling functions.\nAll reported metrics are evaluated against silver labels derived from majority vote over three labeling functions (\\S\\ref{sec:method}).\n\n\\paragraph{Circular evaluation caveat.}\nStructural features (command repetition ratios, file operation counts, edit distances) are computed from the same signals that the labeling functions use to produce silver labels.\nConsequently, the in-domain structural F1 of 0.9951 reflects an upper bound on how well these features can \\emph{reverse-engineer} the labeling functions, not detection accuracy against true ground truth.\nThe cross-agent evaluation on OpenHands (0.967 macro-F1) is non-circular: models trained on SWE-Agent LF distributions are tested on a different agent whose LF firing patterns differ substantially (\\S\\ref{sec:cmd_rep_ablation}).\nA human-annotated gold set provides the definitive non-circular evaluation (\\S\\ref{sec:gold_set}).\n\n%-------------------------------------------------------------------\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe extract sliding windows of $k{=}5$ consecutive actions from agent trajectories.\n\\textbf{SWE-Agent} trajectories from SWE-bench \\citep{jimenez2024swebench,yang2024sweagent} yield 54,809 windows with a stagnation ratio of 28.5\\%.\n\\textbf{OpenHands} (OH) trajectories \\citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 6.6\\%.\nSilver labels are produced by majority vote over three labeling functions; confidence equals the number of agreeing LFs (1--3).\nUnless stated otherwise, evaluation uses the conf${\\geq}$2 subset: $N{=}1{,}824$ for SWE-Agent (485 stagnation, 1,339 progress) and $N{=}43{,}376$ for OH.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrc}\n\\toprule\n\\textbf{Agent} & \\textbf{Source} & \\textbf{Windows} & \\textbf{Stag\\,\\%} & \\textbf{Conf${\\geq}$2} \\\\\n\\midrule\nSWE-Agent & SWE-bench & 54,809 & 28.5 & 15,401 \\\\\nOpenHands & CodeAct   & 150,652 & 6.6 & 43,376 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Dataset statistics. Stagnation ratios differ substantially across agents, reflecting different action distributions.}\n\\label{tab:dataset_stats}\n\\end{table}\n\n\\paragraph{Detection methods.}\n(1)~\\textbf{Structural features}: 30 hand-crafted features (repetition rates, file operation counts, edit distances, output entropy) fed to Logistic Regression (LR), Random Forest (RF), and Gradient Boosting (GB).\n(2)~\\textbf{ProgressProbe}: Qwen3-Embedding-0.6B \\citep{zhang2025qwen3embedding} embeddings (1024-dim) processed by a 2-layer GRU \\citep{cho2014gru} with attention \\citep{bahdanau2015attention} (hidden$=$256, dropout$=$0.3), early-stopped at epoch~3 with patience~5.\n(3)~\\textbf{Mean-pool + LR}: Mean-pooled Qwen3 embeddings with logistic regression.\n(4)~\\textbf{LLM-as-Judge}: Claude Sonnet zero-shot window-level classification (\\$11.66 API cost for the SWE test set).\n(5)~\\textbf{Cosine similarity}: Cosine distance between consecutive window embeddings with a validation-tuned threshold.\n\n\\paragraph{Metrics.}\nMacro-F1 is the primary metric. We also report per-class F1 for stagnation (F1\\textsubscript{stag}) and progress (F1\\textsubscript{prog}).\n\n%-------------------------------------------------------------------\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main_results} presents in-domain results on the SWE-Agent conf${\\geq}$2 test set and cross-agent transfer to OpenHands.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{l ccc cc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{SWE-Agent In-Domain} (conf${\\geq}$2)} & \\multicolumn{2}{c}{\\textbf{OpenHands Transfer}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\n\\textbf{Method} & Macro-F1 & F1\\textsubscript{stag} & F1\\textsubscript{prog} & All & Conf${\\geq}$2 \\\\\n\\midrule\nStructural RF$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & 0.9123 & \\textbf{0.9959} \\\\\nStructural GB$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & \\textbf{0.9674} & \\underline{0.9919} \\\\\nStructural LR$^\\dagger$       & 0.9874 & 0.9815 & 0.9933 & 0.7801 & 0.9671 \\\\\nProgressProbe (GRU)           & \\underline{0.9055} & 0.8593 & 0.9518 & 0.5280 & --- \\\\\n\\quad + full OH fine-tune      & ---    & ---    & ---    & 0.7510 & --- \\\\\nMean-pool + LR                & 0.8435 & 0.7620 & 0.9250 & ---    & --- \\\\\nLLM-as-Judge                  & 0.6625 & 0.6055 & 0.7195 & ---    & --- \\\\\nCosine Similarity             & 0.5606 & ---    & ---    & ---    & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Stagnation detection results. In-domain evaluation on SWE-Agent conf${\\geq}$2 test set ($N{=}1{,}824$) and zero-shot cross-agent transfer to OpenHands. $^\\dagger$Structural metrics are evaluated against LF-derived labels and reflect LF-reconstructibility rather than ground-truth accuracy (see circular evaluation caveat). Best in \\textbf{bold}, second-best \\underline{underlined}.}\n\\label{tab:main_results}\n\\end{table*}\n\nIn-domain, structural RF achieves 0.9951 macro-F1, exceeding the GRU probe by 8.96 percentage points (pp) and the LLM judge by 24.3\\,pp.\nHowever, the structural--probe gap is inflated by circular evaluation: structural features reconstruct the LFs that generated the labels.\nThe more informative comparison is among non-circular methods: the GRU probe outperforms mean-pool~+~LR by 6.2\\,pp, confirming that temporal modeling within windows adds value beyond static embedding aggregation.\nThe LLM judge underperforms all learned methods despite substantially higher cost.\n\n%-------------------------------------------------------------------\n\\subsection{Cross-Agent Transfer}\n\\label{sec:cross_agent}\n\nTable~\\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.\nStructural GB transfers best, achieving 0.967 macro-F1 on all OH windows---21.6\\,pp above the probe fine-tuned on 100\\% of OH data (0.751).\nRF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.\nBoth structural models recover to $>$0.99 on conf${\\geq}$2 OH windows, where label noise is lower.\n\nThe probe's zero-shot transfer (0.528) is near chance, and even full OH fine-tuning only reaches 0.751.\nThis asymmetry---structural features transfer naturally while learned embeddings do not---is a central empirical finding: stagnation manifests in action-level structure that generalizes across agents.\n\n\\paragraph{Multi-seed stability.}\nStructural RF: $0.9951{\\pm}0.0000$ in-domain (5 seeds, zero variance); GB cross-agent: $0.9678{\\pm}0.0015$.\nThe probe shows higher variance: $0.9185{\\pm}0.0113$, though all seeds exceed 0.90.\n\n%-------------------------------------------------------------------\n\\subsection{Robustness Analysis}\n\\label{sec:robustness}\n\n\\paragraph{Encoder ablation.}\nReplacing Qwen3-0.6B with BGE-M3 \\citep{chen2024bgem3} or E5-large-v2 \\citep{wang2024e5} yields probe macro-F1 of 0.9413 and 0.9363, respectively (vs.\\ 0.9055 for Qwen3).\nAll encoders exceed 0.90, indicating the probe's temporal architecture, not a specific encoder, drives performance. Full results appear in Appendix Table~\\ref{tab:encoder_ablation}.\n\n\\paragraph{Window size.}\n$k{=}5$ is optimal (0.9309 macro-F1); $k{=}3$ drops 5.9\\,pp and $k{=}7$ drops 1.8\\,pp.\nShorter windows lack sufficient context; longer windows dilute signal by spanning both progress and stagnation phases.\nDetails in Appendix Table~\\ref{tab:window_ablation}.\n\n\\paragraph{Data scaling.}\nFigure~\\ref{fig:data_scaling} shows probe performance scales monotonically from 0.8054 (10\\% training data) to 0.9055 (100\\%), with structural RF providing a ceiling at 0.9951 (dashed line).\nThe curve has not plateaued, suggesting larger trajectory corpora could further close the structural--probe gap.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_data_scaling.pdf}\n\\caption{Probe macro-F1 vs.\\ training data fraction. Structural RF ceiling shown as dashed line. Performance scales monotonically but has not saturated at 100\\% data.}\n\\label{fig:data_scaling}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Labeling Function Temporal Dynamics}\n\\label{sec:lf_temporal}\n\nWe analyze when each LF first fires relative to the onset of stagnation episodes (Table~\\ref{tab:lf_temporal}, Figure~\\ref{fig:lf_temporal}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{LF} & \\textbf{Lag} & \\textbf{Lead\\,\\%} & \\textbf{Conc.\\,\\%} & \\textbf{Lag\\,\\%} \\\\\n\\midrule\ncmd\\_rep      & $-1.87$ & 36.1 & --- & --- \\\\\nfile\\_diff    & $-1.20$ & 17.1 & --- & --- \\\\\noutcome\\_bp   & $+6.70$ & ---  & --- & 48.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal roles of labeling functions on SWE-Agent. Lag = mean steps relative to stagnation onset (negative = leading). Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; all pairwise comparisons significant after Bonferroni correction.}\n\\label{tab:lf_temporal}\n\\end{table}\n\nThe three LFs occupy distinct temporal niches.\nCommand repetition leads stagnation onset by 1.87 steps on average, making it an early warning signal.\nFile diff is near-concurrent ($-1.20$ steps).\nOutcome backpropagation lags by 6.70 steps, acting as a retrospective confirmation.\n\nAll pairwise differences are significant (Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; Bonferroni-corrected pairwise: cmd\\_rep vs.\\ file\\_diff $p{=}1.44{\\times}10^{-26}$, cmd\\_rep vs.\\ outcome\\_bp $p{=}6.67{\\times}10^{-39}$, file\\_diff vs.\\ outcome\\_bp $p{=}3.47{\\times}10^{-47}$).\n\n\\paragraph{Cross-agent reversal.}\nOn OpenHands, cmd\\_rep shifts from leading ($-1.87$) to lagging ($+3.32$ steps).\nThis reversal explains the cmd\\_rep pathology analyzed in \\S\\ref{sec:cmd_rep_ablation}: OH's action distribution triggers cmd\\_rep on progress windows, inverting its diagnostic value.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_lf_temporal.pdf}\n\\caption{Temporal roles of labeling functions relative to stagnation onset on SWE-Agent. cmd\\_rep leads ($-1.87$ steps), file\\_diff is near-concurrent ($-1.20$), outcome\\_bp lags ($+6.70$). Inset: OH reversal where cmd\\_rep becomes lagging.}\n\\label{fig:lf_temporal}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Command Repetition Ablation}\n\\label{sec:cmd_rep_ablation}\n\nThe cmd\\_rep LF fires on 92.3\\% of OH windows (vs.\\ 65.6\\% on SWE-Agent), with a 71\\% false positive rate on OH progress windows.\nTable~\\ref{tab:cmd_rep_ablation} shows the effect of removing it.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{LF Config} & \\textbf{ZS F1} & \\textbf{FT F1} & \\textbf{FT F1\\textsubscript{s}} & \\textbf{FT F1\\textsubscript{p}} \\\\\n\\midrule\n3-LF (w/ cmd\\_rep) & 0.530 & 0.751 & 0.544 & 0.959 \\\\\n2-LF (no cmd\\_rep) & 0.607 & \\textbf{0.927} & 0.938 & 0.917 \\\\\n\\midrule\n$\\Delta$ & +7.7\\,pp & +17.6\\,pp & +39.4\\,pp & $-4.2$\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Effect of removing cmd\\_rep on OpenHands probe performance. ZS = zero-shot transfer from SWE-Agent; FT = fine-tuned on 100\\% OH data. F1\\textsubscript{s}/F1\\textsubscript{p} = stagnation/progress F1.}\n\\label{tab:cmd_rep_ablation}\n\\end{table}\n\nRemoving cmd\\_rep improves zero-shot transfer by 7.7\\,pp and fine-tuned performance by 17.6\\,pp.\nThe gain is driven almost entirely by stagnation recall (+39.4\\,pp F1\\textsubscript{stag}), at a modest cost to progress detection ($-4.2$\\,pp F1\\textsubscript{prog}).\nThe 3-LF fine-tuned model's stagnation F1 of 0.544 reveals that cmd\\_rep corrupts silver labels so thoroughly that even full fine-tuning on OH data cannot recover.\nThis motivates agent-specific LF selection: labeling functions validated on one agent architecture may become adversarial on another.\n\n%-------------------------------------------------------------------\n\\subsection{Temporal Label Models}\n\\label{sec:temporal_label_models}\n\nWe investigate whether incorporating LF temporal dynamics into label aggregation improves over majority vote (MV).\nTable~\\ref{tab:temporal_models} compares three temporal label models \\citep{ratner2017snorkel,safranchik2020linkedhmm}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Conf${\\geq}$2 F1} & \\textbf{MV Agr.} & \\textbf{Probe F1$^\\ddagger$} \\\\\n\\midrule\nMV (baseline) & 0.8946$^\\ast$ & 1.000 & 0.8468 \\\\\nTWV ($\\sigma{=}2$) & \\textbf{0.9003} & 0.885 & 0.8211 \\\\\nLag-HMM & 0.8936 & 0.820 & --- \\\\\nHMM & 0.7502 & 0.685 & 0.6564 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal label model comparison. $^\\ast$MV conf${\\geq}$2 F1 is a self-evaluation baseline (MV evaluated against itself on high-confidence windows). $^\\ddagger$Downstream: probe trained on each method's labels, evaluated on SWE-Agent conf${\\geq}$2 vs.\\ MV labels.}\n\\label{tab:temporal_models}\n\\end{table}\n\nTWV achieves the highest conf${\\geq}$2 F1 (0.9003, +0.57\\,pp over MV), but this gain does not propagate downstream: a probe trained on TWV labels scores 0.8211 vs.\\ 0.8468 for MV-trained ($-2.57$\\,pp).\nTWV flips 14.1\\% of conf$=$1 labels, introducing noise that hurts probe training.\nHMM overpredicts stagnation (29,176 stagnation vs.\\ 25,633 progress windows), degrading downstream performance to 0.6564.\nLag-HMM closely tracks MV ($-0.1$\\,pp) despite explicitly modeling temporal offsets, suggesting that the temporal structure captured by individual LFs does not improve \\emph{aggregation}.\n\n\\paragraph{TWV sensitivity.}\nThe Gaussian kernel bandwidth $\\sigma$ is critical: $\\sigma{=}2$ is optimal (0.9003); $\\sigma{=}1$ drops to 0.8105 and $\\sigma{\\geq}5$ falls below 0.81.\nThis narrow operating range, combined with the downstream degradation, makes TWV impractical as a drop-in MV replacement.\n\nThese results constitute a negative finding: despite clear temporal structure in LF firing patterns (\\S\\ref{sec:lf_temporal}), temporal label models do not improve over simple majority vote for downstream stagnation detection.\n\n%-------------------------------------------------------------------\n\\subsection{Gold Set Validation}\n\\label{sec:gold_set}\n\\goldset{Human-annotated gold set (650 windows) validation pending. Results will be added upon completion (expected 2026-05-17). This provides the non-circular ground truth evaluation for all methods.}\n"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T21:20:28.542121+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T21:20:28.542262+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
  "description": "Word count of experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
    "description": "Word count of experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T21:20:28.542379+00:00_

1652 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T21:20:28.542491+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c '\\\\cite' /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
  "description": "Count citations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c '\\\\cite' /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
    "description": "Count citations"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T21:20:28.542600+00:00_

5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T21:20:28.542764+00:00_

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
  "session": "worker_paper_writing_experiments_20260514T211641",
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

_source line 42 · 2026-05-14T21:20:28.542887+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T21:20:28.543005+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "experiments-section-v1",
  "type": "paper",
  "description": "Experiments section (§5) for EMNLP 2026 paper — covers setup, main results, cross-agent transfer, robustness, LF temporal dynamics, cmd_rep ablation, temporal label models, and gold set placeholder.",
  "project": "agent_progress_probe",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
  "tags": "['paper', 'experiments', 'latex', 'emnlp2026']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "experiments-section-v1",
    "type": "paper",
    "description": "Experiments section (§5) for EMNLP 2026 paper — covers setup, main results, cross-agent transfer, robustness, LF temporal dynamics, cmd_rep ablation, temporal label models, and gold set placeholder.",
    "project": "agent_progress_probe",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
    "tags": "['paper', 'experiments', 'latex', 'emnlp2026']"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T21:20:28.543150+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_0710d8\", \"name\": \"experiments-section-v1\", \"type\": \"paper\", \"description\": \"Experiments section (§5) for EMNLP 2026 paper — covers setup, main results, cross-agent transfer, robustness, LF temporal dynamics, cmd_rep ablation, temporal label models, and gold set placeholder.\", \"path\": \"projects/agent_progress_probe/artifacts/_project/paper/experiments.tex\", \"url\": null, \"project\": \"agent_progress_probe\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T21:20:16.989077+00:00\", \"tags\": [\"paper\", \"experiments\", \"latex\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260514T211641",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-14T21:20:28.543327+00:00_

文件已写入 `docs/paper/sections/experiments.tex`，artifact 已注册。

自查结果：
- **1652 words**（含 LaTeX 标记），排版后约 2.5 pages（正文 + 5 tables + 2 figures）
- Circular eval caveat 在 §5 开头段明确声明
- D042 约束：in-domain RF 0.9951，cross-agent GB 0.967（rounded），multi-seed 格式 mean±std
- 10 个 citation keys 全部来自 references.bib
- 未使用 "significantly"（除有 Kruskal-Wallis p 值支撑处）和 "state-of-the-art"
- 所有 table 有 `\label` + `\caption`，structural 指标标注 $^\dagger$ circular caveat 脚注
- Gold set placeholder 在末尾使用 `\goldset{}` 命令
- 负向结果完整报告：LLM-judge 低性能、probe 迁移失败、TLM 全部不优于 MV

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_experiments_20260514T211641"
}
```

</details>

---

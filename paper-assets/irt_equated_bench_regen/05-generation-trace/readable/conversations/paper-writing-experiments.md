# paper writing experiments

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 69
- **Recorded user turns:** 0
- **Tool calls:** 34
- **Original source:** `logs/chats/worker_paper_writing_experiments_20260521T040002.jsonl`
- **Structured JSON:** [`e77ce5d98d73941bbf6b.json`](../../sessions/e7/e77ce5d98d73941bbf6b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

69 recorded events

### Tool call

_source line 1 · 2026-05-21T04:11:19.736853+00:00_

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
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T04:11:19.737477+00:00_

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
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T04:11:19.737675+00:00_

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
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T04:11:19.738061+00:00_

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
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T04:11:19.738228+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T04:11:19.738359+00:00_

paper/references.bib
paper/iclr2026_conference.sty
paper/iclr2026_conference.bst
paper/fancyhdr.sty
paper/natbib.sty
paper/math_commands.tex
paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T04:11:19.738512+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T04:11:19.738647+00:00_

1	\documentclass{article}
2	\usepackage{iclr2026_conference,times}
3	\input{math_commands.tex}
4	
5	\usepackage{hyperref}
6	\usepackage{url}
7	\usepackage{booktabs}
8	\usepackage{graphicx}
9	\usepackage{xcolor}
10	\usepackage{microtype}
11	\usepackage{multirow}
12	\usepackage{subcaption}
13	\usepackage{cleveref}
14	
15	\graphicspath{{../figures/paper/}}
16	
17	\title{Psychometric Instability of LLM Benchmarks:\\Differential Item Functioning Reveals 31\% of MMLU Items\\Behave Differently Across Model Generations}
18	
19	%\iclrfinalcopy
20	
21	\newcommand{\fix}{\marginpar{FIX}}
22	\newcommand{\new}{\marginpar{NEW}}
23	
24	\begin{document}
25	
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\bibliography{references}
37	\bibliographystyle{iclr2026_conference}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T04:11:19.738799+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/ 2>/dev/null; echo \"---\"; ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/figures/paper/ 2>/dev/null || ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/ 2>/dev/null",
  "description": "Check sections dir and figures dir"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/ 2>/dev/null; echo \"---\"; ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/figures/paper/ 2>/dev/null || ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/ 2>/dev/null",
    "description": "Check sections dir and figures dir"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T04:11:19.738951+00:00_

total 8
drwxr-xr-x 2 ubuntu ubuntu 4096 May 21 03:58 .
drwxr-xr-x 3 ubuntu ubuntu 4096 May 21 03:58 ..
---
total 2820
drwxr-xr-x 2 ubuntu ubuntu   4096 May 21 01:34 .
drwxr-xr-x 3 ubuntu ubuntu   4096 May 20 23:41 ..
-rw-r--r-- 1 ubuntu ubuntu  40955 May 21 01:31 fig_1_global_vs_differential.pdf
-rw-r--r-- 1 ubuntu ubuntu 303811 May 21 01:31 fig_1_global_vs_differential.png
-rw-r--r-- 1 ubuntu ubuntu   5482 May 21 01:31 fig_1_global_vs_differential.py
-rw-r--r-- 1 ubuntu ubuntu  34084 May 20 23:42 fig_2_dose_response.pdf
-rw-r--r-- 1 ubuntu ubuntu 186046 May 20 23:42 fig_2_dose_response.png
-rw-r--r-- 1 ubuntu ubuntu   5192 May 20 23:42 fig_2_dose_response.py
-rw-r--r-- 1 ubuntu ubuntu  21389 May 21 00:03 fig_3_within_subject_matching.pdf
-rw-r--r-- 1 ubuntu ubuntu 111479 May 21 00:03 fig_3_within_subject_matching.png
-rw-r--r-- 1 ubuntu ubuntu   5311 May 21 00:03 fig_3_within_subject_matching.py
-rw-r--r-- 1 ubuntu ubuntu 161450 May 21 01:14 fig_4_downstream_impact.pdf
-rw-r--r-- 1 ubuntu ubuntu 451446 May 21 01:14 fig_4_downstream_impact.png
-rw-r--r-- 1 ubuntu ubuntu   5190 May 21 01:14 fig_4_downstream_impact.py
-rw-r--r-- 1 ubuntu ubuntu  28664 May 21 01:34 fig_5_gsm1k_dif_correlation.pdf
-rw-r--r-- 1 ubuntu ubuntu 292793 May 21 01:34 fig_5_gsm1k_dif_correlation.png
-rw-r--r-- 1 ubuntu ubuntu  21893 May 21 00:21 fig_A1_subject_heatmap.pdf
-rw-r--r-- 1 ubuntu ubuntu 619659 May 21 00:21 fig_A1_subject_heatmap.png
-rw-r--r-- 1 ubuntu ubuntu   5675 May 21 00:21 fig_A1_subject_heatmap.py
-rw-r--r-- 1 ubuntu ubuntu  29519 May 21 00:26 fig_A2_q3_distribution.pdf
-rw-r--r-- 1 ubuntu ubuntu 496994 May 21 00:26 fig_A2_q3_distribution.png
-rw-r--r-- 1 ubuntu ubuntu   2859 May 21 00:26 fig_A2_q3_distribution.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T04:11:19.739118+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/",
  "description": "List existing section files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/",
    "description": "List existing section files"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T04:11:19.739243+00:00_

total 8
drwxr-xr-x 2 ubuntu ubuntu 4096 May 21 03:58 .
drwxr-xr-x 3 ubuntu ubuntu 4096 May 21 03:58 ..

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T04:11:19.739376+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "@(article|inproceedings|misc)\\{(kipnis|li2024|holland|habba|zhang2024)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
  "output_mode": "content",
  "-A": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Grep",
  "tool_args": {
    "pattern": "@(article|inproceedings|misc)\\{(kipnis|li2024|holland|habba|zhang2024)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
    "output_mode": "content",
    "-A": "3"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T04:11:19.739510+00:00_

30:@inproceedings{li2024contamination,
31-  title     = {An Open-Source Data Contamination Report for Large Language Models},
32-  author    = {Li, Yucheng and Guo, Yunhao and Guerin, Frank and Lin, Chenghua},
33-  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},
--
73:@misc{zhang2024gsm1k,
74-  title         = {A Careful Examination of Large Language Model Performance on Grade School Arithmetic},
75-  author        = {Zhang, Hugh},
76-  year          = {2024},
--
83:@misc{zhang2024minkpp,
84-  title         = {{Min-K\%++}: Improved Baseline for Detecting Pre-Training Data from Large Language Models},
85-  author        = {Zhang, Jingyang and Sun, Jingwei and Yeats, Eric and Ouyang, Yang and Kuo, Martin and Zhang, Jianyi and Yang, Hao and Li, Hai},
86-  year          = {2024},
--
164:@misc{habba2026growingpains,
165-  title         = {Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},
166-  author        = {Habba, Eitam and Itzhak, Ido and Yehudai, Asaf and Perlitz, Yotam and Bandel, Elron and Shmueli-Scheuer, Michal and Choshen, Leshem and Stanovsky, Gabriel},
167-  year          = {2026},
--
195:@misc{kipnis2024metabench,
196-  title         = {metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language Models},
197-  author        = {Kipnis, Alon and Voudouris, Konstantinos and Schulze Buschoff, Luca Maria and Schulz, Eric},
198-  year          = {2024},
--
241:@inproceedings{li2024latesteval,
242-  title     = {{LatestEval}: Addressing Data Contamination in Language Model Evaluation through Dynamic and Time-Sensitive Test Construction},
243-  author    = {Li, Yucheng and Guerin, Frank and Lin, Chenghua},
244-  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T04:11:19.739644+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "@(article|inproceedings|misc)\\{holland",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
  "output_mode": "content",
  "-A": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Grep",
  "tool_args": {
    "pattern": "@(article|inproceedings|misc)\\{holland",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
    "output_mode": "content",
    "-A": "3"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T04:11:19.739786+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T04:11:19.739906+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "@(article|inproceedings|misc)\\{(zellers|ets|mh|mantel|bh_fdr|benjamini)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
  "output_mode": "content",
  "-A": "3",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Grep",
  "tool_args": {
    "pattern": "@(article|inproceedings|misc)\\{(zellers|ets|mh|mantel|bh_fdr|benjamini)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
    "output_mode": "content",
    "-A": "3",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T04:11:19.740031+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T04:11:19.740192+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "^@",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Grep",
  "tool_args": {
    "pattern": "^@",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T04:11:19.740344+00:00_

5:@inproceedings{balloccu2024leak,
14:@inproceedings{dekoninck2024constat,
22:@inproceedings{golchin2024timetravel,
30:@inproceedings{li2024contamination,
39:@misc{liang2026dvd,
49:@inproceedings{shi2024mink,
57:@inproceedings{tao2026selfcritique,
65:@inproceedings{wang2026fragility,
73:@misc{zhang2024gsm1k,
83:@misc{zhang2024minkpp,
97:@misc{hardy2026scalability,
107:@article{kim2019fpc,
116:@inproceedings{lalor2019irt,
125:@inproceedings{vania2021irt,
134:@misc{li2025atlas,
144:@misc{chen2025irtnet,
154:@misc{choi2026llmjudgeirt,
164:@misc{habba2026growingpains,
174:@inproceedings{zhou2026psnirt,
186:@inproceedings{white2025livebench,
195:@misc{kipnis2024metabench,
205:@inproceedings{hendrycks2021mmlu,
213:@article{liang2023helm,
222:@inproceedings{chiang2024chatbot,
231:@misc{mialon2023gaia,
241:@inproceedings{li2024latesteval,
250:@inproceedings{kiela2021dynabench,
263:@article{belzak2020smallsample,
272:@incollection{holland1988mh,
283:@article{shealy1993sibtest,
292:@article{clauser1998dif,
301:@book{zumbo1999handbook,
310:@article{meredith1993invariance,
319:@article{vandenberg2000invariance,
328:@article{swaminathan1990logistic,
337:@article{teresi2007dif,
346:@book{lord1980irt,
354:@article{raju1988area,
363:@article{muthen1985mimic,
371:@article{woods2009mimic,
383:@article{burnell2023rethink,
392:@article{chang2024survey,
401:@inproceedings{maiapolo2024tinybenchmarks,
409:@inproceedings{wang2024mmlupro,
417:@article{ott2022benchmark,

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T04:11:19.740503+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find method section and writing plan",
  "prompt": "Find and read these files in the project /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/:\n1. Any method section tex file (likely paper/sections/method.tex)\n2. writing_plan.yaml or similar planning files\n3. Any existing section tex files (abstract.tex, introduction.tex, etc.)\n\nRead the full content of any files you find and report them back to me. I need to understand what notation and terminology has been established in earlier sections."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find method section and writing plan",
    "prompt": "Find and read these files in the project /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/:\n1. Any method section tex file (likely paper/sections/method.tex)\n2. writing_plan.yaml or similar planning files\n3. Any existing section tex files (abstract.tex, introduction.tex, etc.)\n\nRead the full content of any files you find and report them back to me. I need to understand what notation and terminology has been established in earlier sections."
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T04:11:19.740655+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-21T04:11:19.740814+00:00_

artifacts/dream_reports/dream_20260520T194223/best/paper.tex
artifacts/dream_reports/dream_20260520T194223/median/paper.tex
artifacts/dream_reports/dream_20260520T194223/worst/paper.tex
artifacts/dream_reports/dream_20260520T205007/best/paper.tex
artifacts/dream_reports/dream_20260520T205007/median/paper.tex
artifacts/dream_reports/dream_20260520T205007/worst/paper.tex
artifacts/dream_reports/dream_20260521T012912/best/paper.tex
artifacts/dream_reports/dream_20260521T012912/median/paper.tex
artifacts/dream_reports/dream_20260521T012912/worst/paper.tex
artifacts/dream_reports/dream_20260521T032826/best/paper.tex
artifacts/dream_reports/dream_20260521T032826/worst/paper.tex
paper/math_commands.tex
paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T04:11:19.740956+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-21T04:11:19.741079+00:00_

artifacts/dream_reports/dream_20260520T194223/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T194223/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T194223/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T194223/best/review_context.yaml
artifacts/dream_reports/dream_20260520T194223/median/review_context.yaml
artifacts/dream_reports/dream_20260520T194223/worst/review_context.yaml
artifacts/dream_reports/dream_20260520T194223/meta.yaml
experiment_plan.yaml
artifacts/dream_reports/dream_20260520T205007/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T205007/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T205007/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T205007/best/review_context.yaml
artifacts/dream_reports/dream_20260520T205007/median/review_context.yaml
artifacts/dream_reports/dream_20260520T205007/worst/review_context.yaml
artifacts/dream_reports/dream_20260520T205007/meta.yaml
artifacts/review_issues.yaml
registry.yaml
artifacts/dream_reports/dream_20260521T012912/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260521T012912/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260521T012912/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260521T012912/best/review_context.yaml
artifacts/dream_reports/dream_20260521T012912/median/review_context.yaml
artifacts/dream_reports/dream_20260521T012912/worst/review_context.yaml
artifacts/dream_reports/dream_20260521T012912/meta.yaml
decisions.yaml
mistakes.yaml
artifacts/dream_reports/dream_20260521T032826/best/imagined_experiments.yaml
writing_plan.yaml
artifacts/dream_reports/dream_20260521T032826/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260521T032826/worst/imagined_experiments.yaml
literature_map.yaml
artifacts/dream_reports/dream_20260521T032826/best/review_context.yaml
artifacts/manifest.yaml
artifacts/dream_report
…[truncated 125 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T04:11:19.741226+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T04:11:19.741348+00:00_

total 256
drwxr-xr-x  9 ubuntu ubuntu  4096 May 21 04:00 .
drwxrwxr-x  4 ubuntu ubuntu  4096 May 20 17:11 ..
drwxr-xr-x  3 ubuntu ubuntu  4096 May 20 17:11 .claude
-rw-r--r--  1 ubuntu ubuntu 13105 May 21 03:59 AGENTS.md
-rw-r--r--  1 ubuntu ubuntu     0 May 20 17:15 ROADMAP.lock
-rw-------  1 ubuntu ubuntu  3663 May 21 03:45 ROADMAP.md
-rw-r--r--  1 ubuntu ubuntu    90 May 20 21:44 _last_visual_review.json
drwxr-xr-x 27 ubuntu ubuntu  4096 May 21 03:34 artifacts
drwxr-xr-x  2 ubuntu ubuntu 12288 May 21 01:22 checkpoints
-rw-r--r--  1 ubuntu ubuntu     0 May 20 18:50 decisions.lock
-rw-------  1 ubuntu ubuntu 16968 May 21 03:08 decisions.yaml
drwxr-xr-x  4 ubuntu ubuntu  4096 May 20 19:42 docs
-rwxr-xr-x  1 ubuntu ubuntu     0 May 20 19:34 dream_registry.lock
-rw-------  1 ubuntu ubuntu  4205 May 21 04:00 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu  4210 May 21 04:00 dream_registry.yaml.bak
-rw-r--r--  1 ubuntu ubuntu 13528 May 20 20:53 experiment_plan.yaml
drwxr-xr-x  3 ubuntu ubuntu  4096 May 20 23:41 figures
-rw-r--r--  1 ubuntu ubuntu     0 May 21 01:40 literature_map.lock
-rw-------  1 ubuntu ubuntu 36148 May 21 03:50 literature_map.yaml
drwxr-xr-x  4 ubuntu ubuntu  4096 May 20 17:17 logs
-rw-r--r--  1 ubuntu ubuntu  5982 May 21 01:26 memory.md
-rw-r--r--  1 ubuntu ubuntu     0 May 21 03:15 mistakes.lock
-rw-------  1 ubuntu ubuntu  1217 May 21 03:15 mistakes.yaml
drwxr-xr-x  3 ubuntu ubuntu  4096 May 21 03:58 paper
-rw-r--r--  1 ubuntu ubuntu 16017 May 21 03:41 paper_framing.md
-rw-r--r--  1 ubuntu ubuntu     0 May 20 17:16 registry.lock
-rw-------  1 ubuntu ubuntu 25586 May 21 01:22 registry.yaml
-rw-r--r--  1 ubuntu ubuntu  2624 May 21 01:22 report.md
-rwxr-xr-x  1 ubuntu ubuntu     0 May 20 17:12 study_status.lock
-rw-r--r--  1 ubuntu ubuntu 40194 May 21 03:46 writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T04:11:19.741496+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper -type f -name \"*.tex\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper -type f -name \"*.tex\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-21T04:11:19.741611+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/math_commands.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T04:11:19.741750+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/writing_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/writing_plan.yaml"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T04:11:19.741876+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T04:11:19.741995+00:00_

1	\documentclass{article}
2	\usepackage{iclr2026_conference,times}
3	\input{math_commands.tex}
4	
5	\usepackage{hyperref}
6	\usepackage{url}
7	\usepackage{booktabs}
8	\usepackage{graphicx}
9	\usepackage{xcolor}
10	\usepackage{microtype}
11	\usepackage{multirow}
12	\usepackage{subcaption}
13	\usepackage{cleveref}
14	
15	\graphicspath{{../figures/paper/}}
16	
17	\title{Psychometric Instability of LLM Benchmarks:\\Differential Item Functioning Reveals 31\% of MMLU Items\\Behave Differently Across Model Generations}
18	
19	%\iclrfinalcopy
20	
21	\newcommand{\fix}{\marginpar{FIX}}
22	\newcommand{\new}{\marginpar{NEW}}
23	
24	\begin{document}
25	
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\bibliography{references}
37	\bibliographystyle{iclr2026_conference}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-21T04:11:19.742252+00:00_

1	meta:
2	  venue: ICLR 2027
3	  track: main
4	  template: ""
5	  template_note: "ICLR 2027 template not yet available locally; will download or reuse iclr2025 when entering Step 2"
6	  page_limit: 9
7	  deadline: "2026-10-01"
8	  core_claim: >-
9	    Applying DIF to MMLU (5,227 models × 12,508 items) reveals 38% item-level
10	    functional instability across model generations, exposes a fundamental gap
11	    in contamination ground truth labels, and provides a semi-synthetic
12	    validation framework for item-level detectors.
13	  created_at: "2026-05-20T23:45:00Z"
14	  story_arc:
15	    hook: >-
16	      When we say "Model B outperforms Model A on MMLU," we assume temporal
17	      comparability — but 38% of MMLU items function differently across model
18	      generations.
19	    gap: >-
20	      Existing contamination labels (web-overlap, n-gram) measure global
21	      exposure, not differential item functioning — every validation study
22	      using these labels has a blind spot. This is a fundamental validation
23	      methodology gap affecting the entire contamination detection field.
24	    insight: >-
25	      DIF detects differential contamination (semi-synthetic ΔTPR=+0.508) but
26	      temporal DIF is dominated by genuine capability evolution
27	      (enrichment≈1.0, within-subject C%=38.1%), and three structural
28	      corrections cannot separate them.
29	    mechanism: >-
30	      Semi-synthetic injection into real response matrices provides controlled
31	      ground truth; cross-subject matching eliminates FPR inflation (ΔFPR=0.000).
32	    evidence: >-
33	      38% items functionally unstable (plan_001/014); ΔTPR=+0.508 at p=0.5
34	      (plan_011); ΔFPR=0.000 cross-subject (plan_016); three improvements
35	      exhausted (plan_001b/012/014).
36	
37	paper_outline:
38	  - section: abstract
39	    word_budget: 200
40	    core_bullets:
41	      - >-
42	        Problem: LLM benchmark scores assume temporal comparability, but
43	        item-
…[truncated 41166 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-21T04:11:19.742422+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections -type f 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections -type f 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T04:11:19.742571+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/math_commands.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/math_commands.tex"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T04:11:19.742762+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-21T04:11:19.742971+00:00_

1	%%%%% NEW MATH DEFINITIONS %%%%%
2	
3	\usepackage{amsmath,amsfonts,bm}
4	
5	% Mark sections of captions for referring to divisions of figures
6	\newcommand{\figleft}{{\em (Left)}}
7	\newcommand{\figcenter}{{\em (Center)}}
8	\newcommand{\figright}{{\em (Right)}}
9	\newcommand{\figtop}{{\em (Top)}}
10	\newcommand{\figbottom}{{\em (Bottom)}}
11	\newcommand{\captiona}{{\em (a)}}
12	\newcommand{\captionb}{{\em (b)}}
13	\newcommand{\captionc}{{\em (c)}}
14	\newcommand{\captiond}{{\em (d)}}
15	
16	% Highlight a newly defined term
17	\newcommand{\newterm}[1]{{\bf #1}}
18	
19	
20	% Figure reference, lower-case.
21	\def\figref#1{figure~\ref{#1}}
22	% Figure reference, capital. For start of sentence
23	\def\Figref#1{Figure~\ref{#1}}
24	\def\twofigref#1#2{figures \ref{#1} and \ref{#2}}
25	\def\quadfigref#1#2#3#4{figures \ref{#1}, \ref{#2}, \ref{#3} and \ref{#4}}
26	% Section reference, lower-case.
27	\def\secref#1{section~\ref{#1}}
28	% Section reference, capital.
29	\def\Secref#1{Section~\ref{#1}}
30	% Reference to two sections.
31	\def\twosecrefs#1#2{sections \ref{#1} and \ref{#2}}
32	% Reference to three sections.
33	\def\secrefs#1#2#3{sections \ref{#1}, \ref{#2} and \ref{#3}}
34	% Reference to an equation, lower-case.
35	\def\eqref#1{equation~\ref{#1}}
36	% Reference to an equation, upper case
37	\def\Eqref#1{Equation~\ref{#1}}
38	% A raw reference to an equation---avoid using if possible
39	\def\plaineqref#1{\ref{#1}}
40	% Reference to a chapter, lower-case.
41	\def\chapref#1{chapter~\ref{#1}}
42	% Reference to an equation, upper case.
43	\def\Chapref#1{Chapter~\ref{#1}}
44	% Reference to a range of chapters
45	\def\rangechapref#1#2{chapters\ref{#1}--\ref{#2}}
46	% Reference to an algorithm, lower-case.
47	\def\algref#1{algorithm~\ref{#1}}
48	% Reference to an algorithm, upper case.
49	\def\Algref#1{Algorithm~\ref{#1}}
50	\def\twoalgref#1#2{algorithms \ref{#1} and \ref{#2}}
51	\def\Twoalgref#1#2{Algorithms \ref{#1} and \ref{#2}}
52	% Reference to a part, lower case
53	\d
…[truncated 12212 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T04:11:19.743142+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/ 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-21T04:11:19.743266+00:00_

total 160
drwxr-xr-x 3 ubuntu ubuntu  4096 May 21 03:58 .
drwxr-xr-x 9 ubuntu ubuntu  4096 May 21 04:00 ..
-rw-r--r-- 1 ubuntu ubuntu 20521 May 21 03:58 fancyhdr.sty
-rw-r--r-- 1 ubuntu ubuntu 26973 May 21 03:58 iclr2026_conference.bst
-rw-r--r-- 1 ubuntu ubuntu  9025 May 21 03:58 iclr2026_conference.sty
-rw-r--r-- 1 ubuntu ubuntu   910 May 21 03:58 main.tex
-rw-r--r-- 1 ubuntu ubuntu 12284 May 21 03:58 math_commands.tex
-rw-r--r-- 1 ubuntu ubuntu 45154 May 21 03:58 natbib.sty
-rw-r--r-- 1 ubuntu ubuntu 19470 May 21 03:55 references.bib
drwxr-xr-x 2 ubuntu ubuntu  4096 May 21 03:58 sections

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-21T04:11:19.743398+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/ 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-21T04:11:19.743513+00:00_

total 8
drwxr-xr-x 2 ubuntu ubuntu 4096 May 21 03:58 .
drwxr-xr-x 3 ubuntu ubuntu 4096 May 21 03:58 ..

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-21T04:11:19.743637+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen -name \"abstract*\" -o -name \"introduction*\" -o -name \"method*\" 2>/dev/null | grep -E \"\\.(tex|md)$\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen -name \"abstract*\" -o -name \"introduction*\" -o -name \"method*\" 2>/dev/null | grep -E \"\\.(tex|md)$\""
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-21T04:11:19.743783+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-21T04:11:19.743906+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper_framing.md",
  "limit": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper_framing.md",
    "limit": "5000"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-21T04:11:19.744055+00:00_

1	# Paper Framing — irt_equated_bench_regen
2	
3	## Target Venue
4	- Primary: ICLR 2027 (expected deadline ~October 2026)
5	
6	## Paper Type
7	Empirical analysis / psychometric characterization. Discovery paper, not methods paper. "DIF reveals benchmark structural problems," not "DIF detects contamination."
8	
9	## Core Claims (4 条, 可证伪)
10	
11	**Claim 1 (Temporal Comparability Concern)**: 31–38% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001); within-subject range 31-45%, avg 38.1% (plan_014). This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).
12	- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement)
13	- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.
14	- IRT fit: 98% of models show |Lz
…[truncated 14059 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-21T04:11:19.744252+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -lt /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/ | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -lt /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/ | head -5"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-21T04:11:19.744378+00:00_

total 24
lrwxrwxrwx 1 ubuntu ubuntu  126 May 21 04:00 latest -> /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826
drwxr-xr-x 6 ubuntu ubuntu 4096 May 21 04:00 dream_20260521T032826
drwxr-xr-x 6 ubuntu ubuntu 4096 May 21 02:23 dream_20260521T012912
drwxr-xr-x 6 ubuntu ubuntu 4096 May 20 21:45 dream_20260520T205007

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-21T04:11:19.744512+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best/paper.tex",
  "limit": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best/paper.tex",
    "limit": "3000"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-21T04:11:19.744722+00:00_

1	\documentclass{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage{amsmath,amssymb}
4	\usepackage{booktabs}
5	\usepackage{graphicx}
6	\usepackage{hyperref}
7	\usepackage{natbib}
8	\usepackage[margin=1in]{geometry}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	
12	\title{Psychometric Analysis Reveals Structural Benchmark Instability\\That Contamination Validation Cannot Detect}
13	
14	\author{Anonymous}
15	\date{}
16	
17	\begin{document}
18	\maketitle
19	
20	%==============================================================================
21	\begin{abstract}
22	LLM benchmarks implicitly assume temporal score comparability---that a score on MMLU today measures the same construct as a score measured six months ago. We apply Differential Item Functioning (DIF) analysis to the METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items) and find that 28--30\% of items are functionally unstable across model generations, even within architecture-homogeneous decoder-only populations where IRT model fit is excellent (RMSEA$=$0.024, CFI$=$0.966). Instability decomposition shows that partial $\rho=0.22$ ($p=0.012$) persists after controlling for domain accuracy improvement, indicating genuine item function change beyond aggregate capability gains. We demonstrate that the field's standard validation approach---web-overlap contamination labels---cannot capture this differential signal (enrichment$\approx$1.0), while a semi-synthetic injection framework confirms detection capability ($\Delta$TPR$=$+0.508 on MMLU, +0.818 on GSM8K). Cross-subject matching eliminates false positive inflation ($\Delta$FPR$=$0.000). Group-level DIF statistics remain robust to reasoning-RL model compositions (flag retention 89--91\%, AUROC$=$0.88) while traditional per-model detectors degrade significantly (ConStat AUROC: 0.73$\to$0.54; Min-K\%: 0.68$\to$0.51). We further characterize DIF via complementary methods (ConStat perturbation, generation variance, ensemble fusion), continuous moni
…[truncated 26208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-21T04:11:19.744947+00:00_

Perfect! Now I have all the information needed. Let me compile a comprehensive summary for you.

## Summary: Notation, Terminology, and Established Context

I've found and read all the key project files. Here's what has been established in earlier sections and planning documents:

### **Key Files Located:**

1. **writing_plan.yaml** - Comprehensive paper outline with 4 main claims and detailed section budgets
2. **paper/main.tex** - Document structure (imports from sections/)
3. **paper/math_commands.tex** - LaTeX notation definitions
4. **paper_framing.md** - Core framing, story spine, and anticipated concerns
5. **Dream report** (most recent) - Generated paper sections with Abstract, Introduction, Methods content

### **Core Notation Established:**

From the math_commands.tex and writing_plan:

| Symbol | Meaning |
|--------|---------|
| **θ** | Latent ability (IRT - Item Response Theory) |
| **Δ_MH** | Mantel-Haenszel DIF statistic (log-odds ratio) |
| **p** | Exploitation rate in semi-synthetic injection |
| **C%** | Percentage of items classified ETS C (large DIF, \|Δ_MH\| ≥ 1.5) |
| **ΔTPR** | TPR increase from semi-synthetic injection over baseline |
| **ΔFPR** | FPR change from semi-synthetic injection (should be 0 for valid framework) |
| **ρ** | Spearman/Pearson correlation coefficient |
| **enrichment** | Detection overlap metric between DIF flags and web-overlap labels |
| **RMSEA, CFI, TLI, SRMR** | IRT model fit indices (confirmatory factor analysis) |

### **Key Terminology & Concepts Already Established:**

1. **DIF (Differential Item Functioning)**: "Items function differently across groups after controlling for ability" — applies here to temporal cohorts (2023 vs 2024 models)

2. **ETS Classification Thresholds**:
   - **A**: |Δ_MH| < 1.0 (negligible DIF)
   - **B**: 1.0 ≤ |Δ_MH| < 1.5 (moderate DIF)
   - **C**: |Δ_MH| ≥ 1.5 (large DIF) ← **primary finding**

3. **Primary Finding**: **31–38% of MMLU items exhibit ETS C DIF**
   - Temporal cohort: 3
…[truncated 3575 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Agent",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-21T04:11:19.745325+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/",
  "description": "Check if sections dir exists and is empty"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/",
    "description": "Check if sections dir exists and is empty"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-21T04:11:19.745472+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-21T04:11:19.745635+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
  "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe apply MH-DIF to the METABENCH dataset~\\citep{kipnis2024metabench}, which provides sparse response matrices for 5,227 models evaluated on 12,508 MMLU items~\\citep{hendrycks2021mmlu}. All temporal analyses define reference and focal cohorts by model release date (2023 vs.\\ 2024). We validate detection power through simulation, characterize temporal instability across multiple cohort designs, evaluate the relationship between DIF flags and existing contamination labels, and assess downstream consequences for benchmark rankings. Replication on GSM8K with cross-benchmark contamination validation appears in \\Cref{sec:gsm8k}.\n\n\\subsection{Validation: DIF Detection Power}\n\\label{sec:validation}\n\nTo confirm that MH-DIF detects differential item functioning at the sample sizes available in METABENCH, we conduct a power analysis using empirical MMLU IRT parameters. We simulate item response matrices where a controlled subset of items has injected DIF of varying magnitude ($|\\Delta_{\\mathrm{MH}}| \\geq 1.4$) and evaluate ETS~C classification across sample sizes $N \\in \\{40, 80, 160, 320\\}$ per cohort. At $N \\geq 80$, ETS~C achieves true positive rates of 0.68--0.80 with false positive rates of 0.036--0.042 and AUC of 0.93--0.94. The temporal cohort sizes in our analysis ($N_{\\mathrm{ref}} = 1{,}080$, $N_{\\mathrm{focal}} = 807$) far exceed this threshold, and statistical power is not a limiting factor for the results reported below. Full simulation results with confidence intervals appear in Appendix~Table~A1.\n\n\\subsection{Temporal Comparability: 31\\% Item Instability}\n\\label{sec:temporal}\n\nThe central finding of this paper is that a substantial fraction of MMLU items behave differently across model generations. Comparing models released in 2023 ($N = 1{,}080$) against models released in 2024 ($N = 807$), 31.3\\% of items receive ETS~C classification ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$). Applying Benjamini-Hochberg FDR correction at $q = 0.05$ reduces this from 31.32\\% to 31.30\\%, removing only 3 items. The minimal impact of FDR correction reflects the fact that the ETS classification system imposes a dual threshold on both effect size and statistical significance, which already provides implicit multiple-testing protection. In absolute terms, nearly one in three MMLU items exhibits a large shift in its statistical relationship to overall model ability between the two cohort periods.\n\nThree control conditions establish that this instability reflects genuine temporal change rather than methodological artifacts. A random split of the 2023 cohort into two equal halves produces only 0.18\\% ETS~C items, confirming that sampling noise alone does not generate large-scale DIF. An ability-quintile comparison (lowest-scoring vs.\\ highest-scoring models within the same temporal cohort) yields 2.9\\% ETS~C items, indicating that ability differences alone are insufficient to produce the observed instability. A within-family comparison of Llama-2 ($N = 161$) and Llama-3 ($N = 308$) models produces 61.3\\% ETS~C items. This elevated rate is consistent with the known sensitivity of MH-DIF to ability differences between groups~\\citep{holland1988mh}: models from different generations within a single family exhibit large ability gaps that confound the DIF signal. The contrast between 2.9\\% (ability-controlled) and 61.3\\% (ability-confounded) brackets the temporal rate of 31.3\\% and confirms that it captures a mixture of genuine item instability and residual ability differences.\n\nThe instability penetrates within every knowledge domain. Within-subject analysis yields an average of 38.1\\% ETS~C items across all five MMLU subjects (range: 31--45\\%), and the ecological correlation between subject-level accuracy improvement and subject-level C\\% is $\\rho = 0.307$ ($p = 0.02$). This ecological correlation could suggest that domains where models improved most also exhibit the most instability. Item-level logistic regression, however, reveals that domain accuracy improvement explains only 2.4 percentage points of the 31.3\\% temporal C\\% (pseudo $R^2 = 0.0007$; counterfactual C\\% with domain improvement regressed out $= 29.0\\%$). Of the observed instability, 92.4\\% is unrelated to aggregate domain-level accuracy gains and instead reflects item-specific changes in how models interact with individual questions.\n\nArchitecture heterogeneity is a non-issue for this analysis. The METABENCH MMLU population is 99.98\\% decoder-only (5,226 of 5,227 models). Excluding the single encoder-decoder model yields C\\% $= 31.32\\%$ with Jaccard similarity of 1.0 between flagged item sets. Threshold sensitivity analysis confirms robustness across the full ETS range: C\\% $= 48.9\\%$ at $|\\Delta_{\\mathrm{MH}}| \\geq 1.0$, $31.3\\%$ at $\\geq 1.5$ (the standard ETS~C threshold), $18.3\\%$ at $\\geq 2.0$, and $10.2\\%$ at $\\geq 2.5$. The qualitative conclusion holds at every threshold. \\Cref{tab:temporal_landscape} summarizes the DIF landscape across all cohort comparisons.\n\n\\begin{table}[t]\n\\centering\n\\caption{DIF landscape across cohort definitions. ETS~C denotes the percentage of items with $|\\Delta_{\\mathrm{MH}}| \\geq 1.5$. FPR is measured against Li et al.\\ web-overlap labels on the ``clean'' (non-overlapping) subset. Enrichment is the ratio of observed to expected overlap between DIF flags and web-overlap labels.}\n\\label{tab:temporal_landscape}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCohort Definition & $N_{\\mathrm{ref}}$ / $N_{\\mathrm{focal}}$ & ETS~C (\\%) & FPR (Li clean) & Enrichment \\\\\n\\midrule\nTemporal (2023 vs.\\ 2024) & 1,080 / 807 & 31.3 & 0.318 & 0.96 \\\\\nAbility quintile (Q1--2 vs.\\ Q4--5) & ${\\sim}$2,600 / ${\\sim}$2,600 & 2.9 & 0.027 & 1.19 \\\\\nWithin-family (Llama-2 vs.\\ 3) & 161 / 308 & 61.3 & -- & -- \\\\\nRandom split (sanity) & 540 / 540 & 0.18 & -- & -- \\\\\nWithin-subject (avg, 5 subjects) & \\textit{varies} & 38.1 & -- & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Ground Truth Mismatch}\n\\label{sec:groundtruth}\n\nIf DIF captures differential contamination, flagged items should overlap with independently identified contaminated items. We evaluate this hypothesis against the web-overlap labels of \\citet{li2024contamination}, which classify MMLU items as ``contaminated'' based on verbatim matches in web training corpora. The enrichment ratio of DIF flags against these labels is 0.96 (\\Cref{tab:temporal_landscape}), indistinguishable from chance. This null result does not indicate that DIF fails to detect contamination. Semi-synthetic injection experiments demonstrate a clear dose-response relationship: injecting controlled differential contamination at exploitation rate $p = 0.5$ produces $\\Delta\\mathrm{TPR} = {+}0.508$, and at $p = 1.0$, $\\Delta\\mathrm{TPR} = {+}0.674$ (\\Cref{fig:dose_response}). The disconnect between DIF flags and web-overlap labels arises because the two methods answer fundamentally different questions.\n\nWeb-overlap labels measure \\emph{global exposure}: whether an item exists in publicly accessible training data. DIF measures \\emph{differential functioning}: whether an item's statistical relationship to overall ability changes across temporal cohorts. An item can be globally contaminated yet function identically across cohorts if all model generations have comparable access to the same training data. Conversely, an item can exhibit large DIF without any identifiable contamination source if changes in training methodology alter how models process certain question types. The Li et al.\\ labels are therefore the wrong ground truth for evaluating a differential detection method: the near-chance enrichment is expected, not evidence of failure.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_2_dose_response.pdf}\n\\caption{Semi-synthetic dose-response for DIF detection on MMLU. $\\Delta\\mathrm{TPR}$ increases monotonically with exploitation rate $p$, confirming that MH-DIF detects differential contamination when present. Baseline (no injection) produces $\\Delta\\mathrm{TPR} \\approx 0$.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\subsection{Structural Analysis}\n\\label{sec:structural}\n\nThree progressively refined approaches fail to reduce the temporal false positive rate below 31\\%, revealing a structural property of the data rather than a methodological limitation. Matched-ability quintile analysis restricts comparisons to models of similar total score and yields enrichment ratios of 0.94--1.04, with temporal FPR unchanged at approximately 0.31. IRT $\\theta$-conditioning with 20 ability strata achieves $r(\\theta, \\mathrm{total\\ score}) = 0.9986$ and FPR $= 0.312$, confirming that the external total score already captures nearly all ability variance relevant to DIF computation. Within-subject DIF analysis, intended to isolate subject-specific effects, finds C\\% $= 38.1\\%$ across subjects, exceeding the 25\\% threshold that would indicate viable bifactor structure. \\Cref{tab:structural_comparison} summarizes these results. The temporal FPR reflects genuine item-level instability that persists regardless of how ability is measured or conditioned.\n\n\\begin{table}[t]\n\\centering\n\\caption{Structural approaches to reducing temporal DIF. None reduces baseline FPR below 31\\%, indicating that the observed instability is not an artifact of ability matching.}\n\\label{tab:structural_comparison}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nApproach & Mechanism & Temporal FPR & TPR ($p{=}0.5$) & Outcome \\\\\n\\midrule\nBaseline (external) & Cross-benchmark total score & 0.314 & 0.834 & Reference \\\\\nMatched-ability & Within-quintile temporal DIF & ${\\sim}$0.31 & -- & Enrich.\\ 0.94--1.04 \\\\\n$\\theta$-conditioning & $\\theta$ replaces total score & 0.312 & 0.876 & $r(\\theta,\\mathrm{total}) {=} 0.9986$ \\\\\nWithin-subject & Per-subject DIF & -- & -- & C\\% $= 38.1\\%$ ($>$25\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Semi-Synthetic Framework Validation}\n\\label{sec:semisynthetic}\n\nThe semi-synthetic injection framework enables controlled evaluation of DIF detection by flipping incorrect responses to correct for a designated ``contaminated'' subset of items in the focal cohort at a specified exploitation rate $p$. The critical methodological finding is that the choice of matching strategy determines whether the framework produces valid results. Cross-subject matching computes the matching variable from subjects \\emph{other than} the one being tested, ensuring that the conditioning variable is unaffected by the injected contamination. Under this protocol, $\\Delta\\mathrm{FPR} = 0.000$ across all five MMLU subjects, and four of five subjects produce $\\Delta\\mathrm{TPR} > 0.3$ at $p = 0.5$ (\\Cref{fig:within_subject}). Within-subject matching, by contrast, computes the matching variable from the same subject where contamination was injected, which inflates FPR by an average of ${+}0.186$ because the matching variable absorbs part of the injection signal and violates the conditional independence assumption of the MH procedure. We adopt cross-subject matching as the standard protocol for all subsequent analyses and recommend it as default for semi-synthetic DIF evaluation on multi-subject benchmarks.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_3_within_subject_matching.pdf}\n\\caption{Cross-subject vs.\\ within-subject matching for semi-synthetic DIF detection. Cross-subject matching eliminates FPR inflation ($\\Delta\\mathrm{FPR} = 0.000$) while preserving detection power ($\\Delta\\mathrm{TPR} > 0.3$ for 4/5 subjects at $p = 0.5$). Within-subject matching inflates FPR by ${+}0.186$ on average.}\n\\label{fig:within_subject}\n\\end{figure}\n\n\\subsection{Local Independence}\n\\label{sec:q3}\n\nYen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. Within-subject item pairs show 11.3\\% of correlations exceeding $|Q3| > 0.20$, compared to 2.2\\% for cross-subject pairs (a $5{\\times}$ ratio, $p = 2.3 \\times 10^{-9}$). This mild local dependence within subjects is a contributing factor to elevated within-subject DIF rates but is not the primary driver of temporal instability: the cross-subject matching protocol already addresses this source of bias, and the temporal C\\% of 31.3\\% persists under external matching. Full Q3 distributions appear in Appendix~Figure~A2.\n\n\\subsection{Downstream Impact}\n\\label{sec:downstream}\n\nThe practical relevance of 31\\% item instability depends on whether unstable items affect model evaluation and benchmark rankings. We investigate this through a four-layer analysis that progresses from aggregate statistics to model-specific diagnostics.\n\n\\paragraph{Layer 1: Benchmark redundancy.} Spearman correlation between model rankings computed on all 12,508 items versus stable-only items (ETS~A/B) is $\\rho \\approx 0.997$. At the level of aggregate rankings, removing 31\\% of items changes almost nothing. This redundancy is a consequence of the large item pool: 12,508 items provide sufficient statistical mass that removing nearly a third does not alter rank order.\n\n\\paragraph{Layer 2: Signal concentration with circularity check.} Despite aggregate redundancy, DIF-flagged items carry more discriminative signal than the average item. Removing DIF items degrades ranking discriminability more than removing an equal number of random items ($z = -8$ to $-49$ across 21 experimental conditions). A circularity ablation, however, places this in context: DIF-based removal is the \\emph{least} disruptive among non-random removal strategies. Accuracy-gap removal produces $z = -156.5$, high-variance removal $z = -107.9$, and high-discrimination removal $z = -15.8$, compared to $z = -9.5$ for DIF removal. The Jaccard overlap between DIF-flagged and high-discrimination items is only 0.12. DIF items carry more signal than average, but DIF isolates differential behavior across cohorts specifically, not generally informative items.\n\n\\paragraph{Layer 3: Diagnostic lens.} Individual model families show distinctive DIF profiles that reveal which families disproportionately benefit from unstable items. Phi-3 and Llama-3 models gain ${+}700$ to ${+}850$ rank positions when evaluated on stable items only, suggesting inflated performance on items whose function changed between 2023 and 2024. Mistral-based model merges show the opposite pattern, losing $-400$ to $-587$ positions. A caveat applies: among the top 50 rank movers, 49 of 50 carry ``unknown'' family labels in METABENCH, limiting the scope of family-level interpretation.\n\n\\paragraph{Layer 4: Cross-benchmark signal.} The DIF instability pattern extends beyond MMLU. \\Cref{sec:gsm8k} presents a full replication on GSM8K with independent contamination validation using the GSM1K held-out set~\\citep{zhang2024gsm1k}. \\Cref{fig:downstream} visualizes the relationship between full and DIF-filtered rankings.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_4_downstream_impact.pdf}\n\\caption{Downstream impact of DIF-based item filtering on model rankings. Despite $\\rho \\approx 0.997$ overall, individual model families show systematic rank shifts when evaluated on stable items only, with Phi-3 and Llama-3 gaining and Mistral merges losing rank positions.}\n\\label{fig:downstream}\n\\end{figure}\n\n\\subsection{Cross-Benchmark Validation: GSM8K}\n\\label{sec:gsm8k}\n\nTo test whether temporal DIF is specific to MMLU or reflects a broader phenomenon in LLM benchmarking, we replicate the full analysis pipeline on GSM8K (1,319 items $\\times$ 6,702 models from METABENCH).\n\n\\paragraph{Temporal DIF.} Standard matching yields C\\% $= 18.9\\%$ for the temporal cohort comparison, with a random-split sanity check at 0.3\\%. The lower instability rate compared to MMLU (31.3\\%) is consistent with GSM8K's more homogeneous item structure: single-domain mathematical reasoning versus MMLU's 57 diverse subjects. The sanity check confirms that the signal is non-random.\n\n\\paragraph{Semi-synthetic validation.} Dose-response confirms detection power on this benchmark. Standard matching achieves $\\Delta\\mathrm{TPR} = {+}0.818$ at exploitation rate $p = 0.7$. External matching (using MMLU total score to match models for GSM8K DIF analysis) yields $\\Delta\\mathrm{TPR} = {+}0.517$ at $p = 0.7$, with $\\Delta\\mathrm{FPR}$ well-controlled. \\Cref{tab:gsm8k_comparison} compares key metrics across both benchmarks.\n\n\\paragraph{GSM1K contamination gap.} The GSM1K dataset~\\citep{zhang2024gsm1k} provides an independent measure of per-model contamination by comparing performance on the original GSM8K versus a held-out set of novel problems. For $N = 33$ models with both GSM1K scores and METABENCH evaluations, we correlate each model's contamination gap (GSM8K accuracy minus GSM1K accuracy) with the ranking advantage gained from DIF-flagged items. The observed correlation is $r = -0.478$ (95\\% CI $= [-0.71, -0.16]$, $p = 0.005$), with partial $r = -0.385$ after controlling for overall accuracy and permutation $p = 0.014$. Our original hypothesis predicted a \\emph{positive} correlation: models benefiting more from contamination should also benefit more from DIF items. The observed \\emph{negative} correlation indicates the opposite. DIF-C items resist contamination-based performance gains, and models with larger contamination gaps benefit \\emph{less} from these items. This result is suggestive at $N = 33$ and warrants replication with larger model populations, but it aligns with the broader interpretation that DIF captures item-level behavioral change distinct from simple memorization of training data. \\Cref{fig:gsm1k} shows the correlation scatter.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_5_gsm1k_dif_correlation.pdf}\n\\caption{GSM1K contamination gap vs.\\ DIF ranking advantage for $N = 33$ models. The negative correlation ($r = -0.478$, $p = 0.005$) indicates that models with larger contamination gaps benefit less from DIF-flagged items, contrary to the initial positive-correlation hypothesis.}\n\\label{fig:gsm1k}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-benchmark comparison of DIF analysis on MMLU and GSM8K. Both benchmarks exhibit temporal item instability with validated semi-synthetic detection power.}\n\\label{tab:gsm8k_comparison}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nMetric & MMLU & GSM8K \\\\\n\\midrule\nItems & 12,508 & 1,319 \\\\\nModels & 5,227 & 6,702 \\\\\nTemporal C\\% & 31.3\\% & 18.9\\% \\\\\nSanity C\\% & 0.18\\% & 0.3\\% \\\\\n$\\Delta$TPR ($p{=}0.7$, standard) & -- & ${+}0.818$ \\\\\n$\\Delta$TPR ($p{=}0.5$, external) & ${+}0.508$ & ${+}0.514$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
    "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe apply MH-DIF to the METABENCH dataset~\\citep{kipnis2024metabench}, which provides sparse response matrices for 5,227 models evaluated on 12,508 MMLU items~\\citep{hendrycks2021mmlu}. All temporal analyses define reference and focal cohorts by model release date (2023 vs.\\ 2024). We validate detection power through simulation, characterize temporal instability across multiple cohort designs, evaluate the relationship between DIF flags and existing contamination labels, and assess downstream consequences for benchmark rankings. Replication on GSM8K with cross-benchmark contamination validation appears in \\Cref{sec:gsm8k}.\n\n\\subsection{Validation: DIF Detection Power}\n\\label{sec:validation}\n\nTo confirm that MH-DIF detects differential item functioning at the sample sizes available in METABENCH, we conduct a power analysis using empirical MMLU IRT parameters. We simulate item response matrices where a controlled subset of items has injected DIF of varying magnitude ($|\\Delta_{\\mathrm{MH}}| \\geq 1.4$) and evaluate ETS~C classification across sample sizes $N \\in \\{40, 80, 160, 320\\}$ per cohort. At $N \\geq 80$, ETS~C achieves true positive rates of 0.68--0.80 with false positive rates of 0.036--0.042 and AUC of 0.93--0.94. The temporal cohort sizes in our analysis ($N_{\\mathrm{ref}} = 1{,}080$, $N_{\\mathrm{focal}} = 807$) far exceed this threshold, and statistical power is not a limiting factor for the results reported below. Full simulation results with confidence intervals appear in Appendix~Table~A1.\n\n\\subsection{Temporal Comparability: 31\\% Item Instability}\n\\label{sec:temporal}\n\nThe central finding of this paper is that a substantial fraction of MMLU items behave differently across model generations. Comparing models released in 2023 ($N = 1{,}080$) against models released in 2024 ($N = 807$), 31.3\\% of items receive ETS~C classification ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$). Applying Benjamini-Hochberg FDR correction at $q = 0.05$ reduces this from 31.32\\% to 31.30\\%, removing only 3 items. The minimal impact of FDR correction reflects the fact that the ETS classification system imposes a dual threshold on both effect size and statistical significance, which already provides implicit multiple-testing protection. In absolute terms, nearly one in three MMLU items exhibits a large shift in its statistical relationship to overall model ability between the two cohort periods.\n\nThree control conditions establish that this instability reflects genuine temporal change rather than methodological artifacts. A random split of the 2023 cohort into two equal halves produces only 0.18\\% ETS~C items, confirming that sampling noise alone does not generate large-scale DIF. An ability-quintile comparison (lowest-scoring vs.\\ highest-scoring models within the same temporal cohort) yields 2.9\\% ETS~C items, indicating that ability differences alone are insufficient to produce the observed instability. A within-family comparison of Llama-2 ($N = 161$) and Llama-3 ($N = 308$) models produces 61.3\\% ETS~C items. This elevated rate is consistent with the known sensitivity of MH-DIF to ability differences between groups~\\citep{holland1988mh}: models from different generations within a single family exhibit large ability gaps that confound the DIF signal. The contrast between 2.9\\% (ability-controlled) and 61.3\\% (ability-confounded) brackets the temporal rate of 31.3\\% and confirms that it captures a mixture of genuine item instability and residual ability differences.\n\nThe instability penetrates within every knowledge domain. Within-subject analysis yields an average of 38.1\\% ETS~C items across all five MMLU subjects (range: 31--45\\%), and the ecological correlation between subject-level accuracy improvement and subject-level C\\% is $\\rho = 0.307$ ($p = 0.02$). This ecological correlation could suggest that domains where models improved most also exhibit the most instability. Item-level logistic regression, however, reveals that domain accuracy improvement explains only 2.4 percentage points of the 31.3\\% temporal C\\% (pseudo $R^2 = 0.0007$; counterfactual C\\% with domain improvement regressed out $= 29.0\\%$). Of the observed instability, 92.4\\% is unrelated to aggregate domain-level accuracy gains and instead reflects item-specific changes in how models interact with individual questions.\n\nArchitecture heterogeneity is a non-issue for this analysis. The METABENCH MMLU population is 99.98\\% decoder-only (5,226 of 5,227 models). Excluding the single encoder-decoder model yields C\\% $= 31.32\\%$ with Jaccard similarity of 1.0 between flagged item sets. Threshold sensitivity analysis confirms robustness across the full ETS range: C\\% $= 48.9\\%$ at $|\\Delta_{\\mathrm{MH}}| \\geq 1.0$, $31.3\\%$ at $\\geq 1.5$ (the standard ETS~C threshold), $18.3\\%$ at $\\geq 2.0$, and $10.2\\%$ at $\\geq 2.5$. The qualitative conclusion holds at every threshold. \\Cref{tab:temporal_landscape} summarizes the DIF landscape across all cohort comparisons.\n\n\\begin{table}[t]\n\\centering\n\\caption{DIF landscape across cohort definitions. ETS~C denotes the percentage of items with $|\\Delta_{\\mathrm{MH}}| \\geq 1.5$. FPR is measured against Li et al.\\ web-overlap labels on the ``clean'' (non-overlapping) subset. Enrichment is the ratio of observed to expected overlap between DIF flags and web-overlap labels.}\n\\label{tab:temporal_landscape}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCohort Definition & $N_{\\mathrm{ref}}$ / $N_{\\mathrm{focal}}$ & ETS~C (\\%) & FPR (Li clean) & Enrichment \\\\\n\\midrule\nTemporal (2023 vs.\\ 2024) & 1,080 / 807 & 31.3 & 0.318 & 0.96 \\\\\nAbility quintile (Q1--2 vs.\\ Q4--5) & ${\\sim}$2,600 / ${\\sim}$2,600 & 2.9 & 0.027 & 1.19 \\\\\nWithin-family (Llama-2 vs.\\ 3) & 161 / 308 & 61.3 & -- & -- \\\\\nRandom split (sanity) & 540 / 540 & 0.18 & -- & -- \\\\\nWithin-subject (avg, 5 subjects) & \\textit{varies} & 38.1 & -- & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Ground Truth Mismatch}\n\\label{sec:groundtruth}\n\nIf DIF captures differential contamination, flagged items should overlap with independently identified contaminated items. We evaluate this hypothesis against the web-overlap labels of \\citet{li2024contamination}, which classify MMLU items as ``contaminated'' based on verbatim matches in web training corpora. The enrichment ratio of DIF flags against these labels is 0.96 (\\Cref{tab:temporal_landscape}), indistinguishable from chance. This null result does not indicate that DIF fails to detect contamination. Semi-synthetic injection experiments demonstrate a clear dose-response relationship: injecting controlled differential contamination at exploitation rate $p = 0.5$ produces $\\Delta\\mathrm{TPR} = {+}0.508$, and at $p = 1.0$, $\\Delta\\mathrm{TPR} = {+}0.674$ (\\Cref{fig:dose_response}). The disconnect between DIF flags and web-overlap labels arises because the two methods answer fundamentally different questions.\n\nWeb-overlap labels measure \\emph{global exposure}: whether an item exists in publicly accessible training data. DIF measures \\emph{differential functioning}: whether an item's statistical relationship to overall ability changes across temporal cohorts. An item can be globally contaminated yet function identically across cohorts if all model generations have comparable access to the same training data. Conversely, an item can exhibit large DIF without any identifiable contamination source if changes in training methodology alter how models process certain question types. The Li et al.\\ labels are therefore the wrong ground truth for evaluating a differential detection method: the near-chance enrichment is expected, not evidence of failure.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_2_dose_response.pdf}\n\\caption{Semi-synthetic dose-response for DIF detection on MMLU. $\\Delta\\mathrm{TPR}$ increases monotonically with exploitation rate $p$, confirming that MH-DIF detects differential contamination when present. Baseline (no injection) produces $\\Delta\\mathrm{TPR} \\approx 0$.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\subsection{Structural Analysis}\n\\label{sec:structural}\n\nThree progressively refined approaches fail to reduce the temporal false positive rate below 31\\%, revealing a structural property of the data rather than a methodological limitation. Matched-ability quintile analysis restricts comparisons to models of similar total score and yields enrichment ratios of 0.94--1.04, with temporal FPR unchanged at approximately 0.31. IRT $\\theta$-conditioning with 20 ability strata achieves $r(\\theta, \\mathrm{total\\ score}) = 0.9986$ and FPR $= 0.312$, confirming that the external total score already captures nearly all ability variance relevant to DIF computation. Within-subject DIF analysis, intended to isolate subject-specific effects, finds C\\% $= 38.1\\%$ across subjects, exceeding the 25\\% threshold that would indicate viable bifactor structure. \\Cref{tab:structural_comparison} summarizes these results. The temporal FPR reflects genuine item-level instability that persists regardless of how ability is measured or conditioned.\n\n\\begin{table}[t]\n\\centering\n\\caption{Structural approaches to reducing temporal DIF. None reduces baseline FPR below 31\\%, indicating that the observed instability is not an artifact of ability matching.}\n\\label{tab:structural_comparison}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nApproach & Mechanism & Temporal FPR & TPR ($p{=}0.5$) & Outcome \\\\\n\\midrule\nBaseline (external) & Cross-benchmark total score & 0.314 & 0.834 & Reference \\\\\nMatched-ability & Within-quintile temporal DIF & ${\\sim}$0.31 & -- & Enrich.\\ 0.94--1.04 \\\\\n$\\theta$-conditioning & $\\theta$ replaces total score & 0.312 & 0.876 & $r(\\theta,\\mathrm{total}) {=} 0.9986$ \\\\\nWithin-subject & Per-subject DIF & -- & -- & C\\% $= 38.1\\%$ ($>$25\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Semi-Synthetic Framework Validation}\n\\label{sec:semisynthetic}\n\nThe semi-synthetic injection framework enables controlled evaluation of DIF detection by flipping incorrect responses to correct for a designated ``contaminated'' subset of items in the focal cohort at a specified exploitation rate $p$. The critical methodological finding is that the choice of matching strategy determines whether the framework produces valid results. Cross-subject matching computes the matching variable from subjects \\emph{other than} the one being tested, ensuring that the conditioning variable is unaffected by the injected contamination. Under this protocol, $\\Delta\\mathrm{FPR} = 0.000$ across all five MMLU subjects, and four of five subjects produce $\\Delta\\mathrm{TPR} > 0.3$ at $p = 0.5$ (\\Cref{fig:within_subject}). Within-subject matching, by contrast, computes the matching variable from the same subject where contamination was injected, which inflates FPR by an average of ${+}0.186$ because the matching variable absorbs part of the injection signal and violates the conditional independence assumption of the MH procedure. We adopt cross-subject matching as the standard protocol for all subsequent analyses and recommend it as default for semi-synthetic DIF evaluation on multi-subject benchmarks.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_3_within_subject_matching.pdf}\n\\caption{Cross-subject vs.\\ within-subject matching for semi-synthetic DIF detection. Cross-subject matching eliminates FPR inflation ($\\Delta\\mathrm{FPR} = 0.000$) while preserving detection power ($\\Delta\\mathrm{TPR} > 0.3$ for 4/5 subjects at $p = 0.5$). Within-subject matching inflates FPR by ${+}0.186$ on average.}\n\\label{fig:within_subject}\n\\end{figure}\n\n\\subsection{Local Independence}\n\\label{sec:q3}\n\nYen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. Within-subject item pairs show 11.3\\% of correlations exceeding $|Q3| > 0.20$, compared to 2.2\\% for cross-subject pairs (a $5{\\times}$ ratio, $p = 2.3 \\times 10^{-9}$). This mild local dependence within subjects is a contributing factor to elevated within-subject DIF rates but is not the primary driver of temporal instability: the cross-subject matching protocol already addresses this source of bias, and the temporal C\\% of 31.3\\% persists under external matching. Full Q3 distributions appear in Appendix~Figure~A2.\n\n\\subsection{Downstream Impact}\n\\label{sec:downstream}\n\nThe practical relevance of 31\\% item instability depends on whether unstable items affect model evaluation and benchmark rankings. We investigate this through a four-layer analysis that progresses from aggregate statistics to model-specific diagnostics.\n\n\\paragraph{Layer 1: Benchmark redundancy.} Spearman correlation between model rankings computed on all 12,508 items versus stable-only items (ETS~A/B) is $\\rho \\approx 0.997$. At the level of aggregate rankings, removing 31\\% of items changes almost nothing. This redundancy is a consequence of the large item pool: 12,508 items provide sufficient statistical mass that removing nearly a third does not alter rank order.\n\n\\paragraph{Layer 2: Signal concentration with circularity check.} Despite aggregate redundancy, DIF-flagged items carry more discriminative signal than the average item. Removing DIF items degrades ranking discriminability more than removing an equal number of random items ($z = -8$ to $-49$ across 21 experimental conditions). A circularity ablation, however, places this in context: DIF-based removal is the \\emph{least} disruptive among non-random removal strategies. Accuracy-gap removal produces $z = -156.5$, high-variance removal $z = -107.9$, and high-discrimination removal $z = -15.8$, compared to $z = -9.5$ for DIF removal. The Jaccard overlap between DIF-flagged and high-discrimination items is only 0.12. DIF items carry more signal than average, but DIF isolates differential behavior across cohorts specifically, not generally informative items.\n\n\\paragraph{Layer 3: Diagnostic lens.} Individual model families show distinctive DIF profiles that reveal which families disproportionately benefit from unstable items. Phi-3 and Llama-3 models gain ${+}700$ to ${+}850$ rank positions when evaluated on stable items only, suggesting inflated performance on items whose function changed between 2023 and 2024. Mistral-based model merges show the opposite pattern, losing $-400$ to $-587$ positions. A caveat applies: among the top 50 rank movers, 49 of 50 carry ``unknown'' family labels in METABENCH, limiting the scope of family-level interpretation.\n\n\\paragraph{Layer 4: Cross-benchmark signal.} The DIF instability pattern extends beyond MMLU. \\Cref{sec:gsm8k} presents a full replication on GSM8K with independent contamination validation using the GSM1K held-out set~\\citep{zhang2024gsm1k}. \\Cref{fig:downstream} visualizes the relationship between full and DIF-filtered rankings.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_4_downstream_impact.pdf}\n\\caption{Downstream impact of DIF-based item filtering on model rankings. Despite $\\rho \\approx 0.997$ overall, individual model families show systematic rank shifts when evaluated on stable items only, with Phi-3 and Llama-3 gaining and Mistral merges losing rank positions.}\n\\label{fig:downstream}\n\\end{figure}\n\n\\subsection{Cross-Benchmark Validation: GSM8K}\n\\label{sec:gsm8k}\n\nTo test whether temporal DIF is specific to MMLU or reflects a broader phenomenon in LLM benchmarking, we replicate the full analysis pipeline on GSM8K (1,319 items $\\times$ 6,702 models from METABENCH).\n\n\\paragraph{Temporal DIF.} Standard matching yields C\\% $= 18.9\\%$ for the temporal cohort comparison, with a random-split sanity check at 0.3\\%. The lower instability rate compared to MMLU (31.3\\%) is consistent with GSM8K's more homogeneous item structure: single-domain mathematical reasoning versus MMLU's 57 diverse subjects. The sanity check confirms that the signal is non-random.\n\n\\paragraph{Semi-synthetic validation.} Dose-response confirms detection power on this benchmark. Standard matching achieves $\\Delta\\mathrm{TPR} = {+}0.818$ at exploitation rate $p = 0.7$. External matching (using MMLU total score to match models for GSM8K DIF analysis) yields $\\Delta\\mathrm{TPR} = {+}0.517$ at $p = 0.7$, with $\\Delta\\mathrm{FPR}$ well-controlled. \\Cref{tab:gsm8k_comparison} compares key metrics across both benchmarks.\n\n\\paragraph{GSM1K contamination gap.} The GSM1K dataset~\\citep{zhang2024gsm1k} provides an independent measure of per-model contamination by comparing performance on the original GSM8K versus a held-out set of novel problems. For $N = 33$ models with both GSM1K scores and METABENCH evaluations, we correlate each model's contamination gap (GSM8K accuracy minus GSM1K accuracy) with the ranking advantage gained from DIF-flagged items. The observed correlation is $r = -0.478$ (95\\% CI $= [-0.71, -0.16]$, $p = 0.005$), with partial $r = -0.385$ after controlling for overall accuracy and permutation $p = 0.014$. Our original hypothesis predicted a \\emph{positive} correlation: models benefiting more from contamination should also benefit more from DIF items. The observed \\emph{negative} correlation indicates the opposite. DIF-C items resist contamination-based performance gains, and models with larger contamination gaps benefit \\emph{less} from these items. This result is suggestive at $N = 33$ and warrants replication with larger model populations, but it aligns with the broader interpretation that DIF captures item-level behavioral change distinct from simple memorization of training data. \\Cref{fig:gsm1k} shows the correlation scatter.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_5_gsm1k_dif_correlation.pdf}\n\\caption{GSM1K contamination gap vs.\\ DIF ranking advantage for $N = 33$ models. The negative correlation ($r = -0.478$, $p = 0.005$) indicates that models with larger contamination gaps benefit less from DIF-flagged items, contrary to the initial positive-correlation hypothesis.}\n\\label{fig:gsm1k}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-benchmark comparison of DIF analysis on MMLU and GSM8K. Both benchmarks exhibit temporal item instability with validated semi-synthetic detection power.}\n\\label{tab:gsm8k_comparison}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nMetric & MMLU & GSM8K \\\\\n\\midrule\nItems & 12,508 & 1,319 \\\\\nModels & 5,227 & 6,702 \\\\\nTemporal C\\% & 31.3\\% & 18.9\\% \\\\\nSanity C\\% & 0.18\\% & 0.3\\% \\\\\n$\\Delta$TPR ($p{=}0.7$, standard) & -- & ${+}0.818$ \\\\\n$\\Delta$TPR ($p{=}0.5$, external) & ${+}0.508$ & ${+}0.514$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-21T04:11:19.745980+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-21T04:11:19.746133+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper && grep -n \"—\" sections/experiments.tex && echo \"FOUND EM-DASH\" || echo \"NO EM-DASH: OK\"",
  "description": "Check for em-dashes in experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper && grep -n \"—\" sections/experiments.tex && echo \"FOUND EM-DASH\" || echo \"NO EM-DASH: OK\"",
    "description": "Check for em-dashes in experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-21T04:11:19.746261+00:00_

NO EM-DASH: OK

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-21T04:11:19.746380+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \" – \" sections/experiments.tex && echo \"FOUND EN-DASH\" || echo \"NO EXPLANATORY EN-DASH: OK\"",
  "description": "Check for explanatory en-dashes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \" – \" sections/experiments.tex && echo \"FOUND EN-DASH\" || echo \"NO EXPLANATORY EN-DASH: OK\"",
    "description": "Check for explanatory en-dashes"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-21T04:11:19.746498+00:00_

NO EXPLANATORY EN-DASH: OK

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-21T04:11:19.746623+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -nP \"ing[,.]\" sections/experiments.tex | grep -v \"matching\\|conditioning\\|scoring\\|testing\\|ranking\\|missing\\|training\\|existing\\|benchmarking\\|using\\|\\\\\\\\string\\|meaning\" | head -20; echo \"---\"; grep -niP \"(furthermore|moreover|additionally|notably|it is worth noting|delve|leverage|utilize|facilitate)\" sections/experiments.tex | head -10; echo \"---\"; grep -n \"\\\\\\\\hline\" sections/experiments.tex | head -5; echo \"---\"; grep -n \"\\\\\\\\begin{center}\" sections/experiments.tex | head -5; echo \"---\"; grep -n \"^%\" sections/experiments.tex | head -5",
  "description": "Check for AI-style markers and LaTeX rule violations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -nP \"ing[,.]\" sections/experiments.tex | grep -v \"matching\\|conditioning\\|scoring\\|testing\\|ranking\\|missing\\|training\\|existing\\|benchmarking\\|using\\|\\\\\\\\string\\|meaning\" | head -20; echo \"---\"; grep -niP \"(furthermore|moreover|additionally|notably|it is worth noting|delve|leverage|utilize|facilitate)\" sections/experiments.tex | head -10; echo \"---\"; grep -n \"\\\\\\\\hline\" sections/experiments.tex | head -5; echo \"---\"; grep -n \"\\\\\\\\begin{center}\" sections/experiments.tex | head -5; echo \"---\"; grep -n \"^%\" sections/experiments.tex | head -5",
    "description": "Check for AI-style markers and LaTeX rule violations"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-21T04:11:19.746761+00:00_

---
---
---
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-21T04:11:19.746889+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$%&~^_]//g; s/  */ /g' | wc -w",
  "description": "Estimate word count of experiments section"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$%&~^_]//g; s/  */ /g' | wc -w",
    "description": "Estimate word count of experiments section"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-21T04:11:19.747003+00:00_

2053

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-21T04:11:19.747113+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
  "description": "Raw word count including markup"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
    "description": "Raw word count including markup"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-21T04:11:19.747222+00:00_

2424 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-21T04:11:19.747344+00:00_

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
  "session": "worker_paper_writing_experiments_20260521T040002",
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

_source line 66 · 2026-05-21T04:11:19.747457+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-21T04:11:19.747574+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "experiments_section_v1",
  "type": "paper",
  "description": "Experiments section (§4) for ICLR 2027 paper. 8 subsections: validation, temporal comparability (31% instability), ground truth mismatch, structural analysis, semi-synthetic framework, local independence, downstream impact (four-layer), GSM8K cross-benchmark validation. Includes 3 tables and 4 figures.",
  "project": "irt_equated_bench_regen",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
  "tags": "['paper', 'experiments', 'latex', 'iclr2027']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "experiments_section_v1",
    "type": "paper",
    "description": "Experiments section (§4) for ICLR 2027 paper. 8 subsections: validation, temporal comparability (31% instability), ground truth mismatch, structural analysis, semi-synthetic framework, local independence, downstream impact (four-layer), GSM8K cross-benchmark validation. Includes 3 tables and 4 figures.",
    "project": "irt_equated_bench_regen",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
    "tags": "['paper', 'experiments', 'latex', 'iclr2027']"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-21T04:11:19.747734+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_f524dc\", \"name\": \"experiments_section_v1\", \"type\": \"paper\", \"description\": \"Experiments section (§4) for ICLR 2027 paper. 8 subsections: validation, temporal comparability (31% instability), ground truth mismatch, structural analysis, semi-synthetic framework, local independence, downstream impact (four-layer), GSM8K cross-benchmark validation. Includes 3 tables and 4 figures.\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/paper/experiments.tex\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T04:11:04.241277+00:00\", \"tags\": [\"paper\", \"experiments\", \"latex\", \"iclr2027\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_20260521T040002",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 69 · 2026-05-21T04:11:19.747911+00:00_

Experiments section written to `paper/sections/experiments.tex`. Summary:

**8 subsections, 3 tables, 4 figures, ~2050 rendered words.**

- **§4.1** Validation: power analysis confirms TPR 0.68--0.80, FPR 0.036--0.042 at cohort sizes (1 paragraph, Appendix ref)
- **§4.2** Temporal comparability: 31.3% ETS C, BH FDR removes only 3 items, sanity 0.18%, ability-quintile 2.9%, within-family 61.3%, within-subject 38.1%, 92.4% unexplained by domain improvement, architecture non-issue, threshold-robust (Table 1)
- **§4.3** Ground truth mismatch: enrichment 0.96 vs Li et al., dose-response ΔTPR +0.508/+0.674, web-overlap = wrong ground truth (Figure 2)
- **§4.4** Structural analysis: three approaches fail to reduce FPR below 31% (Table 2)
- **§4.5** Semi-synthetic: cross-subject matching ΔFPR=0.000, within-subject inflates +0.186 (Figure 3)
- **§4.6** Q3 local independence: 11.3% vs 2.2% (5x, p=2.3e-9), mild contributing factor
- **§4.7** Downstream impact: four layers (ρ≈0.997 redundancy, signal concentration with circularity ablation, model-family diagnostics, cross-benchmark) (Figure 4)
- **§4.8** GSM8K: C%=18.9%, ΔTPR=+0.818, GSM1K r=−0.478 negative correlation honestly reported (Figure 5, Table 3)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_experiments_20260521T040002"
}
```

</details>

---

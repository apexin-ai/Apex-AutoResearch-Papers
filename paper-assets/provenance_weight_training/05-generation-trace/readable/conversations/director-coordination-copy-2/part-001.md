# Director coordination — Part 1 of 5

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Conversation logs

[Transcript overview](../director-coordination-copy-2.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/5a/5a5f768420cdca035482.json)

## Round 1

## Round 1

70 recorded events


### User

_source line 1 · 2026-05-18T06:19:42.592820+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: provenance_weight_training
- 论文路径: projects/provenance_weight_training/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-18T06:19:48.234582+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-18T06:19:48.335886+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-18T06:19:50.945178+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-18T06:19:50.995722+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-18T06:19:57.668743+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-18T06:19:57.669118+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-18T06:20:01.391631+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-18T06:20:01.392233+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-18T06:20:10.097771+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-18T06:20:11.503185+00:00_

{"result":"# 项目 provenance_weight_training 概况\n\n## 实验状态 (121 个)\n\n- **adaptive_seed42**: DONE (success) — \n- **uniform_seed456**: DONE (success) — \n- **uniform_seed123**: DONE (success) — \n- **uniform_seed42**: DONE (success) — \n- **detector_modernbert**: DONE (killed) — \n- **nmin1_seed42**: DONE (success) — \n- **golden_ratio_seed42**: DONE (success) — \n- **tau_0.6_seed42**: DONE (killed) — \n- **grid_b_low_seed42**: DONE (failed) — \n- **grid_b1_5_seed456**: DONE (success) — \n- **grid_b1_0_seed456**: DONE (success) — \n- **grid_b0_5_seed456**: DONE (success) — \n- **grid_b_seed42_batch**: DONE (success) — \n- **diagnostic_contamination100**: DONE (killed) — \n- **detector_tfidf_lr**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| contamination_60_grid_b0_3_seed42 | Grid b=0.3 at ρ=0.6: tests whether grid-best remains near b=0.3 at higher contamination. If PPL ≈ contamination_60_seed42_r2 (adaptive, 17.74), confirms adaptive ≈ grid-best holds cross-ρ, strengthening Claim 2 generality. | — | — | — |\n| contamination_60_random_seed42 | Random reweighting baseline at ρ=0.6: random weights ignore detector scores entirely. If PPL > ESS-only (17.77) and > uniform (17.766), completes four-tier ablation hierarchy (adaptive < uniform < ESS-only < random) at ρ=0.6, confirming Claim 1 structural argument holds cross-ρ. | — | — | — |\n\n## 待处理\n- contamination_60_random_seed456（准备中）\n- contamination_60_random_seed123（准备中）\n- contamination_60_ess_only_seed456（准备中）\n- contamination_60_ess_only_seed123（准备中）\n\n## 近期结论\n- **grid_b0_2_seed456** (success): Cross-seed replication (seed456) of grid b=0.2: 3rd seed for b=0.2 plateau confirmation, completing Claim 2 cross-seed grid curve at the optimal region. ← 基于 grid_b0_2_seed42\n- **grid_b0_2_seed123** (success): Cross-seed replication (seed123) of grid b=0.2: if PPL ≈ grid_b0_2_seed42 (17.6
…[truncated 1798 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-18T06:20:11.955613+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-18T06:20:11.956100+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\graphicspath{{../../artifacts/figures/}}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{algorithm}
14	\usepackage{algorithmic}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{hyperref}
20	
21	\newtheorem{proposition}{Proposition}
22	\newtheorem{definition}{Definition}
23	
24	\newcommand{\bstar}{b^*}
25	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
26	\newcommand{\nmin}{n_{\min}}
27	\newcommand{\btau}{b_{\tau}}
28	\newcommand{\bess}{b_{\mathrm{ESS}}}
29	
30	\title{Minimum Intervention Reweighting: Adaptive Exponent Selection\\for Contamination-Aware Pretraining}
31	
32	\author{Anonymous}
33	
34	\begin{document}
35	\maketitle
36	
37	\begin{abstract}
38	\input{sections/abstract}
39	\end{abstract}
40	
41	\section{Introduction}
42	\label{sec:intro}
43	\input{sections/introduction}
44	
45	\section{Related Work}
46	\label{sec:related}
47	\input{sections/related_work}
48	
49	\section{Method}
50	\label{sec:method}
51	\input{sections/method}
52	
53	\section{Experimental Setup}
54	\label{sec:experiments}
55	\input{sections/experiments}
56	
57	\section{Results}
58	\label{sec:results}
59	\input{sections/results}
60	
61	\section{Discussion}
62	\label{sec:discussion}
63	\input{sections/discussion}
64	
65	\section{Conclusion}
66	\label{sec:conclusion}
67	\input{sections/conclusion}
68	
69	\section*{Limitations}
70	\label{sec:limitations}
71	\input{sections/limitations}
72	
73	\bibliography{references}
74	
75	\appendix
76	\input{sections/appendix}
77	
78	\end{document}
79	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-18T06:20:12.470581+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 15 · 2026-05-18T06:20:12.671953+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 16 · 2026-05-18T06:20:21.611056+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on the search results, here is the key information about EMNLP 2026 call for papers submission guidelines and author instructions:

## Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## Important Dates

ARR submission deadline (long & short papers) is May 25, 2026, with rev
…[truncated 1888 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 9140
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-18T06:20:21.611449+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 8939
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-18T06:20:30.346790+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format guidelines page limit template requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format guidelines page limit template requirements"
  }
}
```

</details>

---


### Tool call

_source line 19 · 2026-05-18T06:20:32.153039+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper"
  }
}
```

</details>

---


### Tool result

_source line 20 · 2026-05-18T06:20:32.535785+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 382
}
```

</details>

---


### Tool call

_source line 21 · 2026-05-18T06:20:32.569072+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 22 · 2026-05-18T06:20:32.621584+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-18T06:20:36.377118+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format guidelines page limit template requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here are the ACL Rolling Review 2026 submission format guidelines:

## Page Limits

All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages). More specifically, review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references.

#
…[truncated 1017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 6030
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-18T06:20:45.518649+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-18T06:20:45.569394+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-18T06:20:48.080982+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-18T06:20:48.582927+00:00_

1	Web corpora now contain an estimated 20--60\% machine-generated text, and training on such contaminated data risks model collapse.
2	Detect-and-reweight methods suppress likely-synthetic samples via $w(x) = (1-q(x))^b$, but the exponent $b$ critically determines outcomes and requires per-model grid search (typically multiple complete training runs) to tune.
3	
4	We propose a dual-constrained adaptive exponent $b^*$ derived per-batch from detector scores alone: find the minimum $b$ such that the weighted effective real proportion $\alpha_{\mathrm{eff}}(b) \geq \tau$ (quality floor), subject to $\mathrm{ESS}(b) \geq n_{\min}$ (stability ceiling).
5	This minimum intervention principle applies only as much downweighting as needed, with zero validation cost.
6	
7	On Qwen3-0.6B continued pretraining (132M FineWeb tokens, 40\% synthetic contamination), adaptive $b^*$ is statistically indistinguishable from the grid-searched optimum (3-seed means: PPL 17.651 vs.\ 17.620, $p{=}0.30$).
8	A complete ablation confirms that both detector signal and minimum intervention are necessary: random reweighting degrades performance (17.803), ESS-only maximum intervention provides no improvement (17.737 vs.\ uniform 17.694), and only the dual-constrained method improves.
9	The advantage extends to $\rho{=}0.6$ (3-seed $\Delta{=}{-}0.028$, $p{<}0.01$), where the ESS-only/uniform gap collapses but adaptive reweighting maintains its improvement through the quality constraint alone.
10	Hard filtering achieves lower absolute PPL (17.290) but requires a calibrated detection threshold that reweighting avoids.
11	The quality threshold $\tau$ is robust across $[0.5, 0.8]$, and a lightweight TF-IDF + logistic regression detector (AUC = 0.939, calibrated ECE = 0.048) suffices, suggesting that score calibration may matter as much as raw classification accuracy.
12	
13	Principled per-batch exponent derivation eliminates grid search while retaining the effectiveness of detect-and-reweight pretraining
…[truncated 5 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-18T06:20:48.633517+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-18T06:20:48.634192+00:00_

1	Web corpora increasingly contain machine-generated text.
2	Recent estimates place the synthetic fraction at 20--60\% of crawled data~\citep{cheng2025contamination}, and this share grows as language models are deployed for content production at scale.
3	Training on such contaminated data has concrete consequences: \citet{shumailov2024model} show that recursive training on model outputs leads to irreversible quality degradation (\emph{model collapse}), and \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger this failure mode, ruling out data scaling as a remedy.
4	A central difficulty is that the contamination proportion in any given corpus is unknown: synthetic text enters through diverse, uncoordinated channels with no centralized provenance record.
5	The prevalence, severity, and opacity of synthetic contamination make contamination-aware pretraining a practical necessity.
6	
7	A natural response is \emph{detect-and-reweight}: suppress likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a classifier's synthetic probability estimate.
8	However, the exponent $b$ critically determines outcomes and requires per-model validation-set grid search~\citep{drayson2025detection}; alternative approaches require the exact contamination ratio~\citep{he2025golden} or a well-calibrated detection threshold for hard filtering~\citep{feng2025beyond}.
9	
10	Given per-sample detector scores $q(x)$, how should one choose $b$ without a validation set or known contamination proportion?
11	We formulate this as a dual-constrained optimization over each training batch: find the smallest $b$ that ensures the weighted effective real proportion $\aeff(b)$ reaches a quality threshold $\tau$, while keeping Kish's effective sample size $\mathrm{ESS}(b)$ above a stability floor $\nmin$.
12	The quality constraint has theoretical grounding: convergence rate under contaminated training improves with the effec
…[truncated 3098 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-18T06:20:48.885406+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-18T06:20:49.387656+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.
5	\citet{cheng2025contamination} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\% of web corpora.
6	These results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
7	
8	\paragraph{Detection and Filtering of Machine-Generated Text.}
9	Given the severity of contamination, a natural response is to detect and remove synthetic content.
10	DetectGPT~\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\% Prob~\citep{shi2024minkprob} uses the average log-probability of the lowest-$k$\% tokens as a reference-free signal.
11	Both produce continuous confidence scores suitable as input to downstream weighting, including ours.
12	On the mitigation side, \citet{feng2025beyond} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples.
13	\citet{guo2025escaping} similarly rely on verification-based selection.
14	Hard filtering requires a precision--recall threshold; soft reweighting avoids this trade-off by assigning continuous weights.
15	
16	Most directly related to our work, \citet{drayson2025detection} propose $w_j = (1{-}q_j)^b$ for collapse prevention via detect-and-reweight, where $q_j$ is the detector's synthetic 
…[truncated 3369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-18T06:20:49.388141+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-18T06:20:49.839768+00:00_

1	\subsection{Problem Setup}
2	\label{sec:setup}
3	
4	Let $\mathcal{D} = \mathcal{D}_{\mathrm{real}} \cup \mathcal{D}_{\mathrm{synth}}$ denote a pretraining corpus containing both human-authored and machine-generated text.
5	The contamination ratio $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$ is unknown, a realistic assumption for web-scale corpora where synthetic content enters from diverse, uncoordinated sources~\citep{cheng2025contamination}.
6	
7	A pre-trained detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$.
8	Following \citet{drayson2025detection}, we weight each sample as
9	\begin{equation}
10	  w(x) = (1 - q(x))^{b},
11	  \label{eq:weight}
12	\end{equation}
13	where $b \geq 0$ controls downweighting intensity: $b = 0$ recovers uniform training, while larger $b$ progressively suppresses high-$q$ samples.
14	\citet{drayson2025detection} select $b$ via validation-set grid search, obtaining different optimal values for different model scales ($b{=}10$ for ${\leq}360$M parameters, $b{=}1$ for 1.7B).
15	We instead derive $b$ per-batch from the batch's own $q$-score distribution, requiring no held-out validation data.
16	
17	\subsection{Dual-Constraint Framework}
18	\label{sec:dual}
19	
20	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with detector scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$, we define two batch-level diagnostics that jointly determine $b$.
21	
22	\paragraph{Effective real proportion.}
23	Let $r_i = \mathbf{1}[q_i \leq 0.5]$ estimate whether sample $x_i$ is human-authored.
24	The \emph{effective real proportion}
25	\begin{equation}
26	  \alpha_{\mathrm{eff}}(b) = \frac{\sum_{i=1}^{B} w_i(b) \cdot r_i}{\sum_{i=1}^{B} w_i(b)}
27	  \label{eq:alpha}
28	\end{equation}
29	measures the share of total weight allocated to likely-real samples.
30	At $b = 0$, $\alpha_{\mathrm{eff}}$ equals the raw real fraction in the batch; increasing $b$ shifts weight toward low-$q$ samples, raising $\alpha_{\mathrm{ef
…[truncated 8268 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-18T06:20:49.840243+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-18T06:20:50.445142+00:00_

1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo2024fineweb} as the real-data source.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang2025qwen3}, the same architecture used for continued pretraining, and inject them at ratio $\rho = 0.4$ via uniform random mixing.
4	This self-contamination design creates a challenging detection scenario where generator and trainee share the same distribution.
5	
6	\paragraph{Detector.}
7	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split (AUC\,=\,0.939, calibrated ECE\,=\,0.048 after temperature scaling with $T = 0.204$).
8	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
9	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson2025detection}) to test whether score \emph{calibration} may matter as much as raw discrimination for reweighting.
10	
11	\paragraph{Training.}
12	We continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\,=\,$5{\times}10^{-5}$), max sequence length 2048, and bf16 precision.
13	All main comparisons use three random seeds (42, 123, 456).
14	
15	\paragraph{Evaluation.}
16	We report held-out perplexity (PPL) on a held-out subset of FineWeb (67.8K documents, $\sim$4M tokens) containing only human-authored text, via sliding-window evaluation (stride 1024).
17	All evaluations are post-hoc with a unified pipeline; training involves no inline evaluation.
18	
19	\paragraph{Methods.}
20	We compare five approaches:
21	\begin{itemize}[nosep,leftmargin=*]
22	  \item \textbf{Uniform}: $w_j = 1$ for all $j$ (no contamination handling).
23	  \item \textbf{Grid-$b$}: fixed $b \in \{0.3, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0\}$, best select
…[truncated 914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-18T06:20:50.495873+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-18T06:20:51.249632+00:00_

1	\subsection{Main Results}
2	\label{sec:main-results}
3	
4	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across three seeds.
5	Continued pretraining reduces PPL from 22.970 (pretrained checkpoint) to the 17.3--17.8 range; the initial 5.2-point drop absorbs the bulk of easy gains, and reweighting method comparisons operate within a narrow residual.
6	
7	Adaptive $\bstar$ is statistically indistinguishable from grid-best: 3-seed means 17.651 vs.\ 17.620 for grid $b{=}0.3$ (gap 0.031, bootstrap $p{=}0.30$).
8	The grid sweep requires nine complete training runs to identify the optimum~\citep{drayson2025detection}; the adaptive method requires one, with lower cross-seed variance ($\pm$0.007 vs.\ $\pm$0.033).
9	Using the mean of per-batch $\bstar$ ($\bar{b}^*{=}1.19$) as a fixed exponent yields PPL 17.693, comparable to uniform (17.694); per-batch adaptation is essential.
10	
11	The ablation hierarchy at $\rho{=}0.4$ (Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random, Table~\ref{tab:main}) reveals two requirements for effective reweighting: detector signal and minimum intervention.
12	Random weights $\mathcal{U}(0,2)$ (mean 17.803) perform worse than uniform (17.694): the detector's $q$-scores carry genuine provenance information, and uninformed reweighting increases gradient variance without corrective signal.
13	ESS-only (mean $17.737 {\pm} 0.021$) uses $q$-scores but maximizes $b$ up to the stability ceiling, concentrating weights on a few high-confidence samples; it provides no improvement over uniform.
14	Only the dual-constrained adaptive method, which limits $b$ to the minimum needed, improves over uniform (paired gap $0.086$, $p{<}0.01$, $N{=}3$).
15	Figure~\ref{fig:grid_b_trend} contextualizes this: the grid curve has a broad plateau at $b \in [0.1, 0.5]$ (PPL 17.620--17.655), and adaptive $\bstar$ (mean 17.651) falls within it; ESS-only $\bstar$ (mean 3.5--5.9) lies in the degradation zone beyond the plateau.
16	
17	Golden Ratio~\citep{he202
…[truncated 6805 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-18T06:20:51.350616+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-18T06:20:51.802793+00:00_

1	\paragraph{Why minimum intervention works.}
2	The central finding is that restraint in downweighting outperforms aggressiveness.
3	ESS-only reweighting (PPL 17.737) performs worse than uniform (17.694), while the dual-constrained adaptive $\bstar$ achieves 17.651 by selecting the \emph{smallest} $b$ that meets the quality floor.
4	The binding statistics (\S\ref{sec:regime}) explain why: in the 38.2\% of batches where $\aeff$ determines $\bstar$, the selected exponent is 4.9$\times$ lower than the ESS-only upper bound, preventing unnecessary suppression of borderline samples ($q \approx 0.4$--$0.6$) that carry useful training signal.
5	This behavior is robust across contamination levels ($\aeff$-binding rate: 38.2\% at $\rho{=}0.4$, 33.4\% at $\rho{=}0.6$) and seeds (CV ${<}2\%$).
6	
7	\paragraph{Where the advantage manifests.}
8	The advantage appears entirely at evaluation (PPL 17.65 vs.\ 17.69 on human-authored text); unweighted training loss curves overlap (${\sim}1.4\%$ difference), consistent with reshaping the effective distribution without changing the optimization trajectory.
9	
10	\paragraph{Why not a fixed $b$?}
11	Training with the aggregate mean $\bstar \approx 1.4$ as a fixed exponent yields PPL 17.693, no better than uniform (17.694), because the average masks extreme per-batch heterogeneity (std $\approx$ 1.9, range $[0, 20]$): it over-penalizes the 55\% of batches needing mild correction ($\bstar < 1$) and under-penalizes the 3.6\% requiring aggressive intervention ($\bstar > 5$).
12	The grid-searched optimum ($b{=}0.3$ at $\rho{=}0.4$, $b{=}0.5$ at $\rho{=}0.6$) varies with contamination level, requiring per-setting retuning that the adaptive method eliminates.
13	
14	\paragraph{$\tau$ as a practical dial.}
15	$\tau \in [0.5, 0.8]$ all outperform uniform (Table~\ref{tab:tau}), with asymmetric sensitivity: under-cleaning is mild, while over-cleaning ($\tau > 0.8$) sharply degrades as $\bstar$ inflates.
16	This reinforces the minimum intervention int
…[truncated 762 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-18T06:20:51.803230+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-18T06:20:52.255316+00:00_

1	We introduced Minimum Intervention Reweighting, a dual-constraint framework that derives per-batch exponents $\bstar$ without validation data by finding the smallest $b$ satisfying $\aeff(b) \geq \tau$ subject to $\mathrm{ESS}(b) \geq \nmin$.
2	
3	At 0.6B scale with 40\% contamination, adaptive $\bstar$ is statistically indistinguishable from grid-best (3-seed means 17.651 vs.\ 17.620, $p{=}0.30$) while eliminating grid search entirely.
4	At $\rho{=}0.4$, the ablation Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random confirms that both detector signal and minimum intervention are necessary.
5	Hard filtering achieves lower absolute PPL (17.290) but requires threshold calibration that reweighting avoids.
6	At $\rho{=}0.6$, adaptive $\bstar$ remains significantly better than uniform (3-seed $\Delta{=}{-}0.028$, $p{<}0.01$); the ESS-only/uniform gap collapses at this level, isolating $\aeff$ as the key driver of the advantage.
7	A lightweight TF-IDF + LR detector (AUC\,=\,0.939, ECE\,=\,0.048) suffices throughout.
8	
9	Future work: scaling to 3B+ models, multi-detector comparison to test the calibration hypothesis, and evaluation on naturally contaminated corpora.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-18T06:20:52.305938+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-18T06:20:52.507152+00:00_

1	\paragraph{Scale and cross-model transfer.}
2	All main experiments use Qwen3-0.6B with batch size 4.
3	Cross-model transfer (Llama-3.2-3B, single seed): adaptive training achieves PPL and HellaSwag parity with uniform (within 0.5\,pp).
4	MMLU shows a $+$1.6\,pp advantage for adaptive, though this observation requires multi-seed replication.
5	Overall, the dual-constrained method transfers to a different architecture without degradation, but we cannot claim improvement from a single seed.
6	Batch-level statistics at larger batch sizes and scale-dependent threshold tuning remain important directions for future work.
7	
8	\paragraph{Contamination range.}
9	The method improves over uniform at $\rho \in \{0.4, 0.6\}$ but not at $\rho{=}0.2$ ($+$0.046 PPL, 0.26\% relative), indicating an effective range of $\rho \geq 0.4$ with $\tau{=}0.8$.
10	Behavior at $\rho > 0.8$ is untested; extreme contamination may violate the assumption that sufficient real samples exist per batch for meaningful $\aeff$ estimation.
11	Real web-scale contamination is domain-skewed, which may alter within-batch $\aeff$ distributions.
12	
13	\paragraph{Detector coverage.}
14	We evaluate one detector family (TF-IDF + logistic regression).
15	Whether score calibration matters as much as raw discrimination for reweighting remains a hypothesis; a systematic ablation across detector architectures and quality levels is needed to test it.
16	
17	\paragraph{Threshold.}
18	$\tau$ is an empirical hyperparameter.
19	The convergence theory of \citet{wang2026survive} assumes a known contamination proportion $\alpha$, which we do not require; bridging this gap to derive $\tau$ from first principles remains open.
20	
21	\paragraph{Evaluation.}
22	Main results report held-out perplexity.
23	Downstream benchmarks (Appendix~\ref{app:downstream}) show no significant difference between adaptive and uniform at 0.6B; systematic downstream evaluation across seeds and larger scales would strengthen the practical case.
24
…[truncated 415 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-18T06:20:52.507525+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-18T06:20:52.558637+00:00_

1	\section{Proofs}
2	\label{app:proofs}
3	
4	\begin{proof}[Proof of Proposition~\ref{prop:monotone}]
5	Let $w_i(b) = (1 - q_i)^b$, $W(b) = \sum_{j=1}^B w_j(b)$, and $\pi_i(b) = w_i(b) / W(b)$.
6	Then
7	\begin{equation*}
8	  \alpha_{\mathrm{eff}}(b) = \sum_{i=1}^{B} \pi_i(b)\, r_i,
9	\end{equation*}
10	where $r_i \in \{0, 1\}$ indicates whether sample $i$ is real.
11	Taking the derivative with respect to $b$:
12	\begin{align*}
13	  \frac{d\pi_i}{db}
14	  &= \pi_i \!\left(\frac{d \ln w_i}{db} - \frac{d \ln W}{db}\right)
15	  = \pi_i \!\left(\ln(1{-}q_i) - \sum_j \pi_j \ln(1{-}q_j)\right).
16	\end{align*}
17	Substituting,
18	\begin{align*}
19	  \frac{d\alpha_{\mathrm{eff}}}{db}
20	  &= \sum_i r_i\, \pi_i \!\left(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\right) \\
21	  &= \mathrm{Cov}_{\pi}\!\bigl(r_i,\, \ln(1{-}q_i)\bigr).
22	\end{align*}
23	For any detector with better-than-random discrimination, real samples ($r_i = 1$) have $q_i \leq 0.5$ on average, and thus higher $\ln(1{-}q_i)$ than synthetic samples.
24	The weighted covariance $\mathrm{Cov}_{\pi}(r_i, \ln(1{-}q_i))$ is therefore non-negative, establishing that $\alpha_{\mathrm{eff}}(b)$ is non-decreasing in $b$.
25	\end{proof}
26	
27	\section{Grid Search Details}
28	\label{app:grid}
29	
30	Table~\ref{tab:grid_full} reports held-out PPL for all grid-$b$ values at $\rho = 0.4$ (seed\,42).
31	
32	\begin{table}[h]
33	\centering
34	\small
35	\begin{tabular}{@{}cc@{}}
36	\toprule
37	$b$ & PPL $\downarrow$ \\
38	\midrule
39	0.1 & 17.657 \\
40	0.2 & 17.640 \\
41	0.3 & \textbf{17.640} \\
42	0.5 & 17.651 \\
43	1.0 & 17.692 \\
44	1.5 & 17.718 \\
45	2.0 & 17.741 \\
46	3.0 & 17.774 \\
47	5.0 & 17.818 \\
48	\bottomrule
49	\end{tabular}
50	\caption{Full grid search results ($\rho{=}0.4$, seed\,42).
51	$b \in [0.1, 0.5]$ forms a broad plateau (three-seed mean for $b{=}0.1$: $17.655 \pm 0.009$); $b{=}0.3$ is the post-hoc best.}
52	\label{tab:grid_full}
53	\end{table}
54	
55	\section{Quality Threshold Sweep}
56	\label{app:tau_s
…[truncated 5469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-18T06:21:09.516580+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-18T06:21:09.622502+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 105
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-18T06:21:13.587079+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-18T06:21:14.347654+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 760
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-18T06:21:14.398260+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/references.bib",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/references.bib",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-18T06:21:14.448962+00:00_

1	% References for Minimum Intervention Reweighting paper
2	% Note: entries to be verified via verify_references before final submission
3	
4	@article{drayson2025detection,
5	  title={Machine-Generated Text Detection Prevents Language Model Collapse},
6	  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
7	  journal={arXiv preprint arXiv:2502.15654},
8	  year={2025}
9	}
10	
11	@article{he2025golden,
12	  title={Golden Ratio Weighting Prevents Model Collapse},
13	  author={He, Hengzhi and Xu, Shirong and Cheng, Guang},
14	  journal={arXiv preprint arXiv:2502.18049},
15	  year={2025}
16	}
17	
18	@article{wang2026survive,
19	  title={Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training},
20	  author={Wang, Kevin and Niu, Hongqian and Li, Didong},
21	  journal={arXiv preprint arXiv:2602.16065},
22	  year={2026}
23	}
24	
25	@article{shumailov2024model,
26	  title={{AI} Models Collapse When Trained on Recursively Generated Data},
27	  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
28	  journal={Nature},
29	  volume={631},
30	  pages={755--759},
31	  year={2024}
32	}
33	
34	@inproceedings{dohmatob2025strong,
35	  title={Strong Model Collapse},
36	  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
37	  booktitle={ICLR},
38	  year={2025}
39	}
40	
41	@article{vehtari2024psis,
42	  title={Pareto Smoothed Importance Sampling},
43	  author={Vehtari, Aki and Simpson, Daniel and Gelman, Andrew and Yao, Yuling and Gabry, Jonah},
44	  journal={JMLR},
45	  year={2024}
46	}
47	
48	@inproceedings{sow2025dynamic,
49	  title={Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining},
50	  author={Sow, Daouda and Woisetschl{\"a}ger, Herbert and Bulusu, Saikiran and Wang, Shiqiang and Jacobsen, Hans-Arno and Liang, Yingbin},
51	  booktitle={ICLR},
52	  year={2025}
53	
…[truncated 4590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-18T06:21:19.671020+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-18T06:21:19.771966+00:00_

1	- id: "RR-W1"
2	  summary: "Paper claims 'from random initialization' but code uses from_pretrained() — actually continued pretraining"
3	  category: writing
4	  severity: warning
5	  status: in_progress
6	  first_raised_round: 1
7	  last_seen_round: 1
8	  mentions:
9	    - round: 1
10	      reviewers: [research_reviewer]
11	      note: "Two independent reviews confirmed: pretrain_weighted.py L318 uses from_pretrained(), model.safetensors 1.5GB = full pretrained weights"
12	  action_items:
13	    - round: 1
14	      action: "Fix paper text: 'pretrain from random initialization' → 'continue pretraining Qwen3-0.6B'"
15	      assigned_to: paper_agent
16	      status: pending
17	    - round: 1
18	      action: "Run baseline PPL eval on untrained Qwen3-0.6B checkpoint to quantify absolute improvement"
19	      assigned_to: main_agent
20	      status: in_progress
21	  resolution: ""
22	  resolution_round: null
23	
24	- id: "RR-W2"
25	  summary: "Paper claims 'balanced real/synthetic test set' but eval_holdout.jsonl is human-only (FineWeb)"
26	  category: writing
27	  severity: warning
28	  status: in_progress
29	  first_raised_round: 1
30	  last_seen_round: 1
31	  mentions:
32	    - round: 1
33	      reviewers: [research_reviewer]
34	      note: "eval_holdout.jsonl: 67823 lines, all source=fineweb depth=0, zero synthetic samples"
35	  action_items:
36	    - round: 1
37	      action: "Fix paper text: 'balanced real/synthetic test set' → 'human-only test set drawn from FineWeb'"
38	      assigned_to: paper_agent
39	      status: pending
40	  resolution: ""
41	  resolution_round: null

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-18T06:21:24.593048+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "output_mode": "content",
  "-C": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
    "output_mode": "content",
    "-C": "3"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-18T06:21:26.600451+00:00_

&lt;persisted-output>
Output too large (19.7KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training--claude-sessions-review-director-5d592d28/40449f67-4b2e-4c00-8fab-6c1fdd1e97a2/tool-results/toolu_019hqnu2hKeZa2zw73X6WjRn.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/logs/review_best.log-10-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/logs/review_best.log-11-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/logs/review_best.log-12-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/logs/review_best.log:13:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/logs/review_best.log-14-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/logs/review_best.log-15-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/logs/review_best.log-16-[Omitted long context line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_director_5d592d28/AGENTS.md-79-
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_director_5d592d28/AGENTS.md-80-## 外部审稿线（Stanford Agentic Reviewer）
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/project
…[truncated 258 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "elapsed_ms": 2007
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-18T06:21:29.060543+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai\"",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "glob": "config.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai\"",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
    "glob": "config.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-18T06:21:29.111155+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-18T06:21:31.025002+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-18T06:21:31.075556+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-18T06:21:32.884133+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-18T06:21:32.936020+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-18T06:21:35.194766+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/agent"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-18T06:21:35.248018+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_director_5d592d28.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-18T06:21:38.011023+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "paperreview_ai|external_review\"",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10",
  "glob": "*.yaml",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "paperreview_ai|external_review\"",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10",
    "glob": "*.yaml",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-18T06:21:38.078974+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "elapsed_ms": 67
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-18T06:22:23.730037+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**目标 Venue**: EMNLP 2026（通过 ACL Rolling Review 提交）\n**截止日期**: 2026-05-25 (ARR May cycle)\n**格式要求**: ACL 模板 `[review]`，长文 ≤8 页正文 + unlimited references，Limitations section 不计页数，double-blind\n**论文路径**: `projects/provenance_weight_training/paper/main.tex`（sections/ 子目录含各章节）\n\n### 你的审查侧重：方法严谨性 + 实验设计\n\n请从以下维度深入审查：\n\n1. **方法正确性**\n   - 双约束框架（α_eff ≥ τ, ESS ≥ n_min）的数学推导是否严谨\n   - Proposition 1 (monotonicity) 的证明是否完整/正确\n   - \"minimum intervention principle\" 的形式化是否站得住脚\n   - bisection 算法的正确性和收敛保证\n\n2. **实验设计**\n   - Baseline 选择是否充分公平（Uniform / Grid-b / ESS-only / Random / Golden Ratio / Detect & Remove）\n   - 自污染设计（用 Qwen3-0.6B 生成 synthetic → 同架构训练）的合理性和局限\n   - 评估指标（仅 held-out PPL + 附录 downstream）是否充分\n   - 单一模型（0.6B）、单一数据源（FineWeb）、单一 detector（TF-IDF+LR）的外部效度\n\n3. **统计检验**\n   - 3-seed 比较的统计功效是否足够（特别是 p=0.30 \"indistinguishable\" 这一 claim）\n   - bootstrap p-value 的使用是否恰当\n   - effect size（~0.04 PPL）是否足以支撑论文 claims\n\n4. **消融完整性**\n   - τ sweep、n_min sweep、batch size sweep 是否覆盖关键范围\n   - ρ=0.2 失效、ρ>0.6 未测试的 implications\n   - 缺失的消融（如不同 detector 的影响、不同数据规模）\n\n5. **历史 Issue 检查**\n   - RR-W1: 此前论文错误声称 \"from random initialization\"，应为 \"continued pretraining\"——检查是否已修正\n   - RR-W2: 此前论文错误声称 \"balanced real/synthetic test set\"，实际为 human-only——检查是否已修正\n\n请输出完整结构化审稿报告：Summary → Strengths → Weaknesses（逐条编号，标 [Must-Fix] / [Should-Fix] / [Minor]）→ Questions → Missing References → Score (1-5) + Confidence (1-5)。",
  "reviewer_id": "1",
  "project": "provenance_weight_training",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**目标 Venue**: EMNLP 2026（通过 ACL Rolling Review 提交）\n**截止日期**: 2026-05-25 (ARR May cycle)\n**格式要求**: ACL 模板 `[review]`，长文 ≤8 页正文 + unlimited references，Limitations section 不计页数，double-blind\n**论文路径**: `projects/provenance_weight_training/paper/main.tex`（sections/ 子目录含各章节）\n\n### 你的审查侧重：方法严谨性 + 实验设计\n\n请从以下维度深入审查：\n\n1. **方法正确性**\n   - 双约束框架（α_eff ≥ τ, ESS ≥ n_min）的数学推导是否严谨\n   - Proposition 1 (monotonicity) 的证明是否完整/正确\n   - \"minimum intervention principle\" 的形式化是否站得住脚\n   - bisection 算法的正确性和收敛保证\n\n2. **实验设计**\n   - Baseline 选择是否充分公平（Uniform / Grid-b / ESS-only / Random / Golden Ratio / Detect & Remove）\n   - 自污染设计（用 Qwen3-0.6B 生成 synthetic → 同架构训练）的合理性和局限\n   - 评估指标（仅 held-out PPL + 附录 downstream）是否充分\n   - 单一模型（0.6B）、单一数据源（FineWeb）、单一 detector（TF-IDF+LR）的外部效度\n\n3. **统计检验**\n   - 3-seed 比较的统计功效是否足够（特别是 p=0.30 \"indistinguishable\" 这一 claim）\n   - bootstrap p-value 的使用是否恰当\n   - effect size（~0.04 PPL）是否足以支撑论文 claims\n\n4. **消融完整性**\n   - τ sweep、n_min sweep、batch size sweep 是否覆盖关键范围\n   - ρ=0.2 失效、ρ>0.6 未测试的 implications\n   - 缺失的消融（如不同 detector 的影响、不同数据规模）\n\n5. **历史 Issue 检查**\n   - RR-W1: 此前论文错误声称 \"from random initialization\"，应为 \"continued pretraining\"——检查是否已修正\n   - RR-W2: 此前论文错误声称 \"balanced real/synthetic test set\"，实际为 human-only——检查是否已修正\n\n请输出完整结构化审稿报告：Summary → Strengths → Weaknesses（逐条编号，标 [Must-Fix] / [Should-Fix] / [Minor]）→ Questions → Missing References → Score (1-5) + Confidence (1-5)。",
    "reviewer_id": "1",
    "project": "provenance_weight_training",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-18T06:22:39.485652+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15755
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-18T06:22:39.988976+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**目标 Venue**: EMNLP 2026（通过 ACL Rolling Review 提交）\n**截止日期**: 2026-05-25 (ARR May cycle)\n**格式要求**: ACL 模板 `[review]`，长文 ≤8 页正文 + unlimited references，Limitations section 不计页数，double-blind\n**论文路径**: `projects/provenance_weight_training/paper/main.tex`（sections/ 子目录含各章节）\n\n### 你的审查侧重：新颖性 + 完整性 + 写作质量\n\n请从以下维度深入审查：\n\n1. **新颖性与贡献增量**\n   - 相对于 Drayson et al. (2025) 的 detect-and-reweight 框架，本文的真实增量在哪里？是否足够撑起 EMNLP 长文？\n   - \"minimum intervention principle\" 是否只是一个简单的超参搜索替代方案，还是有更深的 insight？\n   - dual constraint 这一 formulation 在 importance weighting 文献中是否有类似前例？\n\n2. **Related Work 完整性**\n   - 是否遗漏重要的相关工作？特别关注：\n     - 其他 contamination-aware training 方法\n     - importance weighting / curriculum learning 文献\n     - 其他 model collapse prevention 方法\n   - 引用密度是否达到 EMNLP 长文水平？\n   - positioning 是否准确？\n\n3. **叙事连贯性**\n   - Abstract → Intro → Method → Results → Discussion → Conclusion 是否形成一条连贯主线？\n   - 是否存在 framing 不一致（例如 Introduction 讲的故事与 Results 的故事不匹配）？\n   - claims 是否与 evidence 匹配（特别是 \"indistinguishable from grid-best\" 这个 claim）\n\n4. **写作质量（AI 痕迹检查）**\n   - 检查 em-dash (—) 和解释性 en-dash (–) 的使用\n   - 检查 -ing 分词短语结尾\n   - 检查过度分段、过渡词堆砌\n   - 检查用词黑名单（delve, leverage, utilize, facilitate, novel 过度使用等）\n   - 整体语言是否像人类学术写作\n\n5. **格式合规**\n   - 正文是否 ≤8 页？\n   - Limitations section 是否存在且实质性？\n   - 匿名是否完整（无作者信息泄露）？\n   - 引用格式是否一致？\n   - 图表 caption 是否 self-contained？\n\n6. **历史 Issue 检查**\n   - RR-W1: 此前论文错误声称 \"from random initialization\"，应为 \"continued pretraining\"——检查是否已修正\n   - RR-W2: 此前论文错误声称 \"balanced real/synthetic test set\"，实际为 human-only——检查是否已修正\n\n请输出完整结构化审稿报告：Summary → Strengths → Weaknesses（逐条编号，标 [Must-Fix] / [Should-Fix] / [Minor]）→ Questions → Missing References → Score (1-5) + Confidence (1-5)。",
  "reviewer_id": "2",
  "project": "provenance_weight_training",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**目标 Venue**: EMNLP 2026（通过 ACL Rolling Review 提交）\n**截止日期**: 2026-05-25 (ARR May cycle)\n**格式要求**: ACL 模板 `[review]`，长文 ≤8 页正文 + unlimited references，Limitations section 不计页数，double-blind\n**论文路径**: `projects/provenance_weight_training/paper/main.tex`（sections/ 子目录含各章节）\n\n### 你的审查侧重：新颖性 + 完整性 + 写作质量\n\n请从以下维度深入审查：\n\n1. **新颖性与贡献增量**\n   - 相对于 Drayson et al. (2025) 的 detect-and-reweight 框架，本文的真实增量在哪里？是否足够撑起 EMNLP 长文？\n   - \"minimum intervention principle\" 是否只是一个简单的超参搜索替代方案，还是有更深的 insight？\n   - dual constraint 这一 formulation 在 importance weighting 文献中是否有类似前例？\n\n2. **Related Work 完整性**\n   - 是否遗漏重要的相关工作？特别关注：\n     - 其他 contamination-aware training 方法\n     - importance weighting / curriculum learning 文献\n     - 其他 model collapse prevention 方法\n   - 引用密度是否达到 EMNLP 长文水平？\n   - positioning 是否准确？\n\n3. **叙事连贯性**\n   - Abstract → Intro → Method → Results → Discussion → Conclusion 是否形成一条连贯主线？\n   - 是否存在 framing 不一致（例如 Introduction 讲的故事与 Results 的故事不匹配）？\n   - claims 是否与 evidence 匹配（特别是 \"indistinguishable from grid-best\" 这个 claim）\n\n4. **写作质量（AI 痕迹检查）**\n   - 检查 em-dash (—) 和解释性 en-dash (–) 的使用\n   - 检查 -ing 分词短语结尾\n   - 检查过度分段、过渡词堆砌\n   - 检查用词黑名单（delve, leverage, utilize, facilitate, novel 过度使用等）\n   - 整体语言是否像人类学术写作\n\n5. **格式合规**\n   - 正文是否 ≤8 页？\n   - Limitations section 是否存在且实质性？\n   - 匿名是否完整（无作者信息泄露）？\n   - 引用格式是否一致？\n   - 图表 caption 是否 self-contained？\n\n6. **历史 Issue 检查**\n   - RR-W1: 此前论文错误声称 \"from random initialization\"，应为 \"continued pretraining\"——检查是否已修正\n   - RR-W2: 此前论文错误声称 \"balanced real/synthetic test set\"，实际为 human-only——检查是否已修正\n\n请输出完整结构化审稿报告：Summary → Strengths → Weaknesses（逐条编号，标 [Must-Fix] / [Should-Fix] / [Minor]）→ Questions → Missing References → Score (1-5) + Confidence (1-5)。",
    "reviewer_id": "2",
    "project": "provenance_weight_training",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-18T06:22:42.068974+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 2079
}
```

</details>

---


### Assistant

_source line 70 · 2026-05-18T06:22:47.054705+00:00_

Round 1 任务已分配给两位 Reviewer，等待审稿结果返回。

- **R1**（方法严谨性 + 实验设计）— 已触发
- **R2**（新颖性 + 完整性 + 写作质量）— 已触发

两位 Reviewer 将独立审查论文后返回结构化审稿报告。收到后进入 Step 2（交叉分享 + 逐条回应）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 2

## Round 2

2 recorded events


### User

_source line 71 · 2026-05-18T06:27:37.849537+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿报告

**论文**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining
**审查侧重**: 方法严谨性 + 实验设计
**评分标准**: ACL Rolling Review (ARR) 官方 review form

---

## 总体评分

**Overall**: 3.0 / 5 (Findings)
**Confidence**: 4 / 5
**一句话总结**: 方法直觉清晰、框架简洁，但核心 claim 的统计支撑存在方法论缺陷（用 failure-to-reject 代替 equivalence test），实验规模和 detector 覆盖不足以支撑论文的一般性主张。

---

## ARR 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2.5 / 5 | Proposition 1 证明存在 gap（$r_i$ 是估计量非 ground truth，与理论动机脱节）；"indistinguishable" claim 的统计方法不当（§详见 N1）；effect size 极小（0.24%）且 downstream 无显著差异 |
| Excitement | 3.0 / 5 | 问题重要且实际（web 数据污染加剧），minimum intervention 直觉好，但实验未能在下游任务或更大规模上展示实际价值 |
| Reproducibility | 4 / 5 | 算法伪代码清晰、超参设置完整、3-seed 报告；但代码未提供 |
| Datasets | 1 / 5 | 无新数据集 |
| Software | 1 / 5 | 无代码发布 |

---

## Summary

本文提出一种双约束自适应指数选择框架用于 detect-and-reweight 预训练：给定 per-sample 检测器分数 $q(x)$，对每个 batch 求解满足 $\alpha_{\mathrm{eff}}(b) \geq \tau$（质量下界）且 $\mathrm{ESS}(b) \geq n_{\min}$（稳定性上界）的最小 $b$，称为 "minimum intervention principle"。在 Qwen3-0.6B continued pretraining（132M tokens FineWeb，40% 合成污染）上，方法与 grid-searched best 统计不可区分（PPL 17.651 vs 17.620，$p=0.30$），消融证实 detector 信号和 minimum intervention 都是必要的。

## Strengths

**S1.** 问题定义清晰且实际。Web 数据中合成内容比例持续增长，需要无需验证集和已知污染比例的自适应方法。论文清楚地将此问题形式化为受约束优化。

**S2.** 双约束框架设计简洁。$\alpha_{\mathrm{eff}}$ 和 ESS 的对立单调性自然地定义了 feasible region，bisection 求解高效（$\sim$44 FLOPs per batch）。"最小干预"直觉合理：borderline samples 仍有训练价值，过度下权适得其反。

**S3.** 消融设计有层次。Random → ESS-only → Uniform → Adaptive 的四级层次有效分离了 detector 信号和 minimum intervention 两个因素。固定 $\bar{b}^*$ 实验（PPL 17.693 ≈ uniform）进一步证明 per-batch adaptation 的必要性。

**S4.** 超参敏感性分析全面。$\tau$ sweep（0.50–0.95）、$n_{\min}$ sweep、batch size sweep ($B \in \{4,8,16\}$) 均有覆盖，$\tau \in [0.5, 0.8]$ 的宽 safe range 是实用性的重要证据。

**S5.** Related Work 定位准确。与 Drayson et al. (2025) 的三点差异（per-model grid search → per-batch adaptive, SIR resampling → loss reweighting, strong detector → lightweight detector）表述清楚，positioning 不过度。

**S6.** 历史问题已修正。此前版本错误声称 "from random initialization"（现为 "continued pretraining from pretrained weights"，Section 4）和 "balanced real/synthetic test set"（现为 "containing only human-authored text"，Section 4）。两个问题均已正确修正。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **"Statistically indistinguishable" claim 使用了错误的统计范式**
- 具体位置：Abstract, Section 5.1, Section 6 (Conclusion)
- 问题：论文核心 claim 是 adaptive $b^*$ "statistically indistinguishable from grid-searched optimum"，依据是 bootstrap $p = 0.30$。但 $p = 0.30$ 仅表示 **未能拒绝**差异为零的零假设，不等于证明等价。在 N=3（3 seeds）的极小样本下，统计功效（power）极低——即使真实差异为 0.5 PPL，也很可能得到 $p > 0.05$。要正式声称"不可区分"，需要 equivalence test（如 TOST, Two One-Sided Tests），预设实际等价边界 $\delta$，并证明差异落在 $[-\delta, +\delta]$ 内。当前表述将 absence of evidence 当作 evidence of absence，这是统计推断的基本错误。
- 为什么影响接收：这是论文第一贡献的核心支撑。如果 "indistinguishable" claim 不成立，论文的核心价值主张需要重新表述。
- 建议修改方向：(1) 执行 TOST 等价检验，明确 $\delta$（如 0.1 PPL）；(2) 若功效不足，将 claim 降级为 "adaptive $b^*$ achieves comparable PPL to grid-best, with the gap not reaching significance at N=3"；(3) 增加 seeds 数量至少到 5-10 以提高统计功效。

**N2** [critical] **$\alpha_{\mathrm{eff}}$ 的理论动机与实际计算之间存在逻辑断层**
- 具体位置：Section 3.2 (Eq. 2), Proposition 1 proof (Appendix A)
- 问题：$\alpha_{\mathrm{eff}}$ 使用 $r_i = \mathbf{1}[q_i \leq 0.5]$ 作为样本是否为真实数据的 indicator。但理论动机来自 Wang et al. (2026)，其收敛速率定理基于 **真实的** real-data fraction $\alpha$，不是检测器估计的 $\hat{\alpha}$。这个 gap 意味着：当检测器不完美时（AUC = 0.939，46.3% 样本在不确定区间 $[0.2, 0.8]$），$\alpha_{\mathrm{eff}}$ 可能系统性偏离真实 $\alpha$，$\tau$ 的保证不再成立。Proposition 1 的证明也依赖 $r_i$ 与 $\ln(1-q_i)$ 的正协方差，但 $r_i$ 本身就是 $q_i$ 的阈值函数——两者不是独立信号，covariance 的正性是 tautological（高 $q$ 导致 $r_i = 0$，低 $q$ 导致 $r_i = 1$ 且高 $\ln(1-q_i)$）。这意味着 $\alpha_{\mathrm{eff}}$ 增加并非因为"权重转移到真实样本"，而仅仅因为"权重转移到检测器认为是真实的样本"。
- 为什么影响接收：Proposition 1 是方法框架的数学基础。如果 $\alpha_{\mathrm{eff}}$ 不是 true $\alpha$ 的良好代理，quality constraint 的理论根基不稳。
- 建议修改方向：(1) 明确讨论 $\alpha_{\mathrm{eff}}$ 是 estimated effective real proportion，不是 true real proportion；(2) 在已知 ground truth 的合成实验中，报告 $\alpha_{\mathrm{eff}}$ vs true $\alpha$ 的 correlation；(3) 分析检测器精度如何影响 $\alpha_{\mathrm{eff}}$ 的保证。

**N3** [critical] **实验外部效度严重不足**
- 具体位置：Section 4 (Experimental Setup), Section 8 (Limitations)
- 问题：全部主实验在单一设定下完成：
  - **单一模型规模**：0.6B。Limitations 提到 Llama-3.2-3B 迁移实验（单 seed）显示 PPL 和 HellaSwag 与 uniform 持平，MMLU +1.6pp 但需要 multi-seed。这不构成 scaling 证据。
  - **单一数据源**：FineWeb。真实 web 数据的领域分布、噪声模式可能截然不同。
  - **单一 detector**：TF-IDF + LR。论文声称 "score calibration may matter as much as raw classification accuracy"（Abstract, Section 4），但未用任何其他检测器验证。这个 claim 完全无实验支撑。
  - **自污染设计**：用 Qwen3-0.6B 生成合成数据，再用同架构训练。真实场景中生成器通常是更大/不同模型（GPT-4, Claude 等），检测难度和分布特征完全不同。
  - **$\rho = 0.2$ 失效**：Limitations 报告 $\rho = 0.2$ 方法反而伤害 PPL（+0.046），但无深入分析。$\rho > 0.6$ 未测试。
- 为什么影响接收：论文 framing 为 general-purpose contamination-aware pretraining method，但实验证据只覆盖一个极窄的 setting。EMNLP/ARR 审稿人会要求至少 2 个模型规模 + 2 个 detector 的交叉验证。
- 建议修改方向：(1) 至少增加一个 neural detector（如 ModernBERT）的对比实验，直接验证 calibration hypothesis；(2) 增加至少一个 1B+ 规模的 3-seed 实验；(3) 分析 $\rho = 0.2$ 失效的原因（可能是 $\tau = 0.8$ 在低污染时已是 over-constraint）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Downstream benchmarks 未能展示实际价值**
- 具体位置：Appendix E (Table 8)
- 问题：5 个 downstream benchmarks（ARC-Challenge, ARC-Easy, HellaSwag, PIQA, WinoGrande）全部在标准误差内，且 4/5 个 adaptive 略微 **低于** uniform。论文说 "preserves downstream performance"，但审稿人会问：如果 PPL 改善不能转化为任何可测量的下游改善，这个方法的实际价值是什么？
- 建议：(1) 增加更多种类的 benchmarks（如 MMLU, GSM8K），尤其是对数据质量敏感的任务；(2) 在更大模型上验证 PPL 改善是否放大为下游差异；(3) 至少用多 seed 做下游评估。

**W2** [warning] **Proposition 1 声称 strictly increasing 但证明只建立 non-decreasing**
- 具体位置：Section 3.2, Proposition 1 statement vs proof
- 问题：命题声称 "$\alpha_{\mathrm{eff}}(b)$ is strictly increasing in $b$"。证明得到 $d\alpha_{\mathrm{eff}}/db = \mathrm{Cov}_\pi(r_i, \ln(1-q_i))$，然后说 "this covariance is non-negative"。Non-negative 只能推出 non-decreasing，不是 strictly increasing。命题前提 "containing both real and synthetic samples with distinct $q$-values" 旨在排除退化情况，但证明中没有严格论证在此前提下 covariance 严格为正。需要论证 $r_i$ 和 $\ln(1-q_i)$ 不是 $\pi$-a.s. 常数。
- 建议：严格化证明，或将命题降级为 non-decreasing，并注明在 non-degenerate 条件下严格成立。

**W3** [warning] **ESS monotonicity 未证明**
- 具体位置：Section 3.2, line 57
- 问题："$\mathrm{ESS}(b)$ is monotonically decreasing in $b$: larger exponents concentrate the weight distribution, a standard property of exponential tilting (Kimura et al., 2024)."。但 Kimura et al. (2024) 是一篇 importance weighting 综述，不一定包含这个具体结论。ESS 的 monotonicity 对 bisection 算法的正确性至关重要——如果 ESS 非单调，$b_{\mathrm{ESS}}$ 可能不唯一，bisection 会失败。这个性质应该被正式证明或给出精确引用。
- 建议：在 Appendix 中加入 ESS 单调性的简短证明，至少对 $(1-q)^b$ 形式的 weights。

**W4** [warning] **Grid-$b$ baseline 存在 post-hoc oracle 问题但论文未充分讨论**
- 具体位置：Section 4 (Methods), Table 1 caption
- 问题：Grid-$b$ 的 best 是 post-hoc 在测试集上选择的（"best selected post-hoc by held-out PPL"），这给了 grid search 一个 oracle 优势。论文确实在 Table 1 caption 中标注了 $^\ddagger$Post-hoc oracle，但核心 claim "indistinguishable from grid-searched optimum" 是拿 adaptive 和 post-hoc oracle 比。在实践中，grid search 需要一个独立的 validation set 来选择 $b$，选出的 $b$ 在 test set 上通常略差于 post-hoc best。因此，adaptive 方法在公平比较中可能实际上优于真正的 grid search（用 val set 选 $b$，在 test set 上评估）。
- 建议：增加一个 split-validation grid search baseline（用 val set 选 $b$，用 test set 评估），以提供更公平的比较。

**W5** [warning] **Detect & Remove 和 Golden Ratio 仅单 seed**
- 具体位置：Table 1
- 问题：两个重要 baseline 只报告了 seed 42 的结果。Detect & Remove（17.290）显著优于所有 reweighting 方法，但没有多 seed 验证。在论文的核心叙事中，Detect & Remove 的优势被归因于 "distribution match"，但如果这个结果在多 seed 下不稳定，论文的 framing 需要调整。
- 建议：至少用 3 seeds 复现 Detect & Remove 和 Golden Ratio。

**W6** [warning] **效应量在实际意义上是否足够大？**
- 具体位置：Section 5.4, Limitations (Effect size)
- 问题：主要改善 0.043 PPL（0.24% relative）。论文自己也承认 "modest in absolute terms"。在 0.6B 模型上，这个改善完全不可能在任何下游任务上被观测到（Appendix E 已证实）。论文的实际贡献缩小为：消除 grid search，同时不伤害性能。但这个 framing 与论文标题和 Abstract 的主张（"contamination-aware pretraining"）有 mismatch——读者预期一个能显著改善训练质量的方法，而不仅仅是一个省去 grid search 的方法。
- 建议：调整 framing，将核心卖点从 "improved pretraining" 转为 "matching grid-search at zero validation cost"。这更诚实，且仍有实际价值。

---

## Questions for Authors

**Q1.** $\alpha_{\mathrm{eff}}$ 使用阈值 $q_i \leq 0.5$ 判断真实/合成（Section 3.2, Eq. 2），这与 hard filtering 的 $q > 0.5$ 阈值相同。如果将 $r_i$ 改为 soft indicator $r_i = 1 - q_i$，性能如何变化？这会消除 0.5 阈值的硬依赖。

**Q2.** $\rho = 0.2$ 时方法反而伤害 PPL（+0.046，Limitations），但 $\tau = 0.8$ 在低污染下可能要求过高的 $b$。是否测试过 $\tau = 0.5$ 或 $\tau = 0.6$ 在 $\rho = 0.2$ 时的表现？

**Q3.** Section 5.4 提到 "unweighted training loss curves overlap (~1.4% difference)"。如果训练 loss 几乎不变，PPL 改善从何而来？是否因为 evaluation set 是 human-only 而 training 的 reweighting 恰好对 human-like 分布做了隐式 importance weighting？如果 evaluation set 包含合成样本，PPL 差异是否消失？

**Q4.** 论文使用 micro-batch size $B = 4$（Section 4），这意味着 ESS 的取值范围是 $[1, 4]$，$n_{\min} = 2$ 将 ESS 下界设在总样本的 50%。在如此小的 batch 上，$\alpha_{\mathrm{eff}}$ 和 ESS 的估计方差必然很大。是否分析过 per-batch $b^*$ 的噪声对训练稳定性的影响？

**Q5.** 论文声称 "score calibration may matter as much as raw classification accuracy"（Abstract），但只使用了一个 detector。要支撑这个 claim，至少需要一个 high-AUC 但 poorly-calibrated detector 和一个 lower-AUC 但 well-calibrated detector 的对比。是否有计划做这个实验？

---

## Missing References / 引用问题

1. **`guo2025escaping`**（Guo et al., 2025）在线验证未找到匹配。bib 条目缺少 arXiv ID，venue 仅写 "arXiv preprint"，无法确认真实性。需要补充完整信息或确认这篇论文确实存在。

2. **`vehtari2024psis`** 年份不一致：bib 写 2024，但 PSIS 原始版本为 2015（arXiv:1507.02646），JMLR 正式发表版可能为 2024。建议核实并使用正式发表年份。

3. **Temperature scaling** 用于检测器校准（Section 4, "calibrated ECE = 0.048 after temperature scaling with $T = 0.204$"），但未引用 Guo et al. (2017) "On Calibration of Modern Neural Networks" 等温度校准的基础文献。

4. **缺少 data contamination 检测的近期重要工作**：如 Hans et al. (2024) "Spotting LLMs with Binoculars" 等基于 likelihood ratio 的检测方法，可作为 detector 替代方案讨论。

5. **缺少 equivalence testing / TOST 方法引用**：如果论文要声称 "indistinguishable"，应引用统计等价性检验文献（Schuirmann 1987, Lakens 2017）。

---

## Score Summary

| 维度 | 分数 |
|------|------|
| **Soundness** | 2.5 / 5 |
| **Excitement** | 3.0 / 5 |
| **Overall** | 3.0 / 5 (Findings) |
| **Confidence** | 4 / 5 |
| **Reproducibility** | 4 / 5 |

---

## 审稿人总结

本文提出了一个简洁、直觉合理的框架，用于在无需验证集的条件下选择 detect-and-reweight 预训练的下权指数。方法设计思路清晰，消融结构合理。但三个 critical 问题制约了当前版本的接收：(1) "indistinguishable" 的核心 claim 基于错误的统计推断范式，(2) $\alpha_{\mathrm{eff}}$ 的理论动机与实际计算之间存在未讨论的逻辑 gap，(3) 实验仅覆盖单一模型/detector/数据源，外部效度不足以支撑 general-purpose method 的定位。建议将 (1) 的 claim 降级、(2) 加入讨论、(3) 至少增加一个 detector 和一个更大模型的多 seed 实验后重新提交。如果仅修正 (1)(2) 的表述但不扩展实验，可考虑 Findings 接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 72 · 2026-05-18T06:27:58.661162+00:00_

Reviewer 1 报告已收到。评分 3.0/5 (Findings)，3 个 critical issues（统计范式错误、α_eff 理论 gap、外部效度不足）。

等待 Reviewer 2 报告中。收到后将进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 3

## Round 3

2 recorded events


### User

_source line 73 · 2026-05-18T06:28:01.425201+00:00_

[Reviewer 1 审稿结果]:
Round 1 审稿报告已提交给 Review Director。

核心发现：
- **3 个 Must-Fix**："indistinguishable" claim 基于错误的统计范式（failure-to-reject ≠ equivalence）；$\alpha_{\mathrm{eff}}$ 理论动机与实际计算之间的逻辑断层；实验外部效度严重不足（单一模型/detector/数据源）
- **6 个 Should-Fix**：downstream 无改善、Proposition 1 证明 gap、ESS 单调性未证明、grid-$b$ 的 post-hoc oracle 问题、重要 baseline 仅单 seed、效应量过小与 framing 不匹配
- **Overall 3.0 / 5**（Findings 水平），Soundness 2.5，Excitement 3.0
- 历史问题 RR-W1 和 RR-W2 均已修正

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 74 · 2026-05-18T06:28:13.397185+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 报告后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 4

## Round 4

6 recorded events


### User

_source line 75 · 2026-05-18T06:30:37.712482+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告

**论文**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining

---

## 总体评分

**Overall**: 3.0/5 (Findings)
**一句话总结**: 方法 formulation 干净、ablation 诚实，但实验规模（仅 0.6B/132M tokens）和效果量（~0.04 PPL）不足以支撑 EMNLP 长文；hard filtering 以显著优势碾压所有 reweighting 方法，削弱了实际动机。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 数学推导正确，但实验仅 0.6B 单一规模、模拟污染、N=3 seeds；downstream 无改善；hard filtering 碾压 reweighting |
| Excitement | 2.5/5 | 问题重要且 minimum intervention 有直觉吸引力，但相对 Drayson et al. 增量有限；单一规模+模拟数据限制了影响力 |
| Reproducibility | 4/5 | 算法伪代码、超参数细节充分；未提供代码（匿名提交可理解） |
| Confidence | 4/5 | 熟悉 importance weighting 和 model collapse 文献，仔细检查了全文 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 实验规模不足以支撑长文贡献声明
- 具体位置：Section 4 (Experimental Setup), Section 5 (Results), Limitations
- 问题：全部主实验仅在 Qwen3-0.6B（单一模型规模）上进行，数据量 132M tokens。cross-model 实验（Llama-3.2-3B）仅 single seed，Limitations 自己承认"we cannot claim improvement from a single seed"。对于 EMNLP 长文，至少需要两个不同规模的模型 + 多 seed 复现。Drayson et al. (2025) 在 160M/360M/1.7B 三个规模上实验，本文声称改进了 Drayson 的方法却在实验覆盖上远不如它。
- 为什么影响接收：ARR reviewer guidelines 明确要求评估"sufficient support for all claims"——Introduction (line 23) 的 claim"adaptive reweighting is statistically indistinguishable from grid-searched optimum"仅在 0.6B 单规模上验证。
- 建议修改方向：至少补充一个 1-3B 规模的三 seed 实验，或降低 claim scope 到"0.6B continued pretraining"。

**N2** [critical] Hard filtering 碾压所有 reweighting 方法，削弱核心动机
- 具体位置：Section 5.1 (Table 1), Appendix F (Table 4)
- 问题：Detect & Remove（PPL 17.290）比 Adaptive（17.651）低 0.36 PPL，差距远大于 Adaptive vs. Uniform（0.043）。Appendix Table 4 显示即使 suboptimal threshold（$q > 0.3$: 17.253, $q > 0.5$: 17.290）也全面优于所有 reweighting。论文辩称 hard filtering"requires a calibrated detection threshold"，但 threshold 从 0.3 到 0.5 仅差 0.037 PPL，远小于 filtering vs. reweighting 的 0.36 差距——threshold 选择对 filtering 的敏感度远低于论文暗示的程度。
- 为什么影响接收：如果一个更简单的方法全面优于所提方法，审稿人会质疑 reweighting 的实际价值。
- 建议修改方向：(a) 在 filtering threshold 不确定的场景下展示 reweighting 的 robustness 优势（例如 threshold 极端错误时 filtering 崩溃但 reweighting 仍稳定），或 (b) 明确 reposition 为"当 threshold calibration 不可行时的 safe fallback"，并量化这种场景的实际发生频率。

**N3** [critical] 效果量极小，downstream 无改善
- 具体位置：Section 5.1, Appendix G (Table 5), Limitations (Effect size 段)
- 问题：Adaptive vs. Uniform 的 PPL 改善仅 0.043（0.24% relative）。更关键的是，Appendix Table 5 显示所有 downstream benchmarks（ARC-C, ARC-E, HellaSwag, PIQA, WinoGrande）adaptive 均不优于 uniform（4/5 benchmarks 轻微 degradation）。PPL 改善未转化为任何可测量的 downstream benefit。Limitations 虽承认效果量小，但 Introduction 和 Abstract 的 framing 未充分体现这一限制。
- 为什么影响接收：一个在 downstream tasks 上无改善的方法，仅凭 0.04 PPL 差异难以说服审稿人其具有实际价值。
- 建议修改方向：Abstract 和 Introduction 应更明确地定位贡献为"principled exponent selection with comparable performance"而非暗示性能提升。或补充更大规模的 downstream 评估。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 新颖性相对 Drayson et al. 的增量有限
- 具体位置：Section 3 (Method), Related Work paragraph 3
- 问题：核心公式 $w(x) = (1-q(x))^b$ 直接来自 Drayson et al.。本文的增量是选 $b$ 的方法（dual constraint）。论文声称三点差异（per-batch vs global, loss reweighting vs SIR, lightweight detector），但：(i) ESS 作为 importance sampling 的诊断指标是标准做法（Vehtari et al., SMC 文献中广泛使用 ESS 阈值触发 resampling）；(ii) "minimum intervention"本质是标准约束优化中选 feasible region 的最小值，数学上是 trivial 的选择；(iii) loss reweighting vs. SIR 是实现选择，不是方法论创新。Dual constraint 的形式（$\alpha_{\text{eff}} \geq \tau$ + ESS $\geq n_{\min}$）在 importance sampling 文献中有类似先例（e.g., causal inference 中 balance constraint + ESS floor）。
- 建议：更清楚地说明 dual constraint 在 contamination-aware training 语境下的独特性，而非仅依赖"minimum intervention"这一标签。

**W2** [warning] 仅模拟污染，无真实 web 数据验证
- 具体位置：Section 4 (Training Data), Limitations (Contamination range 段)
- 问题：synthetic contamination 通过 Qwen3-0.6B 自己生成的 continuations 注入，是最容易检测的场景（self-contamination, 同一 model）。真实 web 污染来自多种模型、多种风格、paraphrase、翻译等，检测难度更高。方法在 AUC=0.939 的"easy"检测场景下仅获得 0.04 PPL 改善；在检测器更弱的真实场景中表现完全未知。
- 建议：至少用一个不同 model（如 GPT-4 生成的文本 + 不同检测器）进行验证，或在 naturally contaminated corpus（如 recent Common Crawl snapshot）上测试。

**W3** [warning] $\tau$ 实际需要根据 $\rho$ 调整，削弱"zero validation cost"声明
- 具体位置：Section 5.2 (line 72), Discussion ($\tau$ as a practical dial 段)
- 问题：Discussion 建议 "$\tau \approx 1 - \rho/2$ when a rough contamination estimate is available"，但 $\rho$ 在问题设定中被假定未知（Section 3.1: "The contamination ratio $\rho$ is unknown"）。同时实验显示 optimal $\tau$ 从 0.8（$\rho=0.4$）变为 0.7（$\rho=0.6$），$\rho=0.2$ 时方法甚至退化（+0.046 PPL）。这意味着 $\tau$ 不是真正的 set-once 超参数，实际需要某种 contamination estimate，部分否定了"zero validation cost"的核心卖点。
- 建议：诚实讨论 $\tau$ 在不同 $\rho$ 下的敏感性，不应同时声称"$\rho$ unknown"和"$\tau \approx 1-\rho/2$"。

**W4** [warning] 引用密度不足
- 具体位置：references.bib (全文)
- 问题：仅 23 篇引用。EMNLP 长文通常 40-60+ 篇。缺失的重要类别：
  - **Curriculum learning / self-paced learning**（Bengio et al. 2009; Kumar et al. 2010）：foundational sample weighting 文献
  - **Focal loss**（Lin et al. 2017）：per-sample adaptive weighting 的经典先例
  - **DRO 基础论文**（Sagawa et al. 2020）：DoReMi 基于 Group DRO 但原始 DRO 未引
  - **更多检测器**：Fast-DetectGPT (Bao et al. 2024), Binoculars (Hans et al. 2024), ghostbuster 等
  - **Watermarking**（Kirchenbauer et al. 2023）：另一种 provenance tracking 方法，应在 related work 中至少提及
  - **数据质量/curation 文献**：DataComp, D4 等
- 建议：补充至少 15-20 篇相关引用。

**W5** [warning] Baselines 不完整（Golden Ratio 和 Detect & Remove 仅 single seed）
- 具体位置：Table 1 (footnotes $\dagger$ and $\S$)
- 问题：Golden Ratio 和 Detect & Remove 仅报告 seed 42 的结果，无法做统计比较。论文的核心 claim 之一是"adaptive 与 grid-best indistinguishable"需要 3-seed 对比，但 Golden Ratio（理论 baseline）和 Detect & Remove（实际上 strongest baseline）却缺乏多 seed 验证。
- 建议：至少为 Detect & Remove 补充 3-seed 实验。

---

## 小问题（不影响接收）

**M1** [minor] experiments.tex line 20 写"We compare five approaches"但实际列出 6 个方法（Uniform, Grid-$b$, ESS-only, Golden Ratio, Adaptive, Detect & Remove）。

**M2** [minor] Grid search 在正文说"nine complete training runs"（Section 5.1 line 8），但 Appendix Table 2 实际列出 9 个 $b$ 值（0.1-5.0）而 Section 4 Methods 段列出 7 个值"$b \in \{0.3, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0\}$"。Grid 值列表不一致。

**M3** [minor] 引用验证显示 `vehtari2024psis` 年份可能有误（bib 标 2024，API 匹配到 2015 的 JMLR 版本；该论文有多个版本，建议确认引用的是哪个版本）。`guo2025escaping` 缺少 arXiv ID。

**M4** [minor] Abstract line 1 用 `20--60\%` (en-dash 用于数字范围，可接受)，全文无解释性 em-dash 或 en-dash，AI 写作痕迹检查通过。

**M5** [minor] Appendix Table 4 (Hybrid) 的 $\rho=0.6$ 行有 footnote $^*$ 说明 hybrid 方法改变了 effective $\rho$，使结果"not directly comparable"。既然不可比，这行数据的意义需要更清楚的说明。

---

## 历史 Issue 检查

**RR-W1** [已修复] ✓ 此前错误声称"from random initialization"已修正为"continued pretraining"（Abstract line 7, Introduction line 23, Experiments line 12）。

**RR-W2** [已修复] ✓ 此前错误声称"balanced real/synthetic test set"已修正为"containing only human-authored text"（Experiments line 16, Results line 21）。

---

## Questions to Authors

1. 在 downstream tasks 全面无改善（Table 5）的情况下，0.04 PPL 的改善有何实际意义？是否有理论或实证依据表明这种 PPL 差异会在更大规模上被放大？

2. 如果 hard filtering（即使 threshold 选择不完美）始终大幅优于 reweighting，什么情况下用户应该选择 reweighting 而非 filtering？请给出具体场景和量化论据。

3. $\rho = 0.2$ 时方法退化（+0.046 PPL）。如果真实 web 污染是 20-60%（论文自己引用的范围），方法在区间低端失效，如何向 practitioner 推荐？

4. Proposition 1 的证明依赖"for any detector with better-than-random discrimination"。当检测器在某些 domain 上接近 random（AUC ≈ 0.5）时，monotonicity 不成立，方法行为如何？

5. Discussion 建议 $\tau \approx 1 - \rho/2$，但 $\rho$ 被假定未知。如何调和这个矛盾？

---

## Missing References（建议补充）

- Bengio et al. (2009) — Curriculum Learning
- Kumar et al. (2010) — Self-Paced Learning
- Lin et al. (2017) — Focal Loss
- Sagawa et al. (2020) — Distributionally Robust Optimization (Group DRO)
- Kirchenbauer et al. (2023) — Watermarking for LLMs
- Bao et al. (2024) — Fast-DetectGPT
- Hans et al. (2024) — Binoculars (zero-shot LLM text detection)
- Gadre et al. (2024) — DataComp-LM
- Abbas et al. (2023) — Semdedup
- Tirumala et al. (2024) — D4 (data deduplication)

---

## 主要优势

1. **方法 formulation 干净**：dual constraint 的数学表达简洁，Algorithm 1 清晰可实现，Proposition 1 有完整证明。
2. **Ablation 设计好且诚实**：四方法层级（Adaptive < Uniform < ESS-only < Random）有效分解了 detector signal 和 minimum intervention 两个因素的贡献。
3. **写作质量高**：无 AI 写作痕迹（无 em-dash, 无 blacklist 用词, 无过度分段），叙事主线基本连贯，Limitations 诚实全面。
4. **Hard filtering 对比坦诚**：没有隐藏 Detect & Remove 的优势，反而主动讨论，体现学术诚信。
5. **超参数分析充分**：$\tau$ sweep 和 $n_{\min}$ 分析展示了方法的 sensitivity landscape。

---

## 总结评价

这是一篇方法清晰、写作诚实的论文，提出了一个 principled 的 hyperparameter-free exponent 选择框架。但三个核心限制使其不太适合 EMNLP 长文：(1) 实验仅 0.6B 单一规模，远不及被改进的 Drayson et al. 的覆盖范围；(2) 效果量极小（0.04 PPL）且 downstream 无改善；(3) hard filtering 以大幅优势碾压，使 reweighting 的实际应用场景不清晰。方法的新颖性在 importance sampling 文献中也偏增量——dual constraint 是已知技术在新场景的组合应用。建议补充 1-3B 规模实验和自然污染数据验证后，可作为 Findings 论文接收。

**Overall: 3.0/5 (Findings)**
**Confidence: 4/5**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-18T06:31:24.373896+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 1 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — Round 1 审稿报告\n\n**Overall**: 3.0/5 (Findings)\n**Soundness**: 3.0/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n**一句话总结**: 方法 formulation 干净、ablation 诚实，但实验规模（仅 0.6B/132M tokens）和效果量（~0.04 PPL）不足以支撑 EMNLP 长文；hard filtering 以显著优势碾压所有 reweighting 方法，削弱了实际动机。\n\n### Must-Fix 问题\n\n**N1** [critical] 实验规模不足以支撑长文贡献声明\n- 全部主实验仅在 Qwen3-0.6B（单一模型规模）上进行，数据量 132M tokens。cross-model 实验（Llama-3.2-3B）仅 single seed。对于 EMNLP 长文，至少需要两个不同规模的模型 + 多 seed 复现。Drayson et al. (2025) 在 160M/360M/1.7B 三个规模上实验，本文声称改进了 Drayson 的方法却在实验覆盖上远不如它。\n\n**N2** [critical] Hard filtering 碾压所有 reweighting 方法，削弱核心动机\n- Detect & Remove（PPL 17.290）比 Adaptive（17.651）低 0.36 PPL。Appendix 显示即使 suboptimal threshold（$q > 0.3$: 17.253）也全面优于所有 reweighting。threshold 从 0.3 到 0.5 仅差 0.037 PPL，远小于 filtering vs. reweighting 的 0.36 差距——threshold 选择对 filtering 的敏感度远低于论文暗示的程度。\n\n**N3** [critical] 效果量极小，downstream 无改善\n- Adaptive vs. Uniform 的 PPL 改善仅 0.043（0.24% relative）。Appendix Table 5 显示所有 downstream benchmarks adaptive 均不优于 uniform（4/5 benchmarks 轻微 degradation）。\n\n### Should-Fix 问题\n\n**W1** [warning] 新颖性相对 Drayson et al. 的增量有限\n- 核心公式直接来自 Drayson et al.。增量是选 $b$ 的方法。ESS 作为 IS 诊断是标准做法，\"minimum intervention\"本质是选 feasible region 最小值，数学上 trivial。\n\n**W2** [warning] 仅模拟污染，无真实 web 数据验证\n- synthetic contamination 通过自生成注入，是最容易检测的场景。\n\n**W3** [warning] $\\tau$ 实际需要根据 $\\rho$ 调整，削弱\"zero validation cost\"声明\n- optimal $\\tau$ 从 0.8（$\\rho=0.4$）变为 0.7（$\\rho=0.6$），$\\rho=0.2$ 时方法退化。Discussion 建议 \"$\\tau \\approx 1 - \\rho/2$\" 但 $\\rho$ 被假定未知。\n\n**W4** [warning] 引用密度不足\n- 仅 23 篇引用，EMNLP 长文通常 40-60+。缺失 curriculum learning, focal loss, DRO, watermarking, 更多检测器, DataComp 等。\n\n**W5** [warning] Golden Ratio 和 Detect & Remove 仅 single seed\n\n### Minor 问题\n\n**M1** \"five approaches\" 实际列出 6 个方法。\n**M2** Grid 值列表不一致（正文 7 个 vs Appendix 9 个）。\n**M3** vehtari2024psis 年份可能有误，guo2025escaping 缺 arXiv ID。\n**M4** AI 写作痕迹检查通过。\n**M5** Hybrid 方法 $\\rho=0.6$ 行数据可比性说明不清。\n\n### Missing References\nBengio et al. (2009) Curriculum Learning, Kumar et al. (2010) Self-Paced Learning, Lin et al. (2017) Focal Loss, Sagawa et al. (2020) Group DRO, Kirchenbauer et al. (2023) Watermarking, Bao et al. (2024) Fast-DetectGPT, Hans et al. (2024) Binoculars, Gadre et al. (2024) DataComp-LM, Abbas et al. (2023) Semdedup, Tirumala et al. (2024) D4.\n\n---\n\n请对以上每条意见逐一给出 [AGREE] 或 [REBUT] 回应。",
  "reviewer_id": "1",
  "project": "provenance_weight_training",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 1 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — Round 1 审稿报告\n\n**Overall**: 3.0/5 (Findings)\n**Soundness**: 3.0/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n**一句话总结**: 方法 formulation 干净、ablation 诚实，但实验规模（仅 0.6B/132M tokens）和效果量（~0.04 PPL）不足以支撑 EMNLP 长文；hard filtering 以显著优势碾压所有 reweighting 方法，削弱了实际动机。\n\n### Must-Fix 问题\n\n**N1** [critical] 实验规模不足以支撑长文贡献声明\n- 全部主实验仅在 Qwen3-0.6B（单一模型规模）上进行，数据量 132M tokens。cross-model 实验（Llama-3.2-3B）仅 single seed。对于 EMNLP 长文，至少需要两个不同规模的模型 + 多 seed 复现。Drayson et al. (2025) 在 160M/360M/1.7B 三个规模上实验，本文声称改进了 Drayson 的方法却在实验覆盖上远不如它。\n\n**N2** [critical] Hard filtering 碾压所有 reweighting 方法，削弱核心动机\n- Detect & Remove（PPL 17.290）比 Adaptive（17.651）低 0.36 PPL。Appendix 显示即使 suboptimal threshold（$q > 0.3$: 17.253）也全面优于所有 reweighting。threshold 从 0.3 到 0.5 仅差 0.037 PPL，远小于 filtering vs. reweighting 的 0.36 差距——threshold 选择对 filtering 的敏感度远低于论文暗示的程度。\n\n**N3** [critical] 效果量极小，downstream 无改善\n- Adaptive vs. Uniform 的 PPL 改善仅 0.043（0.24% relative）。Appendix Table 5 显示所有 downstream benchmarks adaptive 均不优于 uniform（4/5 benchmarks 轻微 degradation）。\n\n### Should-Fix 问题\n\n**W1** [warning] 新颖性相对 Drayson et al. 的增量有限\n- 核心公式直接来自 Drayson et al.。增量是选 $b$ 的方法。ESS 作为 IS 诊断是标准做法，\"minimum intervention\"本质是选 feasible region 最小值，数学上 trivial。\n\n**W2** [warning] 仅模拟污染，无真实 web 数据验证\n- synthetic contamination 通过自生成注入，是最容易检测的场景。\n\n**W3** [warning] $\\tau$ 实际需要根据 $\\rho$ 调整，削弱\"zero validation cost\"声明\n- optimal $\\tau$ 从 0.8（$\\rho=0.4$）变为 0.7（$\\rho=0.6$），$\\rho=0.2$ 时方法退化。Discussion 建议 \"$\\tau \\approx 1 - \\rho/2$\" 但 $\\rho$ 被假定未知。\n\n**W4** [warning] 引用密度不足\n- 仅 23 篇引用，EMNLP 长文通常 40-60+。缺失 curriculum learning, focal loss, DRO, watermarking, 更多检测器, DataComp 等。\n\n**W5** [warning] Golden Ratio 和 Detect & Remove 仅 single seed\n\n### Minor 问题\n\n**M1** \"five approaches\" 实际列出 6 个方法。\n**M2** Grid 值列表不一致（正文 7 个 vs Appendix 9 个）。\n**M3** vehtari2024psis 年份可能有误，guo2025escaping 缺 arXiv ID。\n**M4** AI 写作痕迹检查通过。\n**M5** Hybrid 方法 $\\rho=0.6$ 行数据可比性说明不清。\n\n### Missing References\nBengio et al. (2009) Curriculum Learning, Kumar et al. (2010) Self-Paced Learning, Lin et al. (2017) Focal Loss, Sagawa et al. (2020) Group DRO, Kirchenbauer et al. (2023) Watermarking, Bao et al. (2024) Fast-DetectGPT, Hans et al. (2024) Binoculars, Gadre et al. (2024) DataComp-LM, Abbas et al. (2023) Semdedup, Tirumala et al. (2024) D4.\n\n---\n\n请对以上每条意见逐一给出 [AGREE] 或 [REBUT] 回应。",
    "reviewer_id": "1",
    "project": "provenance_weight_training",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-18T06:31:54.541613+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 30167
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-18T06:31:54.943909+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 1 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — Round 1 审稿报告\n\n**Overall**: 3.0/5 (Findings)\n**Soundness**: 2.5/5 | **Excitement**: 3.0/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n**一句话总结**: 方法直觉清晰、框架简洁，但核心 claim 的统计支撑存在方法论缺陷（用 failure-to-reject 代替 equivalence test），实验规模和 detector 覆盖不足以支撑论文的一般性主张。\n\n### Must-Fix 问题\n\n**N1** [critical] \"Statistically indistinguishable\" claim 使用了错误的统计范式\n- $p = 0.30$ 仅表示未能拒绝差异为零的零假设，不等于证明等价。N=3 的统计功效极低。要声称\"不可区分\"需要 equivalence test（如 TOST）。将 absence of evidence 当作 evidence of absence 是统计推断的基本错误。\n\n**N2** [critical] $\\alpha_{\\mathrm{eff}}$ 的理论动机与实际计算之间存在逻辑断层\n- $\\alpha_{\\mathrm{eff}}$ 使用 $r_i = \\mathbf{1}[q_i \\leq 0.5]$，但理论动机来自 Wang et al. (2026) 基于真实 $\\alpha$ 的收敛速率定理。当检测器不完美时，$\\alpha_{\\mathrm{eff}}$ 可能系统性偏离真实 $\\alpha$。Proposition 1 的 covariance 正性是 tautological（$r_i$ 是 $q_i$ 的阈值函数）。\n\n**N3** [critical] 实验外部效度严重不足\n- 单一模型（0.6B）、单一数据源（FineWeb）、单一 detector（TF-IDF+LR）、自污染设计。$\\rho = 0.2$ 失效但无深入分析。论文 framing 为 general-purpose 但实验只覆盖极窄 setting。\n\n### Should-Fix 问题\n\n**W1** [warning] Downstream benchmarks 未能展示实际价值\n- 5 个 downstream benchmarks 全部在标准误差内，且 4/5 个 adaptive 略微低于 uniform。\n\n**W2** [warning] Proposition 1 声称 strictly increasing 但证明只建立 non-decreasing\n- Non-negative covariance 只能推出 non-decreasing，不是 strictly increasing。\n\n**W3** [warning] ESS monotonicity 未证明\n- 引用 Kimura et al. (2024) 综述但未给出具体证明。ESS 单调性对 bisection 算法正确性至关重要。\n\n**W4** [warning] Grid-$b$ baseline 存在 post-hoc oracle 问题但论文未充分讨论\n- Grid-best 是在测试集上 post-hoc 选择的，给了 grid search oracle 优势。实践中需独立 validation set。\n\n**W5** [warning] Detect & Remove 和 Golden Ratio 仅单 seed\n\n**W6** [warning] 效应量在实际意义上是否足够大？\n- 0.043 PPL（0.24% relative），downstream 无改善。论文标题和 Abstract 的 framing 与实际效果不匹配。\n\n### Questions\n\n**Q1.** 如果将 $r_i$ 改为 soft indicator $r_i = 1 - q_i$，性能如何变化？\n**Q2.** $\\rho = 0.2$ 时是否测试过 $\\tau = 0.5$ 或 $\\tau = 0.6$？\n**Q3.** 训练 loss 几乎不变，PPL 改善从何而来？evaluation set 是 human-only 是否造成隐式 importance weighting？\n**Q4.** micro-batch size $B = 4$ 上 $\\alpha_{\\mathrm{eff}}$ 和 ESS 的估计方差是否过大？\n**Q5.** \"score calibration may matter as much as raw classification accuracy\" 无实验支撑。\n\n### Missing References\n- Temperature scaling 基础文献（Guo et al., 2017）\n- Hans et al. (2024) Binoculars\n- Equivalence testing 文献（Schuirmann 1987, Lakens 2017）\n- guo2025escaping 缺 arXiv ID，vehtari2024psis 年份待核实\n\n---\n\n请对以上每条意见逐一给出 [AGREE] 或 [REBUT] 回应。",
  "reviewer_id": "2",
  "project": "provenance_weight_training",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 1 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — Round 1 审稿报告\n\n**Overall**: 3.0/5 (Findings)\n**Soundness**: 2.5/5 | **Excitement**: 3.0/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n**一句话总结**: 方法直觉清晰、框架简洁，但核心 claim 的统计支撑存在方法论缺陷（用 failure-to-reject 代替 equivalence test），实验规模和 detector 覆盖不足以支撑论文的一般性主张。\n\n### Must-Fix 问题\n\n**N1** [critical] \"Statistically indistinguishable\" claim 使用了错误的统计范式\n- $p = 0.30$ 仅表示未能拒绝差异为零的零假设，不等于证明等价。N=3 的统计功效极低。要声称\"不可区分\"需要 equivalence test（如 TOST）。将 absence of evidence 当作 evidence of absence 是统计推断的基本错误。\n\n**N2** [critical] $\\alpha_{\\mathrm{eff}}$ 的理论动机与实际计算之间存在逻辑断层\n- $\\alpha_{\\mathrm{eff}}$ 使用 $r_i = \\mathbf{1}[q_i \\leq 0.5]$，但理论动机来自 Wang et al. (2026) 基于真实 $\\alpha$ 的收敛速率定理。当检测器不完美时，$\\alpha_{\\mathrm{eff}}$ 可能系统性偏离真实 $\\alpha$。Proposition 1 的 covariance 正性是 tautological（$r_i$ 是 $q_i$ 的阈值函数）。\n\n**N3** [critical] 实验外部效度严重不足\n- 单一模型（0.6B）、单一数据源（FineWeb）、单一 detector（TF-IDF+LR）、自污染设计。$\\rho = 0.2$ 失效但无深入分析。论文 framing 为 general-purpose 但实验只覆盖极窄 setting。\n\n### Should-Fix 问题\n\n**W1** [warning] Downstream benchmarks 未能展示实际价值\n- 5 个 downstream benchmarks 全部在标准误差内，且 4/5 个 adaptive 略微低于 uniform。\n\n**W2** [warning] Proposition 1 声称 strictly increasing 但证明只建立 non-decreasing\n- Non-negative covariance 只能推出 non-decreasing，不是 strictly increasing。\n\n**W3** [warning] ESS monotonicity 未证明\n- 引用 Kimura et al. (2024) 综述但未给出具体证明。ESS 单调性对 bisection 算法正确性至关重要。\n\n**W4** [warning] Grid-$b$ baseline 存在 post-hoc oracle 问题但论文未充分讨论\n- Grid-best 是在测试集上 post-hoc 选择的，给了 grid search oracle 优势。实践中需独立 validation set。\n\n**W5** [warning] Detect & Remove 和 Golden Ratio 仅单 seed\n\n**W6** [warning] 效应量在实际意义上是否足够大？\n- 0.043 PPL（0.24% relative），downstream 无改善。论文标题和 Abstract 的 framing 与实际效果不匹配。\n\n### Questions\n\n**Q1.** 如果将 $r_i$ 改为 soft indicator $r_i = 1 - q_i$，性能如何变化？\n**Q2.** $\\rho = 0.2$ 时是否测试过 $\\tau = 0.5$ 或 $\\tau = 0.6$？\n**Q3.** 训练 loss 几乎不变，PPL 改善从何而来？evaluation set 是 human-only 是否造成隐式 importance weighting？\n**Q4.** micro-batch size $B = 4$ 上 $\\alpha_{\\mathrm{eff}}$ 和 ESS 的估计方差是否过大？\n**Q5.** \"score calibration may matter as much as raw classification accuracy\" 无实验支撑。\n\n### Missing References\n- Temperature scaling 基础文献（Guo et al., 2017）\n- Hans et al. (2024) Binoculars\n- Equivalence testing 文献（Schuirmann 1987, Lakens 2017）\n- guo2025escaping 缺 arXiv ID，vehtari2024psis 年份待核实\n\n---\n\n请对以上每条意见逐一给出 [AGREE] 或 [REBUT] 回应。",
    "reviewer_id": "2",
    "project": "provenance_weight_training",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-18T06:31:56.509030+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1565
}
```

</details>

---


### Assistant

_source line 80 · 2026-05-18T06:31:58.970917+00:00_

Step 2 交叉分享已发出。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 5

## Round 5

2 recorded events


### User

_source line 81 · 2026-05-18T06:32:01.719938+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**核心判断：Overall 3.0/5 (Findings level)**

三个关键问题：
1. **规模不足**：仅 0.6B/132M tokens，cross-model 仅 single seed，远不及 Drayson et al. 的三规模覆盖
2. **效果量极小 + downstream 无改善**：PPL 改善 0.04（0.24% relative），5 个 downstream benchmarks 全部无显著改善
3. **Hard filtering 碾压**：Detect & Remove (17.290) 远优于 Adaptive (17.651)，即使 threshold 不完美也全面领先

优势方面：formulation 干净、ablation 设计好、写作质量高（无 AI 痕迹）、Limitations 诚实。历史 issue RR-W1/RR-W2 均已修复。引用偏少（23 篇，建议补至 40+）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 82 · 2026-05-18T06:32:08.336100+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 6

## Round 6

2 recorded events


### User

_source line 83 · 2026-05-18T06:33:32.627422+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: 实验规模不足以支撑长文贡献声明**

同意。我在自己的 N3 中提出了高度一致的问题。补充两点：
1. Drayson et al. (2025) 在 160M/360M/1.7B 三个规模上做了系统实验（Related Work, Section 2 对此有明确讨论），本文声称改进其方法却实验覆盖远不如它，这个对比会让审稿人印象很差。
2. Limitations section 的 Llama-3.2-3B 单 seed 结果（"PPL and HellaSwag parity with uniform, MMLU +1.6pp"）实际上**更不利**——PPL parity 意味着方法在 3B 上没有改善，且单 seed 不能下结论。这比没有 3B 实验更糟，因为它暗示方法可能不 scale。

**[AGREE with nuance] R2-N2: Hard filtering 碾压所有 reweighting 方法，削弱核心动机**

基本同意 R2 的观察（0.36 PPL 差距确实显著），但认为 R2 对 threshold 敏感度的分析有遗漏：
- R2 说 "threshold 从 0.3 到 0.5 仅差 0.037 PPL，远小于 filtering vs. reweighting 的 0.36 差距"。这是正确的，但**方向信息**是关键：0.3 比 0.5 更好（17.253 vs 17.290），但论文指出"no principled way to choose the direction without validation data"（Section 5.1）。在实践中，用错方向（选 0.7 而非 0.3）的 cost 可能远大于 0.037。论文没有测试更极端的阈值（如 0.1 或 0.9），所以 threshold robustness 的 full picture 缺失。
- 然而，即使考虑此点，R2 的核心论点成立：Detect & Remove 在论文自己的实验中全面优于 reweighting，论文对此的解释（"requires calibrated detection threshold"）不够有力。如果 threshold 在 [0.3, 0.7] 全面优于 reweighting，那 "threshold-free" 的优势就不够 compelling。
- 论文的 Discussion（Section 6）确实诚实地将 D&R、Hybrid、Adaptive 放在 spectrum 上，但 Introduction 和 Abstract 的 framing 没有充分反映 D&R 的优势。

**[AGREE] R2-N3: 效果量极小，downstream 无改善**

完全同意。我在 W1 和 W6 中详细讨论了这个问题。特别强调 Appendix Table 5 的 downstream 结果：4/5 benchmarks adaptive 略低于 uniform（ARC-Challenge -0.005, ARC-Easy -0.007, HellaSwag -0.005, WinoGrande -0.008），虽然在标准误差内，但方向一致性 suggests 即使有统计显著的 PPL 改善，它也不反映真正的训练质量提升——更可能是对 human-only evaluation set 的隐式 distribution matching（我的 Q3 直接问了这个问题）。

---

### Should-Fix 问题

**[REBUT] R2-W1: 新颖性相对 Drayson et al. 的增量有限**

不完全同意 R2 将贡献定性为 "mathematically trivial"。
1. **ESS-only 失败的反直觉性**：如果 "minimum intervention 本质是选 feasible region 最小值" 是 trivial，那为什么直觉上合理的 "选最大值"（ESS-only）反而比 uniform 更差？Table 1 显示 ESS-only (17.737) 比 uniform (17.694) 差 0.043，和 adaptive 的改善幅度几乎对称。这说明 exponent 选择的方向（最小 vs 最大）有实质性影响，不是 trivial 的 design choice。
2. **Regime analysis 提供了非平凡洞察**：Section 5.4 报告 $\alpha_{\mathrm{eff}}$-binding batches 中 dual-constrained $b^*$ 仅为 ESS-only 的 ~20%（median 0.80 vs 3.59），4.9× 的 over-intervention ratio 量化了 ESS-only 的失败原因。这种失败模式分析不是从 formulation 就能预见的。
3. **但我同意数学深度确实有限**：Proposition 1 的证明是 straightforward 的 covariance 计算，bisection 是标准数值方法。novelty 更多在 problem formulation 和 empirical insight 层面，不在数学工具层面。

综合判断：novelty 属于 "useful engineering insight backed by careful ablation"，足以支撑 Findings，但确实不够 exciting 支撑主会议长文。

**[AGREE] R2-W2: 仅模拟污染，无真实 web 数据验证**

同意。我在 N3 中也指出了这一点。自污染（用 Qwen3-0.6B 生成再用同架构训练）是最容易检测的场景——generator 和 trainee 共享分布，TF-IDF+LR 就能达到 AUC 0.939。真实场景中生成器通常是 GPT-4/Claude 等更大/不同模型，检测难度和分布特征完全不同。

**[AGREE with nuance] R2-W3: $\tau$ 需要根据 $\rho$ 调整，削弱 "zero validation cost"**

基本同意这个逻辑矛盾，但论文有部分 defense：
- Section 5.3 的 $\tau$ sweep 显示 $\tau \in [0.5, 0.8]$ 全部优于 uniform（Table 3），safe range 跨 0.3。这意味着默认 $\tau = 0.8$ 不是唯一可行值，即使不调整也有效。
- 但 R2 指出的矛盾是成立的：Discussion 建议 $\tau \approx 1 - \rho/2$ 作为 heuristic，但 $\rho$ 被假定未知（Section 3.1 的核心假设）。如果需要估计 $\rho$ 来设 $\tau$，那就引入了额外的依赖。论文应该明确说明 $\tau = 0.8$ 作为 fixed default 在 $\rho \in [0.4, 0.6]$ 足够好，而不是暗示可以根据 $\rho$ 微调。
- $\rho = 0.2$ 的失效（Limitations: +0.046 PPL）更严重：它表明方法有一个下界有效范围，但这个下界在实践中可能覆盖大部分真实场景（当前 web 污染估计 20-60%，Section 1）。

**[AGREE] R2-W4: 引用密度不足**

同意。23 篇引用对 EMNLP 长文偏少。R2 列出的缺失引用大部分确实相关：
- **高度相关（应引用）**：Sagawa et al. (2020) Group DRO（和 DoReMi 关联密切）、Hans et al. (2024) Binoculars（检测器替代方案）、Gadre et al. (2024) DataComp-LM（数据质量基准）、Bao et al. (2024) Fast-DetectGPT
- **相关但非必需**：Bengio et al. (2009) Curriculum Learning、Kumar et al. (2010) Self-Paced Learning（方法论关联较弱——这些是 difficulty-based ordering，不是 provenance-based reweighting）；Lin et al. (2017) Focal Loss（loss reweighting 的一般性引用，可以放但不是 gap）
- **我额外建议**：温度校准文献 Guo et al. (2017) "On Calibration of Modern Neural Networks"（论文用了 temperature scaling 但未引用）

**[AGREE] R2-W5: Golden Ratio 和 Detect & Remove 仅 single seed**

同意，与我的 W5 一致。

---

### Minor 问题

**[AGREE] R2-M1: "five approaches" 实际列出 6 个方法**

确认。Section 4 Methods 段落说 "We compare five approaches:" 但列表包含 Uniform, Grid-$b$, ESS-only, Golden Ratio, Adaptive, Detect & Remove = 6 个。简单计数错误。

**[AGREE] R2-M2: Grid 值列表不一致**

确认。Section 4 列出 7 个值 $\{0.3, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0\}$，但 Table 1 caption 说 "nine candidates"，Appendix Table 2 列出 9 个值（多了 0.1 和 0.2）。正文描述和附录数据不一致。

**[AGREE] R2-M3: 引用格式问题**

与我的 Missing References 发现一致。`vehtari2024psis` 年份可能是 JMLR 正式发表年份（2024）但原始版本 2015，需核实。`guo2025escaping` 在线验证完全找不到匹配，存在 phantom reference 风险。

**[AGREE] R2-M4: AI 写作痕迹检查通过**

同意。论文写作风格自然，未发现典型 AI 写作标志（过度 em-dash、-ing 结尾、过度分段等）。

**[AGREE] R2-M5: Hybrid $\rho=0.6$ 数据可比性说明不清**

同意。Appendix Table 4 的脚注（"$^*$Hybrid at $\rho=0.6$ filters high-confidence synthetic ($q>0.95$), reducing effective $\rho$ to $\approx$0.4"）说明这行数据与同列 $\rho=0.6$ baselines 不直接可比，但这个说明容易被忽略。应该在正文中更明确地讨论。

---

### Missing References

R2 列出的引用中，我同意以下为实质性遗漏：
- Hans et al. (2024) Binoculars — 直接相关的检测器方法
- Bao et al. (2024) Fast-DetectGPT — DetectGPT 的改进，论文已引 DetectGPT 但缺后续
- Sagawa et al. (2020) Group DRO — DoReMi 的理论基础，论文引了 DoReMi 但缺其上游
- Gadre et al. (2024) DataComp-LM — 数据选择/质量的重要基准

以下为 nice-to-have 但非 gap：
- Bengio et al. (2009) / Kumar et al. (2010) — difficulty-based，与 provenance-based 机制不同
- Kirchenbauer et al. (2023) Watermarking — 提供 ground-truth provenance 但方法逻辑不同
- Abbas et al. (2023) Semdedup / Tirumala et al. (2024) D4 — deduplication，不是 provenance reweighting

---

### 总结：两位 Reviewer 的共识与分歧

**高度共识区域**（两位 Reviewer 独立指出）：
1. 实验规模不足（单一模型/detector/数据源）— 两位均列为 critical
2. 效果量小且 downstream 无改善 — 两位均列为 critical/warning
3. Detect & Remove 优势明显 — R2 更强调，R1 同意
4. Golden Ratio / D&R 单 seed 不足 — 两位一致
5. 引用问题（guo2025escaping 可疑、vehtari 年份）— 两位一致

**R1 独有的关注点**：
- "Indistinguishable" claim 的统计范式错误（N1）— R2 未提及但这是核心方法论问题
- $\alpha_{\mathrm{eff}}$ 理论动机与实际计算的逻辑断层（N2）— R2 未涉及
- Proposition 1 严格递增 vs 非递减的证明 gap（W2）
- ESS 单调性未证明（W3）

**R2 独有但有效的关注点**：
- Threshold 敏感度分析（N2 中的定量论证）— R1 关注但 R2 分析更锐利
- 引用密度和缺失引用的系统性列举（W4）— R2 更全面
- $\tau$ 与 $\rho$ 的依赖矛盾 "zero validation cost" claim（W3）— R1 在 Q2 问了但 R2 直接指出矛盾

**分歧区域**：
- **Novelty 判断**：R2 认为数学上 trivial，R1 认为 ESS-only 失败的反直觉性和 regime analysis 有非平凡价值。R1 倾向 Findings 可接收，R2 也给了 3.0 但 excitement 更低（2.5 vs 3.0）。

**综合建议**：当前版本适合 Findings，不适合主会议。修改后重投需要至少解决实验规模和统计 claim 两个核心问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 84 · 2026-05-18T06:33:39.480915+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 7

## Round 7

2 recorded events


### User

_source line 85 · 2026-05-18T06:33:47.006934+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

对 R2 的 10 条意见（3 Must-Fix + 5 Should-Fix + 5 Minor），我的判断：
- **8 条 AGREE**（N1, N3, W2, W4, W5, M1-M5）
- **1 条 AGREE with nuance**（N2: 同意 filtering 优势明显，但补充了 threshold 方向不可知的 defense；W3: 同意 $\tau$-$\rho$ 矛盾，但指出 safe range 较宽）
- **1 条 REBUT**（W1: 不同意 novelty "trivial" 判断——ESS-only 失败是反直觉的，regime analysis 提供了非平凡洞察，但同意数学深度有限）

两位 Reviewer 在实验规模不足、效果量小、D&R 优势、引用问题上高度共识。R1 额外关注了统计推断范式错误和 $\alpha_{\mathrm{eff}}$ 理论 gap，R2 在 threshold 敏感度和引用密度上分析更深入。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 86 · 2026-05-18T06:34:03.884816+00:00_

Reviewer 1 交叉回应已收到。

**Step 3 收敛判断**：两位 Reviewer 在所有关键问题上达成高度共识（8/10 条 AGREE，1 条 AGREE with nuance，仅 novelty 判断有轻微分歧但不影响结论）。两位均给出 3.0/5 (Findings)。无需进入 Round 2。

进入 Step 4：汇总报告。等待 Reviewer 2 的交叉回应后统一合并。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 8

## Round 8

6 recorded events


### User

_source line 87 · 2026-05-18T06:37:08.447533+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: "Statistically indistinguishable" claim 使用了错误的统计范式**

完全同意。Abstract (line 7)、Introduction (line 23)、Conclusion (line 2) 均使用 "statistically indistinguishable"，仅凭 bootstrap p=0.30 和 N=3。按 equivalence testing 标准（TOST），需预设 equivalence margin δ 并检验 |μ1 − μ2| < δ，论文从未定义过。N=3 统计功效极低。

补充：Table 1 的实际 gap（0.031 PPL, 0.18% relative）在实践意义上确实很小。论文可改为强调 practical equivalence，同时在 Limitations 中承认 N=3 局限。

---

**[AGREE] R1-N2: α_eff 理论动机与实际计算的逻辑断层**

同意两个层次：(a) 理论-实际 gap——Wang et al. (2026) 基于真实 α，但 α_eff 用 r_i = 1[q_i ≤ 0.5]（Method §3.2, line 23），detector 不完美时会系统性偏离真实 α，论文未给出误差界；(b) Proposition 1 tautological——r_i 是 q_i 的阈值函数，Cov_π(r_i, ln(1−q_i)) ≥ 0 是构造的直接结果，不是 detector 质量的深层性质。

---

**[AGREE] R1-N3: 实验外部效度严重不足**

完全同意，也是我独立审查的最严重问题。单一模型(0.6B)、单一数据源(FineWeb)、单一 detector(TF-IDF+LR)、自污染设计。Llama-3.2-3B 只有单 seed。ρ=0.2 失效无深入分析。论文 framing 暗示 general-purpose 但实验极窄。

---

### Should-Fix 问题

**[AGREE] R1-W1: Downstream benchmarks 未展示实际价值**

同意。Appendix Table 5 显示 4/5 benchmarks adaptive 低于 uniform（ARC-C −0.5pp, ARC-E −0.7pp, HellaSwag −0.5pp, WinoGrande −0.8pp），只有 PIQA +0.1pp。PPL 改善未转化为 downstream gains。

---

**[AGREE] R1-W2: Proposition 1 claims strictly increasing 但 proof 只建立 non-decreasing**

同意。Method §3.2 (line 46-47) 声称 "strictly increasing"，但 Appendix A (line 24) 的证明只建立 covariance "non-negative"。虽然前提 "with distinct q-values" 可能意在排除退化情况，但证明中未利用此条件建立 strict positivity。可修复的数学瑕疵。

---

**[REBUT] R1-W3: ESS monotonicity 未证明**

部分反驳。ESS 在 exponential tilting 下单调递减是 importance sampling 标准结果，论文引用了 Kimura et al. (2024) 综述。重新证明标准性质增加不必要篇幅。但建议提供具体 Lemma/Theorem 编号而非泛泛引用。

---

**[AGREE] R1-W4: Grid-b baseline post-hoc oracle 问题**

同意需要更充分讨论。但补充反向观察：实践中 grid search 需要独立 validation set（非 test set），因此 test-set-oracle grid-best 是 upper bound，实际 grid search 会更差。这反而有利于论文的 claim——adaptive 实际上可能优于 realistic grid search。建议论文增加此讨论。

---

**[AGREE] R1-W5: D&R 和 Golden Ratio 仅单 seed**

同意但严重程度有限。核心 claim（adaptive ≈ grid-best, adaptive > uniform）有 3-seed 支撑。

---

**[AGREE] R1-W6: 效应量实际意义不足**

同意。PPL 0.043（0.24%）+ downstream 无改善 = 实质贡献有限。论文应重新 frame 为 "消除 grid search 成本" 而非 "改善性能"。

---

### Questions 回应

**Q1 (soft indicator)**：有价值建议，r_i = 1 − q_i 使 α_eff 连续，可改善 N2 的理论-实际 gap。
**Q2 (ρ=0.2 低 τ)**：关键缺失实验。τ sweep 只在 ρ=0.4 进行。
**Q3 (训练 loss vs PPL)**：好问题。PPL 改善仅在 human-only eval 上——若 eval 是混合的，adaptive 是否还有优势？未回答。
**Q4 (B=4 方差)**：有效关切。B=4 时 α_eff 只有 5 个可能值 {0, 0.25, 0.5, 0.75, 1.0}，非常粗糙。
**Q5 (calibration hypothesis)**：同意未有实验支撑，但在 Abstract/Conclusion 中过于突出。

---

### Missing References 回应

**同意缺失**：Guo et al. (2017) temperature scaling（论文用了但未引）、Hans et al. (2024) Binoculars、equivalence testing 文献。引用验证发现 guo2025escaping 无 arXiv ID、vehtari2024psis 年份可能为 2015 非 2024。

**补充**：总引用 23 篇偏少（EMNLP 长文通常 40-60+）。缺 curriculum learning (Bengio 2009)、Focal loss (Lin 2017)、Fast-DetectGPT (Bao 2024)。正文 "five approaches" (Experiments line 20) 实际列出 6 个，typo。

---

### 总结

R1 审稿质量高。我在 13/15 个问题上同意，仅在 W3（ESS 单调性有文献支持）部分反驳，W4 补充有利于论文的反向观察。

核心问题共识：(1) N1+W6——效应量极小+统计框架错误导致核心 claim 不可靠；(2) N3——实验覆盖极窄但 framing 为 general-purpose。这两个问题的严重程度我与 R1 一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-18T06:39:00.027183+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "provenance_weight_training",
  "issues_yaml": "- id: \"RR-W1\"\n  summary: \"Paper claims 'from random initialization' but code uses from_pretrained() — actually continued pretraining\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [research_reviewer]\n      note: \"Two independent reviews confirmed: pretrain_weighted.py L318 uses from_pretrained(), model.safetensors 1.5GB = full pretrained weights\"\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Both reviewers confirm fixed: Abstract line 7, Introduction line 23, Experiments line 12 now say 'continued pretraining'\"\n  action_items:\n    - round: 1\n      action: \"Fix paper text: 'pretrain from random initialization' → 'continue pretraining Qwen3-0.6B'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 1\n      action: \"Run baseline PPL eval on untrained Qwen3-0.6B checkpoint to quantify absolute improvement\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Fixed in current version: Abstract, Introduction, Experiments all use 'continued pretraining'\"\n  resolution_round: 2\n\n- id: \"RR-W2\"\n  summary: \"Paper claims 'balanced real/synthetic test set' but eval_holdout.jsonl is human-only (FineWeb)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [research_reviewer]\n      note: \"eval_holdout.jsonl: 67823 lines, all source=fineweb depth=0, zero synthetic samples\"\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Both reviewers confirm fixed: Experiments line 16 now says 'containing only human-authored text'\"\n  action_items:\n    - round: 1\n      action: \"Fix paper text: 'balanced real/synthetic test set' → 'human-only test set drawn from FineWeb'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed in current version: Experiments section explicitly states human-only evaluation\"\n  resolution_round: 2\n\n- id: \"R1-N1\"\n  summary: \"'Statistically indistinguishable' claim uses failure-to-reject (p=0.30, N=3) instead of equivalence test (TOST)\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Full consensus. p=0.30 only means failure to reject H0, not evidence of equivalence. N=3 has extremely low statistical power. Absence of evidence ≠ evidence of absence. Appears in Abstract, Introduction line 23, Conclusion line 2.\"\n  action_items:\n    - round: 2\n      action: \"Either run TOST equivalence test with pre-specified δ, or downgrade claim to 'comparable PPL, gap not reaching significance at N=3'\"\n      assigned_to: research_director\n      status: pending\n    - round: 2\n      action: \"Consider increasing seed count to 5-10 for higher statistical power\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"α_eff theoretical motivation (Wang et al. 2026 true α) disconnected from actual computation (r_i = 1[q_i ≤ 0.5] estimated α); Proposition 1 covariance positivity is tautological\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Full consensus. Two issues: (a) Wang et al. convergence theorem uses true α but α_eff uses detector estimate, no error bound given; (b) r_i is threshold function of q_i, so Cov_π(r_i, ln(1−q_i)) ≥ 0 is by construction, not a property of detector quality.\"\n  action_items:\n    - round: 2\n      action: \"Explicitly discuss α_eff as estimated (not true) effective real proportion; report α_eff vs true α correlation in synthetic experiment\"\n      assigned_to: research_director\n      status: pending\n    - round: 2\n      action: \"Analyze how detector accuracy affects α_eff guarantees\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"Experimental external validity severely insufficient: single model (0.6B), single detector (TF-IDF+LR), single data source (FineWeb), self-contamination only, ρ=0.2 failure unanalyzed\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Full consensus (R1-N3, R2-N1, R2-W2). Drayson et al. tested 160M/360M/1.7B; this paper claims to improve on it but has far less experimental coverage. Llama-3.2-3B single seed shows PPL parity (no improvement), may suggest method doesn't scale. Self-contamination is easiest detection scenario.\"\n  action_items:\n    - round: 2\n      action: \"Add at least one 1-3B scale 3-seed experiment\"\n      assigned_to: research_director\n      status: pending\n    - round: 2\n      action: \"Add at least one neural detector comparison (e.g. ModernBERT) to test calibration hypothesis\"\n      assigned_to: research_director\n      status: pending\n    - round: 2\n      action: \"Analyze ρ=0.2 failure (likely τ=0.8 over-constraint at low contamination)\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"Hard filtering (Detect & Remove) crushes all reweighting methods (17.290 vs 17.651), undermining practical motivation for reweighting\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus (R1 agrees with nuance). Gap is 0.36 PPL (filtering vs adaptive) vs 0.043 (adaptive vs uniform). Threshold sensitivity (0.3→0.5 = 0.037 PPL) is far smaller than filtering vs reweighting gap. R1 adds that threshold direction is unknowable without validation, but agrees core argument stands.\"\n  action_items:\n    - round: 2\n      action: \"Test filtering at extreme thresholds (0.1, 0.9) to show where filtering breaks; or reposition paper as 'safe fallback when threshold calibration unavailable'\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W1\"\n  summary: \"Effect size tiny (0.043 PPL, 0.24% relative) with no downstream improvement (4/5 benchmarks slightly worse); framing mismatch with title/Abstract\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Full consensus (R1-W1, R1-W6, R2-N3). Appendix Table 5: ARC-C −0.5pp, ARC-E −0.7pp, HellaSwag −0.5pp, WinoGrande −0.8pp. Consistent direction suggests PPL gain may be implicit distribution matching to human-only eval set, not genuine quality improvement. R1 suggests re-framing as 'matching grid-search at zero validation cost'.\"\n  action_items:\n    - round: 2\n      action: \"Re-frame Abstract and Introduction: core contribution is 'principled exponent selection with comparable performance' not 'improved pretraining'\"\n      assigned_to: research_director\n      status: pending\n    - round: 2\n      action: \"Add larger-scale downstream evaluation or explicitly scope claims to PPL\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Proposition 1 claims strictly increasing but proof only establishes non-decreasing (covariance non-negative ≠ strictly positive)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. Fixable: tighten proof under 'distinct q-values' premise, or downgrade to non-decreasing.\"\n  action_items:\n    - round: 2\n      action: \"Tighten Proposition 1 proof to establish strict positivity under stated conditions, or relabel as non-decreasing\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"ESS monotonicity not formally proven; cited Kimura et al. (2024) is a survey without specific theorem reference\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Minor divergence: R1 says proof needed for bisection correctness; R2 says standard IS result, only needs specific citation. Both agree current citation is too vague.\"\n  action_items:\n    - round: 2\n      action: \"Add specific lemma/theorem reference for ESS monotonicity, or brief proof in Appendix\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4\"\n  summary: \"Grid-b baseline is post-hoc oracle (best selected on test set); unfair comparison not sufficiently discussed\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. R2 adds reverse observation: realistic grid search (val set selection) would perform worse than post-hoc oracle, actually favoring the paper's claim. Paper should discuss both directions.\"\n  action_items:\n    - round: 2\n      action: \"Add discussion of post-hoc oracle advantage; consider split-validation grid search baseline\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"Detect & Remove and Golden Ratio baselines reported only for seed 42; no multi-seed statistical comparison possible\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. At minimum D&R needs 3-seed replication given it is the strongest baseline.\"\n  action_items:\n    - round: 2\n      action: \"Run 3-seed experiments for Detect & Remove and Golden Ratio\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"Novelty relative to Drayson et al. is limited — core formula borrowed, dual constraint is standard IS technique in new context\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Divergence: R2 says mathematically trivial; R1 rebuts — ESS-only failure is counter-intuitive (17.737 > uniform 17.694), regime analysis (4.9× over-intervention) provides non-trivial insight. Both agree novelty is 'useful engineering insight' sufficient for Findings but not main conference.\"\n  action_items:\n    - round: 2\n      action: \"Clarify unique aspects of dual constraint in contamination-aware context vs general IS literature\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"τ depends on ρ (optimal τ shifts 0.8→0.7 from ρ=0.4→0.6; method fails at ρ=0.2), contradicting 'zero validation cost' and 'ρ unknown' claims\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus (R1 agrees with nuance). τ=[0.5,0.8] safe range is partial defense, but Discussion's τ≈1−ρ/2 heuristic directly contradicts ρ-unknown assumption. ρ=0.2 failure (+0.046 PPL) means method has effective lower bound.\"\n  action_items:\n    - round: 2\n      action: \"Remove τ≈1−ρ/2 heuristic or explicitly discuss contradiction; analyze τ sensitivity at ρ=0.2\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"Citation density insufficient: 23 references vs EMNLP norm of 40-60+; missing curriculum learning, focal loss, DRO, watermarking, more detectors, DataComp\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. High-priority additions: Sagawa et al. (2020) Group DRO, Hans et al. (2024) Binoculars, Bao et al. (2024) Fast-DetectGPT, Gadre et al. (2024) DataComp-LM, Guo et al. (2017) temperature scaling. Nice-to-have: Bengio (2009), Lin (2017), Kirchenbauer (2023).\"\n  action_items:\n    - round: 2\n      action: \"Add at least 15-20 additional references covering identified gaps\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-M1\"\n  summary: \"Experiments says 'five approaches' but lists 6 methods\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. Simple count error in experiments.tex line 20.\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-M2\"\n  summary: \"Grid-b values inconsistent: Section 4 lists 7 values, Section 5.1 says 'nine runs', Appendix Table 2 has 9 values\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. Section 4 lists {0.3,0.5,1.0,1.5,2.0,3.0,5.0} (7), Appendix adds 0.1 and 0.2 (9 total).\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-M3\"\n  summary: \"Reference issues: vehtari2024psis year may be wrong (2015 vs 2024), guo2025escaping missing arXiv ID and possibly phantom\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. guo2025escaping has highest risk — no online match found. vehtari2024psis may be correct if citing 2024 JMLR publication of 2015 preprint.\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-M5\"\n  summary: \"Hybrid method ρ=0.6 row in Appendix Table 4 not directly comparable but footnote easily missed\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. Hybrid changes effective ρ, making same-column comparison misleading.\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "provenance_weight_training",
    "issues_yaml": "- id: \"RR-W1\"\n  summary: \"Paper claims 'from random initialization' but code uses from_pretrained() — actually continued pretraining\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [research_reviewer]\n      note: \"Two independent reviews confirmed: pretrain_weighted.py L318 uses from_pretrained(), model.safetensors 1.5GB = full pretrained weights\"\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Both reviewers confirm fixed: Abstract line 7, Introduction line 23, Experiments line 12 now say 'continued pretraining'\"\n  action_items:\n    - round: 1\n      action: \"Fix paper text: 'pretrain from random initialization' → 'continue pretraining Qwen3-0.6B'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 1\n      action: \"Run baseline PPL eval on untrained Qwen3-0.6B checkpoint to quantify absolute improvement\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Fixed in current version: Abstract, Introduction, Experiments all use 'continued pretraining'\"\n  resolution_round: 2\n\n- id: \"RR-W2\"\n  summary: \"Paper claims 'balanced real/synthetic test set' but eval_holdout.jsonl is human-only (FineWeb)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [research_reviewer]\n      note: \"eval_holdout.jsonl: 67823 lines, all source=fineweb depth=0, zero synthetic samples\"\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Both reviewers confirm fixed: Experiments line 16 now says 'containing only human-authored text'\"\n  action_items:\n    - round: 1\n      action: \"Fix paper text: 'balanced real/synthetic test set' → 'human-only test set drawn from FineWeb'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed in current version: Experiments section explicitly states human-only evaluation\"\n  resolution_round: 2\n\n- id: \"R1-N1\"\n  summary: \"'Statistically indistinguishable' claim uses failure-to-reject (p=0.30, N=3) instead of equivalence test (TOST)\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Full consensus. p=0.30 only means failure to reject H0, not evidence of equivalence. N=3 has extremely low statistical power. Absence of evidence ≠ evidence of absence. Appears in Abstract, Introduction line 23, Conclusion line 2.\"\n  action_items:\n    - round: 2\n      action: \"Either run TOST equivalence test with pre-specified δ, or downgrade claim to 'comparable PPL, gap not reaching significance at N=3'\"\n      assigned_to: research_director\n      status: pending\n    - round: 2\n      action: \"Consider increasing seed count to 5-10 for higher statistical power\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"α_eff theoretical motivation (Wang et al. 2026 true α) disconnected from actual computation (r_i = 1[q_i ≤ 0.5] estimated α); Proposition 1 covariance positivity is tautological\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Full consensus. Two issues: (a) Wang et al. convergence theorem uses true α but α_eff uses detector estimate, no error bound given; (b) r_i is threshold function of q_i, so Cov_π(r_i, ln(1−q_i)) ≥ 0 is by construction, not a property of detector quality.\"\n  action_items:\n    - round: 2\n      action: \"Explicitly discuss α_eff as estimated (not true) effective real proportion; report α_eff vs true α correlation in synthetic experiment\"\n      assigned_to: research_director\n      status: pending\n    - round: 2\n      action: \"Analyze how detector accuracy affects α_eff guarantees\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"Experimental external validity severely insufficient: single model (0.6B), single detector (TF-IDF+LR), single data source (FineWeb), self-contamination only, ρ=0.2 failure unanalyzed\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Full consensus (R1-N3, R2-N1, R2-W2). Drayson et al. tested 160M/360M/1.7B; this paper claims to improve on it but has far less experimental coverage. Llama-3.2-3B single seed shows PPL parity (no improvement), may suggest method doesn't scale. Self-contamination is easiest detection scenario.\"\n  action_items:\n    - round: 2\n      action: \"Add at least one 1-3B scale 3-seed experiment\"\n      assigned_to: research_director\n      status: pending\n    - round: 2\n      action: \"Add at least one neural detector comparison (e.g. ModernBERT) to test calibration hypothesis\"\n      assigned_to: research_director\n      status: pending\n    - round: 2\n      action: \"Analyze ρ=0.2 failure (likely τ=0.8 over-constraint at low contamination)\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"Hard filtering (Detect & Remove) crushes all reweighting methods (17.290 vs 17.651), undermining practical motivation for reweighting\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus (R1 agrees with nuance). Gap is 0.36 PPL (filtering vs adaptive) vs 0.043 (adaptive vs uniform). Threshold sensitivity (0.3→0.5 = 0.037 PPL) is far smaller than filtering vs reweighting gap. R1 adds that threshold direction is unknowable without validation, but agrees core argument stands.\"\n  action_items:\n    - round: 2\n      action: \"Test filtering at extreme thresholds (0.1, 0.9) to show where filtering breaks; or reposition paper as 'safe fallback when threshold calibration unavailable'\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W1\"\n  summary: \"Effect size tiny (0.043 PPL, 0.24% relative) with no downstream improvement (4/5 benchmarks slightly worse); framing mismatch with title/Abstract\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Full consensus (R1-W1, R1-W6, R2-N3). Appendix Table 5: ARC-C −0.5pp, ARC-E −0.7pp, HellaSwag −0.5pp, WinoGrande −0.8pp. Consistent direction suggests PPL gain may be implicit distribution matching to human-only eval set, not genuine quality improvement. R1 suggests re-framing as 'matching grid-search at zero validation cost'.\"\n  action_items:\n    - round: 2\n      action: \"Re-frame Abstract and Introduction: core contribution is 'principled exponent selection with comparable performance' not 'improved pretraining'\"\n      assigned_to: research_director\n      status: pending\n    - round: 2\n      action: \"Add larger-scale downstream evaluation or explicitly scope claims to PPL\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Proposition 1 claims strictly increasing but proof only establishes non-decreasing (covariance non-negative ≠ strictly positive)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. Fixable: tighten proof under 'distinct q-values' premise, or downgrade to non-decreasing.\"\n  action_items:\n    - round: 2\n      action: \"Tighten Proposition 1 proof to establish strict positivity under stated conditions, or relabel as non-decreasing\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"ESS monotonicity not formally proven; cited Kimura et al. (2024) is a survey without specific theorem reference\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Minor divergence: R1 says proof needed for bisection correctness; R2 says standard IS result, only needs specific citation. Both agree current citation is too vague.\"\n  action_items:\n    - round: 2\n      action: \"Add specific lemma/theorem reference for ESS monotonicity, or brief proof in Appendix\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4\"\n  summary: \"Grid-b baseline is post-hoc oracle (best selected on test set); unfair comparison not sufficiently discussed\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. R2 adds reverse observation: realistic grid search (val set selection) would perform worse than post-hoc oracle, actually favoring the paper's claim. Paper should discuss both directions.\"\n  action_items:\n    - round: 2\n      action: \"Add discussion of post-hoc oracle advantage; consider split-validation grid search baseline\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"Detect & Remove and Golden Ratio baselines reported only for seed 42; no multi-seed statistical comparison possible\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. At minimum D&R needs 3-seed replication given it is the strongest baseline.\"\n  action_items:\n    - round: 2\n      action: \"Run 3-seed experiments for Detect & Remove and Golden Ratio\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"Novelty relative to Drayson et al. is limited — core formula borrowed, dual constraint is standard IS technique in new context\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Divergence: R2 says mathematically trivial; R1 rebuts — ESS-only failure is counter-intuitive (17.737 > uniform 17.694), regime analysis (4.9× over-intervention) provides non-trivial insight. Both agree novelty is 'useful engineering insight' sufficient for Findings but not main conference.\"\n  action_items:\n    - round: 2\n      action: \"Clarify unique aspects of dual constraint in contamination-aware context vs general IS literature\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"τ depends on ρ (optimal τ shifts 0.8→0.7 from ρ=0.4→0.6; method fails at ρ=0.2), contradicting 'zero validation cost' and 'ρ unknown' claims\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus (R1 agrees with nuance). τ=[0.5,0.8] safe range is partial defense, but Discussion's τ≈1−ρ/2 heuristic directly contradicts ρ-unknown assumption. ρ=0.2 failure (+0.046 PPL) means method has effective lower bound.\"\n  action_items:\n    - round: 2\n      action: \"Remove τ≈1−ρ/2 heuristic or explicitly discuss contradiction; analyze τ sensitivity at ρ=0.2\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"Citation density insufficient: 23 references vs EMNLP norm of 40-60+; missing curriculum learning, focal loss, DRO, watermarking, more detectors, DataComp\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. High-priority additions: Sagawa et al. (2020) Group DRO, Hans et al. (2024) Binoculars, Bao et al. (2024) Fast-DetectGPT, Gadre et al. (2024) DataComp-LM, Guo et al. (2017) temperature scaling. Nice-to-have: Bengio (2009), Lin (2017), Kirchenbauer (2023).\"\n  action_items:\n    - round: 2\n      action: \"Add at least 15-20 additional references covering identified gaps\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-M1\"\n  summary: \"Experiments says 'five approaches' but lists 6 methods\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. Simple count error in experiments.tex line 20.\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-M2\"\n  summary: \"Grid-b values inconsistent: Section 4 lists 7 values, Section 5.1 says 'nine runs', Appendix Table 2 has 9 values\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. Section 4 lists {0.3,0.5,1.0,1.5,2.0,3.0,5.0} (7), Appendix adds 0.1 and 0.2 (9 total).\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-M3\"\n  summary: \"Reference issues: vehtari2024psis year may be wrong (2015 vs 2024), guo2025escaping missing arXiv ID and possibly phantom\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. guo2025escaping has highest risk — no online match found. vehtari2024psis may be correct if citing 2024 JMLR publication of 2015 preprint.\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-M5\"\n  summary: \"Hybrid method ρ=0.6 row in Appendix Table 4 not directly comparable but footnote easily missed\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. Hybrid changes effective ρ, making same-column comparison misleading.\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-18T06:39:00.128315+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml\", \"bytes\": 14307}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-18T06:41:05.623443+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 圆桌审稿报告 — Round 2\n\n**论文**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\n**目标 Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**审稿编排**: 2 Reviewers, 1 round + cross-sharing\n**收敛状态**: 13/15 条意见达成共识，2 条轻微分歧（ESS 证明必要性、novelty 程度），无需额外轮次\n\n---\n\n## Summary\n\n本文提出双约束自适应指数选择框架，用于 detect-and-reweight 预训练中自动确定下权指数 $b^*$。给定 per-sample 检测器分数 $q(x)$，对每个 batch 求解满足 effective real proportion $\\alpha_{\\mathrm{eff}}(b) \\geq \\tau$ 且 ESS$(b) \\geq n_{\\min}$ 的最小 $b$（minimum intervention principle）。在 Qwen3-0.6B continued pretraining（132M tokens FineWeb, 40% 合成污染）上，方法与 grid-searched best 的 PPL 差距为 0.031（17.651 vs 17.620），消融层级（Adaptive < Uniform < ESS-only < Random）证实 detector 信号和 minimum intervention 两个因素均必要。\n\n---\n\n## Strengths\n\n**S1. 问题定义清晰且实际。** Web 数据合成污染是真实且日益严重的问题，无需验证集/已知 $\\rho$ 的自适应方法有实际需求。\n\n**S2. 框架设计简洁优雅。** $\\alpha_{\\mathrm{eff}}$ 和 ESS 的对立单调性自然定义 feasible region，bisection 求解高效（~44 FLOPs/batch），minimum intervention 直觉合理。\n\n**S3. 消融设计有层次且诚实。** 四级消融（Random > ESS-only > Uniform > Adaptive）有效分解因素贡献。固定 $\\bar{b}^*$ 实验（PPL ≈ uniform）进一步证明 per-batch adaptation 的必要性。Hard filtering 优势被坦诚报告。\n\n**S4. 超参敏感性分析全面。** $\\tau$ sweep（0.50-0.95）、$n_{\\min}$ sweep、batch size sweep ($B \\in \\{4,8,16\\}$) 均有覆盖。$\\tau \\in [0.5, 0.8]$ 宽 safe range 是实用性证据。\n\n**S5. 写作质量高。** 无 AI 写作痕迹（无 em-dash、无黑名单用词、无过度分段），叙事主线基本连贯，Limitations 诚实全面。\n\n**S6. 历史问题已修复。** RR-W1（\"from random initialization\" → \"continued pretraining\"）和 RR-W2（\"balanced test set\" → \"human-only\"）均已正确修正。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**C1. \"Statistically indistinguishable\" claim 基于错误的统计范式** [R1-N1, R2 AGREE]\n- 论文核心 claim（Abstract, Introduction, Conclusion）依据 bootstrap $p = 0.30$, $N = 3$。$p = 0.30$ 仅表示未能拒绝差异为零的零假设，不等于证明等价。$N = 3$ 统计功效极低——即使真实差异 0.5 PPL 也可能得到 $p > 0.05$。声称 \"indistinguishable\" 需要 equivalence test（如 TOST），预设实际等价边界 $\\delta$ 并证明差异落在 $[-\\delta, +\\delta]$ 内。当前表述是 absence of evidence ≠ evidence of absence 的统计推断错误。\n- **两位 Reviewer 完全一致。**\n\n**C2. $\\alpha_{\\mathrm{eff}}$ 理论动机与实际计算存在逻辑断层** [R1-N2, R2 AGREE]\n- 理论动机来自 Wang et al. (2026) 基于真实 $\\alpha$ 的收敛速率定理，但 $\\alpha_{\\mathrm{eff}}$ 用 $r_i = \\mathbf{1}[q_i \\leq 0.5]$ 估计——检测器不完美时（AUC = 0.939, 46.3% 样本在不确定区间 $[0.2, 0.8]$）会系统性偏离真实 $\\alpha$，论文未给出误差界。\n- Proposition 1 的 covariance 正性是 tautological：$r_i$ 是 $q_i$ 的阈值函数，$\\alpha_{\\mathrm{eff}}$ 增加是因为\"权重转移到检测器认为是真实的样本\"而非\"权重转移到真实样本\"。\n- **两位 Reviewer 完全一致。**\n\n**C3. 实验外部效度严重不足** [R1-N3, R2-N1, R2-W2, 全部 AGREE]\n- 单一模型规模（0.6B）、单一 detector（TF-IDF+LR）、单一数据源（FineWeb）、自污染设计（最容易检测的场景）。\n- Drayson et al. (2025) 在 160M/360M/1.7B 三个规模实验，本文声称改进其方法却实验覆盖远不如。\n- Llama-3.2-3B 单 seed 显示 PPL parity（无改善），暗示方法可能不 scale。\n- $\\rho = 0.2$ 失效（+0.046 PPL）无深入分析。$\\rho > 0.6$ 未测试。\n- Abstract 声称 \"score calibration may matter as much as raw classification accuracy\" 但未用任何其他检测器验证。\n- **两位 Reviewer 独立指出，全部一致。这是最严重的问题。**\n\n**C4. Hard filtering 碾压所有 reweighting 方法，削弱核心动机** [R2-N2, R1 AGREE with nuance]\n- Detect & Remove（17.290）比 Adaptive（17.651）低 0.36 PPL，差距远大于 Adaptive vs Uniform（0.043）。\n- 即使 suboptimal threshold（$q > 0.3$: 17.253, $q > 0.5$: 17.290）也全面优于所有 reweighting，threshold 敏感度（0.037 PPL）远小于 filtering vs reweighting 差距（0.36）。\n- R1 补充：threshold 方向不可知是 reweighting 的一个 defense，但论文未测试极端阈值，full robustness picture 缺失。\n- **基本一致，R1 同意核心论点但补充了 nuance。**\n\n**C5. 效果量极小且 downstream 无改善，framing 不匹配** [R1-W1, R1-W6, R2-N3, 全部 AGREE]\n- PPL 改善 0.043（0.24% relative）。Appendix Table 5 的 5 个 downstream benchmarks 中 4/5 adaptive 略低于 uniform（ARC-C -0.5pp, ARC-E -0.7pp, HellaSwag -0.5pp, WinoGrande -0.8pp），方向一致性令人担忧。\n- PPL 改善可能来自对 human-only evaluation set 的隐式 distribution matching，非真正的训练质量提升。\n- 论文标题和 Abstract 的 \"contamination-aware pretraining\" framing 暗示性能提升，但实际贡献更接近 \"消除 grid search 成本\"。\n- **两位 Reviewer 完全一致。**\n\n### Warning（影响评分但不一票否决）\n\n**W1. Proposition 1 证明 gap** [R1-W2, R2 AGREE]\n- 命题声称 strictly increasing，证明只建立 non-decreasing（covariance non-negative ≠ strictly positive）。可修复。\n\n**W2. ESS 单调性未正式证明** [R1-W3, R2 REBUT]\n- R1：对 bisection 算法正确性至关重要，应提供证明。\n- R2：标准 IS 结果，只需提供具体 lemma/theorem 引用。\n- **轻微分歧**：严重程度不一致，但都同意当前引用过于笼统。\n\n**W3. Grid-$b$ baseline 的 post-hoc oracle 问题** [R1-W4, R2 AGREE]\n- Grid-best 在 test set 上 post-hoc 选择，给了 oracle 优势。实践中 grid search 用 val set 选 $b$，test set 表现通常更差。\n- R2 补充：这反而有利于论文——realistic grid search 可能不如 adaptive。但论文应双向讨论。\n\n**W4. 重要 baselines 仅 single seed** [R1-W5, R2-W5, 全部 AGREE]\n- Detect & Remove（最强 baseline）和 Golden Ratio 仅 seed 42。至少 D&R 需要 3-seed。\n\n**W5. Novelty 相对 Drayson et al. 有限** [R2-W1, R1 REBUT]\n- R2：核心公式直接来自 Drayson, dual constraint 是标准 IS 技术在新场景的组合，数学上 trivial。\n- R1 反驳：ESS-only 失败是反直觉的（17.737 > uniform 17.694），regime analysis（4.9× over-intervention ratio）提供非平凡洞察。Novelty 属于 \"useful engineering insight backed by careful ablation\"。\n- **分歧**：novelty 程度判断不同，但都同意足以支撑 Findings。\n\n**W6. $\\tau$ 依赖 $\\rho$ 与 \"zero validation cost\" 矛盾** [R2-W3, R1 AGREE with nuance]\n- optimal $\\tau$ 从 0.8（$\\rho=0.4$）变为 0.7（$\\rho=0.6$），$\\rho=0.2$ 方法退化。\n- Discussion 的 $\\tau \\approx 1 - \\rho/2$ heuristic 与 $\\rho$-unknown 假设直接矛盾。\n- R1 补充：$\\tau \\in [0.5, 0.8]$ safe range 宽 0.3，default $\\tau = 0.8$ 在 $\\rho \\in [0.4, 0.6]$ 足够好。部分缓解但不消除矛盾。\n\n**W7. 引用密度不足** [R2-W4, R1 AGREE]\n- 23 篇引用，EMNLP 长文通常 40-60+。高优先级缺失：Sagawa et al. (2020) Group DRO, Hans et al. (2024) Binoculars, Bao et al. (2024) Fast-DetectGPT, Gadre et al. (2024) DataComp-LM, Guo et al. (2017) temperature scaling。\n\n### Minor\n\n- M1: \"five approaches\" 实际列 6 个方法（experiments.tex line 20）\n- M2: Grid-$b$ 值列表不一致（正文 7 个 vs Appendix 9 个 vs \"nine runs\"）\n- M3: `guo2025escaping` 缺 arXiv ID，可能为 phantom reference；`vehtari2024psis` 年份待核实\n- M4: Hybrid $\\rho=0.6$ 行数据可比性说明不足\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 完全一致：\n1. **统计 claim 错误**（C1）：必须修正 \"indistinguishable\" 表述\n2. **实验覆盖不足**（C3）：至少需要多模型/多 detector 实验才能支撑 general claims\n3. **效果量小 + downstream 无改善**（C5）：需要重新 framing\n4. **Hard filtering 优势明显**（C4）：需要更有力的 reweighting positioning\n5. **历史 issue 已修复**：RR-W1 和 RR-W2 均已正确修正\n6. **写作质量高**：无 AI 痕迹，Limitations 诚实\n\n## Reviewer Divergence [REBUT]\n\n1. **Novelty 程度**（W5）：R2 认为 mathematically trivial，R1 认为 ESS-only 失败的反直觉性和 regime analysis 有非平凡价值。不影响整体评估（都同意 Findings 水平）。\n2. **ESS 证明必要性**（W2）：R1 要求 formal proof，R2 认为标准结果只需精确引用。\n\n---\n\n## Questions for Authors\n\n1. 如果执行 TOST 等价检验（预设 $\\delta = 0.1$ PPL），当前 $N = 3$ 的数据是否能通过？如不能，需要多少 seeds？\n2. 在已知 ground truth 的合成实验中，$\\alpha_{\\mathrm{eff}}$ 与 true $\\alpha$ 的 correlation/误差是多少？\n3. 训练 loss 几乎不变但 PPL 改善——如果 evaluation set 包含合成样本，差异是否消失？（评估 human-only eval 的隐式 distribution matching 效应）\n4. $\\rho = 0.2$ 时用 $\\tau = 0.5$ 或 $\\tau = 0.6$ 是否恢复有效性？\n5. 将 $r_i$ 改为 soft indicator $r_i = 1 - q_i$ 对性能和理论保证的影响？\n6. micro-batch $B = 4$ 时 $\\alpha_{\\mathrm{eff}}$ 仅有 5 个离散值 $\\{0, 0.25, 0.5, 0.75, 1.0\\}$，per-batch $b^*$ 的噪声对训练稳定性有何影响？\n7. 什么具体场景下 practitioner 应该选择 reweighting 而非 hard filtering？请给出量化论据。\n\n---\n\n## Missing References\n\n**高优先级**（实质性遗漏）：\n- Guo et al. (2017) \"On Calibration of Modern Neural Networks\" — 论文用了 temperature scaling 但未引用\n- Sagawa et al. (2020) Group DRO — DoReMi 的理论基础，已引 DoReMi 但缺上游\n- Hans et al. (2024) \"Spotting LLMs with Binoculars\" — 直接相关的检测器\n- Bao et al. (2024) Fast-DetectGPT — 已引 DetectGPT 但缺后续改进\n- Gadre et al. (2024) DataComp-LM — 数据质量/选择基准\n\n**中优先级**：\n- Bengio et al. (2009) Curriculum Learning\n- Lin et al. (2017) Focal Loss\n- Kirchenbauer et al. (2023) Watermarking for LLMs\n- Abbas et al. (2023) SemDeDup\n- Equivalence testing 文献（如 Lakens 2017），若论文要保留 \"indistinguishable\" claim\n\n**引用验证问题**：\n- `guo2025escaping` 无 arXiv ID，在线搜索无匹配，疑似 phantom reference\n- `vehtari2024psis` 年份需核实（2024 JMLR 发表 vs 2015 原始预印本）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置，未请求。\n\n---\n\n## Overall Assessment\n\n**Score: weak reject (Findings borderline)**\n**Confidence: 4/5**\n\n两位 Reviewer 独立给出 3.0/5（Findings 水平），交叉分享后在所有 critical 问题上达成共识。\n\n**核心判断**：方法 formulation 干净、消融设计好、写作诚实，具备 Findings 论文的基本素质。但五个 critical 问题制约当前版本：(1) 核心统计 claim 基于错误范式，(2) 理论动机与实际计算脱节，(3) 实验仅覆盖单一极窄 setting，(4) hard filtering 全面碾压使 reweighting 动机不清，(5) 效果量极小且 downstream 无改善。\n\n**如果仅修正表述**（降级 claim、加入讨论、补引用），可作为 borderline Findings 投稿，但缺乏竞争力。\n\n**如果扩展实验**（至少 1-3B 规模 3-seed + 一个 neural detector + D&R 3-seed + $\\rho = 0.2$ 分析 + reposition framing），可望稳定在 Findings accept，有可能冲击主会议 borderline。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"statistically indistinguishable\" 必须替换（C1）\n- \"score calibration may matter as much as raw classification accuracy\" 无实验支撑，需降级或删除\n\n### Introduction\n- 从 contamination 问题切入、到 dual constraint、到实验证据，叙事线基本连贯\n- Contribution 列表中 \"statistically indistinguishable\" 需同步修改\n- 第三贡献（lightweight detector）更像实验观察而非方法贡献\n\n### Related Work\n- Positioning 准确，与 Drayson et al. 的三点差异表述清楚\n- 引用密度不足（W7），缺 Group DRO、更多检测器、calibration 文献\n- 需补充 curriculum learning / instance reweighting 经典文献\n\n### Method\n- Proposition 1：strictly increasing → non-decreasing 或加强证明（W1）\n- ESS 单调性需精确引用（W2）\n- $r_i = \\mathbf{1}[q_i \\leq 0.5]$ 与理论动机的 gap 需讨论（C2）\n- Algorithm 1 清晰可实现\n\n### Experimental Setup\n- \"five approaches\" → 6 个方法（M1）\n- Grid 值列表与 Appendix 不一致（M2）\n- 自污染设计局限需在正文（非仅 Limitations）讨论\n\n### Results\n- Table 1 的 \"indistinguishable\" claim 需修正（C1）\n- D&R 优势需更充分讨论（C4）\n- Grid-$b$ post-hoc oracle 需双向讨论（W3）\n\n### Discussion\n- $\\tau \\approx 1 - \\rho/2$ 与 $\\rho$-unknown 矛盾需解决（W6）\n- \"where the advantage manifests\" 段落暗示 PPL 改善来自 human-only eval 的 distribution matching——如果如此，应明确讨论\n\n### Limitations\n- 已覆盖大部分局限，诚实度高\n- $\\rho = 0.2$ 失效需更深入分析\n\n### References\n- 总量不足（23 → 建议 40+）\n- `guo2025escaping` 可疑，需核实或删除\n- `vehtari2024psis` 年份需核实",
  "project": "provenance_weight_training",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 圆桌审稿报告 — Round 2\n\n**论文**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\n**目标 Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**审稿编排**: 2 Reviewers, 1 round + cross-sharing\n**收敛状态**: 13/15 条意见达成共识，2 条轻微分歧（ESS 证明必要性、novelty 程度），无需额外轮次\n\n---\n\n## Summary\n\n本文提出双约束自适应指数选择框架，用于 detect-and-reweight 预训练中自动确定下权指数 $b^*$。给定 per-sample 检测器分数 $q(x)$，对每个 batch 求解满足 effective real proportion $\\alpha_{\\mathrm{eff}}(b) \\geq \\tau$ 且 ESS$(b) \\geq n_{\\min}$ 的最小 $b$（minimum intervention principle）。在 Qwen3-0.6B continued pretraining（132M tokens FineWeb, 40% 合成污染）上，方法与 grid-searched best 的 PPL 差距为 0.031（17.651 vs 17.620），消融层级（Adaptive < Uniform < ESS-only < Random）证实 detector 信号和 minimum intervention 两个因素均必要。\n\n---\n\n## Strengths\n\n**S1. 问题定义清晰且实际。** Web 数据合成污染是真实且日益严重的问题，无需验证集/已知 $\\rho$ 的自适应方法有实际需求。\n\n**S2. 框架设计简洁优雅。** $\\alpha_{\\mathrm{eff}}$ 和 ESS 的对立单调性自然定义 feasible region，bisection 求解高效（~44 FLOPs/batch），minimum intervention 直觉合理。\n\n**S3. 消融设计有层次且诚实。** 四级消融（Random > ESS-only > Uniform > Adaptive）有效分解因素贡献。固定 $\\bar{b}^*$ 实验（PPL ≈ uniform）进一步证明 per-batch adaptation 的必要性。Hard filtering 优势被坦诚报告。\n\n**S4. 超参敏感性分析全面。** $\\tau$ sweep（0.50-0.95）、$n_{\\min}$ sweep、batch size sweep ($B \\in \\{4,8,16\\}$) 均有覆盖。$\\tau \\in [0.5, 0.8]$ 宽 safe range 是实用性证据。\n\n**S5. 写作质量高。** 无 AI 写作痕迹（无 em-dash、无黑名单用词、无过度分段），叙事主线基本连贯，Limitations 诚实全面。\n\n**S6. 历史问题已修复。** RR-W1（\"from random initialization\" → \"continued pretraining\"）和 RR-W2（\"balanced test set\" → \"human-only\"）均已正确修正。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**C1. \"Statistically indistinguishable\" claim 基于错误的统计范式** [R1-N1, R2 AGREE]\n- 论文核心 claim（Abstract, Introduction, Conclusion）依据 bootstrap $p = 0.30$, $N = 3$。$p = 0.30$ 仅表示未能拒绝差异为零的零假设，不等于证明等价。$N = 3$ 统计功效极低——即使真实差异 0.5 PPL 也可能得到 $p > 0.05$。声称 \"indistinguishable\" 需要 equivalence test（如 TOST），预设实际等价边界 $\\delta$ 并证明差异落在 $[-\\delta, +\\delta]$ 内。当前表述是 absence of evidence ≠ evidence of absence 的统计推断错误。\n- **两位 Reviewer 完全一致。**\n\n**C2. $\\alpha_{\\mathrm{eff}}$ 理论动机与实际计算存在逻辑断层** [R1-N2, R2 AGREE]\n- 理论动机来自 Wang et al. (2026) 基于真实 $\\alpha$ 的收敛速率定理，但 $\\alpha_{\\mathrm{eff}}$ 用 $r_i = \\mathbf{1}[q_i \\leq 0.5]$ 估计——检测器不完美时（AUC = 0.939, 46.3% 样本在不确定区间 $[0.2, 0.8]$）会系统性偏离真实 $\\alpha$，论文未给出误差界。\n- Proposition 1 的 covariance 正性是 tautological：$r_i$ 是 $q_i$ 的阈值函数，$\\alpha_{\\mathrm{eff}}$ 增加是因为\"权重转移到检测器认为是真实的样本\"而非\"权重转移到真实样本\"。\n- **两位 Reviewer 完全一致。**\n\n**C3. 实验外部效度严重不足** [R1-N3, R2-N1, R2-W2, 全部 AGREE]\n- 单一模型规模（0.6B）、单一 detector（TF-IDF+LR）、单一数据源（FineWeb）、自污染设计（最容易检测的场景）。\n- Drayson et al. (2025) 在 160M/360M/1.7B 三个规模实验，本文声称改进其方法却实验覆盖远不如。\n- Llama-3.2-3B 单 seed 显示 PPL parity（无改善），暗示方法可能不 scale。\n- $\\rho = 0.2$ 失效（+0.046 PPL）无深入分析。$\\rho > 0.6$ 未测试。\n- Abstract 声称 \"score calibration may matter as much as raw classification accuracy\" 但未用任何其他检测器验证。\n- **两位 Reviewer 独立指出，全部一致。这是最严重的问题。**\n\n**C4. Hard filtering 碾压所有 reweighting 方法，削弱核心动机** [R2-N2, R1 AGREE with nuance]\n- Detect & Remove（17.290）比 Adaptive（17.651）低 0.36 PPL，差距远大于 Adaptive vs Uniform（0.043）。\n- 即使 suboptimal threshold（$q > 0.3$: 17.253, $q > 0.5$: 17.290）也全面优于所有 reweighting，threshold 敏感度（0.037 PPL）远小于 filtering vs reweighting 差距（0.36）。\n- R1 补充：threshold 方向不可知是 reweighting 的一个 defense，但论文未测试极端阈值，full robustness picture 缺失。\n- **基本一致，R1 同意核心论点但补充了 nuance。**\n\n**C5. 效果量极小且 downstream 无改善，framing 不匹配** [R1-W1, R1-W6, R2-N3, 全部 AGREE]\n- PPL 改善 0.043（0.24% relative）。Appendix Table 5 的 5 个 downstream benchmarks 中 4/5 adaptive 略低于 uniform（ARC-C -0.5pp, ARC-E -0.7pp, HellaSwag -0.5pp, WinoGrande -0.8pp），方向一致性令人担忧。\n- PPL 改善可能来自对 human-only evaluation set 的隐式 distribution matching，非真正的训练质量提升。\n- 论文标题和 Abstract 的 \"contamination-aware pretraining\" framing 暗示性能提升，但实际贡献更接近 \"消除 grid search 成本\"。\n- **两位 Reviewer 完全一致。**\n\n### Warning（影响评分但不一票否决）\n\n**W1. Proposition 1 证明 gap** [R1-W2, R2 AGREE]\n- 命题声称 strictly increasing，证明只建立 non-decreasing（covariance non-negative ≠ strictly positive）。可修复。\n\n**W2. ESS 单调性未正式证明** [R1-W3, R2 REBUT]\n- R1：对 bisection 算法正确性至关重要，应提供证明。\n- R2：标准 IS 结果，只需提供具体 lemma/theorem 引用。\n- **轻微分歧**：严重程度不一致，但都同意当前引用过于笼统。\n\n**W3. Grid-$b$ baseline 的 post-hoc oracle 问题** [R1-W4, R2 AGREE]\n- Grid-best 在 test set 上 post-hoc 选择，给了 oracle 优势。实践中 grid search 用 val set 选 $b$，test set 表现通常更差。\n- R2 补充：这反而有利于论文——realistic grid search 可能不如 adaptive。但论文应双向讨论。\n\n**W4. 重要 baselines 仅 single seed** [R1-W5, R2-W5, 全部 AGREE]\n- Detect & Remove（最强 baseline）和 Golden Ratio 仅 seed 42。至少 D&R 需要 3-seed。\n\n**W5. Novelty 相对 Drayson et al. 有限** [R2-W1, R1 REBUT]\n- R2：核心公式直接来自 Drayson, dual constraint 是标准 IS 技术在新场景的组合，数学上 trivial。\n- R1 反驳：ESS-only 失败是反直觉的（17.737 > uniform 17.694），regime analysis（4.9× over-intervention ratio）提供非平凡洞察。Novelty 属于 \"useful engineering insight backed by careful ablation\"。\n- **分歧**：novelty 程度判断不同，但都同意足以支撑 Findings。\n\n**W6. $\\tau$ 依赖 $\\rho$ 与 \"zero validation cost\" 矛盾** [R2-W3, R1 AGREE with nuance]\n- optimal $\\tau$ 从 0.8（$\\rho=0.4$）变为 0.7（$\\rho=0.6$），$\\rho=0.2$ 方法退化。\n- Discussion 的 $\\tau \\approx 1 - \\rho/2$ heuristic 与 $\\rho$-unknown 假设直接矛盾。\n- R1 补充：$\\tau \\in [0.5, 0.8]$ safe range 宽 0.3，default $\\tau = 0.8$ 在 $\\rho \\in [0.4, 0.6]$ 足够好。部分缓解但不消除矛盾。\n\n**W7. 引用密度不足** [R2-W4, R1 AGREE]\n- 23 篇引用，EMNLP 长文通常 40-60+。高优先级缺失：Sagawa et al. (2020) Group DRO, Hans et al. (2024) Binoculars, Bao et al. (2024) Fast-DetectGPT, Gadre et al. (2024) DataComp-LM, Guo et al. (2017) temperature scaling。\n\n### Minor\n\n- M1: \"five approaches\" 实际列 6 个方法（experiments.tex line 20）\n- M2: Grid-$b$ 值列表不一致（正文 7 个 vs Appendix 9 个 vs \"nine runs\"）\n- M3: `guo2025escaping` 缺 arXiv ID，可能为 phantom reference；`vehtari2024psis` 年份待核实\n- M4: Hybrid $\\rho=0.6$ 行数据可比性说明不足\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 完全一致：\n1. **统计 claim 错误**（C1）：必须修正 \"indistinguishable\" 表述\n2. **实验覆盖不足**（C3）：至少需要多模型/多 detector 实验才能支撑 general claims\n3. **效果量小 + downstream 无改善**（C5）：需要重新 framing\n4. **Hard filtering 优势明显**（C4）：需要更有力的 reweighting positioning\n5. **历史 issue 已修复**：RR-W1 和 RR-W2 均已正确修正\n6. **写作质量高**：无 AI 痕迹，Limitations 诚实\n\n## Reviewer Divergence [REBUT]\n\n1. **Novelty 程度**（W5）：R2 认为 mathematically trivial，R1 认为 ESS-only 失败的反直觉性和 regime analysis 有非平凡价值。不影响整体评估（都同意 Findings 水平）。\n2. **ESS 证明必要性**（W2）：R1 要求 formal proof，R2 认为标准结果只需精确引用。\n\n---\n\n## Questions for Authors\n\n1. 如果执行 TOST 等价检验（预设 $\\delta = 0.1$ PPL），当前 $N = 3$ 的数据是否能通过？如不能，需要多少 seeds？\n2. 在已知 ground truth 的合成实验中，$\\alpha_{\\mathrm{eff}}$ 与 true $\\alpha$ 的 correlation/误差是多少？\n3. 训练 loss 几乎不变但 PPL 改善——如果 evaluation set 包含合成样本，差异是否消失？（评估 human-only eval 的隐式 distribution matching 效应）\n4. $\\rho = 0.2$ 时用 $\\tau = 0.5$ 或 $\\tau = 0.6$ 是否恢复有效性？\n5. 将 $r_i$ 改为 soft indicator $r_i = 1 - q_i$ 对性能和理论保证的影响？\n6. micro-batch $B = 4$ 时 $\\alpha_{\\mathrm{eff}}$ 仅有 5 个离散值 $\\{0, 0.25, 0.5, 0.75, 1.0\\}$，per-batch $b^*$ 的噪声对训练稳定性有何影响？\n7. 什么具体场景下 practitioner 应该选择 reweighting 而非 hard filtering？请给出量化论据。\n\n---\n\n## Missing References\n\n**高优先级**（实质性遗漏）：\n- Guo et al. (2017) \"On Calibration of Modern Neural Networks\" — 论文用了 temperature scaling 但未引用\n- Sagawa et al. (2020) Group DRO — DoReMi 的理论基础，已引 DoReMi 但缺上游\n- Hans et al. (2024) \"Spotting LLMs with Binoculars\" — 直接相关的检测器\n- Bao et al. (2024) Fast-DetectGPT — 已引 DetectGPT 但缺后续改进\n- Gadre et al. (2024) DataComp-LM — 数据质量/选择基准\n\n**中优先级**：\n- Bengio et al. (2009) Curriculum Learning\n- Lin et al. (2017) Focal Loss\n- Kirchenbauer et al. (2023) Watermarking for LLMs\n- Abbas et al. (2023) SemDeDup\n- Equivalence testing 文献（如 Lakens 2017），若论文要保留 \"indistinguishable\" claim\n\n**引用验证问题**：\n- `guo2025escaping` 无 arXiv ID，在线搜索无匹配，疑似 phantom reference\n- `vehtari2024psis` 年份需核实（2024 JMLR 发表 vs 2015 原始预印本）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置，未请求。\n\n---\n\n## Overall Assessment\n\n**Score: weak reject (Findings borderline)**\n**Confidence: 4/5**\n\n两位 Reviewer 独立给出 3.0/5（Findings 水平），交叉分享后在所有 critical 问题上达成共识。\n\n**核心判断**：方法 formulation 干净、消融设计好、写作诚实，具备 Findings 论文的基本素质。但五个 critical 问题制约当前版本：(1) 核心统计 claim 基于错误范式，(2) 理论动机与实际计算脱节，(3) 实验仅覆盖单一极窄 setting，(4) hard filtering 全面碾压使 reweighting 动机不清，(5) 效果量极小且 downstream 无改善。\n\n**如果仅修正表述**（降级 claim、加入讨论、补引用），可作为 borderline Findings 投稿，但缺乏竞争力。\n\n**如果扩展实验**（至少 1-3B 规模 3-seed + 一个 neural detector + D&R 3-seed + $\\rho = 0.2$ 分析 + reposition framing），可望稳定在 Findings accept，有可能冲击主会议 borderline。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"statistically indistinguishable\" 必须替换（C1）\n- \"score calibration may matter as much as raw classification accuracy\" 无实验支撑，需降级或删除\n\n### Introduction\n- 从 contamination 问题切入、到 dual constraint、到实验证据，叙事线基本连贯\n- Contribution 列表中 \"statistically indistinguishable\" 需同步修改\n- 第三贡献（lightweight detector）更像实验观察而非方法贡献\n\n### Related Work\n- Positioning 准确，与 Drayson et al. 的三点差异表述清楚\n- 引用密度不足（W7），缺 Group DRO、更多检测器、calibration 文献\n- 需补充 curriculum learning / instance reweighting 经典文献\n\n### Method\n- Proposition 1：strictly increasing → non-decreasing 或加强证明（W1）\n- ESS 单调性需精确引用（W2）\n- $r_i = \\mathbf{1}[q_i \\leq 0.5]$ 与理论动机的 gap 需讨论（C2）\n- Algorithm 1 清晰可实现\n\n### Experimental Setup\n- \"five approaches\" → 6 个方法（M1）\n- Grid 值列表与 Appendix 不一致（M2）\n- 自污染设计局限需在正文（非仅 Limitations）讨论\n\n### Results\n- Table 1 的 \"indistinguishable\" claim 需修正（C1）\n- D&R 优势需更充分讨论（C4）\n- Grid-$b$ post-hoc oracle 需双向讨论（W3）\n\n### Discussion\n- $\\tau \\approx 1 - \\rho/2$ 与 $\\rho$-unknown 矛盾需解决（W6）\n- \"where the advantage manifests\" 段落暗示 PPL 改善来自 human-only eval 的 distribution matching——如果如此，应明确讨论\n\n### Limitations\n- 已覆盖大部分局限，诚实度高\n- $\\rho = 0.2$ 失效需更深入分析\n\n### References\n- 总量不足（23 → 建议 40+）\n- `guo2025escaping` 可疑，需核实或删除\n- `vehtari2024psis` 年份需核实",
    "project": "provenance_weight_training",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject"
  }
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-18T06:41:10.039669+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2b6c9bea33a70c93bf4bf04ac36b8df9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4416
}
```

</details>

---


### Assistant

_source line 92 · 2026-05-18T06:41:18.360540+00:00_

圆桌审稿完成。

**审稿结果：weak reject (Findings borderline)**

两位 Reviewer 独立给出 3.0/5，交叉分享后在所有 critical 问题上达成共识：

1. **C1** "statistically indistinguishable" 基于错误的统计范式（failure-to-reject ≠ equivalence）
2. **C2** $\alpha_{\mathrm{eff}}$ 理论动机与实际计算脱节（真实 $\alpha$ vs 检测器估计）
3. **C3** 实验外部效度严重不足（单一模型/detector/数据源/自污染）
4. **C4** Hard filtering 全面碾压 reweighting（0.36 PPL 差距）
5. **C5** 效果量极小（0.04 PPL）且 downstream 无改善，framing 不匹配

优势方面：框架简洁、消融设计好、写作诚实无 AI 痕迹、历史 issue 已修复。

报告已投递给 Research Director，Issue Tracker 已同步更新（2 resolved + 17 new issues）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 9

## Round 9

2 recorded events


### User

_source line 93 · 2026-05-18T06:41:21.068381+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Director。

总结：在 R1 提出的 15 个具体问题中，我同意 13 个（含全部 3 个 Must-Fix），仅在 W3（ESS 单调性）上部分反驳，W4 补充了一个有利于论文的反向观察（grid-best 是 test-set oracle，实际 grid search 会更差）。核心共识聚焦在两个问题：(1) "indistinguishable" claim 的统计基础有缺陷；(2) 实验覆盖度与论文 general-purpose framing 不匹配。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 94 · 2026-05-18T06:41:32.554298+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结**：

- **编排**：2 Reviewers，1 轮独立初审 + 交叉分享，关键问题高度收敛（13/15 AGREE），无需额外轮次
- **评分**：R1 3.0/5, R2 3.0/5，综合 **weak reject (Findings borderline)**
- **5 个 Critical 问题**：统计 claim 范式错误、α_eff 理论-实际断层、实验外部效度不足、hard filtering 碾压、效果量极小
- **7 个 Warning**：Proposition 1 证明 gap、ESS 单调性引用不足、grid-b oracle 问题、baselines 单 seed、novelty 有限、τ-ρ 矛盾、引用密度不足
- **历史 Issue**：RR-W1 和 RR-W2 均已修复
- **Issue Tracker** 已同步更新（17 条新 issue + 2 条旧 issue 标记 resolved）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 10

## Round 10

72 recorded events


### User

_source line 95 · 2026-05-19T04:28:54.444019+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: provenance_weight_training
- 论文路径: projects/provenance_weight_training/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-19T04:29:00.376537+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-19T04:29:00.427578+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-19T04:29:03.489976+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 99 · 2026-05-19T04:29:03.590780+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-19T04:29:08.365353+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-19T04:29:09.269357+00:00_

{"result":"# 项目 provenance_weight_training 概况\n\n## 实验状态 (175 个)\n\n- **adaptive_seed42**: DONE (success) — \n- **uniform_seed456**: DONE (success) — \n- **uniform_seed123**: DONE (success) — \n- **uniform_seed42**: DONE (success) — \n- **detector_modernbert**: DONE (killed) — \n- **nmin1_seed42**: DONE (success) — \n- **golden_ratio_seed42**: DONE (success) — \n- **tau_0.6_seed42**: DONE (killed) — \n- **grid_b_low_seed42**: DONE (failed) — \n- **grid_b1_5_seed456**: DONE (success) — \n- **grid_b1_0_seed456**: DONE (success) — \n- **grid_b0_5_seed456**: DONE (success) — \n- **grid_b_seed42_batch**: DONE (success) — \n- **diagnostic_contamination100**: DONE (killed) — \n- **detector_tfidf_lr**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- eval_q04（准备中）\n- eval_q06（准备中）\n- eval_q03_r2（准备中）\n- adaptive_1_7b_planb_control（准备中）\n- eval_q01_final_v2（准备中）\n- eval_q01_final（准备中）\n- eval_ngram_uniform（准备中）\n- eval_ngram_adaptive（准备中）\n- status_check_41312（准备中）\n- eval_adaptive_1_7b（准备中）\n- …另有 14 项\n\n## 近期结论\n- **uniform_1_7b_seed123** (negative): From-scratch uniform baseline at 1.7B scale with seed123, paired with adaptive_1_7b_seed123, to provide unconfounded comparison (unlike seed42 Plan B which had optimizer resume artifact)\n  [uniform_1_7b_seed123_analysis](/api/workspace-files/projects/provenance_weight_training/artifacts/uniform_1_7b_seed123/report/analysis_d8d0e9.md)\n- **detect_remove_q07_epoch_matched_seed42** (success): Epoch-matched D&R q07: 1 epoch through q07 filtered data (184,908 samples, ~100M tokens, 3047 steps). Part of 5-point epoch-matched curve (q01/q03/q05/q07/q09). If PPL converges to ~17.65-17.74 range like q03(17.74) and q05(17.65), confirms U-shape sweet spot is entirely multi-epoch artifact across the full threshold range.\n  [diagnose_q07_epoch_matched](/api/workspace-files/projects/provenance_weight_training/artifacts/detect_remove_q07_epoch_matched_seed42/report/dia
…[truncated 1800 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-19T04:29:09.771726+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-19T04:29:10.173984+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\graphicspath{{../../artifacts/figures/}}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{algorithm}
14	\usepackage{algorithmic}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{hyperref}
20	
21	\newtheorem{proposition}{Proposition}
22	\newtheorem{definition}{Definition}
23	
24	\newcommand{\bstar}{b^*}
25	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
26	\newcommand{\nmin}{n_{\min}}
27	\newcommand{\btau}{b_{\tau}}
28	\newcommand{\bess}{b_{\mathrm{ESS}}}
29	
30	\title{Minimum Intervention Reweighting: Adaptive Exponent Selection\\for Contamination-Aware Pretraining}
31	
32	\author{Anonymous}
33	
34	\begin{document}
35	\maketitle
36	
37	\begin{abstract}
38	\input{sections/abstract}
39	\end{abstract}
40	
41	\section{Introduction}
42	\label{sec:intro}
43	\input{sections/introduction}
44	
45	\section{Related Work}
46	\label{sec:related}
47	\input{sections/related_work}
48	
49	\section{Method}
50	\label{sec:method}
51	\input{sections/method}
52	
53	\section{Experimental Setup}
54	\label{sec:experiments}
55	\input{sections/experiments}
56	
57	\section{Results}
58	\label{sec:results}
59	\input{sections/results}
60	
61	\section{Discussion}
62	\label{sec:discussion}
63	\input{sections/discussion}
64	
65	\section{Conclusion}
66	\label{sec:conclusion}
67	\input{sections/conclusion}
68	
69	\section*{Limitations}
70	\label{sec:limitations}
71	\input{sections/limitations}
72	
73	\bibliography{references}
74	
75	\appendix
76	\input{sections/appendix}
77	
78	\end{document}
79	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-19T04:29:10.174328+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__read_local_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__read_local_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-19T04:29:10.224757+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-19T04:29:16.098979+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 107 · 2026-05-19T04:29:16.651221+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "literature_map.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "literature_map.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-19T04:29:17.605017+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool call

_source line 109 · 2026-05-19T04:29:19.060650+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_external_review_status",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_external_review_status",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 110 · 2026-05-19T04:29:23.483375+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"}]

Based on the search results, here's the key information about EMNLP 2026 call for papers:

## Submission Deadline

The ARR submission deadline for long and short papers is May 25, 2026.

## Author Guidelines

EMNLP 2026 uses the ACL Rolling Review (ARR) system for paper s
…[truncated 1420 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 7384
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-19T04:29:23.534930+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/literature_map.yaml\", \"content\": \"# Literature Map for provenance_weight_training\\n# 研究方向：基于收敛理论的自适应污染重加权\\n# 核心公式：w=(1-q)^b，q 为检测器合成概率，b* 为理论最优权重指数\\n# 更新日期：2026-05-16（文献验证：新增 6 篇 high-priority 论文，全部经 arXiv/venue 交叉验证）\\n\\n# ============================================================\\n# Category: direct-competitor\\n# 同主题/同方法的论文\\n# ============================================================\\n\\n- id: drayson_2025_detection_collapse\\n  title: \\\"Machine-Generated Text Detection Prevents Language Model Collapse\\\"\\n  authors: \\\"George Drayson, Emine Yilmaz, Vasileios Lampos\\\"\\n  venue: \\\"EMNLP 2025\\\"\\n  year: 2025\\n  arxiv_id: \\\"2502.15654\\\"\\n  url: \\\"https://arxiv.org/abs/2502.15654\\\"\\n  github: \\\"https://github.com/GeorgeDrayson/model_collapse\\\"\\n  category: direct-competitor\\n  role: \\\"使用同一公式 w=(1-q)^b 进行重加权，但 b 为验证集 empirical 选取，训练中固定\\\"\\n  method_summary: >\\n    Detect-and-reweight 防止递归训练 model collapse。检测器为 ModernBERT 150M\\n    (MAGE fine-tune, in-domain AUC=0.986, OOD AUC=0.943)。权重公式 wⱼ=(1-q(xⱼ))^b / Σₗ(1-q(xₗ))^b，\\n    通过 SIR 按权重重采样训练数据。b 通过 WikiText-2 验证集上 1 代递归训练后评估选取\\n    (GPT-2/SmolLM 135M/360M 用 b=10, SmolLM 1.7B 用 b=1)，训练全程固定。\\n    实验覆盖 4 个模型 (GPT-2 124M, SmolLM 135M/360M/1.7B)、10 代递归训练、6 种解码策略。\\n    结果 PPL 降低 0.85%–25.65%，diversity 提升 3.44%–14.62%。\\n  key_findings: \\\"验证 detect-and-reweight 有效防止 model collapse 且优于纯人类数据训练；b 值对模型规模敏感（小模型 b=10，大模型 b=1）\\\"\\n  differentiation:\\n    b_selection: \\\"Drayson: 验证集 empirical grid search, per-model 固定 | 我们: α_eff(b) + ESS 约束, per-batch 自适应\\\"\\n    contamination_setting: \\\"Drayson: 不假设已知比例（原文明确声明），但实验为控制设置 | 我们: 未知比例（batch 统计量在线估计）\\\"\\n    detector: \\\"Drayson: ModernBERT 150M (AUC=0.986) | 我们: TF-IDF+LR (AUC=0.939)，证明轻量检测器即可\\\"\\n    theory: \\\"Drayson: 无 b 选取理论（SIR 启发式） | 我们: 收敛理论 motivated α_eff(b) 推导\\\"\\n 
…[truncated 3804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6883
}
```

</details>

---


### Tool result

_source line 112 · 2026-05-19T04:29:23.535399+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 4474
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-19T04:29:23.535694+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 5930
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-19T04:29:30.075038+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-19T04:29:30.577326+00:00_

1	Web corpora now contain an estimated 20--60\% machine-generated text, and training on such contaminated data risks model collapse.
2	Detect-and-reweight methods suppress likely-synthetic samples via $w(x) = (1-q(x))^b$, but the exponent $b$ critically determines outcomes and requires per-model grid search (typically multiple complete training runs) to tune.
3	
4	We propose a dual-constrained adaptive exponent $b^*$ derived per-batch from detector scores alone: find the minimum $b$ such that the weighted effective real proportion $\alpha_{\mathrm{eff}}(b) \geq \tau$ (quality floor), subject to $\mathrm{ESS}(b) \geq n_{\min}$ (stability ceiling).
5	This minimum intervention principle applies only as much downweighting as needed, with zero validation cost.
6	
7	On Qwen3-0.6B continued pretraining (132M FineWeb tokens, 40\% synthetic contamination), adaptive $b^*$ achieves PPL competitive with the grid-searched optimum (3-seed means: 17.651 vs.\ 17.620, 95\% CI of gap $[-0.039, 0.101]$) while reducing the search cost from nine training runs to one.
8	A complete ablation confirms that both detector signal and minimum intervention are necessary: random reweighting degrades performance (17.803), ESS-only maximum intervention provides no improvement (17.737 vs.\ uniform 17.694), and only the dual-constrained method improves.
9	The advantage extends to $\rho{=}0.6$ (3-seed $\Delta{=}{-}0.027$, $p{<}0.01$) and transfers to 1.7B parameters without degradation ($\Delta{=}{-}0.01$).
10	An epoch-matched control (3 seeds) shows that hard filtering (Detect \& Remove) achieves equivalent PPL to adaptive $b^*$ when content epochs are equalized ($\Delta{=}0.006$, within seed variance); D\&R's apparent advantage at full training length is entirely attributable to multi-epoch exposure on the filtered subset.
11	The quality threshold $\tau$ is robust across $[0.5, 0.8]$, and detector type matters more than AUC: a discriminative detector (TF-IDF+LR, AUC\,=\,0.94) produces consistent gai
…[truncated 286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-19T04:29:30.577765+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-19T04:29:31.029951+00:00_

1	Web corpora increasingly contain machine-generated text.
2	Recent estimates place the synthetic fraction at 20--60\% of crawled data~\citep{cheng2025contamination}, and this share grows as language models are deployed for content production at scale.
3	Training on such contaminated data has concrete consequences: \citet{shumailov2024model} show that recursive training on model outputs leads to irreversible quality degradation (\emph{model collapse}), and \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger this failure mode, ruling out data scaling as a remedy.
4	A central difficulty is that the contamination proportion in any given corpus is unknown: synthetic text enters through diverse, uncoordinated channels with no centralized provenance record.
5	The prevalence, severity, and opacity of synthetic contamination make contamination-aware pretraining a practical necessity.
6	
7	A natural response is \emph{detect-and-reweight}: suppress likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a classifier's synthetic probability estimate.
8	However, the exponent $b$ critically determines outcomes and requires per-model validation-set grid search~\citep{drayson2025detection}; alternative approaches require the exact contamination ratio~\citep{he2025golden} or a well-calibrated detection threshold for hard filtering~\citep{feng2025beyond}.
9	
10	Given per-sample detector scores $q(x)$, how should one choose $b$ without a validation set or known contamination proportion?
11	We formulate this as a dual-constrained optimization over each training batch: find the smallest $b$ that ensures the weighted effective real proportion $\aeff(b)$ reaches a quality threshold $\tau$, while keeping Kish's effective sample size $\mathrm{ESS}(b)$ above a stability floor $\nmin$.
12	The quality constraint has theoretical grounding: convergence rate under contaminated training improves with the effec
…[truncated 3151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-19T04:29:31.080574+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-19T04:29:31.533008+00:00_

1	\subsection{Problem Setup}
2	\label{sec:setup}
3	
4	Let $\mathcal{D} = \mathcal{D}_{\mathrm{real}} \cup \mathcal{D}_{\mathrm{synth}}$ denote a pretraining corpus containing both human-authored and machine-generated text.
5	The contamination ratio $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$ is unknown, a realistic assumption for web-scale corpora where synthetic content enters from diverse, uncoordinated sources~\citep{cheng2025contamination}.
6	
7	A pre-trained detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$.
8	Following \citet{drayson2025detection}, we weight each sample as
9	\begin{equation}
10	  w(x) = (1 - q(x))^{b},
11	  \label{eq:weight}
12	\end{equation}
13	where $b \geq 0$ controls downweighting intensity: $b = 0$ recovers uniform training, while larger $b$ progressively suppresses high-$q$ samples.
14	\citet{drayson2025detection} select $b$ via validation-set grid search, obtaining different optimal values for different model scales ($b{=}10$ for ${\leq}360$M parameters, $b{=}1$ for 1.7B).
15	We instead derive $b$ per-batch from the batch's own $q$-score distribution, requiring no held-out validation data.
16	
17	\subsection{Dual-Constraint Framework}
18	\label{sec:dual}
19	
20	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with detector scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$, we define two batch-level diagnostics that jointly determine $b$.
21	
22	\paragraph{Effective real proportion.}
23	Let $r_i = \mathbf{1}[q_i \leq 0.5]$ estimate whether sample $x_i$ is human-authored.
24	The \emph{effective real proportion}
25	\begin{equation}
26	  \alpha_{\mathrm{eff}}(b) = \frac{\sum_{i=1}^{B} w_i(b) \cdot r_i}{\sum_{i=1}^{B} w_i(b)}
27	  \label{eq:alpha}
28	\end{equation}
29	measures the share of total weight allocated to likely-real samples.
30	The indicator $r_i = \mathbf{1}[q_i \leq 0.5]$ is a proxy for true provenance: $\alpha_{\mathrm{eff}}$ tracks the detector's estimate of the real fraction, not
…[truncated 9052 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-19T04:29:31.533362+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-19T04:29:31.985426+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.
5	\citet{cheng2025contamination} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\% of web corpora.
6	As language models are deployed at scale for content generation~\citep{radford2019language,brown2020language,openai2023gpt4}, these results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
7	
8	\paragraph{Detection and Filtering of Machine-Generated Text.}
9	Given the severity of contamination, a natural response is to detect and remove synthetic content.
10	DetectGPT~\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature; Fast-DetectGPT~\citep{bao2024fastdetectgpt} accelerates this with conditional probability curvature; Binoculars~\citep{hans2024binoculars} uses cross-perplexity ratios between two models; Min-$k$\% Prob~\citep{shi2024minkprob} uses the average log-probability of the lowest-$k$\% tokens.
11	All produce continuous confidence scores suitable as input to downstream weighting, including ours.
12	\citet{kirchenbauer2023watermark} propose watermarking as a complementary provenance mechanism.
13	On the mitigation side, \citet{feng2025beyond} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples.
14	Hard filter
…[truncated 4428 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-19T04:29:31.985888+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-19T04:29:32.940217+00:00_

1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo2024fineweb} as the real-data source.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang2025qwen3}, the same architecture used for continued pretraining, and inject them at token-level ratio $\rho = 0.4$ via uniform random mixing.\footnote{$\rho$ denotes the token-level contamination ratio. Because synthetic documents are shorter on average (304 vs.\ 560 words), the document-level synthetic fraction is 55.6\% at $\rho{=}0.4$.}
4	This self-contamination design creates a challenging detection scenario where generator and trainee share the same distribution.
5	
6	\paragraph{Detector.}
7	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split (AUC\,=\,0.939, calibrated ECE\,=\,0.048 after temperature scaling with $T = 0.204$).
8	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
9	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson2025detection}) to test whether score \emph{calibration} may matter as much as raw discrimination for reweighting.
10	To evaluate detector sensitivity, we additionally test two generative baselines: a GPT-2-based perplexity scorer (AUC\,=\,0.913) and an N-gram language model perplexity scorer (AUC\,=\,0.73); results are reported in \S\ref{sec:robustness}.
11	
12	\paragraph{Training.}
13	We continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\,=\,$5{\times}10^{-5}$), max sequence length 2048, and bf16 precision.
14	All main comparisons use three random seeds (42, 123, 456).
15	
16	\paragraph{Evaluation.}
17	We report held-out perplexity (PPL) on a held-out subset of FineWeb (67.8K documents, $\sim$4M toke
…[truncated 1412 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-19T04:29:32.940740+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-19T04:29:33.443201+00:00_

1	\subsection{Main Results}
2	\label{sec:main-results}
3	
4	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across three seeds.
5	Continued pretraining reduces PPL from 22.970 (pretrained checkpoint) to the 17.3--17.8 range; the initial 5.2-point drop absorbs the bulk of easy gains, and reweighting method comparisons operate within a narrow residual.
6	
7	Adaptive $\bstar$ achieves PPL competitive with grid-best: 3-seed means 17.651 vs.\ 17.620 for grid $b{=}0.3$ (gap 0.031, 95\% CI $[-0.039, 0.101]$).
8	With only $N{=}3$ seeds, this interval is too wide for formal equivalence testing; we refrain from claiming statistical indistinguishability and instead emphasize the practical value: the adaptive method requires one training run instead of nine~\citep{drayson2025detection}, with lower cross-seed variance ($\pm$0.007 vs.\ $\pm$0.033).
9	Using the mean of per-batch $\bstar$ ($\bar{b}^*{=}1.19$) as a fixed exponent yields PPL 17.693, comparable to uniform (17.694); per-batch adaptation is essential.
10	
11	The ablation hierarchy at $\rho{=}0.4$ (Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random, Table~\ref{tab:main}) reveals two requirements for effective reweighting: detector signal and minimum intervention.
12	Random weights $\mathcal{U}(0,2)$ (mean 17.803) perform worse than uniform (17.694): the detector's $q$-scores carry genuine provenance information, and uninformed reweighting increases gradient variance without corrective signal.
13	ESS-only (mean $17.737 {\pm} 0.021$) uses $q$-scores but maximizes $b$ up to the stability ceiling, concentrating weights on a few high-confidence samples; it provides no improvement over uniform.
14	Only the dual-constrained adaptive method, which limits $b$ to the minimum needed, improves over uniform (paired gap $0.086$, $p{<}0.01$, $N{=}3$).
15	Figure~\ref{fig:grid_b_trend} contextualizes this: the grid curve has a broad plateau at $b \in [0.1, 0.5]$ (PPL 17.620--17.655), and adaptive $\bstar$ (mean 17.651) f
…[truncated 8264 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-19T04:29:33.443604+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-19T04:29:33.895619+00:00_

1	\paragraph{Why minimum intervention works.}
2	Restraint in downweighting outperforms aggressiveness.
3	In the 38.2\% of batches where $\aeff$ determines $\bstar$, the selected exponent is 4.9$\times$ lower than the ESS-only upper bound (\S\ref{sec:regime}), preventing unnecessary suppression of borderline samples ($q \approx 0.4$--$0.6$); this rate is robust across contamination levels (33.4\% at $\rho{=}0.6$) and seeds (CV ${<}2\%$).
4	$\aeff$ correlates with the true batch-level real fraction at Pearson $r \approx 0.70$ with a conservative bias of $-0.03$ (Appendix~\ref{app:alpha_validation}).
5	
6	\paragraph{Where the advantage manifests.}
7	The advantage appears entirely at evaluation (PPL 17.65 vs.\ 17.69); training loss curves overlap (${\sim}1.4\%$ difference), consistent with reshaping the effective distribution.
8	Downstream benchmarks show 4 of 5 tasks with small negative $\Delta$ ($p \approx 0.19$, Appendix~\ref{app:downstream}); the aggregate mean $\bstar \approx 1.4$ as a fixed exponent yields PPL no better than uniform (17.693 vs.\ 17.694), confirming that per-batch adaptation is essential.
9	
10	\paragraph{$\tau$ as a practical dial.}
11	$\tau \in [0.5, 0.8]$ all outperform uniform (Table~\ref{tab:tau}); sensitivity is asymmetric (over-cleaning degrades sharply, under-cleaning is mild), and $\tau \in [0.7, 0.8]$ is robust across $\rho \in \{0.4, 0.6\}$ (Appendix~\ref{app:tau_rho}).
12	
13	\paragraph{Detector signal semantics.}
14	The method requires a discriminative detector: both generative alternatives (GPT-2 PPL at AUC\,=\,0.91, $\Delta{=}{+}0.10$; N-gram PPL at AUC\,=\,0.73, $\Delta{=}{+}0.13$) reverse the advantage despite GPT-2's high AUC, because they conflate predictability with synthetic origin and assign high $q$-scores to fluent human text.
15	TF-IDF+LR (AUC\,=\,0.94, ECE\,=\,0.048) succeeds because its features target provenance rather than fluency.
16	
17	\paragraph{Filtering vs.\ reweighting.}
18	The 3-seed epoch-matched experiment (\S
…[truncated 761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-19T04:29:33.896066+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-19T04:29:34.348318+00:00_

1	We introduced Minimum Intervention Reweighting, a dual-constraint framework that derives per-batch $\bstar$ from detector scores alone ($\aeff(b) \geq \tau$, $\mathrm{ESS}(b) \geq \nmin$), reducing grid search from nine runs to one while achieving comparable PPL (3-seed gap 95\% CI $[-0.039, 0.101]$).
2	The ablation confirms both detector signal and minimum intervention are necessary ($\rho{=}0.4$); the advantage persists at $\rho{=}0.6$ ($\Delta{=}{-}0.027$, $p{<}0.01$).
3	A 3-seed epoch-matched control shows D\&R's apparent advantage is entirely due to multi-epoch exposure ($\Delta{=}0.006$); the method transfers to 1.7B without degradation ($\Delta{=}{-}0.01$).
4	Future work: multi-seed scale confirmation, discriminative detector characterization across architectures, and naturally contaminated corpora.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-19T04:29:34.399018+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-19T04:29:34.851273+00:00_

1	\paragraph{Scale and cross-model transfer.}
2	All main experiments use Qwen3-0.6B with batch size 4.
3	A 1.7B verification (Qwen3-1.7B, $\rho{=}0.4$) under matched conditions shows $\Delta{=}{-}0.01$ (adaptive 13.26 vs.\ uniform 13.26), confirming that the method transfers without degradation but does not demonstrate a clear advantage at this scale; multi-seed replication is needed.
4	Cross-model transfer (Llama-3.2-3B, single seed) shows parity with uniform on PPL and HellaSwag, with a $+$1.6\,pp MMLU advantage that requires replication.
5	
6	\paragraph{Contamination range.}
7	The method improves over uniform at $\rho \in \{0.4, 0.6\}$ but not at $\rho{=}0.2$ ($+$0.046 PPL, 0.26\% relative), indicating an effective range of $\rho \geq 0.4$ with $\tau{=}0.8$.
8	Behavior at $\rho > 0.8$ is untested; extreme contamination may violate the assumption that sufficient real samples exist per batch for meaningful $\aeff$ estimation.
9	Real web-scale contamination is domain-skewed, which may alter within-batch $\aeff$ distributions.
10	
11	\paragraph{Detector coverage.}
12	Three detectors have been tested: TF-IDF+LR (discriminative, AUC\,=\,0.94) succeeds, while GPT-2 perplexity (generative, AUC\,=\,0.91) and N-gram perplexity (generative, AUC\,=\,0.73) both fail.
13	The pattern suggests discriminative signal is necessary, but three detectors from two families cannot distinguish a type effect from a calibration effect; testing additional discriminative detectors at varying AUC levels would isolate the mechanism.
14	
15	\paragraph{Threshold.}
16	$\tau$ is an empirical hyperparameter.
17	The convergence theory of \citet{wang2026survive} assumes a known contamination proportion $\alpha$, which we do not require; bridging this gap to derive $\tau$ from first principles remains open.
18	
19	\paragraph{Evaluation.}
20	Main results report held-out perplexity.
21	Downstream benchmarks (Appendix~\ref{app:downstream}) show 4 of 5 tasks with small negative $\Delta$ (uniform slightly 
…[truncated 863 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-19T04:29:34.851735+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-19T04:29:34.952883+00:00_

1	\section{Proofs}
2	\label{app:proofs}
3	
4	\begin{proof}[Proof of Proposition~\ref{prop:monotone}]
5	Let $w_i(b) = (1 - q_i)^b$, $W(b) = \sum_{j=1}^B w_j(b)$, and $\pi_i(b) = w_i(b) / W(b)$.
6	Then
7	\begin{equation*}
8	  \alpha_{\mathrm{eff}}(b) = \sum_{i=1}^{B} \pi_i(b)\, r_i,
9	\end{equation*}
10	where $r_i \in \{0, 1\}$ indicates whether sample $i$ is real.
11	Taking the derivative with respect to $b$:
12	\begin{align*}
13	  \frac{d\pi_i}{db}
14	  &= \pi_i \!\left(\frac{d \ln w_i}{db} - \frac{d \ln W}{db}\right)
15	  = \pi_i \!\left(\ln(1{-}q_i) - \sum_j \pi_j \ln(1{-}q_j)\right).
16	\end{align*}
17	Substituting,
18	\begin{align*}
19	  \frac{d\alpha_{\mathrm{eff}}}{db}
20	  &= \sum_i r_i\, \pi_i \!\left(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\right) \\
21	  &= \mathrm{Cov}_{\pi}\!\bigl(r_i,\, \ln(1{-}q_i)\bigr).
22	\end{align*}
23	For any detector with better-than-random discrimination, real samples ($r_i = 1$) have $q_i \leq 0.5$ on average, and thus higher $\ln(1{-}q_i)$ than synthetic samples.
24	The weighted covariance $\mathrm{Cov}_{\pi}(r_i, \ln(1{-}q_i))$ is therefore non-negative, establishing that $\alpha_{\mathrm{eff}}(b)$ is non-decreasing in $b$.
25	\end{proof}
26	
27	\begin{proposition}[ESS monotonicity]
28	\label{prop:ess_mono}
29	$\mathrm{ESS}(b)$ is non-increasing in $b$, and strictly decreasing whenever the batch contains at least two samples with distinct $q$-values.
30	\end{proposition}
31	
32	\begin{proof}
33	Write $\mathrm{ESS}(b) = 1 / \sum_i \pi_i(b)^2$, where $\pi_i(b) = w_i(b) / W(b)$.
34	The denominator $\sum_i \pi_i^2$ is the Herfindahl index $H$.
35	Differentiating $H$ with respect to $b$:
36	\begin{equation*}
37	  \frac{dH}{db} = 2 \sum_i \pi_i^2 \bigl(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\bigr).
38	\end{equation*}
39	This equals $2\,\mathrm{Var}_{\pi^2}[\ln(1{-}q)]$ under the $\pi^2$-weighted measure.
40	Since variance is non-negative and strictly positive when not all $\ln(1{-}q_i)$ coincide (i.e., when at least two $q$
…[truncated 12675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-19T04:29:42.098409+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex",
  "offset": "297"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex",
    "offset": "297"
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-19T04:29:42.550517+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (297). The file has 297 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-19T04:29:43.052867+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-19T04:29:43.053458+00:00_

1	% References for Minimum Intervention Reweighting paper
2	% Note: entries to be verified via verify_references before final submission
3	
4	@article{drayson2025detection,
5	  title={Machine-Generated Text Detection Prevents Language Model Collapse},
6	  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
7	  journal={arXiv preprint arXiv:2502.15654},
8	  year={2025}
9	}
10	
11	@article{he2025golden,
12	  title={Golden Ratio Weighting Prevents Model Collapse},
13	  author={He, Hengzhi and Xu, Shirong and Cheng, Guang},
14	  journal={arXiv preprint arXiv:2502.18049},
15	  year={2025}
16	}
17	
18	@article{wang2026survive,
19	  title={Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training},
20	  author={Wang, Kevin and Niu, Hongqian and Li, Didong},
21	  journal={arXiv preprint arXiv:2602.16065},
22	  year={2026}
23	}
24	
25	@article{shumailov2024model,
26	  title={{AI} Models Collapse When Trained on Recursively Generated Data},
27	  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
28	  journal={Nature},
29	  volume={631},
30	  pages={755--759},
31	  year={2024}
32	}
33	
34	@inproceedings{dohmatob2025strong,
35	  title={Strong Model Collapse},
36	  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
37	  booktitle={ICLR},
38	  year={2025}
39	}
40	
41	@article{vehtari2024psis,
42	  title={Pareto Smoothed Importance Sampling},
43	  author={Vehtari, Aki and Simpson, Daniel and Gelman, Andrew and Yao, Yuling and Gabry, Jonah},
44	  journal={JMLR},
45	  year={2024}
46	}
47	
48	@inproceedings{sow2025dynamic,
49	  title={Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining},
50	  author={Sow, Daouda and Woisetschl{\"a}ger, Herbert and Bulusu, Saikiran and Wang, Shiqiang and Jacobsen, Hans-Arno and Liang, Yingbin},
51	  booktitle={ICLR},
52	  year={2025}
53	
…[truncated 6354 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-19T04:29:43.656140+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-19T04:29:43.706922+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/decisions.yaml\", \"content\": \"_next_id: 91\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:38 UTC\\n  summary: 投稿目标定为 AAAI 2027 (~Aug 2026)，放弃 EMNLP 2026 ARR May 25\\n  rationale: EMNLP ARR 仅剩 12 天且无任何基础设施，即使 AI 团队速度也无法完成多轮预训练实验。AAAI 2027 有 ~11 周，足够完成\\n    4 phase 全流程。两者均为 A 类会议。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:38 UTC\\n  summary: 'MVP 设计: 单模型(Qwen3-0.6B) + 单污染比例(40%) + 三组对比(uniform/grid-b/adaptive-b*)'\\n  rationale: 核心假设是 adaptive b* 能替代 grid search。最小验证只需一个污染比例下的 A/B/C 对比。40% 选取因为理论和\\n    Strong Model Collapse 均表明该区间效应显著。通过后再扩展到多污染比例/多生成器/多模型。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-13 17:40 UTC\\n  summary: '修正 D001: 主攻 EMNLP 2026 ARR May 25，AAAI 2027 为后备'\\n  rationale: 用户明确指出 EMNLP ARR 5/25 时间不紧、资源会给够。AI 团队 24/7 执行 + 4 卡并行：数据生成 ~2 天、MVP\\n    ~1 天、全矩阵 ~3 天、论文 ~3 天、迭代 ~2 天 = 11 天可完成。12 天 deadline 可行。保守估计完成时间是最大风险。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-13 17:42 UTC\\n  summary: '采纳 Reviewer 4 点 MVP 协议补全: 3 seeds、detector gate、grid-b 定义、kill criteria'\\n  rationale: 'Reviewer 指出 MVP 设计 4 个缺口均合理: (1) 单 seed 无统计保障 → 3 seeds，缩 tokens 到 200M\\n    控预算; (2) 检测器质量是 pipeline 前提 → 加 gate AUC≥0.95/ECE≤0.05; (3) grid search baseline\\n    需可复现 → 定义 b∈{0.5,1,1.5,2,3,5}; (4) 无 fail 路径 → 定义三级 kill/pivot。不增加工程量，只补协议。'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D005\\n  date: 2026-05-13 22:08 UTC\\n  summary: 识别 q-score 极化风险：AUC=0.999998 可能导致 adaptive b* vs grid-b 对比退化，制定分级应对方案\\n  rationale: 'Reviewer 审查发现 detector eval_auc=0.999998（step 2000），q-score 可能高度双峰化。若校准后\\n    >95% 样本 q<0.05 或 q>0.95，则 w=(1-q)^b 对所有 b>0 约等于 0，不同 b 值间无区分度。MVP 技术上可能 PASS（adaptive\\n    ≈ grid-b，满足 ≥90% 条件），但无法证明核心贡献（自适应精细调优的价值）。\\n\\n\\n    应对方案（detector 完成后按 q-score 分布分级执行）：\\n\\n    - 分布有spread（q 在 0.1
…[truncated 1474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-19T04:29:49.481780+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit long paper short paper guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format page limit long paper short paper guidelines"
  }
}
```

</details>

---


### Tool call

_source line 141 · 2026-05-19T04:29:49.783392+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/project_config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/project_config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 142 · 2026-05-19T04:29:49.834032+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-19T04:29:55.404941+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit long paper short paper guidelines"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, here is the submission format information for ACL Rolling Review 2026:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Upon acceptance, final versions of long papers will be given one additional page – up to nine (9) pages of content plus unlimited pages for acknowledgments and references.

Review versions of short p
…[truncated 1122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 5923
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-19T04:30:00.725652+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/project_config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/project_config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
  }
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-19T04:30:00.726109+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 146 · 2026-05-19T04:30:03.543203+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/agent"
  }
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-19T04:30:03.594039+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_director_5d592d28.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-19T04:30:06.387553+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
  }
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-19T04:30:06.438253+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-19T04:30:09.048596+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.toml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.toml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-19T04:30:09.099831+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-19T04:30:13.618067+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10",
  "output_mode": "files_with_matches",
  "head_limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10",
    "output_mode": "files_with_matches",
    "head_limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-19T04:30:14.922964+00:00_

Found 7 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/global/logs/system.log
AGENTS.md
CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/workers/worker_ssh_download_tau_figures_20260515T184814.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/logs/review_best.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/archive/feishu_group_oc_39371eead41d9df941b3542b7f23b377_20260514T202326_265966.jsonl

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "elapsed_ms": 1304
}
```

</details>

---


### Tool call

_source line 154 · 2026-05-19T04:30:17.985030+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review.*enabled",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10",
  "output_mode": "content",
  "head_limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review.*enabled",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10",
    "output_mode": "content",
    "head_limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-19T04:30:18.136093+00:00_

AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_director.jsonl:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_director.jsonl:97:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_director.jsonl:154:{"ts": "2026-05-19T04:30:17.985030+00:00", "role": "tool", "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director", "text": "called Grep", "tool": "Grep", "tool_args": {"pattern": "external_review.*enabled", "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10", "output_mode": "content", "head_limit": "10"}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/global/logs/system.log:27936:2026-05-18 06:19:41 INFO     [HOOKS] [review] external_review_enabled=False for project=provenance_weight_training
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/global/logs/system.log:31870:2026-05-19 04:28:52 INFO     [HOOKS] [review] external_review_enabled=False for project=provenance_weight_training

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-19T04:30:22.151643+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-19T04:30:22.553452+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-19T04:30:22.754580+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-19T04:30:22.807351+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_reports/round_1.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-19T04:30:25.660778+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-19T04:30:25.661536+00:00_

1	- id: "RR-W1"
2	  summary: "Paper claims 'from random initialization' but code uses from_pretrained() — actually continued pretraining"
3	  category: writing
4	  severity: warning
5	  status: resolved
6	  first_raised_round: 1
7	  last_seen_round: 2
8	  mentions:
9	    - round: 1
10	      reviewers: [research_reviewer]
11	      note: "Two independent reviews confirmed: pretrain_weighted.py L318 uses from_pretrained(), model.safetensors 1.5GB = full pretrained weights"
12	    - round: 2
13	      reviewers: [R1, R2]
14	      note: "Both reviewers confirm fixed: Abstract line 7, Introduction line 23, Experiments line 12 now say 'continued pretraining'"
15	  action_items:
16	    - round: 1
17	      action: "Fix paper text: 'pretrain from random initialization' → 'continue pretraining Qwen3-0.6B'"
18	      assigned_to: paper_agent
19	      status: done
20	    - round: 1
21	      action: "Run baseline PPL eval on untrained Qwen3-0.6B checkpoint to quantify absolute improvement"
22	      assigned_to: main_agent
23	      status: done
24	  resolution: "Fixed in current version: Abstract, Introduction, Experiments all use 'continued pretraining'"
25	  resolution_round: 2
26	
27	- id: "RR-W2"
28	  summary: "Paper claims 'balanced real/synthetic test set' but eval_holdout.jsonl is human-only (FineWeb)"
29	  category: writing
30	  severity: warning
31	  status: resolved
32	  first_raised_round: 1
33	  last_seen_round: 2
34	  mentions:
35	    - round: 1
36	      reviewers: [research_reviewer]
37	      note: "eval_holdout.jsonl: 67823 lines, all source=fineweb depth=0, zero synthetic samples"
38	    - round: 2
39	      reviewers: [R1, R2]
40	      note: "Both reviewers confirm fixed: Experiments line 16 now says 'containing only human-authored text'"
41	  action_items:
42	    - round: 1
43	      action: "Fix paper text: 'balanced real/synthetic test set' → 'human-only test set drawn from FineWeb'"
44	      assigned_to: paper_agent
45	      status: done
46	  resolution: "Fixed in
…[truncated 13591 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-19T04:31:19.809064+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计/统计）\n\n### 论文信息\n- **标题**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\n- **论文路径**: `projects/provenance_weight_training/docs/paper/main.tex`（sections 目录下 10 个 .tex 文件）\n- **目标 venue**: EMNLP 2026 Main Conference (ACL Rolling Review May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板 (`\\usepackage[review]{acl}`)，长文正文 ≤ 8 页 + unlimited references，double-blind，Limitations section 必须（不计页数）\n\n### 你的审查侧重\n\n**A. 方法严谨性（重点）**\n1. Dual-constraint framework (α_eff ≥ τ, ESS ≥ n_min) 的理论基础是否solid？\n   - Proposition 1 (α_eff 单调性) 的证明是否完整、条件是否充分？\n   - ESS 单调性证明（Appendix）是否严格？\n   - α_eff 作为 true real fraction 的 proxy，其理论依据和实证验证（Appendix α_eff validation）是否充分？\n   - Wang 2026 的收敛理论要求已知 α，但本文的 τ 是经验超参——这个理论断联是否被充分讨论？\n2. \"Minimum intervention principle\" 是否有理论保证（为何选最小 b 而非其他 b）？\n3. 超参数 τ=0.8 和 n_min=2 的选择是否有足够依据？声称\"principled defaults\"是否过强？\n4. Bisection 算法在 b_max=20 下是否可能遗漏非单调区间？\n\n**B. 实验设计与统计**\n1. N=3 seeds 下的统计推断是否充分？95% CI [-0.039, 0.101] 是否支持所做的 claims？\n2. Grid-b post-hoc oracle selection (best b=0.3 on test set) vs adaptive 的比较是否公平？\n3. D&R epoch-matched 控制实验（Table 2）是否充分解决 multi-epoch confound？\n4. 1.7B scale 验证仅单 seed，Δ=-0.01——是否支持\"transfers without degradation\"的 claim？\n5. 下游 benchmark 4/5 略差——PPL 改善是否可能是 distribution matching artifact？\n6. 自污染设定（Qwen3-0.6B 生成 + Qwen3-0.6B 训练）的外部有效性？\n7. ρ=0.2 时方法失效（+0.046 PPL）——\"effective range ρ≥0.4\"的限制是否被充分讨论？\n\n**C. 可复现性**\n1. 检测器训练细节（TF-IDF feature 设置、LR 超参、calibration 流程）是否足以复现？\n2. 训练配置（lr schedule, warmup, gradient accumulation 等）是否完整？\n\n请输出完整审稿报告，包含 Summary, Strengths, Weaknesses (分 Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (评分 + 置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计/统计）\n\n### 论文信息\n- **标题**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\n- **论文路径**: `projects/provenance_weight_training/docs/paper/main.tex`（sections 目录下 10 个 .tex 文件）\n- **目标 venue**: EMNLP 2026 Main Conference (ACL Rolling Review May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板 (`\\usepackage[review]{acl}`)，长文正文 ≤ 8 页 + unlimited references，double-blind，Limitations section 必须（不计页数）\n\n### 你的审查侧重\n\n**A. 方法严谨性（重点）**\n1. Dual-constraint framework (α_eff ≥ τ, ESS ≥ n_min) 的理论基础是否solid？\n   - Proposition 1 (α_eff 单调性) 的证明是否完整、条件是否充分？\n   - ESS 单调性证明（Appendix）是否严格？\n   - α_eff 作为 true real fraction 的 proxy，其理论依据和实证验证（Appendix α_eff validation）是否充分？\n   - Wang 2026 的收敛理论要求已知 α，但本文的 τ 是经验超参——这个理论断联是否被充分讨论？\n2. \"Minimum intervention principle\" 是否有理论保证（为何选最小 b 而非其他 b）？\n3. 超参数 τ=0.8 和 n_min=2 的选择是否有足够依据？声称\"principled defaults\"是否过强？\n4. Bisection 算法在 b_max=20 下是否可能遗漏非单调区间？\n\n**B. 实验设计与统计**\n1. N=3 seeds 下的统计推断是否充分？95% CI [-0.039, 0.101] 是否支持所做的 claims？\n2. Grid-b post-hoc oracle selection (best b=0.3 on test set) vs adaptive 的比较是否公平？\n3. D&R epoch-matched 控制实验（Table 2）是否充分解决 multi-epoch confound？\n4. 1.7B scale 验证仅单 seed，Δ=-0.01——是否支持\"transfers without degradation\"的 claim？\n5. 下游 benchmark 4/5 略差——PPL 改善是否可能是 distribution matching artifact？\n6. 自污染设定（Qwen3-0.6B 生成 + Qwen3-0.6B 训练）的外部有效性？\n7. ρ=0.2 时方法失效（+0.046 PPL）——\"effective range ρ≥0.4\"的限制是否被充分讨论？\n\n**C. 可复现性**\n1. 检测器训练细节（TF-IDF feature 设置、LR 超参、calibration 流程）是否足以复现？\n2. 训练配置（lr schedule, warmup, gradient accumulation 等）是否完整？\n\n请输出完整审稿报告，包含 Summary, Strengths, Weaknesses (分 Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (评分 + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-19T04:31:37.965175+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18156
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-19T04:31:38.216720+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + Related Work + 写作/格式）\n\n### 论文信息\n- **标题**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\n- **论文路径**: `projects/provenance_weight_training/docs/paper/main.tex`（sections 目录下 10 个 .tex 文件）\n- **目标 venue**: EMNLP 2026 Main Conference (ACL Rolling Review May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板 (`\\usepackage[review]{acl}`)，长文正文 ≤ 8 页 + unlimited references，double-blind，Limitations section 必须（不计页数）\n\n### 你的审查侧重\n\n**A. 新颖性与贡献评估（重点）**\n1. 核心公式 w=(1-q)^b 直接来自 Drayson 2025。本文的增量贡献（dual constraint 选 b*）的新颖性是否足以支撑 EMNLP Main Conference？还是更适合 Findings？\n2. Dual constraint (α_eff + ESS) 是否为标准 importance sampling 技术的直接应用？\n3. \"Minimum intervention principle\" 是真正的新洞察还是 rebranding？\n4. 三条 contributions 是否每条都有充分的支撑证据？\n5. 与 Drayson 2025 的区分度是否在论文中被清楚阐述？\n\n**B. Related Work 覆盖与 Positioning**\n1. 引用覆盖是否充分？EMNLP 长文通常 40-60+ refs，当前 ~30 条是否足够？\n2. 是否遗漏重要 related work？特别关注：\n   - 近期 data quality/curation 工作（2024-2026）\n   - Instance-level reweighting 的其他方法\n   - Importance sampling 理论文献\n   - 其他 model collapse prevention 方法\n3. Related Work 的结构和 positioning 是否有效区分本文贡献？是否有\"论文堆砌\"问题？\n\n**C. 写作质量与格式合规**\n1. **页数检查**：正文是否 ≤ 8 页？（abstract + intro + related + method + experiments + results + discussion + conclusion）\n2. **AI 写作痕迹**：检查 em-dash (—), en-dash (–) 滥用、-ing 分词短语结尾、过度分段、过渡词堆砌等\n3. **叙事一致性**：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否讲同一个故事？\n4. **专有名词定义**：首次出现的术语/缩写是否都有定义？\n5. **图表质量**：Figure/Table 的信息密度、caption 自包含性、数值格式一致性\n6. **匿名化**：是否有破坏 double-blind 的信息泄露？\n7. **Responsible NLP Checklist**：论文是否准备了？\n8. **Abstract** 是否在 150-250 words 范围内，四个必答问题（问题、重要性、方法、结果）是否都回答了？\n\n**D. Limitations Section**\n1. 是否全面覆盖了论文的局限性？\n2. 是否有刻意回避的弱点？\n\n请输出完整审稿报告，包含 Summary, Strengths, Weaknesses (分 Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (评分 + 置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + Related Work + 写作/格式）\n\n### 论文信息\n- **标题**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\n- **论文路径**: `projects/provenance_weight_training/docs/paper/main.tex`（sections 目录下 10 个 .tex 文件）\n- **目标 venue**: EMNLP 2026 Main Conference (ACL Rolling Review May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板 (`\\usepackage[review]{acl}`)，长文正文 ≤ 8 页 + unlimited references，double-blind，Limitations section 必须（不计页数）\n\n### 你的审查侧重\n\n**A. 新颖性与贡献评估（重点）**\n1. 核心公式 w=(1-q)^b 直接来自 Drayson 2025。本文的增量贡献（dual constraint 选 b*）的新颖性是否足以支撑 EMNLP Main Conference？还是更适合 Findings？\n2. Dual constraint (α_eff + ESS) 是否为标准 importance sampling 技术的直接应用？\n3. \"Minimum intervention principle\" 是真正的新洞察还是 rebranding？\n4. 三条 contributions 是否每条都有充分的支撑证据？\n5. 与 Drayson 2025 的区分度是否在论文中被清楚阐述？\n\n**B. Related Work 覆盖与 Positioning**\n1. 引用覆盖是否充分？EMNLP 长文通常 40-60+ refs，当前 ~30 条是否足够？\n2. 是否遗漏重要 related work？特别关注：\n   - 近期 data quality/curation 工作（2024-2026）\n   - Instance-level reweighting 的其他方法\n   - Importance sampling 理论文献\n   - 其他 model collapse prevention 方法\n3. Related Work 的结构和 positioning 是否有效区分本文贡献？是否有\"论文堆砌\"问题？\n\n**C. 写作质量与格式合规**\n1. **页数检查**：正文是否 ≤ 8 页？（abstract + intro + related + method + experiments + results + discussion + conclusion）\n2. **AI 写作痕迹**：检查 em-dash (—), en-dash (–) 滥用、-ing 分词短语结尾、过度分段、过渡词堆砌等\n3. **叙事一致性**：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否讲同一个故事？\n4. **专有名词定义**：首次出现的术语/缩写是否都有定义？\n5. **图表质量**：Figure/Table 的信息密度、caption 自包含性、数值格式一致性\n6. **匿名化**：是否有破坏 double-blind 的信息泄露？\n7. **Responsible NLP Checklist**：论文是否准备了？\n8. **Abstract** 是否在 150-250 words 范围内，四个必答问题（问题、重要性、方法、结果）是否都回答了？\n\n**D. Limitations Section**\n1. 是否全面覆盖了论文的局限性？\n2. 是否有刻意回避的弱点？\n\n请输出完整审稿报告，包含 Summary, Strengths, Weaknesses (分 Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (评分 + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-19T04:31:39.592951+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1376
}
```

</details>

---


### Assistant

_source line 166 · 2026-05-19T04:31:48.173262+00:00_

两名 Reviewer 已启动：

| Reviewer | 侧重 | 状态 |
|----------|------|------|
| R1 | 方法严谨性 + 实验设计/统计 | 审稿中 |
| R2 | 新颖性 + Related Work + 写作/格式 | 审稿中 |

等待 Reviewer 返回初审报告。收到后进入 Step 2（交叉分享 + 逐条回应）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 11

## Round 11

2 recorded events


### User

_source line 167 · 2026-05-19T04:36:59.296489+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿报告

**论文**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining
**Venue**: EMNLP 2026 (ACL Rolling Review May 2026 cycle)

---

## 总体评分

**Overall**: 3.0 (Findings)
**一句话总结**: 方法直觉合理、实验设计有亮点（epoch-matched control），但核心 claim 的统计支撑不足，理论基础与经验选择之间存在未弥合的断联，且效果量极小、外部有效性受限。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 (Acceptable) | 主要 claim 有实验支撑但统计力度不足（N=3, wide CI）；理论与经验超参之间的断联被承认但未解决；Proposition 1 证明正确但表述误导 |
| Excitement | 3/5 (Interesting) | 问题实际且相关，minimum intervention 视角有新意，但效果量过小（0.043 PPL）、适用范围窄（ρ≥0.4、仅 discriminative detectors），实际影响力有限 |
| Confidence | 4/5 | 仔细阅读了全文、附录和证明，熟悉 importance weighting 和 LLM pretraining 文献 |

---

## Summary

本文提出了一个双约束框架，从 batch 级别的检测器分数自动导出 reweighting exponent b*：通过 α_eff(b) ≥ τ（质量下限）和 ESS(b) ≥ n_min（稳定上限）两个约束的交集，选取满足条件的最小 b，称为 "minimum intervention principle"。在 Qwen3-0.6B 的 continued pretraining 上（132M FineWeb tokens, 40% 合成污染），adaptive b* 的 PPL 接近 grid search 最优值（17.651 vs 17.620），且 ablation 表明 detector signal 和 minimum intervention 缺一不可。Epoch-matched 实验显示 D&R 的表面优势完全来自 multi-epoch exposure。

---

## 主要优势

1. **Epoch-matched control 实验设计精巧**（Table 2, Section 5.1）。通过控制 content epochs，将 D&R 的表面 PPL 优势（0.360）分解为 multi-epoch effect vs. filtering effect，结论清晰（Δ=0.006 within seed variance）。这一分析对领域有独立价值，即使方法本身不被采纳。

2. **Ablation 层次清晰**（Table 1）。Random < ESS-only < Uniform < Adaptive 的层级在 ρ=0.4 和 ρ=0.6 两个水平上一致复现，令人信服地分离了 detector signal 和 minimum intervention 两个要素的贡献。

3. **Detector signal type 发现有启发性**（Section 5.2, Table 7, Appendix D）。Discriminative vs. generative detector 的对比揭示了 AUC 并非唯一决定因素，generative detectors 因混淆 fluency 与 synthetic origin 而反转优势。这一发现有实用意义。

4. **写作质量高**。论文结构清楚，叙事主线统一，Limitations section 坦诚地讨论了多数弱点。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **核心 claim 的统计支撑不足：N=3 下的推断力度**
- 具体位置：Section 5.1, Table 1, Abstract
- 问题：Adaptive vs Grid-best 的 95% CI 为 [-0.039, 0.101]，跨越零且包含 adaptive 更差的区间。论文诚实地承认 "too wide for formal equivalence testing"（Section 5.1 第2段），但 Abstract 仍称 "achieves PPL competitive with the grid-searched optimum"。在 paired comparison 中 N=3 的 statistical power 极低（对于 0.03 量级的 effect size，power 远低于 0.5）。Adaptive vs Uniform 的 Δ=0.043 虽 p<0.003，但绝对量级在 22.97→17.65 的 5.3-point drop 背景下极小（0.24% relative）。
- 为什么影响接收：如果核心 claim（"matches grid-searched optimum"）在统计上无法确立，论文的主要贡献就从 "achieves comparable quality" 降级为 "saves compute but quality unknown"。
- 建议修改方向：(a) 增加到 N≥5 seeds 以缩窄 CI；(b) 如果 seed 数无法增加，调整 claim 措辞，将 "competitive" 改为更谨慎的表述，明确说明 CI 包含 degradation；(c) 考虑 TOST equivalence test 并报告 smallest meaningful difference。

**N2** [critical] **理论基础与经验超参之间的断联**
- 具体位置：Section 3.2 (第66-67行), Section 3.5 (第127行), Limitations (第17行)
- 问题：α_eff ≥ τ 的理论 motivation 来自 Wang 2026 的收敛理论（"convergence rate improves with the effective real-data fraction"），但 Wang 2026 假设已知精确污染比例 α，而本文的 τ 是一个需要在 [0.5, 0.95] 范围内搜索的经验超参。Section 3.5 称 "principled defaults"，但 τ=0.8 的选择完全基于 seed 42 的 sweep（Table 3）。这构成一个理论断联：
  (a) 方法声称的理论 grounding 仅限于 "α_eff 越大收敛越快" 这一定性 insight，不提供 τ 的定量推导；
  (b) "principled defaults" 这一措辞暗示比实际更强的理论保证。
  (c) τ 的最优值随 ρ 变化（ρ=0.4 时 0.8，ρ=0.6 时 0.7，Figure 4），意味着 τ 本身也需要某种 per-setting tuning，削弱了 "zero validation cost" 的 claim。
- 为什么影响接收：如果 τ 需要调优，方法的核心卖点（免去 grid search）就被削弱——从 9 次训练减少到 1 次，但代价是一个难以事先确定的超参。
- 建议修改方向：(a) 将 "principled defaults" 改为 "empirically robust defaults"；(b) 承认 τ 的选择本质上替代了对 b 的搜索，并定量比较两者的搜索空间大小和敏感度；(c) 或者推导 τ 与 ρ 的理论关系（即使是近似的）。

**N3** [critical] **1.7B 结果不支持 "transfers without degradation" 的 claim**
- 具体位置：Section 5.2 (第94行), Abstract (第9行), Conclusion (第3行)
- 问题：1.7B 验证仅单 seed，Δ=-0.01（adaptive 13.26 vs uniform 13.26），这个差异在报告精度内几乎为零。"Transfers without degradation" 是一个关于方法鲁棒性的正面 claim，但单 seed、Δ≈0 的结果同样支持 "no effect at this scale" 的解释。Abstract 称 "transfers to 1.7B parameters without degradation"，Conclusion 同样使用，但 Limitations 更谨慎地说 "confirms generalization but not advantage amplification"。
- 为什么影响接收：Scale transfer 是 NLP 社区高度关注的问题。单 seed、无统计显著性的结果不应在 Abstract/Conclusion 中被表述为正面发现。
- 建议修改方向：Abstract/Conclusion 中加入 "single-seed" qualifier，或增加 multi-seed 1.7B 验证。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **自污染设定的外部有效性**
- 具体位置：Section 4 (第1-3行)
- 问题：Qwen3-0.6B 生成 + Qwen3-0.6B 训练的自污染设定是一个特殊场景。现实中 web 污染来自多种不同（通常更强的）模型。当污染源与训练模型不同时：(a) 检测器的 AUC 可能变化；(b) 合成文本的 distribution 与模型自身输出不同，α_eff proxy 的有效性未验证。Limitations 中提到 Llama-3.2-3B 的 cross-model transfer 但数据仅在 Limitations 文本中（未见 table）。
- 建议：增加至少一个 cross-generator 实验（如用 GPT-4/Llama 生成的合成数据），或将 Llama-3.2-3B 结果移入 appendix 并给出完整 table。

**W2** [warning] **Downstream benchmarks 4/5 略差，distribution matching artifact 风险**
- 具体位置：Appendix F (Table 6), Discussion (第7-8行)
- 问题：5 个 downstream benchmarks 中 4 个 adaptive 略差于 uniform（ARC-C -0.005, ARC-E -0.007, HellaSwag -0.005, WinoGrande -0.008），仅 PIQA +0.001。单 seed 下无法做统计检验，但方向性一致地偏负值。Discussion 承认 "may partly reflect distribution matching"，但 Abstract 和 Conclusion 完全未提及这一重要 caveat。
- 为什么重要：PPL 改善可能仅反映 training distribution 向 human-only evaluation set 偏移（因 reweighting 提升了 real-data 权重），而非真正的模型能力提升。如果 downstream 任务系统性地更差，这是 distribution matching artifact 的证据。
- 建议：在 Abstract 或 Conclusion 中加入一句 downstream caveat；增加 multi-seed downstream 评估。

**W3** [warning] **ρ=0.2 失效的讨论不充分**
- 具体位置：Limitations (第7行)
- 问题：ρ=0.2 时 adaptive 比 uniform 差 +0.046 PPL（0.26% relative），方法失效。Limitations 用一行带过（"effective range ρ≥0.4"），但：
  (a) 主文完全不提 ρ=0.2；
  (b) 失效的机制未解释（ρ=0.2 时 α_eff(0) ≈ 0.8 已满足 τ=0.8，大部分 batch 直接 b*=0，那为什么 PPL 反而更差？是否因少数 contaminated batch 的过度干预？）；
  (c) 实际 web 污染比例的分布未讨论——如果真实 ρ 可能低于 0.4，方法的适用性受限。
- 建议：在 Section 5 或 Discussion 中分析 ρ=0.2 失效的机制；讨论何时应当使用 vs 不使用该方法。

**W4** [warning] **Micro-batch 级别 b* 决策的合理性**
- 具体位置：Section 3.3 (第86行), Section 3.5 (第138行)
- 问题：b* 在 micro-batch（B=4）级别计算。B=4 时 α_eff 仅有 5 个离散值 {0, 0.25, 0.5, 0.75, 1.0}（Appendix E），MAE=0.114，这意味着 α_eff 对 true real fraction 的估计精度很粗糙。方法论上，为什么不在 effective batch（B=16, gradient accumulation 后）级别计算 b*？Section 3.5 警告 "setting [n_min] relative to the effective batch silently forces b*=0"，但这只是 n_min 设置的问题，不是不能在更大 batch 上计算。
- 建议：解释 micro-batch vs effective-batch 的设计选择；报告在 B=16 上计算 b* 的对比实验。

**W5** [warning] **Proposition 1 证明表述的误导性**
- 具体位置：Section 3.2 Proof sketch (第52-57行), Appendix A (第1-25行)
- 问题：Proof sketch 称 "for any detector with better-than-random discrimination, real samples (r_i=1) have q_i ≤ 0.5 and thus higher ln(1-q_i)"。但 r_i 的定义是 r_i = 1[q_i ≤ 0.5]（Section 3.2 第23行），所以 r_i=1 ⟹ q_i ≤ 0.5 是定义上的恒等式，不依赖于检测器质量。α_eff 的单调性对任意 q-score 分布成立，是一个关于 weighted proportion 的代数性质，不是关于检测质量的声明。"Better-than-random discrimination" 条件实际上是 α_eff 作为真实 real fraction proxy 有效性的前提（Appendix E 验证的内容），不是单调性成立的前提。这一混淆让读者误以为单调性依赖于检测器质量。
- 建议：在 proof sketch 中明确 r_i = 1[q_i ≤ 0.5] 的定义蕴含了 Cov ≥ 0；将检测器质量条件移至 α_eff proxy 有效性的讨论中。

---

## 小问题（不影响接收）

- **M1**: Table 1 脚注 $^\S$ 说 D&R 用 q>0.3，但正文说 "best threshold (q>0.3)" 是 post-hoc 选出的（Section 5.1 第20行）。应标注为 oracle。
- **M2**: Golden Ratio baseline 仅单 seed（Table 1 脚注 $^\dagger$），与 3-seed 方法不对称。
- **M3**: Appendix Table 4 (D&R threshold) 中 Retained% 和 Epochs 部分行是近似值（用 ~），部分是精确值，不一致。
- **M4**: Llama-3.2-3B cross-model transfer 结果出现在 Limitations 文本中但无 table/appendix，无法 verify。
- **M5**: References: `lin2017focal` venue 写 "ICCV" 但 Focal Loss 发表于 ICCV 2017 作为 article，bib 中 type 为 article 但 venue 为 ICCV，建议改为 inproceedings。`vehtari2024psis` year 与 OpenAlex 不一致（bib=2024 vs API=2015, JMLR 正式发表可能更晚）。
- **M6**: 检测器训练细节不足（TF-IDF n-gram range、max features、LR regularization/solver 未报告），影响可复现性。Section 4 "Detector" 段仅给出 AUC 和 ECE，无法复现检测器本身。
- **M7**: 无代码/数据公开承诺。

---

## Questions to Authors

1. ρ=0.2 时 τ=0.8 使得大部分 batch 的 α_eff(0) ≈ 0.8（因污染比例低），此时 adaptive 方法大多返回 b*=0，理论上应退化为 uniform。为什么 PPL 反而比 uniform 差 +0.046？是否因为少数 contaminated batch 的 b* 过大导致了 negative transfer？能否提供 ρ=0.2 时的 b* 分布和 constraint regime 分解？

2. 为什么选择在 micro-batch（B=4）而非 effective batch（B=16）级别计算 b*？是否有在更大 batch 上的 ablation？

3. τ 的最优值随 ρ 变化（0.8 → 0.7）。如果预先不知道 ρ，如何确定 τ？是否可以从 batch-level 的 α_eff(0) 分布反推 ρ 的估计，再自适应选择 τ？

4. Cross-model transfer (Llama-3.2-3B) 的完整结果（PPL、downstream、per-task breakdown）能否补充到 appendix？

5. Hybrid method（Table 4, q>0.95 filtering + adaptive）显示 PPL 17.514，显著优于 pure adaptive 17.653，但仅在 appendix 提及。为什么不将 hybrid 作为推荐方法？

---

## Missing References

- **Gururangan et al. (2020)** "Don't Stop Pretraining: Adapt Pretraining Language Models to Domains and Tasks" — continued pretraining 的经典工作，直接相关但未引用。
- **Wettig et al. (2023)** "Should You Mask 15% in Masked Language Modeling?" — 关于 pretraining masking ratio 如何影响质量的分析，与本文的 intervention intensity 问题类似。
- 缺少对 **PANDA** (Li et al. 2024, "Purifying Large Language Models by Ensembling a Small Language Model") 或类似 purification/decontamination 方法的讨论。

---

## Reproducibility Assessment

**中等偏低**。训练配置（lr, schedule, optimizer, precision, batch size）基本完整。但以下细节缺失：
- 检测器：TF-IDF feature 设置（n-gram range, max_features, sublinear_tf 等）、LR 超参（C, solver, max_iter）、calibration validation set 大小
- 评估：sliding-window PPL 的实现细节（是否用 strided、overlap 处理）
- 代码/数据未公开
- Contamination injection：synthetic continuation 的 prompt format、decoding parameters（temperature, top-p 等）

---

## Overall Assessment

本文解决了一个实际且重要的问题（如何在不知道污染比例的情况下选择 reweighting exponent），提出的双约束框架在概念上简洁优雅。Epoch-matched control 是实验设计上的亮点，对领域有独立贡献。

然而，三个核心问题限制了论文的 acceptance case：
1. **统计力度不足**：N=3 seeds 下核心 claim 的 CI 过宽，效果量极小（0.043 PPL, 0.24%）；
2. **理论-经验断联**："principled" 和 "theoretical grounding" 的措辞超出了实际的理论保证；
3. **外部有效性受限**：仅验证 self-contamination + discriminative detector + ρ≥0.4 的组合，real-world applicability 未建立。

如果增加 seeds、调整 claims 措辞、补充 cross-generator 实验，这将是一篇适合 Findings 的贡献。当前版本介于 Findings borderline 和 Findings 之间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 168 · 2026-05-19T04:37:14.389305+00:00_

Reviewer 1 审稿报告已收到。评分 3.0 (Findings)，三个 critical issues（统计力度、理论断联、1.7B claim）。

等待 Reviewer 2 报告后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 12

## Round 12

2 recorded events


### User

_source line 169 · 2026-05-19T04:37:16.939790+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

核心结论：**Overall 3.0 (Findings)**，Soundness 3/5，Excitement 3/5。

三个 Must-Fix 问题：
1. **统计支撑不足** — N=3 的 95% CI [-0.039, 0.101] 包含 degradation，无法确立 "competitive with grid-best" 的 claim
2. **理论-经验断联** — τ=0.8 是经验选择但被包装为 "principled default"；τ 最优值随 ρ 变化，削弱 "zero validation cost" 卖点
3. **1.7B 单 seed 结果不支持 "transfers without degradation"** — Δ=-0.01 同样可解读为 "no effect"

主要优势：epoch-matched control 实验设计精巧，ablation 层级清晰，detector type finding 有启发性。

如需要我对特定问题深入分析或进入交叉评审阶段，随时通知。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 170 · 2026-05-19T04:37:26.582325+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 完成初审后进入交叉评审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 13

## Round 13

6 recorded events


### User

_source line 171 · 2026-05-19T04:38:48.648520+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 — Round 1 审稿报告

**论文**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining
**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review May 2026)

---

## 总体评分
**Overall**: 2.5/5（介于 Findings 和 borderline reject 之间）
**一句话总结**: 一个工程上有效的自动超参数选择方案，但核心公式来自已有工作，实验规模过小、效果量微弱，新颖性不足以支撑 EMNLP Main Conference 长文。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 方法论正确，推导无误，但实验规模（0.6B/132M tokens）与论文动机（web-scale contamination）严重脱节；N=3 seeds 的统计检验效力不足；效果量极小（0.24% relative PPL improvement） |
| Excitement | 2.0/5 | 核心贡献是对已有公式 w=(1-q)^b 的自动调参，dual constraint 使用的 α_eff 和 ESS 均为标准工具；"minimum intervention principle" 是标准约束优化的 rebranding；对 EMNLP 社区的启发性有限 |
| Reproducibility | 4.0/5 | 方法描述清晰，Algorithm 1 提供了完整伪代码，超参数默认值有明确说明；但代码和数据均未提供 |
| Confidence | 4/5 | 熟悉 importance sampling 理论和 data curation 文献，仔细阅读了全文及附录 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 新颖性不足以支撑 EMNLP Main Conference

- 具体位置：Section 3（Method），尤其 Eq. (1)-(4) 和 Algorithm 1
- 问题：
  - 核心加权公式 w=(1-q)^b **完全来自 Drayson et al. (2025)**，论文在 Section 2 Related Work 中明确承认（"We adopt the same weighting formula"）。
  - Dual constraint 的两个组件均为标准工具：α_eff（Eq. 2）是加权平均，ESS（Eq. 3）是 Kish (1965) 的经典公式。
  - "Minimum intervention principle" 的数学内涵是：在单调函数上用二分法找满足下界约束的最小 b，同时受上界约束。这是标准的约束优化，并非新洞察。
  - Proposition 1 的证明（α_eff 关于 b 单调）虽然 clean，但本质上是加权平均在指数倾斜下的标准性质。
  - **本文的增量贡献可概括为：对已有公式的一个自动超参数选择程序**，虽然实用，但 novelty 更接近 Findings 水平。
- 为什么影响接收：EMNLP Main 要求 "transformational value" 或显著的方法论创新。本文的核心技术贡献（bisection on two monotone functions）难以达到这一标准。
- 建议修改方向：(1) 提供更强的理论结果，例如证明 minimum intervention 在某种 regret bound 下是最优的；(2) 或将 positioning 调整为 practical contribution，投 Findings。

**N2** [critical] 实验规模与论文动机严重不匹配

- 具体位置：Section 4（Experimental Setup）+ Section 5（Results）
- 问题：
  - 论文动机聚焦 "web-scale corpora" 的 20-60% synthetic contamination（Abstract 第 1 句，Introduction 第 1-5 段），但主要实验仅在 **Qwen3-0.6B + 132M tokens** 上进行。这与 web-scale（数十 B tokens）差距至少两个数量级。
  - 1.7B 实验为 **单 seed**，且 Δ=-0.01 本质上无改善（Section 5.2）。
  - Llama-3.2-3B 仅在 Limitations 中一笔带过，单 seed，PPL 与 uniform 持平。
  - 按 EMNLP 2024-2025 近年论文标准，data curation / training strategy 论文通常至少在 1B+ scale 有 3-seed 结果，或在多个 benchmark 上展示显著改善。
- 为什么影响接收：审稿人无法判断该方法在实际规模下是否有效。0.6B 的微弱改善可能在 scale up 后消失。
- 建议修改方向：至少在 1.7B 上补充 3-seed 实验；或在更大数据规模（>1B tokens）上验证。

**N3** [critical] 效果量极小，且 downstream 无改善

- 具体位置：Table 2（main results）、Appendix Table 5（downstream）
- 问题：
  - ρ=0.4 时，Adaptive vs Uniform 的 PPL 改善为 **0.043**（17.651 vs 17.694），相对改善 **0.24%**。论文 Limitations 自己承认 "modest in absolute terms"。
  - ρ=0.6 时改善缩小到 0.027。
  - **Downstream benchmarks（Table 5）显示 4/5 任务 Adaptive 略差于 Uniform**（ARC-Challenge -0.005, ARC-Easy -0.007, HellaSwag -0.005, WinoGrande -0.008），仅 PIQA +0.001。这直接削弱了 "PPL improvement translates to practical gains" 的论点。
  - 与 Grid-best 的比较（gap 0.031，95% CI [-0.039, 0.101]）包含零，无法排除 Adaptive 劣于 Grid-best 的可能。
- 为什么影响接收：微弱的 PPL 改善 + downstream 全面微弱劣化 = 实际价值存疑。论文的核心卖点是 "one run instead of nine"，但如果改善本身不重要（downstream 无增益），那么省去 grid search 的价值也大打折扣。
- 建议修改方向：(1) 在 downstream 上做 3-seed 统计检验；(2) 或显式定位为 "equivalent performance at lower search cost" 而非 "improvement"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 人造 contamination 不代表真实场景

- 具体位置：Section 4 第 1 段（Training Data）
- 问题：论文使用 Qwen3-0.6B 自身生成 synthetic data，以已知 ρ=0.4 均匀混入。真实 web contamination 的特征是：(1) contamination ratio 未知且非均匀，(2) 多源多模型生成，(3) domain-skewed 分布。论文在 Limitations 中承认了这一点，但这影响所有实验结论的外部效度。
- 建议：增加至少一个 "naturally contaminated" 或 multi-source contamination 实验，哪怕是 ablation 级别的。

**W2** [warning] Abstract 超长，数据堆砌

- 具体位置：sections/abstract.tex
- 问题：Abstract 约 **291 words**，超过 ACL 建议的 150-250 words。更关键的是，Abstract 读起来像 Results 的缩写而非一个引人入胜的 story：连续列举了 PPL 数字（17.651 vs 17.620）、CI（[-0.039, 0.101]）、ablation 排序（Random, ESS-only, Uniform）、epoch-matched 结果、τ range、detector AUC。这违反了 "审稿人 30 秒内判断价值" 的原则。
- 建议：精简至 200 words 以内，保留 problem-method-key finding，删减具体数字。

**W3** [warning] 引用数量偏少，遗漏重要 related work

- 具体位置：Section 2（Related Work）、references.bib
- 问题：
  - 当前 **39 条引用**，EMNLP 长文通常 40-60+。
  - 遗漏的重要工作：
    - **DCLM** (Li et al., 2024) — classifier-based quality filtering 的标准 benchmark，与本文的 TF-IDF+LR 方法直接相关
    - **QuRating** (Wettig et al., 2024) — LLM-based data quality scoring，另一种 instance-level weighting 范式
    - **OLMo** (Groeneveld et al., 2024) 及其数据 pipeline — 开源 pretraining 中 data curation 的标杆
    - 近期 model collapse 理论工作如 **Dohmatob et al. (2024, "Tale of Tails")** 等后续分析
    - **Influence function** 相关的 data selection 方法（如 LESS, Xia et al. 2024）
  - Related Work 中 "Data Mixing and Instance-Level Reweighting" 段过于密集（Section 2 第 23-31 行），在一段中引用了 12 篇论文，呈堆砌式。
- 建议：增加 5-10 条关键引用，将 "Data Mixing" 段拆分为 domain-level 和 instance-level 两段。

**W4** [warning] Discussion 过于单薄

- 具体位置：Section 6（Discussion），仅 20 行
- 问题：Discussion 基本是 Results 的重述（"minimum intervention works"、"advantage manifests at evaluation"、"τ as a practical dial"、"detector signal semantics"、"filtering vs reweighting"），缺少更深层的分析：
  - 为什么 discriminative vs generative detector 的差异如此大？是否有理论解释？
  - Minimum intervention 在什么条件下会失败？
  - 与 curriculum learning 的联系？
  - 对更大规模 pretraining 的 implications？
- 建议：增加对 detector signal semantics 的深入分析，以及对方法局限性的理论讨论。

**W5** [warning] "Minimum Intervention Principle" 的 framing 过度

- 具体位置：论文标题、Abstract、Section 3.2
- 问题：论文将 "选择满足约束的最小 b" 包装为一个 "principle"，但这在约束优化中是 trivial 的：任何优化问题的最优解如果在约束边界上，自然就是 "minimum intervention"。将标准做法命名为 "principle" 并贯穿全文，有 rebranding 嫌疑。
- 建议：弱化措辞，如 "conservative selection strategy" 或 "minimal sufficient intervention"，避免暗示这是一个新的优化原则。

**W6** [warning] ECE 缩写未定义

- 具体位置：首次出现在 Introduction（第 25 行）、Method（第 32 行）、Experiments（第 7 行）
- 问题：ECE（Expected Calibration Error）在多处使用但从未给出全称定义。对非 calibration 领域的读者不够友好。
- 建议：首次出现时写 "Expected Calibration Error (ECE)"。

---

## 小问题（不影响接收）

- **M1**: Limitations 中提到 "Cross-model transfer (Llama-3.2-3B, single seed)" 但正文中从未介绍这个实验的设置。应在 Experiments 或 Appendix 中补充。
- **M2**: Table 2 中 Golden Ratio 和 D&R 的标注符号（†, ‡, §）较多，略显混乱。
- **M3**: references.bib 中 `vehtari2024psis` 的年份与 OpenAlex 记录不一致（bib 写 2024，实际初版 2015）；`alemohammad2024mad` 的 first author 与 API 记录不一致。
- **M4**: 缺少 ACL Responsible NLP Research Checklist。ACL ARR 2025+ 要求作者提交 checklist，遗漏可能导致 desk reject。
- **M5**: 少量 -ing 分词短语结尾（如 "confirming that...", "suggesting that...", "indicating an effective range..."），虽非严重 AI 写作痕迹，但可适当改写。
- **M6**: 论文未提供代码或数据链接（可能出于 double-blind 考虑，但应在 checklist 中说明 reproducibility 计划）。

---

## 主要优势

1. **问题重要且及时**：web-scale synthetic contamination 是当前 pretraining 的现实挑战，detect-and-reweight 的超参数选择是一个真实痛点。
2. **方法清晰**：数学推导干净，Algorithm 1 可直接实现，两个超参数有 principled defaults。
3. **实验设计诚实**：epoch-matched control 揭示 D&R 优势来自 multi-epoch exposure 是一个有价值的发现；Limitations 对效果量、规模限制的坦诚讨论令人赞赏。
4. **Detector signal type 发现**：discriminative vs generative detector 的差异（Section 5.2）是一个有趣的 empirical observation，尽管只测了 3 个 detector。
5. **写作质量高**：叙事一致，无 AI 写作痕迹（无 em-dash/en-dash），排版符合 ACL 模板要求，正文恰好 8 页。
6. **格式基本合规**：ACL template with [review] option，double-blind（Author = Anonymous），Limitations section 在正文后、References 前。

---

## 缺失引用（建议补充）

1. Li et al. (2024) "DataComp-LM" 的后续 DCLM 数据集和 classifier-based filtering pipeline
2. Wettig et al. (2024) "QuRating: Selecting High-Quality Data for Training Language Models"
3. Groeneveld et al. (2024) "OLMo: Accelerating the Science of Language Models" 及其 data pipeline
4. Xia et al. (2024) "LESS: Selecting Influential Data for Targeted Instruction Tuning"
5. Dohmatob et al. (2024) "A Tale of Tails" (model collapse 的后续理论分析)
6. Gerstgrasser et al. (2024) "Is Model Collapse Inevitable?" — 关于 model collapse 缓解条件的理论分析

---

## Overall Assessment

**评分**: 2.5/5
**置信度**: 4/5

本文解决了一个真实问题（detect-and-reweight 的超参数选择），方法正确且写作诚实。但核心技术贡献（对已有公式的自动调参）的新颖性有限，实验规模（0.6B/132M tokens）与论文动机（web-scale contamination）严重脱节，效果量极小（0.24% PPL, downstream 无改善）。在当前状态下，更适合 **ACL Findings** 而非 EMNLP Main Conference。

若要冲击 Main Conference，需要：(1) 在 ≥1B scale 补充 multi-seed 实验；(2) 提供 downstream 改善的统计证据；(3) 增加 naturally contaminated data 实验；(4) 加强理论贡献（如 minimum intervention 的最优性证明）。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-19T04:39:17.577039+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Step 2 — 交叉评审：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的意见。对每个 Must-Fix、Should-Fix 和关键判断，用 **[AGREE]** 或 **[REBUT]** 标注你的立场，并说明理由。如果你 REBUT，请引用论文中的具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 2 的完整审稿报告：\n\n### Overall: 2.5/5（Findings/borderline reject）\nSoundness 3.0/5, Excitement 2.0/5, Reproducibility 4.0/5, Confidence 4/5\n\n### Must-Fix 问题\n\n**R2-N1** [critical] 新颖性不足以支撑 EMNLP Main Conference\n- 核心加权公式 w=(1-q)^b 完全来自 Drayson 2025\n- Dual constraint 的两个组件（α_eff 加权平均 + ESS Kish 1965）均为标准工具\n- \"Minimum intervention principle\" 是标准约束优化的 rebranding\n- 增量贡献可概括为：对已有公式的自动超参数选择程序\n- EMNLP Main 要求 \"transformational value\" 或显著方法论创新\n\n**R2-N2** [critical] 实验规模与论文动机严重不匹配\n- 论文动机聚焦 web-scale（数十B tokens），但主要实验仅 0.6B + 132M tokens\n- 1.7B 单 seed，Δ=-0.01 无改善\n- Llama-3.2-3B 仅在 Limitations 一笔带过\n- EMNLP 2024-2025 data curation 论文通常至少 1B+ scale 有 3-seed 结果\n\n**R2-N3** [critical] 效果量极小，且 downstream 无改善\n- PPL 改善 0.043（0.24% relative）\n- Downstream 4/5 任务 Adaptive 略差于 Uniform\n- Grid-best CI [-0.039, 0.101] 包含零\n- 如果改善本身不重要，省去 grid search 的价值也大打折扣\n\n### Should-Fix 问题\n\n**R2-W1** 人造 contamination 不代表真实场景（自污染 + 已知 ρ 均匀混入 vs 真实 multi-source unknown）\n**R2-W2** Abstract 超长（~291 words > 250 建议上限），数据堆砌而非叙事\n**R2-W3** 引用偏少（~39 条），遗漏 DCLM、QuRating、OLMo、LESS、Tale of Tails、Gerstgrasser 2024\n**R2-W4** Discussion 过于单薄（仅 20 行，基本是 Results 重述）\n**R2-W5** \"Minimum Intervention Principle\" framing 过度，标准约束优化不应命名为 \"principle\"\n**R2-W6** ECE 缩写未定义\n\n### 关键判断\n- Reviewer 2 认为 Excitement 仅 2.0/5，核心理由是 \"对已有公式的自动调参，novelty 更接近 Findings 水平\"\n- Reviewer 2 认为 epoch-matched control 和 detector signal type 发现有价值，但不足以弥补 novelty 不足\n\n---\n\n请对以上所有 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT]，重点关注你与 Reviewer 2 在 novelty 评估和 excitement 分数上是否一致。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Step 2 — 交叉评审：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的意见。对每个 Must-Fix、Should-Fix 和关键判断，用 **[AGREE]** 或 **[REBUT]** 标注你的立场，并说明理由。如果你 REBUT，请引用论文中的具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 2 的完整审稿报告：\n\n### Overall: 2.5/5（Findings/borderline reject）\nSoundness 3.0/5, Excitement 2.0/5, Reproducibility 4.0/5, Confidence 4/5\n\n### Must-Fix 问题\n\n**R2-N1** [critical] 新颖性不足以支撑 EMNLP Main Conference\n- 核心加权公式 w=(1-q)^b 完全来自 Drayson 2025\n- Dual constraint 的两个组件（α_eff 加权平均 + ESS Kish 1965）均为标准工具\n- \"Minimum intervention principle\" 是标准约束优化的 rebranding\n- 增量贡献可概括为：对已有公式的自动超参数选择程序\n- EMNLP Main 要求 \"transformational value\" 或显著方法论创新\n\n**R2-N2** [critical] 实验规模与论文动机严重不匹配\n- 论文动机聚焦 web-scale（数十B tokens），但主要实验仅 0.6B + 132M tokens\n- 1.7B 单 seed，Δ=-0.01 无改善\n- Llama-3.2-3B 仅在 Limitations 一笔带过\n- EMNLP 2024-2025 data curation 论文通常至少 1B+ scale 有 3-seed 结果\n\n**R2-N3** [critical] 效果量极小，且 downstream 无改善\n- PPL 改善 0.043（0.24% relative）\n- Downstream 4/5 任务 Adaptive 略差于 Uniform\n- Grid-best CI [-0.039, 0.101] 包含零\n- 如果改善本身不重要，省去 grid search 的价值也大打折扣\n\n### Should-Fix 问题\n\n**R2-W1** 人造 contamination 不代表真实场景（自污染 + 已知 ρ 均匀混入 vs 真实 multi-source unknown）\n**R2-W2** Abstract 超长（~291 words > 250 建议上限），数据堆砌而非叙事\n**R2-W3** 引用偏少（~39 条），遗漏 DCLM、QuRating、OLMo、LESS、Tale of Tails、Gerstgrasser 2024\n**R2-W4** Discussion 过于单薄（仅 20 行，基本是 Results 重述）\n**R2-W5** \"Minimum Intervention Principle\" framing 过度，标准约束优化不应命名为 \"principle\"\n**R2-W6** ECE 缩写未定义\n\n### 关键判断\n- Reviewer 2 认为 Excitement 仅 2.0/5，核心理由是 \"对已有公式的自动调参，novelty 更接近 Findings 水平\"\n- Reviewer 2 认为 epoch-matched control 和 detector signal type 发现有价值，但不足以弥补 novelty 不足\n\n---\n\n请对以上所有 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT]，重点关注你与 Reviewer 2 在 novelty 评估和 excitement 分数上是否一致。"
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-19T04:39:45.059500+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 27482
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-19T04:39:45.213150+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Step 2 — 交叉评审：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的意见。对每个 Must-Fix、Should-Fix 和关键判断，用 **[AGREE]** 或 **[REBUT]** 标注你的立场，并说明理由。如果你 REBUT，请引用论文中的具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 1 的完整审稿报告：\n\n### Overall: 3.0/5 (Findings)\nSoundness 3/5, Excitement 3/5, Confidence 4/5\n\n### Must-Fix 问题\n\n**R1-N1** [critical] 核心 claim 的统计支撑不足：N=3 下的推断力度\n- Adaptive vs Grid-best 95% CI [-0.039, 0.101] 跨越零且包含 degradation\n- 论文诚实承认 \"too wide for formal equivalence testing\"\n- 但 Abstract 仍称 \"achieves PPL competitive with the grid-searched optimum\"\n- N=3 的 statistical power 极低（对 0.03 量级 effect size，power 远低于 0.5）\n- Adaptive vs Uniform Δ=0.043 虽 p<0.003，但绝对量级仅 0.24% relative\n\n**R1-N2** [critical] 理论基础与经验超参之间的断联\n- α_eff ≥ τ 的理论 motivation 来自 Wang 2026 收敛理论（假设已知精确 α）\n- τ=0.8 完全基于 seed 42 sweep\n- \"principled defaults\" 暗示比实际更强的理论保证\n- τ 最优值随 ρ 变化（0.8 → 0.7），削弱 \"zero validation cost\"\n\n**R1-N3** [critical] 1.7B 结果不支持 \"transfers without degradation\"\n- 单 seed，Δ=-0.01 几乎为零\n- \"Transfers without degradation\" 同样可解读为 \"no effect at this scale\"\n- Limitations 更谨慎但 Abstract/Conclusion 过度表述\n\n### Should-Fix 问题\n\n**R1-W1** 自污染设定的外部有效性（同你的 W1）\n**R1-W2** Downstream 4/5 略差，distribution matching artifact 风险（同你的 N3）\n**R1-W3** ρ=0.2 失效的讨论不充分（主文完全未提）\n**R1-W4** Micro-batch (B=4) 级别 b* 决策的合理性（α_eff 仅 5 个离散值，MAE=0.114）\n**R1-W5** Proposition 1 证明表述误导（r_i=1[q_i≤0.5] 使 Cov≥0 是定义恒等式，非检测器质量依赖）\n\n### 关键差异\n- Reviewer 1 给 Excitement 3/5（vs 你的 2.0/5），认为 \"minimum intervention 视角有新意\" + \"detector signal type 发现有启发性\"\n- Reviewer 1 的 Soundness 3/5 与你相同\n- Reviewer 1 结论是 \"Findings borderline\"，你是 \"Findings/borderline reject\"\n\n### R1 独有的发现（你未提及）\n- ρ=0.2 失效机制的详细分析请求（如果 α_eff(0)≈0.8≥τ 则大部分 batch b*=0，为什么 PPL 更差？）\n- Micro-batch vs effective-batch 的设计选择问题\n- Proposition 1 proof sketch 的逻辑误导（tautological covariance）\n- Hybrid method (Table 4) 17.514 显著优于 pure adaptive 但未被推荐为主方法的疑问\n\n---\n\n请对以上所有 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT]，重点关注：\n1. 你是否同意 Reviewer 1 对 Excitement 3/5 的评价（vs 你的 2.0/5）？\n2. Reviewer 1 提出的 ρ=0.2 失效机制和 micro-batch 问题，你是否认为也应纳入 Must-Fix？\n3. Proposition 1 的 tautological covariance 问题你是否认同？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Step 2 — 交叉评审：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的意见。对每个 Must-Fix、Should-Fix 和关键判断，用 **[AGREE]** 或 **[REBUT]** 标注你的立场，并说明理由。如果你 REBUT，请引用论文中的具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 1 的完整审稿报告：\n\n### Overall: 3.0/5 (Findings)\nSoundness 3/5, Excitement 3/5, Confidence 4/5\n\n### Must-Fix 问题\n\n**R1-N1** [critical] 核心 claim 的统计支撑不足：N=3 下的推断力度\n- Adaptive vs Grid-best 95% CI [-0.039, 0.101] 跨越零且包含 degradation\n- 论文诚实承认 \"too wide for formal equivalence testing\"\n- 但 Abstract 仍称 \"achieves PPL competitive with the grid-searched optimum\"\n- N=3 的 statistical power 极低（对 0.03 量级 effect size，power 远低于 0.5）\n- Adaptive vs Uniform Δ=0.043 虽 p<0.003，但绝对量级仅 0.24% relative\n\n**R1-N2** [critical] 理论基础与经验超参之间的断联\n- α_eff ≥ τ 的理论 motivation 来自 Wang 2026 收敛理论（假设已知精确 α）\n- τ=0.8 完全基于 seed 42 sweep\n- \"principled defaults\" 暗示比实际更强的理论保证\n- τ 最优值随 ρ 变化（0.8 → 0.7），削弱 \"zero validation cost\"\n\n**R1-N3** [critical] 1.7B 结果不支持 \"transfers without degradation\"\n- 单 seed，Δ=-0.01 几乎为零\n- \"Transfers without degradation\" 同样可解读为 \"no effect at this scale\"\n- Limitations 更谨慎但 Abstract/Conclusion 过度表述\n\n### Should-Fix 问题\n\n**R1-W1** 自污染设定的外部有效性（同你的 W1）\n**R1-W2** Downstream 4/5 略差，distribution matching artifact 风险（同你的 N3）\n**R1-W3** ρ=0.2 失效的讨论不充分（主文完全未提）\n**R1-W4** Micro-batch (B=4) 级别 b* 决策的合理性（α_eff 仅 5 个离散值，MAE=0.114）\n**R1-W5** Proposition 1 证明表述误导（r_i=1[q_i≤0.5] 使 Cov≥0 是定义恒等式，非检测器质量依赖）\n\n### 关键差异\n- Reviewer 1 给 Excitement 3/5（vs 你的 2.0/5），认为 \"minimum intervention 视角有新意\" + \"detector signal type 发现有启发性\"\n- Reviewer 1 的 Soundness 3/5 与你相同\n- Reviewer 1 结论是 \"Findings borderline\"，你是 \"Findings/borderline reject\"\n\n### R1 独有的发现（你未提及）\n- ρ=0.2 失效机制的详细分析请求（如果 α_eff(0)≈0.8≥τ 则大部分 batch b*=0，为什么 PPL 更差？）\n- Micro-batch vs effective-batch 的设计选择问题\n- Proposition 1 proof sketch 的逻辑误导（tautological covariance）\n- Hybrid method (Table 4) 17.514 显著优于 pure adaptive 但未被推荐为主方法的疑问\n\n---\n\n请对以上所有 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT]，重点关注：\n1. 你是否同意 Reviewer 1 对 Excitement 3/5 的评价（vs 你的 2.0/5）？\n2. Reviewer 1 提出的 ρ=0.2 失效机制和 micro-batch 问题，你是否认为也应纳入 Must-Fix？\n3. Proposition 1 的 tautological covariance 问题你是否认同？"
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-19T04:39:46.571035+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1357
}
```

</details>

---


### Assistant

_source line 176 · 2026-05-19T04:39:50.830144+00:00_

交叉评审任务已发给两位 Reviewer。等待 [AGREE]/[REBUT] 回应后进入收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 14

## Round 14

2 recorded events


### User

_source line 177 · 2026-05-19T04:39:53.391549+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

总结：论文方法正确、写作诚实，但存在三个 critical 问题：(1) 核心公式来自 Drayson 2025，dual constraint 使用标准 IS 工具，新颖性更接近 Findings 水平；(2) 实验仅在 0.6B/132M tokens 上进行，与 web-scale 动机严重脱节；(3) 效果量极小（0.24% PPL），downstream 4/5 任务略劣于 uniform。整体评分 2.5/5，建议投 Findings 或补充大规模实验后再投 Main。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 178 · 2026-05-19T04:40:01.312416+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 15

## Round 15

2 recorded events


### User

_source line 179 · 2026-05-19T04:41:19.219516+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — 交叉评审回应 Reviewer 2

---

### Must-Fix 逐条回应

**[REBUT] R2-N1: 新颖性不足以支撑 EMNLP Main Conference**

R2 将本文贡献简化为"对已有公式的自动超参数选择程序"，我认为这一概括过于粗暴，遗漏了三个有独立价值的贡献：

1. **Dual-constraint formulation 不是 trivial 的组合**。α_eff 和 ESS 虽然分别是标准工具，但将两者的 opposing monotonicity 形式化为 feasible region [b_τ, b_ESS]，并利用 minimum vs maximum 的选择产生可测量的性能差异（Section 5.1 Table 1: Adaptive 17.651 vs ESS-only 17.737，paired gap 0.086, p<0.01），这一设计选择并非显而易见。R2 说"标准约束优化的 rebranding"，但 ESS-only ablation 的失败恰恰证明约束的选取和优化方向（min vs max）是方法成功的关键。

2. **Epoch-matched control 的实验设计**（Table 2）解决了领域中 D&R vs reweighting 对比的一个系统性 confound，这一分析方法论贡献独立于方法本身。

3. **Detector signal type 发现**（Appendix D, Table 7）揭示 AUC 不是决定因素（GPT-2 AUC=0.91 失败，TF-IDF AUC=0.94 成功），这对后续工作的 detector 选择有实用指导意义。

但我同意 R2 的结论方向：**这些贡献更适合 Findings 而非 Main**。我给 Overall 3.0（Findings），R2 给 2.5（Borderline Findings），分歧在半档。核心方法确实是对已有 weighting scheme 的 hyperparameter automation，Excitement 不足以支撑 Main 是合理判断。

我不同意的是 Excitement 2.0 的评分。Epoch-matched analysis 和 detector-type finding 对领域的实际指导价值使本文值得 "Interesting"（3.0），而非 "Potentially Interesting"（2.0）。

---

**[AGREE] R2-N2: 实验规模与论文动机严重不匹配**

完全同意。论文 Introduction 以 "web corpora now contain an estimated 20-60% machine-generated text"（Section 1, 第1行）开篇，framing 是 web-scale 问题，但实验仅 0.6B model + 132M tokens，与 web-scale pretraining（通常 1T+ tokens）相差 4 个数量级。

我在自己的审稿中将此归入 N3（1.7B 单 seed 不充分），但 R2 更准确地指出了 framing-experiment gap 这一更根本的问题。补充论据：

- EMNLP/ACL 近期的 data curation 论文如 DataComp-LM（Gadre et al. 2024, 引用于本文）在 billions of tokens 上验证。DoReMi（Xie et al. 2023）同样在 GPT-scale 上验证。
- 本文的 "continued pretraining" 设定（从 pretrained checkpoint 开始）部分缓解了这一问题，但 Introduction 的 framing 并未限定为 continued pretraining。

建议：调整 Introduction framing 使之与实验规模匹配（聚焦 continued pretraining 场景），或增加更大规模实验。

---

**[AGREE] R2-N3: 效果量极小，且 downstream 无改善**

同意，这是我自己 N1 和 W2 的核心关注。补充两点 R2 未提及的论据：

1. **效果量的 contextual significance**：PPL 从 pretrained 22.970 降到 17.65 的 5.3-point drop 是 continued pretraining 的主效应；reweighting 的 0.043 改善仅占此 drop 的 0.8%。在如此窄的 residual margin 中，seed variance（±0.007 to ±0.033）与 method difference（0.031 to 0.043）同量级，方法效果很难与噪声分离。

2. **"省去 grid search" 的价值依赖于效果量**。R2 正确指出：如果改善本身不重要，省去 grid search 的 compute saving 也不重要。9 次 0.6B + 132M tokens 的训练总共约 1.2B tokens 的计算量，在现代标准下是 trivial 的开销。

---

### Should-Fix 逐条回应

**[AGREE] R2-W1: 人造 contamination 不代表真实场景**

同意，与我的 W1 一致。补充：自污染设定（generator = trainee）使得检测器的 task 特别难（AUC 仅 0.939 而非 Drayson 2025 的 0.986），但也特别不现实——真实 web 污染来自多种 generators，distribution 更异质。方法在异质污染下的行为完全未知。

---

**[REBUT] R2-W2: Abstract 超长（~291 words > 250 建议上限），数据堆砌**

部分同意长度问题，但 REBUT "数据堆砌"的判断。

ACL ARR 对 Abstract 长度无硬性上限（ARR CfP 未指定 word count）。实测 Abstract 约 280 words，略超惯例但不构成格式违规。

关于"数据堆砌"：Abstract 中的数字（3-seed means, 95% CI, Δ values, p-values）服务于 claim 的 quantitative substantiation，在 empirical NLP 论文中是标准做法。我的审稿关注点相反——Abstract 中的 claim 措辞可能比数字支撑的更强（如 "competitive with grid-searched optimum" 在 CI 包含零时）。问题不在数字多，而在 claim 与数字的对齐。

建议保留关键数字但精简叙事，目标 230-250 words。

---

**[AGREE] R2-W3: 引用偏少（~39 条），遗漏重要工作**

同意。39 条引用对 EMNLP long paper 偏少（同类论文通常 50-70 条）。R2 提到的遗漏中：

- **Gerstgrasser et al. (2024)** "Is Model Collapse Inevitable?" — 直接挑战 Shumailov 2024 的 inevitability claim，是 model collapse 讨论中不可忽略的反面视角。
- **DCLM (Li et al. 2024)** — 大规模 data curation 的直接 comparable，应在 Related Work "Data Mixing" 段讨论。
- **Tale of Tails (Ionescu et al. 2024)** — 关于 importance weighting 中的 heavy-tail 问题，与 ESS 约束的理论基础直接相关。

我自己指出的遗漏（Gururangan 2020, Wettig 2023）加上 R2 的列表，说明 Related Work 的 coverage 确实不足。

---

**[AGREE] R2-W4: Discussion 过于单薄**

同意。Discussion（Section 6）约 20 行，5 个 paragraph，内容基本是 Results 的重新组织（"why minimum intervention works" 重述 Section 5.3 的 regime analysis，"where advantage manifests" 重述 Section 5.1 的 PPL vs training loss 观察）。缺少的内容包括：

- 方法在什么条件下预期失败（beyond ρ=0.2 的简单 mention）
- 与 importance weighting 理论（Vehtari 2024 PSIS, Pareto-k diagnostic）的深入连接
- 对 "soft vs hard filtering" 更广泛的理论讨论（信息论视角：reweighting 保留了多少信息？）
- 实际部署建议（何时用 adaptive，何时用 D&R，何时不需要干预）

---

**[REBUT] R2-W5: "Minimum Intervention Principle" framing 过度**

部分同意措辞可更审慎，但 REBUT "不应命名为 principle"的判断。

"Principle" 在优化文献中常用于命名设计偏好（如 "principle of maximum entropy", "minimum description length principle", "parsimony principle"），并不要求形式化定理。本文的 minimum intervention 选择（选 b_τ 而非 b_ESS 或中间值）是一个有实验支撑的设计决策：ESS-only（maximum intervention）在 Table 1 中显著更差（17.737 vs 17.651），Section 5.3 量化了 4.9× 过度干预。

问题在于 Introduction 第17行的措辞 "embodying a minimum intervention principle" 可能暗示理论最优性，而实际上只有经验优势。建议将 "principle" 保留但加 qualifier：如 "an empirically motivated minimum intervention principle"。

---

**[AGREE] R2-W6: ECE 缩写未定义**

确认。ECE (Expected Calibration Error) 首次出现在 Section 3.2 第32行（"calibrated ECE=0.048"）和 Section 4 第7行（"calibrated ECE=0.048 after temperature scaling"），均未展开定义。应在首次使用时写全称。

---

### 对 Reviewer 2 关键判断的评估

**Excitement 2.0 vs 我的 3.0**：

R2 的核心理由是 "对已有公式的自动调参，novelty 更接近 Findings"。我同意 novelty assessment（Findings 级别），但认为 Excitement 评分应考虑论文的 "useful insights" 维度，而非仅看 method novelty：

- Epoch-matched control 的实验方法论有示范价值（Section 5.1, Table 2）
- Detector signal type 的发现（discriminative vs generative, Appendix D）对后续工作有直接指导
- τ robustness 分析（Table 3, Figure 4）为实际使用提供了可操作的 guidance

ARR guidelines 明确指出 Excitement "does not necessarily follow what is popular in the field"。这些实验 insights 即使方法 novelty 有限，也值得 3.0（"might mention some points to others"）。2.0 过低。

**Overall 2.5 vs 我的 3.0**：

R2 给 2.5（Borderline Findings），我给 3.0（Findings）。分歧来源是对 epoch-matched control 和 detector-type finding 的权重。我认为这两个分析贡献足以将论文推至 Findings 水平，即使核心方法 novelty 有限。但如果 N2（scale mismatch）不被修复，我也会考虑降至 2.5。

---

### 总结

| R2 编号 | 我的立场 | 核心理由 |
|---------|---------|---------|
| R2-N1 | REBUT（部分） | Novelty 确实 incremental（同意 Findings 级别），但 R2 过度简化了贡献，忽略了 ablation 证据和实验 insights |
| R2-N2 | AGREE | Scale mismatch 是真实问题，framing 与实验不匹配 |
| R2-N3 | AGREE | 效果量过小且 downstream 无改善，与我的 N1/W2 一致 |
| R2-W1 | AGREE | 与我的 W1 一致 |
| R2-W2 | REBUT（部分） | 长度略超但无硬性违规；数字服务于 claim 而非堆砌 |
| R2-W3 | AGREE | 引用确实偏少，遗漏多篇重要工作 |
| R2-W4 | AGREE | Discussion 单薄，缺少深入分析 |
| R2-W5 | REBUT（部分） | "Principle" 措辞在优化文献中有先例，但应加 qualifier |
| R2-W6 | AGREE | ECE 未定义，应修复 |
| Excitement | REBUT | 2.0 过低，实验 insights 值得 3.0 |
| Overall | 半同意 | 3.0 vs 2.5 分歧在半档，如果 scale 不修复可降至 2.5 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 180 · 2026-05-19T04:41:27.395329+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 16

## Round 16

2 recorded events


### User

_source line 181 · 2026-05-19T04:41:29.944657+00:00_

[Reviewer 1 审稿结果]:
交叉评审已提交。

核心立场：与 R2 在 scale mismatch (N2)、effect size (N3)、引用不足 (W3)、Discussion 薄弱 (W4) 上一致；在 novelty 评估 (N1) 和 Excitement 评分上有分歧——R2 将贡献简化为"自动调参"过于粗暴，epoch-matched control 和 detector-type finding 有独立价值，Excitement 应为 3.0 而非 2.0。Overall 分歧半档（我 3.0 Findings vs R2 2.5 Borderline Findings）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 182 · 2026-05-19T04:41:35.210530+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 17

## Round 17

8 recorded events


### User

_source line 183 · 2026-05-19T04:41:56.028980+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 — 交叉评审回应 Reviewer 1

---

### Must-Fix 逐条回应

**[AGREE] R1-N1: 核心 claim 的统计支撑不足**

完全同意。这与我的 N3 指向同一问题但 R1 的切入角度更精准。补充两点：

1. 论文在 Abstract 第 7 行写 "achieves PPL competitive with the grid-searched optimum"，但紧接着给出的 CI [-0.039, 0.101] 的上界 0.101 意味着 Adaptive 可能比 Grid-best **差 0.1 PPL**，这在 0.043 的效果量尺度下是 2.3 倍的 degradation。"Competitive" 这个词在 CI 上界为效果量 2 倍以上时是过度表述。
2. Adaptive vs Uniform 的 p<0.003 看似显著，但 N=3 的 paired t-test 的 distributional assumptions 极强（假设差值正态），而 3 个 seed 无法验证这一假设。Wilcoxon signed-rank test 在 N=3 下甚至无法给出 p<0.05。

**[AGREE] R1-N2: 理论基础与经验超参的断联**

同意，且这是我审稿中未充分强调的问题。R1 精准地指出了论文的一个 framing 矛盾：

- Section 3.2 第 66-67 行引用 Wang 2026 作为 α_eff ≥ τ 的理论 motivation，但 Wang 2026 的收敛理论假设已知精确 contamination proportion α，而本文的核心前提恰好是 α 未知。论文用了理论 motivation 但没有理论 guarantee。
- Section 3.4 第 126-131 行的 τ sweep（Table 3）是 seed 42 单 seed 结果。将此称为 "principled defaults" (Section 3.4 第 124 行) 有误导性。
- Appendix Figure 3（τ-ρ rank preservation）显示 τ 最优从 0.8 (ρ=0.4) 偏移到 0.7 (ρ=0.6)。如果 ρ 未知（论文的基本假设），那么 τ 的选择仍需某种 validation——这削弱了 "zero validation cost" 的 claim (Abstract 第 5 行)。

我建议将此从我的 W 级升为 N 级。

**[AGREE] R1-N3: 1.7B "transfers without degradation" 的过度表述**

完全同意。Section 5.2 第 94 行写 "confirming that the method transfers to larger scale without degradation"，但 Δ=-0.01 在 PPL 13.26 的量级上是 0.08% relative，单 seed 下完全在噪声范围内。

Limitations Section 对此更谨慎（"does not demonstrate a clear advantage at this scale"），但 Abstract 第 9 行和 Conclusion 第 3 行的表述未反映这一 hedging。一个方法在 scale up 后效果从 Δ=-0.043 缩小到 Δ=-0.01（缩小 4 倍），按正常科学解读应该说 "effect diminishes with scale" 而非 "transfers without degradation"。

---

### Should-Fix 逐条回应

**[AGREE] R1-W1: 自污染设定的外部有效性**

与我的 W1 一致，不再赘述。

**[AGREE] R1-W2: Downstream distribution matching artifact**

与我的 N3 后半段一致。补充一点：论文在 Discussion Section 6 第 7 行提到 "the advantage appears entirely at evaluation (PPL)"，这实际上暗示了 distribution matching 的解释——training loss 几乎无差异，只有 held-out PPL（与 training data 同源的 human-only FineWeb）改善。如果评估集换成其他分布，改善可能消失。

**[AGREE] R1-W3: ρ=0.2 失效的讨论不充分**

同意且我在原审中遗漏了这一点。Limitations 第 7 行提到 ρ=0.2 时 PPL +0.046（比 uniform 更差），但主文完全未讨论。R1 的分析方向正确：如果 τ=0.8 而 ρ=0.2 意味着大约 80% 的 batch 已经有 α_eff(0) ≈ 0.8 ≥ τ（即 clean batch），那么 b*=0 应该占主导，方法应退化为 uniform——但 PPL 反而更差（+0.046 而非 ≈0），说明可能有少量 batch 被错误地 intervene（false positive driven over-downweighting）。这是一个值得在主文讨论的 failure mode。

我认为这应当作为 **Should-Fix**（非 Must-Fix），因为 ρ=0.2 场景下 contamination 本身的影响已很小，方法不 work 的实际后果有限。

**[AGREE] R1-W4: Micro-batch B=4 的合理性**

同意这是一个有效的设计质疑。Appendix Table 6 显示 B=4 时 α_eff 只有 5 个离散值 {0, 0.25, 0.5, 0.75, 1.0}，MAE=0.114。Method Section 3.4 第 138 行解释了为什么用 micro-batch 而非 effective-batch（n_min 必须 ≤ B_micro，否则 b*≡0），但这意味着 b* 的选择基于极其粗糙的估计。

论文在 Appendix Table 6 中证明 rank correlation 在 B=4 时就已保持（Spearman r=0.699），但 B=4 对应的 5 个离散 α_eff 值意味着 b* 本质上是在做 5-way 分类而非连续优化——这与 "continuous adaptive selection" 的 framing 不一致。应作为 **Should-Fix**。

**[AGREE] R1-W5: Proposition 1 的 tautological covariance**

这是 R1 最锐利的技术发现，我在原审中完全遗漏了。

Proposition 1 证明 d(α_eff)/db = Cov_π(r_i, ln(1-q_i)) ≥ 0，证明 sketch（Section 3.2 第 56 行）称 "For any detector with better-than-random discrimination, real samples (r_i=1) have q_i ≤ 0.5...so this covariance is non-negative"。

但 r_i **定义为** 1[q_i ≤ 0.5]（Section 3.2 第 23 行）。因此 r_i=1 ⟹ q_i ≤ 0.5 ⟹ ln(1-q_i) ≥ ln(0.5) 是定义的直接推论，与 detector quality 完全无关。该 covariance 对 **任何** q 分布、任何 detector（哪怕完全随机）都非负。"better-than-random discrimination" 这个条件是多余的，给读者一个错误印象：似乎单调性依赖于 detector 质量，但实际上它是 r_i 定义的恒等后果。

这不影响方法的正确性（方法确实 work），但影响论文的 **理论呈现的诚实性**。建议改写为："The monotonicity holds by construction of the indicator r_i = 1[q_i ≤ 0.5]; its practical utility depends on the correlation between q_i and true synthetic provenance."

应作为 **Should-Fix**（影响 soundness 评分但不影响方法本身）。

---

### R1 独有发现的回应

**ρ=0.2 failure mechanism**: [AGREE] 如上 W3 所述，应补充主文讨论。我补充的分析方向：ρ=0.2 下 PPL 反而更差可能因为 detector 的 false positive 在低 contamination 下比例相对更高，导致少数 batch 被错误干预。

**Hybrid method (Table 4) 17.514 vs pure adaptive 17.653**: [AGREE] 这是一个被论文忽略的重要发现。Hybrid（先硬滤 q>0.95 再 adaptive reweight）比 pure adaptive 好 0.139 PPL（相当于 adaptive vs uniform 改善的 3.2 倍）。如果作者不推荐 hybrid 作为主方法，至少应在主文解释为什么——是否因为 hybrid 引入了 threshold calibration 的依赖？但 q>0.95 几乎不需要 calibration。

---

### 三个核心分歧问题的回答

**1. Excitement: R1 的 3/5 vs 我的 2.0/5**

维持 2.0/5，但可接受折中至 **2.5/5**。

R1 认为 "minimum intervention 视角有新意"——我不同意。如 N1 所述，在单调函数上求满足约束的 infimum 是标准做法，将其命名为 "principle" 并不增加学术贡献。

R1 认为 "detector signal type 发现有启发性"——部分同意。Discriminative vs generative detector 的对比（Table 7, Appendix）确实有实践价值，但只测了 3 个 detector，不足以建立因果（可能是 calibration 差异而非 signal type 差异）。论文自己在 Limitations 中承认 "three detectors from two families cannot distinguish a type effect from a calibration effect"。

综合考虑，2.5/5 是我的上限。核心技术贡献仍然是 "automatic hyperparameter selection for an existing formula"，不构成 EMNLP Main 级别的 excitement。

**2. ρ=0.2 failure 和 micro-batch 是否应纳入 Must-Fix**

两者都应作为 **Should-Fix**，不是 Must-Fix：
- ρ=0.2 failure：方法的适用范围有限是 limitation 而非 flaw，且 Limitations 中已提及（虽然主文未讨论）。
- Micro-batch B=4：论文在多个 batch size（B=4,8,16）上验证了 PPL 差异 <0.01（Section 5.3 第 112 行），说明离散化带来的噪声在实践中被 averaging 吸收。

**3. Proposition 1 tautological covariance**

**完全同意 R1**，如 W5 所述。这是一个 soundness/presentation 问题而非 correctness 问题。证明本身正确，但 "better-than-random discrimination" 的条件是误导性的——单调性不依赖于此条件。建议升为 Should-Fix 级别。

---

### 修订后的总体判断

考虑 R1 的补充意见后，我略微上调评分：

**Overall: 2.5/5 → 维持 2.5/5**（Findings 或 borderline reject）

R1 的补充发现（ρ=0.2 failure, Proposition 1 tautology, hybrid 遗漏）进一步暴露了论文的问题，不支持上调。R1 的 Excitement 3/5 有一定道理（detector type finding），但不足以改变 overall 判断。

**共识**: 两位 reviewer 均认为论文在当前状态下不适合 EMNLP Main Conference，更适合 Findings。核心分歧仅在 excitement（R1: 3/5, R2: 2.0-2.5/5），overall 判断一致（R1: 3.0/5 Findings borderline, R2: 2.5/5 Findings-to-reject）。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-19T04:42:21.314580+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-19T04:42:21.315389+00:00_

1	- id: "RR-W1"
2	  summary: "Paper claims 'from random initialization' but code uses from_pretrained() — actually continued pretraining"
3	  category: writing
4	  severity: warning
5	  status: resolved
6	  first_raised_round: 1
7	  last_seen_round: 2
8	  mentions:
9	    - round: 1
10	      reviewers: [research_reviewer]
11	      note: "Two independent reviews confirmed: pretrain_weighted.py L318 uses from_pretrained(), model.safetensors 1.5GB = full pretrained weights"
12	    - round: 2
13	      reviewers: [R1, R2]
14	      note: "Both reviewers confirm fixed: Abstract line 7, Introduction line 23, Experiments line 12 now say 'continued pretraining'"
15	  action_items:
16	    - round: 1
17	      action: "Fix paper text: 'pretrain from random initialization' → 'continue pretraining Qwen3-0.6B'"
18	      assigned_to: paper_agent
19	      status: done
20	    - round: 1
21	      action: "Run baseline PPL eval on untrained Qwen3-0.6B checkpoint to quantify absolute improvement"
22	      assigned_to: main_agent
23	      status: done
24	  resolution: "Fixed in current version: Abstract, Introduction, Experiments all use 'continued pretraining'"
25	  resolution_round: 2
26	
27	- id: "RR-W2"
28	  summary: "Paper claims 'balanced real/synthetic test set' but eval_holdout.jsonl is human-only (FineWeb)"
29	  category: writing
30	  severity: warning
31	  status: resolved
32	  first_raised_round: 1
33	  last_seen_round: 2
34	  mentions:
35	    - round: 1
36	      reviewers: [research_reviewer]
37	      note: "eval_holdout.jsonl: 67823 lines, all source=fineweb depth=0, zero synthetic samples"
38	    - round: 2
39	      reviewers: [R1, R2]
40	      note: "Both reviewers confirm fixed: Experiments line 16 now says 'containing only human-authored text'"
41	  action_items:
42	    - round: 1
43	      action: "Fix paper text: 'balanced real/synthetic test set' → 'human-only test set drawn from FineWeb'"
44	      assigned_to: paper_agent
45	      status: done
46	  resolution: "Fixed in
…[truncated 13591 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-19T04:46:05.287342+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "provenance_weight_training",
  "issues_yaml": "- id: \"RR-W1\"\n  summary: \"Paper claims 'from random initialization' but code uses from_pretrained() — actually continued pretraining\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [research_reviewer]\n      note: \"Two independent reviews confirmed: pretrain_weighted.py L318 uses from_pretrained(), model.safetensors 1.5GB = full pretrained weights\"\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Both reviewers confirm fixed: Abstract line 7, Introduction line 23, Experiments line 12 now say 'continued pretraining'\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"本轮未提及，已确认修复\"\n  action_items:\n    - round: 1\n      action: \"Fix paper text: 'pretrain from random initialization' → 'continue pretraining Qwen3-0.6B'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 1\n      action: \"Run baseline PPL eval on untrained Qwen3-0.6B checkpoint to quantify absolute improvement\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Fixed in current version: Abstract, Introduction, Experiments all use 'continued pretraining'\"\n  resolution_round: 2\n\n- id: \"RR-W2\"\n  summary: \"Paper claims 'balanced real/synthetic test set' but eval_holdout.jsonl is human-only (FineWeb)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [research_reviewer]\n      note: \"eval_holdout.jsonl: 67823 lines, all source=fineweb depth=0, zero synthetic samples\"\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Both reviewers confirm fixed: Experiments line 16 now says 'containing only human-authored text'\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"本轮未提及，已确认修复\"\n  action_items:\n    - round: 1\n      action: \"Fix paper text: 'balanced real/synthetic test set' → 'human-only test set drawn from FineWeb'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed in current version: Experiments section explicitly states human-only evaluation\"\n  resolution_round: 2\n\n- id: \"R3-N1\"\n  summary: \"Statistical support insufficient: N=3 CI [-0.039, 0.101] includes degradation; 'competitive' is overstatement; downstream 4/5 tasks worse\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"R1-N1: 'statistically indistinguishable' changed to 'competitive'. R1-W1: effect size tiny.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Full consensus. Even 'competitive' overstatement given CI upper bound 0.101 is 2.3x the effect size. N=3 paired t-test assumptions unverifiable. Wilcoxon impossible at N=3. Downstream 4/5 worse suggests distribution matching artifact.\"\n  action_items:\n    - round: 3\n      action: \"Weaken 'competitive with grid-searched optimum' in Abstract/Conclusion to explicitly acknowledge CI includes degradation. Consider 'comparable in magnitude' or 'within the range of grid-searched values'.\"\n      assigned_to: paper_agent\n      status: open\n    - round: 3\n      action: \"Add multi-seed downstream evaluation (≥3 seeds) or add explicit caveat about distribution matching in Abstract/Conclusion\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N2\"\n  summary: \"Theory-empirical disconnect persists: τ=0.8 is empirical but framed as 'principled default'; Wang 2026 requires known α; τ optimal shifts with ρ\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"R1-N2: α_eff motivation disconnected. R2-W3: τ≈1-ρ/2 heuristic deleted, τ=0.8 reframed as universal default.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Full consensus. Three sub-issues: (a) 'principled defaults' (Section 3.5 L124) still overstates — τ=0.8 selected via single-seed sweep (Table 3); (b) Wang 2026 theory requires known α, paper's τ is not derived from theory; (c) Figure 4 shows τ optimal shifts 0.8→0.7 across ρ, undermining 'zero validation cost'. R2 suggests upgrading to critical.\"\n  action_items:\n    - round: 3\n      action: \"Replace 'principled defaults' with 'empirically robust defaults' globally\"\n      assigned_to: paper_agent\n      status: open\n    - round: 3\n      action: \"Add explicit discussion: τ selection replaces b grid search with a less sensitive but still empirical choice; quantify search space reduction (1D τ∈[0.5,0.8] vs 1D b with 9 candidates)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"1.7B 'transfers without degradation' claim unsupported: single seed, Δ=-0.01, effect diminishes 4x from 0.6B\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"R1-N3: external validity insufficient. 1.7B added but single seed.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Full consensus. Abstract L9 and Conclusion L3 say 'transfers without degradation' but single-seed Δ=-0.01 equally supports 'no effect at this scale'. Effect shrinks 4x (0.043→0.01). Limitations hedges correctly but Abstract/Conclusion do not.\"\n  action_items:\n    - round: 3\n      action: \"Add 'single-seed' qualifier in Abstract/Conclusion for 1.7B claim, or add multi-seed 1.7B experiments\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N4\"\n  summary: \"Novelty insufficient for EMNLP Main: core formula from Drayson 2025, dual constraint is standard IS, minimum intervention is standard constrained optimization\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"R2-W1: Novelty relative to Drayson limited. Both agree Findings-level.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"R2: critical — EMNLP Main requires transformational value, this is automatic hyperparameter selection. R1: partial rebut — ESS-only ablation failure is non-trivial insight, epoch-matched control has independent value, but agrees Findings-level. Consensus: contribution is Findings, not Main.\"\n  action_items:\n    - round: 3\n      action: \"Consider repositioning for Findings track, or strengthen theoretical contribution (e.g., regret bound for minimum intervention)\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N5\"\n  summary: \"Scale mismatch: paper frames web-scale (20-60% contamination, trillions of tokens) but experiments only 0.6B/132M tokens\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Full consensus. Introduction L1 opens with web-scale framing, but experiments are 4 orders of magnitude smaller. EMNLP data curation papers (DataComp-LM, DoReMi) validate at billions of tokens. 'Continued pretraining' partially mitigates but Introduction framing is not limited to this.\"\n  action_items:\n    - round: 3\n      action: \"Either narrow Introduction framing to continued-pretraining scenario, or add experiments at ≥1B tokens\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W1\"\n  summary: \"Self-contamination (generator=trainee) external validity: real web contamination is multi-source, multi-model, domain-skewed\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Part of R1-N3 external validity. Llama-3B cross-model shows parity.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Full consensus. Self-contamination makes detection both harder (AUC 0.939 vs Drayson's 0.986) and less realistic. Method behavior under heterogeneous contamination unknown. Llama-3.2-3B mentioned in Limitations only, no table.\"\n  action_items:\n    - round: 3\n      action: \"Add cross-generator experiment or move Llama-3.2-3B results to Appendix with full table\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2\"\n  summary: \"Abstract ~280-291 words, exceeds 250 convention; data-heavy rather than narrative-driven\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"R2: critical — reads like Results summary, violates '30-second value judgment' principle. R1: partial rebut — numbers serve claims, no hard limit in ARR CFP, but agrees should be 230-250 words.\"\n  action_items:\n    - round: 3\n      action: \"Trim Abstract to ≤250 words; keep 2-3 key numbers, remove detailed ablation listings\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W3\"\n  summary: \"Citation coverage still insufficient: ~39 refs vs EMNLP 50-60+ norm; missing DCLM, QuRating, OLMo, LESS, Gerstgrasser 2024, Gururangan 2020\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"R2-W4: was 23 refs, increased to 30, marked resolved.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Now ~39 refs but still below EMNLP norm. Both reviewers independently identify missing works: DCLM (Li 2024), QuRating (Wettig 2024), OLMo (Groeneveld 2024), LESS (Xia 2024), Gerstgrasser 2024 (Is Model Collapse Inevitable?), Gururangan 2020 (Don't Stop Pretraining), Tale of Tails. Related Work 'Data Mixing' paragraph too dense (12 refs in one paragraph).\"\n  action_items:\n    - round: 3\n      action: \"Add 10-15 missing references; split 'Data Mixing' paragraph into domain-level and instance-level subsections\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W4\"\n  summary: \"Discussion section too thin (~20 lines): rehashes Results without deeper analysis\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Full consensus. Missing: failure conditions beyond ρ=0.2 mention, connection to PSIS/Pareto-k diagnostics, information-theoretic view of soft vs hard filtering, deployment guidance (when to use adaptive vs D&R vs no intervention), why discriminative vs generative gap is so large.\"\n  action_items:\n    - round: 3\n      action: \"Expand Discussion with theoretical analysis of failure modes, PSIS connection, and practical deployment guidance\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W5\"\n  summary: \"'Minimum Intervention Principle' framing overstates a standard constrained optimization choice\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"R2: standard optimization, should not be named 'principle'. R1: partial rebut — 'principle' has precedent in optimization literature (max entropy, MDL), but agrees Introduction L17 'embodying a minimum intervention principle' may imply theoretical optimality. Compromise: keep term but add qualifier.\"\n  action_items:\n    - round: 3\n      action: \"Add qualifier: 'empirically motivated minimum intervention principle' or similar hedging\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W6\"\n  summary: \"ρ=0.2 failure (+0.046 PPL) undiscussed in main text; failure mechanism unexplained\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Consensus. Limitations L7 mentions ρ=0.2 failure in one line. R1 analysis: if τ=0.8 and ρ=0.2, most batches have α_eff(0)≈0.8≥τ, so b*=0 should dominate, method should degrade to uniform — but PPL is worse, suggesting false-positive-driven over-intervention in minority of batches. R2: Should-Fix, not Must-Fix, since low-ρ impact is limited.\"\n  action_items:\n    - round: 3\n      action: \"Add ρ=0.2 b* distribution and constraint regime analysis to Discussion or Appendix; explain failure mechanism\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W7\"\n  summary: \"Micro-batch B=4: α_eff has only 5 discrete values (MAE=0.114), 'continuous adaptive selection' framing inconsistent\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Consensus. B=4 means α_eff ∈ {0, 0.25, 0.5, 0.75, 1.0}. b* is effectively 5-way classification, not continuous optimization. Appendix E shows rank correlation preserved (Spearman r=0.699) and PPL differences <0.01 across B∈{4,8,16}, partially mitigating. But design choice of micro-batch vs effective-batch (B=16) not justified.\"\n  action_items:\n    - round: 3\n      action: \"Explain micro-batch vs effective-batch design choice in Method; consider reporting B=16 b* computation results\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W8\"\n  summary: \"Proposition 1 proof sketch misleading: 'better-than-random discrimination' condition is redundant; Cov≥0 is tautological given r_i=1[q_i≤0.5]\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"R1-N2: covariance positivity is by construction. R1-W2: strictly increasing vs non-decreasing (fixed).\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Full consensus (R2 explicitly agrees with R1's analysis). r_i=1[q_i≤0.5] ⟹ r_i=1 ⟹ q_i≤0.5 ⟹ ln(1-q_i)≥ln(0.5) by definition, not detector quality. 'Better-than-random discrimination' condition misleads reader into thinking monotonicity depends on detector quality. Correctness unaffected; presentation honesty issue.\"\n  action_items:\n    - round: 3\n      action: \"Rewrite proof sketch: state monotonicity holds by construction of r_i; move detector-quality requirement to α_eff proxy validity discussion\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W9\"\n  summary: \"ECE (Expected Calibration Error) abbreviation used multiple times without definition\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Consensus. ECE appears in Section 3.2 L32, Section 4 L7, Introduction L25 without full expansion.\"\n  action_items:\n    - round: 3\n      action: \"Define 'Expected Calibration Error (ECE)' at first occurrence\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M1\"\n  summary: \"Responsible NLP Research Checklist missing — required by ACL ARR, may cause desk reject\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R2]\n      note: \"ACL ARR 2025+ requires authors to submit checklist. Omission risks desk reject.\"\n  action_items:\n    - round: 3\n      action: \"Complete and include Responsible NLP Research Checklist\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M2\"\n  summary: \"Hybrid method (q>0.95 filtering + adaptive) achieves 17.514 vs pure adaptive 17.653 but not discussed as recommended approach\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Both note in cross-review. Hybrid PPL 0.139 better than pure adaptive (3.2x the adaptive-vs-uniform gain). If q>0.95 threshold needs minimal calibration, why not recommend hybrid? At minimum, explain in main text why pure adaptive is preferred.\"\n  action_items:\n    - round: 3\n      action: \"Discuss hybrid in main text: explain why pure adaptive preferred despite hybrid's superior PPL, or adopt hybrid as recommended variant\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M3\"\n  summary: \"Detector training details insufficient for reproducibility (TF-IDF features, LR hyperparams, calibration set size, synthetic generation params)\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1]\n      note: \"Missing: TF-IDF n-gram range, max_features, sublinear_tf; LR C/solver/max_iter; calibration validation set size; synthetic continuation prompt format and decoding params.\"\n  action_items:\n    - round: 3\n      action: \"Add detector and data generation hyperparameters to Appendix\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M4\"\n  summary: \"Llama-3.2-3B cross-model results in Limitations text only — no table, no Appendix, unverifiable\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Limitations mentions Llama-3.2-3B parity with uniform on PPL/HellaSwag and +1.6pp MMLU, but no table or appendix entry.\"\n  action_items:\n    - round: 3\n      action: \"Move Llama-3.2-3B results to Appendix with full breakdown table\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M5\"\n  summary: \"Reference issues: lin2017focal venue type, vehtari2024psis year discrepancy with OpenAlex\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"R2-M3: vehtari2024psis year uncertain. guo2025escaping phantom (resolved R2).\"\n    - round: 3\n      reviewers: [R1]\n      note: \"lin2017focal: bib type=article but venue=ICCV, should be inproceedings. vehtari2024psis: bib=2024 vs OpenAlex=2015 (JMLR formal pub may differ from preprint).\"\n  action_items:\n    - round: 3\n      action: \"Fix lin2017focal to inproceedings; verify vehtari2024psis publication year\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# Legacy issues from rounds 1-2 (status tracking)\n- id: \"R1-N1\"\n  summary: \"'Statistically indistinguishable' claim uses failure-to-reject (p=0.30, N=3) instead of equivalence test (TOST)\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Full consensus. p=0.30 only means failure to reject H0, not evidence of equivalence. N=3 has extremely low statistical power.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Paper changed 'statistically indistinguishable' to 'competitive' and reports 95% CI. But 'competitive' still overstatement given CI includes degradation. See R3-N1.\"\n  action_items:\n    - round: 2\n      action: \"Replace 'statistically indistinguishable' globally with 'comparable' or 'competitive without hyperparameter search'. Report 95% CI, state N=3 insufficient for TOST.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Wording changed but remaining issues tracked in R3-N1\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"α_eff theoretical motivation (true α) disconnected from computation (r_i = 1[q_i ≤ 0.5]); Proposition 1 covariance is tautological\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Full consensus. Two issues: (a) no error bound for α_eff vs true α; (b) covariance positivity is by construction.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"α_eff proxy validation added (Appendix E, Pearson r≈0.70, bias -0.03). Partially addresses (a). Proposition 1 tautology (b) still present. See R3-N2 and R3-W8.\"\n  action_items:\n    - round: 2\n      action: \"Paper: add discussion of α_eff as proxy with detector-quality caveat; cite Guo 2017 calibration; add Appendix table with bs=4/8/16 correlation data\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Proxy validation added. Remaining issues tracked in R3-N2 (theory disconnect) and R3-W8 (proof presentation)\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"Experimental external validity insufficient: single model/detector/data/contamination-type\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Full consensus. Drayson tested 160M/360M/1.7B; this paper has far less coverage.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Improvements: 1.7B added (single seed), 3 detectors tested, D&R epoch-matched 3-seed, threshold curve. Remaining: 1.7B single seed, Llama-3B only in Limitations text, no cross-generator experiment. See R3-N3, R3-N5, R3-W1.\"\n  action_items:\n    - round: 2\n      action: \"Multi-model 3-seed and neural detector: cannot complete in 6 days, acknowledge in Limitations\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Partially addressed. Remaining gaps tracked in R3-N3 (1.7B claim), R3-N5 (scale), R3-W1 (self-contamination)\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"Hard filtering crushes reweighting (17.290 vs 17.651); undermines motivation\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [research_reviewer]\n      note: \"D082 definitive: epoch-matched D&R 3-seed 17.657±0.006 ≈ Adaptive 17.651±0.007 (gap 0.006). D&R's 0.36 PPL advantage was ENTIRELY from 2.4× multi-epoch confound.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Epoch-matched control (Table 2) successfully resolves the confound. Both reviewers praise this analysis. Issue substantially addressed in current version.\"\n  action_items:\n    - round: 2\n      action: \"Paper: add distribution matching + multi-epoch confound discussion\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Epoch-matched 3-seed Table 2 resolves the confound convincingly. Both R3 reviewers cite this as a strength.\"\n  resolution_round: 3\n\n- id: \"R1-W1\"\n  summary: \"Effect size tiny (0.043 PPL) with downstream 4/5 benchmarks slightly worse; framing mismatch\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Full consensus. Suggest re-framing as 'matching grid-search at zero validation cost'.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Reframing done but effect size concern persists and is now escalated. See R3-N1.\"\n  action_items:\n    - round: 2\n      action: \"Reframe: 'automatic exponent selection eliminating grid search cost'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reframing done. Remaining concerns tracked in R3-N1.\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Proposition 1 proof gap: strictly increasing vs non-decreasing\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. Fixable.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"本轮确认已修复：Proposition 1 now states 'non-decreasing' with condition for strict increase\"\n  action_items:\n    - round: 2\n      action: \"Add non-degenerate batch condition for strict positivity, or relabel as non-decreasing\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed: Proposition 1 correctly states non-decreasing with strict condition\"\n  resolution_round: 3\n\n- id: \"R1-W3\"\n  summary: \"ESS monotonicity not formally proven; citation too vague\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Minor divergence on severity but agree current citation insufficient.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"本轮确认已修复：Appendix now contains Proposition 2 (ESS monotonicity) with full proof\"\n  action_items:\n    - round: 2\n      action: \"Add specific lemma/theorem reference (Kish 1965, Owen 2013 Ch9) or brief Appendix proof\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed: Proposition 2 with full Herfindahl-index proof in Appendix A\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"Grid-b post-hoc oracle: best b selected on test set gives unfair advantage\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. R2: reverse direction favors paper.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"本轮确认：Table 1 footnote ‡ now says 'Post-hoc oracle'. Bidirectional discussion present.\"\n  action_items:\n    - round: 2\n      action: \"Add bidirectional discussion: post-hoc oracle helps grid-best, but realistic val-based selection would be worse\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Partially addressed: footnote marks oracle, text discusses. Minor residual: R1-M1 notes D&R q>0.3 also post-hoc but not annotated as oracle.\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"D&R and Golden Ratio baselines only seed 42; no multi-seed comparison\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. At minimum D&R needs 3-seed.\"\n    - round: 2\n      reviewers: [research_reviewer]\n      note: \"D082: epoch-matched D&R 3-seed complete\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"D&R epoch-matched 3-seed in Table 2. Golden Ratio still single seed (noted as minor).\"\n  action_items:\n    - round: 2\n      action: \"D&R q>0.5 seed123/456\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"D&R epoch-matched 3-seed complete. Golden Ratio single seed acknowledged in footnote.\"\n  resolution_round: 2\n\n- id: \"R2-W1\"\n  summary: \"Novelty relative to Drayson limited — core formula borrowed, dual constraint standard IS\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Divergence: R2 trivial vs R1 non-trivial insight. Both agree Findings-level.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Escalated to critical in R3-N4. R2 maintains 'automatic hyperparameter selection', R1 acknowledges but values ablation evidence.\"\n  action_items:\n    - round: 2\n      action: \"Clarify unique aspects: ESS-only counter-intuitive failure + regime analysis\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Clarification added but fundamental novelty concern remains. See R3-N4.\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"τ depends on ρ (0.8→0.7), contradicting 'zero validation cost' and ρ-unknown claims\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. τ≈1−ρ/2 heuristic directly contradicts ρ-unknown assumption.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"τ≈1−ρ/2 heuristic deleted, τ=0.8 reframed as universal default. But Figure 4 still shows τ optimal shifts 0.8→0.7 and 'principled defaults' persists. See R3-N2.\"\n  action_items:\n    - round: 2\n      action: \"Delete τ≈1−ρ/2 heuristic. Reframe: τ=0.8 universal default, robust for ρ∈[0.4,0.6]\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Heuristic deleted. Remaining 'principled defaults' wording tracked in R3-N2.\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"Citation density insufficient: 23 refs vs EMNLP 40-60+ norm\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [director_audit]\n      note: \"Increased to 30 refs, all cited.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Now ~39 refs. Still below EMNLP norm. New missing works identified. See R3-W3.\"\n  action_items:\n    - round: 2\n      action: \"Add 15-20 references\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Increased from 23 to 39 but still insufficient. See R3-W3.\"\n  resolution_round: null\n\n- id: \"R2-M1\"\n  summary: \"'five approaches' but lists 6 methods\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Simple count error.\"\n    - round: 3\n      reviewers: []\n      note: \"本轮未提及，已确认修复\"\n  action_items:\n    - round: 2\n      action: \"Fix method count in experiments.tex\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed.\"\n  resolution_round: 2\n\n- id: \"R2-M2\"\n  summary: \"Grid-b values inconsistent across sections (7 vs 9 vs 'nine runs')\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Section 4 lists 7, Appendix has 9.\"\n    - round: 3\n      reviewers: []\n      note: \"本轮未提及，已确认修复\"\n  action_items:\n    - round: 2\n      action: \"Unify grid-b value lists across all sections\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Unified.\"\n  resolution_round: 2\n\n- id: \"R2-M3\"\n  summary: \"Reference issues: guo2025escaping possibly phantom, vehtari2024psis year uncertain\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [director_audit]\n      note: \"guo2025escaping deleted (phantom). vehtari2024psis confirmed.\"\n    - round: 3\n      reviewers: []\n      note: \"guo2025escaping resolved. vehtari2024psis year discrepancy re-raised in R3-M5.\"\n  action_items:\n    - round: 2\n      action: \"Verify via WebSearch; delete if phantom.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"guo2025escaping deleted. vehtari2024psis residual year issue tracked in R3-M5.\"\n  resolution_round: 2\n\n- id: \"R2-M5\"\n  summary: \"Hybrid ρ=0.6 row comparability unclear in Appendix Table 4\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Hybrid changes effective ρ, making comparison misleading.\"\n    - round: 3\n      reviewers: [R2]\n      note: \"Footnote added (*) in Table 4. Partially addressed.\"\n  action_items:\n    - round: 2\n      action: \"Add explicit comparability note in table caption\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Footnote added. Residual hybrid discussion tracked in R3-M2.\"\n  resolution_round: 3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "provenance_weight_training",
    "issues_yaml": "- id: \"RR-W1\"\n  summary: \"Paper claims 'from random initialization' but code uses from_pretrained() — actually continued pretraining\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [research_reviewer]\n      note: \"Two independent reviews confirmed: pretrain_weighted.py L318 uses from_pretrained(), model.safetensors 1.5GB = full pretrained weights\"\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Both reviewers confirm fixed: Abstract line 7, Introduction line 23, Experiments line 12 now say 'continued pretraining'\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"本轮未提及，已确认修复\"\n  action_items:\n    - round: 1\n      action: \"Fix paper text: 'pretrain from random initialization' → 'continue pretraining Qwen3-0.6B'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 1\n      action: \"Run baseline PPL eval on untrained Qwen3-0.6B checkpoint to quantify absolute improvement\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Fixed in current version: Abstract, Introduction, Experiments all use 'continued pretraining'\"\n  resolution_round: 2\n\n- id: \"RR-W2\"\n  summary: \"Paper claims 'balanced real/synthetic test set' but eval_holdout.jsonl is human-only (FineWeb)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [research_reviewer]\n      note: \"eval_holdout.jsonl: 67823 lines, all source=fineweb depth=0, zero synthetic samples\"\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Both reviewers confirm fixed: Experiments line 16 now says 'containing only human-authored text'\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"本轮未提及，已确认修复\"\n  action_items:\n    - round: 1\n      action: \"Fix paper text: 'balanced real/synthetic test set' → 'human-only test set drawn from FineWeb'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed in current version: Experiments section explicitly states human-only evaluation\"\n  resolution_round: 2\n\n- id: \"R3-N1\"\n  summary: \"Statistical support insufficient: N=3 CI [-0.039, 0.101] includes degradation; 'competitive' is overstatement; downstream 4/5 tasks worse\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"R1-N1: 'statistically indistinguishable' changed to 'competitive'. R1-W1: effect size tiny.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Full consensus. Even 'competitive' overstatement given CI upper bound 0.101 is 2.3x the effect size. N=3 paired t-test assumptions unverifiable. Wilcoxon impossible at N=3. Downstream 4/5 worse suggests distribution matching artifact.\"\n  action_items:\n    - round: 3\n      action: \"Weaken 'competitive with grid-searched optimum' in Abstract/Conclusion to explicitly acknowledge CI includes degradation. Consider 'comparable in magnitude' or 'within the range of grid-searched values'.\"\n      assigned_to: paper_agent\n      status: open\n    - round: 3\n      action: \"Add multi-seed downstream evaluation (≥3 seeds) or add explicit caveat about distribution matching in Abstract/Conclusion\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N2\"\n  summary: \"Theory-empirical disconnect persists: τ=0.8 is empirical but framed as 'principled default'; Wang 2026 requires known α; τ optimal shifts with ρ\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"R1-N2: α_eff motivation disconnected. R2-W3: τ≈1-ρ/2 heuristic deleted, τ=0.8 reframed as universal default.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Full consensus. Three sub-issues: (a) 'principled defaults' (Section 3.5 L124) still overstates — τ=0.8 selected via single-seed sweep (Table 3); (b) Wang 2026 theory requires known α, paper's τ is not derived from theory; (c) Figure 4 shows τ optimal shifts 0.8→0.7 across ρ, undermining 'zero validation cost'. R2 suggests upgrading to critical.\"\n  action_items:\n    - round: 3\n      action: \"Replace 'principled defaults' with 'empirically robust defaults' globally\"\n      assigned_to: paper_agent\n      status: open\n    - round: 3\n      action: \"Add explicit discussion: τ selection replaces b grid search with a less sensitive but still empirical choice; quantify search space reduction (1D τ∈[0.5,0.8] vs 1D b with 9 candidates)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"1.7B 'transfers without degradation' claim unsupported: single seed, Δ=-0.01, effect diminishes 4x from 0.6B\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"R1-N3: external validity insufficient. 1.7B added but single seed.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Full consensus. Abstract L9 and Conclusion L3 say 'transfers without degradation' but single-seed Δ=-0.01 equally supports 'no effect at this scale'. Effect shrinks 4x (0.043→0.01). Limitations hedges correctly but Abstract/Conclusion do not.\"\n  action_items:\n    - round: 3\n      action: \"Add 'single-seed' qualifier in Abstract/Conclusion for 1.7B claim, or add multi-seed 1.7B experiments\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N4\"\n  summary: \"Novelty insufficient for EMNLP Main: core formula from Drayson 2025, dual constraint is standard IS, minimum intervention is standard constrained optimization\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"R2-W1: Novelty relative to Drayson limited. Both agree Findings-level.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"R2: critical — EMNLP Main requires transformational value, this is automatic hyperparameter selection. R1: partial rebut — ESS-only ablation failure is non-trivial insight, epoch-matched control has independent value, but agrees Findings-level. Consensus: contribution is Findings, not Main.\"\n  action_items:\n    - round: 3\n      action: \"Consider repositioning for Findings track, or strengthen theoretical contribution (e.g., regret bound for minimum intervention)\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N5\"\n  summary: \"Scale mismatch: paper frames web-scale (20-60% contamination, trillions of tokens) but experiments only 0.6B/132M tokens\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Full consensus. Introduction L1 opens with web-scale framing, but experiments are 4 orders of magnitude smaller. EMNLP data curation papers (DataComp-LM, DoReMi) validate at billions of tokens. 'Continued pretraining' partially mitigates but Introduction framing is not limited to this.\"\n  action_items:\n    - round: 3\n      action: \"Either narrow Introduction framing to continued-pretraining scenario, or add experiments at ≥1B tokens\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W1\"\n  summary: \"Self-contamination (generator=trainee) external validity: real web contamination is multi-source, multi-model, domain-skewed\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Part of R1-N3 external validity. Llama-3B cross-model shows parity.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Full consensus. Self-contamination makes detection both harder (AUC 0.939 vs Drayson's 0.986) and less realistic. Method behavior under heterogeneous contamination unknown. Llama-3.2-3B mentioned in Limitations only, no table.\"\n  action_items:\n    - round: 3\n      action: \"Add cross-generator experiment or move Llama-3.2-3B results to Appendix with full table\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2\"\n  summary: \"Abstract ~280-291 words, exceeds 250 convention; data-heavy rather than narrative-driven\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"R2: critical — reads like Results summary, violates '30-second value judgment' principle. R1: partial rebut — numbers serve claims, no hard limit in ARR CFP, but agrees should be 230-250 words.\"\n  action_items:\n    - round: 3\n      action: \"Trim Abstract to ≤250 words; keep 2-3 key numbers, remove detailed ablation listings\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W3\"\n  summary: \"Citation coverage still insufficient: ~39 refs vs EMNLP 50-60+ norm; missing DCLM, QuRating, OLMo, LESS, Gerstgrasser 2024, Gururangan 2020\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"R2-W4: was 23 refs, increased to 30, marked resolved.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Now ~39 refs but still below EMNLP norm. Both reviewers independently identify missing works: DCLM (Li 2024), QuRating (Wettig 2024), OLMo (Groeneveld 2024), LESS (Xia 2024), Gerstgrasser 2024 (Is Model Collapse Inevitable?), Gururangan 2020 (Don't Stop Pretraining), Tale of Tails. Related Work 'Data Mixing' paragraph too dense (12 refs in one paragraph).\"\n  action_items:\n    - round: 3\n      action: \"Add 10-15 missing references; split 'Data Mixing' paragraph into domain-level and instance-level subsections\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W4\"\n  summary: \"Discussion section too thin (~20 lines): rehashes Results without deeper analysis\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Full consensus. Missing: failure conditions beyond ρ=0.2 mention, connection to PSIS/Pareto-k diagnostics, information-theoretic view of soft vs hard filtering, deployment guidance (when to use adaptive vs D&R vs no intervention), why discriminative vs generative gap is so large.\"\n  action_items:\n    - round: 3\n      action: \"Expand Discussion with theoretical analysis of failure modes, PSIS connection, and practical deployment guidance\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W5\"\n  summary: \"'Minimum Intervention Principle' framing overstates a standard constrained optimization choice\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"R2: standard optimization, should not be named 'principle'. R1: partial rebut — 'principle' has precedent in optimization literature (max entropy, MDL), but agrees Introduction L17 'embodying a minimum intervention principle' may imply theoretical optimality. Compromise: keep term but add qualifier.\"\n  action_items:\n    - round: 3\n      action: \"Add qualifier: 'empirically motivated minimum intervention principle' or similar hedging\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W6\"\n  summary: \"ρ=0.2 failure (+0.046 PPL) undiscussed in main text; failure mechanism unexplained\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Consensus. Limitations L7 mentions ρ=0.2 failure in one line. R1 analysis: if τ=0.8 and ρ=0.2, most batches have α_eff(0)≈0.8≥τ, so b*=0 should dominate, method should degrade to uniform — but PPL is worse, suggesting false-positive-driven over-intervention in minority of batches. R2: Should-Fix, not Must-Fix, since low-ρ impact is limited.\"\n  action_items:\n    - round: 3\n      action: \"Add ρ=0.2 b* distribution and constraint regime analysis to Discussion or Appendix; explain failure mechanism\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W7\"\n  summary: \"Micro-batch B=4: α_eff has only 5 discrete values (MAE=0.114), 'continuous adaptive selection' framing inconsistent\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Consensus. B=4 means α_eff ∈ {0, 0.25, 0.5, 0.75, 1.0}. b* is effectively 5-way classification, not continuous optimization. Appendix E shows rank correlation preserved (Spearman r=0.699) and PPL differences <0.01 across B∈{4,8,16}, partially mitigating. But design choice of micro-batch vs effective-batch (B=16) not justified.\"\n  action_items:\n    - round: 3\n      action: \"Explain micro-batch vs effective-batch design choice in Method; consider reporting B=16 b* computation results\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W8\"\n  summary: \"Proposition 1 proof sketch misleading: 'better-than-random discrimination' condition is redundant; Cov≥0 is tautological given r_i=1[q_i≤0.5]\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"R1-N2: covariance positivity is by construction. R1-W2: strictly increasing vs non-decreasing (fixed).\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Full consensus (R2 explicitly agrees with R1's analysis). r_i=1[q_i≤0.5] ⟹ r_i=1 ⟹ q_i≤0.5 ⟹ ln(1-q_i)≥ln(0.5) by definition, not detector quality. 'Better-than-random discrimination' condition misleads reader into thinking monotonicity depends on detector quality. Correctness unaffected; presentation honesty issue.\"\n  action_items:\n    - round: 3\n      action: \"Rewrite proof sketch: state monotonicity holds by construction of r_i; move detector-quality requirement to α_eff proxy validity discussion\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W9\"\n  summary: \"ECE (Expected Calibration Error) abbreviation used multiple times without definition\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Consensus. ECE appears in Section 3.2 L32, Section 4 L7, Introduction L25 without full expansion.\"\n  action_items:\n    - round: 3\n      action: \"Define 'Expected Calibration Error (ECE)' at first occurrence\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M1\"\n  summary: \"Responsible NLP Research Checklist missing — required by ACL ARR, may cause desk reject\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R2]\n      note: \"ACL ARR 2025+ requires authors to submit checklist. Omission risks desk reject.\"\n  action_items:\n    - round: 3\n      action: \"Complete and include Responsible NLP Research Checklist\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M2\"\n  summary: \"Hybrid method (q>0.95 filtering + adaptive) achieves 17.514 vs pure adaptive 17.653 but not discussed as recommended approach\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Both note in cross-review. Hybrid PPL 0.139 better than pure adaptive (3.2x the adaptive-vs-uniform gain). If q>0.95 threshold needs minimal calibration, why not recommend hybrid? At minimum, explain in main text why pure adaptive is preferred.\"\n  action_items:\n    - round: 3\n      action: \"Discuss hybrid in main text: explain why pure adaptive preferred despite hybrid's superior PPL, or adopt hybrid as recommended variant\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M3\"\n  summary: \"Detector training details insufficient for reproducibility (TF-IDF features, LR hyperparams, calibration set size, synthetic generation params)\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1]\n      note: \"Missing: TF-IDF n-gram range, max_features, sublinear_tf; LR C/solver/max_iter; calibration validation set size; synthetic continuation prompt format and decoding params.\"\n  action_items:\n    - round: 3\n      action: \"Add detector and data generation hyperparameters to Appendix\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M4\"\n  summary: \"Llama-3.2-3B cross-model results in Limitations text only — no table, no Appendix, unverifiable\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Limitations mentions Llama-3.2-3B parity with uniform on PPL/HellaSwag and +1.6pp MMLU, but no table or appendix entry.\"\n  action_items:\n    - round: 3\n      action: \"Move Llama-3.2-3B results to Appendix with full breakdown table\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M5\"\n  summary: \"Reference issues: lin2017focal venue type, vehtari2024psis year discrepancy with OpenAlex\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"R2-M3: vehtari2024psis year uncertain. guo2025escaping phantom (resolved R2).\"\n    - round: 3\n      reviewers: [R1]\n      note: \"lin2017focal: bib type=article but venue=ICCV, should be inproceedings. vehtari2024psis: bib=2024 vs OpenAlex=2015 (JMLR formal pub may differ from preprint).\"\n  action_items:\n    - round: 3\n      action: \"Fix lin2017focal to inproceedings; verify vehtari2024psis publication year\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# Legacy issues from rounds 1-2 (status tracking)\n- id: \"R1-N1\"\n  summary: \"'Statistically indistinguishable' claim uses failure-to-reject (p=0.30, N=3) instead of equivalence test (TOST)\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Full consensus. p=0.30 only means failure to reject H0, not evidence of equivalence. N=3 has extremely low statistical power.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Paper changed 'statistically indistinguishable' to 'competitive' and reports 95% CI. But 'competitive' still overstatement given CI includes degradation. See R3-N1.\"\n  action_items:\n    - round: 2\n      action: \"Replace 'statistically indistinguishable' globally with 'comparable' or 'competitive without hyperparameter search'. Report 95% CI, state N=3 insufficient for TOST.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Wording changed but remaining issues tracked in R3-N1\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"α_eff theoretical motivation (true α) disconnected from computation (r_i = 1[q_i ≤ 0.5]); Proposition 1 covariance is tautological\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Full consensus. Two issues: (a) no error bound for α_eff vs true α; (b) covariance positivity is by construction.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"α_eff proxy validation added (Appendix E, Pearson r≈0.70, bias -0.03). Partially addresses (a). Proposition 1 tautology (b) still present. See R3-N2 and R3-W8.\"\n  action_items:\n    - round: 2\n      action: \"Paper: add discussion of α_eff as proxy with detector-quality caveat; cite Guo 2017 calibration; add Appendix table with bs=4/8/16 correlation data\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Proxy validation added. Remaining issues tracked in R3-N2 (theory disconnect) and R3-W8 (proof presentation)\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"Experimental external validity insufficient: single model/detector/data/contamination-type\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Full consensus. Drayson tested 160M/360M/1.7B; this paper has far less coverage.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Improvements: 1.7B added (single seed), 3 detectors tested, D&R epoch-matched 3-seed, threshold curve. Remaining: 1.7B single seed, Llama-3B only in Limitations text, no cross-generator experiment. See R3-N3, R3-N5, R3-W1.\"\n  action_items:\n    - round: 2\n      action: \"Multi-model 3-seed and neural detector: cannot complete in 6 days, acknowledge in Limitations\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Partially addressed. Remaining gaps tracked in R3-N3 (1.7B claim), R3-N5 (scale), R3-W1 (self-contamination)\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"Hard filtering crushes reweighting (17.290 vs 17.651); undermines motivation\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [research_reviewer]\n      note: \"D082 definitive: epoch-matched D&R 3-seed 17.657±0.006 ≈ Adaptive 17.651±0.007 (gap 0.006). D&R's 0.36 PPL advantage was ENTIRELY from 2.4× multi-epoch confound.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Epoch-matched control (Table 2) successfully resolves the confound. Both reviewers praise this analysis. Issue substantially addressed in current version.\"\n  action_items:\n    - round: 2\n      action: \"Paper: add distribution matching + multi-epoch confound discussion\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Epoch-matched 3-seed Table 2 resolves the confound convincingly. Both R3 reviewers cite this as a strength.\"\n  resolution_round: 3\n\n- id: \"R1-W1\"\n  summary: \"Effect size tiny (0.043 PPL) with downstream 4/5 benchmarks slightly worse; framing mismatch\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Full consensus. Suggest re-framing as 'matching grid-search at zero validation cost'.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Reframing done but effect size concern persists and is now escalated. See R3-N1.\"\n  action_items:\n    - round: 2\n      action: \"Reframe: 'automatic exponent selection eliminating grid search cost'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reframing done. Remaining concerns tracked in R3-N1.\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Proposition 1 proof gap: strictly increasing vs non-decreasing\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. Fixable.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"本轮确认已修复：Proposition 1 now states 'non-decreasing' with condition for strict increase\"\n  action_items:\n    - round: 2\n      action: \"Add non-degenerate batch condition for strict positivity, or relabel as non-decreasing\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed: Proposition 1 correctly states non-decreasing with strict condition\"\n  resolution_round: 3\n\n- id: \"R1-W3\"\n  summary: \"ESS monotonicity not formally proven; citation too vague\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Minor divergence on severity but agree current citation insufficient.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"本轮确认已修复：Appendix now contains Proposition 2 (ESS monotonicity) with full proof\"\n  action_items:\n    - round: 2\n      action: \"Add specific lemma/theorem reference (Kish 1965, Owen 2013 Ch9) or brief Appendix proof\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed: Proposition 2 with full Herfindahl-index proof in Appendix A\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"Grid-b post-hoc oracle: best b selected on test set gives unfair advantage\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. R2: reverse direction favors paper.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"本轮确认：Table 1 footnote ‡ now says 'Post-hoc oracle'. Bidirectional discussion present.\"\n  action_items:\n    - round: 2\n      action: \"Add bidirectional discussion: post-hoc oracle helps grid-best, but realistic val-based selection would be worse\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Partially addressed: footnote marks oracle, text discusses. Minor residual: R1-M1 notes D&R q>0.3 also post-hoc but not annotated as oracle.\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"D&R and Golden Ratio baselines only seed 42; no multi-seed comparison\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. At minimum D&R needs 3-seed.\"\n    - round: 2\n      reviewers: [research_reviewer]\n      note: \"D082: epoch-matched D&R 3-seed complete\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"D&R epoch-matched 3-seed in Table 2. Golden Ratio still single seed (noted as minor).\"\n  action_items:\n    - round: 2\n      action: \"D&R q>0.5 seed123/456\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"D&R epoch-matched 3-seed complete. Golden Ratio single seed acknowledged in footnote.\"\n  resolution_round: 2\n\n- id: \"R2-W1\"\n  summary: \"Novelty relative to Drayson limited — core formula borrowed, dual constraint standard IS\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Divergence: R2 trivial vs R1 non-trivial insight. Both agree Findings-level.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Escalated to critical in R3-N4. R2 maintains 'automatic hyperparameter selection', R1 acknowledges but values ablation evidence.\"\n  action_items:\n    - round: 2\n      action: \"Clarify unique aspects: ESS-only counter-intuitive failure + regime analysis\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Clarification added but fundamental novelty concern remains. See R3-N4.\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"τ depends on ρ (0.8→0.7), contradicting 'zero validation cost' and ρ-unknown claims\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus. τ≈1−ρ/2 heuristic directly contradicts ρ-unknown assumption.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"τ≈1−ρ/2 heuristic deleted, τ=0.8 reframed as universal default. But Figure 4 still shows τ optimal shifts 0.8→0.7 and 'principled defaults' persists. See R3-N2.\"\n  action_items:\n    - round: 2\n      action: \"Delete τ≈1−ρ/2 heuristic. Reframe: τ=0.8 universal default, robust for ρ∈[0.4,0.6]\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Heuristic deleted. Remaining 'principled defaults' wording tracked in R3-N2.\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"Citation density insufficient: 23 refs vs EMNLP 40-60+ norm\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [director_audit]\n      note: \"Increased to 30 refs, all cited.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Now ~39 refs. Still below EMNLP norm. New missing works identified. See R3-W3.\"\n  action_items:\n    - round: 2\n      action: \"Add 15-20 references\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Increased from 23 to 39 but still insufficient. See R3-W3.\"\n  resolution_round: null\n\n- id: \"R2-M1\"\n  summary: \"'five approaches' but lists 6 methods\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Simple count error.\"\n    - round: 3\n      reviewers: []\n      note: \"本轮未提及，已确认修复\"\n  action_items:\n    - round: 2\n      action: \"Fix method count in experiments.tex\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed.\"\n  resolution_round: 2\n\n- id: \"R2-M2\"\n  summary: \"Grid-b values inconsistent across sections (7 vs 9 vs 'nine runs')\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Section 4 lists 7, Appendix has 9.\"\n    - round: 3\n      reviewers: []\n      note: \"本轮未提及，已确认修复\"\n  action_items:\n    - round: 2\n      action: \"Unify grid-b value lists across all sections\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Unified.\"\n  resolution_round: 2\n\n- id: \"R2-M3\"\n  summary: \"Reference issues: guo2025escaping possibly phantom, vehtari2024psis year uncertain\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [director_audit]\n      note: \"guo2025escaping deleted (phantom). vehtari2024psis confirmed.\"\n    - round: 3\n      reviewers: []\n      note: \"guo2025escaping resolved. vehtari2024psis year discrepancy re-raised in R3-M5.\"\n  action_items:\n    - round: 2\n      action: \"Verify via WebSearch; delete if phantom.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"guo2025escaping deleted. vehtari2024psis residual year issue tracked in R3-M5.\"\n  resolution_round: 2\n\n- id: \"R2-M5\"\n  summary: \"Hybrid ρ=0.6 row comparability unclear in Appendix Table 4\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Hybrid changes effective ρ, making comparison misleading.\"\n    - round: 3\n      reviewers: [R2]\n      note: \"Footnote added (*) in Table 4. Partially addressed.\"\n  action_items:\n    - round: 2\n      action: \"Add explicit comparability note in table caption\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Footnote added. Residual hybrid discussion tracked in R3-M2.\"\n  resolution_round: 3"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-19T04:46:05.438876+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml\", \"bytes\": 31529}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-19T04:48:26.990300+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "provenance_weight_training",
  "report": "# 审稿报告 — Round 3 (Fresh Review)\n\n**论文**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\n**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review May 2026)\n**审稿日期**: 2026-05-19\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验统计，R2: 新颖性+Related Work+写作格式）\n**轮次**: 1 轮 + 交叉评审（关键问题达成共识，无需 Round 2）\n\n---\n\n## Summary\n\n本文提出 Minimum Intervention Reweighting，一个双约束框架，从 batch 级别的检测器分数自动推导 reweighting exponent b*：通过 α_eff(b) ≥ τ（质量下限）和 ESS(b) ≥ n_min（稳定上限）两个约束选取满足条件的最小 b。在 Qwen3-0.6B continued pretraining（132M FineWeb tokens, 40% 合成污染）上，adaptive b* 的 PPL 接近 grid search 最优值（3-seed: 17.651 vs 17.620, 95% CI [-0.039, 0.101]），ablation 确认 detector signal 和 minimum intervention 缺一不可。Epoch-matched 控制实验揭示 D&R 的表面 PPL 优势完全来自 multi-epoch exposure。\n\n---\n\n## Strengths\n\n**S1. Epoch-matched control 实验设计** [R1+R2 共识]\nTable 2 通过控制 content epochs 将 D&R 的 0.360 PPL 表面优势分解为 multi-epoch effect (Δ=0.006 within seed variance)，3-seed 验证 (17.657±0.006 vs 17.651±0.007)。这一分析方法论对领域有独立价值，即使方法本身不被采纳。\n\n**S2. Ablation 层次清晰** [R1+R2 共识]\nRandom < ESS-only < Uniform < Adaptive 的层级在 ρ=0.4 和 ρ=0.6 两个水平上跨 3 seeds 一致复现（Table 1, Table 8），令人信服地分离了 detector signal 和 minimum intervention 两个要素。ESS-only 的反直觉失败（17.737 vs Uniform 17.694）支撑了 dual constraint 的必要性。\n\n**S3. Detector signal type 发现** [R1+R2 共识]\nDiscriminative detector (TF-IDF+LR, AUC=0.94) 成功而两个 generative detectors (GPT-2 AUC=0.91, N-gram AUC=0.73) 均失败（Table 7），揭示 AUC 不是决定因素，signal type 才是关键。有实用指导价值，但 3 个 detector 不足以区分 type effect 和 calibration effect。\n\n**S4. 写作质量** [R1+R2 共识]\n叙事主线一致，无 AI 写作痕迹（无 em-dash/en-dash 滥用），排版符合 ACL 模板，正文恰好 8 页，Limitations section 坦诚讨论了主要弱点。\n\n**S5. 方法描述清晰**\nAlgorithm 1 提供完整伪代码，数学推导干净，两个超参数有明确默认值。Reproducibility 评分较高（除代码/数据未公开外）。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1. 统计支撑不足，核心 claim 过强** [R1+R2 共识, critical]\n- Adaptive vs Grid-best: 95% CI [-0.039, 0.101] 跨越零，上界 0.101 是效果量 0.043 的 2.3 倍。Abstract 称 \"competitive with grid-searched optimum\" 是过度表述。\n- N=3 的 paired t-test assumptions 无法验证，Wilcoxon signed-rank 在 N=3 下无法给出 p<0.05。\n- 效果量 0.043 PPL (0.24% relative) 在 5.3-point continued pretraining drop 中仅占 0.8%。\n- Downstream benchmarks 4/5 任务 Adaptive 略差于 Uniform (Table 5)，可能为 distribution matching artifact——PPL 评估集是同源的 human-only FineWeb。\n- **修复方向**: 弱化 Abstract/Conclusion claim 措辞（承认 CI 包含 degradation）；增加 seeds 或添加 downstream caveat。\n\n**N2. 理论-经验断联：τ 非 \"principled\"** [R1+R2 共识, critical]\n- Wang 2026 收敛理论假设已知精确 α，但本文的 τ 是经验超参（seed 42 单 seed sweep, Table 3）。\n- \"Principled defaults\" (Section 3.5 L124) 暗示比实际更强的理论保证。\n- τ 最优值随 ρ 变化（0.8→0.7, Figure 4），削弱 \"zero validation cost\" claim (Abstract L5)。\n- **修复方向**: \"principled\" → \"empirically robust\"；承认 τ 选择替代了 b search，量化搜索空间缩减。\n\n**N3. 1.7B claim 不充分** [R1+R2 共识, critical]\n- 单 seed, Δ=-0.01 (13.26 vs 13.26)，效果从 0.6B 的 0.043 缩小 4 倍。\n- Abstract/Conclusion 称 \"transfers without degradation\"，但 Limitations 更谨慎地说 \"does not demonstrate a clear advantage\"。\n- **修复方向**: Abstract/Conclusion 加 \"single-seed\" qualifier，或补充 multi-seed 1.7B。\n\n**N4. 新颖性不足以支撑 Main Conference** [R2 critical, R1 partial rebut → 共识 Findings 级别]\n- 核心公式 w=(1-q)^b 完全来自 Drayson 2025。\n- α_eff（加权平均）和 ESS (Kish 1965) 均为标准工具。\n- \"Minimum intervention principle\" 是标准约束优化的 infimum 求解。\n- R1 认为 ESS-only ablation 的非平凡失败和 epoch-matched analysis 有独立价值，Excitement 应为 3/5 而非 2/5。\n- **两位 Reviewer 共识**: 贡献为 Findings 级别，不足以支撑 Main。\n- **修复方向**: 投 Findings，或提供更强理论结果（如 minimum intervention 的 regret bound）。\n\n**N5. 实验规模与论文动机严重脱节** [R1+R2 共识, critical]\n- Introduction 以 \"web corpora 20-60% machine-generated text\" 开篇，framing 为 web-scale 问题。\n- 实验仅 0.6B model + 132M tokens，与 web-scale (1T+ tokens) 差 4 个数量级。\n- EMNLP data curation 论文 (DataComp-LM, DoReMi) 通常在 billions of tokens 上验证。\n- **修复方向**: 缩窄 Introduction framing 至 continued pretraining 场景，或补充 ≥1B tokens 实验。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. 自污染外部有效性** [R1+R2 共识]\nQwen3-0.6B 生成 + 训练的自污染设定不代表真实 multi-source web contamination。方法在异质污染下行为未知。Llama-3.2-3B cross-model 结果仅在 Limitations 文本中，无 table。\n\n**W2. Abstract 超长且数据密集** [R2 raised, R1 partial agree]\n~280 words，超 250 word 惯例。列举了过多具体数字（PPL, CI, Δ, ablation 排序），读起来像 Results 缩写而非 story。R1 认为数字服务 claim 不算堆砌，但同意应精简至 230-250 words。\n\n**W3. 引用覆盖不足** [R1+R2 共识]\n~39 条引用，低于 EMNLP 长文 50-60+ 惯例。遗漏: DCLM (Li 2024), QuRating (Wettig 2024), OLMo (Groeneveld 2024), LESS (Xia 2024), Gerstgrasser 2024 (Is Model Collapse Inevitable?), Gururangan 2020 (Don't Stop Pretraining), Tale of Tails (Dohmatob 2024)。Related Work \"Data Mixing\" 段过密（一段 12 引用）。\n\n**W4. Discussion 过于单薄** [R1+R2 共识]\n~20 行，基本重述 Results。缺少: 失败条件分析、PSIS/Pareto-k 理论连接、soft vs hard filtering 信息论视角、部署指导（何时用 adaptive/D&R/不干预）。\n\n**W5. \"Minimum Intervention Principle\" framing 过度** [R2 raised, R1 partial rebut]\nR2 认为标准约束优化不应命名为 \"principle\"。R1 认为有先例但应加 qualifier。折中: \"empirically motivated minimum intervention strategy\"。\n\n**W6. ρ=0.2 失效机制未讨论** [R1 raised, R2 agrees]\nLimitations 一行带过 (+0.046 PPL)。机制不清: τ=0.8 时大部分 batch 应 b*=0，为什么 PPL 反而更差？可能 false-positive driven 过度干预。应在 Discussion 或 Appendix 分析。\n\n**W7. Micro-batch B=4 粗糙度** [R1 raised, R2 agrees]\nB=4 时 α_eff 仅 5 个离散值 (MAE=0.114)，b* 本质上是 5-way 分类，与 \"continuous adaptive selection\" framing 不一致。PPL 差异 <0.01 across B∈{4,8,16} 部分缓解，但 micro-batch vs effective-batch 设计选择未充分论证。\n\n**W8. Proposition 1 proof sketch 误导** [R1 raised, R2 agrees]\nr_i = 1[q_i ≤ 0.5] 使 Cov(r_i, ln(1-q_i)) ≥ 0 是定义恒等式，不依赖 detector quality。\"Better-than-random discrimination\" 条件是多余的，误导读者以为单调性依赖检测器质量。不影响方法正确性，影响呈现诚实性。\n\n### Minor\n\n- **M1** [R2]: Responsible NLP Research Checklist 缺失，ACL ARR 要求，可能 desk reject\n- **M2** [R1+R2 cross]: Hybrid method (q>0.95 + adaptive, PPL 17.514) 比 pure adaptive 好 0.139 但未在主文讨论/推荐\n- **M3** [R1]: 检测器训练细节不足（TF-IDF features, LR 超参, calibration set size, 合成数据生成参数）\n- **M4** [R1+R2]: Llama-3.2-3B 结果无 table，仅 Limitations 文本，不可验证\n- **M5** [R1]: lin2017focal bib type 错误（article→inproceedings），vehtari2024psis 年份与 OpenAlex 不一致\n- **M6** [R1+R2]: ECE 缩写多处使用未定义\n- **M7** [R1+R2]: 无代码/数据公开承诺\n- **M8** [R2]: 少量 -ing 分词短语结尾 (\"confirming that...\", \"suggesting that...\")\n- **M9** [R1]: D&R q>0.3 post-hoc oracle 未在 Table 1 注释中标注\n- **M10** [R1]: Golden Ratio baseline 仅单 seed，与 3-seed 方法不对称\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 完全一致:\n\n1. **核心 claim 统计支撑不足** (N1): CI 包含 degradation, N=3 power 极低, 效果量微弱\n2. **理论-经验断联** (N2): τ 是经验超参但 framing 为 \"principled\"\n3. **1.7B claim 过强** (N3): 单 seed, Δ≈0, Abstract/Conclusion 过度表述\n4. **实验规模脱节** (N5): 0.6B/132M vs web-scale framing\n5. **适合 Findings 而非 Main** (N4): 方法 novelty 为 incremental，核心公式来自 Drayson 2025\n6. **自污染外部有效性** (W1): 不代表真实 multi-source contamination\n7. **引用不足** (W3): ~39 条，遗漏多篇重要工作\n8. **Discussion 单薄** (W4): 缺少深入分析\n9. **ρ=0.2 失效** (W6): 机制未解释\n10. **Proposition 1 tautological** (W8): proof sketch 误导\n11. **Epoch-matched control 是亮点** (S1): 对领域有独立贡献\n\n---\n\n## Reviewer Divergence [分歧]\n\n| 问题 | R1 | R2 | 折中 |\n|------|----|----|------|\n| Excitement | 3/5 (epoch-matched + detector-type 有启发性) | 2.0→2.5/5 (自动调参 novelty 不足) | **2.5/5** |\n| Overall | 3.0/5 (Findings) | 2.5/5 (Findings/borderline reject) | **3.0/5 (Findings)** |\n| Abstract 数据堆砌 | 数字服务 claim，非堆砌 | 读起来像 Results 缩写 | 保留关键数字，精简至 250 words |\n| MIP 命名 | \"Principle\" 有先例，加 qualifier | 标准优化不应称 \"principle\" | 加 \"empirically motivated\" qualifier |\n\n---\n\n## Questions to Authors\n\n1. ρ=0.2 时，如果大部分 batch α_eff(0) ≈ 0.8 ≥ τ 且 b*=0，为什么 PPL 比 uniform 更差 (+0.046)？请提供 ρ=0.2 的 b* 分布和 constraint regime 分解。\n2. 为什么选择 micro-batch (B=4) 而非 effective batch (B=16) 计算 b*？是否有 B=16 计算的 ablation？\n3. Hybrid method (q>0.95 + adaptive, 17.514) 比 pure adaptive 好 0.139 PPL。为什么不推荐 hybrid 作为默认方法？\n4. τ 最优从 0.8 (ρ=0.4) 到 0.7 (ρ=0.6)。如果 ρ 未知，能否从 batch-level α_eff(0) 分布反推 ρ 估计来自适应选择 τ？\n5. Downstream 4/5 任务略差。如果评估集换成非 FineWeb 来源的 human text，PPL 改善是否仍然存在？\n6. Llama-3.2-3B cross-model 的完整结果（PPL, per-task breakdown）能否补充到 Appendix？\n\n---\n\n## Missing References\n\n**高优先级（直接相关，必须引用）:**\n- Gerstgrasser et al. (2024) \"Is Model Collapse Inevitable?\" — 挑战 model collapse inevitability claim\n- Gururangan et al. (2020) \"Don't Stop Pretraining\" — continued pretraining 经典工作\n\n**中优先级（加强 Related Work 覆盖）:**\n- Li et al. (2024) DCLM — classifier-based data curation benchmark\n- Wettig et al. (2024) QuRating — LLM-based data quality scoring\n- Groeneveld et al. (2024) OLMo — 开源 pretraining data pipeline\n- Xia et al. (2024) LESS — influence-function data selection\n- Dohmatob et al. (2024) \"A Tale of Tails\" — model collapse heavy-tail analysis\n\n---\n\n## Overall Assessment\n\n**评分: weak reject (for Main) / borderline accept (for Findings)**\n**综合分数: 3.0/5**\n**置信度: 4/5**\n\n本文解决了一个实际问题（detect-and-reweight 的超参数选择），方法正确，写作诚实。Epoch-matched control 和 detector-type 发现对领域有贡献价值。\n\n但五个 critical 问题限制了 Main Conference 的 acceptance case:\n1. 核心 claim 的 CI 包含 degradation，N=3 统计力度不足\n2. \"Principled\" framing 超出了理论实际提供的保证\n3. 1.7B 单 seed 结果不支持 scale transfer claim\n4. 核心公式来自 Drayson 2025，dual constraint 是标准 IS 工具组合\n5. 0.6B/132M tokens 实验与 web-scale framing 脱节 4 个数量级\n\n**建议**: 投 Findings track。如冲击 Main，需要: (a) ≥1B scale multi-seed 实验，(b) downstream 改善的统计证据，(c) 更强理论贡献（如 minimum intervention optimality bound），(d) cross-generator contamination 实验。\n\n---\n\n## Detailed Comments by Section\n\n### Abstract\n- ~280 words，建议精简至 ≤250。保留核心数字 (3-seed mean, CI)，删除 ablation 细节和 τ range。\n- \"Competitive with grid-searched optimum\" → \"comparable in magnitude to grid-searched values, while eliminating the search cost\"。\n- 补充一句 downstream caveat。\n\n### Introduction\n- 叙事结构完整 (background → gap → insight → method → results → contributions)。\n- 开头 \"web corpora\" framing 与实验规模不匹配——建议聚焦 \"continued pretraining on potentially contaminated data\"。\n- Contribution 3 (detector signal type) 在 Introduction 中铺垫不足。\n\n### Related Work\n- 结构合理（4 个主题段）。与 Drayson 2025 的区分清晰。\n- \"Data Mixing\" 段过密（一段 12 引用），建议拆分为 domain-level 和 instance-level。\n- 引用量 (~39) 偏少，遗漏见上文。\n\n### Method\n- 数学推导干净，Algorithm 1 可直接实现。\n- \"Principled defaults\" → \"empirically robust defaults\"。\n- Proposition 1 proof sketch 需修正（去除 misleading \"better-than-random\" condition）。\n- Micro-batch vs effective-batch 设计选择需论证。\n\n### Experiments\n- 训练配置基本完整。检测器细节不足。\n- 方法列表完整（6 种 + epoch-matched）。\n- 合成数据生成参数（decoding temperature, prompt format）缺失。\n\n### Results\n- 最强部分。Epoch-matched control (Table 2) 是实验设计亮点。\n- Grid-b trend (Figure 1) 有效可视化了 adaptive vs ESS-only 的定位。\n- 统计 claim 需弱化（见 N1）。\n\n### Discussion\n- 太短 (~20 行)，大部分重述 Results。需增加失败条件分析、理论连接、部署指导。\n\n### Conclusion\n- 1.7B claim 需加 qualifier。\n\n### Limitations\n- 坦诚且全面。唯一缺漏: ρ=0.2 失效机制应展开。\n\n### Appendix\n- 内容丰富（proofs, grid search, τ sweep, regime, τ-ρ, hybrid, downstream, ρ=0.6, α_eff validation, detector comparison）。\n- D&R threshold table (Table 8) 和 dual curve (Figure 5) 是重要补充材料。\n- α_eff proxy validation (Table 6) 有效回应了上轮审稿意见。",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "provenance_weight_training",
    "report": "# 审稿报告 — Round 3 (Fresh Review)\n\n**论文**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\n**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review May 2026)\n**审稿日期**: 2026-05-19\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验统计，R2: 新颖性+Related Work+写作格式）\n**轮次**: 1 轮 + 交叉评审（关键问题达成共识，无需 Round 2）\n\n---\n\n## Summary\n\n本文提出 Minimum Intervention Reweighting，一个双约束框架，从 batch 级别的检测器分数自动推导 reweighting exponent b*：通过 α_eff(b) ≥ τ（质量下限）和 ESS(b) ≥ n_min（稳定上限）两个约束选取满足条件的最小 b。在 Qwen3-0.6B continued pretraining（132M FineWeb tokens, 40% 合成污染）上，adaptive b* 的 PPL 接近 grid search 最优值（3-seed: 17.651 vs 17.620, 95% CI [-0.039, 0.101]），ablation 确认 detector signal 和 minimum intervention 缺一不可。Epoch-matched 控制实验揭示 D&R 的表面 PPL 优势完全来自 multi-epoch exposure。\n\n---\n\n## Strengths\n\n**S1. Epoch-matched control 实验设计** [R1+R2 共识]\nTable 2 通过控制 content epochs 将 D&R 的 0.360 PPL 表面优势分解为 multi-epoch effect (Δ=0.006 within seed variance)，3-seed 验证 (17.657±0.006 vs 17.651±0.007)。这一分析方法论对领域有独立价值，即使方法本身不被采纳。\n\n**S2. Ablation 层次清晰** [R1+R2 共识]\nRandom < ESS-only < Uniform < Adaptive 的层级在 ρ=0.4 和 ρ=0.6 两个水平上跨 3 seeds 一致复现（Table 1, Table 8），令人信服地分离了 detector signal 和 minimum intervention 两个要素。ESS-only 的反直觉失败（17.737 vs Uniform 17.694）支撑了 dual constraint 的必要性。\n\n**S3. Detector signal type 发现** [R1+R2 共识]\nDiscriminative detector (TF-IDF+LR, AUC=0.94) 成功而两个 generative detectors (GPT-2 AUC=0.91, N-gram AUC=0.73) 均失败（Table 7），揭示 AUC 不是决定因素，signal type 才是关键。有实用指导价值，但 3 个 detector 不足以区分 type effect 和 calibration effect。\n\n**S4. 写作质量** [R1+R2 共识]\n叙事主线一致，无 AI 写作痕迹（无 em-dash/en-dash 滥用），排版符合 ACL 模板，正文恰好 8 页，Limitations section 坦诚讨论了主要弱点。\n\n**S5. 方法描述清晰**\nAlgorithm 1 提供完整伪代码，数学推导干净，两个超参数有明确默认值。Reproducibility 评分较高（除代码/数据未公开外）。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1. 统计支撑不足，核心 claim 过强** [R1+R2 共识, critical]\n- Adaptive vs Grid-best: 95% CI [-0.039, 0.101] 跨越零，上界 0.101 是效果量 0.043 的 2.3 倍。Abstract 称 \"competitive with grid-searched optimum\" 是过度表述。\n- N=3 的 paired t-test assumptions 无法验证，Wilcoxon signed-rank 在 N=3 下无法给出 p<0.05。\n- 效果量 0.043 PPL (0.24% relative) 在 5.3-point continued pretraining drop 中仅占 0.8%。\n- Downstream benchmarks 4/5 任务 Adaptive 略差于 Uniform (Table 5)，可能为 distribution matching artifact——PPL 评估集是同源的 human-only FineWeb。\n- **修复方向**: 弱化 Abstract/Conclusion claim 措辞（承认 CI 包含 degradation）；增加 seeds 或添加 downstream caveat。\n\n**N2. 理论-经验断联：τ 非 \"principled\"** [R1+R2 共识, critical]\n- Wang 2026 收敛理论假设已知精确 α，但本文的 τ 是经验超参（seed 42 单 seed sweep, Table 3）。\n- \"Principled defaults\" (Section 3.5 L124) 暗示比实际更强的理论保证。\n- τ 最优值随 ρ 变化（0.8→0.7, Figure 4），削弱 \"zero validation cost\" claim (Abstract L5)。\n- **修复方向**: \"principled\" → \"empirically robust\"；承认 τ 选择替代了 b search，量化搜索空间缩减。\n\n**N3. 1.7B claim 不充分** [R1+R2 共识, critical]\n- 单 seed, Δ=-0.01 (13.26 vs 13.26)，效果从 0.6B 的 0.043 缩小 4 倍。\n- Abstract/Conclusion 称 \"transfers without degradation\"，但 Limitations 更谨慎地说 \"does not demonstrate a clear advantage\"。\n- **修复方向**: Abstract/Conclusion 加 \"single-seed\" qualifier，或补充 multi-seed 1.7B。\n\n**N4. 新颖性不足以支撑 Main Conference** [R2 critical, R1 partial rebut → 共识 Findings 级别]\n- 核心公式 w=(1-q)^b 完全来自 Drayson 2025。\n- α_eff（加权平均）和 ESS (Kish 1965) 均为标准工具。\n- \"Minimum intervention principle\" 是标准约束优化的 infimum 求解。\n- R1 认为 ESS-only ablation 的非平凡失败和 epoch-matched analysis 有独立价值，Excitement 应为 3/5 而非 2/5。\n- **两位 Reviewer 共识**: 贡献为 Findings 级别，不足以支撑 Main。\n- **修复方向**: 投 Findings，或提供更强理论结果（如 minimum intervention 的 regret bound）。\n\n**N5. 实验规模与论文动机严重脱节** [R1+R2 共识, critical]\n- Introduction 以 \"web corpora 20-60% machine-generated text\" 开篇，framing 为 web-scale 问题。\n- 实验仅 0.6B model + 132M tokens，与 web-scale (1T+ tokens) 差 4 个数量级。\n- EMNLP data curation 论文 (DataComp-LM, DoReMi) 通常在 billions of tokens 上验证。\n- **修复方向**: 缩窄 Introduction framing 至 continued pretraining 场景，或补充 ≥1B tokens 实验。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. 自污染外部有效性** [R1+R2 共识]\nQwen3-0.6B 生成 + 训练的自污染设定不代表真实 multi-source web contamination。方法在异质污染下行为未知。Llama-3.2-3B cross-model 结果仅在 Limitations 文本中，无 table。\n\n**W2. Abstract 超长且数据密集** [R2 raised, R1 partial agree]\n~280 words，超 250 word 惯例。列举了过多具体数字（PPL, CI, Δ, ablation 排序），读起来像 Results 缩写而非 story。R1 认为数字服务 claim 不算堆砌，但同意应精简至 230-250 words。\n\n**W3. 引用覆盖不足** [R1+R2 共识]\n~39 条引用，低于 EMNLP 长文 50-60+ 惯例。遗漏: DCLM (Li 2024), QuRating (Wettig 2024), OLMo (Groeneveld 2024), LESS (Xia 2024), Gerstgrasser 2024 (Is Model Collapse Inevitable?), Gururangan 2020 (Don't Stop Pretraining), Tale of Tails (Dohmatob 2024)。Related Work \"Data Mixing\" 段过密（一段 12 引用）。\n\n**W4. Discussion 过于单薄** [R1+R2 共识]\n~20 行，基本重述 Results。缺少: 失败条件分析、PSIS/Pareto-k 理论连接、soft vs hard filtering 信息论视角、部署指导（何时用 adaptive/D&R/不干预）。\n\n**W5. \"Minimum Intervention Principle\" framing 过度** [R2 raised, R1 partial rebut]\nR2 认为标准约束优化不应命名为 \"principle\"。R1 认为有先例但应加 qualifier。折中: \"empirically motivated minimum intervention strategy\"。\n\n**W6. ρ=0.2 失效机制未讨论** [R1 raised, R2 agrees]\nLimitations 一行带过 (+0.046 PPL)。机制不清: τ=0.8 时大部分 batch 应 b*=0，为什么 PPL 反而更差？可能 false-positive driven 过度干预。应在 Discussion 或 Appendix 分析。\n\n**W7. Micro-batch B=4 粗糙度** [R1 raised, R2 agrees]\nB=4 时 α_eff 仅 5 个离散值 (MAE=0.114)，b* 本质上是 5-way 分类，与 \"continuous adaptive selection\" framing 不一致。PPL 差异 <0.01 across B∈{4,8,16} 部分缓解，但 micro-batch vs effective-batch 设计选择未充分论证。\n\n**W8. Proposition 1 proof sketch 误导** [R1 raised, R2 agrees]\nr_i = 1[q_i ≤ 0.5] 使 Cov(r_i, ln(1-q_i)) ≥ 0 是定义恒等式，不依赖 detector quality。\"Better-than-random discrimination\" 条件是多余的，误导读者以为单调性依赖检测器质量。不影响方法正确性，影响呈现诚实性。\n\n### Minor\n\n- **M1** [R2]: Responsible NLP Research Checklist 缺失，ACL ARR 要求，可能 desk reject\n- **M2** [R1+R2 cross]: Hybrid method (q>0.95 + adaptive, PPL 17.514) 比 pure adaptive 好 0.139 但未在主文讨论/推荐\n- **M3** [R1]: 检测器训练细节不足（TF-IDF features, LR 超参, calibration set size, 合成数据生成参数）\n- **M4** [R1+R2]: Llama-3.2-3B 结果无 table，仅 Limitations 文本，不可验证\n- **M5** [R1]: lin2017focal bib type 错误（article→inproceedings），vehtari2024psis 年份与 OpenAlex 不一致\n- **M6** [R1+R2]: ECE 缩写多处使用未定义\n- **M7** [R1+R2]: 无代码/数据公开承诺\n- **M8** [R2]: 少量 -ing 分词短语结尾 (\"confirming that...\", \"suggesting that...\")\n- **M9** [R1]: D&R q>0.3 post-hoc oracle 未在 Table 1 注释中标注\n- **M10** [R1]: Golden Ratio baseline 仅单 seed，与 3-seed 方法不对称\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 完全一致:\n\n1. **核心 claim 统计支撑不足** (N1): CI 包含 degradation, N=3 power 极低, 效果量微弱\n2. **理论-经验断联** (N2): τ 是经验超参但 framing 为 \"principled\"\n3. **1.7B claim 过强** (N3): 单 seed, Δ≈0, Abstract/Conclusion 过度表述\n4. **实验规模脱节** (N5): 0.6B/132M vs web-scale framing\n5. **适合 Findings 而非 Main** (N4): 方法 novelty 为 incremental，核心公式来自 Drayson 2025\n6. **自污染外部有效性** (W1): 不代表真实 multi-source contamination\n7. **引用不足** (W3): ~39 条，遗漏多篇重要工作\n8. **Discussion 单薄** (W4): 缺少深入分析\n9. **ρ=0.2 失效** (W6): 机制未解释\n10. **Proposition 1 tautological** (W8): proof sketch 误导\n11. **Epoch-matched control 是亮点** (S1): 对领域有独立贡献\n\n---\n\n## Reviewer Divergence [分歧]\n\n| 问题 | R1 | R2 | 折中 |\n|------|----|----|------|\n| Excitement | 3/5 (epoch-matched + detector-type 有启发性) | 2.0→2.5/5 (自动调参 novelty 不足) | **2.5/5** |\n| Overall | 3.0/5 (Findings) | 2.5/5 (Findings/borderline reject) | **3.0/5 (Findings)** |\n| Abstract 数据堆砌 | 数字服务 claim，非堆砌 | 读起来像 Results 缩写 | 保留关键数字，精简至 250 words |\n| MIP 命名 | \"Principle\" 有先例，加 qualifier | 标准优化不应称 \"principle\" | 加 \"empirically motivated\" qualifier |\n\n---\n\n## Questions to Authors\n\n1. ρ=0.2 时，如果大部分 batch α_eff(0) ≈ 0.8 ≥ τ 且 b*=0，为什么 PPL 比 uniform 更差 (+0.046)？请提供 ρ=0.2 的 b* 分布和 constraint regime 分解。\n2. 为什么选择 micro-batch (B=4) 而非 effective batch (B=16) 计算 b*？是否有 B=16 计算的 ablation？\n3. Hybrid method (q>0.95 + adaptive, 17.514) 比 pure adaptive 好 0.139 PPL。为什么不推荐 hybrid 作为默认方法？\n4. τ 最优从 0.8 (ρ=0.4) 到 0.7 (ρ=0.6)。如果 ρ 未知，能否从 batch-level α_eff(0) 分布反推 ρ 估计来自适应选择 τ？\n5. Downstream 4/5 任务略差。如果评估集换成非 FineWeb 来源的 human text，PPL 改善是否仍然存在？\n6. Llama-3.2-3B cross-model 的完整结果（PPL, per-task breakdown）能否补充到 Appendix？\n\n---\n\n## Missing References\n\n**高优先级（直接相关，必须引用）:**\n- Gerstgrasser et al. (2024) \"Is Model Collapse Inevitable?\" — 挑战 model collapse inevitability claim\n- Gururangan et al. (2020) \"Don't Stop Pretraining\" — continued pretraining 经典工作\n\n**中优先级（加强 Related Work 覆盖）:**\n- Li et al. (2024) DCLM — classifier-based data curation benchmark\n- Wettig et al. (2024) QuRating — LLM-based data quality scoring\n- Groeneveld et al. (2024) OLMo — 开源 pretraining data pipeline\n- Xia et al. (2024) LESS — influence-function data selection\n- Dohmatob et al. (2024) \"A Tale of Tails\" — model collapse heavy-tail analysis\n\n---\n\n## Overall Assessment\n\n**评分: weak reject (for Main) / borderline accept (for Findings)**\n**综合分数: 3.0/5**\n**置信度: 4/5**\n\n本文解决了一个实际问题（detect-and-reweight 的超参数选择），方法正确，写作诚实。Epoch-matched control 和 detector-type 发现对领域有贡献价值。\n\n但五个 critical 问题限制了 Main Conference 的 acceptance case:\n1. 核心 claim 的 CI 包含 degradation，N=3 统计力度不足\n2. \"Principled\" framing 超出了理论实际提供的保证\n3. 1.7B 单 seed 结果不支持 scale transfer claim\n4. 核心公式来自 Drayson 2025，dual constraint 是标准 IS 工具组合\n5. 0.6B/132M tokens 实验与 web-scale framing 脱节 4 个数量级\n\n**建议**: 投 Findings track。如冲击 Main，需要: (a) ≥1B scale multi-seed 实验，(b) downstream 改善的统计证据，(c) 更强理论贡献（如 minimum intervention optimality bound），(d) cross-generator contamination 实验。\n\n---\n\n## Detailed Comments by Section\n\n### Abstract\n- ~280 words，建议精简至 ≤250。保留核心数字 (3-seed mean, CI)，删除 ablation 细节和 τ range。\n- \"Competitive with grid-searched optimum\" → \"comparable in magnitude to grid-searched values, while eliminating the search cost\"。\n- 补充一句 downstream caveat。\n\n### Introduction\n- 叙事结构完整 (background → gap → insight → method → results → contributions)。\n- 开头 \"web corpora\" framing 与实验规模不匹配——建议聚焦 \"continued pretraining on potentially contaminated data\"。\n- Contribution 3 (detector signal type) 在 Introduction 中铺垫不足。\n\n### Related Work\n- 结构合理（4 个主题段）。与 Drayson 2025 的区分清晰。\n- \"Data Mixing\" 段过密（一段 12 引用），建议拆分为 domain-level 和 instance-level。\n- 引用量 (~39) 偏少，遗漏见上文。\n\n### Method\n- 数学推导干净，Algorithm 1 可直接实现。\n- \"Principled defaults\" → \"empirically robust defaults\"。\n- Proposition 1 proof sketch 需修正（去除 misleading \"better-than-random\" condition）。\n- Micro-batch vs effective-batch 设计选择需论证。\n\n### Experiments\n- 训练配置基本完整。检测器细节不足。\n- 方法列表完整（6 种 + epoch-matched）。\n- 合成数据生成参数（decoding temperature, prompt format）缺失。\n\n### Results\n- 最强部分。Epoch-matched control (Table 2) 是实验设计亮点。\n- Grid-b trend (Figure 1) 有效可视化了 adaptive vs ESS-only 的定位。\n- 统计 claim 需弱化（见 N1）。\n\n### Discussion\n- 太短 (~20 行)，大部分重述 Results。需增加失败条件分析、理论连接、部署指导。\n\n### Conclusion\n- 1.7B claim 需加 qualifier。\n\n### Limitations\n- 坦诚且全面。唯一缺漏: ρ=0.2 失效机制应展开。\n\n### Appendix\n- 内容丰富（proofs, grid search, τ sweep, regime, τ-ρ, hybrid, downstream, ρ=0.6, α_eff validation, detector comparison）。\n- D&R threshold table (Table 8) 和 dual curve (Figure 5) 是重要补充材料。\n- α_eff proxy validation (Table 6) 有效回应了上轮审稿意见。",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-19T04:48:31.010952+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2b6c9bea33a70c93bf4bf04ac36b8df9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4020
}
```

</details>

---


### Assistant

_source line 190 · 2026-05-19T04:48:40.959409+00:00_

审稿报告已投递至 Research Director。

---

**审稿完成汇总**：

**Overall: weak reject (Main) / borderline accept (Findings) — 3.0/5**

5 个 critical 问题：
1. **统计支撑不足** — CI [-0.039, 0.101] 包含 degradation，N=3 power 极低，"competitive" 过度表述
2. **理论-经验断联** — τ=0.8 是经验选择但 framing 为 "principled default"，τ 最优随 ρ 变化
3. **1.7B claim 不充分** — 单 seed Δ=-0.01，效果缩小 4 倍，Abstract/Conclusion 过度表述
4. **新颖性 Findings 级别** — 核心公式来自 Drayson 2025，dual constraint 是标准 IS 工具
5. **Scale mismatch** — 0.6B/132M tokens vs web-scale framing 差 4 个数量级

主要优势：epoch-matched control（对领域有独立贡献）、ablation 设计清晰、detector type 发现有启发性。

**建议**：投 Findings track，或补充大规模实验 + 理论贡献后冲击 Main。

Issue Tracker 已同步更新（16 条新/更新条目 + 历史条目状态维护）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 18

## Round 18

2 recorded events


### User

_source line 191 · 2026-05-19T04:48:43.760455+00:00_

[Reviewer 2 审稿结果]:
交叉评审回应已提交。

核心结论：与 R1 在绝大多数问题上达成一致。R1 的 Proposition 1 tautological covariance 和 ρ=0.2 failure mechanism 是两个我原审遗漏的有效技术发现，已纳入。Excitement 评分维持 2.0-2.5/5（低于 R1 的 3/5），Overall 维持 2.5/5。两位 reviewer 的共识是：当前状态更适合 Findings 而非 EMNLP Main。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 192 · 2026-05-19T04:48:56.359665+00:00_

审稿报告已投递至 Research Director。

**Round 3 审稿完成，汇总如下：**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3/5 | 3/5 | 3/5 |
| Excitement | 3/5 | 2.5/5 | 2.5/5 |
| Overall | 3.0 (Findings) | 2.5 (Findings/borderline) | **3.0 (weak reject for Main)** |

**5 个 Critical 问题（全部共识）：**
1. 统计支撑不足（CI 含 degradation, N=3, 效果量 0.24%）
2. 理论-经验断联（τ 是经验超参但 framed as "principled"）
3. 1.7B 单 seed 不支持 "transfers without degradation"
4. 新颖性为 Findings 级别（核心公式来自 Drayson 2025）
5. 实验规模与 web-scale framing 脱节 4 个数量级

**核心建议：投 Findings track。** 如冲击 Main 需补充 ≥1B scale multi-seed、downstream 统计证据、cross-generator 实验、更强理论贡献。

Issue Tracker 已同步更新（17 条新/更新 issue + 历史记录）。报告已投递 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 19

## Round 19

68 recorded events


### User

_source line 193 · 2026-05-19T05:49:16.417212+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: provenance_weight_training
- 论文路径: projects/provenance_weight_training/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-19T05:49:22.247519+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-19T05:49:22.298614+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-19T05:49:25.669666+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-19T05:49:25.749406+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 79
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-19T05:49:30.666363+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-19T05:49:30.718681+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-19T05:49:34.081710+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-19T05:49:34.082107+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-19T05:49:37.393414+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-19T05:49:38.798616+00:00_

{"result":"# 项目 provenance_weight_training 概况\n\n## 实验状态 (175 个)\n\n- **adaptive_seed42**: DONE (success) — \n- **uniform_seed456**: DONE (success) — \n- **uniform_seed123**: DONE (success) — \n- **uniform_seed42**: DONE (success) — \n- **detector_modernbert**: DONE (killed) — \n- **nmin1_seed42**: DONE (success) — \n- **golden_ratio_seed42**: DONE (success) — \n- **tau_0.6_seed42**: DONE (killed) — \n- **grid_b_low_seed42**: DONE (failed) — \n- **grid_b1_5_seed456**: DONE (success) — \n- **grid_b1_0_seed456**: DONE (success) — \n- **grid_b0_5_seed456**: DONE (success) — \n- **grid_b_seed42_batch**: DONE (success) — \n- **diagnostic_contamination100**: DONE (killed) — \n- **detector_tfidf_lr**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- eval_q04（准备中）\n- eval_q06（准备中）\n- eval_q03_r2（准备中）\n- adaptive_1_7b_planb_control（准备中）\n- eval_q01_final_v2（准备中）\n- eval_q01_final（准备中）\n- eval_ngram_uniform（准备中）\n- eval_ngram_adaptive（准备中）\n- status_check_41312（准备中）\n- eval_adaptive_1_7b（准备中）\n- …另有 14 项\n\n## 近期结论\n- **uniform_1_7b_seed123** (negative): From-scratch uniform baseline at 1.7B scale with seed123, paired with adaptive_1_7b_seed123, to provide unconfounded comparison (unlike seed42 Plan B which had optimizer resume artifact)\n  [uniform_1_7b_seed123_analysis](/api/workspace-files/projects/provenance_weight_training/artifacts/uniform_1_7b_seed123/report/analysis_d8d0e9.md)\n- **detect_remove_q07_epoch_matched_seed42** (success): Epoch-matched D&R q07: 1 epoch through q07 filtered data (184,908 samples, ~100M tokens, 3047 steps). Part of 5-point epoch-matched curve (q01/q03/q05/q07/q09). If PPL converges to ~17.65-17.74 range like q03(17.74) and q05(17.65), confirms U-shape sweet spot is entirely multi-epoch artifact across the full threshold range.\n  [diagnose_q07_epoch_matched](/api/workspace-files/projects/provenance_weight_training/artifacts/detect_remove_q07_epoch_matched_seed42/report/dia
…[truncated 1800 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-19T05:49:38.949783+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-19T05:49:39.100730+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\graphicspath{{../../artifacts/figures/}}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{algorithm}
14	\usepackage{algorithmic}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{hyperref}
20	
21	\newtheorem{proposition}{Proposition}
22	\newtheorem{definition}{Definition}
23	
24	\newcommand{\bstar}{b^*}
25	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
26	\newcommand{\nmin}{n_{\min}}
27	\newcommand{\btau}{b_{\tau}}
28	\newcommand{\bess}{b_{\mathrm{ESS}}}
29	
30	\title{Minimum Intervention Reweighting: Adaptive Exponent Selection\\for Contamination-Aware Pretraining}
31	
32	\author{Anonymous}
33	
34	\begin{document}
35	\maketitle
36	
37	\begin{abstract}
38	\input{sections/abstract}
39	\end{abstract}
40	
41	\section{Introduction}
42	\label{sec:intro}
43	\input{sections/introduction}
44	
45	\section{Related Work}
46	\label{sec:related}
47	\input{sections/related_work}
48	
49	\section{Method}
50	\label{sec:method}
51	\input{sections/method}
52	
53	\section{Experimental Setup}
54	\label{sec:experiments}
55	\input{sections/experiments}
56	
57	\section{Results}
58	\label{sec:results}
59	\input{sections/results}
60	
61	\section{Discussion}
62	\label{sec:discussion}
63	\input{sections/discussion}
64	
65	\section{Conclusion}
66	\label{sec:conclusion}
67	\input{sections/conclusion}
68	
69	\section*{Limitations}
70	\label{sec:limitations}
71	\input{sections/limitations}
72	
73	\input{sections/checklist}
74	
75	\bibliography{references}
76	
77	\appendix
78	\input{sections/appendix}
79	
80	\end{document}
81	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-19T05:49:39.151281+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-19T05:49:49.232508+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on the search results, here's the key information about EMNLP 2026 call for papers submission guidelines and author instructions:

## Submission Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## Paper Types and Theme

EMNLP 2026 has a goal of curating a diverse technical p
…[truncated 2189 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 10081
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-19T05:49:55.107351+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 long paper page limit formatting template ACL ARR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 long paper page limit formatting template ACL ARR 2026"
  }
}
```

</details>

---


### Tool call

_source line 209 · 2026-05-19T05:49:55.906579+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 210 · 2026-05-19T05:49:56.408643+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 211 · 2026-05-19T05:49:56.660016+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "literature_map.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "literature_map.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 212 · 2026-05-19T05:50:01.028178+00:00_

Web search results for query: "EMNLP 2026 long paper page limit formatting template ACL ARR 2026"

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"acl2026/formatting.md at master · Lilaizhen/acl2026","url":"https://github.com/Lilaizhen/acl2026/blob/master/formatting.md"},{"title":"ClimateNLP 2026","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"GitHub - acl-org/emnlp-2026: Repository for the EMNLP 2026 conference · GitHub","url":"https://github.com/acl-org/emnlp-2026"}]

Based on the search results, here's the information about EMNLP 2026 long paper formatting and requirements:

## Page Limit
EMNLP 2026 has an 8-page limit for long papers, with unlimited pages for references in the review version.

## Formatting Template
EMNLP 2026 uses the official ACL style files, which are identical to those used for ACL, NAACL, and other *ACL conferences. *ACL provides style files for LaTeX and Microsoft Word at https://github.com/acl-org/acl-style-files.

## Format Details
The format is two-column, and the mandatory Limitations section is required, placed after the conclusion.

## Submission Process
All submissions go through ACL Rolling Review (ARR), with the ARR submission deadline of May 25, 2026.

## Accepted Papers
Upon acceptance, final versions of long papers will be given one additional page -- up to nine (9) pages of content plus unlimited pages for acknowledgements and references.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 5920
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-19T05:50:01.028747+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/literature_map.yaml\", \"content\": \"# Literature Map for provenance_weight_training\\n# 研究方向：基于收敛理论的自适应污染重加权\\n# 核心公式：w=(1-q)^b，q 为检测器合成概率，b* 为理论最优权重指数\\n# 更新日期：2026-05-16（文献验证：新增 6 篇 high-priority 论文，全部经 arXiv/venue 交叉验证）\\n\\n# ============================================================\\n# Category: direct-competitor\\n# 同主题/同方法的论文\\n# ============================================================\\n\\n- id: drayson_2025_detection_collapse\\n  title: \\\"Machine-Generated Text Detection Prevents Language Model Collapse\\\"\\n  authors: \\\"George Drayson, Emine Yilmaz, Vasileios Lampos\\\"\\n  venue: \\\"EMNLP 2025\\\"\\n  year: 2025\\n  arxiv_id: \\\"2502.15654\\\"\\n  url: \\\"https://arxiv.org/abs/2502.15654\\\"\\n  github: \\\"https://github.com/GeorgeDrayson/model_collapse\\\"\\n  category: direct-competitor\\n  role: \\\"使用同一公式 w=(1-q)^b 进行重加权，但 b 为验证集 empirical 选取，训练中固定\\\"\\n  method_summary: >\\n    Detect-and-reweight 防止递归训练 model collapse。检测器为 ModernBERT 150M\\n    (MAGE fine-tune, in-domain AUC=0.986, OOD AUC=0.943)。权重公式 wⱼ=(1-q(xⱼ))^b / Σₗ(1-q(xₗ))^b，\\n    通过 SIR 按权重重采样训练数据。b 通过 WikiText-2 验证集上 1 代递归训练后评估选取\\n    (GPT-2/SmolLM 135M/360M 用 b=10, SmolLM 1.7B 用 b=1)，训练全程固定。\\n    实验覆盖 4 个模型 (GPT-2 124M, SmolLM 135M/360M/1.7B)、10 代递归训练、6 种解码策略。\\n    结果 PPL 降低 0.85%–25.65%，diversity 提升 3.44%–14.62%。\\n  key_findings: \\\"验证 detect-and-reweight 有效防止 model collapse 且优于纯人类数据训练；b 值对模型规模敏感（小模型 b=10，大模型 b=1）\\\"\\n  differentiation:\\n    b_selection: \\\"Drayson: 验证集 empirical grid search, per-model 固定 | 我们: α_eff(b) + ESS 约束, per-batch 自适应\\\"\\n    contamination_setting: \\\"Drayson: 不假设已知比例（原文明确声明），但实验为控制设置 | 我们: 未知比例（batch 统计量在线估计）\\\"\\n    detector: \\\"Drayson: ModernBERT 150M (AUC=0.986) | 我们: TF-IDF+LR (AUC=0.939)，证明轻量检测器即可\\\"\\n    theory: \\\"Drayson: 无 b 选取理论（SIR 启发式） | 我们: 收敛理论 motivated α_eff(b) 推导\\\"\\n 
…[truncated 1599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4368
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-19T05:50:06.007801+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-19T05:50:06.460392+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/related_work_963aec.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/method_76a694.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/experiments_1613c9.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/results_819b43.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/method_3f5a58.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/experiments_86dfd1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/related_work_0b6096.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/results_d0d647.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/introduction_c6a67f.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/table1_main_results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/conclusion_386ecc.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/discussion_270aaa.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_
…[truncated 2005 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-19T05:50:06.561238+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/sections/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/sections/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-19T05:50:06.611975+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-19T05:50:16.804974+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 219 · 2026-05-19T05:50:16.855676+00:00_

1	Web corpora now contain an estimated 20--60\% machine-generated text, and training on such contaminated data risks model collapse.
2	Detect-and-reweight methods suppress likely-synthetic samples via $w(x) = (1-q(x))^b$, but the exponent $b$ critically determines outcomes and requires per-model grid search (typically multiple complete training runs) to tune.
3	
4	We propose a dual-constrained adaptive exponent $b^*$ derived per-batch from detector scores alone: find the minimum $b$ such that the weighted effective real proportion $\alpha_{\mathrm{eff}}(b) \geq \tau$ (quality floor), subject to $\mathrm{ESS}(b) \geq n_{\min}$ (stability ceiling).
5	This minimum intervention strategy applies only as much downweighting as needed, with zero validation cost.
6	
7	On Qwen3-0.6B continued pretraining (132M FineWeb tokens, 40\% synthetic contamination), the gap between adaptive and grid-best (0.031 PPL) falls within grid-search's own cross-seed variance ($\pm$0.033), eliminating the need for exhaustive search (nine runs to one; 95\% CI of gap $[-0.039, 0.101]$, which includes possible degradation).
8	The advantage extends to $\rho{=}0.6$ ($\Delta{=}{-}0.028$, $p{<}0.01$, $N{=}3$) and transfers to 1.7B without degradation ($\Delta{=}{-}0.01$).
9	An epoch-matched control ($N{=}3$) shows D\&R's full-length advantage is entirely attributable to multi-epoch exposure ($\Delta{=}0.006$ at equal epochs).
10	Detector type matters more than AUC: a discriminative detector (TF-IDF+LR, AUC\,=\,0.94) produces consistent gains, while two generative perplexity detectors (AUC up to 0.91) both reverse the advantage.
11	
12	Soft provenance-based reweighting matches hard filtering at equal data exposure, eliminating both grid search and the multi-epoch training that drives D\&R's apparent advantage.
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-19T05:50:17.157120+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-19T05:50:17.157660+00:00_

1	Web corpora increasingly contain machine-generated text.
2	Recent estimates place the synthetic fraction at 20--60\% of crawled data~\citep{cheng2025contamination}, and this share grows as language models are deployed for content production at scale.
3	Training on such contaminated data has concrete consequences: \citet{shumailov2024model} show that recursive training on model outputs leads to irreversible quality degradation (\emph{model collapse}), and \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger this failure mode, ruling out data scaling as a remedy.
4	A central difficulty is that the contamination proportion in any given corpus is unknown: synthetic text enters through diverse, uncoordinated channels with no centralized provenance record.
5	The prevalence, severity, and opacity of synthetic contamination make contamination-aware training a practical necessity, particularly for continued pretraining on potentially contaminated data.
6	
7	A natural response is \emph{detect-and-reweight}: suppress likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a classifier's synthetic probability estimate.
8	However, the exponent $b$ critically determines outcomes and requires per-model validation-set grid search~\citep{drayson2025detection}; alternative approaches require the exact contamination ratio~\citep{he2025golden} or a well-calibrated detection threshold for hard filtering~\citep{feng2025beyond}.
9	
10	Given per-sample detector scores $q(x)$, how should one choose $b$ without a validation set or known contamination proportion?
11	We formulate this as a dual-constrained optimization over each training batch: find the smallest $b$ that ensures the weighted effective real proportion $\aeff(b)$ reaches a quality threshold $\tau$, while keeping Kish's effective sample size $\mathrm{ESS}(b)$ above a stability floor $\nmin$.
12	The quality constraint has theoretical grounding
…[truncated 3291 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-19T05:50:17.358839+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-19T05:50:17.459708+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy; \citet{dohmatob2024tale} characterize this as a change of scaling laws.
5	\citet{gerstgrasser2024collapse} show that accumulating real data alongside synthetic data can break the recursion, though at substantial collection cost.
6	\citet{cheng2025contamination} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\% of web corpora.
7	As language models are deployed at scale for content generation~\citep{radford2019language,brown2020language,openai2023gpt4}, these results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
8	
9	\paragraph{Detection and Filtering of Machine-Generated Text.}
10	Given the severity of contamination, a natural response is to detect and remove synthetic content.
11	DetectGPT~\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature; Fast-DetectGPT~\citep{bao2024fastdetectgpt} accelerates this with conditional probability curvature; Binoculars~\citep{hans2024binoculars} uses cross-perplexity ratios between two models; Min-$k$\% Prob~\citep{shi2024minkprob} uses the average log-probability of the lowest-$k$\% tokens.
12	All produce continuous confidence scores suitable as input to downstream weighting, including ours.
13	\citet{kirchenbauer2023watermark} propose watermarkin
…[truncated 5042 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-19T05:50:17.660808+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-19T05:50:17.661497+00:00_

1	\subsection{Problem Setup}
2	\label{sec:setup}
3	
4	Let $\mathcal{D} = \mathcal{D}_{\mathrm{real}} \cup \mathcal{D}_{\mathrm{synth}}$ denote a pretraining corpus containing both human-authored and machine-generated text.
5	The contamination ratio $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$ is unknown, a realistic assumption for web-scale corpora where synthetic content enters from diverse, uncoordinated sources~\citep{cheng2025contamination}.
6	
7	A pre-trained detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$.
8	Following \citet{drayson2025detection}, we weight each sample as
9	\begin{equation}
10	  w(x) = (1 - q(x))^{b},
11	  \label{eq:weight}
12	\end{equation}
13	where $b \geq 0$ controls downweighting intensity: $b = 0$ recovers uniform training, while larger $b$ progressively suppresses high-$q$ samples.
14	\citet{drayson2025detection} select $b$ via validation-set grid search, obtaining different optimal values for different model scales ($b{=}10$ for ${\leq}360$M parameters, $b{=}1$ for 1.7B).
15	We instead derive $b$ per-batch from the batch's own $q$-score distribution, requiring no held-out validation data.
16	
17	\subsection{Dual-Constraint Framework}
18	\label{sec:dual}
19	
20	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with detector scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$, we define two batch-level diagnostics that jointly determine $b$.
21	
22	\paragraph{Effective real proportion.}
23	Let $r_i = \mathbf{1}[q_i \leq 0.5]$ estimate whether sample $x_i$ is human-authored.
24	The \emph{effective real proportion}
25	\begin{equation}
26	  \alpha_{\mathrm{eff}}(b) = \frac{\sum_{i=1}^{B} w_i(b) \cdot r_i}{\sum_{i=1}^{B} w_i(b)}
27	  \label{eq:alpha}
28	\end{equation}
29	measures the share of total weight allocated to likely-real samples.
30	The indicator $r_i = \mathbf{1}[q_i \leq 0.5]$ is a proxy for true provenance: $\alpha_{\mathrm{eff}}$ tracks the detector's estimate of the real fraction, not
…[truncated 9713 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 226 · 2026-05-19T05:50:17.963059+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-19T05:50:18.013796+00:00_

1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo2024fineweb} as the real-data source, comparable to typical domain-adaptive continued pretraining budgets~\citep{gururangan2020dont}.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang2025qwen3}, the same architecture used for continued pretraining, and inject them at token-level ratio $\rho = 0.4$ via uniform random mixing.\footnote{$\rho$ denotes the token-level contamination ratio. Because synthetic documents are shorter on average (304 vs.\ 560 words), the document-level synthetic fraction is 55.6\% at $\rho{=}0.4$.}
4	This self-contamination design creates a challenging detection scenario where generator and trainee share the same distribution.
5	
6	\paragraph{Detector.}
7	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split (AUC\,=\,0.939, calibrated ECE\,=\,0.048 after temperature scaling with $T = 0.204$).
8	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
9	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson2025detection}) to test whether score \emph{calibration} may matter as much as raw discrimination for reweighting.
10	To evaluate detector sensitivity, we additionally test two generative baselines: a GPT-2-based perplexity scorer (AUC\,=\,0.913) and an N-gram language model perplexity scorer (AUC\,=\,0.73); results are reported in \S\ref{sec:robustness}.
11	
12	\paragraph{Training.}
13	We continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\,=\,$5{\times}10^{-5}$), max sequence length 2048, and bf16 precision.
14	All main comparisons use three random seeds (42, 123, 456).
15	
16	\paragraph{Evaluation.}
17	We 
…[truncated 1508 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-19T05:50:18.215001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-19T05:50:18.215478+00:00_

1	\subsection{Main Results}
2	\label{sec:main-results}
3	
4	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across three seeds.
5	Continued pretraining reduces PPL from 22.970 (pretrained checkpoint) to the 17.3--17.8 range; the initial 5.2-point drop absorbs the bulk of easy gains, and reweighting method comparisons operate within a narrow residual.
6	
7	Adaptive $\bstar$ achieves PPL competitive with grid-best: 3-seed means 17.651 vs.\ 17.620 for grid $b{=}0.3$ (gap 0.031, 95\% CI $[-0.039, 0.101]$).
8	With only $N{=}3$ seeds, this interval is too wide for formal equivalence testing; we refrain from claiming statistical indistinguishability and instead emphasize the practical value: the adaptive method requires one training run instead of nine~\citep{drayson2025detection}, with lower cross-seed variance ($\pm$0.007 vs.\ $\pm$0.033).
9	Using the mean of per-batch $\bstar$ ($\bar{b}^*{=}1.19$) as a fixed exponent yields PPL 17.693, comparable to uniform (17.694); per-batch adaptation is essential.
10	
11	The ablation hierarchy at $\rho{=}0.4$ (Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random, Table~\ref{tab:main}) reveals two requirements for effective reweighting: detector signal and minimum intervention.
12	Random weights $\mathcal{U}(0,2)$ (mean 17.803) perform worse than uniform (17.694): the detector's $q$-scores carry genuine provenance information, and uninformed reweighting increases gradient variance without corrective signal.
13	ESS-only (mean $17.737 {\pm} 0.017$) uses $q$-scores but maximizes $b$ up to the stability ceiling, concentrating weights on a few high-confidence samples; it provides no improvement over uniform.
14	Only the dual-constrained adaptive method, which limits $b$ to the minimum needed, improves over uniform (paired gap $0.043$, $p{<}0.01$, $N{=}3$).
15	Figure~\ref{fig:grid_b_trend} contextualizes this: the grid curve has a broad plateau at $b \in [0.1, 0.5]$ (PPL 17.620--17.655), and adaptive $\bstar$ (mean 17.651) f
…[truncated 8578 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-19T05:50:18.366294+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-19T05:50:18.366685+00:00_

1	\paragraph{Why minimum intervention works.}
2	In the 38.2\% of batches where $\aeff$ determines $\bstar$, the selected exponent is 4.9$\times$ lower than the ESS-only upper bound (\S\ref{sec:regime}); this rate is robust across contamination levels (33.4\% at $\rho{=}0.6$) and seeds (CV ${<}2\%$).
3	The aggregate mean $\bstar \approx 1.4$ as a fixed exponent yields PPL no better than uniform (17.693 vs.\ 17.694), confirming per-batch adaptation is essential.
4	
5	\paragraph{Failure modes.}
6	At $\rho{=}0.2$, the method degrades ($+$0.046 PPL): detector mean $q{=}0.393$ indicates poor discrimination, yet $\aeff$-binding in ${\sim}$60\% of batches causes active but misdirected reweighting (Appendix~\ref{app:rho02}).
7	Both generative detectors (GPT-2 PPL AUC\,=\,0.91, $\Delta{=}{+}0.10$; N-gram PPL AUC\,=\,0.73, $\Delta{=}{+}0.13$) fail via the same mechanism: conflating predictability with synthetic origin.
8	The method requires discriminative signal targeting provenance rather than fluency.
9	
10	\paragraph{Soft vs.\ hard filtering.}
11	At equal content epochs, D\&R ($17.657 \pm 0.006$) and adaptive $\bstar$ ($17.651 \pm 0.007$) are equivalent ($\Delta{=}0.006$, $N{=}3$).
12	D\&R's best full-length PPL (17.250 at $q{>}0.3$) requires ${\sim}$3.2$\times$ effective compute and a calibrated threshold; the raw U-shaped curve is entirely a multi-epoch artifact (Figure~\ref{fig:dr_dual_curve}).
13	A hybrid ($q{>}0.95$ removal + adaptive, PPL\,=\,17.514) further improves but assigns $w{=}0$, conflicting with minimum intervention; its advantage likely also reflects multi-epoch exposure.
14	
15	\paragraph{$\tau$ and deployment.}
16	$\tau \in [0.5, 0.8]$ all outperform uniform; $\tau \in [0.7, 0.8]$ is robust across $\rho \in \{0.4, 0.6\}$ (Appendix~\ref{app:tau_rho}).
17	$\tau$ remains empirical; theoretical derivation is open (\S\ref{sec:limitations}).
18	Defaults: discriminative detector with AUC ${\geq}$ 0.94, $\tau{=}0.8$, $\nmin{=}\lfloor B/2 \rfloor$.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-19T05:50:18.468198+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-19T05:50:18.468580+00:00_

1	We introduced Minimum Intervention Reweighting, a dual-constraint framework that derives per-batch $\bstar$ from detector scores alone ($\aeff(b) \geq \tau$, $\mathrm{ESS}(b) \geq \nmin$), reducing grid search from nine runs to one; the adaptive-to-grid gap (0.031 PPL) falls within grid-search's own cross-seed variance ($\pm$0.033, 95\% CI $[-0.039, 0.101]$).
2	The ablation confirms both detector signal and minimum intervention are necessary ($\rho{=}0.4$); a 3-seed epoch-matched control shows D\&R's apparent advantage is entirely due to multi-epoch exposure ($\Delta{=}0.006$).
3	Empirically, the advantage diminishes at higher contamination ($\rho{=}0.6$: $\Delta{=}{-}0.028$) and is negligible at 1.7B scale ($\Delta{=}{-}0.01$), suggesting the method's primary value lies in the 0.6B continued pretraining regime tested here.
4	Future work: multi-seed scale confirmation, discriminative detector characterization across architectures, and naturally contaminated corpora.
5	Code and data will be released upon acceptance.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-19T05:50:18.569214+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-19T05:50:18.569623+00:00_

1	\paragraph{Scale and cross-model transfer.}
2	All main experiments use Qwen3-0.6B with batch size 4 on 132--200M tokens, comparable to domain-adaptive continued pretraining but far below full pretraining scale; validation at ${>}$100B tokens remains an important direction.
3	A 1.7B verification (Qwen3-1.7B, $\rho{=}0.4$) under matched conditions shows $\Delta{=}{-}0.01$ (adaptive 13.26 vs.\ uniform 13.26), confirming that the method transfers without degradation but does not demonstrate a clear advantage at this scale; multi-seed replication is needed.
4	Cross-model transfer (Llama-3.2-3B, single seed) shows parity with uniform on PPL and HellaSwag, with a $+$1.6\,pp MMLU advantage that requires replication.
5	
6	\paragraph{Contamination range.}
7	The method improves over uniform at $\rho \in \{0.4, 0.6\}$ but not at $\rho{=}0.2$ ($+$0.046 PPL, 0.26\% relative), indicating an effective range of $\rho \geq 0.4$ with $\tau{=}0.8$.
8	Behavior at $\rho > 0.8$ is untested; extreme contamination may violate the assumption that sufficient real samples exist per batch for meaningful $\aeff$ estimation.
9	Real web-scale contamination is domain-skewed, which may alter within-batch $\aeff$ distributions.
10	
11	\paragraph{Detector coverage.}
12	Three detectors have been tested: TF-IDF+LR (discriminative, AUC\,=\,0.94) succeeds, while GPT-2 perplexity (generative, AUC\,=\,0.91) and N-gram perplexity (generative, AUC\,=\,0.73) both fail.
13	The pattern suggests discriminative signal is necessary, but three detectors from two families cannot distinguish a type effect from a calibration effect; testing additional discriminative detectors at varying AUC levels would isolate the mechanism.
14	
15	\paragraph{Threshold.}
16	$\tau$ is an empirical hyperparameter.
17	The convergence theory of \citet{wang2026survive} assumes a known contamination proportion $\alpha$, which we do not require; bridging this gap to derive $\tau$ from first principles remains open.
18	
19	\paragraph{Evalua
…[truncated 1036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-19T05:50:18.720474+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-19T05:50:18.721091+00:00_

1	\section{Proofs}
2	\label{app:proofs}
3	
4	\begin{proof}[Proof of Proposition~\ref{prop:monotone}]
5	Let $w_i(b) = (1 - q_i)^b$, $W(b) = \sum_{j=1}^B w_j(b)$, and $\pi_i(b) = w_i(b) / W(b)$.
6	Then
7	\begin{equation*}
8	  \alpha_{\mathrm{eff}}(b) = \sum_{i=1}^{B} \pi_i(b)\, r_i,
9	\end{equation*}
10	where $r_i \in \{0, 1\}$ indicates whether sample $i$ is real.
11	Taking the derivative with respect to $b$:
12	\begin{align*}
13	  \frac{d\pi_i}{db}
14	  &= \pi_i \!\left(\frac{d \ln w_i}{db} - \frac{d \ln W}{db}\right)
15	  = \pi_i \!\left(\ln(1{-}q_i) - \sum_j \pi_j \ln(1{-}q_j)\right).
16	\end{align*}
17	Substituting,
18	\begin{align*}
19	  \frac{d\alpha_{\mathrm{eff}}}{db}
20	  &= \sum_i r_i\, \pi_i \!\left(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\right) \\
21	  &= \mathrm{Cov}_{\pi}\!\bigl(r_i,\, \ln(1{-}q_i)\bigr).
22	\end{align*}
23	For any detector with better-than-random discrimination, real samples ($r_i = 1$) have $q_i \leq 0.5$ on average, and thus higher $\ln(1{-}q_i)$ than synthetic samples.
24	The weighted covariance $\mathrm{Cov}_{\pi}(r_i, \ln(1{-}q_i))$ is therefore non-negative, establishing that $\alpha_{\mathrm{eff}}(b)$ is non-decreasing in $b$.
25	\end{proof}
26	
27	\begin{proposition}[ESS monotonicity]
28	\label{prop:ess_mono}
29	$\mathrm{ESS}(b)$ is non-increasing in $b$, and strictly decreasing whenever the batch contains at least two samples with distinct $q$-values.
30	\end{proposition}
31	
32	\begin{proof}
33	Write $\mathrm{ESS}(b) = 1 / \sum_i \pi_i(b)^2$, where $\pi_i(b) = w_i(b) / W(b)$.
34	The denominator $\sum_i \pi_i^2$ is the Herfindahl index $H$.
35	Differentiating $H$ with respect to $b$:
36	\begin{equation*}
37	  \frac{dH}{db} = 2 \sum_i \pi_i^2 \bigl(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\bigr).
38	\end{equation*}
39	This equals $2\,\mathrm{Var}_{\pi^2}[\ln(1{-}q)]$ under the $\pi^2$-weighted measure.
40	Since variance is non-negative and strictly positive when not all $\ln(1{-}q_i)$ coincide (i.e., when at least two $q$
…[truncated 16281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-19T05:50:18.821794+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-19T05:50:18.873259+00:00_

1	% Responsible NLP Research Checklist
2	% https://aclrollingreview.org/responsibleNLPresearch/
3	
4	\section*{Responsible NLP Research Checklist}
5	
6	\subsection*{A. For Every Submission}
7	
8	\begin{itemize}[nosep,leftmargin=*]
9	\item[\checkmark] \textbf{A1.} Did you describe the limitations of your work?
10	\textit{Yes, \S\ref{sec:limitations} discusses scale, contamination range, detector coverage, threshold, evaluation, and effect size limitations.}
11	
12	\item[\checkmark] \textbf{A2.} Did you discuss any potential risks of your work?
13	\textit{Yes. The method assumes a pre-trained detector is available; deploying it with a poorly calibrated detector could degrade training quality (discussed in \S\ref{sec:limitations}, Detector coverage). The method does not generate new content or enable harmful uses beyond standard language model pretraining.}
14	\end{itemize}
15	
16	\subsection*{B. Did You Use or Create Scientific Artifacts?}
17	
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\checkmark] \textbf{B1.} Did you cite the creators of artifacts you used?
20	\textit{Yes. FineWeb~\citep{penedo2024fineweb}, Qwen3~\citep{yang2025qwen3}, and all baseline methods are cited in \S\ref{sec:experiments} and \S\ref{sec:related}.}
21	
22	\item[\checkmark] \textbf{B2.} Did you discuss the license or terms for use and/or distribution of any artifacts?
23	\textit{FineWeb is released under Apache-2.0; Qwen3 under Apache-2.0. Our code and data will be released upon acceptance.}
24	
25	\item[\checkmark] \textbf{B3.} Did you discuss if your use of existing artifacts was consistent with their intended use?
26	\textit{Yes. FineWeb is intended for language model training; we use it as a pretraining corpus. Qwen3 is used for both continued pretraining and synthetic data generation, consistent with its general-purpose design.}
27	
28	\item[\checkmark] \textbf{B4.} Did you discuss the steps taken to check whether the data contains information that names or uniquely identifies individ
…[truncated 3080 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-19T05:50:25.247904+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-19T05:50:25.599488+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-19T05:50:26.122937+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-19T05:50:26.223988+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/decisions.yaml\", \"content\": \"_next_id: 91\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:38 UTC\\n  summary: 投稿目标定为 AAAI 2027 (~Aug 2026)，放弃 EMNLP 2026 ARR May 25\\n  rationale: EMNLP ARR 仅剩 12 天且无任何基础设施，即使 AI 团队速度也无法完成多轮预训练实验。AAAI 2027 有 ~11 周，足够完成\\n    4 phase 全流程。两者均为 A 类会议。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:38 UTC\\n  summary: 'MVP 设计: 单模型(Qwen3-0.6B) + 单污染比例(40%) + 三组对比(uniform/grid-b/adaptive-b*)'\\n  rationale: 核心假设是 adaptive b* 能替代 grid search。最小验证只需一个污染比例下的 A/B/C 对比。40% 选取因为理论和\\n    Strong Model Collapse 均表明该区间效应显著。通过后再扩展到多污染比例/多生成器/多模型。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-13 17:40 UTC\\n  summary: '修正 D001: 主攻 EMNLP 2026 ARR May 25，AAAI 2027 为后备'\\n  rationale: 用户明确指出 EMNLP ARR 5/25 时间不紧、资源会给够。AI 团队 24/7 执行 + 4 卡并行：数据生成 ~2 天、MVP\\n    ~1 天、全矩阵 ~3 天、论文 ~3 天、迭代 ~2 天 = 11 天可完成。12 天 deadline 可行。保守估计完成时间是最大风险。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-13 17:42 UTC\\n  summary: '采纳 Reviewer 4 点 MVP 协议补全: 3 seeds、detector gate、grid-b 定义、kill criteria'\\n  rationale: 'Reviewer 指出 MVP 设计 4 个缺口均合理: (1) 单 seed 无统计保障 → 3 seeds，缩 tokens 到 200M\\n    控预算; (2) 检测器质量是 pipeline 前提 → 加 gate AUC≥0.95/ECE≤0.05; (3) grid search baseline\\n    需可复现 → 定义 b∈{0.5,1,1.5,2,3,5}; (4) 无 fail 路径 → 定义三级 kill/pivot。不增加工程量，只补协议。'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D005\\n  date: 2026-05-13 22:08 UTC\\n  summary: 识别 q-score 极化风险：AUC=0.999998 可能导致 adaptive b* vs grid-b 对比退化，制定分级应对方案\\n  rationale: 'Reviewer 审查发现 detector eval_auc=0.999998（step 2000），q-score 可能高度双峰化。若校准后\\n    >95% 样本 q<0.05 或 q>0.95，则 w=(1-q)^b 对所有 b>0 约等于 0，不同 b 值间无区分度。MVP 技术上可能 PASS（adaptive\\n    ≈ grid-b，满足 ≥90% 条件），但无法证明核心贡献（自适应精细调优的价值）。\\n\\n\\n    应对方案（detector 完成后按 q-score 分布分级执行）：\\n\\n    - 分布有spread（q 在 0.1
…[truncated 1474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-19T05:50:26.224380+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-19T05:50:26.224600+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-19T05:50:29.488292+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 247 · 2026-05-19T05:50:29.991572+00:00_

1	% References for Minimum Intervention Reweighting paper
2	% Note: entries to be verified via verify_references before final submission
3	
4	@article{drayson2025detection,
5	  title={Machine-Generated Text Detection Prevents Language Model Collapse},
6	  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
7	  journal={arXiv preprint arXiv:2502.15654},
8	  year={2025}
9	}
10	
11	@article{he2025golden,
12	  title={Golden Ratio Weighting Prevents Model Collapse},
13	  author={He, Hengzhi and Xu, Shirong and Cheng, Guang},
14	  journal={arXiv preprint arXiv:2502.18049},
15	  year={2025}
16	}
17	
18	@article{wang2026survive,
19	  title={Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training},
20	  author={Wang, Kevin and Niu, Hongqian and Li, Didong},
21	  journal={arXiv preprint arXiv:2602.16065},
22	  year={2026}
23	}
24	
25	@article{shumailov2024model,
26	  title={{AI} Models Collapse When Trained on Recursively Generated Data},
27	  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
28	  journal={Nature},
29	  volume={631},
30	  pages={755--759},
31	  year={2024}
32	}
33	
34	@inproceedings{dohmatob2025strong,
35	  title={Strong Model Collapse},
36	  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
37	  booktitle={ICLR},
38	  year={2025}
39	}
40	
41	@article{vehtari2024psis,
42	  title={Pareto Smoothed Importance Sampling},
43	  author={Vehtari, Aki and Simpson, Daniel and Gelman, Andrew and Yao, Yuling and Gabry, Jonah},
44	  journal={JMLR},
45	  year={2024}
46	}
47	
48	@inproceedings{sow2025dynamic,
49	  title={Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining},
50	  author={Sow, Daouda and Woisetschl{\"a}ger, Herbert and Bulusu, Saikiran and Wang, Shiqiang and Jacobsen, Hans-Arno and Liang, Yingbin},
51	  booktitle={ICLR},
52	  year={2025}
53	
…[truncated 11064 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-19T05:50:30.142656+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-19T05:50:30.193379+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-19T05:50:36.070054+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "glob": "*.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
    "glob": "*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-19T05:50:36.120725+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-19T05:50:40.495091+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-19T05:50:40.550793+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 55
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-19T05:50:40.985097+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-19T05:50:41.056153+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_reports/round_2.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 71
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-19T05:51:32.724178+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的侧重**: 方法严谨性 + 实验设计 + 统计推断\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 Main Conference（通过 ARR May 2026 cycle 提交）\n- **截止日期**: 2026-05-25\n- **正文页数**: 8 页（参考文献不限）\n- **模板**: ACL 官方 style files，双栏格式\n- **匿名规则**: Double-blind\n- **必需**: Limitations section + Responsible NLP Research Checklist\n\n### 论文信息\n- **标题**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\n- **论文路径**: `projects/provenance_weight_training/docs/paper/main.tex`\n  - Sections 在 `docs/paper/sections/` 下: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, results.tex, discussion.tex, conclusion.tex, limitations.tex, checklist.tex, appendix.tex\n  - 引用: `docs/paper/references.bib`\n\n### 审查重点（你的职责）\n\n1. **方法严谨性**:\n   - Dual-constraint framework（α_eff ≥ τ, ESS ≥ n_min）的数学推导是否正确、完备？\n   - Proposition 1（α_eff 单调性）的证明是否严密？proof sketch 是否充分？\n   - ESS 单调性（Proposition 2）是否正确？\n   - \"Minimum intervention\" 语义是否有理论支撑，还是仅仅是设计选择？\n   - α_eff 作为 true real fraction 的 proxy 是否可靠？r_i = 1[q_i ≤ 0.5] 这个 indicator 的合理性？\n   - 超参数 τ=0.8 和 n_min=⌊B/2⌋ 的选择是否有充分依据？\n\n2. **实验设计**:\n   - 自污染设计（Qwen3-0.6B 生成 + 同模型训练）的合理性和局限性\n   - 132M tokens 的数据规模是否足以支撑结论？\n   - Batch size 4（micro-batch）下计算 α_eff 的统计可靠性（只有 5 个离散值）\n   - Grid search baseline（9 个 b 值，post-hoc 最优选择）是否公平？\n   - Epoch-matched control 的实验设计是否正确？是否真的消除了 multi-epoch confound？\n   - 3 seeds 的统计检验力是否充足？95% CI [-0.039, 0.101] 包含正值的含义\n\n3. **统计推断**:\n   - \"competitive with grid-best\" 的 claim 是否被数据支撑？（CI 包含 degradation）\n   - p < 0.01（N=3）的可信度\n   - 效应量（0.043 PPL at ρ=0.4）的实际意义\n   - 1.7B 结果（Δ=-0.01，2 seeds）能否支撑 \"transfers without degradation\" 的 claim？\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的侧重**: 方法严谨性 + 实验设计 + 统计推断\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 Main Conference（通过 ARR May 2026 cycle 提交）\n- **截止日期**: 2026-05-25\n- **正文页数**: 8 页（参考文献不限）\n- **模板**: ACL 官方 style files，双栏格式\n- **匿名规则**: Double-blind\n- **必需**: Limitations section + Responsible NLP Research Checklist\n\n### 论文信息\n- **标题**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\n- **论文路径**: `projects/provenance_weight_training/docs/paper/main.tex`\n  - Sections 在 `docs/paper/sections/` 下: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, results.tex, discussion.tex, conclusion.tex, limitations.tex, checklist.tex, appendix.tex\n  - 引用: `docs/paper/references.bib`\n\n### 审查重点（你的职责）\n\n1. **方法严谨性**:\n   - Dual-constraint framework（α_eff ≥ τ, ESS ≥ n_min）的数学推导是否正确、完备？\n   - Proposition 1（α_eff 单调性）的证明是否严密？proof sketch 是否充分？\n   - ESS 单调性（Proposition 2）是否正确？\n   - \"Minimum intervention\" 语义是否有理论支撑，还是仅仅是设计选择？\n   - α_eff 作为 true real fraction 的 proxy 是否可靠？r_i = 1[q_i ≤ 0.5] 这个 indicator 的合理性？\n   - 超参数 τ=0.8 和 n_min=⌊B/2⌋ 的选择是否有充分依据？\n\n2. **实验设计**:\n   - 自污染设计（Qwen3-0.6B 生成 + 同模型训练）的合理性和局限性\n   - 132M tokens 的数据规模是否足以支撑结论？\n   - Batch size 4（micro-batch）下计算 α_eff 的统计可靠性（只有 5 个离散值）\n   - Grid search baseline（9 个 b 值，post-hoc 最优选择）是否公平？\n   - Epoch-matched control 的实验设计是否正确？是否真的消除了 multi-epoch confound？\n   - 3 seeds 的统计检验力是否充足？95% CI [-0.039, 0.101] 包含正值的含义\n\n3. **统计推断**:\n   - \"competitive with grid-best\" 的 claim 是否被数据支撑？（CI 包含 degradation）\n   - p < 0.01（N=3）的可信度\n   - 效应量（0.043 PPL at ρ=0.4）的实际意义\n   - 1.7B 结果（Δ=-0.01，2 seeds）能否支撑 \"transfers without degradation\" 的 claim？\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-19T05:51:49.456541+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16732
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-19T05:51:49.758002+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的侧重**: 新颖性 + 叙事完整性 + Related Work 覆盖 + 写作与格式规范\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 Main Conference（通过 ARR May 2026 cycle 提交）\n- **截止日期**: 2026-05-25\n- **正文页数**: 8 页（参考文献不限）\n- **模板**: ACL 官方 style files，双栏格式\n- **匿名规则**: Double-blind\n- **必需**: Limitations section + Responsible NLP Research Checklist\n\n### 论文信息\n- **标题**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\n- **论文路径**: `projects/provenance_weight_training/docs/paper/main.tex`\n  - Sections 在 `docs/paper/sections/` 下: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, results.tex, discussion.tex, conclusion.tex, limitations.tex, checklist.tex, appendix.tex\n  - 引用: `docs/paper/references.bib`\n\n### 审查重点（你的职责）\n\n1. **新颖性评估**:\n   - 与 Drayson et al. (2025) 的区分度是否充分？（同一公式 w=(1-q)^b，区别在于 b 的选择方式）\n   - \"Dual-constraint framework\" 是否构成 sufficient novelty for EMNLP？\n   - 三个 Contribution 的 claim 是否过大或过小？\n   - \"Minimum intervention\" 作为概念的新颖性如何？\n\n2. **叙事完整性与主线统一**:\n   - Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成连贯主线？\n   - 是否存在 \"Introduction 讲故事 A，Results 讲故事 B\" 的脱节？\n   - Contribution 列表中的每一条是否都有实验支撑？\n   - Limitations 是否诚实且完整？（论文自己承认 ρ=0.2 失败、downstream 结果 mixed、1.7B 无优势——是否还遗漏了什么？）\n   - 结论是否与实验结果一致？是否存在 overclaiming？\n\n3. **Related Work 覆盖**:\n   - 是否遗漏了重要的相关工作？请用 web search 检查以下方向的最新论文：\n     - Model collapse prevention (2024-2026)\n     - Data reweighting for LLM pretraining (2024-2026)\n     - Machine-generated text detection applied to training (2024-2026)\n   - 与 Drayson et al. (2025) 的对比是否准确且公平？\n   - 引用密度是否符合 EMNLP 标准？（当前 41 条引用）\n\n4. **写作与格式规范**:\n   - AI 写作痕迹检查：em-dash (—)、解释性 en-dash (–)、-ing 分词短语结尾、过度分段\n   - 专有名词/缩写首次出现是否有定义？\n   - 图表质量：caption 是否自包含？信息密度是否足够？\n   - 格式合规：是否使用 ACL review 模板？行号是否开启？页数是否在限制内？\n   - Checklist 是否认真填写？\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues → Missing References",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的侧重**: 新颖性 + 叙事完整性 + Related Work 覆盖 + 写作与格式规范\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 Main Conference（通过 ARR May 2026 cycle 提交）\n- **截止日期**: 2026-05-25\n- **正文页数**: 8 页（参考文献不限）\n- **模板**: ACL 官方 style files，双栏格式\n- **匿名规则**: Double-blind\n- **必需**: Limitations section + Responsible NLP Research Checklist\n\n### 论文信息\n- **标题**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\n- **论文路径**: `projects/provenance_weight_training/docs/paper/main.tex`\n  - Sections 在 `docs/paper/sections/` 下: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, results.tex, discussion.tex, conclusion.tex, limitations.tex, checklist.tex, appendix.tex\n  - 引用: `docs/paper/references.bib`\n\n### 审查重点（你的职责）\n\n1. **新颖性评估**:\n   - 与 Drayson et al. (2025) 的区分度是否充分？（同一公式 w=(1-q)^b，区别在于 b 的选择方式）\n   - \"Dual-constraint framework\" 是否构成 sufficient novelty for EMNLP？\n   - 三个 Contribution 的 claim 是否过大或过小？\n   - \"Minimum intervention\" 作为概念的新颖性如何？\n\n2. **叙事完整性与主线统一**:\n   - Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成连贯主线？\n   - 是否存在 \"Introduction 讲故事 A，Results 讲故事 B\" 的脱节？\n   - Contribution 列表中的每一条是否都有实验支撑？\n   - Limitations 是否诚实且完整？（论文自己承认 ρ=0.2 失败、downstream 结果 mixed、1.7B 无优势——是否还遗漏了什么？）\n   - 结论是否与实验结果一致？是否存在 overclaiming？\n\n3. **Related Work 覆盖**:\n   - 是否遗漏了重要的相关工作？请用 web search 检查以下方向的最新论文：\n     - Model collapse prevention (2024-2026)\n     - Data reweighting for LLM pretraining (2024-2026)\n     - Machine-generated text detection applied to training (2024-2026)\n   - 与 Drayson et al. (2025) 的对比是否准确且公平？\n   - 引用密度是否符合 EMNLP 标准？（当前 41 条引用）\n\n4. **写作与格式规范**:\n   - AI 写作痕迹检查：em-dash (—)、解释性 en-dash (–)、-ing 分词短语结尾、过度分段\n   - 专有名词/缩写首次出现是否有定义？\n   - 图表质量：caption 是否自包含？信息密度是否足够？\n   - 格式合规：是否使用 ACL review 模板？行号是否开启？页数是否在限制内？\n   - Checklist 是否认真填写？\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues → Missing References",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-19T05:51:51.223053+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1465
}
```

</details>

---


### Assistant

_source line 260 · 2026-05-19T05:51:55.483898+00:00_

Round 1 任务已分配给两位 Reviewer。

- **Reviewer 1** → 方法严谨性 + 实验设计 + 统计推断
- **Reviewer 2** → 新颖性 + 叙事完整性 + Related Work + 格式

等待两位 Reviewer 返回独立初审意见，收到后进入 Step 2（交叉分享 + 逐条回应）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 20

## Round 20

2 recorded events


### User

_source line 261 · 2026-05-19T05:57:18.076615+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见

**论文**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining
**审查侧重**: 新颖性 + 叙事完整性 + Related Work 覆盖 + 写作与格式规范

---

## 总体评分

**Overall**: 3/5 (Findings)
**一句话总结**: 技术正确、诚实透明的工作，corrective findings（D&R epoch confound、detector type）有价值，但核心方法相对 Drayson et al. (2025) 新颖性不足，效果量小且实验范围有限，达到 Findings 水平但距离 Main Conference 有差距。

## 官方维度打分（ACL ARR Review Form, Feb 2025+）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 (Acceptable) | 方法技术正确（命题、证明完整），但效果量极小（0.043 PPL），自污染实验设计限制结论泛化性，downstream 结果 4/5 为负 |
| Excitement | 2/5 (Potentially Interesting) | 核心方法对 Drayson et al. 增量有限（同一公式，不同 b 选择策略）；corrective findings 有社区价值但不构成方法论突破 |
| Reproducibility | 4/5 | 超参数、训练细节、detector 配置描述充分；承诺 code release；3-seed 主实验 |
| Confidence | 4/5 | 该领域在我的专长范围内，仔细检查了技术 claims |
| **Overall** | **3/5 (Findings)** | 见下方详细分析 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 与 Drayson et al. (2025) 的区分度不足以支撑 Main Conference 新颖性

- 具体位置：Section 2 (Related Work, paragraph 3)、Section 3 (Method)、Introduction contribution list
- 问题：论文使用与 Drayson et al. **完全相同的公式** $w=(1-q)^b$。全部创新在于 b 的选择方式。论文声称三点差异（Section 2, Related Work 第三段 (i)(ii)(iii)）：
  - (i) per-batch vs fixed b：合理但属于 engineering improvement
  - (ii) loss reweighting vs SIR resampling：实现层面的选择差异，非方法论贡献
  - (iii) lightweight detector suffices：这是一个实验发现，不是方法贡献
  - α_eff 约束来自 Wang et al. (2026) 的收敛理论的直接应用；ESS 约束是 importance sampling 的标准做法 (Kish, 1965)
  - "Minimum intervention" 概念优雅但 thin：本质上是在两个单调函数上做 bisection 取下界
- 为什么影响接收：EMNLP Main Conference 要求 sufficient novelty。同一公式 + 不同超参数选择策略 = 增量贡献。论文最有价值的部分（D&R epoch confound, detector type finding）反而是 **分析性发现** 而非方法贡献，但论文 framing 为方法论文
- 建议修改方向：(a) 重新 frame 论文：将 D&R epoch confound 和 detector type 发现提升为主要贡献，方法作为副产品；(b) 在更多场景下验证方法的 generalization（多种 generator、自然污染语料），以实用价值弥补理论新颖性不足

**N2** [critical] 效果量极小，实际意义不明

- 具体位置：Table 1 (Section 5.1)、Section 5.2、Limitations
- 问题：
  - ρ=0.4: Δ = -0.043 PPL (0.24% relative), 95% CI [-0.039, 0.101] **包含退化**
  - ρ=0.6: Δ = -0.028 PPL
  - 1.7B: Δ = -0.01 (negligible)
  - Downstream: 4/5 benchmarks 显示 uniform 略优（Table 8, Appendix F）
  - 统计显著（p<0.01）但 practical significance 未讨论
- 为什么影响接收：在 continued pretraining 已经吸收了 5.2 PPL 的 easy gains 之后（22.970 → 17.6），0.043 PPL 的改进是否值得引入一套新框架？downstream 结果反向更令人担忧——PPL 改进可能仅反映 distribution matching（训练数据更接近 human-only 评估集）而非 genuine quality gain
- 建议：(a) 明确讨论 effect size 的 practical significance；(b) 补充更多 downstream tasks 和多 seed 评估；(c) 考虑 PPL 改进是否为 distribution matching artifact

**N3** [critical] 自污染实验设计严重限制泛化性

- 具体位置：Section 4 (Experimental Setup), paragraph 1 ("Training Data")
- 问题：Qwen3-0.6B 既是 synthetic data generator 又是 trainee model（self-contamination）。这是检测最容易的场景——generator 和 trainee 共享同一分布。现实 web 污染涉及多种 generators（GPT-4, Claude, Gemini, 各种 fine-tuned models），风格差异大，检测难度高得多。Limitations section 提到 scale 和 detector coverage，但**未讨论 self-contamination 这一根本性设计局限**
- 为什么影响接收：TF-IDF+LR 在 self-contamination 场景下达到 AUC=0.939 可能不具代表性。如果检测器在真实多源污染下表现不同，整套方法的前提（reliable q-scores）可能不成立
- 建议：(a) Limitations 中明确讨论 self-contamination 限制；(b) 至少补充一个 cross-generator 场景（Appendix G 的 Llama-3.2-3B 是 cross-generator 但结果 mixed 且无 PPL 对比）

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] "D&R" 缩写在 Abstract 和 Introduction 中使用但未定义

- 具体位置：Abstract line 9 ("D&R's full-length advantage"), line 12; Introduction contribution #2
- 问题：全称 "Detect & Remove" 首次出现在 Section 4 (Experimental Setup)，但 Abstract 和 Introduction 已多次使用 "D&R"
- 建议：Abstract 和 Introduction 首次使用时写全称 "Detect and Remove (D&R)"

**W2** [warning] "robust defaults" 声明验证不足

- 具体位置：Section 5.4 (Hyperparameter Sensitivity)、Section 3.4
- 问题：τ 的 safe range [0.5, 0.8] 基于 ρ=0.4, seed 42 的单次 sweep。ρ=0.6 时 optimal 已经 shift 到 τ=0.7（Figure 7, Appendix D）。n_min = ⌊B/2⌋ 的 default 在 B∈{4,8,16} 验证但只在一个 contamination level。声称 "empirically robust defaults that transfer without per-model tuning"（Section 5.4 最后一句）过于自信
- 建议：弱化 "robust defaults" 表述，改为 "default values that perform well in the tested configurations"

**W3** [warning] Grid search 在 ρ=0.6 为单 seed

- 具体位置：Table 5 (Appendix E)
- 问题：ρ=0.6 的 Grid (b=0.3) 结果仅 seed 42 (17.634)。Adaptive-vs-Grid gap (0.106) 基于单 seed 比较，不可靠。ρ=0.4 的 Grid 3-seed variance 高达 ±0.033，说明单 seed Grid 结果波动大
- 建议：补充 ρ=0.6 的 3-seed Grid 结果，或明确标注该比较为 single-seed preliminary

**W4** [warning] 缺少重要的近期相关工作

- 具体位置：Section 2 (Related Work)
- 问题：以下 2025 年论文与本文直接相关但未引用：
  1. **Kang et al. (EMNLP 2025)**: "Demystifying Synthetic Data in LLM Pre-training" — 大规模研究 (>1000 LLMs) synthetic data mixing 对 pretraining 的影响，含 scaling laws 分析，直接相关于本文的 contamination-aware training 主题
  2. **Zhang et al. (2025, arXiv:2509.08972)**: "ForTIFAI: Fending Off Recursive Training Induced Failure" — 通过 Truncated Cross-Entropy loss 修改防止 model collapse，提供了不依赖检测器的替代方案，应在 Related Work 中讨论
  3. **Yi et al. (2025, arXiv:2510.16657)**: "Escaping Model Collapse via Synthetic Data Verification" — 理论分析 verifier-guided retraining 的 near-term improvements 和 long-term convergence，与本文的 α_eff 理论动机相关
- 当前 41 条引用对 EMNLP 来说偏少（覆盖 model collapse + data reweighting + MGT detection 三个活跃方向）
- 建议：补充上述引用并在 Related Work 中讨论其与本文方法的关系

**W5** [warning] Downstream 评估不充分

- 具体位置：Table 8 (Appendix F)
- 问题：仅 5 个 benchmarks, single seed (42), 4/5 显示 uniform 略优。sign test p≈0.19 虽未达显著性，但 4/5 negative 的 pattern 值得警惕。论文在 Limitations 承认但未充分解释：PPL 改进是否仅反映 training data 更接近 human-only 评估集（distribution matching artifact），而非真正的模型质量提升？
- 建议：(a) 多 seed downstream 评估；(b) 在 Discussion 中明确讨论 PPL vs downstream 的 divergence 及其含义

**W6** [warning] Micro-batch B=4 下 α_eff 仅取 5 个离散值，bisection 的理论优雅性在实践中被削弱

- 具体位置：Section 3.3 (Algorithm), Appendix H (Table 6)
- 问题：B=4 时 α_eff ∈ {0, 0.25, 0.5, 0.75, 1.0}。在如此粗粒度的函数上做 bisection 与其说是连续优化，不如说是 5-way case dispatch。Pearson r≈0.70 与 true real fraction 的相关性是 moderate，不是 strong。方法在 Section 3 的理论叙事（连续单调函数上的 bisection）与 B=4 的实际实现之间存在 gap
- 建议：(a) 承认 B=4 时 bisection 退化为离散 lookup；(b) 讨论更大 micro-batch 是否会带来不同结论（B=16 结果在 Appendix 但未深入分析）

---

## 小问题（不影响接收）

- Introduction line 21: "4.9× more aggressive (mean ratio)" 中 "mean ratio" 歧义——是 ratio of means 还是 mean of ratios？
- Abstract 和正文大量使用 `{=}` 紧凑写法（如 ρ{=}0.6），在某些 LaTeX 配置下可能渲染异常，建议检查编译输出
- `wang2026survive` (arXiv:2602.16065) 是 2026 年的 arXiv preprint，这个日期需要核实是否真实存在（2026 年 2 月的 arXiv 论文在审稿时可能尚未公开足够久）
- Conclusion "Code and data will be released upon acceptance" — 建议通过 anonymous GitHub 提供 code 供审稿人验证
- Table 1 caption: "Best per column in **bold**" 但 Detect & Remove 的 bold 与 Grid 的 bold 分属不同 comparison groups（一个有 epoch confound），建议分开标注或用不同标记

---

## 主要优势

1. **诚实透明**：论文对自身局限性的讨论异常坦诚（ρ=0.2 失败、downstream mixed、1.7B 无优势、CI 包含退化）。这在该领域少见，值得肯定
2. **D&R epoch confound 发现**：Table 2 的 epoch-matched 实验干净地分离了 data exposure 和 filtering quality 的贡献。这一 corrective finding 对社区有独立价值，无论方法本身是否被接受
3. **Detector type 发现**：discriminative vs generative detector 的对比（Table 9, Appendix G）揭示了 AUC 不等于 reweighting effectiveness 的 insight，有实用指导意义
4. **叙事完整性好**：Abstract → Introduction → Method → Results → Discussion → Conclusion 主线连贯，"minimum intervention" 作为概念线索贯穿始终
5. **写作干净**：无 em-dash/en-dash AI 痕迹，无过度分段，无 -ing 分词短语结尾，用词精准技术性强
6. **格式合规**：使用 ACL review 模板 (`\usepackage[review]{acl}`)，匿名化正确，有 Limitations section 和 Responsible NLP Research Checklist（且 checklist 认真填写，非敷衍）

---

## 缺失引用汇总

| 论文 | 为什么相关 |
|------|-----------|
| Kang et al. (EMNLP 2025) "Demystifying Synthetic Data in LLM Pre-training" | 大规模 synthetic data mixing 研究，直接相关 |
| Zhang et al. (2025) "ForTIFAI" (arXiv:2509.08972) | 不依赖检测器的 model collapse prevention 替代方案 |
| Yi et al. (2025) "Escaping Model Collapse via Synthetic Data Verification" (arXiv:2510.16657) | Verifier-guided retraining 理论分析 |

---

## 审稿总结

这是一篇技术执行干净、写作诚实的论文，但核心方法对 Drayson et al. (2025) 的增量有限（同一公式，不同 b 选择策略），效果量小且实验范围窄。论文最有价值的贡献是两个 corrective/analytical findings（D&R epoch confound 和 detector type effect），而非方法本身。建议重新考虑 framing——如果以 analytical study 为主、method 为辅，可能更好地匹配论文的实际贡献。当前状态适合 Findings 但不足以支撑 Main Conference 接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 262 · 2026-05-19T05:57:25.136907+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 21

## Round 21

2 recorded events


### User

_source line 263 · 2026-05-19T05:57:27.758275+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：评分 Overall 3/5 (Findings level)。三个 critical 问题：(1) 与 Drayson et al. 使用同一公式，新颖性不足以支撑 Main Conference；(2) 效果量极小（0.043 PPL），95% CI 包含退化，downstream 4/5 为负；(3) self-contamination 实验设计限制泛化性。主要优势：论文诚实透明，D&R epoch confound 和 detector type 两个 corrective findings 有独立社区价值，写作干净无 AI 痕迹，格式完全合规。建议重新 frame 为 analytical study 而非 method paper，以更好匹配实际贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 264 · 2026-05-19T05:57:33.259035+00:00_

Reviewer 2 意见已收到。等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 22

## Round 22

6 recorded events


### User

_source line 265 · 2026-05-19T05:57:34.767992+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 — Round 1 审稿意见

### Paper Summary

本文提出 Minimum Intervention Reweighting (MIR)，一种用于污染感知预训练的自适应指数选择方法。给定 detect-and-reweight 框架 w(x) = (1-q(x))^b，作者提出 per-batch 双约束优化：找最小的 b 使得 weighted effective real proportion α_eff(b) ≥ τ（质量下限），同时保持 ESS(b) ≥ n_min（稳定性上限）。在 Qwen3-0.6B 上的 132M token 续训实验中，自适应方法与 grid search 最优值竞争（gap 0.031 PPL），同时将搜索成本从 9 次训练降至 1 次。论文还发现 D&R 相对于 reweighting 的优势完全来自多 epoch 暴露，以及判别式检测器（而非生成式）是 reweighting 有效性的必要条件。

---

## 总体评分

**Overall**: 2.5 / 5 (Borderline Findings)
**一句话总结**: 框架设计清晰、epoch-matched 发现有价值，但效应量极小且未能转移到下游任务或更大规模，核心统计推断力不足以支撑主要 claims。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0 / 5 | 数学推导基本正确，但实验证据与 claims 之间存在系统性落差：CI 包含降级、下游评估为负、1.7B 仅 2 seeds |
| Excitement | 2.5 / 5 | 问题重要且 framing 清楚，但 0.043 PPL 的效应量（0.24% 相对改善）在实际应用中意义有限，且方法在 ρ=0.2 失败、ρ=0.6 减弱、1.7B 消失 |
| Reproducibility | 4.0 / 5 | 算法、超参、训练配置描述充分；代码承诺发布但尚未提供 |
| Reviewer Confidence | 4 / 5 | 熟悉 importance weighting、LM pretraining 和统计推断 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 效应量极小，下游任务不支持 PPL 改善的实际意义

- 具体位置：Table 1 (main results), Table 8 (downstream, Appendix D)
- 问题：核心 PPL 改善为 0.043（17.694 → 17.651，0.24% 相对），发生在已被续训吸收 5.2 PPL 的"残差"区间内。更关键的是，Table 8 的下游评估显示 5 个 benchmark 中 4 个为负 Δ（ARC-C -0.005, ARC-E -0.007, HellaSwag -0.005, WinoGrande -0.008），仅 PIQA 微正（+0.001）。sign-test p ≈ 0.19，suggestive but not significant。
- 为什么影响接收：如果 PPL 改善无法转化为任何可测量的下游增益，那么方法的实际价值存疑。论文 §Limitations 承认"the PPL improvement may partly reflect distribution matching (training data closer to the human-only evaluation set) rather than a generalizable quality gain"，但这一关键限制被藏在 Limitations 而非 Results 或 Abstract 中。Abstract 和 Introduction 的 framing 给出了比实际证据更强的印象。
- 建议修改方向：(1) 在 Results 正文中报告下游结果（而非仅 Appendix），并诚实讨论 PPL-downstream 脱节；(2) 多 seed 下游评估以判断趋势是否稳定；(3) 考虑在 Abstract 中明确 PPL 改善的局限性。

**N2** [critical] 1.7B "transfers without degradation" 的 claim 缺乏统计支撑

- 具体位置：§5.2 (Scale and detector signal), §Conclusion, §Limitations
- 问题：1.7B 结果基于 2 seeds（13.25, 13.27），uniform baseline 仅 1 seed（13.26）。Δ = -0.01 在任何标准下都无法区分 noise 和 signal。2 个数据点无法计算有意义的 CI 或 p-value。论文 Conclusion 称"the advantage observed at 0.6B does not amplify"，但实际上连"advantage 是否存在"都无法判断。
- 为什么影响接收：这是三个 Contribution 的实验基础之一。如果 1.7B 结果不可靠，method 的 scale transfer claim 就悬空了。
- 建议修改方向：(1) 至少 3 seeds for both adaptive 和 uniform at 1.7B；(2) 或明确降级 claim 为 "preliminary evidence"，不在 Abstract/Conclusion 中作为 contribution。

**N3** [critical] "competitive with grid-best" 的 framing 与 CI 不一致

- 具体位置：Abstract, §5.1, §Conclusion
- 问题：95% CI of gap 为 [-0.039, 0.101]。这意味着自适应方法可能比 grid-best 差 0.101 PPL，而 grid-best 自身的 cross-seed 标准差为 ±0.033。Abstract 称 "the gap (0.031 PPL) falls within grid-search's own cross-seed variance (±0.033)"，但这种比较混淆了两个不同的统计量：gap 的 CI 是 paired variability 的函数，cross-seed variance 是 marginal variability。CI 包含 0 本身不构成等价性证据——N=3 下 CI 过宽是 power 不足的结果，不是等价性的证明。
- 论文 §5.1 确实写了 "we refrain from claiming statistical indistinguishability"，但 Abstract 和 Conclusion 的措辞隐含了等价性 claim。
- 为什么影响接收：核心 claim 的统计逻辑不成立。
- 建议修改方向：(1) Abstract 中明确 CI 包含降级的可能性；(2) 增加 seeds 以缩窄 CI；(3) 若无法增加 seeds，将 claim 明确为"point estimate competitive, but wide CI prevents formal equivalence"。

**N4** [critical] Batch size B=4 下 α_eff 仅有 5 个离散值，bisection 搜索的意义存疑

- 具体位置：§3.3 (Algorithm), §3.4 (Hyperparameters), Appendix F (α_eff Proxy Validation)
- 问题：B=4 时，α_eff(0) 取值仅有 {0, 0.25, 0.5, 0.75, 1.0}。r_i ∈ {0,1} 的 4 个值之和除以 4，最多 5 种可能。这意味着 bisection 搜索 b_τ 使得 α_eff(b) = τ = 0.8 时，α_eff 作为 b 的函数是一个最多有 4 个跳跃点的阶梯函数。整个"连续优化"框架在 B=4 下退化为一个极粗粒度的离散选择。
- Appendix Table 5 报告 Pearson r ≈ 0.70, MAE = 0.114。r=0.70 意味着 51% 的方差未被解释；MAE=0.114 意味着平均 11.4% 的估计误差。这对于一个声称提供"quality floor"的指标来说是相当粗糙的。
- 论文辩称 "PPL differs by <0.01 across B ∈ {4, 8, 16}"，但这些实验的细节（多少 seeds？哪些 B 值实际测试了？）不够清楚。
- 为什么影响接收：方法的核心机制——per-batch α_eff-driven b* selection——在实际使用的 batch size 下几乎丧失了设计中的连续性和精度。如果 B=4 和 B=16 的 PPL 差异 <0.01，且 B=4 下 α_eff 如此粗糙，那是否说明 per-batch adaptation 的价值主要不在于 α_eff 的精确值，而在于其他因素？这需要更深入的分析。
- 建议修改方向：(1) 在方法 section 中明确讨论 B=4 下的离散化问题及其对 bisection 的影响；(2) 提供 B=8 和 B=16 的多 seed 结果以验证 robustness claim；(3) 分析 α_eff-binding 在不同 B 下的频率和 b* 分布变化。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 自污染设计（self-contamination）的生态效度有限

- 具体位置：§4 (Experimental Setup), §Limitations
- 问题：用 Qwen3-0.6B 生成合成数据再训练同模型，是一种特殊的自污染场景。真实 web 污染来自多种不同模型、不同大小、非均匀混合。论文的 cross-model 结果（Llama-3.2-3B generator, Appendix H）是单 seed 且结果 mixed（MMLU +1.57pp, HellaSwag -0.60pp），无法支撑泛化性。
- 建议：(1) 至少测试一个"强生成器 + 弱训练模型"场景（如 GPT-4 生成 → 0.6B 训练）；(2) 或明确将 self-contamination 标注为主要假设限制。

**W2** [warning] 132M tokens 的规模太小，结论的可迁移性未知

- 具体位置：§4, §Limitations
- 问题：132M tokens 对应 domain-adaptive continued pretraining，但论文动机和 introduction 讨论的是 web-scale 污染场景。方法在 1.7B 上已无 measurable advantage (Δ=-0.01)。论文 Conclusion 诚实地承认"the method's primary value lies in the 0.6B continued pretraining regime tested here"，但 Introduction 和 Abstract 的 framing 没有反映这一限制。
- 建议：Introduction 中明确方法的目标场景是 continued pretraining（而非 from-scratch pretraining），并在 Abstract 中限定 scope。

**W3** [warning] Epoch-matched 对比存在潜在混淆变量

- 具体位置：§5.1 (Hard filtering and the epoch confound), Table 2
- 问题：D&R epoch-matched 运行 2,533 步（vs. adaptive 6,103 步），以匹配约 1.0 content epoch。但两个实验的 cosine learning rate schedule 总长度不同（2,533 vs. 6,103 步），这意味着 warmup 比例和 decay 曲线不同。D&R epoch-matched 可能因为更短的 schedule 导致 under-optimization（更少的 gradient updates），也可能因为更快的 decay 受益。这个混淆变量未被讨论。
- 更严格的设计是：两个方法使用相同总步数但不同 data pipeline（adaptive 看所有数据一次，D&R 过滤后用剩余数据填充到相同步数但不重复）。
- 为什么重要：Contribution 2 的核心 claim——"D&R's reported advantage over reweighting is entirely a multi-epoch artifact"——依赖于这个 epoch-matched 设计的正确性。
- 建议：(1) 讨论 LR schedule 差异对结果的潜在影响；(2) 或提供控制实验（相同步数 + 不同 data pipeline）。

**W4** [warning] Grid search baseline 的公平性需要讨论

- 具体位置：§4 (Methods), §5.1
- 问题：Grid-$b$ 从 9 个值中 post-hoc 选最优，是一个 oracle baseline。实际使用中 grid search 需要 validation set 选择，且容易 overfit to validation distribution。论文正确标注了 "post-hoc oracle"，但比较的 fairness 需要更显式的讨论：
  - 如果 grid search 用 validation set 选择（而非 post-hoc on test set），其 PPL 会更差
  - 因此 adaptive 相对于"实际可用的 grid search"可能有更大优势
- 这其实对论文有利，但目前的呈现方式没有充分利用这一点。
- 建议：明确讨论 post-hoc vs. validation-based grid search 的区别，可能增加一个 validation-based grid search 结果作为更公平的 baseline。

**W5** [warning] p < 0.01 (N=3) 的可信度和解释

- 具体位置：§5.1, §5.2
- 问题：N=3 的 paired t-test 只有 2 个自由度。p < 0.01 在数学上是可能的（paired differences 的 t 值足够大），但正态性假设在 N=3 下无法验证。论文使用 p-value 时应附带这一 caveat。此外，p < 0.01 at ρ=0.6 的报告方式给人以"高度显著"的印象，但在 N=3 下任何 p-value 都应持保留态度。
- 建议：(1) 报告 exact paired differences 而非仅 p-value；(2) 注明 N=3 下 t-test p-value 应谨慎解读；(3) 考虑非参数检验（如 sign test）作为 robustness check。

**W6** [warning] "Minimum intervention" 缺乏理论最优性证明

- 具体位置：§3.2, §6 (Discussion)
- 问题：选择 b* = b_τ（最小 b）而非 b_ESS（最大 b）或其他中间值，论文称之为 "minimum intervention strategy"，理由是"borderline samples still carry useful training signal"。这是一个合理的设计直觉，但不是定理。论文引用 wang2026survive 提供 α_eff ≥ τ 的动机，但 wang2026survive 假设已知 α，且未证明"最小 b"是最优的。
- Empirically, ESS-only (maximum b) 确实更差，但这只排除了一个极端，不证明 minimum 是最优——例如 b* = (b_τ + b_ESS)/2 可能更好，论文没有测试。
- 建议：(1) 测试 feasible region 中的其他选择策略（如 midpoint, geometric mean）；(2) 或明确标注 minimum intervention 是一个 heuristic，不是 optimal。

---

## 小问题（不影响接收）

- §5.1: "3-seed means: 17.651 vs. 17.620 for grid b=0.3 (gap 0.031, 95% CI [−0.039, 0.101])"——应说明 CI 计算方法（paired t-based? bootstrap?）
- Table 1: D&R full (q>0.5) 标注为 seed 42 only，但 D&R (q>0.3) 标注为 3 seeds；不同 D&R threshold 的 seed 数量不一致，增加了比较的复杂性
- §3.4: "We leave fine-grained ratio characterization (e.g., 0.4 vs. 0.6) to future work"——考虑到 n_min 是核心超参之一，这一留白略显不足
- Appendix Table 5: "Spearman r=0.699" 在正文 §3.3 中被引用为 "sufficient variance within micro-batches"，但 0.699 是否"sufficient"是主观判断
- Abstract 中 "eliminating the need for exhaustive search (nine runs to one; 95% CI of gap [−0.039, 0.101], which includes possible degradation)" 这句话的后半部分削弱了前半部分的 claim，导致 Abstract 内部信息传达矛盾
- §5.2 报告 ρ=0.6 时 Grid b=0.3 仅 seed 42 (17.634)，adaptive 三 seed mean 17.736——gap 扩大到 0.102。如果 grid 也是 3-seed 结果，gap 可能不同，这个比较不公平
- Checklist E1 "AI assistants were used for code development and manuscript drafting" 可以更具体（哪些 AI、用于哪些部分）

---

## 主要优势

1. **问题定义清晰，框架设计优雅**：将 b 的选择形式化为双约束优化，两个约束具有自然的对立单调性，这是一个比 grid search 更优雅的解决方案框架。
2. **Epoch-matched 发现有独立价值**：证明 D&R 的优势来自多 epoch 暴露（而非 filtering 本身）是一个有意义的负面结果，对 community 有参考价值（§5.1, Table 2, Figure in Appendix）。
3. **检测器类型发现是 novel 的**：discriminative vs. generative 检测器的差异（Table 9, §5.2）提供了关于 reweighting 何时有效的实践指导，这个发现比主方法本身可能更有影响。
4. **诚实的 Limitations**：§Limitations 相当全面，覆盖了 scale, ρ range, detector coverage, τ, evaluation, effect size 等方面。许多问题在 Limitations 中已被承认。
5. **写作质量较高**：论文结构清晰，Related Work 做了有效的 positioning（特别是与 Drayson et al. 2025 的三点区别），Algorithm 1 描述明确。

---

## 总结建议

本文提出了一个设计清晰的框架，但实验证据系统性地弱于 claims。核心困境：方法在唯一充分测试的 setting（0.6B, ρ=0.4, 132M tokens）中效应量极小（0.24%），且无法转化为下游增益；在其他 settings（ρ=0.2, 1.7B, cross-model）中要么失败要么不可判断。建议增加实验规模（更多 seeds、更大模型、下游评估）后重投，或重新 framing 为一个聚焦于 epoch-matched 和 detector-type 发现的分析性贡献。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-19T05:58:06.422258+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Step 2 — 交叉分享：请回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — Round 1 审稿意见\n\n**Overall**: 3/5 (Findings)\n\n### Must-Fix 问题\n\n**N1** [critical] 与 Drayson et al. (2025) 的区分度不足以支撑 Main Conference 新颖性\n- 论文使用与 Drayson et al. 完全相同的公式 w=(1-q)^b。全部创新在于 b 的选择方式。\n- (i) per-batch vs fixed b：engineering improvement\n- (ii) loss reweighting vs SIR resampling：实现层面差异\n- (iii) lightweight detector suffices：实验发现而非方法贡献\n- α_eff 约束来自 Wang et al. (2026) 的直接应用；ESS 约束是 IS 标准做法\n- \"Minimum intervention\" 本质是在两个单调函数上做 bisection 取下界\n- 建议重新 frame：将 D&R epoch confound 和 detector type 发现提升为主要贡献\n\n**N2** [critical] 效果量极小，实际意义不明\n- ρ=0.4: Δ=-0.043, 95% CI 包含退化\n- ρ=0.6: Δ=-0.028\n- 1.7B: Δ=-0.01 (negligible)\n- Downstream: 4/5 benchmarks uniform 略优\n- PPL 改进可能仅反映 distribution matching\n\n**N3** [critical] 自污染实验设计严重限制泛化性\n- Qwen3-0.6B 既是 generator 又是 trainee（self-contamination），检测最容易的场景\n- Limitations 未讨论 self-contamination 限制\n- Cross-generator 结果 (Llama-3.2-3B) mixed 且无 PPL 对比\n\n### Should-Fix 问题\n\n**W1** \"D&R\" 缩写在 Abstract/Introduction 中未定义\n**W2** \"robust defaults\" 声明验证不足（τ safe range 基于单 seed, ρ=0.6 optimal shift 到 τ=0.7）\n**W3** Grid search 在 ρ=0.6 为单 seed，Adaptive-vs-Grid gap (0.106) 不可靠\n**W4** 缺少重要近期相关工作（Kang et al. EMNLP 2025, Zhang et al. 2025 ForTIFAI, Yi et al. 2025）\n**W5** Downstream 评估不充分（5 benchmarks, single seed, 4/5 negative）\n**W6** Micro-batch B=4 下 α_eff 仅 5 个离散值，bisection 退化为离散 lookup\n\n### 主要优势\n1. 诚实透明的 Limitations\n2. D&R epoch confound 发现有独立社区价值\n3. Detector type 发现有实用指导意义\n4. 叙事完整性好\n5. 写作干净无 AI 痕迹\n6. 格式完全合规\n\n---\n\n请对以上每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W6) 逐条回应 [AGREE] 或 [REBUT]。",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Step 2 — 交叉分享：请回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — Round 1 审稿意见\n\n**Overall**: 3/5 (Findings)\n\n### Must-Fix 问题\n\n**N1** [critical] 与 Drayson et al. (2025) 的区分度不足以支撑 Main Conference 新颖性\n- 论文使用与 Drayson et al. 完全相同的公式 w=(1-q)^b。全部创新在于 b 的选择方式。\n- (i) per-batch vs fixed b：engineering improvement\n- (ii) loss reweighting vs SIR resampling：实现层面差异\n- (iii) lightweight detector suffices：实验发现而非方法贡献\n- α_eff 约束来自 Wang et al. (2026) 的直接应用；ESS 约束是 IS 标准做法\n- \"Minimum intervention\" 本质是在两个单调函数上做 bisection 取下界\n- 建议重新 frame：将 D&R epoch confound 和 detector type 发现提升为主要贡献\n\n**N2** [critical] 效果量极小，实际意义不明\n- ρ=0.4: Δ=-0.043, 95% CI 包含退化\n- ρ=0.6: Δ=-0.028\n- 1.7B: Δ=-0.01 (negligible)\n- Downstream: 4/5 benchmarks uniform 略优\n- PPL 改进可能仅反映 distribution matching\n\n**N3** [critical] 自污染实验设计严重限制泛化性\n- Qwen3-0.6B 既是 generator 又是 trainee（self-contamination），检测最容易的场景\n- Limitations 未讨论 self-contamination 限制\n- Cross-generator 结果 (Llama-3.2-3B) mixed 且无 PPL 对比\n\n### Should-Fix 问题\n\n**W1** \"D&R\" 缩写在 Abstract/Introduction 中未定义\n**W2** \"robust defaults\" 声明验证不足（τ safe range 基于单 seed, ρ=0.6 optimal shift 到 τ=0.7）\n**W3** Grid search 在 ρ=0.6 为单 seed，Adaptive-vs-Grid gap (0.106) 不可靠\n**W4** 缺少重要近期相关工作（Kang et al. EMNLP 2025, Zhang et al. 2025 ForTIFAI, Yi et al. 2025）\n**W5** Downstream 评估不充分（5 benchmarks, single seed, 4/5 negative）\n**W6** Micro-batch B=4 下 α_eff 仅 5 个离散值，bisection 退化为离散 lookup\n\n### 主要优势\n1. 诚实透明的 Limitations\n2. D&R epoch confound 发现有独立社区价值\n3. Detector type 发现有实用指导意义\n4. 叙事完整性好\n5. 写作干净无 AI 痕迹\n6. 格式完全合规\n\n---\n\n请对以上每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W6) 逐条回应 [AGREE] 或 [REBUT]。",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-19T05:58:30.861533+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24439
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-19T05:58:31.012712+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Step 2 — 交叉分享：请回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — Round 1 审稿意见\n\n**Overall**: 2.5/5 (Borderline Findings)\n\n### Must-Fix 问题\n\n**N1** [critical] 效应量极小，下游任务不支持 PPL 改善的实际意义\n- 核心 PPL 改善 0.043（0.24% relative），在已被续训吸收 5.2 PPL 的残差区间内\n- Table 8 下游 5 个 benchmark 中 4 个为负 Δ（ARC-C -0.005, ARC-E -0.007, HellaSwag -0.005, WinoGrande -0.008），sign-test p≈0.19\n- PPL 改善可能反映 distribution matching 而非 generalizable quality gain\n- Abstract/Introduction framing 给出比实际证据更强的印象\n- 建议：Results 正文报告下游结果，多 seed downstream 评估\n\n**N2** [critical] 1.7B \"transfers without degradation\" claim 缺乏统计支撑\n- 2 seeds adaptive（13.25, 13.27），1 seed uniform（13.26）\n- Δ=-0.01 无法区分 noise 和 signal\n- 建议：至少 3 seeds both sides，或降级为 preliminary evidence\n\n**N3** [critical] \"competitive with grid-best\" framing 与 CI 不一致\n- 95% CI [-0.039, 0.101] 包含 0.101 PPL 的降级\n- Abstract 将 gap vs cross-seed variance 比较混淆了两个不同统计量\n- CI 包含 0 不构成等价性证据——N=3 下 CI 过宽是 power 不足\n- 建议：Abstract 明确 CI 包含降级，增加 seeds，或明确标注 CI 过宽\n\n**N4** [critical] Batch size B=4 下 α_eff 仅 5 个离散值，bisection 意义存疑\n- α_eff ∈ {0, 0.25, 0.5, 0.75, 1.0}，阶梯函数上做 bisection\n- Pearson r≈0.70 意味着 51% 方差未解释；MAE=0.114\n- \"连续优化\"框架在 B=4 下退化为粗粒度离散选择\n- 建议：承认 B=4 离散化问题，提供 B=8/16 多 seed 结果\n\n### Should-Fix 问题\n\n**W1** 自污染设计（self-contamination）的生态效度有限\n- 真实 web 污染来自多种不同模型，Cross-model 结果（Llama-3.2-3B）single seed 且 mixed\n- 建议：测试\"强生成器+弱训练模型\"场景\n\n**W2** 132M tokens 规模太小，Introduction 动机与实际实验 scope 不匹配\n- 1.7B 上已无 measurable advantage\n- Conclusion 诚实但 Introduction/Abstract 未限定 scope\n- 建议：Introduction 明确目标场景为 continued pretraining\n\n**W3** Epoch-matched 对比存在潜在混淆变量\n- D&R 运行 2,533 步 vs adaptive 6,103 步，cosine LR schedule 总长度不同\n- warmup 比例和 decay 曲线差异未讨论\n- 建议：讨论 LR schedule 差异影响，或提供相同步数不同 data pipeline 的控制实验\n\n**W4** Grid search baseline 的公平性需要讨论\n- Post-hoc oracle 选择对论文有利（实际使用中 grid search 用 validation set 会更差）\n- 建议：明确讨论 post-hoc vs validation-based 区别\n\n**W5** p<0.01 (N=3) 的可信度\n- 2 个自由度，正态性假设无法验证\n- 建议：报告 exact paired differences，注明 N=3 下 t-test 应谨慎解读\n\n**W6** \"Minimum intervention\" 缺乏理论最优性证明\n- 选择 b* = b_τ 而非中间值是设计直觉而非定理\n- b* = (b_τ + b_ESS)/2 可能更好，未测试\n- 建议：测试 feasible region 中其他策略，或标注为 heuristic\n\n### 主要优势\n1. 问题定义清晰，框架设计优雅\n2. Epoch-matched 发现有独立价值\n3. 检测器类型发现是 novel 的\n4. 诚实的 Limitations\n5. 写作质量较高\n\n---\n\n请对以上每个 Must-Fix (N1-N4) 和 Should-Fix (W1-W6) 逐条回应 [AGREE] 或 [REBUT]。",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Step 2 — 交叉分享：请回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — Round 1 审稿意见\n\n**Overall**: 2.5/5 (Borderline Findings)\n\n### Must-Fix 问题\n\n**N1** [critical] 效应量极小，下游任务不支持 PPL 改善的实际意义\n- 核心 PPL 改善 0.043（0.24% relative），在已被续训吸收 5.2 PPL 的残差区间内\n- Table 8 下游 5 个 benchmark 中 4 个为负 Δ（ARC-C -0.005, ARC-E -0.007, HellaSwag -0.005, WinoGrande -0.008），sign-test p≈0.19\n- PPL 改善可能反映 distribution matching 而非 generalizable quality gain\n- Abstract/Introduction framing 给出比实际证据更强的印象\n- 建议：Results 正文报告下游结果，多 seed downstream 评估\n\n**N2** [critical] 1.7B \"transfers without degradation\" claim 缺乏统计支撑\n- 2 seeds adaptive（13.25, 13.27），1 seed uniform（13.26）\n- Δ=-0.01 无法区分 noise 和 signal\n- 建议：至少 3 seeds both sides，或降级为 preliminary evidence\n\n**N3** [critical] \"competitive with grid-best\" framing 与 CI 不一致\n- 95% CI [-0.039, 0.101] 包含 0.101 PPL 的降级\n- Abstract 将 gap vs cross-seed variance 比较混淆了两个不同统计量\n- CI 包含 0 不构成等价性证据——N=3 下 CI 过宽是 power 不足\n- 建议：Abstract 明确 CI 包含降级，增加 seeds，或明确标注 CI 过宽\n\n**N4** [critical] Batch size B=4 下 α_eff 仅 5 个离散值，bisection 意义存疑\n- α_eff ∈ {0, 0.25, 0.5, 0.75, 1.0}，阶梯函数上做 bisection\n- Pearson r≈0.70 意味着 51% 方差未解释；MAE=0.114\n- \"连续优化\"框架在 B=4 下退化为粗粒度离散选择\n- 建议：承认 B=4 离散化问题，提供 B=8/16 多 seed 结果\n\n### Should-Fix 问题\n\n**W1** 自污染设计（self-contamination）的生态效度有限\n- 真实 web 污染来自多种不同模型，Cross-model 结果（Llama-3.2-3B）single seed 且 mixed\n- 建议：测试\"强生成器+弱训练模型\"场景\n\n**W2** 132M tokens 规模太小，Introduction 动机与实际实验 scope 不匹配\n- 1.7B 上已无 measurable advantage\n- Conclusion 诚实但 Introduction/Abstract 未限定 scope\n- 建议：Introduction 明确目标场景为 continued pretraining\n\n**W3** Epoch-matched 对比存在潜在混淆变量\n- D&R 运行 2,533 步 vs adaptive 6,103 步，cosine LR schedule 总长度不同\n- warmup 比例和 decay 曲线差异未讨论\n- 建议：讨论 LR schedule 差异影响，或提供相同步数不同 data pipeline 的控制实验\n\n**W4** Grid search baseline 的公平性需要讨论\n- Post-hoc oracle 选择对论文有利（实际使用中 grid search 用 validation set 会更差）\n- 建议：明确讨论 post-hoc vs validation-based 区别\n\n**W5** p<0.01 (N=3) 的可信度\n- 2 个自由度，正态性假设无法验证\n- 建议：报告 exact paired differences，注明 N=3 下 t-test 应谨慎解读\n\n**W6** \"Minimum intervention\" 缺乏理论最优性证明\n- 选择 b* = b_τ 而非中间值是设计直觉而非定理\n- b* = (b_τ + b_ESS)/2 可能更好，未测试\n- 建议：测试 feasible region 中其他策略，或标注为 heuristic\n\n### 主要优势\n1. 问题定义清晰，框架设计优雅\n2. Epoch-matched 发现有独立价值\n3. 检测器类型发现是 novel 的\n4. 诚实的 Limitations\n5. 写作质量较高\n\n---\n\n请对以上每个 Must-Fix (N1-N4) 和 Should-Fix (W1-W6) 逐条回应 [AGREE] 或 [REBUT]。",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-19T05:58:32.482779+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1470
}
```

</details>

---


### Assistant

_source line 270 · 2026-05-19T05:58:36.839113+00:00_

Step 2 交叉分享已发出。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 23

## Round 23

2 recorded events


### User

_source line 271 · 2026-05-19T05:58:39.428647+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

审稿核心判断：**Borderline Findings (2.5/5)**。

主要问题集中在四个 critical issues：
1. 效应量仅 0.043 PPL (0.24%)，下游 5 个 benchmark 中 4 个为负，PPL 改善可能是 distribution matching artifact
2. 1.7B "transfers without degradation" 仅 2 seeds，无法支撑 claim
3. "competitive with grid-best" 的 CI [-0.039, 0.101] 包含实质性降级，统计逻辑不成立
4. B=4 下 α_eff 仅 5 个离散值，核心机制的连续优化退化为粗粒度离散选择

主要优势在于框架设计优雅、epoch-matched 发现和 detector type 发现具有独立价值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 272 · 2026-05-19T05:58:44.943935+00:00_

Reviewer 1 的 Round 1 初审和交叉回应均已收到。等待 Reviewer 2 的交叉回应后进行收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 24

## Round 24

4 recorded events


### User

_source line 273 · 2026-05-19T05:59:58.546916+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见

---

### Must-Fix 逐条回应

**[AGREE] R1-N1: 效应量极小，下游任务不支持 PPL 改善的实际意义**

完全同意，这也是我的 N2 的核心关切。补充两点：
1. 论文 Limitations（Section 7, "Effect size" 段）确实承认了 "modest in absolute terms"，但 Abstract 和 Introduction 的 framing 并未体现这一审慎态度。Abstract line 7 写 "eliminating the need for exhaustive search" 给人一种方法带来了显著收益的印象，但实际收益在 noise 范围内。
2. 4/5 downstream 为负这一 pattern 比单个 benchmark 的负值更值得关注——如果 PPL 改进仅仅是让模型更好地拟合 human-only 评估集的分布特征而非提升真实语言建模能力，那么方法的核心 value proposition 就存疑。R1 建议将 downstream 结果纳入正文而非仅放 Appendix，我认为这是合理的——当前结构让读者在读完 Results 正文后会高估方法的实用价值。

**[AGREE] R1-N2: 1.7B "transfers without degradation" claim 缺乏统计支撑**

同意。2 seeds adaptive vs 1 seed uniform，Δ=-0.01，这个比较在统计上没有意义。Section 5.2 写 "confirming that the method transfers to larger scale without degradation" 这个 "confirming" 用词过强。不过论文 Conclusion 的表述相对克制（"the method's primary value lies in the 0.6B continued pretraining regime tested here"），说明作者自己也意识到了这一局限。R1 建议至少 3 seeds both sides 合理，或者将 "confirms" 改为 "preliminary evidence suggests"。

**[AGREE] R1-N3: "competitive with grid-best" framing 与 CI 不一致**

同意。95% CI [-0.039, 0.101] 确实包含 0.101 PPL 的降级，这意味着 adaptive 有可能比 grid-best 差 0.101 PPL。Abstract line 7 将 gap (0.031) 与 cross-seed variance (±0.033) 做比较来暗示等价性，但这在统计上不严谨——gap 和 variance 是不同量。N=3 下 CI 过宽本质上是 power 不足问题，不能用 "CI 包含 0" 来声称等价。论文 Section 5.1 的表述 "we refrain from claiming statistical indistinguishability" 是正确的审慎态度，但 Abstract 的 framing 与此矛盾。

补充一点：Introduction contribution #1 写 "computed per-batch from detector scores with minimum-intervention semantics"，这个表述本身没问题，但紧接着 Section 5.1 的数据无法完全支撑 "eliminates the need for exhaustive search" 的强 claim——如果 adaptive 有 10% 概率比 grid-best 差 0.1 PPL，那么 grid search 并非被 "eliminated"，而是被一个可能略差的替代方案所取代。

**[REBUT] R1-N4: Batch size B=4 下 α_eff 仅 5 个离散值，bisection 意义存疑**

部分反驳。R1 的技术观察完全正确（α_eff 在 B=4 下确实只有 5 个离散值），我在自己的 W6 中也提出了这一问题。但我不同意将其列为 **Must-Fix / Critical**，理由如下：

1. **离散化不改变方法的功能正确性**。bisection 在阶梯函数上仍然能正确找到使 α_eff(b) ≥ τ 的最小 b——结果是精确的，只是搜索过程有冗余。这是 efficiency 问题而非 correctness 问题。
2. **论文提供了 B=8, 16 的验证**（Appendix H, Table 6; Section 3.3 最后一句）：三个 batch size 下 PPL 差异 <0.01，说明离散化的粗粒度并未实质影响结果。
3. **Pearson r≈0.70 的解读**：R1 说 "51% 方差未解释"，但 α_eff 是一个 proxy metric 用于指导 b 选择，不需要完美重建 true real fraction。关键是 rank-order 信息（Spearman r=0.699, Table 6）足以让 bisection 选择合理的 b 值。

建议降级为 Should-Fix：承认 B=4 下理论叙事与实际实现的 gap，但不作为影响接收的 critical issue。

---

### Should-Fix 逐条回应

**[AGREE] R1-W1: 自污染设计的生态效度有限**

同意，与我的 N3 一致。self-contamination 是最容易检测的场景。Appendix I 的 cross-model 结果（Llama-3.2-3B）是 single seed 且无 PPL 对比（"checkpoints were not retained for re-evaluation"），不足以支撑泛化性。

**[AGREE] R1-W2: 132M tokens 规模太小，Introduction 动机与实验 scope 不匹配**

同意。Introduction 第一段以 "Web corpora increasingly contain machine-generated text" 开头，暗示方法面向 web-scale pretraining，但实验仅在 132M tokens 上进行。Conclusion 的 "the method's primary value lies in the 0.6B continued pretraining regime tested here" 是诚实的，但 Introduction 应更早限定 scope。不过要注意，132M tokens 对 continued pretraining（非 from-scratch pretraining）来说并非不合理——Section 4 引用了 Gururangan et al. (2020) 的 domain-adaptive continued pretraining 作为参照。建议 Introduction 明确写 "continued pretraining on moderate-scale corpora"。

**[REBUT] R1-W3: Epoch-matched 对比存在潜在混淆变量（LR schedule 差异）**

部分反驳。R1 指出 D&R 2,533 步 vs adaptive 6,103 步的 cosine LR schedule 总长度不同，这个观察是正确的——schedule 总长度会影响 warmup 比例和 decay 曲线。但：

1. **这个 confound 的方向对论文结论有利而非不利**。如果 D&R epoch-matched 因为 schedule 更短（更少 warmup、更快 decay）而表现更差，那么在 "公平" schedule 下 D&R 可能表现更好，这会**强化**论文的 "epoch confound" 结论——即 D&R 的优势不仅来自 multi-epoch，还可能部分来自 schedule 优势。
2. 更根本地，epoch-matched 实验的核心发现是 D&R full-length 的 0.360 PPL 优势几乎完全消失（Δ=0.006），这个效应大到不太可能被 schedule 差异完全解释。
3. 不过 R1 的建议仍有价值：讨论 schedule 差异的潜在影响并不困难，一两句话即可，且能增强实验的可信度。

**[AGREE] R1-W4: Grid search baseline 的公平性需要讨论**

同意。Grid search 是 post-hoc oracle（从 9 个 b 值中选最优），这对论文有利——在实际使用中，grid search 需要 validation set，选出的 b 可能不是真正最优。论文 Table 1 caption 标注了 "$^\ddagger$ Post-hoc oracle"，但正文讨论不够。明确讨论这一点会让比较更公平：adaptive 无需 validation set，而 grid search 在实际使用中表现可能更差。

**[AGREE] R1-W5: p<0.01 (N=3) 的可信度**

同意。N=3 的 paired t-test 只有 2 个自由度，t 分布的尾部非常厚，p<0.01 需要极端一致的 paired differences。论文的 p-values 在技术上可能是正确的（如果 3 个 seeds 的 paired differences 完全同号且量级一致），但 reviewer 和读者有权质疑 N=3 下 parametric test 的可靠性。建议报告 exact paired differences 并注明 sample size 限制。

**[REBUT] R1-W6: "Minimum intervention" 缺乏理论最优性证明**

部分反驳。R1 建议测试 b* = (b_τ + b_ESS)/2 等其他策略。这个建议合理但不构成 weakness：

1. **论文已提供 empirical justification**。Section 5.1 和 Section 5.5 的 ESS-only ablation（即 b* = b_ESS，最大化 intervention）显示明显退化（PPL 17.737 vs adaptive 17.651）。这证明了 minimum intervention 优于 maximum intervention。
2. **中间策略的缺失是 completeness 问题而非 soundness 问题**。论文测试了两个极端（minimum: b_τ; maximum: b_ESS）和一个 ablation（ESS-only = maximum），分别对应 mean b* = 1.19 和 5.88。中间值可能有意义，但当前已有的 ablation 足以支撑 "minimum intervention is better than maximum intervention" 的 claim。
3. **"Minimum intervention" 的动机来自 Section 3.2 的最后一段**（"Borderline samples carry useful training signal; over-downweighting discards this signal unnecessarily"），这是一个合理的 inductive bias 而非需要证明的定理。

不过论文确实应将其标注为 design choice / heuristic 而非暗示最优性。

---

### 综合判断

与 R1 的审稿在多数 critical issues 上高度一致：效果量小（R1-N1 = 我的 N2）、统计支撑不足（R1-N2, N3）、自污染设计限制泛化性（R1-W1 = 我的 N3）。我对 R1-N4（B=4 离散化）的严重程度有分歧——认为应降为 Should-Fix。

两份审稿共同指向一个核心判断：**这篇论文的 analytical findings（D&R epoch confound, detector type effect）比方法本身更有价值**，但当前 framing 将方法置于核心位置。如果作者能重新定位论文的主要贡献（analytical study with a practical method as byproduct），并补充 downstream 和 multi-seed 证据，Findings 级别是合理的接收决定。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-19T06:00:15.512877+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-19T06:00:15.815108+00:00_

1	- id: "RR-W1"
2	  summary: "Paper claims 'from random initialization' but code uses from_pretrained() — actually continued pretraining"
3	  category: writing
4	  severity: warning
5	  status: resolved
6	  first_raised_round: 1
7	  last_seen_round: 2
8	  mentions:
9	    - round: 1
10	      reviewers: [research_reviewer]
11	      note: "Two independent reviews confirmed: pretrain_weighted.py L318 uses from_pretrained(), model.safetensors 1.5GB = full pretrained weights"
12	    - round: 2
13	      reviewers: [R1, R2]
14	      note: "Both reviewers confirm fixed: Abstract line 7, Introduction line 23, Experiments line 12 now say 'continued pretraining'"
15	    - round: 3
16	      reviewers: [R1, R2]
17	      note: "本轮未提及，已确认修复"
18	  action_items:
19	    - round: 1
20	      action: "Fix paper text: 'pretrain from random initialization' → 'continue pretraining Qwen3-0.6B'"
21	      assigned_to: paper_agent
22	      status: done
23	    - round: 1
24	      action: "Run baseline PPL eval on untrained Qwen3-0.6B checkpoint to quantify absolute improvement"
25	      assigned_to: main_agent
26	      status: done
27	  resolution: "Fixed in current version: Abstract, Introduction, Experiments all use 'continued pretraining'"
28	  resolution_round: 2
29	
30	- id: "RR-W2"
31	  summary: "Paper claims 'balanced real/synthetic test set' but eval_holdout.jsonl is human-only (FineWeb)"
32	  category: writing
33	  severity: warning
34	  status: resolved
35	  first_raised_round: 1
36	  last_seen_round: 2
37	  mentions:
38	    - round: 1
39	      reviewers: [research_reviewer]
40	      note: "eval_holdout.jsonl: 67823 lines, all source=fineweb depth=0, zero synthetic samples"
41	    - round: 2
42	      reviewers: [R1, R2]
43	      note: "Both reviewers confirm fixed: Experiments line 16 now says 'containing only human-authored text'"
44	    - round: 3
45	      reviewers: [R1, R2]
46	      note: "本轮未提及，已确认修复"
47	  action_items:
48	    - round: 1
49	      action: "Fix paper text: 'balanced
…[truncated 27282 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Assistant

_source line 276 · 2026-05-19T06:01:42.575252+00:00_

Reviewer 2 的交叉回应已收到。R2 对 R1 的 4 个 Must-Fix 中 3 个标注 [AGREE]（N1 效应量、N2 1.7B 统计不足、N3 CI framing），1 个标注 [REBUT]（N4 B=4 离散化，建议降为 Should-Fix）。Should-Fix 中 4 个 [AGREE]（W1 自污染、W2 规模、W4 grid 公平性、W5 p-value），2 个 [REBUT]（W3 epoch-matched LR confound 方向有利、W6 minimum intervention 已有 ablation 支撑）。

等待 Reviewer 1 的交叉回应后进入收敛判断和报告汇总。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 25

## Round 25

6 recorded events


### User

_source line 277 · 2026-05-19T06:01:43.787288+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。对 R1 的 10 个问题：6 个 [AGREE]，4 个 [REBUT]（部分反驳）。

核心共识点：效果量小、统计支撑不足、自污染设计限制泛化性。分歧点：B=4 离散化的严重程度（我认为应降为 Should-Fix）、epoch-matched LR schedule confound（方向对论文结论有利）、minimum intervention 的理论最优性要求（empirical ablation 已足够）。

---

[Reviewer 1 审稿意见]:

## Reviewer 1 交叉回应 — 对 Reviewer 2 审稿意见

---

### Must-Fix 问题

**[AGREE] R2-N1: 与 Drayson et al. (2025) 的区分度不足**

同意核心判断。论文采用完全相同的权重公式 w=(1-q)^b（§3.1, Eq.1），方法创新集中在 b 的选择方式上：(i) per-batch bisection 是工程层面的改进而非概念突破；(ii) α_eff ≥ τ 约束是 wang2026survive 收敛率结论的直接操作化（§3.2 line 66 明确承认 "convergence under contaminated training improves with the effective real-data fraction"）；(iii) ESS 约束是 importance sampling 领域的标准做法（§3.2 引用 kish1965survey, owen2013mc）。

但我要补充：R2 的 reframing 建议（将 D&R epoch confound 和 detector type 发现提升为主要贡献）是建设性的，也与我的审稿意见一致。这两个发现的独立价值高于方法本身：

- Epoch confound 发现（Table 2, §5.1）：D&R 全长 17.290 vs. epoch-matched 17.657，Δ=0.367 完全来自多 epoch——这对 community 有纠偏价值
- Detector type 发现（Table 9, Appendix G）：GPT-2 PPL (AUC=0.91) 反而使 adaptive 退化 (+0.10)，证明 AUC 不是决定因素——这是一个 non-trivial 的实践指导

如果论文重新定位为 "analysis-driven contribution with a methodological tool"，novelty 问题可能缓解。但当前 framing 将 dual-constraint framework 作为 Contribution 1（§1, contribution list），抬高了 novelty 预期。

---

**[AGREE] R2-N2: 效果量极小，实际意义不明**

完全同意。这与我的 N1 判断一致。补充几个 R2 未展开的点：

1. **PPL-downstream 脱节的严重性**：不仅是 4/5 benchmark 为负 Δ，而且方向一致（ARC-C -0.005, ARC-E -0.007, HellaSwag -0.005, WinoGrande -0.008），仅 PIQA +0.001 例外（Table 8, Appendix D）。sign-test p ≈ 0.19 虽不显著，但一致的负方向 suggestive，论文将此归为 "within standard error" 有回避之嫌。

2. **效应量的 context**：0.043 PPL 改善发生在 22.970 → 17.694 的 5.276 PPL 下降之后（Table 1），占总改善的 0.8%。方法在"残差"区间操作，实际效果被大幅稀释。

3. **Conclusion 的自我矛盾**：§Conclusion 称 "the method's primary value lies in the 0.6B continued pretraining regime tested here"——如果连作者都承认 value 仅限于一个特定 regime，这对 general contribution claim 是致命的。

---

**[AGREE] R2-N3: 自污染实验设计限制泛化性**

同意，且 R2 指出的 "Limitations 未讨论 self-contamination" 这一点是准确的。我核查了 §Limitations 的六个段落（Scale, Contamination range, Detector coverage, Threshold, Evaluation, Effect size），没有一个段落将 self-contamination 作为独立限制讨论。§Limitations 的 "Scale and cross-model transfer" 段落提到了 Llama-3.2-3B cross-model 结果，但这是关于 cross-model transfer 的，不是关于 self-contamination 设计本身的局限性。

补充我的分析：

- 论文 §4 声称 self-contamination "creates a challenging detection scenario where generator and trainee share the same distribution"，但这实际上是一个 **可控的** 场景——TF-IDF+LR 在此 setting 下达到 AUC=0.94（§4 detector paragraph），说明 self-contamination 并非特别困难
- 真实 web 污染的关键挑战——**多源异构**（不同模型、不同 prompt 策略、不同时间段生成）、**非均匀混合**（特定 domain/topic 污染更重）——在 uniform random mixing 设计中完全缺失
- Cross-generator 结果（Appendix H, Table 10）不仅 single seed 且 mixed results，还缺少 PPL 对比（"Perplexity comparison omitted due to inconsistent evaluation configurations; checkpoints were not retained for re-evaluation"），这是一个严重的实验管理疏忽

---

### Should-Fix 问题

**[AGREE] R2-W1: "D&R" 缩写未定义**

确认。Abstract line 9 使用 "D&R's full-length advantage" 时无前置定义。Introduction contribution list（§1 line 30）同样直接使用 "D&R's reported advantage"。§4 的 Methods 部分（experiments.tex line 30）定义了 "Detect & Remove"，但这在 Abstract/Introduction 之后。对于 double-blind review，审稿人可能不熟悉这个缩写。

---

**[AGREE] R2-W2: "robust defaults" 验证不足**

同意。τ sweep（Table 3, Appendix B）仅基于 seed 42, ρ=0.4。当 ρ 变化时，optimal τ 从 0.8 移动到 0.7（Figure 3, §5.2 line 90: "A τ sweep at this level finds τ=0.7 optimal"）。论文声称 "τ ∈ [0.7, 0.8] performs well across tested ρ"，但这仅基于两个 ρ 值（0.4, 0.6）且 τ=0.7 的数据仅来自 ρ=0.6 的实验。

"empirically robust defaults that transfer without per-model tuning"（§5.4 最后一句）这个 claim 对于仅在一个模型（Qwen3-0.6B）的两个 ρ 值上验证的超参来说过强。

---

**[AGREE] R2-W3: Grid search 在 ρ=0.6 为单 seed**

同意。Table 6（Appendix E）的 Grid (b=0.3) 在 ρ=0.6 标注为 "seed 42 only"。Adaptive 3-seed mean 17.736 vs. Grid 单 seed 17.634，gap 0.102 不具可比性。如果 Grid 在 ρ=0.6 也有 3-seed variance（如 ρ=0.4 的 ±0.033），真实 gap 可能显著缩窄或扩大。这使得 §5.2 中关于 "Adaptive-vs-Grid gap widens from 0.013 at ρ=0.4 to 0.106 at ρ=0.6" 的叙述不可靠。

---

**[AGREE with caveat] R2-W4: 缺少重要近期相关工作**

原则上同意相关工作应完整覆盖。但我无法独立验证 R2 提到的三篇论文（Kang et al. EMNLP 2025, Zhang et al. 2025 ForTIFAI, Yi et al. 2025）的存在和相关性。如果这些论文确实存在且直接相关，应被引用。

从论文当前引用来看（45 篇，覆盖 contamination、detection、data mixing、instance selection、theory 五个方向），引用密度合理。但如果 R2 提到的工作涉及 contamination-aware training 的替代方法，缺失会影响 positioning 的完整性。建议 R2 提供具体论文信息以便作者核实。

---

**[AGREE] R2-W5: Downstream 评估不充分**

同意，与我的 N1 判断一致。5 benchmarks、single seed、4/5 negative Δ。论文将下游结果放在 Appendix 而非正文，且 framing 为 "preserves downstream performance"（Table 8 caption: "adaptive reweighting preserves downstream performance"）而非"downstream results are inconclusive or mildly negative"，这是对证据的 over-positive interpretation。

---

**[AGREE] R2-W6: B=4 下 α_eff 仅 5 个离散值**

同意，与我的 N4 判断一致。补充：论文 §3.3 line 119-120 写道 "we compute b* at the micro-batch level (B=4) rather than the effective batch (B=16 after gradient accumulation) because q-score statistics exhibit sufficient variance within micro-batches: Spearman r=0.699"。但 Spearman r=0.699 是 α_eff(0) 与 true real fraction 的 rank correlation，不是 α_eff(b*) 与最优 b 之间的相关性。这两个量之间存在概念跳跃，论文未能 bridge。

此外，当 α_eff(0) = 0.5 且 τ = 0.8 时，bisection 需要找 b 使得 α_eff 从 0.5 跳到 ≥ 0.8。但在 B=4 的阶梯函数上，这个 "跳跃" 发生在某个特定 b 值处，bisection 的精度（ε=0.01）远超函数本身的分辨率。这不影响正确性，但暴露了方法描述与实际操作之间的失配。

---

### 总体评价

R2 的审稿意见整体准确，与我的独立评估高度一致。主要分歧在于定位：

- R2 给了 3.0/5 (Findings)，我给了 2.5/5 (Borderline Findings)。差异主要来自我对效应量的权重更大——我认为 0.043 PPL 无下游转化是一个比 novelty 问题更根本的缺陷。即使 reframing 后 novelty 足够 Findings，效应量问题仍然存在。
- 两位 reviewer 在以下问题上完全一致：(1) 效应量过小；(2) 1.7B 证据不足；(3) 自污染设计限制泛化；(4) B=4 离散化问题；(5) 下游评估不充分。这种独立一致性增强了这些问题的权重。


---

[Reviewer 1 审稿结果]:
交叉回应已提交。对 R2 的 9 个问题全部标注 [AGREE]（W4 附带 caveat），核心一致点：效应量过小、1.7B 证据不足、自污染限制、B=4 离散化、下游评估不充分。主要分歧在 Overall 评分（我 2.5 vs R2 3.0），因为我对效应量无下游转化的权重更大。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-19T06:05:17.456120+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "provenance_weight_training",
  "issues_yaml": "- id: \"RR-W1\"\n  summary: \"Paper claims 'from random initialization' but code uses from_pretrained() — actually continued pretraining\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [research_reviewer]\n      note: \"Two independent reviews confirmed: pretrain_weighted.py L318 uses from_pretrained()\"\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Both reviewers confirm fixed\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"本轮未提及，已确认修复\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及，已确认修复\"\n  action_items:\n    - round: 1\n      action: \"Fix paper text\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed in current version\"\n  resolution_round: 2\n\n- id: \"RR-W2\"\n  summary: \"Paper claims 'balanced real/synthetic test set' but eval_holdout.jsonl is human-only\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [research_reviewer]\n      note: \"eval_holdout.jsonl: 67823 lines, all source=fineweb\"\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Confirmed fixed\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及，已确认修复\"\n  action_items:\n    - round: 1\n      action: \"Fix paper text\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed\"\n  resolution_round: 2\n\n- id: \"R3-N1\"\n  summary: \"Statistical support insufficient: N=3 CI [-0.039, 0.101] includes degradation; 'competitive' is overstatement; downstream 4/5 tasks worse\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"R1-N1: 'statistically indistinguishable' changed to 'competitive'.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Full consensus. 'competitive' still overstatement.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Full consensus again. R1 emphasizes CI upper bound 0.101 is 2.3x the effect; Abstract/Conclusion framing inconsistent with §5.1 caveats. R2 adds downstream 4/5 negative pattern more concerning than individual negatives. Both agree PPL may be distribution matching artifact.\"\n  action_items:\n    - round: 3\n      action: \"Weaken framing; add CI caveat; add downstream caveat\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 4\n      action: \"Abstract must explicitly note CI includes degradation; move downstream results to main text (not just Appendix); discuss PPL-downstream divergence in Results or Discussion\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N2\"\n  summary: \"Theory-empirical disconnect: τ=0.8 is empirical but framed as 'principled default'; Wang 2026 requires known α; τ optimal shifts with ρ\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"α_eff motivation disconnected.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Full consensus.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"R1 confirms τ sweep based on single seed/single ρ. R2 agrees 'robust defaults' overclaimed. Both: τ validated on only 2 ρ values (0.4, 0.6) and 1 model.\"\n  action_items:\n    - round: 3\n      action: \"'principled defaults' → 'empirically robust defaults'\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 4\n      action: \"Further weaken to 'default values that perform well in the tested configurations'; explicitly state τ sweep is single-seed\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"1.7B 'transfers without degradation' claim unsupported: 2 seeds adaptive vs 1 seed uniform, Δ=-0.01\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"1.7B added but single seed.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Δ=-0.01 equally supports 'no effect at this scale'.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Full consensus. R1: 2 data points cannot compute meaningful CI or p-value; 'confirming' in §5.2 is too strong. R2 agrees, notes Conclusion is more restrained but §5.2 is not.\"\n  action_items:\n    - round: 3\n      action: \"Reposition as 'does not degrade' with explicit no-amplification acknowledgment\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 4\n      action: \"§5.2 change 'confirming' → 'preliminary evidence suggests'; do not cite as contribution in Abstract/Conclusion; add 3+ seeds or remove scale claim\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N4\"\n  summary: \"Novelty insufficient for EMNLP Main: core formula from Drayson 2025, dual constraint is standard IS, minimum intervention is standard constrained optimization\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Both agree Findings-level.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Consensus Findings-level.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Full consensus. R2: three claimed differentiators are (i) engineering, (ii) implementation, (iii) experimental finding. R1 agrees and adds: analytical findings (epoch confound, detector type) have higher independent value than the method. Both recommend reframing as analysis-driven contribution.\"\n  action_items:\n    - round: 3\n      action: \"Strengthen contributions: epoch-matched as corrective, detector type as practical\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 4\n      action: \"Consider reframing paper: analytical study (epoch confound + detector type findings) as primary contributions, method as practical byproduct. This better matches actual evidence and may improve reception at Findings track.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N5\"\n  summary: \"Scale mismatch: paper frames web-scale but experiments only 0.6B/132M tokens\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Full consensus.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"R1: Introduction opens with web-scale but experiments 4 orders of magnitude smaller. R2: 132M tokens reasonable for continued pretraining (cites Gururangan 2020) but Introduction should limit scope explicitly.\"\n  action_items:\n    - round: 3\n      action: \"Narrow Introduction to continued pretraining scenario\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 4\n      action: \"Introduction must explicitly state 'continued pretraining on moderate-scale corpora' early; Abstract should limit scope\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W1\"\n  summary: \"Self-contamination (generator=trainee) external validity: real web contamination is multi-source, multi-model\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Part of external validity.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Self-contamination not representative.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Escalated by both reviewers. R1: self-contamination is NOT the 'challenging scenario' claimed — AUC=0.94 shows it's easy. R2: Limitations has no dedicated paragraph on self-contamination design. Cross-model (Appendix H) single seed, mixed results, no PPL ('checkpoints not retained' is experimental management failure).\"\n  action_items:\n    - round: 3\n      action: \"Strengthen Limitations discussion\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 4\n      action: \"Add dedicated self-contamination limitation paragraph; remove 'challenging detection scenario' claim from §4; if possible run one cross-generator experiment with retained checkpoints\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2\"\n  summary: \"Abstract ~280-291 words, exceeds 250 convention; data-heavy rather than narrative-driven\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"R2: reads like Results summary.\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未单独提及，但R1-N3指出Abstract framing与证据不一致，属相关问题\"\n  action_items:\n    - round: 3\n      action: \"Trim to ≤250 words\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W3\"\n  summary: \"Citation coverage still insufficient: ~41 refs; missing recent contamination-aware training works\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [director_audit]\n      note: \"Increased to 30 refs.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Now ~39 still below norm.\"\n    - round: 4\n      reviewers: [R2]\n      note: \"Now ~41 refs. R2 identifies 3 specific missing works: Kang et al. (EMNLP 2025) 'Demystifying Synthetic Data in LLM Pre-training'; Zhang et al. (2025) 'ForTIFAI' (arXiv:2509.08972); Yi et al. (2025) 'Escaping Model Collapse via Synthetic Data Verification' (arXiv:2510.16657). R1 agrees in principle but cannot independently verify existence.\"\n  action_items:\n    - round: 3\n      action: \"Add 10-15 references\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 4\n      action: \"Verify and add R2's 3 suggested references if confirmed real; aim for 50+ total\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W4\"\n  summary: \"Discussion section too thin: rehashes Results without deeper analysis\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Missing failure conditions, PSIS, deployment guidance.\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未单独提及，Discussion 内容已有扩展但仍偏薄\"\n  action_items:\n    - round: 3\n      action: \"Expand to ~40-50 lines\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W5\"\n  summary: \"'Minimum Intervention Principle' framing overstates a standard constrained optimization choice\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Standard optimization not a 'principle'.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"R1-W6: minimum intervention not proven optimal, (b_τ+b_ESS)/2 not tested. R2 partially rebuts: ESS-only ablation shows maximum is worse, so minimum > maximum established; but agrees should label as heuristic/design choice. Consensus: label as 'empirically motivated strategy', not 'principle' or implied optimality.\"\n  action_items:\n    - round: 3\n      action: \"'minimum intervention principle' → 'empirically motivated minimum intervention strategy'\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 4\n      action: \"Consider testing midpoint strategy as ablation; if not feasible, explicitly state minimum intervention is a design choice, not proven optimal\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W6\"\n  summary: \"ρ=0.2 failure (+0.046 PPL) undiscussed in main text; failure mechanism unexplained\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Consensus.\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未单独提及。论文已在 Discussion 中加入 ρ=0.2 failure 分析段落（mean_q=0.393, 60% α_eff-binding）。Appendix K 也新增了低污染分析。\"\n  action_items:\n    - round: 3\n      action: \"Add ρ=0.2 analysis\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W7\"\n  summary: \"Micro-batch B=4: α_eff has only 5 discrete values, 'continuous adaptive selection' framing inconsistent\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"B=4 means α_eff ∈ {0, 0.25, 0.5, 0.75, 1.0}.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"R1 raises to critical (N4): bisection on staircase function; Pearson r=0.70 means 51% variance unexplained; MAE=0.114 is crude for 'quality floor'. R2 rebuts severity: bisection still correct on staircase (efficiency not correctness issue); B=8/16 validated PPL <0.01 diff; rank-order sufficient for b* selection. Consensus on substance, divergence on severity (R1: critical, R2: should-fix).\"\n  action_items:\n    - round: 3\n      action: \"Add micro-batch design justification\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 4\n      action: \"§3.3 must acknowledge B=4 discretization explicitly; clarify bisection is correct but 'continuous optimization' framing misleads; strengthen B=8/16 evidence (multi-seed if possible)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W8\"\n  summary: \"Proposition 1 proof sketch misleading: Cov≥0 is tautological given r_i=1[q_i≤0.5]\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Covariance positivity by construction.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Full consensus. Presentation issue.\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未单独提及\"\n  action_items:\n    - round: 3\n      action: \"Rewrite: state monotonicity by construction\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W9\"\n  summary: \"ECE abbreviation used without definition\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"ECE appears multiple times without expansion.\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未单独提及。当前版本 Introduction line 25 已有 'Expected Calibration Error, ECE' 定义。\"\n  action_items:\n    - round: 3\n      action: \"Define ECE at first occurrence\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M1\"\n  summary: \"Responsible NLP Research Checklist — required by ACL ARR\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [R2]\n      note: \"ACL ARR requires checklist.\"\n    - round: 4\n      reviewers: [R2]\n      note: \"Checklist now present (sections/checklist.tex, A1-E1 all filled). R2 confirms '格式完全合规' and 'checklist 认真填写'. Resolved.\"\n  action_items:\n    - round: 3\n      action: \"Complete checklist\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Checklist present and substantively filled\"\n  resolution_round: 4\n\n- id: \"R3-M2\"\n  summary: \"Hybrid method (q>0.95 + adaptive) achieves 17.514 but not discussed as recommended approach\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Hybrid 0.139 PPL better.\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未单独提及。Discussion 中有'hybrid + minimum intervention philosophy contradiction'段落。\"\n  action_items:\n    - round: 3\n      action: \"Discuss in main text\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M3\"\n  summary: \"Detector training details insufficient for reproducibility\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [R1]\n      note: \"Missing TF-IDF details.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Appendix J now contains full detector details: TF-IDF features (unigrams+bigrams, max 50K, sublinear TF), LR (C=1.0, L2, lbfgs, max_iter=100), calibration (T=0.204), generation params (nucleus p=0.95, T=0.8, 384 tokens). R1 gives Reproducibility 4/5.\"\n  action_items:\n    - round: 3\n      action: \"Add Appendix section\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Appendix J (Detector and Synthetic Data Details) added with full specs\"\n  resolution_round: 4\n\n- id: \"R3-M4\"\n  summary: \"Llama-3.2-3B cross-model results — no table, unverifiable\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Limitations mentions Llama-3.2-3B parity but no table.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Appendix I (Table 10) now exists with MMLU +1.57pp / HellaSwag -0.60pp. But still single seed and no PPL ('checkpoints not retained'). R1 flags this as experimental management failure.\"\n  action_items:\n    - round: 3\n      action: \"Add Appendix table\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"Re-run cross-model experiment with checkpoint retention for PPL comparison; or clearly label as 'preliminary, single seed, no PPL available'\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M5\"\n  summary: \"Reference issues: lin2017focal venue type, vehtari2024psis year\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"vehtari2024psis year uncertain.\"\n    - round: 3\n      reviewers: [R1]\n      note: \"lin2017focal: article→inproceedings.\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未单独提及\"\n  action_items:\n    - round: 3\n      action: \"Fix reference types/years\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"Hard filtering crushes reweighting (17.290 vs 17.651); undermines motivation\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [research_reviewer]\n      note: \"Epoch-matched controls added.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Table 2 resolves confound. Both cite as strength.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Epoch-matched finding remains a consensus strength. Table 2 convincing.\"\n  action_items:\n    - round: 2\n      action: \"Add epoch-matched discussion\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Epoch-matched 3-seed Table 2 resolves the confound\"\n  resolution_round: 3\n\n- id: \"R1-N1\"\n  summary: \"'Statistically indistinguishable' → 'competitive' but CI still problematic\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"p=0.30 failure-to-reject ≠ equivalence.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Changed to 'competitive'. Residual in R3-N1.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"R1-N3: 'competitive' still implied equivalence. Abstract compares gap to cross-seed variance (different statistical quantities). CI [-0.039, 0.101] means possible 0.101 degradation.\"\n  action_items:\n    - round: 2\n      action: \"Replace 'statistically indistinguishable'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"Tracked via R3-N1\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"α_eff motivation disconnected from computation; Proposition 1 covariance tautological\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"No error bound for α_eff vs true α.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Proxy validation added. Proposition 1 tautology persists.\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未单独提及。Tracked via R3-N2 and R3-W8.\"\n  action_items:\n    - round: 2\n      action: \"Add proxy discussion\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Proxy validation added. Remaining in R3-N2, R3-W8.\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"External validity insufficient: single model/detector/data/contamination-type\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Far less coverage than Drayson.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"1.7B added, 3 detectors tested.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Tracked via R3-N3, R3-N5, R3-W1.\"\n  action_items:\n    - round: 2\n      action: \"Acknowledge in Limitations\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Partially addressed. Remaining in R3-N3, R3-N5, R3-W1.\"\n  resolution_round: null\n\n- id: \"R1-W1\"\n  summary: \"Effect size tiny with downstream 4/5 benchmarks worse\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Suggest reframing.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Reframing done but concern persists.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Tracked via R3-N1.\"\n  action_items:\n    - round: 2\n      action: \"Reframe\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reframing done. Remaining in R3-N1.\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Proposition 1 proof gap: strictly increasing vs non-decreasing\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Fixable.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Confirmed fixed.\"\n  action_items:\n    - round: 2\n      action: \"Fix\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed\"\n  resolution_round: 3\n\n- id: \"R1-W3\"\n  summary: \"ESS monotonicity not formally proven\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Citation insufficient.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Confirmed fixed: Proposition 2 with proof.\"\n  action_items:\n    - round: 2\n      action: \"Add proof\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"Grid-b post-hoc oracle\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Footnote added.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"R1-W4: post-hoc vs validation-based distinction should be discussed more explicitly; this actually favors the paper. R2 agrees.\"\n  action_items:\n    - round: 2\n      action: \"Add annotation\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"Expand discussion: note that validation-based grid search would likely be worse than post-hoc, making adaptive's advantage larger in practice\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"D&R and Golden Ratio baselines seed coverage\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"D&R needs 3-seed.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"D&R epoch-matched 3-seed in Table 2.\"\n  action_items:\n    - round: 2\n      action: \"Run multi-seed\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"D&R epoch-matched 3-seed complete\"\n  resolution_round: 2\n\n- id: \"R2-W1\"\n  summary: \"Novelty relative to Drayson limited\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Both agree Findings-level.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Escalated to critical in R3-N4.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Tracked via R3-N4.\"\n  action_items:\n    - round: 2\n      action: \"Clarify unique aspects\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Residual in R3-N4.\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"τ depends on ρ, contradicting 'zero validation cost'\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"τ≈1−ρ/2 contradicts ρ-unknown.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Heuristic deleted.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Tracked via R3-N2.\"\n  action_items:\n    - round: 2\n      action: \"Delete heuristic\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Heuristic deleted. Remaining in R3-N2.\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"Citation density insufficient\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [director_audit]\n      note: \"Increased to 30.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Now ~39.\"\n    - round: 4\n      reviewers: [R2]\n      note: \"Tracked via R3-W3.\"\n  action_items:\n    - round: 2\n      action: \"Add references\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Increased to 41 but still below norm. See R3-W3.\"\n  resolution_round: null\n\n- id: \"R2-M1\"\n  summary: \"'five approaches' but lists 6 methods\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Count error.\"\n  action_items:\n    - round: 2\n      action: \"Fix\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed: now says 'six approaches'\"\n  resolution_round: 2\n\n- id: \"R2-M2\"\n  summary: \"Grid-b values inconsistent\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Inconsistent.\"\n  action_items:\n    - round: 2\n      action: \"Unify\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Unified\"\n  resolution_round: 2\n\n- id: \"R2-M3\"\n  summary: \"Reference guo2025escaping phantom\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [director_audit]\n      note: \"Deleted.\"\n  action_items:\n    - round: 2\n      action: \"Remove\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Deleted\"\n  resolution_round: 2\n\n- id: \"R2-M5\"\n  summary: \"Hybrid ρ=0.6 comparability\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Hybrid changes effective ρ.\"\n    - round: 3\n      reviewers: [R2]\n      note: \"Footnote added.\"\n  action_items:\n    - round: 2\n      action: \"Add note\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Footnote added\"\n  resolution_round: 3\n\n# New issues from Round 4\n- id: \"R4-N1\"\n  summary: \"'D&R' abbreviation used in Abstract and Introduction without definition\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Abstract line 9 'D&R's full-length advantage' and Introduction contribution #2 use D&R without prior definition. Full form 'Detect & Remove' first appears in §4. Consensus.\"\n  action_items:\n    - round: 4\n      action: \"Define 'Detect and Remove (D&R)' at first use in Abstract or Introduction\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N2\"\n  summary: \"Grid search at ρ=0.6 is single seed; Adaptive-vs-Grid gap 0.106 unreliable\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Table 5 (Appendix E): Grid b=0.3 at ρ=0.6 is seed 42 only. Adaptive 3-seed mean 17.736 vs Grid 17.634, gap 0.102. At ρ=0.4, Grid 3-seed variance ±0.033, so single-seed comparison unreliable. §5.2 'gap widens' narrative not supported. Consensus.\"\n  action_items:\n    - round: 4\n      action: \"Run 3-seed Grid at ρ=0.6, or clearly label comparison as single-seed preliminary; remove 'gap widens' claim\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N3\"\n  summary: \"Epoch-matched LR schedule confound: D&R 2533 steps vs adaptive 6103 steps with different cosine schedules\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"R1-W3 raises this. R2 partially rebuts: confound direction likely favors paper's conclusion (shorter schedule may hurt D&R, so fair comparison would strengthen epoch-confound finding). Both agree 1-2 sentence discussion would suffice. Minor divergence on severity.\"\n  action_items:\n    - round: 4\n      action: \"Add brief discussion of LR schedule difference in §5.1 or Table 2 caption\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N4\"\n  summary: \"p<0.01 (N=3) reporting needs caveats: 2 df, normality unverifiable\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"R1-W5: N=3 paired t-test has 2 df, t-distribution tails very thick, normality assumption uncheckable. R2 agrees. Both suggest: report exact paired differences, add sample size caveat, consider non-parametric robustness check.\"\n  action_items:\n    - round: 4\n      action: \"Report exact paired differences alongside p-values; add caveat about N=3 t-test limitations\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N5\"\n  summary: \"wang2026survive (arXiv:2602.16065) date needs verification — 2026 February arXiv preprint\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [R2]\n      note: \"arXiv ID 2602.16065 implies February 2026 posting. Needs verification that this paper actually exists and is publicly available.\"\n  action_items:\n    - round: 4\n      action: \"Verify wang2026survive exists on arXiv; confirm ID and publication status\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "provenance_weight_training",
    "issues_yaml": "- id: \"RR-W1\"\n  summary: \"Paper claims 'from random initialization' but code uses from_pretrained() — actually continued pretraining\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [research_reviewer]\n      note: \"Two independent reviews confirmed: pretrain_weighted.py L318 uses from_pretrained()\"\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Both reviewers confirm fixed\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"本轮未提及，已确认修复\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及，已确认修复\"\n  action_items:\n    - round: 1\n      action: \"Fix paper text\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed in current version\"\n  resolution_round: 2\n\n- id: \"RR-W2\"\n  summary: \"Paper claims 'balanced real/synthetic test set' but eval_holdout.jsonl is human-only\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [research_reviewer]\n      note: \"eval_holdout.jsonl: 67823 lines, all source=fineweb\"\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Confirmed fixed\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及，已确认修复\"\n  action_items:\n    - round: 1\n      action: \"Fix paper text\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed\"\n  resolution_round: 2\n\n- id: \"R3-N1\"\n  summary: \"Statistical support insufficient: N=3 CI [-0.039, 0.101] includes degradation; 'competitive' is overstatement; downstream 4/5 tasks worse\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"R1-N1: 'statistically indistinguishable' changed to 'competitive'.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Full consensus. 'competitive' still overstatement.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Full consensus again. R1 emphasizes CI upper bound 0.101 is 2.3x the effect; Abstract/Conclusion framing inconsistent with §5.1 caveats. R2 adds downstream 4/5 negative pattern more concerning than individual negatives. Both agree PPL may be distribution matching artifact.\"\n  action_items:\n    - round: 3\n      action: \"Weaken framing; add CI caveat; add downstream caveat\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 4\n      action: \"Abstract must explicitly note CI includes degradation; move downstream results to main text (not just Appendix); discuss PPL-downstream divergence in Results or Discussion\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N2\"\n  summary: \"Theory-empirical disconnect: τ=0.8 is empirical but framed as 'principled default'; Wang 2026 requires known α; τ optimal shifts with ρ\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"α_eff motivation disconnected.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Full consensus.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"R1 confirms τ sweep based on single seed/single ρ. R2 agrees 'robust defaults' overclaimed. Both: τ validated on only 2 ρ values (0.4, 0.6) and 1 model.\"\n  action_items:\n    - round: 3\n      action: \"'principled defaults' → 'empirically robust defaults'\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 4\n      action: \"Further weaken to 'default values that perform well in the tested configurations'; explicitly state τ sweep is single-seed\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"1.7B 'transfers without degradation' claim unsupported: 2 seeds adaptive vs 1 seed uniform, Δ=-0.01\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"1.7B added but single seed.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Δ=-0.01 equally supports 'no effect at this scale'.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Full consensus. R1: 2 data points cannot compute meaningful CI or p-value; 'confirming' in §5.2 is too strong. R2 agrees, notes Conclusion is more restrained but §5.2 is not.\"\n  action_items:\n    - round: 3\n      action: \"Reposition as 'does not degrade' with explicit no-amplification acknowledgment\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 4\n      action: \"§5.2 change 'confirming' → 'preliminary evidence suggests'; do not cite as contribution in Abstract/Conclusion; add 3+ seeds or remove scale claim\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N4\"\n  summary: \"Novelty insufficient for EMNLP Main: core formula from Drayson 2025, dual constraint is standard IS, minimum intervention is standard constrained optimization\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Both agree Findings-level.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Consensus Findings-level.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Full consensus. R2: three claimed differentiators are (i) engineering, (ii) implementation, (iii) experimental finding. R1 agrees and adds: analytical findings (epoch confound, detector type) have higher independent value than the method. Both recommend reframing as analysis-driven contribution.\"\n  action_items:\n    - round: 3\n      action: \"Strengthen contributions: epoch-matched as corrective, detector type as practical\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 4\n      action: \"Consider reframing paper: analytical study (epoch confound + detector type findings) as primary contributions, method as practical byproduct. This better matches actual evidence and may improve reception at Findings track.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N5\"\n  summary: \"Scale mismatch: paper frames web-scale but experiments only 0.6B/132M tokens\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Full consensus.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"R1: Introduction opens with web-scale but experiments 4 orders of magnitude smaller. R2: 132M tokens reasonable for continued pretraining (cites Gururangan 2020) but Introduction should limit scope explicitly.\"\n  action_items:\n    - round: 3\n      action: \"Narrow Introduction to continued pretraining scenario\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 4\n      action: \"Introduction must explicitly state 'continued pretraining on moderate-scale corpora' early; Abstract should limit scope\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W1\"\n  summary: \"Self-contamination (generator=trainee) external validity: real web contamination is multi-source, multi-model\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Part of external validity.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Self-contamination not representative.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Escalated by both reviewers. R1: self-contamination is NOT the 'challenging scenario' claimed — AUC=0.94 shows it's easy. R2: Limitations has no dedicated paragraph on self-contamination design. Cross-model (Appendix H) single seed, mixed results, no PPL ('checkpoints not retained' is experimental management failure).\"\n  action_items:\n    - round: 3\n      action: \"Strengthen Limitations discussion\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 4\n      action: \"Add dedicated self-contamination limitation paragraph; remove 'challenging detection scenario' claim from §4; if possible run one cross-generator experiment with retained checkpoints\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2\"\n  summary: \"Abstract ~280-291 words, exceeds 250 convention; data-heavy rather than narrative-driven\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"R2: reads like Results summary.\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未单独提及，但R1-N3指出Abstract framing与证据不一致，属相关问题\"\n  action_items:\n    - round: 3\n      action: \"Trim to ≤250 words\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W3\"\n  summary: \"Citation coverage still insufficient: ~41 refs; missing recent contamination-aware training works\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [director_audit]\n      note: \"Increased to 30 refs.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Now ~39 still below norm.\"\n    - round: 4\n      reviewers: [R2]\n      note: \"Now ~41 refs. R2 identifies 3 specific missing works: Kang et al. (EMNLP 2025) 'Demystifying Synthetic Data in LLM Pre-training'; Zhang et al. (2025) 'ForTIFAI' (arXiv:2509.08972); Yi et al. (2025) 'Escaping Model Collapse via Synthetic Data Verification' (arXiv:2510.16657). R1 agrees in principle but cannot independently verify existence.\"\n  action_items:\n    - round: 3\n      action: \"Add 10-15 references\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 4\n      action: \"Verify and add R2's 3 suggested references if confirmed real; aim for 50+ total\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W4\"\n  summary: \"Discussion section too thin: rehashes Results without deeper analysis\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Missing failure conditions, PSIS, deployment guidance.\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未单独提及，Discussion 内容已有扩展但仍偏薄\"\n  action_items:\n    - round: 3\n      action: \"Expand to ~40-50 lines\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W5\"\n  summary: \"'Minimum Intervention Principle' framing overstates a standard constrained optimization choice\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Standard optimization not a 'principle'.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"R1-W6: minimum intervention not proven optimal, (b_τ+b_ESS)/2 not tested. R2 partially rebuts: ESS-only ablation shows maximum is worse, so minimum > maximum established; but agrees should label as heuristic/design choice. Consensus: label as 'empirically motivated strategy', not 'principle' or implied optimality.\"\n  action_items:\n    - round: 3\n      action: \"'minimum intervention principle' → 'empirically motivated minimum intervention strategy'\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 4\n      action: \"Consider testing midpoint strategy as ablation; if not feasible, explicitly state minimum intervention is a design choice, not proven optimal\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W6\"\n  summary: \"ρ=0.2 failure (+0.046 PPL) undiscussed in main text; failure mechanism unexplained\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Consensus.\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未单独提及。论文已在 Discussion 中加入 ρ=0.2 failure 分析段落（mean_q=0.393, 60% α_eff-binding）。Appendix K 也新增了低污染分析。\"\n  action_items:\n    - round: 3\n      action: \"Add ρ=0.2 analysis\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W7\"\n  summary: \"Micro-batch B=4: α_eff has only 5 discrete values, 'continuous adaptive selection' framing inconsistent\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"B=4 means α_eff ∈ {0, 0.25, 0.5, 0.75, 1.0}.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"R1 raises to critical (N4): bisection on staircase function; Pearson r=0.70 means 51% variance unexplained; MAE=0.114 is crude for 'quality floor'. R2 rebuts severity: bisection still correct on staircase (efficiency not correctness issue); B=8/16 validated PPL <0.01 diff; rank-order sufficient for b* selection. Consensus on substance, divergence on severity (R1: critical, R2: should-fix).\"\n  action_items:\n    - round: 3\n      action: \"Add micro-batch design justification\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 4\n      action: \"§3.3 must acknowledge B=4 discretization explicitly; clarify bisection is correct but 'continuous optimization' framing misleads; strengthen B=8/16 evidence (multi-seed if possible)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W8\"\n  summary: \"Proposition 1 proof sketch misleading: Cov≥0 is tautological given r_i=1[q_i≤0.5]\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Covariance positivity by construction.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Full consensus. Presentation issue.\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未单独提及\"\n  action_items:\n    - round: 3\n      action: \"Rewrite: state monotonicity by construction\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W9\"\n  summary: \"ECE abbreviation used without definition\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"ECE appears multiple times without expansion.\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未单独提及。当前版本 Introduction line 25 已有 'Expected Calibration Error, ECE' 定义。\"\n  action_items:\n    - round: 3\n      action: \"Define ECE at first occurrence\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M1\"\n  summary: \"Responsible NLP Research Checklist — required by ACL ARR\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [R2]\n      note: \"ACL ARR requires checklist.\"\n    - round: 4\n      reviewers: [R2]\n      note: \"Checklist now present (sections/checklist.tex, A1-E1 all filled). R2 confirms '格式完全合规' and 'checklist 认真填写'. Resolved.\"\n  action_items:\n    - round: 3\n      action: \"Complete checklist\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Checklist present and substantively filled\"\n  resolution_round: 4\n\n- id: \"R3-M2\"\n  summary: \"Hybrid method (q>0.95 + adaptive) achieves 17.514 but not discussed as recommended approach\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Hybrid 0.139 PPL better.\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未单独提及。Discussion 中有'hybrid + minimum intervention philosophy contradiction'段落。\"\n  action_items:\n    - round: 3\n      action: \"Discuss in main text\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M3\"\n  summary: \"Detector training details insufficient for reproducibility\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [R1]\n      note: \"Missing TF-IDF details.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Appendix J now contains full detector details: TF-IDF features (unigrams+bigrams, max 50K, sublinear TF), LR (C=1.0, L2, lbfgs, max_iter=100), calibration (T=0.204), generation params (nucleus p=0.95, T=0.8, 384 tokens). R1 gives Reproducibility 4/5.\"\n  action_items:\n    - round: 3\n      action: \"Add Appendix section\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Appendix J (Detector and Synthetic Data Details) added with full specs\"\n  resolution_round: 4\n\n- id: \"R3-M4\"\n  summary: \"Llama-3.2-3B cross-model results — no table, unverifiable\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Limitations mentions Llama-3.2-3B parity but no table.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Appendix I (Table 10) now exists with MMLU +1.57pp / HellaSwag -0.60pp. But still single seed and no PPL ('checkpoints not retained'). R1 flags this as experimental management failure.\"\n  action_items:\n    - round: 3\n      action: \"Add Appendix table\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"Re-run cross-model experiment with checkpoint retention for PPL comparison; or clearly label as 'preliminary, single seed, no PPL available'\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M5\"\n  summary: \"Reference issues: lin2017focal venue type, vehtari2024psis year\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"vehtari2024psis year uncertain.\"\n    - round: 3\n      reviewers: [R1]\n      note: \"lin2017focal: article→inproceedings.\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未单独提及\"\n  action_items:\n    - round: 3\n      action: \"Fix reference types/years\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"Hard filtering crushes reweighting (17.290 vs 17.651); undermines motivation\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [research_reviewer]\n      note: \"Epoch-matched controls added.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Table 2 resolves confound. Both cite as strength.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Epoch-matched finding remains a consensus strength. Table 2 convincing.\"\n  action_items:\n    - round: 2\n      action: \"Add epoch-matched discussion\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Epoch-matched 3-seed Table 2 resolves the confound\"\n  resolution_round: 3\n\n- id: \"R1-N1\"\n  summary: \"'Statistically indistinguishable' → 'competitive' but CI still problematic\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"p=0.30 failure-to-reject ≠ equivalence.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Changed to 'competitive'. Residual in R3-N1.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"R1-N3: 'competitive' still implied equivalence. Abstract compares gap to cross-seed variance (different statistical quantities). CI [-0.039, 0.101] means possible 0.101 degradation.\"\n  action_items:\n    - round: 2\n      action: \"Replace 'statistically indistinguishable'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"Tracked via R3-N1\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"α_eff motivation disconnected from computation; Proposition 1 covariance tautological\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"No error bound for α_eff vs true α.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Proxy validation added. Proposition 1 tautology persists.\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未单独提及。Tracked via R3-N2 and R3-W8.\"\n  action_items:\n    - round: 2\n      action: \"Add proxy discussion\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Proxy validation added. Remaining in R3-N2, R3-W8.\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"External validity insufficient: single model/detector/data/contamination-type\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Far less coverage than Drayson.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"1.7B added, 3 detectors tested.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Tracked via R3-N3, R3-N5, R3-W1.\"\n  action_items:\n    - round: 2\n      action: \"Acknowledge in Limitations\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Partially addressed. Remaining in R3-N3, R3-N5, R3-W1.\"\n  resolution_round: null\n\n- id: \"R1-W1\"\n  summary: \"Effect size tiny with downstream 4/5 benchmarks worse\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Suggest reframing.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Reframing done but concern persists.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Tracked via R3-N1.\"\n  action_items:\n    - round: 2\n      action: \"Reframe\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reframing done. Remaining in R3-N1.\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Proposition 1 proof gap: strictly increasing vs non-decreasing\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Fixable.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Confirmed fixed.\"\n  action_items:\n    - round: 2\n      action: \"Fix\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed\"\n  resolution_round: 3\n\n- id: \"R1-W3\"\n  summary: \"ESS monotonicity not formally proven\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Citation insufficient.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Confirmed fixed: Proposition 2 with proof.\"\n  action_items:\n    - round: 2\n      action: \"Add proof\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"Grid-b post-hoc oracle\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Consensus.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Footnote added.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"R1-W4: post-hoc vs validation-based distinction should be discussed more explicitly; this actually favors the paper. R2 agrees.\"\n  action_items:\n    - round: 2\n      action: \"Add annotation\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"Expand discussion: note that validation-based grid search would likely be worse than post-hoc, making adaptive's advantage larger in practice\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"D&R and Golden Ratio baselines seed coverage\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"D&R needs 3-seed.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"D&R epoch-matched 3-seed in Table 2.\"\n  action_items:\n    - round: 2\n      action: \"Run multi-seed\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"D&R epoch-matched 3-seed complete\"\n  resolution_round: 2\n\n- id: \"R2-W1\"\n  summary: \"Novelty relative to Drayson limited\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Both agree Findings-level.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Escalated to critical in R3-N4.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Tracked via R3-N4.\"\n  action_items:\n    - round: 2\n      action: \"Clarify unique aspects\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Residual in R3-N4.\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"τ depends on ρ, contradicting 'zero validation cost'\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"τ≈1−ρ/2 contradicts ρ-unknown.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Heuristic deleted.\"\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Tracked via R3-N2.\"\n  action_items:\n    - round: 2\n      action: \"Delete heuristic\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Heuristic deleted. Remaining in R3-N2.\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"Citation density insufficient\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [director_audit]\n      note: \"Increased to 30.\"\n    - round: 3\n      reviewers: [R1, R2]\n      note: \"Now ~39.\"\n    - round: 4\n      reviewers: [R2]\n      note: \"Tracked via R3-W3.\"\n  action_items:\n    - round: 2\n      action: \"Add references\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Increased to 41 but still below norm. See R3-W3.\"\n  resolution_round: null\n\n- id: \"R2-M1\"\n  summary: \"'five approaches' but lists 6 methods\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Count error.\"\n  action_items:\n    - round: 2\n      action: \"Fix\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed: now says 'six approaches'\"\n  resolution_round: 2\n\n- id: \"R2-M2\"\n  summary: \"Grid-b values inconsistent\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Inconsistent.\"\n  action_items:\n    - round: 2\n      action: \"Unify\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Unified\"\n  resolution_round: 2\n\n- id: \"R2-M3\"\n  summary: \"Reference guo2025escaping phantom\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [director_audit]\n      note: \"Deleted.\"\n  action_items:\n    - round: 2\n      action: \"Remove\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Deleted\"\n  resolution_round: 2\n\n- id: \"R2-M5\"\n  summary: \"Hybrid ρ=0.6 comparability\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Hybrid changes effective ρ.\"\n    - round: 3\n      reviewers: [R2]\n      note: \"Footnote added.\"\n  action_items:\n    - round: 2\n      action: \"Add note\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Footnote added\"\n  resolution_round: 3\n\n# New issues from Round 4\n- id: \"R4-N1\"\n  summary: \"'D&R' abbreviation used in Abstract and Introduction without definition\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Abstract line 9 'D&R's full-length advantage' and Introduction contribution #2 use D&R without prior definition. Full form 'Detect & Remove' first appears in §4. Consensus.\"\n  action_items:\n    - round: 4\n      action: \"Define 'Detect and Remove (D&R)' at first use in Abstract or Introduction\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N2\"\n  summary: \"Grid search at ρ=0.6 is single seed; Adaptive-vs-Grid gap 0.106 unreliable\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"Table 5 (Appendix E): Grid b=0.3 at ρ=0.6 is seed 42 only. Adaptive 3-seed mean 17.736 vs Grid 17.634, gap 0.102. At ρ=0.4, Grid 3-seed variance ±0.033, so single-seed comparison unreliable. §5.2 'gap widens' narrative not supported. Consensus.\"\n  action_items:\n    - round: 4\n      action: \"Run 3-seed Grid at ρ=0.6, or clearly label comparison as single-seed preliminary; remove 'gap widens' claim\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N3\"\n  summary: \"Epoch-matched LR schedule confound: D&R 2533 steps vs adaptive 6103 steps with different cosine schedules\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"R1-W3 raises this. R2 partially rebuts: confound direction likely favors paper's conclusion (shorter schedule may hurt D&R, so fair comparison would strengthen epoch-confound finding). Both agree 1-2 sentence discussion would suffice. Minor divergence on severity.\"\n  action_items:\n    - round: 4\n      action: \"Add brief discussion of LR schedule difference in §5.1 or Table 2 caption\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N4\"\n  summary: \"p<0.01 (N=3) reporting needs caveats: 2 df, normality unverifiable\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [R1, R2]\n      note: \"R1-W5: N=3 paired t-test has 2 df, t-distribution tails very thick, normality assumption uncheckable. R2 agrees. Both suggest: report exact paired differences, add sample size caveat, consider non-parametric robustness check.\"\n  action_items:\n    - round: 4\n      action: \"Report exact paired differences alongside p-values; add caveat about N=3 t-test limitations\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N5\"\n  summary: \"wang2026survive (arXiv:2602.16065) date needs verification — 2026 February arXiv preprint\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [R2]\n      note: \"arXiv ID 2602.16065 implies February 2026 posting. Needs verification that this paper actually exists and is publicly available.\"\n  action_items:\n    - round: 4\n      action: \"Verify wang2026survive exists on arXiv; confirm ID and publication status\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-19T06:05:17.557540+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml\", \"bytes\": 31880}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-19T06:07:52.858824+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "provenance_weight_training",
  "report": "# 审稿报告 — Round 4 (Fresh Review)\n\n**论文**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验+统计; R2: 新颖性+叙事+Related Work+格式）\n**审稿轮次**: Round 1 独立初审 → 交叉分享 → 收敛（1 轮收敛，关键问题全部达成共识）\n\n---\n\n## Summary\n\n本文提出 Minimum Intervention Reweighting (MIR)，在 detect-and-reweight 框架 w(x)=(1-q(x))^b 下，通过 per-batch 双约束优化（α_eff(b) ≥ τ 质量下限 + ESS(b) ≥ n_min 稳定性上限）自动选择最小 b，消除 grid search。在 Qwen3-0.6B 续训（132M FineWeb tokens, 40% 合成污染）上，adaptive b* 与 grid-best 竞争（gap 0.031 PPL, 95% CI [-0.039, 0.101]），将搜索从 9 次训练降至 1 次。论文还发现 D&R 的优势完全来自多 epoch 暴露（epoch-matched Δ=0.006），以及判别式检测器（而非生成式）是 reweighting 有效性的必要条件。\n\n---\n\n## Strengths\n\n**S1. D&R Epoch Confound 发现（独立社区价值）** [共识]\nTable 2 的 epoch-matched 实验干净地分离了 data exposure 和 filtering quality：D&R 全长 17.290 vs. epoch-matched 17.657（Δ=0.367 完全来自多 epoch），3-seed 验证。这是一个有纠偏价值的 corrective finding，无论方法本身是否被接受。\n\n**S2. Detector Type 发现（实践指导意义）** [共识]\nGPT-2 PPL (AUC=0.91) 反而使 adaptive 退化 (+0.10)，证明 AUC 不等于 reweighting effectiveness。discriminative vs. generative 的区分对实践有指导意义，这个发现可能比方法本身更有影响力。\n\n**S3. 诚实透明的 Limitations** [共识]\n论文对自身局限的讨论异常坦诚：ρ=0.2 失败、downstream mixed、1.7B 无优势、CI 包含退化。Conclusion 明确承认 \"the method's primary value lies in the 0.6B continued pretraining regime tested here\"。在该领域少见。\n\n**S4. 框架设计优雅** [共识]\n将 b 选择形式化为双约束优化，两个约束具有自然的对立单调性（Proposition 1 & 2），比 grid search 更有原则性。\n\n**S5. 写作和格式** [共识]\n写作干净，无 em-dash/en-dash AI 痕迹，无过度分段，技术术语使用精准。格式完全合规（ACL review 模板, double-blind, 行号开启, Limitations section, Responsible NLP Research Checklist 认真填写）。\n\n**S6. 可复现性高** [共识]\n算法、超参、训练配置、detector 细节（Appendix J）描述充分。R1/R2 均给出 Reproducibility 4/5。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**C1. 新颖性不足以支撑 Main Conference** [R1 AGREE, R2 raised; 共识]\n论文使用与 Drayson et al. (2025) 完全相同的公式 w=(1-q)^b。全部方法创新在于 b 的选择方式：\n- (i) per-batch vs fixed b：工程层面改进\n- (ii) loss reweighting vs SIR resampling：实现选择差异\n- (iii) lightweight detector suffices：实验发现而非方法贡献\n- α_eff 约束是 Wang et al. (2026) 收敛理论的直接操作化；ESS 约束是 importance sampling 标准做法 (Kish 1965)\n- \"Minimum intervention\" 本质是在两个单调函数上取 infimum，属标准约束优化\n\n论文最有价值的贡献（D&R epoch confound, detector type finding）是**分析性发现**而非方法贡献，但当前 framing 将方法置于核心（Contribution 1）。两位 Reviewer 一致建议重新定位：以 analytical study 为主、method 为辅。\n\n**C2. 效应量极小，下游任务不支持 PPL 改善的实际意义** [R1 raised, R2 AGREE; 共识]\n- ρ=0.4: Δ = -0.043 PPL (0.24% relative)，在续训已吸收 5.2 PPL 的残差区间内\n- ρ=0.6: Δ = -0.028 (减弱)\n- 1.7B: Δ = -0.01 (negligible)\n- Downstream: 5 个 benchmark 中 4 个为负（ARC-C -0.005, ARC-E -0.007, HellaSwag -0.005, WinoGrande -0.008），sign-test p≈0.19\n- PPL 改善可能仅反映 distribution matching（训练数据更接近 human-only 评估集），而非真正的模型质量提升\n- Abstract/Introduction framing 给出比实际证据更强的印象\n\n**C3. \"Competitive with grid-best\" 的 framing 与统计证据不一致** [R1 raised, R2 AGREE; 共识]\n- 95% CI [-0.039, 0.101] 包含 0.101 PPL 的降级（upper bound 是 effect size 的 2.3x）\n- Abstract 将 gap (0.031) 与 cross-seed variance (±0.033) 做比较，但这是两个不同统计量（paired variability vs. marginal variability）\n- N=3 下 CI 过宽是 power 不足的结果，不是等价性的证明\n- §5.1 的 \"we refrain from claiming statistical indistinguishability\" 是正确的审慎态度，但 Abstract 和 Conclusion 的措辞与此矛盾\n\n**C4. 1.7B \"transfers without degradation\" claim 缺乏统计支撑** [R1 raised, R2 AGREE; 共识]\n- 2 seeds adaptive (13.25, 13.27) vs. 1 seed uniform (13.26)\n- Δ = -0.01 在任何标准下都无法区分 noise 和 signal\n- §5.2 的 \"confirming\" 用词过强\n- 效应量从 0.6B 到 1.7B 缩小 4x，equally consistent with \"no effect at this scale\"\n\n**C5. 自污染实验设计严重限制泛化性** [R2 raised as critical, R1 AGREE; 共识]\n- Self-contamination (generator=trainee) 是最容易检测的场景，不是论文声称的 \"challenging detection scenario\"\n- TF-IDF+LR 在此场景下达到 AUC=0.94 恰好证明了检测的容易性\n- 真实 web 污染的关键挑战（多源异构、非均匀混合）在 uniform random mixing 设计中完全缺失\n- Limitations section **没有**将 self-contamination 作为独立限制讨论\n- Cross-model 结果 (Appendix H) 单 seed、mixed results、缺少 PPL（\"checkpoints not retained\"）\n\n### Warning（影响评分但不一票否决）\n\n**W1. B=4 下 α_eff 仅 5 个离散值，与 \"连续优化\" 叙事不一致** [R1: critical N4; R2: should-fix W6; 严重程度分歧]\n- B=4 时 α_eff ∈ {0, 0.25, 0.5, 0.75, 1.0}，bisection 在阶梯函数上运行\n- Pearson r≈0.70（51% 方差未解释），MAE=0.114\n- R2 反驳严重程度：bisection 仍正确（效率非正确性问题）；B=8/16 验证 PPL <0.01 差异\n- 共识：substance 成立，但方法描述与实际操作之间存在失配，需在§3.3 承认\n\n**W2. \"Robust defaults\" 声明验证不足** [共识]\n- τ sweep 基于 seed 42, ρ=0.4 单次实验\n- ρ=0.6 时 optimal τ shift 到 0.7（Figure 3）\n- \"empirically robust defaults that transfer without per-model tuning\" 仅在 1 个模型、2 个 ρ 值上验证\n- 建议弱化为 \"default values that perform well in the tested configurations\"\n\n**W3. Grid search 在 ρ=0.6 为单 seed** [共识]\n- Table 5: Grid b=0.3 at ρ=0.6 仅 seed 42 (17.634)\n- Adaptive 3-seed mean 17.736 vs Grid 单 seed，gap 0.102 不具可比性\n- §5.2 \"gap widens from 0.013 to 0.106\" 叙述不可靠\n\n**W4. \"D&R\" 缩写在 Abstract/Introduction 中未定义** [共识]\n- Abstract line 9, Introduction contribution #2 直接使用，全称首次出现在 §4\n\n**W5. 下游评估不充分** [共识]\n- 5 benchmarks, single seed, 4/5 negative Δ\n- 放在 Appendix 而非正文，且 caption 称 \"preserves downstream performance\"（over-positive interpretation）\n- 建议纳入正文并诚实讨论 PPL-downstream 脱节\n\n**W6. p<0.01 (N=3) 需要附带 caveats** [共识]\n- 2 df, t 分布尾部极厚，正态性假设不可验证\n- 建议报告 exact paired differences，注明 sample size 限制\n\n**W7. 缺少近期重要相关工作** [R2 raised, R1 AGREE with caveat]\n- R2 识别 3 篇未引用论文：Kang et al. (EMNLP 2025), Zhang et al. (2025 ForTIFAI), Yi et al. (2025)\n- R1 无法独立验证存在性但原则同意应覆盖\n- 当前 41 条引用偏少\n\n**W8. Scale mismatch: Introduction 框架 web-scale 但实验 132M tokens** [共识]\n- Introduction 以 \"Web corpora increasingly contain machine-generated text\" 开头\n- 实验规模与 web-scale 差 4 个数量级\n- 建议 Introduction 明确限定为 \"continued pretraining on moderate-scale corpora\"\n\n**W9. \"Minimum intervention\" 缺乏最优性证明** [R1 raised, R2 partially rebuts]\n- 选择 b*=b_τ (minimum) 而非中间值是设计直觉\n- R2 反驳：ESS-only ablation (maximum) 已显示退化，minimum > maximum 已建立\n- 但 (b_τ+b_ESS)/2 等中间策略未测试\n- 共识：应标注为 \"empirically motivated strategy\"，不暗示最优性\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer **完全一致**（[AGREE]）：\n\n1. 效应量过小（0.043 PPL, 0.24%），下游 4/5 为负，PPL 改善可能是 distribution matching artifact\n2. 1.7B claim 统计不支撑（2 seeds vs 1 seed, Δ=-0.01）\n3. \"Competitive\" framing 与 CI [-0.039, 0.101] 矛盾\n4. 新颖性不足以支撑 Main Conference（同一公式，不同 b 选择）\n5. 自污染设计限制泛化性，Limitations 未充分讨论\n6. \"Robust defaults\" 验证不足\n7. Grid ρ=0.6 单 seed 比较不可靠\n8. 下游评估不充分\n9. D&R 缩写未定义\n10. p<0.01 (N=3) 需要 caveats\n11. 分析性发现（epoch confound, detector type）比方法本身更有价值\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 分析 |\n|------|----|----|------|\n| B=4 离散化严重程度 | Critical (N4) | Should-Fix (W6) | R2 认为正确性不受影响，B=8/16 已验证。Director 判断：Should-Fix 更合理，离散化不影响算法正确性 |\n| Epoch-matched LR confound | Should-Fix (W3) | REBUT（方向有利） | R2 认为 schedule 差异的方向对论文结论有利而非不利。Director 判断：R2 分析合理，但应在论文中简要讨论 |\n| Minimum intervention 最优性 | Should-Fix (W6) | REBUT（ablation 已足够） | R2 认为 min > max 已通过 ESS-only ablation 建立。Director 判断：中间策略未测试是 completeness gap，但不构成 soundness 问题 |\n| Overall 评分 | 2.5/5 (Borderline Findings) | 3.0/5 (Findings) | R1 对效应量权重更大。Director 综合判断见下 |\n\n---\n\n## Questions（需要作者澄清）\n\n1. 如果 PPL 改善仅反映 distribution matching（训练数据更接近 human-only 评估集），方法的核心 value proposition 是什么？\n2. 在 B=4 的阶梯函数上，per-batch adaptation 的实际机制是什么？是 α_eff 的精确值驱动了 b* 的选择，还是其他因素（如 batch-level contamination composition 的变异性）？\n3. 论文 Conclusion 承认 \"primary value lies in the 0.6B continued pretraining regime\"——如果方法不 scale，它的 target audience 是谁？\n4. Midpoint 策略 b* = (b_τ + b_ESS)/2 是否测试过？如果 minimum 是唯一测试的 feasible region 内策略，\"minimum intervention\" 的 claim 缺乏对照\n5. Self-contamination 设计下 AUC=0.94 是否代表了真实 web 污染场景下的检测器性能？如果真实场景 AUC 显著更低，α_eff proxy 的可靠性如何？\n\n---\n\n## Missing References（R2 识别，R1 原则同意）\n\n| 论文 | 为什么相关 |\n|------|-----------|\n| Kang et al. (EMNLP 2025) \"Demystifying Synthetic Data in LLM Pre-training\" | 大规模 synthetic data mixing 研究（>1000 LLMs），直接相关 |\n| Zhang et al. (2025) \"ForTIFAI\" (arXiv:2509.08972) | 不依赖检测器的 model collapse prevention（Truncated CE loss），替代方案 |\n| Yi et al. (2025) \"Escaping Model Collapse via Synthetic Data Verification\" (arXiv:2510.16657) | Verifier-guided retraining 理论分析，与 α_eff 动机相关 |\n\n注：R1 无法独立验证这些论文的存在性，建议 Research Director 核实后决定是否引用。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。项目配置中无 `external_review.paperreview_ai.enabled` 字段。\n\n---\n\n## Overall Assessment\n\n**Overall Score: Weak Reject (for Main Conference) / Borderline Accept (for Findings)**\n\n**评分依据:**\n- R1: 2.5/5 (Borderline Findings)\n- R2: 3.0/5 (Findings)\n- Director 综合: **Weak Reject for Main Conference, potential Findings-level accept**\n\n**核心判断:**\n\n论文技术执行干净、写作诚实，但存在两个根本性问题：\n\n1. **新颖性不足以支撑 Main Conference**。核心方法对 Drayson et al. (2025) 的增量有限——同一公式，不同的 b 选择策略。双约束框架虽优雅，但各组件（α_eff 约束、ESS 约束、bisection）均来自已有工具的组合。\n\n2. **实验证据系统性地弱于 claims**。效应量极小（0.043 PPL, 0.24%），下游 4/5 为负，1.7B 无 measurable advantage，CI 包含 substantial degradation。论文在 Limitations 和 Conclusion 中审慎表述，但 Abstract 和 Introduction 的 framing 过度乐观。\n\n**论文最有价值的部分是两个分析性发现**：(1) D&R 优势完全来自多 epoch 暴露（Table 2）；(2) 检测器 signal type 而非 AUC 决定 reweighting 有效性。这些发现有独立社区价值，但在当前 framing 中被方法论述遮盖。\n\n**建议投稿路径:**\n- **Findings track**: 重新 frame 为 analytical study（epoch confound + detector type 为主要贡献，method 为实用工具），补充下游评估和统计 caveats 后，Findings 级别可行\n- **Main Conference**: 需要显著增强实验证据（更多 seeds、更大规模、下游转化、cross-generator 验证）或提出本质不同的方法创新\n\n**置信度**: 4/5（两位 Reviewer 在关键问题上独立达成高度一致，增强了判断的可信度）\n\n---\n\n## Detailed Comments\n\n### Abstract (sections/abstract.tex)\n- \"eliminating the need for exhaustive search (nine runs to one; 95% CI of gap [−0.039, 0.101], which includes possible degradation)\" — 后半句削弱前半句的 claim，造成 Abstract 内部信息矛盾。建议选择一个一致的 framing [R1]\n- \"D&R's full-length advantage\" — D&R 缩写未定义 [共识]\n- 字数偏多（约 280 words），数据堆砌过多，建议精简到 ≤250 words [R3-W2 延续]\n\n### Introduction (sections/introduction.tex)\n- Line 1 \"Web corpora increasingly contain machine-generated text\" 开启 web-scale framing，但实验仅 132M tokens / 0.6B。建议明确 scope 为 continued pretraining [共识]\n- Contribution list 将方法置于 #1，分析发现置于 #2 和 #3。建议颠倒优先级，以 analytical contributions 为主 [共识]\n- \"D&R's reported advantage\" (contribution #2) — 缩写未定义 [共识]\n\n### Method (sections/method.tex)\n- §3.2 Proposition 1 proof sketch: \"better-than-random discrimination\" 条件对 Cov ≥ 0 是冗余的（given r_i = 1[q_i ≤ 0.5]，covariance non-negativity is by construction）[R3-W8 延续]\n- §3.3 \"we compute b* at the micro-batch level (B=4)\" — 应明确承认 B=4 下 α_eff 仅 5 个离散值，bisection 退化为离散 lookup [R1-N4 / R2-W6]\n- §3.4 \"empirically robust defaults\" — 验证不足，建议弱化表述 [共识]\n\n### Experiments (sections/experiments.tex)\n- \"creates a challenging detection scenario\" — 实际上 self-contamination 下 AUC=0.94 证明这不 challenging。建议移除或改述 [R1 交叉回应]\n\n### Results (sections/results.tex)\n- §5.1 \"competitive with grid-best\" 与后文 CI caveat 矛盾 [共识]\n- §5.1 downstream 结果不在正文——4/5 negative 的 pattern 应在正文讨论 [R1-N1]\n- §5.2 \"confirming that the method transfers to larger scale without degradation\" — 2 seeds 不足以 \"confirm\"，改为 \"preliminary evidence suggests\" [共识]\n- §5.2 ρ=0.6 Grid 比较为单 seed，\"gap widens\" 叙述不可靠 [共识]\n\n### Discussion (sections/discussion.tex)\n- \"the selected exponent is 4.9× lower than the ESS-only upper bound\" — 有价值但本节整体仍偏薄\n- 缺少 PPL-downstream divergence 的讨论 [R1-N1]\n\n### Limitations (sections/limitations.tex)\n- 缺少 self-contamination 设计作为独立限制的讨论 [共识]\n- \"Cross-model transfer\" 段落讨论 Llama-3.2-3B 但这是 cross-generator transfer，不是 self-contamination 限制\n\n### References (references.bib)\n- wang2026survive (arXiv:2602.16065): 2026 年 2 月 arXiv，需验证存在性 [R2]\n- 可能缺少 3 篇近期相关工作 [R2-W4]\n- 总数 41 条偏少 [共识]\n\n### Appendix (sections/appendix.tex)\n- Detector details (Appendix J) 现在完整 [resolved]\n- Cross-model table (Appendix H, Table 10) 存在但 single seed + no PPL [R3-M4]",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject",
  "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "provenance_weight_training",
    "report": "# 审稿报告 — Round 4 (Fresh Review)\n\n**论文**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验+统计; R2: 新颖性+叙事+Related Work+格式）\n**审稿轮次**: Round 1 独立初审 → 交叉分享 → 收敛（1 轮收敛，关键问题全部达成共识）\n\n---\n\n## Summary\n\n本文提出 Minimum Intervention Reweighting (MIR)，在 detect-and-reweight 框架 w(x)=(1-q(x))^b 下，通过 per-batch 双约束优化（α_eff(b) ≥ τ 质量下限 + ESS(b) ≥ n_min 稳定性上限）自动选择最小 b，消除 grid search。在 Qwen3-0.6B 续训（132M FineWeb tokens, 40% 合成污染）上，adaptive b* 与 grid-best 竞争（gap 0.031 PPL, 95% CI [-0.039, 0.101]），将搜索从 9 次训练降至 1 次。论文还发现 D&R 的优势完全来自多 epoch 暴露（epoch-matched Δ=0.006），以及判别式检测器（而非生成式）是 reweighting 有效性的必要条件。\n\n---\n\n## Strengths\n\n**S1. D&R Epoch Confound 发现（独立社区价值）** [共识]\nTable 2 的 epoch-matched 实验干净地分离了 data exposure 和 filtering quality：D&R 全长 17.290 vs. epoch-matched 17.657（Δ=0.367 完全来自多 epoch），3-seed 验证。这是一个有纠偏价值的 corrective finding，无论方法本身是否被接受。\n\n**S2. Detector Type 发现（实践指导意义）** [共识]\nGPT-2 PPL (AUC=0.91) 反而使 adaptive 退化 (+0.10)，证明 AUC 不等于 reweighting effectiveness。discriminative vs. generative 的区分对实践有指导意义，这个发现可能比方法本身更有影响力。\n\n**S3. 诚实透明的 Limitations** [共识]\n论文对自身局限的讨论异常坦诚：ρ=0.2 失败、downstream mixed、1.7B 无优势、CI 包含退化。Conclusion 明确承认 \"the method's primary value lies in the 0.6B continued pretraining regime tested here\"。在该领域少见。\n\n**S4. 框架设计优雅** [共识]\n将 b 选择形式化为双约束优化，两个约束具有自然的对立单调性（Proposition 1 & 2），比 grid search 更有原则性。\n\n**S5. 写作和格式** [共识]\n写作干净，无 em-dash/en-dash AI 痕迹，无过度分段，技术术语使用精准。格式完全合规（ACL review 模板, double-blind, 行号开启, Limitations section, Responsible NLP Research Checklist 认真填写）。\n\n**S6. 可复现性高** [共识]\n算法、超参、训练配置、detector 细节（Appendix J）描述充分。R1/R2 均给出 Reproducibility 4/5。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**C1. 新颖性不足以支撑 Main Conference** [R1 AGREE, R2 raised; 共识]\n论文使用与 Drayson et al. (2025) 完全相同的公式 w=(1-q)^b。全部方法创新在于 b 的选择方式：\n- (i) per-batch vs fixed b：工程层面改进\n- (ii) loss reweighting vs SIR resampling：实现选择差异\n- (iii) lightweight detector suffices：实验发现而非方法贡献\n- α_eff 约束是 Wang et al. (2026) 收敛理论的直接操作化；ESS 约束是 importance sampling 标准做法 (Kish 1965)\n- \"Minimum intervention\" 本质是在两个单调函数上取 infimum，属标准约束优化\n\n论文最有价值的贡献（D&R epoch confound, detector type finding）是**分析性发现**而非方法贡献，但当前 framing 将方法置于核心（Contribution 1）。两位 Reviewer 一致建议重新定位：以 analytical study 为主、method 为辅。\n\n**C2. 效应量极小，下游任务不支持 PPL 改善的实际意义** [R1 raised, R2 AGREE; 共识]\n- ρ=0.4: Δ = -0.043 PPL (0.24% relative)，在续训已吸收 5.2 PPL 的残差区间内\n- ρ=0.6: Δ = -0.028 (减弱)\n- 1.7B: Δ = -0.01 (negligible)\n- Downstream: 5 个 benchmark 中 4 个为负（ARC-C -0.005, ARC-E -0.007, HellaSwag -0.005, WinoGrande -0.008），sign-test p≈0.19\n- PPL 改善可能仅反映 distribution matching（训练数据更接近 human-only 评估集），而非真正的模型质量提升\n- Abstract/Introduction framing 给出比实际证据更强的印象\n\n**C3. \"Competitive with grid-best\" 的 framing 与统计证据不一致** [R1 raised, R2 AGREE; 共识]\n- 95% CI [-0.039, 0.101] 包含 0.101 PPL 的降级（upper bound 是 effect size 的 2.3x）\n- Abstract 将 gap (0.031) 与 cross-seed variance (±0.033) 做比较，但这是两个不同统计量（paired variability vs. marginal variability）\n- N=3 下 CI 过宽是 power 不足的结果，不是等价性的证明\n- §5.1 的 \"we refrain from claiming statistical indistinguishability\" 是正确的审慎态度，但 Abstract 和 Conclusion 的措辞与此矛盾\n\n**C4. 1.7B \"transfers without degradation\" claim 缺乏统计支撑** [R1 raised, R2 AGREE; 共识]\n- 2 seeds adaptive (13.25, 13.27) vs. 1 seed uniform (13.26)\n- Δ = -0.01 在任何标准下都无法区分 noise 和 signal\n- §5.2 的 \"confirming\" 用词过强\n- 效应量从 0.6B 到 1.7B 缩小 4x，equally consistent with \"no effect at this scale\"\n\n**C5. 自污染实验设计严重限制泛化性** [R2 raised as critical, R1 AGREE; 共识]\n- Self-contamination (generator=trainee) 是最容易检测的场景，不是论文声称的 \"challenging detection scenario\"\n- TF-IDF+LR 在此场景下达到 AUC=0.94 恰好证明了检测的容易性\n- 真实 web 污染的关键挑战（多源异构、非均匀混合）在 uniform random mixing 设计中完全缺失\n- Limitations section **没有**将 self-contamination 作为独立限制讨论\n- Cross-model 结果 (Appendix H) 单 seed、mixed results、缺少 PPL（\"checkpoints not retained\"）\n\n### Warning（影响评分但不一票否决）\n\n**W1. B=4 下 α_eff 仅 5 个离散值，与 \"连续优化\" 叙事不一致** [R1: critical N4; R2: should-fix W6; 严重程度分歧]\n- B=4 时 α_eff ∈ {0, 0.25, 0.5, 0.75, 1.0}，bisection 在阶梯函数上运行\n- Pearson r≈0.70（51% 方差未解释），MAE=0.114\n- R2 反驳严重程度：bisection 仍正确（效率非正确性问题）；B=8/16 验证 PPL <0.01 差异\n- 共识：substance 成立，但方法描述与实际操作之间存在失配，需在§3.3 承认\n\n**W2. \"Robust defaults\" 声明验证不足** [共识]\n- τ sweep 基于 seed 42, ρ=0.4 单次实验\n- ρ=0.6 时 optimal τ shift 到 0.7（Figure 3）\n- \"empirically robust defaults that transfer without per-model tuning\" 仅在 1 个模型、2 个 ρ 值上验证\n- 建议弱化为 \"default values that perform well in the tested configurations\"\n\n**W3. Grid search 在 ρ=0.6 为单 seed** [共识]\n- Table 5: Grid b=0.3 at ρ=0.6 仅 seed 42 (17.634)\n- Adaptive 3-seed mean 17.736 vs Grid 单 seed，gap 0.102 不具可比性\n- §5.2 \"gap widens from 0.013 to 0.106\" 叙述不可靠\n\n**W4. \"D&R\" 缩写在 Abstract/Introduction 中未定义** [共识]\n- Abstract line 9, Introduction contribution #2 直接使用，全称首次出现在 §4\n\n**W5. 下游评估不充分** [共识]\n- 5 benchmarks, single seed, 4/5 negative Δ\n- 放在 Appendix 而非正文，且 caption 称 \"preserves downstream performance\"（over-positive interpretation）\n- 建议纳入正文并诚实讨论 PPL-downstream 脱节\n\n**W6. p<0.01 (N=3) 需要附带 caveats** [共识]\n- 2 df, t 分布尾部极厚，正态性假设不可验证\n- 建议报告 exact paired differences，注明 sample size 限制\n\n**W7. 缺少近期重要相关工作** [R2 raised, R1 AGREE with caveat]\n- R2 识别 3 篇未引用论文：Kang et al. (EMNLP 2025), Zhang et al. (2025 ForTIFAI), Yi et al. (2025)\n- R1 无法独立验证存在性但原则同意应覆盖\n- 当前 41 条引用偏少\n\n**W8. Scale mismatch: Introduction 框架 web-scale 但实验 132M tokens** [共识]\n- Introduction 以 \"Web corpora increasingly contain machine-generated text\" 开头\n- 实验规模与 web-scale 差 4 个数量级\n- 建议 Introduction 明确限定为 \"continued pretraining on moderate-scale corpora\"\n\n**W9. \"Minimum intervention\" 缺乏最优性证明** [R1 raised, R2 partially rebuts]\n- 选择 b*=b_τ (minimum) 而非中间值是设计直觉\n- R2 反驳：ESS-only ablation (maximum) 已显示退化，minimum > maximum 已建立\n- 但 (b_τ+b_ESS)/2 等中间策略未测试\n- 共识：应标注为 \"empirically motivated strategy\"，不暗示最优性\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer **完全一致**（[AGREE]）：\n\n1. 效应量过小（0.043 PPL, 0.24%），下游 4/5 为负，PPL 改善可能是 distribution matching artifact\n2. 1.7B claim 统计不支撑（2 seeds vs 1 seed, Δ=-0.01）\n3. \"Competitive\" framing 与 CI [-0.039, 0.101] 矛盾\n4. 新颖性不足以支撑 Main Conference（同一公式，不同 b 选择）\n5. 自污染设计限制泛化性，Limitations 未充分讨论\n6. \"Robust defaults\" 验证不足\n7. Grid ρ=0.6 单 seed 比较不可靠\n8. 下游评估不充分\n9. D&R 缩写未定义\n10. p<0.01 (N=3) 需要 caveats\n11. 分析性发现（epoch confound, detector type）比方法本身更有价值\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 分析 |\n|------|----|----|------|\n| B=4 离散化严重程度 | Critical (N4) | Should-Fix (W6) | R2 认为正确性不受影响，B=8/16 已验证。Director 判断：Should-Fix 更合理，离散化不影响算法正确性 |\n| Epoch-matched LR confound | Should-Fix (W3) | REBUT（方向有利） | R2 认为 schedule 差异的方向对论文结论有利而非不利。Director 判断：R2 分析合理，但应在论文中简要讨论 |\n| Minimum intervention 最优性 | Should-Fix (W6) | REBUT（ablation 已足够） | R2 认为 min > max 已通过 ESS-only ablation 建立。Director 判断：中间策略未测试是 completeness gap，但不构成 soundness 问题 |\n| Overall 评分 | 2.5/5 (Borderline Findings) | 3.0/5 (Findings) | R1 对效应量权重更大。Director 综合判断见下 |\n\n---\n\n## Questions（需要作者澄清）\n\n1. 如果 PPL 改善仅反映 distribution matching（训练数据更接近 human-only 评估集），方法的核心 value proposition 是什么？\n2. 在 B=4 的阶梯函数上，per-batch adaptation 的实际机制是什么？是 α_eff 的精确值驱动了 b* 的选择，还是其他因素（如 batch-level contamination composition 的变异性）？\n3. 论文 Conclusion 承认 \"primary value lies in the 0.6B continued pretraining regime\"——如果方法不 scale，它的 target audience 是谁？\n4. Midpoint 策略 b* = (b_τ + b_ESS)/2 是否测试过？如果 minimum 是唯一测试的 feasible region 内策略，\"minimum intervention\" 的 claim 缺乏对照\n5. Self-contamination 设计下 AUC=0.94 是否代表了真实 web 污染场景下的检测器性能？如果真实场景 AUC 显著更低，α_eff proxy 的可靠性如何？\n\n---\n\n## Missing References（R2 识别，R1 原则同意）\n\n| 论文 | 为什么相关 |\n|------|-----------|\n| Kang et al. (EMNLP 2025) \"Demystifying Synthetic Data in LLM Pre-training\" | 大规模 synthetic data mixing 研究（>1000 LLMs），直接相关 |\n| Zhang et al. (2025) \"ForTIFAI\" (arXiv:2509.08972) | 不依赖检测器的 model collapse prevention（Truncated CE loss），替代方案 |\n| Yi et al. (2025) \"Escaping Model Collapse via Synthetic Data Verification\" (arXiv:2510.16657) | Verifier-guided retraining 理论分析，与 α_eff 动机相关 |\n\n注：R1 无法独立验证这些论文的存在性，建议 Research Director 核实后决定是否引用。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。项目配置中无 `external_review.paperreview_ai.enabled` 字段。\n\n---\n\n## Overall Assessment\n\n**Overall Score: Weak Reject (for Main Conference) / Borderline Accept (for Findings)**\n\n**评分依据:**\n- R1: 2.5/5 (Borderline Findings)\n- R2: 3.0/5 (Findings)\n- Director 综合: **Weak Reject for Main Conference, potential Findings-level accept**\n\n**核心判断:**\n\n论文技术执行干净、写作诚实，但存在两个根本性问题：\n\n1. **新颖性不足以支撑 Main Conference**。核心方法对 Drayson et al. (2025) 的增量有限——同一公式，不同的 b 选择策略。双约束框架虽优雅，但各组件（α_eff 约束、ESS 约束、bisection）均来自已有工具的组合。\n\n2. **实验证据系统性地弱于 claims**。效应量极小（0.043 PPL, 0.24%），下游 4/5 为负，1.7B 无 measurable advantage，CI 包含 substantial degradation。论文在 Limitations 和 Conclusion 中审慎表述，但 Abstract 和 Introduction 的 framing 过度乐观。\n\n**论文最有价值的部分是两个分析性发现**：(1) D&R 优势完全来自多 epoch 暴露（Table 2）；(2) 检测器 signal type 而非 AUC 决定 reweighting 有效性。这些发现有独立社区价值，但在当前 framing 中被方法论述遮盖。\n\n**建议投稿路径:**\n- **Findings track**: 重新 frame 为 analytical study（epoch confound + detector type 为主要贡献，method 为实用工具），补充下游评估和统计 caveats 后，Findings 级别可行\n- **Main Conference**: 需要显著增强实验证据（更多 seeds、更大规模、下游转化、cross-generator 验证）或提出本质不同的方法创新\n\n**置信度**: 4/5（两位 Reviewer 在关键问题上独立达成高度一致，增强了判断的可信度）\n\n---\n\n## Detailed Comments\n\n### Abstract (sections/abstract.tex)\n- \"eliminating the need for exhaustive search (nine runs to one; 95% CI of gap [−0.039, 0.101], which includes possible degradation)\" — 后半句削弱前半句的 claim，造成 Abstract 内部信息矛盾。建议选择一个一致的 framing [R1]\n- \"D&R's full-length advantage\" — D&R 缩写未定义 [共识]\n- 字数偏多（约 280 words），数据堆砌过多，建议精简到 ≤250 words [R3-W2 延续]\n\n### Introduction (sections/introduction.tex)\n- Line 1 \"Web corpora increasingly contain machine-generated text\" 开启 web-scale framing，但实验仅 132M tokens / 0.6B。建议明确 scope 为 continued pretraining [共识]\n- Contribution list 将方法置于 #1，分析发现置于 #2 和 #3。建议颠倒优先级，以 analytical contributions 为主 [共识]\n- \"D&R's reported advantage\" (contribution #2) — 缩写未定义 [共识]\n\n### Method (sections/method.tex)\n- §3.2 Proposition 1 proof sketch: \"better-than-random discrimination\" 条件对 Cov ≥ 0 是冗余的（given r_i = 1[q_i ≤ 0.5]，covariance non-negativity is by construction）[R3-W8 延续]\n- §3.3 \"we compute b* at the micro-batch level (B=4)\" — 应明确承认 B=4 下 α_eff 仅 5 个离散值，bisection 退化为离散 lookup [R1-N4 / R2-W6]\n- §3.4 \"empirically robust defaults\" — 验证不足，建议弱化表述 [共识]\n\n### Experiments (sections/experiments.tex)\n- \"creates a challenging detection scenario\" — 实际上 self-contamination 下 AUC=0.94 证明这不 challenging。建议移除或改述 [R1 交叉回应]\n\n### Results (sections/results.tex)\n- §5.1 \"competitive with grid-best\" 与后文 CI caveat 矛盾 [共识]\n- §5.1 downstream 结果不在正文——4/5 negative 的 pattern 应在正文讨论 [R1-N1]\n- §5.2 \"confirming that the method transfers to larger scale without degradation\" — 2 seeds 不足以 \"confirm\"，改为 \"preliminary evidence suggests\" [共识]\n- §5.2 ρ=0.6 Grid 比较为单 seed，\"gap widens\" 叙述不可靠 [共识]\n\n### Discussion (sections/discussion.tex)\n- \"the selected exponent is 4.9× lower than the ESS-only upper bound\" — 有价值但本节整体仍偏薄\n- 缺少 PPL-downstream divergence 的讨论 [R1-N1]\n\n### Limitations (sections/limitations.tex)\n- 缺少 self-contamination 设计作为独立限制的讨论 [共识]\n- \"Cross-model transfer\" 段落讨论 Llama-3.2-3B 但这是 cross-generator transfer，不是 self-contamination 限制\n\n### References (references.bib)\n- wang2026survive (arXiv:2602.16065): 2026 年 2 月 arXiv，需验证存在性 [R2]\n- 可能缺少 3 篇近期相关工作 [R2-W4]\n- 总数 41 条偏少 [共识]\n\n### Appendix (sections/appendix.tex)\n- Detector details (Appendix J) 现在完整 [resolved]\n- Cross-model table (Appendix H, Table 10) 存在但 single seed + no PPL [R3-M4]",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject",
    "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-19T06:07:57.145969+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2b6c9bea33a70c93bf4bf04ac36b8df9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4287
}
```

</details>

---


### Assistant

_source line 282 · 2026-05-19T06:08:06.484484+00:00_

审稿报告已投递给 Research Director。

---

**圆桌审稿完成总结：**

- **Overall Score**: Weak Reject (Main Conference) / Borderline Accept (Findings)
- **R1**: 2.5/5 | **R2**: 3.0/5
- **收敛**: 1 轮收敛，关键问题全部达成共识，3 处轻微严重程度分歧

**5 个 Critical 问题**（共识）：
1. 新颖性不足——同一公式 w=(1-q)^b，仅 b 选择方式不同
2. 效应量极小（0.043 PPL），下游 4/5 为负，可能是 distribution matching
3. "Competitive" framing 与 CI [-0.039, 0.101] 矛盾
4. 1.7B claim 仅 2 seeds，不足以支撑
5. 自污染设计限制泛化性

**核心建议**：论文最有价值的部分是两个 corrective findings（D&R epoch confound + detector type effect），而非方法本身。重新 frame 为 analytical study 投 Findings track 是最可行的路径。

Issue Tracker 已同步更新至 `artifacts/review_issues.yaml`（Round 4）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 26

## Round 26

130 recorded events


### User

_source line 283 · 2026-05-19T07:09:46.071242+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: provenance_weight_training
- 论文路径: projects/provenance_weight_training/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2025 - Findings
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-19T07:09:52.669989+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-19T07:09:52.771481+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-19T07:10:00.707806+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-19T07:10:00.758550+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-19T07:10:04.230816+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 289 · 2026-05-19T07:10:05.085412+00:00_

{"result":"# 项目 provenance_weight_training 概况\n\n## 实验状态 (175 个)\n\n- **adaptive_seed42**: DONE (success) — \n- **uniform_seed456**: DONE (success) — \n- **uniform_seed123**: DONE (success) — \n- **uniform_seed42**: DONE (success) — \n- **detector_modernbert**: DONE (killed) — \n- **nmin1_seed42**: DONE (success) — \n- **golden_ratio_seed42**: DONE (success) — \n- **tau_0.6_seed42**: DONE (killed) — \n- **grid_b_low_seed42**: DONE (failed) — \n- **grid_b1_5_seed456**: DONE (success) — \n- **grid_b1_0_seed456**: DONE (success) — \n- **grid_b0_5_seed456**: DONE (success) — \n- **grid_b_seed42_batch**: DONE (success) — \n- **diagnostic_contamination100**: DONE (killed) — \n- **detector_tfidf_lr**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- eval_q04（准备中）\n- eval_q06（准备中）\n- eval_q03_r2（准备中）\n- adaptive_1_7b_planb_control（准备中）\n- eval_q01_final_v2（准备中）\n- eval_q01_final（准备中）\n- eval_ngram_uniform（准备中）\n- eval_ngram_adaptive（准备中）\n- status_check_41312（准备中）\n- eval_adaptive_1_7b（准备中）\n- …另有 14 项\n\n## 近期结论\n- **uniform_1_7b_seed123** (negative): From-scratch uniform baseline at 1.7B scale with seed123, paired with adaptive_1_7b_seed123, to provide unconfounded comparison (unlike seed42 Plan B which had optimizer resume artifact)\n  [uniform_1_7b_seed123_analysis](/api/workspace-files/projects/provenance_weight_training/artifacts/uniform_1_7b_seed123/report/analysis_d8d0e9.md)\n- **detect_remove_q07_epoch_matched_seed42** (success): Epoch-matched D&R q07: 1 epoch through q07 filtered data (184,908 samples, ~100M tokens, 3047 steps). Part of 5-point epoch-matched curve (q01/q03/q05/q07/q09). If PPL converges to ~17.65-17.74 range like q03(17.74) and q05(17.65), confirms U-shape sweet spot is entirely multi-epoch artifact across the full threshold range.\n  [diagnose_q07_epoch_matched](/api/workspace-files/projects/provenance_weight_training/artifacts/detect_remove_q07_epoch_matched_seed42/report/dia
…[truncated 1800 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 290 · 2026-05-19T07:10:05.438043+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-19T07:10:05.488658+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-19T07:10:12.318286+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 293 · 2026-05-19T07:10:12.770545+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\graphicspath{{../../artifacts/figures/}}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{algorithm}
14	\usepackage{algorithmic}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{hyperref}
20	
21	\newtheorem{proposition}{Proposition}
22	\newtheorem{definition}{Definition}
23	
24	\newcommand{\bstar}{b^*}
25	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
26	\newcommand{\nmin}{n_{\min}}
27	\newcommand{\btau}{b_{\tau}}
28	\newcommand{\bess}{b_{\mathrm{ESS}}}
29	
30	\title{When Does Detect-and-Reweight Work? Epoch Confounds\\and Adaptive Reweighting in LM Pretraining}
31	
32	\author{Anonymous}
33	
34	\begin{document}
35	\maketitle
36	
37	\begin{abstract}
38	\input{sections/abstract}
39	\end{abstract}
40	
41	\section{Introduction}
42	\label{sec:intro}
43	\input{sections/introduction}
44	
45	\section{Related Work}
46	\label{sec:related}
47	\input{sections/related_work}
48	
49	\section{Method}
50	\label{sec:method}
51	\input{sections/method}
52	
53	\section{Experimental Setup}
54	\label{sec:experiments}
55	\input{sections/experiments}
56	
57	\section{Results}
58	\label{sec:results}
59	\input{sections/results}
60	
61	\section{Discussion}
62	\label{sec:discussion}
63	\input{sections/discussion}
64	
65	\section{Conclusion}
66	\label{sec:conclusion}
67	\input{sections/conclusion}
68	
69	\section*{Limitations}
70	\label{sec:limitations}
71	\input{sections/limitations}
72	
73	\input{sections/checklist}
74	
75	\bibliography{references}
76	
77	\appendix
78	\input{sections/appendix}
79	
80	\end{document}
81	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-19T07:10:12.770930+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-19T07:10:12.771147+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-19T07:10:13.724884+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-19T07:10:13.825670+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'provenance_weight_training'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-19T07:10:19.021890+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR May 2025 submission guidelines author instructions page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR May 2025 submission guidelines author instructions page limit"
  }
}
```

</details>

---


### Tool call

_source line 299 · 2026-05-19T07:10:19.374073+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline commitment"
  }
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-19T07:10:20.378082+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-19T07:10:20.378499+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-19T07:10:20.629752+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "literature_map.yaml",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "literature_map.yaml",
    "max_chars": "6000"
  }
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-19T07:10:25.246259+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"}]

…[truncated 1111 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 5872
}
```

</details>

---


### Tool result

_source line 304 · 2026-05-19T07:10:25.699128+00:00_

Web search results for query: "ACL Rolling Review ARR May 2025 submission guidelines author instructions page limit"

Links: [{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.06751v2"}]

I found comprehensive information about ACL Rolling Review submission guidelines for May 2025. Here's what the search results show:

## Page Limits

The paper must follow page limits of 8 pages for long papers and 4 pages for short papers, not including limitations and ethical considerations.

## Submission Guidelines and Author Instructions

All long, short, and theme papers must follow the ACL Author Guidelines. Starting in May 2025, all submitting authors have to also sign up as reviewers with a deadline of 48 hours after the submission deadline.

## Limitations Section

Authors are required to d
…[truncated 712 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 6677
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-19T07:10:25.699940+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/literature_map.yaml\", \"content\": \"# Literature Map for provenance_weight_training\\n# 研究方向：基于收敛理论的自适应污染重加权\\n# 核心公式：w=(1-q)^b，q 为检测器合成概率，b* 为理论最优权重指数\\n# 更新日期：2026-05-16（文献验证：新增 6 篇 high-priority 论文，全部经 arXiv/venue 交叉验证）\\n\\n# ============================================================\\n# Category: direct-competitor\\n# 同主题/同方法的论文\\n# ============================================================\\n\\n- id: drayson_2025_detection_collapse\\n  title: \\\"Machine-Generated Text Detection Prevents Language Model Collapse\\\"\\n  authors: \\\"George Drayson, Emine Yilmaz, Vasileios Lampos\\\"\\n  venue: \\\"EMNLP 2025\\\"\\n  year: 2025\\n  arxiv_id: \\\"2502.15654\\\"\\n  url: \\\"https://arxiv.org/abs/2502.15654\\\"\\n  github: \\\"https://github.com/GeorgeDrayson/model_collapse\\\"\\n  category: direct-competitor\\n  role: \\\"使用同一公式 w=(1-q)^b 进行重加权，但 b 为验证集 empirical 选取，训练中固定\\\"\\n  method_summary: >\\n    Detect-and-reweight 防止递归训练 model collapse。检测器为 ModernBERT 150M\\n    (MAGE fine-tune, in-domain AUC=0.986, OOD AUC=0.943)。权重公式 wⱼ=(1-q(xⱼ))^b / Σₗ(1-q(xₗ))^b，\\n    通过 SIR 按权重重采样训练数据。b 通过 WikiText-2 验证集上 1 代递归训练后评估选取\\n    (GPT-2/SmolLM 135M/360M 用 b=10, SmolLM 1.7B 用 b=1)，训练全程固定。\\n    实验覆盖 4 个模型 (GPT-2 124M, SmolLM 135M/360M/1.7B)、10 代递归训练、6 种解码策略。\\n    结果 PPL 降低 0.85%–25.65%，diversity 提升 3.44%–14.62%。\\n  key_findings: \\\"验证 detect-and-reweight 有效防止 model collapse 且优于纯人类数据训练；b 值对模型规模敏感（小模型 b=10，大模型 b=1）\\\"\\n  differentiation:\\n    b_selection: \\\"Drayson: 验证集 empirical grid search, per-model 固定 | 我们: α_eff(b) + ESS 约束, per-batch 自适应\\\"\\n    contamination_setting: \\\"Drayson: 不假设已知比例（原文明确声明），但实验为控制设置 | 我们: 未知比例（batch 统计量在线估计）\\\"\\n    detector: \\\"Drayson: ModernBERT 150M (AUC=0.986) | 我们: TF-IDF+LR (AUC=0.939)，证明轻量检测器即可\\\"\\n    theory: \\\"Drayson: 无 b 选取理论（SIR 启发式） | 我们: 收敛理论 motivated α_eff(b) 推导\\\"\\n 
…[truncated 4900 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5070
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-19T07:10:33.731335+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-19T07:10:34.384412+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-19T07:10:34.435180+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-19T07:10:34.486026+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/decisions.yaml\", \"content\": \"_next_id: 93\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:38 UTC\\n  summary: 投稿目标定为 AAAI 2027 (~Aug 2026)，放弃 EMNLP 2026 ARR May 25\\n  rationale: EMNLP ARR 仅剩 12 天且无任何基础设施，即使 AI 团队速度也无法完成多轮预训练实验。AAAI 2027 有 ~11 周，足够完成\\n    4 phase 全流程。两者均为 A 类会议。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:38 UTC\\n  summary: 'MVP 设计: 单模型(Qwen3-0.6B) + 单污染比例(40%) + 三组对比(uniform/grid-b/adaptive-b*)'\\n  rationale: 核心假设是 adaptive b* 能替代 grid search。最小验证只需一个污染比例下的 A/B/C 对比。40% 选取因为理论和\\n    Strong Model Collapse 均表明该区间效应显著。通过后再扩展到多污染比例/多生成器/多模型。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-13 17:40 UTC\\n  summary: '修正 D001: 主攻 EMNLP 2026 ARR May 25，AAAI 2027 为后备'\\n  rationale: 用户明确指出 EMNLP ARR 5/25 时间不紧、资源会给够。AI 团队 24/7 执行 + 4 卡并行：数据生成 ~2 天、MVP\\n    ~1 天、全矩阵 ~3 天、论文 ~3 天、迭代 ~2 天 = 11 天可完成。12 天 deadline 可行。保守估计完成时间是最大风险。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-13 17:42 UTC\\n  summary: '采纳 Reviewer 4 点 MVP 协议补全: 3 seeds、detector gate、grid-b 定义、kill criteria'\\n  rationale: 'Reviewer 指出 MVP 设计 4 个缺口均合理: (1) 单 seed 无统计保障 → 3 seeds，缩 tokens 到 200M\\n    控预算; (2) 检测器质量是 pipeline 前提 → 加 gate AUC≥0.95/ECE≤0.05; (3) grid search baseline\\n    需可复现 → 定义 b∈{0.5,1,1.5,2,3,5}; (4) 无 fail 路径 → 定义三级 kill/pivot。不增加工程量，只补协议。'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D005\\n  date: 2026-05-13 22:08 UTC\\n  summary: 识别 q-score 极化风险：AUC=0.999998 可能导致 adaptive b* vs grid-b 对比退化，制定分级应对方案\\n  rationale: 'Reviewer 审查发现 detector eval_auc=0.999998（step 2000），q-score 可能高度双峰化。若校准后\\n    >95% 样本 q<0.05 或 q>0.95，则 w=(1-q)^b 对所有 b>0 约等于 0，不同 b 值间无区分度。MVP 技术上可能 PASS（adaptive\\n    ≈ grid-b，满足 ≥90% 条件），但无法证明核心贡献（自适应精细调优的价值）。\\n\\n\\n    应对方案（detector 完成后按 q-score 分布分级执行）：\\n\\n    - 分布有spread（q 在 0.1
…[truncated 1474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-19T07:10:40.208537+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-19T07:10:40.560282+00:00_

1	Detect-and-reweight methods suppress likely-synthetic samples during pretraining via $w(x) = (1-q(x))^b$, where $q(x)$ is a detector's synthetic probability.
2	Two questions are open: does hard filtering (Detect and Remove, D\&R) outperform soft reweighting, and how should $b$ be set without per-model grid search?
3	
4	We address both through controlled experiments on Qwen3-0.6B continued pretraining (132M FineWeb tokens, 40\% synthetic contamination, 3 seeds).
5	First, D\&R's reported advantage is entirely a multi-epoch artifact: at equal content epochs, reweighting and D\&R differ by only 0.006 PPL ($N{=}3$).
6	Second, a dual-constrained adaptive exponent $b^*$ that selects the minimum $b$ satisfying a quality floor ($\alpha_{\mathrm{eff}}(b) \geq \tau$) and stability ceiling ($\mathrm{ESS}(b) \geq n_{\min}$) consistently improves over uniform weighting ($\Delta{=}{-}0.043$, $p{<}0.003$) and over maximizing $b$ to the ESS limit; adaptive $b^*$ performs comparably to grid-best in our experiments ($N{=}3$, 95\% CI of the gap includes possible degradation up to 0.10 PPL).
7	Third, detector signal type matters more than discrimination accuracy: two generative detectors (AUC up to 0.91) both reverse the advantage that a discriminative classifier (AUC\,=\,0.94) provides.
8	
9	The method fails at low contamination ($\rho{=}0.2$), establishing a clear applicability boundary.
10	These findings inform practical choices for contamination-aware continued pretraining.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-19T07:10:40.711275+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-19T07:10:41.012912+00:00_

1	The detect-and-reweight paradigm~\citep{drayson2025detection} has emerged as a response to synthetic contamination in web corpora, now estimated at 20--60\% of crawled data~\citep{cheng2025contamination}.
2	Training on such data risks model collapse~\citep{shumailov2024model,dohmatob2025strong}, motivating methods that downweight likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a detector's synthetic probability.
3	An alternative, Detect and Remove (D\&R), hard-filters samples above a threshold~\citep{feng2025beyond}.
4	
5	Despite growing adoption, fundamental questions remain.
6	Does D\&R genuinely outperform soft reweighting, or do published comparisons confound filtering quality with multi-epoch exposure?
7	How should $b$ be chosen, given that \citet{drayson2025detection} find optimal values vary from $b{=}10$ (GPT-2 124M) to $b{=}1$ (SmolLM 1.7B), requiring costly grid search?
8	What detector properties are necessary for effective reweighting?
9	
10	We address these through controlled experiments on Qwen3-0.6B continued pretraining (132M FineWeb tokens, $\rho{=}0.4$, 3 seeds), with extensions to $\rho \in \{0.2, 0.6\}$ and 1.7B parameters.
11	This scope, continued pretraining on moderate-scale corpora with known contamination~\citep{gururangan2020dont}, does not address from-scratch pretraining at web scale.
12	We formulate adaptive exponent selection as a dual-constrained problem: find the minimum $b$ such that the weighted effective real proportion $\alpha_{\mathrm{eff}}(b) \geq \tau$ (quality floor, motivated by convergence theory~\citep{wang2026survive}), subject to Kish's effective sample size $\mathrm{ESS}(b) \geq n_{\min}$ (stability ceiling)~\citep{kish1965survey,vehtari2024psis}.
13	
14	Our contributions:
15	\begin{itemize}[nosep,leftmargin=*]
16	\item \textbf{Epoch confound in D\&R comparisons.}
17	D\&R at its post-hoc best threshold achieves PPL 17.250 at full training length.
18	Epoch-matched controls ($N{=}3$) that equalize cont
…[truncated 1437 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-19T07:10:41.013518+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-19T07:10:41.515920+00:00_

1	\subsection{Problem Setup}
2	\label{sec:setup}
3	
4	Let $\mathcal{D} = \mathcal{D}_{\mathrm{real}} \cup \mathcal{D}_{\mathrm{synth}}$ denote a pretraining corpus containing both human-authored and machine-generated text.
5	The contamination ratio $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$ is unknown, a realistic assumption for web-scale corpora where synthetic content enters from diverse, uncoordinated sources~\citep{cheng2025contamination}.
6	
7	A pre-trained detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$.
8	Following \citet{drayson2025detection}, we weight each sample as
9	\begin{equation}
10	  w(x) = (1 - q(x))^{b},
11	  \label{eq:weight}
12	\end{equation}
13	where $b \geq 0$ controls downweighting intensity: $b = 0$ recovers uniform training, while larger $b$ progressively suppresses high-$q$ samples.
14	\citet{drayson2025detection} select $b$ via validation-set grid search, obtaining different optimal values for different model scales ($b{=}10$ for ${\leq}360$M parameters, $b{=}1$ for 1.7B).
15	We instead derive $b$ per-batch from the batch's own $q$-score distribution, requiring no held-out validation data.
16	
17	\subsection{Dual-Constraint Framework}
18	\label{sec:dual}
19	
20	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with detector scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$, we define two batch-level diagnostics that jointly determine $b$.
21	
22	\paragraph{Effective real proportion.}
23	Let $r_i = \mathbf{1}[q_i \leq 0.5]$ estimate whether sample $x_i$ is human-authored.
24	The \emph{effective real proportion}
25	\begin{equation}
26	  \alpha_{\mathrm{eff}}(b) = \frac{\sum_{i=1}^{B} w_i(b) \cdot r_i}{\sum_{i=1}^{B} w_i(b)}
27	  \label{eq:alpha}
28	\end{equation}
29	measures the share of total weight allocated to likely-real samples.
30	The indicator $r_i = \mathbf{1}[q_i \leq 0.5]$ is a proxy for true provenance: $\alpha_{\mathrm{eff}}$ tracks the detector's estimate of the real fraction, not
…[truncated 9233 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-19T07:10:41.616681+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-19T07:10:42.420178+00:00_

1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo2024fineweb} as the real-data source, comparable to typical domain-adaptive continued pretraining budgets~\citep{gururangan2020dont}.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang2025qwen3}, the same architecture used for continued pretraining, and inject them at token-level ratio $\rho = 0.4$ via uniform random mixing.\footnote{$\rho$ denotes the token-level contamination ratio. Because synthetic documents are shorter on average (304 vs.\ 560 words), the document-level synthetic fraction is 55.6\% at $\rho{=}0.4$.}
4	This self-contamination design means generator and trainee share the same distribution; implications for detection difficulty are discussed in \S\ref{sec:limitations}.
5	
6	\paragraph{Detector.}
7	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split (AUC\,=\,0.939, calibrated ECE\,=\,0.048 after temperature scaling with $T = 0.204$).
8	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
9	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson2025detection}) to test whether score \emph{calibration} may matter as much as raw discrimination for reweighting.
10	To evaluate detector sensitivity, we additionally test two generative baselines: a GPT-2-based perplexity scorer (AUC\,=\,0.913) and an N-gram language model perplexity scorer (AUC\,=\,0.73); results are reported in \S\ref{sec:robustness}.
11	
12	\paragraph{Training.}
13	We continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\,=\,$5{\times}10^{-5}$), max sequence length 2048, and bf16 precision.
14	All main comparisons use three random seeds (42, 123, 456)
…[truncated 1547 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-19T07:10:42.420542+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-19T07:10:42.872504+00:00_

1	\subsection{Main Results}
2	\label{sec:main-results}
3	
4	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across three seeds.
5	Continued pretraining reduces PPL from 22.970 (pretrained checkpoint) to the 17.3--17.8 range; the initial 5.2-point drop absorbs the bulk of easy gains, and reweighting method comparisons operate within a narrow residual.
6	
7	Adaptive $\bstar$ achieves 3-seed mean PPL 17.651, compared to 17.620 for grid $b{=}0.3$ (gap 0.031, 95\% CI $[-0.039, 0.101]$, which includes possible degradation).
8	With only $N{=}3$ seeds (2 degrees of freedom), normality of paired differences cannot be verified; we report exact per-seed gaps: 0.010, 0.064, 0.020.
9	The practical value is reducing search cost from nine full training runs to one~\citep{drayson2025detection}, with lower cross-seed variance ($\pm$0.007 vs.\ $\pm$0.033).
10	The grid-best $b{=}0.3$ is a post-hoc oracle selected after observing all nine candidates; in practice, validation-based selection from the same grid would yield worse results due to the noisy PPL plateau at $b \in [0.1, 0.5]$ (Figure~\ref{fig:grid_b_trend}).
11	Using the mean of per-batch $\bstar$ ($\bar{b}^*{=}1.19$) as a fixed exponent yields PPL 17.693, comparable to uniform (17.694); per-batch adaptation is essential.
12	
13	The ablation hierarchy at $\rho{=}0.4$ (Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random, Table~\ref{tab:main}) reveals two requirements for effective reweighting: detector signal and minimum intervention.
14	Random weights $\mathcal{U}(0,2)$ (mean 17.803) perform worse than uniform (17.694): the detector's $q$-scores carry genuine provenance information, and uninformed reweighting increases gradient variance without corrective signal.
15	ESS-only (mean $17.737 {\pm} 0.007$) uses $q$-scores but maximizes $b$ up to the stability ceiling, concentrating weights on a few high-confidence samples; it provides no improvement over uniform.
16	Only the dual-constrained adaptive method, which l
…[truncated 8746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-19T07:10:43.023472+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-19T07:10:43.375156+00:00_

1	\paragraph{Why minimum intervention works.}
2	The $\aeff$ quality constraint prevents 4.9$\times$ over-aggressive downweighting in 38.2\% of batches (\S\ref{sec:regime}), robust across contamination levels (33.4\% at $\rho{=}0.6$) and seeds (CV ${<}2\%$).
3	Using the aggregate mean $\bstar \approx 1.4$ as a fixed exponent yields PPL comparable to uniform (17.693 vs.\ 17.694), confirming per-batch adaptation is essential.
4	
5	\paragraph{Failure modes and applicability boundary.}
6	At $\rho{=}0.2$, the method degrades by $+$0.046 PPL (Appendix~\ref{app:rho02}): the detector's mean $q$-score drops to 0.393, yet $\aeff$-binding rises to 60.1\%, so the method actively intervenes on unreliable signal.
7	The same failure appears with generative detectors (GPT-2 PPL: $\Delta{=}{+}0.10$; N-gram PPL: $\Delta{=}{+}0.13$), which conflate predictability with provenance; when $q$-scores do not separate real from synthetic, the framework amplifies detector error.
8	Discriminative signal is required, and the effective range with $\tau{=}0.8$ is $\rho \geq 0.4$.
9	
10	\paragraph{PPL vs.\ downstream divergence.}
11	Downstream benchmarks at 0.6B show 4 of 5 tasks with small negative $\Delta$ ($p{\approx}0.19$, $N{=}5$, single seed); cross-model evaluation (Llama-3.2-3B, single seed) is similarly mixed (Appendix~\ref{app:downstream},~\ref{app:cross_model}).
12	The PPL gain may reflect distribution matching rather than generalizable quality improvement.
13	
14	\paragraph{Soft vs.\ hard filtering.}
15	At equal content epochs, D\&R ($17.657 \pm 0.006$) and adaptive $\bstar$ ($17.651 \pm 0.007$) are equivalent ($\Delta{=}0.006$, $N{=}3$); D\&R's full-length advantage (17.250 at $q{>}0.3$) requires ${\sim}$3.2$\times$ effective compute, and its U-shaped threshold curve is entirely a multi-epoch artifact (Figure~\ref{fig:dr_dual_curve}).
16	
17	\paragraph{$\tau$ and deployment.}
18	$\tau{=}0.8$ is validated at $\rho{=}0.4$ (single-seed sweep) and $\rho{=}0.6$ ($\tau{=}0.7$ is optimal ther
…[truncated 238 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-19T07:10:43.426001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-19T07:10:43.878103+00:00_

1	Our empirical analysis of contamination-aware reweighting in continued pretraining yields three findings.
2	First, D\&R's reported advantage over soft reweighting is entirely attributable to multi-epoch exposure; at equal content epochs ($N{=}3$), the two approaches differ by $\Delta{=}0.006$ PPL (Table~\ref{tab:epoch_match}).
3	Second, dual-constrained exponent selection with minimum intervention outperforms both uniform weighting and the ESS-only alternative ($\rho \in \{0.4, 0.6\}$), with the quality constraint preventing 4.9$\times$ over-aggressive downweighting; the adaptive-to-grid gap (0.031 PPL, 95\% CI $[-0.039, 0.101]$) falls within grid-search's cross-seed variance, reducing search from nine runs to one.
4	Third, detector signal type (discriminative vs.\ generative), not AUC, determines effectiveness.
5	The method fails at $\rho{=}0.2$, and at 1.7B we find no evidence of improvement or degradation ($\Delta{=}{-}0.01$, 2 seeds), suggesting its value lies in moderate-scale continued pretraining.
6	Future work: multi-seed scale experiments, discriminative detector characterization, and evaluation on naturally contaminated corpora. Code and data will be released upon acceptance.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-19T07:10:43.878438+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-19T07:10:44.330614+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy; \citet{dohmatob2024tale} characterize this as a change of scaling laws.
5	\citet{gerstgrasser2024collapse} show that accumulating real data alongside synthetic data can break the recursion, though at substantial collection cost.
6	\citet{kang2025demystifying} systematically study scaling laws for synthetic data in pretraining, finding that rephrased synthetic data mixed with natural text improves data efficiency but textbook-style data degrades loss on many domains.
7	\citet{cheng2025contamination} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\% of web corpora.
8	As language models are deployed at scale for content generation~\citep{radford2019language,brown2020language,openai2023gpt4}, these results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
9	
10	\paragraph{Detection and Filtering of Machine-Generated Text.}
11	Given the severity of contamination, a natural response is to detect and remove synthetic content.
12	DetectGPT~\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature; Fast-DetectGPT~\citep{bao2024fastdetectgpt} accelerates this with conditional probability curvature; Binoculars~\citep{hans2024binoculars} uses cross-perplexity ratios between two models; Min-$k$\% Prob~\
…[truncated 5528 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-19T07:10:44.331053+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-19T07:10:44.732867+00:00_

1	\paragraph{Self-contamination.}
2	All main experiments use self-contamination (generator = trainee), which does not represent realistic web contamination from multiple models and sources.
3	The resulting AUC of 0.94 reflects that self-generated text is relatively easy to detect; real multi-source contamination may yield lower detection accuracy, shifting the operating regime.
4	Cross-model results (Llama-3.2-3B generator, Appendix~\ref{app:cross_model}) are single-seed and lack PPL evaluation, providing insufficient evidence for generalization beyond self-contamination.
5	
6	\paragraph{Scale.}
7	All main experiments use Qwen3-0.6B with batch size 4 on 132--200M tokens, comparable to domain-adaptive continued pretraining but far below full pretraining scale; validation at ${>}$100B tokens remains an important direction.
8	Preliminary evidence at 1.7B (Qwen3-1.7B, $\rho{=}0.4$, 2 seeds) shows $\Delta{=}{-}0.01$ (adaptive 13.26 vs.\ uniform 13.26); with only 2 seeds, this is insufficient for statistical conclusions about scale transfer.
9	
10	\paragraph{Contamination range.}
11	The method improves over uniform at $\rho \in \{0.4, 0.6\}$ but not at $\rho{=}0.2$ ($+$0.046 PPL, 0.26\% relative), indicating an effective range of $\rho \geq 0.4$ with $\tau{=}0.8$.
12	Behavior at $\rho > 0.8$ is untested; extreme contamination may violate the assumption that sufficient real samples exist per batch for meaningful $\aeff$ estimation.
13	Real web-scale contamination is domain-skewed, which may alter within-batch $\aeff$ distributions.
14	
15	\paragraph{Detector coverage.}
16	Three detectors have been tested: TF-IDF+LR (discriminative, AUC\,=\,0.94) succeeds, while GPT-2 perplexity (generative, AUC\,=\,0.91) and N-gram perplexity (generative, AUC\,=\,0.73) both fail.
17	The pattern suggests discriminative signal is necessary, but three detectors from two families cannot distinguish a type effect from a calibration effect; testing additional discriminative detectors at varying 
…[truncated 1534 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-19T07:10:44.733261+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-19T07:10:44.783921+00:00_

1	\section{Proofs}
2	\label{app:proofs}
3	
4	\begin{proposition}[$\alpha_{\mathrm{eff}}$ monotonicity]
5	\label{prop:monotone}
6	$\alpha_{\mathrm{eff}}(b)$ is non-decreasing in $b$, and strictly increasing whenever the batch contains at least one sample with $q_i \in (0,1)$ and $r_i$ is not constant.
7	\end{proposition}
8	
9	\begin{proof}[Proof of Proposition~\ref{prop:monotone}]
10	Let $w_i(b) = (1 - q_i)^b$, $W(b) = \sum_{j=1}^B w_j(b)$, and $\pi_i(b) = w_i(b) / W(b)$.
11	Then
12	\begin{equation*}
13	  \alpha_{\mathrm{eff}}(b) = \sum_{i=1}^{B} \pi_i(b)\, r_i,
14	\end{equation*}
15	where $r_i \in \{0, 1\}$ indicates whether sample $i$ is real.
16	Taking the derivative with respect to $b$:
17	\begin{align*}
18	  \frac{d\pi_i}{db}
19	  &= \pi_i \!\left(\frac{d \ln w_i}{db} - \frac{d \ln W}{db}\right)
20	  = \pi_i \!\left(\ln(1{-}q_i) - \sum_j \pi_j \ln(1{-}q_j)\right).
21	\end{align*}
22	Substituting,
23	\begin{align*}
24	  \frac{d\alpha_{\mathrm{eff}}}{db}
25	  &= \sum_i r_i\, \pi_i \!\left(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\right) \\
26	  &= \mathrm{Cov}_{\pi}\!\bigl(r_i,\, \ln(1{-}q_i)\bigr).
27	\end{align*}
28	By construction, real samples ($r_i = 1$) have $q_i \leq 0.5$ and thus higher $\ln(1{-}q_i)$ than synthetic samples ($r_i = 0$, $q_i > 0.5$).
29	The weighted covariance $\mathrm{Cov}_{\pi}(r_i, \ln(1{-}q_i))$ is therefore non-negative, establishing that $\alpha_{\mathrm{eff}}(b)$ is non-decreasing in $b$.
30	\end{proof}
31	
32	\begin{proposition}[ESS monotonicity]
33	\label{prop:ess_mono}
34	$\mathrm{ESS}(b)$ is non-increasing in $b$, and strictly decreasing whenever the batch contains at least two samples with distinct $q$-values.
35	\end{proposition}
36	
37	\begin{proof}
38	Write $\mathrm{ESS}(b) = 1 / \sum_i \pi_i(b)^2$, where $\pi_i(b) = w_i(b) / W(b)$.
39	The denominator $\sum_i \pi_i^2$ is the Herfindahl index $H$.
40	Differentiating $H$ with respect to $b$:
41	\begin{equation*}
42	  \frac{dH}{db} = 2 \sum_i \pi_i^2 \bigl(\ln(1{-}q_i) - \math
…[truncated 16519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-19T07:10:51.993651+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-19T07:10:52.498013+00:00_

1	% Responsible NLP Research Checklist
2	% https://aclrollingreview.org/responsibleNLPresearch/
3	
4	\section*{Responsible NLP Research Checklist}
5	
6	\subsection*{A. For Every Submission}
7	
8	\begin{itemize}[nosep,leftmargin=*]
9	\item[\checkmark] \textbf{A1.} Did you describe the limitations of your work?
10	\textit{Yes, \S\ref{sec:limitations} discusses scale, contamination range, detector coverage, threshold, evaluation, and effect size limitations.}
11	
12	\item[\checkmark] \textbf{A2.} Did you discuss any potential risks of your work?
13	\textit{Yes. The method assumes a pre-trained detector is available; deploying it with a poorly calibrated detector could degrade training quality (discussed in \S\ref{sec:limitations}, Detector coverage). The method does not generate new content or enable harmful uses beyond standard language model pretraining.}
14	\end{itemize}
15	
16	\subsection*{B. Did You Use or Create Scientific Artifacts?}
17	
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\checkmark] \textbf{B1.} Did you cite the creators of artifacts you used?
20	\textit{Yes. FineWeb~\citep{penedo2024fineweb}, Qwen3~\citep{yang2025qwen3}, and all baseline methods are cited in \S\ref{sec:experiments} and \S\ref{sec:related}.}
21	
22	\item[\checkmark] \textbf{B2.} Did you discuss the license or terms for use and/or distribution of any artifacts?
23	\textit{FineWeb is released under Apache-2.0; Qwen3 under Apache-2.0. Our code and data will be released upon acceptance.}
24	
25	\item[\checkmark] \textbf{B3.} Did you discuss if your use of existing artifacts was consistent with their intended use?
26	\textit{Yes. FineWeb is intended for language model training; we use it as a pretraining corpus. Qwen3 is used for both continued pretraining and synthetic data generation, consistent with its general-purpose design.}
27	
28	\item[\checkmark] \textbf{B4.} Did you discuss the steps taken to check whether the data contains information that names or uniquely identifies individ
…[truncated 3080 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---

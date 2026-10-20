# Director coordination — Part 1 of 8

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Conversation logs

[Transcript overview](../director-coordination-copy-2.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/6d/6ddf598184a3dac569b9.json)

## Round 1

## Round 1

70 recorded events


### User

_source line 1 · 2026-05-18T08:35:26.096687+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: persuasion_turn_jailbreak_detect
- 论文路径: projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: LLM Security / Discourse and Pragmatics
- 截止日期: 2026-05-25
- 补充材料: projects/persuasion_turn_jailbreak_detect/figures/paper/fig1_architecture.pdf, projects/persuasion_turn_jailbreak_detect/figures/paper/fig2_cross_attack_bar.pdf, projects/persuasion_turn_jailbreak_detect/figures/paper/fig3_strategy_heatmap.pdf

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-18T08:35:32.582589+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-18T08:35:32.633888+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-18T08:35:36.151298+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
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

_source line 5 · 2026-05-18T08:35:36.203352+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-18T08:35:41.861299+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-18T08:35:41.937276+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 75
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-18T08:35:44.197840+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-18T08:35:46.156389+00:00_

{"result":"# 项目 persuasion_turn_jailbreak_detect 概况\n\n## 实验状态 (41 个)\n\n- **plan_016_sentiment_control**: PREPARING (failed) — \n- **plan_012_gpt55_judge**: DONE (success) — \n- **plan_015_dd_eval**: DONE (success) — \n- **plan_006_cross_attack_clean**: DONE (success) — \n- **plan_004_perturbation_eval**: DONE (success) — \n- **plan_013_none_collapse**: DONE (success) — \n- **plan_012_llm_judge_qwen**: DONE (success) — \n- **plan_002_clean_training**: DONE (negative) — \n- **plan_003_scrambled_ablation**: DONE (negative) — \n- **cross_attack_baseline**: DONE (negative) — \n- **plan_008_strategy_transition**: DONE (success) — \n- **plan_007_tfidf_fitd_dd**: DONE (success) — \n- **plan_005_multi_attack_gen**: DONE (success) — \n- **phase_b_full**: DONE (success) — \n- **pilot_phase_b**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_003_scrambled_retrain（准备中）\n- plan_018_eval_seed456（准备中）\n- plan_018_eval_seed123（准备中）\n- plan_018_wiki_mlm_seed456（准备中）\n- plan_018_wiki_mlm_seed123（准备中）\n- plan_017_eval_seed456（准备中）\n- plan_017_eval_seed123（准备中）\n- plan_016v2_topic_eval_seed42（准备中）\n- plan_016v2_topic_eval_seed456（准备中）\n- plan_016v2_topic_eval_seed123（准备中）\n- …另有 6 项\n\n## 近期结论\n- **plan_003_scrambled_fix** (negative): If correct persuasion strategy labels are the key mechanism for jailbreak detection, then scrambling these labels (while keeping intent labels intact) should significantly degrade detection performance, especially on OOD data. ← 基于 plan_003_scrambled_perturbation\n- **plan_002_seed456** (success): Reproduce plan_002 with seed=456 to confirm stability of persuasion-grounded DeBERTa detection advantage over vanilla baseline across random seeds ← 基于 plan_002_clean_training\n  [plan_002_seed456_dd_ood_results](file:///root/persuasion_turn_jailbreak_detect/results/plan_002_seed456_dd_ood.json)\n- **plan_002_seed123** (success): 9-class persuasion treatment seed=123 achieves same DD 
…[truncated 421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1958
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-18T08:35:46.257328+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-18T08:35:46.659516+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\graphicspath{{../../}}
12	\usepackage{amsmath}
13	\usepackage{booktabs}
14	\usepackage{enumitem}
15	\usepackage{amssymb}
16	\usepackage{multirow}
17	
18	\title{What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	
27	\input{introduction}
28	
29	\input{related_work}
30	
31	\input{method}
32	
33	\input{experiments}
34	
35	\input{conclusion}
36	
37	\bibliography{references}
38	
39	\input{appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-18T08:35:46.659958+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-18T08:35:51.631106+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2024: Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2024-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Call for Papers: NLP for Science Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/nlp-science"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"[Call for participation] Present your Findings of EMNLP paper at the NLP4MusA (NLP for Music and Audio) workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-participation-present-your-findings-emnlp-paper-nlp4musa-nlp-music-and-audio-workshop"}]

The search results show information about various ACL conferences and related events, but I didn't find a specific "EMNLP 2026 Call for Papers
…[truncated 1103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "elapsed_ms": 4971
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-18T08:37:25.732390+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission deadline paper format guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission deadline paper format guidelines"
  }
}
```

</details>

---


### Tool call

_source line 15 · 2026-05-18T08:37:26.586596+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"EMNLP 2026\" call for papers long paper short paper page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"EMNLP 2026\" call for papers long paper short paper page limit"
  }
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-18T08:37:28.446175+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-18T08:37:28.446683+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 18 · 2026-05-18T08:37:31.512257+00:00_

Web search results for query: "EMNLP 2026 submission deadline paper format guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"}]

Based on the search results, here is information about EMNLP 2026 submission deadline and paper format guidelines:

## Submission Deadline

The EMNLP 2026 paper submission deadline is May 25, 2026, 23:59:59 (UTC-12). All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

## Paper Format Guidelines

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. The mandatory Limitations section is required, placed after the conclusion.

Papers must follow the ACL format. Papers must follow the ACL format and conform to the EMNLP 2026 Submission Guidelines.

## Important Author Requirements

After s
…[truncated 514 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "elapsed_ms": 5779
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-18T08:37:32.567434+00:00_

Web search results for query: ""EMNLP 2026" call for papers long paper short paper page limit"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"}]

Based on the search results, here's the information about EMNLP 2026 call for papers page limits:

## EMNLP 2026 Main Conference

Long Papers are limited to 8 pages and Short Papers are limited to 4 pages. This follows the standard formatting requirements for *ACL conferences.

## EMNLP 2026 Industry Track

For the Industry Track specifically, Industry Track papers cannot exceed 6 pages in length (excluding ethical considerations and references). Additionally, references and limitations sections do not count toward the page limit, nor do the following optional sections: acknowledgements (only in the final version), ethical considerations, and appendices.
…[truncated 334 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "elapsed_ms": 5980
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-18T08:37:38.946471+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-18T08:37:39.298380+00:00_

1	% abstract.tex — D024 compressed
2	\begin{abstract}
3	Multi-turn jailbreak attacks against Large Language Models (LLMs) distribute adversarial intent across seemingly benign conversational turns, evading per-turn safety filters.
4	Standard temporal classifiers fail to generalize: a vanilla DeBERTa encoder achieves only F1\,=\,0.28 on out-of-distribution (OOD) attack types.
5	We design seven controlled variants of a DeBERTa-based detection framework to decompose what enables cross-attack generalization.
6	Masked language modeling (MLM) continued pretraining, without any classification labels, achieves near-perfect early detection on unseen attacks (mean F1\,$\geq$\,0.97 at $K\leq 5$ turns) but shows instability at full conversation length (F1\,=\,0.91$\pm$0.12).
7	Any continued pretraining bridges most of the OOD gap (vanilla 0.28 $\to$ $\sim$0.91); jailbreak-domain text improves early detection ($K$=2: 8 percentage point advantage over Wikipedia MLM).
8	Misaligned supervision yields unstable generalization (topic F1\,=\,0.54$\pm$0.21, worst seed below vanilla).
9	The 9-class persuasion model achieves the highest F1 (0.997$\pm$0.005), and classification supervision further contributes stability, perturbation robustness (zero degradation at full length for all classification-supervised variants; correct fine-grained labels add early-turn robustness, $n$=76), and interpretability through strategy trajectories.
10	These results reframe multi-turn jailbreak detection as primarily a domain adaptation problem, with classification supervision providing complementary stability, robustness, and interpretability.
11	\end{abstract}
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-18T08:37:39.449398+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-18T08:37:40.253406+00:00_

1	% introduction.tex — expanded for 8-page target
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Multi-turn jailbreak attacks pose a qualitatively different threat to large language model (LLM) safety than their single-turn counterparts. Attacks such as Crescendo~\citep{russinovich2024crescendo}, Foot-in-the-Door (FITD)~\citep{fitd2024}, and Deceptive Delight~\citep{deceptivedelight2024} distribute adversarial intent across individually benign turns through rapport building, logical reframing, and incremental escalation. Persuasion is the common mechanism: \citet{zeng2024pap} catalogue 40 persuasion techniques across jailbreak families, and \citet{hagendorff2026reasoning} find identifiable strategies in 97\% of successful attacks. Individual attack turns occupy the same embedding region as benign text~\citep{bullwinkel2025repeng}, rendering per-turn safety filters fundamentally blind.
7	
8	Production classifiers such as Llama Guard~\citep{inan2023llamaguard}, WildGuard~\citep{han2024wildguard}, and ShieldGemma~\citep{zeng2024shieldgemma} operate on individual turns and cannot model manipulation trajectories across exchanges. Recent multi-turn defenses have begun to address conversation-level structure: DeepContext~\citep{deepcontext2026} aggregates BERT embeddings with a recurrent network, BIID~\citep{tong2025biid} infers turn-level intentions, and G-Guard~\citep{gguard2025} applies graph neural networks. These systems achieve reasonable in-distribution performance but degrade on unseen attack types, and none systematically analyze \emph{why} some representations generalize while others fail. The open question is: \emph{what representation properties enable cross-attack generalization?}
9	
10	A vanilla DeBERTa encoder~\citep{he2021deberta} with temporal aggregation collapses from F1\,=\,1.000 on in-distribution data to F1\,=\,0.284 on out-of-distribution (OOD) Deceptive Delight, worsening with more turns (0.575 at turn~1 to 0.284 at full conversation). 
…[truncated 3417 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-18T08:37:40.404425+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-18T08:37:40.706492+00:00_

1	% related_work.tex — D024 compressed
2	
3	\section{Related Work}
4	\label{sec:related_work}
5	
6	\paragraph{Multi-turn jailbreak attacks.}
7	Multi-turn attacks distribute adversarial intent across individually benign turns. Crescendo~\citep{russinovich2024crescendo} implements gradual escalation, FITD~\citep{fitd2024} exploits commitment-consistency bias, Deceptive Delight~\citep{deceptivedelight2024} combines emotional manipulation with role assignment, ActorAttack~\citep{ren2024actorattack} uses multi-persona steering, and PAIR~\citep{chao2023pair} automates iterative refinement. \citet{wei2023jailbroken} provide a unifying taxonomy grounded in competing objectives and mismatched generalization. Across these families, a shared reliance on persuasion dynamics~\citep{zeng2024pap,hagendorff2026reasoning,li2024mhj} distinguishes them from token-level attacks such as GCG~\citep{zou2023gcg}.
8	
9	\paragraph{Multi-turn defenses.}
10	Existing defenses model conversation-level structure but do not decompose what enables cross-attack generalization. DeepContext~\citep{deepcontext2026} aggregates BERT embeddings with a recurrent network (F1 = 0.84 IID, fails OOD). BIID~\citep{tong2025biid} infers turn-level intentions, G-Guard~\citep{gguard2025} applies GNN classification, and SafeDream~\citep{safedream2026} predicts unsafe continuations. None ground analysis in the mechanism enabling generalization across attack families. DisPeD addresses this through domain-adaptive continued training, with decomposition experiments showing that domain exposure, not the training objective, is the primary factor.
11	
12	\paragraph{Production safety systems.}
13	Per-turn classifiers (Llama Guard~\citep{inan2023llamaguard,metallamaguard3_2024}, ShieldGemma~\citep{zeng2024shieldgemma}, WildGuard~\citep{han2024wildguard}, Constitutional Classifiers~\citep{anthropic2025constitutional}) cannot model manipulation trajectories spanning multiple turns. LLM-as-judge approaches also fail: GPT-5.5 ac
…[truncated 2207 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-18T08:37:40.757244+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-18T08:37:40.858202+00:00_

1	% method.tex — D024 compressed
2	
3	\section{Method}
4	\label{sec:method}
5	
6	DisPeD is a two-stage framework for multi-turn jailbreak detection. Stage~1 adapts a turn-level encoder through continued training on jailbreak conversation text. Stage~2 aggregates turn representations for conversation-level binary classification. To systematically identify what enables cross-attack generalization, we design seven Stage-1 variants that decompose the contributions of domain exposure, classification supervision, label quality, label granularity, and domain specificity. Figure~\ref{fig:architecture} illustrates the pipeline.
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=\columnwidth]{figures/paper/fig1_architecture.pdf}
11	\caption{DisPeD architecture. Stage~1 adapts a DeBERTa encoder on jailbreak conversation text (seven variant objectives). Stage~2 aggregates frozen \texttt{[CLS]} embeddings via BiGRU for conversation-level jailbreak detection. Only user turns are processed.}
12	\label{fig:architecture}
13	\end{figure}
14	
15	\subsection{Problem Formulation}
16	
17	A conversation $C = \{u_1, a_1, \ldots, u_N, a_N\}$ alternates user turns $u_i$ and assistant responses $a_i$. Given a prefix of $K$ user turns, the model predicts $y \in \{0, 1\}$ (jailbreak vs.\ benign). We restrict input to user turns because adversarial intent resides in the attacker's messages. This formulation supports early detection from partial prefixes.
18	
19	\subsection{Stage 1: Turn-Level Encoder Adaptation}
20	\label{sec:stage1}
21	
22	Each user turn $u_i$ is encoded by DeBERTa-v3-base~\citep{he2021deberta}; the \texttt{[CLS]} embedding $h_i \in \mathbb{R}^d$ serves as the turn representation. Seven variants, summarized in Table~\ref{tab:variants}, share the same training data but differ in objective.
23	
24	\begin{table}[t]
25	\centering
26	\small
27	\caption{Stage-1 encoder variants. All operate on the same training conversations except Wikipedia MLM (matched token count on Wik
…[truncated 3742 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-18T08:37:41.210132+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-18T08:37:41.663194+00:00_

1	% experiments.tex — D024 compressed for 8-page limit
2	
3	\section{Experiments}
4	\label{sec:experiments}
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	\paragraph{Data.}
10	We train on 250 Crescendo~\citep{russinovich2024crescendo} jailbreak and 250 topic-anchored benign conversations generated via Qwen3-8B.
11	OOD evaluation uses 80 FITD~\citep{fitd2024} and 80 Deceptive Delight (DD)~\citep{deceptivedelight2024} conversations with no overlap in attack templates.
12	The IID test set consists of 76 held-out Crescendo conversations; a paraphrased version (BERTScore 0.92, lexical overlap 0.20) serves as the adversarial robustness benchmark.
13	
14	\paragraph{Models.}
15	Seven variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\ref{sec:method}).
16	We also compare TF-IDF LR and LLM-as-judge baselines (Appendix~\ref{sec:llm_judge}): GPT-5.5 achieves only F1 = 0.191--0.449 on IID Crescendo with 30--47\% unparseable responses. Content-level reasoning is insufficient for this task.
17	
18	\paragraph{Metrics.}
19	F1 for binary jailbreak detection at prefix $K$=2 and full conversations (full per-$K$ results in Appendix~\ref{sec:full_prefix}).
20	OOD DD results for 9-class, MLM, and Wikipedia MLM report 3-seed mean$\pm$std (seeds 42, 123, 456); topic reports 3-seed due to high variance; binary and scrambled use seed 42.
21	Stage-1: learning rate $2 \times 10^{-5}$, batch 16, 4 epochs, MLM masking 15\%.
22	Stage-2: two-layer MLP, 20 epochs.
23	
24	%----------------------------------------------------------------------
25	\subsection{Cross-Attack Generalization}
26	\label{sec:cross_attack}
27	
28	\begin{table}[t]
29	\centering
30	\small
31	\caption{Cross-attack generalization (F1) at $K$=2 and full conversation. 3-seed mean$\pm$std where noted. Full per-$K$ results in Appendix~\ref{sec:full_prefix}.}
32	\label{tab:main_results}
33	\begin{tabular}{@{}lcc|cc@{}}
34	\toprule
35	& \multicolumn{2}{c|}{\textit{IID (Cresc.)}} & \multicolumn{2}{c}
…[truncated 13246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-18T08:37:41.663598+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-18T08:37:42.628113+00:00_

1	% conclusion.tex — D024 compressed
2	
3	\section{Conclusion}
4	\label{sec:conclusion}
5	
6	DisPeD's seven controlled Stage~1 variants establish that continued pretraining is the primary mechanism for cross-attack generalization: MLM without labels bridges the dominant $\sim$62\,pp gap (vanilla 0.28 $\to$ MLM 0.91$\pm$0.12), with near-perfect early detection (F1 $\geq$ 0.97 at $K \leq 5$). Any continued pretraining bridges most of this gap; Wikipedia MLM (0.90$\pm$0.12) nearly matches jailbreak-domain MLM at full length, while jailbreak-domain text provides a meaningful advantage for early detection ($K$=2: 8\,pp gap). Classification supervision adds stability (9-class 0.997$\pm$0.005 vs.\ MLM 0.91$\pm$0.12), perturbation robustness with a three-layer attribution (classification structure provides full-length robustness, the combination of correct and fine-grained labels is required at $K$=2, and both properties contribute independently at $K$=1), and interpretability through strategy trajectories. These results reframe multi-turn jailbreak detection as primarily a domain adaptation problem.
7	
8	\paragraph{Limitations and future work.}
9	The dataset is small (500 training, 160 OOD test conversations) and synthetically generated by Qwen3-8B, which may not capture the full diversity of real-world attack strategies.
10	TF-IDF achieves F1 = 0.944 on DD, which reveals substantial lexical separability in the current evaluation data; DisPeD's advantage over bag-of-words is strongest under perturbation (0\,pp vs.\ $\sim$12\,pp degradation) and for interpretability via strategy trajectories.
11	The perturbation robustness evaluation uses $n$=76 paraphrased conversations, where tier boundaries correspond to 1--3 misclassifications; larger-scale evaluation is needed to confirm the three-layer attribution pattern.
12	Binary and scrambled variants report single-seed results; multi-seed evaluation would strengthen the comparison with 3-seed variants.
13	Only persuasion-mediated
…[truncated 649 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 964
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-18T08:37:42.628584+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-18T08:37:43.080723+00:00_

1	% appendix.tex — Supplementary material
2	
3	\appendix
4	
5	\section{LLM-as-Judge Baseline}
6	\label{sec:llm_judge}
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\caption{LLM-as-judge zero-shot Crescendo detection (IID test set). F1 values exclude unparseable responses and represent upper bounds.}
12	\label{tab:llm_judge}
13	\begin{tabular}{@{}lccccr@{}}
14	\toprule
15	\textbf{Method} & $K$=2 & $K$=3 & $K$=5 & Full & Unparse. \\
16	\midrule
17	GPT-5.5 & .191 & .273 & .449 & .383 & 30--47\% \\
18	Qwen3-8B & .000 & .051 & .146 & .100 & 0\% \\
19	\midrule
20	9-class (ours) & \textbf{1.000} & \textbf{1.000} & \textbf{1.000} & \textbf{1.000} & 0\% \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	Table~\ref{tab:llm_judge} reports zero-shot performance for GPT-5.5 and Qwen3-8B on the IID Crescendo test set.
26	GPT-5.5 achieves precision of 1.0 at all turn prefixes but recall ranges from only 0.105 to 0.290, resulting in F1 of 0.191 at $K$=2 and 0.449 at $K$=5.
27	A substantial fraction (30--47\%) of responses are unparseable; F1 values exclude these and represent upper bounds.
28	Full-conversation F1 (0.383) is lower than $K$=5 F1 (0.449) because the unparseable rate grows with context length.
29	Qwen3-8B performs worse across all prefixes (F1 from 0.000 at $K$=2 to 0.100 on full conversations).
30	The failure of both a frontier commercial model and an open-weight model confirms a fundamental limitation of content-level reasoning for multi-turn jailbreak detection.
31	
32	\section{Full Cross-Attack Results by Prefix}
33	\label{sec:full_prefix}
34	
35	\begin{table*}[t]
36	\centering
37	\small
38	\caption{Full cross-attack generalization results (F1) at all prefix lengths. 3-seed mean$\pm$std where available.}
39	\label{tab:full_prefix}
40	\begin{tabular}{@{}lccccc@{}}
41	\toprule
42	\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\
43	\midrule
44	\multicolumn{6}{l}{\textit{IID (Crescendo)}} \\[2pt]
45	9-class (ours) & 1.000$\pm$.000 & 1.000$\pm$.000 & 1.
…[truncated 904 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-18T08:37:43.482864+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "literature_map.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect",
    "file": "literature_map.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-18T08:37:43.534012+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/literature_map.yaml\", \"content\": \"# Literature Map — persuasion_turn_jailbreak_detect\\n# Generated: 2026-05-17 by Paper Agent\\n# Target: EMNLP 2026 Main (ARR May cycle)\\n# Total entries: 39 (across 8 categories + technical foundation)\\n# All entries WebSearch-verified\\n\\nmetadata:\\n  project: persuasion_turn_jailbreak_detect\\n  target_venue: EMNLP 2026\\n  last_updated: \\\"2026-05-17\\\"\\n  total_papers: 39\\n  categories:\\n    - production_safety_systems\\n    - multi_turn_defenses\\n    - discourse_analysis\\n    - computational_persuasion\\n    - jailbreak_attacks_taxonomies\\n    - red_teaming\\n    - annotation_artifacts\\n    - adaptive_attacks\\n    - technical_foundation\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Production Multi-Turn Safety Systems (5 papers)\\n  # ============================================================\\n\\n  - bibtex_key: inan2023llamaguard\\n    title: \\\"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\\\"\\n    authors: \\\"Inan et al.\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2023\\n    arxiv: \\\"2312.06674\\\"\\n    category: production_safety_systems\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Foundational production safety classifier. Per-turn input/output guard\\n      that lacks multi-turn context modeling. DisPeD addresses this gap by\\n      modeling conversation-level persuasion trajectories.\\n\\n  - bibtex_key: metallamaguard3_2024\\n    title: \\\"Llama Guard 3\\\"\\n    authors: \\\"Meta AI\\\"\\n    venue: \\\"Meta AI (released with Llama 3.1)\\\"\\n    year: 2024\\n    category: production_safety_systems\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Latest iteration of Llama Guard with multili
…[truncated 11344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-18T08:37:51.425315+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-18T08:37:51.877408+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-18T08:37:52.530795+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "review_issues.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect",
    "file": "review_issues.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-18T08:37:52.832455+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-18T08:37:52.832901+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-18T08:37:53.812516+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 979
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-18T08:37:54.013742+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/fig1_architecture.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/fig1_architecture.pdf"
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-18T08:38:00.240073+00:00_

PDF file read: /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/fig1_architecture.pdf (54.3KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 6226
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-18T08:38:00.391741+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/fig2_cross_attack_bar.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/fig2_cross_attack_bar.pdf"
  }
}
```

</details>

---


### Tool call

_source line 45 · 2026-05-18T08:38:00.442475+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/fig3_strategy_heatmap.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/fig3_strategy_heatmap.pdf"
  }
}
```

</details>

---


### Tool result

_source line 46 · 2026-05-18T08:38:00.493472+00:00_

PDF file read: /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/fig2_cross_attack_bar.pdf (18KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-18T08:38:00.494322+00:00_

PDF file read: /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/fig3_strategy_heatmap.pdf (26.4KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-18T08:38:04.768631+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-18T08:38:04.819507+00:00_

1	% References for persuasion_turn_jailbreak_detect
2	% Auto-generated from literature_map.yaml (2026-05-18)
3	% Total entries: 31
4	
5	% ============================================================
6	% Category 1: Production Multi-Turn Safety Systems
7	% ============================================================
8	
9	@article{inan2023llamaguard,
10	  title={Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations},
11	  author={Inan, Hakan and Upasani, Kartikeya and Chi, Jianfeng and Rungta, Rashi and Iyer, Krithika and Mao, Yuning and Tontchev, Michael and Hu, Qing and Fuller, Brian and Testuggine, Davide and Khabsa, Madian},
12	  journal={arXiv preprint},
13	  year={2023},
14	  eprint={2312.06674},
15	  archivePrefix={arXiv},
16	}
17	
18	@misc{metallamaguard3_2024,
19	  title={Llama Guard 3},
20	  author={{Meta AI}},
21	  year={2024},
22	  howpublished={Meta AI (released with Llama 3.1)},
23	}
24	
25	@article{zeng2024shieldgemma,
26	  title={ShieldGemma: Generative AI Content Moderation Based on Gemma},
27	  author={Zeng, Wenjun and Liu, Yuchi and Mullins, Ryan and Peran, Ludovic and Fernandez, Joe and Harkous, Hamza and Narasimhan, Karthik and Proud, Drew and Kumar, Piyush and Radharapu, Bhaktipriya and Sturman, Olivia and Wahltinez, Oscar},
28	  journal={arXiv preprint},
29	  year={2024},
30	  eprint={2407.21772},
31	  archivePrefix={arXiv},
32	}
33	
34	@inproceedings{han2024wildguard,
35	  title={WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs},
36	  author={Han, Seungju and Rao, Kavel and Ettinger, Allyson and Jiang, Liwei and Lin, Bill Yuchen and Lambert, Nathan and Choi, Yejin and Dziri, Nouha},
37	  booktitle={Advances in Neural Information Processing Systems},
38	  year={2024},
39	}
40	
41	@article{anthropic2025constitutional,
42	  title={Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming},
43	  author={{Anthropic}},
44	  journal={arXiv 
…[truncated 12277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-18T08:38:23.419872+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
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

_source line 51 · 2026-05-18T08:38:23.470465+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-18T08:38:26.783940+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-18T08:38:26.834535+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-18T08:38:29.749745+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-18T08:38:29.800576+00:00_

Found 3 files
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/logs/chats/feishu_group_oc_613965f45d48763f375aa83e9294b24a_director.jsonl
AGENTS.md
CLAUDE.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-18T08:38:32.765478+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai\"\n",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "glob": "*.yaml",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai\"\n",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
    "glob": "*.yaml",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-18T08:38:32.967757+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Grep",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-18T08:38:35.530314+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review\"\n",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "glob": "**/config*.yaml",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review\"\n",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
    "glob": "**/config*.yaml",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-18T08:38:35.581174+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-18T08:38:37.841095+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/project_config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/project_config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-18T08:38:37.891843+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-18T08:38:40.103674+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-18T08:38:40.154314+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/_project/data/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260518T032748/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260518T032748/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260518T032748/worst/imagined_experiments.yaml
/home/ubu
…[truncated 1490 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-18T08:38:52.969419+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-18T08:38:53.020130+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-18T08:39:36.972655+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "persuasion_turn_jailbreak_detect",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验有效性**\n\n### Venue 信息\n- **目标会议**：EMNLP 2026 Main Conference (ARR May cycle)\n- **截止日期**：2026-05-25\n- **页数限制**：长文 8 页（不含 references、limitations、ethics）\n- **模板**：ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**：Double-blind review\n\n### 论文路径\n- 主文件：`projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex`\n- 各章节：`abstract.tex`, `introduction.tex`, `related_work.tex`, `method.tex`, `experiments.tex`, `conclusion.tex`, `appendix.tex`\n- 引用：`references.bib`\n- 图片：`figures/paper/fig1_architecture.pdf`, `fig2_cross_attack_bar.pdf`, `fig3_strategy_heatmap.pdf`\n\n### 审查要求\n\n请重点评估以下方面，给出逐条意见：\n\n1. **实验设计严谨性**\n   - 7 个 Stage-1 变体的消融设计是否真正隔离了声称的因素？是否存在混淆变量？\n   - 控制变量是否充分？（同一训练数据、同一 Stage-2 pipeline、同一超参）\n   - 数据集规模（500 训练、160 OOD 测试）是否足以支撑论文的 claims？\n\n2. **统计显著性与可靠性**\n   - 3-seed 报告 vs 单 seed 报告的不一致（binary/scrambled 仅 seed 42）——这是否削弱了关键比较？\n   - perturbation robustness 的样本量（n=76）是否足够？论文承认 tier boundaries = 1-3 misclassifications，这多大程度上削弱了 three-layer attribution 的可信度？\n   - MLM 的高方差（0.91±0.12）是否充分讨论？\n\n3. **方法论问题**\n   - 策略标注由 Qwen3-8B 生成（Cohen's κ=0.78, n=50），这个标注质量是否足够？人工标注样本量是否太小？\n   - Stage-1 冻结后进入 Stage-2，这个设计选择的合理性？为什么不 end-to-end fine-tune？\n   - Mean pooling = BiGRU 的结论（仅 single seed）是否过强？\n\n4. **Baseline 充分性**\n   - 缺少与 DeepContext (F1=0.84)、BIID、G-Guard、SafeDream 的直接实验对比\n   - LLM-as-judge baseline 仅测 IID（Crescendo），未测 OOD\n   - TF-IDF LR 达 0.944 on DD，与 9-class 的差距是否足以证明复杂模型的必要性？\n\n5. **可复现性**\n   - 超参报告是否完整？\n   - 数据生成过程（Qwen3-8B 生成对话）是否有足够细节？\n   - 代码/数据是否承诺开源？\n\n请按 EMNLP 标准给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Score (1-5)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "persuasion_turn_jailbreak_detect",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验有效性**\n\n### Venue 信息\n- **目标会议**：EMNLP 2026 Main Conference (ARR May cycle)\n- **截止日期**：2026-05-25\n- **页数限制**：长文 8 页（不含 references、limitations、ethics）\n- **模板**：ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**：Double-blind review\n\n### 论文路径\n- 主文件：`projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex`\n- 各章节：`abstract.tex`, `introduction.tex`, `related_work.tex`, `method.tex`, `experiments.tex`, `conclusion.tex`, `appendix.tex`\n- 引用：`references.bib`\n- 图片：`figures/paper/fig1_architecture.pdf`, `fig2_cross_attack_bar.pdf`, `fig3_strategy_heatmap.pdf`\n\n### 审查要求\n\n请重点评估以下方面，给出逐条意见：\n\n1. **实验设计严谨性**\n   - 7 个 Stage-1 变体的消融设计是否真正隔离了声称的因素？是否存在混淆变量？\n   - 控制变量是否充分？（同一训练数据、同一 Stage-2 pipeline、同一超参）\n   - 数据集规模（500 训练、160 OOD 测试）是否足以支撑论文的 claims？\n\n2. **统计显著性与可靠性**\n   - 3-seed 报告 vs 单 seed 报告的不一致（binary/scrambled 仅 seed 42）——这是否削弱了关键比较？\n   - perturbation robustness 的样本量（n=76）是否足够？论文承认 tier boundaries = 1-3 misclassifications，这多大程度上削弱了 three-layer attribution 的可信度？\n   - MLM 的高方差（0.91±0.12）是否充分讨论？\n\n3. **方法论问题**\n   - 策略标注由 Qwen3-8B 生成（Cohen's κ=0.78, n=50），这个标注质量是否足够？人工标注样本量是否太小？\n   - Stage-1 冻结后进入 Stage-2，这个设计选择的合理性？为什么不 end-to-end fine-tune？\n   - Mean pooling = BiGRU 的结论（仅 single seed）是否过强？\n\n4. **Baseline 充分性**\n   - 缺少与 DeepContext (F1=0.84)、BIID、G-Guard、SafeDream 的直接实验对比\n   - LLM-as-judge baseline 仅测 IID（Crescendo），未测 OOD\n   - TF-IDF LR 达 0.944 on DD，与 9-class 的差距是否足以证明复杂模型的必要性？\n\n5. **可复现性**\n   - 超参报告是否完整？\n   - 数据生成过程（Qwen3-8B 生成对话）是否有足够细节？\n   - 代码/数据是否承诺开源？\n\n请按 EMNLP 标准给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Score (1-5)。"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-18T08:39:57.960902+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20988
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-18T08:39:58.412903+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "persuasion_turn_jailbreak_detect",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + 写作质量**\n\n### Venue 信息\n- **目标会议**：EMNLP 2026 Main Conference (ARR May cycle)\n- **截止日期**：2026-05-25\n- **页数限制**：长文 8 页（不含 references、limitations、ethics）\n- **模板**：ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**：Double-blind review\n\n### 论文路径\n- 主文件：`projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex`\n- 各章节：`abstract.tex`, `introduction.tex`, `related_work.tex`, `method.tex`, `experiments.tex`, `conclusion.tex`, `appendix.tex`\n- 引用：`references.bib`\n- 图片：`figures/paper/fig1_architecture.pdf`, `fig2_cross_attack_bar.pdf`, `fig3_strategy_heatmap.pdf`\n\n### 审查要求\n\n请重点评估以下方面，给出逐条意见：\n\n1. **新颖性与贡献定位**\n   - 核心发现（domain-adaptive pretraining 是主要机制）是否足够新颖？Gururangan et al. (2020) 的 DAPT 已是成熟方法论，将其应用于 jailbreak detection 的增量贡献如何评估？\n   - \"partially falsified our original hypothesis\" 的叙事策略是否有效？这是否使论文的 contribution 显得不够聚焦？\n   - 7 个变体的消融实验本身是否构成足够的方法贡献，还是更偏向 empirical study？\n   - 如果定位为 empirical study，在 EMNLP 的接受标准下是否足够？\n\n2. **Related Work 覆盖与定位**\n   - 引用是否覆盖了所有直接相关工作？是否有重要遗漏？\n   - 与 DeepContext、BIID、SafeDream 等 direct competitors 的定位是否准确？\n   - 论文声称这些系统 \"none systematically analyze why some representations generalize\"——这个 gap 声明是否准确？\n   - 引用密度（31 entries）对于 EMNLP 长文是否足够？\n\n3. **叙事结构与主线统一性**\n   - Abstract → Introduction → Method → Experiments → Conclusion 是否形成连贯主线？\n   - 论文标题 \"What Makes Multi-Turn Jailbreaks Detectable?\" 是否与实际内容匹配？副标题 \"Domain Exposure Bridges the Cross-Attack Gap\" 是否准确概括核心发现？\n   - Introduction 的故事线是否清晰：问题 → 洞察 → 方法 → 验证？\n   - \"partially falsified\" 的叙事是否在全文中保持一致？\n\n4. **写作质量（严格按照 AI 写作检测标准）**\n   - 检查是否有 em-dash (—) 或解释性 en-dash (–) 的使用\n   - 检查 -ing 短语结尾（如 \"..., highlighting the...\"）\n   - 检查过度分段、过渡词堆积\n   - 检查用词黑名单：delve, leverage, utilize, facilitate, myriad, plethora, paradigm shift\n   - Abstract 是否在 150-250 words 范围内？缩写是否定义？\n   - 每个 Contribution 是否有对应 section/table 支撑？\n\n5. **格式合规**\n   - 正文是否在 8 页以内？\n   - Limitations section 是否存在且实质性？\n   - 匿名化是否完整？是否有泄露作者身份的线索？\n   - 表格/图片格式是否符合 ACL 标准？Caption 是否自包含？\n   - 引用格式是否一致？\n\n请按 EMNLP 标准给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Score (1-5)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "persuasion_turn_jailbreak_detect",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + 写作质量**\n\n### Venue 信息\n- **目标会议**：EMNLP 2026 Main Conference (ARR May cycle)\n- **截止日期**：2026-05-25\n- **页数限制**：长文 8 页（不含 references、limitations、ethics）\n- **模板**：ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**：Double-blind review\n\n### 论文路径\n- 主文件：`projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex`\n- 各章节：`abstract.tex`, `introduction.tex`, `related_work.tex`, `method.tex`, `experiments.tex`, `conclusion.tex`, `appendix.tex`\n- 引用：`references.bib`\n- 图片：`figures/paper/fig1_architecture.pdf`, `fig2_cross_attack_bar.pdf`, `fig3_strategy_heatmap.pdf`\n\n### 审查要求\n\n请重点评估以下方面，给出逐条意见：\n\n1. **新颖性与贡献定位**\n   - 核心发现（domain-adaptive pretraining 是主要机制）是否足够新颖？Gururangan et al. (2020) 的 DAPT 已是成熟方法论，将其应用于 jailbreak detection 的增量贡献如何评估？\n   - \"partially falsified our original hypothesis\" 的叙事策略是否有效？这是否使论文的 contribution 显得不够聚焦？\n   - 7 个变体的消融实验本身是否构成足够的方法贡献，还是更偏向 empirical study？\n   - 如果定位为 empirical study，在 EMNLP 的接受标准下是否足够？\n\n2. **Related Work 覆盖与定位**\n   - 引用是否覆盖了所有直接相关工作？是否有重要遗漏？\n   - 与 DeepContext、BIID、SafeDream 等 direct competitors 的定位是否准确？\n   - 论文声称这些系统 \"none systematically analyze why some representations generalize\"——这个 gap 声明是否准确？\n   - 引用密度（31 entries）对于 EMNLP 长文是否足够？\n\n3. **叙事结构与主线统一性**\n   - Abstract → Introduction → Method → Experiments → Conclusion 是否形成连贯主线？\n   - 论文标题 \"What Makes Multi-Turn Jailbreaks Detectable?\" 是否与实际内容匹配？副标题 \"Domain Exposure Bridges the Cross-Attack Gap\" 是否准确概括核心发现？\n   - Introduction 的故事线是否清晰：问题 → 洞察 → 方法 → 验证？\n   - \"partially falsified\" 的叙事是否在全文中保持一致？\n\n4. **写作质量（严格按照 AI 写作检测标准）**\n   - 检查是否有 em-dash (—) 或解释性 en-dash (–) 的使用\n   - 检查 -ing 短语结尾（如 \"..., highlighting the...\"）\n   - 检查过度分段、过渡词堆积\n   - 检查用词黑名单：delve, leverage, utilize, facilitate, myriad, plethora, paradigm shift\n   - Abstract 是否在 150-250 words 范围内？缩写是否定义？\n   - 每个 Contribution 是否有对应 section/table 支撑？\n\n5. **格式合规**\n   - 正文是否在 8 页以内？\n   - Limitations section 是否存在且实质性？\n   - 匿名化是否完整？是否有泄露作者身份的线索？\n   - 表格/图片格式是否符合 ACL 标准？Caption 是否自包含？\n   - 引用格式是否一致？\n\n请按 EMNLP 标准给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Score (1-5)。"
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-18T08:40:00.289351+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1876
}
```

</details>

---


### Assistant

_source line 70 · 2026-05-18T08:40:03.057944+00:00_

Round 1 任务已分配给 Reviewer 1（方法/实验）和 Reviewer 2（新颖性/写作）。等待两位 Reviewer 返回独立初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 2

## Round 2

2 recorded events


### User

_source line 71 · 2026-05-18T08:46:23.633245+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿意见 — Round 1

**论文**: "What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap"
**审查侧重**: 方法严谨性 + 实验有效性

---

## 总体评分

**Overall**: 2/5 (Resubmit next cycle)
**一句话总结**: 研究问题有价值、消融设计有想法，但核心 claims 的统计支撑严重不足（single-seed vs 3-seed 不一致、n=76 上的 three-layer attribution、缺少与 SOTA multi-turn defense 的直接对比），需要在下一轮提交前做实质性修订。

---

## 官方维度打分（来自 ACL ARR review form, Feb 2025+）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2/5 | 多项核心 claim 缺乏充分统计支撑：evidence hierarchy 中 binary/scrambled 仅 single seed，three-layer attribution 建立在 n=76（1-3 misclassifications = tier boundary）上，mean pooling = BiGRU 也是 single seed。这些不是 minor details，而是直接影响主要结论可信度的方法论缺陷。 |
| Excitement | 3/5 | 研究问题（什么表征属性使跨攻击泛化成为可能）有真正的学术价值。"partially falsified" 原始假设的诚实报告令人欣赏。MLM 即可桥接 ~62pp OOD gap 的发现与 domain-adaptive pretraining 文献良好对接。但执行层面的统计问题限制了影响力。 |
| Overall | 2/5 | 核心洞察（multi-turn jailbreak detection 本质上是 domain adaptation 问题）有意义，但需要：(1) 所有变体的 multi-seed 报告，(2) 更大规模评估或至少 significance tests，(3) 与已发表 multi-turn defense 系统的直接实验对比。这些修订可在下一个 ARR cycle 完成。 |
| Confidence | 4/5 | 对实验设计和统计方法论问题的评估比较确信。论文的 domain adaptation 核心论点与我的专业知识领域吻合。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Evidence hierarchy 的统计基础不一致：single-seed vs 3-seed 比较

- 具体位置：Section 5.2 Table 3, Section 5 Table 2, Abstract
- 问题：论文的核心贡献——evidence hierarchy（vanilla 0.28 < topic 0.54±0.21 ≪ wiki-MLM 0.90±0.12 ≈ jb-MLM 0.91±0.12 < scrambled 0.99 ≈ binary 0.99 ≈ 9-class 0.997±0.005）——混合了两种不同统计精度的结果。9-class、MLM、wiki-MLM、topic、vanilla 报告 3-seed mean±std，而 **binary 和 scrambled 仅报告 seed 42 的单点估计**（Section 5 明确说明："binary and scrambled use seed 42"）。
  
  这意味着 "scrambled (0.990) ≈ binary (0.990)" 这一关键等式没有方差信息。我们完全不知道 binary 和 scrambled 在 seeds 123、456 上的表现。考虑到 MLM 的方差高达 0.115（seed 456 recall 仅 0.64，见 Section 5.1），binary/scrambled 的真实分布可能有显著不同。

  更严重的是，论文从这一不一致的比较中推导出多项因果性结论：
  - "Label quality and granularity are non-factors for detection: scrambled (0.990) ≈ binary (0.990)"（Section 5.2）
  - "the classification objective functions as a regularizer that shapes representation geometry regardless of whether the labels carry meaningful semantic information"（Section 5.2）
  
  这些 claims 建立在 **两个 single-seed 数据点的巧合相等** 之上，无法排除 seed-specific 的可能性。

- 为什么影响接收：这是 evidence hierarchy 的核心环节。如果 binary 和 scrambled 的 multi-seed 结果出现显著方差（如 MLM 那样），整个 hierarchy 的排序和解释都可能改变。审稿人无法从现有数据判断 "label quality is a non-factor" 是否为 robust 结论。
- 建议修改方向：**所有 7 个变体必须报告相同的 3-seed（或更多 seed）mean±std**。这是最基本的实验公平性要求。论文 Conclusion 已承认这一限制（"Binary and scrambled variants report single-seed results; multi-seed evaluation would strengthen the comparison"），但这不是 "would strengthen"——这是最低要求。

**N2** [critical] Three-layer robustness attribution 在 n=76 上缺乏统计显著性

- 具体位置：Section 5.3 Table 4, Introduction contribution #2, Conclusion
- 问题：论文提出的 three-layer robustness attribution 是第二项核心贡献，但完全建立在 n=76 paraphrased conversations 上。**论文自身承认 "tier boundaries correspond to 1-3 misclassifications"**（Section 5.3 最后一句, Conclusion）。

  具体量化：
  - Δ=2.6pp ≈ 2 个样本的分类差异
  - Δ=5.3pp ≈ 4 个样本的分类差异
  - Δ=9.2pp ≈ 7 个样本的分类差异
  
  论文从这些极小的绝对差异中推导出精细的三层因果结构：
  - Layer 1: "classification structure provides full-length robustness"（基于 classification-supervised 的 Δ=0.0 vs 其他 Δ≠0）
  - Layer 2: "the combination of correct and fine-grained labels is required at K=2"（基于 9-class Δ=0.0 vs scrambled=binary=−2.6pp，即 2 个样本的差异）
  - Layer 3: "both granularity and correctness contribute independently at K=1"（基于 9-class −2.6 vs scrambled −5.3 vs binary −9.2）
  
  **没有报告任何统计显著性检验**（如 McNemar's test、bootstrap confidence intervals、permutation test）。在 n=76 的样本量下，2 个样本的差异极易被随机波动解释。

- 为什么影响接收：Three-layer attribution 是论文 Introduction 列出的第二项 contribution 的核心内容，占据了正文约 1/3 的讨论。如果统计显著性不成立，这一整块贡献都不可信。ARR reviewer guidelines 明确要求 "appropriate information about statistical significance (error bars, confidence intervals, statistical significance tests)"。
- 建议修改方向：(1) 大幅扩大 perturbation test set（至少 n≥300 才能使 2.6pp 的差异有统计意义），或 (2) 报告 bootstrap confidence intervals / McNemar's test p-values，或 (3) 如果无法扩大数据，将 three-layer attribution 降级为 "observed pattern" 而非 "established finding"，大幅弱化相关 claims。

**N3** [critical] 缺少与已发表 multi-turn defense 系统的直接实验对比

- 具体位置：Section 2 (Related Work), Section 5 (Experiments)
- 问题：论文在 Related Work 中讨论了 4 个直接相关的 multi-turn defense 系统：DeepContext（F1=0.84 IID, "fails OOD"）、BIID、G-Guard、SafeDream。但 **实验部分没有任何一个作为 baseline 进行头对头比较**。
  
  实际使用的 baselines 仅有：
  - Vanilla DeBERTa（论文自己的 ablation baseline）
  - TF-IDF LR（简单 baseline）
  - LLM-as-judge（GPT-5.5, Qwen3-8B，仅测 IID）
  
  DeepContext 的 F1=0.84 数字来自该论文自身报告，但其评估数据集、attack types、evaluation protocol 可能与本文不同。直接引用其他论文的数字进行隐式比较，在方法论上不成立。

- 为什么影响接收：论文的核心叙事是 "existing multi-turn defenses degrade on unseen attack types, and none systematically analyze why"（Introduction para 2）。如果不在相同数据集和评估条件下复现并对比这些方法，就无法支撑 "DisPeD addresses this" 的 claim。审稿人会认为这是一项缺乏充分 baseline 比较的 incremental work。
- 建议修改方向：至少复现 DeepContext（BERT + recurrent network, 结构简单）作为 direct baseline，在相同的 Crescendo/FITD/DD 数据上评估。如果无法获取其他系统的代码，应明确说明并讨论。

**N4** [critical] 数据集规模过小，影响所有核心 claims 的可信度

- 具体位置：Section 5.1, Conclusion (Limitations)
- 问题：
  - 训练集：250 Crescendo jailbreak + 250 benign = 500 conversations
  - OOD 测试集：80 FITD + 80 DD = 160 conversations
  - IID 测试集：76 Crescendo
  - Perturbation 测试集：76 paraphrased conversations
  
  在 n=80 的 DD 测试集上，每个 misclassification 改变 F1 约 1.25pp。这意味着：
  - 9-class 的 0.997±0.005 意味着平均约 0.24 个错误（3-seed，部分 seed 0 错误、部分 seed 1 错误）
  - MLM 的 0.914±0.115 在 seed 456 时 recall 仅 0.64，即约 29 个 misclassifications
  
  The entire evidence hierarchy 的精确排序在这种粒度下意义有限。

- 为什么影响接收：论文的核心贡献是 "systematic decomposition"，但 decomposition 的统计分辨率受制于极小的测试集。在 n=80 上区分 0.990 和 0.997 在统计上是无意义的。
- 建议修改方向：(1) 增加更多 attack families（如 ActorAttack, PAIR 的 multi-turn variants）扩大 OOD 测试范围，(2) 增加每种 attack 的样本量到至少 300+，(3) 在所有核心比较上报告 confidence intervals。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Mean pooling = BiGRU 的结论基于 single seed

- 具体位置：Section 5.2 Table 3（footnote $^\dagger$Single seed (42)）
- 问题：论文做出强因果 claim "Temporal modeling is not the detection mechanism. Mean pooling matches BiGRU (F1 = 1.000 on DD); detection relies on per-turn representations rather than their sequential order."（Section 5.2）。但 Table 3 脚注显示 mean pooling 结果仅为 seed 42。Mean pooling 在 DD-Full 和 DD-K=2 上均为 1.000，而 BiGRU 9-class 的 3-seed mean 为 0.997±0.005 和 0.981±0.013。在 n=80 的测试集上，1.000 vs 0.997 = 0 vs ~0.24 个错误的差异，统计上无意义。
- 建议：(1) 报告 mean pooling 的 3-seed 结果，(2) 弱化 claim 为 "the evidence suggests" 而非因果性结论，(3) 在更大测试集上验证。

**W2** [warning] 策略标注质量验证不充分（Qwen3-8B, κ=0.78, n=50）

- 具体位置：Section 3.2
- 问题：9-class 的策略标注由 Qwen3-8B 生成，人工验证仅 n=50 turns，Cohen's κ=0.78。对于 9 个类别，n=50 意味着每类平均约 5-6 个样本。某些低频类别（如 Direct Request, Obfuscation）可能只有 1-2 个验证样本。κ=0.78 是 "substantial agreement"（Landis & Koch 标准），但在人工样本量如此小的情况下，confidence interval 会很宽。
  
  更重要的是，论文 three-layer attribution 中 "correct labels" 的优势（Layer 2-3）完全依赖于标注质量。如果标注本身有 ~22% 的噪声率，"correct fine-grained labels" 的实际效果可能被高估。
- 建议：(1) 增加人工验证样本至 200+（按类别分层抽样），(2) 报告每类的 κ 或至少 confusion matrix，(3) 讨论标注噪声对 three-layer attribution 的影响。

**W3** [warning] LLM-as-judge baseline 仅测 IID，未测 OOD

- 具体位置：Appendix A Table 5
- 问题：GPT-5.5 和 Qwen3-8B 仅在 IID Crescendo 测试集上评估。论文的核心贡献是 OOD cross-attack generalization，不测 LLM baseline 的 OOD 表现是不公平的比较。LLM-as-judge 在 OOD 上可能表现更好（因为 IID Crescendo 数据是 Qwen3-8B 生成的，GPT-5.5 可能对 Qwen 生成的文本有 distributional mismatch）。
- 建议：在 FITD 和 DD 上也评估 LLM-as-judge。

**W4** [warning] TF-IDF LR 的强表现未被充分讨论

- 具体位置：Section 5.1 Table 2, Section 2 最后一段
- 问题：TF-IDF LR 在 DD-Full 上达到 0.944，与 9-class 的 0.997 仅差 5.3pp。在 perturbation 下（Table 4），TF-IDF 在 Full length 仅降 1.3pp。论文辩称 DisPeD 的优势在于 "robustness under perturbation (0pp vs ~12pp degradation)" 和 "interpretability"，但：
  - 12pp degradation 是 Wikipedia MLM 和 vanilla 的降级幅度，不是 TF-IDF 的
  - TF-IDF 自身仅降 1.3pp，与 9-class 的 0pp 差异在 n=76 上不具统计显著性
  - 如果 "substantial lexical separability" 是一个 known limitation（Related Work 最后一段承认），那么 DisPeD 相对于 TF-IDF 的真正增量在哪里？
- 建议：更诚实地讨论 TF-IDF baseline 的竞争力，并明确 DisPeD 在何种条件下具有不可替代的优势。

**W5** [warning] 可复现性不足

- 具体位置：全文
- 问题：
  - **超参不完整**：Stage-2 缺少 learning rate, batch size, optimizer, warmup schedule
  - **数据生成细节不足**：Qwen3-8B 生成对话的 prompt、temperature、conversation length distribution 未提供
  - **无代码/数据发布承诺**：全文未提及是否开源
  - **策略标注 prompt 未提供**：Section 3.2 仅说 "structured prompting that includes definitions and examples"，但未给出实际 prompt
- 建议：(1) 补充 Stage-2 完整超参，(2) 在 Appendix 提供数据生成和策略标注的完整 prompt，(3) 明确代码和数据发布计划。

**W6** [warning] FITD 评估贡献有限

- 具体位置：Section 5.1, Appendix B Table 7
- 问题：Appendix Table 7 显示 FITD 结果几乎全为 perfect（9-class 和 vanilla 均 F1≥0.990）。这意味着 FITD 作为 OOD 测试集没有区分度。论文的所有 OOD claims 实际上仅依赖 DD 这一种 attack type，严重限制了 "cross-attack generalization" claim 的 generalizability。
- 建议：增加更多 attack families（ActorAttack、PAIR 等）的 OOD 评估，或至少明确讨论当前 OOD 评估仅覆盖 2 种 attack type（其中 1 种区分度极低）的局限性。

---

## 小问题（不影响接收）

- Figure 1: Stage 1 和 Stage 2 标题有轻微重叠，"Frozen [CLS]" 文字与 "9-class Persuasion" 位置略有拥挤。建议调整 layout。
- Figure 3: 三个 heatmap 在单栏宽度下较小，axis labels 难以辨认（尤其 strategy 名称）。建议使用 `figure*` 环境占双栏宽度，或增大字体。
- 引用: `chao2023pair` 的 year 与 OpenAlex 记录不一致（bib 2023 vs API 2025，可能是 arXiv preprint vs 正式发表的差异）。`austin1962speechacts` 的 year 有 bib 1962 vs API 1975 的差异（可能是不同版本）。建议检查并更新。
- Section 5.1: "binary and scrambled use seed 42" 的原因未解释。为什么这两个变体没有运行 3-seed？是时间/计算资源限制还是其他原因？应说明。
- 论文未讨论不同变体的计算成本（training time, GPU hours）。对于一个 "systematic decomposition" 的工作，展示各变体的资源开销是有意义的。
- Section 3.1: 问题定义仅使用 user turns（"We restrict input to user turns because adversarial intent resides in the attacker's messages"）。这一合理假设值得更多讨论——assistant responses 是否可能包含有用的检测信号（如 refusal patterns, compliance indicators）？

---

## 主要优势

1. **研究问题有价值且定义清晰**：从 "what representation properties enable cross-attack generalization?" 切入，问题有明确的操作化路径。这是一个 community 关心但尚未系统回答的问题。

2. **消融设计思路优秀**：7 个 Stage-1 变体系统测试 domain exposure、classification supervision、label quality、label granularity、domain specificity 五个因素的贡献。Table 1 清楚展示了每个变体测试的假设，设计逻辑清晰。

3. **知识诚实地报告 "partially falsified" 假设**：论文坦承 MLM 无标签即可桥接大部分 OOD gap，原始的 "persuasion classification is key" 假设被部分否定。这种诚实的科学态度在论文中并不常见，值得肯定。

4. **与 domain-adaptive pretraining 文献的良好连接**：核心发现（continued pretraining 是主要机制）与 Gururangan et al. (2020) 的经典结论一致，将 jailbreak detection 重新定位为 domain adaptation 问题有理论深度。

5. **写作质量总体较好**：论文叙事连贯，从 "vanilla collapses on OOD" 到 "MLM bridges the gap" 到 "classification adds stability" 的层进式展开易于follow。Evidence hierarchy 的可视化呈现清晰。

6. **Strategy trajectory analysis 提供定性 insight**：Figure 3 的 transition matrices 展示了不同 attack families 的不同策略签名（Crescendo broad coverage vs FITD sparse Role→Obfuscation vs DD Emotion→Obfuscation），为安全分析提供了可操作的信息。

---

## 总结

论文提出了一个有价值的研究问题，消融设计思路优秀，核心发现（domain adaptation 是 multi-turn jailbreak detection 的主要机制）有理论意义。但当前版本在统计严谨性上有 4 项 critical 问题：(1) single-seed vs 3-seed 不一致破坏了 evidence hierarchy 的可比性，(2) three-layer robustness attribution 建立在 n=76 上且无 significance tests，(3) 缺少与 SOTA multi-turn defense 的直接实验对比，(4) 数据集规模过小限制了所有核心 claims 的统计分辨率。这些问题需要实质性修订，建议在下一个 ARR cycle 重新提交。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 72 · 2026-05-18T08:46:40.819676+00:00_

Reviewer 1 审稿意见已收到。评分 2/5，提出 4 项 critical 问题（single-seed 不一致、n=76 统计显著性、缺 SOTA 对比、数据集过小）和 6 项 warning。

等待 Reviewer 2 提交审稿意见后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 3

## Round 3

2 recorded events


### User

_source line 73 · 2026-05-18T08:46:43.690853+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心评判：**Overall 2/5 (Resubmit next cycle)**。论文研究问题有价值，7 变体消融设计思路优秀，但 4 项 critical 问题影响接收决定：

1. **Evidence hierarchy 统计基础不一致**：binary/scrambled 仅 seed 42，其他变体 3-seed，核心排序 "scrambled ≈ binary" 无方差支撑
2. **Three-layer robustness attribution 无统计显著性**：n=76 上 2.6pp 差异仅 ~2 个样本，无 significance tests
3. **缺少与 SOTA multi-turn defense 的直接对比**：DeepContext/BIID/G-Guard/SafeDream 仅讨论未实验
4. **数据集规模过小**：80 DD 测试样本下，0.990 vs 0.997 的区分无统计意义

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 74 · 2026-05-18T08:46:50.834880+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 4

## Round 4

6 recorded events


### User

_source line 75 · 2026-05-18T08:46:56.100560+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 1 审稿意见

**论文标题**: What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap
**审查侧重**: 新颖性 + 完整性 + 写作质量
**评审依据**: ACL ARR Review Form (2025年2月更新版)

---

## 总体评分

**Overall**: 2.5 (Borderline Findings)
**一句话总结**: 实验设计思路清晰（7 个受控变体逐层剥离因素），但核心发现（continued pretraining 是主要机制）在方法论上缺乏新颖性，实验规模过小（500 训练 + 160 OOD 测试），且缺少与直接竞争方法的实验对比，难以支撑论文的核心 claims。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3/5 (Acceptable) | 7 变体消融设计合理，但实验规模过小、有效 OOD 评估仅单数据集(DD)、部分变体只报告单 seed，削弱了统计可信度 |
| **Excitement** | 2.5/5 | 问题本身（什么使 jailbreak 可检测）有价值，但核心发现（DAPT 是主机制）在 NLP 社区已是成熟认知，应用到 jailbreak detection 的增量贡献有限 |
| **Overall** | 2.5/5 (Borderline Findings) | 系统性消融是贡献点，但规模和对比不足使结论的普适性存疑；定位偏 empirical study，对 Findings 有一定竞争力但对 Main Conference 不够 |
| **Reproducibility** | 3/5 | 超参数、架构细节描述充分，但训练数据为合成数据（Qwen3-8B 生成），数据生成 pipeline 细节不足，策略标注过程也缺乏详细描述 |
| **Reviewer Confidence** | 4/5 | 熟悉 domain-adaptive pretraining、LLM safety 和 multi-turn jailbreak 相关工作 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 实验规模过小，无法支撑"reframe multi-turn jailbreak detection as primarily a domain adaptation problem"的核心 claim
- 具体位置：Section 4.1 (Setup)、Abstract 最后一句、Conclusion 第一段
- 问题：训练集仅 250 jailbreak + 250 benign 对话，OOD 测试仅 80 FITD + 80 DD，perturbation 测试仅 n=76。论文在 Conclusion 中承认 "tier boundaries correspond to 1–3 misclassifications"（Section 6, Limitations），这意味着 perturbation robustness 的三层归因模式中，F1 差异可能仅由 1-2 个样本决定。在此规模下，论文不宜将结论概括为对 multi-turn jailbreak detection 整个任务的重新定义。
- 为什么影响接收：核心 claim 的证据强度与 claim 的广度严重不匹配。审稿人会质疑：这些发现是否只反映了这 500 条 Qwen3-8B 合成对话的特性，而非 multi-turn jailbreak 的一般性质？
- 建议修改方向：(1) 扩大数据集规模和来源多样性（多模型生成、人工红队数据）；(2) 若无法扩大规模，需显著降低 claim 强度，明确限定为 preliminary empirical findings on synthetic data。

**N2** [critical] 缺少与直接竞争方法（DeepContext、BIID、G-Guard、SafeDream）的实验对比
- 具体位置：Section 2 (Related Work) 与 Section 4 (Experiments)
- 问题：论文在 Related Work 中明确定位了四个 direct competitors（DeepContext, BIID, G-Guard, SafeDream），并声称它们 "achieve reasonable in-distribution performance but degrade on unseen attack types"（Section 2, Multi-turn defenses 段），以及 "none systematically analyze why some representations generalize while others fail"（Section 1, para 2）。但 Experiments 部分完全没有与这些方法的实验对比——唯一的 baselines 是 vanilla DeBERTa、TF-IDF LR 和 LLM-as-judge (GPT-5.5/Qwen3-8B)。论文对 DeepContext 引用了 "F1 = 0.84 IID, fails OOD" 的数据，但这是引自原文而非在相同实验条件下的复现。
- 为什么影响接收：对于一篇声称在 cross-attack generalization 问题上有新发现的论文，不与声称要超越的系统做实验对比是重大缺陷。审稿人无法判断 DisPeD 相对于现有 multi-turn defenses 的真实增量。
- 建议修改方向：至少复现 DeepContext（BERT + RNN，架构接近 vanilla baseline）在相同数据上的结果。若其他系统无法复现，需明确说明原因并在 Limitations 中讨论。

**N3** [critical] 有效 OOD 评估实质上是 single-dataset evaluation
- 具体位置：Section 4.2, Table 1, Appendix Table 4
- 问题：论文使用两个 OOD 数据集（FITD 和 DD），但 FITD 对方法几乎没有区分度——9-class 和 vanilla 均在所有 prefix 长度达到 F1≥0.990（Appendix Table 4: "FITD is easier: 9-class and vanilla both reach F1 ≥ 0.990 at all prefixes", Section 4.2）。这意味着 7 个变体的消融对比实际上只在 DD 一个数据集上有意义。单数据集的消融结论很可能受到该特定 attack type 特性的影响，无法证明跨 attack 的一般性。
- 为什么影响接收：论文的核心贡献是 "systematic decomposition of cross-attack generalization"，但如果该 decomposition 只在一个 OOD attack type 上有效，claim 的可信度大打折扣。
- 建议修改方向：增加至少 2-3 个难度适中的 OOD attack types（如 ActorAttack, PAIR），使消融对比在多个 OOD 数据集上可验证。

**N4** [critical] 变体间 seed 报告不一致，影响统计可比性
- 具体位置：Section 4.1 (Metrics 段)、Table 2、Table 3
- 问题：9-class、MLM、vanilla、topic 报告 3-seed 均值±标准差，但 binary 和 scrambled 只报告 seed 42 的单次结果。论文在 Limitations 中承认 "Binary and scrambled variants report single-seed results; multi-seed evaluation would strengthen the comparison"（Section 6）。然而，这两个变体在 evidence hierarchy 中处于关键位置（区分 label correctness 和 granularity 的作用），它们的 F1=0.990 是否稳定直接影响论文的核心论证。如果 binary/scrambled 在其他 seeds 下表现像 topic 那样有高方差（0.54±0.21），整个 evidence hierarchy 将被推翻。
- 为什么影响接收：消融实验的可信度依赖于变体间的公平对比。选择性报告部分变体的多 seed 结果而对关键变体只报告单 seed，是方法论缺陷。
- 建议修改方向：必须为所有 7 个变体提供相同数量的 seed 结果（至少 3 seeds）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Abstract 过度堆砌数据，不符合叙事驱动的写作标准
- 具体位置：Abstract
- 问题：Abstract 约 180 词，在范围内，但包含了大量具体数字（F1=0.28, F1≥0.97, F1=0.91±0.12, 0.54±0.21, 0.997±0.005, K≤5, K=2, 8 percentage point, n=76 等）。这使得 Abstract 读起来像压缩版的 Results 表格，而非一个有吸引力的研究故事。审稿人在 30 秒内难以从密集数字中提取核心价值判断。
- 建议：保留 2-3 个最关键的数字（如 vanilla 0.28 → MLM 0.91 → 9-class 0.997），将其余数字移入正文。Abstract 应聚焦于 "问题→洞察→方法→关键结论" 的叙事弧。

**W2** [warning] "partially falsified our original hypothesis" 叙事策略效果存疑
- 具体位置：Section 1, para 4; Abstract 第 6 句隐含
- 问题：Introduction 明确写道 "The result partially falsified our original hypothesis that persuasion-specific classification is the key ingredient"。虽然这体现了科学诚实，但在顶会投稿中，这种叙事策略会让审稿人觉得：(1) 作者在设计实验前没有明确的 hypothesis；(2) 论文的 contribution 是 "unexpected negative result" 而非 "deliberate systematic investigation"。实际上，论文的 7 变体消融设计本身就是一个系统性调查框架，不需要以 "假设被证伪" 来包装。
- 建议：将叙事重构为正面框架——"We discover that domain exposure, rather than task-specific supervision, is the primary mechanism for cross-attack generalization"。消融设计自然引出这一结论，无需 "falsification" 包装。

**W3** [warning] Contributions 列表过于密集，难以快速提取核心 claim
- 具体位置：Section 1, Contributions 列表
- 问题：两个 contribution bullet 各自是一个完整段落（约 60-80 词），包含大量数字和多层嵌套信息。审稿人扫读时难以快速识别具体的 claim 边界。第二个 contribution 甚至包含了三个子 claim（stability, robustness, interpretability）和一个嵌套的三层 attribution pattern。
- 建议：拆分为 3-4 个简短的 contribution bullets，每个聚焦一个 claim，数字证据放在括号中简要引用。

**W4** [warning] TF-IDF baseline 的强表现未被充分讨论
- 具体位置：Table 1 (TF-IDF LR: DD-Full F1=0.944)、Section 4.2, Section 2 最后一段
- 问题：TF-IDF LR 在 OOD DD 上达到 F1=0.944，仅比 MLM (0.914) 高 3pp，比 9-class (0.997) 低 5.3pp。论文承认 "substantial lexical separability persists across attack families"（Section 4.2）以及 "TF-IDF achieves F1 = 0.944 on DD, which reveals substantial lexical separability in current evaluation data"（Section 6）。这对论文的 framing 构成威胁：如果一个简单的词袋模型就能达到 0.944，那么 "domain exposure captures pragmatic features (hedging, escalation markers, topic-shifting patterns)" 的解释是否可靠？也许模型只是在捕捉词汇统计差异，而非真正的语用特征。
- 为什么影响评分：削弱了论文关于 "domain-adaptive pretraining captures pragmatic features" 的机制性解释。
- 建议：(1) 在更大规模、更多样化的数据上验证，以降低 lexical separability 的影响；(2) 增加特征分析实验（如 probing 实验或 attention 可视化），直接验证模型是否确实学到了语用特征而非词汇统计。

**W5** [warning] Strategy Trajectory Analysis 使用的是 ground-truth labels 而非模型预测
- 具体位置：Section 4.5, Figure 3
- 问题：Figure 3 caption 明确写道 "based on ground-truth intended strategy labels"（即 Qwen3-8B 标注的 labels）。正文也说 "transition count matrices based on ground-truth intended strategy labels for three attack types"（Section 4.5）。但论文将此作为 "interpretability" 的贡献——这是 9-class 模型相对于 MLM 模型的一个优势。如果 trajectory analysis 使用的是 ground-truth labels 而非模型在 OOD 数据上的预测 labels，那么它展示的是数据集的特性而非模型的可解释性能力。模型在 OOD 数据上能否正确预测策略标签？这个问题未被回答。
- 建议：补充模型在 OOD 数据上的策略预测准确率，并用模型预测 labels 重做 trajectory analysis，与 ground-truth 对比。

**W6** [warning] Mean Pooling 实验结果意外但讨论不充分
- 具体位置：Table 2 (Mean pooling: DD-Full 1.000, DD-K=2 1.000)、Section 4.4 最后一段
- 问题：Mean pooling 替代 BiGRU 后达到 F1=1.000（DD-Full 和 DD-K=2），甚至优于 BiGRU 的 9-class 模型（0.997）。论文据此得出 "detection relies on per-turn representations rather than their sequential order"（Section 4.4）。但这个实验只用了 9-class encoder、单 seed (42)。如此强的结论需要在更多变体和 seeds 上验证。如果 mean pooling 一致优于 BiGRU，那 BiGRU 组件的存在意义是什么？
- 建议：为 mean pooling 实验补充多 seed、多变体结果。如果 mean pooling 确实更好，需要重新审视 Stage 2 设计的 motivation。

**W7** [warning] Limitations section 格式不符合 ACL/ARR 要求
- 具体位置：Section 6 (Conclusion)
- 问题：Limitations 作为 `\paragraph{Limitations and future work.}` 嵌入在 Conclusion 中，而非独立的 `\section{Limitations}`。ACL ARR 明确要求 Limitations 是一个单独的 section（不计入页数限制），内容应实质性地讨论局限。当前格式可能导致在 submission checklist 中被标记为不符合要求。同时，Future Work 应与 Limitations 分开。
- 建议：将 Limitations 拆分为独立的 `\section{Limitations}`，放在 Conclusion 之后、References 之前。Future Work 可保留在 Conclusion 中或也独立成节。

---

## 小问题（不影响接收）

1. **Fig 1 (Architecture)**: Stage 1 和 Stage 2 的标题文字在图中有重叠。"Frozen [CLS] embeddings" 标签位置与 "Training Objectives" 框有视觉冲突。建议调整布局。
2. **Fig 3 (Strategy Heatmap)**: 作为 `figure*`（双栏宽），三个子图的轴标签字体偏小（尤其是策略名称），打印后可能不清晰。建议增大字体或减少轴标签密度。
3. **缩写 "pp"（percentage points）**: 在 Abstract 和正文中多次使用但未定义。虽然 NLP 社区常用，建议首次使用时给出全称。
4. **Introduction 中有一处 "additionally"**（Section 1, Contribution 2 最后一句: "The persuasion taxonomy additionally provides distinct strategy trajectories per attack type"），属于 AI 写作风格词汇。建议改为更自然的表述。
5. **references.bib 文件头注释 "Total entries: 31" 与实际条目数 (36) 不符**。这不影响编译，但反映 bib 维护不够严谨。
6. **部分引用条目有轻微问题**: `han2024wildguard` 的 first author 与 OpenAlex 记录不匹配（bib: Han vs API: Choi）；`chao2023pair` 年份与正式发表年份不匹配（bib: 2023, 正式发表: 2025）。建议核实并更新。
7. **-ing 分词短语**: 正文中存在少量句末 -ing 结构（如 experiments.tex: "reflecting inherent lexical separability when test matches training"），虽不严重但可优化为独立句。
8. **全文未发现 em-dash (—) 或解释性 en-dash (–) 的滥用**，无 delve/leverage/utilize/facilitate/myriad/plethora 等 AI 高频词（除上述一处 "additionally"），AI 痕迹控制总体良好。

---

## 缺失引用

1. **计算说服检测**: 论文的 9-class taxonomy 基于 PAP 和 Cialdini，但缺少 computational persuasion detection 的实证工作引用（如 propaganda detection, persuasion technique identification 相关的 SemEval shared tasks）。
2. **Adversarial NLP robustness**: Perturbation analysis 是论文的重要贡献之一，但 adversarial robustness in NLP 的基础文献引用不足（如 TextFooler, BERT-Attack 等对抗性文本攻击方法）。
3. **Probing classifiers**: 论文讨论了 representation 层面的 domain adaptation，但未引用 probing classifier 相关文献（如 Hewitt & Manning 2019, Belinkov & Glass 2019），这些方法可以直接验证 "模型是否学到了语用特征" 的 claim。
4. **引用总量**: 36 条引用对于 EMNLP 长文偏少。同类论文通常在 40-60 条范围。建议扩充上述缺失方向的引用。

---

## 主要优势

1. **实验设计思路优秀**: 7 个 Stage-1 变体的消融设计是论文最大亮点。每个变体精准隔离一个因素（domain exposure, classification supervision, label quality, label granularity, domain specificity），实验逻辑清晰。这种 controlled decomposition 的方法论本身对社区有参考价值。
2. **问题定位准确**: "What enables cross-attack generalization?" 是 multi-turn jailbreak defense 领域的一个 under-explored question。从 representation learning 角度系统分析而非仅追求 SOTA 数字，是有价值的研究方向。
3. **诚实的局限性讨论**: 论文坦诚承认 TF-IDF 的强表现、数据规模的局限性、单 seed 变体的不足。这种科学诚实值得肯定。
4. **写作质量总体可控**: AI 写作痕迹少，叙事有一定连贯性，技术描述准确。虽然 Abstract 数字过密、narrative framing 有优化空间，但不构成写作层面的硬伤。
5. **Perturbation robustness 的三层归因**: 虽然样本量小，但 classification structure → label correctness+granularity → independent contribution 的三层发现如果在更大规模上验证，将是有价值的 insight。

---

## 对 Director 提出的特定问题的回应

**Q1: 核心发现（DAPT 是主要机制）是否足够新颖？**
不够新颖作为 methods contribution。Gururangan et al. (2020) 已经在 4 个 domain 上系统验证了 DAPT 的有效性。将其应用到 jailbreak detection 是 straightforward 的 engineering application。论文的增量在于消融的系统性，而非 DAPT 本身。如果定位为 empirical study，需要更大的实验规模。

**Q2: "partially falsified" 叙事策略是否有效？**
对接收有负面影响。它暗示作者缺乏明确的初始假设，使 contribution 显得模糊。建议改为正面 framing。

**Q3: 7 个变体消融是否构成方法贡献？**
消融设计是方法论贡献（how to decompose representation learning factors），但具体结论（DAPT works）不是。这更适合 Findings track。

**Q4: Related Work gap 声明是否准确？**
"none systematically analyze why some representations generalize" 措辞过强。DeepContext 和 BIID 都在探索 representation-level 的方案。更准确的 gap 应是 "none provide controlled ablation to isolate the contributing factors"。

**Q5: 标题是否与内容匹配？**
标题 "What Makes Multi-Turn Jailbreaks Detectable?" 与内容匹配。副标题 "Domain Exposure Bridges the Cross-Attack Gap" 准确概括核心发现。

**Q6: 引用密度是否足够？**
36 条偏少，建议补充至 45-50 条。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-18T08:47:47.802369+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "persuasion_turn_jailbreak_detect",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2（侧重新颖性 + 完整性 + 写作质量）的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n重点关注与你自己意见有分歧或互补的部分。\n\n---\n\n### Reviewer 2 完整审稿意见\n\n**Overall**: 2.5/5 (Borderline Findings)\n\n**Must-Fix 问题：**\n\n**N1** [critical] 实验规模过小，无法支撑\"reframe multi-turn jailbreak detection as primarily a domain adaptation problem\"的核心 claim\n- 训练集仅 250 jailbreak + 250 benign，OOD 测试仅 80 FITD + 80 DD，perturbation 测试仅 n=76\n- 核心 claim 的证据强度与 claim 的广度严重不匹配\n- 建议：扩大数据集或显著降低 claim 强度\n\n**N2** [critical] 缺少与直接竞争方法（DeepContext、BIID、G-Guard、SafeDream）的实验对比\n- Related Work 定位了 4 个 direct competitors 但 Experiments 无头对头比较\n- 唯一 baselines 是 vanilla DeBERTa、TF-IDF LR 和 LLM-as-judge\n\n**N3** [critical] 有效 OOD 评估实质上是 single-dataset evaluation\n- FITD 对方法几乎没有区分度（9-class 和 vanilla 均 F1≥0.990）\n- 7 个变体消融对比实际上只在 DD 一个数据集上有意义\n- 单数据集消融结论可能受该特定 attack type 特性影响\n\n**N4** [critical] 变体间 seed 报告不一致，影响统计可比性\n- binary 和 scrambled 只报告 seed 42，其他变体 3-seed\n- 这两个变体在 evidence hierarchy 中处于关键位置\n\n**Should-Fix 问题：**\n\n**W1** [warning] Abstract 过度堆砌数据（约 180 词含大量 F1 数字），读起来像压缩版 Results\n- 建议保留 2-3 个关键数字，聚焦叙事弧\n\n**W2** [warning] \"partially falsified our original hypothesis\" 叙事策略对接收有负面影响\n- 暗示作者缺乏明确初始假设，使 contribution 显得模糊\n- 建议改为正面框架：\"We discover that domain exposure, rather than task-specific supervision, is the primary mechanism\"\n\n**W3** [warning] Contributions 列表过于密集（两个 bullet 各约 60-80 词），难以快速提取核心 claim\n- 建议拆分为 3-4 个简短 bullets\n\n**W4** [warning] TF-IDF baseline 的强表现（DD-Full 0.944）未被充分讨论\n- 如果词袋模型就能达到 0.944，\"domain-adaptive pretraining captures pragmatic features\" 的解释是否可靠？\n- 建议增加特征分析实验（probing/attention 可视化）\n\n**W5** [warning] Strategy Trajectory Analysis 使用 ground-truth labels 而非模型预测\n- Figure 3 用 Qwen3-8B 标注的 ground-truth labels，不是 9-class 模型在 OOD 数据上的预测\n- 展示的是数据集特性而非模型可解释性能力\n- 建议补充 OOD 策略预测准确率\n\n**W6** [warning] Mean Pooling 达 F1=1.000 但仅单 seed、单变体，结论过强\n- 如果 mean pooling 一致优于 BiGRU，BiGRU 存在意义是什么？\n\n**W7** [warning] Limitations 作为 `\\paragraph` 嵌入 Conclusion 而非独立 `\\section{Limitations}`，不符合 ACL ARR 格式要求\n\n**新颖性判断：**\n- 核心发现（DAPT 是主要机制）方法论上不够新颖，Gururangan et al. (2020) 已成熟\n- 增量在消融的系统性而非 DAPT 本身\n- 更适合 Findings track\n- \"none systematically analyze why\" 的 gap 声明过强\n\n**缺失引用：**\n- computational persuasion detection 实证工作（SemEval propaganda detection tasks）\n- adversarial NLP robustness 基础文献（TextFooler, BERT-Attack）\n- probing classifiers（Hewitt & Manning 2019, Belinkov & Glass 2019）\n- 总量 36 条偏少，建议 45-50 条\n\n---\n\n请对以上每个 Must-Fix（N1-N4）和 Should-Fix（W1-W7）逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "persuasion_turn_jailbreak_detect",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2（侧重新颖性 + 完整性 + 写作质量）的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n重点关注与你自己意见有分歧或互补的部分。\n\n---\n\n### Reviewer 2 完整审稿意见\n\n**Overall**: 2.5/5 (Borderline Findings)\n\n**Must-Fix 问题：**\n\n**N1** [critical] 实验规模过小，无法支撑\"reframe multi-turn jailbreak detection as primarily a domain adaptation problem\"的核心 claim\n- 训练集仅 250 jailbreak + 250 benign，OOD 测试仅 80 FITD + 80 DD，perturbation 测试仅 n=76\n- 核心 claim 的证据强度与 claim 的广度严重不匹配\n- 建议：扩大数据集或显著降低 claim 强度\n\n**N2** [critical] 缺少与直接竞争方法（DeepContext、BIID、G-Guard、SafeDream）的实验对比\n- Related Work 定位了 4 个 direct competitors 但 Experiments 无头对头比较\n- 唯一 baselines 是 vanilla DeBERTa、TF-IDF LR 和 LLM-as-judge\n\n**N3** [critical] 有效 OOD 评估实质上是 single-dataset evaluation\n- FITD 对方法几乎没有区分度（9-class 和 vanilla 均 F1≥0.990）\n- 7 个变体消融对比实际上只在 DD 一个数据集上有意义\n- 单数据集消融结论可能受该特定 attack type 特性影响\n\n**N4** [critical] 变体间 seed 报告不一致，影响统计可比性\n- binary 和 scrambled 只报告 seed 42，其他变体 3-seed\n- 这两个变体在 evidence hierarchy 中处于关键位置\n\n**Should-Fix 问题：**\n\n**W1** [warning] Abstract 过度堆砌数据（约 180 词含大量 F1 数字），读起来像压缩版 Results\n- 建议保留 2-3 个关键数字，聚焦叙事弧\n\n**W2** [warning] \"partially falsified our original hypothesis\" 叙事策略对接收有负面影响\n- 暗示作者缺乏明确初始假设，使 contribution 显得模糊\n- 建议改为正面框架：\"We discover that domain exposure, rather than task-specific supervision, is the primary mechanism\"\n\n**W3** [warning] Contributions 列表过于密集（两个 bullet 各约 60-80 词），难以快速提取核心 claim\n- 建议拆分为 3-4 个简短 bullets\n\n**W4** [warning] TF-IDF baseline 的强表现（DD-Full 0.944）未被充分讨论\n- 如果词袋模型就能达到 0.944，\"domain-adaptive pretraining captures pragmatic features\" 的解释是否可靠？\n- 建议增加特征分析实验（probing/attention 可视化）\n\n**W5** [warning] Strategy Trajectory Analysis 使用 ground-truth labels 而非模型预测\n- Figure 3 用 Qwen3-8B 标注的 ground-truth labels，不是 9-class 模型在 OOD 数据上的预测\n- 展示的是数据集特性而非模型可解释性能力\n- 建议补充 OOD 策略预测准确率\n\n**W6** [warning] Mean Pooling 达 F1=1.000 但仅单 seed、单变体，结论过强\n- 如果 mean pooling 一致优于 BiGRU，BiGRU 存在意义是什么？\n\n**W7** [warning] Limitations 作为 `\\paragraph` 嵌入 Conclusion 而非独立 `\\section{Limitations}`，不符合 ACL ARR 格式要求\n\n**新颖性判断：**\n- 核心发现（DAPT 是主要机制）方法论上不够新颖，Gururangan et al. (2020) 已成熟\n- 增量在消融的系统性而非 DAPT 本身\n- 更适合 Findings track\n- \"none systematically analyze why\" 的 gap 声明过强\n\n**缺失引用：**\n- computational persuasion detection 实证工作（SemEval propaganda detection tasks）\n- adversarial NLP robustness 基础文献（TextFooler, BERT-Attack）\n- probing classifiers（Hewitt & Manning 2019, Belinkov & Glass 2019）\n- 总量 36 条偏少，建议 45-50 条\n\n---\n\n请对以上每个 Must-Fix（N1-N4）和 Should-Fix（W1-W7）逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-18T08:48:20.162724+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 32360
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-18T08:48:20.364617+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "persuasion_turn_jailbreak_detect",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1（侧重方法严谨性 + 实验有效性）的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n重点关注与你自己意见有分歧或互补的部分。\n\n---\n\n### Reviewer 1 完整审稿意见\n\n**Overall**: 2/5 (Resubmit next cycle)\n\n**Must-Fix 问题：**\n\n**N1** [critical] Evidence hierarchy 的统计基础不一致：single-seed vs 3-seed 比较\n- binary/scrambled 仅 seed 42，其他变体 3-seed\n- \"scrambled (0.990) ≈ binary (0.990)\" 无方差信息\n- 论文从中推导因果性结论：\"Label quality and granularity are non-factors for detection\"、\"classification objective functions as a regularizer\"\n- 这些 claims 建立在两个 single-seed 数据点的巧合相等上\n\n**N2** [critical] Three-layer robustness attribution 在 n=76 上缺乏统计显著性\n- Δ=2.6pp ≈ 2 个样本差异，Δ=5.3pp ≈ 4 个样本，Δ=9.2pp ≈ 7 个样本\n- 无 McNemar's test、bootstrap CI、permutation test\n- Three-layer attribution 是第二项核心 contribution，占正文约 1/3 讨论\n- 建议：扩大 perturbation test set 至 n≥300，或报告 significance tests，或降级为 \"observed pattern\"\n\n**N3** [critical] 缺少与已发表 multi-turn defense 系统的直接实验对比\n- DeepContext/BIID/G-Guard/SafeDream 仅讨论未实验\n- 实际 baselines 仅为 vanilla DeBERTa、TF-IDF LR、LLM-as-judge\n- 至少应复现 DeepContext（BERT + RNN，结构简单）\n\n**N4** [critical] 数据集规模过小，影响所有核心 claims 的可信度\n- 500 训练、160 OOD 测试、76 IID 测试、76 perturbation\n- n=80 DD 上每个 misclassification 改变 F1 约 1.25pp\n- 区分 0.990 和 0.997 在统计上无意义\n\n**Should-Fix 问题：**\n\n**W1** [warning] Mean pooling = BiGRU 结论基于 single seed\n- Mean pooling DD-Full/K=2 均为 1.000（单 seed 42）\n- vs BiGRU 9-class 3-seed mean 0.997±0.005\n- 在 n=80 上 1.000 vs 0.997 = 0 vs ~0.24 个错误，统计上无意义\n\n**W2** [warning] 策略标注质量验证不充分（Qwen3-8B, κ=0.78, n=50）\n- 9 个类别 n=50 意味着每类约 5-6 个验证样本\n- κ=0.78 在 n=50 时 CI 很宽\n- three-layer attribution 中 \"correct labels\" 优势依赖标注质量\n- 建议增加人工验证至 200+\n\n**W3** [warning] LLM-as-judge baseline 仅测 IID，未测 OOD\n- 论文核心贡献是 OOD generalization，LLM baseline 不测 OOD 是不公平比较\n\n**W4** [warning] TF-IDF LR 的强表现未被充分讨论\n- DD-Full 0.944 vs 9-class 0.997 仅差 5.3pp\n- perturbation 下 TF-IDF 仅降 1.3pp vs 9-class 0pp，在 n=76 上不具统计显著性\n- DisPeD 相对 TF-IDF 的真正增量在哪里？\n\n**W5** [warning] 可复现性不足\n- Stage-2 缺 learning rate, batch size, optimizer, warmup\n- 数据生成 pipeline 细节不足\n- 无代码/数据发布承诺\n- 策略标注 prompt 未提供\n\n**W6** [warning] FITD 评估贡献有限\n- FITD 结果几乎全为 perfect，对方法无区分度\n- OOD claims 实际仅依赖 DD 一种 attack type\n\n**小问题：**\n- Fig 1 Stage 1/Stage 2 标题重叠\n- Fig 3 单栏下字体过小\n- 部分引用 year 不一致（chao2023pair, austin1962speechacts）\n- binary/scrambled 仅 seed 42 原因未说明\n- 缺少各变体计算成本信息\n- 仅用 user turns 的假设需更多讨论\n\n---\n\n请对以上每个 Must-Fix（N1-N4）和 Should-Fix（W1-W6）逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "persuasion_turn_jailbreak_detect",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1（侧重方法严谨性 + 实验有效性）的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n重点关注与你自己意见有分歧或互补的部分。\n\n---\n\n### Reviewer 1 完整审稿意见\n\n**Overall**: 2/5 (Resubmit next cycle)\n\n**Must-Fix 问题：**\n\n**N1** [critical] Evidence hierarchy 的统计基础不一致：single-seed vs 3-seed 比较\n- binary/scrambled 仅 seed 42，其他变体 3-seed\n- \"scrambled (0.990) ≈ binary (0.990)\" 无方差信息\n- 论文从中推导因果性结论：\"Label quality and granularity are non-factors for detection\"、\"classification objective functions as a regularizer\"\n- 这些 claims 建立在两个 single-seed 数据点的巧合相等上\n\n**N2** [critical] Three-layer robustness attribution 在 n=76 上缺乏统计显著性\n- Δ=2.6pp ≈ 2 个样本差异，Δ=5.3pp ≈ 4 个样本，Δ=9.2pp ≈ 7 个样本\n- 无 McNemar's test、bootstrap CI、permutation test\n- Three-layer attribution 是第二项核心 contribution，占正文约 1/3 讨论\n- 建议：扩大 perturbation test set 至 n≥300，或报告 significance tests，或降级为 \"observed pattern\"\n\n**N3** [critical] 缺少与已发表 multi-turn defense 系统的直接实验对比\n- DeepContext/BIID/G-Guard/SafeDream 仅讨论未实验\n- 实际 baselines 仅为 vanilla DeBERTa、TF-IDF LR、LLM-as-judge\n- 至少应复现 DeepContext（BERT + RNN，结构简单）\n\n**N4** [critical] 数据集规模过小，影响所有核心 claims 的可信度\n- 500 训练、160 OOD 测试、76 IID 测试、76 perturbation\n- n=80 DD 上每个 misclassification 改变 F1 约 1.25pp\n- 区分 0.990 和 0.997 在统计上无意义\n\n**Should-Fix 问题：**\n\n**W1** [warning] Mean pooling = BiGRU 结论基于 single seed\n- Mean pooling DD-Full/K=2 均为 1.000（单 seed 42）\n- vs BiGRU 9-class 3-seed mean 0.997±0.005\n- 在 n=80 上 1.000 vs 0.997 = 0 vs ~0.24 个错误，统计上无意义\n\n**W2** [warning] 策略标注质量验证不充分（Qwen3-8B, κ=0.78, n=50）\n- 9 个类别 n=50 意味着每类约 5-6 个验证样本\n- κ=0.78 在 n=50 时 CI 很宽\n- three-layer attribution 中 \"correct labels\" 优势依赖标注质量\n- 建议增加人工验证至 200+\n\n**W3** [warning] LLM-as-judge baseline 仅测 IID，未测 OOD\n- 论文核心贡献是 OOD generalization，LLM baseline 不测 OOD 是不公平比较\n\n**W4** [warning] TF-IDF LR 的强表现未被充分讨论\n- DD-Full 0.944 vs 9-class 0.997 仅差 5.3pp\n- perturbation 下 TF-IDF 仅降 1.3pp vs 9-class 0pp，在 n=76 上不具统计显著性\n- DisPeD 相对 TF-IDF 的真正增量在哪里？\n\n**W5** [warning] 可复现性不足\n- Stage-2 缺 learning rate, batch size, optimizer, warmup\n- 数据生成 pipeline 细节不足\n- 无代码/数据发布承诺\n- 策略标注 prompt 未提供\n\n**W6** [warning] FITD 评估贡献有限\n- FITD 结果几乎全为 perfect，对方法无区分度\n- OOD claims 实际仅依赖 DD 一种 attack type\n\n**小问题：**\n- Fig 1 Stage 1/Stage 2 标题重叠\n- Fig 3 单栏下字体过小\n- 部分引用 year 不一致（chao2023pair, austin1962speechacts）\n- binary/scrambled 仅 seed 42 原因未说明\n- 缺少各变体计算成本信息\n- 仅用 user turns 的假设需更多讨论\n\n---\n\n请对以上每个 Must-Fix（N1-N4）和 Should-Fix（W1-W6）逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-18T08:48:22.079645+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1715
}
```

</details>

---


### Assistant

_source line 80 · 2026-05-18T08:48:24.471260+00:00_

交叉分享已发送给两位 Reviewer，等待逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 5

## Round 5

2 recorded events


### User

_source line 81 · 2026-05-18T08:48:27.343258+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿完成，已通过 `review_reviewer_post_to_director` 提交给 Review Director。

审稿摘要：

- **Overall: 2.5/5 (Borderline Findings)**
- **Soundness: 3/5**, **Excitement: 2.5/5**

**4 个 Must-Fix (Critical) 问题**：
1. 实验规模过小（500训练+160 OOD），无法支撑将 multi-turn jailbreak detection "reframe as domain adaptation problem" 的宏大 claim
2. 缺少与 4 个直接竞争方法（DeepContext/BIID/G-Guard/SafeDream）的实验对比
3. 有效 OOD 评估实质上只在 DD 单数据集上有区分度（FITD 上所有方法都≥0.990）
4. Binary/scrambled 变体只报告单 seed，而它们在 evidence hierarchy 中处于关键位置

**7 个 Should-Fix (Warning) 问题**：Abstract 数字堆砌、"partially falsified" 叙事策略不利、Contributions 密度过高、TF-IDF 强表现讨论不充分、Strategy Trajectory 用的是 ground-truth labels 而非模型预测、Mean Pooling 实验讨论不充分、Limitations 格式不符合 ACL/ARR 独立 section 要求。

**主要优势**：7 变体消融设计优秀、问题定位有价值、局限性讨论诚实、AI 写作痕迹控制良好。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 82 · 2026-05-18T08:48:31.749982+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 6

## Round 6

2 recorded events


### User

_source line 83 · 2026-05-18T08:49:52.148212+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 交叉回应 — 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: 实验规模过小，无法支撑核心 claim**

同意。这与我的 N4 完全一致。补充一点量化论据：在 n=80 的 DD 测试集上，单个 misclassification 改变 F1 约 1.25pp，这意味着 evidence hierarchy 中 0.990 vs 0.997 的差异仅对应约 0.5 个错误样本（3-seed 平均），在统计上不可区分。论文 Conclusion 自己也承认 "The dataset is small (500 training, 160 OOD test conversations) and synthetically generated by Qwen3-8B, which may not capture the full diversity of real-world attack strategies"，但论文主体的 claim 强度并未因此降低。R2 建议 "扩大数据集或显著降低 claim 强度" 是合理的——至少应做到其中一项。

**[AGREE] R2-N2: 缺少与直接竞争方法的实验对比**

完全同意。这与我的 N3 一致。论文在 Introduction（Section 1 para 2）和 Related Work（Section 2 "Multi-turn defenses" 段）中明确将 DeepContext、BIID、G-Guard、SafeDream 定位为 "existing multi-turn defenses"，并声称它们 "do not decompose what enables cross-attack generalization"。但如果不在相同实验条件下对比，就无法证明 DisPeD 相对这些方法的真实增量。至少 DeepContext（BERT + recurrent network）的架构足够简单，应该可以复现。

**[AGREE] R2-N3: 有效 OOD 评估实质上是 single-dataset evaluation**

同意，且认为 R2 将此提升为 critical 是合理的。我在自己的审稿中将此作为 W6（should-fix）处理，现在认为应该更严厉。

具体证据：Appendix B Table 7 显示 FITD 在几乎所有变体和 prefix 长度上都接近 perfect F1：9-class 全 prefix 1.000，vanilla 在 K=1 时 0.990、K=2 和 Full 时 1.000。这意味着 FITD 对论文的核心问题（什么使跨攻击泛化成为可能？）提供的区分度为零。

论文实质上是在单一 OOD attack type（Deceptive Delight）上做消融分析，然后将结论泛化为 "cross-attack generalization" 的通用机制。DD 可能有特殊属性（例如其 emotion-based manipulation 风格可能特别容易被 MLM 捕获），使得当前发现不具普遍性。这一点严重削弱了 "reframe multi-turn jailbreak detection as primarily a domain adaptation problem" 这一核心 claim 的外部效度。

**[AGREE] R2-N4: 变体间 seed 报告不一致**

完全同意。这是我自己审稿中的 N1（第一条 critical issue）。R2 简洁地抓住了要害："这两个变体在 evidence hierarchy 中处于关键位置"。

补充我的原始分析：binary 和 scrambled 在 evidence hierarchy 中的位置（0.990）正好处于 MLM（0.914±0.115）和 9-class（0.997±0.005）之间，这一排序对于 "classification supervision adds stability over MLM" 和 "label quality is a non-factor for detection" 两项 claim 都至关重要。如果 binary/scrambled 的 3-seed 结果表现出类似 MLM 的高方差（例如某个 seed 降到 0.85），整个 evidence hierarchy 的解释框架就需要重写。

---

### Should-Fix 问题

**[AGREE] R2-W1: Abstract 过度堆砌数据**

同意。Abstract（约 180 词）包含至少 10 个具体 F1 数字和 2 个标准差值。这远超论文写作规范建议的 "最多引用 2-3 个关键数字"。当前 Abstract 读起来确实像压缩版 Results，而非独立的叙事单元。

建议保留的关键数字：(1) vanilla OOD collapse（0.28），(2) MLM 的 OOD recovery（≥0.97 at early turns），(3) 9-class 的最终表现（0.997±0.005）。其他数字应移至正文。

**[AGREE with nuance] R2-W2: "partially falsified" 叙事策略**

部分同意。我在自己的审稿中将 "partially falsified" 列为优势之一（"知识诚实地报告 partially falsified 假设……这种诚实的科学态度在论文中并不常见"）。从科学诚信角度，这种写法值得肯定。

但 R2 的实用主义建议有道理——"We discover that domain exposure, rather than task-specific supervision, is the primary mechanism" 这一正面框架实际上与论文的最终结论完全一致，且对审稿人更友好。关键是：论文可以在叙事上做正面框架，同时在 Discussion 中诚实地提及原始假设被修正的过程。两者不矛盾。

不过，我不同意 R2 说这 "暗示作者缺乏明确初始假设"——恰恰相反，有明确假设才能被 falsify。问题不在于科学态度，而在于修辞效果。建议作者权衡取舍。

**[AGREE] R2-W3: Contributions 列表过于密集**

同意。Introduction 的两条 contributions 各约 60-80 词，尤其第二条（"Classification supervision adds stability, robustness, and interpretability"）试图在单个 bullet 中塞入 three-layer attribution 的完整描述（包括 K=1, K=2, full 三个层次的具体数字）。这对快速扫描 Introduction 的审稿人不友好。

建议拆为 4 条：(1) 系统消融设计，(2) domain exposure 是主要机制，(3) classification supervision 提供稳定性和鲁棒性，(4) 策略轨迹的可解释性。每条控制在 30-40 词。

**[AGREE] R2-W4: TF-IDF baseline 强表现未充分讨论**

完全同意。这与我的 W4 一致。R2 额外提出的 "如果词袋模型就能达到 0.944，'domain-adaptive pretraining captures pragmatic features' 的解释是否可靠？" 是一个尖锐的好问题。

如果 TF-IDF（纯词频特征）能在 OOD 上达到 0.944，这暗示当前数据集存在显著的 lexical shortcuts（论文在 Section 2 最后一段和 Conclusion 都承认了这一点）。那么 MLM/classification 变体的高 F1 是否也主要依赖词汇特征而非 "pragmatic features（hedging, escalation markers, topic-shifting patterns）"（Section 5.2 的解释）？R2 建议的 probing/attention 可视化实验是验证这一问题的正确方法。

**[AGREE] R2-W5: Strategy Trajectory Analysis 使用 ground-truth labels 而非模型预测**

同意。这是一个我遗漏的重要问题。

Figure 3 caption 明确说 "based on ground-truth intended strategy labels"，Section 5.4 也确认使用 ground-truth labels。但论文的 interpretability claim（Introduction contribution #2: "interpretability through strategy trajectories"）暗示 9-class 模型的预测能提供可解释性。Figure 3 展示的是数据集本身的策略分布特性（由 Qwen3-8B 标注生成），而非 DisPeD 9-class 模型在 OOD 数据上的预测能力。

这个区别至关重要：如果 9-class 模型在 OOD 数据上的策略预测准确率很低，那么 "interpretability through strategy trajectories" 这一 contribution 就不成立——模型可以检测 jailbreak（binary F1=0.990 也行），但无法正确解释为什么。

R2 建议 "补充 OOD 策略预测准确率" 是必要的。

**[AGREE] R2-W6: Mean Pooling 结论过强**

完全同意。这与我的 W1 一致。R2 补充的问题 "如果 mean pooling 一致优于 BiGRU，BiGRU 存在意义是什么？" 值得论文回答。当前论文的架构选择（BiGRU 作为 Stage-2 aggregator）与其自己的实验发现（mean pooling = BiGRU）存在张力。

**[AGREE] R2-W7: Limitations 格式不符合 ACL ARR 要求**

同意。ACL ARR 要求 Limitations 作为独立 section（`\section{Limitations}`），而非嵌入 Conclusion 的 `\paragraph`。这是一个简单但必须修复的格式问题。论文当前使用 `\paragraph{Limitations and future work.}` 放在 Section 6 (Conclusion) 内，不符合 ACL 2023+ 的格式要求。

---

### 对 R2 新颖性判断的回应

**[AGREE with nuance]** R2 认为核心发现（DAPT 是主要机制）方法论上不够新颖，增量在消融的系统性而非 DAPT 本身。

我同意新颖性主要在于 **消融实验的系统设计** 和 **将 DAPT 思想应用于 jailbreak detection 的具体验证**，而非 DAPT 技术本身。Gururangan et al. (2020) 的 DAPT 方法论确实已成熟，但将其应用于多轮 jailbreak 检测并系统分解各因素贡献是新的。

对于 "none systematically analyze why" 的 gap 声明（Introduction Section 1 para 2），R2 认为过强。我部分同意——该声明的严格版本需要对所有相关工作进行穷尽性调查，但论文引用的 4 个 multi-turn defense 确实未做此类分解。建议改为更温和的表述如 "existing systems achieve reasonable in-distribution performance but provide limited insight into which representation properties drive cross-attack generalization"。

**[AGREE with nuance]** R2 认为更适合 Findings track。在当前版本下（统计问题未解决、baselines 不充分），我同意 Findings track 更合适。如果所有 critical issues 修复（完整 multi-seed、更大数据集、baseline 对比），主会议长文也是可能的。

---

### 对 R2 缺失引用的回应

**[AGREE]** SemEval propaganda detection tasks 确实与 computational persuasion detection 相关，应在 Related Work "Discourse analysis and computational persuasion" 段引用。

**[AGREE]** adversarial NLP robustness 文献（TextFooler, BERT-Attack）与 Section 5.3 perturbation robustness 分析直接相关。论文使用 "adversarial paraphrasing"（BERTScore 0.92, lexical overlap 0.20）但未引用这些基础工作。

**[AGREE]** probing classifiers 文献（Hewitt & Manning 2019, Belinkov & Glass 2019）与论文的核心问题高度相关——如果要声称 DAPT "captures pragmatic features"，probing experiments 是验证这一解释的标准方法。缺少这些引用同时也暗示论文缺少相应的分析实验。

**[REBUT]** 关于引用总量（36 条偏少，建议 45-50 条）：36 条对于 8 页 EMNLP 论文处于合理范围的低端，但引用数量本身不应作为评判标准。问题不在于 "数量不够"，而在于 **特定方向的覆盖缺失**（如 R2 具体指出的三个方向）。如果补充这些方向的关键引用，总量自然会增加。但不应为凑数而添加无关引用。

---

### 总结

R2 的 4 项 Must-Fix 中有 3 项与我的独立发现一致（N1=我的N4, N2=我的N3, N4=我的N1），N3 将我的 W6 合理升级为 critical。两位 reviewer 的核心关切高度一致：**统计严谨性不足、数据规模过小、缺少 baseline 对比**。

R2 的 Should-Fix 中，W5（strategy trajectory analysis 使用 ground-truth labels 而非模型预测）是我遗漏的重要发现，直接影响 "interpretability" contribution 的成立。W7（Limitations 格式）也是我未注意到的格式问题。

两位 reviewer 的主要分歧仅在 "partially falsified" 的叙事策略上（我认为是优势，R2 认为有负面影响），但这属于修辞偏好而非实质性分歧。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 84 · 2026-05-18T08:50:01.390061+00:00_

Reviewer 1 的交叉回应已收到，等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 7

## Round 7

2 recorded events


### User

_source line 85 · 2026-05-18T08:50:04.276267+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

核心结论：两位 reviewer 的意见高度一致。R2 的 4 项 Must-Fix 中 3 项与我独立发现重合（数据规模不足、缺少 baseline 对比、seed 报告不一致），第 4 项（OOD 评估实质上是 single-dataset）将我的 should-fix 合理升级为 critical。我对 R2 的 11 条意见中 9 条给出 [AGREE]，2 条 [AGREE with nuance]（"partially falsified" 叙事策略、新颖性判断），1 条 [REBUT]（引用数量本身不应作为标准，关键是特定方向的覆盖缺失）。R2 的 W5（Figure 3 用 ground-truth labels 而非模型预测）是我遗漏的重要发现。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 86 · 2026-05-18T08:50:08.856173+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 8

## Round 8

6 recorded events


### User

_source line 87 · 2026-05-18T08:50:19.934511+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — 交叉回应 Reviewer 1 审稿意见

---

## Must-Fix 问题回应

**[AGREE] R1-N1: Evidence hierarchy 的统计基础不一致（single-seed vs 3-seed）**

完全同意，我在自己的 N4 中也将此标记为 critical。

R1 的分析比我更精确：binary 和 scrambled 的 F1=0.990 均来自单次 seed 42，而论文从中推导的因果性 claim "Label quality and granularity are non-factors for detection"（Section 4.4, para 1）和 "classification objective functions as a regularizer that shapes representation geometry regardless of whether the labels carry meaningful semantic information"（Section 4.4, para 1）逻辑跳跃过大。

补充一点 R1 未提及的：topic 变体（3-seed: 0.541±0.207）表明某些变体在不同 seeds 下方差极大（seed 123 甚至低于 vanilla 的 0.284，见 Section 4.4, Misaligned supervision 段）。这恰恰说明 single-seed 结果完全可能是不稳定的。如果 binary 或 scrambled 在其他 seeds 下也出现类似的高方差，整个 evidence hierarchy 的中间层（0.99 tier）将坍塌，"classification as regularizer" 的 claim 不成立。

---

**[AGREE] R1-N2: Three-layer robustness attribution 在 n=76 上缺乏统计显著性**

完全同意。我在自己的 N1 中将此作为 "实验规模过小" 的一部分讨论，但 R1 的量化分析更到位。

论文自身也承认这一点："The 76-sample test set means tier boundaries correspond to 1–3 misclassifications; larger-scale evaluation is needed to confirm"（Section 4.3, 最后一句）。问题在于，论文承认了这一局限后，仍然在 Introduction（Contribution 2）和 Conclusion 中将 three-layer attribution 作为核心 contribution 来呈现，没有对 claim 强度做任何降级。

R1 建议的 "降级为 observed pattern" 是最低成本的修改方案。但我认为即使降级措辞，如果 n=76 不变，这部分内容的 contribution 权重也需要大幅削减——不宜占正文约 1/3 的讨论篇幅（R1 的估计准确）。Table 3 的 perturbation 分析可以保留，但 "three-layer attribution" 的叙事框架在缺乏统计检验的情况下不应作为核心 contribution 之一。

---

**[AGREE] R1-N3: 缺少与已发表 multi-turn defense 系统的直接实验对比**

完全同意，我在自己的 N2 中也将此标记为 critical，且分析基本一致。

R1 建议至少复现 DeepContext（BERT + RNN）是合理的——DeepContext 的架构（BERT encoder + recurrent aggregation）与 DisPeD 的 vanilla baseline（DeBERTa + BiGRU）高度相似。区别仅在于：(1) encoder 选择（BERT vs DeBERTa），(2) DeepContext 不做 Stage 1 adaptation。实际上，DisPeD 的 vanilla variant 本身就可以视为 DeepContext 的近似复现（同为 pretrained encoder + RNN，无 domain adaptation）。论文可以在讨论中显式地建立这种联系来部分弥补，但更好的做法是在相同数据上直接复现。

补充：论文在 Related Work 中引用了 DeepContext 的性能数字 "F1 = 0.84 IID, fails OOD"（Section 2, Multi-turn defenses 段），但这是从 DeepContext 原文引用的，不在相同的实验设置下，因此不构成公平对比。

---

**[AGREE] R1-N4: 数据集规模过小**

完全同意，我在自己的 N1 中也将此标记为 critical，且优先级最高。

R1 提供了更精确的量化："n=80 DD 上每个 misclassification 改变 F1 约 1.25pp"。这直接说明了为什么 "区分 0.990 和 0.997 在统计上无意义"——两者差 0.7pp，不足 1 个样本的误差。同理，0.914±0.115 和 0.904±0.115（jailbreak MLM vs Wikipedia MLM，Table 2）的 1pp 差距在 n=80 上毫无统计意义，但论文仍基于此讨论了 "domain specificity is marginal at full length"（Section 4.4, para 2）。

综合 R1-N1 到 R1-N4，我同意 R1 的 overall 判断方向——这些问题联合起来确实严重。不过我对 overall 评分略高于 R1（我给 2.5 vs R1 给 2），原因见下文关于 W4 的讨论。

---

## Should-Fix 问题回应

**[AGREE] R1-W1: Mean pooling = BiGRU 结论基于 single seed**

同意，我在自己的 W6 中也标记了这一点。R1 的分析更精确："在 n=80 上 1.000 vs 0.997 = 0 vs ~0.24 个错误"。这意味着 mean pooling 实验在当前规模下完全无法得出 "detection relies on per-turn representations rather than their sequential order"（Section 4.4, 最后一段）这样的强结论。

---

**[AGREE] R1-W2: 策略标注质量验证不充分（Qwen3-8B, κ=0.78, n=50）**

同意。这是我的审查中未充分讨论的一个有效问题。

论文描述标注过程为 "Strategy annotations are produced by Qwen3-8B with structured prompting... inter-annotator agreement between model annotations and a human sample (n=50) yields Cohen's κ=0.78"（Section 3.2, 9-class variant 段）。

R1 指出 9 类 × n=50 意味着每类约 5-6 个验证样本，这使得 κ=0.78 的置信区间非常宽。更重要的是，three-layer robustness attribution 中 9-class 相对于 scrambled 的优势（"correct labels" 的贡献）直接依赖标注质量。如果 ground-truth labels 本身不可靠（高噪声），则 9-class 和 scrambled 之间的性能差异可能并非来自 "label correctness" 而是来自 noise pattern 的差异。

补充一个与此相关的问题：我在自己的 W5 中指出，Section 4.5 的 strategy trajectory analysis 使用的是 ground-truth labels（Qwen3-8B 标注）而非模型预测，这进一步削弱了标注质量问题的影响评估——因为我们不知道模型自身的策略预测准确率。

---

**[AGREE with nuance] R1-W3: LLM-as-judge baseline 仅测 IID，未测 OOD**

基本同意，但有保留。

R1 的逻辑是正确的：论文核心 contribution 是 OOD generalization，LLM baseline 不测 OOD 确实是不对称比较。

但有一个合理的辩护角度：LLM-as-judge 在 IID 上已经严重失败（GPT-5.5: F1=0.191-0.449, 30-47% unparseable，见 Appendix Table 5），按常理 OOD 表现只会更差。因此 IID 结果已经足以排除 LLM-as-judge 作为有效 baseline 的可能。

不过我同意 R1 的观点，从论文完整性角度，OOD 结果应该报告——即使是 "更差" 的预期结果，报告它也能加强 "content-level reasoning is insufficient" 的 claim（Section 4.1, Models 段）。建议在 Appendix 中补充 OOD 的 LLM-as-judge 结果。

---

**[AGREE] R1-W4: TF-IDF LR 的强表现未被充分讨论**

完全同意，我在自己的 W4 中也标记了这一问题，且分析一致。

补充 R1 未提及的一点：TF-IDF 在 perturbation 下仅降 1.3pp（Table 3, Full 列），且在 K=2 和 K=3 上降幅也不大（4.1pp 和 1.3pp）。论文将 perturbation robustness 作为 DisPeD 相对于 "non-adapted models" 的优势，但实际上 TF-IDF 的 robustness 远好于 vanilla DeBERTa 和 Wikipedia MLM（后两者降 ~12pp），接近 MLM-only（降 2.6pp）。这意味着 "domain exposure provides robustness" 的 claim 部分被 TF-IDF（一个纯词汇统计模型）实现了，进一步质疑了 "pragmatic features" 的机制性解释。

这也是我给 overall 2.5 而非 2 的原因之一——论文至少诚实报告了 TF-IDF 的结果并承认了 lexical separability（Section 4.2, Section 6）。但这种诚实性不能替代对 claim 的实质性修订。

---

**[AGREE] R1-W5: 可复现性不足**

同意。我在 Reproducibility 维度打了 3/5，但未列出具体缺失项。R1 的清单更为具体：

验证 R1 的指控：
- Stage-2 超参数：论文写 "two-layer MLP (256→64→2, ReLU activation, dropout 0.3), 20 epochs"（Section 3.3），确实缺 learning rate, batch size, optimizer, warmup。
- Stage-1 超参数：相对完整——"learning rate 2×10^-5, batch 16, 4 epochs, MLM masking 15%"（Section 4.1），但也未提 optimizer 和 warmup。
- 数据生成：仅写 "generated via Qwen3-8B"（Section 4.1），generation prompt 和 pipeline 未提供。
- 策略标注 prompt：仅写 "structured prompting that includes definitions and examples for each category"（Section 3.2），具体 prompt 未提供。
- 无代码/数据发布承诺。

这些缺失会对 reproducibility 造成实质性影响。建议在 Appendix 中补充完整超参数表、data generation prompt 模板和 annotation prompt。

---

**[AGREE, 但我评级更高] R1-W6: FITD 评估贡献有限**

同意 R1 的判断，但我认为这个问题的严重性高于 Should-Fix。我在自己的 N3 中将此标记为 critical（"有效 OOD 评估实质上是 single-dataset evaluation"）。

原因：论文的核心 claim 是关于 "cross-attack generalization" 的 decomposition。如果只在一个 OOD attack type (DD) 上有区分度，那么 "cross-attack" 的标签名不符实——这更接近 "single-OOD-attack generalization"。FITD 的 perfect performance 实际上证明了 FITD 对当前方法组没有区分度（vanilla 和 9-class 均 F1≥0.990，Appendix Table 4），使得整个消融分析只有 DD 一个 OOD 数据点支撑。

建议将此提升为 Must-Fix：增加至少 2 个难度适中的 OOD attack types，确保消融结论在多数据集上一致。

---

## 综合评价

与 R1 的审稿意见高度一致。四个 Must-Fix 问题（seed 不一致、n=76 统计性、缺少直接对比、规模过小）和大部分 Should-Fix 问题在我的独立审查中也有覆盖。R1 的分析在量化层面（每 pp 对应的样本数、κ 的 CI 问题）比我更精确，我完全认可这些量化论证。

主要分歧点：
1. **FITD 的问题**：我认为是 critical（影响 "cross-attack" claim 的根基），R1 归为 warning。建议 Director 考虑提升。
2. **Overall 评分**：我给 2.5（Borderline Findings），R1 给 2（Resubmit next cycle）。差异来自：我认为 7 变体消融的实验设计思路本身有方法论价值（即使当前执行有缺陷），且论文的诚实性（承认 TF-IDF 强表现、标注 single-seed 局限）在一定程度上加分。但如果 binary/scrambled 的多 seed 结果确认 evidence hierarchy 不稳定，我会将评分降至 2。
3. **写作和叙事问题**：R1 侧重方法严谨性，未充分讨论 Abstract 数据堆砌、"partially falsified" 叙事策略、AI 写作痕迹等写作层面的问题。这些在我的审查中有详细覆盖（W1, W2, W3 及小问题 4, 7, 8），建议 Director 在综合意见中纳入。



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-18T08:52:12.357916+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"Evidence hierarchy 统计基础不一致：binary/scrambled 仅 seed 42，其他变体 3-seed，核心排序无方差支撑\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提 N1，R2 独立发现 N4，交叉回应双方完全同意。binary/scrambled 在 evidence hierarchy 中处于关键位置（区分 label correctness/granularity），单 seed 无法排除 seed-specific artifact。topic 的高方差(0.54±0.21)表明单 seed 可能极不稳定。\"\n    action_items:\n      - round: 1\n        action: \"所有 7 个变体必须报告相同的 3-seed（或更多）mean±std\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2\"\n    summary: \"Three-layer robustness attribution 在 n=76 上缺乏统计显著性（Δ=2.6pp≈2 样本差异），无 significance tests\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提 N2 并量化（2.6pp≈2样本, 5.3pp≈4样本, 9.2pp≈7样本）。R2 在交叉回应中完全同意，建议降级为 observed pattern 或大幅削减讨论篇幅。论文自身承认 tier boundaries=1-3 misclassifications 但未降级 claim 强度。\"\n    action_items:\n      - round: 1\n        action: \"扩大 perturbation test set 至 n≥300，或报告 bootstrap CI/McNemar's test，或将 three-layer attribution 降级为 observed pattern 并削减讨论篇幅\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3\"\n    summary: \"缺少与已发表 multi-turn defense（DeepContext/BIID/G-Guard/SafeDream）的直接实验对比\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提 N3，R2 独立发现 N2，交叉回应完全同意。论文在 Related Work 定位 4 个 direct competitors 但 Experiments 无头对头比较。R2 补充：vanilla variant 本身可视为 DeepContext 近似复现（pretrained encoder + RNN, 无 domain adaptation），应在讨论中显式建立联系。\"\n    action_items:\n      - round: 1\n        action: \"至少复现 DeepContext（BERT+RNN）在相同数据上的结果，或在讨论中显式将 vanilla variant 与 DeepContext 建立联系\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N4\"\n    summary: \"数据集规模过小（500 训练, 160 OOD 测试, 76 perturbation），所有核心 claims 的统计分辨率不足\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提 N4，R2 独立发现 N1（优先级最高）。n=80 DD 上每个 misclassification 改变 F1 约 1.25pp，区分 0.990 vs 0.997（差 0.7pp）统计上无意义。全部由 Qwen3-8B 合成生成，可能不反映真实攻击多样性。\"\n    action_items:\n      - round: 1\n        action: \"扩大数据集规模和来源多样性（多模型生成、人工红队数据），或显著降低 claim 强度并限定为 preliminary findings on synthetic data\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"有效 OOD 评估实质上是 single-dataset（FITD 无区分度，所有变体 F1≥0.990），cross-attack claim 仅由 DD 支撑\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 首提为 N3 critical，R1 原为 W6 warning 但在交叉回应中同意升级为 critical。FITD 在几乎所有变体和 prefix 上接近 perfect，消融分析实质上只在 DD 单数据集有效。cross-attack generalization 的 claim 外部效度严重不足。\"\n    action_items:\n      - round: 1\n        action: \"增加至少 2-3 个难度适中的 OOD attack types（如 ActorAttack, PAIR），使消融结论可在多数据集验证\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"Mean pooling=BiGRU 结论基于 single seed (42)，在 n=80 上 1.000 vs 0.997 统计上无意义\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W1, R2 W6。双方同意。如果 mean pooling 一致优于 BiGRU，BiGRU 作为 Stage-2 的架构选择缺乏 motivation。\"\n    action_items:\n      - round: 1\n        action: \"报告 mean pooling 的 3-seed 多变体结果，弱化因果性结论\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"策略标注质量验证不充分：Qwen3-8B 标注, κ=0.78, 人工验证仅 n=50（每类约 5-6 样本）\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W2, R2 在交叉回应中同意。κ=0.78 在 n=50 时 CI 很宽。three-layer attribution 中 correct labels 的优势依赖标注质量。\"\n    action_items:\n      - round: 1\n        action: \"增加人工验证至 200+（按类别分层抽样），报告每类 κ 或 confusion matrix\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"LLM-as-judge baseline 仅测 IID Crescendo，未测 OOD（FITD/DD）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W3, R2 AGREE with nuance（IID 已严重失败，OOD 预期更差，但完整性要求补充）。\"\n    action_items:\n      - round: 1\n        action: \"在 Appendix 补充 OOD 的 LLM-as-judge 结果\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"TF-IDF LR 强表现（DD-Full 0.944, perturbation 仅降 1.3pp）未被充分讨论，质疑 pragmatic features 的机制性解释\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W4, R2 W4，双方完全同意。TF-IDF robustness 远好于 vanilla/wiki-MLM，接近 MLM-only，暗示 domain exposure provides robustness 的 claim 部分被纯词汇模型实现。建议增加 probing/attention 分析验证是否学到语用特征。\"\n    action_items:\n      - round: 1\n        action: \"更诚实地讨论 TF-IDF 竞争力，增加特征分析实验（probing/attention 可视化），明确 DisPeD 在何种条件下具不可替代优势\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"可复现性不足：Stage-2 缺 lr/batch/optimizer，数据生成 prompt 未提供，标注 prompt 未提供，无代码/数据发布承诺\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W5, R2 在交叉回应中验证并同意所有缺失项。\"\n    action_items:\n      - round: 1\n        action: \"在 Appendix 补充完整超参数表、data generation prompt、annotation prompt，明确代码/数据发布计划\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1\"\n    summary: \"Abstract 过度堆砌数据（~10 个 F1 数字），读起来像压缩版 Results 而非独立叙事单元\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 W1, R1 在交叉回应中同意。建议保留 2-3 个关键数字。\"\n    action_items:\n      - round: 1\n        action: \"精简 Abstract 数字至 2-3 个关键值，聚焦问题→洞察→方法→结论的叙事弧\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2\"\n    summary: \"\\\"partially falsified our original hypothesis\\\" 叙事策略对审稿人接收判断有负面影响\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 W2, R1 AGREE with nuance（科学诚实值得肯定但修辞效果不佳）。分歧属修辞偏好，非实质性矛盾。建议正面框架叙事 + Discussion 中提及假设修正过程。\"\n    action_items:\n      - round: 1\n        action: \"将叙事重构为正面框架，在 Discussion 中保留假设修正的科学过程\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"Contributions 列表过于密集（两条各 60-80 词），难以快速提取核心 claim\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 W3, R1 同意。建议拆为 3-4 条简短 bullets。\"\n    action_items:\n      - round: 1\n        action: \"将 Contributions 拆分为 3-4 条，每条 30-40 词\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W5\"\n    summary: \"Strategy Trajectory Analysis (Figure 3) 使用 ground-truth labels 而非模型预测，展示数据集特性而非模型可解释性\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 W5, R1 在交叉回应中同意（此前遗漏）。如果 9-class 模型在 OOD 上策略预测准确率低，interpretability contribution 不成立。\"\n    action_items:\n      - round: 1\n        action: \"补充 OOD 策略预测准确率，用模型预测 labels 重做 trajectory analysis 与 ground-truth 对比\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W7\"\n    summary: \"Limitations 作为 paragraph 嵌入 Conclusion 而非独立 section，不符合 ACL/ARR 格式要求\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 W7, R1 在交叉回应中同意。ACL ARR 要求 Limitations 为独立 section。\"\n    action_items:\n      - round: 1\n        action: \"将 Limitations 拆分为独立 \\\\section{Limitations}，放在 Conclusion 之后 References 之前\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-REF1\"\n    summary: \"缺失引用：computational persuasion detection（SemEval propaganda tasks）、adversarial NLP robustness（TextFooler/BERT-Attack）、probing classifiers（Hewitt & Manning 2019）\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 在交叉回应中对三个方向均 AGREE，对引用数量 REBUT（关注覆盖方向而非数量）。\"\n    action_items:\n      - round: 1\n        action: \"补充 SemEval propaganda detection、TextFooler/BERT-Attack、probing classifier 相关引用\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect",
    "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"Evidence hierarchy 统计基础不一致：binary/scrambled 仅 seed 42，其他变体 3-seed，核心排序无方差支撑\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提 N1，R2 独立发现 N4，交叉回应双方完全同意。binary/scrambled 在 evidence hierarchy 中处于关键位置（区分 label correctness/granularity），单 seed 无法排除 seed-specific artifact。topic 的高方差(0.54±0.21)表明单 seed 可能极不稳定。\"\n    action_items:\n      - round: 1\n        action: \"所有 7 个变体必须报告相同的 3-seed（或更多）mean±std\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2\"\n    summary: \"Three-layer robustness attribution 在 n=76 上缺乏统计显著性（Δ=2.6pp≈2 样本差异），无 significance tests\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提 N2 并量化（2.6pp≈2样本, 5.3pp≈4样本, 9.2pp≈7样本）。R2 在交叉回应中完全同意，建议降级为 observed pattern 或大幅削减讨论篇幅。论文自身承认 tier boundaries=1-3 misclassifications 但未降级 claim 强度。\"\n    action_items:\n      - round: 1\n        action: \"扩大 perturbation test set 至 n≥300，或报告 bootstrap CI/McNemar's test，或将 three-layer attribution 降级为 observed pattern 并削减讨论篇幅\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3\"\n    summary: \"缺少与已发表 multi-turn defense（DeepContext/BIID/G-Guard/SafeDream）的直接实验对比\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提 N3，R2 独立发现 N2，交叉回应完全同意。论文在 Related Work 定位 4 个 direct competitors 但 Experiments 无头对头比较。R2 补充：vanilla variant 本身可视为 DeepContext 近似复现（pretrained encoder + RNN, 无 domain adaptation），应在讨论中显式建立联系。\"\n    action_items:\n      - round: 1\n        action: \"至少复现 DeepContext（BERT+RNN）在相同数据上的结果，或在讨论中显式将 vanilla variant 与 DeepContext 建立联系\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N4\"\n    summary: \"数据集规模过小（500 训练, 160 OOD 测试, 76 perturbation），所有核心 claims 的统计分辨率不足\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提 N4，R2 独立发现 N1（优先级最高）。n=80 DD 上每个 misclassification 改变 F1 约 1.25pp，区分 0.990 vs 0.997（差 0.7pp）统计上无意义。全部由 Qwen3-8B 合成生成，可能不反映真实攻击多样性。\"\n    action_items:\n      - round: 1\n        action: \"扩大数据集规模和来源多样性（多模型生成、人工红队数据），或显著降低 claim 强度并限定为 preliminary findings on synthetic data\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"有效 OOD 评估实质上是 single-dataset（FITD 无区分度，所有变体 F1≥0.990），cross-attack claim 仅由 DD 支撑\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 首提为 N3 critical，R1 原为 W6 warning 但在交叉回应中同意升级为 critical。FITD 在几乎所有变体和 prefix 上接近 perfect，消融分析实质上只在 DD 单数据集有效。cross-attack generalization 的 claim 外部效度严重不足。\"\n    action_items:\n      - round: 1\n        action: \"增加至少 2-3 个难度适中的 OOD attack types（如 ActorAttack, PAIR），使消融结论可在多数据集验证\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"Mean pooling=BiGRU 结论基于 single seed (42)，在 n=80 上 1.000 vs 0.997 统计上无意义\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W1, R2 W6。双方同意。如果 mean pooling 一致优于 BiGRU，BiGRU 作为 Stage-2 的架构选择缺乏 motivation。\"\n    action_items:\n      - round: 1\n        action: \"报告 mean pooling 的 3-seed 多变体结果，弱化因果性结论\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"策略标注质量验证不充分：Qwen3-8B 标注, κ=0.78, 人工验证仅 n=50（每类约 5-6 样本）\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W2, R2 在交叉回应中同意。κ=0.78 在 n=50 时 CI 很宽。three-layer attribution 中 correct labels 的优势依赖标注质量。\"\n    action_items:\n      - round: 1\n        action: \"增加人工验证至 200+（按类别分层抽样），报告每类 κ 或 confusion matrix\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"LLM-as-judge baseline 仅测 IID Crescendo，未测 OOD（FITD/DD）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W3, R2 AGREE with nuance（IID 已严重失败，OOD 预期更差，但完整性要求补充）。\"\n    action_items:\n      - round: 1\n        action: \"在 Appendix 补充 OOD 的 LLM-as-judge 结果\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"TF-IDF LR 强表现（DD-Full 0.944, perturbation 仅降 1.3pp）未被充分讨论，质疑 pragmatic features 的机制性解释\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W4, R2 W4，双方完全同意。TF-IDF robustness 远好于 vanilla/wiki-MLM，接近 MLM-only，暗示 domain exposure provides robustness 的 claim 部分被纯词汇模型实现。建议增加 probing/attention 分析验证是否学到语用特征。\"\n    action_items:\n      - round: 1\n        action: \"更诚实地讨论 TF-IDF 竞争力，增加特征分析实验（probing/attention 可视化），明确 DisPeD 在何种条件下具不可替代优势\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"可复现性不足：Stage-2 缺 lr/batch/optimizer，数据生成 prompt 未提供，标注 prompt 未提供，无代码/数据发布承诺\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W5, R2 在交叉回应中验证并同意所有缺失项。\"\n    action_items:\n      - round: 1\n        action: \"在 Appendix 补充完整超参数表、data generation prompt、annotation prompt，明确代码/数据发布计划\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1\"\n    summary: \"Abstract 过度堆砌数据（~10 个 F1 数字），读起来像压缩版 Results 而非独立叙事单元\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 W1, R1 在交叉回应中同意。建议保留 2-3 个关键数字。\"\n    action_items:\n      - round: 1\n        action: \"精简 Abstract 数字至 2-3 个关键值，聚焦问题→洞察→方法→结论的叙事弧\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2\"\n    summary: \"\\\"partially falsified our original hypothesis\\\" 叙事策略对审稿人接收判断有负面影响\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 W2, R1 AGREE with nuance（科学诚实值得肯定但修辞效果不佳）。分歧属修辞偏好，非实质性矛盾。建议正面框架叙事 + Discussion 中提及假设修正过程。\"\n    action_items:\n      - round: 1\n        action: \"将叙事重构为正面框架，在 Discussion 中保留假设修正的科学过程\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"Contributions 列表过于密集（两条各 60-80 词），难以快速提取核心 claim\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 W3, R1 同意。建议拆为 3-4 条简短 bullets。\"\n    action_items:\n      - round: 1\n        action: \"将 Contributions 拆分为 3-4 条，每条 30-40 词\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W5\"\n    summary: \"Strategy Trajectory Analysis (Figure 3) 使用 ground-truth labels 而非模型预测，展示数据集特性而非模型可解释性\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 W5, R1 在交叉回应中同意（此前遗漏）。如果 9-class 模型在 OOD 上策略预测准确率低，interpretability contribution 不成立。\"\n    action_items:\n      - round: 1\n        action: \"补充 OOD 策略预测准确率，用模型预测 labels 重做 trajectory analysis 与 ground-truth 对比\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W7\"\n    summary: \"Limitations 作为 paragraph 嵌入 Conclusion 而非独立 section，不符合 ACL/ARR 格式要求\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 W7, R1 在交叉回应中同意。ACL ARR 要求 Limitations 为独立 section。\"\n    action_items:\n      - round: 1\n        action: \"将 Limitations 拆分为独立 \\\\section{Limitations}，放在 Conclusion 之后 References 之前\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-REF1\"\n    summary: \"缺失引用：computational persuasion detection（SemEval propaganda tasks）、adversarial NLP robustness（TextFooler/BERT-Attack）、probing classifiers（Hewitt & Manning 2019）\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 在交叉回应中对三个方向均 AGREE，对引用数量 REBUT（关注覆盖方向而非数量）。\"\n    action_items:\n      - round: 1\n        action: \"补充 SemEval propaganda detection、TextFooler/BERT-Attack、probing classifier 相关引用\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-18T08:52:12.461096+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/review_issues.yaml\", \"bytes\": 9705}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-18T08:54:32.570304+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject",
  "report": "# 圆桌审稿报告 — Round 1\n\n**论文**: What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May cycle)\n**截止日期**: 2026-05-25\n**审稿组**: Reviewer 1（方法严谨性 + 实验有效性）、Reviewer 2（新颖性 + 完整性 + 写作质量）\n**收敛状态**: Round 1 完成，关键问题已达成共识，无需 Round 2\n\n---\n\n## Summary\n\n论文提出 DisPeD，一个两阶段多轮 jailbreak 检测框架，通过 7 个 Stage-1 encoder 变体系统分解跨攻击泛化的机制。核心发现：continued pretraining（MLM）是桥接 OOD gap 的主要机制（vanilla 0.28 → MLM 0.91±0.12），classification supervision 提供额外稳定性（9-class 0.997±0.005）。论文据此将多轮 jailbreak 检测重新定位为 domain adaptation 问题。\n\n---\n\n## Strengths\n\n**S1** [共识] 研究问题有价值且定义清晰。\"What representation properties enable cross-attack generalization?\" 是多轮 jailbreak defense 领域的 under-explored question，从 representation learning 角度系统分析而非追求 SOTA 数字。\n\n**S2** [共识] 7 变体消融设计是论文最大亮点。每个变体精准隔离一个因素（domain exposure, classification supervision, label quality, label granularity, domain specificity），Table 1 展示了清晰的实验逻辑。这种 controlled decomposition 的方法论本身对社区有参考价值。\n\n**S3** [共识] 诚实的科学态度。论文坦承 MLM 无标签即可桥接大部分 OOD gap，坦承 TF-IDF 达 0.944，坦承单 seed 变体的局限性。\n\n**S4** [共识] 与 domain-adaptive pretraining 文献的良好连接。核心发现与 Gururangan et al. (2020) 一致，将 jailbreak detection 重新定位为 domain adaptation 问题有理论深度。\n\n**S5** [共识] AI 写作痕迹控制良好。全文无 em-dash 滥用，无 delve/leverage/utilize 等 AI 高频词（仅一处 \"additionally\"），叙事连贯。\n\n---\n\n## Weaknesses\n\n### Must-Fix（5 项，两位 Reviewer 均标记为 critical 且达成共识）\n\n**MF1** [R1-N1, R2-N4] **Evidence hierarchy 统计基础不一致：binary/scrambled 仅 seed 42**\n- 论文核心 evidence hierarchy 混合了 3-seed 和 single-seed 结果。binary 和 scrambled 的 F1=0.990 来自 seed 42 单点估计，无方差信息。\n- 论文从中推导因果性 claim：\"Label quality and granularity are non-factors for detection\"（Section 4.4）、\"classification objective functions as a regularizer\"（Section 4.4）。这些 claims 建立在两个 single-seed 数据点的巧合相等上。\n- topic 变体的高方差（0.54±0.21，seed 123 低于 vanilla）证明某些变体在不同 seeds 下可能极不稳定。如果 binary/scrambled 出现类似方差，evidence hierarchy 中间层将坍塌。\n- **修复要求**：所有 7 个变体必须报告相同的 3-seed（或更多）mean±std。\n\n**MF2** [R1-N2, R2 交叉同意] **Three-layer robustness attribution 在 n=76 上缺乏统计显著性**\n- Δ=2.6pp ≈ 2 个样本差异，Δ=5.3pp ≈ 4 个样本，Δ=9.2pp ≈ 7 个样本。无 McNemar's test、bootstrap CI 或 permutation test。\n- 论文自身承认 \"tier boundaries correspond to 1-3 misclassifications\"（Section 4.3），但未降级 claim 强度。Three-layer attribution 是 Introduction Contribution #2 的核心，占正文约 1/3 讨论。\n- **修复要求**：(1) 扩大 perturbation test set 至 n≥300，或 (2) 报告统计显著性检验，或 (3) 将 three-layer attribution 降级为 \"observed pattern\" 并大幅削减讨论篇幅。\n\n**MF3** [R1-N3, R2-N2] **缺少与已发表 multi-turn defense 系统的直接实验对比**\n- 论文在 Related Work 定位 DeepContext、BIID、G-Guard、SafeDream 为 direct competitors，声称它们 \"do not decompose what enables cross-attack generalization\"（Section 1）。但 Experiments 无任何头对头比较。\n- 实际 baselines 仅为 vanilla DeBERTa（论文自身 ablation）、TF-IDF LR、LLM-as-judge（仅测 IID）。\n- R2 补充：vanilla variant 本身可视为 DeepContext 的近似复现（pretrained encoder + RNN, 无 domain adaptation），应在讨论中显式建立联系。\n- **修复要求**：至少复现 DeepContext 在相同数据上的结果。\n\n**MF4** [R1-N4, R2-N1] **数据集规模过小，所有核心 claims 的统计分辨率不足**\n- 500 训练、160 OOD 测试、76 perturbation，全部由 Qwen3-8B 合成生成。\n- n=80 DD 上每个 misclassification 改变 F1 约 1.25pp。区分 0.990 和 0.997（差 0.7pp）在统计上无意义。\n- jailbreak-MLM vs wiki-MLM 在 full length 仅差 1pp（0.914 vs 0.904），但论文基于此讨论 domain specificity。\n- 论文的 \"reframe multi-turn jailbreak detection as primarily a domain adaptation problem\" claim 的证据强度与 claim 广度严重不匹配。\n- **修复要求**：扩大数据集规模和来源多样性，或显著降低 claim 强度并限定为 preliminary findings on synthetic data。\n\n**MF5** [R2-N3, R1-W6→交叉升级为 critical] **有效 OOD 评估实质上是 single-dataset**\n- FITD 在几乎所有变体和 prefix 长度上 F1≥0.990（含 vanilla），对方法无区分度。\n- 7 变体消融分析实质上只在 DD 一个 OOD attack type 上有效。DD 可能有特殊属性（emotion-based manipulation 风格），使当前发现不具普遍性。\n- \"cross-attack generalization\" 的 claim 仅由单一 OOD attack type 支撑，外部效度严重不足。\n- **修复要求**：增加至少 2-3 个难度适中的 OOD attack types（ActorAttack, PAIR 等）。\n\n### Should-Fix（12 项）\n\n**SF1** [R1-W1, R2-W6] Mean pooling = BiGRU 结论基于 single seed (42)，在 n=80 上 1.000 vs 0.997 统计上无意义。\"detection relies on per-turn representations rather than their sequential order\" 的强因果 claim 缺乏充分支撑。如果 mean pooling 一致优于 BiGRU，Stage-2 BiGRU 的架构选择缺乏 motivation。需报告 3-seed 多变体结果。\n\n**SF2** [R1-W2] 策略标注质量验证不充分。Qwen3-8B 标注，κ=0.78，人工验证仅 n=50（每类约 5-6 样本）。three-layer attribution 中 \"correct labels\" 的优势直接依赖标注质量。建议增加人工验证至 200+，报告每类 κ 或 confusion matrix。\n\n**SF3** [R1-W3] LLM-as-judge baseline 仅测 IID，未测 OOD。论文核心贡献是 OOD generalization，虽然 IID 已严重失败（GPT-5.5 F1=0.191-0.449），但 OOD 结果应报告以加强 \"content-level reasoning is insufficient\" 的 claim。\n\n**SF4** [R1-W4, R2-W4] TF-IDF LR 强表现未被充分讨论。DD-Full 0.944，perturbation 仅降 1.3pp。TF-IDF robustness 远好于 vanilla/wiki-MLM（~12pp），接近 MLM-only（2.6pp）。这质疑了 \"domain-adaptive pretraining captures pragmatic features\" 的机制性解释——也许模型只在捕捉词汇统计差异。建议增加 probing/attention 分析验证。\n\n**SF5** [R1-W5] 可复现性不足。Stage-2 缺 learning rate/batch size/optimizer/warmup；数据生成 pipeline 和策略标注 prompt 未提供；无代码/数据发布承诺。建议在 Appendix 补充完整超参数表和 prompt。\n\n**SF6** [R2-W1] Abstract 过度堆砌数据（约 180 词含 ~10 个 F1 数字），读起来像压缩版 Results。建议保留 2-3 个关键数字（vanilla 0.28, MLM ≥0.97, 9-class 0.997），聚焦叙事弧。\n\n**SF7** [R2-W2, R1 AGREE with nuance] \"partially falsified our original hypothesis\" 叙事策略对审稿人接收判断有负面影响。R1 认为科学诚实值得肯定但修辞效果不佳。建议正面框架叙事 + Discussion 中保留假设修正过程。\n\n**SF8** [R2-W3] Contributions 列表过于密集（两条各 60-80 词）。第二条试图在单 bullet 中描述 three-layer attribution 的完整结构。建议拆为 3-4 条简短 bullets，每条 30-40 词。\n\n**SF9** [R2-W5] Strategy Trajectory Analysis (Figure 3) 使用 ground-truth labels（Qwen3-8B 标注）而非模型预测。如果 9-class 模型在 OOD 上策略预测准确率低，\"interpretability through strategy trajectories\" 这一 contribution 不成立。必须补充 OOD 策略预测准确率。\n\n**SF10** [R2-W7] Limitations 作为 `\\paragraph{Limitations and future work.}` 嵌入 Conclusion，不符合 ACL/ARR 独立 `\\section{Limitations}` 的格式要求。需拆分为独立 section。\n\n**SF11** [R2-REF1, R1 交叉同意] 缺失关键引用方向：(1) computational persuasion detection 实证工作（SemEval propaganda detection tasks），(2) adversarial NLP robustness 基础文献（TextFooler, BERT-Attack），(3) probing classifiers（Hewitt & Manning 2019, Belinkov & Glass 2019）。覆盖方向的缺失比引用总量更重要。\n\n**SF12** [R1 小问题, R2 小问题] 图表问题：Fig 1 Stage 1/Stage 2 标题重叠、\"Frozen [CLS]\" 位置拥挤；Fig 3 轴标签字体偏小（已使用 `figure*` 但仍需增大字体）。部分引用 year 不一致（chao2023pair 2023 vs 正式发表 2025）。缩写 \"pp\" 未定义。缺少各变体计算成本信息。仅用 user turns 的假设需更多讨论。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识 [AGREE]：\n1. binary/scrambled 必须补充 multi-seed 结果（MF1）\n2. three-layer attribution 缺乏统计显著性检验（MF2）\n3. 必须增加 multi-turn defense baseline 对比（MF3）\n4. 数据集规模不足以支撑核心 claims（MF4）\n5. FITD 无区分度导致 OOD 评估实质上是 single-dataset（MF5）\n6. TF-IDF 的强表现质疑 pragmatic features 的机制性解释（SF4）\n7. Strategy trajectory analysis 应使用模型预测而非 ground-truth（SF9）\n8. Limitations 格式需修改为独立 section（SF10）\n9. 三个方向的引用覆盖缺失（SF11）\n\n---\n\n## Reviewer Divergence\n\n仅一处修辞偏好分歧，非实质性矛盾：\n- **\"partially falsified\" 叙事**：R1 认为科学诚实值得肯定（列为优势），R2 认为对审稿人接收判断有负面影响（列为 should-fix）。R1 在交叉回应中 AGREE with nuance：可正面框架叙事同时在 Discussion 中保留假设修正过程。\n\n---\n\n## Questions\n\n1. binary/scrambled 仅报告 seed 42 的原因是什么？是计算资源限制还是其他原因？\n2. 9-class 模型在 OOD (DD/FITD) 数据上的策略预测准确率是多少？\n3. 论文声称 \"pragmatic features (hedging, escalation markers, topic-shifting patterns)\" 是 DAPT 捕获的特征，有什么直接证据（如 probing 实验、attention 分析）？\n4. 为什么不 end-to-end fine-tune Stage 1 + Stage 2？冻结 Stage 1 的设计选择基于什么实验或理论依据？\n5. assistant responses 是否可能包含有用的检测信号（如 refusal patterns, compliance indicators）？仅用 user turns 的决策是否经过实验验证？\n6. 如果 mean pooling 一致优于 BiGRU，Stage-2 的 BiGRU 设计 motivation 是什么？\n\n---\n\n## Missing References\n\n1. **Computational persuasion detection**：SemEval propaganda detection shared tasks (Da San Martino et al., 2019; Dimitrov et al., 2021)\n2. **Adversarial NLP robustness**：TextFooler (Jin et al., 2020), BERT-Attack (Li et al., 2020)\n3. **Probing classifiers**：Hewitt & Manning 2019, Belinkov & Glass 2019\n4. 部分引用条目 year 不一致需核实（chao2023pair, austin1962speechacts, han2024wildguard）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置，跳过。\n\n---\n\n## Overall Assessment\n\n**评分: Weak Reject (2/5)**\n**置信度: 4/5**\n\n论文提出了一个有价值的研究问题（什么使跨攻击泛化成为可能），7 变体消融的实验设计思路优秀，核心发现（domain adaptation 是主要机制）有理论意义。但当前版本存在 5 项 critical 问题的联合效应严重：\n\n1. **统计可信度不足**：binary/scrambled 单 seed、n=76 三层归因无显著性检验、n=80 上精细排序无统计意义\n2. **评估范围不足**：有效 OOD 仅 DD 单数据集，缺少与 SOTA multi-turn defense 的直接对比\n3. **Claim 强度与证据不匹配**：\"reframe multi-turn jailbreak detection as primarily a domain adaptation problem\" 基于 500 条合成对话和单一 OOD attack type\n\nR1 评分 2/5（Resubmit），R2 评分 2.5/5（Borderline Findings）。综合判断：weak reject。如果 (1) 所有变体补充 multi-seed 结果，(2) 增加 2-3 个 OOD attack types，(3) 至少复现 DeepContext 作为 baseline，(4) 补充统计显著性检验或降级 three-layer attribution claims，论文有望在下一个 ARR cycle 达到 accept 水平。当前版本更适合 Findings track（如果降低 claim 强度并补充关键实验）。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 约 180 词，在范围内，但数字过密（~10 个 F1 值 + 2 个 std）。建议保留 3 个关键数字，其余移入正文。\n- \"pp\" 缩写未定义。\n\n### Introduction\n- \"partially falsified our original hypothesis\" 叙事有科学价值但对接收不利，建议正面重构。\n- Contributions 列表过于密集，建议拆为 3-4 条。\n- Evidence hierarchy 在 Introduction 中完整呈现（含 6 个 F1 值），信息过载。\n\n### Related Work\n- 结构清晰，5 个 paragraph 覆盖 attacks/defenses/production systems/discourse/DAPT。\n- \"none systematically analyze why\" 的 gap 声明过强，建议温和化为 \"provide limited insight into which representation properties drive cross-attack generalization\"。\n- 缺失 3 个引用方向（propaganda detection, adversarial robustness, probing classifiers）。\n\n### Method\n- 7 变体设计逻辑清晰，Table 1 是论文最佳表格。\n- 策略标注质量验证不足（κ=0.78, n=50）。\n- 仅用 user turns 的假设合理但需更多讨论。\n\n### Experiments\n- 核心问题：数据规模、seed 不一致、单 OOD 数据集、缺 baseline 对比。\n- Three-layer robustness attribution 的 claim 强度需大幅降级。\n- Figure 3 使用 ground-truth labels 而非模型预测，不支撑 interpretability claim。\n- Mean pooling 实验仅单 seed，与 BiGRU 架构选择矛盾。\n\n### Conclusion\n- Limitations 需拆为独立 section（ACL/ARR 格式要求）。\n- 论文诚实承认多项局限但未在主体 claims 中做对应降级。\n\n### Figures\n- Fig 1: Stage 1/Stage 2 标题重叠，\"Frozen [CLS]\" 拥挤，需调整 layout。\n- Fig 2: 清晰展示 prefix-length trajectory，是有效的可视化。\n- Fig 3: 轴标签字体偏小，strategy 名称难辨认。应使用 ground-truth + 模型预测的对比版本。\n\n### References\n- 31 条（bib 头注释 31，实际可能略多），覆盖基本到位但 3 个方向缺失。\n- 部分 year 不一致需核实。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject",
    "report": "# 圆桌审稿报告 — Round 1\n\n**论文**: What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May cycle)\n**截止日期**: 2026-05-25\n**审稿组**: Reviewer 1（方法严谨性 + 实验有效性）、Reviewer 2（新颖性 + 完整性 + 写作质量）\n**收敛状态**: Round 1 完成，关键问题已达成共识，无需 Round 2\n\n---\n\n## Summary\n\n论文提出 DisPeD，一个两阶段多轮 jailbreak 检测框架，通过 7 个 Stage-1 encoder 变体系统分解跨攻击泛化的机制。核心发现：continued pretraining（MLM）是桥接 OOD gap 的主要机制（vanilla 0.28 → MLM 0.91±0.12），classification supervision 提供额外稳定性（9-class 0.997±0.005）。论文据此将多轮 jailbreak 检测重新定位为 domain adaptation 问题。\n\n---\n\n## Strengths\n\n**S1** [共识] 研究问题有价值且定义清晰。\"What representation properties enable cross-attack generalization?\" 是多轮 jailbreak defense 领域的 under-explored question，从 representation learning 角度系统分析而非追求 SOTA 数字。\n\n**S2** [共识] 7 变体消融设计是论文最大亮点。每个变体精准隔离一个因素（domain exposure, classification supervision, label quality, label granularity, domain specificity），Table 1 展示了清晰的实验逻辑。这种 controlled decomposition 的方法论本身对社区有参考价值。\n\n**S3** [共识] 诚实的科学态度。论文坦承 MLM 无标签即可桥接大部分 OOD gap，坦承 TF-IDF 达 0.944，坦承单 seed 变体的局限性。\n\n**S4** [共识] 与 domain-adaptive pretraining 文献的良好连接。核心发现与 Gururangan et al. (2020) 一致，将 jailbreak detection 重新定位为 domain adaptation 问题有理论深度。\n\n**S5** [共识] AI 写作痕迹控制良好。全文无 em-dash 滥用，无 delve/leverage/utilize 等 AI 高频词（仅一处 \"additionally\"），叙事连贯。\n\n---\n\n## Weaknesses\n\n### Must-Fix（5 项，两位 Reviewer 均标记为 critical 且达成共识）\n\n**MF1** [R1-N1, R2-N4] **Evidence hierarchy 统计基础不一致：binary/scrambled 仅 seed 42**\n- 论文核心 evidence hierarchy 混合了 3-seed 和 single-seed 结果。binary 和 scrambled 的 F1=0.990 来自 seed 42 单点估计，无方差信息。\n- 论文从中推导因果性 claim：\"Label quality and granularity are non-factors for detection\"（Section 4.4）、\"classification objective functions as a regularizer\"（Section 4.4）。这些 claims 建立在两个 single-seed 数据点的巧合相等上。\n- topic 变体的高方差（0.54±0.21，seed 123 低于 vanilla）证明某些变体在不同 seeds 下可能极不稳定。如果 binary/scrambled 出现类似方差，evidence hierarchy 中间层将坍塌。\n- **修复要求**：所有 7 个变体必须报告相同的 3-seed（或更多）mean±std。\n\n**MF2** [R1-N2, R2 交叉同意] **Three-layer robustness attribution 在 n=76 上缺乏统计显著性**\n- Δ=2.6pp ≈ 2 个样本差异，Δ=5.3pp ≈ 4 个样本，Δ=9.2pp ≈ 7 个样本。无 McNemar's test、bootstrap CI 或 permutation test。\n- 论文自身承认 \"tier boundaries correspond to 1-3 misclassifications\"（Section 4.3），但未降级 claim 强度。Three-layer attribution 是 Introduction Contribution #2 的核心，占正文约 1/3 讨论。\n- **修复要求**：(1) 扩大 perturbation test set 至 n≥300，或 (2) 报告统计显著性检验，或 (3) 将 three-layer attribution 降级为 \"observed pattern\" 并大幅削减讨论篇幅。\n\n**MF3** [R1-N3, R2-N2] **缺少与已发表 multi-turn defense 系统的直接实验对比**\n- 论文在 Related Work 定位 DeepContext、BIID、G-Guard、SafeDream 为 direct competitors，声称它们 \"do not decompose what enables cross-attack generalization\"（Section 1）。但 Experiments 无任何头对头比较。\n- 实际 baselines 仅为 vanilla DeBERTa（论文自身 ablation）、TF-IDF LR、LLM-as-judge（仅测 IID）。\n- R2 补充：vanilla variant 本身可视为 DeepContext 的近似复现（pretrained encoder + RNN, 无 domain adaptation），应在讨论中显式建立联系。\n- **修复要求**：至少复现 DeepContext 在相同数据上的结果。\n\n**MF4** [R1-N4, R2-N1] **数据集规模过小，所有核心 claims 的统计分辨率不足**\n- 500 训练、160 OOD 测试、76 perturbation，全部由 Qwen3-8B 合成生成。\n- n=80 DD 上每个 misclassification 改变 F1 约 1.25pp。区分 0.990 和 0.997（差 0.7pp）在统计上无意义。\n- jailbreak-MLM vs wiki-MLM 在 full length 仅差 1pp（0.914 vs 0.904），但论文基于此讨论 domain specificity。\n- 论文的 \"reframe multi-turn jailbreak detection as primarily a domain adaptation problem\" claim 的证据强度与 claim 广度严重不匹配。\n- **修复要求**：扩大数据集规模和来源多样性，或显著降低 claim 强度并限定为 preliminary findings on synthetic data。\n\n**MF5** [R2-N3, R1-W6→交叉升级为 critical] **有效 OOD 评估实质上是 single-dataset**\n- FITD 在几乎所有变体和 prefix 长度上 F1≥0.990（含 vanilla），对方法无区分度。\n- 7 变体消融分析实质上只在 DD 一个 OOD attack type 上有效。DD 可能有特殊属性（emotion-based manipulation 风格），使当前发现不具普遍性。\n- \"cross-attack generalization\" 的 claim 仅由单一 OOD attack type 支撑，外部效度严重不足。\n- **修复要求**：增加至少 2-3 个难度适中的 OOD attack types（ActorAttack, PAIR 等）。\n\n### Should-Fix（12 项）\n\n**SF1** [R1-W1, R2-W6] Mean pooling = BiGRU 结论基于 single seed (42)，在 n=80 上 1.000 vs 0.997 统计上无意义。\"detection relies on per-turn representations rather than their sequential order\" 的强因果 claim 缺乏充分支撑。如果 mean pooling 一致优于 BiGRU，Stage-2 BiGRU 的架构选择缺乏 motivation。需报告 3-seed 多变体结果。\n\n**SF2** [R1-W2] 策略标注质量验证不充分。Qwen3-8B 标注，κ=0.78，人工验证仅 n=50（每类约 5-6 样本）。three-layer attribution 中 \"correct labels\" 的优势直接依赖标注质量。建议增加人工验证至 200+，报告每类 κ 或 confusion matrix。\n\n**SF3** [R1-W3] LLM-as-judge baseline 仅测 IID，未测 OOD。论文核心贡献是 OOD generalization，虽然 IID 已严重失败（GPT-5.5 F1=0.191-0.449），但 OOD 结果应报告以加强 \"content-level reasoning is insufficient\" 的 claim。\n\n**SF4** [R1-W4, R2-W4] TF-IDF LR 强表现未被充分讨论。DD-Full 0.944，perturbation 仅降 1.3pp。TF-IDF robustness 远好于 vanilla/wiki-MLM（~12pp），接近 MLM-only（2.6pp）。这质疑了 \"domain-adaptive pretraining captures pragmatic features\" 的机制性解释——也许模型只在捕捉词汇统计差异。建议增加 probing/attention 分析验证。\n\n**SF5** [R1-W5] 可复现性不足。Stage-2 缺 learning rate/batch size/optimizer/warmup；数据生成 pipeline 和策略标注 prompt 未提供；无代码/数据发布承诺。建议在 Appendix 补充完整超参数表和 prompt。\n\n**SF6** [R2-W1] Abstract 过度堆砌数据（约 180 词含 ~10 个 F1 数字），读起来像压缩版 Results。建议保留 2-3 个关键数字（vanilla 0.28, MLM ≥0.97, 9-class 0.997），聚焦叙事弧。\n\n**SF7** [R2-W2, R1 AGREE with nuance] \"partially falsified our original hypothesis\" 叙事策略对审稿人接收判断有负面影响。R1 认为科学诚实值得肯定但修辞效果不佳。建议正面框架叙事 + Discussion 中保留假设修正过程。\n\n**SF8** [R2-W3] Contributions 列表过于密集（两条各 60-80 词）。第二条试图在单 bullet 中描述 three-layer attribution 的完整结构。建议拆为 3-4 条简短 bullets，每条 30-40 词。\n\n**SF9** [R2-W5] Strategy Trajectory Analysis (Figure 3) 使用 ground-truth labels（Qwen3-8B 标注）而非模型预测。如果 9-class 模型在 OOD 上策略预测准确率低，\"interpretability through strategy trajectories\" 这一 contribution 不成立。必须补充 OOD 策略预测准确率。\n\n**SF10** [R2-W7] Limitations 作为 `\\paragraph{Limitations and future work.}` 嵌入 Conclusion，不符合 ACL/ARR 独立 `\\section{Limitations}` 的格式要求。需拆分为独立 section。\n\n**SF11** [R2-REF1, R1 交叉同意] 缺失关键引用方向：(1) computational persuasion detection 实证工作（SemEval propaganda detection tasks），(2) adversarial NLP robustness 基础文献（TextFooler, BERT-Attack），(3) probing classifiers（Hewitt & Manning 2019, Belinkov & Glass 2019）。覆盖方向的缺失比引用总量更重要。\n\n**SF12** [R1 小问题, R2 小问题] 图表问题：Fig 1 Stage 1/Stage 2 标题重叠、\"Frozen [CLS]\" 位置拥挤；Fig 3 轴标签字体偏小（已使用 `figure*` 但仍需增大字体）。部分引用 year 不一致（chao2023pair 2023 vs 正式发表 2025）。缩写 \"pp\" 未定义。缺少各变体计算成本信息。仅用 user turns 的假设需更多讨论。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识 [AGREE]：\n1. binary/scrambled 必须补充 multi-seed 结果（MF1）\n2. three-layer attribution 缺乏统计显著性检验（MF2）\n3. 必须增加 multi-turn defense baseline 对比（MF3）\n4. 数据集规模不足以支撑核心 claims（MF4）\n5. FITD 无区分度导致 OOD 评估实质上是 single-dataset（MF5）\n6. TF-IDF 的强表现质疑 pragmatic features 的机制性解释（SF4）\n7. Strategy trajectory analysis 应使用模型预测而非 ground-truth（SF9）\n8. Limitations 格式需修改为独立 section（SF10）\n9. 三个方向的引用覆盖缺失（SF11）\n\n---\n\n## Reviewer Divergence\n\n仅一处修辞偏好分歧，非实质性矛盾：\n- **\"partially falsified\" 叙事**：R1 认为科学诚实值得肯定（列为优势），R2 认为对审稿人接收判断有负面影响（列为 should-fix）。R1 在交叉回应中 AGREE with nuance：可正面框架叙事同时在 Discussion 中保留假设修正过程。\n\n---\n\n## Questions\n\n1. binary/scrambled 仅报告 seed 42 的原因是什么？是计算资源限制还是其他原因？\n2. 9-class 模型在 OOD (DD/FITD) 数据上的策略预测准确率是多少？\n3. 论文声称 \"pragmatic features (hedging, escalation markers, topic-shifting patterns)\" 是 DAPT 捕获的特征，有什么直接证据（如 probing 实验、attention 分析）？\n4. 为什么不 end-to-end fine-tune Stage 1 + Stage 2？冻结 Stage 1 的设计选择基于什么实验或理论依据？\n5. assistant responses 是否可能包含有用的检测信号（如 refusal patterns, compliance indicators）？仅用 user turns 的决策是否经过实验验证？\n6. 如果 mean pooling 一致优于 BiGRU，Stage-2 的 BiGRU 设计 motivation 是什么？\n\n---\n\n## Missing References\n\n1. **Computational persuasion detection**：SemEval propaganda detection shared tasks (Da San Martino et al., 2019; Dimitrov et al., 2021)\n2. **Adversarial NLP robustness**：TextFooler (Jin et al., 2020), BERT-Attack (Li et al., 2020)\n3. **Probing classifiers**：Hewitt & Manning 2019, Belinkov & Glass 2019\n4. 部分引用条目 year 不一致需核实（chao2023pair, austin1962speechacts, han2024wildguard）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置，跳过。\n\n---\n\n## Overall Assessment\n\n**评分: Weak Reject (2/5)**\n**置信度: 4/5**\n\n论文提出了一个有价值的研究问题（什么使跨攻击泛化成为可能），7 变体消融的实验设计思路优秀，核心发现（domain adaptation 是主要机制）有理论意义。但当前版本存在 5 项 critical 问题的联合效应严重：\n\n1. **统计可信度不足**：binary/scrambled 单 seed、n=76 三层归因无显著性检验、n=80 上精细排序无统计意义\n2. **评估范围不足**：有效 OOD 仅 DD 单数据集，缺少与 SOTA multi-turn defense 的直接对比\n3. **Claim 强度与证据不匹配**：\"reframe multi-turn jailbreak detection as primarily a domain adaptation problem\" 基于 500 条合成对话和单一 OOD attack type\n\nR1 评分 2/5（Resubmit），R2 评分 2.5/5（Borderline Findings）。综合判断：weak reject。如果 (1) 所有变体补充 multi-seed 结果，(2) 增加 2-3 个 OOD attack types，(3) 至少复现 DeepContext 作为 baseline，(4) 补充统计显著性检验或降级 three-layer attribution claims，论文有望在下一个 ARR cycle 达到 accept 水平。当前版本更适合 Findings track（如果降低 claim 强度并补充关键实验）。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 约 180 词，在范围内，但数字过密（~10 个 F1 值 + 2 个 std）。建议保留 3 个关键数字，其余移入正文。\n- \"pp\" 缩写未定义。\n\n### Introduction\n- \"partially falsified our original hypothesis\" 叙事有科学价值但对接收不利，建议正面重构。\n- Contributions 列表过于密集，建议拆为 3-4 条。\n- Evidence hierarchy 在 Introduction 中完整呈现（含 6 个 F1 值），信息过载。\n\n### Related Work\n- 结构清晰，5 个 paragraph 覆盖 attacks/defenses/production systems/discourse/DAPT。\n- \"none systematically analyze why\" 的 gap 声明过强，建议温和化为 \"provide limited insight into which representation properties drive cross-attack generalization\"。\n- 缺失 3 个引用方向（propaganda detection, adversarial robustness, probing classifiers）。\n\n### Method\n- 7 变体设计逻辑清晰，Table 1 是论文最佳表格。\n- 策略标注质量验证不足（κ=0.78, n=50）。\n- 仅用 user turns 的假设合理但需更多讨论。\n\n### Experiments\n- 核心问题：数据规模、seed 不一致、单 OOD 数据集、缺 baseline 对比。\n- Three-layer robustness attribution 的 claim 强度需大幅降级。\n- Figure 3 使用 ground-truth labels 而非模型预测，不支撑 interpretability claim。\n- Mean pooling 实验仅单 seed，与 BiGRU 架构选择矛盾。\n\n### Conclusion\n- Limitations 需拆为独立 section（ACL/ARR 格式要求）。\n- 论文诚实承认多项局限但未在主体 claims 中做对应降级。\n\n### Figures\n- Fig 1: Stage 1/Stage 2 标题重叠，\"Frozen [CLS]\" 拥挤，需调整 layout。\n- Fig 2: 清晰展示 prefix-length trajectory，是有效的可视化。\n- Fig 3: 轴标签字体偏小，strategy 名称难辨认。应使用 ground-truth + 模型预测的对比版本。\n\n### References\n- 31 条（bib 头注释 31，实际可能略多），覆盖基本到位但 3 个方向缺失。\n- 部分 year 不一致需核实。"
  }
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-18T08:54:37.745344+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a90fe0dde422576f214f12233cfe27a3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 5175
}
```

</details>

---


### Assistant

_source line 92 · 2026-05-18T08:54:47.480477+00:00_

圆桌审稿 Round 1 完成。

**最终结果：Weak Reject (2/5)**

两位 Reviewer 在 5 项 critical 问题上达成完全共识：
1. binary/scrambled 单 seed 破坏 evidence hierarchy 可比性
2. Three-layer robustness attribution 在 n=76 上无统计显著性
3. 缺少与 SOTA multi-turn defense 的直接实验对比
4. 数据集规模过小（500 训练 + 160 OOD）
5. 有效 OOD 评估实质上仅 DD 单数据集

核心判断：研究问题有价值、消融设计优秀，但 claim 强度与证据规模严重不匹配。修复路径明确——补全 multi-seed、扩大 OOD 范围、增加 baseline 对比——下一个 ARR cycle 有望改善。

审稿报告已投递 Research Director，Issue Tracker（17 条）已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 9

## Round 9

2 recorded events


### User

_source line 93 · 2026-05-18T08:54:50.304831+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Director。

主要结论：与 Reviewer 1 高度一致，四个 Must-Fix 全部 [AGREE]，六个 Should-Fix 中五个完全 [AGREE]、一个 [AGREE with nuance]（W3 关于 LLM-as-judge 仅测 IID）。主要分歧在于 FITD 问题的严重性（我认为应升级为 critical）和 overall 评分（我 2.5 vs R1 的 2）。我的审查在写作质量方面有 R1 未覆盖的补充意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 94 · 2026-05-18T08:55:02.193013+00:00_

审稿报告已投递完成。

**审稿圆桌会议总结：**

- **评分：Weak Reject (2/5)**，置信度 4/5
- **收敛状态**：Round 1 完成，两位 Reviewer 在所有 critical 问题上达成共识，无需 Round 2
- **5 项 Must-Fix**：seed 报告不一致、three-layer attribution 无统计显著性、缺 SOTA baseline 对比、数据规模过小、OOD 评估实质 single-dataset
- **12 项 Should-Fix**：涵盖标注质量、TF-IDF 讨论不充分、strategy analysis 用 ground-truth 而非模型预测、Limitations 格式、缺失引用方向等
- **Issue Tracker**：已同步 17 条 issue 至 `review_issues.yaml`
- **报告已投递**至 Research Director

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 10

## Round 10

60 recorded events


### User

_source line 95 · 2026-05-18T15:49:34.137201+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: persuasion_turn_jailbreak_detect
- 论文路径: projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: LLM Security / Discourse and Pragmatics
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-18T15:49:40.011706+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-18T15:49:40.163004+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-18T15:49:43.375431+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
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

_source line 99 · 2026-05-18T15:49:43.476250+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-18T15:49:46.488501+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-18T15:49:47.793973+00:00_

{"result":"# 项目 persuasion_turn_jailbreak_detect 概况\n\n## 实验状态 (56 个)\n\n- **plan_016_sentiment_control**: PREPARING (failed) — \n- **plan_012_gpt55_judge**: DONE (success) — \n- **plan_015_dd_eval**: DONE (success) — \n- **plan_006_cross_attack_clean**: DONE (success) — \n- **plan_004_perturbation_eval**: DONE (success) — \n- **plan_013_none_collapse**: DONE (success) — \n- **plan_012_llm_judge_qwen**: DONE (success) — \n- **plan_002_clean_training**: DONE (negative) — \n- **plan_003_scrambled_ablation**: DONE (negative) — \n- **cross_attack_baseline**: DONE (negative) — \n- **plan_008_strategy_transition**: DONE (success) — \n- **plan_007_tfidf_fitd_dd**: DONE (success) — \n- **plan_005_multi_attack_gen**: DONE (success) — \n- **phase_b_full**: DONE (success) — \n- **pilot_phase_b**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp3_probing: 9-class persuasion fine-tuned DeBERTa encodes richer discourse structure (turn position, escalation level, persuasion presence) than vanilla/MLM variants, as measured by linear probing accuracy and CKA divergence（准备中）\n- exp1_roberta_vanilla: Off-the-shelf RoBERTa-base without any fine-tuning will show poor DD OOD performance, matching DeBERTa vanilla baseline pattern and confirming encoder-agnostic findings（准备中）\n- exp1_roberta_mlm: RoBERTa-base with MLM-only continued pretraining will show intermediate DD OOD performance between vanilla and 9-class, matching DeBERTa's evidence hierarchy pattern（准备中）\n- exp1_roberta_9class: RoBERTa-base with 9-class persuasion multi-task fine-tuning will reproduce the DeBERTa evidence hierarchy (9-class >> vanilla), proving findings are encoder-agnostic（准备中）\n- plan_003_scrambled_retrain（准备中）\n- plan_018_eval_seed456（准备中）\n- plan_018_eval_seed123（准备中）\n- plan_018_wiki_mlm_seed456（准备中）\n- plan_018_wiki_mlm_seed123（准备中）\n- plan_017_eval_seed456（准备中）\n- …另有 10 项\n\n## 近期结论\n- **exp6_actorattack_perturbation** (negative): 
…[truncated 924 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1305
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-18T15:49:47.844732+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-18T15:49:47.845173+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-18T15:49:54.672381+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-18T15:49:54.873637+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\graphicspath{{../../}}
12	\usepackage{amsmath}
13	\usepackage{booktabs}
14	\usepackage{enumitem}
15	\usepackage{amssymb}
16	\usepackage{multirow}
17	
18	\title{What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	
27	\input{introduction}
28	
29	\input{related_work}
30	
31	\input{method}
32	
33	\input{experiments}
34	
35	\input{conclusion}
36	
37	\bibliography{references}
38	
39	\input{appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-18T15:49:54.873983+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
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

_source line 107 · 2026-05-18T15:49:54.874139+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-18T15:49:55.627255+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "literature_map.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect",
    "file": "literature_map.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-18T15:49:55.678389+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/literature_map.yaml\", \"content\": \"# Literature Map — persuasion_turn_jailbreak_detect\\n# Generated: 2026-05-17 by Paper Agent\\n# Target: EMNLP 2026 Main (ARR May cycle)\\n# Total entries: 39 (across 8 categories + technical foundation)\\n# All entries WebSearch-verified\\n\\nmetadata:\\n  project: persuasion_turn_jailbreak_detect\\n  target_venue: EMNLP 2026\\n  last_updated: \\\"2026-05-17\\\"\\n  total_papers: 39\\n  categories:\\n    - production_safety_systems\\n    - multi_turn_defenses\\n    - discourse_analysis\\n    - computational_persuasion\\n    - jailbreak_attacks_taxonomies\\n    - red_teaming\\n    - annotation_artifacts\\n    - adaptive_attacks\\n    - technical_foundation\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Production Multi-Turn Safety Systems (5 papers)\\n  # ============================================================\\n\\n  - bibtex_key: inan2023llamaguard\\n    title: \\\"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\\\"\\n    authors: \\\"Inan et al.\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2023\\n    arxiv: \\\"2312.06674\\\"\\n    category: production_safety_systems\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Foundational production safety classifier. Per-turn input/output guard\\n      that lacks multi-turn context modeling. DisPeD addresses this gap by\\n      modeling conversation-level persuasion trajectories.\\n\\n  - bibtex_key: metallamaguard3_2024\\n    title: \\\"Llama Guard 3\\\"\\n    authors: \\\"Meta AI\\\"\\n    venue: \\\"Meta AI (released with Llama 3.1)\\\"\\n    year: 2024\\n    category: production_safety_systems\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Latest iteration of Llama Guard with multili
…[truncated 11344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-18T15:50:01.682876+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 111 · 2026-05-18T15:50:02.637112+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 112 · 2026-05-18T15:50:03.039056+00:00_

1	% abstract.tex — cross-encoder revision
2	\begin{abstract}
3	Multi-turn jailbreak attacks distribute adversarial intent across seemingly benign conversational turns, evading per-turn safety filters.
4	We present preliminary findings from a systematic ablation on two encoder architectures that decomposes what enables cross-attack generalization in multi-turn jailbreak detection.
5	On DeBERTa-v3, continued pretraining is the primary mechanism: masked language modeling without labels bridges $\sim$60 percentage points (pp) of the out-of-distribution (OOD) gap (vanilla F1\,=\,0.31$\pm$0.03 $\to$ 0.91$\pm$0.12 on unseen attack types).
6	Cross-encoder validation on RoBERTa shows that domain adaptation is universally beneficial: RoBERTa vanilla achieves F1\,=\,0.981 on structurally simple Deceptive Delight but collapses to 0.466 on multi-persona ActorAttack, while classification-supervised variants maintain F1\,$\geq$\,0.93 on both.
7	Across both encoders, classification supervision provides cross-seed stability (variance reduced 4--20$\times$ vs.\ MLM-only, consistent across both OOD families). Domain adaptation's detection advantage persists under adversarial paraphrasing (McNemar $p < 0.001$), though absolute perturbation robustness varies by attack family.
8	These results on synthetic conversations from four attack families suggest that domain adaptation universally improves cross-attack generalization, with encoder pretraining method determining the difficulty threshold at which adaptation becomes critical; validation on larger, human-generated datasets is needed.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 113 · 2026-05-18T15:50:03.089724+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 114 · 2026-05-18T15:50:04.043978+00:00_

1	% introduction.tex — expanded for 8-page target
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Multi-turn jailbreak attacks pose a qualitatively different threat to large language model (LLM) safety than their single-turn counterparts. Attacks such as Crescendo~\citep{russinovich2024crescendo}, Foot-in-the-Door (FITD)~\citep{fitd2024}, and Deceptive Delight~\citep{deceptivedelight2024} distribute adversarial intent across individually benign turns through rapport building, logical reframing, and incremental escalation. Persuasion is the common mechanism: \citet{zeng2024pap} catalogue 40 persuasion techniques across jailbreak families, and \citet{hagendorff2026reasoning} find identifiable strategies in 97\% of successful attacks. Individual attack turns occupy the same embedding region as benign text~\citep{bullwinkel2025repeng}, rendering per-turn safety filters fundamentally blind.
7	
8	Production classifiers such as Llama Guard~\citep{inan2023llamaguard}, WildGuard~\citep{han2024wildguard}, and ShieldGemma~\citep{zeng2024shieldgemma} operate on individual turns and cannot model manipulation trajectories across exchanges. Recent multi-turn defenses have begun to address conversation-level structure: DeepContext~\citep{deepcontext2026} combines fine-tuned BERT with a multi-layer GRU, BIID~\citep{tong2025biid} infers turn-level intentions, and G-Guard~\citep{gguard2025} applies graph neural networks. These systems achieve reasonable in-distribution performance but are evaluated on single attack families and do not assess cross-dataset OOD transfer. None systematically analyze \emph{why} some representations generalize while others fail. The open question is: \emph{what representation properties enable cross-attack generalization?}
9	
10	A vanilla DeBERTa encoder~\citep{he2021deberta} with temporal aggregation collapses from F1\,=\,1.000 on in-distribution data to F1\,=\,0.312$\pm$0.026 on out-of-distribution (OOD) Deceptive Delight, worsening with more
…[truncated 3355 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 115 · 2026-05-18T15:50:04.044564+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 116 · 2026-05-18T15:50:04.547001+00:00_

1	% related_work.tex — D024 compressed
2	
3	\section{Related Work}
4	\label{sec:related_work}
5	
6	\paragraph{Multi-turn jailbreak attacks.}
7	Multi-turn attacks distribute adversarial intent across individually benign turns. Crescendo~\citep{russinovich2024crescendo} implements gradual escalation, FITD~\citep{fitd2024} exploits commitment-consistency bias, Deceptive Delight~\citep{deceptivedelight2024} combines emotional manipulation with role assignment, ActorAttack~\citep{ren2024actorattack} uses multi-persona steering, and PAIR~\citep{chao2023pair} automates iterative refinement. \citet{wei2023jailbroken} provide a unifying taxonomy grounded in competing objectives and mismatched generalization. Across these families, a shared reliance on persuasion dynamics~\citep{zeng2024pap,hagendorff2026reasoning,li2024mhj} distinguishes them from token-level attacks such as GCG~\citep{zou2023gcg}.
8	
9	\paragraph{Multi-turn defenses.}
10	Existing defenses model conversation-level structure but do not decompose what enables cross-attack generalization. DeepContext~\citep{deepcontext2026} combines fine-tuned BERT with a 3-layer GRU (hidden=2048) and achieves F1 = 0.84 on in-distribution data; however, its evaluation is limited to a single attack family and does not assess cross-dataset OOD transfer. BIID~\citep{tong2025biid} infers turn-level intentions, G-Guard~\citep{gguard2025} applies GNN classification, and SafeDream~\citep{safedream2026} predicts unsafe continuations. None of these systems evaluate generalization across attack families or analyze the mechanism that enables it. DisPeD's vanilla baseline represents the class of pretrained-encoder-plus-RNN approaches \emph{without} domain adaptation; it is not a direct proxy for DeepContext, which differs in encoder fine-tuning, model capacity, and loss function. Our contribution is the systematic decomposition showing that domain exposure, not architectural choices, is the primary factor for cross-attack generalization.
1
…[truncated 3599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 117 · 2026-05-18T15:50:04.547352+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 118 · 2026-05-18T15:50:04.999313+00:00_

1	% method.tex — D024 compressed
2	
3	\section{Method}
4	\label{sec:method}
5	
6	DisPeD is a two-stage framework for multi-turn jailbreak detection. Stage~1 adapts a turn-level encoder through continued training on jailbreak conversation text. Stage~2 aggregates turn representations for conversation-level binary classification. To systematically identify what enables cross-attack generalization, we design seven Stage-1 variants that decompose the contributions of domain exposure, classification supervision, label quality, label granularity, and domain specificity. Figure~\ref{fig:architecture} illustrates the pipeline.
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=\columnwidth]{figures/paper/fig1_architecture.pdf}
11	\caption{DisPeD architecture. Stage~1 adapts a DeBERTa encoder on jailbreak conversation text (seven variant objectives). Stage~2 aggregates frozen \texttt{[CLS]} embeddings via BiGRU for conversation-level jailbreak detection. Only user turns are processed.}
12	\label{fig:architecture}
13	\end{figure}
14	
15	\subsection{Problem Formulation}
16	
17	A conversation $C = \{u_1, a_1, \ldots, u_N, a_N\}$ alternates user turns $u_i$ and assistant responses $a_i$. Given a prefix of $K$ user turns, the model predicts $y \in \{0, 1\}$ (jailbreak vs.\ benign). We restrict input to user turns because adversarial intent resides in the attacker's messages. This formulation supports early detection from partial prefixes.
18	
19	\subsection{Stage 1: Turn-Level Encoder Adaptation}
20	\label{sec:stage1}
21	
22	Each user turn $u_i$ is encoded by DeBERTa-v3-base~\citep{he2021deberta}; the \texttt{[CLS]} embedding $h_i \in \mathbb{R}^d$ serves as the turn representation. Seven variants, summarized in Table~\ref{tab:variants}, share the same training data but differ in objective.
23	
24	\begin{table}[t]
25	\centering
26	\small
27	\caption{Stage-1 encoder variants. All operate on the same training conversations except Wikipedia MLM (matched token count on Wik
…[truncated 3728 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 119 · 2026-05-18T15:50:04.999715+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 120 · 2026-05-18T15:50:05.502320+00:00_

1	% experiments.tex — D024 compressed for 8-page limit
2	
3	\section{Experiments}
4	\label{sec:experiments}
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	\paragraph{Data.}
10	We train on 250 Crescendo~\citep{russinovich2024crescendo} jailbreak and 250 topic-anchored benign conversations generated via Qwen3-8B.
11	OOD evaluation uses 80 FITD~\citep{fitd2024}, 80 Deceptive Delight (DD)~\citep{deceptivedelight2024}, and ActorAttack~\citep{ren2024actorattack} conversations with no overlap in attack templates.
12	The IID test set consists of 76 held-out Crescendo conversations; a paraphrased version (BERTScore 0.92, lexical overlap 0.20) serves as the adversarial robustness benchmark.
13	
14	\paragraph{Models.}
15	Seven DeBERTa-v3 variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\ref{sec:method}).
16	For cross-encoder validation, we replicate vanilla, MLM, and 9-class variants on RoBERTa-base~\citep{liu2019roberta} (Section~\ref{sec:cross_encoder}).
17	We also compare TF-IDF LR and LLM-as-judge baselines (Appendix~\ref{sec:llm_judge}): GPT-5.5 achieves only F1 = 0.191--0.449 on IID Crescendo with 30--47\% unparseable responses; on OOD data, Qwen3-8B achieves F1 = 0.0 (DD) by predicting all conversations as benign. Content-level reasoning is insufficient for this task.
18	
19	\paragraph{Metrics.}
20	F1 for binary jailbreak detection at prefix $K$=2 and full conversations (full per-$K$ results in Appendix~\ref{sec:full_prefix}).
21	OOD results report 3-seed mean$\pm$std (seeds 42, 123, 456) for all variants except mean pooling (single seed).
22	Stage-1: learning rate $2 \times 10^{-5}$, batch 16, 4 epochs, MLM masking 15\%.
23	Stage-2: two-layer MLP, 20 epochs.
24	
25	%----------------------------------------------------------------------
26	\subsection{Cross-Attack Generalization}
27	\label{sec:cross_attack}
28	
29	\begin{table}[t]
30	\centering
31	\small
32	\caption{Cross-attack generalization (F1) at $K$=2 and full conversation. 3
…[truncated 23765 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 121 · 2026-05-18T15:50:05.502853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 122 · 2026-05-18T15:50:06.407802+00:00_

1	% conclusion.tex — reviewer revision
2	
3	\section{Conclusion}
4	\label{sec:conclusion}
5	
6	DisPeD's controlled ablation across two encoder architectures and four attack families provides preliminary evidence that domain adaptation universally improves cross-attack generalization. On DeBERTa-v3, continued pretraining bridges $\sim$60\,pp of the OOD gap (vanilla 0.31$\pm$0.03 $\to$ MLM 0.91$\pm$0.12), with strong early detection (F1 $\geq$ 0.97 at $K \leq 5$). RoBERTa vanilla achieves F1\,=\,0.981 on structurally simple Deceptive Delight but collapses to 0.466 on multi-persona ActorAttack; classification-supervised RoBERTa recovers to F1\,=\,0.939 on ActorAttack. Encoder pretraining method determines the difficulty threshold at which adaptation becomes critical, not whether adaptation is needed. Across both encoders, classification supervision provides cross-seed stability (variance reduced 4--20$\times$ vs.\ MLM-only, consistent across DD and ActorAttack) and interpretable characterization of known attack families (though strategy predictions do not transfer to unseen attacks, OOD $\kappa$=0.126). Domain adaptation's detection advantage persists under adversarial paraphrasing (McNemar $p < 0.001$), though absolute perturbation robustness is attack-family-dependent (zero degradation on DD, domain-adapted variants degrading on ActorAttack). On structurally complex ActorAttack, all three classification-supervised variants remain equivalent (0.951--0.990), confirming that label quality is not a factor for detection at any OOD difficulty level. Validation on larger and more diverse datasets is needed.
7	
8	\section{Limitations}
9	\label{sec:limitations}
10	
11	\paragraph{Dataset scale and diversity.}
12	The training set contains 500 synthetic conversations generated by a single model (Qwen3-8B), and OOD evaluation covers three attack families (FITD, Deceptive Delight, ActorAttack). This scale limits statistical power: the perturbation evaluation ($n$=76) means tier bo
…[truncated 2814 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 123 · 2026-05-18T15:50:06.408146+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 124 · 2026-05-18T15:50:06.960824+00:00_

1	% appendix.tex — Supplementary material
2	
3	\appendix
4	
5	\section{LLM-as-Judge Baseline}
6	\label{sec:llm_judge}
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\caption{LLM-as-judge zero-shot jailbreak detection (F1). IID: Crescendo test set; OOD: Deceptive Delight (DD) and FITD. F1 values for GPT-5.5 and Qwen3-8B exclude unparseable responses and represent upper bounds.}
12	\label{tab:llm_judge}
13	\begin{tabular}{@{}lccccr@{}}
14	\toprule
15	\textbf{Method} & $K$=2 & $K$=3 & $K$=5 & Full & Unparse. \\
16	\midrule
17	\multicolumn{6}{l}{\textit{IID (Crescendo)}} \\[2pt]
18	GPT-5.5 & .191 & .273 & .449 & .383 & 30--47\% \\
19	Qwen3-8B & .000 & .051 & .146 & .100 & 0\% \\
20	9-class (ours) & \textbf{1.000} & \textbf{1.000} & \textbf{1.000} & \textbf{1.000} & 0\% \\
21	\midrule
22	\multicolumn{6}{l}{\textit{OOD (Deceptive Delight)}} \\[2pt]
23	Qwen3-8B & .000 & .000 & .000 & .000 & 0\% \\
24	9-class (ours) & \textbf{.981} & \textbf{.972} & \textbf{.997} & \textbf{.997} & 0\% \\
25	\midrule
26	\multicolumn{6}{l}{\textit{OOD (FITD)}} \\[2pt]
27	Qwen3-8B & .000 & .000 & .025 & .025 & 0\% \\
28	9-class (ours) & \textbf{1.000} & -- & -- & \textbf{1.000} & 0\% \\
29	\bottomrule
30	\end{tabular}
31	\end{table}
32	
33	Table~\ref{tab:llm_judge} reports zero-shot performance for GPT-5.5 and Qwen3-8B on IID and OOD data.
34	On IID Crescendo, GPT-5.5 achieves precision of 1.0 at all turn prefixes but recall ranges from only 0.105 to 0.290, resulting in F1 of 0.191 at $K$=2 and 0.449 at $K$=5.
35	A substantial fraction (30--47\%) of responses are unparseable; F1 values exclude these and represent upper bounds.
36	Full-conversation F1 (0.383) is lower than $K$=5 F1 (0.449) because the unparseable rate grows with context length.
37	Qwen3-8B performs worse across all IID prefixes (F1 from 0.000 at $K$=2 to 0.100 on full conversations).
38	On OOD data, Qwen3-8B predicts all conversations as benign (F1 = 0.0 on DD, F1 = 0.025 on FITD), while DisPeD maintains F1 $\geq$ 0.997 on DD 
…[truncated 6704 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 125 · 2026-05-18T15:50:07.061709+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 126 · 2026-05-18T15:50:13.285829+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here's a comprehensive overview of the EMNLP 2026 call for papers submission guidelines and author instructions:

## General Submission Information

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. EMNLP 2026 has a goal of curating a diverse technical program—in addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## 
…[truncated 2000 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "elapsed_ms": 11602
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-18T15:50:13.286309+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'persuasion_turn_jailbreak_detect'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6224
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-18T15:50:23.880709+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit long short paper guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format page limit long short paper guidelines"
  }
}
```

</details>

---


### Tool call

_source line 129 · 2026-05-18T15:50:24.533937+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR May submission template anonymous review requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR May submission template anonymous review requirements"
  }
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-18T15:50:25.337130+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "decisions.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect",
    "file": "decisions.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool call

_source line 131 · 2026-05-18T15:50:26.742770+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-18T15:50:27.746726+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-18T15:50:30.307377+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit long short paper guidelines"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, here are the ACL Rolling Review 2026 submission format guidelines:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Short papers may consist of up to four (4) pages of content, plus unlimited pages of references.

## Sections Not Counted Toward Page Limit

ACL currently requires all submissions to have a sec
…[truncated 1072 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "elapsed_ms": 6426
}
```

</details>

---


### Tool result

_source line 134 · 2026-05-18T15:50:33.313230+00:00_

Web search results for query: "EMNLP 2026 ARR May submission template anonymous review requirements"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"CoNLL 2026 | CoNLL","url":"https://conll.org/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the web search results, here's what I found regarding EMNLP 2026 ARR May submission requirements:

## Anonymity and Review Requirements

Following the ACL and ARR policies, there is no anonymity period requirement. However, there is no anonymity period or limitation on posting or discussing non-anonymous preprints while the work is under peer review, but the policy incentivizes anonymous submissions by special paper awards and priority in acceptance decisions for borderline papers.

The reviewing process will continue to be double-blind. Reviewers will not see authors, nor wil
…[truncated 1025 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "elapsed_ms": 8779
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-18T15:50:33.364266+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/decisions.yaml\", \"content\": \"_next_id: 35\\ndecisions:\\n- id: D001\\n  date: 2026-05-17 16:09 UTC\\n  summary: 接受 DeBERTa F1=0.789 作为 baseline，停止数据 TF-IDF 迭代，reframe MVP 为 early detection\\n  rationale: 'DeBERTa F1=0.789 已在目标范围(0.70-0.85)。TF-IDF F1=0.924 高但不致命——论文 reframe:\\n    TF-IDF/vanilla 方法需完整对话才能分类，DisPeD 在 K=2-3 turns 即可通过 persuasion trajectory 早期检测。这完美对齐\\n    Bullwinkel et al. 的核心发现（早期 turns 表征为 benign）。数据迭代已耗 4 轮 6+ 小时，继续追 TF-IDF 阈值的 ROI\\n    为负。用 Crescendo oracle labels (intended_strategy) 替代 GPT 标注，节省 API 成本和时间。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-17 16:49 UTC\\n  summary: MVP PASS — early detection K=2 +10.8pp, K=3 +5.9pp 超过阈值；TF-IDF=1.0 标记为\\n    research 阶段优先解决项\\n  rationale: Treatment (persuasion-grounded DeBERTa → GRU) 在 K=2 时 F1=0.987 vs baseline\\n    0.879 (+10.8pp)，K=3 时 +5.9pp，均超过 MVP 阈值 +5pp。Full conversation F1 差距仅 +1.3pp 未达\\n    +2pp 阈值，但 early detection 是核心 claim 所在。TF-IDF=1.0 表明词汇 shortcut 仍存在，但 (1) 不影响\\n    treatment vs baseline 相对比较的有效性，(2) 可作为 paper motivation（lexical cues 偶然有效但可被攻击者规避，pragmatic\\n    patterns 不可规避），(3) research 阶段通过 adversarial perturbation 实验验证 robustness。\\n  related_experiments:\\n  - exp_id: pilot_phase_b\\n    role: pipeline_validation\\n    result: success (n=270, directionally positive but not statistically meaningful)\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-17 16:59 UTC\\n  summary: 进入 Research 阶段，framing 定位为 Pragmatic Evasion Asymmetry，experiment plan\\n    含 6 个 P0 实验\\n  rationale: MVP PASS (D002) 后按 post-mvp-kickoff 流程：paper_framing.md 将核心贡献从\\\"更好的检测器\\\"升级为\\\"语用逃逸不对称性原则的首个实证验证\\\"（源自\\n    Human Review Note），experiment_plan.yaml 优先解决 TF-IDF=1.0 数据质量阻塞。Dream full review\\n    已发起，等回调后审批 P0。\\n  related_experiments:\\n  - exp_id: phase_b_full\\n    role: motivation\\n    result: K=2 +10.8pp but 
…[truncated 3563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 8027
}
```

</details>

---


### Tool result

_source line 136 · 2026-05-18T15:50:33.364835+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "elapsed_ms": 6622
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-18T15:50:33.365391+00:00_

1	% References for persuasion_turn_jailbreak_detect
2	% Auto-generated from literature_map.yaml (2026-05-18)
3	% Total entries: 31
4	
5	% ============================================================
6	% Category 1: Production Multi-Turn Safety Systems
7	% ============================================================
8	
9	@article{inan2023llamaguard,
10	  title={Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations},
11	  author={Inan, Hakan and Upasani, Kartikeya and Chi, Jianfeng and Rungta, Rashi and Iyer, Krithika and Mao, Yuning and Tontchev, Michael and Hu, Qing and Fuller, Brian and Testuggine, Davide and Khabsa, Madian},
12	  journal={arXiv preprint},
13	  year={2023},
14	  eprint={2312.06674},
15	  archivePrefix={arXiv},
16	}
17	
18	@misc{metallamaguard3_2024,
19	  title={Llama Guard 3},
20	  author={{Meta AI}},
21	  year={2024},
22	  howpublished={Meta AI (released with Llama 3.1)},
23	}
24	
25	@article{zeng2024shieldgemma,
26	  title={ShieldGemma: Generative AI Content Moderation Based on Gemma},
27	  author={Zeng, Wenjun and Liu, Yuchi and Mullins, Ryan and Peran, Ludovic and Fernandez, Joe and Harkous, Hamza and Narasimhan, Karthik and Proud, Drew and Kumar, Piyush and Radharapu, Bhaktipriya and Sturman, Olivia and Wahltinez, Oscar},
28	  journal={arXiv preprint},
29	  year={2024},
30	  eprint={2407.21772},
31	  archivePrefix={arXiv},
32	}
33	
34	@inproceedings{han2024wildguard,
35	  title={WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs},
36	  author={Han, Seungju and Rao, Kavel and Ettinger, Allyson and Jiang, Liwei and Lin, Bill Yuchen and Lambert, Nathan and Choi, Yejin and Dziri, Nouha},
37	  booktitle={Advances in Neural Information Processing Systems},
38	  year={2024},
39	}
40	
41	@article{anthropic2025constitutional,
42	  title={Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming},
43	  author={{Anthropic}},
44	  journal={arXiv 
…[truncated 15524 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 5618
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-18T15:50:37.836185+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
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

_source line 139 · 2026-05-18T15:50:37.836676+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-18T15:50:39.393373+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-18T15:50:39.444266+00:00_

1	issues:
2	  - id: "R1-N1"
3	    summary: "Evidence hierarchy 统计基础不一致：binary/scrambled 仅 seed 42，其他变体 3-seed，核心排序无方差支撑"
4	    category: experiment
5	    severity: critical
6	    status: resolved
7	    first_raised_round: 1
8	    last_seen_round: 1
9	    mentions:
10	      - round: 1
11	        reviewers: [1, 2]
12	        note: "R1 首提 N1，R2 独立发现 N4，交叉回应双方完全同意。"
13	    action_items:
14	      - round: 1
15	        action: "训练 binary (seed 123, 456) + scrambled (seed 123, 456) Stage 1+2，DD OOD 评估"
16	        assigned_to: main_agent
17	        status: resolved
18	    resolution: "MF1 完成: binary 3-seed=0.997±0.005, scrambled 3-seed=0.997±0.005"
19	    resolution_round: 1
20	
21	  - id: "R1-N2"
22	    summary: "Three-layer robustness attribution 在 n=76 上缺乏统计显著性"
23	    category: experiment
24	    severity: critical
25	    status: resolved
26	    first_raised_round: 1
27	    last_seen_round: 1
28	    mentions:
29	      - round: 1
30	        reviewers: [1, 2]
31	        note: "R1 首提 N2。"
32	    action_items:
33	      - round: 1
34	        action: "McNemar's test + bootstrap CI; 降级为 observed pattern"
35	        assigned_to: main_agent
36	        status: resolved
37	    resolution: "MF2 完成: IID McNemar 全不显著 (p>0.13). OOD perturbation (n=118): 9-class vs vanilla p<0.001 (49-78 discordant pairs). Three-layer 降级为 observed pattern."
38	    resolution_round: 1
39	
40	  - id: "R1-N3"
41	    summary: "缺少与已发表 multi-turn defense 的直接实验对比"
42	    category: experiment
43	    severity: critical
44	    status: resolved
45	    first_raised_round: 1
46	    last_seen_round: 1
47	    mentions:
48	      - round: 1
49	        reviewers: [1, 2]
50	        note: "R1 首提 N3。"
51	    action_items:
52	      - round: 1
53	        action: "重构论证：vanilla ≠ DeepContext proxy"
54	        assigned_to: paper_agent
55	        status: resolved
56	    resolution: "Paper Agent 已重构 related_work.tex"
57	    resolution_round: 1
58	
59	  - id: "R1-N4"
60	    summary: "数据集规模过小"
61	    category: experiment
62	    seve
…[truncated 7581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-18T15:50:45.268286+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-18T15:50:45.319007+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-18T15:50:48.883941+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/agent"
  }
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-18T15:50:48.984849+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_director_93d7fc7c.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 146 · 2026-05-18T15:50:53.352893+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect -name \"*.yaml\" -not -path \"*/artifacts/*\" -not -path \"*/.claude/*\" 2>/dev/null | head -20",
  "description": "Find project config YAML files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect -name \"*.yaml\" -not -path \"*/artifacts/*\" -not -path \"*/.claude/*\" 2>/dev/null | head -20",
    "description": "Find project config YAML files"
  }
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-18T15:50:53.554628+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/experiment_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-18T15:50:56.821750+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-18T15:50:56.922804+00:00_

AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:151:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:151:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/logs/chats/feishu_group_oc_613965f45d48763f375aa83e9294b24a_director.jsonl:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/logs/chats/feishu_group_oc_613965f45d48763f375aa83e9294b24a_director.jsonl:6:{"ts": "2026-05-18T08:35:41.861299+00:00", "role": "tool", "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director", "text": "called ToolSearch", "tool": "ToolSearch", "tool_args": {"query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status", "max_result
…[truncated 3613 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Grep",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-18T15:51:51.911901+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你负责审查**方法严谨性、实验设计和统计有效性**。\n\n## 论文信息\n- **标题**: What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap\n- **目标 venue**: EMNLP 2026（ARR May cycle）\n- **Deadline**: 2026-05-25\n- **格式**: ACL style long paper（8 页正文 + unlimited references + Limitations section 不计页数）\n- **匿名规则**: Double-blind\n- **论文路径**: projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex\n  - 分文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex\n  - 引用: references.bib\n\n## 你的审查侧重\n\n重点评估以下方面：\n\n1. **实验设计合理性**\n   - 7 个 Stage-1 变体的 ablation 是否充分隔离了目标因素？是否存在未控制的 confound？\n   - 训练数据 250+250 对话、OOD 数据 80-118 对话的规模是否足以支撑所宣称的结论？\n   - 3-seed 评估是否足够？哪些结论需要更多 seed？\n   - Cross-encoder validation（RoBERTa）的设计是否充分？\n\n2. **统计有效性**\n   - 报告的 mean±std 是否有 significance test 支撑？\n   - McNemar test 的使用是否恰当？样本量是否足够？\n   - Perturbation analysis 中的 three-layer pattern 的统计基础是否充分？\n   - 置信区间是否被报告？效应量是否有意义？\n\n3. **方法设计**\n   - BiGRU + frozen encoder 的 two-stage 设计是否合理？为什么不 end-to-end？\n   - Stage-1 七个变体之间是否真正公平比较（相同数据、相同超参数、相同 Stage-2）？\n   - Mean pooling vs BiGRU 的对比是否充分？\n   - 策略标注质量（Cohen's κ=0.78, n=50）是否足够？\n\n4. **Baseline 充分性**\n   - 是否缺少关键 baseline？（如 DeepContext、BIID、G-Guard 的直接对比）\n   - TF-IDF LR 强表现（0.944）对核心 claim 的冲击有多大？\n   - LLM-as-judge baseline 的设置是否公平？\n\n5. **可复现性**\n   - 超参数、数据生成流程、标注 prompt 是否完整披露？\n   - 代码/数据是否承诺发布？\n\n请按以下格式输出审稿意见：\n- **Summary**: 2-3 句论文概述\n- **Strengths** [S1, S2, ...]: 优点\n- **Weaknesses** [W1, W2, ...]: 缺点（标注 severity: critical/major/minor）\n- **Questions** [Q1, Q2, ...]: 需作者澄清的问题\n- **Missing References**: 遗漏的重要引用\n- **Overall Assessment**: 评分 + 置信度"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你负责审查**方法严谨性、实验设计和统计有效性**。\n\n## 论文信息\n- **标题**: What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap\n- **目标 venue**: EMNLP 2026（ARR May cycle）\n- **Deadline**: 2026-05-25\n- **格式**: ACL style long paper（8 页正文 + unlimited references + Limitations section 不计页数）\n- **匿名规则**: Double-blind\n- **论文路径**: projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex\n  - 分文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex\n  - 引用: references.bib\n\n## 你的审查侧重\n\n重点评估以下方面：\n\n1. **实验设计合理性**\n   - 7 个 Stage-1 变体的 ablation 是否充分隔离了目标因素？是否存在未控制的 confound？\n   - 训练数据 250+250 对话、OOD 数据 80-118 对话的规模是否足以支撑所宣称的结论？\n   - 3-seed 评估是否足够？哪些结论需要更多 seed？\n   - Cross-encoder validation（RoBERTa）的设计是否充分？\n\n2. **统计有效性**\n   - 报告的 mean±std 是否有 significance test 支撑？\n   - McNemar test 的使用是否恰当？样本量是否足够？\n   - Perturbation analysis 中的 three-layer pattern 的统计基础是否充分？\n   - 置信区间是否被报告？效应量是否有意义？\n\n3. **方法设计**\n   - BiGRU + frozen encoder 的 two-stage 设计是否合理？为什么不 end-to-end？\n   - Stage-1 七个变体之间是否真正公平比较（相同数据、相同超参数、相同 Stage-2）？\n   - Mean pooling vs BiGRU 的对比是否充分？\n   - 策略标注质量（Cohen's κ=0.78, n=50）是否足够？\n\n4. **Baseline 充分性**\n   - 是否缺少关键 baseline？（如 DeepContext、BIID、G-Guard 的直接对比）\n   - TF-IDF LR 强表现（0.944）对核心 claim 的冲击有多大？\n   - LLM-as-judge baseline 的设置是否公平？\n\n5. **可复现性**\n   - 超参数、数据生成流程、标注 prompt 是否完整披露？\n   - 代码/数据是否承诺发布？\n\n请按以下格式输出审稿意见：\n- **Summary**: 2-3 句论文概述\n- **Strengths** [S1, S2, ...]: 优点\n- **Weaknesses** [W1, W2, ...]: 缺点（标注 severity: critical/major/minor）\n- **Questions** [Q1, Q2, ...]: 需作者澄清的问题\n- **Missing References**: 遗漏的重要引用\n- **Overall Assessment**: 评分 + 置信度"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-18T15:52:06.403188+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 14491
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-18T15:52:06.654150+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你负责审查**新颖性、Related Work 定位、写作质量和论文完整性**。\n\n## 论文信息\n- **标题**: What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap\n- **目标 venue**: EMNLP 2026（ARR May cycle）\n- **Deadline**: 2026-05-25\n- **格式**: ACL style long paper（8 页正文 + unlimited references + Limitations section 不计页数）\n- **匿名规则**: Double-blind\n- **论文路径**: projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex\n  - 分文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex\n  - 引用: references.bib\n\n## 你的审查侧重\n\n重点评估以下方面：\n\n1. **新颖性与贡献评估**\n   - 核心贡献（domain exposure 是 cross-attack generalization 的主因）是否足够新颖？\n   - 与 Don't Stop Pretraining (Gururangan et al., 2020) 的增量在哪里？\n   - 论文自称 \"preliminary findings\"，这种定位在 EMNLP long paper 中是否合适？\n   - 七个 ablation 变体的设计是否有独到之处？\n\n2. **Related Work 评估**\n   - 对 multi-turn defense 的综述是否全面？是否遗漏重要工作？\n   - 与 DeepContext/BIID/G-Guard/SafeDream 的定位是否清晰准确？\n   - Discourse analysis 和 computational persuasion 的理论基础是否扎实？\n   - 是否存在 overclaiming 或 underclaiming 的定位问题？\n\n3. **写作质量**\n   - Abstract 是否在 30 秒内传达核心价值？\n   - Introduction 的故事线是否连贯（问题 → 洞察 → 方法 → 证据）？\n   - 段落结构、过渡、术语一致性\n   - 是否存在 AI 写作痕迹（em-dash、-ing phrases、过度分段等）？\n   - 图表知识密度和可读性\n   - Limitations section 是否诚实且全面？\n\n4. **论文完整性**\n   - 是否有未回答的关键问题？\n   - 结论是否与证据匹配（不过度宣称也不过度保守）？\n   - 附录内容是否在正文中被引用？\n   - 引用格式和充足度\n\n5. **格式合规**\n   - 页数是否符合 8 页限制？\n   - Limitations section 是否作为独立 section 存在？\n   - ACL style 合规性（行号、匿名化、字体）\n   - Responsible NLP Checklist 是否需要？\n\n请按以下格式输出审稿意见：\n- **Summary**: 2-3 句论文概述\n- **Strengths** [S1, S2, ...]: 优点\n- **Weaknesses** [W1, W2, ...]: 缺点（标注 severity: critical/major/minor）\n- **Questions** [Q1, Q2, ...]: 需作者澄清的问题\n- **Missing References**: 遗漏的重要引用\n- **Overall Assessment**: 评分 + 置信度"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你负责审查**新颖性、Related Work 定位、写作质量和论文完整性**。\n\n## 论文信息\n- **标题**: What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap\n- **目标 venue**: EMNLP 2026（ARR May cycle）\n- **Deadline**: 2026-05-25\n- **格式**: ACL style long paper（8 页正文 + unlimited references + Limitations section 不计页数）\n- **匿名规则**: Double-blind\n- **论文路径**: projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex\n  - 分文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex\n  - 引用: references.bib\n\n## 你的审查侧重\n\n重点评估以下方面：\n\n1. **新颖性与贡献评估**\n   - 核心贡献（domain exposure 是 cross-attack generalization 的主因）是否足够新颖？\n   - 与 Don't Stop Pretraining (Gururangan et al., 2020) 的增量在哪里？\n   - 论文自称 \"preliminary findings\"，这种定位在 EMNLP long paper 中是否合适？\n   - 七个 ablation 变体的设计是否有独到之处？\n\n2. **Related Work 评估**\n   - 对 multi-turn defense 的综述是否全面？是否遗漏重要工作？\n   - 与 DeepContext/BIID/G-Guard/SafeDream 的定位是否清晰准确？\n   - Discourse analysis 和 computational persuasion 的理论基础是否扎实？\n   - 是否存在 overclaiming 或 underclaiming 的定位问题？\n\n3. **写作质量**\n   - Abstract 是否在 30 秒内传达核心价值？\n   - Introduction 的故事线是否连贯（问题 → 洞察 → 方法 → 证据）？\n   - 段落结构、过渡、术语一致性\n   - 是否存在 AI 写作痕迹（em-dash、-ing phrases、过度分段等）？\n   - 图表知识密度和可读性\n   - Limitations section 是否诚实且全面？\n\n4. **论文完整性**\n   - 是否有未回答的关键问题？\n   - 结论是否与证据匹配（不过度宣称也不过度保守）？\n   - 附录内容是否在正文中被引用？\n   - 引用格式和充足度\n\n5. **格式合规**\n   - 页数是否符合 8 页限制？\n   - Limitations section 是否作为独立 section 存在？\n   - ACL style 合规性（行号、匿名化、字体）\n   - Responsible NLP Checklist 是否需要？\n\n请按以下格式输出审稿意见：\n- **Summary**: 2-3 句论文概述\n- **Strengths** [S1, S2, ...]: 优点\n- **Weaknesses** [W1, W2, ...]: 缺点（标注 severity: critical/major/minor）\n- **Questions** [Q1, Q2, ...]: 需作者澄清的问题\n- **Missing References**: 遗漏的重要引用\n- **Overall Assessment**: 评分 + 置信度"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-18T15:52:08.114076+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1459
}
```

</details>

---


### Assistant

_source line 154 · 2026-05-18T15:52:11.122842+00:00_

Round 1 任务已分配给两位 Reviewer。等待审稿结果返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 11

## Round 11

2 recorded events


### User

_source line 155 · 2026-05-18T15:56:35.983808+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿意见：方法严谨性、实验设计与统计有效性

**论文**: What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap
**Venue**: EMNLP 2026 (ARR May cycle)

---

## Summary

本文提出 DisPeD，一个两阶段框架（Stage-1 encoder adaptation + Stage-2 BiGRU aggregation），通过 7 个受控 Stage-1 变体系统分解跨攻击泛化的机制。核心发现是：(1) 在 DeBERTa-v3 上，continued pretraining（MLM）桥接了约 60pp 的 OOD gap；(2) 分类监督提供跨 seed 稳定性而非检测提升；(3) RoBERTa 交叉验证显示 encoder pretraining method 决定适应阈值。实验在合成数据（Qwen3-8B 生成）上的 4 个攻击家族上进行。

---

## 总体评分

**Overall**: 2.5（介于 Findings 和 Resubmit next cycle 之间）
**一句话总结**: ablation 设计思路清晰，但极小的合成数据规模、缺失的关键 baseline 对比、以及 TF-IDF 对核心 claim 的冲击，使得主要结论缺乏充分支撑。

---

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2.5/5 | 核心 confound 未控制（单模型生成全部数据）；统计功效不足；TF-IDF 威胁核心叙事 |
| Excitement | 2.5/5 | 问题重要且 ablation 思路有价值，但合成数据 + 小规模限制了实际影响力 |
| Reproducibility | 3.5/5 | 超参数和训练细节充分；但生成 prompt 和标注 prompt 未披露（仅承诺发布） |
| Confidence | 4/5 | 熟悉 domain-adaptive pretraining、adversarial NLP 和 jailbreak detection 领域 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 单模型生成全部数据造成系统性 confound
- 具体位置：Section 4.1 (Setup), Section 3 (Method), Appendix E (Reproducibility Details)
- 问题：Qwen3-8B 同时用于生成训练数据（Crescendo jailbreak + benign）、策略标注（9-class labels）、OOD 测试数据（DD, FITD）、以及对抗性 paraphrase。这意味着所有数据共享同一个 LLM 的文本分布特征。TF-IDF LR 在 OOD DD 上达到 0.944（Table 1），**强烈暗示模型在利用单一 LLM 的 stylistic artifacts 而非真正的 discourse-level 特征**。论文在 Section 5（Limitations）承认了 lexical separability，但未做任何实验区分 "domain adaptation captures pragmatic features" vs. "domain adaptation memorizes Qwen3-8B's generation artifacts" 这两个竞争假设。
- 为什么影响接收：这是论文最核心 claim（"domain exposure bridges the cross-attack gap"）的替代解释。如果 OOD gap 的桥接主要来自学习生成模型的 stylistic fingerprint，则整个 evidence hierarchy 可能是 artifact-driven。
- 建议修改方向：(1) 至少用一个不同 LLM（如 Llama 3）生成部分 OOD 数据并测试；(2) 用人类编写的 multi-turn jailbreak 数据（如 MHJ dataset, Li et al. 2024）做 OOD 评估；(3) 做 probing 实验（论文自己在 Section 5 提到了但 defer 到 future work）区分 lexical 和 discourse-level 特征。

**N2** [critical] 缺少与现有 multi-turn defense 系统的直接对比
- 具体位置：Section 2 (Related Work), Table 1
- 问题：论文在 Introduction 和 Related Work 中讨论了 DeepContext、BIID、G-Guard、SafeDream 四个同期/近期系统，但实验中**未与任何一个直接对比**。Section 2 声称 "DisPeD's vanilla baseline represents the class of pretrained-encoder-plus-RNN approaches without domain adaptation"，但 vanilla DeBERTa（frozen, 1-layer BiGRU, hidden=128）与 DeepContext（fine-tuned BERT, 3-layer GRU, hidden=2048）在 capacity、训练方式、loss function 上完全不同。用一个刻意弱化的 baseline 来 "represent" 一类方法是不公平的。
- 为什么影响接收：审稿人无法判断 DisPeD 相对于已有 multi-turn defense 的实际增量。论文声称 "none systematically analyze why some representations generalize"（Introduction, para 2），但如果 DeepContext 的 fine-tuned BERT+GRU 本身就能泛化（其论文未测 OOD 不代表不能泛化），则 DisPeD 的贡献主要是分析性的而非方法论的，这需要更明确的 positioning。
- 建议修改方向：(1) 复现 DeepContext（BERT + 3-layer GRU）作为 baseline；(2) 如果无法复现，至少在一个共同 benchmark 上比较数值；(3) 明确 claim 论文贡献是分析框架（"what enables generalization"）而非 SOTA 方法。

**N3** [critical] 数据规模严重不足以支撑 statistical claims
- 具体位置：Section 4.1, Table 3, Section 4.4
- 问题：训练数据 500 对话（250 jailbreak + 250 benign）、IID 测试 76 对话、OOD DD 80-118 对话、OOD FITD 80 对话。在这样的规模上：
  - Table 3 (Perturbation) 的 "three-layer pattern" 基于 n=76，discordant pairs ≤7。论文自己承认 "tier boundaries correspond to 1-3 misclassifications"（Section 5），但仍在 Section 4.4 用了大量篇幅讨论这个 pattern（包括 "K=1 both granularity and correctness contribute independently"），且将其放在 Table 3 caption 中。
  - FITD 完全不提供 discriminative power：vanilla 和 9-class 均达到 F1 ≥ 0.990（Section 4.2, "FITD is easier"）。实际有效的 OOD 测试只有 DD 和 ActorAttack。
  - 3-seed 评估下，MLM-only 的 DD-Full std = 0.115（seed 456 recall = 0.64，Section 4.2）。如此大的 seed variance 意味着 3 个 seed 远不足以可靠估计 mean performance。
- 为什么影响接收：Evidence hierarchy 中的排序关系（Table 2）在 3-seed 下很多对之间的 confidence intervals 重叠。"Classification supervision adds ~8pp over MLM" 这个 claim 可能在 5-seed 或 10-seed 下不成立。
- 建议修改方向：(1) 至少 5 seeds，理想情况下 10 seeds；(2) 报告 bootstrap 95% confidence intervals；(3) 对关键对比（MLM vs. 9-class, adapted vs. non-adapted）进行 paired bootstrap 或 permutation test。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] TF-IDF baseline 对核心叙事的冲击未充分 address
- 具体位置：Table 1, Section 4.2 (para 3), Section 5 (Limitations)
- 问题：TF-IDF LR 在 OOD DD 达到 0.944，仅比 MLM（0.914）高 3pp，比 9-class（0.997）低 5.3pp。论文声称 DisPeD 优势在 "cross-seed stability, temporal early detection at K≤5, and interpretability"。但 TF-IDF 无 seed variance（deterministic），且论文未报告 TF-IDF 在 K&lt;Full 的表现（Table 1 中 TF-IDF 的 K=2 列为 "--"）。如果 TF-IDF 在 K=2 表现也不错，则 DisPeD 的 "early detection" 优势也可能不成立。
- 建议：(1) 报告 TF-IDF 在所有 prefix lengths 的结果；(2) 报告 TF-IDF 在 ActorAttack 上的结果；(3) 更诚实地讨论 "当前合成数据上，bag-of-words 足矣" 的含义。

**W2** [major] BiGRU + frozen encoder 的设计选择缺乏充分 justification
- 具体位置：Section 3.3, Section 4.3 ("Temporal modeling" paragraph)
- 问题：(1) 为什么 freeze Stage-1 encoder？end-to-end fine-tuning 可能改变 evidence hierarchy。论文声称 "this separation ensures that the seven Stage-1 variants produce comparable embeddings evaluated under identical downstream conditions"，但 ablation study 可以在 end-to-end 设置下同样进行。(2) Mean pooling 在 single seed 下达到 F1=1.000，高于 3-seed BiGRU average（0.997）。这个 single-seed 结果被用来支持 "detection relies primarily on per-turn representations rather than their sequential order" 的 claim，但 single-seed 与 3-seed 结果不可比。
- 建议：(1) 讨论 frozen vs. end-to-end 的 trade-off，承认 frozen 设计可能低估某些 variants 的潜力；(2) Mean pooling 需要 multi-seed 验证后才能做任何 claim。

**W3** [major] LLM-as-judge baseline 不公平
- 具体位置：Appendix A (Table 5), Introduction (para 3), Section 4.1
- 问题：GPT-5.5 和 Qwen3-8B 仅做 zero-shot evaluation。(1) 未测试 few-shot 或 chain-of-thought prompting；(2) 30-47% unparseable responses 暗示 prompt 设计可能有问题而非 LLM 能力不足；(3) 用 unparseable responses 之外的数据计算的 F1 被称为 "upper bounds"，但实际上 unparseable 可能都是 positive cases（conservative 估计），反过来也可能都是 negative cases。这个 baseline 被用来支持 "content-level reasoning is insufficient"（Introduction, para 3）这个强 claim。
- 建议：(1) 测试 few-shot（至少 3-5 examples）；(2) 修复 prompt 使 unparseable rate < 5%；(3) 弱化 claim 为 "zero-shot LLM-as-judge is insufficient"。

**W4** [major] 策略标注质量验证不足
- 具体位置：Section 3.2 (para 3), Section 5 (Limitations)
- 问题：Cohen's κ=0.78 基于 n=50 的 human-model agreement，且只有 "a human sample"（似乎是单个标注员）。(1) n=50 对于 9-class classification 太小（每类平均 ~5.5 samples）；(2) 单个人类标注员无法评估 inter-annotator agreement（κ 衡量的是 model-vs-single-human，不是 human-human agreement）；(3) κ=0.78 被描述为 "substantial"，但对于 9-class taxonomy 作为训练信号，这个 agreement level 意味着约 22% 的标注是错误的。
- 建议：(1) 至少两个独立人类标注员 + human-human κ；(2) n ≥ 100 以覆盖所有 9 个 class。

**W5** [minor] α=0.3 的 loss weight 未 justify
- 具体位置：Section 3.2 (para 3, "α = 0.3")
- 问题：9-class variant 的 combined loss 中 binary intent loss 的权重 α=0.3 未提供选择依据或 sensitivity analysis。
- 建议：简要说明选择理由或报告 α ∈ {0.1, 0.3, 0.5, 1.0} 的 sensitivity。

---

## 小问题（不影响接收）

- Table 2: Mean pooling 标注为 single seed(†) 但 F1=1.000 是所有 variants 中最高的，容易误导读者。建议将其从 evidence hierarchy 中移出或标注更显著的 caveat。
- Section 4.2: "MLM achieves mean F1 ≥ 0.97 at all prefixes K ≤ 5" — 但 Table 6 显示 MLM K=1 为 0.973±0.019，这里用 "≥ 0.97" 是准确的但给人印象比实际更强。
- Appendix Table 7 (ActorAttack): Binary 的 per-K 结果标注为 n=2 seeds，与其他 variants 的 3 seeds 不一致，未解释原因。
- CKA 分析（Section 4.5）：Centered CKA 数值（vanilla-to-MLM: 0.442）被用于 interpretive analysis，但未解释 CKA 在这个 context 下的意义（什么 CKA 值算 "large shift"？）。

---

## Questions（需作者澄清）

**Q1**: OOD test data (DD, FITD, ActorAttack) 是否也由 Qwen3-8B 生成？如果是，那么 "cross-attack generalization" 实际上是 "cross-template generalization within same LLM distribution"，这与论文标题和 claim 的含义有本质区别。

**Q2**: Table 2 中 scrambled labels 达到 0.997±0.005（与 9-class 完全相同），论文将此解释为 "classification objective functions as a regularizer"。但另一个解释是：在如此小的数据集上，任何分类 head 的 gradient signal 都足以 nudge representations 到 separable region，这不需要 "regularizer" 这样的 mechanistic 解释。作者如何区分这两种解释？

**Q3**: 为什么 FITD results 在 Table 6 中缺少 K=3, K=5 的结果（标注为 "--"）？FITD 对话不够长吗？如果是，这应该在 data description 中说明。

**Q4**: Perturbation analysis 中 ActorAttack 的 9-class 变体 Δ Full 为 -20.4±13.5pp，seed variance 极大（-1.3pp to -30.3pp）。3 个 seed 中 2 个 degradation > 30pp 而 1 个仅 1.3pp。这是否暗示 ActorAttack 的 perturbation robustness 根本不稳定，现有结论不可靠？

**Q5**: 论文声称 "encoder pretraining method determines the difficulty threshold"（Section 4.5），但 DeBERTa-v3-base 和 RoBERTa-base 的参数量和训练数据也不同。如何排除 model capacity 或 training data 规模的 confounding effect？

---

## Missing References

- **MHJ dataset** (Li et al., 2024): 论文已 cite 但未用其人类生成的 multi-turn jailbreak 数据做评估，这是最明显的遗漏实验。
- **JailbreakBench** (Chao et al., 2024): 标准化的 jailbreak evaluation benchmark，未讨论。
- **HarmBench** (Mazeika et al., 2024): 标准化的 red-teaming evaluation framework，未讨论。
- 未见 **Latent Jailbreak** (Qiu et al., 2023) 或 **AutoDAN** (Liu et al., 2024) 等其他 multi-turn/iterative 攻击方法的讨论。

---

## 主要优势

**S1**: ablation 设计思路优秀。7 个 Stage-1 变体的设计经过深思熟虑，每个变体隔离一个特定因素（domain exposure, label quality, granularity, domain specificity, misaligned supervision）。这是论文最有价值的贡献。

**S2**: 诚实的 limitations 讨论。论文在 Section 5 中坦率地承认了数据规模、lexical separability、strategy annotation quality、single-seed issues、scope limitations 等问题。这种 intellectual honesty 在同类论文中少见。

**S3**: Cross-encoder validation 提供了有价值的对比视角。DeBERTa vs. RoBERTa 的 "difficulty threshold" 观察（DD 上 RoBERTa vanilla 成功但 ActorAttack 上失败）是一个有趣且有 practical implications 的发现。

**S4**: Topic classification 作为 negative control。Topic variant 的表现（worse than Wiki MLM despite using same domain data）cleanly separates "having a training objective" from "having the right training objective"，这是一个 elegant 的实验设计。

**S5**: Perturbation analysis 的 family-dependent 结论。论文没有 overclaim perturbation robustness，而是诚实地报告了 DD 上 zero degradation vs. ActorAttack 上 substantial degradation 的差异。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 156 · 2026-05-18T15:56:53.572928+00:00_

Reviewer 1 审稿意见已收到。核心发现：

- **评分**: 2.5/5（Soundness 2.5, Excitement 2.5）
- **3 个 critical issues**: 单模型生成全部数据的 confound (N1)、缺少已有 defense 直接对比 (N2)、数据规模不足 (N3)
- **4 个 major issues**: TF-IDF 冲击 (W1)、frozen encoder 设计 (W2)、LLM-as-judge 不公平 (W3)、标注质量 (W4)

等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 12

## Round 12

2 recorded events


### User

_source line 157 · 2026-05-18T15:56:56.143447+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交至 Review Director。

核心判断：**Overall 2.5/5**（介于 Findings 和 Resubmit next cycle 之间）。

三个 critical 问题：
1. **单模型 confound** — Qwen3-8B 同时生成训练数据、标注、测试数据和 paraphrase，TF-IDF 0.944 强烈暗示 stylistic artifacts 而非 discourse features
2. **缺失关键 baseline 对比** — 讨论了 DeepContext/BIID/G-Guard/SafeDream 但未直接比较，vanilla DeBERTa 不能 "represent" 这类方法
3. **数据规模不足** — 500 训练 + 76-118 测试对话，3 seeds，many claims（特别是 three-layer perturbation pattern）的统计功效严重不足

论文的主要优势在于 ablation 设计思路清晰（7 个 well-controlled variants）和诚实的 limitations 讨论。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 158 · 2026-05-18T15:57:03.502018+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 完成后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 13

## Round 13

6 recorded events


### User

_source line 159 · 2026-05-18T15:59:31.938507+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见（Round 1）

**论文**: What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap
**Venue**: EMNLP 2026 (ACL ARR May cycle)
**审查侧重**: 新颖性、Related Work 定位、写作质量、论文完整性

---

## 总体评分

**Overall**: 2.5/5（介于 Resubmit next cycle 和 Findings acceptance 之间）
**一句话总结**: 消融实验设计有系统性，但核心发现（domain-adaptive pretraining 提升 OOD 泛化）是已知结论在新领域的直接应用，TF-IDF 基线（F1=0.944）严重削弱了 discourse-level representation 的价值主张，且论文自称 "preliminary findings" 与 long paper 定位矛盾。

---

## ACL ARR 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.0/5 | 消融设计系统完整，但 TF-IDF 基线暴露了 lexical separability 问题，无法区分模型是否学到了 discourse-level features；统计检验不够完整 |
| **Excitement** | 2.0/5 | 核心机制（continued pretraining）已被 Gururangan et al. (2020) 充分建立；scrambled labels 发现有趣但不足以支撑 long paper |
| **Reproducibility** | 4.0/5 | 超参数和训练细节完整，承诺开源，计算成本合理（<4 GPU-hours） |
| **Reviewer Confidence** | 4/5 | 熟悉 domain-adaptive pretraining、adversarial robustness、safety alignment 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心贡献新颖性不足：Don't Stop Pretraining 的领域应用
- 具体位置：Section 4.2 (experiments.tex:101-107), Related Work domain-adaptive pretraining paragraph (related_work.tex:19)
- 问题：论文的核心发现——"continued pretraining on domain text bridges ~60 pp of the OOD gap"——本质上是 Gururangan et al. (2020) "Don't Stop Pretraining" 在 jailbreak detection 领域的直接验证。论文在 Related Work 中明确承认 "continued pretraining on domain text yields consistent gains across domains"（related_work.tex:19），但未充分论证自身超越该结论的增量在哪里。
- 为什么影响接收：ACL ARR Excitement 维度要求论文推进领域认知。将一个已确立的 NLP 通用结论应用到新任务，更适合 workshop paper 或 short paper，而非 EMNLP long paper。
- 建议：(1) 将 "difficulty threshold" 跨架构发现提升为主要贡献而非附属验证；(2) 深入分析 DeBERTa RTD 与 RoBERTa MLM 的表征差异导致不同泛化 threshold 的原因，而非仅报告现象；(3) 或者重新定位为 Findings paper。

**N2** [critical] TF-IDF 基线严重削弱 discourse-level representation 价值主张
- 具体位置：Table 1 (experiments.tex:42), Section 4.2 (experiments.tex:52), Limitations (conclusion.tex:15)
- 问题：TF-IDF LR 在 OOD DD 上达到 F1=0.944，而论文最佳模型为 0.997。论文诚实地承认了 lexical separability（conclusion.tex:15: "We cannot conclusively distinguish whether DisPeD's continued pretraining captures pragmatic discourse features or primarily exploits lexical cues"），但这直接动摇了论文的核心叙事——paper title 是 "What Makes Multi-Turn Jailbreaks Detectable"，answer 可能只是 "lexical cues"。
- 为什么影响接收：如果 bag-of-words 模型能达到 94.4%，那么 neural representation learning 的 marginal gain 仅为 5.3 pp。论文声称的 "discourse-level persuasion detection" 缺乏证据支撑。DisPeD 的优势被降格为 cross-seed stability 和 early detection，这些优势在 TF-IDF 缺少 per-prefix 评估的情况下无法完全比较。
- 建议：(1) 补充 TF-IDF 在所有 prefix length 上的结果（K=1,2,3,5）以公平比较 early detection；(2) 补充 probing experiments 证明 continued pretraining 确实编码了超越 lexical cues 的 discourse features；(3) 在 ActorAttack 上补充 TF-IDF 结果（当前缺失）。

**N3** [critical] "Preliminary findings" 定位与 long paper 格式矛盾
- 具体位置：Abstract (abstract.tex:4: "We present preliminary findings"), Introduction (introduction.tex:16: "Our contributions on this preliminary study"), Conclusion (conclusion.tex:6: "preliminary evidence")
- 问题：论文在三个关键位置使用 "preliminary" 限定。ACL ARR long paper 预期是完整、成熟的研究贡献。如果作者自己认为发现是 preliminary 的，审稿人没有理由给予更高评价。
- 为什么影响接收：自我降格的 framing 信号表明作者对贡献的充分性缺乏信心，这在 peer review 中是致命的。
- 建议：要么移除所有 "preliminary" 限定词并以完整研究贡献的姿态重新 frame（需要补充实验支撑），要么承认当前成果的范围并投稿为 Findings paper 或 short paper。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] Related Work 中不应包含自身实验结果
- 具体位置：related_work.tex:19 ("DisPeD's MLM control confirms that continued pretraining bridges ~60 pp"), related_work.tex:22 ("TF-IDF achieves F1 = 0.944 on our OOD evaluation")
- 问题：Related Work 的 "Domain-adaptive pretraining" 和 "Dataset artifacts" 段落中大量引用本文自身实验数据（F1 数值、pp 差距等）。Related Work 的功能是定位自身工作相对于已有文献的位置，不是预报 Results。
- 建议：移除 Related Work 中所有本文实验数据的具体引用，改为概念层面的对比（"We extend this finding to the multi-turn jailbreak domain with controlled ablations"）。

**W2** [major] Abstract 数据过载，叙事被数字淹没
- 具体位置：abstract.tex:5-8
- 问题：Abstract 共约 150 词，包含至少 12 个具体数值（0.31±0.03, 0.91±0.12, 0.981, 0.466, 0.93, 4-20×, p<0.001 等）。一个审稿人在 30 秒内无法从这些数字中提取核心价值。Abstract 读起来像 Results 的压缩版而非独立阅读单元。
- 建议：保留 2-3 个最关键的数字（例如 vanilla→MLM 的 ~60 pp gap, 和 cross-encoder 在 ActorAttack 上的坍塌），其余用定性描述替代。

**W3** [major] ActorAttack 样本量未说明
- 具体位置：experiments.tex:11
- 问题："OOD evaluation uses 80 FITD, 80 Deceptive Delight, and ActorAttack conversations" — FITD 和 DD 明确标注了 80 条，但 ActorAttack 的数量缺失。考虑到 ActorAttack 是论文的关键验证数据集（区分 "structurally simple" vs "structurally complex" 攻击），样本量对结果可信度至关重要。
- 建议：补充 ActorAttack 的具体样本数。

**W4** [major] Introduction 结果段过于冗长
- 具体位置：introduction.tex:14（整段约 200 词，包含 15+ 个数值）
- 问题：Introduction 第四段是一个密集的 results dump，包含两个架构、两个攻击族、多个 F1 值、CKA 分数等。这不是 Introduction 应有的写法——读者在此阶段尚未了解方法细节，无法消化这些数字。
- 建议：保留核心发现的定性总结（"domain exposure bridges the majority of the OOD gap; classification supervision provides stability"），将具体数字移至 Experiments。

**W5** [major] 缺少 Responsible NLP Research Checklist
- 具体位置：整篇论文
- 问题：ACL ARR 提交要求包含 Responsible NLP Research Checklist（与 Limitations section 不同）。论文中未发现此 checklist。
- 为什么影响评分：格式不合规可能导致 desk reject。
- 建议：按 ARR 要求填写完整 checklist。

**W6** [minor → major] 页数可能超限
- 具体位置：编译后 PDF 显示主体内容（含 Conclusion）延伸至第 9 页
- 问题：ACL long paper 限制为 8 页正文内容（Limitations 和 References 不计入）。Conclusion (Section 5) 与 Limitations (Section 6) 共享第 9 页。如果 Conclusion 的末尾超出了第 8 页底部，则正文内容超限。需要精确验证 Conclusion 结束的确切位置。
- 建议：(1) 精确检查 Conclusion 是否在第 8 页内结束；(2) 如有超限，压缩 Experiments 中的重复叙述（多处重复相同数字）。

**W7** [minor] Figure* 浮动位置异常
- 具体位置：Figure 3 (experiments.tex:247-252, `figure*` 环境)
- 问题：PDF 视觉检查显示 Figure 3 (strategy heatmap) 可能浮动到了主体之外的位置（接近 References 页面）。LaTeX `figure*` 在双栏格式中容易浮动失控。
- 建议：检查编译后 Figure 3 是否出现在 Section 5.5 附近；如果浮动过远，考虑使用 `[!ht]` 或 `\FloatBarrier`。

---

## 小问题（不影响接收）

- **重复数据**: 0.31±0.03 → 0.91±0.12 这组数字在 Abstract、Introduction、Related Work (×2)、Experiments、Conclusion 中出现了至少 6 次。
- **-ing phrases** (轻度): experiments.tex:63 "progressively confuse"、experiments.tex:103 "captures pragmatic features... that distinguish"——可接受但稍有 AI 生成痕迹。
- **Em-dash**: 正文无解释性 em-dash（仅 LaTeX 注释中有），合格。
- **术语一致性**: "domain exposure" / "domain adaptation" / "continued pretraining" / "domain-adaptive pretraining" 四个术语交替使用，指代同一概念。建议统一。
- **引用格式**: `austin1962speechacts` 年份 bib 中为 1962，OpenAlex 匹配到 1975（应为第二版/重印）。`chao2023pair` bib 年份 2023，实际发表于 2025。`han2024wildguard` 第一作者不匹配（bib=Han, API=Choi）。这些是小问题但审稿人可能注意到。

---

## 主要优势

**S1** 消融实验设计系统严谨。七个 Stage-1 变体各自隔离一个因素（domain exposure, classification supervision, label quality, label granularity, domain specificity），且共享相同的 Stage-2 pipeline，使对比公平。这种实验设计本身有方法论价值。

**S2** Scrambled labels 发现有洞察力。Scrambled、binary、9-class 三种分类变体在检测 F1 上完全相同（0.997±0.005），证明分类目标作为 representation regularizer 而非 semantic classifier 起作用。这是超越简单 domain adaptation 的新认知。

**S3** Cross-encoder "difficulty threshold" 概念有价值。DeBERTa RTD vs RoBERTa MLM 在不同攻击复杂度上表现出不同的泛化 threshold，提供了一个理解 encoder pretraining 与下游 adaptation 关系的框架。

**S4** 诚实的 Limitations section。论文坦诚承认 TF-IDF 基线问题、strategy prediction 不泛化、数据规模限制等——这种自我批评的诚实在 ML safety 论文中难能可贵。

**S5** 可复现性优秀。完整的超参数、训练时间（<4 GPU-hours 全部变体）、承诺开源。

---

## Questions（需作者澄清）

**Q1** TF-IDF 在 ActorAttack 上的 F1 是多少？如果 TF-IDF 在 ActorAttack 上也表现良好，则 discourse-level representation 的必要性进一步被削弱；如果 TF-IDF 在 ActorAttack 上坍塌，则反而支持了论文的 claim。这是判断贡献大小的关键数据点。

**Q2** Mean pooling 匹配 BiGRU (F1=1.000) 的单 seed 结果是否在 ActorAttack 上也成立？如果 mean pooling 在简单和复杂攻击上都匹配 BiGRU，则 temporal modeling 完全不必要——这会进一步支持论文的 per-turn detection 解释，但也意味着 BiGRU 是不必要的架构复杂度。

**Q3** 论文声称 "continued training on jailbreak conversation text captures pragmatic features (hedging, escalation markers, topic-shifting patterns)"（experiments.tex:103）。是否有直接证据？Probing classifiers 可以验证这一假设，但论文明确将其留给 future work。如果没有 probing 证据，这一 claim 不应出现。

**Q4** ActorAttack 的 OOD evaluation 使用了多少条对话？experiments.tex:11 只写了 "ActorAttack conversations" 未标数量。

**Q5** Topic classification 变体使用了什么具体标签？experiments.tex 提到 5-class (technology, health, finance, education, general)，但这些 topic 类别与 benign conversations 的生成 prompt 完全一致（appendix.tex:139）。这意味着 topic classification 可能直接学习了区分 jailbreak vs benign 的 shortcut（jailbreak 对话不属于这五个 topic），而非 topic 分类失败导致表征退化。

---

## Missing References

1. **Circuit Breakers** (Zou et al., 2024) — representation-engineering defense，与 Bullwinkel et al. (2025) 直接相关，应在 "Multi-turn defenses" 或 "Production safety" 中讨论。
2. **SmoothLLM** (Robey et al., 2024) — perturbation-based defense，与论文的 adversarial paraphrasing 分析直接相关。
3. **GradSafe** (Xie et al., 2024) — gradient-based jailbreak detection，另一种检测范式。
4. **TAP** (Mehrotra et al., 2024) — tree of attacks with pruning，作为多轮攻击的自动化变体应在 attacks 部分提及。
5. **Persuasion for Good** (Wang et al., 2019) — 早期 computational persuasion 数据集，对 persuasion taxonomy 的理论基础有补充价值。
6. **Rainbow Teaming** (Samvelyan et al., 2024) — 多样化 red-teaming 方法，与 cross-attack generalization 评估直接相关。

---

## Overall Assessment

**Overall: 2.5/5 (介于 Resubmit next cycle 和 Findings acceptance)**
**Confidence: 4/5**

这篇论文的实验设计（七变体消融）和诚实的自我批评是优点，但三个核心问题阻碍接收：(1) 主要发现是已知结论在新领域的应用，novelty 有限；(2) TF-IDF 基线暴露了 lexical separability，削弱了 discourse-level representation 的核心叙事；(3) "preliminary findings" 定位与 long paper 格式矛盾。如果作者能补充 probing experiments 证明 discourse-level features、移除 preliminary 限定、并以 "difficulty threshold across encoder architectures" 为主线重新 frame，可能达到 Findings acceptance 水准。当前版本更适合作为 workshop paper 或 Findings short paper。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-18T16:00:02.762939+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W7)、Strength (S1-S5)、Question (Q1-Q5) 和 Missing Reference，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见（Round 1）\n\n**审查侧重**: 新颖性、Related Work 定位、写作质量、论文完整性\n\n## 总体评分: 2.5/5\n\n## Must-Fix 问题\n\n**N1** [critical] 核心贡献新颖性不足：Don't Stop Pretraining 的领域应用\n- 论文核心发现（continued pretraining bridges ~60 pp OOD gap）本质上是 Gururangan et al. (2020) 在 jailbreak detection 领域的直接验证。论文在 Related Work 中承认 \"continued pretraining on domain text yields consistent gains across domains\"，但未充分论证超越该结论的增量。\n- ACL ARR Excitement 维度要求推进领域认知，将已确立的 NLP 通用结论应用到新任务更适合 workshop paper。\n\n**N2** [critical] TF-IDF 基线严重削弱 discourse-level representation 价值主张\n- TF-IDF LR 在 OOD DD 上达到 F1=0.944，论文最佳 0.997。论文承认 \"We cannot conclusively distinguish whether DisPeD's continued pretraining captures pragmatic discourse features or primarily exploits lexical cues\"。paper title 是 \"What Makes Multi-Turn Jailbreaks Detectable\"，answer 可能只是 \"lexical cues\"。\n- Neural representation learning 的 marginal gain 仅为 5.3 pp。DisPeD 优势降格为 cross-seed stability 和 early detection，但 TF-IDF 缺少 per-prefix 评估。\n\n**N3** [critical] \"Preliminary findings\" 定位与 long paper 格式矛盾\n- Abstract、Introduction、Conclusion 三处使用 \"preliminary\"。如果作者自己认为发现是 preliminary，审稿人没有理由给予更高评价。自我降格的 framing 在 peer review 中致命。\n\n## Should-Fix 问题\n\n**W1** [major] Related Work 中不应包含自身实验结果\n- \"Domain-adaptive pretraining\" 和 \"Dataset artifacts\" 段落中大量引用本文自身 F1 数值。Related Work 功能是定位自身工作相对于已有文献的位置，不是预报 Results。\n\n**W2** [major] Abstract 数据过载\n- 约 150 词包含至少 12 个数值。审稿人 30 秒内无法提取核心价值。\n\n**W3** [major] ActorAttack 样本量未说明\n- FITD 和 DD 标注了 80 条，但 ActorAttack 数量缺失。\n\n**W4** [major] Introduction 结果段过于冗长\n- 第四段约 200 词包含 15+ 数值，读者尚未了解方法细节无法消化。\n\n**W5** [major] 缺少 Responsible NLP Research Checklist\n- ACL ARR 要求包含此 checklist，可能导致 desk reject。\n\n**W6** [minor → major] 页数可能超限\n- 需验证 Conclusion 是否在第 8 页内结束。\n\n**W7** [minor] Figure* 浮动位置异常\n- Figure 3 可能浮动到 References 页面。\n\n## Strengths\n\n**S1** 消融实验设计系统严谨\n**S2** Scrambled labels 发现有洞察力\n**S3** Cross-encoder \"difficulty threshold\" 概念有价值\n**S4** 诚实的 Limitations section\n**S5** 可复现性优秀\n\n## Questions\n\n**Q1** TF-IDF 在 ActorAttack 上的 F1？\n**Q2** Mean pooling 在 ActorAttack 上是否也匹配 BiGRU？\n**Q3** \"pragmatic features (hedging, escalation markers, topic-shifting patterns)\" 有直接证据吗？\n**Q4** ActorAttack OOD evaluation 使用了多少条对话？\n**Q5** Topic classification 的 5-class 与 benign 生成 prompt 的 topic 完全一致——是否学习了 jailbreak vs benign shortcut 而非 topic 分类失败？\n\n## Missing References\nCircuit Breakers (Zou et al., 2024), SmoothLLM (Robey et al., 2024), GradSafe (Xie et al., 2024), TAP (Mehrotra et al., 2024), Persuasion for Good (Wang et al., 2019), Rainbow Teaming (Samvelyan et al., 2024)\n\n---\n\n请对以上每个条目逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W7)、Strength (S1-S5)、Question (Q1-Q5) 和 Missing Reference，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见（Round 1）\n\n**审查侧重**: 新颖性、Related Work 定位、写作质量、论文完整性\n\n## 总体评分: 2.5/5\n\n## Must-Fix 问题\n\n**N1** [critical] 核心贡献新颖性不足：Don't Stop Pretraining 的领域应用\n- 论文核心发现（continued pretraining bridges ~60 pp OOD gap）本质上是 Gururangan et al. (2020) 在 jailbreak detection 领域的直接验证。论文在 Related Work 中承认 \"continued pretraining on domain text yields consistent gains across domains\"，但未充分论证超越该结论的增量。\n- ACL ARR Excitement 维度要求推进领域认知，将已确立的 NLP 通用结论应用到新任务更适合 workshop paper。\n\n**N2** [critical] TF-IDF 基线严重削弱 discourse-level representation 价值主张\n- TF-IDF LR 在 OOD DD 上达到 F1=0.944，论文最佳 0.997。论文承认 \"We cannot conclusively distinguish whether DisPeD's continued pretraining captures pragmatic discourse features or primarily exploits lexical cues\"。paper title 是 \"What Makes Multi-Turn Jailbreaks Detectable\"，answer 可能只是 \"lexical cues\"。\n- Neural representation learning 的 marginal gain 仅为 5.3 pp。DisPeD 优势降格为 cross-seed stability 和 early detection，但 TF-IDF 缺少 per-prefix 评估。\n\n**N3** [critical] \"Preliminary findings\" 定位与 long paper 格式矛盾\n- Abstract、Introduction、Conclusion 三处使用 \"preliminary\"。如果作者自己认为发现是 preliminary，审稿人没有理由给予更高评价。自我降格的 framing 在 peer review 中致命。\n\n## Should-Fix 问题\n\n**W1** [major] Related Work 中不应包含自身实验结果\n- \"Domain-adaptive pretraining\" 和 \"Dataset artifacts\" 段落中大量引用本文自身 F1 数值。Related Work 功能是定位自身工作相对于已有文献的位置，不是预报 Results。\n\n**W2** [major] Abstract 数据过载\n- 约 150 词包含至少 12 个数值。审稿人 30 秒内无法提取核心价值。\n\n**W3** [major] ActorAttack 样本量未说明\n- FITD 和 DD 标注了 80 条，但 ActorAttack 数量缺失。\n\n**W4** [major] Introduction 结果段过于冗长\n- 第四段约 200 词包含 15+ 数值，读者尚未了解方法细节无法消化。\n\n**W5** [major] 缺少 Responsible NLP Research Checklist\n- ACL ARR 要求包含此 checklist，可能导致 desk reject。\n\n**W6** [minor → major] 页数可能超限\n- 需验证 Conclusion 是否在第 8 页内结束。\n\n**W7** [minor] Figure* 浮动位置异常\n- Figure 3 可能浮动到 References 页面。\n\n## Strengths\n\n**S1** 消融实验设计系统严谨\n**S2** Scrambled labels 发现有洞察力\n**S3** Cross-encoder \"difficulty threshold\" 概念有价值\n**S4** 诚实的 Limitations section\n**S5** 可复现性优秀\n\n## Questions\n\n**Q1** TF-IDF 在 ActorAttack 上的 F1？\n**Q2** Mean pooling 在 ActorAttack 上是否也匹配 BiGRU？\n**Q3** \"pragmatic features (hedging, escalation markers, topic-shifting patterns)\" 有直接证据吗？\n**Q4** ActorAttack OOD evaluation 使用了多少条对话？\n**Q5** Topic classification 的 5-class 与 benign 生成 prompt 的 topic 完全一致——是否学习了 jailbreak vs benign shortcut 而非 topic 分类失败？\n\n## Missing References\nCircuit Breakers (Zou et al., 2024), SmoothLLM (Robey et al., 2024), GradSafe (Xie et al., 2024), TAP (Mehrotra et al., 2024), Persuasion for Good (Wang et al., 2019), Rainbow Teaming (Samvelyan et al., 2024)\n\n---\n\n请对以上每个条目逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-18T16:00:37.900738+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 35137
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-18T16:00:38.102078+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W5)、Strength (S1-S5)、Question (Q1-Q5) 和 Missing Reference，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见（Round 1）\n\n**审查侧重**: 方法严谨性、实验设计、统计有效性\n\n## 总体评分: 2.5/5\n\n## Must-Fix 问题\n\n**N1** [critical] 单模型生成全部数据造成系统性 confound\n- Qwen3-8B 同时用于生成训练数据（Crescendo + benign）、策略标注（9-class labels）、OOD 测试数据（DD, FITD）、对抗性 paraphrase。所有数据共享同一 LLM 的文本分布特征。TF-IDF LR 在 OOD DD 上达到 0.944，强烈暗示 stylistic artifacts 而非 discourse-level 特征。\n- 如果 OOD gap 的桥接主要来自学习 Qwen3-8B 的 stylistic fingerprint，则整个 evidence hierarchy 可能是 artifact-driven。\n- 建议：(1) 用不同 LLM 生成部分 OOD 数据；(2) 用人类编写数据（MHJ dataset）做评估；(3) 做 probing 实验区分 lexical 和 discourse-level 特征。\n\n**N2** [critical] 缺少与现有 multi-turn defense 系统的直接对比\n- 讨论了 DeepContext/BIID/G-Guard/SafeDream 但未直接实验对比。vanilla DeBERTa（frozen, 1-layer BiGRU, hidden=128）与 DeepContext（fine-tuned BERT, 3-layer GRU, hidden=2048）完全不同。\n- 建议：复现 DeepContext 作为 baseline，或在共同 benchmark 上比较，或明确 claim 论文贡献是分析框架而非 SOTA 方法。\n\n**N3** [critical] 数据规模严重不足以支撑 statistical claims\n- 训练 500 对话、IID 测试 76、OOD 80-118。Table 3 three-layer pattern 基于 n=76, discordant pairs ≤7。FITD 无 discriminative power。MLM-only DD-Full std=0.115（seed 456 recall=0.64），3 seeds 不足以可靠估计 mean performance。\n- Evidence hierarchy 中多对之间 confidence intervals 重叠。\"Classification supervision adds ~8pp over MLM\" 在更多 seeds 下可能不成立。\n- 建议：至少 5 seeds，bootstrap 95% CI，paired bootstrap 或 permutation test。\n\n## Should-Fix 问题\n\n**W1** [major] TF-IDF baseline 对核心叙事的冲击未充分 address\n- TF-IDF 在 OOD DD 达 0.944，但未报告 K<Full 和 ActorAttack 结果。如果 TF-IDF 在 K=2 也表现良好，early detection 优势可能不成立。\n\n**W2** [major] BiGRU + frozen encoder 设计缺乏 justification\n- freeze 可能低估某些 variants 潜力。Mean pooling single-seed F1=1.000 与 3-seed BiGRU 不可比。\n\n**W3** [major] LLM-as-judge baseline 不公平\n- 仅 zero-shot，30-47% unparseable。未测 few-shot/CoT。prompt 设计可能有问题。\n\n**W4** [major] 策略标注质量验证不足\n- κ=0.78 基于 n=50 single annotator。9-class 每类平均 ~5.5 samples 太小。\n\n**W5** [minor] α=0.3 loss weight 未 justify\n\n## Strengths\n\n**S1** ablation 设计思路优秀\n**S2** 诚实的 limitations 讨论\n**S3** Cross-encoder validation 有价值\n**S4** Topic classification 作为 negative control 优雅\n**S5** Perturbation analysis 的 family-dependent 结论诚实\n\n## Questions\n\n**Q1** OOD test data 是否也由 Qwen3-8B 生成？如果是，\"cross-attack generalization\" 实为 \"cross-template generalization within same LLM distribution\"。\n\n**Q2** scrambled labels = 9-class = 0.997 的替代解释：在小数据集上任何分类 head 的 gradient signal 都可能足够，不需要 \"regularizer\" 解释。\n\n**Q3** FITD Table 6 中缺少 K=3, K=5 结果？\n\n**Q4** ActorAttack perturbation 中 9-class Δ=-20.4±13.5pp（seed variance 极大），现有结论是否可靠？\n\n**Q5** DeBERTa-v3 vs RoBERTa 的参数量和训练数据也不同，如何排除 model capacity confound？\n\n## Missing References\nMHJ dataset (Li et al., 2024), JailbreakBench (Chao et al., 2024), HarmBench (Mazeika et al., 2024), Latent Jailbreak (Qiu et al., 2023), AutoDAN (Liu et al., 2024)\n\n---\n\n请对以上每个条目逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W5)、Strength (S1-S5)、Question (Q1-Q5) 和 Missing Reference，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见（Round 1）\n\n**审查侧重**: 方法严谨性、实验设计、统计有效性\n\n## 总体评分: 2.5/5\n\n## Must-Fix 问题\n\n**N1** [critical] 单模型生成全部数据造成系统性 confound\n- Qwen3-8B 同时用于生成训练数据（Crescendo + benign）、策略标注（9-class labels）、OOD 测试数据（DD, FITD）、对抗性 paraphrase。所有数据共享同一 LLM 的文本分布特征。TF-IDF LR 在 OOD DD 上达到 0.944，强烈暗示 stylistic artifacts 而非 discourse-level 特征。\n- 如果 OOD gap 的桥接主要来自学习 Qwen3-8B 的 stylistic fingerprint，则整个 evidence hierarchy 可能是 artifact-driven。\n- 建议：(1) 用不同 LLM 生成部分 OOD 数据；(2) 用人类编写数据（MHJ dataset）做评估；(3) 做 probing 实验区分 lexical 和 discourse-level 特征。\n\n**N2** [critical] 缺少与现有 multi-turn defense 系统的直接对比\n- 讨论了 DeepContext/BIID/G-Guard/SafeDream 但未直接实验对比。vanilla DeBERTa（frozen, 1-layer BiGRU, hidden=128）与 DeepContext（fine-tuned BERT, 3-layer GRU, hidden=2048）完全不同。\n- 建议：复现 DeepContext 作为 baseline，或在共同 benchmark 上比较，或明确 claim 论文贡献是分析框架而非 SOTA 方法。\n\n**N3** [critical] 数据规模严重不足以支撑 statistical claims\n- 训练 500 对话、IID 测试 76、OOD 80-118。Table 3 three-layer pattern 基于 n=76, discordant pairs ≤7。FITD 无 discriminative power。MLM-only DD-Full std=0.115（seed 456 recall=0.64），3 seeds 不足以可靠估计 mean performance。\n- Evidence hierarchy 中多对之间 confidence intervals 重叠。\"Classification supervision adds ~8pp over MLM\" 在更多 seeds 下可能不成立。\n- 建议：至少 5 seeds，bootstrap 95% CI，paired bootstrap 或 permutation test。\n\n## Should-Fix 问题\n\n**W1** [major] TF-IDF baseline 对核心叙事的冲击未充分 address\n- TF-IDF 在 OOD DD 达 0.944，但未报告 K<Full 和 ActorAttack 结果。如果 TF-IDF 在 K=2 也表现良好，early detection 优势可能不成立。\n\n**W2** [major] BiGRU + frozen encoder 设计缺乏 justification\n- freeze 可能低估某些 variants 潜力。Mean pooling single-seed F1=1.000 与 3-seed BiGRU 不可比。\n\n**W3** [major] LLM-as-judge baseline 不公平\n- 仅 zero-shot，30-47% unparseable。未测 few-shot/CoT。prompt 设计可能有问题。\n\n**W4** [major] 策略标注质量验证不足\n- κ=0.78 基于 n=50 single annotator。9-class 每类平均 ~5.5 samples 太小。\n\n**W5** [minor] α=0.3 loss weight 未 justify\n\n## Strengths\n\n**S1** ablation 设计思路优秀\n**S2** 诚实的 limitations 讨论\n**S3** Cross-encoder validation 有价值\n**S4** Topic classification 作为 negative control 优雅\n**S5** Perturbation analysis 的 family-dependent 结论诚实\n\n## Questions\n\n**Q1** OOD test data 是否也由 Qwen3-8B 生成？如果是，\"cross-attack generalization\" 实为 \"cross-template generalization within same LLM distribution\"。\n\n**Q2** scrambled labels = 9-class = 0.997 的替代解释：在小数据集上任何分类 head 的 gradient signal 都可能足够，不需要 \"regularizer\" 解释。\n\n**Q3** FITD Table 6 中缺少 K=3, K=5 结果？\n\n**Q4** ActorAttack perturbation 中 9-class Δ=-20.4±13.5pp（seed variance 极大），现有结论是否可靠？\n\n**Q5** DeBERTa-v3 vs RoBERTa 的参数量和训练数据也不同，如何排除 model capacity confound？\n\n## Missing References\nMHJ dataset (Li et al., 2024), JailbreakBench (Chao et al., 2024), HarmBench (Mazeika et al., 2024), Latent Jailbreak (Qiu et al., 2023), AutoDAN (Liu et al., 2024)\n\n---\n\n请对以上每个条目逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-18T16:00:39.510768+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1408
}
```

</details>

---


### Assistant

_source line 164 · 2026-05-18T16:00:42.312906+00:00_

交叉分享已分发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 14

## Round 14

2 recorded events


### User

_source line 165 · 2026-05-18T16:00:44.883726+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**Overall 2.5/5**。

三个 critical 问题：
1. **新颖性不足** — 核心发现是 Don't Stop Pretraining (Gururangan et al., 2020) 在 jailbreak detection 上的直接应用，增量有限
2. **TF-IDF 基线（F1=0.944）** 严重削弱了 discourse-level representation 的价值主张，论文自己也承认无法区分模型学到的是 pragmatic features 还是 lexical cues
3. **"Preliminary findings" 定位** 在 Abstract/Introduction/Conclusion 中出现三次，与 EMNLP long paper 的成熟贡献预期矛盾

主要优势是消融设计的系统性（七变体各隔离一个因素）、scrambled labels 的 regularizer 洞察、以及诚实的 Limitations section。

建议重新定位为 Findings paper，或补充 probing experiments 后以 cross-encoder difficulty threshold 为主线重新 frame。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 166 · 2026-05-18T16:00:50.002520+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 15

## Round 15

2 recorded events


### User

_source line 167 · 2026-05-18T16:02:41.427001+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 (Round 1) 的逐条回应

---

### Must-Fix 问题

**[AGREE with nuance] R2-N1: 核心贡献新颖性 — Don't Stop Pretraining 的领域应用**

R2 的批评方向正确，但过于简化。论文的贡献不仅是 "DAPT applied to jailbreak detection"，还包括：(1) scrambled labels = binary = 9-class 的 regularizer 发现（Section 4.3, Table 2），(2) cross-encoder "difficulty threshold" 概念（Section 4.5, Table 3），(3) topic classification 作为 negative control 的 misaligned supervision 发现（Section 4.3）。这些超越了 Gururangan et al. (2020) 的简单领域验证。

但 R2 的核心观点仍然成立：论文的 **headline result**（~60pp OOD gap bridging by MLM）确实是 DAPT 的直接推论，在 500 条合成对话的小规模上验证。更精细的 decomposition 发现（scrambled labels, difficulty threshold）虽然有趣，但统计支撑不足（3 seeds, n=76-118）。作为 long paper 的核心贡献，novelty 确实偏弱。如果 novelty claim 重新聚焦在 "difficulty threshold across encoders" 和 "regularizer interpretation of classification supervision" 上（而非 DAPT 验证本身），论文的 positioning 会更强。

**[AGREE] R2-N2: TF-IDF 削弱 discourse-level representation 价值主张**

完全同意。这与我 R1 审稿意见中的 N1（单模型 confound）和 W1（TF-IDF 冲击）高度一致。论文自己在 Section 5 (Limitations, "Lexical separability" paragraph) 承认 "We cannot conclusively distinguish whether DisPeD's continued pretraining captures pragmatic discourse features or primarily exploits lexical cues"。Section 4.3 (line 103) 声称 MLM "captures pragmatic features (hedging, escalation markers, topic-shifting patterns)"，但没有任何 probing 证据支撑这一 claim。唯一的线性探测（Section 4.5, line 185-186）测试的是 turn position / escalation phase / persuasion presence，改进仅 1-5pp，且无法区分 lexical 和 discourse-level 特征。

补充 R2 的论点：TF-IDF 在 Table 1 中的 K=2 列标为 "--"，即**未报告 per-prefix 结果**。如果 TF-IDF 在 K=2 也表现良好，则 DisPeD 声称的 "early detection advantage" 也可能不成立。此外，TF-IDF 在 ActorAttack 上的结果也未报告（我在 R1-Q1 和 R1-W1 中也提到了这一遗漏）。

**[AGREE with important nuance] R2-N3: "Preliminary findings" 与 long paper 格式矛盾**

R2 的策略性建议是对的：在 peer review 中，self-hedging 确实会被 weaponized。论文在 Abstract (line 2: "preliminary findings")、Introduction (line 16: "preliminary study")、Conclusion (line 6: "preliminary evidence") 三处使用 "preliminary"。

但我认为需要区分两种情况：
1. 如果作者 **去掉 "preliminary" 但不改变实验规模**，论文反而会更容易被批评为 overclaiming（500 条合成数据、3 seeds、n=76 perturbation test 确实无法支撑 definitive claims）。
2. 正确的修复是 **同时移除 "preliminary" hedging 和扩大实验规模**。仅做文字修改而不加强证据，会使论文更脆弱。

所以 R2 发现了一个真问题，但建议方向需要 clarify：问题不是 "不该用 preliminary"，而是 "如果规模不够支撑 definitive claims，则 long paper 投稿本身需要重新考虑"。这更接近 R2 原意中 "更适合 workshop paper" 的判断。

---

### Should-Fix 问题

**[AGREE] R2-W1: Related Work 不应包含自身实验结果**

验证了原文。至少三处 Related Work 段落包含本文数值：
- "Domain-adaptive pretraining" 段 (related_work.tex line 19): "DisPeD's MLM control confirms that continued pretraining bridges ~60pp of the OOD gap" 以及 RoBERTa F1 数值
- "Dataset artifacts" 段 (line 22): "TF-IDF achieves F1 = 0.944 on our OOD evaluation"
- "Production safety systems" 段 (line 13): "GPT-5.5 achieves F1 = 0.191-0.449"

这些内容属于 Results/Discussion，不属于 Related Work。Related Work 的功能是 positioning（定位自身工作相对于已有文献），不是 preview results。将这些数值移到 Experiments/Discussion 即可修复。

**[AGREE] R2-W2: Abstract 数据过载**

统计 Abstract 中的独立数值：60pp, 0.31±0.03, 0.91±0.12, 0.981, 0.466, 0.93, 4-20×, p<0.001。共 8-10 个数值点在约 150 词中出现。R2 说 12 个可能计入了 F1 标注等，数量级一致。核心问题是：审稿人 30 秒内无法从 Abstract 提取论文的核心洞察。Abstract 应该讲 story（什么问题、什么洞察、什么机制），数字是支撑而非主体。

**[AGREE] R2-W3: ActorAttack 样本量未说明**

Section 4.1 (experiments.tex line 11) 原文："OOD evaluation uses 80 FITD, 80 Deceptive Delight (DD), and ActorAttack conversations"。FITD 和 DD 标注了 80 条，ActorAttack 数量确实缺失。这是一个基础的 reporting gap，必须修复。（我在 R1-Q4 中也问了同一问题。）

**[AGREE] R2-W4: Introduction 结果段过于冗长**

Introduction 第 4 段（introduction.tex line 14）约 200 词，包含 15+ 数值（0.31±0.03, 0.91±0.12, 60pp, 0.97, K≤5, 0.997±0.005, 0.981, 0.466±0.163, 0.93, RTD, MLM, 0.005-0.046 等）。读者此时尚未看到 Method 和 Experiment 细节，无法消化这些数字。应压缩为 2-3 个 headline numbers + 核心 takeaway，将细节留给 Experiments。

**[AGREE — elevated to critical] R2-W5: 缺少 Responsible NLP Research Checklist**

确认 main.tex 和 appendix.tex 中均未包含 ACL ARR 要求的 Responsible NLP Research Checklist。这不仅仅是 minor formatting issue。ACL ARR 明确要求此 checklist，缺失可能导致 desk reject。鉴于论文涉及 jailbreak attack 和 adversarial techniques，ethical considerations checklist 尤为重要。我将此问题的 severity 从 R2 的 "major" 提升为 **critical**，因为 desk reject 风险直接影响接收可能性。

**[AGREE with caveat] R2-W6: 页数可能超限**

无法在不编译 PDF 的情况下验证。但鉴于内容密度（7 个 variants × 4 attack families × multiple prefix lengths + perturbation analysis + cross-encoder + strategy analysis + CKA + linear probing），在 8 页正文 + unlimited references 的限制下确实紧张。Limitations section 不计页数（ACL 2026 规则），但 Conclusion 必须在第 8 页内结束。建议作者确认编译后页数。

**[AGREE] R2-W7: Figure* 浮动位置异常**

Figure 3 (fig3_strategy_heatmap) 使用 `figure*` 环境（experiments.tex line 247），full-width figure 在两栏排版中容易浮动到非预期位置。这是 LaTeX 常见问题，用 `[t!]` 或 `\afterpage` 可修复。Minor issue。

---

### Strengths

**[AGREE] R2-S1: 消融实验设计系统严谨**
与我 R1-S1 一致。7 个变体的设计是论文最有价值的贡献。

**[AGREE] R2-S2: Scrambled labels 发现有洞察力**
与我 R1-S1 一致。Scrambled = binary = 9-class 的 convergence（Table 2, Section 4.3）是一个 elegant finding。

**[AGREE] R2-S3: Cross-encoder "difficulty threshold" 概念**
与我 R1-S3 一致。DeBERTa vs. RoBERTa 在 DD vs. ActorAttack 上的差异模式（Table 3, Section 4.5）提供了有实践意义的洞察。

**[AGREE] R2-S4: 诚实的 Limitations section**
与我 R1-S2 一致。Section 5 覆盖了 7 个具体 limitation，坦率程度在同类论文中罕见。

**[AGREE] R2-S5: 可复现性优秀**
Appendix E 的超参数、训练流程细节比较完整，总计算成本 < 4 GPU-hours（Section 5, "Computation cost"）。但我在 R1 review 中指出生成 prompt 和标注 prompt 未在论文中披露（仅承诺 release upon acceptance），这使得 reproducibility 不完全。

---

### Questions

**[AGREE] R2-Q1: TF-IDF 在 ActorAttack 上的 F1？**
与我 R1-W1 一致。未报告，且这是评估 TF-IDF 对核心 claim 冲击的关键缺失数据。

**[AGREE] R2-Q2: Mean pooling 在 ActorAttack 上是否也匹配 BiGRU？**
与我 R1-W2 观点一致（mean pooling single-seed 不可靠）。论文在 Section 4.3 (line 135-137) 自己标注了 "single seed on a single OOD attack type"。在 ActorAttack 这样更难的 benchmark 上，mean pooling 是否仍匹配 BiGRU 是一个关键的未回答问题。

**[AGREE] R2-Q3: "pragmatic features" 缺乏直接证据**
与我对 R2-N2 的分析一致。Section 4.3 line 103 声称 "captures pragmatic features (hedging, escalation markers, topic-shifting patterns)" 但无 probing 证据。Section 4.5 line 185-186 的线性探测改进仅 1-5pp，且测试的维度（turn position, escalation phase, persuasion presence）不直接对应 hedging 或 topic-shifting。

**[AGREE] R2-Q4: ActorAttack 样本量？**
与 W3 重复。Section 4.1 确实未标注 ActorAttack 数量。

**[AGREE — important confound] R2-Q5: Topic classification 的 5-class 与 benign 生成 topic 一致**

这是一个非常 insightful 的观察，我在 R1 审稿中未发现这个 confound。

验证事实：
- method.tex line 50: "The topic variant trains a 5-class topic classifier (technology, health, finance, education, general) on the same conversations"
- appendix.tex line 139 (Reproducibility Details): "Benign conversations are generated with topic-anchored prompts across five domains (technology, health, finance, education, general)"

两个 category set 完全一致。这意味着 topic labels 与 benign/jailbreak status 存在 systematic correlation：benign conversations 有清晰的 topic label，而 jailbreak conversations 的 topic 分布不同。Topic classifier 可能学到了 "某些 topic 分布 = benign"的 shortcut，而非论文声称的 "misaligned supervision forces encoder to allocate capacity to irrelevant discriminative features"（Section 4.3, line 118）。

这个 confound 改变了 topic classification 结果的解释：OOD 性能差（0.541±0.207）可能不是因为 "misaligned objective destabilizes representations"，而是因为 OOD 数据的 topic-benign correlation 与训练数据不同。如果真是 shortcut learning，则 "separates the effect of 'having a training objective' from 'having the right training objective'" 这个 claim（Section 4.3, line 119）不成立。

**建议修复：用与 jailbreak domains 正交的 topic categories 重新训练 topic variant，或者在 jailbreak 和 benign conversations 上都使用相同 topic 分布。**

---

### Missing References

**[PARTIALLY AGREE]**

按相关性排序：
- **Persuasion for Good (Wang et al., 2019)**: [AGREE] 直接相关。这是 dialogue 中 persuasion detection 的重要先驱工作，论文的 persuasion taxonomy (Section 3.2) 应该 cite 并 compare。论文 cite 了 propaganda analysis (Da San Martino et al., 2019/2020) 作为类比，但遗漏了 dialogue persuasion 方向，这是更直接的对照。
- **SmoothLLM (Robey et al., 2024)**: [AGREE] 与 perturbation analysis (Section 4.4) 直接相关。SmoothLLM 本身就是基于 perturbation 的防御方法，论文做了 perturbation robustness 分析却未 cite。
- **TAP (Mehrotra et al., 2024)**: [AGREE] 作为另一个 iterative/multi-turn attack method，应在 Related Work "Multi-turn jailbreak attacks" 段落中提及。论文 cite 了 PAIR 但遗漏了 TAP。
- **Circuit Breakers (Zou et al., 2024)**: [PARTIALLY AGREE] 相关但不直接。这是 representation engineering 方向的防御，与 DisPeD 的 encoder adaptation 有概念联系，但方法论不同。
- **GradSafe (Xie et al., 2024)**: [PARTIALLY AGREE] gradient-based safety 方向，与 DisPeD 方法不同，但应在 production safety systems 段落中 acknowledged。
- **Rainbow Teaming (Samvelyan et al., 2024)**: [MINOR] 多样化 adversarial prompt 生成，相关性较弱。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 168 · 2026-05-18T16:02:51.766730+00:00_

收到 Reviewer 1 对 Reviewer 2 的交叉回应。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 16

## Round 16

6 recorded events


### User

_source line 169 · 2026-05-18T16:02:52.874997+00:00_

[Reviewer 1 审稿结果]:
已提交对 R2 的逐条交叉回应。

核心判断：R2 的 3 个 Must-Fix 中，N1（novelty）和 N2（TF-IDF 冲击）我基本同意，N3（preliminary framing）同意但认为根源是实验规模而非措辞。Should-Fix 中全部同意，且将 W5（缺 Responsible NLP Checklist）升级为 critical。特别值得注意的是 R2-Q5 发现了一个我遗漏的重要 confound：topic classification 的 5-class categories 与 benign 数据生成的 topic 完全一致，可能存在 shortcut learning 而非论文声称的 "misaligned supervision"。

---

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 的逐条回应

---

## Must-Fix 问题

**[AGREE] R1-N1: 单模型生成全部数据造成系统性 confound**

同意这是 critical 问题，且我认为 R1 的分析比我的 N2（TF-IDF 基线）更精准地定位了问题根源。

证据补充：experiments.tex:10-12 确认训练数据（Crescendo + benign）由 Qwen3-8B 生成，但未明确说明 OOD 数据（DD、FITD、ActorAttack）是否也由同一模型生成。如果 OOD 数据也是 Qwen3-8B 生成的，TF-IDF 在 OOD DD 上 F1=0.944（Table 1）就有了完美解释：TF-IDF 捕获的不是 cross-attack discourse features，而是 Qwen3-8B 的 stylistic fingerprint。这一点论文在 Limitations 中完全没有提及（conclusion.tex:12-15 讨论了 lexical separability 但未讨论 single-LLM confound）。

额外观察：appendix.tex:139 写道 benign conversations 用 "topic-anchored prompts across five domains (technology, health, finance, education, general)"，method.tex:50 的 Topic classification 变体也使用这五个类别。如果 jailbreak 对话不属于这五个 topic，topic classifier 可能通过 shortcut 学习区分 jailbreak vs benign，而非 R1 和论文所说的 "misaligned supervision destabilizes representations"。这进一步支持 artifact-driven 的解释。

---

**[AGREE] R1-N2: 缺少与现有 multi-turn defense 系统的直接对比**

同意，但对 severity 有微调。

论文在 related_work.tex:10 中承认 "DisPeD's vanilla baseline... is not a direct proxy for DeepContext, which differs in encoder fine-tuning, model capacity, and loss function"，这是诚实的声明。但问题是论文同时在 Introduction (introduction.tex:8) 和 Related Work 中暗示 DisPeD 优于这些系统（"These systems achieve reasonable in-distribution performance but are evaluated on single attack families and do not assess cross-dataset OOD transfer"），却没有在同一数据上直接验证。

我认为更核心的问题是：论文应该更清楚地将自身定位为 **分析框架**（analysis paper）而非 **方法论贡献**（method paper）。当前的混合定位（既声称分析贡献又暗示方法优越）导致了 R1 的合理质疑。如果明确定位为分析框架，不与 DeepContext 直接对比也可以接受；但如果声称方法贡献，则必须对比。

---

**[AGREE] R1-N3: 数据规模严重不足以支撑 statistical claims**

完全同意。补充两个具体证据：

1. experiments.tex:11 中 ActorAttack 样本量未说明（我在 Round 1 审稿中已标记为 W3），进一步削弱了 ActorAttack evidence hierarchy 的可信度。

2. Table 6 (appendix.tex:68-70) 中 FITD 的 K=3 和 K=5 结果为 "--"（缺失），意味着 "FITD is easier" 的结论（experiments.tex:53）基于不完整的评估。论文在此处可能隐藏了缺失数据点而非真正评估了所有前缀。

3. MLM-only DD-Full 的三个 seed 中一个 seed (456) recall=0.64（experiments.tex:51），mean=0.914 的置信度极低。3-seed mean±std 作为 performance estimate 在如此高方差下是不可靠的。R1 提议的 5+ seeds 和 bootstrap CI 是合理的最低要求。

---

## Should-Fix 问题

**[AGREE] R1-W1: TF-IDF baseline 对核心叙事的冲击未充分 address**

与我的 N2 完全一致。Table 6 (appendix.tex:65) 显示 TF-IDF 在 OOD DD 上只有 Full 结果（0.944），K=1 到 K=5 全部为 "--"。论文声称 "temporal early detection at K≤5" 是 DisPeD 相对于 TF-IDF 的优势（experiments.tex:52），但从未实际验证 TF-IDF 在 early prefix 上的表现。这是 unsubstantiated claim。

此外，TF-IDF 在 ActorAttack 上完全缺失（Table 1 和 Table 6 均无）。ActorAttack 被论文用作 "structurally complex" 攻击的关键证据（experiments.tex:122），如果 TF-IDF 在 ActorAttack 上也能达到 0.9+，则论文的 discourse-level claim 彻底站不住脚。

---

**[AGREE] R1-W2: BiGRU + frozen encoder 设计缺乏 justification**

同意。补充观察：Table 3 (experiments.tex:84) 中 mean pooling 的单 seed 结果 (F1=1.000) 与 3-seed BiGRU (0.997±0.005) 不可比，但论文基于此讨论 temporal modeling（experiments.tex:135-137: "This preliminary result suggests that detection relies primarily on per-turn representations rather than their sequential order"）。从一个 seed 得出 architectural claim 是过度推断。

同时，frozen encoder 的设计选择限制了消融的解释力：如果允许 end-to-end fine-tuning，vanilla encoder 的表现可能大幅提升，缩小与 domain-adapted variants 的差距。论文没有讨论这一替代方案。

---

**[REBUT] R1-W3: LLM-as-judge baseline 不公平**

部分不同意。R1 认为 "仅 zero-shot，30-47% unparseable" 使比较不公平，建议测试 few-shot/CoT。但我认为论文的 LLM-as-judge 对比的目的不是建立 SOTA baseline，而是证明 "content-level reasoning is insufficient"（experiments.tex:17）。

GPT-5.5 在 IID 数据上 recall 仅 0.105-0.290（appendix.tex:34），Qwen3-8B 在 OOD DD 上预测全部为 benign（F1=0.0，appendix.tex:38）。即使 few-shot/CoT 能改善 parsing，recall 如此低的根本原因可能是 LLM 难以在长对话中识别分布式的恶意意图。

但我同意 R1 的方向：至少应该测试 few-shot 设置以证明 zero-shot 的失败不是 prompt engineering 问题。如果 few-shot GPT-5.5 仍然 recall 很低，论文的 claim 更可信。当前版本确实缺少这一对比。

---

**[AGREE] R1-W4: 策略标注质量验证不足**

同意。method.tex:44 报告 κ=0.78 基于 n=50，平均每类仅约 5.5 个样本。此外，human annotator 是单人（"a human sample"），没有 inter-annotator agreement between multiple humans 的数据。0.78 的 κ 对于 9-class 问题并不算高，尤其在训练数据量有限的情况下。

不过，从论文自身的发现来看（Section 4.2: scrambled = binary = 9-class on detection），标注质量对 **检测** 结果影响不大。标注质量主要影响 Section 5.5 的 strategy trajectory analysis（experiments.tex:244-269），而该分析的 OOD 泛化已经失败（OOD κ=0.126，experiments.tex:266）。所以这个问题的 severity 取决于论文多大程度上依赖 strategy analysis 作为贡献。

---

**[AGREE] R1-W5: α=0.3 loss weight 未 justify**

同意，但 severity 低于 R1 的 "minor" 标注。method.tex:44 使用 α=0.3 但未给出选择理由或 sensitivity analysis。考虑到 scrambled/binary/9-class 三种分类变体在检测上完全相同（Table 3），α 值的选择可能对最终结果影响很小。但仍应在 reproducibility details（appendix.tex:132）中说明。

---

## Strengths

**[AGREE] R1-S1: ablation 设计思路优秀**

完全同意，这也是我的 S1。七变体设计是论文最突出的方法论贡献。

---

**[AGREE] R1-S2: 诚实的 limitations 讨论**

完全同意（我的 S4）。论文对 TF-IDF 基线、OOD strategy prediction 失败、数据规模限制的坦诚承认在 ML safety 论文中罕见。

---

**[AGREE] R1-S3: Cross-encoder validation 有价值**

完全同意（我的 S3）。DeBERTa vs RoBERTa 在不同攻击复杂度上的差异表现（Table 4）是支撑 "difficulty threshold" 概念的有力证据。

---

**[AGREE] R1-S4: Topic classification 作为 negative control 优雅**

同意设计意图优雅，但补充一个 caveat：如我在 R1-N1 回应中提到的，topic classification 使用的 5 个类别与 benign 对话生成的 5 个 topic 完全一致（method.tex:50 vs appendix.tex:139）。这意味着 topic classifier 可能通过区分 "属于五类之一"（benign）vs "不属于"（jailbreak）来做 shortcut detection，而非如论文解释的 "misaligned supervision destabilizes representations"（experiments.tex:118）。如果 topic 分类本身就是一个 jailbreak 检测的 noisy proxy，那它就不是一个纯粹的 negative control。

---

**[AGREE] R1-S5: Perturbation analysis 的 family-dependent 结论诚实**

完全同意。experiments.tex:236 中对 ActorAttack perturbation 的失败（9-class Δ=-20.4±13.5pp）的诚实报告是论文 integrity 的体现。

---

## Questions

**[AGREE] R1-Q1: OOD test data 是否也由 Qwen3-8B 生成？**

这是最关键的问题。experiments.tex:10-11 的措辞模糊："We train on 250 Crescendo... generated via Qwen3-8B. OOD evaluation uses 80 FITD... conversations with no overlap in attack templates." OOD 数据的生成方式未明确说明。如果 OOD 也是 Qwen3-8B 生成，则 R1-N1 的 confound 问题直接成立；如果是不同模型或人类生成，论文应明确说明以消除这一合理质疑。

---

**[REBUT] R1-Q2: scrambled = 9-class 的替代解释——小数据集上任何分类 head 的 gradient signal 都够**

部分不同意。R1 提出 "在小数据集上任何分类 head 的 gradient signal 都可能足够" 作为替代解释，但 topic classification 变体同样有分类 head 和 gradient signal，却产生了截然不同的结果：DD-Full F1=0.541±0.207（Table 3, experiments.tex:116）远低于 scrambled 的 0.997±0.005。如果 "任何分类 head 都够"，topic classification 不应如此差。

所以证据表明不是 "任何分类 head 都够"，而是 "在正确领域数据上的分类 head 都够"，这与论文的 "domain exposure + classification regularization" 解释一致。论文的 regularizer 解释虽然可能不是唯一解释，但 topic 变体的对照确实排除了 R1 提出的这个特定替代假设。

但需要注意：如果 topic classification 的差表现是因为 shortcut learning（如我在 S4 回应中提到的），则这一 rebuttal 的力度会减弱。

---

**[AGREE] R1-Q3: FITD Table 6 中缺少 K=3, K=5 结果**

确认。appendix.tex:68-69 中 FITD 的 9-class 和 vanilla 在 K=3 和 K=5 处为 "--"。FITD 对话通常只有 2-3 轮（appendix.tex:139: "FITD conversations use a 2-3 turn commitment-consistency structure"），所以 K=3+ 可能因对话长度不足而不适用。论文应该明确说明这一点而非留空。

---

**[AGREE] R1-Q4: ActorAttack perturbation 中 9-class 结论可靠性**

同意。experiments.tex:236 报告 9-class Δ 范围从 -1.3pp (seed 123) 到 -30.3pp (seeds 42, 456)。这种 seed-level variance 意味着 perturbation robustness 在 ActorAttack 上完全不可靠。论文虽然诚实报告了（S5），但在 Section 4.4 的叙事中仍然尝试从这些数据中提取 "three-layer pattern"，即使自己承认 "this pattern does not generalize to ActorAttack"（experiments.tex:236）。不可复现的 pattern 不应作为贡献点讨论。

---

**[AGREE] R1-Q5: DeBERTa-v3 vs RoBERTa 的 model capacity confound**

有效问题。DeBERTa-v3-base (184M, RTD pretraining on larger data) vs RoBERTa-base (125M, MLM pretraining) 在参数量和预训练数据上存在差异。论文将跨编码器差异归因于 "pretraining method (RTD vs MLM)" (experiments.tex:172)，但未控制参数量。如果 DeBERTa-v3 的更大 capacity 是导致不同泛化 threshold 的原因，"pretraining method determines the difficulty threshold" 的 claim 就不成立。

理想的控制实验是使用相同参数量的 encoder（如 BERT-base vs RoBERTa-base，两者都是 MLM 但数据/超参不同），或 DeBERTa-v3-base vs DeBERTa-v2-base（同系列不同预训练目标）。当前的比较无法解耦 pretraining method 和 model capacity。

---

## Missing References

**[AGREE] MHJ dataset (Li et al., 2024)**: 论文已引用 Li et al., 2024 (li2024mhj) 但仅在 Introduction 提及 (related_work.tex:7)，未作为评估数据集使用。MHJ 包含人类生成的多轮 jailbreak，直接解决 R1-N1 的 single-LLM confound 问题。应作为 evaluation benchmark。

**[AGREE] JailbreakBench (Chao et al., 2024)**: 标准化 benchmark 对可比性至关重要。

**[AGREE] HarmBench (Mazeika et al., 2024)**: 多维度安全评估 benchmark，相关。

**[REBUT] Latent Jailbreak (Qiu et al., 2023)**: 这是 single-turn latent instruction attack，与论文的 multi-turn persuasion-based 范围关联较弱。论文在 Limitations (conclusion.tex:27) 明确声明 "Single-turn token-level attacks... are not addressed"。不过简要提及作为 scope boundary 仍有价值。

**[AGREE] AutoDAN (Liu et al., 2024)**: 自动化攻击生成方法，与 PAIR (chao2023pair) 类似属于 automated attack 范畴，应在 attacks paragraph 中补充。

---

## 总结：两位 Reviewer 的共识

R1 和我（R2）在以下核心问题上高度一致：
1. **TF-IDF/lexical separability 问题**（R1-W1 ≈ R2-N2）：最关键的 unresolved question
2. **"Preliminary" 定位问题**（R2-N3）：R1 未直接提及但通过 N3 (数据规模不足) 间接暗示同一问题
3. **数据规模和统计 power 不足**（R1-N3 ≈ R2 对 ActorAttack 样本量的质疑）
4. **消融设计有方法论价值**（R1-S1 = R2-S1）
5. **诚实的 Limitations**（R1-S2 = R2-S4）

R1 提出了我未覆盖的关键问题：**single-LLM confound (N1)**。这可能是最严重的威胁——如果所有数据共享 Qwen3-8B 分布，整个 evidence hierarchy 可能是 stylistic artifact。这应作为 rebuttal 要求的最高优先级项。

我维持 Overall 2.5/5 的评分。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-18T16:05:42.089809+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1 历史 issues（全部 resolved，本轮未被提及）\n  # ============================================================\n  - id: \"R1-N1\"\n    summary: \"Evidence hierarchy 统计基础不一致：binary/scrambled 仅 seed 42，其他变体 3-seed，核心排序无方差支撑\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提 N1，R2 独立发现 N4，交叉回应双方完全同意。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未提及，已修复（binary/scrambled 已补充 3-seed）。\"\n    action_items:\n      - round: 1\n        action: \"训练 binary (seed 123, 456) + scrambled (seed 123, 456) Stage 1+2，DD OOD 评估\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"MF1 完成: binary 3-seed=0.997±0.005, scrambled 3-seed=0.997±0.005\"\n    resolution_round: 1\n\n  - id: \"R1-N2\"\n    summary: \"Three-layer robustness attribution 在 n=76 上缺乏统计显著性\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提 N2。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未作为独立 issue 提及，McNemar test 已添加。但 R1 round 2 仍质疑 3-seed 统计功效（归入 R2-N3-new）。\"\n    action_items:\n      - round: 1\n        action: \"McNemar's test + bootstrap CI; 降级为 observed pattern\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"MF2 完成\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"缺少与已发表 multi-turn defense 的直接实验对比\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提 N3。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"本轮再次被两位 Reviewer 提出（R1-N2-new, R2 交叉 AGREE）。Round 1 的修复（重构 related_work.tex 声明 vanilla≠DeepContext proxy）被认为不充分——仍缺直接对比实验。\"\n    action_items:\n      - round: 1\n        action: \"重构论证：vanilla ≠ DeepContext proxy\"\n        assigned_to: paper_agent\n        status: resolved\n      - round: 2\n        action: \"复现 DeepContext 或在共同 benchmark 对比，或明确定位为分析框架而非 SOTA 方法\"\n        assigned_to: research_director\n        status: open\n    resolution: \"Round 1 修复被认为不充分，Round 2 再次提出\"\n    resolution_round: null\n\n  - id: \"R1-N4\"\n    summary: \"数据集规模过小\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"n=80 DD 上每个 misclassification 改变 F1 约 1.25pp。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"本轮再次被两位 Reviewer 提出（R1-N3-new, R2 交叉 AGREE）。虽然 ActorAttack 扩展了 OOD 范围，但 500 训练 + 76-118 测试 + 3 seeds 仍不足。\"\n    action_items:\n      - round: 1\n        action: \"降级 claim 为 preliminary findings\"\n        assigned_to: paper_agent\n        status: resolved\n      - round: 2\n        action: \"至少 5 seeds + bootstrap 95% CI + paired bootstrap/permutation test\"\n        assigned_to: research_director\n        status: open\n    resolution: \"Round 1 降级为 preliminary，但 preliminary framing 本身成为新 critical issue（R2-N3-new）\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"有效 OOD 评估实质上是 single-dataset（FITD 无区分度），cross-attack claim 仅由 DD 支撑\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 首提为 N3 critical，R1 交叉升级。\"\n      - round: 2\n        reviewers: []\n        note: \"ActorAttack 扩展后不再作为独立 issue。但 FITD 仍无区分度（R1 Q3 交叉确认）。\"\n    action_items:\n      - round: 1\n        action: \"生成 ActorAttack 风格 OOD 对话 80 条\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"EXP-2 完成: ActorAttack 118 conversations\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Mean pooling=BiGRU 结论基于 single seed\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W1, R2 W6。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"虽已弱化为 preliminary，但两位 Reviewer 仍认为 single-seed 不应支撑 architectural claim。归入 R2-W2-new。\"\n    action_items:\n      - round: 1\n        action: \"弱化因果性结论\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"Paper Agent 已弱化: single seed...preliminary\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"策略标注质量验证不充分\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W2。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"本轮再次提出（R1-W4-new）：n=50 单标注员仍不充分。\"\n    action_items:\n      - round: 1\n        action: \"Limitations 讨论 + 承诺数据发布\"\n        assigned_to: paper_agent\n        status: resolved\n      - round: 2\n        action: \"至少两个独立标注员 + human-human κ + n≥100\"\n        assigned_to: research_director\n        status: open\n    resolution: \"Round 1 添加了 Limitations 讨论，但验证规模仍不足\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"LLM-as-judge baseline 仅测 IID\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W3。\"\n      - round: 2\n        reviewers: []\n        note: \"OOD LLM-as-judge 已补充。但 zero-shot only 问题被 R1-W3-new 提出。\"\n    action_items:\n      - round: 1\n        action: \"DD/FITD OOD 上跑 Qwen3-8B\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"EXP-5 完成: Qwen3-8B DD F1=0.000, FITD F1=0.025\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"TF-IDF LR 强表现未被充分讨论\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W4, R2 W4。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"虽已添加讨论，但本轮升级为 critical（R2-N2-new, R1-W1-new）：缺 TF-IDF per-prefix 和 ActorAttack 结果，discourse-level claim 仍无 probing 支撑。\"\n    action_items:\n      - round: 1\n        action: \"诚实讨论 TF-IDF，probing 作为 future work\"\n        assigned_to: paper_agent\n        status: resolved\n      - round: 2\n        action: \"补充 TF-IDF 全 prefix + ActorAttack 结果；做 probing experiments\"\n        assigned_to: research_director\n        status: open\n    resolution: \"Round 1 添加了讨论，但缺关键数据点\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"可复现性不足\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W5。\"\n      - round: 2\n        reviewers: []\n        note: \"Appendix 已补充。生成 prompt 仍未直接披露（仅承诺发布），但 Reviewer 未再单独提出。\"\n    action_items:\n      - round: 1\n        action: \"Appendix 补充完整超参数表\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"Paper Agent 已添加 Appendix C (Reproducibility Details)\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"Abstract 过度堆砌数据\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 W1。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"本轮再次提出（R2-W2-new）：仍有 12+ 数值在 ~150 词中。Round 1 修复不充分。\"\n    action_items:\n      - round: 1\n        action: \"精简至 2-3 关键数字\"\n        assigned_to: paper_agent\n        status: resolved\n      - round: 2\n        action: \"保留 2-3 headline numbers，其余用定性描述\"\n        assigned_to: research_director\n        status: open\n    resolution: \"Round 1 精简不充分，仍有数据过载\"\n    resolution_round: null\n\n  - id: \"R2-W2\"\n    summary: \"partially falsified 叙事对接收不利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 W2。\"\n      - round: 2\n        reviewers: []\n        note: \"已重构。但 preliminary framing 问题以新形式出现（R2-N3-new）。\"\n    action_items:\n      - round: 1\n        action: \"正面重构叙事\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"Paper Agent 已重构\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Contributions 列表过于密集\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 W3。\"\n      - round: 2\n        reviewers: []\n        note: \"已拆为 3 条，本轮未再提及。\"\n    action_items:\n      - round: 1\n        action: \"拆为 3-4 条\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"Paper Agent 已拆为 3 条\"\n    resolution_round: 1\n\n  - id: \"R2-W5\"\n    summary: \"Strategy trajectory 使用 ground-truth labels 而非模型预测\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 W5。\"\n      - round: 2\n        reviewers: []\n        note: \"已报告 OOD κ=0.126，scope 限于 IID。本轮未再单独提出。\"\n    action_items:\n      - round: 1\n        action: \"报告 OOD κ=0.126, scope interpretability to IID\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"完成: OOD accuracy=30.7%, κ=0.126\"\n    resolution_round: 1\n\n  - id: \"R2-W7\"\n    summary: \"Limitations 格式不符合 ACL/ARR\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 W7。\"\n      - round: 2\n        reviewers: []\n        note: \"已创建独立 Limitations section。本轮未再提及。\"\n    action_items:\n      - round: 1\n        action: \"拆为独立 section\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"Paper Agent 已创建独立 Limitations section\"\n    resolution_round: 1\n\n  - id: \"R2-REF1\"\n    summary: \"缺失引用方向\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"已补充 6 条引用，但本轮又发现新的缺失引用（见 R2-REF2-new）。\"\n    action_items:\n      - round: 1\n        action: \"补充引用\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"Paper Agent 已新增 6 条引用\"\n    resolution_round: 1\n\n  - id: \"SF12\"\n    summary: \"图表问题合集\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"小问题合集。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未再提及原始问题，但 Figure 3 浮动问题作为新 issue 出现（R2-W7-new）。\"\n    action_items:\n      - round: 1\n        action: \"修复各项\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"Paper Agent 已修复\"\n    resolution_round: 1\n\n  # ============================================================\n  # Round 2 新 issues\n  # ============================================================\n  - id: \"R1-N1-v2\"\n    summary: \"单模型（Qwen3-8B）生成全部数据造成系统性 confound，TF-IDF 0.944 暗示 stylistic artifacts\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 交叉 AGREE 并补充。两位共识：如果 OOD 也是 Qwen3-8B 生成，整个 evidence hierarchy 可能是 artifact-driven。\"\n    action_items:\n      - round: 2\n        action: \"用不同 LLM 生成部分 OOD 数据；用 MHJ 人类数据评估；做 probing 区分 lexical vs discourse features\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N1-v2\"\n    summary: \"核心贡献新颖性不足：Don't Stop Pretraining 在 jailbreak detection 的直接应用\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉 AGREE with nuance。共识：headline result (~60pp by MLM) 是 DAPT 直接推论，更精细发现（scrambled regularizer, difficulty threshold）有趣但统计支撑不足。\"\n    action_items:\n      - round: 2\n        action: \"重新 frame：以 difficulty threshold 和 regularizer interpretation 为主线，DAPT 验证降为支撑\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N2-v2\"\n    summary: \"TF-IDF 基线（F1=0.944）严重削弱 discourse-level representation 价值主张，缺 per-prefix 和 ActorAttack 数据\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉 AGREE 并补充。共识：TF-IDF per-prefix 和 ActorAttack 结果缺失使 early detection 和 discourse-level claim 均为 unsubstantiated。\"\n    action_items:\n      - round: 2\n        action: \"补充 TF-IDF 全 prefix + ActorAttack 结果；做 probing experiments 区分 lexical 和 discourse features\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3-v2\"\n    summary: \"'Preliminary findings' 在 Abstract/Introduction/Conclusion 三处出现，与 long paper 定位矛盾\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉 AGREE with nuance（根源是实验规模而非措辞）。共识：仅删 preliminary 而不扩大实验会变成 overclaiming，需同时解决。\"\n    action_items:\n      - round: 2\n        action: \"同时移除 preliminary hedging 并扩大实验规模以支撑 definitive claims；或改投 Findings/short paper\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2-v2\"\n    summary: \"缺少与 DeepContext/BIID/G-Guard/SafeDream 的直接实验对比（Round 1 修复不充分）\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 交叉 AGREE（建议明确定位为分析框架 vs 方法论贡献）。Round 1 仅重构文字，未加实验。\"\n    action_items:\n      - round: 2\n        action: \"复现 DeepContext 或共同 benchmark 对比；或明确定位为 analysis paper\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3-v2\"\n    summary: \"数据规模（500 训练 + 76-118 测试 + 3 seeds）不足以支撑 statistical claims\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 交叉完全 AGREE。MLM DD-Full std=0.115（seed 456 recall=0.64），3 seeds 不可靠。\"\n    action_items:\n      - round: 2\n        action: \"至少 5 seeds（理想 10）；bootstrap 95% CI；paired bootstrap/permutation test\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W5-v2\"\n    summary: \"缺少 ACL ARR Responsible NLP Research Checklist（desk reject 风险）\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提为 major，R1 交叉升级为 critical（desk reject 风险）。论文涉及 jailbreak attack 技术，ethical checklist 尤为重要。\"\n    action_items:\n      - round: 2\n        action: \"按 ACL ARR 要求填写完整 Responsible NLP Research Checklist\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1-v2\"\n    summary: \"Related Work 段落包含大量本文实验数据（F1 数值、pp 差距），应移至 Results\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉 AGREE。至少 3 处 Related Work 段落包含本文数值。\"\n    action_items:\n      - round: 2\n        action: \"移除 Related Work 中所有本文实验数据引用，改为概念层面对比\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2-v2\"\n    summary: \"Abstract 仍有 12+ 数值在 ~150 词中，数据过载（Round 1 修复不充分）\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉 AGREE。\"\n    action_items:\n      - round: 2\n        action: \"保留 2-3 headline numbers + 核心 takeaway，其余用定性描述\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3-v2\"\n    summary: \"ActorAttack 样本量未在 Section 4.1 中说明\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉 AGREE（R1 Q4 同问）。\"\n    action_items:\n      - round: 2\n        action: \"补充 ActorAttack 具体样本数\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W4-v2\"\n    summary: \"Introduction 第四段结果段过于冗长（~200 词 15+ 数值），读者无法消化\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉 AGREE。\"\n    action_items:\n      - round: 2\n        action: \"压缩为 2-3 headline numbers + 核心 takeaway\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1-v2\"\n    summary: \"TF-IDF 缺 per-prefix (K=1-5) 和 ActorAttack 结果，early detection claim 未验证\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 交叉 AGREE。与 R2-N2-v2 关联。\"\n    action_items:\n      - round: 2\n        action: \"报告 TF-IDF 在所有 prefix lengths 和 ActorAttack 的结果\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2-v2\"\n    summary: \"BiGRU + frozen encoder 设计缺乏 justification；mean pooling single-seed 不可比\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 交叉 AGREE。frozen 设计可能低估某些 variants 潜力。\"\n    action_items:\n      - round: 2\n        action: \"讨论 frozen vs end-to-end trade-off；mean pooling 需 multi-seed\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3-v2\"\n    summary: \"LLM-as-judge baseline 仅 zero-shot，30-47% unparseable，不公平\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 部分 REBUT（目的是证明 content-level reasoning 不足而非建立 SOTA），但同意应补 few-shot。\"\n    action_items:\n      - round: 2\n        action: \"补充 few-shot (3-5 examples) 评估；修复 prompt 降低 unparseable rate；弱化 claim\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4-v2\"\n    summary: \"策略标注质量验证不足：n=50 单标注员，9-class 每类 ~5.5 samples\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 交叉 AGREE（但认为 severity 取决于 strategy analysis 在贡献中的权重）。\"\n    action_items:\n      - round: 2\n        action: \"至少两个独立标注员 + human-human κ + n≥100\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5-v2\"\n    summary: \"α=0.3 loss weight 未 justify\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 首提 minor，R2 交叉 AGREE（severity 低）。\"\n    action_items:\n      - round: 2\n        action: \"简要说明选择理由或报告 sensitivity\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W6-v2\"\n    summary: \"页数可能超限（Conclusion 是否在第 8 页内结束需验证）\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉 AGREE with caveat（无法编译验证）。\"\n    action_items:\n      - round: 2\n        action: \"确认编译后页数；如超限则压缩\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W7-v2\"\n    summary: \"Figure 3 (figure*) 可能浮动到非预期位置\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉 AGREE。Minor LaTeX issue。\"\n    action_items:\n      - round: 2\n        action: \"检查编译后 Figure 3 位置，必要时用 [t!] 或 FloatBarrier\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"CROSS-Q5\"\n    summary: \"Topic classification 5-class 与 benign 生成 topic 完全一致，存在 shortcut learning confound\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 Q5 首次发现，R1 交叉回应中独立验证并升级。method.tex:50 和 appendix.tex:139 的 5 个类别完全一致。\"\n    action_items:\n      - round: 2\n        action: \"用与 jailbreak 正交的 topic categories 重训 topic variant，或确保 jailbreak/benign 共享 topic 分布\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-TERM\"\n    summary: \"术语不一致：domain exposure / domain adaptation / continued pretraining / domain-adaptive pretraining 混用\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [2]\n        note: \"R2 小问题中提出。\"\n    action_items:\n      - round: 2\n        action: \"统一术语\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-REF2\"\n    summary: \"缺失引用：Persuasion for Good, SmoothLLM, TAP, Circuit Breakers, GradSafe, MHJ dataset, JailbreakBench, HarmBench, AutoDAN\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 和 R2 各提出部分缺失引用，交叉回应中达成共识。高优先级：Persuasion for Good, SmoothLLM, TAP, MHJ, JailbreakBench, HarmBench。\"\n    action_items:\n      - round: 2\n        action: \"补充高优先级缺失引用\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-CAPACITY\"\n    summary: \"DeBERTa-v3 vs RoBERTa 参数量/训练数据不同，difficulty threshold claim 可能混淆 capacity confound\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 Q5 首提，R2 交叉 AGREE。DeBERTa-v3-base 184M vs RoBERTa-base 125M。\"\n    action_items:\n      - round: 2\n        action: \"讨论 capacity confound；理想情况下用 BERT-base vs RoBERTa-base 或 DeBERTa-v3 vs v2 控制\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-BIB\"\n    summary: \"引用格式问题：austin1962 年份可能有误，chao2023pair 实为 2025，han2024wildguard 作者不匹配\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [2]\n        note: \"R2 小问题中提出。\"\n    action_items:\n      - round: 2\n        action: \"核查并修正 bib 条目\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1 历史 issues（全部 resolved，本轮未被提及）\n  # ============================================================\n  - id: \"R1-N1\"\n    summary: \"Evidence hierarchy 统计基础不一致：binary/scrambled 仅 seed 42，其他变体 3-seed，核心排序无方差支撑\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提 N1，R2 独立发现 N4，交叉回应双方完全同意。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未提及，已修复（binary/scrambled 已补充 3-seed）。\"\n    action_items:\n      - round: 1\n        action: \"训练 binary (seed 123, 456) + scrambled (seed 123, 456) Stage 1+2，DD OOD 评估\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"MF1 完成: binary 3-seed=0.997±0.005, scrambled 3-seed=0.997±0.005\"\n    resolution_round: 1\n\n  - id: \"R1-N2\"\n    summary: \"Three-layer robustness attribution 在 n=76 上缺乏统计显著性\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提 N2。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未作为独立 issue 提及，McNemar test 已添加。但 R1 round 2 仍质疑 3-seed 统计功效（归入 R2-N3-new）。\"\n    action_items:\n      - round: 1\n        action: \"McNemar's test + bootstrap CI; 降级为 observed pattern\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"MF2 完成\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"缺少与已发表 multi-turn defense 的直接实验对比\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提 N3。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"本轮再次被两位 Reviewer 提出（R1-N2-new, R2 交叉 AGREE）。Round 1 的修复（重构 related_work.tex 声明 vanilla≠DeepContext proxy）被认为不充分——仍缺直接对比实验。\"\n    action_items:\n      - round: 1\n        action: \"重构论证：vanilla ≠ DeepContext proxy\"\n        assigned_to: paper_agent\n        status: resolved\n      - round: 2\n        action: \"复现 DeepContext 或在共同 benchmark 对比，或明确定位为分析框架而非 SOTA 方法\"\n        assigned_to: research_director\n        status: open\n    resolution: \"Round 1 修复被认为不充分，Round 2 再次提出\"\n    resolution_round: null\n\n  - id: \"R1-N4\"\n    summary: \"数据集规模过小\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"n=80 DD 上每个 misclassification 改变 F1 约 1.25pp。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"本轮再次被两位 Reviewer 提出（R1-N3-new, R2 交叉 AGREE）。虽然 ActorAttack 扩展了 OOD 范围，但 500 训练 + 76-118 测试 + 3 seeds 仍不足。\"\n    action_items:\n      - round: 1\n        action: \"降级 claim 为 preliminary findings\"\n        assigned_to: paper_agent\n        status: resolved\n      - round: 2\n        action: \"至少 5 seeds + bootstrap 95% CI + paired bootstrap/permutation test\"\n        assigned_to: research_director\n        status: open\n    resolution: \"Round 1 降级为 preliminary，但 preliminary framing 本身成为新 critical issue（R2-N3-new）\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"有效 OOD 评估实质上是 single-dataset（FITD 无区分度），cross-attack claim 仅由 DD 支撑\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 首提为 N3 critical，R1 交叉升级。\"\n      - round: 2\n        reviewers: []\n        note: \"ActorAttack 扩展后不再作为独立 issue。但 FITD 仍无区分度（R1 Q3 交叉确认）。\"\n    action_items:\n      - round: 1\n        action: \"生成 ActorAttack 风格 OOD 对话 80 条\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"EXP-2 完成: ActorAttack 118 conversations\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Mean pooling=BiGRU 结论基于 single seed\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W1, R2 W6。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"虽已弱化为 preliminary，但两位 Reviewer 仍认为 single-seed 不应支撑 architectural claim。归入 R2-W2-new。\"\n    action_items:\n      - round: 1\n        action: \"弱化因果性结论\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"Paper Agent 已弱化: single seed...preliminary\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"策略标注质量验证不充分\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W2。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"本轮再次提出（R1-W4-new）：n=50 单标注员仍不充分。\"\n    action_items:\n      - round: 1\n        action: \"Limitations 讨论 + 承诺数据发布\"\n        assigned_to: paper_agent\n        status: resolved\n      - round: 2\n        action: \"至少两个独立标注员 + human-human κ + n≥100\"\n        assigned_to: research_director\n        status: open\n    resolution: \"Round 1 添加了 Limitations 讨论，但验证规模仍不足\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"LLM-as-judge baseline 仅测 IID\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W3。\"\n      - round: 2\n        reviewers: []\n        note: \"OOD LLM-as-judge 已补充。但 zero-shot only 问题被 R1-W3-new 提出。\"\n    action_items:\n      - round: 1\n        action: \"DD/FITD OOD 上跑 Qwen3-8B\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"EXP-5 完成: Qwen3-8B DD F1=0.000, FITD F1=0.025\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"TF-IDF LR 强表现未被充分讨论\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W4, R2 W4。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"虽已添加讨论，但本轮升级为 critical（R2-N2-new, R1-W1-new）：缺 TF-IDF per-prefix 和 ActorAttack 结果，discourse-level claim 仍无 probing 支撑。\"\n    action_items:\n      - round: 1\n        action: \"诚实讨论 TF-IDF，probing 作为 future work\"\n        assigned_to: paper_agent\n        status: resolved\n      - round: 2\n        action: \"补充 TF-IDF 全 prefix + ActorAttack 结果；做 probing experiments\"\n        assigned_to: research_director\n        status: open\n    resolution: \"Round 1 添加了讨论，但缺关键数据点\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"可复现性不足\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W5。\"\n      - round: 2\n        reviewers: []\n        note: \"Appendix 已补充。生成 prompt 仍未直接披露（仅承诺发布），但 Reviewer 未再单独提出。\"\n    action_items:\n      - round: 1\n        action: \"Appendix 补充完整超参数表\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"Paper Agent 已添加 Appendix C (Reproducibility Details)\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"Abstract 过度堆砌数据\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 W1。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"本轮再次提出（R2-W2-new）：仍有 12+ 数值在 ~150 词中。Round 1 修复不充分。\"\n    action_items:\n      - round: 1\n        action: \"精简至 2-3 关键数字\"\n        assigned_to: paper_agent\n        status: resolved\n      - round: 2\n        action: \"保留 2-3 headline numbers，其余用定性描述\"\n        assigned_to: research_director\n        status: open\n    resolution: \"Round 1 精简不充分，仍有数据过载\"\n    resolution_round: null\n\n  - id: \"R2-W2\"\n    summary: \"partially falsified 叙事对接收不利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 W2。\"\n      - round: 2\n        reviewers: []\n        note: \"已重构。但 preliminary framing 问题以新形式出现（R2-N3-new）。\"\n    action_items:\n      - round: 1\n        action: \"正面重构叙事\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"Paper Agent 已重构\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Contributions 列表过于密集\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 W3。\"\n      - round: 2\n        reviewers: []\n        note: \"已拆为 3 条，本轮未再提及。\"\n    action_items:\n      - round: 1\n        action: \"拆为 3-4 条\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"Paper Agent 已拆为 3 条\"\n    resolution_round: 1\n\n  - id: \"R2-W5\"\n    summary: \"Strategy trajectory 使用 ground-truth labels 而非模型预测\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 W5。\"\n      - round: 2\n        reviewers: []\n        note: \"已报告 OOD κ=0.126，scope 限于 IID。本轮未再单独提出。\"\n    action_items:\n      - round: 1\n        action: \"报告 OOD κ=0.126, scope interpretability to IID\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"完成: OOD accuracy=30.7%, κ=0.126\"\n    resolution_round: 1\n\n  - id: \"R2-W7\"\n    summary: \"Limitations 格式不符合 ACL/ARR\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 W7。\"\n      - round: 2\n        reviewers: []\n        note: \"已创建独立 Limitations section。本轮未再提及。\"\n    action_items:\n      - round: 1\n        action: \"拆为独立 section\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"Paper Agent 已创建独立 Limitations section\"\n    resolution_round: 1\n\n  - id: \"R2-REF1\"\n    summary: \"缺失引用方向\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 提出。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"已补充 6 条引用，但本轮又发现新的缺失引用（见 R2-REF2-new）。\"\n    action_items:\n      - round: 1\n        action: \"补充引用\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"Paper Agent 已新增 6 条引用\"\n    resolution_round: 1\n\n  - id: \"SF12\"\n    summary: \"图表问题合集\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"小问题合集。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未再提及原始问题，但 Figure 3 浮动问题作为新 issue 出现（R2-W7-new）。\"\n    action_items:\n      - round: 1\n        action: \"修复各项\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"Paper Agent 已修复\"\n    resolution_round: 1\n\n  # ============================================================\n  # Round 2 新 issues\n  # ============================================================\n  - id: \"R1-N1-v2\"\n    summary: \"单模型（Qwen3-8B）生成全部数据造成系统性 confound，TF-IDF 0.944 暗示 stylistic artifacts\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 交叉 AGREE 并补充。两位共识：如果 OOD 也是 Qwen3-8B 生成，整个 evidence hierarchy 可能是 artifact-driven。\"\n    action_items:\n      - round: 2\n        action: \"用不同 LLM 生成部分 OOD 数据；用 MHJ 人类数据评估；做 probing 区分 lexical vs discourse features\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N1-v2\"\n    summary: \"核心贡献新颖性不足：Don't Stop Pretraining 在 jailbreak detection 的直接应用\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉 AGREE with nuance。共识：headline result (~60pp by MLM) 是 DAPT 直接推论，更精细发现（scrambled regularizer, difficulty threshold）有趣但统计支撑不足。\"\n    action_items:\n      - round: 2\n        action: \"重新 frame：以 difficulty threshold 和 regularizer interpretation 为主线，DAPT 验证降为支撑\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N2-v2\"\n    summary: \"TF-IDF 基线（F1=0.944）严重削弱 discourse-level representation 价值主张，缺 per-prefix 和 ActorAttack 数据\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉 AGREE 并补充。共识：TF-IDF per-prefix 和 ActorAttack 结果缺失使 early detection 和 discourse-level claim 均为 unsubstantiated。\"\n    action_items:\n      - round: 2\n        action: \"补充 TF-IDF 全 prefix + ActorAttack 结果；做 probing experiments 区分 lexical 和 discourse features\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3-v2\"\n    summary: \"'Preliminary findings' 在 Abstract/Introduction/Conclusion 三处出现，与 long paper 定位矛盾\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉 AGREE with nuance（根源是实验规模而非措辞）。共识：仅删 preliminary 而不扩大实验会变成 overclaiming，需同时解决。\"\n    action_items:\n      - round: 2\n        action: \"同时移除 preliminary hedging 并扩大实验规模以支撑 definitive claims；或改投 Findings/short paper\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2-v2\"\n    summary: \"缺少与 DeepContext/BIID/G-Guard/SafeDream 的直接实验对比（Round 1 修复不充分）\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 交叉 AGREE（建议明确定位为分析框架 vs 方法论贡献）。Round 1 仅重构文字，未加实验。\"\n    action_items:\n      - round: 2\n        action: \"复现 DeepContext 或共同 benchmark 对比；或明确定位为 analysis paper\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3-v2\"\n    summary: \"数据规模（500 训练 + 76-118 测试 + 3 seeds）不足以支撑 statistical claims\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 交叉完全 AGREE。MLM DD-Full std=0.115（seed 456 recall=0.64），3 seeds 不可靠。\"\n    action_items:\n      - round: 2\n        action: \"至少 5 seeds（理想 10）；bootstrap 95% CI；paired bootstrap/permutation test\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W5-v2\"\n    summary: \"缺少 ACL ARR Responsible NLP Research Checklist（desk reject 风险）\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提为 major，R1 交叉升级为 critical（desk reject 风险）。论文涉及 jailbreak attack 技术，ethical checklist 尤为重要。\"\n    action_items:\n      - round: 2\n        action: \"按 ACL ARR 要求填写完整 Responsible NLP Research Checklist\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1-v2\"\n    summary: \"Related Work 段落包含大量本文实验数据（F1 数值、pp 差距），应移至 Results\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉 AGREE。至少 3 处 Related Work 段落包含本文数值。\"\n    action_items:\n      - round: 2\n        action: \"移除 Related Work 中所有本文实验数据引用，改为概念层面对比\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2-v2\"\n    summary: \"Abstract 仍有 12+ 数值在 ~150 词中，数据过载（Round 1 修复不充分）\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉 AGREE。\"\n    action_items:\n      - round: 2\n        action: \"保留 2-3 headline numbers + 核心 takeaway，其余用定性描述\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3-v2\"\n    summary: \"ActorAttack 样本量未在 Section 4.1 中说明\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉 AGREE（R1 Q4 同问）。\"\n    action_items:\n      - round: 2\n        action: \"补充 ActorAttack 具体样本数\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W4-v2\"\n    summary: \"Introduction 第四段结果段过于冗长（~200 词 15+ 数值），读者无法消化\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉 AGREE。\"\n    action_items:\n      - round: 2\n        action: \"压缩为 2-3 headline numbers + 核心 takeaway\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1-v2\"\n    summary: \"TF-IDF 缺 per-prefix (K=1-5) 和 ActorAttack 结果，early detection claim 未验证\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 交叉 AGREE。与 R2-N2-v2 关联。\"\n    action_items:\n      - round: 2\n        action: \"报告 TF-IDF 在所有 prefix lengths 和 ActorAttack 的结果\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2-v2\"\n    summary: \"BiGRU + frozen encoder 设计缺乏 justification；mean pooling single-seed 不可比\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 交叉 AGREE。frozen 设计可能低估某些 variants 潜力。\"\n    action_items:\n      - round: 2\n        action: \"讨论 frozen vs end-to-end trade-off；mean pooling 需 multi-seed\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3-v2\"\n    summary: \"LLM-as-judge baseline 仅 zero-shot，30-47% unparseable，不公平\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 部分 REBUT（目的是证明 content-level reasoning 不足而非建立 SOTA），但同意应补 few-shot。\"\n    action_items:\n      - round: 2\n        action: \"补充 few-shot (3-5 examples) 评估；修复 prompt 降低 unparseable rate；弱化 claim\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4-v2\"\n    summary: \"策略标注质量验证不足：n=50 单标注员，9-class 每类 ~5.5 samples\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 交叉 AGREE（但认为 severity 取决于 strategy analysis 在贡献中的权重）。\"\n    action_items:\n      - round: 2\n        action: \"至少两个独立标注员 + human-human κ + n≥100\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5-v2\"\n    summary: \"α=0.3 loss weight 未 justify\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 首提 minor，R2 交叉 AGREE（severity 低）。\"\n    action_items:\n      - round: 2\n        action: \"简要说明选择理由或报告 sensitivity\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W6-v2\"\n    summary: \"页数可能超限（Conclusion 是否在第 8 页内结束需验证）\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉 AGREE with caveat（无法编译验证）。\"\n    action_items:\n      - round: 2\n        action: \"确认编译后页数；如超限则压缩\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W7-v2\"\n    summary: \"Figure 3 (figure*) 可能浮动到非预期位置\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉 AGREE。Minor LaTeX issue。\"\n    action_items:\n      - round: 2\n        action: \"检查编译后 Figure 3 位置，必要时用 [t!] 或 FloatBarrier\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"CROSS-Q5\"\n    summary: \"Topic classification 5-class 与 benign 生成 topic 完全一致，存在 shortcut learning confound\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 Q5 首次发现，R1 交叉回应中独立验证并升级。method.tex:50 和 appendix.tex:139 的 5 个类别完全一致。\"\n    action_items:\n      - round: 2\n        action: \"用与 jailbreak 正交的 topic categories 重训 topic variant，或确保 jailbreak/benign 共享 topic 分布\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-TERM\"\n    summary: \"术语不一致：domain exposure / domain adaptation / continued pretraining / domain-adaptive pretraining 混用\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [2]\n        note: \"R2 小问题中提出。\"\n    action_items:\n      - round: 2\n        action: \"统一术语\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-REF2\"\n    summary: \"缺失引用：Persuasion for Good, SmoothLLM, TAP, Circuit Breakers, GradSafe, MHJ dataset, JailbreakBench, HarmBench, AutoDAN\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 和 R2 各提出部分缺失引用，交叉回应中达成共识。高优先级：Persuasion for Good, SmoothLLM, TAP, MHJ, JailbreakBench, HarmBench。\"\n    action_items:\n      - round: 2\n        action: \"补充高优先级缺失引用\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-CAPACITY\"\n    summary: \"DeBERTa-v3 vs RoBERTa 参数量/训练数据不同，difficulty threshold claim 可能混淆 capacity confound\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 Q5 首提，R2 交叉 AGREE。DeBERTa-v3-base 184M vs RoBERTa-base 125M。\"\n    action_items:\n      - round: 2\n        action: \"讨论 capacity confound；理想情况下用 BERT-base vs RoBERTa-base 或 DeBERTa-v3 vs v2 控制\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-BIB\"\n    summary: \"引用格式问题：austin1962 年份可能有误，chao2023pair 实为 2025，han2024wildguard 作者不匹配\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [2]\n        note: \"R2 小问题中提出。\"\n    action_items:\n      - round: 2\n        action: \"核查并修正 bib 条目\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-18T16:05:42.191148+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/review_issues.yaml\", \"bytes\": 23769}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-18T16:07:47.175916+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject",
  "report": "# 圆桌审稿报告（Round 2）\n\n**论文**: What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**审稿模式**: 重新审稿（fresh review，无 Round 1 记忆）\n**Reviewer 编排**: 2 人（EMNLP 标准）\n- Reviewer 1: 方法严谨性 + 实验设计 + 统计有效性\n- Reviewer 2: 新颖性 + Related Work 定位 + 写作质量 + 完整性\n\n---\n\n## Summary\n\n本文提出 DisPeD，一个两阶段框架（Stage-1 encoder adaptation + Stage-2 BiGRU aggregation），通过 7 个受控 Stage-1 变体系统分解跨攻击泛化的机制。核心发现：(1) 在 DeBERTa-v3 上 continued pretraining（MLM）桥接约 60pp OOD gap；(2) 分类监督（9-class/binary/scrambled 三种分类变体检测 F1 相同）作为 representation regularizer 而非 semantic classifier 起作用；(3) RoBERTa 交叉验证显示 encoder pretraining method 决定 domain adaptation 变为必要的难度阈值。实验在 Qwen3-8B 合成数据上覆盖 4 个攻击家族（Crescendo IID + FITD/DD/ActorAttack OOD），规模为 500 训练 + 76-118 测试对话。\n\n---\n\n## Strengths\n\n**S1** [共识] **消融实验设计系统严谨**。七个 Stage-1 变体各自隔离一个因素（domain exposure, classification supervision, label quality, label granularity, domain specificity, misaligned supervision），共享相同 Stage-2 pipeline，使对比公平。这是论文最突出的方法论贡献。\n\n**S2** [共识] **Scrambled labels 发现有洞察力**。Scrambled = binary = 9-class 在检测 F1 上完全相同（0.997±0.005, Table 2），证明分类目标作为 representation regularizer 而非 semantic classifier 起作用。这超越了简单的 domain adaptation 验证。\n\n**S3** [共识] **Cross-encoder \"difficulty threshold\" 概念有价值**。DeBERTa-v3 vanilla 在 DD 上坍塌（F1=0.312）而 RoBERTa vanilla 不坍塌（0.981），但 RoBERTa 在结构更复杂的 ActorAttack 上坍塌（0.466），揭示 encoder pretraining method 决定了 adaptation 变为必要的难度阈值（Table 4）。\n\n**S4** [共识] **诚实的 Limitations section**。论文坦率承认 TF-IDF 基线问题、strategy prediction 不泛化（OOD κ=0.126）、数据规模限制、single-seed mean pooling 等。这种 intellectual honesty 在 ML safety 论文中罕见。\n\n**S5** [共识] **可复现性优秀**。完整超参数（Appendix E）、总计算成本 <4 GPU-hours、承诺开源。\n\n---\n\n## Weaknesses（按 severity 排序）\n\n### Must-Fix（7 项 critical，影响接收决定）\n\n**N1** [critical, 共识] **单模型（Qwen3-8B）生成全部数据造成系统性 confound**\n- Qwen3-8B 同时用于生成训练数据、策略标注、OOD 测试数据和对抗性 paraphrase。TF-IDF LR 在 OOD DD 上 F1=0.944（Table 1），强烈暗示模型利用的是 Qwen3-8B stylistic fingerprint 而非 discourse-level features。论文在 Limitations 中讨论了 lexical separability 但完全未提及 single-LLM confound。\n- **影响**：如果 OOD gap 的桥接主要来自学习生成模型的 stylistic artifacts，则整个 evidence hierarchy 可能是 artifact-driven。这是论文最核心 claim 的替代解释。\n- **修复方向**：(1) 用不同 LLM 生成部分 OOD 数据；(2) 用人类编写数据（MHJ dataset）评估；(3) 做 probing 实验区分 lexical 和 discourse-level features。\n\n**N2** [critical, 共识] **核心贡献新颖性不足**\n- 核心发现（continued pretraining bridges ~60pp OOD gap）是 Gururangan et al. (2020) \"Don't Stop Pretraining\" 在 jailbreak detection 的直接验证。更精细的 decomposition（scrambled regularizer, difficulty threshold）有趣，但在 3 seeds + 500 对话规模上统计支撑不足。\n- **影响**：ACL ARR Excitement 维度要求推进领域认知。当前 headline result 在新领域验证已知结论，更适合 Findings paper 或 short paper。\n- **修复方向**：以 \"difficulty threshold across encoder architectures\" 和 \"regularizer interpretation of classification supervision\" 为主线重新 frame，DAPT 验证降为支撑。\n\n**N3** [critical, 共识] **TF-IDF 基线严重削弱 discourse-level representation 价值主张**\n- TF-IDF LR 在 OOD DD 达 0.944，论文最佳 0.997，marginal gain 仅 5.3pp。论文自己承认无法区分 pragmatic features 和 lexical cues（Limitations）。关键缺失：TF-IDF per-prefix (K=1-5) 结果和 ActorAttack 结果均未报告，使 \"early detection advantage\" 和 \"discourse-level claim\" 均为 unsubstantiated。\n- **修复方向**：补充 TF-IDF 全 prefix + ActorAttack 结果；做 probing experiments 证明超越 lexical cues 的 discourse features。\n\n**N4** [critical, 共识] **\"Preliminary findings\" 定位与 long paper 格式矛盾**\n- Abstract、Introduction、Conclusion 三处使用 \"preliminary\"。自我降格信号表明作者对贡献充分性缺乏信心。但仅删除 \"preliminary\" 而不扩大实验规模会变成 overclaiming。\n- **修复方向**：同时移除 preliminary hedging 并扩大实验规模；或改投 Findings paper。\n\n**N5** [critical, 共识] **缺少与现有 multi-turn defense 的直接实验对比**\n- 讨论了 DeepContext/BIID/G-Guard/SafeDream 但未直接比较。vanilla DeBERTa（frozen, 1-layer BiGRU, 128 hidden）不能 represent DeepContext（fine-tuned BERT, 3-layer GRU, 2048 hidden）。\n- **修复方向**：复现 DeepContext 或在共同 benchmark 对比；或明确定位为 analysis paper（分析什么使泛化成为可能）而非 method paper（提出更好的方法）。\n\n**N6** [critical, 共识] **数据规模不足以支撑 statistical claims**\n- 500 训练 + 76-118 测试 + 3 seeds。MLM DD-Full std=0.115（seed 456 recall=0.64）。Evidence hierarchy 中多对 confidence intervals 重叠。FITD 无 discriminative power（vanilla 和 9-class 均 F1≥0.990）。\n- **修复方向**：至少 5 seeds（理想 10）；bootstrap 95% CI；paired bootstrap/permutation test。\n\n**N7** [critical, R2 提出 R1 升级] **缺少 ACL ARR Responsible NLP Research Checklist**\n- 论文涉及 jailbreak attack 技术，未包含 ARR 要求的 Responsible NLP Research Checklist。存在 desk reject 风险。\n- **修复方向**：按 ARR 要求填写完整 checklist。\n\n### Should-Fix（11 项 major/warning）\n\n**W1** [major, 共识] **Related Work 包含大量本文实验数据**。\"Domain-adaptive pretraining\" 和 \"Dataset artifacts\" 段落中引用本文 F1 数值，应移至 Results/Discussion。\n\n**W2** [major, 共识] **Abstract 数据过载**。~150 词中包含 12+ 数值。保留 2-3 headline numbers，其余用定性描述。\n\n**W3** [major, 共识] **ActorAttack 样本量未在 Section 4.1 中说明**。FITD 和 DD 标注了 80 条，ActorAttack 数量缺失。\n\n**W4** [major, 共识] **Introduction 第四段结果段过于冗长**。~200 词 15+ 数值，读者尚未了解方法细节无法消化。\n\n**W5** [major, R1 提出] **BiGRU + frozen encoder 设计缺乏 justification**。frozen 设计可能低估某些 variants 潜力。Mean pooling single-seed 与 3-seed BiGRU 不可比。\n\n**W6** [major, 部分分歧] **LLM-as-judge baseline 仅 zero-shot**。R1 认为不公平，R2 认为目的合理但同意应补 few-shot。共识：至少测试 few-shot 设置。\n\n**W7** [major, 共识] **策略标注质量验证不足**。κ=0.78 基于 n=50 单标注员。需至少两个独立标注员 + human-human κ + n≥100。\n\n**W8** [warning, 共识] **Topic classification 存在 shortcut learning confound**。5-class topic labels 与 benign 数据生成的 5 个 topic 完全一致（method.tex:50 vs appendix.tex:139），topic classifier 可能学习了 jailbreak vs benign 的 shortcut 而非论文声称的 \"misaligned supervision destabilizes representations\"。\n\n**W9** [warning, 共识] **DeBERTa-v3 vs RoBERTa 的 capacity confound 未控制**。DeBERTa-v3-base (184M) vs RoBERTa-base (125M) 在参数量和训练数据上不同，\"pretraining method determines the difficulty threshold\" claim 可能混淆 capacity effect。\n\n**W10** [warning, R2 提出] **页数可能超限**。需确认 Conclusion 在第 8 页内结束。\n\n**W11** [warning, R2 提出] **Figure 3 (figure*) 浮动位置可能异常**。\n\n### Minor Issues\n\n- **术语不一致**: \"domain exposure\" / \"domain adaptation\" / \"continued pretraining\" / \"domain-adaptive pretraining\" 混用，应统一。\n- **数据重复**: 0.31±0.03 → 0.91±0.12 在 Abstract/Introduction/Related Work/Experiments/Conclusion 出现至少 6 次。\n- **α=0.3 loss weight 未 justify**: 未提供选择理由或 sensitivity analysis。\n- **引用格式**: austin1962 年份、chao2023pair 年份、han2024wildguard 作者可能有误。\n- **FITD K=3/K=5 缺失**: Table 6 中为 \"--\"，原因未说明（可能因 FITD 对话仅 2-3 轮）。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上完全一致 [AGREE]：\n1. **Single-LLM confound + TF-IDF 0.944** 是最严重的威胁——整个 evidence hierarchy 可能是 stylistic artifact\n2. **Novelty 有限**——headline result 是 DAPT 在新领域的验证；更精细发现统计支撑不足\n3. **\"Preliminary\" framing + 数据规模不足** 构成恶性循环：移除 preliminary 需要更多证据，但当前证据确实只支撑 preliminary 结论\n4. **缺失 baseline 直接对比** 使 method-level 贡献无法评估\n5. **消融设计本身有方法论价值**（七变体隔离、scrambled regularizer、difficulty threshold）\n\n## Reviewer Divergence\n\n仅有两个局部分歧，均已在交叉回应中趋于共识：\n\n1. **LLM-as-judge 公平性** (R1-W3): R1 认为仅 zero-shot 不公平，R2 认为目的合理但同意应补 few-shot。**共识**：至少补充 few-shot 评估。\n\n2. **Scrambled labels 替代解释** (R1-Q2): R1 提出 \"小数据集上任何分类 head 的 gradient signal 都够\"，R2 反驳 topic classification 同有分类 head 但表现差，排除了该假设。R1 未进一步反驳。**共识**：R2 的 rebuttal 成立，但 topic classification 本身存在 shortcut confound（CROSS-Q5）。\n\n---\n\n## Questions（需作者澄清）\n\n**Q1** [最高优先级] OOD test data (DD, FITD, ActorAttack) 是否也由 Qwen3-8B 生成？如果是，\"cross-attack generalization\" 实为 \"cross-template generalization within same LLM distribution\"。\n\n**Q2** TF-IDF 在 ActorAttack 上的 F1？这决定了 discourse-level claim 是否站得住脚。\n\n**Q3** TF-IDF 在 K=1, 2, 3, 5 各 prefix 上的表现？这决定了 \"early detection advantage\" 是否成立。\n\n**Q4** ActorAttack OOD 数据的具体样本数量？\n\n**Q5** \"Pragmatic features (hedging, escalation markers, topic-shifting patterns)\" 的直接 probing 证据？\n\n**Q6** DeBERTa-v3 vs RoBERTa 的差异是 pretraining method (RTD vs MLM) 还是 model capacity (184M vs 125M) 导致？\n\n---\n\n## Missing References\n\n**高优先级（交叉共识）**:\n- Persuasion for Good (Wang et al., 2019) — dialogue persuasion detection 先驱\n- SmoothLLM (Robey et al., 2024) — perturbation-based defense，直接相关\n- TAP (Mehrotra et al., 2024) — multi-turn automated attack\n- MHJ dataset (Li et al., 2024) — 人类生成的 multi-turn jailbreak（已 cite 但未用作评估）\n- JailbreakBench (Chao et al., 2024) — 标准化 jailbreak 评估\n- HarmBench (Mazeika et al., 2024) — 多维度安全评估 benchmark\n\n**中等优先级**:\n- AutoDAN (Liu et al., 2024) — 自动化攻击生成\n- Circuit Breakers (Zou et al., 2024) — representation engineering defense\n- GradSafe (Xie et al., 2024) — gradient-based jailbreak detection\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。项目配置中未启用 `external_review.paperreview_ai`。\n\n---\n\n## Overall Assessment\n\n**Overall: Weak Reject (2.5/5)**\n**Confidence: 4/5**\n\n两位 Reviewer 独立给出相同评分（2.5/5），交叉回应后维持。\n\n论文的核心价值在于消融实验设计（七变体隔离 + scrambled regularizer 发现 + cross-encoder difficulty threshold），这些在方法论上有贡献。但以下问题阻碍接收：\n\n1. **Single-LLM confound 未解决**：所有数据可能共享 Qwen3-8B 分布，TF-IDF 0.944 是最直接的 red flag。\n2. **Novelty 定位混乱**：headline result 是已知结论的领域验证，更精细发现的统计基础不足。\n3. **\"Preliminary\" 与 long paper 矛盾**：数据规模（500 训练 + 76-118 测试 + 3 seeds）确实只能支撑 preliminary 结论。\n4. **缺失关键数据点**：TF-IDF per-prefix、TF-IDF on ActorAttack、probing experiments、direct baseline comparison——任何一项补充都可能显著改变论文的可信度。\n\n**建议路径**：\n- **Path A（扩展后重投 long paper）**：补充不同 LLM/人类数据评估 + probing experiments + TF-IDF 全结果 + 5+ seeds + 明确 analysis paper 定位 → 有机会达到 borderline/weak accept\n- **Path B（当前规模投 Findings）**：移除 preliminary hedging + 以 difficulty threshold / regularizer interpretation 为主线 + 补充缺失数据点 → 作为 Findings paper 有竞争力\n\n当前版本不适合 EMNLP 2026 long paper 接收。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 数据过载：12+ 数值在 ~150 词中。保留 ~60pp gap bridging 和 ActorAttack cross-encoder collapse 两个 headline numbers，其余定性描述。\n- \"preliminary findings\" 为首句核心限定词，在 peer review 中致命。\n\n### Introduction\n- 第 1-3 段叙事线清晰（问题 → 现有不足 → gap）。\n- 第 4 段是 ~200 词的 results dump，应压缩为 2-3 句 headline takeaway。\n- Contributions 列表合理（3 条），但每条过于密集。\n\n### Related Work\n- 覆盖面合理（attacks, defenses, production systems, discourse, DAPT, artifacts）。\n- 3 处包含本文实验数据，违反 Related Work 定位功能。\n- 缺失 Persuasion for Good、SmoothLLM、TAP 等引用。\n\n### Method\n- 七变体设计清晰且各有 ablation 目标。\n- Topic classification 的 5-class 与 benign 生成 topic 一致，存在 shortcut confound。\n- α=0.3 loss weight 未 justify。\n- Frozen encoder 选择需更多 justification。\n\n### Experiments\n- Evidence hierarchy 可视化清晰，但 confidence intervals 缺失。\n- TF-IDF per-prefix 和 ActorAttack 结果缺失是最大漏洞。\n- ActorAttack 样本量未说明。\n- Perturbation analysis 的 three-layer pattern 在 ActorAttack 上不成立，不应作为贡献点。\n- Cross-encoder 分析有价值但 capacity confound 未控制。\n\n### Conclusion + Limitations\n- Limitations 诚实全面，但 single-LLM confound 未被列为 limitation。\n- \"Preliminary\" 在 Conclusion 中再次出现。\n\n### Appendix\n- LLM-as-judge 仅 zero-shot，应补 few-shot。\n- FITD K=3/K=5 缺失未解释。\n- Reproducibility details 完整但生成 prompt 未直接披露。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject",
    "report": "# 圆桌审稿报告（Round 2）\n\n**论文**: What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**审稿模式**: 重新审稿（fresh review，无 Round 1 记忆）\n**Reviewer 编排**: 2 人（EMNLP 标准）\n- Reviewer 1: 方法严谨性 + 实验设计 + 统计有效性\n- Reviewer 2: 新颖性 + Related Work 定位 + 写作质量 + 完整性\n\n---\n\n## Summary\n\n本文提出 DisPeD，一个两阶段框架（Stage-1 encoder adaptation + Stage-2 BiGRU aggregation），通过 7 个受控 Stage-1 变体系统分解跨攻击泛化的机制。核心发现：(1) 在 DeBERTa-v3 上 continued pretraining（MLM）桥接约 60pp OOD gap；(2) 分类监督（9-class/binary/scrambled 三种分类变体检测 F1 相同）作为 representation regularizer 而非 semantic classifier 起作用；(3) RoBERTa 交叉验证显示 encoder pretraining method 决定 domain adaptation 变为必要的难度阈值。实验在 Qwen3-8B 合成数据上覆盖 4 个攻击家族（Crescendo IID + FITD/DD/ActorAttack OOD），规模为 500 训练 + 76-118 测试对话。\n\n---\n\n## Strengths\n\n**S1** [共识] **消融实验设计系统严谨**。七个 Stage-1 变体各自隔离一个因素（domain exposure, classification supervision, label quality, label granularity, domain specificity, misaligned supervision），共享相同 Stage-2 pipeline，使对比公平。这是论文最突出的方法论贡献。\n\n**S2** [共识] **Scrambled labels 发现有洞察力**。Scrambled = binary = 9-class 在检测 F1 上完全相同（0.997±0.005, Table 2），证明分类目标作为 representation regularizer 而非 semantic classifier 起作用。这超越了简单的 domain adaptation 验证。\n\n**S3** [共识] **Cross-encoder \"difficulty threshold\" 概念有价值**。DeBERTa-v3 vanilla 在 DD 上坍塌（F1=0.312）而 RoBERTa vanilla 不坍塌（0.981），但 RoBERTa 在结构更复杂的 ActorAttack 上坍塌（0.466），揭示 encoder pretraining method 决定了 adaptation 变为必要的难度阈值（Table 4）。\n\n**S4** [共识] **诚实的 Limitations section**。论文坦率承认 TF-IDF 基线问题、strategy prediction 不泛化（OOD κ=0.126）、数据规模限制、single-seed mean pooling 等。这种 intellectual honesty 在 ML safety 论文中罕见。\n\n**S5** [共识] **可复现性优秀**。完整超参数（Appendix E）、总计算成本 <4 GPU-hours、承诺开源。\n\n---\n\n## Weaknesses（按 severity 排序）\n\n### Must-Fix（7 项 critical，影响接收决定）\n\n**N1** [critical, 共识] **单模型（Qwen3-8B）生成全部数据造成系统性 confound**\n- Qwen3-8B 同时用于生成训练数据、策略标注、OOD 测试数据和对抗性 paraphrase。TF-IDF LR 在 OOD DD 上 F1=0.944（Table 1），强烈暗示模型利用的是 Qwen3-8B stylistic fingerprint 而非 discourse-level features。论文在 Limitations 中讨论了 lexical separability 但完全未提及 single-LLM confound。\n- **影响**：如果 OOD gap 的桥接主要来自学习生成模型的 stylistic artifacts，则整个 evidence hierarchy 可能是 artifact-driven。这是论文最核心 claim 的替代解释。\n- **修复方向**：(1) 用不同 LLM 生成部分 OOD 数据；(2) 用人类编写数据（MHJ dataset）评估；(3) 做 probing 实验区分 lexical 和 discourse-level features。\n\n**N2** [critical, 共识] **核心贡献新颖性不足**\n- 核心发现（continued pretraining bridges ~60pp OOD gap）是 Gururangan et al. (2020) \"Don't Stop Pretraining\" 在 jailbreak detection 的直接验证。更精细的 decomposition（scrambled regularizer, difficulty threshold）有趣，但在 3 seeds + 500 对话规模上统计支撑不足。\n- **影响**：ACL ARR Excitement 维度要求推进领域认知。当前 headline result 在新领域验证已知结论，更适合 Findings paper 或 short paper。\n- **修复方向**：以 \"difficulty threshold across encoder architectures\" 和 \"regularizer interpretation of classification supervision\" 为主线重新 frame，DAPT 验证降为支撑。\n\n**N3** [critical, 共识] **TF-IDF 基线严重削弱 discourse-level representation 价值主张**\n- TF-IDF LR 在 OOD DD 达 0.944，论文最佳 0.997，marginal gain 仅 5.3pp。论文自己承认无法区分 pragmatic features 和 lexical cues（Limitations）。关键缺失：TF-IDF per-prefix (K=1-5) 结果和 ActorAttack 结果均未报告，使 \"early detection advantage\" 和 \"discourse-level claim\" 均为 unsubstantiated。\n- **修复方向**：补充 TF-IDF 全 prefix + ActorAttack 结果；做 probing experiments 证明超越 lexical cues 的 discourse features。\n\n**N4** [critical, 共识] **\"Preliminary findings\" 定位与 long paper 格式矛盾**\n- Abstract、Introduction、Conclusion 三处使用 \"preliminary\"。自我降格信号表明作者对贡献充分性缺乏信心。但仅删除 \"preliminary\" 而不扩大实验规模会变成 overclaiming。\n- **修复方向**：同时移除 preliminary hedging 并扩大实验规模；或改投 Findings paper。\n\n**N5** [critical, 共识] **缺少与现有 multi-turn defense 的直接实验对比**\n- 讨论了 DeepContext/BIID/G-Guard/SafeDream 但未直接比较。vanilla DeBERTa（frozen, 1-layer BiGRU, 128 hidden）不能 represent DeepContext（fine-tuned BERT, 3-layer GRU, 2048 hidden）。\n- **修复方向**：复现 DeepContext 或在共同 benchmark 对比；或明确定位为 analysis paper（分析什么使泛化成为可能）而非 method paper（提出更好的方法）。\n\n**N6** [critical, 共识] **数据规模不足以支撑 statistical claims**\n- 500 训练 + 76-118 测试 + 3 seeds。MLM DD-Full std=0.115（seed 456 recall=0.64）。Evidence hierarchy 中多对 confidence intervals 重叠。FITD 无 discriminative power（vanilla 和 9-class 均 F1≥0.990）。\n- **修复方向**：至少 5 seeds（理想 10）；bootstrap 95% CI；paired bootstrap/permutation test。\n\n**N7** [critical, R2 提出 R1 升级] **缺少 ACL ARR Responsible NLP Research Checklist**\n- 论文涉及 jailbreak attack 技术，未包含 ARR 要求的 Responsible NLP Research Checklist。存在 desk reject 风险。\n- **修复方向**：按 ARR 要求填写完整 checklist。\n\n### Should-Fix（11 项 major/warning）\n\n**W1** [major, 共识] **Related Work 包含大量本文实验数据**。\"Domain-adaptive pretraining\" 和 \"Dataset artifacts\" 段落中引用本文 F1 数值，应移至 Results/Discussion。\n\n**W2** [major, 共识] **Abstract 数据过载**。~150 词中包含 12+ 数值。保留 2-3 headline numbers，其余用定性描述。\n\n**W3** [major, 共识] **ActorAttack 样本量未在 Section 4.1 中说明**。FITD 和 DD 标注了 80 条，ActorAttack 数量缺失。\n\n**W4** [major, 共识] **Introduction 第四段结果段过于冗长**。~200 词 15+ 数值，读者尚未了解方法细节无法消化。\n\n**W5** [major, R1 提出] **BiGRU + frozen encoder 设计缺乏 justification**。frozen 设计可能低估某些 variants 潜力。Mean pooling single-seed 与 3-seed BiGRU 不可比。\n\n**W6** [major, 部分分歧] **LLM-as-judge baseline 仅 zero-shot**。R1 认为不公平，R2 认为目的合理但同意应补 few-shot。共识：至少测试 few-shot 设置。\n\n**W7** [major, 共识] **策略标注质量验证不足**。κ=0.78 基于 n=50 单标注员。需至少两个独立标注员 + human-human κ + n≥100。\n\n**W8** [warning, 共识] **Topic classification 存在 shortcut learning confound**。5-class topic labels 与 benign 数据生成的 5 个 topic 完全一致（method.tex:50 vs appendix.tex:139），topic classifier 可能学习了 jailbreak vs benign 的 shortcut 而非论文声称的 \"misaligned supervision destabilizes representations\"。\n\n**W9** [warning, 共识] **DeBERTa-v3 vs RoBERTa 的 capacity confound 未控制**。DeBERTa-v3-base (184M) vs RoBERTa-base (125M) 在参数量和训练数据上不同，\"pretraining method determines the difficulty threshold\" claim 可能混淆 capacity effect。\n\n**W10** [warning, R2 提出] **页数可能超限**。需确认 Conclusion 在第 8 页内结束。\n\n**W11** [warning, R2 提出] **Figure 3 (figure*) 浮动位置可能异常**。\n\n### Minor Issues\n\n- **术语不一致**: \"domain exposure\" / \"domain adaptation\" / \"continued pretraining\" / \"domain-adaptive pretraining\" 混用，应统一。\n- **数据重复**: 0.31±0.03 → 0.91±0.12 在 Abstract/Introduction/Related Work/Experiments/Conclusion 出现至少 6 次。\n- **α=0.3 loss weight 未 justify**: 未提供选择理由或 sensitivity analysis。\n- **引用格式**: austin1962 年份、chao2023pair 年份、han2024wildguard 作者可能有误。\n- **FITD K=3/K=5 缺失**: Table 6 中为 \"--\"，原因未说明（可能因 FITD 对话仅 2-3 轮）。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上完全一致 [AGREE]：\n1. **Single-LLM confound + TF-IDF 0.944** 是最严重的威胁——整个 evidence hierarchy 可能是 stylistic artifact\n2. **Novelty 有限**——headline result 是 DAPT 在新领域的验证；更精细发现统计支撑不足\n3. **\"Preliminary\" framing + 数据规模不足** 构成恶性循环：移除 preliminary 需要更多证据，但当前证据确实只支撑 preliminary 结论\n4. **缺失 baseline 直接对比** 使 method-level 贡献无法评估\n5. **消融设计本身有方法论价值**（七变体隔离、scrambled regularizer、difficulty threshold）\n\n## Reviewer Divergence\n\n仅有两个局部分歧，均已在交叉回应中趋于共识：\n\n1. **LLM-as-judge 公平性** (R1-W3): R1 认为仅 zero-shot 不公平，R2 认为目的合理但同意应补 few-shot。**共识**：至少补充 few-shot 评估。\n\n2. **Scrambled labels 替代解释** (R1-Q2): R1 提出 \"小数据集上任何分类 head 的 gradient signal 都够\"，R2 反驳 topic classification 同有分类 head 但表现差，排除了该假设。R1 未进一步反驳。**共识**：R2 的 rebuttal 成立，但 topic classification 本身存在 shortcut confound（CROSS-Q5）。\n\n---\n\n## Questions（需作者澄清）\n\n**Q1** [最高优先级] OOD test data (DD, FITD, ActorAttack) 是否也由 Qwen3-8B 生成？如果是，\"cross-attack generalization\" 实为 \"cross-template generalization within same LLM distribution\"。\n\n**Q2** TF-IDF 在 ActorAttack 上的 F1？这决定了 discourse-level claim 是否站得住脚。\n\n**Q3** TF-IDF 在 K=1, 2, 3, 5 各 prefix 上的表现？这决定了 \"early detection advantage\" 是否成立。\n\n**Q4** ActorAttack OOD 数据的具体样本数量？\n\n**Q5** \"Pragmatic features (hedging, escalation markers, topic-shifting patterns)\" 的直接 probing 证据？\n\n**Q6** DeBERTa-v3 vs RoBERTa 的差异是 pretraining method (RTD vs MLM) 还是 model capacity (184M vs 125M) 导致？\n\n---\n\n## Missing References\n\n**高优先级（交叉共识）**:\n- Persuasion for Good (Wang et al., 2019) — dialogue persuasion detection 先驱\n- SmoothLLM (Robey et al., 2024) — perturbation-based defense，直接相关\n- TAP (Mehrotra et al., 2024) — multi-turn automated attack\n- MHJ dataset (Li et al., 2024) — 人类生成的 multi-turn jailbreak（已 cite 但未用作评估）\n- JailbreakBench (Chao et al., 2024) — 标准化 jailbreak 评估\n- HarmBench (Mazeika et al., 2024) — 多维度安全评估 benchmark\n\n**中等优先级**:\n- AutoDAN (Liu et al., 2024) — 自动化攻击生成\n- Circuit Breakers (Zou et al., 2024) — representation engineering defense\n- GradSafe (Xie et al., 2024) — gradient-based jailbreak detection\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。项目配置中未启用 `external_review.paperreview_ai`。\n\n---\n\n## Overall Assessment\n\n**Overall: Weak Reject (2.5/5)**\n**Confidence: 4/5**\n\n两位 Reviewer 独立给出相同评分（2.5/5），交叉回应后维持。\n\n论文的核心价值在于消融实验设计（七变体隔离 + scrambled regularizer 发现 + cross-encoder difficulty threshold），这些在方法论上有贡献。但以下问题阻碍接收：\n\n1. **Single-LLM confound 未解决**：所有数据可能共享 Qwen3-8B 分布，TF-IDF 0.944 是最直接的 red flag。\n2. **Novelty 定位混乱**：headline result 是已知结论的领域验证，更精细发现的统计基础不足。\n3. **\"Preliminary\" 与 long paper 矛盾**：数据规模（500 训练 + 76-118 测试 + 3 seeds）确实只能支撑 preliminary 结论。\n4. **缺失关键数据点**：TF-IDF per-prefix、TF-IDF on ActorAttack、probing experiments、direct baseline comparison——任何一项补充都可能显著改变论文的可信度。\n\n**建议路径**：\n- **Path A（扩展后重投 long paper）**：补充不同 LLM/人类数据评估 + probing experiments + TF-IDF 全结果 + 5+ seeds + 明确 analysis paper 定位 → 有机会达到 borderline/weak accept\n- **Path B（当前规模投 Findings）**：移除 preliminary hedging + 以 difficulty threshold / regularizer interpretation 为主线 + 补充缺失数据点 → 作为 Findings paper 有竞争力\n\n当前版本不适合 EMNLP 2026 long paper 接收。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 数据过载：12+ 数值在 ~150 词中。保留 ~60pp gap bridging 和 ActorAttack cross-encoder collapse 两个 headline numbers，其余定性描述。\n- \"preliminary findings\" 为首句核心限定词，在 peer review 中致命。\n\n### Introduction\n- 第 1-3 段叙事线清晰（问题 → 现有不足 → gap）。\n- 第 4 段是 ~200 词的 results dump，应压缩为 2-3 句 headline takeaway。\n- Contributions 列表合理（3 条），但每条过于密集。\n\n### Related Work\n- 覆盖面合理（attacks, defenses, production systems, discourse, DAPT, artifacts）。\n- 3 处包含本文实验数据，违反 Related Work 定位功能。\n- 缺失 Persuasion for Good、SmoothLLM、TAP 等引用。\n\n### Method\n- 七变体设计清晰且各有 ablation 目标。\n- Topic classification 的 5-class 与 benign 生成 topic 一致，存在 shortcut confound。\n- α=0.3 loss weight 未 justify。\n- Frozen encoder 选择需更多 justification。\n\n### Experiments\n- Evidence hierarchy 可视化清晰，但 confidence intervals 缺失。\n- TF-IDF per-prefix 和 ActorAttack 结果缺失是最大漏洞。\n- ActorAttack 样本量未说明。\n- Perturbation analysis 的 three-layer pattern 在 ActorAttack 上不成立，不应作为贡献点。\n- Cross-encoder 分析有价值但 capacity confound 未控制。\n\n### Conclusion + Limitations\n- Limitations 诚实全面，但 single-LLM confound 未被列为 limitation。\n- \"Preliminary\" 在 Conclusion 中再次出现。\n\n### Appendix\n- LLM-as-judge 仅 zero-shot，应补 few-shot。\n- FITD K=3/K=5 缺失未解释。\n- Reproducibility details 完整但生成 prompt 未直接披露。"
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-18T16:07:51.443739+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a90fe0dde422576f214f12233cfe27a3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4267
}
```

</details>

---


### Assistant

_source line 174 · 2026-05-18T16:08:00.321283+00:00_

审稿报告已投递。

**审稿完成总结：**

- **Overall: Weak Reject (2.5/5)**，两位 Reviewer 独立评分一致
- **7 项 critical issues**：单模型 confound、novelty 不足、TF-IDF 削弱核心叙事、preliminary framing 矛盾、缺 baseline 对比、数据规模不足、缺 ARR checklist
- **11 项 should-fix**：Related Work 含自身数据、Abstract/Introduction 数据过载、ActorAttack 样本量缺失、frozen encoder justification、LLM-as-judge 公平性、标注质量等
- **共识最强的 red flag**：所有数据由同一 LLM 生成 + TF-IDF 0.944，使整个 evidence hierarchy 的 discourse-level 解释受到根本质疑
- **建议路径**：扩展后重投 long paper（补数据源 + probing + seeds），或以当前规模投 Findings paper

Issue Tracker 已同步更新至 `artifacts/review_issues.yaml`（17 项 Round 1 历史 + 20 项 Round 2 新 issues）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 17

## Round 17

2 recorded events


### User

_source line 175 · 2026-05-18T16:08:01.829853+00:00_

[Reviewer 2 审稿结果]:
已汇报给 Director。逐条回应摘要：

- **Must-Fix**: 3/3 同意 R1（N1 single-LLM confound、N2 缺少直接对比、N3 数据规模不足），并为 N1 补充了 topic classification shortcut 证据
- **Should-Fix**: 4/5 同意（W1-W2, W4-W5），对 W3 (LLM-as-judge 不公平) 部分反驳——zero-shot 失败可能确实反映 content-level reasoning 的局限，但同意应补 few-shot 对比
- **Questions**: 4/5 同意（Q1, Q3-Q5），对 Q2 (scrambled labels 替代解释) 反驳——topic classification 的差表现排除了 "任何分类 head 都够" 的假设
- **Missing References**: 4/5 同意，Latent Jailbreak 因为是 single-turn 与论文 scope 不符而反驳
- **新增共识**：R1-N1 (single-LLM confound) 是我 Round 1 未覆盖的最严重问题，应作为 rebuttal 最高优先级

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 176 · 2026-05-18T16:08:12.766887+00:00_

审稿报告已投递至 Research Director。

**圆桌审稿完成总结：**

- **Overall: Weak Reject (2.5/5)**，两位 Reviewer 独立评分一致，交叉回应后维持
- **7 项 critical issues**：single-LLM confound、novelty 不足、TF-IDF 削弱 discourse claim、preliminary framing 矛盾、缺失 baseline 对比、数据规模不足、缺 ARR checklist
- **11 项 should-fix**，涵盖写作（Abstract/Introduction 数据过载、Related Work 包含自身结果）、方法（frozen encoder justification、topic classification shortcut confound）、实验（TF-IDF per-prefix 缺失、标注质量验证不足）
- **Issue Tracker 已同步**：17 项 Round 1 历史 issue + 22 项 Round 2 新 issue，全部写入 `review_issues.yaml`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 18

## Round 18

90 recorded events


### User

_source line 177 · 2026-05-18T17:57:22.631673+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: persuasion_turn_jailbreak_detect
- 论文路径: projects/persuasion_turn_jailbreak_detect/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: LLM Security
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-18T17:57:31.529052+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-18T17:57:31.530038+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-18T17:57:36.911440+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "8"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-18T17:57:36.911917+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-18T17:57:42.993426+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---


### Tool call

_source line 183 · 2026-05-18T17:57:43.194398+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
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

_source line 184 · 2026-05-18T17:57:43.345346+00:00_

{"result":"# 项目 persuasion_turn_jailbreak_detect 概况\n\n## 实验状态 (60 个)\n\n- **plan_016_sentiment_control**: PREPARING (failed) — \n- **plan_012_gpt55_judge**: DONE (success) — \n- **plan_015_dd_eval**: DONE (success) — \n- **plan_006_cross_attack_clean**: DONE (success) — \n- **plan_004_perturbation_eval**: DONE (success) — \n- **plan_013_none_collapse**: DONE (success) — \n- **plan_012_llm_judge_qwen**: DONE (success) — \n- **plan_002_clean_training**: DONE (negative) — \n- **plan_003_scrambled_ablation**: DONE (negative) — \n- **cross_attack_baseline**: DONE (negative) — \n- **plan_008_strategy_transition**: DONE (success) — \n- **plan_007_tfidf_fitd_dd**: DONE (success) — \n- **plan_005_multi_attack_gen**: DONE (success) — \n- **phase_b_full**: DONE (success) — \n- **pilot_phase_b**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp3_probing: 9-class persuasion fine-tuned DeBERTa encodes richer discourse structure (turn position, escalation level, persuasion presence) than vanilla/MLM variants, as measured by linear probing accuracy and CKA divergence（准备中）\n- exp1_roberta_vanilla: Off-the-shelf RoBERTa-base without any fine-tuning will show poor DD OOD performance, matching DeBERTa vanilla baseline pattern and confirming encoder-agnostic findings（准备中）\n- exp1_roberta_mlm: RoBERTa-base with MLM-only continued pretraining will show intermediate DD OOD performance between vanilla and 9-class, matching DeBERTa's evidence hierarchy pattern（准备中）\n- exp1_roberta_9class: RoBERTa-base with 9-class persuasion multi-task fine-tuning will reproduce the DeBERTa evidence hierarchy (9-class >> vanilla), proving findings are encoder-agnostic（准备中）\n- plan_003_scrambled_retrain（准备中）\n- plan_018_eval_seed456（准备中）\n- plan_018_eval_seed123（准备中）\n- plan_018_wiki_mlm_seed456（准备中）\n- plan_018_wiki_mlm_seed123（准备中）\n- plan_017_eval_seed456（准备中）\n- …另有 10 项\n\n## 近期结论\n- **exp9_bootstrap_ci** (success): BCa bootstrap
…[truncated 1376 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 351
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-18T17:57:43.345830+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-18T17:57:48.975140+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 187 · 2026-05-18T17:57:50.886100+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 188 · 2026-05-18T17:57:51.287710+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\graphicspath{{../../}}
12	\usepackage{amsmath}
13	\usepackage{booktabs}
14	\usepackage{enumitem}
15	\usepackage{amssymb}
16	\usepackage{multirow}
17	
18	\title{What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	
27	\input{introduction}
28	
29	\input{related_work}
30	
31	\input{method}
32	
33	\input{experiments}
34	
35	\input{conclusion}
36	
37	\bibliography{references}
38	
39	\input{appendix}
40	
41	\input{checklist}
42	
43	\end{document}
44	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 189 · 2026-05-18T17:57:51.588868+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "literature_map.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect",
    "file": "literature_map.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 190 · 2026-05-18T17:57:57.974222+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

I've found comprehensive information about EMNLP 2026's call for papers submission guidelines and author instructions. Here's what the search results reveal:

## Key Submission Guidelines

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## Important Dates

The ARR submission deadline for l
…[truncated 1812 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "elapsed_ms": 8999
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-18T17:57:58.025167+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/literature_map.yaml\", \"content\": \"# Literature Map — persuasion_turn_jailbreak_detect\\n# Generated: 2026-05-17 by Paper Agent\\n# Target: EMNLP 2026 Main (ARR May cycle)\\n# Total entries: 39 (across 8 categories + technical foundation)\\n# All entries WebSearch-verified\\n\\nmetadata:\\n  project: persuasion_turn_jailbreak_detect\\n  target_venue: EMNLP 2026\\n  last_updated: \\\"2026-05-17\\\"\\n  total_papers: 39\\n  categories:\\n    - production_safety_systems\\n    - multi_turn_defenses\\n    - discourse_analysis\\n    - computational_persuasion\\n    - jailbreak_attacks_taxonomies\\n    - red_teaming\\n    - annotation_artifacts\\n    - adaptive_attacks\\n    - technical_foundation\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Production Multi-Turn Safety Systems (5 papers)\\n  # ============================================================\\n\\n  - bibtex_key: inan2023llamaguard\\n    title: \\\"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\\\"\\n    authors: \\\"Inan et al.\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2023\\n    arxiv: \\\"2312.06674\\\"\\n    category: production_safety_systems\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Foundational production safety classifier. Per-turn input/output guard\\n      that lacks multi-turn context modeling. DisPeD addresses this gap by\\n      modeling conversation-level persuasion trajectories.\\n\\n  - bibtex_key: metallamaguard3_2024\\n    title: \\\"Llama Guard 3\\\"\\n    authors: \\\"Meta AI\\\"\\n    venue: \\\"Meta AI (released with Llama 3.1)\\\"\\n    year: 2024\\n    category: production_safety_systems\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Latest iteration of Llama Guard with multili
…[truncated 3744 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6436
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-18T17:58:09.417719+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-18T17:58:10.521965+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "elapsed_ms": 1104
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-18T17:58:10.572564+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May submission format page limits long paper short paper requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 May submission format page limits long paper short paper requirements"
  }
}
```

</details>

---


### Tool call

_source line 195 · 2026-05-18T17:58:10.924120+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 196 · 2026-05-18T17:58:16.492197+00:00_

Web search results for query: "ACL Rolling Review 2026 May submission format page limits long paper short paper requirements"

Links: [{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here are the ACL Rolling Review submission format requirements:

## Page Limits

Long papers must follow a page limit of 8 pages for content, while short papers are limited to 4 pages, not including limitations and ethical considerations.

## Long Papers

Long papers may consist of up to 8 pages of content, plus unlimited pages for references and appendices. Upon acceptance, long papers will be given one additional page of content (up to 9 pages) in the proceedings so that reviewers' comments can be taken into account.

## Short Papers

Short papers may consist of up to four (4) pages of content, plus unlimited pages of references. A short paper is not a shortened long paper; instead short papers should 
…[truncated 559 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "elapsed_ms": 5919
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-18T17:58:16.494045+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/decisions.yaml\", \"content\": \"_next_id: 37\\ndecisions:\\n- id: D001\\n  date: 2026-05-17 16:09 UTC\\n  summary: 接受 DeBERTa F1=0.789 作为 baseline，停止数据 TF-IDF 迭代，reframe MVP 为 early detection\\n  rationale: 'DeBERTa F1=0.789 已在目标范围(0.70-0.85)。TF-IDF F1=0.924 高但不致命——论文 reframe:\\n    TF-IDF/vanilla 方法需完整对话才能分类，DisPeD 在 K=2-3 turns 即可通过 persuasion trajectory 早期检测。这完美对齐\\n    Bullwinkel et al. 的核心发现（早期 turns 表征为 benign）。数据迭代已耗 4 轮 6+ 小时，继续追 TF-IDF 阈值的 ROI\\n    为负。用 Crescendo oracle labels (intended_strategy) 替代 GPT 标注，节省 API 成本和时间。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-17 16:49 UTC\\n  summary: MVP PASS — early detection K=2 +10.8pp, K=3 +5.9pp 超过阈值；TF-IDF=1.0 标记为\\n    research 阶段优先解决项\\n  rationale: Treatment (persuasion-grounded DeBERTa → GRU) 在 K=2 时 F1=0.987 vs baseline\\n    0.879 (+10.8pp)，K=3 时 +5.9pp，均超过 MVP 阈值 +5pp。Full conversation F1 差距仅 +1.3pp 未达\\n    +2pp 阈值，但 early detection 是核心 claim 所在。TF-IDF=1.0 表明词汇 shortcut 仍存在，但 (1) 不影响\\n    treatment vs baseline 相对比较的有效性，(2) 可作为 paper motivation（lexical cues 偶然有效但可被攻击者规避，pragmatic\\n    patterns 不可规避），(3) research 阶段通过 adversarial perturbation 实验验证 robustness。\\n  related_experiments:\\n  - exp_id: pilot_phase_b\\n    role: pipeline_validation\\n    result: success (n=270, directionally positive but not statistically meaningful)\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-17 16:59 UTC\\n  summary: 进入 Research 阶段，framing 定位为 Pragmatic Evasion Asymmetry，experiment plan\\n    含 6 个 P0 实验\\n  rationale: MVP PASS (D002) 后按 post-mvp-kickoff 流程：paper_framing.md 将核心贡献从\\\"更好的检测器\\\"升级为\\\"语用逃逸不对称性原则的首个实证验证\\\"（源自\\n    Human Review Note），experiment_plan.yaml 优先解决 TF-IDF=1.0 数据质量阻塞。Dream full review\\n    已发起，等回调后审批 P0。\\n  related_experiments:\\n  - exp_id: phase_b_full\\n    role: motivation\\n    result: K=2 +10.8pp but 
…[truncated 1467 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5569
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-18T17:58:21.713862+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-18T17:58:22.065988+00:00_

1	% abstract.tex — D034 analysis reframe
2	\begin{abstract}
3	Multi-turn jailbreak attacks distribute adversarial intent across seemingly benign conversational turns, evading per-turn safety filters.
4	What representation properties enable detection that generalizes across attack families?
5	We address this through a controlled ablation: seven encoder variants on DeBERTa-v3 and three on RoBERTa, evaluated across four attack families (Crescendo, FITD, Deceptive Delight, ActorAttack), decompose the roles of domain exposure, classification supervision, label quality, and domain specificity.
6	Three findings emerge.
7	First, domain exposure via domain-adaptive continued pretraining (DAPT) on jailbreak text is the primary mechanism, bridging $\sim$60 percentage points (pp) of the out-of-distribution (OOD) generalization gap without any classification labels; lexical baselines collapse on structurally complex attacks (TF-IDF F1\,=\,0.961 on Deceptive Delight $\to$ 0.261 on ActorAttack) while domain-adapted models maintain F1\,$\geq$\,0.89.
8	Second, encoder pretraining method determines the difficulty threshold at which DAPT becomes critical: RoBERTa succeeds on structurally simple attacks but collapses on multi-persona ActorAttack (F1\,=\,0.981 $\to$ 0.466).
9	Third, classification supervision functions as a representational regularizer rather than a meaningful strategy classifier, providing cross-seed stability on synthetic OOD evaluations (variance reduced 4--20$\times$) regardless of label correctness.
10	The domain-adapted vs.\ vanilla gap holds on human-written ToxicChat jailbreaks (macro F1: 0.596--0.837 vs.\ 0.413), confirming that DAPT on synthetic text transfers beyond LLM-generated data. Full multi-turn validation on human data remains a direction for future work.
11	\end{abstract}
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-18T17:58:22.116808+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-18T17:58:22.268081+00:00_

1	% introduction.tex — expanded for 8-page target
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Multi-turn jailbreak attacks pose a qualitatively different threat to large language model (LLM) safety than their single-turn counterparts. Attacks such as Crescendo~\citep{russinovich2024crescendo}, Foot-in-the-Door (FITD)~\citep{fitd2024}, and Deceptive Delight~\citep{deceptivedelight2024} distribute adversarial intent across individually benign turns through rapport building, logical reframing, and incremental escalation. Persuasion is the common mechanism: \citet{zeng2024pap} catalogue 40 persuasion techniques across jailbreak families, and \citet{hagendorff2026reasoning} find identifiable strategies in 97\% of successful attacks. Individual attack turns occupy the same embedding region as benign text~\citep{bullwinkel2025repeng}, rendering per-turn safety filters fundamentally blind.
7	
8	Production classifiers such as Llama Guard~\citep{inan2023llamaguard}, WildGuard~\citep{han2024wildguard}, and ShieldGemma~\citep{zeng2024shieldgemma} operate on individual turns and cannot model manipulation trajectories across exchanges. Recent multi-turn defenses have begun to address conversation-level structure: DeepContext~\citep{deepcontext2026} combines fine-tuned BERT with a multi-layer GRU, BIID~\citep{tong2025biid} infers turn-level intentions, and G-Guard~\citep{gguard2025} applies graph neural networks. These systems achieve reasonable in-distribution performance but are evaluated on single attack families and do not assess cross-dataset OOD transfer. None systematically analyze \emph{why} some representations generalize while others fail. The open question is: \emph{what representation properties enable cross-attack generalization?}
9	
10	A vanilla DeBERTa encoder~\citep{he2021deberta} with temporal aggregation (replicating the frozen-encoder-plus-RNN approach of DeepContext~\citep{deepcontext2026}) collapses from F1\,=\,1.000 on in-distribution data to 
…[truncated 3225 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-18T17:58:23.071870+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-18T17:58:23.273075+00:00_

1	% related_work.tex — D024 compressed
2	
3	\section{Related Work}
4	\label{sec:related_work}
5	
6	\paragraph{Multi-turn jailbreak attacks.}
7	Multi-turn attacks distribute adversarial intent across individually benign turns. Crescendo~\citep{russinovich2024crescendo} implements gradual escalation, FITD~\citep{fitd2024} exploits commitment-consistency bias, Deceptive Delight~\citep{deceptivedelight2024} combines emotional manipulation with role assignment, ActorAttack~\citep{ren2024actorattack} uses multi-persona steering, PAIR~\citep{chao2023pair} and TAP~\citep{mehrotra2024tap} automate iterative refinement. \citet{wei2023jailbroken} provide a unifying taxonomy grounded in competing objectives and mismatched generalization. Standardized evaluation frameworks such as HarmBench~\citep{mazeika2024harmbench} and JailbreakBench~\citep{chao2024jailbreakbench} have enabled systematic comparison across attack types. Across these families, a shared reliance on persuasion dynamics~\citep{zeng2024pap,hagendorff2026reasoning,li2024mhj} distinguishes them from token-level attacks such as GCG~\citep{zou2023gcg}.
8	
9	\paragraph{Multi-turn defenses.}
10	Existing defenses model conversation-level structure but do not decompose what enables cross-attack generalization. DeepContext~\citep{deepcontext2026} combines fine-tuned BERT with a multi-layer GRU; however, its evaluation is limited to a single attack family and does not assess cross-dataset OOD transfer. BIID~\citep{tong2025biid} infers turn-level intentions, G-Guard~\citep{gguard2025} applies GNN classification, and SafeDream~\citep{safedream2026} predicts unsafe continuations. None of these systems evaluate generalization across attack families or analyze the mechanism that enables it. DisPeD's vanilla baseline represents the class of pretrained-encoder-plus-RNN approaches \emph{without} domain adaptation; it is not a direct proxy for DeepContext, which differs in encoder fine-tuning, model capacity, and loss function. Our 
…[truncated 3391 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-18T17:58:23.273435+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-18T17:58:23.374161+00:00_

1	% method.tex — D024 compressed
2	
3	\section{Method}
4	\label{sec:method}
5	
6	DisPeD is a two-stage framework for multi-turn jailbreak detection. Stage~1 performs domain-adaptive continued pretraining (DAPT) on jailbreak conversation text to adapt a turn-level encoder. Stage~2 aggregates turn representations for conversation-level binary classification. To systematically identify what enables cross-attack generalization, we design seven Stage-1 variants that decompose the contributions of domain exposure, classification supervision, label quality, label granularity, and domain specificity. Figure~\ref{fig:architecture} illustrates the pipeline.
7	
8	\begin{figure}[t]
9	\centering
10	\fbox{\parbox{0.9\columnwidth}{\centering\vspace{2em}\textit{Architecture diagram placeholder}\vspace{2em}}}
11	\caption{DisPeD architecture. Stage~1 adapts a DeBERTa encoder on jailbreak conversation text (seven variant objectives). Stage~2 aggregates frozen \texttt{[CLS]} embeddings via BiGRU for conversation-level jailbreak detection. Only user turns are processed.}
12	\label{fig:architecture}
13	\end{figure}
14	
15	\subsection{Problem Formulation}
16	
17	A conversation $C = \{u_1, a_1, \ldots, u_N, a_N\}$ alternates user turns $u_i$ and assistant responses $a_i$. Given a prefix of $K$ user turns, the model predicts $y \in \{0, 1\}$ (jailbreak vs.\ benign). We restrict input to user turns because adversarial intent resides in the attacker's messages. This formulation supports early detection from partial prefixes.
18	
19	\subsection{Stage 1: Turn-Level Encoder Adaptation}
20	\label{sec:stage1}
21	
22	Each user turn $u_i$ is encoded by DeBERTa-v3-base~\citep{he2021deberta}; the \texttt{[CLS]} embedding $h_i \in \mathbb{R}^d$ serves as the turn representation. Seven variants, summarized in Table~\ref{tab:variants}, share the same training data but differ in objective.
23	
24	\begin{table}[t]
25	\centering
26	\small
27	\caption{Stage-1 encoder variants. All operate on the same trainin
…[truncated 3957 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-18T17:58:27.088482+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-18T17:58:27.621317+00:00_

1	% experiments.tex — D024 compressed for 8-page limit
2	
3	\section{Experiments}
4	\label{sec:experiments}
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	\paragraph{Data.}
10	We train on 250 Crescendo~\citep{russinovich2024crescendo} jailbreak and 250 topic-anchored benign conversations generated via Qwen3-8B.
11	OOD evaluation uses 80 FITD~\citep{fitd2024}, 80 Deceptive Delight (DD)~\citep{deceptivedelight2024}, and 118 ActorAttack~\citep{ren2024actorattack} conversations with no overlap in attack templates.
12	The IID test set consists of 76 held-out Crescendo conversations; a paraphrased version (BERTScore 0.92, lexical overlap 0.20) serves as the adversarial robustness benchmark.
13	For human data validation, we use ToxicChat~\citep{lin2023toxicchat} (204 jailbreak + 204 benign from real LMSYS user interactions), entirely independent of Qwen3-8B generation.
14	
15	\paragraph{Models.}
16	Seven DeBERTa-v3 variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\ref{sec:method}).
17	For cross-encoder validation, we replicate vanilla, MLM, and 9-class variants on RoBERTa-base~\citep{liu2019roberta} (Section~\ref{sec:cross_encoder}).
18	We also compare TF-IDF LR and LLM-as-judge baselines (Appendix~\ref{sec:llm_judge}): GPT-5.5 achieves only F1 = 0.191--0.449 on IID Crescendo with 30--47\% unparseable responses; on OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 (DD and ActorAttack) by predicting nearly all conversations as benign, and even 3-shot prompting reaches only 0.566 (DD) and 0.652 (ActorAttack). Content-level reasoning is insufficient for this task.
19	
20	\paragraph{Metrics.}
21	F1 for binary jailbreak detection at prefix $K$=2 and full conversations (full per-$K$ results in Appendix~\ref{sec:full_prefix}).
22	OOD results report 3-seed mean$\pm$std (seeds 42, 123, 456) for all variants except mean pooling (single seed).
23	For key pairwise comparisons, we report BCa bootstrap 95\% confidence intervals (10,000 resampl
…[truncated 28050 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 532
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-18T17:58:27.621744+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-18T17:58:28.123935+00:00_

1	% conclusion.tex — D034 analysis reframe
2	
3	\section{Discussion}
4	\label{sec:discussion}
5	
6	\paragraph{Topic shortcut confound.}
7	One concern is whether a topic-level shortcut (jailbreak conversations discuss different topics than benign ones) could explain the detection results. Three observations argue against this. First, topic classification on the same jailbreak training data yields unstable OOD generalization (F1\,=\,0.541$\pm$0.207 on DD), with one seed falling below vanilla (0.252 vs.\ 0.312); if a topic shortcut drove detection, topic-supervised models should outperform, not underperform, unsupervised alternatives. Second, scrambled labels achieve detection equivalent to correct labels (F1 gap $\leq$3.9\,pp across all OOD evaluations), indicating that specific label content does not drive detection. Third, MLM without any classification labels achieves strong detection (F1\,$\geq$\,0.97 at $K \leq 5$ on DD), confirming that the benefit comes from domain exposure rather than any classification-based shortcut.
8	
9	\paragraph{Single-LLM confound.}
10	Both training and synthetic OOD data are generated by Qwen3-8B, raising the concern that the evidence hierarchy reflects within-LLM stylistic transfer rather than discourse-level generalization. Evaluation on ToxicChat~\citep{lin2023toxicchat} (204 human-written jailbreaks from LMSYS) provides partial resolution: all domain-adapted variants outperform vanilla by 18--42\,pp (Table~\ref{tab:human_data}), confirming that DAPT on synthetic text transfers to human-written attacks. ToxicChat is single-turn, so the relative ordering among domain-adapted variants reflects single-turn modality rather than variant quality. This evidence validates the core DAPT benefit but does not test the full multi-turn pipeline; multi-turn human jailbreak datasets are needed to confirm the complete hierarchy.
11	
12	\paragraph{Variance reversal on human data.}
13	On synthetic OOD evaluations, classification supervision reduces c
…[truncated 6251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-18T17:58:28.124407+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-18T17:58:28.576628+00:00_

1	% appendix.tex — Supplementary material
2	
3	\appendix
4	
5	\section{LLM-as-Judge Baseline}
6	\label{sec:llm_judge}
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\caption{LLM-as-judge jailbreak detection. IID: binary F1 (Crescendo test set); OOD: macro F1 (DD = Deceptive Delight, AA = ActorAttack). GPT-5.5 F1 values exclude unparseable responses and represent upper bounds.}
12	\label{tab:llm_judge}
13	\begin{tabular}{@{}lcccr@{}}
14	\toprule
15	\textbf{Method} & DD & AA & IID & Unparse. \\
16	\midrule
17	\multicolumn{5}{l}{\textit{Zero-shot}} \\[2pt]
18	GPT-5.5 & -- & -- & .383 & 30--47\% \\
19	Qwen3-8B & .244 & .244 & .100 & 0\% \\
20	\midrule
21	\multicolumn{5}{l}{\textit{3-shot}} \\[2pt]
22	Qwen3-8B & .566 & .652 & -- & 0\% \\
23	\midrule
24	\multicolumn{5}{l}{\textit{Trained classifier}} \\[2pt]
25	9-class (ours) & \textbf{.997} & \textbf{.972} & \textbf{1.000} & 0\% \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	Table~\ref{tab:llm_judge} reports LLM-as-judge performance on IID and OOD data.
31	On IID Crescendo, GPT-5.5 achieves precision of 1.0 at all turn prefixes but recall ranges from only 0.105 to 0.290, resulting in F1 = 0.383 on full conversations; 30--47\% of responses are unparseable.
32	Qwen3-8B performs worse (IID F1 = 0.100).
33	On OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 on both DD and ActorAttack by predicting nearly all conversations as benign.
34	Even with 3-shot prompting, Qwen3-8B reaches only 0.566 (DD) and 0.652 (AA), while DisPeD maintains macro F1 $\geq$ 0.972.
35	The poor performance of content-level reasoning on unseen attack types underscores the necessity of trained discourse-aware classifiers.
36	
37	\section{Full Cross-Attack Results by Prefix}
38	\label{sec:full_prefix}
39	
40	\begin{table*}[t]
41	\centering
42	\small
43	\caption{Full cross-attack generalization results (F1) at all prefix lengths. 3-seed mean$\pm$std where available. ``--'' indicates insufficient conversation length for that prefix (FITD c
…[truncated 6386 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-18T17:58:28.577129+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-18T17:58:28.627652+00:00_

1	% checklist.tex — ARR Responsible NLP Research Checklist
2	
3	\section*{Responsible NLP Research Checklist}
4	
5	\paragraph{A. Limitations.}
6	\begin{enumerate}[label=A\arabic*.,leftmargin=2em]
7	  \item Did you describe the limitations of your work? \textbf{Yes.} Section~\ref{sec:limitations} discusses dataset scale, lexical separability, annotation quality, OOD strategy prediction, single-seed variants, scope, and compute cost.
8	  \item Did you discuss any potential risks of your work? \textbf{Yes.} See below.
9	\end{enumerate}
10	
11	\paragraph{B. Potential Risks and Ethical Considerations.}
12	This work studies multi-turn jailbreak attacks against LLMs. While the analysis is defensive (improving detection), we acknowledge dual-use risk: the persuasion taxonomy and attack strategy analysis could inform adversarial actors. We mitigate this by: (1) using only synthetic conversations generated by an open-weight model (Qwen3-8B), not real attack data targeting production systems; (2) not releasing attack-generation prompts that could enable novel attacks; (3) focusing the contribution on detection mechanisms rather than attack techniques. All jailbreak conversations are synthetic and do not contain real harmful content. No human subjects were involved.
13	
14	\paragraph{C. Computational Experiments.}
15	\begin{enumerate}[label=C\arabic*.,leftmargin=2em]
16	  \item Did you report the number of parameters in the models used? \textbf{Yes.} DeBERTa-v3-base (184M) and RoBERTa-base (125M) in Sections~\ref{sec:method} and~\ref{sec:discussion}.
17	  \item Did you report the total amount of compute and the type of resources used? \textbf{Yes.} Under 4 GPU-hours total on a single NVIDIA A100 (40GB). Section~\ref{sec:limitations} and Appendix~\ref{sec:reproducibility}.
18	  \item Did you report the implementation details sufficient for reproducibility? \textbf{Yes.} Appendix~\ref{sec:reproducibility} provides all hyperparameters. We will release code and data upon acceptance
…[truncated 1209 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-18T17:58:34.310788+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "paper_framing.md",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect",
    "file": "paper_framing.md",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-18T17:58:35.315868+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper_framing.md\", \"content\": \"# Paper Framing — persuasion_turn_jailbreak_detect\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR submission)\\n- Deadline: 2026-05-25 (ARR May cycle)\\n- Track: LLM Security / Discourse and Pragmatics\\n- Commitment deadline: 2026-08-02\\n\\n## Title (Working)\\nWhat Makes Multi-Turn Jailbreaks Detectable? A Systematic Decomposition of Cross-Attack Generalization\\n\\n## Core Insight (D030 — post-ActorAttack universal DA reframe)\\nDomain adaptation universally improves cross-attack generalization across encoder architectures; encoder pretraining determines the difficulty threshold at which adaptation becomes critical. Systematic ablation across two encoders (DeBERTa-v3, RoBERTa) and three OOD attack families (DD, FITD, ActorAttack) reveals:\\n\\n**On Deceptive Delight (moderate OOD)**: DeBERTa vanilla collapses (F1=0.31±0.03), continued pretraining bridges ~60pp (MLM=0.91±0.12), classification achieves 0.997±0.005. RoBERTa vanilla already succeeds (0.981±0.026) — hierarchy is flat. Scrambled=binary=9-class (all 0.997±0.005).\\n\\n**On ActorAttack (hard OOD)**: RoBERTa vanilla ALSO collapses (0.466±0.163), proving \\\"no DA needed\\\" was DD-specific. DeBERTa vanilla=0.258±0.000. Both encoders benefit from DA: DeBERTa 9-class=0.972±0.026, RoBERTa 9-class=0.939±0.046. Binary (0.990±0.008) ≈ 9-class (0.972±0.026) ≈ scrambled (0.951±0.043) — all three classification variants equivalent at Full (max gap 3.9pp, variance intervals fully overlap, n=3). Label quality is not a significant factor on ActorAttack, consistent with DD findings (D032).\\n\\n**On Human-Written Jailbreaks (exp8, ToxicChat, macro F1 — D036)**: Domain-adapted variants outperform vanilla on human-authored data from ToxicChat (LMSYS, 204 jailbreaks + 204 benign, balanced, no data leakage). Macro F1: JB-MLM=0.837±0.013,
…[truncated 3404 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-18T17:58:35.416533+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper"
  }
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-18T17:58:35.467105+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-18T17:58:41.648319+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Check project config for external review",
  "prompt": "Read the file at /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/config.yaml and tell me:\n1. Is there an external_review section? Is paperreview_ai enabled?\n2. Any other relevant review-related configuration?\n\nJust report the facts, keep it under 100 words."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Agent",
  "tool_args": {
    "description": "Check project config for external review",
    "prompt": "Read the file at /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/config.yaml and tell me:\n1. Is there an external_review section? Is paperreview_ai enabled?\n2. Any other relevant review-related configuration?\n\nJust report the facts, keep it under 100 words."
  }
}
```

</details>

---


### Tool call

_source line 219 · 2026-05-18T17:58:41.999646+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 220 · 2026-05-18T17:58:42.100601+00:00_

1	% References for persuasion_turn_jailbreak_detect
2	% Auto-generated from literature_map.yaml (2026-05-18)
3	% Total entries: 31
4	
5	% ============================================================
6	% Category 1: Production Multi-Turn Safety Systems
7	% ============================================================
8	
9	@article{inan2023llamaguard,
10	  title={Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations},
11	  author={Inan, Hakan and Upasani, Kartikeya and Chi, Jianfeng and Rungta, Rashi and Iyer, Krithika and Mao, Yuning and Tontchev, Michael and Hu, Qing and Fuller, Brian and Testuggine, Davide and Khabsa, Madian},
12	  journal={arXiv preprint},
13	  year={2023},
14	  eprint={2312.06674},
15	  archivePrefix={arXiv},
16	}
17	
18	@misc{metallamaguard3_2024,
19	  title={Llama Guard 3},
20	  author={{Meta AI}},
21	  year={2024},
22	  howpublished={Meta AI (released with Llama 3.1)},
23	}
24	
25	@article{zeng2024shieldgemma,
26	  title={ShieldGemma: Generative AI Content Moderation Based on Gemma},
27	  author={Zeng, Wenjun and Liu, Yuchi and Mullins, Ryan and Peran, Ludovic and Fernandez, Joe and Harkous, Hamza and Narasimhan, Karthik and Proud, Drew and Kumar, Piyush and Radharapu, Bhaktipriya and Sturman, Olivia and Wahltinez, Oscar},
28	  journal={arXiv preprint},
29	  year={2024},
30	  eprint={2407.21772},
31	  archivePrefix={arXiv},
32	}
33	
34	@inproceedings{han2024wildguard,
35	  title={WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs},
36	  author={Han, Seungju and Rao, Kavel and Ettinger, Allyson and Jiang, Liwei and Lin, Bill Yuchen and Lambert, Nathan and Choi, Yejin and Dziri, Nouha},
37	  booktitle={Advances in Neural Information Processing Systems},
38	  year={2024},
39	}
40	
41	@article{anthropic2025constitutional,
42	  title={Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming},
43	  author={{Anthropic}},
44	  journal={arXiv 
…[truncated 18093 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 221 · 2026-05-18T17:58:44.663323+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/config.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 222 · 2026-05-18T17:58:44.714101+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_director_93d7fc7c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 223 · 2026-05-18T17:58:47.177960+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/persuasion_turn_jailbreak_detect/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/persuasion_turn_jailbreak_detect/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2"
  }
}
```

</details>

---


### Tool result

_source line 224 · 2026-05-18T17:58:47.278952+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 225 · 2026-05-18T17:58:49.793738+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/persuasion_turn_jailbreak_detect/config.*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/persuasion_turn_jailbreak_detect/config.*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2"
  }
}
```

</details>

---


### Tool result

_source line 226 · 2026-05-18T17:58:49.844451+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 227 · 2026-05-18T17:58:52.105402+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/persuasion_turn_jailbreak_detect/**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/persuasion_turn_jailbreak_detect/**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2"
  }
}
```

</details>

---


### Tool result

_source line 228 · 2026-05-18T17:58:52.156047+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/_project/data/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/config/secrets/persuasion_turn_jailbreak_detect/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260518T032748/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260518T032748/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion
…[truncated 1719 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 229 · 2026-05-18T17:58:57.232836+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 230 · 2026-05-18T17:58:57.233218+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 231 · 2026-05-18T17:58:57.723303+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/config"
  }
}
```

</details>

---


### Tool result

_source line 232 · 2026-05-18T17:58:57.775389+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 233 · 2026-05-18T17:59:00.336226+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---


### Tool result

_source line 234 · 2026-05-18T17:59:00.537667+00:00_

{"result":"# 项目 persuasion_turn_jailbreak_detect 概况\n\n## 实验状态 (60 个)\n\n- **plan_016_sentiment_control**: PREPARING (failed) — \n- **plan_012_gpt55_judge**: DONE (success) — \n- **plan_015_dd_eval**: DONE (success) — \n- **plan_006_cross_attack_clean**: DONE (success) — \n- **plan_004_perturbation_eval**: DONE (success) — \n- **plan_013_none_collapse**: DONE (success) — \n- **plan_012_llm_judge_qwen**: DONE (success) — \n- **plan_002_clean_training**: DONE (negative) — \n- **plan_003_scrambled_ablation**: DONE (negative) — \n- **cross_attack_baseline**: DONE (negative) — \n- **plan_008_strategy_transition**: DONE (success) — \n- **plan_007_tfidf_fitd_dd**: DONE (success) — \n- **plan_005_multi_attack_gen**: DONE (success) — \n- **phase_b_full**: DONE (success) — \n- **pilot_phase_b**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp3_probing: 9-class persuasion fine-tuned DeBERTa encodes richer discourse structure (turn position, escalation level, persuasion presence) than vanilla/MLM variants, as measured by linear probing accuracy and CKA divergence（准备中）\n- exp1_roberta_vanilla: Off-the-shelf RoBERTa-base without any fine-tuning will show poor DD OOD performance, matching DeBERTa vanilla baseline pattern and confirming encoder-agnostic findings（准备中）\n- exp1_roberta_mlm: RoBERTa-base with MLM-only continued pretraining will show intermediate DD OOD performance between vanilla and 9-class, matching DeBERTa's evidence hierarchy pattern（准备中）\n- exp1_roberta_9class: RoBERTa-base with 9-class persuasion multi-task fine-tuning will reproduce the DeBERTa evidence hierarchy (9-class >> vanilla), proving findings are encoder-agnostic（准备中）\n- plan_003_scrambled_retrain（准备中）\n- plan_018_eval_seed456（准备中）\n- plan_018_eval_seed123（准备中）\n- plan_018_wiki_mlm_seed456（准备中）\n- plan_018_wiki_mlm_seed123（准备中）\n- plan_017_eval_seed456（准备中）\n- …另有 10 项\n\n## 近期结论\n- **exp9_bootstrap_ci** (success): BCa bootstrap
…[truncated 1376 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 235 · 2026-05-18T17:59:00.538039+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/constraints.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/constraints.yaml"
  }
}
```

</details>

---


### Tool result

_source line 236 · 2026-05-18T17:59:00.588729+00:00_

1	_next_id: 2
2	constraints:
3	- id: C001
4	  added: 2026-05-17 06:29 UTC
5	  summary: GPU 使用严格限制在 cuda:0, cuda:1, cuda:2, cuda:3（westd-33183 共 9 张卡，本项目只分配前 4
6	    张）。训练脚本必须设置 CUDA_VISIBLE_DEVICES=0,1,2,3。
7	  scope: all
8	  reason: 服务器共 9 GPU，Manager 只分配 4 张给本项目。L1 红线：禁止使用白名单外 GPU。
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 237 · 2026-05-18T17:59:04.669084+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
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

_source line 238 · 2026-05-18T17:59:04.820686+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 239 · 2026-05-18T17:59:08.015295+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/registry.yaml",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/registry.yaml",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 240 · 2026-05-18T17:59:08.066009+00:00_

1	baseline: null
2	experiments:
3	  pilot_phase_b:
4	    status: DONE
5	    retry_count: 0
6	    created_at: '2026-05-17T16:29:35.872Z'
7	    updated_at: '2026-05-17T16:29:57.108Z'
8	    hypothesis: Persuasion-aware DeBERTa embeddings (multi-task fine-tuned) fed to
9	      Bi-GRU will outperform vanilla DeBERTa embeddings at early detection (K=2,3,5
10	      turns) of Crescendo-style jailbreak attacks
11	    spec:
12	      command: DeBERTa multi-task 5ep -> embedding extraction -> GRU 29/50ep (disk
13	        full early stop)
14	      server: westd-33183
15	      data_path: /root/persuasion_turn_jailbreak_detect/data/pilot/
16	      data_count: 270
17	      model_name: microsoft/deberta-v3-base
18	      seed: 42
19	      checkpoint_path: /root/persuasion_turn_jailbreak_detect/checkpoints/pilot_deberta/best.pt
20	      log_path: /root/persuasion_turn_jailbreak_detect/results/pilot_results.json
21	    conclusion: success
22	    completed_at: '2026-05-17T16:29:51.169Z'
23	    metrics:
24	      treatment_full_f1: 1
25	      baseline_full_f1: 0.737
26	      tfidf_full_f1: 1
27	      treatment_k2_f1: 1
28	      baseline_k2_f1: 0.737
29	      tfidf_k2_f1: 0.894
30	      treatment_k3_f1: 1
31	      baseline_k3_f1: 0.894
32	      tfidf_k3_f1: 0.894
33	      treatment_k5_f1: 1
34	      baseline_k5_f1: 0.894
35	      tfidf_k5_f1: 0.894
36	      deberta_persuasion_acc: 0.718
37	      deberta_intent_acc: 0.984
38	      test_size: 41
39	      test_benign: 3
40	      test_jailbreak: 38
41	  phase_b_full:
42	    status: DONE
43	    retry_count: 0
44	    created_at: '2026-05-17T16:46:02.649Z'
45	    updated_at: '2026-05-17T16:53:30.358Z'
46	    hypothesis: Persuasion-grounded DeBERTa embeddings (multi-task fine-tuned on 8-class
47	      persuasion + intent) enable significantly earlier detection of Crescendo jailbreak
48	      attacks compared to vanilla DeBERTa embeddings, especially at low K (2-3 turns)
49	    parent: pilot_phase_b
50	    spec:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 241 · 2026-05-18T17:59:12.386510+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "glob": "*.yaml",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
    "glob": "*.yaml",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 242 · 2026-05-18T17:59:12.787986+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Grep",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 243 · 2026-05-18T17:59:13.240531+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "glob": "*.{json,toml,cfg}",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
    "glob": "*.{json,toml,cfg}",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 244 · 2026-05-18T17:59:13.293154+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Grep",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 245 · 2026-05-18T17:59:15.852728+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 246 · 2026-05-18T17:59:16.054014+00:00_

Found 14 files
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/logs/chats/feishu_group_oc_613965f45d48763f375aa83e9294b24a_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/global/logs/system.log
AGENTS.md
CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/logs/chats/feishu_group_oc_a90fe0dde422576f214f12233cfe27a3_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/logs/chats/archive/feishu_group_oc_906e3fa834aa7d39c8bac5ba3dabe7d2_director_20260516T102157_169417.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/logs/chats/feishu_group_oc_8acbea284219b548bfc4c50949ea43a8_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/.claude/sessions/review_director_b5e6fd6f/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/.claude/sessions/review_director_b5e6fd6f/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/logs/chats/worker_analysis_merge-training-dynamics_20260515T032947.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/logs/workers/worker_analysis_merge-training-dynamics_20260515T032947.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Grep",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 247 · 2026-05-18T17:59:19.623683+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview|review.*enabl\"",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "glob": "**/config*.{yaml,yml,json,toml}",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview|review.*enabl\"",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
    "glob": "**/config*.{yaml,yml,json,toml}",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 248 · 2026-05-18T17:59:20.028340+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Grep",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 249 · 2026-05-18T17:59:20.028850+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/project_config*.{yaml,yml,json}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/project_config*.{yaml,yml,json}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2"
  }
}
```

</details>

---


### Tool result

_source line 250 · 2026-05-18T17:59:20.129477+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 251 · 2026-05-18T17:59:22.687168+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config/**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config/**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2"
  }
}
```

</details>

---


### Tool result

_source line 252 · 2026-05-18T17:59:22.737824+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_2/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/config/secrets/tax_error_inject_agent/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/config/projects/tax_error_inject_agent.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/config/venue_rules/corl-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/config/venue_rules/emnlp-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/config/secrets/persuasion_turn_jailbreak_detect/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/config/projects/persuasion_turn_jailbreak_detect.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 253 · 2026-05-18T17:59:25.851019+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/config/projects/persuasion_turn_jailbreak_detect.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/config/projects/persuasion_turn_jailbreak_detect.yaml"
  }
}
```

</details>

---


### Tool result

_source line 254 · 2026-05-18T17:59:25.901613+00:00_

1	execution:
2	  account: root
3	  gpu_constraint: westd-33183:cuda:0,cuda:1,cuda:2,cuda:3
4	  gpu_ids:
5	  - cuda:0
6	  - cuda:1
7	  - cuda:2
8	  - cuda:3
9	  project_path: /root/persuasion_turn_jailbreak_detect
10	  servers:
11	  - westd-33183
12	feishu:
13	  chat_id: oc_a90fe0dde422576f214f12233cfe27a3
14	  operational_chat_id: oc_68ab8931ec4907f792551ec1fb03c882
15	  review_mode: fresh
16	  review_paper_path: projects/persuasion_turn_jailbreak_detect/paper/main.tex
17	  review_round: 3
18	  review_supplementary_paths: ''
19	  submission_chat_id: oc_613965f45d48763f375aa83e9294b24a
20	project:
21	  created_at: '2026-05-17T05:39:56.653Z'
22	  description: 'Beyond Intent Drift: Persuasion-Grounded Turn Representations for
23	    Multi-Turn Jailbreak Detection'
24	  name: persuasion_turn_jailbreak_detect
25	  phase: research
26	  source_idea_id: idea_008
27	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-18T17:59:31.543467+00:00_

Here are the findings:

1. **No `external_review` section exists.** There is no `external_review` or `paperreview_ai` configuration anywhere in the project config at `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/config/projects/persuasion_turn_jailbreak_detect.yaml`. External review via paperreview.ai is **not enabled**.

2. **Review-related configuration found:**
   - `review_mode: fresh` (full re-review, no prior round context)
   - `review_round: 3` (this is the 3rd review round)
   - `review_paper_path: projects/persuasion_turn_jailbreak_detect/paper/main.tex`
   - `review_supplementary_paths: ''` (no supplementary materials specified)
   - `submission_chat_id: oc_613965f45d48763f375aa83e9294b24a` (the review group chat)
agentId: a19dc1b68db054c5b (use SendMessage with to: 'a19dc1b68db054c5b' to continue this agent)
&lt;usage>total_tokens: 27789
tool_uses: 17
duration_ms: 49895&lt;/usage>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Agent",
  "elapsed_ms": 49895
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-18T17:59:38.677640+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
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

_source line 257 · 2026-05-18T17:59:38.778352+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-18T17:59:42.340450+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "review_issues.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect",
    "file": "review_issues.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-18T17:59:42.391082+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-18T17:59:46.512898+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check for existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check for existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-18T17:59:46.715712+00:00_

issues:
  # ============================================================
  # Round 1 历史 issues（全部 resolved）
  # ============================================================
  - id: "R1-N1"
    summary: "Evidence hierarchy 统计基础不一致"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    mentions:
      - round: 1
        reviewers: [1, 2]
        note: "binary/scrambled 仅 seed 42"
    action_items:
      - round: 1
        action: "训练 binary/scrambled 3-seed"
        assigned_to: main_agent
        status: resolved
    resolution: "MF1 完成: binary 3-seed=0.997±0.005, scrambled 3-seed=0.997±0.005"
    resolution_round: 1

  - id: "R1-N2"
    summary: "Three-layer robustness attribution 缺乏统计显著性"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    mentions:
      - round: 1
        reviewers: [1, 2]
        note: "R1 首提 N2"
    action_items:
      - round: 1
        action: "McNemar's test + bootstrap CI"
        assigned_to: main_agent
        status: resolved
    resolution: "MF2 完成"
    resolution_round: 1

  - id: "R1-N3"
    summary: "缺少与已发表 multi-turn defense 的直接实验对比"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    mentions:
      - round: 1
        reviewers: [1, 2]
        note: "R1 首提 N3"
      - round: 2
        reviewers: [1, 2]
        note: "Round 1 修复不充分，再次提出"
    action_items:
      - round: 1
        action: "重构论证"
        assigned_to: paper_agent
        status: resolved
      - round: 2
        action: "Analysis paper reframe 消解直接对比硬性要求"
        assigned_to: research_director
        status: in_progress
    resolution: ""
    resolution_round: null

  - id: "R1-N4"
    summary: "数据集规模过小"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    mentions:
      - round: 1
        revie
…[truncated 17238 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-18T18:00:36.583292+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## 论文信息\n- 标题: \"What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap\"\n- 路径: `projects/persuasion_turn_jailbreak_detect/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex, checklist.tex, references.bib）\n- 目标 Venue: EMNLP 2026 (ARR May cycle)\n- 截止日期: 2026-05-25\n- 页数限制: 正文 ≤ 8 页，references + appendices 无限制\n- 模板: ACL (`\\usepackage[review]{acl}`)\n- 匿名规则: Double-blind\n- 附录规则: 附录不计入页数限制，审稿人可选择性阅读\n\n## 你的审查侧重\n\n### 1. 实验设计与 Ablation 控制\n- 七个 DeBERTa 变体 + 三个 RoBERTa 变体的 ablation 设计是否真正隔离了声称的因素（domain exposure, classification supervision, label quality, label granularity, domain specificity）？\n- frozen encoder 设计是否引入系统性偏差？是否低估了某些变体的潜力？\n- Stage 2 BiGRU vs mean pooling 的比较仅单 seed——这对结论有何影响？\n\n### 2. 统计严谨性\n- 3-seed 设计（seeds 42, 123, 456）是否足够支撑 claims？\n- Bootstrap CI 和 permutation test 的使用是否恰当？样本量（n=76 IID, n=80-118 OOD）的统计效力如何？\n- McNemar's test 对稀疏 discordant pairs (≤7) 的适用性。\n- Evidence hierarchy 中各层级差异的统计显著性。\n\n### 3. 数据质量与潜在偏差\n- 所有训练和 OOD 评估数据均由 Qwen3-8B 生成——single-LLM confound 是否被充分解决？\n- ToxicChat 验证（单轮）能否充分证明 multi-turn evidence hierarchy 不是 artifact？\n- TF-IDF 在 DD 上的强表现（F1=0.961）——lexical separability 对 discourse-level claim 的影响。\n- 策略标注质量：Qwen3-8B 标注，κ=0.78，n=50 验证——是否充分？\n\n### 4. 结论支撑\n- 每个 claim（domain exposure primary, difficulty threshold, classification as regularizer）是否有充分的实验证据支撑？\n- 是否存在 overclaiming 或 underclaiming？\n- Perturbation robustness 在 ActorAttack 上不成立——这对整体叙事的影响。\n\n### 5. 可复现性\n- 是否提供了足够的实现细节？\n- 数据集构建过程是否透明？\n- Checklist 是否如实填写？\n\n请提供完整审稿报告，格式：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分 + 置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## 论文信息\n- 标题: \"What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap\"\n- 路径: `projects/persuasion_turn_jailbreak_detect/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex, checklist.tex, references.bib）\n- 目标 Venue: EMNLP 2026 (ARR May cycle)\n- 截止日期: 2026-05-25\n- 页数限制: 正文 ≤ 8 页，references + appendices 无限制\n- 模板: ACL (`\\usepackage[review]{acl}`)\n- 匿名规则: Double-blind\n- 附录规则: 附录不计入页数限制，审稿人可选择性阅读\n\n## 你的审查侧重\n\n### 1. 实验设计与 Ablation 控制\n- 七个 DeBERTa 变体 + 三个 RoBERTa 变体的 ablation 设计是否真正隔离了声称的因素（domain exposure, classification supervision, label quality, label granularity, domain specificity）？\n- frozen encoder 设计是否引入系统性偏差？是否低估了某些变体的潜力？\n- Stage 2 BiGRU vs mean pooling 的比较仅单 seed——这对结论有何影响？\n\n### 2. 统计严谨性\n- 3-seed 设计（seeds 42, 123, 456）是否足够支撑 claims？\n- Bootstrap CI 和 permutation test 的使用是否恰当？样本量（n=76 IID, n=80-118 OOD）的统计效力如何？\n- McNemar's test 对稀疏 discordant pairs (≤7) 的适用性。\n- Evidence hierarchy 中各层级差异的统计显著性。\n\n### 3. 数据质量与潜在偏差\n- 所有训练和 OOD 评估数据均由 Qwen3-8B 生成——single-LLM confound 是否被充分解决？\n- ToxicChat 验证（单轮）能否充分证明 multi-turn evidence hierarchy 不是 artifact？\n- TF-IDF 在 DD 上的强表现（F1=0.961）——lexical separability 对 discourse-level claim 的影响。\n- 策略标注质量：Qwen3-8B 标注，κ=0.78，n=50 验证——是否充分？\n\n### 4. 结论支撑\n- 每个 claim（domain exposure primary, difficulty threshold, classification as regularizer）是否有充分的实验证据支撑？\n- 是否存在 overclaiming 或 underclaiming？\n- Perturbation robustness 在 ActorAttack 上不成立——这对整体叙事的影响。\n\n### 5. 可复现性\n- 是否提供了足够的实现细节？\n- 数据集构建过程是否透明？\n- Checklist 是否如实填写？\n\n请提供完整审稿报告，格式：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分 + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-18T18:00:57.849073+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21265
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-18T18:00:58.048495+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- 标题: \"What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap\"\n- 路径: `projects/persuasion_turn_jailbreak_detect/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex, checklist.tex, references.bib）\n- 目标 Venue: EMNLP 2026 (ARR May cycle)\n- 截止日期: 2026-05-25\n- 页数限制: 正文 ≤ 8 页，references + appendices 无限制\n- 模板: ACL (`\\usepackage[review]{acl}`)\n- 匿名规则: Double-blind\n- 附录规则: 附录不计入页数限制，审稿人可选择性阅读\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 核心贡献（DAPT 是 cross-attack generalization 的主要机制）是否足够新颖？Gururangan et al. (2020) \"Don't Stop Pretraining\" 已建立 DAPT 范式——本文在此基础上的增量贡献是什么？\n- \"Classification as regularizer\" 的发现是否意外/有价值？scrambled labels = correct labels 的结果对 NLP 社区有多少新信息？\n- Difficulty threshold（DeBERTa vs RoBERTa）的发现是否构成独立贡献？\n- 作为 analysis paper 的定位是否恰当？ablation 的深度和广度是否达到 EMNLP 长文标准？\n\n### 2. Related Work 评估\n- 是否覆盖了所有关键方向：multi-turn attacks, multi-turn defenses, production safety systems, discourse analysis, DAPT, adversarial robustness?\n- Positioning 是否准确——特别是与 DeepContext (2026), BIID (2025), G-Guard (2025), SafeDream (2026) 的区分。\n- 是否有重要的遗漏引用？特别是 2025-2026 年的最新工作。\n- 引用密度是否达到 EMNLP 标准（当前 31 条 bib 条目）？\n\n### 3. 叙事与写作质量\n- Abstract: 是否在 250 words 内清楚回答了四个必答问题（问题、重要性、方法、结果）？是否有数据堆砌？\n- Introduction: 叙事线是否连贯？从问题到贡献的过渡是否自然？\n- 主线统一性: Abstract → Introduction → Method → Experiments → Discussion → Conclusion 是否讲同一个故事？\n- AI 写作风格检查: 是否有 em-dash、-ing 结尾、过度分段、过渡词滥用、用词黑名单中的词？\n- 术语一致性: domain exposure / domain adaptation / continued pretraining / DAPT 等术语是否一致使用？\n- 专有名词首次出现时是否有定义？\n\n### 4. 格式合规\n- 页数是否在 8 页正文限制内（需要编译才能确认，但从 tex 内容估算）？\n- Figure 1 是 placeholder——这对投稿有何影响？\n- 表格格式是否规范（小数精度、最优加粗等）？\n- Responsible NLP Research Checklist 是否完整、如实填写？\n- References 格式是否符合 ACL/ARR 要求？\n\n### 5. 图表质量\n- 现有图表（fig2, fig3）的信息密度和可读性。\n- Figure 1 为 placeholder——是否需要实际架构图？\n- 图表 caption 是否自包含？\n\n请提供完整审稿报告，格式：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分 + 置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- 标题: \"What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap\"\n- 路径: `projects/persuasion_turn_jailbreak_detect/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex, checklist.tex, references.bib）\n- 目标 Venue: EMNLP 2026 (ARR May cycle)\n- 截止日期: 2026-05-25\n- 页数限制: 正文 ≤ 8 页，references + appendices 无限制\n- 模板: ACL (`\\usepackage[review]{acl}`)\n- 匿名规则: Double-blind\n- 附录规则: 附录不计入页数限制，审稿人可选择性阅读\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 核心贡献（DAPT 是 cross-attack generalization 的主要机制）是否足够新颖？Gururangan et al. (2020) \"Don't Stop Pretraining\" 已建立 DAPT 范式——本文在此基础上的增量贡献是什么？\n- \"Classification as regularizer\" 的发现是否意外/有价值？scrambled labels = correct labels 的结果对 NLP 社区有多少新信息？\n- Difficulty threshold（DeBERTa vs RoBERTa）的发现是否构成独立贡献？\n- 作为 analysis paper 的定位是否恰当？ablation 的深度和广度是否达到 EMNLP 长文标准？\n\n### 2. Related Work 评估\n- 是否覆盖了所有关键方向：multi-turn attacks, multi-turn defenses, production safety systems, discourse analysis, DAPT, adversarial robustness?\n- Positioning 是否准确——特别是与 DeepContext (2026), BIID (2025), G-Guard (2025), SafeDream (2026) 的区分。\n- 是否有重要的遗漏引用？特别是 2025-2026 年的最新工作。\n- 引用密度是否达到 EMNLP 标准（当前 31 条 bib 条目）？\n\n### 3. 叙事与写作质量\n- Abstract: 是否在 250 words 内清楚回答了四个必答问题（问题、重要性、方法、结果）？是否有数据堆砌？\n- Introduction: 叙事线是否连贯？从问题到贡献的过渡是否自然？\n- 主线统一性: Abstract → Introduction → Method → Experiments → Discussion → Conclusion 是否讲同一个故事？\n- AI 写作风格检查: 是否有 em-dash、-ing 结尾、过度分段、过渡词滥用、用词黑名单中的词？\n- 术语一致性: domain exposure / domain adaptation / continued pretraining / DAPT 等术语是否一致使用？\n- 专有名词首次出现时是否有定义？\n\n### 4. 格式合规\n- 页数是否在 8 页正文限制内（需要编译才能确认，但从 tex 内容估算）？\n- Figure 1 是 placeholder——这对投稿有何影响？\n- 表格格式是否规范（小数精度、最优加粗等）？\n- Responsible NLP Research Checklist 是否完整、如实填写？\n- References 格式是否符合 ACL/ARR 要求？\n\n### 5. 图表质量\n- 现有图表（fig2, fig3）的信息密度和可读性。\n- Figure 1 为 placeholder——是否需要实际架构图？\n- 图表 caption 是否自包含？\n\n请提供完整审稿报告，格式：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分 + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-18T18:00:59.416739+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1368
}
```

</details>

---


### Assistant

_source line 266 · 2026-05-18T18:01:02.435836+00:00_

Round 1 任务已分配给两位 Reviewer。等待独立审稿结果返回后进行交叉分享（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 19

## Round 19

2 recorded events


### User

_source line 267 · 2026-05-18T18:06:00.648914+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告

**论文**: "What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap"
**Venue**: EMNLP 2026 (ARR May cycle)
**审查侧重**: 新颖性 + 完整性 + 写作质量

---

## 总体评分

**Overall Assessment**: 2.5 / 5 (介于 Resubmit 和 Findings 之间)
**一句话总结**: 实验设计严谨的消融研究，但核心发现（DAPT 有效）缺乏足够新颖性，且合成数据依赖构成系统性威胁——证据层级在人类数据上发生逆转，动摇了论文的核心叙事。

---

## 官方维度打分（ACL ARR Review Form, Feb 2025+）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.0 / 5 | 消融设计严谨，统计检验恰当（McNemar、bootstrap CI、permutation test），但单一 LLM 生成数据构成系统性混淆，人类数据上的证据层级逆转（Table 5）未得到充分解释 |
| **Excitement** | 2.5 / 5 | 问题重要（cross-attack generalization），但 DAPT 有效性已由 Gururangan et al. (2020) 确立，本文增量贡献（应用于新领域 + 正交消融）在概念层面有限 |
| **Reproducibility** | 4.0 / 5 | 超参数详尽（Appendix E），计算成本低（<4 GPU-hours），承诺开源代码和数据 |
| **Confidence** | 4 / 5 | 仔细阅读了全文，熟悉 DAPT、adversarial robustness、multi-turn safety 相关文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Figure 1 为 Placeholder，不可接受
- 具体位置：Section 3 (method.tex line 8-12), `\fbox{\parbox{...}{Architecture diagram placeholder}}`
- 问题：主架构图是一个文字占位框。这是论文唯一的方法概览图，对读者理解 DisPeD 的两阶段流程至关重要。
- 为什么影响接收：审稿人会将此视为论文未完成的信号。架构图是 EMNLP 投稿的基本要求，缺失直接影响可读性和专业性。
- 建议修改方向：绘制完整架构图，展示 Stage 1（七个变体的训练目标分支）到 Stage 2（frozen encoder → BiGRU → MLP）的流程，标注关键消融点。

**N2** [critical] 核心发现"DAPT 是主要机制"的新颖性不足
- 具体位置：Abstract line 6-7, Introduction line 14, Section 5.2 (experiments.tex line 105-112)
- 问题：Gururangan et al. (2020) "Don't Stop Pretraining" 已在四个领域（biomedical、CS、news、reviews）系统验证了 DAPT 的有效性。本文的核心发现——DAPT 在 jailbreak detection 领域同样有效，且 MLM-only 就能桥接约 60pp 的 OOD gap——是该范式在新领域的直接应用。论文虽然承认与 Gururangan et al. 的关系（Related Work, Section 4.5），但未充分说明：在哪些方面本文的发现**超出**了"Don't Stop Pretraining"的预期？
- 为什么影响接收：对于 EMNLP 长文而言，"X 方法在 Y 领域也有效"的验证需要伴随意外发现或深层机制洞察。当前三个 findings 中，Finding 1（DAPT 有效）是预期内的，Finding 2（encoder pretraining 影响 difficulty threshold）有一定信息量但偏描述性，Finding 3（classification as regularizer）是最有新颖性的贡献，但在人类数据上逆转（见 N3）。
- 建议修改方向：(a) 更明确地框定本文的增量贡献——不是"DAPT 有效"，而是"DAPT 为什么在 jailbreak 这种 cross-domain OOD 场景中有效，而其他看似合理的替代方案（topic classification、Wikipedia MLM）失败"；(b) 加强对 representation geometry 的分析（CKA 分析目前只有一段描述，Section 5.4 line 183-191），作为支撑"why"的机制证据。

**N3** [critical] 证据层级在人类数据上逆转，动摇核心叙事
- 具体位置：Table 5 (experiments.tex line 199-217), Discussion "Variance reversal" (conclusion.tex line 12-13)
- 问题：在合成 OOD 数据上，论文建立了清晰的证据层级：classification-supervised ≈ (同等 F1, 更低方差) > MLM > vanilla。但在 ToxicChat 人类数据上（Table 5），层级完全逆转：JB-MLM (0.837) >> Binary (0.705) >> 9-class (0.596)。9-class（论文的"full model"）在人类数据上排名第 5/6（仅高于 Topic 和 Vanilla），且方差最高（std=0.087）。
  - 论文将此归因为"modality mismatch"（ToxicChat 是单轮数据），但这个解释存在问题：如果 classification supervision 的好处仅限于多轮序列正则化，那么 Binary 和 Scrambled 为什么在单轮数据上也弱于 MLM？更合理的解释是 classification supervision 将表征过拟合到了合成数据的分布特征上。
  - Discussion 中"Variance reversal"段落（conclusion.tex line 12-13）提出 classification supervision 是"within-distribution regularizer"而 MLM 是"cross-distribution generalizer"，但这个事后解释与 Abstract/Introduction 的叙事框架不一致——那里将 classification supervision 定位为提供"cross-seed stability"的正面贡献。
- 为什么影响接收：论文仅有的人类数据验证（唯一能排除 single-LLM confound 的证据）恰好推翻了核心叙事。审稿人无法确信在真实部署场景中，哪种变体更优。
- 建议修改方向：(a) 在 Abstract 和 Introduction 中诚实地呈现这个 tension，而非仅在 Discussion 中讨论；(b) 重新框定贡献：classification supervision 的好处是 distribution-specific 的，MLM 在 distribution shift 下更鲁棒——这本身可以是一个有价值的发现，但需要作为主线的一部分，而非事后修补；(c) 增加多轮人类数据评估（如 Li et al. 2024 的 MHJ 数据集已被引用但未用于评估）。

**N4** [critical] 缺少与现有多轮防御方法的直接对比
- 具体位置：Related Work (related_work.tex line 9-10), Section 5.1 (experiments.tex line 16-18)
- 问题：论文讨论了 DeepContext (2026)、BIID (2025)、G-Guard (2025)、SafeDream (2026) 四个多轮防御方法，但没有与其中任何一个进行直接实验对比。Introduction (line 10) 称 vanilla DeBERTa + BiGRU "replicating the frozen-encoder-plus-RNN approach of DeepContext"，但 Related Work (line 10) 又明确声明 "it is not a direct proxy for DeepContext, which differs in encoder fine-tuning, model capacity, and loss function"。
  - 这个自相矛盾削弱了论文的定位。如果 vanilla baseline 不代表 DeepContext，那么论文没有与任何现有方法的可比数据。
  - LLM-as-judge baseline (GPT-5.5, Qwen3-8B) 是一类完全不同的方法，不能替代与同类 encoder-based 多轮防御的对比。
- 为什么影响接收：缺乏 head-to-head comparison 使审稿人无法判断本文方法在实际检测任务中的相对位置。作为 analysis paper 可以不追求 SOTA，但至少需要一个 calibration point 来定位贡献。
- 建议修改方向：(a) 复现 DeepContext（BERT + multi-layer GRU，代码或足够细节可能已公开）在本文数据集上的表现；(b) 或在 DeepContext 的数据集上评估 DisPeD，建立双向对比；(c) 若确实无法对比，需要在 Limitations 中明确承认并解释原因。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Abstract 数据堆砌，叙事不足
- 具体位置：abstract.tex line 3-11
- 问题：Abstract（约 220 words）包含至少 12 个具体数值（60pp、0.961、0.261、0.89、0.981、0.466、3.9pp、4-20×、0.596-0.837、0.413 等）。审稿人在 30 秒内难以从这些数字中提取核心信息。关键结果被数字淹没——例如"TF-IDF F1=0.961 on Deceptive Delight → 0.261 on ActorAttack"这种对比虽信息丰富，但在 Abstract 中过于技术化。
- 建议：保留 2-3 个最关键的数字（如 ~60pp gap bridged、cross-seed variance reduced 4-20×），其余用定性描述替代。Abstract 应该让审稿人 30 秒内判断：问题重要、方法清晰、贡献可信。

**W2** [warning] 合成数据规模过小（n=500 训练，n=76-118 评估）
- 具体位置：Section 5.1 (experiments.tex line 10-13), Limitations (conclusion.tex line 25-27)
- 问题：训练集仅 250 jailbreak + 250 benign 对话。OOD 评估集为 80 FITD + 80 DD + 118 ActorAttack。IID perturbation 评估仅 76 条。论文自己承认（Limitations）perturbation 评估中"tier boundaries in Table 6 correspond to 1-3 misclassifications"——这意味着消融研究中许多看似有意义的差异可能不可靠。
- 为什么影响评分：对于一篇以消融为核心贡献的论文，数据量是统计结论可靠性的关键。500 条训练数据 + 76-118 条评估数据的规模，难以支撑"systematic ablation"的定位。
- 建议：(a) 增加训练和评估数据量（用多个 LLM 生成，同时部分解决 single-LLM confound）；(b) 若保持当前规模，加强 effect size 分析和 power analysis。

**W3** [warning] Related Work 引用密度偏低
- 具体位置：references.bib, related_work.tex
- 问题：当前 31 条 bib 条目（实际去重后 49 条含 checklist 引用），对于 EMNLP 长文偏低（典型范围 40-60+ 正文引用）。具体遗漏方向包括：
  - **Safety training / alignment**: Bai et al. (2022) RLHF, Ouyang et al. (2022) InstructGPT 等安全训练基础工作未引用，而本文讨论的 safety classifier 与 alignment 方法密切相关
  - **Input preprocessing defenses**: Jain et al. (2023) "Baseline Defenses for Adversarial Attacks Against Aligned Language Models" 提出了 perplexity filtering、paraphrasing 等 baseline defense，与本文的 perturbation analysis 直接相关
  - **Multi-turn benchmark / evaluation**: WildChat (Zhao et al., 2024), LMSYS-Chat-1M (Zheng et al., 2024) 等多轮对话数据集未引用
  - **Representation analysis**: CKA 用于表征分析是本文方法之一，但原始 CKA 论文（Kornblith et al., 2019）未被引用
  - **DeBERTa-v3 的准确引用**: 论文始终引用 he2021deberta (DeBERTa v1 论文, ICLR 2021)。DeBERTa-v3 实际使用了不同的预训练目标（replaced token detection, RTD），应引用 He et al. (2023) "DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing"
- 引用验证结果：自动化验证显示 9 条 not_found（包括 liu2019roberta、gururangan2020dontstop 等经典论文——这是 OpenAlex API 的索引问题，非论文问题）和 9 条 mismatch（主要是 first_author 或 year 的小差异）。实质性问题不大，但 austin1962speechacts 的年份 bib 中为 1962，OpenAlex 返回 1975（这是再版 vs 原版的差异，可接受）。

**W4** [warning] TF-IDF 作为强 baseline 削弱 DD 上的结果叙事
- 具体位置：Table 3 (experiments.tex line 36-47), Section 5.1 (experiments.tex line 54-55)
- 问题：TF-IDF LR 在 OOD Deceptive Delight 上达到 F1=0.961（full）和 1.000（K=1-3），几乎匹配所有 domain-adapted 模型。这意味着 DD 数据集存在严重的 lexical separability，DD 上的"strong OOD generalization"可能主要反映词汇层面的差异而非 discourse-level 特征。
  - 论文用 ActorAttack 来解决这个问题（TF-IDF 在 ActorAttack 上 collapse 到 0.261），但 ActorAttack 是唯一能区分 lexical 和 discourse-level 特征的测试集。整个消融的可信度在很大程度上依赖于这单一数据集。
- 建议：(a) 在叙事中更早承认 DD 的 lexical separability 问题；(b) 增加更多结构复杂的 OOD 攻击类型，减少对单一 ActorAttack 数据集的依赖。

**W5** [warning] 术语不一致
- 具体位置：全文
- 问题：以下术语在不同位置交替使用，可能造成混淆：
  - "domain exposure" vs "domain adaptation" vs "continued pretraining" vs "DAPT"：这四个术语在 Abstract、Introduction、Method、Experiments 中混用。例如 Abstract 同时使用 "domain exposure" 和 "domain-adaptive continued pretraining (DAPT)"；Introduction 使用 "domain exposure"。应选定一个首选术语并在首次出现时定义与其他术语的关系。
  - "evidence hierarchy" 首次出现于 Table 4 caption (experiments.tex line 78) 和 Section 5.2 (line 99)，但未在 Introduction 或 Method 中预告。
  - "DisPeD" 在 Method (line 6) 首次出现并定义，但从 Introduction (line 12) 已经使用 "DisPeD" 一词。应在 Introduction 中给出全称定义。
- 建议：统一术语并在首次出现处给出明确定义。

**W6** [warning] Analysis paper 的深度有待加强
- 具体位置：Section 5.4 (experiments.tex line 183-191), Conclusion (conclusion.tex)
- 问题：论文定位为 analysis paper（Introduction line 12: "The core contribution is the systematic decomposition..."），但分析深度在某些关键点上不够：
  - CKA 分析仅一段文字描述（Section 5.4 line 183-191），没有可视化（如 CKA 矩阵热力图）
  - Linear probing 结果（line 190-191: "9-class outperforms vanilla and MLM by 1-5pp"）仅一句话带过，没有表格
  - 没有对 representation space 的可视化（如 t-SNE/UMAP 展示不同变体的 embedding 分布差异）
  - 没有 attention pattern 分析来说明 DAPT 后 encoder 关注了什么不同的特征
  - Related Work 提到 probing classifiers (Conneau et al., 2018; Hewitt & Manning, 2019) 但论文自己说 "we leave this for future work"
- 为什么影响评分：作为 analysis paper，读者期望看到超越 F1 数字对比的深层分析。当前分析在 representation level 的证据太薄。
- 建议：(a) 增加 CKA 矩阵可视化；(b) 展开 linear probing 为完整表格和讨论；(c) 增加 embedding 空间可视化。

---

## 小问题（不影响接收）

**M1** Introduction (line 12) 首次使用 "DisPeD" 但未给出全称展开（"Discourse Persuasion Detection"？论文从未给出全称）。

**M2** Table 3 (experiments.tex) 仅展示 3 个方法（9-class, MLM, Vanilla, TF-IDF），而 Table 4 展示全部 7 个变体。Table 3 的选择性展示可能给审稿人造成 cherry-picking 印象。建议在 Table 3 中也包含其他变体或注明完整结果在 Table 4。

**M3** experiments.tex line 88, Table 4 中 Mean pooling 标注 "single seed (42)"，但在列标题 "3-seed mean±std where available" 下容易被忽略。建议在表格中更显著标注。

**M4** MLM-only 变体在 Table 4 (experiments.tex line 87) 中的标注是 "MLM-only (no labels)"，但在 Section 5.2 line 52 和 Table 3 中的数值 "0.974" 没有 ±std，而其他变体有。是否 MLM-only 是单 seed 训练？需要澄清。

**M5** AI 写作风格检查：
- 整体写作质量较高，没有明显的 em-dash (—) 滥用
- 有几处 -ing 结尾短语：Introduction line 6 "rendering per-turn safety filters fundamentally blind"；experiments.tex line 68 "suggesting that domain exposure enables early detection..."
- 过渡词使用合理，未见 "Furthermore/Moreover/Additionally" 连续出现
- 未发现用词黑名单中的词（delve, leverage, utilize, facilitate 等）
- 段落长度合理，未见过度分段

**M6** Checklist (checklist.tex) 中 Section E2 关于 license 的回答（"will be released under a research-use license"）较模糊。建议指明具体 license（如 CC-BY-NC 4.0）。

**M7** experiments.tex line 22-23: "population std with $N$ divisor" 放在括号中——这是一个重要的方法学细节（population std vs sample std），不应仅在括号中一笔带过。对于 n=3 seeds，两者差异显著。

---

## 主要优势

1. **消融设计精良**：七个 Stage-1 变体（9-class、binary、scrambled、MLM-only、topic、wiki-MLM、vanilla）各自干净地隔离一个变量（label quality、granularity、domain specificity 等），加上两个 encoder 架构的交叉验证，构成了一个教科书级的消融矩阵。

2. **统计严谨性**：3-seed 评估、McNemar's test、BCa bootstrap CI、permutation test 的组合使用超过了大多数 EMNLP 投稿的统计标准。论文主动报告 effect size 不显著的结果（如 classification-supervised variants 间 McNemar all p > 0.13），体现了诚实的学术态度。

3. **Negative results 的价值**：Topic classification 的失败（Section 5.2 line 121-124）和 strategy prediction 在 OOD 上的失败（Section 5.6 line 302-303, κ=0.126）都是有信息量的 negative results。

4. **低计算成本**：全部七个变体 + 两个 encoder 共 <4 GPU-hours，使结果高度可复现。

5. **诚实的 Limitations**：Section 7 覆盖了主要弱点（dataset scale、lexical separability、annotation quality、OOD strategy prediction、single-seed、scope、compute），每个都有具体量化。

---

## 缺失引用（建议补充）

1. He et al. (2023) "DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing" — 论文使用 DeBERTa-v3-base 但只引用了 v1 论文
2. Kornblith et al. (2019) "Similarity of Neural Network Representations Revisited" — 论文使用 Centered CKA 但未引用原始方法
3. Bai et al. (2022) "Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback" — safety training 基础工作
4. Jain et al. (2023) "Baseline Defenses for Adversarial Attacks Against Aligned Language Models" — input preprocessing defense baseline
5. Zhao et al. (2024) "WildChat: 1M ChatGPT Interaction Logs in the Wild" — 相关多轮对话数据集
6. Zheng et al. (2024) "LMSYS-Chat-1M" — 相关对话数据集
7. Qi et al. (2024) "Fine-tuning Aligned Language Models Compromises Safety" — 与 DAPT 改变 safety properties 直接相关

---

## 总体评估

这篇论文提出了一个重要的研究问题（什么表征属性使多轮 jailbreak 检测能跨攻击家族泛化？），并通过精心设计的消融实验给出了系统性答案。实验设计和统计方法论是论文最强的方面。

然而，论文存在几个根本性问题阻碍了当前版本的接收：

(1) **新颖性不足**：核心发现（DAPT 有效）是 Gururangan et al. (2020) 的领域延伸，概念增量有限。"Classification as regularizer"是更有新意的贡献，但在人类数据上逆转（N3），削弱了其可信度。

(2) **外部效度不足**：所有多轮评估均在合成数据上完成；唯一的人类数据验证（ToxicChat）是单轮且推翻了证据层级。作为一篇关于"什么使检测泛化"的论文，缺乏对真实多轮人类 jailbreak 的验证是致命弱点。

(3) **缺乏 baseline 对比**：未与任何现有多轮防御方法（DeepContext、BIID、G-Guard）进行直接对比，审稿人无法判断方法的实际价值。

(4) **Figure 1 为 placeholder**：对提交论文的完成度产生严重怀疑。

建议作者：(a) 补充 Figure 1；(b) 增加多轮人类数据评估；(c) 重新框定叙事，将人类数据上的逆转作为核心发现的一部分而非例外；(d) 加深 representation-level 分析。修改后的版本适合 EMNLP Findings 或下一 cycle 的 main conference 投稿。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 268 · 2026-05-18T18:06:28.362135+00:00_

Reviewer 2 报告已收到，记录关键发现：

**Reviewer 2 评分**: 2.5/5（介于 Resubmit 和 Findings）

**Must-Fix (4)**:
- N1: Figure 1 为 placeholder
- N2: DAPT 有效性的新颖性不足
- N3: 证据层级在人类数据上逆转，动摇核心叙事
- N4: 缺少与现有多轮防御的直接对比

**Should-Fix (6)**: Abstract 数据堆砌、数据规模小、引用密度低、TF-IDF 削弱 DD 结果、术语不一致、analysis 深度不足

**Minor (7)**: DisPeD 全称未展开、表格选择性展示、单 seed 标注不清等

等待 Reviewer 1 报告返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 20

## Round 20

2 recorded events


### User

_source line 269 · 2026-05-18T18:06:30.878027+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

总结：

**Overall: 2.5/5** — 介于 Resubmit 和 Findings 之间。

**4 个 Must-Fix 问题**：
1. Figure 1 是 placeholder，不可接受
2. DAPT 有效性作为核心发现缺乏新颖性（Gururangan et al. 2020 的领域延伸）
3. 证据层级在人类数据（ToxicChat）上逆转（9-class 排名 5/6），动摇核心叙事
4. 未与任何现有多轮防御方法直接对比

**6 个 Should-Fix 问题**：Abstract 数据堆砌、合成数据规模过小（n=500）、引用密度偏低（31 条）、TF-IDF 强 baseline 削弱 DD 叙事、术语不一致、analysis paper 深度不够（缺 CKA 可视化、embedding 空间分析等）

**主要优势**：消融设计精良、统计严谨性高、negative results 有价值、计算成本低、Limitations 诚实

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 270 · 2026-05-18T18:06:44.635880+00:00_

Reviewer 2 审稿报告已收到。等待 Reviewer 1 完成独立审稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 21

## Round 21

6 recorded events


### User

_source line 271 · 2026-05-18T18:07:59.357877+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告

**论文**: "What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap"
**审查侧重**: 方法严谨性 + 实验设计
**审稿模式**: fresh

---

## Summary

本文通过控制性消融研究，分析了什么表示属性使 multi-turn jailbreak 检测能够跨攻击族泛化。作者设计了七个 DeBERTa-v3 Stage-1 变体和三个 RoBERTa 变体（统称 DisPeD），在四个攻击族上评估，得出三个发现：(1) domain-adaptive continued pretraining (DAPT) 是 OOD 泛化的主要机制（~60pp gap）；(2) encoder 预训练方法决定了 DAPT 变得关键的难度阈值；(3) 分类监督起正则化作用而非策略分类作用。ToxicChat 验证表明 DAPT 优势迁移至 human-written 数据。

研究问题明确（"什么使得表示能泛化？"而非"如何检测"），消融设计巧妙。但 single-LLM confound、"discourse-level" overclaiming、统计效力不足，以及 Figure 1 缺失等问题影响了论文的 soundness 和完成度。

---

## Strengths

**S1. 研究问题定位精准，消融设计巧妙。**
七个 Stage-1 变体的设计系统地隔离了 domain exposure、classification supervision、label quality、label granularity、domain specificity 五个因素（Table 1, Section 3.2）。每个变体的对比意义清晰——例如 scrambled labels 隔离 label correctness，topic classification 测试 task alignment。这种 controlled ablation 方法论优于典型的"提出新模型→在 benchmark 上跑"的范式。

**S2. 核心发现（DAPT 为主要机制）有跨 encoder 支撑。**
DeBERTa-v3 上 vanilla→MLM 的 ~60pp 提升（Table 3: DD 0.312→0.914）和 RoBERTa 上 ActorAttack 的 vanilla→9-class 提升（Table 4: 0.466→0.939）从两个架构验证了 DAPT 的核心作用。Bootstrap CIs 确认了关键对比不重叠（Section 5.1: 9-class DD Full CI [0.943, 1.000] vs. vanilla [0.202, 0.341]）。

**S3. "分类作为正则化器"发现具有反直觉的价值。**
Scrambled labels 与 correct labels 在所有 OOD 评估上达到等效检测 F1（gap ≤3.9pp, Table 3, Table S3），而 OOD 策略预测精度仅 30.7%（κ=0.126, Section 5.6）。这挑战了"需要好标签才能泛化"的朴素假设，对安全分类器设计有实际启示。

**S4. 诚实地报告了负面结果。**
Perturbation robustness 在 ActorAttack 上不成立（9-class Δ=-20.4±13.5pp, Section 5.5），variance reversal 在 ToxicChat 上出现（Section 5.4），McNemar's test 的 power 限制被明确讨论。相比于掩盖不利结果，这种透明度值得肯定。

**S5. Compute cost 极低，可复现性设计合理。**
全部变体训练 <4 GPU-hours（Section 6），所有超参数在 Appendix D 中完整报告，承诺 release code/data。3-seed 设计虽然 minimal，但在 ACL/EMNLP 短论文传统下是可接受的。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**N1** [critical] Figure 1 为占位符，论文未完成
- 具体位置：method.tex line 10，`\fbox{\parbox{0.9\columnwidth}{\centering\vspace{2em}\textit{Architecture diagram placeholder}\vspace{2em}}}`
- 问题：Figure 1 是论文中唯一的架构图，目前是一个写着"Architecture diagram placeholder"的空框。这不是一个可提交的状态。
- 为什么影响接收：审稿人会认为论文未完成（desk reject 风险），且缺少架构图使 two-stage pipeline 的理解完全依赖文字描述。
- 建议：替换为真正的架构图，展示 Stage 1 七个变体的训练目标 → frozen encoder → Stage 2 BiGRU → classification 的完整 pipeline。

**N2** [critical] Single-LLM confound 对 "cross-attack generalization" claim 的威胁未充分解决
- 具体位置：Section 4 (Setup), Section 5.4 (Human Data), Section 6 (Discussion)
- 问题：训练数据（250 Crescendo + 250 benign）和全部 OOD 评估数据（FITD, DD, ActorAttack）均由 Qwen3-8B 生成。所谓 "cross-attack generalization" 实际上是 "cross-attack-strategy generalization within Qwen3-8B generation distribution"。DAPT 在 Qwen3-8B 文本上训练后对 Qwen3-8B 生成的新攻击文本泛化，可能部分反映 within-model stylistic transfer 而非 genuine discourse-level feature learning。
- ToxicChat 验证（Table 5）仅部分缓解此问题：(a) ToxicChat 是 single-turn，无法验证 multi-turn evidence hierarchy；(b) 在 ToxicChat 上 classification-supervised variants 的排序完全逆转（9-class=0.596 < MLM=0.837），这恰好是对 Finding 3（classification as regularizer）最强的反面证据。
- 为什么影响接收：如果不能在非 Qwen3-8B 生成的 multi-turn 数据上验证核心 findings，则 "domain exposure bridges the cross-attack gap" 的 claim 范围被严重限制。至少需要一个额外 LLM（如 Llama-3, GPT-4o-mini）生成的 OOD 攻击评估。
- 建议：(1) 用至少一个其他 LLM 生成部分 OOD 评估数据；(2) 如果不可行，需将论文标题和 claims 限定为 "within synthetic data manifold" 的发现；(3) 在 abstract 和 conclusion 中将此作为首要 caveat 而非 "direction for future work"。

**N3** [critical] "Discourse-level" claims 缺乏直接证据
- 具体位置：Section 5.2 ("continued pretraining on jailbreak conversation text captures pragmatic features: hedging, escalation markers, topic-shifting patterns"), Section 5.1 ("domain-adapted representations capture structural features beyond bag-of-words")
- 问题：论文声称 DAPT 捕获了 discourse-level 特征，但唯一的间接证据是 TF-IDF 在 ActorAttack 上失败而 DAPT 模型成功（Section 5.1: TF-IDF F1=0.261 vs. 9-class F1=0.972）。TF-IDF 失败证明 DAPT 捕获了超越 unigram/bigram 的特征，但 "超越 bag-of-words" ≠ "discourse-level"。可能的非 discourse 解释包括：(a) 更长 n-gram 或 sub-word 模式；(b) token embedding 空间中的 distributional shift；(c) 句内语法结构而非跨 turn 语用结构。
- Related Work 最后一句提到 probing classifiers 可以回答这个问题，但将其留给 future work。如果论文的核心 framing 是 "discourse-level"，则需要 probing 证据来支撑。
- 为什么影响接收：这影响论文的核心叙事可信度。"DAPT 捕获了 something beyond BoW" 和 "DAPT 捕获了 discourse-level pragmatic structure" 是两个 claim 层级，后者远超前者但论文给出的证据只支撑前者。
- 建议：(1) 在 diagnostic probing 中增加 discourse-level task（如跨 turn 一致性、escalation 阶段判断——Section 5.3 的 linear probing 已有部分尝试但结果仅差 1-5pp，不足以证明 discourse-level feature）；或 (2) 降低 claim 层级，替换所有 "discourse-level" / "pragmatic features" 的描述为更准确的 "features beyond lexical overlap"。

**N4** [critical] 评估集大小不一致，数据划分不透明
- 具体位置：Section 4 (Setup) vs. Section 5.5 (Perturbation Analysis)
- 问题：
  (a) Setup 声明 DD 有 80 个对话（experiments.tex line 11），但 Perturbation Analysis 声称 "On OOD Deceptive Delight (n=118)" （experiments.tex line 265）。80 ≠ 118，论文未解释差异来源。
  (b) IID test 声明为 "76 held-out Crescendo conversations"（line 12），但 Crescendo 仅指 jailbreak 对话。计算 F1 需要 benign 样本。论文从未说明 IID 和 OOD 评估中有多少 benign 对话、来源是什么。
  (c) 如果 n=118 = 80 jailbreak + 38 benign，那 benign 来自哪里？IID 的 benign test set 大小是多少？
- 为什么影响接收：这直接影响可复现性，且可能影响 F1 计算的准确性（class balance 影响 F1）。
- 建议：在 Setup 中明确报告每个评估集的完整构成（jailbreak + benign 数量），并解释 n=118 与 n=80 的关系。

### Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 3-seed variance estimation 的统计可靠性
- 具体位置：Section 5.2 ("4-20× variance reduction"), Table 3, Table 4
- 问题："4-20× variance reduction" 是 Finding 3 的核心定量表述，但基于仅 3 个 seeds 的 std 计算。用 3 个点估计的 std 本身有极大不确定性（std 的标准误约为 std/√(2(n-1)) = std/2，即 50% 相对误差）。例如，MLM DD-Full std=0.115 主要由 seed 456（recall=0.64）驱动；如果该 seed 是 outlier，真实 variance 可能远低于 0.115。
- 建议：(1) 增加到 5-10 seeds 验证 variance reduction claim；或 (2) 明确声明 "4-20×" 是基于 3 seeds 的 point estimate，confidence interval 覆盖范围很大。

**W2** [warning] McNemar's test 在 sparse discordant pairs 上的使用
- 具体位置：Section 5.5 ("all p > 0.13; discordant pairs ≤7")
- 问题：论文使用 McNemar's test 声称分类变体之间"无显著差异"，但 ≤7 discordant pairs 下该检验几乎无统计效力。absence of significance ≠ evidence of equivalence。要证明等效性，应使用 equivalence testing（如 TOST procedure 或 Bayesian approach）。
- 论文部分承认了这一点（"should be interpreted as an observed pattern rather than a statistically confirmed hierarchy"），但仍在多处将 McNemar p>0.13 作为"no difference" 的证据引用。
- 建议：将 McNemar 结果替换为或补充以 equivalence test；或明确在每次引用 McNemar 时标注 power 限制。

**W3** [warning] Encoder 容量混淆变量
- 具体位置：Table 4 (Cross-Encoder), Section 6 Discussion
- 问题：DeBERTa-v3-base (184M) vs. RoBERTa-base (125M) 在参数量上有 47% 差异。"难度阈值由 encoder 预训练方法决定" 的 claim（Finding 2）与 "难度阈值由 encoder 容量决定" 无法区分。例如，DeBERTa-v3 在 DD 上 vanilla F1=0.312 可能部分因为其更大容量导致 RTD 表示在小数据 fine-tune 下更不稳定，而非 RTD 本身的问题。
- Discussion 承认了这一点但主文叙述仍将其归因于预训练方法。
- 建议：在 Contribution 列表和 abstract 中对 Finding 2 添加 "controlling for architecture but not model size" 的限定；或用 RoBERTa-large (355M) 复现以隔离容量效应。

**W4** [warning] ToxicChat 上 evidence hierarchy 的完全逆转
- 具体位置：Table 5 (Human Data)
- 问题：在 ToxicChat 上，MLM（0.837）>> 9-class（0.596），排序与 synthetic OOD 完全逆转。论文将此归因于 "modality mismatch"（single-turn vs. multi-turn），但这个解释有问题：如果 classification supervision 是一个 generic representational regularizer（如论文所 claim），它不应该在 single-turn 上表现更差；如果它的 regularization 是 distribution-specific 的（如 Discussion 承认的），那 "regularizer" 这个 framing 就需要大幅修改。
- 当前论文在 Section 6 Discussion 中做了细致分析（"distribution-specific regularization"），但 abstract 和 contributions 中的 Finding 3 表述未反映这一重要限定。
- 建议：在 abstract 和 Contribution 3 中明确 "classification supervision 的 regularization 效果是 distribution-specific 的"，避免读者误认为这是一个 generic finding。

**W5** [warning] Perturbation robustness 在 ActorAttack 上不成立
- 具体位置：Section 5.5, experiments.tex lines 272-274
- 问题：9-class 在 ActorAttack 上 paraphrasing 后 F1 从 0.972 下降到 0.768（Δ=-20.4±13.5pp），且 cross-seed 方差极大（seed 123: Δ=-1.3pp; seeds 42, 456: Δ=-30.3pp）。这与 IID 和 DD 上的 zero-degradation 结论完全矛盾。
- 虽然论文诚实报告了此结果（S4），但 perturbation analysis 在论文叙事中占了 ~1 页篇幅（Section 5.5），而最终结论是 "attack-family-dependent"，这削弱了整个 section 的叙事价值。
- 建议：考虑将 perturbation analysis 移至 appendix，在正文中简要报告 "perturbation robustness is observed on IID and DD but does not generalize to structurally complex attacks"。

**W6** [warning] TF-IDF 在 DD 上的强表现削弱了 DD 作为核心评估集的意义
- 具体位置：Table 2 (TF-IDF DD Full F1=0.961), Section 5.1
- 问题：TF-IDF LR 在 DD 上 per-prefix F1 达到 0.994-1.000（Appendix Table S2），full conversation F1=0.961。这意味着 DD 几乎完全被词汇特征解决。论文在 DD 上建立的 evidence hierarchy（Table 3 的核心结果）可能仅反映不同变体捕获词汇特征的能力，而非 discourse-level representation quality。
- ActorAttack 才是真正区分 discourse-level 和 lexical features 的评估集（TF-IDF 0.261 vs. 9-class 0.972），但论文的主要结果表（Table 2）和 Figure 2 都以 DD 为中心。
- 建议：将 ActorAttack 提升为主要展示评估集（不仅是辅助），因为它是唯一能支持 "beyond lexical" claim 的 OOD 数据集。

**W7** [warning] 策略标注验证不充分
- 具体位置：Section 3.2 (Method), Section 6 (Limitations)
- 问题：策略标注由 Qwen3-8B 完成，human validation 仅 n=50、κ=0.78、单个人类标注者。对于 9-class taxonomy：(a) 50 个样本平均每类 ~5.5 个，不足以评估每个类别的标注质量；(b) κ=0.78 是 "substantial" 但不是 "almost perfect"（>0.81）；(c) 单个人类标注者无法区分 inter-human agreement 和 human-model agreement。
- 论文的 Finding 3（classification as regularizer）间接缓解了这一问题——label 质量不影响检测。但 Figure 3 的策略轨迹分析和 Section 5.6 的解释性分析仍依赖标注质量。
- 建议：增加第二个人类标注者计算 inter-human κ 作为 upper bound；或在 Figure 3 分析中添加 caveat。

### Minor 问题（不影响接收）

**M1.** Qwen3-8B 在论文中被广泛使用（数据生成、标注、paraphrasing、LLM-as-judge baseline）但 references.bib 中无对应引用。Checklist E1 中仅提及 "Qwen3-8B (for data generation)"。应添加正式引用。

**M2.** MLM-only 变体在 Table 3 中部分结果无 std（DD-Full: .914±.115 有 std，但 IID 列 .974 和 1.000 无 std）。这暗示 MLM 可能仅运行了单 seed？应统一为 3-seed 报告或注明。

**M3.** FITD 评估几乎无区分力：所有变体（包括 vanilla）达到 F1 ≥ 0.990（Appendix Table S2）。建议在 Discussion 中解释为何 FITD 如此简单（可能因对话仅 2-3 turns 且模式明显）。

**M4.** Population std (N divisor) 与 sample std (N-1 divisor)：Checklist C4 声明使用 population std。3 seeds 下 N=3，population std 比 sample std 低 18%。应说明选择理由，或改用 sample std。

**M5.** Abstract 第 5 行 "seven encoder variants on DeBERTa-v3 and three on RoBERTa" 中 "on" 的使用 awkward，建议改为 "of DeBERTa-v3" or "based on DeBERTa-v3"。

**M6.** Table 2 caption 说 "3-seed mean±std where noted" 但 TF-IDF 行无 std 注释。应注明 TF-IDF 是确定性模型。

---

## Questions for Authors

**Q1.** DD 的评估样本量在 Setup (n=80) 和 Perturbation Analysis (n=118) 中不一致。请澄清 n=118 的构成——是 80 jailbreak + 38 benign 吗？benign 样本来源是什么？

**Q2.** 论文声称 "classification supervision functions as a representational regularizer"，但在 ToxicChat 上该效果完全逆转（9-class std=0.087 > MLM std=0.013）。如果 regularization 是 distribution-specific 的，那么在什么条件下应该使用 classification supervision vs. MLM-only？论文能否给出实践建议？

**Q3.** Mean pooling 在 DD 上 single-seed F1=1.000（Table 3），如果 multi-seed 确认此结果，则意味着 temporal modeling（BiGRU）完全不必要。这对 "multi-turn" jailbreak detection 的 discourse-level framing 意味着什么？每个 turn 独立可分 vs. 需要跨 turn 推理是一个根本区别。

**Q4.** Linear probing 结果（Section 5.3）显示 9-class 仅在 diagnostic tasks 上超出 vanilla/MLM 1-5pp。这种微小差异如何与 detection F1 上的巨大差异（9-class 0.997 vs. vanilla 0.312）共存？probing accuracy 和 detection F1 之间的 disconnect 是否暗示 detection 依赖不同于 probing tasks 测量的特征？

**Q5.** 对于 ActorAttack perturbation robustness 的 cross-seed 极端方差（seed 123: Δ=-1.3pp vs. seed 42/456: Δ=-30.3pp），是否检查过 seed 123 的行为是否是 outlier（如看 per-sample prediction 分布）？

---

## Missing References

1. **Qwen3-8B 官方引用缺失** — 论文的数据生成、标注、paraphrasing、baseline 均依赖 Qwen3-8B，但无引用。
2. **DeBERTa-v3 论文** — 论文引用的是 `he2021deberta`（原始 DeBERTa），但使用的是 DeBERTa-v3-base。DeBERTa v3 有单独的技术报告（He et al., 2023, "DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing"），应引用 v3 版本以准确对应 RTD pretraining 的讨论。
3. **ELECTRA** — 论文讨论了 DeBERTa-v3 的 RTD (Replaced Token Detection) 预训练，但未引用 ELECTRA (Clark et al., 2020)，而 RTD 正是 ELECTRA 引入的训练方法。

---

## Overall Assessment

### ACL ARR 评分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3/5 (Acceptable) | 核心 DAPT finding 有跨 encoder 支撑，消融设计合理。但 single-LLM confound 限制了 "cross-attack generalization" claim 的范围；"discourse-level" 缺乏直接证据；数据划分不透明（N1-N4）。主要 claims 的支撑 sufficient 但有显著 caveats 未在 abstract/contributions 中反映。 |
| **Excitement** | 3/5 (Interesting) | 研究问题好（"什么使表示泛化" 而非 "怎么检测"），"classification as regularizer" 发现有 surprising value。但实际 impact 受限于全 synthetic 数据评估，且无法与 DeepContext/BIID/G-Guard 直接对比性能。 |
| **Overall** | 3.0 (Findings) | 消融设计巧妙、DAPT finding 稳健、论文对负面结果诚实。但 Figure 1 缺失、single-LLM confound、discourse-level overclaiming、数据划分不透明 四个 critical issues 需要解决。修复 N1 后可达 borderline conference；解决 N2-N4 可能提升至 conference level。当前状态适合 Findings。 |
| **Confidence** | 4/5 | 仔细阅读全文，熟悉 domain adaptation、safety classifiers、multi-turn dialogue 相关工作。 |

### 一句话总结

消融设计优秀且 DAPT finding 稳健，但 single-LLM confound 和 "discourse-level" overclaiming 使得核心 claims 的范围比论文表述的更窄；Figure 1 placeholder 是 submission-readiness 硬伤。

---

## 引用验证附注

通过 verify_references 工具检查了全部 49 条 bib entries：
- 31 条 verified，9 条 not found（多为 OpenAlex API coverage 问题，非幻觉引用），9 条有 minor mismatch（主要是 first author 姓名格式或年份差异）
- 无 orphan bib（未引用的条目）或 missing bib（引用了但无条目）
- 需注意：`he2021deberta` 引用的是 DeBERTa v1 而非实际使用的 v3；Qwen3-8B 完全未引用


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-18T18:08:49.941745+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]**：同意该问题，并说明你的理由或补充观察\n- **[REBUT]**：不同意或认为该问题被高估，提供证据（引用具体 Section/Table/Figure）\n\n---\n\n**Reviewer 2 Overall: 2.5/5**\n\n### Must-Fix 问题\n\n**N1** [critical] Figure 1 为 Placeholder，不可接受\n- Section 3 (method.tex line 8-12)，主架构图是文字占位框。审稿人将此视为论文未完成的信号。\n\n**N2** [critical] 核心发现\"DAPT 是主要机制\"的新颖性不足\n- Gururangan et al. (2020) \"Don't Stop Pretraining\" 已在四个领域验证 DAPT 有效性。本文核心发现是该范式在新领域的直接应用。Finding 1（DAPT 有效）预期内，Finding 2（difficulty threshold）偏描述性，Finding 3（classification as regularizer）最有新颖性但在人类数据上逆转。建议更明确框定增量贡献——不是\"DAPT 有效\"而是\"为什么 DAPT 在 jailbreak cross-domain OOD 场景有效而其他替代方案失败\"；加强 CKA representation geometry 分析。\n\n**N3** [critical] 证据层级在人类数据上逆转，动摇核心叙事\n- ToxicChat 上 JB-MLM (0.837) >> 9-class (0.596)。9-class 排名 5/6，方差最高（std=0.087）。论文的\"modality mismatch\"解释有问题：如果好处仅限于多轮正则化，Binary 和 Scrambled 为何在单轮也弱于 MLM？更合理解释是 classification supervision 过拟合到合成分布。Discussion 中\"variance reversal\"与 Abstract/Introduction 叙事不一致。建议在 Abstract/Introduction 中呈现这个 tension，重新框定贡献。\n\n**N4** [critical] 缺少与现有多轮防御方法的直接对比\n- 未与 DeepContext、BIID、G-Guard、SafeDream 直接实验对比。Introduction 称 vanilla baseline \"replicating the frozen-encoder-plus-RNN approach of DeepContext\"，但 Related Work 又说 \"not a direct proxy\"——自相矛盾。建议复现 DeepContext 在本文数据集上的表现，或在其数据集上评估 DisPeD。\n\n### Should-Fix 问题\n\n**W1** Abstract 数据堆砌（12+ 数值），建议保留 2-3 个。\n\n**W2** 合成数据规模过小（n=500 训练，n=76-118 评估）。\n\n**W3** Related Work 引用密度偏低（31 条 bib），遗漏方向包括 RLHF/alignment、input preprocessing defenses、多轮对话数据集、CKA 原始论文、DeBERTa-v3 正确引用。\n\n**W4** TF-IDF 在 DD 上 F1=0.961，DD 存在严重 lexical separability，整个消融可信度依赖单一 ActorAttack 数据集。\n\n**W5** 术语不一致：domain exposure / domain adaptation / continued pretraining / DAPT 混用；\"evidence hierarchy\" 未预告；\"DisPeD\" 在 Introduction 使用但未定义。\n\n**W6** Analysis paper 深度不够：CKA 仅一段描述无可视化，Linear probing 结果仅一句话，无 t-SNE/UMAP，无 attention pattern 分析。\n\n### Minor 问题\nM1-M7: DisPeD 全称未给出、Table 3 选择性展示、mean pooling 标注不显著、MLM-only seed 数不明确、AI 写作风格基本合格、Checklist license 模糊、population std 细节。\n\n### 优势\n消融设计精良、统计严谨、negative results 有价值、低计算成本、诚实 Limitations。\n\n### 缺失引用\nHe et al. (2023) DeBERTa-v3, Kornblith et al. (2019) CKA, Bai et al. (2022) RLHF, Jain et al. (2023) Baseline Defenses, WildChat, LMSYS-Chat-1M, Qi et al. (2024)。\n\n---\n\n请对以上每个 Must-Fix (N1-N4) 和 Should-Fix (W1-W6) 逐条给出 [AGREE] 或 [REBUT]，并说明理由。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]**：同意该问题，并说明你的理由或补充观察\n- **[REBUT]**：不同意或认为该问题被高估，提供证据（引用具体 Section/Table/Figure）\n\n---\n\n**Reviewer 2 Overall: 2.5/5**\n\n### Must-Fix 问题\n\n**N1** [critical] Figure 1 为 Placeholder，不可接受\n- Section 3 (method.tex line 8-12)，主架构图是文字占位框。审稿人将此视为论文未完成的信号。\n\n**N2** [critical] 核心发现\"DAPT 是主要机制\"的新颖性不足\n- Gururangan et al. (2020) \"Don't Stop Pretraining\" 已在四个领域验证 DAPT 有效性。本文核心发现是该范式在新领域的直接应用。Finding 1（DAPT 有效）预期内，Finding 2（difficulty threshold）偏描述性，Finding 3（classification as regularizer）最有新颖性但在人类数据上逆转。建议更明确框定增量贡献——不是\"DAPT 有效\"而是\"为什么 DAPT 在 jailbreak cross-domain OOD 场景有效而其他替代方案失败\"；加强 CKA representation geometry 分析。\n\n**N3** [critical] 证据层级在人类数据上逆转，动摇核心叙事\n- ToxicChat 上 JB-MLM (0.837) >> 9-class (0.596)。9-class 排名 5/6，方差最高（std=0.087）。论文的\"modality mismatch\"解释有问题：如果好处仅限于多轮正则化，Binary 和 Scrambled 为何在单轮也弱于 MLM？更合理解释是 classification supervision 过拟合到合成分布。Discussion 中\"variance reversal\"与 Abstract/Introduction 叙事不一致。建议在 Abstract/Introduction 中呈现这个 tension，重新框定贡献。\n\n**N4** [critical] 缺少与现有多轮防御方法的直接对比\n- 未与 DeepContext、BIID、G-Guard、SafeDream 直接实验对比。Introduction 称 vanilla baseline \"replicating the frozen-encoder-plus-RNN approach of DeepContext\"，但 Related Work 又说 \"not a direct proxy\"——自相矛盾。建议复现 DeepContext 在本文数据集上的表现，或在其数据集上评估 DisPeD。\n\n### Should-Fix 问题\n\n**W1** Abstract 数据堆砌（12+ 数值），建议保留 2-3 个。\n\n**W2** 合成数据规模过小（n=500 训练，n=76-118 评估）。\n\n**W3** Related Work 引用密度偏低（31 条 bib），遗漏方向包括 RLHF/alignment、input preprocessing defenses、多轮对话数据集、CKA 原始论文、DeBERTa-v3 正确引用。\n\n**W4** TF-IDF 在 DD 上 F1=0.961，DD 存在严重 lexical separability，整个消融可信度依赖单一 ActorAttack 数据集。\n\n**W5** 术语不一致：domain exposure / domain adaptation / continued pretraining / DAPT 混用；\"evidence hierarchy\" 未预告；\"DisPeD\" 在 Introduction 使用但未定义。\n\n**W6** Analysis paper 深度不够：CKA 仅一段描述无可视化，Linear probing 结果仅一句话，无 t-SNE/UMAP，无 attention pattern 分析。\n\n### Minor 问题\nM1-M7: DisPeD 全称未给出、Table 3 选择性展示、mean pooling 标注不显著、MLM-only seed 数不明确、AI 写作风格基本合格、Checklist license 模糊、population std 细节。\n\n### 优势\n消融设计精良、统计严谨、negative results 有价值、低计算成本、诚实 Limitations。\n\n### 缺失引用\nHe et al. (2023) DeBERTa-v3, Kornblith et al. (2019) CKA, Bai et al. (2022) RLHF, Jain et al. (2023) Baseline Defenses, WildChat, LMSYS-Chat-1M, Qi et al. (2024)。\n\n---\n\n请对以上每个 Must-Fix (N1-N4) 和 Should-Fix (W1-W6) 逐条给出 [AGREE] 或 [REBUT]，并说明理由。"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-18T18:09:23.761605+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 33819
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-18T18:09:23.962787+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]**：同意该问题，并说明你的理由或补充观察\n- **[REBUT]**：不同意或认为该问题被高估，提供证据（引用具体 Section/Table/Figure）\n\n---\n\n**Reviewer 1 Overall: 3.0/5 (Findings)**\n\n### Must-Fix 问题\n\n**N1** [critical] Figure 1 为占位符，论文未完成\n- method.tex line 10，Architecture diagram placeholder。desk reject 风险。\n\n**N2** [critical] Single-LLM confound 对 \"cross-attack generalization\" claim 的威胁未充分解决\n- 训练和全部 OOD 评估数据均由 Qwen3-8B 生成。\"cross-attack generalization\" 实际上是 \"within Qwen3-8B generation distribution\" 的泛化。ToxicChat 验证仅部分缓解（单轮且 classification-supervised 排序逆转）。建议用至少一个其他 LLM 生成 OOD 评估数据，或限定 claims 范围。\n\n**N3** [critical] \"Discourse-level\" claims 缺乏直接证据\n- 论文声称 DAPT 捕获了 pragmatic features（hedging, escalation markers, topic-shifting patterns），但唯一间接证据是 TF-IDF 在 ActorAttack 失败。\"超越 bag-of-words\" ≠ \"discourse-level\"。可能的非 discourse 解释包括更长 n-gram、sub-word 模式、句内语法结构。Related Work 提到 probing classifiers 可回答此问题但留给 future work。建议增加 discourse-level diagnostic probing，或降低 claim 层级为 \"features beyond lexical overlap\"。\n\n**N4** [critical] 评估集大小不一致，数据划分不透明\n- Setup 声明 DD n=80，但 Perturbation Analysis 声称 n=118。80 ≠ 118 未解释。IID test \"76 held-out Crescendo\" 仅指 jailbreak，未说明 benign 样本数量和来源。\n\n### Should-Fix 问题\n\n**W1** 3-seed variance estimation 的统计可靠性\n- \"4-20× variance reduction\" 基于仅 3 seeds，std 的相对误差约 50%。MLM DD-Full std=0.115 主要由 seed 456 驱动。建议增加到 5-10 seeds 或明确声明 confidence interval 覆盖范围。\n\n**W2** McNemar's test 在 sparse discordant pairs (≤7) 上几乎无统计效力\n- absence of significance ≠ evidence of equivalence。建议使用 equivalence testing（TOST 或 Bayesian approach）。\n\n**W3** Encoder 容量混淆变量\n- DeBERTa-v3-base (184M) vs RoBERTa-base (125M) 47% 差异。Finding 2（difficulty threshold 由 pretraining method 决定）与\"由 capacity 决定\"无法区分。建议添加限定或用 RoBERTa-large 复现。\n\n**W4** ToxicChat 上 evidence hierarchy 完全逆转\n- MLM (0.837) >> 9-class (0.596)。如果 classification supervision 是 generic regularizer，不应在单轮上更差。\"regularizer\" framing 需要大幅修改。建议在 abstract 和 Contribution 3 中明确 \"distribution-specific\"。\n\n**W5** Perturbation robustness 在 ActorAttack 上不成立\n- 9-class ActorAttack Δ=-20.4±13.5pp，cross-seed 方差极大。整个 Section 5.5 占 ~1 页但结论是 \"attack-family-dependent\"。建议移至 appendix。\n\n**W6** TF-IDF 在 DD 上 F1=0.961 削弱 DD 作为核心评估集的意义\n- DD 几乎完全被词汇特征解决。建议将 ActorAttack 提升为主要展示评估集。\n\n**W7** 策略标注验证不充分\n- n=50、κ=0.78、单个人类标注者。建议增加第二个标注者或添加 caveat。\n\n### Minor 问题\nM1-M6: Qwen3-8B 无引用、MLM-only 部分结果无 std、FITD 无区分力、population vs sample std、Abstract 措辞、TF-IDF 确定性未标注。\n\n### Questions\nQ1. DD n=80 vs n=118 构成？\nQ2. Classification supervision vs MLM-only 的实践建议？\nQ3. Mean pooling=BiGRU 对 discourse-level framing 的含义？\nQ4. Probing accuracy 与 detection F1 的 disconnect？\nQ5. ActorAttack perturbation seed 123 是否 outlier？\n\n### 缺失引用\nQwen3-8B 官方引用、DeBERTa-v3 论文 (He et al. 2023)、ELECTRA (Clark et al. 2020)。\n\n---\n\n请对以上每个 Must-Fix (N1-N4) 和 Should-Fix (W1-W7) 逐条给出 [AGREE] 或 [REBUT]，并说明理由。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]**：同意该问题，并说明你的理由或补充观察\n- **[REBUT]**：不同意或认为该问题被高估，提供证据（引用具体 Section/Table/Figure）\n\n---\n\n**Reviewer 1 Overall: 3.0/5 (Findings)**\n\n### Must-Fix 问题\n\n**N1** [critical] Figure 1 为占位符，论文未完成\n- method.tex line 10，Architecture diagram placeholder。desk reject 风险。\n\n**N2** [critical] Single-LLM confound 对 \"cross-attack generalization\" claim 的威胁未充分解决\n- 训练和全部 OOD 评估数据均由 Qwen3-8B 生成。\"cross-attack generalization\" 实际上是 \"within Qwen3-8B generation distribution\" 的泛化。ToxicChat 验证仅部分缓解（单轮且 classification-supervised 排序逆转）。建议用至少一个其他 LLM 生成 OOD 评估数据，或限定 claims 范围。\n\n**N3** [critical] \"Discourse-level\" claims 缺乏直接证据\n- 论文声称 DAPT 捕获了 pragmatic features（hedging, escalation markers, topic-shifting patterns），但唯一间接证据是 TF-IDF 在 ActorAttack 失败。\"超越 bag-of-words\" ≠ \"discourse-level\"。可能的非 discourse 解释包括更长 n-gram、sub-word 模式、句内语法结构。Related Work 提到 probing classifiers 可回答此问题但留给 future work。建议增加 discourse-level diagnostic probing，或降低 claim 层级为 \"features beyond lexical overlap\"。\n\n**N4** [critical] 评估集大小不一致，数据划分不透明\n- Setup 声明 DD n=80，但 Perturbation Analysis 声称 n=118。80 ≠ 118 未解释。IID test \"76 held-out Crescendo\" 仅指 jailbreak，未说明 benign 样本数量和来源。\n\n### Should-Fix 问题\n\n**W1** 3-seed variance estimation 的统计可靠性\n- \"4-20× variance reduction\" 基于仅 3 seeds，std 的相对误差约 50%。MLM DD-Full std=0.115 主要由 seed 456 驱动。建议增加到 5-10 seeds 或明确声明 confidence interval 覆盖范围。\n\n**W2** McNemar's test 在 sparse discordant pairs (≤7) 上几乎无统计效力\n- absence of significance ≠ evidence of equivalence。建议使用 equivalence testing（TOST 或 Bayesian approach）。\n\n**W3** Encoder 容量混淆变量\n- DeBERTa-v3-base (184M) vs RoBERTa-base (125M) 47% 差异。Finding 2（difficulty threshold 由 pretraining method 决定）与\"由 capacity 决定\"无法区分。建议添加限定或用 RoBERTa-large 复现。\n\n**W4** ToxicChat 上 evidence hierarchy 完全逆转\n- MLM (0.837) >> 9-class (0.596)。如果 classification supervision 是 generic regularizer，不应在单轮上更差。\"regularizer\" framing 需要大幅修改。建议在 abstract 和 Contribution 3 中明确 \"distribution-specific\"。\n\n**W5** Perturbation robustness 在 ActorAttack 上不成立\n- 9-class ActorAttack Δ=-20.4±13.5pp，cross-seed 方差极大。整个 Section 5.5 占 ~1 页但结论是 \"attack-family-dependent\"。建议移至 appendix。\n\n**W6** TF-IDF 在 DD 上 F1=0.961 削弱 DD 作为核心评估集的意义\n- DD 几乎完全被词汇特征解决。建议将 ActorAttack 提升为主要展示评估集。\n\n**W7** 策略标注验证不充分\n- n=50、κ=0.78、单个人类标注者。建议增加第二个标注者或添加 caveat。\n\n### Minor 问题\nM1-M6: Qwen3-8B 无引用、MLM-only 部分结果无 std、FITD 无区分力、population vs sample std、Abstract 措辞、TF-IDF 确定性未标注。\n\n### Questions\nQ1. DD n=80 vs n=118 构成？\nQ2. Classification supervision vs MLM-only 的实践建议？\nQ3. Mean pooling=BiGRU 对 discourse-level framing 的含义？\nQ4. Probing accuracy 与 detection F1 的 disconnect？\nQ5. ActorAttack perturbation seed 123 是否 outlier？\n\n### 缺失引用\nQwen3-8B 官方引用、DeBERTa-v3 论文 (He et al. 2023)、ELECTRA (Clark et al. 2020)。\n\n---\n\n请对以上每个 Must-Fix (N1-N4) 和 Should-Fix (W1-W7) 逐条给出 [AGREE] 或 [REBUT]，并说明理由。"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-18T18:09:25.322222+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1359
}
```

</details>

---


### Assistant

_source line 276 · 2026-05-18T18:09:28.627783+00:00_

交叉分享已发出。等待两位 Reviewer 的逐条 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 22

## Round 22

2 recorded events


### User

_source line 277 · 2026-05-18T18:09:31.154868+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**报告概要：**

- **Overall: 3.0 (Findings)**，Soundness 3/5，Excitement 3/5，Confidence 4/5
- **4 个 Must-Fix 问题**：(1) Figure 1 为占位符，论文未完成；(2) single-LLM confound（训练和全部 OOD 数据均来自 Qwen3-8B）对 "cross-attack generalization" claim 的威胁未充分解决；(3) "discourse-level" claims 缺乏 probing 等直接证据，仅有 TF-IDF 失败这一间接证据；(4) DD 评估样本量在 Setup (n=80) 和 Perturbation (n=118) 中矛盾，数据划分（benign 样本数量/来源）未说明
- **7 个 Should-Fix 问题**：3-seed variance estimation 可靠性、McNemar sparse pairs 无 power、encoder 容量混淆、ToxicChat 上 hierarchy 逆转、ActorAttack perturbation 不成立、TF-IDF 在 DD 上表现过强削弱 DD 作为评估集的意义、策略标注验证不充分
- **6 个 Minor 问题**：Qwen3-8B 缺引用、MLM-only 部分结果缺 std、FITD 无区分力、population vs sample std、措辞、TF-IDF 确定性注释

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 278 · 2026-05-18T18:09:37.238987+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 23

## Round 23

2 recorded events


### User

_source line 279 · 2026-05-18T18:10:55.001109+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 交叉回应：Reviewer 2 意见

---

## Must-Fix 逐条回应

**[AGREE] R2-N1: Figure 1 为 Placeholder**
完全同意。我在 R1-N1 中独立提出了同一问题。这是 submission-readiness 硬伤，无需讨论。

---

**[REBUT] R2-N2: "DAPT 是主要机制"新颖性不足**

R2 认为 Finding 1 是 Gururangan et al. (2020) 在新领域的直接应用，新颖性不足。我部分不同意，理由如下：

(1) **论文的核心贡献不是 "DAPT works" 而是 "what doesn't work and why"。** Gururangan et al. (2020) 验证了 DAPT 在 biomedical/CS/news/reviews 上有效，但没有设计消融来回答"DAPT 的哪个方面在起作用"。本文的关键增量是：scrambled labels = correct labels（Table 3: 三个分类变体均 0.997±0.005 on DD），topic classification 主动破坏泛化（0.541±0.207），Wiki-MLM 几乎匹配 JB-MLM at full length（0.904 vs. 0.914）。这些负面结果和等价性结果不能从 "Don't Stop Pretraining" 预测得出。

(2) **但 R2 关于 framing 的建议是正确的。** 论文应该更强调"为什么替代方案失败"而非"DAPT 有效"。当前 abstract 和 Introduction 的 Finding 1 表述确实过于接近 "DAPT works in a new domain"。Contribution 1 如果改为 "systematic evidence that classification labels are not the mechanism, and misaligned objectives actively harm generalization" 会更有新颖性信号。

(3) **R2 建议加强 CKA representation geometry 分析也是合理的**——我在 R1 审稿中虽未单独提出此项，但与 R1-N3（"discourse-level" 缺乏直接证据）一致。CKA 可视化能部分回答 DAPT 到底改变了表示空间的什么结构。

**结论：N2 作为 critical 级别偏高。** novelty 不在 "DAPT works" 而在消融设计和负面发现。但 framing 确实需要调整以凸显真正的增量。建议降为 should-fix（framing adjustment），而非 critical。

---

**[AGREE] R2-N3: 证据层级在人类数据上逆转**

同意这是一个严重问题。我在 R1-W4 中作为 should-fix 提出了同样的问题，但 R2 的分析更深入，说服我将其提升为 critical 级别。

R2 的关键洞察是：**如果 "modality mismatch" 是充分解释，那 Binary（0.705）和 Scrambled（0.616）不应低于 MLM（0.837），因为它们也有相同的 domain exposure。** 事实是所有包含 classification objective 的变体（无论 label quality）都在 ToxicChat 上低于纯 MLM，这表明 classification head 不是"无害的正则化器"，而是在表示空间中引入了 distribution-specific boundaries，这些 boundaries 在分布迁移时成为障碍。

具体证据：
- Table 5: JB-MLM (0.837±0.013) > Wiki-MLM (0.791±0.093) > Binary (0.705±0.072) > Scrambled (0.616±0.056) > 9-class (0.596±0.087) > Topic (0.496±0.042)
- 排序严格按 "classification objective 的复杂度" 递减：无分类 > 2-class > 9-class（scrambled）> 9-class（correct）
- 9-class 排名 5/6 且 std 最高（0.087），这与 synthetic OOD 上 std 最低（0.005）形成鲜明对比

R2 的替代解释——classification supervision 过拟合到合成分布——比论文的 "modality mismatch" 更有解释力。论文 Discussion 中 "distribution-specific regularization" 的分析（conclusion.tex line 13）部分触及了这一点，但 abstract 和 Contribution 3 的表述完全未反映这一重要限定。

**建议**：Contribution 3 应改为 "classification supervision provides distribution-specific regularization that stabilizes within-manifold predictions but can hurt cross-distribution transfer"。当前的 "classification as regularizer" framing 过于笼统。

---

**[REBUT] R2-N4: 缺少与现有多轮防御方法的直接对比**

R2 的矛盾指出（Introduction "replicating" vs. Related Work "not a direct proxy"）完全正确——这是论文的真实写作 bug，需要修复。但我不同意将"缺少直接对比"提升为 critical。

理由：

(1) **论文定位是 analysis/ablation paper，不是 system paper。** 论文在 Introduction 第四段明确说 "The core contribution is the systematic decomposition of what enables cross-attack generalization, not the detection pipeline itself"（introduction.tex line 12）。要求 analysis paper 提供 SOTA comparison 是混淆了论文类型。HotpotQA 的 probing 分析论文不需要打败 SOTA QA 系统，DAPT 论文不需要打败 BERT-large。

(2) **现有方法的公平对比在实践中极难实现。** DeepContext、BIID、G-Guard、SafeDream 使用不同的数据集、不同的评估协议、不同的攻击族。在本文的数据集上复现它们，或在它们的数据集上评估 DisPeD，都需要大量工程工作，且可能因数据/评估差异引入新的混淆变量。

(3) **但矛盾的 framing 必须修复。** Introduction 不应说 "replicating"，Related Work 的 "not a direct proxy" 措辞是正确的。建议统一为：vanilla baseline 代表 "pretrained-encoder-plus-RNN without domain adaptation" 这一类方法，而非特定复现。

**结论：语言矛盾是 must-fix（写作 bug），但要求与 DeepContext 等方法直接实验对比是 nice-to-have 而非 critical。** 建议降为 should-fix。

---

## Should-Fix 逐条回应

**[AGREE] R2-W1: Abstract 数据堆砌**
同意。我重新数了一遍 abstract：至少 12 个数值（~60pp, F1=0.961, 0.261, ≥0.89, 0.981→0.466, 4-20×, 0.596-0.837, 0.413，加上几个 percentage points）。对于 ~200 words 的 abstract，数据密度过高。保留 3-4 个最核心数字（vanilla→MLM gap, ActorAttack TF-IDF vs. 9-class gap, ToxicChat domain-adapted vs. vanilla gap），将其余移至 introduction 或正文。

---

**[REBUT] R2-W2: 合成数据规模过小**
部分不同意。对于 system paper（追求 SOTA），n=500 训练确实偏小。但对于 analysis paper（追求 controlled ablation），小规模反而有利：(a) 计算成本低（<4 GPU-hours），允许 7 variants × 3 seeds × 2 encoders 的完整消融；(b) 所有变体在相同数据上训练，严格控制了数据变量；(c) 更大数据可能掩盖变体之间的差异（IID 上所有变体已经达到 F1=1.0，数据增大只会使 OOD 差异也缩小）。

评估规模（n=76-118）确实限制了统计效力——我在 R1-W1 和 R1-W2 中已提出 3-seed variance estimation 和 McNemar sparse discordant pairs 的问题。但这是统计效力问题，不是数据规模问题。建议加 seeds 而非加数据。

---

**[AGREE] R2-W3: 引用密度偏低，遗漏方向**
同意。31 条 bib 对 EMNLP main 偏低（典型 40-60 条）。R2 指出的遗漏中，我优先同意以下几项：
- **DeBERTa-v3 正确引用**（He et al., 2023）——我在 R1 Missing References 中独立提出
- **CKA 原始论文**（Kornblith et al., 2019）——论文使用 Centered CKA 但未引用定义论文
- **ELECTRA**（Clark et al., 2020）——我在 R1 中独立提出，RTD 预训练来自 ELECTRA

RLHF/alignment 方向（Bai et al., 2022）和多轮对话数据集（WildChat, LMSYS-Chat-1M）的引用建议合理但非 critical。

---

**[AGREE] R2-W4: DD lexical separability，消融可信度依赖单一 ActorAttack**
同意。我在 R1-W6 中提出了相同问题。补充一个量化观察：TF-IDF 在 DD 上 per-prefix F1 达到 0.994-1.000（Appendix Table S2），甚至超过部分 neural 变体。DD 上的 evidence hierarchy 可能仅反映不同变体捕获 lexical features 的效率，而非 discourse-level representation quality。

ActorAttack 是唯一真正区分 lexical 和 beyond-lexical 的评估集，但它也是唯一一个 perturbation robustness 崩溃的评估集（Section 5.5: 9-class Δ=-20.4±13.5pp）。这意味着在 "beyond lexical" 的唯一评估集上，模型的 robustness 是脆弱的。这进一步支持了 R2 的 concern。

---

**[AGREE with qualification] R2-W5: 术语不一致**
部分同意。"domain exposure" / "domain adaptation" / "continued pretraining" / "DAPT" 混用确实影响可读性，应统一。"evidence hierarchy" 作为论文的核心分析框架，首次使用前应有定义。

但 R2 说 **"DisPeD 在 Introduction 使用但未定义"** 这一点是 **不准确的**。Introduction line 12 明确写了 "encoder adaptation followed by frozen BiGRU classification, which we call **DisPeD**"。DisPeD 在 Introduction 首次出现时即有定义。R2 可能遗漏了这一定义。不过，DisPeD 的全称（presumed: Discourse-level Persuasion Detection?）确实未在论文中给出——如果这是缩写，应展开。

---

**[AGREE] R2-W6: Analysis paper 深度不够**
同意这是一个重要问题。作为自称 analysis/ablation paper 的工作，分析工具的运用确实单薄：
- CKA：仅 Section 5.3 一段文字描述（experiments.tex lines 184-191），无可视化矩阵或图表。考虑到论文声称 "substantially reshape the representation space"，至少需要一个 CKA heatmap。
- Linear probing：仅一句话总结 "9-class outperforms vanilla and MLM by 1-5pp"（line 190），未给出 per-task 数据表。
- 无 t-SNE/UMAP 可视化来直观展示 vanilla vs. MLM vs. 9-class 的表示空间差异。
- 无 attention pattern 分析来检验 "discourse-level" claim。

这与我在 R1-N3 中提出的 "discourse-level claims 缺乏直接证据" 高度相关。CKA 可视化 + probing 详细结果 + 表示空间可视化可以部分回应 R1-N3 和 R2-N2/W6 三个问题。

---

## 与 R1 审稿意见的交叉总结

| R2 问题 | R1 对应 | 判断 | 备注 |
|---------|---------|------|------|
| R2-N1 Figure placeholder | R1-N1 | 完全一致 | 两位 reviewer 独立发现 |
| R2-N2 Novelty 不足 | — | 部分不同意 | 建议降为 should-fix (framing) |
| R2-N3 Human data reversal | R1-W4 | 同意升级为 critical | R2 分析更深入 |
| R2-N4 缺少直接对比 | — | 语言矛盾 agree，要求对比 rebut | 建议降为 should-fix |
| R2-W1 Abstract 数据堆砌 | — | 同意 | |
| R2-W2 数据规模小 | R1-W1 | 部分不同意 | analysis paper vs. system paper |
| R2-W3 引用偏低 | R1 Missing Refs | 同意 | DeBERTa-v3, ELECTRA, CKA |
| R2-W4 DD lexical sep. | R1-W6 | 完全一致 | R2 进一步强化 |
| R2-W5 术语不一致 | — | 部分同意 | DisPeD 定义存在于 Intro |
| R2-W6 分析深度不够 | R1-N3 | 同意 | 与 discourse-level claim 相关 |

两份审稿的核心共识：(1) Figure 1 缺失不可接受；(2) human data 上的 evidence hierarchy reversal 是最严重的实质性问题；(3) "discourse-level" claim 缺乏分析深度支撑；(4) DD 的 lexical separability 问题。

两份审稿的主要分歧：R2 认为 novelty 不足和缺少 baseline comparison 是 critical，我认为这两点对 analysis paper 而言应为 should-fix。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 280 · 2026-05-18T18:11:02.679708+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 24

## Round 24

2 recorded events


### User

_source line 281 · 2026-05-18T18:11:05.227311+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

核心判断：4 个 AGREE（N1 Figure placeholder, N3 human data reversal, W1 abstract 堆砌, W3/W4/W6 引用+分析深度），2 个 REBUT（N2 novelty — 消融设计本身有增量，建议降级; N4 baseline comparison — analysis paper 不应强制要求 SOTA 对比），W2/W5 部分同意。两份审稿最大共识是 human data reversal 和 Figure 缺失；最大分歧在于对 analysis paper 应否要求 novelty 和 baseline comparison 的标准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 282 · 2026-05-18T18:11:09.862992+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 25

## Round 25

6 recorded events


### User

_source line 283 · 2026-05-18T18:11:29.536076+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 Reviewer 1 审稿意见

---

## Must-Fix 问题

**[AGREE] R1-N1: Figure 1 为占位符**
完全同意，我在自己的审稿中也将此列为 N1 (critical)。补充一点：对于一篇以"systematic decomposition"为核心卖点的论文，架构图不仅是格式要求，更是帮助读者理解七个变体之间关系的关键工具。当前 Table 1 (method.tex line 24-42) 已有变体列表，但缺乏视觉化的因果隔离关系图。

**[AGREE] R1-N2: Single-LLM confound**
同意此为 critical 问题。我在自己的 N3 中从另一个角度（证据层级逆转）讨论了同一问题。补充两点：
1. 论文在 experiments.tex line 197 称 ToxicChat "entirely independent of any LLM generation pipeline"，这是事实，但 ToxicChat 的验证仅覆盖了"DAPT vs vanilla gap transfers"这一最弱的 claim，而未覆盖核心的证据层级排序。
2. R1 建议"用至少一个其他 LLM 生成 OOD 评估数据"——这是最小成本的改进，但仍不能完全排除合成数据共性问题。更理想的做法是使用 Li et al. (2024) MHJ 数据集中的真实多轮人类 jailbreak（论文已引用 li2024mhj 但未用于评估）。

**[AGREE] R1-N3: "Discourse-level" claims 缺乏直接证据**
同意，且我认为这个问题比 R1 描述的更严重。具体证据：
1. experiments.tex line 107 声称 DAPT 捕获了 "pragmatic features (hedging, escalation markers, topic-shifting patterns)"，但没有任何 probing 实验支持这一具体解释。这是一个未经检验的假设被当作发现呈现。
2. experiments.tex line 140-141 报告 mean pooling ≈ BiGRU (F1=1.000, single seed)，论文自己也承认 "detection relies primarily on per-turn representations rather than their sequential order"。这与 discourse-level 叙事存在直接矛盾——如果检测不依赖 turn 之间的顺序关系，那么所谓的 "discourse-level structure" 体现在哪里？
3. Related Work (related_work.tex line 22) 明确提到 probing classifiers 可以回答这个问题但 "we leave this for future work"。对于一篇 analysis paper，将回答核心机制问题的工具留给 future work 是一个重大缺陷。
4. R1 提出的替代解释（longer n-gram, sub-word patterns, intra-sentence syntax）都是合理的。"beyond bag-of-words"（TF-IDF collapse on ActorAttack）确实不等于"discourse-level"。建议将 claim 降级为 "features beyond lexical overlap that may include but are not limited to discourse-level structure"。

**[AGREE] R1-N4: DD n=80 vs n=118 数据不一致**
同意。我重新核实了原文：
- experiments.tex line 11: "80 FITD, 80 Deceptive Delight (DD), and 118 ActorAttack conversations"
- experiments.tex line 265: "On OOD Deceptive Delight ($n$=118)"

这两处数字明确矛盾。最可能的解释是 line 265 的 n=118 是笔误（可能混淆了 DD 和 ActorAttack 的样本量），或者 n=118 包含了 jailbreak + benign 对话总数（80 jailbreak + 38 benign？但 Setup 中未说明 OOD benign 样本来源和数量）。无论哪种情况，这都是数据报告的严重不透明。

补充 R1 未提到的一个相关问题：IID test set "76 held-out Crescendo" (experiments.tex line 12) 仅指 jailbreak 对话数。benign test set 的大小和来源完全未说明——是从 250 benign 训练集中划出的吗？如果是，划分比例是多少？这影响所有 IID 结果的可解读性。

---

## Should-Fix 问题

**[AGREE] R1-W1: 3-seed variance estimation 不可靠**
同意。补充：experiments.tex line 53 明确指出 MLM DD-Full 的 seed 456 recall=0.64，这意味着 std=0.115 几乎完全由这一个 seed 的异常表现驱动。当 n=3 且一个 seed 是 outlier 时，std 的含义存疑。论文在 Abstract (line 7) 和 Conclusion (line 21) 中将 "4-20× variance reduction" 作为 classification supervision 的核心优势之一反复强调，但这个数字的统计基础是 3 个 seed 的 population std 比较——相对误差约 50%，不足以支撑如此强的 claim。我在自己的 M7 中也指出了 population std vs sample std 的问题（n=3 时两者差异显著）。

**[AGREE] R1-W2: McNemar's test 在 sparse discordant pairs 上无效力**
同意，且我认为论文在这一点上存在逻辑矛盾。experiments.tex line 109-110 用 McNemar's test 的不显著结果（"all $p > 0.13$"）来支持 "label quality and granularity are non-factors for detection" 的 claim，但 line 263 又承认 "limited statistical power to detect differences of this magnitude"。不显著结果 + 承认 power 不足 = 不能得出任何方向的结论。R1 建议的 equivalence testing (TOST) 是正确的统计方法——它可以积极地证明等价性，而非依赖 null result。

**[AGREE] R1-W3: Encoder 容量混淆变量**
同意。Discussion (conclusion.tex line 15-16) 承认了这个问题但未解决。DeBERTa-v3-base (184M) 比 RoBERTa-base (125M) 大 47%，这个差异足以成为 Finding 2（"encoder pretraining method determines difficulty threshold"）的替代解释。论文应至少在 Contribution 列表（Introduction line 20）和 Conclusion 中对此加限定词。

**[AGREE] R1-W4: ToxicChat 证据层级逆转**
强烈同意——这与我自己的 N3 (critical) 完全一致。R1 的表述比我更精确："如果 classification supervision 是 generic regularizer，不应在单轮上更差"。补充一个具体数字对比：9-class 在 ToxicChat 上不仅低于 JB-MLM（0.596 vs 0.837，差距 24pp），还低于 Wiki-MLM（0.596 vs 0.791，差距 20pp）——这意味着即使是非 jailbreak 领域的 MLM 都比 classification supervision 更能泛化到人类数据。这直接挑战了 "classification as regularizer" 的正面叙事。R1 建议在 Abstract 和 Contribution 3 中明确 "distribution-specific"，我完全支持。

**[REBUT] R1-W5: Perturbation robustness 在 ActorAttack 上不成立，建议移至 appendix**
部分不同意移至 appendix 的建议。理由：
1. ActorAttack 上的 perturbation 失败（experiments.tex line 272: 9-class Δ=-20.4±13.5pp）是论文最诚实的 negative result 之一。将 negative result 移到 appendix 会给审稿人"选择性报告"的印象，反而不利于论文。
2. 这个结果有实际意义：它表明即使 DAPT 改善了 clean detection（9-class F1=0.972 on ActorAttack），perturbation robustness 是一个正交维度，不被 DAPT 自动赋予。这对 practitioners 很重要。
3. 但我同意 R1 的隐含批评——当前 Section 5.5 的篇幅（约 1 页主文）相对其结论密度偏大。建议压缩为半页：保留 IID + DD 的正面结果和 ActorAttack 的 negative result，删去中间的逐 seed 分析细节（如 experiments.tex line 262 "9-class outperforms scrambled at seed 42 but the reverse holds at seed 456"），将这些移到 appendix。

**[AGREE] R1-W6: TF-IDF 在 DD 上的强表现削弱 DD 作为评估集的意义**
同意——与我自己的 W4 一致。补充：Table 3 (experiments.tex line 36-47) 作为论文的第一个结果表，以 IID Crescendo 和 OOD DD 为展示，但 DD 上 TF-IDF 达到 0.961（full）和 1.000（K=1-3）。这意味着论文的"核心结果"表展示的是一个 lexically solvable 的任务。ActorAttack 的结果（TF-IDF=0.261 vs 9-class=0.972）远更有说服力，但被安排在 Section 5.2 的后半段（experiments.tex line 127-137）。R1 建议将 ActorAttack 提升为主要展示集是正确的——Table 3 应同时包含 ActorAttack 列。

**[AGREE] R1-W7: 策略标注验证不充分**
同意。n=50 样本、单一人类标注者、κ=0.78 在标注质量验证中属于最低标准。Method (method.tex line 44) 称标注由 "Qwen3-8B with structured prompting" 完成，人类验证仅是 "a human sample"——未说明标注者的专业背景、标注指南、标注时间等。对于以策略分类为核心组件之一的论文，标注质量的验证需要更加严格。至少应增加第二个独立标注者以计算 inter-annotator agreement，或增加标注样本量。

---

## 对 R1 Questions 的补充意见

**Q3 (Mean pooling = BiGRU 对 discourse-level framing 的含义)**: 这是一个关键问题，与 N3 直接相关。如果 mean pooling（丢弃所有顺序信息）与 BiGRU（保留顺序信息）表现相当，那么 discourse-level structure（本质上是跨 turn 的时序关系）对检测没有贡献。这并不意味着 DAPT 无效，但意味着 DAPT 的作用可能在 per-turn representation 层面（使每个 turn 的 embedding 更具辨别力），而非论文叙事中暗示的 discourse-level。

**Q4 (Probing accuracy 与 detection F1 的 disconnect)**: experiments.tex line 190-191 报告 "9-class outperforms vanilla and MLM by 1-5pp" on linear probing, 但 detection F1 差距（MLM vs 9-class）在 DD 上仅 0.083pp (0.914 vs 0.997)，在 ActorAttack 上为 0.079pp (0.893 vs 0.972)。Probing 差异与 detection 差异的方向一致但量级不匹配，暗示 probing tasks 未捕获实际驱动检测的特征维度。这进一步支持了 N3 中"论文尚未识别出真正驱动检测的表征属性"的判断。

---

## 两位 Reviewer 的共识总结

R1 和 R2 在以下问题上完全一致（按严重性排序）：
1. **Figure 1 placeholder** (R1-N1, R2-N1): 必须补充
2. **Single-LLM confound + 人类数据逆转** (R1-N2 + R1-W4, R2-N3): 核心叙事面临的最大威胁
3. **TF-IDF 削弱 DD 评估** (R1-W6, R2-W4): 需要重组结果展示
4. **引用不足** (R1-缺失引用, R2-W3): DeBERTa-v3 论文、CKA 原始论文等
5. **数据规模和统计 power** (R1-W1/W2, R2-W2): 3-seed 不足以支撑方差对比

R1 独有的重要发现：
- **N3 (discourse-level claims)**: 这是一个我应该但未在自己的审稿中作为 critical 问题提出的重要观点。Mean pooling ≈ BiGRU 的结果与 discourse-level 叙事的矛盾需要论文直接回应。
- **N4 (DD n=80 vs 118)**: 数据报告的具体不一致，是审稿细致度的体现。
- **W2 (equivalence testing)**: 正确的统计方法学建议。

R2 独有的重要发现：
- **N2 (DAPT 新颖性不足)**: R1 给了 Overall 3.0 (Findings)，可能部分考虑了这个问题但未显式讨论新颖性。
- **N4 (缺少与现有方法的直接对比)**: R1 未明确提出，但对定位论文的实际价值至关重要。
- **W6 (analysis paper 深度不足)**: CKA 可视化、probing 表格、embedding 空间分析的缺失。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-18T18:14:49.597034+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-2 历史 issues（全部 resolved）\n  # ============================================================\n  - id: \"R1-N1\"\n    summary: \"Evidence hierarchy 统计基础不一致\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"binary/scrambled 仅 seed 42\"\n    action_items:\n      - round: 1\n        action: \"训练 binary/scrambled 3-seed\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"MF1 完成: binary 3-seed=0.997±0.005, scrambled 3-seed=0.997±0.005\"\n    resolution_round: 1\n\n  - id: \"R1-N2\"\n    summary: \"Three-layer robustness attribution 缺乏统计显著性\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提 N2\"\n    action_items:\n      - round: 1\n        action: \"McNemar's test + bootstrap CI\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"MF2 完成\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"缺少与已发表 multi-turn defense 的直接实验对比\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提 N3\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Round 1 修复不充分，再次提出\"\n    action_items:\n      - round: 1\n        action: \"重构论证\"\n        assigned_to: paper_agent\n        status: resolved\n      - round: 2\n        action: \"Analysis paper reframe 消解直接对比硬性要求\"\n        assigned_to: research_director\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N4\"\n    summary: \"数据集规模过小\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"n=80\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"500训练+76-118测试+3seeds仍不足\"\n    action_items:\n      - round: 1\n        action: \"降级 claim 为 preliminary\"\n        assigned_to: paper_agent\n        status: resolved\n      - round: 2\n        action: \"Bootstrap 95% CI + permutation test\"\n        assigned_to: main_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"有效 OOD 评估实质上是 single-dataset\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 首提\"\n    action_items:\n      - round: 1\n        action: \"ActorAttack OOD 数据生成\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"EXP-2 完成: ActorAttack 118 conversations\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Mean pooling=BiGRU 结论基于 single seed\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W1\"\n    action_items:\n      - round: 1\n        action: \"弱化因果性结论\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"Paper Agent 已弱化\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"策略标注质量验证不充分\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W2\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"n=50 单标注员仍不充分\"\n    action_items:\n      - round: 1\n        action: \"Limitations 讨论\"\n        assigned_to: paper_agent\n        status: resolved\n      - round: 2\n        action: \"扩展标注验证规模\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"LLM-as-judge baseline 仅测 IID\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W3\"\n    action_items:\n      - round: 1\n        action: \"DD/FITD OOD 评估\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"EXP-5 完成\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"TF-IDF LR 强表现未被充分讨论\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W4\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"升级为 critical，缺关键数据点\"\n    action_items:\n      - round: 1\n        action: \"诚实讨论 TF-IDF\"\n        assigned_to: paper_agent\n        status: resolved\n      - round: 2\n        action: \"TF-IDF 全 prefix + ActorAttack\"\n        assigned_to: main_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"可复现性不足\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Paper Agent 已添加 Appendix C\"\n    resolution_round: 1\n    mentions: []\n    action_items: []\n\n  - id: \"R2-W1\"\n    summary: \"Abstract 过度堆砌数据\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"仍有 12+ 数值\"\n    action_items:\n      - round: 2\n        action: \"保留 2-3 headline numbers\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2\"\n    summary: \"partially falsified 叙事对接收不利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Paper Agent 已重构\"\n    resolution_round: 1\n    mentions: []\n    action_items: []\n\n  - id: \"R2-W3\"\n    summary: \"Contributions 列表过于密集\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Paper Agent 已拆为 3 条\"\n    resolution_round: 1\n    mentions: []\n    action_items: []\n\n  - id: \"R2-W5\"\n    summary: \"Strategy trajectory 使用 ground-truth labels 而非模型预测\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"OOD κ=0.126, scope to IID\"\n    resolution_round: 1\n    mentions: []\n    action_items: []\n\n  - id: \"R2-W7\"\n    summary: \"Limitations 格式不符合 ACL/ARR\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"独立 Limitations section 已创建\"\n    resolution_round: 1\n    mentions: []\n    action_items: []\n\n  - id: \"R2-REF1\"\n    summary: \"缺失引用方向\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"新缺失引用被发现\"\n    action_items:\n      - round: 2\n        action: \"补充新缺失引用\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"SF12\"\n    summary: \"图表问题合集\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Paper Agent 已修复\"\n    resolution_round: 1\n    mentions: []\n    action_items: []\n\n  - id: \"R1-N1-v2\"\n    summary: \"单模型（Qwen3-8B）生成全部数据造成系统性 confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"整个 evidence hierarchy 可能是 artifact-driven\"\n    action_items:\n      - round: 2\n        action: \"ToxicChat 人类数据评估 (exp8)\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"exp8 ToxicChat completed. DA >> vanilla on human data. Caveat: single-turn only.\"\n    resolution_round: 2\n\n  - id: \"R2-N1-v2\"\n    summary: \"核心贡献新颖性不足：DAPT 在 jailbreak detection 的直接应用\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"headline result 是 DAPT 直接推论\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 维持 critical; R1 REBUT 建议降级为 should-fix，认为消融设计本身有增量（负面发现+等价性结果不能从 Don't Stop Pretraining 预测）\"\n    action_items:\n      - round: 2\n        action: \"Reframe 为 analysis paper\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 3\n        action: \"Framing 调整：强调'为什么替代方案失败'而非'DAPT 有效'；Contribution 1 改为关于消融负面发现\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N2-v2\"\n    summary: \"TF-IDF 0.944 削弱 discourse-level claim，缺 per-prefix 和 ActorAttack 数据\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"early detection 和 discourse-level claim 均 unsubstantiated\"\n    action_items:\n      - round: 2\n        action: \"TF-IDF per-prefix K=1,2,3,5 on DD + ActorAttack\"\n        assigned_to: main_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3-v2\"\n    summary: \"'Preliminary findings' 与 long paper 定位矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"删 preliminary 需同时扩大实验规模\"\n    action_items:\n      - round: 2\n        action: \"删除所有 preliminary + bootstrap CI 提升统计基础\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"所有 preliminary 已删除 + exp9 BCa bootstrap 95% CI + paired permutation test.\"\n    resolution_round: 2\n\n  - id: \"R1-N2-v2\"\n    summary: \"缺少与 DeepContext 等的直接实验对比（Round 1 修复不充分）\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"建议定位为分析框架 vs 方法论贡献\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2 维持 critical; R1 REBUT 认为 analysis paper 不应要求 SOTA comparison，但 Introduction 中 'replicating' vs Related Work 'not a direct proxy' 的自相矛盾必须修复\"\n    action_items:\n      - round: 2\n        action: \"Analysis paper reframe\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 3\n        action: \"修复 Introduction/Related Work 关于 vanilla baseline 与 DeepContext 关系的自相矛盾措辞\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3-v2\"\n    summary: \"数据规模不足以支撑 statistical claims\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"500训练+76-118测试+3seeds\"\n    action_items:\n      - round: 2\n        action: \"BCa bootstrap 95% CI + paired permutation test\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"exp9 完成\"\n    resolution_round: 2\n\n  - id: \"R2-W5-v2\"\n    summary: \"缺少 ACL ARR Responsible NLP Research Checklist（desk reject 风险）\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"desk reject 风险\"\n    action_items:\n      - round: 2\n        action: \"按 ARR 要求填写完整 checklist\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"checklist.tex 已添加\"\n    resolution_round: 2\n\n  - id: \"R2-W1-v2\"\n    summary: \"Related Work 包含大量本文实验数据\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"至少 3 处\"\n    action_items:\n      - round: 2\n        action: \"移除 Related Work 中本文数值\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"Related Work 已清理本文数值\"\n    resolution_round: 3\n\n  - id: \"R2-W2-v2\"\n    summary: \"Abstract 仍有 12+ 数值，数据过载\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Round 1 修复不充分\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"仍有 12+ 数值，两位 Reviewer 一致同意需压缩至 2-3 个 headline numbers\"\n    action_items:\n      - round: 2\n        action: \"保留 2-3 headline numbers\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3-v2\"\n    summary: \"ActorAttack 样本量未在 Section 4.1 中说明\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提\"\n    action_items:\n      - round: 2\n        action: \"补充 ActorAttack 118 对话\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"experiments.tex line 11 已包含 118 ActorAttack\"\n    resolution_round: 3\n\n  - id: \"R2-W4-v2\"\n    summary: \"Introduction 第四段结果段过于冗长\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"~200 词 15+ 数值\"\n    action_items:\n      - round: 2\n        action: \"压缩为 2-3 句\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1-v2\"\n    summary: \"TF-IDF 缺 per-prefix 和 ActorAttack 结果\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"与 R2-N2-v2 关联\"\n    action_items:\n      - round: 2\n        action: \"TF-IDF 全 prefix + ActorAttack\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"TF-IDF per-prefix + ActorAttack 结果已添加\"\n    resolution_round: 3\n\n  - id: \"R1-W2-v2\"\n    summary: \"BiGRU + frozen encoder 设计缺乏 justification\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"frozen 可能低估某些 variants 潜力\"\n    action_items:\n      - round: 2\n        action: \"Method 中增加 frozen 设计 justification\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"method.tex line 59-61 已添加 justification\"\n    resolution_round: 3\n\n  - id: \"R1-W3-v2\"\n    summary: \"LLM-as-judge baseline 仅 zero-shot\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"应补 few-shot\"\n    action_items:\n      - round: 2\n        action: \"补充 few-shot (3-shot) LLM-as-judge 评估\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"exp10 3-shot Qwen3-8B completed\"\n    resolution_round: 2\n\n  - id: \"R1-W4-v2\"\n    summary: \"策略标注质量验证不足：n=50 单标注员\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 n>=100 + 两个标注员\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 一致同意标注验证不足，至少需要第二个标注者或增加样本量\"\n    action_items:\n      - round: 2\n        action: \"扩展标注验证（P2，如时间允许）\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5-v2\"\n    summary: \"α=0.3 loss weight 未 justify\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"severity 低\"\n    action_items:\n      - round: 2\n        action: \"在 Method 中引用 lambda ablation 结果\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"method.tex line 44 已添加 α ablation 结果\"\n    resolution_round: 3\n\n  - id: \"R2-W6-v2\"\n    summary: \"页数可能超限\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需编译验证\"\n    action_items:\n      - round: 2\n        action: \"检查编译后页数\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W7-v2\"\n    summary: \"Figure 3 浮动位置可能异常\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Minor LaTeX issue\"\n    action_items:\n      - round: 2\n        action: \"检查 Figure 3 浮动\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"CROSS-Q5\"\n    summary: \"Topic classification 5-class 与 benign topic 一致，存在 shortcut confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"method.tex:50 vs appendix.tex:139 完全一致\"\n    action_items:\n      - round: 2\n        action: \"Discussion 中三层反驳论证\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"Discussion 'Topic shortcut confound' paragraph added\"\n    resolution_round: 3\n\n  - id: \"R2-TERM\"\n    summary: \"术语不一致：domain exposure / domain adaptation 等混用\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [2]\n        note: \"minor\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 同意需统一术语；R1 补充 'evidence hierarchy' 和 'DisPeD' 全称也需定义\"\n    action_items:\n      - round: 2\n        action: \"统一术语\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-REF2\"\n    summary: \"缺失引用：Persuasion for Good, SmoothLLM, TAP 等\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"高优先级 6 条 + 中优先级 3 条\"\n    action_items:\n      - round: 2\n        action: \"补充缺失引用\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"Round 2 缺失引用已补充到 references.bib\"\n    resolution_round: 3\n\n  - id: \"R1-CAPACITY\"\n    summary: \"DeBERTa-v3 vs RoBERTa capacity confound\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"184M vs 125M\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 一致同意需在 Contribution 列表和 Conclusion 对 Finding 2 加限定词\"\n    action_items:\n      - round: 2\n        action: \"Discussion 中诚实承认 + future work\"\n        assigned_to: paper_agent\n        status: resolved\n      - round: 3\n        action: \"在 Contribution 2 和 Abstract 中对 difficulty threshold claim 添加 capacity caveat\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-BIB\"\n    summary: \"引用格式问题\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [2]\n        note: \"austin1962, chao2023pair, han2024wildguard\"\n    action_items:\n      - round: 2\n        action: \"核查并修正 bib 条目\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 3 新 issues\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"Figure 1 为 placeholder，论文未完成状态\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"method.tex line 10, 'Architecture diagram placeholder'。两位 Reviewer 独立发现，交叉回应完全一致。desk reject 风险。\"\n    action_items:\n      - round: 3\n        action: \"绘制完整架构图：Stage 1（七个变体训练目标分支）→ frozen encoder → Stage 2 BiGRU → MLP classification\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N2\"\n    summary: \"Single-LLM confound：训练和全部 OOD 数据均由 Qwen3-8B 生成，cross-attack generalization claim 范围过宽\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 作为 N2 提出，R2 作为 N3 的关联问题提出。交叉回应完全一致。ToxicChat 仅验证最弱 claim（DA>vanilla），未验证证据层级排序。\"\n    action_items:\n      - round: 3\n        action: \"(1) 用至少一个其他 LLM 生成部分 OOD 评估数据，或使用 MHJ 真实多轮人类 jailbreak 数据；(2) 若不可行，在标题、Abstract、Conclusion 中限定 claim 范围为 within synthetic data manifold\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N3\"\n    summary: \"证据层级在人类数据（ToxicChat）上完全逆转，动摇 'classification as regularizer' 核心叙事\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2 作为 N3 提出（critical），R1 先作为 W4 提出后在交叉回应中升级为 critical。Table 5: JB-MLM(0.837) >> 9-class(0.596)。所有含 classification objective 的变体均低于纯 MLM，严格按分类复杂度递减排序。论文的 'modality mismatch' 解释不充分（Binary/Scrambled 也应有 domain exposure 但仍弱于 MLM）。更合理解释：classification supervision 过拟合到合成分布。Abstract/Introduction 中 Finding 3 表述未反映 Discussion 中 'distribution-specific' 限定。\"\n    action_items:\n      - round: 3\n        action: \"(1) 在 Abstract 和 Contribution 3 中明确 'classification supervision 的 regularization 是 distribution-specific 的'；(2) 将人类数据逆转作为核心发现之一而非例外；(3) 增加多轮人类数据评估\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N4\"\n    summary: \"'Discourse-level' claims 缺乏直接证据，存在 overclaiming\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 作为 N3 提出，R2 在交叉回应中强烈同意并升级严重性。(1) experiments.tex line 107 声称 DAPT 捕获 'pragmatic features' 但无 probing 支持；(2) mean pooling ≈ BiGRU（丢弃顺序信息等效）与 discourse-level 叙事矛盾；(3) Related Work 将 probing classifiers 留给 future work，对 analysis paper 是重大缺陷；(4) 'beyond BoW' ≠ 'discourse-level'，可能是 longer n-gram / sub-word / intra-sentence syntax。\"\n    action_items:\n      - round: 3\n        action: \"(1) 增加 discourse-level diagnostic probing（跨 turn 一致性、escalation 阶段）或 (2) 将所有 'discourse-level' / 'pragmatic features' 降级为 'features beyond lexical overlap'\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N5\"\n    summary: \"DD 评估样本量 n=80 vs n=118 矛盾，数据划分（benign 样本数/来源）不透明\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 作为 N4 提出，R2 交叉回应确认并补充 IID benign test set 也未说明。experiments.tex line 11 说 80 DD，line 265 说 n=118。可能是 80 jailbreak + 38 benign = 118？但 benign 来源未交代。\"\n    action_items:\n      - round: 3\n        action: \"在 Setup 中明确每个评估集的完整构成（jailbreak + benign 数量和来源）\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W1\"\n    summary: \"3-seed variance estimation 不可靠，'4-20× variance reduction' claim 统计基础薄弱\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"std 基于 3 seeds 的相对误差约 50%。MLM DD-Full std=0.115 主要由 seed 456 驱动。population std vs sample std 在 n=3 时差异显著（18%）。\"\n    action_items:\n      - round: 3\n        action: \"增加到 5-10 seeds 验证 variance reduction claim，或对 '4-20×' 添加显著的 uncertainty caveat\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W2\"\n    summary: \"McNemar's test 在 sparse discordant pairs (≤7) 上无统计效力，被误用为等价性证据\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 强烈同意并指出逻辑矛盾：p>0.13 用于支持 'non-factors' claim，但同时承认 power 不足。建议 equivalence testing (TOST)。\"\n    action_items:\n      - round: 3\n        action: \"补充 equivalence test (TOST 或 Bayesian approach)，或在每次引用 McNemar 时标注 power 限制\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W3\"\n    summary: \"TF-IDF 在 DD 上 F1≥0.961 削弱 DD 作为核心评估集，消融可信度过度依赖单一 ActorAttack\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立提出且交叉一致。Table 3 以 DD 为中心但 DD 是 lexically solvable。ActorAttack 是唯一区分 lexical/beyond-lexical 的评估集，且恰好是 perturbation robustness 崩溃的评估集。\"\n    action_items:\n      - round: 3\n        action: \"将 ActorAttack 提升为主要展示评估集（Table 3 增加 ActorAttack 列）；在叙事中更早承认 DD lexical separability\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W4\"\n    summary: \"Analysis paper 深度不足：CKA 无可视化、probing 无表格、无 embedding 空间分析\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2 作为 W6 提出，R1 在交叉回应中同意并关联到 discourse-level claim。CKA 仅一段描述（Section 5.3），linear probing 仅一句（line 190-191），无 t-SNE/UMAP，无 attention pattern。\"\n    action_items:\n      - round: 3\n        action: \"增加 CKA 矩阵热力图、probing 详细表格、embedding 空间 t-SNE/UMAP 可视化\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W5\"\n    summary: \"Introduction 与 Related Work 关于 vanilla baseline 与 DeepContext 关系的自相矛盾\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2 作为 N4 提出（critical），R1 REBUT 认为 analysis paper 不需 SOTA comparison 但语言矛盾是 must-fix。Introduction 'replicating' vs Related Work 'not a direct proxy'。\"\n    action_items:\n      - round: 3\n        action: \"统一措辞：vanilla baseline 代表 'pretrained-encoder-plus-RNN without domain adaptation' 这一类方法，而非特定复现 DeepContext\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W6\"\n    summary: \"引用不足：DeBERTa-v3 正确论文、ELECTRA、CKA、Qwen3-8B 等关键引用缺失\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立提出。必须补充：He et al. (2023) DeBERTa-v3, Clark et al. (2020) ELECTRA, Kornblith et al. (2019) CKA, Qwen3-8B 官方引用。建议补充：Bai et al. (2022) RLHF, Jain et al. (2023) Baseline Defenses, Qi et al. (2024)。总引用量 31 条对 EMNLP 偏低。\"\n    action_items:\n      - round: 3\n        action: \"补充必要引用（DeBERTa-v3, ELECTRA, CKA, Qwen3-8B）+ 建议引用\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W7\"\n    summary: \"Perturbation analysis 占 ~1 页但结论为 'attack-family-dependent'，性价比低\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 建议移至 appendix，R2 REBUT 认为 negative result 应留正文但建议压缩为半页。两位同意当前篇幅过长。\"\n    action_items:\n      - round: 3\n        action: \"压缩 Section 5.5 为半页：保留 IID+DD 正面结果和 ActorAttack negative result，删逐 seed 细节移至 appendix\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M1\"\n    summary: \"MLM-only 部分结果缺 std，seed 数不明确\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Table 3 IID MLM-only 0.974/1.000 无 std；两位 Reviewer 均指出\"\n    action_items:\n      - round: 3\n        action: \"统一为 3-seed 报告或注明单 seed\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M2\"\n    summary: \"Qwen3-8B 广泛使用但 references.bib 中无引用\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"数据生成、标注、paraphrasing、LLM baseline 均依赖 Qwen3-8B\"\n    action_items:\n      - round: 3\n        action: \"添加 Qwen3-8B 正式引用\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M3\"\n    summary: \"DisPeD 全称从未给出\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Introduction line 12 定义了 DisPeD 但未展开全称\"\n    action_items:\n      - round: 3\n        action: \"给出 DisPeD 全称\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M4\"\n    summary: \"Population std (N divisor) vs sample std (N-1) 选择未 justify\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"n=3 时差异 18%，仅在括号中一笔带过\"\n    action_items:\n      - round: 3\n        action: \"说明选择理由或改用 sample std\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-2 历史 issues（全部 resolved）\n  # ============================================================\n  - id: \"R1-N1\"\n    summary: \"Evidence hierarchy 统计基础不一致\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"binary/scrambled 仅 seed 42\"\n    action_items:\n      - round: 1\n        action: \"训练 binary/scrambled 3-seed\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"MF1 完成: binary 3-seed=0.997±0.005, scrambled 3-seed=0.997±0.005\"\n    resolution_round: 1\n\n  - id: \"R1-N2\"\n    summary: \"Three-layer robustness attribution 缺乏统计显著性\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提 N2\"\n    action_items:\n      - round: 1\n        action: \"McNemar's test + bootstrap CI\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"MF2 完成\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"缺少与已发表 multi-turn defense 的直接实验对比\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提 N3\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Round 1 修复不充分，再次提出\"\n    action_items:\n      - round: 1\n        action: \"重构论证\"\n        assigned_to: paper_agent\n        status: resolved\n      - round: 2\n        action: \"Analysis paper reframe 消解直接对比硬性要求\"\n        assigned_to: research_director\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N4\"\n    summary: \"数据集规模过小\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"n=80\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"500训练+76-118测试+3seeds仍不足\"\n    action_items:\n      - round: 1\n        action: \"降级 claim 为 preliminary\"\n        assigned_to: paper_agent\n        status: resolved\n      - round: 2\n        action: \"Bootstrap 95% CI + permutation test\"\n        assigned_to: main_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"有效 OOD 评估实质上是 single-dataset\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 首提\"\n    action_items:\n      - round: 1\n        action: \"ActorAttack OOD 数据生成\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"EXP-2 完成: ActorAttack 118 conversations\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Mean pooling=BiGRU 结论基于 single seed\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W1\"\n    action_items:\n      - round: 1\n        action: \"弱化因果性结论\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"Paper Agent 已弱化\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"策略标注质量验证不充分\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W2\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"n=50 单标注员仍不充分\"\n    action_items:\n      - round: 1\n        action: \"Limitations 讨论\"\n        assigned_to: paper_agent\n        status: resolved\n      - round: 2\n        action: \"扩展标注验证规模\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"LLM-as-judge baseline 仅测 IID\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W3\"\n    action_items:\n      - round: 1\n        action: \"DD/FITD OOD 评估\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"EXP-5 完成\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"TF-IDF LR 强表现未被充分讨论\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 W4\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"升级为 critical，缺关键数据点\"\n    action_items:\n      - round: 1\n        action: \"诚实讨论 TF-IDF\"\n        assigned_to: paper_agent\n        status: resolved\n      - round: 2\n        action: \"TF-IDF 全 prefix + ActorAttack\"\n        assigned_to: main_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"可复现性不足\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Paper Agent 已添加 Appendix C\"\n    resolution_round: 1\n    mentions: []\n    action_items: []\n\n  - id: \"R2-W1\"\n    summary: \"Abstract 过度堆砌数据\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"仍有 12+ 数值\"\n    action_items:\n      - round: 2\n        action: \"保留 2-3 headline numbers\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2\"\n    summary: \"partially falsified 叙事对接收不利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Paper Agent 已重构\"\n    resolution_round: 1\n    mentions: []\n    action_items: []\n\n  - id: \"R2-W3\"\n    summary: \"Contributions 列表过于密集\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Paper Agent 已拆为 3 条\"\n    resolution_round: 1\n    mentions: []\n    action_items: []\n\n  - id: \"R2-W5\"\n    summary: \"Strategy trajectory 使用 ground-truth labels 而非模型预测\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"OOD κ=0.126, scope to IID\"\n    resolution_round: 1\n    mentions: []\n    action_items: []\n\n  - id: \"R2-W7\"\n    summary: \"Limitations 格式不符合 ACL/ARR\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"独立 Limitations section 已创建\"\n    resolution_round: 1\n    mentions: []\n    action_items: []\n\n  - id: \"R2-REF1\"\n    summary: \"缺失引用方向\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"新缺失引用被发现\"\n    action_items:\n      - round: 2\n        action: \"补充新缺失引用\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"SF12\"\n    summary: \"图表问题合集\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Paper Agent 已修复\"\n    resolution_round: 1\n    mentions: []\n    action_items: []\n\n  - id: \"R1-N1-v2\"\n    summary: \"单模型（Qwen3-8B）生成全部数据造成系统性 confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"整个 evidence hierarchy 可能是 artifact-driven\"\n    action_items:\n      - round: 2\n        action: \"ToxicChat 人类数据评估 (exp8)\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"exp8 ToxicChat completed. DA >> vanilla on human data. Caveat: single-turn only.\"\n    resolution_round: 2\n\n  - id: \"R2-N1-v2\"\n    summary: \"核心贡献新颖性不足：DAPT 在 jailbreak detection 的直接应用\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"headline result 是 DAPT 直接推论\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 维持 critical; R1 REBUT 建议降级为 should-fix，认为消融设计本身有增量（负面发现+等价性结果不能从 Don't Stop Pretraining 预测）\"\n    action_items:\n      - round: 2\n        action: \"Reframe 为 analysis paper\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 3\n        action: \"Framing 调整：强调'为什么替代方案失败'而非'DAPT 有效'；Contribution 1 改为关于消融负面发现\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N2-v2\"\n    summary: \"TF-IDF 0.944 削弱 discourse-level claim，缺 per-prefix 和 ActorAttack 数据\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"early detection 和 discourse-level claim 均 unsubstantiated\"\n    action_items:\n      - round: 2\n        action: \"TF-IDF per-prefix K=1,2,3,5 on DD + ActorAttack\"\n        assigned_to: main_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3-v2\"\n    summary: \"'Preliminary findings' 与 long paper 定位矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"删 preliminary 需同时扩大实验规模\"\n    action_items:\n      - round: 2\n        action: \"删除所有 preliminary + bootstrap CI 提升统计基础\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"所有 preliminary 已删除 + exp9 BCa bootstrap 95% CI + paired permutation test.\"\n    resolution_round: 2\n\n  - id: \"R1-N2-v2\"\n    summary: \"缺少与 DeepContext 等的直接实验对比（Round 1 修复不充分）\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"建议定位为分析框架 vs 方法论贡献\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2 维持 critical; R1 REBUT 认为 analysis paper 不应要求 SOTA comparison，但 Introduction 中 'replicating' vs Related Work 'not a direct proxy' 的自相矛盾必须修复\"\n    action_items:\n      - round: 2\n        action: \"Analysis paper reframe\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 3\n        action: \"修复 Introduction/Related Work 关于 vanilla baseline 与 DeepContext 关系的自相矛盾措辞\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3-v2\"\n    summary: \"数据规模不足以支撑 statistical claims\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"500训练+76-118测试+3seeds\"\n    action_items:\n      - round: 2\n        action: \"BCa bootstrap 95% CI + paired permutation test\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"exp9 完成\"\n    resolution_round: 2\n\n  - id: \"R2-W5-v2\"\n    summary: \"缺少 ACL ARR Responsible NLP Research Checklist（desk reject 风险）\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"desk reject 风险\"\n    action_items:\n      - round: 2\n        action: \"按 ARR 要求填写完整 checklist\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"checklist.tex 已添加\"\n    resolution_round: 2\n\n  - id: \"R2-W1-v2\"\n    summary: \"Related Work 包含大量本文实验数据\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"至少 3 处\"\n    action_items:\n      - round: 2\n        action: \"移除 Related Work 中本文数值\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"Related Work 已清理本文数值\"\n    resolution_round: 3\n\n  - id: \"R2-W2-v2\"\n    summary: \"Abstract 仍有 12+ 数值，数据过载\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Round 1 修复不充分\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"仍有 12+ 数值，两位 Reviewer 一致同意需压缩至 2-3 个 headline numbers\"\n    action_items:\n      - round: 2\n        action: \"保留 2-3 headline numbers\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3-v2\"\n    summary: \"ActorAttack 样本量未在 Section 4.1 中说明\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提\"\n    action_items:\n      - round: 2\n        action: \"补充 ActorAttack 118 对话\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"experiments.tex line 11 已包含 118 ActorAttack\"\n    resolution_round: 3\n\n  - id: \"R2-W4-v2\"\n    summary: \"Introduction 第四段结果段过于冗长\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"~200 词 15+ 数值\"\n    action_items:\n      - round: 2\n        action: \"压缩为 2-3 句\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1-v2\"\n    summary: \"TF-IDF 缺 per-prefix 和 ActorAttack 结果\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"与 R2-N2-v2 关联\"\n    action_items:\n      - round: 2\n        action: \"TF-IDF 全 prefix + ActorAttack\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"TF-IDF per-prefix + ActorAttack 结果已添加\"\n    resolution_round: 3\n\n  - id: \"R1-W2-v2\"\n    summary: \"BiGRU + frozen encoder 设计缺乏 justification\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"frozen 可能低估某些 variants 潜力\"\n    action_items:\n      - round: 2\n        action: \"Method 中增加 frozen 设计 justification\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"method.tex line 59-61 已添加 justification\"\n    resolution_round: 3\n\n  - id: \"R1-W3-v2\"\n    summary: \"LLM-as-judge baseline 仅 zero-shot\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"应补 few-shot\"\n    action_items:\n      - round: 2\n        action: \"补充 few-shot (3-shot) LLM-as-judge 评估\"\n        assigned_to: main_agent\n        status: resolved\n    resolution: \"exp10 3-shot Qwen3-8B completed\"\n    resolution_round: 2\n\n  - id: \"R1-W4-v2\"\n    summary: \"策略标注质量验证不足：n=50 单标注员\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 n>=100 + 两个标注员\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 一致同意标注验证不足，至少需要第二个标注者或增加样本量\"\n    action_items:\n      - round: 2\n        action: \"扩展标注验证（P2，如时间允许）\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5-v2\"\n    summary: \"α=0.3 loss weight 未 justify\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"severity 低\"\n    action_items:\n      - round: 2\n        action: \"在 Method 中引用 lambda ablation 结果\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"method.tex line 44 已添加 α ablation 结果\"\n    resolution_round: 3\n\n  - id: \"R2-W6-v2\"\n    summary: \"页数可能超限\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需编译验证\"\n    action_items:\n      - round: 2\n        action: \"检查编译后页数\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W7-v2\"\n    summary: \"Figure 3 浮动位置可能异常\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Minor LaTeX issue\"\n    action_items:\n      - round: 2\n        action: \"检查 Figure 3 浮动\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"CROSS-Q5\"\n    summary: \"Topic classification 5-class 与 benign topic 一致，存在 shortcut confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"method.tex:50 vs appendix.tex:139 完全一致\"\n    action_items:\n      - round: 2\n        action: \"Discussion 中三层反驳论证\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"Discussion 'Topic shortcut confound' paragraph added\"\n    resolution_round: 3\n\n  - id: \"R2-TERM\"\n    summary: \"术语不一致：domain exposure / domain adaptation 等混用\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [2]\n        note: \"minor\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 同意需统一术语；R1 补充 'evidence hierarchy' 和 'DisPeD' 全称也需定义\"\n    action_items:\n      - round: 2\n        action: \"统一术语\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-REF2\"\n    summary: \"缺失引用：Persuasion for Good, SmoothLLM, TAP 等\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"高优先级 6 条 + 中优先级 3 条\"\n    action_items:\n      - round: 2\n        action: \"补充缺失引用\"\n        assigned_to: paper_agent\n        status: resolved\n    resolution: \"Round 2 缺失引用已补充到 references.bib\"\n    resolution_round: 3\n\n  - id: \"R1-CAPACITY\"\n    summary: \"DeBERTa-v3 vs RoBERTa capacity confound\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"184M vs 125M\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 一致同意需在 Contribution 列表和 Conclusion 对 Finding 2 加限定词\"\n    action_items:\n      - round: 2\n        action: \"Discussion 中诚实承认 + future work\"\n        assigned_to: paper_agent\n        status: resolved\n      - round: 3\n        action: \"在 Contribution 2 和 Abstract 中对 difficulty threshold claim 添加 capacity caveat\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-BIB\"\n    summary: \"引用格式问题\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [2]\n        note: \"austin1962, chao2023pair, han2024wildguard\"\n    action_items:\n      - round: 2\n        action: \"核查并修正 bib 条目\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 3 新 issues\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"Figure 1 为 placeholder，论文未完成状态\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"method.tex line 10, 'Architecture diagram placeholder'。两位 Reviewer 独立发现，交叉回应完全一致。desk reject 风险。\"\n    action_items:\n      - round: 3\n        action: \"绘制完整架构图：Stage 1（七个变体训练目标分支）→ frozen encoder → Stage 2 BiGRU → MLP classification\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N2\"\n    summary: \"Single-LLM confound：训练和全部 OOD 数据均由 Qwen3-8B 生成，cross-attack generalization claim 范围过宽\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 作为 N2 提出，R2 作为 N3 的关联问题提出。交叉回应完全一致。ToxicChat 仅验证最弱 claim（DA>vanilla），未验证证据层级排序。\"\n    action_items:\n      - round: 3\n        action: \"(1) 用至少一个其他 LLM 生成部分 OOD 评估数据，或使用 MHJ 真实多轮人类 jailbreak 数据；(2) 若不可行，在标题、Abstract、Conclusion 中限定 claim 范围为 within synthetic data manifold\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N3\"\n    summary: \"证据层级在人类数据（ToxicChat）上完全逆转，动摇 'classification as regularizer' 核心叙事\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2 作为 N3 提出（critical），R1 先作为 W4 提出后在交叉回应中升级为 critical。Table 5: JB-MLM(0.837) >> 9-class(0.596)。所有含 classification objective 的变体均低于纯 MLM，严格按分类复杂度递减排序。论文的 'modality mismatch' 解释不充分（Binary/Scrambled 也应有 domain exposure 但仍弱于 MLM）。更合理解释：classification supervision 过拟合到合成分布。Abstract/Introduction 中 Finding 3 表述未反映 Discussion 中 'distribution-specific' 限定。\"\n    action_items:\n      - round: 3\n        action: \"(1) 在 Abstract 和 Contribution 3 中明确 'classification supervision 的 regularization 是 distribution-specific 的'；(2) 将人类数据逆转作为核心发现之一而非例外；(3) 增加多轮人类数据评估\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N4\"\n    summary: \"'Discourse-level' claims 缺乏直接证据，存在 overclaiming\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 作为 N3 提出，R2 在交叉回应中强烈同意并升级严重性。(1) experiments.tex line 107 声称 DAPT 捕获 'pragmatic features' 但无 probing 支持；(2) mean pooling ≈ BiGRU（丢弃顺序信息等效）与 discourse-level 叙事矛盾；(3) Related Work 将 probing classifiers 留给 future work，对 analysis paper 是重大缺陷；(4) 'beyond BoW' ≠ 'discourse-level'，可能是 longer n-gram / sub-word / intra-sentence syntax。\"\n    action_items:\n      - round: 3\n        action: \"(1) 增加 discourse-level diagnostic probing（跨 turn 一致性、escalation 阶段）或 (2) 将所有 'discourse-level' / 'pragmatic features' 降级为 'features beyond lexical overlap'\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N5\"\n    summary: \"DD 评估样本量 n=80 vs n=118 矛盾，数据划分（benign 样本数/来源）不透明\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 作为 N4 提出，R2 交叉回应确认并补充 IID benign test set 也未说明。experiments.tex line 11 说 80 DD，line 265 说 n=118。可能是 80 jailbreak + 38 benign = 118？但 benign 来源未交代。\"\n    action_items:\n      - round: 3\n        action: \"在 Setup 中明确每个评估集的完整构成（jailbreak + benign 数量和来源）\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W1\"\n    summary: \"3-seed variance estimation 不可靠，'4-20× variance reduction' claim 统计基础薄弱\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"std 基于 3 seeds 的相对误差约 50%。MLM DD-Full std=0.115 主要由 seed 456 驱动。population std vs sample std 在 n=3 时差异显著（18%）。\"\n    action_items:\n      - round: 3\n        action: \"增加到 5-10 seeds 验证 variance reduction claim，或对 '4-20×' 添加显著的 uncertainty caveat\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W2\"\n    summary: \"McNemar's test 在 sparse discordant pairs (≤7) 上无统计效力，被误用为等价性证据\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 强烈同意并指出逻辑矛盾：p>0.13 用于支持 'non-factors' claim，但同时承认 power 不足。建议 equivalence testing (TOST)。\"\n    action_items:\n      - round: 3\n        action: \"补充 equivalence test (TOST 或 Bayesian approach)，或在每次引用 McNemar 时标注 power 限制\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W3\"\n    summary: \"TF-IDF 在 DD 上 F1≥0.961 削弱 DD 作为核心评估集，消融可信度过度依赖单一 ActorAttack\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立提出且交叉一致。Table 3 以 DD 为中心但 DD 是 lexically solvable。ActorAttack 是唯一区分 lexical/beyond-lexical 的评估集，且恰好是 perturbation robustness 崩溃的评估集。\"\n    action_items:\n      - round: 3\n        action: \"将 ActorAttack 提升为主要展示评估集（Table 3 增加 ActorAttack 列）；在叙事中更早承认 DD lexical separability\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W4\"\n    summary: \"Analysis paper 深度不足：CKA 无可视化、probing 无表格、无 embedding 空间分析\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2 作为 W6 提出，R1 在交叉回应中同意并关联到 discourse-level claim。CKA 仅一段描述（Section 5.3），linear probing 仅一句（line 190-191），无 t-SNE/UMAP，无 attention pattern。\"\n    action_items:\n      - round: 3\n        action: \"增加 CKA 矩阵热力图、probing 详细表格、embedding 空间 t-SNE/UMAP 可视化\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W5\"\n    summary: \"Introduction 与 Related Work 关于 vanilla baseline 与 DeepContext 关系的自相矛盾\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2 作为 N4 提出（critical），R1 REBUT 认为 analysis paper 不需 SOTA comparison 但语言矛盾是 must-fix。Introduction 'replicating' vs Related Work 'not a direct proxy'。\"\n    action_items:\n      - round: 3\n        action: \"统一措辞：vanilla baseline 代表 'pretrained-encoder-plus-RNN without domain adaptation' 这一类方法，而非特定复现 DeepContext\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W6\"\n    summary: \"引用不足：DeBERTa-v3 正确论文、ELECTRA、CKA、Qwen3-8B 等关键引用缺失\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立提出。必须补充：He et al. (2023) DeBERTa-v3, Clark et al. (2020) ELECTRA, Kornblith et al. (2019) CKA, Qwen3-8B 官方引用。建议补充：Bai et al. (2022) RLHF, Jain et al. (2023) Baseline Defenses, Qi et al. (2024)。总引用量 31 条对 EMNLP 偏低。\"\n    action_items:\n      - round: 3\n        action: \"补充必要引用（DeBERTa-v3, ELECTRA, CKA, Qwen3-8B）+ 建议引用\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W7\"\n    summary: \"Perturbation analysis 占 ~1 页但结论为 'attack-family-dependent'，性价比低\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 建议移至 appendix，R2 REBUT 认为 negative result 应留正文但建议压缩为半页。两位同意当前篇幅过长。\"\n    action_items:\n      - round: 3\n        action: \"压缩 Section 5.5 为半页：保留 IID+DD 正面结果和 ActorAttack negative result，删逐 seed 细节移至 appendix\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M1\"\n    summary: \"MLM-only 部分结果缺 std，seed 数不明确\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Table 3 IID MLM-only 0.974/1.000 无 std；两位 Reviewer 均指出\"\n    action_items:\n      - round: 3\n        action: \"统一为 3-seed 报告或注明单 seed\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M2\"\n    summary: \"Qwen3-8B 广泛使用但 references.bib 中无引用\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"数据生成、标注、paraphrasing、LLM baseline 均依赖 Qwen3-8B\"\n    action_items:\n      - round: 3\n        action: \"添加 Qwen3-8B 正式引用\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M3\"\n    summary: \"DisPeD 全称从未给出\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Introduction line 12 定义了 DisPeD 但未展开全称\"\n    action_items:\n      - round: 3\n        action: \"给出 DisPeD 全称\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M4\"\n    summary: \"Population std (N divisor) vs sample std (N-1) 选择未 justify\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"n=3 时差异 18%，仅在括号中一笔带过\"\n    action_items:\n      - round: 3\n        action: \"说明选择理由或改用 sample std\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-18T18:14:49.701759+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/review_issues.yaml\", \"bytes\": 29959}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 104
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-18T18:17:51.053103+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject",
  "report": "# 圆桌审稿汇总报告 — Round 3 (Fresh)\n\n**论文**: \"What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap\"\n**目标 Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作）\n**审稿轮次**: Round 1 独立审稿 + 交叉分享，1 轮收敛\n**外部审稿**: 未启用\n\n---\n\n## Summary\n\n本文通过控制性消融研究，分析什么表示属性使 multi-turn jailbreak 检测跨攻击族泛化。设计七个 DeBERTa-v3 Stage-1 变体和三个 RoBERTa 变体（统称 DisPeD），在四个攻击族（Crescendo, FITD, DD, ActorAttack）上评估，得出三个发现：(1) DAPT 是 OOD 泛化主要机制（~60pp gap on DeBERTa-v3）；(2) encoder 预训练方法决定 DAPT 变得关键的难度阈值；(3) 分类监督起正则化作用而非策略分类作用。ToxicChat 验证表明 DAPT 优势迁移至 human-written 数据，但证据层级在人类数据上完全逆转。\n\n---\n\n## Strengths\n\n**S1. 消融设计精良。** 七个 Stage-1 变体系统隔离五个因素（domain exposure, classification supervision, label quality, granularity, domain specificity），每个变体的对比意义清晰。加上两个 encoder 架构的交叉验证，构成教科书级消融矩阵。[R1, R2 一致]\n\n**S2. 统计方法论严谨。** 3-seed 评估、McNemar's test、BCa bootstrap CI（10,000 resamples）、paired permutation test 的组合使用超过大多数 EMNLP 投稿的统计标准。主动报告 effect size 不显著的结果（分类变体间 McNemar all p>0.13）。[R1, R2 一致]\n\n**S3. \"分类作为正则化器\"发现具有反直觉价值。** Scrambled labels = correct labels 在所有 OOD 评估上等效（gap ≤3.9pp），而 OOD 策略预测精度仅 30.7%（κ=0.126）。挑战了\"需要好标签才能泛化\"的朴素假设。[R1]\n\n**S4. 诚实报告负面结果。** Perturbation robustness 在 ActorAttack 上不成立、variance reversal 在 ToxicChat 上出现、McNemar power 限制被明确讨论。这种透明度值得肯定。[R1, R2 一致]\n\n**S5. 极低计算成本，可复现性好。** 全部变体 <4 GPU-hours，超参数完整报告（Appendix D），承诺开源。[R1, R2 一致]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [critical] Figure 1 为 placeholder，论文未完成状态**\n- method.tex line 10: `\\fbox{\\parbox{...}{Architecture diagram placeholder}}`\n- 主架构图是空框。对于以 \"systematic decomposition\" 为核心的论文，架构图是理解七个变体关系的关键工具。\n- desk reject 风险。\n- [R1-N1, R2-N1: 两位 Reviewer 独立发现，交叉回应 **完全一致**]\n\n**MF2. [critical] Single-LLM confound：cross-attack generalization claim 范围过宽**\n- 训练数据和全部 OOD 评估数据（FITD, DD, ActorAttack）均由 Qwen3-8B 生成。\"cross-attack generalization\" 实际上是 \"within Qwen3-8B generation distribution\" 的泛化。\n- ToxicChat 验证仅覆盖最弱 claim（DA > vanilla），未验证核心证据层级排序。且 ToxicChat 是单轮数据。\n- 建议：(a) 用至少一个其他 LLM 生成 OOD 评估数据，或使用 MHJ 真实多轮人类 jailbreak 数据；(b) 若不可行，在标题/Abstract/Conclusion 中限定 claim 范围。\n- [R1-N2, R2-N3 关联: **完全一致**]\n\n**MF3. [critical] 证据层级在人类数据上完全逆转，动摇核心叙事**\n- ToxicChat (Table 5): JB-MLM (0.837±0.013) >> Binary (0.705) >> 9-class (0.596±0.087)。所有含 classification objective 的变体均低于纯 MLM，严格按分类复杂度递减排序。\n- 论文的 \"modality mismatch\" 解释不充分：如果好处仅限于多轮正则化，Binary 和 Scrambled 不应低于 MLM（它们有相同的 domain exposure）。更合理解释：classification supervision 过拟合到合成分布的 decision boundaries。\n- Discussion 中 \"distribution-specific regularization\" 分析与 Abstract/Introduction 的 Finding 3 表述不一致。\n- 建议：(a) 在 Abstract 和 Contribution 3 中明确 \"distribution-specific\"；(b) 将逆转作为核心发现之一而非例外；(c) 增加多轮人类数据评估。\n- [R2-N3 critical, R1-W4 → 交叉后升级为 critical: **完全一致**]\n\n**MF4. [critical] \"Discourse-level\" claims 缺乏直接证据，存在系统性 overclaiming**\n- experiments.tex line 107 声称 DAPT 捕获 \"pragmatic features (hedging, escalation markers, topic-shifting patterns)\"，但无 probing 支持。\n- mean pooling ≈ BiGRU（单 seed）：如果丢弃顺序信息不影响检测，discourse-level structure 体现在哪里？\n- Related Work 将 probing classifiers 留给 future work，对自称 analysis paper 是重大缺陷。\n- \"beyond bag-of-words\"（TF-IDF on ActorAttack 失败）≠ \"discourse-level\"，可能是 longer n-gram、sub-word、intra-sentence syntax。\n- linear probing 结果（9-class vs vanilla/MLM 仅 1-5pp）与 detection F1 巨大差距的 disconnect 暗示 probing tasks 未捕获驱动检测的特征。\n- 建议：增加 discourse-level diagnostic probing，或将 claim 降级为 \"features beyond lexical overlap\"。\n- [R1-N3, R2 交叉回应强烈同意并升级: **完全一致**]\n\n**MF5. [critical] DD 评估样本量数据矛盾，数据划分不透明**\n- experiments.tex line 11: \"80 Deceptive Delight\" vs. line 265: \"On OOD Deceptive Delight ($n$=118)\"。80 ≠ 118 未解释。\n- IID test \"76 held-out Crescendo\" 仅指 jailbreak，benign test set 大小和来源完全未说明。\n- OOD 评估的 benign 样本数量和来源未交代。\n- 直接影响可复现性和 F1 计算准确性。\n- [R1-N4, R2 交叉确认: **完全一致**]\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [warning] 3-seed variance estimation 不可靠**\n- \"4-20× variance reduction\"（Finding 3 核心定量表述）基于 3 seeds，std 相对误差约 50%。MLM DD-Full std=0.115 主要由 seed 456 (recall=0.64) 驱动。Population std (N divisor) 在 n=3 时比 sample std 低 18%。\n- 建议：增加到 5-10 seeds，或对 \"4-20×\" 添加显著 uncertainty caveat。\n- [R1-W1, R2 交叉同意]\n\n**SF2. [warning] McNemar's test 被误用为等价性证据**\n- ≤7 discordant pairs 下 McNemar 几乎无统计效力。论文一方面用 p>0.13 支持 \"non-factors\" claim，一方面承认 power 不足——逻辑矛盾。\n- absence of significance ≠ evidence of equivalence。\n- 建议：补充 equivalence test (TOST)，或在每次引用 McNemar 时标注 power 限制。\n- [R1-W2, R2 交叉同意]\n\n**SF3. [warning] TF-IDF 在 DD 上 F1≥0.961，DD 作为核心评估集意义被削弱**\n- TF-IDF per-prefix F1 达到 0.994-1.000（Appendix Table S2），full F1=0.961。DD 几乎完全被词汇特征解决。\n- Table 3（论文第一个结果表）以 DD 为中心，但 DD 是 lexically solvable 的任务。ActorAttack（TF-IDF=0.261 vs 9-class=0.972）远更有说服力但被安排在后半段。\n- ActorAttack 是唯一区分 lexical/beyond-lexical 的评估集，但也是唯一 perturbation robustness 崩溃的评估集——整个\"beyond lexical\"claim 的证据基础偏窄。\n- 建议：将 ActorAttack 提升为主要展示评估集；在叙事中更早承认 DD lexical separability。\n- [R1-W6, R2-W4: 独立提出，交叉完全一致]\n\n**SF4. [warning] Encoder 容量混淆变量**\n- DeBERTa-v3-base (184M) vs RoBERTa-base (125M) 参数量差 47%。Finding 2（\"encoder pretraining method determines difficulty threshold\"）与 \"encoder capacity determines threshold\" 无法区分。\n- Discussion 承认但主文叙述仍归因于预训练方法。\n- 建议：在 Contribution 2 和 Abstract 中添加 capacity caveat。\n- [R1-W3, R2 交叉同意]\n\n**SF5. [warning] Analysis paper 分析深度不足**\n- CKA 仅一段描述无可视化；linear probing 仅一句话（1-5pp）无详细表格；无 t-SNE/UMAP embedding 空间可视化；无 attention pattern 分析。\n- 作为 analysis paper，分析工具运用单薄，与 discourse-level claim 缺乏分析支撑直接相关。\n- 建议：增加 CKA 矩阵热力图、probing 详细表格、embedding 空间可视化。\n- [R2-W6, R1 交叉同意并关联到 discourse-level claim]\n\n**SF6. [warning] Abstract 数据堆砌（12+ 数值）**\n- ~220 words 中至少 12 个具体数值。审稿人 30 秒内难以提取核心信息。\n- 建议：保留 2-3 个 headline numbers（~60pp gap, TF-IDF vs 9-class on ActorAttack, ToxicChat DA vs vanilla），其余用定性描述。\n- [R2-W1, R1 交叉同意]\n\n**SF7. [warning] Introduction vs Related Work 关于 vanilla baseline 与 DeepContext 关系自相矛盾**\n- Introduction: \"replicating the frozen-encoder-plus-RNN approach of DeepContext\"\n- Related Work: \"it is not a direct proxy for DeepContext, which differs in encoder fine-tuning, model capacity, and loss function\"\n- 写作 bug，削弱论文可信度。\n- 建议：统一为 \"vanilla baseline represents the class of pretrained-encoder-plus-RNN approaches without domain adaptation\"。\n- [R2-N4 提出, R1 REBUT 但同意语言矛盾是 must-fix level writing bug]\n\n**SF8. [warning] 策略标注验证不充分**\n- n=50、单人类标注者、κ=0.78。每类平均 ~5.5 样本。无 inter-human agreement baseline。\n- Finding 3 间接缓解（label quality 不影响检测），但 Figure 3 策略轨迹分析仍依赖标注质量。\n- 建议：增加第二个标注者或增加样本量；至少在 Figure 3 添加 caveat。\n- [R1-W7, R2 交叉同意]\n\n**SF9. [warning] 引用不足**\n- 当前 31 条 bib 对 EMNLP 偏低（典型 40-60+）。\n- 必须补充：He et al. (2023) DeBERTa-v3, Clark et al. (2020) ELECTRA, Kornblith et al. (2019) CKA, Qwen3-8B 官方引用。\n- 建议补充：Bai et al. (2022) RLHF, Jain et al. (2023) Baseline Defenses, Qi et al. (2024), WildChat, LMSYS-Chat-1M。\n- [R1 Missing Refs, R2-W3: 独立提出，关键遗漏交叉一致]\n\n**SF10. [warning] Perturbation analysis 篇幅过长**\n- Section 5.5 占约 1 页正文，但结论为 \"attack-family-dependent\"。\n- R1 建议移至 appendix，R2 REBUT 认为 negative result 应留正文但压缩。\n- 建议：压缩为半页，保留 IID+DD 正面结果和 ActorAttack negative result，逐 seed 细节移至 appendix。\n- [R1-W5 提出, R2 REBUT 但同意压缩]\n\n**SF11. [warning] 术语不一致**\n- \"domain exposure\" / \"domain adaptation\" / \"continued pretraining\" / \"DAPT\" 四个术语混用。\n- \"evidence hierarchy\" 首次出现于 Table 4 caption 但未预告。\n- DisPeD 全称从未给出。\n- [R2-W5, R1 交叉部分同意]\n\n### Minor（不影响接收）\n\n- **M1.** MLM-only 部分结果缺 std，seed 数不明确（Table 3 IID 列）。[R1-M2, R2-M4]\n- **M2.** Qwen3-8B 广泛使用但无正式引用。[R1-M1, R2]\n- **M3.** Population std (N divisor) vs sample std (N-1) 在 n=3 时差异 18%，选择未 justify。[R1-M4, R2-M7]\n- **M4.** Table 3 选择性展示 3 个方法（可能给 cherry-picking 印象）。[R2-M2]\n- **M5.** FITD 评估几乎无区分力（所有变体 F1≥0.990）。[R1-M3]\n- **M6.** Checklist E2 关于 license 模糊（应指明具体 license）。[R2-M6]\n- **M7.** TF-IDF 行无 std 注释（确定性模型应标注）。[R1-M6]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 在独立审稿和交叉回应中完全一致：\n\n1. **Figure 1 缺失不可接受** — desk reject 风险\n2. **Single-LLM confound** — cross-attack generalization claim 需要限定或扩展数据\n3. **人类数据证据层级逆转** — \"classification as regularizer\" 的 Finding 3 需要根本性重新框定\n4. **Discourse-level overclaiming** — 缺乏 probing 等直接证据，mean pooling≈BiGRU 与 discourse 叙事矛盾\n5. **DD 评估样本量矛盾** — 数据划分不透明\n6. **TF-IDF 削弱 DD 评估** — ActorAttack 应提升为主要评估集\n7. **引用不足** — DeBERTa-v3, ELECTRA, CKA, Qwen3-8B 等关键引用缺失\n\n## Reviewer Divergence [REBUT]\n\n以下问题存在分歧，但已通过交叉回应达成部分共识：\n\n1. **新颖性是否构成 critical 问题**: R2 认为 DAPT 作为核心发现新颖性不足 (critical)；R1 REBUT 认为消融设计和负面发现本身有增量，建议降级为 should-fix (framing)。**Director 判断**：R1 论证更有说服力——论文的增量不在 \"DAPT works\" 而在 \"what doesn't work and why\"，但 framing 确需调整以凸显真正增量。归类为 SF（framing adjustment）。\n\n2. **是否需要与 DeepContext 等直接实验对比**: R2 认为缺少对比是 critical；R1 REBUT 认为 analysis paper 不应要求 SOTA comparison，但写作矛盾必须修复。**Director 判断**：R1 论证合理——analysis paper 的贡献在于 insight 而非 SOTA。语言矛盾归为 SF7（writing bug）。\n\n3. **Perturbation analysis 是否应移至 appendix**: R1 建议移至 appendix；R2 REBUT 认为 negative result 应留正文但压缩。**Director 判断**：R2 论证合理——保留但压缩至半页。\n\n---\n\n## Questions for Authors\n\n**Q1.** DD 评估 n=80 (Setup) vs n=118 (Perturbation Analysis) 的构成是什么？benign 样本来源？IID benign test set 大小？\n\n**Q2.** 论文声称 \"classification supervision functions as a representational regularizer\"，但 ToxicChat 上所有含 classification objective 的变体均低于纯 MLM，且严格按分类复杂度递减排序。如何调和这两个结论？在什么条件下应选择 classification supervision vs MLM-only？\n\n**Q3.** Mean pooling (single seed) ≈ BiGRU on DD。如果多 seed 确认此结果，这对 discourse-level framing 意味着什么？每个 turn 独立可分 vs 需要跨 turn 推理是根本区别。\n\n**Q4.** Linear probing 差异（1-5pp）与 detection F1 差异（MLM vs 9-class ~8pp on DD, ~8pp on ActorAttack）量级不匹配。probing tasks 是否未捕获实际驱动检测的特征维度？\n\n**Q5.** DAPT 捕获了什么具体特征使其超越 TF-IDF on ActorAttack？论文声称 \"pragmatic features\" 但有哪些证据（beyond TF-IDF failure）？\n\n---\n\n## Missing References\n\n**必须补充**:\n1. He et al. (2023) \"DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing\" — 论文使用 DeBERTa-v3 但仅引用 v1\n2. Clark et al. (2020) \"ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators\" — DeBERTa-v3 的 RTD 预训练来自 ELECTRA\n3. Kornblith et al. (2019) \"Similarity of Neural Network Representations Revisited\" — 论文使用 Centered CKA 但未引用原始方法\n4. Qwen3-8B 官方引用 — 数据生成、标注、paraphrasing、baseline 均依赖此模型\n\n**建议补充**:\n5. Bai et al. (2022) \"Training a Helpful and Harmless Assistant with RLHF\"\n6. Jain et al. (2023) \"Baseline Defenses for Adversarial Attacks Against Aligned Language Models\"\n7. Qi et al. (2024) \"Fine-tuning Aligned Language Models Compromises Safety\"\n8. WildChat (Zhao et al., 2024) / LMSYS-Chat-1M (Zheng et al., 2024)\n\n---\n\n## Overall Assessment\n\n**评分: Weak Reject (2.75/5)**\n- R1: 3.0/5 (Findings)\n- R2: 2.5/5 (介于 Resubmit 和 Findings)\n- Director 综合: 2.75/5\n\n**置信度: 4/5**（两位 Reviewer 均仔细阅读全文，熟悉相关领域）\n\n**一句话总结**: 消融设计优秀，DAPT finding 稳健，但 Figure 1 缺失、single-LLM confound、discourse-level overclaiming、人类数据上证据层级逆转四个 critical 问题使论文当前版本不适合 EMNLP main conference。\n\n**详细判断**:\n\n论文提出了一个好的研究问题（\"什么使表示能跨攻击族泛化\"），消融设计精巧且负面结果有价值。然而存在几个根本性障碍：\n\n(1) **外部效度不足**：所有多轮评估在单一 LLM 生成的合成数据上完成；唯一的人类数据验证（ToxicChat）是单轮且推翻了证据层级。论文无法回答\"这些发现在真实多轮场景中是否成立\"。\n\n(2) **核心 Finding 3 被自己的数据削弱**：ToxicChat 上所有含 classification objective 的变体均低于 MLM，严格按分类复杂度递减。\"classification as regularizer\" 更准确的说法是 \"classification as distribution-specific regularizer that can hurt cross-distribution transfer\"——这本身是有价值的发现，但需要作为主线的一部分而非事后修补。\n\n(3) **Discourse-level framing 无支撑**：mean pooling ≈ BiGRU、probing 差异仅 1-5pp、无 attention/representation 可视化。\"beyond lexical\" 有证据（TF-IDF on ActorAttack），但 \"discourse-level\" 是 overclaiming。\n\n(4) **完成度问题**：Figure 1 placeholder、数据矛盾（n=80 vs n=118）、关键引用缺失。\n\n**修改建议优先级**:\n1. [必须] 补 Figure 1\n2. [必须] 修复数据矛盾（n=80 vs n=118），完善数据划分说明\n3. [必须] 补充关键引用（DeBERTa-v3, ELECTRA, CKA, Qwen3-8B）\n4. [高优] 重新框定 Finding 3：将人类数据逆转整合进核心叙事\n5. [高优] 将 discourse-level claims 降级为 beyond-lexical，或补充 probing 证据\n6. [高优] 限定 cross-attack generalization claim 的范围（within synthetic data manifold）\n7. [中优] 将 ActorAttack 提升为主要展示评估集\n8. [中优] 压缩 Abstract 数值、统一术语、压缩 perturbation section\n9. [低优] 增加 seeds、补充 equivalence test、补充 representation 可视化\n\n修复 1-3 后可视为完成稿提交；修复 1-6 后适合 EMNLP Findings；全面修复后有潜力冲击 main conference。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 12+ 数值过载，保留 2-3 个 headline numbers\n- Finding 3 表述需反映 distribution-specific 限定\n- \"seven encoder variants on DeBERTa-v3\" 中 \"on\" 改为 \"of\" 或 \"based on\"\n\n### Introduction\n- 第四段结果段过长（~200 words, 15+ 数值），需压缩至 2-3 句\n- \"replicating the frozen-encoder-plus-RNN approach of DeepContext\" 与 Related Work 矛盾\n- Contribution 1 应强调\"为什么替代方案失败\"而非\"DAPT 有效\"\n- Contribution 3 需添加 \"distribution-specific\" 限定\n\n### Related Work\n- Related Work 中本文实验数值已清理（Round 2 修复有效）\n- 引用密度偏低，需补充上述引用\n\n### Method\n- Figure 1 placeholder 必须替换\n- DisPeD 全称未给出\n- α=0.3 的 ablation 结果已添加（Round 2 修复有效）\n- frozen encoder 设计 justification 已添加（Round 2 修复有效）\n\n### Experiments\n- n=80 vs n=118 矛盾必须解释\n- IID/OOD benign 样本来源和数量必须说明\n- MLM-only IID 结果缺 std\n- Table 3 应包含 ActorAttack 列或至少注明完整结果在 Table 4\n- TF-IDF 确定性应标注\n- Perturbation section 压缩为半页\n\n### Discussion & Conclusion\n- \"variance reversal\" 分析需前移至 Abstract/Contributions\n- Encoder capacity confound 需在 Contribution 2 中添加限定\n\n### Appendix & Checklist\n- Checklist E2 license 模糊，建议指明具体 license\n- Checklist 整体填写合理\n\n### Format\n- 页数需编译验证\n- Figure 3 浮动位置需检查\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject",
    "report": "# 圆桌审稿汇总报告 — Round 3 (Fresh)\n\n**论文**: \"What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap\"\n**目标 Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作）\n**审稿轮次**: Round 1 独立审稿 + 交叉分享，1 轮收敛\n**外部审稿**: 未启用\n\n---\n\n## Summary\n\n本文通过控制性消融研究，分析什么表示属性使 multi-turn jailbreak 检测跨攻击族泛化。设计七个 DeBERTa-v3 Stage-1 变体和三个 RoBERTa 变体（统称 DisPeD），在四个攻击族（Crescendo, FITD, DD, ActorAttack）上评估，得出三个发现：(1) DAPT 是 OOD 泛化主要机制（~60pp gap on DeBERTa-v3）；(2) encoder 预训练方法决定 DAPT 变得关键的难度阈值；(3) 分类监督起正则化作用而非策略分类作用。ToxicChat 验证表明 DAPT 优势迁移至 human-written 数据，但证据层级在人类数据上完全逆转。\n\n---\n\n## Strengths\n\n**S1. 消融设计精良。** 七个 Stage-1 变体系统隔离五个因素（domain exposure, classification supervision, label quality, granularity, domain specificity），每个变体的对比意义清晰。加上两个 encoder 架构的交叉验证，构成教科书级消融矩阵。[R1, R2 一致]\n\n**S2. 统计方法论严谨。** 3-seed 评估、McNemar's test、BCa bootstrap CI（10,000 resamples）、paired permutation test 的组合使用超过大多数 EMNLP 投稿的统计标准。主动报告 effect size 不显著的结果（分类变体间 McNemar all p>0.13）。[R1, R2 一致]\n\n**S3. \"分类作为正则化器\"发现具有反直觉价值。** Scrambled labels = correct labels 在所有 OOD 评估上等效（gap ≤3.9pp），而 OOD 策略预测精度仅 30.7%（κ=0.126）。挑战了\"需要好标签才能泛化\"的朴素假设。[R1]\n\n**S4. 诚实报告负面结果。** Perturbation robustness 在 ActorAttack 上不成立、variance reversal 在 ToxicChat 上出现、McNemar power 限制被明确讨论。这种透明度值得肯定。[R1, R2 一致]\n\n**S5. 极低计算成本，可复现性好。** 全部变体 <4 GPU-hours，超参数完整报告（Appendix D），承诺开源。[R1, R2 一致]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [critical] Figure 1 为 placeholder，论文未完成状态**\n- method.tex line 10: `\\fbox{\\parbox{...}{Architecture diagram placeholder}}`\n- 主架构图是空框。对于以 \"systematic decomposition\" 为核心的论文，架构图是理解七个变体关系的关键工具。\n- desk reject 风险。\n- [R1-N1, R2-N1: 两位 Reviewer 独立发现，交叉回应 **完全一致**]\n\n**MF2. [critical] Single-LLM confound：cross-attack generalization claim 范围过宽**\n- 训练数据和全部 OOD 评估数据（FITD, DD, ActorAttack）均由 Qwen3-8B 生成。\"cross-attack generalization\" 实际上是 \"within Qwen3-8B generation distribution\" 的泛化。\n- ToxicChat 验证仅覆盖最弱 claim（DA > vanilla），未验证核心证据层级排序。且 ToxicChat 是单轮数据。\n- 建议：(a) 用至少一个其他 LLM 生成 OOD 评估数据，或使用 MHJ 真实多轮人类 jailbreak 数据；(b) 若不可行，在标题/Abstract/Conclusion 中限定 claim 范围。\n- [R1-N2, R2-N3 关联: **完全一致**]\n\n**MF3. [critical] 证据层级在人类数据上完全逆转，动摇核心叙事**\n- ToxicChat (Table 5): JB-MLM (0.837±0.013) >> Binary (0.705) >> 9-class (0.596±0.087)。所有含 classification objective 的变体均低于纯 MLM，严格按分类复杂度递减排序。\n- 论文的 \"modality mismatch\" 解释不充分：如果好处仅限于多轮正则化，Binary 和 Scrambled 不应低于 MLM（它们有相同的 domain exposure）。更合理解释：classification supervision 过拟合到合成分布的 decision boundaries。\n- Discussion 中 \"distribution-specific regularization\" 分析与 Abstract/Introduction 的 Finding 3 表述不一致。\n- 建议：(a) 在 Abstract 和 Contribution 3 中明确 \"distribution-specific\"；(b) 将逆转作为核心发现之一而非例外；(c) 增加多轮人类数据评估。\n- [R2-N3 critical, R1-W4 → 交叉后升级为 critical: **完全一致**]\n\n**MF4. [critical] \"Discourse-level\" claims 缺乏直接证据，存在系统性 overclaiming**\n- experiments.tex line 107 声称 DAPT 捕获 \"pragmatic features (hedging, escalation markers, topic-shifting patterns)\"，但无 probing 支持。\n- mean pooling ≈ BiGRU（单 seed）：如果丢弃顺序信息不影响检测，discourse-level structure 体现在哪里？\n- Related Work 将 probing classifiers 留给 future work，对自称 analysis paper 是重大缺陷。\n- \"beyond bag-of-words\"（TF-IDF on ActorAttack 失败）≠ \"discourse-level\"，可能是 longer n-gram、sub-word、intra-sentence syntax。\n- linear probing 结果（9-class vs vanilla/MLM 仅 1-5pp）与 detection F1 巨大差距的 disconnect 暗示 probing tasks 未捕获驱动检测的特征。\n- 建议：增加 discourse-level diagnostic probing，或将 claim 降级为 \"features beyond lexical overlap\"。\n- [R1-N3, R2 交叉回应强烈同意并升级: **完全一致**]\n\n**MF5. [critical] DD 评估样本量数据矛盾，数据划分不透明**\n- experiments.tex line 11: \"80 Deceptive Delight\" vs. line 265: \"On OOD Deceptive Delight ($n$=118)\"。80 ≠ 118 未解释。\n- IID test \"76 held-out Crescendo\" 仅指 jailbreak，benign test set 大小和来源完全未说明。\n- OOD 评估的 benign 样本数量和来源未交代。\n- 直接影响可复现性和 F1 计算准确性。\n- [R1-N4, R2 交叉确认: **完全一致**]\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [warning] 3-seed variance estimation 不可靠**\n- \"4-20× variance reduction\"（Finding 3 核心定量表述）基于 3 seeds，std 相对误差约 50%。MLM DD-Full std=0.115 主要由 seed 456 (recall=0.64) 驱动。Population std (N divisor) 在 n=3 时比 sample std 低 18%。\n- 建议：增加到 5-10 seeds，或对 \"4-20×\" 添加显著 uncertainty caveat。\n- [R1-W1, R2 交叉同意]\n\n**SF2. [warning] McNemar's test 被误用为等价性证据**\n- ≤7 discordant pairs 下 McNemar 几乎无统计效力。论文一方面用 p>0.13 支持 \"non-factors\" claim，一方面承认 power 不足——逻辑矛盾。\n- absence of significance ≠ evidence of equivalence。\n- 建议：补充 equivalence test (TOST)，或在每次引用 McNemar 时标注 power 限制。\n- [R1-W2, R2 交叉同意]\n\n**SF3. [warning] TF-IDF 在 DD 上 F1≥0.961，DD 作为核心评估集意义被削弱**\n- TF-IDF per-prefix F1 达到 0.994-1.000（Appendix Table S2），full F1=0.961。DD 几乎完全被词汇特征解决。\n- Table 3（论文第一个结果表）以 DD 为中心，但 DD 是 lexically solvable 的任务。ActorAttack（TF-IDF=0.261 vs 9-class=0.972）远更有说服力但被安排在后半段。\n- ActorAttack 是唯一区分 lexical/beyond-lexical 的评估集，但也是唯一 perturbation robustness 崩溃的评估集——整个\"beyond lexical\"claim 的证据基础偏窄。\n- 建议：将 ActorAttack 提升为主要展示评估集；在叙事中更早承认 DD lexical separability。\n- [R1-W6, R2-W4: 独立提出，交叉完全一致]\n\n**SF4. [warning] Encoder 容量混淆变量**\n- DeBERTa-v3-base (184M) vs RoBERTa-base (125M) 参数量差 47%。Finding 2（\"encoder pretraining method determines difficulty threshold\"）与 \"encoder capacity determines threshold\" 无法区分。\n- Discussion 承认但主文叙述仍归因于预训练方法。\n- 建议：在 Contribution 2 和 Abstract 中添加 capacity caveat。\n- [R1-W3, R2 交叉同意]\n\n**SF5. [warning] Analysis paper 分析深度不足**\n- CKA 仅一段描述无可视化；linear probing 仅一句话（1-5pp）无详细表格；无 t-SNE/UMAP embedding 空间可视化；无 attention pattern 分析。\n- 作为 analysis paper，分析工具运用单薄，与 discourse-level claim 缺乏分析支撑直接相关。\n- 建议：增加 CKA 矩阵热力图、probing 详细表格、embedding 空间可视化。\n- [R2-W6, R1 交叉同意并关联到 discourse-level claim]\n\n**SF6. [warning] Abstract 数据堆砌（12+ 数值）**\n- ~220 words 中至少 12 个具体数值。审稿人 30 秒内难以提取核心信息。\n- 建议：保留 2-3 个 headline numbers（~60pp gap, TF-IDF vs 9-class on ActorAttack, ToxicChat DA vs vanilla），其余用定性描述。\n- [R2-W1, R1 交叉同意]\n\n**SF7. [warning] Introduction vs Related Work 关于 vanilla baseline 与 DeepContext 关系自相矛盾**\n- Introduction: \"replicating the frozen-encoder-plus-RNN approach of DeepContext\"\n- Related Work: \"it is not a direct proxy for DeepContext, which differs in encoder fine-tuning, model capacity, and loss function\"\n- 写作 bug，削弱论文可信度。\n- 建议：统一为 \"vanilla baseline represents the class of pretrained-encoder-plus-RNN approaches without domain adaptation\"。\n- [R2-N4 提出, R1 REBUT 但同意语言矛盾是 must-fix level writing bug]\n\n**SF8. [warning] 策略标注验证不充分**\n- n=50、单人类标注者、κ=0.78。每类平均 ~5.5 样本。无 inter-human agreement baseline。\n- Finding 3 间接缓解（label quality 不影响检测），但 Figure 3 策略轨迹分析仍依赖标注质量。\n- 建议：增加第二个标注者或增加样本量；至少在 Figure 3 添加 caveat。\n- [R1-W7, R2 交叉同意]\n\n**SF9. [warning] 引用不足**\n- 当前 31 条 bib 对 EMNLP 偏低（典型 40-60+）。\n- 必须补充：He et al. (2023) DeBERTa-v3, Clark et al. (2020) ELECTRA, Kornblith et al. (2019) CKA, Qwen3-8B 官方引用。\n- 建议补充：Bai et al. (2022) RLHF, Jain et al. (2023) Baseline Defenses, Qi et al. (2024), WildChat, LMSYS-Chat-1M。\n- [R1 Missing Refs, R2-W3: 独立提出，关键遗漏交叉一致]\n\n**SF10. [warning] Perturbation analysis 篇幅过长**\n- Section 5.5 占约 1 页正文，但结论为 \"attack-family-dependent\"。\n- R1 建议移至 appendix，R2 REBUT 认为 negative result 应留正文但压缩。\n- 建议：压缩为半页，保留 IID+DD 正面结果和 ActorAttack negative result，逐 seed 细节移至 appendix。\n- [R1-W5 提出, R2 REBUT 但同意压缩]\n\n**SF11. [warning] 术语不一致**\n- \"domain exposure\" / \"domain adaptation\" / \"continued pretraining\" / \"DAPT\" 四个术语混用。\n- \"evidence hierarchy\" 首次出现于 Table 4 caption 但未预告。\n- DisPeD 全称从未给出。\n- [R2-W5, R1 交叉部分同意]\n\n### Minor（不影响接收）\n\n- **M1.** MLM-only 部分结果缺 std，seed 数不明确（Table 3 IID 列）。[R1-M2, R2-M4]\n- **M2.** Qwen3-8B 广泛使用但无正式引用。[R1-M1, R2]\n- **M3.** Population std (N divisor) vs sample std (N-1) 在 n=3 时差异 18%，选择未 justify。[R1-M4, R2-M7]\n- **M4.** Table 3 选择性展示 3 个方法（可能给 cherry-picking 印象）。[R2-M2]\n- **M5.** FITD 评估几乎无区分力（所有变体 F1≥0.990）。[R1-M3]\n- **M6.** Checklist E2 关于 license 模糊（应指明具体 license）。[R2-M6]\n- **M7.** TF-IDF 行无 std 注释（确定性模型应标注）。[R1-M6]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 在独立审稿和交叉回应中完全一致：\n\n1. **Figure 1 缺失不可接受** — desk reject 风险\n2. **Single-LLM confound** — cross-attack generalization claim 需要限定或扩展数据\n3. **人类数据证据层级逆转** — \"classification as regularizer\" 的 Finding 3 需要根本性重新框定\n4. **Discourse-level overclaiming** — 缺乏 probing 等直接证据，mean pooling≈BiGRU 与 discourse 叙事矛盾\n5. **DD 评估样本量矛盾** — 数据划分不透明\n6. **TF-IDF 削弱 DD 评估** — ActorAttack 应提升为主要评估集\n7. **引用不足** — DeBERTa-v3, ELECTRA, CKA, Qwen3-8B 等关键引用缺失\n\n## Reviewer Divergence [REBUT]\n\n以下问题存在分歧，但已通过交叉回应达成部分共识：\n\n1. **新颖性是否构成 critical 问题**: R2 认为 DAPT 作为核心发现新颖性不足 (critical)；R1 REBUT 认为消融设计和负面发现本身有增量，建议降级为 should-fix (framing)。**Director 判断**：R1 论证更有说服力——论文的增量不在 \"DAPT works\" 而在 \"what doesn't work and why\"，但 framing 确需调整以凸显真正增量。归类为 SF（framing adjustment）。\n\n2. **是否需要与 DeepContext 等直接实验对比**: R2 认为缺少对比是 critical；R1 REBUT 认为 analysis paper 不应要求 SOTA comparison，但写作矛盾必须修复。**Director 判断**：R1 论证合理——analysis paper 的贡献在于 insight 而非 SOTA。语言矛盾归为 SF7（writing bug）。\n\n3. **Perturbation analysis 是否应移至 appendix**: R1 建议移至 appendix；R2 REBUT 认为 negative result 应留正文但压缩。**Director 判断**：R2 论证合理——保留但压缩至半页。\n\n---\n\n## Questions for Authors\n\n**Q1.** DD 评估 n=80 (Setup) vs n=118 (Perturbation Analysis) 的构成是什么？benign 样本来源？IID benign test set 大小？\n\n**Q2.** 论文声称 \"classification supervision functions as a representational regularizer\"，但 ToxicChat 上所有含 classification objective 的变体均低于纯 MLM，且严格按分类复杂度递减排序。如何调和这两个结论？在什么条件下应选择 classification supervision vs MLM-only？\n\n**Q3.** Mean pooling (single seed) ≈ BiGRU on DD。如果多 seed 确认此结果，这对 discourse-level framing 意味着什么？每个 turn 独立可分 vs 需要跨 turn 推理是根本区别。\n\n**Q4.** Linear probing 差异（1-5pp）与 detection F1 差异（MLM vs 9-class ~8pp on DD, ~8pp on ActorAttack）量级不匹配。probing tasks 是否未捕获实际驱动检测的特征维度？\n\n**Q5.** DAPT 捕获了什么具体特征使其超越 TF-IDF on ActorAttack？论文声称 \"pragmatic features\" 但有哪些证据（beyond TF-IDF failure）？\n\n---\n\n## Missing References\n\n**必须补充**:\n1. He et al. (2023) \"DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing\" — 论文使用 DeBERTa-v3 但仅引用 v1\n2. Clark et al. (2020) \"ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators\" — DeBERTa-v3 的 RTD 预训练来自 ELECTRA\n3. Kornblith et al. (2019) \"Similarity of Neural Network Representations Revisited\" — 论文使用 Centered CKA 但未引用原始方法\n4. Qwen3-8B 官方引用 — 数据生成、标注、paraphrasing、baseline 均依赖此模型\n\n**建议补充**:\n5. Bai et al. (2022) \"Training a Helpful and Harmless Assistant with RLHF\"\n6. Jain et al. (2023) \"Baseline Defenses for Adversarial Attacks Against Aligned Language Models\"\n7. Qi et al. (2024) \"Fine-tuning Aligned Language Models Compromises Safety\"\n8. WildChat (Zhao et al., 2024) / LMSYS-Chat-1M (Zheng et al., 2024)\n\n---\n\n## Overall Assessment\n\n**评分: Weak Reject (2.75/5)**\n- R1: 3.0/5 (Findings)\n- R2: 2.5/5 (介于 Resubmit 和 Findings)\n- Director 综合: 2.75/5\n\n**置信度: 4/5**（两位 Reviewer 均仔细阅读全文，熟悉相关领域）\n\n**一句话总结**: 消融设计优秀，DAPT finding 稳健，但 Figure 1 缺失、single-LLM confound、discourse-level overclaiming、人类数据上证据层级逆转四个 critical 问题使论文当前版本不适合 EMNLP main conference。\n\n**详细判断**:\n\n论文提出了一个好的研究问题（\"什么使表示能跨攻击族泛化\"），消融设计精巧且负面结果有价值。然而存在几个根本性障碍：\n\n(1) **外部效度不足**：所有多轮评估在单一 LLM 生成的合成数据上完成；唯一的人类数据验证（ToxicChat）是单轮且推翻了证据层级。论文无法回答\"这些发现在真实多轮场景中是否成立\"。\n\n(2) **核心 Finding 3 被自己的数据削弱**：ToxicChat 上所有含 classification objective 的变体均低于 MLM，严格按分类复杂度递减。\"classification as regularizer\" 更准确的说法是 \"classification as distribution-specific regularizer that can hurt cross-distribution transfer\"——这本身是有价值的发现，但需要作为主线的一部分而非事后修补。\n\n(3) **Discourse-level framing 无支撑**：mean pooling ≈ BiGRU、probing 差异仅 1-5pp、无 attention/representation 可视化。\"beyond lexical\" 有证据（TF-IDF on ActorAttack），但 \"discourse-level\" 是 overclaiming。\n\n(4) **完成度问题**：Figure 1 placeholder、数据矛盾（n=80 vs n=118）、关键引用缺失。\n\n**修改建议优先级**:\n1. [必须] 补 Figure 1\n2. [必须] 修复数据矛盾（n=80 vs n=118），完善数据划分说明\n3. [必须] 补充关键引用（DeBERTa-v3, ELECTRA, CKA, Qwen3-8B）\n4. [高优] 重新框定 Finding 3：将人类数据逆转整合进核心叙事\n5. [高优] 将 discourse-level claims 降级为 beyond-lexical，或补充 probing 证据\n6. [高优] 限定 cross-attack generalization claim 的范围（within synthetic data manifold）\n7. [中优] 将 ActorAttack 提升为主要展示评估集\n8. [中优] 压缩 Abstract 数值、统一术语、压缩 perturbation section\n9. [低优] 增加 seeds、补充 equivalence test、补充 representation 可视化\n\n修复 1-3 后可视为完成稿提交；修复 1-6 后适合 EMNLP Findings；全面修复后有潜力冲击 main conference。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 12+ 数值过载，保留 2-3 个 headline numbers\n- Finding 3 表述需反映 distribution-specific 限定\n- \"seven encoder variants on DeBERTa-v3\" 中 \"on\" 改为 \"of\" 或 \"based on\"\n\n### Introduction\n- 第四段结果段过长（~200 words, 15+ 数值），需压缩至 2-3 句\n- \"replicating the frozen-encoder-plus-RNN approach of DeepContext\" 与 Related Work 矛盾\n- Contribution 1 应强调\"为什么替代方案失败\"而非\"DAPT 有效\"\n- Contribution 3 需添加 \"distribution-specific\" 限定\n\n### Related Work\n- Related Work 中本文实验数值已清理（Round 2 修复有效）\n- 引用密度偏低，需补充上述引用\n\n### Method\n- Figure 1 placeholder 必须替换\n- DisPeD 全称未给出\n- α=0.3 的 ablation 结果已添加（Round 2 修复有效）\n- frozen encoder 设计 justification 已添加（Round 2 修复有效）\n\n### Experiments\n- n=80 vs n=118 矛盾必须解释\n- IID/OOD benign 样本来源和数量必须说明\n- MLM-only IID 结果缺 std\n- Table 3 应包含 ActorAttack 列或至少注明完整结果在 Table 4\n- TF-IDF 确定性应标注\n- Perturbation section 压缩为半页\n\n### Discussion & Conclusion\n- \"variance reversal\" 分析需前移至 Abstract/Contributions\n- Encoder capacity confound 需在 Contribution 2 中添加限定\n\n### Appendix & Checklist\n- Checklist E2 license 模糊，建议指明具体 license\n- Checklist 整体填写合理\n\n### Format\n- 页数需编译验证\n- Figure 3 浮动位置需检查\n"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-18T18:17:55.229822+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a90fe0dde422576f214f12233cfe27a3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4176
}
```

</details>

---


### Assistant

_source line 288 · 2026-05-18T18:18:06.966586+00:00_

审稿报告已投递。

**圆桌审稿完成总结**：

- **评分**: Weak Reject (2.75/5)
- **R1**: 3.0/5 (Findings), **R2**: 2.5/5 (Resubmit~Findings)
- **5 个 Must-Fix**: Figure 1 placeholder、single-LLM confound、人类数据证据层级逆转、discourse-level overclaiming、数据矛盾(n=80 vs n=118)
- **11 个 Should-Fix**: 3-seed variance、McNemar 误用、TF-IDF 削弱 DD、encoder capacity confound、analysis 深度不足、Abstract 堆砌、baseline framing 矛盾、标注验证不足、引用不足、perturbation 篇幅过长、术语不一致
- **7 个 Minor**: MLM-only std、Qwen3-8B 引用、population std、Table 3 选择性、FITD 无区分力、license 模糊、TF-IDF 标注

两位 Reviewer 在所有核心问题上达成共识。唯一分歧（novelty 和 baseline comparison 的严重级别）已在交叉回应中通过合理论证收敛。Issue Tracker 已同步更新至 `review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 26

## Round 26

2 recorded events


### User

_source line 289 · 2026-05-18T18:18:09.568713+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心结论：R1 的 4 个 Must-Fix 和 7 个 Should-Fix 中，我对 6 个 Must-Fix/Should-Fix 完全同意（N1-N4、W1-W4、W6-W7），仅对 W5（perturbation 移至 appendix）部分反驳——negative result 应保留在正文但压缩篇幅。两位 Reviewer 的最大共识是 single-LLM confound + 人类数据逆转构成论文核心叙事的系统性威胁。R1 的 N3（discourse-level claims 缺乏直接证据）是我在自己审稿中遗漏的重要问题，mean pooling ≈ BiGRU 的结果与 discourse-level 叙事存在直接矛盾。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 290 · 2026-05-18T18:18:27.479062+00:00_

审稿报告已投递至 Research Director。汇总如下：

---

**Overall: Weak Reject (2.75/5)**

**5 个 Must-Fix（两位 Reviewer 完全一致）**：
1. Figure 1 为 placeholder（desk reject 风险）
2. Single-LLM confound（cross-attack generalization claim 范围过宽）
3. 证据层级在 ToxicChat 上完全逆转（Finding 3 需根本性重框定）
4. Discourse-level claims 无直接证据（mean pooling≈BiGRU 与叙事矛盾）
5. DD 样本量矛盾（n=80 vs n=118）+数据划分不透明

**11 个 Should-Fix**：3-seed variance 不可靠、McNemar 误用为等价性证据、DD lexical separability、encoder capacity confound、analysis paper 分析深度不足、Abstract 数据堆砌、vanilla-DeepContext 措辞矛盾、标注验证不充分、引用不足、perturbation 篇幅过长、术语不一致

**Reviewer 分歧（已协调）**：
- 新颖性：R2 认为 critical → R1 REBUT → Director 采纳 R1（消融设计有增量，降为 framing SF）
- Baseline 对比：R2 认为 critical → R1 REBUT → Director 采纳 R1（analysis paper 不要求 SOTA comparison，语言矛盾归为 writing SF）
- Perturbation 移至 appendix：R1 提议 → R2 REBUT → Director 采纳 R2（保留但压缩至半页）

Issue Tracker 已同步更新（`review_issues.yaml`），含 Round 1-2 历史 issues + Round 3 新增 17 条。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director"
}
```

</details>

---


## Round 27

## Round 27

62 recorded events


### User

_source line 291 · 2026-05-20T05:16:18.385502+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: persuasion_turn_jailbreak_detect
- 论文路径: projects/persuasion_turn_jailbreak_detect/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-20T05:16:25.013464+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 293 · 2026-05-20T05:16:25.065010+00:00_

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
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-20T05:16:31.340742+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-20T05:16:31.341242+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-20T05:16:31.743087+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,read_local_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,read_local_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-20T05:16:31.797702+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 54
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-20T05:16:39.134334+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-20T05:16:39.185135+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-20T05:16:41.950512+00:00_

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
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
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

_source line 301 · 2026-05-20T05:16:42.001231+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-20T05:16:48.349743+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-20T05:16:49.705407+00:00_

{"result":"# 项目 persuasion_turn_jailbreak_detect 概况\n\n## 实验状态 (81 个)\n\n- **plan_016_sentiment_control**: PREPARING (failed) — \n- **plan_012_gpt55_judge**: DONE (success) — \n- **plan_015_dd_eval**: DONE (success) — \n- **plan_006_cross_attack_clean**: DONE (success) — \n- **plan_004_perturbation_eval**: DONE (success) — \n- **plan_013_none_collapse**: DONE (success) — \n- **plan_012_llm_judge_qwen**: DONE (success) — \n- **plan_002_clean_training**: DONE (negative) — \n- **plan_003_scrambled_ablation**: DONE (negative) — \n- **cross_attack_baseline**: DONE (negative) — \n- **plan_008_strategy_transition**: DONE (success) — \n- **plan_007_tfidf_fitd_dd**: DONE (success) — \n- **plan_005_multi_attack_gen**: DONE (success) — \n- **phase_b_full**: DONE (success) — \n- **pilot_phase_b**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp16_9class_train（准备中）\n- exp16_vanilla_train（准备中）\n- exp17_qwen_benign_gen（准备中）\n- exp17_qwen_jailbreak_gen（准备中）\n- exp17_dryrun（准备中）\n- exp16_llama_benign_gen（准备中）\n- exp16_llama_jailbreak_gen（准备中）\n- llama_crescendo_dryrun（准备中）\n- exp16_multi_llm_training: Training on mixed-LLM data (Qwen + Llama) will eliminate the single-LLM confound: the model will generalize cross-LLM (Llama OOD F1 from 0.37-0.43 to 0.8+) because mixed benign distribution covers both LLMs' stylistic patterns, resolving the false-positive-driven failure identified in exp14.（准备中）\n- exp13_meanpool_multiseed: Mean pooling classifier (without temporal modeling) will perform comparably to BiGRU across 3 seeds on both DD OOD and ActorAttack, confirming that persuasion-grounded embeddings alone drive cross-attack generalization and GRU temporal modeling is not necessary.（准备中）\n- …另有 22 项\n\n## 近期结论\n- **exp16b_llama_only_mlm** (failed): MLM DAPT on Llama-only data (250 conversations) will produce stable intermediate performance between vanilla and 9-class on DD OOD and AA OOD, distinguishing whether
…[truncated 907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-20T05:16:49.705934+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-20T05:16:49.957247+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/figures/cka_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/figures/cka_heatmap.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/figures/fig1_architecture.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/figures/fig1_architecture.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/figures/fig3_strategy_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/figures/embedding_tsne.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/figures/fig2_cross_attack_bar.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex
/home/ubuntu/.agent-ml-research-
…[truncated 1997 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-20T05:16:49.957702+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-20T05:16:56.697972+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2024: Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2024-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Call for Papers: NLP for Science Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/nlp-science"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"}]

I found search results, but they don't contain a specific "EMNLP 2026 Call for Papers" with main conference submission guidelines and author instructions. The search results include calls for EMNLP-related activities (tutorials and workshops), EMNLP 2024 and 2025
…[truncated 1027 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "elapsed_ms": 6740
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-20T05:17:01.698295+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 official website call for papers submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 official website call for papers submission deadline"
  }
}
```

</details>

---


### Tool call

_source line 309 · 2026-05-20T05:17:01.851637+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 submission guidelines page limit formatting requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_613965f45d48763f375aa83e9294b24a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 submission guidelines page limit formatting requirements"
  }
}
```

</details>

---

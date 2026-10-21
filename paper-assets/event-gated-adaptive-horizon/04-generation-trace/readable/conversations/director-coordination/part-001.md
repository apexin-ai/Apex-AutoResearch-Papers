# Director coordination — Part 1 of 2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

[Transcript overview](../director-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/29/29ab7f6deeee29654378.json)

## Round 1

## Round 1

64 recorded events


### User

_source line 1 · 2026-05-15T12:26:34.750478+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: event-gated-adaptive-horizon
- 论文路径: projects/event-gated-adaptive-horizon/docs/paper/main.tex
- 目标 venue: CoRL 2026
- Track: main conference
- 截止日期: 2026-05-29

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-15T12:26:42.405679+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-15T12:26:42.456963+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-15T12:26:48.662557+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-15T12:26:48.662996+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-15T12:26:52.489249+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-15T12:26:52.489690+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-15T12:26:55.915780+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-15T12:26:55.966450+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-15T12:27:02.407643+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_local_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read_local_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-15T12:27:02.458561+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-15T12:27:11.070426+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-15T12:27:12.381105+00:00_

{"result":"# 项目 event-gated-adaptive-horizon 概况\n\n## 实验状态 (32 个)\n\n- **exp_009b_008d_walker_s2**: DONE (negative) — \n- **exp_009c_008f_walker_s2**: DONE (negative) — \n- **exp_009f_008f_walker_s1**: QUEUED — \n- **exp_007_fixed_dt4**: DONE (negative) — \n- **exp_006_fixed_dt2**: DONE (negative) — \n- **exp_008d_subsample_on_h8**: DONE (negative) — \n- **exp_008f_no_dt_embed_subsample_on_h8**: DONE (success) — \n- **exp_008a_no_subsample_dt2**: DONE (success) — \n- **exp_008c_no_subsample_dt2_h8**: DONE (negative) — \n- **exp_008e_subsample_on_fixed_dt1**: DONE (killed) — \n- **exp_008e_subsample_on_dt1_h15**: DONE (killed) — \n- **exp_005_event_gated_v4**: DONE (negative) — \n- **exp_004_event_gated_v3**: DONE (negative) — \n- **exp_003_event_gated_v2**: DONE (negative) — \n- **exp_002_event_gated**: DONE (failed) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-15T12:24:16Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 32 个实验 — DONE 28, QUEUED 3, RUNNING 1\n**DONE 分布**: failed 2, killed 8, negative 11, success 7\n\n### GPU 占用\n- **分配**: 2 张 — bjb1-45299:cuda:0, bjb1-45299:cuda:1\n- **实际运行**: 1 张 — bjb1-45299:cuda:1(exp_015b_frozen_dt_emb)\n- **空闲（分配了没跑）**: bjb1-45299:cuda:0\n\n### 🏃 RUNNING\n| exp_id | server | gpu | pid | log |\n|--------|--------|-----|-----|-----|\n| `exp_015b_frozen_dt_emb` | bjb1-45299 | cuda:1 | exp_015b_frozen_dt_emb | `—` |\n\n### 📌 最近完成 (top 5)\n- `exp_009d_baseline_walker_s0` [failed] — 2026-05-15T12:24:15 — EXIT_CODE=129 (non-zero)\n- `exp_009d_baseline_walker_s1` [killed] — 2026-05-15T11:54:55\n- `exp_009e_008d_walker_s1` [negative] — 2026-05-15T11:31:04\n- `exp_009a_baseline_walker_s2` [success] — 2026-05-15T06:33:16\n- `exp_008e_v3_walker_s2` [negative] — 2026-05-15T06:24:21\n\n### 🔴 最近失败原因 (top 3)\n- `exp_009d_baseline_walker_s0`: EXIT_CODE=129 (non-zero)\n- `exp_009d_baseline_walker_s1`: _(no failure_reason — pre-2026-04-24 entry)_\n\n&lt;!-- AUTO-FACTS-END -->\n\
…[truncated 1915 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1310
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-15T12:27:12.431931+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-15T12:27:13.300419+00:00_

1	\documentclass[10pt,letterpaper,twocolumn]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{graphicx}
8	\graphicspath{{../../artifacts/}}
9	\usepackage[table]{xcolor}
10	\usepackage{colortbl}
11	\usepackage[margin=0.75in]{geometry}
12	\usepackage[colorlinks,citecolor=blue,urlcolor=blue,linkcolor=blue]{hyperref}
13	\usepackage{natbib}
14	\usepackage{caption}
15	\usepackage{subcaption}
16	\usepackage{array}
17	\usepackage{enumitem}
18	\usepackage{wrapfig}
19	
20	% Custom commands
21	\newcommand{\dt}{\mathrm{dt}}
22	\newcommand{\nve}{\mathrm{nve}}
23	\newcommand{\ie}{\textit{i.e.}}
24	\newcommand{\eg}{\textit{e.g.}}
25	\newcommand{\cf}{\textit{cf.}}
26	\newcommand{\etal}{\textit{et al.}}
27	
28	\title{Why Temporal Abstraction Fails in Imagination-Based RL:\\
29	A Diagnostic Analysis of Variable-Rate DreamerV3}
30	
31	\author{Anonymous Authors}
32	\date{}
33	
34	\begin{document}
35	\maketitle
36	
37	% --- ABSTRACT ---
38	\input{sections/abstract}
39	
40	% --- INTRODUCTION ---
41	\input{sections/introduction}
42	
43	% --- RELATED WORK ---
44	\input{sections/related_work}
45	
46	% --- METHODOLOGY ---
47	\input{sections/methodology}
48	
49	% --- RESULTS ---
50	\input{sections/results}
51	
52	% --- ANALYSIS ---
53	\input{sections/analysis}
54	
55	% --- CONCLUSION ---
56	\input{sections/conclusion}
57	
58	\bibliographystyle{plainnat}
59	\bibliography{references}
60	
61	\end{document}
62	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 868
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-15T12:27:13.300964+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 call for papers submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 call for papers submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 17 · 2026-05-15T12:27:13.452363+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 18 · 2026-05-15T12:27:13.560073+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/sessions/review_director_9a57450c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 107
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-15T12:27:20.695906+00:00_

Web search results for query: "CoRL 2026 call for papers submission deadline author guidelines"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Refactor conference data · huggingface/ai-deadlines at f3cc2d7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 - Call for Workshops | Danfei Xu","url":"https://www.linkedin.com/posts/danfei-xu-94522133_corl-2026-call-for-workshops-activity-7458261431461965824-yH7b"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"}]

Based on the search results, here's the key information for CoRL 2026:

## Submission Deadlines

The abstract submission deadline is May 26, 2026 11:59 UTC and the paper submission deadline is May 29, 2026 11:59 UTC. The deadlines are final, and no accommodations can be made for missing the abstract deadline or paper deadline.

## Author Guidelines

**Page Limit:** The page limit is 8 pages for the main paper, with Acknowledgments, References, and Appendix (optional) not counting towards the page limit.

**Content Requirements:** All submissions should include a Limitations section, explicitly describing limiting assumptions, failure modes, and other limitations of the results and experime
…[truncated 740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "WebSearch",
  "elapsed_ms": 7394
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-15T12:27:43.943566+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 submission format template double blind anonymous review policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 submission format template double blind anonymous review policy"
  }
}
```

</details>

---


### Tool call

_source line 21 · 2026-05-15T12:27:44.898717+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-15T12:27:45.301075+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-15T12:27:51.204990+00:00_

Web search results for query: "CoRL 2026 submission format template double blind anonymous review policy"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"ICML 2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"ICLR 2026 Workshop on AI with Recursive Self-Improvement 1 Workshop Summary","url":"https://openreview.net/pdf?id=OsPQ6zTQXV"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"Double-Anonymous Review for Robotics","url":"https://arxiv.org/html/2406.10059v1"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Instruction for Presentations","url":"https://www.corl.org/contributions/instruction-for-presentations"},{"title":"ICWSM 2026: Submit","url":"https://www.icwsm.org/2026/submit.html"}]

Based on the search results, here's the information about CoRL 2026 submission format, template, and anonymity policy:

## Double-Blind Anonymous Review Policy

CoRL is double-blind, which means all papers must be anonymized. The accepted papers and reviews will be publicly accessible and de-anonymized after decisions are announced.

## Submission Format

The page limit is 8 pages for the main paper, with acknowledgments, references, and appendix (optional) not counting towards the page limit. The CoRL LaTeX template uses a custom style based on PMLR (Proceedings of Machine Learning Research) format, with papers limited to 8 pages of content plus unlimited references.

## Template

The LaTeX template is available at https://drive.google.com/file/d/1R9irIW0ImqeDHh5g8Ukm2XGy91sWxOsQ/view?usp=drive_link, and auth
…[truncated 602 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "WebSearch",
  "elapsed_ms": 7261
}
```

</details>

---


### Tool result

_source line 24 · 2026-05-15T12:27:51.205544+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'event-gated-adaptive-horizon'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6306
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-15T12:27:51.258022+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "elapsed_ms": 5956
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-15T12:27:55.888017+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-15T12:27:56.390265+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-15T12:27:56.641769+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "memory.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "file": "memory.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-15T12:27:56.692906+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/memory.md\", \"content\": \"# Memory\\n\\n## 2026-05-15: dm_control 渲染崩溃修复 — LD_PRELOAD + MUJOCO_GL\\n\\n**问题**：conda base 环境的 `libstdc++.so.6` 仅支持 GLIBCXX_3.4.26，系统 `libOSMesa.so` → `libLLVM-15.so.1` 需要 3.4.30。PyOpenGL 加载失败 → `_p.GL = None` → `AttributeError: 'NoneType' object has no attribute 'glGetError'`。另一种表现：dm_control rendering executor 线程池崩溃 `RuntimeError: cannot schedule new futures after shutdown`。\\n\\n**修复**：所有训练命令必须包含：\\n```\\nLD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=osmesa python dreamer.py ...\\n```\\n\\n**持久化**：已写入 conda activate.d 脚本 (`/root/miniconda3/etc/conda/activate.d/mujoco_env.sh`)，后续 conda activate base 自动生效。但 submit_training_job 的 command 仍应显式包含这两个环境变量以防万一。\\n\\n**submit_training_job vs ssh_execute 的 device 陷阱**：submit_training_job 设置 CUDA_VISIBLE_DEVICES 隔离，脚本内只能用 `--device cuda:0`。直接 ssh_execute 不隔离，两张卡都可见，可用 `cuda:0` 或 `cuda:1`。混用会导致 \\\"invalid device ordinal\\\"。\\n\\n## 2026-05-15: 服务器代码目录确认\\n\\n源码在 `/root/autodl-tmp/event-gated-adaptive-horizon/`，不在 `/root/runs/event-gated-adaptive-horizon/`（后者只有日志）。启动命令的 cd 必须指向 autodl-tmp。\\n\\n## 2026-05-15: 009e Collapse 确认 — 独立 Collapse Rate = 1/2\\n\\n**009e 是 008d 的延续运行（same seed=1）**，eval 5K-55K 完全一致（确定性复现）。009e 延长到 105K：eval 131.08，nve@55K=4.12x (normalized)。65K bounce 到 250 是 transient，actor_loss@85K 翻正（+0.011）。\\n\\n**独立 seed 统计（2 个独立 seed）**：\\n- seed 1 (008d/009e): **Collapsed** (eval 131@105K, nve@55K=4.12x)\\n- seed 2 (009b): **Self-corrected** (eval 268@105K, nve transient 2.05x@25K → 0.38x@105K)\\n\\n**正确崩溃率**：trained dt_emb + subsample ON → **1/2 independent seeds collapse (50%)**。不是 2/3——008d 和 009e 是同一 seed，只计一次。\\n\\n**009e 额外价值**：延长运行揭示\\\"部分恢复后再崩\\\"模式（65K bounce 但 value 仍膨胀 174→190，最终 95K-105K 再跌至 131）。证明 transient recovery 不代表真恢复。\\n\\n## 2026-05-15: D038 — C6 Falsified: dt=1 Imagination 不阻止 CIVO Collapse\\n\\n**008e
…[truncated 1454 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-15T12:28:02.323643+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-15T12:28:02.424760+00:00_

1	\begin{abstract}
2	Temporal abstraction via variable-rate imagination is a natural extension of world-model reinforcement learning, yet we find that every variable-rate configuration of DreamerV3 degrades performance---despite the success of identical $\Delta t$-conditioning in MPC-based methods. Through a factorial diagnostic on Walker Walk, we identify trained temporal embedding as the causal factor and characterize the resulting failure mode: \emph{conditioning-induced value overestimation} (CIVO). The trained embedding enables the RSSM reward head to develop a $2.78\times$ prediction gap between $\Delta t{=}1$ and $\Delta t{=}2$, which the critic internalizes as optimistic values. A normalized value-to-eval ratio threshold of $1.5\times$ achieves 4/4 separating power within the factorial grid (88.9\% accuracy across all configurations, with one false negative under $\Delta t{=}1$-only imagination). The same CIVO trigger produces stochastic downstream outcomes across seeds---full collapse, self-correction, and oscillatory degradation---from identical configurations. Critically, restricting imagination to $\Delta t{=}1$ does not prevent collapse: one of two seeds fails via a distinct non-CIVO pathway with increasing entropy, revealing that trained temporal conditioning creates vulnerability through multiple mechanisms. Our analysis identifies the feedback architecture---imagination-based actor-critic bootstrapping versus MPC re-planning---as the structural factor that transforms manageable model imprecision into pathological value dynamics.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-15T12:28:03.329708+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-15T12:28:03.531297+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	TAWM \citep{nhu2025tawm} shows that conditioning a world model on step size $\dt$ yields consistent gains within TD-MPC2's MPC framework \citep{hansen2024tdmpc2}. Can the same $\dt$-conditioning bring temporal abstraction to imagination-based actor-critic methods like DreamerV3 \citep{hafner2023dreamerv3}, where policies are trained entirely in imagined rollouts?
5	
6	We find that it cannot. Every variable-rate configuration we test degrades performance catastrophically: fixed $\dt{=}2$ collapses to $14\%$ of baseline, fixed $\dt{=}4$ never exceeds $19\%$ of baseline, and a learned Gumbel-Softmax gate collapses to $11\%$. Through a factorial analysis on Walker Walk \citep{tassa2018dmcontrol}, we isolate the \emph{trained} $\dt$-embedding as the causal factor. This embedding enables the RSSM reward head to develop a $2.78\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$, which the critic internalizes as optimistic value estimates---a failure mode we term \emph{conditioning-induced value overestimation} (CIVO). A normalized value-to-eval threshold of $\nve > 1.5\times$ achieves 4/4 separating power within the factorial grid (88.9\% across all configurations), analogous to the delusional bias of \citet{lu2018nondelusional} but arising from model imprecision amplified by learned temporal conditioning.
7	
8	Three further findings complicate the picture: (1)~the same CIVO trigger produces stochastic downstream outcomes---full collapse, self-correction, and oscillatory degradation---across seeds of identical configurations; (2)~restricting imagination to $\dt{=}1$ while retaining the trained embedding does not prevent collapse, with one of two seeds failing via a qualitatively distinct non-CIVO pathway (evaluation-driven, increasing entropy); and (3)~the contrast with TAWM identifies the feedback architecture---imagination-based bootstrapping versus MPC re-planning---as the structural factor that transforms mana
…[truncated 61 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-15T12:28:03.531694+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-15T12:28:03.583017+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-15T12:28:06.903699+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/agent"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-15T12:28:07.861106+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/sessions/review_director_9a57450c.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-15T12:28:07.961972+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-15T12:28:08.063068+00:00_

1	\section{Experimental Setup}
2	\label{sec:methodology}
3	
4	\subsection{Base Architecture}
5	\label{sec:base_arch}
6	
7	All experiments build on DreamerV3 \citep{hafner2023dreamerv3}, which learns a recurrent state-space model (RSSM) with discrete latent states ($32$ categories $\times$ $32$ classes), uses symlog-transformed predictions, and trains an actor-critic entirely within imagined trajectories. The standard configuration imagines $H{=}15$ steps at a fixed temporal resolution of $\dt{=}1$, meaning each imagination step corresponds to one environment transition.
8	
9	\subsection{Variable-Rate Imagination Mechanism}
10	\label{sec:variable_rate}
11	
12	We introduce three orthogonal architectural modifications that enable variable-rate imagination in DreamerV3. Each can be independently toggled to isolate its contribution.
13	
14	\paragraph{Temporal embedding.}
15	A learned embedding $e(\dt)$ is concatenated to the RSSM input at each imagination step, conditioning state predictions on the temporal scale. We test three modes:
16	\begin{itemize}[nosep,leftmargin=*]
17	\item \textbf{Trained}: embedding parameters are updated via backpropagation through the world model loss, allowing the RSSM to co-adapt its dynamics and reward predictions to the temporal scale.
18	\item \textbf{Untrained}: a fixed random projection of identical dimensionality. The RSSM receives a temporal signal but cannot co-adapt to it.
19	\item \textbf{Removed}: embedding dimension set to zero; no temporal conditioning signal is provided.
20	\end{itemize}
21	The trained-vs-untrained contrast is the key causal control: it isolates the effect of \emph{learning} the temporal conditioning from its mere architectural presence.
22	
23	\paragraph{Temporal subsampling.}
24	When enabled, the replay buffer augments training data with variable-$\dt$ transitions by subsampling consecutive frames. Concretely, with a maximum subsampling factor of~2, the RSSM trains on both $\dt{=}1$ and $\dt{=}2$ transitions
…[truncated 6703 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-15T12:28:08.063527+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-15T12:28:08.114438+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around six findings (F1--F6) that establish a causal chain from trained temporal conditioning to pathological value dynamics and performance collapse. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\nve$), defined as the ratio of a configuration's imagined value to evaluation return, normalized by the baseline's ratio at the same training step.
5	
6	%% ============================================================
7	%% TABLE 1: Main results summary
8	%% ============================================================
9	
10	\begin{table*}[t]
11	\centering
12	\caption{All configurations and outcomes. Configurations with trained $\dt$-embedding and $\nve > 1.5\times$ are shaded.}
13	\label{tab:main_results}
14	\footnotesize
15	\setlength{\tabcolsep}{4pt}
16	\begin{tabular}{llcccccl}
17	\toprule
18	\textbf{Exp} & \textbf{Config} & \textbf{dt\_emb} & \textbf{Sub} & \textbf{H} & \textbf{Eval@final} & \textbf{NVE} & \textbf{Outcome} \\
19	\midrule
20	001 & Baseline ($\dt{=}1$) & --- & OFF & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
21	006 & Fixed $\dt{=}2$ & trained & OFF & 15 & 132.9 @65K & --- & Collapsed \\
22	007 & Fixed $\dt{=}4$ & trained & OFF & 15 & 152.5 @55K & --- & Collapsed \\
23	005 & Learned gate & trained & ON & 15 & 98.8 @145K & --- & Collapsed \\
24	\midrule
25	\rowcolor{gray!15}
26	008d & Factorial (s0) & trained & ON & 8 & 82.8 @55K & 4.12$\times$ & Full collapse \\
27	\rowcolor{gray!15}
28	009b & Factorial (s2) & trained & ON & 8 & 267.9 @105K & 0.38$\times$ & Self-correction \\
29	\rowcolor{gray!15}
30	009e & Factorial (s1) & trained & ON & 8 & 131.1 @105K & 1.57$\times$ & Oscillatory \\
31	008f & No dt\_emb (s0) & none & ON & 8 & 503.0 @105K & 0.30$\times$ & Healthy \\
32	009c & No dt\_emb (s2) & none & ON & 8 & 148.3 @105K & 1.1
…[truncated 15200 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-15T12:28:12.763138+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-15T12:28:13.215850+00:00_

1	\section{Analysis \& Discussion}
2	\label{sec:analysis}
3	
4	The preceding results establish that trained $\dt$-embedding is the causal factor behind pathological value dynamics in variable-rate DreamerV3. In this section, we synthesize these findings into a mechanistic account of conditioning-induced value overestimation (CIVO), explain why the same CIVO trigger produces divergent outcomes across seeds, contrast the imagination-based setting with MPC-based temporal conditioning, and discuss the fundamental tension inherent in the $\dt$-embedding design.
5	
6	\subsection{The CIVO Mechanism}
7	\label{sec:civo_mechanism}
8	
9	The RSSM fidelity analysis (Table~\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO.  The trained $\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\dt{=}1$ is $0.0568$, while at $\dt{=}2$ it rises to $0.1579$---a $2.78\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\times$ gap, and the baseline shows $1.56\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.
10	
11	This asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\dt$-embedding causes RSSM predictions at $\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\nve$ above $1.5\times$, followed by evaluation collapse.  In exp\_008d (seed 0), $\nve$ rises from $1
…[truncated 10750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-15T12:28:13.216341+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-15T12:28:13.720701+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We have presented a systematic factorial diagnostic of temporal abstraction in DreamerV3, identifying trained $\dt$-embedding as the causal factor behind conditioning-induced value overestimation (CIVO). The key findings are:
5	
6	\begin{enumerate}[nosep,leftmargin=*]
7	\item Every variable-rate imagination configuration degrades relative to the $\dt{=}1$ baseline, with degradation scaling monotonically with $\dt$.
8	\item Trained $\dt$-embedding reliably triggers pathological value overestimation ($\nve > 1.5\times$, 4/4 separating power within the factorial grid, 88.9\% across all configurations), while untrained or removed embeddings prevent it.
9	\item The RSSM reward head develops a $2.78\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$ under trained conditioning, providing the systematic bias that drives critic overestimation.
10	\item The same CIVO trigger produces stochastic downstream outcomes---full collapse, self-correction, and oscillatory degradation---across seeds of identical configurations.
11	\item Restricting imagination to $\dt{=}1$ does not fully prevent collapse: one of two seeds fails via a qualitatively distinct non-CIVO pathway (eval-driven with increasing entropy), demonstrating that the trained $\dt$-embedding creates vulnerability through multiple mechanisms.
12	\end{enumerate}
13	
14	The contrast with TAWM's success in MPC identifies the feedback architecture as the critical factor: $\dt$-conditioning succeeds when errors are contained by re-planning from real states, but fails when errors compound through imagination-based actor-critic bootstrapping.
15	
16	\paragraph{Limitations.}
17	Our experiments focus on a single environment (Walker Walk) and a single world-model architecture (DreamerV3/RSSM). While multi-seed replication establishes robustness within this setting, generalization to other environments and architectures---particularly transformer-based world models such as Dre
…[truncated 863 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-15T12:28:13.721224+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-15T12:28:13.774110+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Temporal Abstraction.}
5	The options framework \citep{sutton1999options} and model-free action-repetition methods \citep{sharma2017figar, biedenkapp2021temporl, lakshminarayanan2017dynamic} achieve temporal abstraction by training values on real transitions, insulating them from model-induced bias. In world-model RL, the Dreamer family \citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3} and transformer-based variants \citep{micheli2023iris, robine2023twm, hafner2025dreamerv4} train policies in imagination at fixed $\dt{=}1$. Several works introduce temporal abstraction via hierarchical representations \citep{gumbsch2024thick, mattes2024hieros}, goal-conditioned jumps \citep{li2025lsimagine}, or multi-scale state-space models \citep{shaj2023mts3}, but none conditions a flat dynamics model on $\dt$ for imagination-based policy training.
6	
7	\paragraph{TAWM and the MPC--Imagination Contrast.}
8	TAWM \citep{nhu2025tawm} conditions a world model on $\dt$ within TD-MPC2 \citep{hansen2024tdmpc2} and achieves consistent gains. The critical distinction is architectural: TAWM re-plans from real states at every step, so model errors do not accumulate into the critic. We show that identical $\dt$-conditioning fails in DreamerV3's imagination loop, where errors compound through bootstrapping---transforming manageable imprecision into pathological value overestimation.
9	
10	\paragraph{Value Overestimation.}
11	Value overestimation is well-studied in model-free \citep{fujimoto2018td3, vanhasselt2016double} and model-based settings \citep{janner2019mbpo, yu2020mopo}. \citet{lu2018nondelusional} identify delusional bias from policy-class constraints; our CIVO is mechanistically distinct, arising from model imprecision amplified by learned temporal conditioning. \citet{tallec2019making} show Q-function degradation with temporal resolution mismatches, underpinning our finding at $\dt > 1$. \citet{f
…[truncated 299 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-15T12:28:20.378035+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-15T12:28:20.428727+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/code/configs.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260514T062606/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260514T062606/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260514T062606/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260514T062606/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260514T062606/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260514T062606/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260514T062606/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260515T004704/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260515T004704/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/dream_reports/dream_20260515T004704/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen
…[truncated 1417 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-15T12:28:24.395518+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-15T12:28:24.500400+00:00_

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
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/chats/feishu_group_oc_dd4a07a509df7e5f9a31d65f776059bc_director.jsonl:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/chats/feishu_group_oc_dd4a07a509df7e5f9a31d65f776059bc_director.jsonl:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/chats/feishu_group_oc_dd4a07a509df7e5f9a31d65f776059bc_director.jsonl:50:{"ts": "2026-05-15T12:28:24.395518+00:00", "role": "tool", "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director", "text": "called Grep", "tool": "Grep", "tool_args": {"pattern": "external_review|paperreview", "path": "/
…[truncated 113 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Grep",
  "elapsed_ms": 104
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-15T12:28:29.421386+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai\"",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9",
  "glob": "**/config*.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai\"",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9",
    "glob": "**/config*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-15T12:28:29.472015+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-15T12:28:33.343068+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.{yaml,yml,toml,json}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.{yaml,yml,toml,json}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-15T12:28:33.393700+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/code/configs.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-15T12:28:39.398636+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external|paperreview|review\"",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9",
  "glob": "**/settings*.{yaml,yml,json,toml}",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external|paperreview|review\"",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9",
    "glob": "**/settings*.{yaml,yml,json,toml}",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-15T12:28:39.450915+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Grep",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-15T12:29:30.848351+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 & 实验设计**\n\n### 投稿信息\n- **Venue**: CoRL 2026 Main Conference\n- **Deadline**: 2026-05-29 (abstract: 2026-05-26)\n- **格式要求**: 8页正文, PMLR模板 (`\\usepackage[final]{corl_2026}`), double-blind, 须包含 Limitations section\n- **论文路径**: `projects/event-gated-adaptive-horizon/docs/paper/main.tex`（含7个分节 .tex 文件）\n\n### 论文概述\n标题：\"Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n\n这是一篇诊断性论文，通过 factorial ablation 在 Walker Walk (DMC) 上分析为什么 dt-conditioning 在 DreamerV3 的 imagination-based actor-critic 中失败（尽管在 TAWM/TD-MPC2 的 MPC 框架中成功）。核心发现：trained dt-embedding 导致 RSSM reward head 产生 2.78× 的跨时间尺度预测偏差，critic 将其内化为过度估值（CIVO）。\n\n### 你需要重点审查\n1. **因果推断有效性**：factorial design 是否真的能支撑\"trained dt-embedding is the causal factor\"的强因果声明？有无混淆因素？\n2. **统计检验力**：大多数配置仅 2-3 seeds。对于声称的\"4/4 separating power\"和\"88.9% accuracy\"，这个样本量是否足够支撑结论？是否需要置信区间或统计检验？\n3. **NVE 阈值 1.5×**：该阈值是 empirically determined 还是 data-driven overfitting？是否 post-hoc 选择？\n4. **单环境局限**：所有实验仅在 Walker Walk 上进行。因果声明能否推广？\n5. **实验设计逻辑**：factorial grid 的设计是否有遗漏的关键对比组？例如 trained embedding + subsample OFF + H=8 是否测试过？\n6. **105K 训练步数**：baseline 跑到 505K 而 treatment 只跑到 105K，这是否公平？\n\n请按标准学术审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues → Overall Assessment (1-10分)。",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 & 实验设计**\n\n### 投稿信息\n- **Venue**: CoRL 2026 Main Conference\n- **Deadline**: 2026-05-29 (abstract: 2026-05-26)\n- **格式要求**: 8页正文, PMLR模板 (`\\usepackage[final]{corl_2026}`), double-blind, 须包含 Limitations section\n- **论文路径**: `projects/event-gated-adaptive-horizon/docs/paper/main.tex`（含7个分节 .tex 文件）\n\n### 论文概述\n标题：\"Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n\n这是一篇诊断性论文，通过 factorial ablation 在 Walker Walk (DMC) 上分析为什么 dt-conditioning 在 DreamerV3 的 imagination-based actor-critic 中失败（尽管在 TAWM/TD-MPC2 的 MPC 框架中成功）。核心发现：trained dt-embedding 导致 RSSM reward head 产生 2.78× 的跨时间尺度预测偏差，critic 将其内化为过度估值（CIVO）。\n\n### 你需要重点审查\n1. **因果推断有效性**：factorial design 是否真的能支撑\"trained dt-embedding is the causal factor\"的强因果声明？有无混淆因素？\n2. **统计检验力**：大多数配置仅 2-3 seeds。对于声称的\"4/4 separating power\"和\"88.9% accuracy\"，这个样本量是否足够支撑结论？是否需要置信区间或统计检验？\n3. **NVE 阈值 1.5×**：该阈值是 empirically determined 还是 data-driven overfitting？是否 post-hoc 选择？\n4. **单环境局限**：所有实验仅在 Walker Walk 上进行。因果声明能否推广？\n5. **实验设计逻辑**：factorial grid 的设计是否有遗漏的关键对比组？例如 trained embedding + subsample OFF + H=8 是否测试过？\n6. **105K 训练步数**：baseline 跑到 505K 而 treatment 只跑到 105K，这是否公平？\n\n请按标准学术审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues → Overall Assessment (1-10分)。",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-15T12:29:44.180476+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13332
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-15T12:29:44.683258+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 & 贡献度 & Venue Fit & Related Work**\n\n### 投稿信息\n- **Venue**: CoRL 2026 Main Conference\n- **Deadline**: 2026-05-29 (abstract: 2026-05-26)\n- **格式要求**: 8页正文, PMLR模板 (`\\usepackage[final]{corl_2026}`), double-blind, 须包含 Limitations section\n- **论文路径**: `projects/event-gated-adaptive-horizon/docs/paper/main.tex`（含7个分节 .tex 文件）\n\n### 论文概述\n标题：\"Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n\n诊断性论文，识别出在 DreamerV3 中 dt-conditioning 失败的根因（trained dt-embedding 导致 CIVO），并与 TAWM (MPC-based) 的成功形成对比，归因于 feedback architecture 的差异。\n\n### 你需要重点审查\n1. **Venue Fit (CoRL)**：CoRL 侧重 robot learning，本文实验仅在 DMC Walker Walk（非真实机器人任务）上进行。temporal abstraction 对 robotics 的重要性是否被充分 motivate？是否应该有更多 robotics-relevant 的讨论或实验？\n2. **贡献度**：这是一篇\"负面结果+诊断\"论文。CIVO 的发现是否足够深入和 actionable 以达到 CoRL 主会议的接收门槛？\n3. **新颖性**：\n   - value overestimation 在 MBRL 中已被广泛研究 (TD3, MBPO, MOPO)。CIVO 与已有工作的区别是否清晰？\n   - factorial ablation 方法本身是否有方法论创新？\n4. **Related Work 完整性**：\n   - 是否遗漏了重要的 temporal abstraction in MBRL 工作？\n   - DreamerV4 (transformer-based) 的讨论是否充分？\n   - 是否有其他尝试在 Dreamer 中做 multi-dt 的工作被遗漏？\n   - TempoRL, FiGAR, Dynamic-dt 等 model-free temporal abstraction 的关系是否充分讨论？\n5. **与 TAWM 的对比**：仅基于 architectural reasoning 而非实证对比——是否应该实际运行 TAWM 来验证？\n6. **Actionability**：论文是否提供了足够的前进方向？\"hierarchical approaches may work\"是否太泛？\n\n请按标准学术审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues → Overall Assessment (1-10分)。",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 & 贡献度 & Venue Fit & Related Work**\n\n### 投稿信息\n- **Venue**: CoRL 2026 Main Conference\n- **Deadline**: 2026-05-29 (abstract: 2026-05-26)\n- **格式要求**: 8页正文, PMLR模板 (`\\usepackage[final]{corl_2026}`), double-blind, 须包含 Limitations section\n- **论文路径**: `projects/event-gated-adaptive-horizon/docs/paper/main.tex`（含7个分节 .tex 文件）\n\n### 论文概述\n标题：\"Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n\n诊断性论文，识别出在 DreamerV3 中 dt-conditioning 失败的根因（trained dt-embedding 导致 CIVO），并与 TAWM (MPC-based) 的成功形成对比，归因于 feedback architecture 的差异。\n\n### 你需要重点审查\n1. **Venue Fit (CoRL)**：CoRL 侧重 robot learning，本文实验仅在 DMC Walker Walk（非真实机器人任务）上进行。temporal abstraction 对 robotics 的重要性是否被充分 motivate？是否应该有更多 robotics-relevant 的讨论或实验？\n2. **贡献度**：这是一篇\"负面结果+诊断\"论文。CIVO 的发现是否足够深入和 actionable 以达到 CoRL 主会议的接收门槛？\n3. **新颖性**：\n   - value overestimation 在 MBRL 中已被广泛研究 (TD3, MBPO, MOPO)。CIVO 与已有工作的区别是否清晰？\n   - factorial ablation 方法本身是否有方法论创新？\n4. **Related Work 完整性**：\n   - 是否遗漏了重要的 temporal abstraction in MBRL 工作？\n   - DreamerV4 (transformer-based) 的讨论是否充分？\n   - 是否有其他尝试在 Dreamer 中做 multi-dt 的工作被遗漏？\n   - TempoRL, FiGAR, Dynamic-dt 等 model-free temporal abstraction 的关系是否充分讨论？\n5. **与 TAWM 的对比**：仅基于 architectural reasoning 而非实证对比——是否应该实际运行 TAWM 来验证？\n6. **Actionability**：论文是否提供了足够的前进方向？\"hierarchical approaches may work\"是否太泛？\n\n请按标准学术审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues → Overall Assessment (1-10分)。",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-15T12:29:57.640555+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12957
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-15T12:29:57.742430+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "3",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 3\n\n**你的审查侧重：格式合规 & 写作质量 & 呈现清晰度**\n\n### 投稿信息\n- **Venue**: CoRL 2026 Main Conference\n- **Deadline**: 2026-05-29 (abstract: 2026-05-26)\n- **格式要求**: 8页正文, PMLR模板 (`\\usepackage[final]{corl_2026}`), double-blind, 须包含 Limitations section\n- **匿名规则**: Double-blind（不可泄露作者身份）\n- **论文路径**: `projects/event-gated-adaptive-horizon/docs/paper/main.tex`（含7个分节 .tex 文件）\n- **模板**: 官方 LaTeX template 使用 `\\usepackage[final]{corl_2026}`，基于 PMLR 格式\n\n### 论文概述\n标题：\"Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n\n诊断性论文，factorial ablation 分析 DreamerV3 中 variable-rate imagination 失败的原因。\n\n### 你需要重点审查\n1. **模板合规**：当前论文使用 `\\documentclass[10pt,letterpaper,twocolumn]{article}` + `\\usepackage[margin=0.75in]{geometry}`，**未使用 CoRL 官方 PMLR 模板**。这是否会导致 desk reject？\n2. **页数合规**：检查正文是否在8页以内（不含参考文献和附录）\n3. **Double-blind 合规**：\n   - 作者信息是否正确匿名化？（当前显示 \"Anonymous Authors\"）\n   - 正文中是否有泄露身份的线索（如 self-citation 用第一人称、GitHub 链接、致谢等）？\n4. **Limitations Section**：CoRL 2026 要求包含 Limitations section。检查是否存在及质量。\n5. **写作质量**：\n   - Abstract 是否过长？是否清晰传达核心贡献？\n   - Introduction 的叙事是否引人入胜？\n   - Figures/Tables 是否 self-contained（caption 足够描述内容）？\n   - 术语是否一致（CIVO, NVE, dt-embedding 等首次出现是否定义）？\n6. **图表质量**：引用了 fig1-fig6 的 PDF 文件，检查路径和命名是否一致\n7. **参考文献格式**：使用 natbib + plainnat，是否符合 PMLR 惯例？\n8. **Supplementary materials**：是否需要附录或补充材料？\n\n请按标准学术审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues → Overall Assessment (1-10分)。",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "3",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 3\n\n**你的审查侧重：格式合规 & 写作质量 & 呈现清晰度**\n\n### 投稿信息\n- **Venue**: CoRL 2026 Main Conference\n- **Deadline**: 2026-05-29 (abstract: 2026-05-26)\n- **格式要求**: 8页正文, PMLR模板 (`\\usepackage[final]{corl_2026}`), double-blind, 须包含 Limitations section\n- **匿名规则**: Double-blind（不可泄露作者身份）\n- **论文路径**: `projects/event-gated-adaptive-horizon/docs/paper/main.tex`（含7个分节 .tex 文件）\n- **模板**: 官方 LaTeX template 使用 `\\usepackage[final]{corl_2026}`，基于 PMLR 格式\n\n### 论文概述\n标题：\"Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n\n诊断性论文，factorial ablation 分析 DreamerV3 中 variable-rate imagination 失败的原因。\n\n### 你需要重点审查\n1. **模板合规**：当前论文使用 `\\documentclass[10pt,letterpaper,twocolumn]{article}` + `\\usepackage[margin=0.75in]{geometry}`，**未使用 CoRL 官方 PMLR 模板**。这是否会导致 desk reject？\n2. **页数合规**：检查正文是否在8页以内（不含参考文献和附录）\n3. **Double-blind 合规**：\n   - 作者信息是否正确匿名化？（当前显示 \"Anonymous Authors\"）\n   - 正文中是否有泄露身份的线索（如 self-citation 用第一人称、GitHub 链接、致谢等）？\n4. **Limitations Section**：CoRL 2026 要求包含 Limitations section。检查是否存在及质量。\n5. **写作质量**：\n   - Abstract 是否过长？是否清晰传达核心贡献？\n   - Introduction 的叙事是否引人入胜？\n   - Figures/Tables 是否 self-contained（caption 足够描述内容）？\n   - 术语是否一致（CIVO, NVE, dt-embedding 等首次出现是否定义）？\n6. **图表质量**：引用了 fig1-fig6 的 PDF 文件，检查路径和命名是否一致\n7. **参考文献格式**：使用 natbib + plainnat，是否符合 PMLR 惯例？\n8. **Supplementary materials**：是否需要附录或补充材料？\n\n请按标准学术审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues → Overall Assessment (1-10分)。",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-15T12:29:59.358607+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1616
}
```

</details>

---


### Assistant

_source line 64 · 2026-05-15T12:30:07.685620+00:00_

Round 1 审稿任务已分配给 3 名 Reviewer：

- **R1** (方法严谨性 & 实验设计) → 已触发
- **R2** (新颖性 & 贡献度 & Venue Fit) → 已触发  
- **R3** (格式合规 & 写作质量) → 已触发

等待各 Reviewer 独立审稿结果返回后进入交叉分享阶段（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 2

## Round 2

2 recorded events


### User

_source line 65 · 2026-05-15T12:34:09.485555+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿意见

**论文**: "Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
**审查侧重**: 方法严谨性 & 实验设计

---

## 总体评分

**Overall**: 4/10 (Ok but not good enough — rejection)
**Confidence**: 4/5 (Confident but not absolutely certain)

**一句话总结**: 有趣的诊断视角和清晰的 CIVO 机制描述，但 2-3 seeds 的统计基础无法支撑论文的强因果声明，单环境局限严重削弱泛化性，且对 CoRL 的 robotics relevance 不足。

---

## 官方维度打分（基于 CoRL review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Originality | 3/5 | CIVO 机制是新的观察，但本质是"model error + bootstrapping = value overestimation"的已知问题在新 setting 下的实例化 |
| Quality | 2/5 | Factorial design 结构良好但统计检验力极弱（2-3 seeds），NVE 阈值 post-hoc，因果声明过强 |
| Clarity | 4/5 | 写作清晰，结构良好，Figure/Table 信息量充足 |
| Significance | 2/5 | 单环境 + 单架构的 negative result，对社区的指导价值有限 |
| Relevance | 1/5 | 无任何机器人实验或机器人问题讨论，DMC Walker Walk 不满足 CoRL 对 robot learning relevance 的要求 |
| Limitations | 4/5 | 诚实地报告了单环境和单架构的局限，但未充分讨论统计检验力不足的问题 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 统计检验力严重不足，无法支撑因果声明

- 具体位置：Section 4.3 ("2--3 seeds"), Section 5.2 ("4/4 separating power"), Abstract ("88.9% accuracy")
- 问题：核心因果声明"trained dt-embedding is the causal factor"依赖于 factorial grid 内 2 trained seeds vs 2 untrained seeds 的比较。"4/4 separating power"即 n=2 per group 的完美分离——即使在随机零假设下（每个 seed 独立 50% 概率超阈值），P(4/4) = 1/16 ≈ 6.25%，这离统计显著性（p<0.05 需考虑多重比较修正）甚远。更重要的是，deep RL 中 2-3 seeds 的高方差已被 Henderson et al. (2018) 和 Colas et al. (2018)（后者在论文 bib 中但未被正文引用）反复证明不足以得出可靠结论。论文引用 Agarwal et al. (2021) 来辩护报告 per-seed trajectories，但该文的核心论点恰恰是需要 **更多** seeds 并使用 IQM 等稳健统计量，而非在更少 seeds 上报告个体轨迹。
- 为什么影响接收：一篇诊断性论文的核心价值在于其结论的可靠性。当样本量无法排除随机效应时，"causal factor" 这一强声明不成立。
- 建议修改方向：(1) 至少增加到 5-10 seeds per configuration；(2) 使用 bootstrap CI 或 permutation test 报告置信区间；(3) 将语言从"causal factor"弱化为"associated factor"或"candidate mechanism"。

**N2** [critical] NVE 阈值 1.5× 为 post-hoc 选择，"88.9% accuracy"是训练准确率

- 具体位置：Section 4.4 (Eq. 1), Section 5.2, Abstract
- 问题：NVE > 1.5× 阈值在论文中未说明选择依据。查看数据分布：trained seeds 的 NVE 值为 {4.12, 2.05, 4.12, 1.57, 3.78}，untrained/none seeds 为 {0.30, 1.14, 0.59, 0.58, 0.80}。两组之间有明显间隙，[1.2, 2.0] 范围内任何阈值都能达到类似分类效果。这强烈暗示阈值是在观察数据后选定的。在此基础上报告的 "88.9% accuracy" 是在训练集上的准确率，没有任何 held-out 验证或 cross-validation，因此不具有泛化意义。
- 为什么影响接收：将 post-hoc 选择的指标阈值包装为具有诊断价值的 "separating power" 是方法论上的严重问题，可能误导后续研究者将其作为通用诊断工具使用。
- 建议修改方向：(1) 明确说明阈值选择过程（是 pre-registered 还是 data-driven）；(2) 在独立环境/配置上验证该阈值；(3) 或去除定量声明，改为定性描述"trained embedding 配置的 NVE 系统性高于 untrained 配置"。

**N3** [critical] CoRL Relevance 严重不足

- 具体位置：全文；Section 4.5 (Environment: Walker Walk DMC, proprioceptive)
- 问题：CoRL 明确要求论文"explicitly address a learning question for physical robots"或"test the proposed learning solution on physical robots"。本文仅在 DMC Walker Walk（一个 low-dimensional locomotion simulation）上用 proprioceptive observations 做实验。全文未讨论任何 robotics application，未测试任何 robotics benchmark（如 RoboSuite, ManiSkill, IsaacGym），未讨论 CIVO 对 real-robot deployment 的影响。DreamerV3 虽然可用于 robotics，但本文的分析完全局限在 control suite simulation 层面。
- 为什么影响接收：这是 CoRL 的基本投稿要求，不满足 relevance 门槛可能导致 desk reject。
- 建议修改方向：(1) 至少在一个 robotics-relevant benchmark 上复现核心发现；(2) 增加 Discussion section 讨论 CIVO 对 real-world robot learning 的具体影响（如 sim-to-real transfer 中的 temporal abstraction）。

**N4** [critical] 单环境局限使因果声明不可泛化

- 具体位置：Section 4.5, Conclusion (Limitations paragraph)
- 问题：所有实验仅在 Walker Walk 上进行。这是 DMC 中最简单的连续控制任务之一（24-dim observation, 6-dim action）。CIVO 的发生可能高度依赖于：(a) 动力学的低维度和可预测性——更复杂任务中 RSSM 的 reward gap 模式可能不同；(b) reward 的密度和 scale——sparse reward 任务中 value overestimation 的表现可能不同；(c) observation modality——visual observations 会引入额外的 representation bottleneck。在一个环境上做的诊断无法支撑 Section 6 中关于"structural incompatibility between flat temporal conditioning and imagination-based actor-critic training"的泛化性声明。
- 为什么影响接收：诊断性论文的价值取决于发现的普遍性。单环境发现可能只是 task-specific artifact。
- 建议修改方向：至少增加 2-3 个不同复杂度的 DMC 任务（如 Cheetah Run, Quadruped Walk, Humanoid Walk），验证 CIVO 在不同动力学复杂度下是否稳定出现。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Factorial design 存在混淆变量

- 具体位置：Table 1 (Section 4.3)
- 问题：Factorial grid 的关键比较存在混淆。核心的 "trained vs untrained" 比较：008d (trained + Sub ON + H=8) vs 008a (untrained + Sub OFF + H=15)——这同时改变了三个因素（embedding type, subsampling, horizon）。唯一干净的比较是 008d vs 008f，但 008f 是 embedding **完全移除**（none），而非 untrained。因此实际上没有一组配置同时保持 subsampling 和 horizon 不变，仅改变 trained → untrained embedding。论文声称 008a/008c 是 untrained 控制组，但它们与 008d 在 subsampling 上不同（OFF vs ON），引入了混淆。
- 建议：补充 untrained + Sub ON + H=8 + dt=2 配置，形成与 008d 的干净对比。

**W2** [warning] 105K vs 505K 训练步数不对等

- 具体位置：Section 4.5 ("Treatment configurations run for 105K steps")
- 问题：Baseline 运行到 505K 展示了完整的收敛行为（peak 970.4），但所有 treatment 仅运行到 105K。对于一篇诊断 "collapse" 动态的论文，这创造了不对称的观察窗口：(a) Self-correcting seed 009b（267.9 @105K）可能在更长训练后恢复；(b) "healthy" 的 untrained configs 可能在后期发展出其他 pathology；(c) Oscillatory pattern (009e) 的长期命运未知。论文在 Section 4.5 辩护说 "105K is sufficient to observe both collapse onset and diagnostic markers"，但这是循环论证——你不知道 105K 之后会发生什么，因为你没观察。
- 建议：至少将关键配置（008d 三个 seeds + 008f + 008e_v3 两个 seeds）延长到 300-500K，与 baseline 对等。

**W3** [warning] 对 Pathway B 的解释不充分

- 具体位置：Section 5.6, Section 6.5
- 问题：008e_v3 seed 2 的 non-CIVO collapse (Pathway B) 是论文最有趣的发现之一，但解释极其薄弱。论文仅描述了现象（entropy 增加、eval 下降、value 稳定），然后含糊地归因于 "representation space" 影响。没有提供任何机制性解释：trained embedding 如何在 dt=1 imagination 下导致 actor destabilization？为什么 entropy 增加而非减少？这个 Pathway B 是否可能只是普通的 training instability，与 dt-embedding 无关？Baseline seed 2 (009a) 的稳定性不能排除这一可能，因为增加任何额外 module（包括 subsampling data augmentation）都可能引入 instability。
- 建议：(1) 提供 Pathway B 的具体机制假说并设计实验验证；(2) 或诚实地承认 Pathway B 的 causation 未建立，仅为观察。

**W4** [warning] RSSM fidelity analysis 的解释可能有误

- 具体位置：Table 4 (Section 5.6), Section 6.1
- 问题：Table 4 中 008d (trained embedding) 的 reward MAE at dt=1 是 0.0568，at dt=2 是 0.1579（gap 2.78×）。论文将此解释为 "reward head systematically overpredicts rewards at dt=2"。但 MAE 只衡量误差大小，不区分 over- 和 under-prediction。高 MAE 可能是正向偏差、负向偏差、或高方差的结果。论文需要证明偏差方向是系统性正向的（即 reward over-prediction 而非 under-prediction），才能支撑 CIVO 的 "overestimation" 机制。
- 建议：报告 reward prediction bias（signed error）而非仅 MAE，以验证方向性假设。

**W5** [warning] 格式不符合 CoRL 2026 要求

- 具体位置：main.tex line 1
- 问题：论文使用 `\documentclass[10pt,letterpaper,twocolumn]{article}`，而 CoRL 2026 要求 PMLR 模板（`\usepackage[final]{corl_2026}`）。当前格式虽然视觉上接近双栏，但不符合官方提交要求，可能导致 desk reject。
- 建议：切换到 CoRL 2026 官方 PMLR 模板。

---

## 小问题（不影响接收）

- **bib 质量问题**：`splates2025` 条目 author 为 "SPlaTES, authors"（占位符），`nie2025sdar` 和多个条目使用 "et, al" 代替完整作者列表——BibTeX 中 "et al." 应写完整作者或正确截断。
- **hafner2023dreamerv3** 标注 year=2025 (Nature 发表年) 但 cite key 用 2023——可能造成混淆。
- **Missing citation**: `colas2018seeds` 在 bib 中存在但正文未引用，该文恰恰是关于 seed 数量对 deep RL 结论可靠性影响的直接相关工作，应当引用并讨论。
- Abstract 中 "88.9% accuracy" 放在如此显眼位置有误导性（如 N2 所述）。
- Section 6.4 对 "dt-embedding dilemma" 的讨论倾向于将 negative result 包装为 fundamental insight，但在单环境 + 低 seed 数下，这个 "dilemma" 可能只是实验设计的 artifact。

---

## 主要优势

- **清晰的问题定义**：将 "为什么 dt-conditioning 在 MPC 中成功但在 imagination-based AC 中失败" 作为核心问题，切入点明确且有实际意义。
- **结构化的实验设计**：Factorial ablation 的框架设计本身是好的方法论选择，配置间的对比逻辑清晰。
- **机制描述细致**：CIVO 的四阶段反馈回路（Section 6.1）描述得清楚且有说服力，三种 post-CIVO 结果的刻画也很有信息量。
- **诚实的 Limitations**：论文承认了单环境和单架构的局限，且 Finding F6 的 partial falsification 展示了良好的科学态度。
- **写作质量高**：论文组织良好，Figure/Table 信息密度高，notation 一致。

---

## 总结判断

本文提出了一个有趣的诊断视角（CIVO），但在当前形态下存在多个根本性问题：(1) 2-3 seeds 的统计基础无法支撑强因果声明；(2) NVE 阈值为 post-hoc 选择且无独立验证；(3) 单环境实验严重限制泛化性；(4) 对 CoRL 的 robotics relevance 要求未满足。建议作者大幅增加实验规模（更多 seeds、更多环境），弱化因果语言，并在修改后投稿到更 general 的 RL venue（如 ICML/NeurIPS 的 workshop 或 RLC）。

**建议决定**: Reject (4/10)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 66 · 2026-05-15T12:34:26.689365+00:00_

Reviewer 1 审稿意见已收到。评分 4/10（Reject），核心问题集中在统计检验力不足（2-3 seeds）、NVE 阈值 post-hoc、单环境局限、以及 CoRL robotics relevance 缺失。

等待 Reviewer 2 和 Reviewer 3 的审稿意见返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 3

## Round 3

2 recorded events


### User

_source line 67 · 2026-05-15T12:34:29.313487+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心评价：**4/10 (Reject)**。主要问题：

1. **统计检验力严重不足**（N1）：2-3 seeds 无法支撑 "causal factor" 的强声明，"4/4 separating power" 在 n=2 per group 下缺乏统计意义
2. **NVE 阈值 post-hoc**（N2）：1.5× 阈值明显是数据驱动选择，"88.9% accuracy" 是训练准确率，无独立验证
3. **CoRL relevance 不足**（N3）：全文无 robotics 实验/讨论，不满足 CoRL 基本投稿要求
4. **单环境不可泛化**（N4）：Walker Walk 是 DMC 最简单任务之一，诊断结论可能是 task-specific artifact
5. **Factorial 混淆**（W1）：trained vs untrained 的对比同时改变了 subsampling 和 horizon
6. **训练步数不对等**（W2）：baseline 505K vs treatment 105K 的不对称观察窗口削弱了对 collapse dynamics 的结论

论文的优势在于清晰的问题定义、结构化的 factorial 设计、细致的 CIVO 机制描述和诚实的 limitations 报告。建议增加实验规模后投稿 ICML/NeurIPS workshop 或 RLC。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 68 · 2026-05-15T12:34:38.883620+00:00_

Reviewer 1 审稿意见已收到（4/10, Reject）。等待 Reviewer 2 和 Reviewer 3 的审稿结果返回后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 4

## Round 4

2 recorded events


### User

_source line 69 · 2026-05-15T12:35:13.572984+00:00_

[Reviewer 3 审稿意见]:
## Reviewer 3 — Round 1 审稿报告

**论文**: "Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
**Venue**: CoRL 2026 Main Conference
**审查侧重**: 格式合规 & 写作质量 & 呈现清晰度

---

## 总体评分

**Overall**: 4/10（Borderline Reject）
**一句话总结**: 写作质量出色、诊断方法论清晰，但**未使用 CoRL 官方 PMLR 模板**构成 desk reject 风险，且论文与物理机器人学习的关联薄弱，可能不符合 CoRL scope。

---

## 官方维度打分（基于 CoRL review form 维度）

| 维度 | 评分 | 理由摘要 |
|------|------|----------|
| Originality | 3/5 | CIVO 作为诊断性发现有新意，但本质是 negative result + factorial ablation，概念增量有限 |
| Quality | 3/5 | 实验设计严谨（factorial design），但单环境（Walker Walk）、少 seeds（2-3）限制结论可靠性 |
| Clarity | 4/5 | 写作组织出色，F1-F6 因果链叙述清晰，术语定义到位 |
| Significance | 2/5 | 诊断性发现有价值，但无解决方案；对 CoRL 社区的直接 actionable insight 有限 |
| Relevance | 1/5 | **未涉及物理机器人**，仅在 DMC Walker Walk 上做 proprioceptive 实验；未讨论 robot learning 场景 |
| Limitations | 3/5 | 存在 Limitations 段落，诚实列出了单环境和单架构的限制，但作为子段落而非独立 section |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **未使用 CoRL 2026 官方 PMLR 模板——desk reject 风险**
- 具体位置：`main.tex` 第 1-11 行
- 问题：论文使用 `\documentclass[10pt,letterpaper,twocolumn]{article}` + `\usepackage[margin=0.75in]{geometry}`，**完全没有使用 CoRL 2026 官方模板**。CoRL 2026 Instruction for Authors 明确要求使用官方提供的 LaTeX template（camera-ready 需 `\usepackage[final]{corl_2026}`），并要求保持模板规定的 "text density, fonts, spacing, and margins"。当前的自定义排版（0.75in margins、无 PMLR 页眉/脚注、无 conference footer）与官方格式差异巨大。
- 为什么影响接收：CoRL 2024 desk rejection criteria 明确包括 "formatting issues (length or incorrect format)"。使用非官方模板**极大概率导致 desk reject**，不会进入审稿流程。
- 建议修改方向：立即切换到 CoRL 2026 官方 PMLR 模板，确保首页 footer 包含 "10th Conference on Robot Learning (CoRL 2026), Austin, Texas, USA."。

**N2** [critical] **CoRL scope 适配性严重不足**
- 具体位置：全文，尤其是 Section 4.5（Environment and Training Details）
- 问题：CoRL CFP 明确要求 "Submissions should focus on a core robotics problem" 且 "Papers without robotics focus will be rejected without review"。CoRL 2024 desk rejection criteria 包括 scope（必须 "address a learning question for physical robots" 或 "test solutions on physical robots"）。本文仅在 DMC Walker Walk（一个纯仿真 locomotion task）上使用 proprioceptive observations 做实验，**全文未提及任何物理机器人场景、sim-to-real transfer、或 robot learning 的直接应用**。Analysis & Discussion（Section 6）也未讨论 findings 对 robot learning 的意义。
- 为什么影响接收：即使论文技术质量过关，CoRL 的 relevance 要求是硬约束。当前论文更适合 ICML/NeurIPS/ICLR 等 general ML venue。
- 建议修改方向：(1) 至少增加一个 robot-relevant 环境（如 DMC 的 manipulation task 或 robosuite）的验证实验；(2) 在 Introduction 和 Discussion 中明确阐述 CIVO 对 robot learning 的影响——例如 variable-rate world model 对于需要 multi-timescale control 的实际机器人任务（manipulation、locomotion、navigation）的重要性；(3) 讨论 findings 对 sim-to-real pipeline 中时间分辨率选择的启示。

**N3** [critical] **页数合规性无法验证（因模板错误）**
- 具体位置：全文
- 问题：由于未使用 PMLR 模板，当前排版下的页数无法与 CoRL 的 8-page 限制进行对照。自定义的 0.75in 全向 margins 比 PMLR 模板通常更紧凑，意味着**换成 PMLR 模板后正文极有可能超过 8 页**。论文包含 5 个 figure（其中 3 个 columnwidth、2 个需要验证）、4 个 table（其中 1 个 table*）、大量详细文本（F1-F6 每个 finding 都有完整阐述），内容量很大。
- 为什么影响接收：超页是另一个 desk reject 条件。
- 建议修改方向：换模板后立即编译检查页数。如超页，优先压缩的候选：(a) Section 5（Results）中 F4 和 F5 可精简为1-2段；(b) Table 3（Post-CIVO outcomes）可合并入正文叙述或移至 appendix；(c) Analysis Section 6.2（Seed Divergence）的假设性讨论可大幅精简。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Limitations 作为段落嵌入 Conclusion，而非独立 Section**
- 具体位置：`conclusion.tex` 第 16-17 行，`\paragraph{Limitations.}`
- 问题：CoRL 2026 Instruction for Authors 要求 "must include a Limitations section"，CoRL reviewer guidelines 要求 reviewer 评估 Limitations section 的质量。当前 Limitations 仅是 Conclusion 中的一个 `\paragraph`，不是一个独立的 `\section` 或 `\subsection`。这在形式上可能不满足要求。
- 建议：将 `\paragraph{Limitations.}` 提升为 `\subsection{Limitations}` 或单独的 `\section{Limitations}`（放在 Conclusion 之前或之后）。

**W2** [warning] **Abstract 过长且过于技术化**
- 具体位置：`abstract.tex`
- 问题：Abstract 约 180 词，包含大量具体数字（$2.78\times$、$1.5\times$、88.9%、4/4）和技术术语（CIVO、NVE、RSSM reward head、Gumbel-Softmax gate）。对于 CoRL 这样的 robotics + learning 交叉会议，abstract 需要对不熟悉 DreamerV3 内部机制的 reviewer（如来自 robotics 背景的 reviewer）也能快速理解。当前 abstract 读起来更像是一个 ICML workshop 的 extended abstract。
- 建议：(1) 开头增加 1-2 句建立 motivation（为什么 temporal abstraction 对 robot learning 重要）；(2) 减少具体数字，保留关键发现的定性描述；(3) 结尾增加对 robot learning community 的 takeaway。

**W3** [warning] **Bibliography 严重冗余：77 条 bib entry 中仅 29 条被引用**
- 具体位置：`references.bib`
- 问题：引用验证显示 77 条 bib entry 中有 48 条是 orphan（在 .bib 中存在但论文正文未引用）。此外，`splates2025` 条目的 author 字段为 "SPlaTES, authors"（明显是占位符/不完整条目），多个条目（`nie2025sdar`, `zhang2026instability`, `kobayashi2025metacontroller`, `liu2022dmve`, `kim2025deas`, `lenz2025macura`）使用 "et, al" 作为字面 author，说明 bib 文件是批量生成且未经清理。
- 建议：清理 .bib，移除所有未引用条目；修复占位符 author 字段。虽然未引用的条目不会出现在 compiled PDF 的参考文献列表中，但提交时包含这样的 .bib 文件显得不够专业，且如果 reviewer 查看源文件可能留下负面印象。

**W4** [warning] **参考文献格式可能不符合 PMLR 惯例**
- 具体位置：`main.tex` 第 58 行 `\bibliographystyle{plainnat}`
- 问题：当前使用 `natbib` + `plainnat` 格式。PMLR/CoRL 模板通常自带或指定特定的 bibliography style。切换到官方模板后需确认是否需要使用模板指定的 bib style。
- 建议：换模板后检查并使用官方模板附带的 bibliography style。

**W5** [warning] **fig4_mechanism_diagram.pdf 存在但未被论文引用**
- 具体位置：`artifacts/figures/paper/` 目录
- 问题：论文引用了 fig1, fig2, fig3, fig5, fig6 五个图文件，fig4_mechanism_diagram.pdf 存在于目录中但未在任何 .tex 文件中引用。这意味着论文中图编号为 1-5（LaTeX 自动编号），但底层文件命名跳过了 fig4。如果这个 mechanism diagram 对理解 CIVO 机制有帮助，缺少它是一个呈现缺陷。
- 建议：评估 fig4_mechanism_diagram.pdf 是否应纳入论文（一个 CIVO 机制流程图对理解 Section 6.1 非常有帮助）。如不纳入，重命名其余文件以保持一致性。

---

## 小问题（不影响接收）

- `\ie`, `\eg`, `\cf` 宏定义为 `\textit{i.e.}` 等，但标准学术排版要求这些缩写后面有逗号（"i.e.," 而非 "i.e."），且是否使用斜体存在争议（多数 style guide 不建议斜体）。
- `main.tex` 第 26 行定义了 `\etal` 宏但未在正文中使用（正文用 `et al.` 的自然文本形式或在 bib 中处理）。
- `hafner2023dreamerv3` 的 bib key 用 2023 但 year 字段是 2025（Nature 发表年）。引用验证确认 OpenAlex 记录年为 2023。建议统一。
- 部分 bib entry 的 journal 字段不规范，如 `sutton1999options` 的 journal 为 "Artificial Intelligence 112"（卷号不应在 journal 字段中）。
- Conclusion（Section 7）中 `\paragraph{Future directions.}` 应考虑是否需要保留——如果页数紧张，可移至 appendix。

---

## 主要优势

- **实验设计方法论出色**：factorial ablation 设计清晰，trained vs. untrained vs. removed embedding 的三重对照是确立因果关系的典范做法。
- **叙事结构强**：F1-F6 的因果链式展开使论文从 "what fails" 到 "why it fails" 到 "what doesn't fix it" 有清晰的逻辑递进。
- **诊断指标有价值**：NVE threshold（$1.5\times$）和 RSSM fidelity gap 作为诊断工具有实用价值，且论文诚实报告了 88.9% 准确率（而非声称完美分离）。
- **Multiple pathways 的发现**（F6）是真正有价值的 insight——表明问题比 "fix the critic" 更深层，为后续研究指明了方向。
- **写作清晰度高**：Section 3（Methodology）的 factorial design table 和 Section 5（Results）的 per-seed trajectory 报告方式专业规范，遵循了 Agarwal et al. (2021) 的 best practice。

---

## 总结

本文在写作质量和实验方法论上达到了高标准，factorial diagnostic 框架对 MBRL 社区有价值。然而，**三个 critical 问题严重阻碍其在 CoRL 2026 的接收前景**：

1. **模板不合规**（desk reject 级别）——必须立即切换到 PMLR 官方模板
2. **CoRL scope**——无物理机器人实验、无 robot learning 讨论，不符合 CoRL 的 relevance 要求
3. **页数未知**——换模板后可能超页

建议作者认真考虑目标 venue 的选择。如果坚持投 CoRL，需要增加 robot-relevant 实验并大幅强化 robotics motivation。如果 timeline 不允许这些改动，ICML/NeurIPS/ICLR 可能是更自然的选择。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_3"
}
```

</details>

---


### Assistant

_source line 70 · 2026-05-15T12:35:30.034321+00:00_

已收到 Reviewer 1（4/10）和 Reviewer 3（4/10）的审稿意见。等待 Reviewer 2 的报告到达后进入 Step 2（交叉分享）。

当前状态：
- R1 ✅ 方法严谨性 — 核心问题：统计检验力不足、NVE 阈值 post-hoc、CoRL relevance、单环境
- R2 ⏳ 新颖性 & 贡献度 & Venue Fit — 等待中
- R3 ✅ 格式合规 & 写作质量 — 核心问题：模板不合规(desk reject 风险)、CoRL scope、页数未知

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 5

## Round 5

2 recorded events


### User

_source line 71 · 2026-05-15T12:35:32.673650+00:00_

[Reviewer 3 审稿结果]:
审稿报告已提交给 Review Director。

**核心结论**：论文写作质量和实验方法论均达到较高水准，但有 3 个 critical 问题：

1. **模板不合规**（desk reject 级别）：使用自定义 `\documentclass{article}` 而非 CoRL PMLR 官方模板
2. **CoRL scope 不符**：全文仅在 DMC Walker Walk 仿真环境做实验，未涉及物理机器人
3. **页数风险**：换到 PMLR 模板后正文大概率超过 8 页限制

评分 4/10（Borderline Reject）。建议作者认真考虑是否应转投 ICML/NeurIPS/ICLR 等 general ML venue。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_3"
}
```

</details>

---


### Assistant

_source line 72 · 2026-05-15T12:35:52.531311+00:00_

已收到 Reviewer 1 和 Reviewer 3 的 Round 1 审稿意见。等待 Reviewer 2 提交后进入交叉分享环节。

**当前进度**：
- ✅ Reviewer 1 (方法严谨性): 4/10 — 统计检验力不足、NVE post-hoc、单环境、CoRL relevance
- ⏳ Reviewer 2 (新颖性 & Venue Fit): 待提交
- ✅ Reviewer 3 (格式 & 写作): 4/10 — 模板不合规(desk reject风险)、scope不符、页数风险

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 6

## Round 6

8 recorded events


### User

_source line 73 · 2026-05-15T12:35:54.037322+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 1 审稿意见

**论文**: "Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
**审查侧重**: 新颖性 & 贡献度 & Venue Fit & Related Work

---

## Summary

本文系统调查了将 dt-conditioning（源自 TAWM/TD-MPC2 框架）移植到 DreamerV3 imagination-based actor-critic 中的失败原因。通过 Walker Walk 上的 9 组 factorial ablation，作者识别出 trained dt-embedding 是导致 conditioning-induced value overestimation (CIVO) 的因果因子：trained embedding 使 RSSM reward head 在 dt=1 和 dt=2 之间产生 2.78× 的预测偏差，该偏差通过 imagination bootstrapping 被 critic 内化为系统性高估。论文进一步发现：(1) 同一 CIVO trigger 产生三种随机下游结果（full collapse、self-correction、oscillatory degradation）；(2) 限制 imagination 到 dt=1 不能完全防止崩溃，存在一条 non-CIVO pathway（Pathway B）；(3) 与 TAWM 的对比将 feedback architecture（imagination bootstrapping vs. MPC re-planning）定位为关键结构差异。

---

## 官方维度打分（基于 CoRL Review Form: Originality, Quality, Clarity, Significance, Relevance, Limitations）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Originality | 4/10 | CIVO 是已知 value overestimation 问题在特定 dt-conditioning 下的实例化，方法论（factorial ablation）无创新 |
| Quality | 5/10 | Factorial 设计合理但单环境 + 2-3 seeds 的统计效力不足，TAWM 对比缺乏实证 |
| Clarity | 7/10 | 写作清晰、结构好，NVE 指标定义明确，Findings 组织有序 |
| Significance | 4/10 | 诊断性负面结果，actionable takeaway 太弱，对社区指导有限 |
| Relevance | 3/10 | 仅 DMC Walker Walk，无机器人任务，robotics motivation 缺失 |
| Limitations | 7/10 | 诚实承认单环境和单架构局限，但未讨论统计效力问题 |

---

## 总体评分

**Overall: 4/10 (Reject)**

**一句话总结**: 对一个有趣的负面结果给出了结构化诊断，但单环境实验、与 CoRL robotics 主题的弱关联、以及缺乏 actionable 解决方案，使得本文不达到 CoRL 主会议的接收门槛。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Venue Fit 严重不足——CoRL 要求 robot learning 相关性

- 具体位置：全文；Section 5 (Methodology) §5.5 Environment
- 问题：CoRL 的 scope 要求论文 "explicitly address a learning question for physical robots" 或 "test the proposed learning solution on physical robots"（参考 CoRL 2023 Reviewer Guidelines）。本文全部实验仅在 DMC Walker Walk（proprioceptive，非视觉）上进行，且论文正文未讨论 temporal abstraction 对 robotics 的具体重要性——例如变频控制对机械臂操作的必要性、sim-to-real 中时间分辨率 mismatch 问题、或 real robot 上 MPC vs. imagination 的延迟约束。Introduction (Section 1) 直接从 TAWM 的 RL 结果出发，完全没有 robotics motivation。
- 为什么影响接收：CoRL 审稿人会首先检查 robotics relevance。一篇纯粹在 DMC locomotion 上做 DreamerV3 诊断的论文，即使技术正确，也更适合投 ICML/NeurIPS/ICLR 的 RL track 而非 CoRL。
- 建议修改方向：(1) 增加至少 1-2 个 robotics-relevant 环境（如 Meta-World manipulation、RoboSuite、或 real robot locomotion）上的验证实验；(2) 在 Introduction 中用具体 robotics scenario 来 motivate temporal abstraction 的重要性；(3) 讨论 CIVO 对 sim-to-real transfer 的 implications。

**N2** [critical] 单环境实验无法支撑因果 claim 的泛化性

- 具体位置：Section 5.5 及 Conclusion (Section 7)
- 问题：全部 findings（F1-F6）仅来自 Walker Walk 一个环境。论文声称识别出 "structural incompatibility between flat temporal conditioning and imagination-based actor-critic training"（Section 6.6），但这一结论的泛化性完全未经验证。Walker Walk 是一个相对简单的 locomotion 任务，reward 接近 dense；在 sparse reward 环境、高维视觉输入、multi-object manipulation 等场景下，CIVO 可能表现完全不同——例如 reward prediction gap 的幅度可能因任务 reward structure 而异。
- 为什么影响接收：CoRL 审稿人在 Quality 维度会要求 "results are objectively established"。单环境 + 2-3 seeds 的实验设置不满足这一标准，尤其是论文自身发现 seed 间的巨大方差（F2 中 1/2 seeds collapse）。按 Colas et al. (2018)（论文 .bib 中有但未引用），2-3 seeds 的统计效力极低。
- 建议修改方向：(1) 至少在 3-5 个 DMC tasks 上复现核心 finding（如 Cheetah Run、Humanoid Walk）；(2) 增加 seeds 到 5+ 以提供有意义的统计检验；(3) 如果资源有限，至少对 NVE threshold 的鲁棒性做跨任务讨论。

**N3** [critical] 贡献度不足——纯诊断负面结果缺乏 actionable solution

- 具体位置：Section 6.6 (Implications) 和 Section 7 (Conclusion, Future directions)
- 问题：论文的核心贡献是 "识别 CIVO 失败模式"。但诊断之后，论文未提供任何可验证的解决方案。Section 6.6 提到三个 future directions：(1) hierarchical approaches (THICK/Hieros)、(2) embedding regularization (gradient stopping/spectral norm)、(3) 扩展到 transformer world models——但这些全部是 "we leave to future work" 的表述。Conclusion 的 Future directions 同样只是重述这三点。这意味着论文的 output 仅仅是 "dt-conditioning 在 DreamerV3 中不 work"，缺乏 constructive contribution。
- 为什么影响接收：CoRL 主会议对负面结果论文的接收门槛很高——需要 finding 本身足够深入且 actionable 以抵消缺少正面算法贡献的劣势。类比 "Implementation Matters" (Engstrom et al., 2020) 之所以被接收，是因为它跨大量环境和超参数做了系统性发现且提供了具体的实践指导。本文的 CIVO 诊断局限于单环境且缺乏等价的实践指导。
- 建议修改方向：(1) 实现并测试至少一种 mitigation（如 gradient-stop dt-embedding 对 reward head 的梯度），将其作为 actionable contribution；(2) 或者将 NVE 指标包装为一个通用的 early-warning diagnostic tool，提供可复用的代码和使用指南。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 与 TAWM 的对比仅基于 architectural reasoning，缺乏实证验证

- 具体位置：Section 6.3 (Why MPC Is Immune), Related Work §2 (TAWM paragraph)
- 问题：论文的核心 narrative 之一是 "同一 dt-conditioning 在 TAWM (MPC) 中 work 但在 DreamerV3 (imagination) 中 fail"。但论文从未实际运行 TAWM 来验证。Section 6.3 的分析完全基于 architectural reasoning（"MPC re-plans from real states at every step, so model errors do not accumulate into the critic"）。这一论证虽然 plausible，但存在替代解释——例如 TD-MPC2 和 DreamerV3 的 world model architecture 本身不同（连续 vs. 离散 latent states），training objective 不同（joint vs. detached），这些差异可能同样 confound 对比。
- 建议：至少运行 TAWM 的公开代码在 Walker Walk 上，验证 dt-conditioning 确实在 MPC setting 下 healthy（NVE ≈ 1.0），或引用 TAWM 原文中 Walker Walk 的具体数字。

**W2** [warning] NVE threshold 1.5× 的选取缺乏 principled justification

- 具体位置：Section 5.4 (Diagnostic Metrics), Equation 1
- 问题：1.5× threshold 被描述为在 factorial grid 内有 "4/4 separating power"，但这是事后拟合（post-hoc fitting）到一个仅有 9 个 configurations 的 grid。论文声称 88.9% accuracy (8/9)，但 false negative（008e_v3 s1）恰好是最有诊断价值的 case。没有交叉验证、bootstrapped confidence interval、或理论推导来支撑 1.5× 这个具体数值。对于一个试图建立 diagnostic 标准的论文，这一点令人担忧。
- 建议：讨论 threshold sensitivity（如 1.3× 和 2.0× 下的 accuracy 变化），或承认该 threshold 是探索性的。

**W3** [warning] CIVO 与已知 value overestimation 的区分不够清晰

- 具体位置：Section 6.1 (CIVO Mechanism), Related Work §3 (Value Overestimation paragraph)
- 问题：论文将 CIVO 与 delusional bias (Lu et al., 2018) 区分为 "model-induced vs. policy-class constraints"（Section 6.1, line 13）。但 CIVO 的核心机制——model error 通过 bootstrapping 被 critic 放大——与已知的 MBRL value overestimation 文献（MBPO, MOPO, Frauenknecht et al.）高度相似。论文 Related Work 中对 Frauenknecht et al. (2025) 的讨论是 "we identify the specific dt-embedding-induced reward bias by which rollout divergence corrupts values"（Section 2, line 11），但这一区分的粒度是 "what triggers the bias"（dt-embedding），而非 "how the bias propagates"（同样是 bootstrapping amplification）。一个 reviewer 会问：CIVO 是否只是 "compounding model error in MBRL" 的一个特定实例化（instantiation），而非一个新的失败模式？
- 建议：更精确地定义 CIVO 相对于 general compounding error 的新颖性——可能在于 "learned conditioning feature 主动引入偏差" 而非 "模型本身不够准"，但这一点需要更清晰地阐述。

**W4** [warning] Related Work 遗漏若干相关工作

- 具体位置：Section 2 (Related Work)
- 问题：
  (a) **Becker-Ehmck et al. (2023) "Multi-timestep models for Model-based RL"**——该论文直接研究 multi-timestep world model 在 MBRL 中的效果，与本文主题高度相关，但在 .bib 中存在（`beckerehmck2023multitimestep`）却未在正文中引用或讨论。
  (b) **Park et al. (2021) "Time Discretization-Invariant Safe Action Repetition"** 和 **Wang & Beltrame (2024) "Reinforcement Learning with Elastic Time Steps"**——均在 .bib 中但未引用，它们研究 time-discretization 对 RL 的影响，与 Section 6.3 (Why MPC Is Immune) 和 Tallec et al. (2019) 的讨论直接相关。
  (c) **DreamerV4 讨论不足**：Section 6.6 仅用一段提到 DreamerV4 的 transformer architecture "may mitigate or amplify" CIVO，但未讨论 DreamerV4 的 attention mechanism 如何具体影响 temporal conditioning 的 co-adaptation 问题。考虑到 DreamerV4 是 Dreamer 家族的最新成员，这一讨论的缺失是显著的。
  (d) **.bib 中 48 个 orphan entries** 未在正文引用——虽然这是一个 housekeeping 问题，但表明 related work 讨论尚未完成。
- 建议：引用并讨论 Becker-Ehmck et al. (2023) 和 Park et al. (2021)；加深 DreamerV4 讨论；清理 .bib 中未引用的条目。

---

## 小问题（不影响接收）

- **格式问题**：当前使用 `\documentclass[10pt,letterpaper,twocolumn]{article}` 而非 CoRL 2026 要求的 PMLR 模板（`\usepackage[final]{corl_2026}`）。投稿前需切换模板并验证页数。
- **引用格式问题**：.bib 中 `splates2025` 的 author 字段为 "SPlaTES, authors"——这不是合法的 BibTeX author 格式。`nie2025sdar` 和 `kim2025deas` 使用了 "et, al" 而非完整作者列表。
- **Baseline seeds 不完整**：Section 5.3 (line 63) 提到 "a third seed (seed 0) is in progress"——提交时应完成。
- **Treatment 训练步数**：Treatment configurations 仅跑到 105K steps，而 baseline 跑到 505K。Section 5.5 声称 105K "sufficient to observe collapse onset"，但对于 self-correction 的 seed（009b, eval 267.9 at 105K），无法判断是否会在更长训练后进一步恢复或最终也崩溃——这削弱了 "three post-CIVO outcomes" 结论的可靠性。
- **Table 1 中 NVE 的缺失值**：exp_006, 007, 005 的 NVE 标注为 "---"。即使这些 early experiments 没有完整的 NVE 计算，解释原因或补充数据会增强一致性。

---

## 主要优势

1. **清晰的因果 ablation 设计**：trained vs. untrained vs. removed embedding 的三向对比是方法论亮点。008d vs. 008f 的 key control 设计精巧，在其控制的范围内具有说服力。
2. **多路径发现有价值**：Pathway A (CIVO, value-driven) 和 Pathway B (non-CIVO, eval-driven) 的识别是一个 genuine discovery，表明 trained temporal conditioning 的危害超出单一 value overestimation 机制。这一发现对 future work 有实际指导意义。
3. **NVE 指标设计合理**：normalized value-to-eval ratio 作为诊断工具思路清晰，通过 baseline normalization 控制了自然的 v/e 动态。尽管 threshold 选取缺乏 principled justification，指标本身有推广价值。
4. **写作质量**：F1-F6 的组织清晰，每个 finding 有明确的实验证据支撑。Analysis section 的 CIVO 机制四阶段描述和 seed divergence 分析写得好。
5. **诚实的 limitations**：Conclusion 承认单环境和单架构局限，这比许多论文做得好。

---

## Questions for Authors

1. 你们是否在其他 DMC 任务上做过任何初步验证？即使是不完整的数据（如 Cheetah Run 上的 1 seed），也能大幅增强 CIVO 发现的可信度。
2. Pathway B (non-CIVO) 中 entropy 增加而 evaluation 崩溃——你们是否分析过 actor 的 action distribution 在崩溃前后的变化？这对区分 exploration-driven degradation 和 representation corruption 很关键。
3. 你们在 Section 6.4 (dt-Embedding Dilemma) 提到 gradient stopping 作为可能的 mitigation——为什么没有在实验中测试？这只需要修改一行代码，且结果（无论正面或负面）都会显著提升论文贡献。
4. 对于 TAWM 的对比：TD-MPC2 使用 continuous latent states 而 DreamerV3 使用 discrete latent states——你们是否考虑过 latent space 的离散化本身是否放大了 dt-conditioning 的偏差？

---

## 总结

本文提出了一个结构化的诊断框架来分析 DreamerV3 中 temporal abstraction 的失败，CIVO 机制和双路径发现有一定学术价值。但三个核心问题使其不适合 CoRL 主会议：(1) 与 robotics 的关联太弱；(2) 单环境单架构的实验无法支撑泛化性声明；(3) 纯诊断无 solution 的贡献形式难以达到主会议门槛。建议作者增加 robotics-relevant 环境、实现至少一种 mitigation 策略、并更多 seeds 的验证后，考虑投 ICML/NeurIPS 或 CoRL workshop track。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-15T12:36:33.065123+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 和 Reviewer 3 的意见\n\n以下是 Reviewer 2 和 Reviewer 3 的完整审稿意见。请对每条 Must-Fix 和 Should-Fix 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 的审稿意见（侧重：新颖性 & 贡献度 & Venue Fit & Related Work）\n\n**Overall: 4/10 (Reject)**\n\n### Must-Fix:\n- **N1** [critical] Venue Fit 严重不足——CoRL 要求 robot learning 相关性。全文无 robotics 实验/讨论，仅 DMC Walker Walk proprioceptive。\n- **N2** [critical] 单环境实验无法支撑因果 claim 的泛化性。全部 findings F1-F6 仅来自 Walker Walk。\"structural incompatibility\" 结论的泛化性完全未经验证。\n- **N3** [critical] 贡献度不足——纯诊断负面结果缺乏 actionable solution。Section 6.6 的三个 future directions 全部 \"leave to future work\"。\n\n### Should-Fix:\n- **W1** 与 TAWM 的对比仅基于 architectural reasoning，缺乏实证验证（未实际运行 TAWM）。\n- **W2** NVE threshold 1.5× 的选取缺乏 principled justification（post-hoc fitting to 9 configs）。\n- **W3** CIVO 与已知 value overestimation 的区分不够清晰——可能只是 \"compounding model error in MBRL\" 的特定实例化。\n- **W4** Related Work 遗漏：Becker-Ehmck et al. (2023)、Park et al. (2021)、Wang & Beltrame (2024) 在 .bib 中但未引用；DreamerV4 讨论不足；48 个 orphan bib entries。\n\n---\n\n## Reviewer 3 的审稿意见（侧重：格式合规 & 写作质量）\n\n**Overall: 4/10 (Borderline Reject)**\n\n### Must-Fix:\n- **N1** [critical] 未使用 CoRL 2026 官方 PMLR 模板——desk reject 风险。使用 `\\documentclass{article}` + 自定义 geometry。\n- **N2** [critical] CoRL scope 适配性严重不足——无物理机器人实验或讨论。\n- **N3** [critical] 页数合规性无法验证——换到 PMLR 模板后正文极有可能超过 8 页。\n\n### Should-Fix:\n- **W1** Limitations 作为段落嵌入 Conclusion 而非独立 Section。\n- **W2** Abstract 过长且过于技术化，缺乏 robotics motivation。\n- **W3** Bibliography 严重冗余：77 条 bib entry 中仅 29 条被引用，多个占位符 author。\n- **W4** 参考文献格式可能不符合 PMLR 惯例（使用 plainnat）。\n- **W5** fig4_mechanism_diagram.pdf 存在但未被论文引用。\n\n---\n\n请逐条给出你的 [AGREE] 或 [REBUT] 回应。",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 和 Reviewer 3 的意见\n\n以下是 Reviewer 2 和 Reviewer 3 的完整审稿意见。请对每条 Must-Fix 和 Should-Fix 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 的审稿意见（侧重：新颖性 & 贡献度 & Venue Fit & Related Work）\n\n**Overall: 4/10 (Reject)**\n\n### Must-Fix:\n- **N1** [critical] Venue Fit 严重不足——CoRL 要求 robot learning 相关性。全文无 robotics 实验/讨论，仅 DMC Walker Walk proprioceptive。\n- **N2** [critical] 单环境实验无法支撑因果 claim 的泛化性。全部 findings F1-F6 仅来自 Walker Walk。\"structural incompatibility\" 结论的泛化性完全未经验证。\n- **N3** [critical] 贡献度不足——纯诊断负面结果缺乏 actionable solution。Section 6.6 的三个 future directions 全部 \"leave to future work\"。\n\n### Should-Fix:\n- **W1** 与 TAWM 的对比仅基于 architectural reasoning，缺乏实证验证（未实际运行 TAWM）。\n- **W2** NVE threshold 1.5× 的选取缺乏 principled justification（post-hoc fitting to 9 configs）。\n- **W3** CIVO 与已知 value overestimation 的区分不够清晰——可能只是 \"compounding model error in MBRL\" 的特定实例化。\n- **W4** Related Work 遗漏：Becker-Ehmck et al. (2023)、Park et al. (2021)、Wang & Beltrame (2024) 在 .bib 中但未引用；DreamerV4 讨论不足；48 个 orphan bib entries。\n\n---\n\n## Reviewer 3 的审稿意见（侧重：格式合规 & 写作质量）\n\n**Overall: 4/10 (Borderline Reject)**\n\n### Must-Fix:\n- **N1** [critical] 未使用 CoRL 2026 官方 PMLR 模板——desk reject 风险。使用 `\\documentclass{article}` + 自定义 geometry。\n- **N2** [critical] CoRL scope 适配性严重不足——无物理机器人实验或讨论。\n- **N3** [critical] 页数合规性无法验证——换到 PMLR 模板后正文极有可能超过 8 页。\n\n### Should-Fix:\n- **W1** Limitations 作为段落嵌入 Conclusion 而非独立 Section。\n- **W2** Abstract 过长且过于技术化，缺乏 robotics motivation。\n- **W3** Bibliography 严重冗余：77 条 bib entry 中仅 29 条被引用，多个占位符 author。\n- **W4** 参考文献格式可能不符合 PMLR 惯例（使用 plainnat）。\n- **W5** fig4_mechanism_diagram.pdf 存在但未被论文引用。\n\n---\n\n请逐条给出你的 [AGREE] 或 [REBUT] 回应。",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-15T12:36:54.718674+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21653
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-15T12:36:54.819647+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 和 Reviewer 3 的意见\n\n以下是 Reviewer 1 和 Reviewer 3 的完整审稿意见。请对每条 Must-Fix 和 Should-Fix 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n- 特别关注与你自己意见的共识和分歧点\n\n---\n\n## Reviewer 1 的审稿意见（侧重：方法严谨性 & 实验设计）\n\n**Overall: 4/10 (Reject)**\n\n### Must-Fix:\n- **N1** [critical] 统计检验力严重不足。核心 \"causal factor\" 声明依赖 n=2 per group。\"4/4 separating power\" 在随机零假设下 P=1/16≈6.25%，不够显著。Henderson et al. (2018) 和 Colas et al. (2018) 已证明 2-3 seeds 不足以得出可靠结论。Agarwal et al. (2021) 的核心论点是需要更多 seeds + IQM，而非更少 seeds 上报告个体轨迹。\n- **N2** [critical] NVE 阈值 1.5× 为 post-hoc 选择。两组间 [1.2, 2.0] 范围内任何阈值都能达到类似分类效果。\"88.9% accuracy\"是训练准确率，无 held-out 验证。\n- **N3** [critical] CoRL Relevance 严重不足。CoRL 要求论文 \"explicitly address a learning question for physical robots\"。全文无 robotics 实验/讨论。\n- **N4** [critical] 单环境局限使因果声明不可泛化。Walker Walk 是 DMC 最简单任务之一。CIVO 可能高度依赖动力学低维度、dense reward、proprioceptive observation。\n\n### Should-Fix:\n- **W1** Factorial design 存在混淆变量：008d vs 008a 同时改变了三个因素；008d vs 008f 是 trained vs removed（不是 trained vs untrained）。缺少 untrained + Sub ON + H=8 + dt=2 的干净对比。\n- **W2** 105K vs 505K 训练步数不对等——self-correcting seeds 可能在更长训练后恢复。\n- **W3** Pathway B 解释不充分——可能只是普通 training instability 而非 dt-embedding 特有。\n- **W4** RSSM fidelity analysis：MAE 不区分 over- vs under-prediction。需要 signed error 验证方向性。\n- **W5** 格式不符合 CoRL 2026 要求（未使用 PMLR 模板）。\n\n---\n\n## Reviewer 3 的审稿意见（侧重：格式合规 & 写作质量）\n\n**Overall: 4/10 (Borderline Reject)**\n\n### Must-Fix:\n- **N1** [critical] 未使用 CoRL 2026 官方 PMLR 模板——desk reject 风险。\n- **N2** [critical] CoRL scope 适配性严重不足——无物理机器人实验或讨论。CoRL CFP 明确要求 \"Submissions should focus on a core robotics problem\"。\n- **N3** [critical] 页数合规性无法验证——换到 PMLR 模板后正文极有可能超过 8 页。\n\n### Should-Fix:\n- **W1** Limitations 作为段落嵌入 Conclusion 而非独立 Section。\n- **W2** Abstract 过长且过于技术化，缺乏 robotics motivation。\n- **W3** Bibliography 冗余：77 条 bib 中仅 29 条被引用；占位符 author 字段。\n- **W4** 参考文献格式可能不符合 PMLR 惯例。\n- **W5** fig4_mechanism_diagram.pdf 存在但未被引用。\n\n---\n\n请逐条给出你的 [AGREE] 或 [REBUT] 回应，特别注意与你自己意见的共识和分歧。",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 和 Reviewer 3 的意见\n\n以下是 Reviewer 1 和 Reviewer 3 的完整审稿意见。请对每条 Must-Fix 和 Should-Fix 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n- 特别关注与你自己意见的共识和分歧点\n\n---\n\n## Reviewer 1 的审稿意见（侧重：方法严谨性 & 实验设计）\n\n**Overall: 4/10 (Reject)**\n\n### Must-Fix:\n- **N1** [critical] 统计检验力严重不足。核心 \"causal factor\" 声明依赖 n=2 per group。\"4/4 separating power\" 在随机零假设下 P=1/16≈6.25%，不够显著。Henderson et al. (2018) 和 Colas et al. (2018) 已证明 2-3 seeds 不足以得出可靠结论。Agarwal et al. (2021) 的核心论点是需要更多 seeds + IQM，而非更少 seeds 上报告个体轨迹。\n- **N2** [critical] NVE 阈值 1.5× 为 post-hoc 选择。两组间 [1.2, 2.0] 范围内任何阈值都能达到类似分类效果。\"88.9% accuracy\"是训练准确率，无 held-out 验证。\n- **N3** [critical] CoRL Relevance 严重不足。CoRL 要求论文 \"explicitly address a learning question for physical robots\"。全文无 robotics 实验/讨论。\n- **N4** [critical] 单环境局限使因果声明不可泛化。Walker Walk 是 DMC 最简单任务之一。CIVO 可能高度依赖动力学低维度、dense reward、proprioceptive observation。\n\n### Should-Fix:\n- **W1** Factorial design 存在混淆变量：008d vs 008a 同时改变了三个因素；008d vs 008f 是 trained vs removed（不是 trained vs untrained）。缺少 untrained + Sub ON + H=8 + dt=2 的干净对比。\n- **W2** 105K vs 505K 训练步数不对等——self-correcting seeds 可能在更长训练后恢复。\n- **W3** Pathway B 解释不充分——可能只是普通 training instability 而非 dt-embedding 特有。\n- **W4** RSSM fidelity analysis：MAE 不区分 over- vs under-prediction。需要 signed error 验证方向性。\n- **W5** 格式不符合 CoRL 2026 要求（未使用 PMLR 模板）。\n\n---\n\n## Reviewer 3 的审稿意见（侧重：格式合规 & 写作质量）\n\n**Overall: 4/10 (Borderline Reject)**\n\n### Must-Fix:\n- **N1** [critical] 未使用 CoRL 2026 官方 PMLR 模板——desk reject 风险。\n- **N2** [critical] CoRL scope 适配性严重不足——无物理机器人实验或讨论。CoRL CFP 明确要求 \"Submissions should focus on a core robotics problem\"。\n- **N3** [critical] 页数合规性无法验证——换到 PMLR 模板后正文极有可能超过 8 页。\n\n### Should-Fix:\n- **W1** Limitations 作为段落嵌入 Conclusion 而非独立 Section。\n- **W2** Abstract 过长且过于技术化，缺乏 robotics motivation。\n- **W3** Bibliography 冗余：77 条 bib 中仅 29 条被引用；占位符 author 字段。\n- **W4** 参考文献格式可能不符合 PMLR 惯例。\n- **W5** fig4_mechanism_diagram.pdf 存在但未被引用。\n\n---\n\n请逐条给出你的 [AGREE] 或 [REBUT] 回应，特别注意与你自己意见的共识和分歧。",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-15T12:37:05.833077+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 11013
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-15T12:37:06.135248+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "3",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 和 Reviewer 2 的意见\n\n以下是 Reviewer 1 和 Reviewer 2 的完整审稿意见。请对每条 Must-Fix 和 Should-Fix 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n- 特别关注与你自己意见的共识和分歧点\n\n---\n\n## Reviewer 1 的审稿意见（侧重：方法严谨性 & 实验设计）\n\n**Overall: 4/10 (Reject)**\n\n### Must-Fix:\n- **N1** [critical] 统计检验力严重不足。核心 \"causal factor\" 声明依赖 n=2 per group。\"4/4 separating power\" 在随机零假设下 P=1/16≈6.25%，离统计显著性甚远（需考虑多重比较修正）。Agarwal et al. (2021) 的核心论点是需要更多 seeds + IQM。\n- **N2** [critical] NVE 阈值 1.5× 为 post-hoc 选择。\"88.9% accuracy\"是训练准确率，无独立验证。\n- **N3** [critical] CoRL Relevance 严重不足。\n- **N4** [critical] 单环境局限使因果声明不可泛化。\n\n### Should-Fix:\n- **W1** Factorial design 混淆变量：trained vs untrained 对比同时改变 subsampling 和 horizon。\n- **W2** 105K vs 505K 训练步数不对等。\n- **W3** Pathway B 解释不充分——可能只是普通 training instability。\n- **W4** RSSM fidelity analysis：MAE 不区分 over- vs under-prediction，需 signed error。\n- **W5** 格式不符合 CoRL 2026 要求。\n\n---\n\n## Reviewer 2 的审稿意见（侧重：新颖性 & 贡献度 & Venue Fit & Related Work）\n\n**Overall: 4/10 (Reject)**\n\n### Must-Fix:\n- **N1** [critical] Venue Fit 严重不足——CoRL 要求 robot learning 相关性。Introduction 直接从 TAWM 的 RL 结果出发，完全没有 robotics motivation。\n- **N2** [critical] 单环境实验无法支撑因果 claim 的泛化性。Dense reward + low-dim observation 的 Walker Walk 不具代表性。\n- **N3** [critical] 贡献度不足——纯诊断负面结果缺乏 actionable solution。论文的 output 仅是 \"dt-conditioning 在 DreamerV3 中不 work\"。\n\n### Should-Fix:\n- **W1** 与 TAWM 的对比仅基于 architectural reasoning，未实际运行 TAWM 验证。\n- **W2** NVE threshold 1.5× post-hoc fitting，无 cross-validation。\n- **W3** CIVO 与已知 value overestimation 的区分不够清晰——可能只是 compounding model error 的实例化。\n- **W4** Related Work 遗漏：Becker-Ehmck et al. (2023)、Park et al. (2021)、Wang & Beltrame (2024) 在 .bib 中未引用；DreamerV4 讨论不足。\n\n---\n\n请逐条给出你的 [AGREE] 或 [REBUT] 回应，特别关注与你自己审稿意见的共识和分歧。",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "3",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 和 Reviewer 2 的意见\n\n以下是 Reviewer 1 和 Reviewer 2 的完整审稿意见。请对每条 Must-Fix 和 Should-Fix 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n- 特别关注与你自己意见的共识和分歧点\n\n---\n\n## Reviewer 1 的审稿意见（侧重：方法严谨性 & 实验设计）\n\n**Overall: 4/10 (Reject)**\n\n### Must-Fix:\n- **N1** [critical] 统计检验力严重不足。核心 \"causal factor\" 声明依赖 n=2 per group。\"4/4 separating power\" 在随机零假设下 P=1/16≈6.25%，离统计显著性甚远（需考虑多重比较修正）。Agarwal et al. (2021) 的核心论点是需要更多 seeds + IQM。\n- **N2** [critical] NVE 阈值 1.5× 为 post-hoc 选择。\"88.9% accuracy\"是训练准确率，无独立验证。\n- **N3** [critical] CoRL Relevance 严重不足。\n- **N4** [critical] 单环境局限使因果声明不可泛化。\n\n### Should-Fix:\n- **W1** Factorial design 混淆变量：trained vs untrained 对比同时改变 subsampling 和 horizon。\n- **W2** 105K vs 505K 训练步数不对等。\n- **W3** Pathway B 解释不充分——可能只是普通 training instability。\n- **W4** RSSM fidelity analysis：MAE 不区分 over- vs under-prediction，需 signed error。\n- **W5** 格式不符合 CoRL 2026 要求。\n\n---\n\n## Reviewer 2 的审稿意见（侧重：新颖性 & 贡献度 & Venue Fit & Related Work）\n\n**Overall: 4/10 (Reject)**\n\n### Must-Fix:\n- **N1** [critical] Venue Fit 严重不足——CoRL 要求 robot learning 相关性。Introduction 直接从 TAWM 的 RL 结果出发，完全没有 robotics motivation。\n- **N2** [critical] 单环境实验无法支撑因果 claim 的泛化性。Dense reward + low-dim observation 的 Walker Walk 不具代表性。\n- **N3** [critical] 贡献度不足——纯诊断负面结果缺乏 actionable solution。论文的 output 仅是 \"dt-conditioning 在 DreamerV3 中不 work\"。\n\n### Should-Fix:\n- **W1** 与 TAWM 的对比仅基于 architectural reasoning，未实际运行 TAWM 验证。\n- **W2** NVE threshold 1.5× post-hoc fitting，无 cross-validation。\n- **W3** CIVO 与已知 value overestimation 的区分不够清晰——可能只是 compounding model error 的实例化。\n- **W4** Related Work 遗漏：Becker-Ehmck et al. (2023)、Park et al. (2021)、Wang & Beltrame (2024) 在 .bib 中未引用；DreamerV4 讨论不足。\n\n---\n\n请逐条给出你的 [AGREE] 或 [REBUT] 回应，特别关注与你自己审稿意见的共识和分歧。",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-15T12:37:07.601545+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1466
}
```

</details>

---


### Assistant

_source line 80 · 2026-05-15T12:37:12.422995+00:00_

交叉分享已发出，等待三位 Reviewer 的逐条回应。收到后将进行收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 7

## Round 7

2 recorded events


### User

_source line 81 · 2026-05-15T12:37:15.019845+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：**Overall 4/10, Reject**。三个核心问题：

1. **Venue fit 严重不足**——全部实验仅 DMC Walker Walk，无 robotics motivation，不符合 CoRL 对 robot learning 的 scope 要求
2. **单环境 + 2-3 seeds 无法支撑因果泛化 claim**——CIVO 可能是 Walker Walk 特异的现象，论文自身发现 seed 间巨大方差（1/2 seeds collapse）却只用 2 seeds
3. **纯诊断负面结果缺乏 actionable solution**——gradient stopping 作为 mitigation 只需一行代码却未测试，三个 future directions 全部 "leave to future work"

主要优势是清晰的 factorial ablation 设计和 Pathway A/B 双路径发现。建议增加 robotics 环境、实现至少一种 mitigation、增加 seeds 后考虑投 ICML/NeurIPS 或 CoRL workshop。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 82 · 2026-05-15T12:37:20.293598+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 8

## Round 8

2 recorded events


### User

_source line 83 · 2026-05-15T12:38:23.337413+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — 交叉回应 Reviewer 2 & Reviewer 3

---

# 回应 Reviewer 2

## Must-Fix

**[AGREE] R2-N1: Venue Fit 严重不足**
完全同意。这与我的 N3 一致。CoRL 明确要求论文 "explicitly address a learning question for physical robots" 或 "test the proposed learning solution on physical robots"。全文无任何 robotics 实验、robotics benchmark（RoboSuite/ManiSkill/IsaacGym 等）、或对 real-robot deployment 的实质性讨论。Section 6.7 提到 "extending this diagnostic framework to... continuous-control benchmarks" 作为 future work，进一步说明当前版本不满足 CoRL 的 scope 要求。三位 reviewer 在此问题上完全一致，这应当是接收决定的核心考量。

**[AGREE] R2-N2: 单环境无法支撑因果泛化性**
完全同意。这与我的 N4 一致。补充一点定量论据：Walker Walk 是 DMC 中最简单的 locomotion 任务之一（24-dim obs, 6-dim action），其 RSSM 容易达到高 fidelity（baseline reward MAE 仅 0.0102，Table 4）。在更复杂任务中，RSSM 的 baseline reward prediction 本身就更差，trained embedding 带来的 differential gap 可能被整体预测噪声淹没——即 CIVO 的 2.78× reward gap 可能是 Walker Walk 特有的现象。Section 6.7 的 "structural incompatibility" 声明在没有多环境验证的情况下是不负责任的泛化。

**[AGREE with nuance] R2-N3: 贡献度不足——纯诊断负面结果缺乏 actionable solution**
基本同意，但有一定保留。诊断性论文（negative results / diagnostic analysis）在学术上有独立价值——Engstrom et al. (2020) 和 Andrychowicz et al. (2021) 都是纯诊断工作且获高引。问题不在于 "没有 solution" 本身，而在于：(1) 诊断的统计基础不够扎实（2-3 seeds，如我的 N1）；(2) 诊断的泛化范围不够广（单环境）；(3) Section 6.6 提出的三个 future direction（hierarchical abstraction、embedding regularization、transformer extension）都是 one-sentence speculation，未提供任何初步验证。如果诊断本身足够 robust 且 generalizable，缺少 solution 不应成为 reject 的理由；但在当前形态下，诊断的可靠性本身就存疑，叠加缺少 solution 使贡献确实不足。

## Should-Fix

**[AGREE] R2-W1: 与 TAWM 的对比缺乏实证**
同意。Section 6.3 关于 "MPC re-plans from real states" vs "imagination-based bootstrapping" 的分析是合理的架构推理，但未用实验验证。具体来说：(1) 论文未实际运行 TAWM 或 TD-MPC2 + dt-conditioning 来确认它们确实不产生 CIVO；(2) 未验证在 DreamerV3 中添加 "re-plan from real states" 的机制（如缩短 rollout + 更频繁 re-grounding）是否能缓解 CIVO。这两个实验中任一个都会大幅强化论文的核心论点。仅靠 architectural reasoning 无法排除 TAWM 的成功可能源于其他差异（如 planning horizon 长度、采样策略、value function 的不同角色等）。

**[AGREE] R2-W2: NVE threshold 1.5× post-hoc**
完全同意，这与我的 N2 一致。不再赘述。

**[REBUT with partial agreement] R2-W3: CIVO 可能只是 "compounding model error in MBRL" 的实例化**
部分反驳。R2 说得对，CIVO 的上层逻辑（model error → value overestimation → policy exploitation）确实是 MBRL 中已知的 failure mode（MBPO [Janner et al. 2019], MOPO [Yu et al. 2020]）。但论文在 Section 6.1 提供了一个有价值的细化：CIVO 的触发机制是 *learned input feature* (dt-embedding) 与 reward head 的 co-adaptation 导致的 *asymmetric* fidelity（Table 4, 2.78× gap），而非简单的 compounding error 或 rollout 长度问题。untrained embedding 消除 CIVO（Section 5.3）而 compounding error 不会因 embedding 训练方式改变，这一对比提供了超越 "compounding error" 泛化解释的机制特异性。当然，这个 specific mechanism 是否稳健成立仍受限于统计检验力不足（N1），但 R2 将 CIVO 完全等同于已知 failure mode 过于简化。

**[AGREE] R2-W4: Related Work 遗漏 + orphan bib entries**
同意。我验证了 references.bib：`beckerehmck2023multitimestep`（multi-timestep models for MBRL）、`park2021sar`（time discretization-invariant action repetition）、`wang2024seac`（elastic time steps）均在 bib 中但未在正文中引用。这三篇都与 variable temporal resolution in RL 直接相关，遗漏引用是 scholarship 缺陷。此外，`colas2018seeds` 也在 bib 中但未引用，而该文恰好是关于 seed 数量对 deep RL 结论可靠性影响的关键参考——如我在 N1 中指出的。77 条 bib entries 中大量未引用的 orphan entries 反映了论文的粗糙程度。

---

# 回应 Reviewer 3

## Must-Fix

**[AGREE] R3-N1: 未使用 CoRL 2026 官方 PMLR 模板**
完全同意。这与我的 W5 一致。main.tex line 1 使用 `\documentclass[10pt,letterpaper,twocolumn]{article}` + 自定义 `\usepackage[margin=0.75in]{geometry}`（line 12），完全不符合 CoRL 2026 要求的 PMLR 模板。这不仅是格式问题——PMLR 模板的 margin、字号、行距与当前 setup 不同，切换后的页面利用率和排版效果会有显著变化。

**[AGREE] R3-N2: CoRL scope 适配性**
同意，与 R2-N1 和我的 N3 一致。三位 reviewer 共识。

**[AGREE] R3-N3: 换模板后可能超页**
同意这是合理担忧。当前用 0.75in margin + 10pt article class 的双栏排版比 PMLR 模板更紧凑。粗略估计：PMLR corl_2026 模板通常有更宽的 margin 和更大的行距。当前论文 7 个 section + 6 个 figure + 4 个 table 的内容量，切换到 PMLR 后正文很可能超过 8 页。作者需要压缩内容——可能需要删减 Section 6 (Analysis & Discussion) 中的部分展开论述，或将某些 table/figure 移入 appendix。

## Should-Fix

**[REBUT] R3-W1: Limitations 应为独立 Section**
部分反驳。查看 conclusion.tex，Limitations 确实是 `\paragraph{Limitations.}` 嵌入 Conclusion section。但 CoRL 的要求是 "papers must include a limitations section"——这里的 "section" 未必指 LaTeX 的 `\section{}`。查看 CoRL 2023 reviewer guidelines 的原文，是要求 "honestly reported limitations" 并给予正面评价。当前实现是一个清晰标注的段落，内容实质到位（承认了单环境和单架构的局限）。我认为 R3 对此的 severity 有些夸大——这是一个 minor formatting preference，而非 must-fix。不过为保险起见，改为 `\subsection{Limitations}` 或独立 `\section{Limitations}` 确实更安全。

**[AGREE with partial caveat] R3-W2: Abstract 过长且缺乏 robotics motivation**
同意 "缺乏 robotics motivation" 的部分——对 CoRL 投稿，abstract 应在首句建立 robotics 相关性。但 "过长且过于技术化" 我认为对于诊断性论文是可接受的风格选择。Abstract 中的具体数字（2.78×, 4/4, 88.9%）使其 self-contained 且可检索。真正的问题不是技术密度，而是缺少 "这对 robot learning 意味着什么" 的一句话。

**[AGREE] R3-W3: Bibliography 严重冗余**
完全同意。如我在小问题中指出，77 条 bib entries 中大量 orphan（R2-W4 也提到此问题）。`splates2025` 的 author 是 "SPlaTES, authors"（明显的占位符），`nie2025sdar` 使用 "et, al" 代替完整作者列表。这些不仅是冗余问题，更反映了论文准备的粗糙度。

**[AGREE] R3-W4: 参考文献格式可能不符 PMLR**
同意。main.tex line 58 使用 `\bibliographystyle{plainnat}`，而 PMLR 模板通常自带 bibliography style（如 `\bibliographystyle{pmlr-style}` 或 `abbrvnat`）。切换模板后需要同步更换 bibliography style，否则格式不一致。

**[AGREE] R3-W5: fig4_mechanism_diagram.pdf 未被引用**
同意。我检查了全部 .tex 文件：正文引用了 fig1 (learning curves), fig2 (NVE trajectory), fig3 (factorial grid), fig5 (dt amplification), fig6 (multiple pathways)——唯独跳过了 fig4。`\graphicspath` 指向 `../../artifacts/`，如果该目录下确实存在 `figures/paper/fig4_mechanism_diagram.pdf`，这是一个遗漏（mechanism diagram 对于解释 CIVO 的四阶段反馈回路可能很有价值）。如果是 intentionally excluded，至少不应留在目录中。

---

## 综合评估

三位 reviewer 在三个核心问题上达成完全共识：
1. **CoRL venue fit 不足**（R1-N3, R2-N1, R3-N2）
2. **单环境局限**（R1-N4, R2-N2）
3. **格式不合规**（R1-W5, R3-N1）

我与 R2 的主要分歧在 W3：R2 认为 CIVO 完全是已知问题的 repackaging，我认为 trained vs untrained embedding 的对比提供了一定的机制特异性（虽然 statistical power 不足削弱了这一贡献）。

我的独有关注点（未被 R2/R3 充分覆盖）是 **统计检验力**（N1）和 **NVE 阈值的 post-hoc 性质**（N2）——这些是方法严谨性层面的根本问题，即使解决了 venue fit 和格式问题，论文的结论可靠性仍然存疑。

**维持评分: 4/10 (Reject)**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 84 · 2026-05-15T12:38:29.391494+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 9

## Round 9

2 recorded events


### User

_source line 85 · 2026-05-15T12:38:32.023797+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。对 R2 和 R3 的每条 Must-Fix/Should-Fix 逐条给出了 [AGREE] 或 [REBUT]，并标注了与我自己审稿意见的交叉关系。三位 reviewer 在 venue fit、单环境局限、格式合规三个核心问题上完全一致。我与 R2 唯一的实质分歧是 W3（CIVO 的新颖性），我认为 trained vs untrained embedding 对比提供了一定的机制特异性，不应完全归为已知 failure mode 的 repackaging。维持 4/10 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 86 · 2026-05-15T12:38:38.736544+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 10

## Round 10

2 recorded events


### User

_source line 87 · 2026-05-15T12:38:59.041986+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — 交叉回应 R1 & R3

## 回应 Reviewer 1

**[AGREE] R1-N1 (统计检验力)**: 完全同意。与我的 N2 一致。n=2 下 "4/4 separating power" P=1/16≈6.25%，论文引用 Agarwal et al. 来辩护 per-seed 报告，但 Agarwal 的核心论点是 IQM + bootstrap，不是更少 seeds。

**[AGREE] R1-N2 (NVE threshold post-hoc)**: 同意，与我的 W2 一致。该阈值在最关键 case (008e_v3 s1) 上 false negative，却被 "88.9%" 包装为高精度。

**[AGREE] R1-N3 (CoRL relevance)**: 三 reviewer 一致。

**[AGREE] R1-N4 (单环境)**: 同意，与我的 N2 一致。R1 补充的 "Walker Walk 是最简任务之一" 进一步削弱泛化性。

**[AGREE] R1-W1 (Factorial confounds)**: 我审稿时漏掉此点。008d vs 008f 是 trained vs removed（非 untrained），且缺少 untrained+SubON+H=8+dt=2 的干净 cell。

**[AGREE] R1-W2 (训练步数不对等)**: 与我的小问题一致。

**[REBUT] R1-W3 (Pathway B 是普通 instability)**: 部分反驳——baseline seed 2 (009a) 稳定在 836.5 排除了 seed 脆弱性，008e_v3 s2 与 009a 唯一差异是 trained dt-embedding。但仅 1/2 seeds，统计效力确实不足。

**[AGREE] R1-W4 (RSSM signed error)**: 好的技术点，我漏掉了。MAE 无法验证 CIVO 假设的方向性（高估 vs 低估）。

**[AGREE] R1-W5 (格式)**: 三方均提及。

## 回应 Reviewer 3

**[AGREE] R3-N1 (PMLR 模板)**: 同意升级为 critical，desk reject 风险实质存在。

**[AGREE] R3-N2 (CoRL scope)**: 三 reviewer 一致。

**[REBUT] R3-N3 (页数超限)**: 合理担忧但 critical 过重——需要实际测试，可能通过压缩解决，建议降为 should-fix。

**[AGREE] R3-W1 (Limitations 非独立 section)**: 确实只是 Conclusion 中的 \paragraph。

**[AGREE] R3-W2 (Abstract 缺 robotics motivation)**: 完全同意。

**[AGREE] R3-W3 (Bibliography 冗余)**: 我的引用验证确认 77 条中 48 条 orphan。

**[AGREE] R3-W4 (参考文献格式)**: 同意。

**[AGREE] R3-W5 (fig4 未引用)**: 确认 fig4_mechanism_diagram.pdf 在全部 tex 文件中无 \includegraphics 引用。

## 三 Reviewer 共识

三位 reviewer scores (4, 4, 4) 高度一致。核心拒稿共识：(1) CoRL venue fit 严重不足（三方一致）；(2) 单环境 + 低 seeds 无法支撑因果声明（R1+R2 一致）；(3) 格式不合规（三方均提及）。我与 R1 唯一分歧在 Pathway B 的解释——我认为 baseline control 提供了部分证据，但统计效力仍然不足。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 88 · 2026-05-15T12:39:05.843079+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 11

## Round 11

2 recorded events


### User

_source line 89 · 2026-05-15T12:39:08.467709+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。三位 reviewer 评分一致（4/4/4），在 CoRL venue fit、统计效力、单环境局限三个核心问题上形成强共识。我与 R1 唯一分歧在 Pathway B 的解释——我认为 baseline seed 2 的 control 提供了部分因果证据，但同意统计效力不足以做强声明。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 90 · 2026-05-15T12:39:15.471528+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 12

## Round 12

6 recorded events


### User

_source line 91 · 2026-05-15T12:39:36.405146+00:00_

[Reviewer 3 审稿意见]:
## Reviewer 3 — 交叉回应 Reviewer 1 和 Reviewer 2 意见

---

# 回应 Reviewer 1（方法严谨性 & 实验设计）

## Must-Fix

**[AGREE] R1-N1: 统计检验力不足**
同意这是核心方法论缺陷。论文的 "4/4 separating power" 声明（Section 5.2, F2）确实仅基于 n=2 per group（008d/009b vs 008f/009c）。在随机零假设下 P(4/4)=1/16≈6.25%，虽然接近传统 5% 显著性水平但未达到，且未做多重比较修正。论文引用 Agarwal et al. (2021) 作为方法论背书，但该文的核心主张恰恰是需要更多 seeds + IQM 聚合——论文实际做法（2-3 seeds，报告 per-seed trajectory）仅采纳了其部分建议。

补充我的视角：作为格式/写作审查者，我注意到论文在语言上频繁使用因果性措辞（"causal factor", "triggers", "necessary and sufficient"），这些措辞与 n=2 的证据强度不匹配。即使因果方向大致正确，措辞应降级为 "strongly suggests" 或 "consistent with"。

**[AGREE] R1-N2: NVE 阈值 1.5× post-hoc**
同意。Section 4.4 定义 NVE 阈值时（methodology.tex 第 79-80 行）说 "We use nve > 1.5× as a diagnostic threshold"，但未说明该值是 a priori 选定还是 data-driven。从 "achieves 4/4 separating power" 和 "88.9% accuracy" 的表述看，这明显是在全部数据上拟合后报告的 in-sample 准确率。论文缺少任何形式的 cross-validation、sensitivity analysis（如 1.3× 或 1.7× 会怎样？）、或 held-out 验证。这严重削弱了 NVE 作为 "diagnostic marker" 的可信度。

**[AGREE] R1-N3: CoRL Relevance 不足**
与我自己的 N2（critical）完全一致。三位 reviewer 一致认为这是 critical issue，进一步确认了 venue fit 问题的严重性。

**[AGREE] R1-N4: 单环境局限**
同意。Walker Walk 是 DMC 中相对简单的连续控制任务（dense reward、low-dim proprioceptive observation、smooth dynamics）。CIVO 是否在 sparse reward、high-dim observation、contact-rich dynamics 环境中同样出现完全未知。论文 Limitations 段（conclusion.tex 第 16-17 行）虽然承认了这一点，但 "causal factor" 级别的声明需要至少 2-3 个环境才能让 reviewer 信服。

## Should-Fix

**[REBUT] R1-W1: Factorial design 混淆变量**
部分不同意。R1 的担忧对部分比较成立，但**论文的核心因果对照（008d vs 008f）是干净的**。

查看 Table 1（methodology.tex 第 34-59 行）：
- 008d: trained emb, Sub=ON, H=8, dt=2
- 008f: **none** emb, Sub=ON, H=8, dt=2

两者**仅在 embedding 上不同**，其余三个因素完全一致。论文在 Section 3.3 明确说明："comparing 008d (trained embedding) against 008f (no embedding) with all other factors held constant isolates whether training the temporal conditioning triggers pathological dynamics."

R1 的混淆变量担忧适用于 008a（utr, OFF, 15）和 008c（utr, OFF, 8）与 008d 的比较——这些比较确实同时改变了 embedding、subsampling 和 horizon。但论文并未将这些作为主要因果证据，而是作为辅助对照（Section 5.5, F5："horizon length and temporal subsampling affect learning speed [but] neither is sufficient to trigger collapse"）。

建议论文更明确地区分 primary causal comparison（008d vs 008f，干净）和 secondary comparisons（有混淆但用于排除辅助因素），以避免 R1 的误读。

**[AGREE] R1-W2: 105K vs 505K 不对等**
同意这存在解释性局限。虽然 105K 足以观察 collapse onset，但对于 self-correction 的 seed（如 009b 在 105K 时 eval=267.9、nve=0.38×），我们无法知道它是否最终能恢复到 baseline 水平。Section 5.2 将 seed 2 标记为 "self-correction"，但 267.9 vs baseline 的 915.7 仍然只有 29%——这可能只是 "slower collapse" 而非真正的 self-correction。延长 treatment runs 至少到 200-300K 步才能区分这两种可能性。

**[AGREE] R1-W3: Pathway B 解释不充分**
同意。Pathway B（008e_v3 seed 2）的证据仅来自**单个 seed**（analysis.tex 第 42-43 行）。论文用 baseline seed 2（009a）的稳定性排除 "inherent seed fragility"，但这不足以排除所有混淆因素。Pathway B 的特征（entropy increase, eval-driven collapse）与普通 training instability（如 plasticity loss、capacity collapse 等已知现象）的区分不够清晰。论文需要更强的证据或更谨慎的措辞来支撑 "qualitatively distinct pathway" 的声明。

**[AGREE] R1-W4: RSSM fidelity 需 signed error**
同意这是技术审查的合理要求。Table 4（results.tex 第 196-212 行）报告 reward MAE，但 CIVO 机制依赖于 **systematic overprediction**（而非双向误差）。MAE=0.1579 at dt=2 可能是均匀分布的 over/under prediction，也可能是单向 overprediction——两者对 CIVO 机制的支持力度完全不同。补充 signed error（mean error 而非 MAE）是验证 CIVO 因果链条的关键一步。

**[AGREE] R1-W5: 格式不符合 CoRL 2026**
与我自己的 N1（critical）完全一致。

---

# 回应 Reviewer 2（新颖性 & 贡献度 & Venue Fit）

## Must-Fix

**[AGREE] R2-N1: Venue Fit 不足**
与我的 N2 和 R1-N3 一致。三位 reviewer 形成共识：论文的 Introduction（introduction.tex）直接从 "TAWM shows that conditioning a world model on step size dt yields consistent gains within TD-MPC2's MPC framework" 出发，完全没有 robotics motivation 或 robot learning 的 framing。这对 CoRL 来说是根本性问题。

**[AGREE] R2-N2: 单环境 + dense reward 不具代表性**
同意，且 R2 补充的 "dense reward + low-dim observation" 视角比 R1-N4 更精确。Dense reward 环境中 critic 获得频繁的真实信号，value overestimation 的影响可能与 sparse reward 环境截然不同。在 sparse reward 下，critic 更依赖 imagination 中的 bootstrapped values，CIVO 可能更严重——但也可能不会出现（因为 reward head 本身就难以学好）。这两种可能性都未被讨论。

**[REBUT] R2-N3: 贡献度不足——纯诊断负面结果缺乏 actionable solution**
部分不同意。R2 将论文定性为 "output 仅是 dt-conditioning 在 DreamerV3 中不 work"，我认为这低估了论文的实际贡献。

论文的核心输出不仅是负面结果，还包括：
1. **NVE 诊断框架**（Section 4.4）：提供了可复用的 value overestimation 检测指标，虽然阈值需要 cross-validation
2. **CIVO 机制分析**（Section 6.1）：不只是说 "不 work"，而是通过 RSSM fidelity analysis（Table 4）定位到 reward head co-adaptation 这一具体机制
3. **MPC vs imagination 架构对比**（Section 6.3）：识别出 feedback architecture 作为结构性因素，这对后续研究设计有直接指导意义
4. **Multiple pathways 发现**（Section 6.5）：表明问题比 "fix the critic" 更深层

这些发现对 MBRL 社区有 diagnostic value，类似于 Henderson et al. (2018) "Deep RL that Matters" 和 Engstrom et al. (2020) "Implementation Matters" 的贡献模式。

**但我同意**，对于 CoRL 这个特定 venue，纯诊断论文确实贡献度偏低——CoRL 更偏好有实际解决方案或系统实现的工作。如果投 ICML/NeurIPS，贡献度的评价可能不同。

## Should-Fix

**[AGREE] R2-W1: 未实际运行 TAWM 验证**
同意。Section 6.3（analysis.tex 第 24-28 行）对 MPC 免疫性的解释完全基于 architectural reasoning（"re-plans from real states at every step, so model errors do not accumulate into the critic"）。这是合理的假说，但未经验证。一个可能的反驳是 TAWM 使用了不同的 world model architecture（不是 RSSM），所以直接复现不等价。但至少应该 (a) 在 TD-MPC2 框架下复现 dt-conditioning 的增益以确认 baseline，或 (b) 引用 TAWM 的具体数据来支撑论点。

**[AGREE] R2-W2: NVE threshold post-hoc**
与 R1-N2 一致。两位 reviewer 独立指出同一问题，进一步确认了这是论文的关键方法论弱点。

**[REBUT] R2-W3: CIVO 可能只是 compounding model error 的实例化**
部分不同意。R2 的观点是 CIVO 可能只是已知 compounding model error 的一个具体 case。这在高层面上成立，但论文通过 trained vs untrained embedding 的对照（Section 5.2-5.3）提供了超越 generic compounding error 的特异性证据：

- 如果 CIVO 仅是 compounding error 的实例化，那么 untrained embedding + dt=2 imagination（008a, 008c）也应该出现类似 value overestimation——因为 dt=2 本身就会增加 compounding error。但实际上 008a（nve=0.59×）和 008c（nve=0.58×）均未出现 overestimation。
- 关键区别在于 **learned co-adaptation**：trained embedding 使 reward head 对不同 dt 产生 asymmetric prediction quality（Table 4, 2.78× reward gap），这不是 generic compounding error 会产生的模式。

然而，我同意论文应该更系统地区分 CIVO 和 generic compounding model error——例如通过控制实验：在 untrained embedding 下也测量 RSSM fidelity gap，以展示 trained embedding 特有的 asymmetric co-adaptation。实际上 Table 4 已经包含了 008f（no emb）的数据（reward gap 1.01×），但论文没有将此显式框架为 "CIVO vs generic compounding error" 的对照论证。

**[AGREE] R2-W4: Related Work 遗漏**
同意。我在引用验证中也发现：`beckerehmck2023multitimestep`、`park2021sar`、`wang2024seac` 均存在于 .bib 但未在正文中引用。这三篇分别涉及 multi-timestep models、time discretization-invariant action repetition、elastic time steps——都与本文主题高度相关。

关于 DreamerV4：R2 说 "讨论不足"，但我查证 analysis.tex 第 52 行确实有一段讨论（"DreamerV4 replaces the RSSM with a transformer architecture, raising the question of whether CIVO transfers..."），篇幅约 4 行。这段讨论的深度对于一篇非 DreamerV4 的论文来说是合理的，但可以增加对 transformer 架构下 CIVO 是否会出现的更具体分析。

---

# 三位 Reviewer 的共识总结

| 问题 | R1 | R2 | R3 (我) | 共识 |
|------|----|----|---------|------|
| 模板不合规 | W5 | — | N1 (critical) | 2/3 提到，desk reject 级 |
| CoRL scope/relevance | N3 | N1 | N2 (critical) | **3/3 一致**，最强共识 |
| 单环境局限 | N4 | N2 | 未单独列出但认同 | **3/3 一致** |
| 统计检验力不足 | N1 | — | 交叉回应中同意 | 2/3 |
| NVE 阈值 post-hoc | N2 | W2 | 交叉回应中同意 | **3/3 一致** |
| 贡献度/解决方案缺失 | — | N3 | 部分同意 | 2/3 |

**最终判断**：三位 reviewer 在 CoRL scope、单环境局限、NVE post-hoc 三个问题上形成完全共识。这些问题叠加在一起，使得论文在 CoRL 2026 的接收前景非常不乐观。建议作者认真考虑 (1) 增加 robot-relevant 环境、(2) 增加 seeds、(3) 对 NVE 做 cross-validation，然后转投 ICML/NeurIPS。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_3"
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-15T12:40:51.345139+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"统计检验力严重不足：2-3 seeds 无法支撑 causal factor 声明，4/4 separating power 在 n=2 下 P≈6.25%\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 均认同统计效力不足。R2 在交叉回应中 AGREE，R3 在交叉回应中 AGREE 并补充语言措辞问题\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2\"\n    summary: \"NVE 阈值 1.5× 为 post-hoc 选择，88.9% accuracy 是训练准确率，无独立验证或 cross-validation\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 一致认为 post-hoc。R2-W2 独立提出同一问题。R3 交叉回应中 AGREE\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3\"\n    summary: \"CoRL venue fit 严重不足：全文无 robotics 实验/讨论，不满足 CoRL 对 robot learning 的 scope 要求\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 最强共识。R1-N3, R2-N1, R3-N2 均独立列为 critical\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N4\"\n    summary: \"单环境（Walker Walk）局限使因果声明不可泛化，CIVO 可能是 task-specific artifact\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 一致。R2 补充 dense reward + low-dim observation 不具代表性\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N1\"\n    summary: \"未使用 CoRL 2026 官方 PMLR 模板，使用自定义 article class，desk reject 风险\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"R3 列为 N1 critical，R1 列为 W5。R2 在小问题中提及\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"纯诊断负面结果缺乏 actionable solution，三个 future directions 全部 leave to future work\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 列为 N3 critical。R1 交叉回应 AGREE with nuance（诊断有独立价值但当前统计基础不够）。R3 交叉回应 partial REBUT（论文有 NVE 框架等贡献）\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"Factorial design 存在混淆变量：trained vs untrained 对比（008d vs 008a/008c）同时改变 subsampling 和 horizon\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R1 提出。R2 交叉回应 AGREE。R3 交叉回应 REBUT——指出 008d vs 008f 是干净对照，混淆仅存在于 secondary comparisons\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"105K vs 505K 训练步数不对等，self-correcting seeds 长期命运未知\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 均同意。R3 补充 009b 的 267.9 仅为 baseline 29%，可能是 slower collapse 而非 self-correction\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"Pathway B (non-CIVO collapse) 解释不充分，可能只是普通 training instability\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R1 提出。R2 partial REBUT（baseline control 提供部分证据）。R3 AGREE\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"RSSM fidelity analysis 仅报告 MAE，无法验证 reward overprediction 的方向性假设\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"R1 提出，R2 交叉回应 AGREE，R3 交叉回应 AGREE\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1\"\n    summary: \"与 TAWM 的对比仅基于 architectural reasoning，未实际运行 TAWM 实证验证\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 提出，R1 和 R3 交叉回应均 AGREE\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"CIVO 与已知 value overestimation (MBPO/MOPO/delusional bias) 的区分不够清晰\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 提出。R1 和 R3 均 partial REBUT——认为 trained vs untrained embedding 对比提供了机制特异性，但同意论文应更清晰地阐述区分\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W4\"\n    summary: \"Related Work 遗漏多篇相关工作（Becker-Ehmck 2023, Park 2021, Wang 2024 在 bib 中未引用）；DreamerV4 讨论不足\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 提出。R1 和 R3 交叉回应均 AGREE。R1 补充 colas2018seeds 也未引用\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W1\"\n    summary: \"Limitations 作为 paragraph 嵌入 Conclusion 而非独立 Section\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"R3 提出。R1 交叉回应 REBUT（内容实质到位，paragraph 可接受）。R2 AGREE\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W2\"\n    summary: \"Abstract 过长且缺乏 robotics motivation，对 CoRL 受众不够友好\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"R3 提出。R1 交叉回应 partial AGREE（同意缺 robotics motivation，但技术密度可接受）。R2 AGREE\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W3\"\n    summary: \"Bibliography 严重冗余：77 条 bib entry 中仅 29 条被引用，多个占位符 author 字段\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 均提及。splates2025 author 为占位符，多个条目 author 不完整\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W5\"\n    summary: \"fig4_mechanism_diagram.pdf 存在于目录但未被论文引用\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"R3 提出，R1 交叉回应 AGREE。CIVO 机制图可能对理解 Section 6.1 有帮助\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N3\"\n    summary: \"换到 PMLR 模板后正文极可能超过 8 页限制\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"R3 列为 critical，R2 交叉回应 REBUT 降为 should-fix（需实际测试，可能通过压缩解决）\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"统计检验力严重不足：2-3 seeds 无法支撑 causal factor 声明，4/4 separating power 在 n=2 下 P≈6.25%\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 均认同统计效力不足。R2 在交叉回应中 AGREE，R3 在交叉回应中 AGREE 并补充语言措辞问题\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2\"\n    summary: \"NVE 阈值 1.5× 为 post-hoc 选择，88.9% accuracy 是训练准确率，无独立验证或 cross-validation\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 一致认为 post-hoc。R2-W2 独立提出同一问题。R3 交叉回应中 AGREE\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3\"\n    summary: \"CoRL venue fit 严重不足：全文无 robotics 实验/讨论，不满足 CoRL 对 robot learning 的 scope 要求\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 最强共识。R1-N3, R2-N1, R3-N2 均独立列为 critical\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N4\"\n    summary: \"单环境（Walker Walk）局限使因果声明不可泛化，CIVO 可能是 task-specific artifact\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 一致。R2 补充 dense reward + low-dim observation 不具代表性\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N1\"\n    summary: \"未使用 CoRL 2026 官方 PMLR 模板，使用自定义 article class，desk reject 风险\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"R3 列为 N1 critical，R1 列为 W5。R2 在小问题中提及\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"纯诊断负面结果缺乏 actionable solution，三个 future directions 全部 leave to future work\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 列为 N3 critical。R1 交叉回应 AGREE with nuance（诊断有独立价值但当前统计基础不够）。R3 交叉回应 partial REBUT（论文有 NVE 框架等贡献）\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"Factorial design 存在混淆变量：trained vs untrained 对比（008d vs 008a/008c）同时改变 subsampling 和 horizon\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R1 提出。R2 交叉回应 AGREE。R3 交叉回应 REBUT——指出 008d vs 008f 是干净对照，混淆仅存在于 secondary comparisons\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"105K vs 505K 训练步数不对等，self-correcting seeds 长期命运未知\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 均同意。R3 补充 009b 的 267.9 仅为 baseline 29%，可能是 slower collapse 而非 self-correction\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"Pathway B (non-CIVO collapse) 解释不充分，可能只是普通 training instability\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R1 提出。R2 partial REBUT（baseline control 提供部分证据）。R3 AGREE\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"RSSM fidelity analysis 仅报告 MAE，无法验证 reward overprediction 的方向性假设\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"R1 提出，R2 交叉回应 AGREE，R3 交叉回应 AGREE\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1\"\n    summary: \"与 TAWM 的对比仅基于 architectural reasoning，未实际运行 TAWM 实证验证\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 提出，R1 和 R3 交叉回应均 AGREE\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"CIVO 与已知 value overestimation (MBPO/MOPO/delusional bias) 的区分不够清晰\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 提出。R1 和 R3 均 partial REBUT——认为 trained vs untrained embedding 对比提供了机制特异性，但同意论文应更清晰地阐述区分\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W4\"\n    summary: \"Related Work 遗漏多篇相关工作（Becker-Ehmck 2023, Park 2021, Wang 2024 在 bib 中未引用）；DreamerV4 讨论不足\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 提出。R1 和 R3 交叉回应均 AGREE。R1 补充 colas2018seeds 也未引用\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W1\"\n    summary: \"Limitations 作为 paragraph 嵌入 Conclusion 而非独立 Section\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"R3 提出。R1 交叉回应 REBUT（内容实质到位，paragraph 可接受）。R2 AGREE\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W2\"\n    summary: \"Abstract 过长且缺乏 robotics motivation，对 CoRL 受众不够友好\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"R3 提出。R1 交叉回应 partial AGREE（同意缺 robotics motivation，但技术密度可接受）。R2 AGREE\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W3\"\n    summary: \"Bibliography 严重冗余：77 条 bib entry 中仅 29 条被引用，多个占位符 author 字段\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 均提及。splates2025 author 为占位符，多个条目 author 不完整\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W5\"\n    summary: \"fig4_mechanism_diagram.pdf 存在于目录但未被论文引用\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"R3 提出，R1 交叉回应 AGREE。CIVO 机制图可能对理解 Section 6.1 有帮助\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N3\"\n    summary: \"换到 PMLR 模板后正文极可能超过 8 页限制\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"R3 列为 critical，R2 交叉回应 REBUT 降为 should-fix（需实际测试，可能通过压缩解决）\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-15T12:40:51.447030+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml\", \"bytes\": 7351}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-15T12:43:17.703213+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "report": "# 审稿报告 — Round 1\n\n**论文**: \"Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**目标 Venue**: CoRL 2026 Main Conference\n**审稿日期**: 2026-05-15\n**Reviewer 编排**: 3 人（R1: 方法严谨性 & 实验设计 | R2: 新颖性 & 贡献度 & Venue Fit | R3: 格式合规 & 写作质量）\n**轮次**: Round 1 初审 + 交叉分享（1 轮收敛）\n\n---\n\n## Summary\n\n本文通过 factorial ablation 分析 DreamerV3 中 variable-rate imagination 的失败原因。在 Walker Walk (DMC) 上测试 9 组配置（2-3 seeds each），识别出 trained dt-embedding 导致 RSSM reward head 产生 2.78× 跨时间尺度预测偏差，critic 通过 imagination bootstrapping 将其内化为系统性高估——称为 conditioning-induced value overestimation (CIVO)。论文进一步发现同一 trigger 产生三种随机下游结果（full collapse / self-correction / oscillatory degradation），且限制 imagination 到 dt=1 不能完全防止崩溃（存在 non-CIVO Pathway B）。与 TAWM (MPC-based) 的对比将 feedback architecture 定位为关键结构差异。\n\n---\n\n## Strengths\n\n1. **清晰的问题定义和切入点**：将 \"为什么 dt-conditioning 在 MPC 中成功但在 imagination-based AC 中失败\" 作为核心问题，切入角度明确且有实际意义（3/3 reviewer 认可）\n2. **结构化的 factorial 设计**：trained vs untrained vs removed embedding 的三向对比是方法论亮点，核心对照 008d vs 008f 在控制变量上是干净的（R3 在交叉回应中澄清）\n3. **CIVO 机制描述细致**：四阶段反馈回路描述清晰，三种 post-CIVO 结果的刻画有信息量\n4. **Multiple pathways 发现 (F6)**：Pathway A (value-driven) 和 Pathway B (eval-driven) 的识别是 genuine discovery，表明问题比单一 value overestimation 更深层（3/3 认可为论文最有价值的 insight）\n5. **写作质量高**：F1-F6 因果链式叙述清晰，Figure/Table 信息密度高，术语定义到位（Clarity 获三位 reviewer 最高分 4/5 或 7/10）\n6. **诚实的 Limitations**：承认单环境和单架构局限，F6 的 partial falsification 展示良好科学态度\n\n---\n\n## Weaknesses（按严重性排序）\n\n### Critical（影响接收决定）\n\n**W-C1. CoRL Venue Fit 严重不足 [3/3 reviewer 共识，最强共识]**\n全文仅在 DMC Walker Walk（proprioceptive observations）上做实验，无任何 robotics benchmark（RoboSuite/ManiSkill/IsaacGym）、无 real-robot 实验、无 robotics application 讨论。Introduction 直接从 TAWM 的 RL 结果出发，完全没有 robotics motivation。CoRL CFP 明确要求 \"Submissions should focus on a core robotics problem\"——当前论文不满足这一硬约束，存在 desk reject 风险。\n\n**W-C2. 统计检验力严重不足 [3/3 reviewer 共识]**\n核心因果声明 \"trained dt-embedding is the causal factor\" 依赖 n=2 per group 的 factorial 比较。\"4/4 separating power\" 在随机零假设下 P=1/16≈6.25%，未达 p<0.05 且未做多重比较修正。论文引用 Agarwal et al. (2021) 辩护 per-seed reporting，但该文的核心论点恰恰是需要更多 seeds + IQM 等稳健统计量。语言中频繁使用 \"causal factor\"、\"triggers\"、\"necessary and sufficient\" 等因果措辞，与 n=2 的证据强度严重不匹配。\n\n**W-C3. 单环境（Walker Walk）局限使因果声明不可泛化 [3/3 reviewer 共识]**\nWalker Walk 是 DMC 中最简单的 locomotion 任务之一（24-dim obs, 6-dim action, dense reward）。CIVO 的 2.78× reward gap 可能高度依赖：(a) 低维动力学的高 RSSM fidelity（baseline reward MAE 仅 0.0102）；(b) dense reward 下 critic 获得频繁真实信号；(c) proprioceptive observations 无 representation bottleneck。在 sparse reward、高维视觉、contact-rich dynamics 环境下，CIVO 可能表现完全不同或不出现。Section 6.6 的 \"structural incompatibility\" 声明在没有多环境验证下是过度泛化。\n\n**W-C4. NVE 阈值 1.5× 为 post-hoc 选择 [3/3 reviewer 共识]**\n1.5× 阈值未说明选择依据（pre-registered vs data-driven）。数据显示 [1.2, 2.0] 范围内任何阈值均可达到类似分类效果，强烈暗示 post-hoc 选择。\"88.9% accuracy\" 是在训练集上的准确率，无 held-out 验证、cross-validation 或 sensitivity analysis。将 post-hoc 指标阈值包装为 \"separating power\" 可能误导后续研究者。\n\n**W-C5. 未使用 CoRL 2026 官方 PMLR 模板 [2/3 reviewer 列为 critical]**\n论文使用 `\\documentclass[10pt,letterpaper,twocolumn]{article}` + 自定义 geometry（0.75in margins），完全不符合 CoRL 2026 要求的 PMLR 模板（`\\usepackage[final]{corl_2026}`）。这构成 desk reject 的独立理由。换模板后正文极可能超过 8 页限制。\n\n### Warning（影响评分但不一票否决）\n\n**W-W1. 纯诊断负面结果缺乏 actionable solution [2/3 reviewer 共识，1/3 partial disagreement]**\n论文 Section 6.6 提出三个 future directions（hierarchical abstraction、embedding regularization、transformer extension），全部 \"leave to future work\"。Gradient stopping 作为 mitigation 仅需一行代码改动却未测试。R3 部分反驳：论文有 NVE 框架、CIVO 机制分析、MPC vs imagination 架构对比等诊断贡献，类似 Henderson et al. (2018) 的模式。但三位 reviewer 均同意：对 CoRL 这个偏重实际 solution 的 venue，纯诊断贡献度偏低。\n\n**W-W2. 与 TAWM 的对比缺乏实证 [3/3 reviewer 共识]**\nSection 6.3 关于 MPC 免疫性的解释完全基于 architectural reasoning，未实际运行 TAWM/TD-MPC2 验证。TD-MPC2 与 DreamerV3 的多重差异（连续 vs 离散 latent、training objective 等）可能 confound 对比。\n\n**W-W3. 105K vs 505K 训练步数不对等 [3/3 reviewer 共识]**\nBaseline 运行 505K 展示完整收敛，treatment 仅 105K。Self-correcting seed 009b（eval 267.9@105K = baseline 的 29%）可能只是 slower collapse 而非真正的 self-correction。Oscillatory seed 009e 的长期命运未知。\n\n**W-W4. Pathway B 解释不充分 [2/3 AGREE, 1/3 partial REBUT]**\n008e_v3 seed 2 的 non-CIVO collapse 仅有 1 个 seed 的证据。论文用 baseline seed 2 (009a) 的稳定性排除 seed fragility（R2 认为此 control 有一定价值），但未排除 subsampling data augmentation 等引入的普通 training instability。Pathway B 的特征（entropy increase, eval-driven）与已知 plasticity loss / capacity collapse 的区分不够清晰。\n\n**W-W5. RSSM fidelity 仅报告 MAE，未验证 overprediction 方向性 [3/3 AGREE]**\nTable 4 的 reward MAE 不区分 over- vs under-prediction。CIVO 机制假设 reward head \"systematically overpredicts rewards at dt=2\"，但 MAE=0.1579 可能是双向误差。需 signed error 验证方向性。\n\n**W-W6. CIVO 与已知 value overestimation 的区分不够清晰 [R2 提出，R1/R3 partial REBUT]**\nR2 认为 CIVO 可能只是 compounding model error 的实例化。R1 和 R3 均 partial REBUT：trained vs untrained embedding 对比（008a/008c nve<0.6× vs 008d nve=4.12×）提供了超越 generic compounding error 的机制特异性——如果仅是 compounding error，untrained embedding + dt=2 也应出现 overestimation。但论文应更系统地阐述这一区分。\n\n**W-W7. Factorial design 部分对比存在混淆 [R1 提出，R3 partial REBUT]**\n008d vs 008a/008c 的比较同时改变了 embedding、subsampling、horizon 三个因素。R3 澄清：核心对照 008d vs 008f 是干净的（仅 embedding 不同），混淆仅存在于 secondary comparisons。但论文未清晰区分 primary vs secondary comparisons，容易导致误读。\n\n**W-W8. Related Work 遗漏 + Bibliography 冗余 [3/3 reviewer 共识]**\nBecker-Ehmck et al. (2023)、Park et al. (2021)、Wang & Beltrame (2024)、Colas et al. (2018) 均在 .bib 中但未在正文引用，且与论文主题高度相关。77 条 bib entries 中 48 条 orphan，多个占位符 author 字段（splates2025 等）。\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | R3 | 共识度 |\n|------|----|----|-----|--------|\n| CoRL venue fit 不足 | N3 critical | N1 critical | N2 critical | **3/3 一致** |\n| 统计检验力不足 | N1 critical | 交叉 AGREE | 交叉 AGREE | **3/3 一致** |\n| 单环境不可泛化 | N4 critical | N2 critical | 交叉 AGREE | **3/3 一致** |\n| NVE 阈值 post-hoc | N2 critical | W2 warning | 交叉 AGREE | **3/3 一致** |\n| 模板不合规 | W5 warning | 小问题 | N1 critical | 3/3 提及 |\n| 缺乏 actionable solution | 交叉 nuance | N3 critical | 交叉 partial REBUT | 2/3 |\n\n---\n\n## Reviewer Divergence\n\n**1. Factorial design 混淆变量（R1-W1）**\n- R1/R2: AGREE——缺少干净的 trained vs untrained 对比\n- R3: REBUT——核心对照 008d vs 008f 是干净的（仅 embedding 不同），混淆仅在 secondary comparisons\n- **Director 判断**：R3 的 REBUT 有理据（Table 1 确认 008d/008f 仅 embedding 不同），但论文确实缺少 untrained+SubON+H=8 的配置来完成完整 factorial grid\n\n**2. CIVO 新颖性（R2-W3）**\n- R2: CIVO 可能只是 compounding model error 的实例化\n- R1/R3: partial REBUT——trained vs untrained 对比提供了机制特异性，untrained embedding 不触发 overestimation 说明不是 generic compounding error\n- **Director 判断**：R1/R3 的 REBUT 在技术上合理——CIVO 的 specific trigger（learned co-adaptation between embedding and reward head）超越了 generic compounding error 的解释。但这一区分在论文中应更显式地阐述\n\n**3. Pathway B 解释（R1-W3）**\n- R1/R3: Pathway B 可能是普通 training instability\n- R2: partial REBUT——baseline seed 2 (009a) 的稳定性提供了部分因果证据\n- **Director 判断**：baseline control 有一定说服力，但仅 1 个 seed 的证据确实不足以做 \"qualitatively distinct pathway\" 的强声明\n\n---\n\n## Questions for Authors\n\n1. 是否在其他 DMC 任务上做过任何初步验证？即使不完整的数据也能大幅增强 CIVO 发现的可信度。\n2. Gradient stopping（阻止 dt-embedding 梯度流向 reward head）作为 mitigation 只需一行代码——为什么未测试？\n3. Table 4 的 reward MAE 能否补充 signed error（mean error），验证 dt=2 是否为系统性正向偏差？\n4. TAWM 原文中 Walker Walk 的具体数据是什么？能否直接引用来支撑 MPC vs imagination 的对比论点？\n5. NVE 阈值 1.5× 在 1.3× 或 2.0× 下的分类结果如何变化？是否做过 sensitivity analysis？\n6. 008e_v3 seed 2 (Pathway B) 的 actor action distribution 在崩溃前后是否有分析？这对区分 exploration-driven degradation 和 representation corruption 很关键。\n\n---\n\n## Missing References\n\n以下工作存在于 .bib 中但未在正文引用，且与论文主题高度相关：\n- **Becker-Ehmck et al. (2023)** \"Multi-timestep models for Model-based RL\" — 直接研究 multi-timestep world model 在 MBRL 中的效果\n- **Park et al. (2021)** \"Time Discretization-Invariant Safe Action Repetition\" — time-discretization 对 RL 的影响\n- **Wang & Beltrame (2024)** \"Reinforcement Learning with Elastic Time Steps\" — elastic time steps in RL\n- **Colas et al. (2018)** — seed 数量对 deep RL 结论可靠性的影响，与 N1 直接相关\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目中未找到 `external_review.paperreview_ai.enabled: true`）。\n\n---\n\n## Overall Assessment\n\n**评分: Strong Reject (4/10)**\n**置信度: High (4/5)**\n\n三位 Reviewer 评分完全一致（4/4/4），在以下核心问题上形成强共识：\n\n1. **CoRL venue fit**（3/3 critical）：论文不满足 CoRL 对 robot learning 的 scope 要求，存在 desk reject 风险\n2. **统计基础**（3/3 一致）：2-3 seeds 无法支撑因果声明，NVE 阈值 post-hoc\n3. **单环境泛化性**（3/3 一致）：Walker Walk 一个环境的诊断无法支撑 \"structural incompatibility\" 级别的结论\n4. **格式合规**（3/3 提及）：未使用 PMLR 模板，独立的 desk reject 理由\n\n论文的 factorial 设计思路和 CIVO 机制描述有价值，但在当前形态下存在多个根本性缺陷。\n\n**建议**：\n1. **Venue 选择**：论文更适合 ICML/NeurIPS/ICLR 的 RL track 或 RLC，而非 CoRL。如坚持投 CoRL，需大幅增加 robotics motivation 和 robot-relevant 实验。\n2. **实验扩展**：至少增加 2-3 个不同复杂度的环境（如 Cheetah Run, Humanoid Walk, 或 manipulation task），每配置 5+ seeds。\n3. **方法论修正**：(a) 将因果语言弱化为 \"strongly associated\" 或 \"candidate mechanism\"；(b) 对 NVE 阈值做 sensitivity analysis 或跨环境验证；(c) 补充 reward signed error 验证 CIVO 方向性假设。\n4. **增加 actionable 贡献**：实现并测试至少一种 mitigation（如 gradient stopping dt-embedding 对 reward head 的梯度）。\n5. **格式修正**：切换到目标 venue 官方模板，清理 bibliography。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 过长且过于技术化（~180 词含大量具体数字）\n- 缺乏 robotics motivation（对 CoRL 是硬伤）\n- \"88.9% accuracy\" 放在 abstract 有误导性（post-hoc in-sample accuracy）\n\n### Introduction (Section 1)\n- 问题定义清晰，从 TAWM 的 MPC 成功切入有效\n- 但完全没有 robotics framing——需要首段建立 temporal abstraction 对 robot learning 的重要性\n- \"causal factor\" 措辞过强\n\n### Related Work (Section 2)\n- 覆盖面合理但有遗漏（Becker-Ehmck 2023, Park 2021, Wang 2024, Colas 2018 在 bib 中未引用）\n- DreamerV4 讨论移至 Analysis 而非 Related Work 是合理选择\n- CIVO 与已知 value overestimation 的区分需更清晰阐述\n\n### Methodology (Section 3)\n- Factorial design 结构良好，Table 1 信息清晰\n- 核心对照 008d vs 008f 干净（R3 交叉确认），但 secondary comparisons 有混淆\n- \"2--3 seeds\" 应直接讨论统计效力局限而非仅在 Limitations 中提及\n- NVE 阈值选取过程需透明化\n\n### Results (Section 5)\n- F1-F6 的因果链组织出色\n- Table 2 和 per-seed trajectory 报告方式专业\n- 但 exp_006/007/005 的 NVE 标注为 \"---\" 未解释原因\n- \"self-correction\" 的标签对 009b（eval 267.9 = baseline 29%）可能过于乐观\n\n### Analysis & Discussion (Section 6)\n- CIVO 四阶段机制描述（6.1）清晰有说服力\n- Seed divergence 讨论（6.2）引用 Lyle et al. 的 capacity loss 假说有价值\n- MPC immune 分析（6.3）合理但缺乏实证\n- dt-Embedding Dilemma（6.4）包装过度——在单环境 + 低 seeds 下，\"dilemma\" 可能只是 artifact\n- Multiple Pathways（6.5）是论文最有价值的 section，但 Pathway B 仅 1 seed 证据\n\n### Conclusion (Section 7)\n- Limitations paragraph 内容实质到位，但形式上应提升为独立 section/subsection\n- Future directions 过于 speculative，缺乏初步验证\n- Baseline seed 0 \"in progress\" 不应出现在提交版本中\n",
  "reviewer_ids_acknowledged": "[1, 2, 3]",
  "cross_response_reviewer_ids": "[1, 2, 3]",
  "overall_score": "strong reject",
  "review_chat_id": "oc_dd4a07a509df7e5f9a31d65f776059bc"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "report": "# 审稿报告 — Round 1\n\n**论文**: \"Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**目标 Venue**: CoRL 2026 Main Conference\n**审稿日期**: 2026-05-15\n**Reviewer 编排**: 3 人（R1: 方法严谨性 & 实验设计 | R2: 新颖性 & 贡献度 & Venue Fit | R3: 格式合规 & 写作质量）\n**轮次**: Round 1 初审 + 交叉分享（1 轮收敛）\n\n---\n\n## Summary\n\n本文通过 factorial ablation 分析 DreamerV3 中 variable-rate imagination 的失败原因。在 Walker Walk (DMC) 上测试 9 组配置（2-3 seeds each），识别出 trained dt-embedding 导致 RSSM reward head 产生 2.78× 跨时间尺度预测偏差，critic 通过 imagination bootstrapping 将其内化为系统性高估——称为 conditioning-induced value overestimation (CIVO)。论文进一步发现同一 trigger 产生三种随机下游结果（full collapse / self-correction / oscillatory degradation），且限制 imagination 到 dt=1 不能完全防止崩溃（存在 non-CIVO Pathway B）。与 TAWM (MPC-based) 的对比将 feedback architecture 定位为关键结构差异。\n\n---\n\n## Strengths\n\n1. **清晰的问题定义和切入点**：将 \"为什么 dt-conditioning 在 MPC 中成功但在 imagination-based AC 中失败\" 作为核心问题，切入角度明确且有实际意义（3/3 reviewer 认可）\n2. **结构化的 factorial 设计**：trained vs untrained vs removed embedding 的三向对比是方法论亮点，核心对照 008d vs 008f 在控制变量上是干净的（R3 在交叉回应中澄清）\n3. **CIVO 机制描述细致**：四阶段反馈回路描述清晰，三种 post-CIVO 结果的刻画有信息量\n4. **Multiple pathways 发现 (F6)**：Pathway A (value-driven) 和 Pathway B (eval-driven) 的识别是 genuine discovery，表明问题比单一 value overestimation 更深层（3/3 认可为论文最有价值的 insight）\n5. **写作质量高**：F1-F6 因果链式叙述清晰，Figure/Table 信息密度高，术语定义到位（Clarity 获三位 reviewer 最高分 4/5 或 7/10）\n6. **诚实的 Limitations**：承认单环境和单架构局限，F6 的 partial falsification 展示良好科学态度\n\n---\n\n## Weaknesses（按严重性排序）\n\n### Critical（影响接收决定）\n\n**W-C1. CoRL Venue Fit 严重不足 [3/3 reviewer 共识，最强共识]**\n全文仅在 DMC Walker Walk（proprioceptive observations）上做实验，无任何 robotics benchmark（RoboSuite/ManiSkill/IsaacGym）、无 real-robot 实验、无 robotics application 讨论。Introduction 直接从 TAWM 的 RL 结果出发，完全没有 robotics motivation。CoRL CFP 明确要求 \"Submissions should focus on a core robotics problem\"——当前论文不满足这一硬约束，存在 desk reject 风险。\n\n**W-C2. 统计检验力严重不足 [3/3 reviewer 共识]**\n核心因果声明 \"trained dt-embedding is the causal factor\" 依赖 n=2 per group 的 factorial 比较。\"4/4 separating power\" 在随机零假设下 P=1/16≈6.25%，未达 p<0.05 且未做多重比较修正。论文引用 Agarwal et al. (2021) 辩护 per-seed reporting，但该文的核心论点恰恰是需要更多 seeds + IQM 等稳健统计量。语言中频繁使用 \"causal factor\"、\"triggers\"、\"necessary and sufficient\" 等因果措辞，与 n=2 的证据强度严重不匹配。\n\n**W-C3. 单环境（Walker Walk）局限使因果声明不可泛化 [3/3 reviewer 共识]**\nWalker Walk 是 DMC 中最简单的 locomotion 任务之一（24-dim obs, 6-dim action, dense reward）。CIVO 的 2.78× reward gap 可能高度依赖：(a) 低维动力学的高 RSSM fidelity（baseline reward MAE 仅 0.0102）；(b) dense reward 下 critic 获得频繁真实信号；(c) proprioceptive observations 无 representation bottleneck。在 sparse reward、高维视觉、contact-rich dynamics 环境下，CIVO 可能表现完全不同或不出现。Section 6.6 的 \"structural incompatibility\" 声明在没有多环境验证下是过度泛化。\n\n**W-C4. NVE 阈值 1.5× 为 post-hoc 选择 [3/3 reviewer 共识]**\n1.5× 阈值未说明选择依据（pre-registered vs data-driven）。数据显示 [1.2, 2.0] 范围内任何阈值均可达到类似分类效果，强烈暗示 post-hoc 选择。\"88.9% accuracy\" 是在训练集上的准确率，无 held-out 验证、cross-validation 或 sensitivity analysis。将 post-hoc 指标阈值包装为 \"separating power\" 可能误导后续研究者。\n\n**W-C5. 未使用 CoRL 2026 官方 PMLR 模板 [2/3 reviewer 列为 critical]**\n论文使用 `\\documentclass[10pt,letterpaper,twocolumn]{article}` + 自定义 geometry（0.75in margins），完全不符合 CoRL 2026 要求的 PMLR 模板（`\\usepackage[final]{corl_2026}`）。这构成 desk reject 的独立理由。换模板后正文极可能超过 8 页限制。\n\n### Warning（影响评分但不一票否决）\n\n**W-W1. 纯诊断负面结果缺乏 actionable solution [2/3 reviewer 共识，1/3 partial disagreement]**\n论文 Section 6.6 提出三个 future directions（hierarchical abstraction、embedding regularization、transformer extension），全部 \"leave to future work\"。Gradient stopping 作为 mitigation 仅需一行代码改动却未测试。R3 部分反驳：论文有 NVE 框架、CIVO 机制分析、MPC vs imagination 架构对比等诊断贡献，类似 Henderson et al. (2018) 的模式。但三位 reviewer 均同意：对 CoRL 这个偏重实际 solution 的 venue，纯诊断贡献度偏低。\n\n**W-W2. 与 TAWM 的对比缺乏实证 [3/3 reviewer 共识]**\nSection 6.3 关于 MPC 免疫性的解释完全基于 architectural reasoning，未实际运行 TAWM/TD-MPC2 验证。TD-MPC2 与 DreamerV3 的多重差异（连续 vs 离散 latent、training objective 等）可能 confound 对比。\n\n**W-W3. 105K vs 505K 训练步数不对等 [3/3 reviewer 共识]**\nBaseline 运行 505K 展示完整收敛，treatment 仅 105K。Self-correcting seed 009b（eval 267.9@105K = baseline 的 29%）可能只是 slower collapse 而非真正的 self-correction。Oscillatory seed 009e 的长期命运未知。\n\n**W-W4. Pathway B 解释不充分 [2/3 AGREE, 1/3 partial REBUT]**\n008e_v3 seed 2 的 non-CIVO collapse 仅有 1 个 seed 的证据。论文用 baseline seed 2 (009a) 的稳定性排除 seed fragility（R2 认为此 control 有一定价值），但未排除 subsampling data augmentation 等引入的普通 training instability。Pathway B 的特征（entropy increase, eval-driven）与已知 plasticity loss / capacity collapse 的区分不够清晰。\n\n**W-W5. RSSM fidelity 仅报告 MAE，未验证 overprediction 方向性 [3/3 AGREE]**\nTable 4 的 reward MAE 不区分 over- vs under-prediction。CIVO 机制假设 reward head \"systematically overpredicts rewards at dt=2\"，但 MAE=0.1579 可能是双向误差。需 signed error 验证方向性。\n\n**W-W6. CIVO 与已知 value overestimation 的区分不够清晰 [R2 提出，R1/R3 partial REBUT]**\nR2 认为 CIVO 可能只是 compounding model error 的实例化。R1 和 R3 均 partial REBUT：trained vs untrained embedding 对比（008a/008c nve<0.6× vs 008d nve=4.12×）提供了超越 generic compounding error 的机制特异性——如果仅是 compounding error，untrained embedding + dt=2 也应出现 overestimation。但论文应更系统地阐述这一区分。\n\n**W-W7. Factorial design 部分对比存在混淆 [R1 提出，R3 partial REBUT]**\n008d vs 008a/008c 的比较同时改变了 embedding、subsampling、horizon 三个因素。R3 澄清：核心对照 008d vs 008f 是干净的（仅 embedding 不同），混淆仅存在于 secondary comparisons。但论文未清晰区分 primary vs secondary comparisons，容易导致误读。\n\n**W-W8. Related Work 遗漏 + Bibliography 冗余 [3/3 reviewer 共识]**\nBecker-Ehmck et al. (2023)、Park et al. (2021)、Wang & Beltrame (2024)、Colas et al. (2018) 均在 .bib 中但未在正文引用，且与论文主题高度相关。77 条 bib entries 中 48 条 orphan，多个占位符 author 字段（splates2025 等）。\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | R3 | 共识度 |\n|------|----|----|-----|--------|\n| CoRL venue fit 不足 | N3 critical | N1 critical | N2 critical | **3/3 一致** |\n| 统计检验力不足 | N1 critical | 交叉 AGREE | 交叉 AGREE | **3/3 一致** |\n| 单环境不可泛化 | N4 critical | N2 critical | 交叉 AGREE | **3/3 一致** |\n| NVE 阈值 post-hoc | N2 critical | W2 warning | 交叉 AGREE | **3/3 一致** |\n| 模板不合规 | W5 warning | 小问题 | N1 critical | 3/3 提及 |\n| 缺乏 actionable solution | 交叉 nuance | N3 critical | 交叉 partial REBUT | 2/3 |\n\n---\n\n## Reviewer Divergence\n\n**1. Factorial design 混淆变量（R1-W1）**\n- R1/R2: AGREE——缺少干净的 trained vs untrained 对比\n- R3: REBUT——核心对照 008d vs 008f 是干净的（仅 embedding 不同），混淆仅在 secondary comparisons\n- **Director 判断**：R3 的 REBUT 有理据（Table 1 确认 008d/008f 仅 embedding 不同），但论文确实缺少 untrained+SubON+H=8 的配置来完成完整 factorial grid\n\n**2. CIVO 新颖性（R2-W3）**\n- R2: CIVO 可能只是 compounding model error 的实例化\n- R1/R3: partial REBUT——trained vs untrained 对比提供了机制特异性，untrained embedding 不触发 overestimation 说明不是 generic compounding error\n- **Director 判断**：R1/R3 的 REBUT 在技术上合理——CIVO 的 specific trigger（learned co-adaptation between embedding and reward head）超越了 generic compounding error 的解释。但这一区分在论文中应更显式地阐述\n\n**3. Pathway B 解释（R1-W3）**\n- R1/R3: Pathway B 可能是普通 training instability\n- R2: partial REBUT——baseline seed 2 (009a) 的稳定性提供了部分因果证据\n- **Director 判断**：baseline control 有一定说服力，但仅 1 个 seed 的证据确实不足以做 \"qualitatively distinct pathway\" 的强声明\n\n---\n\n## Questions for Authors\n\n1. 是否在其他 DMC 任务上做过任何初步验证？即使不完整的数据也能大幅增强 CIVO 发现的可信度。\n2. Gradient stopping（阻止 dt-embedding 梯度流向 reward head）作为 mitigation 只需一行代码——为什么未测试？\n3. Table 4 的 reward MAE 能否补充 signed error（mean error），验证 dt=2 是否为系统性正向偏差？\n4. TAWM 原文中 Walker Walk 的具体数据是什么？能否直接引用来支撑 MPC vs imagination 的对比论点？\n5. NVE 阈值 1.5× 在 1.3× 或 2.0× 下的分类结果如何变化？是否做过 sensitivity analysis？\n6. 008e_v3 seed 2 (Pathway B) 的 actor action distribution 在崩溃前后是否有分析？这对区分 exploration-driven degradation 和 representation corruption 很关键。\n\n---\n\n## Missing References\n\n以下工作存在于 .bib 中但未在正文引用，且与论文主题高度相关：\n- **Becker-Ehmck et al. (2023)** \"Multi-timestep models for Model-based RL\" — 直接研究 multi-timestep world model 在 MBRL 中的效果\n- **Park et al. (2021)** \"Time Discretization-Invariant Safe Action Repetition\" — time-discretization 对 RL 的影响\n- **Wang & Beltrame (2024)** \"Reinforcement Learning with Elastic Time Steps\" — elastic time steps in RL\n- **Colas et al. (2018)** — seed 数量对 deep RL 结论可靠性的影响，与 N1 直接相关\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目中未找到 `external_review.paperreview_ai.enabled: true`）。\n\n---\n\n## Overall Assessment\n\n**评分: Strong Reject (4/10)**\n**置信度: High (4/5)**\n\n三位 Reviewer 评分完全一致（4/4/4），在以下核心问题上形成强共识：\n\n1. **CoRL venue fit**（3/3 critical）：论文不满足 CoRL 对 robot learning 的 scope 要求，存在 desk reject 风险\n2. **统计基础**（3/3 一致）：2-3 seeds 无法支撑因果声明，NVE 阈值 post-hoc\n3. **单环境泛化性**（3/3 一致）：Walker Walk 一个环境的诊断无法支撑 \"structural incompatibility\" 级别的结论\n4. **格式合规**（3/3 提及）：未使用 PMLR 模板，独立的 desk reject 理由\n\n论文的 factorial 设计思路和 CIVO 机制描述有价值，但在当前形态下存在多个根本性缺陷。\n\n**建议**：\n1. **Venue 选择**：论文更适合 ICML/NeurIPS/ICLR 的 RL track 或 RLC，而非 CoRL。如坚持投 CoRL，需大幅增加 robotics motivation 和 robot-relevant 实验。\n2. **实验扩展**：至少增加 2-3 个不同复杂度的环境（如 Cheetah Run, Humanoid Walk, 或 manipulation task），每配置 5+ seeds。\n3. **方法论修正**：(a) 将因果语言弱化为 \"strongly associated\" 或 \"candidate mechanism\"；(b) 对 NVE 阈值做 sensitivity analysis 或跨环境验证；(c) 补充 reward signed error 验证 CIVO 方向性假设。\n4. **增加 actionable 贡献**：实现并测试至少一种 mitigation（如 gradient stopping dt-embedding 对 reward head 的梯度）。\n5. **格式修正**：切换到目标 venue 官方模板，清理 bibliography。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 过长且过于技术化（~180 词含大量具体数字）\n- 缺乏 robotics motivation（对 CoRL 是硬伤）\n- \"88.9% accuracy\" 放在 abstract 有误导性（post-hoc in-sample accuracy）\n\n### Introduction (Section 1)\n- 问题定义清晰，从 TAWM 的 MPC 成功切入有效\n- 但完全没有 robotics framing——需要首段建立 temporal abstraction 对 robot learning 的重要性\n- \"causal factor\" 措辞过强\n\n### Related Work (Section 2)\n- 覆盖面合理但有遗漏（Becker-Ehmck 2023, Park 2021, Wang 2024, Colas 2018 在 bib 中未引用）\n- DreamerV4 讨论移至 Analysis 而非 Related Work 是合理选择\n- CIVO 与已知 value overestimation 的区分需更清晰阐述\n\n### Methodology (Section 3)\n- Factorial design 结构良好，Table 1 信息清晰\n- 核心对照 008d vs 008f 干净（R3 交叉确认），但 secondary comparisons 有混淆\n- \"2--3 seeds\" 应直接讨论统计效力局限而非仅在 Limitations 中提及\n- NVE 阈值选取过程需透明化\n\n### Results (Section 5)\n- F1-F6 的因果链组织出色\n- Table 2 和 per-seed trajectory 报告方式专业\n- 但 exp_006/007/005 的 NVE 标注为 \"---\" 未解释原因\n- \"self-correction\" 的标签对 009b（eval 267.9 = baseline 29%）可能过于乐观\n\n### Analysis & Discussion (Section 6)\n- CIVO 四阶段机制描述（6.1）清晰有说服力\n- Seed divergence 讨论（6.2）引用 Lyle et al. 的 capacity loss 假说有价值\n- MPC immune 分析（6.3）合理但缺乏实证\n- dt-Embedding Dilemma（6.4）包装过度——在单环境 + 低 seeds 下，\"dilemma\" 可能只是 artifact\n- Multiple Pathways（6.5）是论文最有价值的 section，但 Pathway B 仅 1 seed 证据\n\n### Conclusion (Section 7)\n- Limitations paragraph 内容实质到位，但形式上应提升为独立 section/subsection\n- Future directions 过于 speculative，缺乏初步验证\n- Baseline seed 0 \"in progress\" 不应出现在提交版本中\n",
    "reviewer_ids_acknowledged": "[1, 2, 3]",
    "cross_response_reviewer_ids": "[1, 2, 3]",
    "overall_score": "strong reject",
    "review_chat_id": "oc_dd4a07a509df7e5f9a31d65f776059bc"
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-15T12:43:22.429024+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5e879064da2e47dad864c1f891eb37a8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4725
}
```

</details>

---


### Assistant

_source line 96 · 2026-05-15T12:43:33.588394+00:00_

审稿报告已投递至 Research Director。

**Round 1 审稿完成。** 最终结论：

- **评分**: Strong Reject (4/10)，三位 Reviewer 一致
- **核心拒稿理由**：CoRL venue fit 不满足（3/3）、统计检验力不足（3/3）、单环境不可泛化（3/3）、模板不合规（3/3）
- **论文优势**：factorial 设计思路好、CIVO 机制描述清晰、Pathway A/B 双路径发现有价值、写作质量高
- **建议**：转投 ICML/NeurIPS/ICLR 等 general ML venue，增加环境和 seeds，实现至少一种 mitigation，弱化因果语言

Issue Tracker 已同步更新至 `artifacts/review_issues.yaml`（18 条 issue）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 13

## Round 13

2 recorded events


### User

_source line 97 · 2026-05-15T12:43:36.303293+00:00_

[Reviewer 3 审稿结果]:
交叉回应已提交。核心判断：

- R1 的 5 条 Must-Fix 全部同意，W1（factorial confound）部分反驳——论文的核心对照 008d vs 008f 实际上是干净的，但 secondary comparisons 确实有混淆
- R2 的 N1/N2 同意，**N3（贡献度不足）部分反驳**——论文的诊断框架（NVE、RSSM fidelity、multiple pathways）超越了简单的 negative result，但对 CoRL 确实偏弱
- R2-W3（CIVO vs generic compounding error）部分反驳——trained vs untrained 对照提供了特异性证据，Table 4 的 reward gap 1.01× vs 2.78× 是关键区分
- **三位 reviewer 在 CoRL scope、单环境、NVE post-hoc 上形成完全共识**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_3"
}
```

</details>

---


### Assistant

_source line 98 · 2026-05-15T12:43:50.079893+00:00_

审稿流程已完成。

**最终结果**：

- **评分**：Strong Reject (4/10)，三位 Reviewer 一致
- **审稿报告**已通过 `submit_review_report_to_research_director` 投递给 Research Director
- **Issue Tracker** 已同步更新至 `artifacts/review_issues.yaml`（18 条 issue，6 critical / 10 warning / 2 info）

**核心拒稿共识**（3/3 一致）：
1. CoRL venue fit 不满足——无 robotics 实验/讨论
2. 单环境 + 2-3 seeds 统计基础无法支撑因果声明
3. NVE 阈值 post-hoc，无独立验证
4. 模板不合规，desk reject 风险

**唯一实质性分歧**：R2 认为 CIVO 仅是已知 compounding error 的 repackaging，R1/R3 认为 trained vs untrained 对比提供了超越 generic failure mode 的机制特异性。Director 判断 R1/R3 的 REBUT 在技术上合理，但论文应更显式地阐述区分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 14

## Round 14

74 recorded events


### User

_source line 99 · 2026-05-18T02:07:17.585808+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: event-gated-adaptive-horizon
- 论文路径: projects/event-gated-adaptive-horizon/docs/paper/main.tex
- 目标 venue: CoRL 2026
- 截止日期: 2026-05-29

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-18T02:07:23.867330+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-18T02:07:23.918739+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-18T02:07:29.150654+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file",
  "max_results": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file",
    "max_results": "8"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-18T02:07:29.201548+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-18T02:07:33.988843+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-18T02:07:34.543301+00:00_

{"result":"# 项目 event-gated-adaptive-horizon 概况\n\n## 实验状态 (61 个)\n\n- **exp_009a_baseline_walker_s2**: DONE (success) — \n- **exp_008e_v3_walker_s2**: DONE (negative) — \n- **exp_008e_v3_walker_s1**: DONE (success) — \n- **exp_006**: DONE (killed) — \n- **exp_008a**: DONE (killed) — \n- **exp_008c**: DONE (killed) — \n- **exp_008d**: DONE (killed) — \n- **exp_008e_v2_subsample_on_dt1_h15**: DONE (killed) — \n- **exp_rssm_fidelity_analysis**: DONE (success) — \n- **exp_008e_v3_subsample_on_dt1_h15**: DONE (success) — \n- **exp_009c_008f_walker_s2**: DONE (negative) — \n- **exp_006_fixed_dt2**: DONE (negative) — \n- **exp_008e_subsample_on_fixed_dt1**: DONE (killed) — \n- **exp_008e_subsample_on_dt1_h15**: DONE (killed) — \n- **exp_002_event_gated**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_010b_cheetah_civo_trigger_s0 | Cheetah Run CIVO trigger seed=0: trained dt_emb + subsample ON + H=8. 第二 seed 复现 Cheetah CIVO (NVE>1.5×)，加强跨环境因果论证统计力度。Rebuttal 储备。 | — | — | — |\n| exp_008d_civo_trigger_s4 | Walker Walk CIVO trigger seed=4: trained dt_emb + subsample ON + H=8. 第四 seed 复现 CIVO (NVE>1.5×)，加强 Walker 因果论证的统计力度。Rebuttal 储备。 | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp_024b_cheetah_no_dt_emb_s0** (success): Cheetah Run no-dt-emb causal control: dt_embed_dim=0 + subsample ON + H=8. 预期无CIVO（健康基线水平），证明trained dt_emb是Cheetah CIVO的必要条件。对应Walker的008f逻辑，完成Cheetah因果三角。 ← 基于 exp_010b_cheetah_civo_trigger\n  [cheetah_integration_template](/api/workspace-files/projects/event-gated-adaptive-horizon/artifacts/exp_024b_cheetah_no_dt_emb_s0/intermediate/cheetah_integration_template.md)\n- **exp_024b_cheetah_no_dt_emb_s1** (success): Cheetah Run no-dt-emb causal control seed=1: gate_dt_embed_dim=0 + subsample ON + H=8. 第二 seed 验证 024 的结论（trained dt_emb 是 Cheetah CIVO 必要条件），加强因果三角的统计力度。 ← 基于 exp_024_cheetah_no_dt_emb_s0\n- **exp_024_cheetah_n
…[truncated 1429 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-18T02:07:34.645240+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "literature_map.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "file": "literature_map.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-18T02:07:34.697633+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml\", \"content\": \"# Literature Map — event-gated-adaptive-horizon\\n# Last updated: 2026-05-16\\n# Total: 90 papers (76 existing + 14 related-work expansion 2026-05-16)\\n\\n# ============================================================\\n# EXISTING CITATIONS (already in paper.tex)\\n# ============================================================\\n\\n- paper_id: sutton1999options\\n  title: \\\"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\\\"\\n  authors: [Sutton R.S., Precup D., Singh S.]\\n  year: 1999\\n  venue: \\\"Artificial Intelligence 112(1-2):181-211\\\"\\n  category: background\\n  role: \\\"Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL\\\"\\n  relevance_score: 5\\n\\n- paper_id: hafner2020dreamerv1\\n  title: \\\"Dream to Control: Learning Behaviors by Latent Imagination\\\"\\n  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]\\n  year: 2020\\n  venue: ICLR\\n  category: background\\n  role: \\\"DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm\\\"\\n  relevance_score: 5\\n\\n- paper_id: hafner2023dreamerv3\\n  title: \\\"Mastering Diverse Domains through World Models\\\"\\n  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]\\n  year: 2023\\n  venue: \\\"arXiv:2301.04104 (Nature 2025)\\\"\\n  category: background\\n  role: \\\"DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here\\\"\\n  relevance_score: 5\\n\\n- paper_id: sharma2017figar\\n  title: \\\"Fine Grained Action Repetition for Deep Reinforcement Learning\\\"\\n  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]\\n  year: 2017\\n  venue: \\\"ICLR Workshop
…[truncated 11187 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-18T02:07:44.128431+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-18T02:07:44.580924+00:00_

1	\documentclass{article}
2	
3	% Load xcolor before corl_2026 (which loads color internally)
4	\usepackage[table]{xcolor}
5	\usepackage{corl_2026}
6	
7	\usepackage[utf8]{inputenc}
8	\usepackage[T1]{fontenc}
9	\usepackage{amsmath,amssymb}
10	\usepackage{booktabs}
11	\usepackage{multirow}
12	\usepackage{graphicx}
13	\graphicspath{{../../artifacts/}}
14	\usepackage{colortbl}
15	\usepackage{caption}
16	\usepackage{subcaption}
17	\usepackage{array}
18	\usepackage{enumitem}
19	\usepackage{wrapfig}
20	\usepackage{algorithm}
21	\usepackage{algorithmic}
22	
23	% Custom commands
24	\newcommand{\dt}{\mathrm{dt}}
25	\newcommand{\nve}{\mathrm{nve}}
26	% SGS result values (018 seed 1 only; seed 2 collapsed — 50% prevention rate)
27	\newcommand{\sgseval}{448.3}
28	\newcommand{\sgsnve}{1.66}
29	\newcommand{\sgsclaim}{enabled recovery in one of two seeds}
30	\newcommand{\ie}{\textit{i.e.}}
31	\newcommand{\eg}{\textit{e.g.}}
32	\newcommand{\cf}{\textit{cf.}}
33	\newcommand{\etal}{\textit{et al.}}
34	
35	\title{Why Temporal Abstraction Fails in Imagination-Based RL:\\
36	A Diagnostic Analysis of Variable-Rate DreamerV3}
37	
38	\author{
39	  Anonymous Authors
40	}
41	
42	\begin{document}
43	\maketitle
44	
45	\begin{abstract}
46	\input{sections/abstract_body}
47	\end{abstract}
48	
49	\keywords{World Models, Temporal Abstraction, Value Overestimation, DreamerV3}
50	
51	% --- INTRODUCTION ---
52	\input{sections/introduction}
53	
54	% --- RELATED WORK ---
55	\input{sections/related_work}
56	
57	% --- METHODOLOGY ---
58	\input{sections/methodology}
59	
60	% --- RESULTS ---
61	\input{sections/results}
62	
63	% --- ANALYSIS ---
64	\input{sections/analysis}
65	
66	% --- CONCLUSION ---
67	\input{sections/conclusion}
68	
69	% no \bibliographystyle needed — corl_2026.sty sets it automatically
70	\bibliography{references}
71	
72	% --- APPENDIX ---
73	\appendix
74	\input{sections/appendix}
75	
76	\end{document}
77	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-18T02:07:45.085590+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
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

_source line 111 · 2026-05-18T02:07:45.086139+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-18T02:07:45.695276+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-18T02:07:45.797088+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'event-gated-adaptive-horizon'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-18T02:07:50.637035+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 115 · 2026-05-18T02:07:53.857413+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_reports/ 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml 2>/dev/null; echo \"---\"; cat /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/agent/config.yaml 2>/dev/null | grep -A 10 \"external_review\"",
  "description": "Check existing review reports, issues tracker, and external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_reports/ 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml 2>/dev/null; echo \"---\"; cat /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/agent/config.yaml 2>/dev/null | grep -A 10 \"external_review\"",
    "description": "Check existing review reports, issues tracker, and external review config"
  }
}
```

</details>

---


### Tool result

_source line 116 · 2026-05-18T02:07:54.109614+00:00_

round_1.md
---
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "elapsed_ms": 252
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-18T02:07:59.292001+00:00_

Web search results for query: "CoRL 2026 call for papers submission guidelines author instructions"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Instruction for Presentations","url":"https://www.corl.org/contributions/instruction-for-presentations"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"ICML 2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"}]

Based on the search results, here are the key submission guidelines and author instructions for CoRL 2026:

## Paper Format

The camera-ready paper should follow the template: 8-page main text + acknowledgment + references + appendix (optional).

## Reviewer Requirement

Every author with 3 or more submissions must agree to serve as a reviewer. Submissions that do not meet this reciprocal review requirement may be desk-rejected.

## Rebuttal Process

Papers that receive all reviews in the "reject" range in the initial round will not proceed to the rebuttal phase. Authors of all other papers are invited to submit a 1-page rebuttal in pdf by the rebuttal deadline.

## Content Requirements

Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, data
…[truncated 1106 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "WebSearch",
  "elapsed_ms": 8654
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-18T02:08:30.182874+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 instruction for authors page limit template double blind anonymous",
  "allowed_domains": "['corl.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 instruction for authors page limit template double blind anonymous",
    "allowed_domains": "['corl.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 119 · 2026-05-18T02:08:30.233539+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 120 · 2026-05-18T02:08:30.233942+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 121 · 2026-05-18T02:08:30.284674+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 122 · 2026-05-18T02:08:30.335938+00:00_

1	issues:
2	  - id: "R1-N1"
3	    summary: "统计检验力严重不足：2-3 seeds 无法支撑 causal factor 声明，4/4 separating power 在 n=2 下 P≈6.25%"
4	    category: experiment
5	    severity: critical
6	    status: in_progress
7	    first_raised_round: 1
8	    last_seen_round: 1
9	    mentions:
10	      - round: 1
11	        reviewers: [1, 2, 3]
12	        note: "三位 reviewer 均认同统计效力不足"
13	    action_items:
14	      - round: 1
15	        action: "补 seeds: plan_010 (baseline s0 running), plan_011 (008d s1-s2), plan_012 (008f s3), plan_014 (008e_v3 s1-s2)"
16	        assigned_to: agent
17	        status: in_progress
18	      - round: 1
19	        action: "弱化因果语言: causal factor → strongly associated factor; necessary and sufficient → reliable predictor"
20	        assigned_to: paper_agent
21	        status: pending
22	      - round: 1
23	        action: "统计报告改用 IQM + bootstrap CI per Agarwal et al. 2021"
24	        assigned_to: paper_agent
25	        status: pending
26	    resolution: ""
27	    resolution_round: null
28	
29	  - id: "R1-N2"
30	    summary: "NVE 阈值 1.5× 为 post-hoc 选择，88.9% accuracy 是训练准确率，无独立验证"
31	    category: method
32	    severity: critical
33	    status: in_progress
34	    first_raised_round: 1
35	    last_seen_round: 1
36	    mentions:
37	      - round: 1
38	        reviewers: [1, 2, 3]
39	        note: "三位 reviewer 一致认为 post-hoc"
40	    action_items:
41	      - round: 1
42	        action: "plan_034 NVE sensitivity analysis (1.3x/1.5x/1.7x/2.0x + AUROC), 0 GPU"
43	        assigned_to: agent
44	        status: in_progress
45	      - round: 1
46	        action: "跨环境验证 (Cheetah 数据到后)"
47	        assigned_to: agent
48	        status: pending
49	      - round: 1
50	        action: "改措辞: separating power → diagnostic threshold; 标注 in-sample post-hoc"
51	        assigned_to: paper_agent
52	        status: pending
53	    resolution: ""
54	    resolution_round: null
55	
56	  - id: "R1-N3"
57	    summary: "CoRL venue fit 严重不足：全文无 robotics 实验/讨论"
58	    category: framing
59	    severi
…[truncated 11288 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-18T02:08:36.663893+00:00_

Web search results for query: "CoRL 2026 instruction for authors page limit template double blind anonymous"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2024 - Instruction for Authors","url":"https://2024.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Instruction for Presentations","url":"https://www.corl.org/contributions/instruction-for-presentations"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"FORMATTING INSTRUCTIONS FOR ICLR 2026 ...","url":"https://openreview.net/pdf?id=qioDi3afqm"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2021 - Submission Instructions","url":"https://2021.corl.org/author-information/submission-instructions"},{"title":"CoRL 2026 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2026"}]

Based on the search results, here's what I found regarding the CoRL 2026 Instructions for Authors:

**Page Limit:**
The page limit is 8 pages for the main paper. Acknowledgments, References, and Appendix (optional) will not count towards the page limit.

**Template:**
Authors should use the LaTeX template available via Google Drive link. The template should use "\usepackage[final]{corl_2026}"

**Double-Blind Anonymity:**
While the search results don't explicitly detail the anonymity requirements for CoRL 2026 specifically, they do reference that CoRL uses a double-blind review process. The search results show that CoRL is double-blind, which means all papers must be anonymized, and the submitted papers and reviews will be publicly accessible, but only accepted papers will be de-anonymized.

**Supplementary Materials:**
A
…[truncated 483 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "WebSearch",
  "elapsed_ms": 6481
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-18T02:08:44.614164+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "Extract ALL submission requirements: page limit, template name, anonymity rules (double-blind?), appendix rules, supplementary material rules, limitations section requirements, checklist requirements, font size, margin requirements, reference format. List every concrete requirement."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl.org/contributions/instruction-for-authors",
    "prompt": "Extract ALL submission requirements: page limit, template name, anonymity rules (double-blind?), appendix rules, supplementary material rules, limitations section requirements, checklist requirements, font size, margin requirements, reference format. List every concrete requirement."
  }
}
```

</details>

---


### Tool call

_source line 125 · 2026-05-18T02:08:45.872268+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl.org/contributions/call-for-papers",
  "prompt": "Extract all key deadlines, topics of interest, submission requirements, review process details, and any specific content requirements (e.g. robotics focus, limitations section, ethical statement)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl.org/contributions/call-for-papers",
    "prompt": "Extract all key deadlines, topics of interest, submission requirements, review process details, and any specific content requirements (e.g. robotics focus, limitations section, ethical statement)."
  }
}
```

</details>

---


### Tool result

_source line 126 · 2026-05-18T02:08:49.708186+00:00_

# CoRL 2026 Call for Papers - Key Information

## Deadlines
No specific deadlines are provided on this page. Authors should refer to the "Instruction for Authors" section for submission timeline details.

## Topics of Interest
CoRL 2026 welcomes research at the robotics-machine learning intersection, including:

- "Learning representations for robotic perception and control"
- Foundation models and general-purpose knowledge systems for robotics
- Imitation and reinforcement learning for robot control
- Probabilistic learning and uncertainty representation
- Robot perception, sensor fusion, and vision systems
- Human-robot interaction and natural language instruction
- Robot manipulation, navigation, locomotion, and autonomous driving
- Theoretical foundations, generalization theory, and uncertainty quantification
- Video/latent world models, benchmarks, and datasets

## Submission Requirements

**Core Focus:** Submissions must center on "a core robotics problem" with demonstrated relevance to robotics. Papers lacking a robotics focus will be rejected without review.

**Mandatory Sections:** All submissions must include "a Limitations section, explicitly describing limiting assumptions, failure modes, and other limitations."

**Encouraged Supplementary Materials:** Authors should consider submitting video, code, and datasets alongside their papers.

**Evidence of Transferability:** Real-robot experiments or "convincing evidence that simulation experiments are transferable to real robots" is strongly encouraged.

## Review Process Details
No specific peer review procedures, reviewer qualifications, or decision timelines are detailed on this page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "WebFetch",
  "elapsed_ms": 3835
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-18T02:08:49.909383+00:00_

# CoRL 2026 Submission Requirements

## Page Limits
- **Initial submission:** "8 pages for the main paper"
- **Camera-ready:** 9 pages main text
- Acknowledgments, references, and appendix do not count toward limits

## Template & Formatting
- LaTeX template required (provided via Google Drive link)
- Camera-ready uses `\usepackage[final]{corl_2026}`
- Footer on first page: "10th Conference on Robot Learning (CoRL 2026), Austin, Texas, USA"
- Text density, fonts, spacing, and margins must match provided template

## Anonymity
- "Double-blind, which means all papers must be anonymized"
- Camera-ready version includes full author names (not anonymous)

## Required Sections
- **Limitations section:** "explicitly describing limiting assumptions, failure modes, and other limitations" (counts toward 8-page limit)

## Appendix
- Optional for both submissions
- "Reviewers are not required to read the Appendix"
- Camera-ready: include appendix at end of PDF, not separately

## Supplementary Materials
- Submit as single zip file through OpenReview
- Video: maximum 250 MB, suggested 3 minutes maximum
- PMLR does not allow videos as supplementary material; host externally instead
- Authors encouraged to provide reproducibility details

## Additional Requirements
- No specific checklist mentioned
- No explicit font size or margin measurements stated (must match template)
- Reference format follows PMLR standards (not detailed separately)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "WebFetch",
  "elapsed_ms": 5295
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-18T02:09:03.471004+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/",
  "description": "List paper section files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/",
    "description": "List paper section files"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-18T02:09:03.572244+00:00_

abstract_body.tex
analysis.tex
appendix.tex
conclusion.tex
introduction.tex
methodology.tex
related_work.tex
results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-18T02:09:12.138303+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-18T02:09:12.591154+00:00_

1	Temporal abstraction via variable-rate imagination is a natural extension of world-model reinforcement learning, yet we find that every variable-rate configuration of DreamerV3 degrades performance, despite the success of identical $\Delta t$-conditioning in MPC-based methods. Through factorial diagnostics on two continuous-control tasks (Walker Walk, Cheetah Run), we identify the combination of trained temporal embedding and multi-rate data exposure as the causal factor and characterize the resulting failure mode: \emph{conditioning-induced value overestimation} (CIVO). The trained embedding enables the RSSM reward head to develop a $2.78\times$ prediction gap between $\Delta t{=}1$ and $\Delta t{=}2$, which the critic internalizes as optimistic values. This mechanism universally degrades performance to below 30\% of baseline across all three tested seeds ($n{=}3$), with two progressing toward full collapse and one self-correcting to a stable but degraded state. Gradient decomposition reveals that despite the reward head providing the largest gradient contribution (38--49\%), the observation decoder channel (16--22\%) carries the critical $\Delta t$-specific spatial information that drives the fidelity gap. Full-pathway gradient stopping partially prevents CIVO but succeeds in only 50\% of cases; this exposes additional mechanisms beyond gradient-mediated co-adaptation. A lightweight online detector that monitors value-to-evaluation ratio dynamics identifies CIVO onset with 100\% sensitivity (3/3 cases) and provides predictive warning before performance degradation in 2/3 cases, which supports early intervention without a reference baseline. The contrast with MPC-based methods identifies the feedback architecture (imagination-based bootstrapping versus re-planning) as the structural factor that transforms manageable model imprecision into pathological value dynamics.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-18T02:09:12.591639+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-18T02:09:13.044646+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	TAWM \citep{nhu2025tawm} shows that conditioning a world model on step size $\dt$ yields consistent gains within TD-MPC2's MPC framework \citep{hansen2024tdmpc2}. Can the same $\dt$-conditioning bring temporal abstraction to imagination-based actor-critic methods like DreamerV3 \citep{hafner2023dreamerv3}, where policies are trained entirely in imagined rollouts?
5	
6	We find that it cannot. Every variable-rate configuration we test degrades performance catastrophically: fixed $\dt{=}2$ collapses to $14\%$ of baseline, fixed $\dt{=}4$ never exceeds $19\%$ of baseline, and a learned Gumbel-Softmax gate collapses to $11\%$. Through a factorial analysis on Walker Walk \citep{tassa2018dmcontrol}, we isolate the combination of a \emph{trained} $\dt$-embedding and multi-rate data exposure as the causal factor within the factorial design tested. This trained-and-exposed embedding enables the RSSM reward head to develop a $2.78\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$, which the critic internalizes as optimistic value estimates, a failure mode we term \emph{conditioning-induced value overestimation} (CIVO). A $\nve \geq 1.5\times$ threshold (35K+ window) achieves 11/12 CIVO classification ($n{=}12$, single environment), with one non-CIVO false positive, a failure mode analogous to delusional bias \citep{lu2018nondelusional} that arises from model imprecision amplified by learned temporal conditioning. Gradient decomposition reveals a non-obvious mechanism: the reward head contributes the largest gradient share (38--49\%) but does not encode $\dt$-specific structural information, while the observation decoder channel (16--22\%) carries the critical spatial predictions that drive the RSSM fidelity gap. Reward-only gradient stopping fails (NVE $10.42\times$) despite targeting the largest pathway; full-pathway SGS that removes observation decoder gradients from the temporal embedding \sgsclaim{} (eval \sgseva
…[truncated 1239 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-18T02:09:13.045186+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-18T02:09:13.498136+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Temporal Abstraction.}
5	The options framework \citep{sutton1999options} and model-free action-repetition methods \citep{sharma2017figar, biedenkapp2021temporl, lakshminarayanan2017dynamic} achieve temporal abstraction by training values on real transitions, insulating them from model-induced bias. In world-model RL, the Dreamer family \citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3} and transformer-based variants \citep{micheli2023iris, robine2023twm, hafner2025dreamerv4} train policies in imagination at fixed $\dt{=}1$. Several works introduce temporal abstraction via hierarchical representations \citep{gumbsch2024thick, mattes2024hieros}, goal-conditioned jumps \citep{li2025lsimagine}, or multi-scale state-space models \citep{shaj2023mts3}, but none conditions a flat dynamics model on $\dt$ for imagination-based policy training.
6	
7	\paragraph{TAWM and the MPC--Imagination Contrast.}
8	TAWM \citep{nhu2025tawm} conditions a world model on $\dt$ within TD-MPC2 \citep{hansen2024tdmpc2} and achieves consistent gains. The critical distinction is architectural: TAWM re-plans from real states at every step, so model errors do not accumulate into the critic. We show that identical $\dt$-conditioning fails in DreamerV3's imagination loop, where errors compound through bootstrapping and transform manageable imprecision into pathological value overestimation.
9	
10	\paragraph{Value Overestimation.}
11	\citet{thrun1993issues} first identified maximization bias in Q-learning with function approximation. Double Q-learning \citep{vanhasselt2016double} decouples action selection from evaluation; TD3 \citep{fujimoto2018td3} extends this to actor-critic methods via clipped double-Q critics; SAC \citep{haarnoja2018sac} uses entropy regularization to implicitly reduce overestimation; REDQ \citep{chen2021redq} further mitigates overestimation through randomized Q-function ensembles. These model-
…[truncated 2516 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-18T02:09:13.548950+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex"
  }
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-18T02:09:13.549642+00:00_

1	\section{Experimental Setup}
2	\label{sec:methodology}
3	
4	\subsection{Base Architecture}
5	\label{sec:base_arch}
6	
7	All experiments build on DreamerV3 \citep{hafner2023dreamerv3}, which learns a recurrent state-space model (RSSM) with discrete latent states ($32$ categories $\times$ $32$ classes), uses symlog-transformed predictions, and trains an actor-critic entirely within imagined trajectories. The standard configuration imagines $H{=}15$ steps at a fixed temporal resolution of $\dt{=}1$, meaning each imagination step corresponds to one environment transition.
8	
9	\subsection{Variable-Rate Imagination Mechanism}
10	\label{sec:variable_rate}
11	
12	We introduce three orthogonal architectural modifications that enable variable-rate imagination in DreamerV3. Each can be independently toggled to isolate its contribution.
13	
14	\paragraph{Temporal embedding.}
15	A learned embedding $e(\dt)$ is concatenated to the RSSM input at each imagination step to condition state predictions on the temporal scale. We test three modes:
16	\begin{itemize}[nosep,leftmargin=*]
17	\item \textbf{Trained}: embedding parameters are updated via backpropagation through the world model loss, so the RSSM can co-adapt its dynamics and reward predictions to the temporal scale.
18	\item \textbf{Frozen}: a fixed random projection of identical dimensionality (\texttt{requires\_grad=False}). The RSSM receives a temporal signal but cannot co-adapt to it.
19	\item \textbf{Removed}: embedding dimension set to zero; no temporal conditioning signal is provided.
20	\end{itemize}
21	We further distinguish \textbf{trained-and-exposed} (subsample ON: the RSSM trains on $\dt{>}1$ transitions) from \textbf{trained-but-unexposed} (subsample OFF: $\dt{>}1$ used only during imagination). This four-way classification (trained/exposed, trained/unexposed, frozen, removed) is the key causal structure of our factorial design.
22	
23	\paragraph{Temporal subsampling.}
24	When enabled, the replay buffer augment
…[truncated 9234 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-18T02:09:17.881945+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-18T02:09:18.335171+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\nve$, \S\ref{sec:metrics}).
5	
6	%% ============================================================
7	%% TABLE 1: Main results summary
8	%% ============================================================
9	
10	\begin{table*}[t]
11	\centering
12	\caption{Key configurations and outcomes. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded. Complete results for all 20 configurations in Table~\ref{tab:complete_results}.}
13	\label{tab:main_results}
14	\footnotesize
15	\setlength{\tabcolsep}{4pt}
16	\begin{tabular}{llcccccl}
17	\toprule
18	\textbf{Exp} & \textbf{Config} & \textbf{dt\_emb} & \textbf{Sub} & \textbf{H} & \textbf{Eval@final} & \textbf{NVE} & \textbf{Outcome} \\
19	\midrule
20	001 & Baseline ($\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
21	\midrule
22	\rowcolor{gray!15}
23	008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\times$ & Full collapse \\
24	008f & No dt\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\times$ & Healthy \\
25	008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\times$ & Healthy \\
26	015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\times$ & Grad.\ starvation \\
27	022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\times$ & No CIVO \\
28	\midrule
29	\multicolumn{8}{l}{\textit{Cross-environment validation}} \\
30	\rowcolor{gray!15}
31	010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\times$ & Collapsed \\
32	019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\times$$^c$ & Transient onset \\
33	\bottomrule
34	\end{tabular
…[truncated 20999 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-18T02:09:18.595645+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-18T02:09:19.349718+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	The results establish three insights that frame CIVO as a structural vulnerability of flat temporal conditioning in imagination-based RL. Full mechanistic analysis, gradient decomposition, and seed-divergence discussion are in Appendix~\ref{sec:appendix_analysis}.
5	
6	\paragraph{CIVO mechanism.}
7	The RSSM reward head develops a $2.78\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$ under trained conditioning (Table~\ref{tab:rssm_fidelity}), providing the systematic bias that the critic internalizes and the actor exploits. This creates a four-stage feedback loop analogous to delusional bias \citep{lu2018nondelusional} but model-induced rather than policy-class-induced.  Full-pathway SGS (exp\_018) targets the gradient channel that maintains this bias, yet yields mixed results (50\% recovery rate). This indicates that CIVO involves mechanisms beyond gradient-mediated co-adaptation of the temporal embedding.
8	
9	\paragraph{Gradient decomposition and intervention design.}
10	\label{sec:gradient_evolution_main}
11	Gradient decomposition (Figure~\ref{fig:gradient_decomp}, Table~\ref{tab:gradient_decomposition}) reveals a non-obvious structure: the reward head provides the largest gradient contribution to $e_{\Delta t}$ (49.0\% at 55K, 38.1\% at 112K), yet reward-only SGS (exp\_016e) is functionally insufficient (NVE $10.42\times$, collapse).  The observation decoder channel contributes the smallest share (16.3\% at 55K, 21.5\% at 112K) but encodes the critical $\dt$-specific spatial predictions that generate the RSSM fidelity gap.  Full-pathway SGS, which removes observation decoder \emph{and} reward gradients from $e_{\Delta t}$, \sgsclaim{} (seed~1: peak NVE $\sgsnve{}\times$, eval \sgseval{}; seed~2: collapsed, eval 40.8).  The 50\% recovery rate confirms that the observation decoder gradient pathway is causally involved but reveals that CIVO's feedback loop has redundant mechanisms not fully captured by grad
…[truncated 4233 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-18T02:09:19.400491+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-18T02:09:19.602128+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We have presented a systematic factorial diagnostic of temporal abstraction in DreamerV3 across two continuous-control environments. The analysis identifies the combination of trained $\dt$-embedding and multi-rate data exposure as the causal factor behind conditioning-induced value overestimation (CIVO). The key findings are:
5	
6	\begin{enumerate}[nosep,leftmargin=*]
7	\item Every variable-rate imagination configuration degrades relative to the $\dt{=}1$ baseline, with degradation scaling monotonically with $\dt$.
8	\item A normalized value-to-eval threshold of $\nve \geq 1.5\times$ (35K+ window) achieves 11/12 CIVO classification ($n{=}12$, 91.7\%), with the single false positive arising from a mechanistically distinct non-CIVO collapse. The combination of trained $\dt$-embedding and multi-rate data exposure is the causal factor; unexposed, frozen, or removed embeddings prevent overestimation.
9	\item The RSSM reward head develops a $2.78\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$ under trained conditioning. This systematic bias drives critic overestimation.
10	\item The same CIVO trigger produces stochastic downstream outcomes (full collapse and transient CIVO with self-correction) across seeds of identical configurations.
11	\item Restricting imagination to $\dt{=}1$ does not fully prevent collapse: one of two seeds fails via a qualitatively distinct non-CIVO pathway (eval-driven with increasing entropy). This shows that the trained $\dt$-embedding creates vulnerability through multiple mechanisms.
12	\item A lightweight online detector that monitors the dynamics of the value-to-evaluation ratio identifies CIVO onset with 100\% sensitivity across three positive cases, with predictive detection (alert before performance degradation) in two of three. A timing guideline ($<$70K steps = high confidence) separates genuine CIVO from late-stage false positives.
13	\end{enumerate}
14	
15	The contrast with 
…[truncated 2422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-18T02:09:19.602681+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-18T02:09:19.907778+00:00_

1	% --- APPENDIX ---
2	
3	\section{Complete Experimental Results}
4	\label{sec:complete_results}
5	
6	Table~\ref{tab:complete_results} reports all 20 experimental configurations. The main text (Table~\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\_s3), SGS interventions (018), and mitigation experiments (008e\_v3).
7	
8	\begin{table*}[t]
9	\centering
10	\caption{Complete experimental results. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded; $\dagger$\,marks a false positive (non-CIVO collapse with elevated NVE).}
11	\label{tab:complete_results}
12	\footnotesize
13	\setlength{\tabcolsep}{4pt}
14	\begin{tabular}{llcccccl}
15	\toprule
16	\textbf{Exp} & \textbf{Config} & \textbf{dt\_emb} & \textbf{Sub} & \textbf{H} & \textbf{Eval@final} & \textbf{NVE} & \textbf{Outcome} \\
17	\midrule
18	001 & Baseline ($\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
19	\rowcolor{gray!15}
20	006 & Fixed $\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\times$ & Collapsed \\
21	007 & Fixed $\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\
22	005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\
23	\midrule
24	\rowcolor{gray!15}
25	008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\times$ & Full collapse \\
26	\rowcolor{gray!15}
27	009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\times$ & Transient CIVO \\
28	\rowcolor{gray!15}
29	008d\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\diamond$ @105K & 1.53$\times$ & Late-onset collapse \\
30	008f & No dt\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\times$ & Healthy \\
31	008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\times$ & Healthy \\
32	015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\times$ & Grad.\ starvation \\
33	022b & Frozen emb + Gumbel gate 
…[truncated 32618 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 305
}
```

</details>

---


### Tool call

_source line 146 · 2026-05-18T02:09:27.251181+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-18T02:09:28.708512+00:00_

1	% Auto-generated from literature_map.yaml
2	% 76 entries
3	
4	@article{sutton1999options,
5	  title = {Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning},
6	  author = {Sutton, R.S and Precup, D and Singh, S},
7	  year = {1999},
8	  journal = {Artificial Intelligence 112},
9	}
10	
11	@inproceedings{hafner2020dreamerv1,
12	  title = {Dream to Control: Learning Behaviors by Latent Imagination},
13	  author = {Hafner, D and Lillicrap, T and Ba, J and Norouzi, M},
14	  year = {2020},
15	  booktitle = {International Conference on Learning Representations},
16	}
17	
18	@article{hafner2023dreamerv3,
19	  title = {Mastering Diverse Domains through World Models},
20	  author = {Hafner, Danijar and Pasukonis, Jurgis and Ba, Jimmy and Lillicrap, Timothy},
21	  year = {2025},
22	  journal = {Nature},
23	  eprint = {2301.04104},
24	  archivePrefix = {arXiv},
25	}
26	
27	@inproceedings{sharma2017figar,
28	  title = {Fine Grained Action Repetition for Deep Reinforcement Learning},
29	  author = {Sharma, S and Lakshminarayanan, A.S and Ravindran, B},
30	  year = {2017},
31	  booktitle = {International Conference on Learning Representations},
32	}
33	
34	@inproceedings{janner2019mbpo,
35	  title = {When to Trust Your Model: Model-Based Policy Optimization},
36	  author = {Janner, M and Fu, J and Zhang, M and Levine, S},
37	  year = {2019},
38	  booktitle = {Advances in Neural Information Processing Systems},
39	}
40	
41	@inproceedings{ke2019learning,
42	  title = {Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future},
43	  author = {Ke, N.R and Singh, A and Touati, A and Goyal, A and Bengio, Y and Parikh, D and Batra, D},
44	  year = {2019},
45	  booktitle = {International Conference on Learning Representations},
46	}
47	
48	@article{asadi2019combating,
49	  title = {Combating the Compounding-Error Problem with a Multi-step Model},
50	  author = {Asadi, K and Misra, D and Kim, S and Littman, M.L},
51	  yea
…[truncated 1979 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 1457
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-18T02:09:28.760052+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon && ls artifacts/figures/paper/ 2>/dev/null; echo \"===\"; ls artifacts/figures/ 2>/dev/null | head -20",
  "description": "List available figure files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon && ls artifacts/figures/paper/ 2>/dev/null; echo \"===\"; ls artifacts/figures/ 2>/dev/null | head -20",
    "description": "List available figure files"
  }
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-18T02:09:32.030335+00:00_

README.md
__pycache__
actor_loss_data.json
fig1_learning_curves.pdf
fig1_learning_curves.png
fig1_learning_curves.py
fig2_nve_trajectory.pdf
fig2_nve_trajectory.png
fig2_nve_trajectory.py
fig3_factorial_grid.pdf
fig3_factorial_grid.png
fig3_factorial_grid.py
fig3_nve_diagnostic_d054.pdf
fig3_nve_diagnostic_d054.png
fig3_nve_diagnostic_d054.py
fig4_mechanism_diagram.pdf
fig4_mechanism_diagram.png
fig4_mechanism_diagram.py
fig5_dt_amplification.pdf
fig5_dt_amplification.png
fig5_dt_amplification.py
fig6_collapse_pathways_d054.pdf
fig6_collapse_pathways_d054.png
fig6_collapse_pathways_d054.py
fig6_multiple_pathways.pdf
fig6_multiple_pathways.png
fig6_multiple_pathways.py
fig_style.py
===
archive
civo_detector_validation.pdf
civo_detector_validation.png
data
fig1_nve_trajectory.pdf
fig1_nve_trajectory.png
fig2_civo_decomposition.pdf
fig2_civo_decomposition.png
fig3_gradient_decomposition.pdf
fig3_gradient_decomposition.png
fig4_entropy_dynamics.pdf
fig4_entropy_dynamics.png
paper
pickcube_ve_comparison.pdf
pickcube_ve_comparison.png
plot_civo_detector_validation.py
plot_pickcube_ve_comparison.py
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/sessions/review_director_9a57450c

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "elapsed_ms": 3270
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-18T02:09:32.332051+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper && grep -c '\\\\\\\\cite' sections/*.tex && echo \"===\"; grep -oP '\\\\\\\\cite[tp]?\\{[^}]+\\}' sections/*.tex | sed 's/.*\\\\\\\\cite[tp]\\?{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u | wc -l && echo \"=== unique cite keys ===\" && grep -oP '\\\\\\\\cite[tp]?\\{[^}]+\\}' sections/*.tex | sed 's/.*\\\\\\\\cite[tp]\\?{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
  "description": "Count citations and list unique cite keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper && grep -c '\\\\\\\\cite' sections/*.tex && echo \"===\"; grep -oP '\\\\\\\\cite[tp]?\\{[^}]+\\}' sections/*.tex | sed 's/.*\\\\\\\\cite[tp]\\?{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u | wc -l && echo \"=== unique cite keys ===\" && grep -oP '\\\\\\\\cite[tp]?\\{[^}]+\\}' sections/*.tex | sed 's/.*\\\\\\\\cite[tp]\\?{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
    "description": "Count citations and list unique cite keys"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-18T02:09:32.433197+00:00_

sections/abstract_body.tex:0
sections/analysis.tex:0
sections/appendix.tex:0
sections/conclusion.tex:0
sections/introduction.tex:0
sections/methodology.tex:0
sections/related_work.tex:0
sections/results.tex:0
0
=== unique cite keys ===
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/sessions/review_director_9a57450c

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-18T02:09:43.389039+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper && grep -ohP '\\\\\\\\cite[tp]?\\{[^}]+\\}' sections/*.tex | sed 's/.*cite[tp]\\?{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
  "description": "Extract all unique citation keys from tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper && grep -ohP '\\\\\\\\cite[tp]?\\{[^}]+\\}' sections/*.tex | sed 's/.*cite[tp]\\?{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
    "description": "Extract all unique citation keys from tex files"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-18T02:09:44.815480+00:00_

Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/sessions/review_director_9a57450c

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "elapsed_ms": 1426
}
```

</details>

---


### Tool call

_source line 154 · 2026-05-18T02:09:45.318930+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper && grep -c '@' references.bib && echo \"=== bib keys ===\" && grep -oP '@\\w+\\{(\\w+)' references.bib | sed 's/@\\w*{//' | sort -u",
  "description": "Count and list all bib entry keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper && grep -c '@' references.bib && echo \"=== bib keys ===\" && grep -oP '@\\w+\\{(\\w+)' references.bib | sed 's/@\\w*{//' | sort -u",
    "description": "Count and list all bib entry keys"
  }
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-18T02:09:45.419879+00:00_

78
=== bib keys ===
agarwal2021precipice
andrychowicz2021whatmatters
asadi2019combating
barkley2024stealing
beckerehmck2023multitimestep
biedenkapp2021temporl
bjorck2022variance
braylan2015frame
bredis2026nedreamer
chen2021redq
chen2022transdreamer
chua2018pets
colas2018seeds
engstrom2020implementation
farebrother2024stopregressing
frauenknecht2025rollouts
fujimoto2018td3
gumbsch2024thick
haarnoja2018sac
hafner2020dreamerv1
hafner2021dreamerv2
hafner2022director
hafner2023dreamerv3
hafner2025dreamerv4
hansen2024tdmpc2
henderson2018deep
hussing2024dissecting
jaderberg2017unreal
janner2019mbpo
ke2019learning
kim2025deas
kobayashi2025metacontroller
kumar2022dr3
lakshminarayanan2017dynamic
lambert2020objective
lambert2022investigating
lee2021sunrise
lee2024dreamsmooth
lenz2025macura
li2025lsimagine
liu2022dmve
liu2025vanta
lu2018nondelusional
luo2025vpl
lyle2021auxiliary
lyle2022capacity
lyle2024normalization
ma2024harmonydream
mattes2024hieros
micheli2023iris
nachum2018hiro
nagabandi2018neural
nhu2025tawm
nie2025sdar
nikishin2022primacy
nikishin2023plasticity
palenicek2025diminishing
park2021sar
qiao2023mind
robine2023twm
schwarzer2023bbf
shaj2023mts3
sharma2017figar
sokar2023dormant
splates2025
su2020conqur
sutton1999options
tallec2019making
tassa2018dmcontrol
thrun1993issues
vanhasselt2016double
venkatraman2015improving
voelcker2025madtd
wang2024seac
yu2020mopo
zhang2025dymodreamer
zhang2026hwm
zhang2026instability
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/sessions/review_director_9a57450c

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-18T02:09:49.857939+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper && grep -ohP 'cite[tp]?\\{[^}]+\\}' sections/*.tex | sed 's/cite[tp]\\?{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
  "description": "Extract citation keys with fixed regex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper && grep -ohP 'cite[tp]?\\{[^}]+\\}' sections/*.tex | sed 's/cite[tp]\\?{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
    "description": "Extract citation keys with fixed regex"
  }
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-18T02:09:49.960247+00:00_

agarwal2021precipice
andrychowicz2021whatmatters
asadi2019combating
biedenkapp2021temporl
chen2021redq
engstrom2020implementation
frauenknecht2025rollouts
fujimoto2018td3
gumbsch2024thick
haarnoja2018sac
hafner2020dreamerv1
hafner2021dreamerv2
hafner2023dreamerv3
hafner2025dreamerv4
hansen2024tdmpc2
henderson2018deep
janner2019mbpo
lakshminarayanan2017dynamic
lambert2020objective
lambert2022investigating
li2025lsimagine
lu2018nondelusional
lyle2022capacity
ma2024harmonydream
mattes2024hieros
micheli2023iris
nhu2025tawm
nikishin2022primacy
nikishin2023plasticity
palenicek2025diminishing
robine2023twm
shaj2023mts3
sharma2017figar
sutton1999options
tallec2019making
tassa2018dmcontrol
thrun1993issues
vanhasselt2016double
yu2020mopo
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/sessions/review_director_9a57450c

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-18T02:10:03.880557+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon && cat agent/config.yaml | grep -A 15 \"external_review\" 2>/dev/null; echo \"---\"; cat agent/config.yaml 2>/dev/null | head -50",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon && cat agent/config.yaml | grep -A 15 \"external_review\" 2>/dev/null; echo \"---\"; cat agent/config.yaml 2>/dev/null | head -50",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-18T02:10:05.693603+00:00_

cat: agent/config.yaml: No such file or directory
---
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/sessions/review_director_9a57450c

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "elapsed_ms": 1813
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-18T02:10:05.846070+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper && comm -23 <(grep -oP '@\\w+\\{(\\w+)' references.bib | sed 's/@\\w*{//' | sort -u) <(grep -ohP 'cite[tp]?\\{[^}]+\\}' sections/*.tex | sed 's/cite[tp]\\?{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u)",
  "description": "List orphan bib entries not cited in text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper && comm -23 <(grep -oP '@\\w+\\{(\\w+)' references.bib | sed 's/@\\w*{//' | sort -u) <(grep -ohP 'cite[tp]?\\{[^}]+\\}' sections/*.tex | sed 's/cite[tp]\\?{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u)",
    "description": "List orphan bib entries not cited in text"
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-18T02:10:05.896790+00:00_

barkley2024stealing
beckerehmck2023multitimestep
bjorck2022variance
braylan2015frame
bredis2026nedreamer
chen2022transdreamer
chua2018pets
colas2018seeds
farebrother2024stopregressing
hafner2022director
hussing2024dissecting
jaderberg2017unreal
ke2019learning
kim2025deas
kobayashi2025metacontroller
kumar2022dr3
lee2021sunrise
lee2024dreamsmooth
lenz2025macura
liu2022dmve
liu2025vanta
luo2025vpl
lyle2021auxiliary
lyle2024normalization
nachum2018hiro
nagabandi2018neural
nie2025sdar
park2021sar
qiao2023mind
schwarzer2023bbf
sokar2023dormant
splates2025
su2020conqur
venkatraman2015improving
voelcker2025madtd
wang2024seac
zhang2025dymodreamer
zhang2026hwm
zhang2026instability
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/sessions/review_director_9a57450c

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-18T02:10:13.652630+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find config files"
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-18T02:10:14.129210+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "elapsed_ms": 476
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-18T02:10:14.582313+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n 'splates2025' /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib",
  "description": "Check splates2025 bib entry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n 'splates2025' /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib",
    "description": "Check splates2025 bib entry"
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-18T02:10:16.255003+00:00_

550:@article{splates2025,

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "elapsed_ms": 1672
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-18T02:10:16.355990+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper && wc -l sections/*.tex && echo \"=== total ===\" && cat sections/abstract_body.tex sections/introduction.tex sections/related_work.tex sections/methodology.tex sections/results.tex sections/analysis.tex sections/conclusion.tex | wc -l",
  "description": "Count lines in each section"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper && wc -l sections/*.tex && echo \"=== total ===\" && cat sections/abstract_body.tex sections/introduction.tex sections/related_work.tex sections/methodology.tex sections/results.tex sections/analysis.tex sections/conclusion.tex | wc -l",
    "description": "Count lines in each section"
  }
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-18T02:10:16.457248+00:00_

    1 sections/abstract_body.tex
   23 sections/analysis.tex
  357 sections/appendix.tex
   21 sections/conclusion.tex
    8 sections/introduction.tex
  109 sections/methodology.tex
   17 sections/related_work.tex
  227 sections/results.tex
  763 total
=== total ===
406
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/sessions/review_director_9a57450c

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-18T02:10:25.770562+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib",
  "offset": "548",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib",
    "offset": "548",
    "limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-18T02:10:25.771010+00:00_

548	}
549	
550	@article{splates2025,
551	  title = {Stable Planning with Temporally Extended Skills},
552	  author = {SPlaTES, authors},
553	  year = {2025},
554	  journal = {Reinforcement Learning Journal},
555	}
556	
557	@article{beckerehmck2023multitimestep,

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-18T02:10:26.574869+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "paper_framing.md",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "file": "paper_framing.md",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-18T02:10:26.625727+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md\", \"content\": \"# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\\n\\n## Title Candidates\\n\\n1. **\\\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\\\"**\\n2. ~~**\\\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\\\"**~~ (deprecated — \\\"delusional critic\\\" conflicts with Lu et al. 2018)\\n3. **\\\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\\\"** ← preferred after D037 terminology decision\\n4. **\\\"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination\\\"**\\n\\n**⚠️ D037 术语决定**: \\\"delusional critic\\\" → **\\\"conditioning-induced value overestimation\\\"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换：\\\"delusional critic\\\" → \\\"conditioning-induced value overestimation\\\"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。\\n\\n**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 \\\"known failure class 的 specific instance\\\" 升级为 \\\"dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability\\\"**。TAWM 是强化 novelty 的最关键参考文献。\\n\\n## Venue\\n\\n**CoRL 2026** — Deadline: 2026-05-29\\n\\n## Narrative Positioning\\n\\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\\n\\nThe contribution is a **strongly supported causal chain** from mechanism to failure 
…[truncated 3493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 172 · 2026-05-18T02:11:16.278577+00:00_

`splates2025` 仍有占位作者名 "SPlaTES, authors"。39/78 bib 条目未被引用。

现在汇报审稿编排并启动 Reviewer。

---

**审稿圆桌会议启动 — Round 2**

**投稿信息：**
- 目标 venue: CoRL 2026
- Deadline: Abstract 2026-05-26, Paper 2026-05-29
- 格式: 8 页正文 + 附录/参考文献不计页数, double-blind, 必须包含 Limitations section (计入 8 页)
- 关键要求: **论文必须聚焦核心 robotics 问题，否则不予审稿 (desk reject)**

**论文概况：**
- 标题: "Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
- 诊断分析论文，研究 DreamerV3 中 dt-conditioning 导致的 CIVO 现象
- 实验环境: Walker Walk, Cheetah Run (DMC), PickCube-v1 (ManiSkill3)
- 现有 Round 1 issue tracker 有 18 个 issues (6 critical)

**Reviewer 编排 (3 人)：**
1. **Reviewer 1** — 方法/实验严谨性: 因果声明、统计效力、实验设计、CIVO 机制论证
2. **Reviewer 2** — 新颖性/Venue Fit/Related Work: CoRL robotics 相关性、与 prior work 定位、贡献增量
3. **Reviewer 3** — 格式/写作/完整性: 模板合规、bibliography、AI 写作痕迹、页数、Limitations section

现在向三位 Reviewer 分配任务。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 15

## Round 15

60 recorded events


### User

_source line 173 · 2026-05-24T06:57:32.537993+00:00_

[Round 3 - 继续审稿]
论文已更新。请基于上一轮审稿意见，重点审查修改是否充分回应了之前提出的问题。
重点关注：
1. 上轮提出的问题是否已充分解决
2. 修改是否引入了新问题
3. 整体评分是否需要调整

上一轮审稿报告: `projects/event-gated-adaptive-horizon/artifacts/review_reports/round_2.md`
跨轮次问题追踪: `projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml`
请用 read_local_file 先读这两个文件,重点验证 status=in_progress 的 issue 是否已被充分修复。
派 Reviewer 时把 open/in_progress 的 issue 列表附在任务里,要求逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由。

[论文提交]
- 项目: event-gated-adaptive-horizon
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex
- 目标 venue: CoRL 2026
- 截止日期: 2026-05-29
- **引用验证**: ❌ 未启用

请继续审稿流程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-24T06:57:45.883523+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/skills/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/skills/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-24T06:57:45.934868+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/sessions/review_director_9a57450c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-24T06:57:46.186105+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-24T06:57:46.236742+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-24T06:57:56.923435+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-24T06:57:57.277589+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 354
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-24T06:57:57.428507+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
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

_source line 181 · 2026-05-24T06:57:57.480003+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-24T06:58:01.043657+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
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

_source line 183 · 2026-05-24T06:58:01.094308+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-24T06:58:04.011027+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read local file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read local file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-24T06:58:04.063039+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-24T06:58:09.638075+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_reports/round_2.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_reports/round_2.md"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-24T06:58:10.140405+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/sessions/review_director_9a57450c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-24T06:58:10.190997+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-24T06:58:10.241884+00:00_

1	issues:
2	  - id: "R1-N1"
3	    summary: "统计检验力严重不足：2-3 seeds 无法支撑 causal factor 声明，4/4 separating power 在 n=2 下 P≈6.25%"
4	    category: experiment
5	    severity: critical
6	    status: in_progress
7	    first_raised_round: 1
8	    last_seen_round: 1
9	    mentions:
10	      - round: 1
11	        reviewers: [1, 2, 3]
12	        note: "三位 reviewer 均认同统计效力不足"
13	    action_items:
14	      - round: 1
15	        action: "补 seeds: plan_010 (baseline s0 running), plan_011 (008d s1-s2), plan_012 (008f s3), plan_014 (008e_v3 s1-s2)"
16	        assigned_to: agent
17	        status: in_progress
18	      - round: 1
19	        action: "弱化因果语言: causal factor → strongly associated factor; necessary and sufficient → reliable predictor"
20	        assigned_to: paper_agent
21	        status: done
22	      - round: 1
23	        action: "统计报告改用 IQM + bootstrap CI per Agarwal et al. 2021"
24	        assigned_to: paper_agent
25	        status: done
26	    resolution: ""
27	    resolution_round: null
28	
29	  - id: "R1-N2"
30	    summary: "NVE 阈值 1.5× 为 post-hoc 选择，88.9% accuracy 是训练准确率，无独立验证"
31	    category: method
32	    severity: critical
33	    status: resolved
34	    first_raised_round: 1
35	    last_seen_round: 1
36	    mentions:
37	      - round: 1
38	        reviewers: [1, 2, 3]
39	        note: "三位 reviewer 一致认为 post-hoc"
40	    action_items:
41	      - round: 1
42	        action: "plan_034 NVE sensitivity analysis (1.3x/1.5x/1.7x/2.0x + AUROC), 0 GPU"
43	        assigned_to: agent
44	        status: done
45	      - round: 1
46	        action: "跨环境验证 (Cheetah 数据到后)"
47	        assigned_to: agent
48	        status: done
49	      - round: 1
50	        action: "改措辞: separating power → diagnostic threshold; 标注 in-sample post-hoc"
51	        assigned_to: paper_agent
52	        status: done
53	      - round: 1
54	        action: "LOEO cross-validation: mean AUROC 0.981, θ=1.5 在所有 fold 最优范围内"
55	        assigned_to: agent
56	        status: done
57	    resolution: "LOEO 交叉验证完成：3 环
…[truncated 13303 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-24T06:58:30.753609+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-24T06:58:31.207057+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_reports/round_1.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-24T06:58:31.207546+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool call

_source line 193 · 2026-05-24T06:58:31.258024+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 194 · 2026-05-24T06:58:31.760627+00:00_

{"result":"# 项目 event-gated-adaptive-horizon 概况\n\n## 实验状态 (133 个)\n\n- **exp_009a_baseline_walker_s2**: DONE (success) — \n- **exp_008e_v3_walker_s2**: DONE (negative) — \n- **exp_008e_v3_walker_s1**: DONE (success) — \n- **exp_006**: DONE (killed) — \n- **exp_008a**: DONE (killed) — \n- **exp_008c**: DONE (killed) — \n- **exp_008d**: DONE (killed) — \n- **exp_008e_v2_subsample_on_dt1_h15**: DONE (killed) — \n- **exp_rssm_fidelity_analysis**: DONE (success) — \n- **exp_008e_v3_subsample_on_dt1_h15**: DONE (success) — \n- **exp_009c_008f_walker_s2**: DONE (negative) — \n- **exp_006_fixed_dt2**: DONE (negative) — \n- **exp_008e_subsample_on_fixed_dt1**: DONE (killed) — \n- **exp_008e_subsample_on_dt1_h15**: DONE (killed) — \n- **exp_002_event_gated**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp_059_walker_trained_s5** (negative): Walker CIVO trigger 第5个独立seed验证。当前4/4 seeds触发sustained CIVO（p=0.0625 binomial test）。如果s5也触发 → p=0.03125，达到统计显著性阈值。关联 Claim 1: CIVO reproducibility。 ← 基于 exp_008d_civo_trigger_s3\n- **exp_008d_civo_trigger_s4** (success): Walker Walk CIVO trigger seed=4: trained dt_emb + subsample ON + H=8. 第四 seed 复现 CIVO (NVE>1.5×)，加强 Walker 因果论证的统计力度。Rebuttal 储备。 ← 基于 exp_008d_civo_trigger_s3\n- **exp_009b_008d_walker_s2** (negative): CIVO onset (NVE≥1.5×) reproduces on seed=2 with identical architecture, confirming the phenomenon is systematic rather than seed-specific. Collapse outcome may be stochastic. ← 基于 exp_008d_subsample_on_h8\n  [009b_literature_linkage](/api/workspace-files/projects/event-gated-adaptive-horizon/artifacts/exp_009b_008d_walker_s2/report/009b_literature_search.md)\n\n## 趋势\n成功 65 / 负向 36 / 失败 11 / 共 133\nnve_peak: 4.44 ↑（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nbjb1-40020: 空闲 cuda:0, cuda:1\nbjb1-45299: 无 GPU 信息\n\n## 告警\n- 016e: 已被终止 — unknown\n- exp_002_event_gated: 训练失败 — unknown\n- exp_006: 已被终止 — unknown\n- 
…[truncated 1245 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 553
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-24T06:58:31.761189+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-24T06:58:46.047875+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_reports/round_1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_reports/round_1.md"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-24T06:58:46.802317+00:00_

1	---
2	round: 1
3	overall_score: strong reject
4	timestamp: 2026-05-15T12:43:17.705786+00:00
5	reviewer_ids: [1, 2, 3]
6	cross_response_reviewer_ids: [1, 2, 3]
7	force_resubmit: False
8	---
9	
10	# 审稿报告 — Round 1
11	
12	**论文**: "Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
13	**目标 Venue**: CoRL 2026 Main Conference
14	**审稿日期**: 2026-05-15
15	**Reviewer 编排**: 3 人（R1: 方法严谨性 & 实验设计 | R2: 新颖性 & 贡献度 & Venue Fit | R3: 格式合规 & 写作质量）
16	**轮次**: Round 1 初审 + 交叉分享（1 轮收敛）
17	
18	---
19	
20	## Summary
21	
22	本文通过 factorial ablation 分析 DreamerV3 中 variable-rate imagination 的失败原因。在 Walker Walk (DMC) 上测试 9 组配置（2-3 seeds each），识别出 trained dt-embedding 导致 RSSM reward head 产生 2.78× 跨时间尺度预测偏差，critic 通过 imagination bootstrapping 将其内化为系统性高估——称为 conditioning-induced value overestimation (CIVO)。论文进一步发现同一 trigger 产生三种随机下游结果（full collapse / self-correction / oscillatory degradation），且限制 imagination 到 dt=1 不能完全防止崩溃（存在 non-CIVO Pathway B）。与 TAWM (MPC-based) 的对比将 feedback architecture 定位为关键结构差异。
23	
24	---
25	
26	## Strengths
27	
28	1. **清晰的问题定义和切入点**：将 "为什么 dt-conditioning 在 MPC 中成功但在 imagination-based AC 中失败" 作为核心问题，切入角度明确且有实际意义（3/3 reviewer 认可）
29	2. **结构化的 factorial 设计**：trained vs untrained vs removed embedding 的三向对比是方法论亮点，核心对照 008d vs 008f 在控制变量上是干净的（R3 在交叉回应中澄清）
30	3. **CIVO 机制描述细致**：四阶段反馈回路描述清晰，三种 post-CIVO 结果的刻画有信息量
31	4. **Multiple pathways 发现 (F6)**：Pathway A (value-driven) 和 Pathway B (eval-driven) 的识别是 genuine discovery，表明问题比单一 value overestimation 更深层（3/3 认可为论文最有价值的 insight）
32	5. **写作质量高**：F1-F6 因果链式叙述清晰，Figure/Table 信息密度高，术语定义到位（Clarity 获三位 reviewer 最高分 4/5 或 7/10）
33	6. **诚实的 Limitations**：承认单环境和单架构局限，F6 的 partial falsification 展示良好科学态度
34	
35	---
36	
37	## Weaknesses（按严重性排序）
38	
39	### Critical（影响接收决定）
40	
41	**W-C1. CoRL Venue Fit 严重不足 [3/3 reviewer 共识，最强共识]**
42	全文仅在 DMC Walker Walk（proprioceptive observations）上做实验，无任何 robotics benchmark（RoboSuite/ManiSkill/IsaacGym）、无 real-robot 实验、无 robotics application 讨论。Intro
…[truncated 9211 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-24T06:58:46.802786+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-24T06:58:46.953634+00:00_

1	\documentclass{article}
2	
3	% Load xcolor before corl_2026 (which loads color internally)
4	\usepackage[table]{xcolor}
5	\usepackage{corl_2026}
6	
7	\usepackage[utf8]{inputenc}
8	\usepackage[T1]{fontenc}
9	\usepackage{amsmath,amssymb}
10	\usepackage{booktabs}
11	\usepackage{multirow}
12	\usepackage{graphicx}
13	\graphicspath{{../../artifacts/}}
14	\usepackage{colortbl}
15	\usepackage{caption}
16	\usepackage{subcaption}
17	\usepackage{array}
18	\usepackage{enumitem}
19	\usepackage{wrapfig}
20	\usepackage{algorithm}
21	\usepackage{algorithmic}
22	
23	% Custom commands
24	\newcommand{\dt}{\mathrm{dt}}
25	\newcommand{\nve}{\mathrm{nve}}
26	% SGS result values (018 seed 1: partial mitigation; seed 2: collapsed — 0/3 CIVO elimination)
27	\newcommand{\sgseval}{448.3}
28	\newcommand{\sgsnve}{1.66}
29	\newcommand{\sgsclaim}{reduced CIVO severity in one of two Walker seeds but eliminated it in neither (0/3 across environments)}
30	\newcommand{\ie}{\textit{i.e.}}
31	\newcommand{\eg}{\textit{e.g.}}
32	\newcommand{\cf}{\textit{cf.}}
33	\newcommand{\etal}{\textit{et al.}}
34	
35	\title{Why Temporal Abstraction Can Fail in Imagination-Based RL:\\
36	A Diagnostic Analysis of Variable-Rate DreamerV3}
37	
38	\author{
39	  Anonymous Authors
40	}
41	
42	\begin{document}
43	\maketitle
44	
45	\begin{abstract}
46	\input{sections/abstract_body}
47	\end{abstract}
48	
49	\keywords{World Models, Temporal Abstraction, Value Overestimation, DreamerV3}
50	
51	% --- INTRODUCTION ---
52	\input{sections/introduction}
53	
54	% --- RELATED WORK ---
55	\input{sections/related_work}
56	
57	% --- METHODOLOGY ---
58	\input{sections/methodology}
59	
60	% --- RESULTS ---
61	\input{sections/results}
62	
63	% --- ANALYSIS ---
64	\input{sections/analysis}
65	
66	% --- CONCLUSION ---
67	\input{sections/conclusion}
68	
69	% no \bibliographystyle needed — corl_2026.sty sets it automatically
70	\bibliography{references}
71	
72	% --- APPENDIX ---
73	\appendix
74	\input{sections/appendix}
75	
76	\end{document}
7
…[truncated 2 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-24T06:59:04.591181+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-24T06:59:04.591641+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-24T06:59:08.492214+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-24T06:59:08.542902+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/_corl_template/corl_2026_template_submission/example.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/_corl_template/__MACOSX/corl_2026_template_submission/._example.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-24T06:59:11.403491+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-24T06:59:11.859222+00:00_

1	World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales. We find that $\Delta t$-conditioning, effective in model-predictive control (MPC), cannot transfer to imagination-based actor-critic training: every variable-rate DreamerV3 configuration degrades to 14--19\% of baseline. Factorial diagnostics on two continuous-control tasks isolate trained temporal embedding with multi-rate data exposure as the strongest predictor of this failure---\emph{conditioning-induced value overestimation} (CIVO; 26/29, AUROC${=}0.953$, LOEO cross-validated). The RSSM develops a $2.78\times$ reward prediction gap at $\Delta t{>}1$ that the critic internalizes as optimistic values; the contrast with MPC identifies feedback architecture as the structural factor. No tested intervention across four levels (gradient, output, representation, architecture) reliably eliminates CIVO: dual critics converge in pure imagination ($\rho > 0.999$), rendering Double Q pessimism ineffective, though min $+$ increased capacity enables recovery. A lightweight NVE detector achieves 100\% sensitivity.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-24T06:59:11.959966+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-24T06:59:12.311848+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	World-model reinforcement learning enables sample-efficient learning directly on physical hardware \citep{wu2023daydreamer, hansen2024tdmpc2}. Real robotic tasks demand temporal abstraction: manipulation requires fast reactive grasping alongside slow approach planning, locomotion involves gait phases at different frequencies, and sim-to-real transfer must handle $\dt$ mismatches between simulation and hardware. TAWM \citep{nhu2025tawm} shows that conditioning a world model on step size $\dt$ yields consistent gains within TD-MPC2's MPC framework \citep{hansen2024tdmpc2}. Can the same $\dt$-conditioning bring temporal abstraction to imagination-based actor-critic methods like DreamerV3 \citep{hafner2023dreamerv3}, where policies are trained entirely in imagined rollouts?
5	
6	We find that it cannot. Every variable-rate configuration degrades performance catastrophically (14--19\% of baseline). Through a factorial analysis on Walker Walk \citep{tassa2018dmcontrol}, we isolate the combination of a \emph{trained} $\dt$-embedding and multi-rate data exposure as the strongest predictor. This combination enables the RSSM reward head to develop a $2.78\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$, which the critic internalizes as optimistic value estimates, a failure mode we term \emph{conditioning-induced value overestimation} (CIVO), analogous to delusional bias \citep{lu2018nondelusional} but model-induced rather than policy-class-induced. A normalized value-to-eval (NVE) threshold of $\geq 1.5\times$ achieves 26/29 classification ($n{=}29$, two environments, AUROC${=}0.953$, in-sample; LOEO cross-validated, Appendix~Table~\ref{tab:nve_loeo}).
7	
8	Gradient decomposition reveals that gradient magnitude does not predict causal importance: the reward head contributes 38--49\% of $\nabla_\theta e_{\dt}$ yet reward-only stopping fails, while the observation decoder (16--22\%) carries the critical signal. A fou
…[truncated 2265 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-24T06:59:12.312351+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-24T06:59:13.216220+00:00_

1	\section{Experimental Setup}
2	\label{sec:methodology}
3	
4	\subsection{Base Architecture}
5	\label{sec:base_arch}
6	
7	All experiments build on DreamerV3 \citep{hafner2023dreamerv3}, which learns a recurrent state-space model (RSSM) with discrete latent states ($32$ categories $\times$ $32$ classes), uses symlog-transformed predictions, and trains an actor-critic entirely within imagined trajectories. The standard configuration imagines $H{=}15$ steps at a fixed temporal resolution of $\dt{=}1$, meaning each imagination step corresponds to one environment transition.
8	
9	\subsection{Variable-Rate Imagination Mechanism}
10	\label{sec:variable_rate}
11	
12	We introduce three orthogonal architectural modifications that enable variable-rate imagination in DreamerV3. Each can be independently toggled to isolate its contribution.
13	
14	\paragraph{Temporal embedding.}
15	A learned embedding $e(\dt)$ is concatenated to the RSSM input at each imagination step to condition state predictions on the temporal scale. We test three modes:
16	\begin{itemize}[nosep,leftmargin=*]
17	\item \textbf{Trained}: embedding parameters are updated via backpropagation through the world model loss, so the RSSM can co-adapt its dynamics and reward predictions to the temporal scale.
18	\item \textbf{Frozen}: a fixed random projection of identical dimensionality (\texttt{requires\_grad=False}). The RSSM receives a temporal signal but cannot co-adapt to it.
19	\item \textbf{Removed}: embedding dimension set to zero; no temporal conditioning signal is provided.
20	\end{itemize}
21	We further distinguish \textbf{trained-and-exposed} (subsample ON: the RSSM trains on $\dt{>}1$ transitions) from \textbf{trained-but-unexposed} (subsample OFF: $\dt{>}1$ used only during imagination). This four-way classification (trained/exposed, trained/unexposed, frozen, removed) is the key experimental structure of our factorial design.
22	
23	\paragraph{Temporal subsampling.}
24	When enabled, the replay buffer a
…[truncated 5040 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-24T06:59:13.216720+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-24T06:59:13.769492+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\nve$, \S\ref{sec:metrics}).
5	
6	%% ============================================================
7	%% TABLE 1: Main results summary
8	%% ============================================================
9	
10	\begin{table*}[t]
11	\centering
12	\caption{Key configurations and outcomes. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded. Complete results for all 43 configurations in Table~\ref{tab:complete_results}.}
13	\label{tab:main_results}
14	\footnotesize
15	\setlength{\tabcolsep}{4pt}
16	\begin{tabular}{llcccccl}
17	\toprule
18	\textbf{Exp} & \textbf{Config} & \textbf{dt\_emb} & \textbf{Sub} & \textbf{H} & \textbf{Eval@final} & \textbf{NVE} & \textbf{Outcome} \\
19	\midrule
20	001 & Baseline ($\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
21	\midrule
22	\rowcolor{gray!15}
23	008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\times$ & Full collapse \\
24	008f & No dt\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\times$ & Healthy \\
25	008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\times$ & Healthy \\
26	015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\times$ & Grad.\ starvation \\
27	022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\times$ & No CIVO \\
28	\midrule
29	\multicolumn{8}{l}{\textit{Cross-environment validation}} \\
30	\rowcolor{gray!15}
31	010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\times$ & Collapsed \\
32	019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\times$$^c$ & Transient onset \\
33	049 & StackCube-v1 & trn & 
…[truncated 12455 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-24T06:59:13.770015+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-24T06:59:14.197730+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{CIVO mechanism.}
5	The RSSM develops a $2.78\times$ reward prediction gap under trained conditioning (Table~\ref{tab:rssm_fidelity}), analogous to delusional bias \citep{lu2018nondelusional}. Gradient magnitude $\neq$ causal importance: the reward head (38--49\% of $\nabla_\theta e_{\dt}$) fails when blocked alone; the observation decoder (16--22\%) carries the critical signal; full-pathway SGS (0/3) confirms forward-pass conditioning as the irreducible vulnerability. CIVO is upstream of estimation error---dual critics converge (\S\ref{sec:arch_results})---so standard corrections are inapplicable; MPC re-planning prevents accumulation (Appendix~\ref{sec:mpc_immune}).
6	
7	\paragraph{Practitioner guidelines.}
8	Monitor via NVE diagnostic ($\geq 1.5\times$, AUROC${=}0.953$; Table~\ref{tab:nve_loeo}). Freezing the $\dt$-embedding converts sustained CIVO (6/6 trained locomotion, NVE $1.53$--$108\times$) to transient spikes that self-correct within 20K steps (2/3 frozen Walker, $1.71$--$1.88\times$; 0/2 frozen Cheetah); untreated, extreme CIVO ($70.6\times$) causes irrecoverable damage (Appendix~\ref{sec:appendix_analysis}).
9	
10	\paragraph{Implications for robot learning.}
11	No $\dt$-embedding-dependent CIVO was observed in manipulation: all three ManiSkill environments exhibit ve-ratio transients (peaks $4$--$11\times$), but frozen controls show comparable or higher peaks (Table~\ref{tab:cross_domain}), establishing environment-specific origin. A possible mediator is reward density: locomotion provides continuous rewards accumulating coherent $\dt$-embedding bias, while manipulation rewards are sparse and contact-gated.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 427
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-24T06:59:14.225413+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-24T06:59:14.627309+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We identify trained $\dt$-embedding with multi-rate data exposure as the strongest predictor of CIVO in DreamerV3 (26/29, AUROC${=}0.953$; LOEO cross-validated). No tested intervention reliably eliminates CIVO; in pure imagination, dual critics converge ($\rho > 0.999$), rendering Double Q pessimism ineffective. The feedback architecture---MPC re-planning versus imagination-based bootstrapping---is the structural factor.
5	
6	\paragraph{Limitations.}
7	Our analysis covers proprioceptive locomotion (DMC) and simulated manipulation (ManiSkill) but does not test pixel-based observations, Atari benchmarks, or real-robot deployments where sensor noise and actuation latency introduce additional confounds.
8	All experiments use DreamerV3's RSSM; whether CIVO manifests in other imagination-based architectures (e.g., IRIS \citep{micheli2023iris} or latent-space planners beyond TD-MPC2) remains open.
9	We characterize CIVO under fixed-$\dt$ subsampling; learned temporal gates warrant separate study.
10	Statistical power with 4 seeds per configuration is limited \citep{colas2018seeds}; the NVE threshold (LOEO AUROC${=}0.981$) may require recalibration for different reward scales.
11	Code: upon acceptance.
12	\label{sec:limitations}
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-24T06:59:14.627741+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-24T06:59:15.230666+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Temporal abstraction in RL.}
5	The options framework \citep{sutton1999options}, option-critic \citep{bacon2017optioncritc}, HAM \citep{parr1998ham}, and MAXQ \citep{dietterich2000maxq} formalize temporal abstraction through hierarchical policies. Semi-MDP theory \citep{bradtke1995smdp} provides the mathematical foundation. Action-repetition methods \citep{sharma2017figar, biedenkapp2021temporl, park2021timediscretization} achieve simpler temporal abstraction via real transitions; \citet{wang2024elastic} learn elastic time steps that adapt step size to state dynamics. The Dreamer family \citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3, hafner2025dreamerv4} trains policies in imagination at fixed $\dt{=}1$; hierarchical variants \citep{hafner2022director, gumbsch2024thick, mattes2024hieros, li2025lsimagine} use subgoals or separate dynamics per scale, avoiding flat $\dt$-conditioning. TAWM \citep{nhu2025tawm} conditions a world model on $\dt$ within TD-MPC2 \citep{hansen2024tdmpc2} and achieves consistent gains; the critical distinction is that MPC re-plans from real states, so model errors do not accumulate into a critic (\S\ref{sec:discussion}).
6	
7	\paragraph{Value overestimation and model fidelity.}
8	Maximization bias \citep{thrun1993issues} has been addressed by Double Q-learning \citep{vanhasselt2016double}, TD3 \citep{fujimoto2018td3}, and ensemble methods \citep{chen2021redq}; in model-based settings, MBPO \citep{janner2019mbpo} and MOPO \citep{yu2020mopo} bound rollout error, while MOReL \citep{kidambi2020morel} and COMBO \citep{yu2021combo} penalize model uncertainty. \citet{lu2018nondelusional} identify delusional bias from policy-class constraints. CIVO is mechanistically distinct: the amplifier is the world model's co-adaptation with a learned temporal embedding, producing systematic reward-prediction bias at $\dt > 1$. Multi-timestep world models \citep{benechehab20
…[truncated 1421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-24T06:59:29.541750+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 219 · 2026-05-24T06:59:29.542520+00:00_

1	% --- APPENDIX ---
2	
3	\section{Complete Experimental Results}
4	\label{sec:complete_results}
5	
6	Table~\ref{tab:complete_results} reports all 42 experimental configurations. The main text (Table~\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\_s3, 008d\_s4), SGS interventions (018), cross-environment seeds (010b\_s0), and mitigation experiments (008e\_v3).
7	
8	\begin{table*}[t]
9	\centering
10	\caption{Complete experimental results. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded; $\dagger$\,marks a false positive (non-CIVO collapse with elevated NVE).}
11	\label{tab:complete_results}
12	\scriptsize
13	\setlength{\tabcolsep}{3pt}
14	\begin{tabular}{llcccccl}
15	\toprule
16	\textbf{Exp} & \textbf{Config} & \textbf{dt\_emb} & \textbf{Sub} & \textbf{H} & \textbf{Eval@final} & \textbf{NVE} & \textbf{Outcome} \\
17	\midrule
18	001 & Baseline ($\dt{=}1$, s1) & --- & --- & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
19	001 s2 & Baseline ($\dt{=}1$, s2) & --- & --- & 15 & 443.5 @105K & ---$^e$ & Healthy \\
20	\rowcolor{gray!15}
21	006 & Fixed $\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\times$ & Collapsed \\
22	007 & Fixed $\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\
23	005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\
24	\midrule
25	\rowcolor{gray!15}
26	008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\times$ & Full collapse \\
27	\rowcolor{gray!15}
28	009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\times$ & Transient CIVO \\
29	\rowcolor{gray!15}
30	008d\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\diamond$ @105K & 1.53$\times$ & Late-onset collapse \\
31	\rowcolor{gray!15}
32	008d\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\times$ & Full collapse \\
33	008f & No dt\_emb (s1) & --- & ON & 8 & 50
…[truncated 21737 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-24T06:59:29.593078+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
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

_source line 221 · 2026-05-24T06:59:29.643658+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-24T06:59:33.366174+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 223 · 2026-05-24T06:59:35.826080+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": "300",
  "limit": "400"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "offset": "300",
    "limit": "400"
  }
}
```

</details>

---


### Tool result

_source line 224 · 2026-05-24T06:59:36.077690+00:00_

300	
301	\section{Factorial Ablation Details}
302	\label{sec:appendix_factorial}
303	
304	This appendix provides the full factorial ablation results summarized in \S\ref{sec:f3f5_summary} of the main text.
305	
306	\paragraph{Embedding gradient analysis.}
307	Table~\ref{tab:three_way_emb} isolates embedding \emph{trainability} as the necessary condition for CIVO by comparing four gradient conditions under otherwise identical configurations ($H{=}8$, subsample ON, $\dt{=}2$ imagination).
308	
309	\begin{table}[h]
310	\centering
311	\caption{$\dt$-embedding gradient conditions on Walker Walk. Any gradient pathway updating $e_{\dt}$ is sufficient to induce CIVO; freezing or removing the embedding dramatically reduces severity.}
312	\label{tab:three_way_emb}
313	\footnotesize
314	\begin{tabular}{lccccl}
315	\toprule
316	Condition & Grad flow & Exp(s) & NVE peak & Eval & CIVO \\
317	\midrule
318	Trained & all & 008d & $1.53$--$4.62\times$ & 64--268 & 4/4 \\
319	Reward detach & obs+KL only & 044 & $4.45\times$ & 44$\to$538$^\dagger$ & 1/1 \\
320	Full SGS & KL only & 018 & $1.66\times$ & 448 & 1/1$^*$ \\
321	Frozen & none & 042, 015b, 047, 057 & $0.19$--$1.88\times$$^\ddagger$ & 204--612 & 2/4 \\
322	Removed & N/A & 008f & $0.97$--$1.41\times$ & 307--503 & 0/3 \\
323	\bottomrule
324	\end{tabular}
325	\vspace{1pt}
326	{\raggedright\footnotesize $^*$Full-SGS seed~1 (NVE $1.66\times$); seed~2 collapsed. $^\dagger$Self-corrected at ${\sim}175$K (eval 44$\to$538, 59\% baseline; 224K run). $^\ddagger$Exp\_047 (NVE $1.71\times$) and Exp\_057 (NVE $1.88\times$): both transient, self-correcting within 20K steps.\par}
327	\end{table}
328	
329	The reward-detach condition (exp\_044, \texttt{reward\_dt\_emb\_detach=True}) uses a backward hook to block reward-head gradients from reaching $e_{\dt}$, complementing the framework-level Reward SGS (exp\_016e). Both yield the same directional result---CIVO onset not prevented---ruling out implementation artifacts. Exp\_044 exhibits delayed CI
…[truncated 37433 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-24T06:59:40.706679+00:00_

Web search results for query: "CoRL 2026 call for papers submission guidelines author instructions"

Links: [{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Refactor conference data · huggingface/ai-deadlines at f3cc2d7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"}]

Based on the search results, here are the key submission guidelines and author instructions for CoRL 2026:

## Paper Format and Length

The page limit is 8 pages for the main paper, with Acknowledgments, References, and Appendix (optional) not counting towards the page limit. Reviewers are not required to read the Appendix.

## Required Content

All submissions should include a Limitations section (counted toward the 8-page limit), explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments, and how these might be addressed in the future. Authors are also encouraged to submit video, code and data as supplementary materials.

## Author Responsibilities and Policies

Every author with 3 or more submissions
…[truncated 915 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "WebSearch",
  "elapsed_ms": 7340
}
```

</details>

---


### Tool call

_source line 226 · 2026-05-24T07:01:04.284737+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "3",
  "text": "## Round 3 修订评估任务 — Reviewer 1（方法严谨性 + 实验充分性）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex`\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/submitted.pdf`\n**目标 Venue**: CoRL 2026 Main Conference\n**Deadline**: 2026-05-29\n**页数限制**: 8 页正文（References/Appendix 不计）\n**模板**: PMLR (`\\usepackage{corl_2026}`)\n**匿名规则**: Double-blind\n**审查侧重**: 方法严谨性、实验设计充分性、统计论证\n\n### 你的核心任务\n\n这是 Round 3 继续审稿。论文在 Round 1 后进行了大幅修改。你需要**逐条检查以下 open/in_progress issue**，标注 `[RESOLVED]` 或 `[STILL_OPEN]` + 理由：\n\n---\n\n### 必须逐条检查的 Issue（方法/实验类）\n\n**1. R1-N1 [critical, in_progress]: 统计检验力不足**\n- Round 1 问题：2-3 seeds 无法支撑 causal 声明\n- 已知修改：seeds 增至 4，语言从 \"causal factor\" 改为 \"strongest predictor\"，IQM + bootstrap CI 已添加\n- **检查要点**：4 seeds 是否足够？因果语言是否已充分弱化？IQM/CI 报告是否到位？论文现称 26/29 accuracy (AUROC=0.953, LOEO)——这些数字的统计意义如何？\n\n**2. R1-N4 [critical, in_progress]: 单环境局限**\n- Round 1 问题：仅 Walker Walk，无法泛化\n- 已知修改：扩展到 Walker Walk + Cheetah Run + 3 个 ManiSkill 任务（PickCube、StackCube、PegInsertionSide），Table cross_domain 已添加\n- **检查要点**：5 环境覆盖度是否足够？ManiSkill 结果（非 CIVO）对论文论点是积极还是消极贡献？跨环境结论的措辞是否准确？\n\n**3. R1-W1 [warning, in_progress]: Factorial design 混淆变量**\n- Round 1 问题：secondary comparisons 同时改变多个因素\n- 已知修改：论文应已标注 primary vs secondary comparisons\n- **检查要点**：是否在文中显式区分了 primary（008d vs 008f）和 secondary comparisons？2×2 factorial grid 是否完整？\n\n**4. R1-W2 / REV-2 [warning, in_progress]: 105K vs 505K 训练步数不对等**\n- Round 1 问题：treatment 仅 105K，baseline 505K，可能是速度差\n- 已知修改：baseline 4 seeds 到 505K，treatment extension exp_045 延长到 300K\n- **检查要点**：论文中是否讨论了步数不对等问题？是否有 treatment 长跑数据？结论是否仍然站得住脚？\n\n**5. R1-W3 [warning, open]: Pathway B 解释不充分**\n- Round 1 问题：仅 1 seed 证据\n- 已知修改：语言弱化为 \"preliminary evidence\"，现有 2 seeds\n- **检查要点**：2 seeds 是否改善了可信度？声明力度是否与证据匹配？\n\n**6. R2-W1 [warning, open]: TAWM 对比无实证**\n- Round 1 问题：仅 architectural reasoning\n- **检查要点**：论文是否改进了 TAWM 对比的论证？是否引用了 TAWM 原文数据？是否在 Limitations 中承认了这一局限？\n\n**7. R1-W4 [warning, resolved in R1]: RSSM signed reward error**\n- 已标记 resolved，验证 signed error 分析是否在论文中体现。\n\n---\n\n### 额外审查要点（不限于上述 issue）\n\n- 四级干预层级（gradient/output/representation/architecture）的实验设计是否严谨？结论是否过度泛化？\n- Dual-critic convergence 分析（ρ > 0.999）的方法论是否正确？\n- Online CIVO detector 的评估（TPR=5/5, FPR=2/9）是否有足够样本量？\n- 修改是否引入了新的方法论问题？\n\n### 输出格式\n\n1. 对每个 issue 给出 [RESOLVED] 或 [STILL_OPEN] + 理由\n2. 列出新发现的问题（如有）\n3. 给出方法严谨性评分（1-10）和简要总评"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "3",
    "text": "## Round 3 修订评估任务 — Reviewer 1（方法严谨性 + 实验充分性）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex`\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/submitted.pdf`\n**目标 Venue**: CoRL 2026 Main Conference\n**Deadline**: 2026-05-29\n**页数限制**: 8 页正文（References/Appendix 不计）\n**模板**: PMLR (`\\usepackage{corl_2026}`)\n**匿名规则**: Double-blind\n**审查侧重**: 方法严谨性、实验设计充分性、统计论证\n\n### 你的核心任务\n\n这是 Round 3 继续审稿。论文在 Round 1 后进行了大幅修改。你需要**逐条检查以下 open/in_progress issue**，标注 `[RESOLVED]` 或 `[STILL_OPEN]` + 理由：\n\n---\n\n### 必须逐条检查的 Issue（方法/实验类）\n\n**1. R1-N1 [critical, in_progress]: 统计检验力不足**\n- Round 1 问题：2-3 seeds 无法支撑 causal 声明\n- 已知修改：seeds 增至 4，语言从 \"causal factor\" 改为 \"strongest predictor\"，IQM + bootstrap CI 已添加\n- **检查要点**：4 seeds 是否足够？因果语言是否已充分弱化？IQM/CI 报告是否到位？论文现称 26/29 accuracy (AUROC=0.953, LOEO)——这些数字的统计意义如何？\n\n**2. R1-N4 [critical, in_progress]: 单环境局限**\n- Round 1 问题：仅 Walker Walk，无法泛化\n- 已知修改：扩展到 Walker Walk + Cheetah Run + 3 个 ManiSkill 任务（PickCube、StackCube、PegInsertionSide），Table cross_domain 已添加\n- **检查要点**：5 环境覆盖度是否足够？ManiSkill 结果（非 CIVO）对论文论点是积极还是消极贡献？跨环境结论的措辞是否准确？\n\n**3. R1-W1 [warning, in_progress]: Factorial design 混淆变量**\n- Round 1 问题：secondary comparisons 同时改变多个因素\n- 已知修改：论文应已标注 primary vs secondary comparisons\n- **检查要点**：是否在文中显式区分了 primary（008d vs 008f）和 secondary comparisons？2×2 factorial grid 是否完整？\n\n**4. R1-W2 / REV-2 [warning, in_progress]: 105K vs 505K 训练步数不对等**\n- Round 1 问题：treatment 仅 105K，baseline 505K，可能是速度差\n- 已知修改：baseline 4 seeds 到 505K，treatment extension exp_045 延长到 300K\n- **检查要点**：论文中是否讨论了步数不对等问题？是否有 treatment 长跑数据？结论是否仍然站得住脚？\n\n**5. R1-W3 [warning, open]: Pathway B 解释不充分**\n- Round 1 问题：仅 1 seed 证据\n- 已知修改：语言弱化为 \"preliminary evidence\"，现有 2 seeds\n- **检查要点**：2 seeds 是否改善了可信度？声明力度是否与证据匹配？\n\n**6. R2-W1 [warning, open]: TAWM 对比无实证**\n- Round 1 问题：仅 architectural reasoning\n- **检查要点**：论文是否改进了 TAWM 对比的论证？是否引用了 TAWM 原文数据？是否在 Limitations 中承认了这一局限？\n\n**7. R1-W4 [warning, resolved in R1]: RSSM signed reward error**\n- 已标记 resolved，验证 signed error 分析是否在论文中体现。\n\n---\n\n### 额外审查要点（不限于上述 issue）\n\n- 四级干预层级（gradient/output/representation/architecture）的实验设计是否严谨？结论是否过度泛化？\n- Dual-critic convergence 分析（ρ > 0.999）的方法论是否正确？\n- Online CIVO detector 的评估（TPR=5/5, FPR=2/9）是否有足够样本量？\n- 修改是否引入了新的方法论问题？\n\n### 输出格式\n\n1. 对每个 issue 给出 [RESOLVED] 或 [STILL_OPEN] + 理由\n2. 列出新发现的问题（如有）\n3. 给出方法严谨性评分（1-10）和简要总评"
  }
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-24T07:01:33.309293+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 29024
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-24T07:01:33.510371+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "3",
  "text": "## Round 3 修订评估任务 — Reviewer 2（Venue Fit + 贡献度 + 写作质量）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex`\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/submitted.pdf`\n**目标 Venue**: CoRL 2026 Main Conference\n**Deadline**: 2026-05-29\n**页数限制**: 8 页正文（References/Appendix 不计）\n**模板**: PMLR (`\\usepackage{corl_2026}`)\n**匿名规则**: Double-blind\n**附录规则**: 不计页数，reviewer 不必阅读\n**审查侧重**: CoRL venue fit、贡献度、写作质量、格式合规\n\n### CoRL 2026 CFP 要点（实时搜索确认）\n- 8 页正文 + unlimited appendix/refs\n- Limitations section 必须包含（计入 8 页）\n- 每位有 3+ 篇提交的作者必须同意审稿\n- PMLR 模板\n- Double-blind\n- Submissions should focus on core robotics problems\n\n### 你的核心任务\n\n这是 Round 3 继续审稿。论文在 Round 1 后进行了大幅修改。你需要**逐条检查以下 open/in_progress issue**，标注 `[RESOLVED]` 或 `[STILL_OPEN]` + 理由：\n\n---\n\n### 必须逐条检查的 Issue（Venue fit/贡献/写作类）\n\n**1. R1-N3 [critical, in_progress]: CoRL venue fit 不足**\n- Round 1 问题：全文无 robotics 实验/讨论，desk reject 风险\n- 已知修改：Abstract 加 robotics motivation，Intro 引用 DayDreamer/TD-MPC2，Discussion 加 \"Implications for robot learning\" 段落，ManiSkill 实验（PickCube/StackCube/PegInsertionSide）\n- **检查要点**：\n  - robotics framing 是否贯穿全文（不仅仅是开头结尾的点缀）？\n  - ManiSkill 实验是否足以满足 CoRL \"core robotics problem\" 要求？\n  - 论文的核心贡献是否与 robot learning 社区的关注点对齐？\n  - 是否还存在 desk reject 风险？\n\n**2. R2-N3 [critical, in_progress]: 纯诊断缺乏 actionable solution**\n- Round 1 问题：仅诊断问题不提供解决方案\n- 已知修改：Practitioner guidelines 段落，frozen embedding mitigation，四级干预层级，online detector\n- **检查要点**：\n  - 这些 actionable 贡献是否足够有分量？\n  - Practitioner guidelines 是否具体可操作？\n  - 对 CoRL 社区（偏重实际部署）来说，诊断+partial mitigation 的贡献模式是否可接受？\n\n**3. R2-W3 [warning, in_progress]: CIVO 与已知 value overestimation 区分不清**\n- Round 1 问题：CIVO 可能只是 compounding error 的实例\n- 已知修改：Related Work 增加显式对比，signed error 证据\n- **检查要点**：Related Work 和 Discussion 中 CIVO 与 compounding error、delusional bias 的区分是否清晰充分？\n\n**4. R2-W4 / R3-W3 [warning, in_progress]: Related Work 遗漏 + Bib 冗余**\n- Round 1 问题：Becker-Ehmck 2023、Park 2021、Wang 2024、Colas 2018 未引用；77 条 bib 仅 29 条被引用\n- 已知修改：清理 bib，引用遗漏文献\n- **检查要点**：这四篇文献是否已被引用？bib 是否已清理？是否有新的 orphan entries？\n\n**5. R3-W2 [warning, in_progress]: Abstract 过长缺 robotics motivation**\n- Round 1 问题：~180 词，缺 robotics\n- 已知修改：缩短 + 加 robotics motivation\n- **检查要点**：当前 Abstract 长度和内容是否合适？robotics motivation 是否到位？\"88.9% accuracy\" 是否已移除/修正？\n\n**6. R3-N1 [critical, resolved]: 未使用 PMLR 模板**\n- 验证是否使用 `\\usepackage{corl_2026}`。\n\n**7. R3-N3 [warning, resolved]: 正文超 8 页**\n- 验证当前正文是否在 8 页以内。\n\n---\n\n### 额外审查要点\n\n- 写作质量整体评估：clarity、organization、terminology consistency\n- 是否有残留的非匿名信息（代码链接、机构名）？\n- Limitations section 是否满足 CoRL 要求？\n- Contribution 列表是否与实际内容一致？\n- Title 是否准确反映论文内容（\"Can Fail\" vs 之前的 \"Fails\"）？\n- 修改是否引入了新的写作/framing 问题？\n\n### 输出格式\n\n1. 对每个 issue 给出 [RESOLVED] 或 [STILL_OPEN] + 理由\n2. 列出新发现的问题（如有）\n3. 给出 Venue Fit 评分（1-10）、贡献度评分（1-10）、写作质量评分（1-10）和简要总评"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "3",
    "text": "## Round 3 修订评估任务 — Reviewer 2（Venue Fit + 贡献度 + 写作质量）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex`\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/submitted.pdf`\n**目标 Venue**: CoRL 2026 Main Conference\n**Deadline**: 2026-05-29\n**页数限制**: 8 页正文（References/Appendix 不计）\n**模板**: PMLR (`\\usepackage{corl_2026}`)\n**匿名规则**: Double-blind\n**附录规则**: 不计页数，reviewer 不必阅读\n**审查侧重**: CoRL venue fit、贡献度、写作质量、格式合规\n\n### CoRL 2026 CFP 要点（实时搜索确认）\n- 8 页正文 + unlimited appendix/refs\n- Limitations section 必须包含（计入 8 页）\n- 每位有 3+ 篇提交的作者必须同意审稿\n- PMLR 模板\n- Double-blind\n- Submissions should focus on core robotics problems\n\n### 你的核心任务\n\n这是 Round 3 继续审稿。论文在 Round 1 后进行了大幅修改。你需要**逐条检查以下 open/in_progress issue**，标注 `[RESOLVED]` 或 `[STILL_OPEN]` + 理由：\n\n---\n\n### 必须逐条检查的 Issue（Venue fit/贡献/写作类）\n\n**1. R1-N3 [critical, in_progress]: CoRL venue fit 不足**\n- Round 1 问题：全文无 robotics 实验/讨论，desk reject 风险\n- 已知修改：Abstract 加 robotics motivation，Intro 引用 DayDreamer/TD-MPC2，Discussion 加 \"Implications for robot learning\" 段落，ManiSkill 实验（PickCube/StackCube/PegInsertionSide）\n- **检查要点**：\n  - robotics framing 是否贯穿全文（不仅仅是开头结尾的点缀）？\n  - ManiSkill 实验是否足以满足 CoRL \"core robotics problem\" 要求？\n  - 论文的核心贡献是否与 robot learning 社区的关注点对齐？\n  - 是否还存在 desk reject 风险？\n\n**2. R2-N3 [critical, in_progress]: 纯诊断缺乏 actionable solution**\n- Round 1 问题：仅诊断问题不提供解决方案\n- 已知修改：Practitioner guidelines 段落，frozen embedding mitigation，四级干预层级，online detector\n- **检查要点**：\n  - 这些 actionable 贡献是否足够有分量？\n  - Practitioner guidelines 是否具体可操作？\n  - 对 CoRL 社区（偏重实际部署）来说，诊断+partial mitigation 的贡献模式是否可接受？\n\n**3. R2-W3 [warning, in_progress]: CIVO 与已知 value overestimation 区分不清**\n- Round 1 问题：CIVO 可能只是 compounding error 的实例\n- 已知修改：Related Work 增加显式对比，signed error 证据\n- **检查要点**：Related Work 和 Discussion 中 CIVO 与 compounding error、delusional bias 的区分是否清晰充分？\n\n**4. R2-W4 / R3-W3 [warning, in_progress]: Related Work 遗漏 + Bib 冗余**\n- Round 1 问题：Becker-Ehmck 2023、Park 2021、Wang 2024、Colas 2018 未引用；77 条 bib 仅 29 条被引用\n- 已知修改：清理 bib，引用遗漏文献\n- **检查要点**：这四篇文献是否已被引用？bib 是否已清理？是否有新的 orphan entries？\n\n**5. R3-W2 [warning, in_progress]: Abstract 过长缺 robotics motivation**\n- Round 1 问题：~180 词，缺 robotics\n- 已知修改：缩短 + 加 robotics motivation\n- **检查要点**：当前 Abstract 长度和内容是否合适？robotics motivation 是否到位？\"88.9% accuracy\" 是否已移除/修正？\n\n**6. R3-N1 [critical, resolved]: 未使用 PMLR 模板**\n- 验证是否使用 `\\usepackage{corl_2026}`。\n\n**7. R3-N3 [warning, resolved]: 正文超 8 页**\n- 验证当前正文是否在 8 页以内。\n\n---\n\n### 额外审查要点\n\n- 写作质量整体评估：clarity、organization、terminology consistency\n- 是否有残留的非匿名信息（代码链接、机构名）？\n- Limitations section 是否满足 CoRL 要求？\n- Contribution 列表是否与实际内容一致？\n- Title 是否准确反映论文内容（\"Can Fail\" vs 之前的 \"Fails\"）？\n- 修改是否引入了新的写作/framing 问题？\n\n### 输出格式\n\n1. 对每个 issue 给出 [RESOLVED] 或 [STILL_OPEN] + 理由\n2. 列出新发现的问题（如有）\n3. 给出 Venue Fit 评分（1-10）、贡献度评分（1-10）、写作质量评分（1-10）和简要总评"
  }
}
```

</details>

---


### Tool call

_source line 229 · 2026-05-24T07:01:34.866758+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "review_chat_id": "oc_dd4a07a509df7e5f9a31d65f776059bc"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "review_chat_id": "oc_dd4a07a509df7e5f9a31d65f776059bc"
  }
}
```

</details>

---


### Tool result

_source line 230 · 2026-05-24T07:01:35.079204+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1568
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-24T07:01:36.796331+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 1929
}
```

</details>

---


### Assistant

_source line 232 · 2026-05-24T07:01:52.277921+00:00_

**Round 3 审稿已启动。** 编排如下：

| 角色 | 侧重 | 状态 |
|------|------|------|
| R1 | 方法严谨性 + 实验充分性 | 已派发，审稿中 |
| R2 | Venue fit + 贡献度 + 写作 | 已派发，审稿中 |
| 视觉审查 | PDF 排版质量 | 已派发（并行，不阻塞） |

**论文主要修改概览**（基于 issue tracker 对照）：
- 环境：Walker Walk → Walker + Cheetah + 3 ManiSkill（5 环境）
- Seeds：2-3 → 4 per key config，语言弱化为 "strongest predictor"
- NVE 验证：LOEO 交叉验证（mean AUROC 0.981）
- 干预：四级层级（gradient/output/repr/arch），dual-critic 2×2 factorial
- Robotics framing：Abstract/Intro/Discussion 全面添加
- 格式：已切换 PMLR 模板，bib 已清理

待 R1、R2 返回后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 16

## Round 16

2 recorded events


### User

_source line 233 · 2026-05-24T07:07:03.273283+00:00_

[Reviewer 2 审稿意见]:
## Round 3 修订评估 — Reviewer 2（Venue Fit / 贡献度 / 写作质量）

**论文**: "Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"

---

## 逐条 Issue 检查

### 1. R1-N3 [critical, in_progress]: CoRL venue fit 不足
**[STILL_OPEN]** — 改善明显但仍有结构性问题

**已改进**：
- Abstract 首句加入 "increasingly deployed for robot control" (Section 1, abstract_body.tex:1)
- Introduction 引用 DayDreamer [wu2023daydreamer] 和 TD-MPC2 [hansen2024tdmpc2]，提到 "Real robotic tasks demand temporal abstraction: manipulation requires fast reactive grasping alongside slow approach planning, locomotion involves gait phases at different frequencies, and sim-to-real transfer must handle dt mismatches between simulation and hardware" (Section 1, introduction.tex:4)
- 新增 ManiSkill 实验（PickCube-v1, StackCube-v1, PegInsertionSide-v1；Table 1, Section 4.3）
- Discussion 新增 "Implications for robot learning" 段落 (Section 5, analysis.tex:10-11)

**仍存在的问题**：
- **ManiSkill 结果反向证明了 CIVO 与 robotics manipulation 无关**：所有三个 ManiSkill 环境均未出现 dt-embedding-dependent CIVO（Section 4.3: "None of three ManiSkill environments exhibit dt-embedding-dependent CIVO"），frozen controls 表现相当甚至更高。这些结果实际上削弱了 robotics relevance——论文的核心发现（CIVO）仅在 DMC locomotion 中出现，而 locomotion 恰恰不是 CoRL 的核心关注点。
- **Robotics framing 仍是 "bookend" 式的**：robotics motivation 集中在 Introduction 的前两句和 Discussion 的一个段落，中间的方法和结果部分（Section 3-4，约 4 页）完全是通用 RL 分析，没有任何 robotics-specific 的实验设计考量（如 sim-to-real、sensor noise、actuation delay）。
- **核心贡献定位问题**：CoRL CFP 要求 "submissions should focus on core robotics problems"。本文的核心贡献是诊断 DreamerV3 中一个特定的 value overestimation 机制——这是一个通用 RL 问题，并非 robotics-specific 的。Limitations 部分自己也承认 "does not test...real-robot deployments"（conclusion.tex:7）。
- **Desk reject 风险已降低但未消除**：ManiSkill 实验的加入使论文不至于完全没有 robot-relevant 实验，但一位严格的 AC 可能会认为：(a) ManiSkill 结果为 negative（CIVO 不存在），(b) 核心实验仍在 DMC Walker/Cheetah 上完成，这些不是 "core robotics problems"。

**建议**：如果有时间，考虑在 Discussion 中更深入地讨论 CIVO 不出现在 manipulation 的原因（reward density 假说需要更多证据），以及这对 real-robot deployment（如 DayDreamer 式的 online learning）的具体指导意义。

---

### 2. R2-N3 [critical, in_progress]: 纯诊断缺乏 actionable solution
**[STILL_OPEN]** — 有改善但贡献模式仍偏弱

**已改进**：
- Practitioner guidelines 段落（Section 5, analysis.tex:7-8）：提供 NVE≥1.5× 诊断阈值（AUROC=0.953）、embedding freezing 作为缓解手段
- Table 2（intervention hierarchy）：系统展示四级干预的效果
- Online CIVO detector（Section 4.7）：TPR=5/5, FPR=2/9
- Contribution 列表明确标注 "Four-level intervention hierarchy" 和 "Online detection"

**仍存在的问题**：
- **核心结论仍是 negative**：Table 2 最终结论是 "No level reliably eliminates CIVO across environments"。最有效的 "solution" 是 embedding removed（5/5, 100%），即**不使用这个功能**——这等于说 temporal abstraction via dt-conditioning 在 imagination-based RL 中就是不可行的。
- **Frozen embedding 不是真正的解决方案**：71% prevention rate（5/7），且成功案例中 eval 仍然很差（如 015b: 204.2, 仅 22% baseline；042: 612.0 但只有单 seed）。这说明 freezing 既不能 reliably prevent CIVO，也不能恢复 baseline 性能。
- **Wide dual critic 部分有效**：75% prevention（3/4 Walker），但 Cheetah 0/1，跨环境 transfer 有限。
- **对 CoRL 社区的价值**：CoRL 偏重 deployable methods。"这个方法不行，我们可以告诉你什么时候它不行" 的贡献模式在 ML theory venue（ICML/NeurIPS）可能可以接受，但对 CoRL 来说显得不够 actionable。

**评估**：贡献模式从 "纯诊断" 升级为 "诊断 + partial mitigation + detection"，这是有进步的。但 actionable 部分的实际效果不强——practitioner 的最佳策略仍然是 "不要用 trained dt-embedding"。

---

### 3. R2-W3 [warning, in_progress]: CIVO 与已知 value overestimation 区分不清
**[RESOLVED]**

Related Work (related_work.tex:8) 提供了清晰的经验性区分：
- **控制实验证据**："if CIVO were generic compounding error, untrained dt-embeddings at dt=2 should also produce overestimation, yet they do not (NVE<0.6× for 008a/008c vs. 4.12× for 008d)"
- **Signed error 分析**："dt=2 rewards are underpredicted (mean SE=-0.599), ruling out observation-level overprediction and localizing CIVO to imagination-level prior drift"
- **与 delusional bias 的类比和区分**：明确指出 "analogous to delusional bias but model-induced rather than policy-class-induced"

区分充分、有数据支撑。

---

### 4. R2-W4 / R3-W3 [warning, in_progress]: Related Work 遗漏 + Bib 冗余
**[PARTIALLY RESOLVED]**

- **Park 2021** (park2021timediscretization): ✅ 已在 related_work.tex:5 引用
- **Wang 2024** (wang2024elastic): ✅ 已在 related_work.tex:5 引用
- **Colas 2018** (colas2018seeds): ✅ 已在 conclusion.tex:10 引用
- **Becker-Ehmck 2023**: ❌ **仍未引用**。在 references.bib 和所有 .tex 文件中均未找到。Becker-Ehmck et al. (2023) 关于 temporal abstraction in model-based RL 的工作与本文直接相关，应予引用。
- **Bib 清理**：从 Round 1 的 77 条减至 44 条，所有 44 条均被正文引用，无 orphan entries ✅

---

### 5. R3-W2 [warning, in_progress]: Abstract 过长缺 robotics motivation
**[RESOLVED]**

- Abstract 约 150 词，长度合理（CoRL 通常 150-200 词）
- 首句即包含 robotics motivation："World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales"
- "88.9% accuracy" 已移除，替换为更精确的 "26/29, AUROC=0.953, LOEO cross-validated"
- Keywords 合理：World Models, Temporal Abstraction, Value Overestimation, DreamerV3

---

### 6. R3-N1 [critical, resolved]: 未使用 PMLR 模板
**[RESOLVED]** — main.tex:5 确认 `\usepackage{corl_2026}` ✅

---

### 7. R3-N3 [warning, resolved]: 正文超 8 页
**[RESOLVED]** — PDF 确认正文 8 页（pages 1-8），References 从第 9 页开始，Appendix 从第 11 页开始 ✅

---

## 额外审查发现

### 写作质量评估

**优点**：
- 论文结构清晰：Introduction → Related Work → Experimental Setup → Results (F1-F7) → Discussion → Conclusion，逻辑链条完整
- Factorial design 的表述专业严谨
- Table 1 和 Table 2 信息密度高且组织良好
- Contribution 列表与正文内容一致

**问题**：
- **E1** [minor] Abstract 统计数据过密：在约 150 词内包含了 "14-19%", "26/29", "AUROC=0.953", "2.78×", "ρ > 0.999", "100% sensitivity" 等 6 个以上数字指标。建议精简到 2-3 个关键数字，其余放入正文。
- **E2** [minor] Section 标题混用：Section 4 (Results) 用 "F1", "F2", "F3-F5", "F6-F7" 编号，而 Section 5 (Discussion) 和其他 section 用标准编号。这种双编号系统可能让读者困惑。
- **E3** [minor] Conclusion 中 Limitations 部分的 `\label{sec:limitations}` 放在段落末尾（conclusion.tex:12），如果 CoRL 要求 Limitations 作为独立 section，当前作为 Conclusion 的 paragraph 是否满足格式要求需确认。

### 匿名合规
- 作者："Anonymous Authors" ✅
- 代码链接："Code: upon acceptance" ✅
- DreamerV3 仓库链接（methodology.tex:58 脚注）：`https://github.com/danijar/dreamerv3` 是公开的官方仓库，非作者代码，不破坏 double-blind ✅
- 未发现机构名称或自引泄露 ✅

### Contribution 列表一致性
四项 contribution（Failure mode identification, Architectural boundary, Four-level intervention hierarchy, Online detection）与正文内容一致 ✅

### Title 准确性
"Can Fail" 比之前的 "Fails" 更准确——论文发现 CIVO 是条件性的（需要 trained embedding + multi-rate exposure），且仅在 locomotion 中出现，manipulation 不受影响。Title 准确反映内容 ✅

### 潜在新问题
- **N1** [warning] **ManiSkill 实验的 baseline 缺失**：Table 1 中 ManiSkill 任务（019b, 049, 050）没有给出 vanilla DreamerV3 baseline 的 eval 值，只有脚注 c 提到 "NVE normalized against exp_019a_v2 (vanilla DreamerV3 on PickCube-v1)"。读者无法直接判断这些任务上 variable-rate 配置的相对性能。
- **N2** [warning] **Cheetah Run baseline 同样缺失**：Table 1 中 Cheetah Run 只有 trained (010b) 和 frozen (046) 的结果，没有 standard baseline 的 eval 值供参照。
- **N3** [minor] **统计功效限制**：论文自己承认 "Statistical power with 4 seeds per configuration is limited"（conclusion.tex:10），部分配置只有 1-2 seeds（如 TCN σ=0.1 和 σ=1.0 各只有 1 seed）。Table 2 中一些 100% prevention rate 的条目（TCN σ=0.1: 1/1, TCN σ=1.0: 1/1）在统计上完全无意义。

---

## 评分

### Venue Fit: 5/10
论文与 CoRL 的核心要求（"focus on core robotics problems"）之间存在结构性 gap。Robotics framing 主要是 opening/closing 的修辞包装，核心实验在 DMC locomotion 上完成。ManiSkill 实验虽然增加了 robotics 相关性，但 negative results（CIVO 不出现）反而削弱了论文对 robotics 社区的直接价值。论文更适合 ICML/NeurIPS 的 RL/world-model track。

### 贡献度: 6/10
- 优势：CIVO 的诊断和因果分离做得扎实（factorial design + AUROC + LOEO），architectural boundary（MPC vs imagination-based bootstrapping）的发现有洞见
- 劣势：核心贡献是 negative result（temporal abstraction 在 imagination-based RL 中不可行），且没有找到可靠的解决方案。Practitioner guidelines 的实际建议是 "不要用"。对 CoRL 的 deployment-oriented 社区来说价值有限。

### 写作质量: 7/10
- 论文结构清晰、专业
- Factorial design 的展示严谨
- Abstract 过于数字密集
- F1-F7 编号系统增加认知负担
- 总体可读性良好

### 总体评估
论文在 Round 1 基础上做了实质性改进：ManiSkill 实验、practitioner guidelines、bib 清理、CIVO-compounding error 区分、PMLR 模板、页数控制。但两个 critical issue（venue fit 和 actionable contribution）的核心矛盾未解决：
1. CIVO 是 locomotion-specific 的发现，robotics framing 仍是装饰性的
2. 最有效的 "solution" 是不用该功能，这对需要 temporal abstraction 的 robotics 应用帮助有限

如果提交到 ICML/NeurIPS 作为 diagnostic/negative-result contribution，评分会明显更高。对 CoRL 来说，论文处于 borderline 区域。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 234 · 2026-05-24T07:07:19.157236+00:00_

Reviewer 2 审稿已收到。关键发现：

- **R1-N3 (venue fit)**: STILL_OPEN — ManiSkill negative results 反而削弱 robotics relevance
- **R2-N3 (actionable)**: STILL_OPEN — 最佳建议仍是"不要用"
- **R2-W3 (CIVO 区分)**: RESOLVED
- **R2-W4 (refs/bib)**: PARTIALLY RESOLVED — Becker-Ehmck 2023 仍未引用
- **R3-W2/N1/N3**: 均 RESOLVED
- 新发现：N1 ManiSkill baseline 缺失、N2 Cheetah baseline 缺失、N3 单 seed 统计无意义

等待 Reviewer 1 返回后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 17

## Round 17

2 recorded events


### User

_source line 235 · 2026-05-24T07:07:29.699620+00:00_

[Reviewer 2 审稿结果]:
Round 3 审稿意见已提交给 Review Director。

**总结**：

7 个 issue 中：
- **3 个 RESOLVED**：CIVO vs compounding error 区分（R2-W3）、Abstract 长度/robotics（R3-W2）、PMLR 模板（R3-N1）、页数（R3-N3）
- **1 个 PARTIALLY RESOLVED**：Related Work/Bib（R2-W4/R3-W3）— Becker-Ehmck 2023 仍未引用
- **2 个 STILL_OPEN**：CoRL venue fit（R1-N3）和 actionable solution（R2-N3）— 这两个是结构性问题

**评分**：Venue Fit 5/10、贡献度 6/10、写作质量 7/10。论文做了实质性改进但核心矛盾未解：CIVO 是 locomotion-specific 的 negative result，robotics framing 仍是装饰性的，最佳 "solution" 是不用该功能。更适合 ICML/NeurIPS。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 236 · 2026-05-24T07:07:39.746256+00:00_

Reviewer 2 审稿收到。等待 Reviewer 1 返回后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 18

## Round 18

6 recorded events


### User

_source line 237 · 2026-05-24T07:11:56.519996+00:00_

[Reviewer 1 审稿意见]:

# Round 3 审稿报告 — Reviewer 1（方法严谨性 + 实验充分性）

**论文**: "Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
**目标 Venue**: CoRL 2026

---

## 总体评分

**方法严谨性**: 7/10
**一句话总结**: 论文在 Round 1 后有实质性改进——统计语言适度弱化、LOEO 交叉验证增加了可信度、五环境扩展提供了 discriminative validity——但 CIVO 仅在 2 个运动任务中复现、训练步数不对等未显式讨论、TAWM 对比仍无实证，这些残留问题将方法严谨性限制在"solid but not exceptional"层面。

## 官方维度打分（基于 CoRL review form: Originality / Quality / Clarity / Significance / Relevance / Limitations）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Originality | 4/5 | 首个系统性诊断 DreamerV3 变速想象失败模式的工作；CIVO 现象的识别和四级干预层级分析均为新贡献 |
| Quality | 3/5 | Factorial design 严谨、LOEO 验证有力，但 CIVO 仅在 2/5 环境复现、per-intervention 样本量小（2-7 seeds）、detector 仅 5 个正例 |
| Clarity | 4/5 | 写作清晰、F1-F7 结构化叙事好；primary/secondary comparison 标注明确；33 页 appendix 非常详尽 |
| Significance | 3/5 | 对想象式 RL 社区有价值的 negative result，但 locomotion-specific 的结论限制了 impact |
| Relevance | 4/5 | 直接关联 robot control 中的 world-model RL；temporal abstraction 是 CoRL 核心话题 |
| Limitations | 4/5 | Limitations section 诚实全面（承认 4 seeds 局限、architecture 局限、reward scale 局限），ManiSkill non-CIVO 结果如实报告 |

---

## 逐条 Issue 检查

### 1. R1-N1 [critical, in_progress]: 统计检验力不足
**[RESOLVED]**

改进清单：
- Seeds 从 2-3 增至 4（关键配置），Section 4.2 报告 IQM 175.2, mean 170.6, n=4（citing Agarwal et al. 2021）
- 因果语言全面弱化：Abstract 和 Conclusion 统一使用 "strongest predictor" 而非 "causal factor"
- NVE 阈值验证：26/29 accuracy, AUROC=0.953 (in-sample), LOEO cross-validated mean AUROC=0.981（Appendix Table B.4）
- Bootstrap CI：ROC 曲线配 95% bootstrap CI (10,000 resamples)（Appendix Figure 3）
- Limitations 显式承认："Statistical power with 4 seeds per configuration is limited; the NVE threshold (LOEO AUROC=0.981) may require recalibration for different reward scales"

**残留小问题**: Abstract 仍用 "isolate" 一词（"Factorial diagnostics...isolate trained temporal embedding"），该词携带近因果含义。建议改为 "identify...as the strongest predictor" 以保持全文一致。但这不影响接收决定。

---

### 2. R1-N4 [critical, in_progress]: 单环境局限
**[RESOLVED]，附重要说明**

改进：
- 从 1 环境扩展到 5 环境：Walker Walk（primary factorial）、Cheetah Run（severity probe, NVE 8-70×）、PickCube-v1、StackCube-v1、PegInsertionSide-v1
- ManiSkill 结果诚实报告为 non-CIVO：frozen control 匹配 trained spikes（StackCube frozen 4.30× vs trained 5.05×），PegInsertion seed-dependent ordering
- Cross-domain Table 1 + Appendix Table 4 提供完整跨环境数据

**重要说明**: CIVO 被证实为 locomotion-specific（仅 Walker Walk + Cheetah Run），ManiSkill 3 个任务均未展现 dt-embedding-dependent CIVO。论文诚实地陈述了这一点（Section 4.3: "CIVO is locomotion-specific in DreamerV3"），且 ManiSkill 结果提供了重要的 discriminative validity（NVE 诊断能正确区分 CIVO 与环境特异性 transient）。

标题使用 "Can Fail" 的措辞是恰当的。但论文应更突出讨论**为什么**运动任务触发 CIVO 而操作任务不触发——当前解释仅在 Appendix D.3 中简要提及 "representational capacity already partially consumed when CIVO injects"，不够深入。

---

### 3. R1-W1 [warning, in_progress]: Factorial design 混淆变量
**[RESOLVED]**

- Section 4.2 明确标注 primary comparison（008d vs 008f，仅 embedding 因素不同）vs secondary comparisons（008a/008c 同时改变 subsample 和 horizon）
- 2×2 factorial grid 隐式完整：{trained, no-emb} × {sub-ON, sub-OFF} = {008d(CIVO), 008a(healthy), 008f(healthy), 001(healthy)}，仅 (trained, sub-ON) 单元触发 CIVO
- 论文正确推断 "jointly sufficient in tested configurations"

---

### 4. R1-W2 / REV-2 [warning, in_progress]: 105K vs 505K 训练步数不对等
**[STILL_OPEN]**

**已改善之处**:
- Table 1 报告 baseline 在 105K 时的 eval（915.7），与 treatment 在相同训练步数比较——这确保了 matched-timestep comparison
- 1/4 Walker seeds 展示 self-correction（29.3% of baseline by 105K）

**仍然存在的问题**:
1. 论文**未显式讨论**步数不对等问题。Section 3.8 仅说 "treatments run for 105K steps, sufficient to observe collapse onset"，但未论证**为什么** 105K 足够——尤其当 1/4 seeds 展示 self-correction trajectory 时
2. Director 提到的 exp_045 延长到 300K 的 treatment 数据**未在正文中呈现**或讨论。如果存在这样的数据，应至少在 Appendix 中报告 treatment 长跑结果
3. Cheetah Run frozen (046) 运行到 215K，PickCube 到 200K——说明作者有能力运行更长实验。为什么 Walker 的 treatment 不延长？
4. Figure 5 (Appendix C.2) 显示 performance 随 dt 单调下降，但 x 轴止于 105K。如果 self-correction 在更长时间窗口内更普遍，则 "all variable-rate configurations degrade" (F1) 可能过强

**建议**: 在 Discussion 或 Appendix 中增加一段明确说明：(a) comparison 在 matched 105K 步数进行；(b) 已知 1/4 seeds self-correct 但 3/4 不在 105K 内恢复；(c) 如有 exp_045 长跑数据，报告之。

---

### 5. R1-W3 [warning, open]: Pathway B 解释不充分
**[RESOLVED]**

- 证据从 1 seed 增至 2 seeds
- Section 4.6 措辞为 "preliminary Pathway B (entropy increase, nve = 3.78×; 2 seeds only, requires confirmation)"
- "requires confirmation" 的声明力度与 2 seeds 的证据量匹配
- Appendix D.6 提供了 Pathway B 的 entropy dynamics 对比（Figure 10）

---

### 6. R2-W1 [warning, open]: TAWM 对比无实证
**[STILL_OPEN]**

- 论文的 MPC vs imagination-based 论证仍为纯架构/理论分析：Section 5 ("The feedback architecture—MPC re-planning versus imagination-based bootstrapping—is the structural factor") 和 Conclusion 重复此 claim
- **无实证数据**对比 TAWM、TD-MPC2 或其他 MPC 方法在相同环境下的表现
- Limitations 承认 "whether CIVO manifests in other imagination-based architectures (e.g., IRIS or latent-space planners beyond TD-MPC2) remains open"，但这仅覆盖了其他 imagination-based 方法，未覆盖 MPC 方法的实证
- Related Work (Section 2) 引用了 TD-MPC2 [11] 和 MBPO [27]，但仅做 architectural reasoning

**严谨性影响**: "feedback architecture as the structural factor" 这一核心论断无实验支撑。论文声称 MPC re-planning 避免了 CIVO 是基于推理而非数据。这是一个合理的假说，但不应作为 "the structural factor" 呈现。

**建议**: (a) 弱化措辞为 "hypothesized structural factor" 或 "we conjecture that feedback architecture is the key differentiator"；或 (b) 在 at least 1 MPC baseline (e.g., vanilla TD-MPC2 with dt-conditioning) 上验证无 CIVO。

---

### 7. R1-W4 [warning, resolved in R1]: RSSM signed reward error
**[RESOLVED]**

- Appendix D.1 / Table 15 提供完整的 signed reward error 分析
- 结论：trained-embedding model 在 dt=2 时**低估**奖励（mean signed error = -0.150, 仅 8% 样本过预测），排除了 observation-level reward overprediction 作为 CIVO 机制
- 方法学正确：在 posterior-conditioned RSSM predictions 上计算，isolate 了 reward head 的 prediction bias

---

## 新发现的问题

### N-new-1 [warning]: Online CIVO Detector 评估样本量不足
- **位置**: Section 4.7, Appendix F
- **问题**: Detector 在 n=14 runs 上评估，仅 5 个正例（TPR=5/5）。任何单个漏检就会将 TPR 降至 80%。FPR=2/9 (22%) 意味着近 1/4 的非 CIVO 配置被误报。论文称 "achieves 100% sensitivity" 在 n=5 的基础上统计意义有限
- **与 NVE 分类的区别**: NVE 阈值分类用了 n=29 configs（AUROC=0.953），这是合理的。但 online detector 的 streaming 评估仅 14 runs，应与 NVE 静态分类的统计效力区分讨论
- **建议**: 承认 detector 评估的 small-sample limitation，或在更多配置上运行 retrospective 验证

### N-new-2 [minor]: IQM 报告不完整
- **位置**: Section 4.2
- **问题**: 仅对一个配置报告 IQM (175.2, n=4)。既然 cite Agarwal et al. 2021 作为统计最佳实践，其他关键 comparison（如 008f control, frozen variants, Cheetah runs）也应报告 IQM + stratified bootstrap CI
- **影响**: 不影响接收决定，但如果声称遵循 Agarwal et al. best practices，应更一致地应用

### N-new-3 [minor]: Dual-critic convergence 的因果推理存在跳跃
- **位置**: Section 4.8
- **问题**: 论文从 ρ > 0.999 推导出 "rendering Double Q pessimism ineffective"。逻辑链是：identical training data → critic convergence → no pessimism gap → min operation ineffective。但 ρ > 0.999 是在 converged critics 上测量的——early training 时 critics 可能有差异。论文在 Appendix G 分析了 recovery mechanism（"min operation reduces both peak CIVO severity"），说明 min 操作确实在某些 seed 有效（3/4 wide dual-critic CIVO prevention）。这与 "pessimism ineffective" 的叙事有张力
- **论文部分地址了这个问题**: Appendix G.3 区分了 recovery（min-dominated）和 prevention（min + capacity synergy），并承认 "the mechanism for this synergy is an open question"。但主文 Section 4.8 的 framing 过于简化
- **建议**: 在主文中 nuance：ρ > 0.999 convergence 是 asymptotic 结果；early training 时的 brief divergence 可能足以让 min operation 发挥作用，这解释了 wide dual-critic 的部分成功

---

## Must-Fix 问题（影响接收决定）

无新增 critical 问题。Round 1 的两个 critical issues (N1, N4) 均已实质性解决。

---

## Should-Fix 问题（影响评分但不一票否决）

**S1**: 训练步数不对等未显式讨论（R1-W2, [STILL_OPEN]）——论文应在正文中明确说明 matched-timestep comparison 和 self-correction 现象

**S2**: TAWM/MPC 对比仍无实证（R2-W1, [STILL_OPEN]）——"the structural factor" 措辞应弱化或增加实验验证

**S3**: Online detector 评估的 small-sample limitation 应被承认（N-new-1）

---

## 小问题（不影响接收）

- Abstract 中 "isolate" 应改为 "identify...as" 以与全文 "strongest predictor" 措辞一致
- IQM 报告应更一致地应用于多个关键配置（N-new-2）
- Dual-critic convergence 的主文叙事应增加 nuance 关于 early-training divergence（N-new-3）

---

## 主要优势

1. **Factorial design 系统且严谨**: 43 配置 × 4 seeds × 5 环境的设计空间覆盖广泛；primary/secondary comparison 标注清晰
2. **LOEO 交叉验证显著增强统计可信度**: AUROC=0.953 (in-sample), 0.981 (LOEO) 在 29 配置上表现出色
3. **四级干预层级分析**（gradient/output/repr/arch）提供了系统性的 negative result，对社区有长期价值
4. **ManiSkill non-CIVO 结果增加了 discriminative validity**: NVE 诊断能正确区分 dt-embedding-dependent CIVO 与环境特异性 transient
5. **Dual-critic convergence (ρ > 0.999)** 是关于 imagination-based training 的有价值的 structural insight
6. **Limitations section 诚实全面**: 主动承认 4-seed 局限、architecture 局限、ManiSkill locomotion-specificity

---

## Issue 状态汇总

| Issue | 状态 | 理由 |
|-------|------|------|
| R1-N1 统计检验力 | [RESOLVED] | 4 seeds, "strongest predictor" 语言, LOEO AUROC=0.981, IQM 报告 |
| R1-N4 单环境 | [RESOLVED] | 5 环境, CIVO locomotion-specificity 诚实报告, discriminative validity |
| R1-W1 Factorial 混淆 | [RESOLVED] | Primary vs secondary 明确标注, 2×2 grid 完整 |
| R1-W2 步数不对等 | [STILL_OPEN] | Matched-timestep 比较存在但未显式讨论; 缺少 treatment 长跑数据 |
| R1-W3 Pathway B | [RESOLVED] | 2 seeds + "preliminary/requires confirmation" 措辞 |
| R2-W1 TAWM 对比 | [STILL_OPEN] | 仍为纯 architectural reasoning, "structural factor" 措辞过强 |
| R1-W4 Signed error | [RESOLVED] | Appendix D.1 / Table 15 完整呈现 |

**5/7 issues resolved, 2/7 still open (均为 warning 级别，非 critical)**

---

## 方法严谨性总评

**评分: 7/10**

论文在 Round 1 后取得了显著进步。核心 factorial design 严谨，LOEO 交叉验证有效提升了统计论证质量，五环境扩展提供了正面和反面证据。两个残留 warning 级问题（步数不对等讨论不足 + TAWM 对比缺实证）不构成 fatal flaw，但将方法论评分限制在 7 而非 8。

作为 diagnostic/negative-result paper，这是一个 solid 的工作——它不需要解决 CIVO，只需正确识别和表征它。论文在这方面做得好。主要限制是 CIVO 的 locomotion-specificity 收窄了 impact，以及 "structural factor" 论断缺乏跨架构实验验证。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-24T07:12:52.314757+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "3",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的意见\n\n以下是 Reviewer 2（Venue Fit / 贡献度 / 写作质量）的完整审稿意见。请对每个要点标注 `[AGREE]`（同意并说明理由）或 `[REBUT]`（反驳并引用论文具体 Section/Table/Figure 作为证据）。\n\n---\n\n**Reviewer 2 完整审稿意见：**\n\n### 1. R1-N3 [STILL_OPEN]: CoRL venue fit 不足\nR2 认为改善明显但有结构性问题：\n- ManiSkill 结果**反向证明** CIVO 与 robotics manipulation 无关（所有 3 个 ManiSkill 环境均未出现 dt-embedding-dependent CIVO）\n- Robotics framing 是 \"bookend\" 式的（集中在 Intro 前两句和 Discussion 一段，中间 4 页纯 RL 分析）\n- CoRL CFP 要求 \"focus on core robotics problems\"，CIVO 是通用 RL 问题\n- Desk reject 风险降低但未消除\n- **评分：Venue Fit 5/10**\n\n### 2. R2-N3 [STILL_OPEN]: 纯诊断缺乏 actionable solution\nR2 认为有改善但贡献模式偏弱：\n- Table 2 核心结论仍是 \"No level reliably eliminates CIVO across environments\"\n- 最有效 \"solution\" 是 embedding removed (100%) = 不使用该功能\n- Frozen embedding 71% prevention rate 但 eval 仍差\n- Wide dual critic 75% Walker 但 Cheetah 0/1\n- 对 CoRL deployment-oriented 社区价值有限\n- **评分：贡献度 6/10**\n\n### 3. R2-W3 [RESOLVED]: CIVO 与 compounding error 区分\nR2 认为 Related Work 提供了清晰的经验性区分，数据支撑充分。\n\n### 4. R2-W4/R3-W3 [PARTIALLY RESOLVED]: Related Work/Bib\nR2 发现 Becker-Ehmck 2023 仍未引用。其他 3 篇（Park, Wang, Colas）已引用。Bib 从 77 条清理至 44 条。\n\n### 5. R3-W2 [RESOLVED]: Abstract 过长缺 robotics\nR2 确认约 150 词，robotics motivation 到位，88.9% accuracy 已替换。\n\n### 6-7. R3-N1, R3-N3 [RESOLVED]: 模板和页数。\n\n### R2 额外发现：\n- **E1** [minor]: Abstract 统计数据过密（6+ 数字指标）\n- **E2** [minor]: Section 标题 F1-F7 与标准编号混用\n- **E3** [minor]: Limitations 作为 Conclusion paragraph 是否满足 CoRL 要求\n- **N1** [warning]: ManiSkill 实验的 baseline eval 值缺失\n- **N2** [warning]: Cheetah Run baseline 同样缺失\n- **N3** [minor]: Table 2 中 1-seed 条目（TCN σ=0.1, σ=1.0）统计无意义\n\n### R2 总评：\n- Venue Fit 5/10, 贡献度 6/10, 写作质量 7/10\n- 论文更适合 ICML/NeurIPS\n- 核心矛盾：CIVO 是 locomotion-specific negative result，robotics framing 装饰性"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "3",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的意见\n\n以下是 Reviewer 2（Venue Fit / 贡献度 / 写作质量）的完整审稿意见。请对每个要点标注 `[AGREE]`（同意并说明理由）或 `[REBUT]`（反驳并引用论文具体 Section/Table/Figure 作为证据）。\n\n---\n\n**Reviewer 2 完整审稿意见：**\n\n### 1. R1-N3 [STILL_OPEN]: CoRL venue fit 不足\nR2 认为改善明显但有结构性问题：\n- ManiSkill 结果**反向证明** CIVO 与 robotics manipulation 无关（所有 3 个 ManiSkill 环境均未出现 dt-embedding-dependent CIVO）\n- Robotics framing 是 \"bookend\" 式的（集中在 Intro 前两句和 Discussion 一段，中间 4 页纯 RL 分析）\n- CoRL CFP 要求 \"focus on core robotics problems\"，CIVO 是通用 RL 问题\n- Desk reject 风险降低但未消除\n- **评分：Venue Fit 5/10**\n\n### 2. R2-N3 [STILL_OPEN]: 纯诊断缺乏 actionable solution\nR2 认为有改善但贡献模式偏弱：\n- Table 2 核心结论仍是 \"No level reliably eliminates CIVO across environments\"\n- 最有效 \"solution\" 是 embedding removed (100%) = 不使用该功能\n- Frozen embedding 71% prevention rate 但 eval 仍差\n- Wide dual critic 75% Walker 但 Cheetah 0/1\n- 对 CoRL deployment-oriented 社区价值有限\n- **评分：贡献度 6/10**\n\n### 3. R2-W3 [RESOLVED]: CIVO 与 compounding error 区分\nR2 认为 Related Work 提供了清晰的经验性区分，数据支撑充分。\n\n### 4. R2-W4/R3-W3 [PARTIALLY RESOLVED]: Related Work/Bib\nR2 发现 Becker-Ehmck 2023 仍未引用。其他 3 篇（Park, Wang, Colas）已引用。Bib 从 77 条清理至 44 条。\n\n### 5. R3-W2 [RESOLVED]: Abstract 过长缺 robotics\nR2 确认约 150 词，robotics motivation 到位，88.9% accuracy 已替换。\n\n### 6-7. R3-N1, R3-N3 [RESOLVED]: 模板和页数。\n\n### R2 额外发现：\n- **E1** [minor]: Abstract 统计数据过密（6+ 数字指标）\n- **E2** [minor]: Section 标题 F1-F7 与标准编号混用\n- **E3** [minor]: Limitations 作为 Conclusion paragraph 是否满足 CoRL 要求\n- **N1** [warning]: ManiSkill 实验的 baseline eval 值缺失\n- **N2** [warning]: Cheetah Run baseline 同样缺失\n- **N3** [minor]: Table 2 中 1-seed 条目（TCN σ=0.1, σ=1.0）统计无意义\n\n### R2 总评：\n- Venue Fit 5/10, 贡献度 6/10, 写作质量 7/10\n- 论文更适合 ICML/NeurIPS\n- 核心矛盾：CIVO 是 locomotion-specific negative result，robotics framing 装饰性"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-24T07:12:57.445016+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 5130
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-24T07:12:57.597028+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "3",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的意见\n\n以下是 Reviewer 1（方法严谨性 + 实验充分性）的完整审稿意见。请对每个要点标注 `[AGREE]`（同意并说明理由）或 `[REBUT]`（反驳并引用论文具体 Section/Table/Figure 作为证据）。\n\n---\n\n**Reviewer 1 完整审稿意见：**\n\n### Issue 状态判定：\n| Issue | R1 判定 | 理由 |\n|-------|---------|------|\n| R1-N1 统计检验力 | [RESOLVED] | 4 seeds, \"strongest predictor\", LOEO AUROC=0.981, IQM |\n| R1-N4 单环境 | [RESOLVED] | 5 环境, discriminative validity, locomotion-specificity 诚实报告 |\n| R1-W1 Factorial 混淆 | [RESOLVED] | Primary vs secondary 标注, 2×2 grid 完整 |\n| R1-W2 步数不对等 | [STILL_OPEN] | Matched-timestep 比较存在但未显式讨论; 缺少 treatment 长跑数据; exp_045 未在正文呈现 |\n| R1-W3 Pathway B | [RESOLVED] | 2 seeds + \"preliminary/requires confirmation\" |\n| R2-W1 TAWM 对比 | [STILL_OPEN] | 仍为纯 architectural reasoning, \"structural factor\" 措辞过强 |\n| R1-W4 Signed error | [RESOLVED] | Appendix 完整呈现 |\n\n### R1 评分：方法严谨性 7/10\n\n### R1 的 CoRL 维度打分：\nOriginality 4/5, Quality 3/5, Clarity 4/5, Significance 3/5, Relevance 4/5, Limitations 4/5\n\n### R1 新发现的问题：\n\n**N-new-1 [warning]: Online CIVO Detector 评估样本量不足**\n- n=14 runs, 仅 5 正例, TPR=5/5 但统计意义有限\n- FPR=2/9 (22%) 意味着近 1/4 非 CIVO 被误报\n- 应与 NVE 静态分类（n=29）区分讨论\n\n**N-new-2 [minor]: IQM 报告不完整**\n- 仅对一个配置报告 IQM (175.2, n=4)\n- 其他关键 comparison 也应报告 IQM + stratified bootstrap CI\n\n**N-new-3 [minor]: Dual-critic convergence 因果推理跳跃**\n- ρ > 0.999 是 asymptotic 结果，early training 可能有差异\n- 与 wide dual-critic 3/4 prevention 成功存在张力\n- 主文 \"pessimism ineffective\" 叙事过于简化\n\n### R1 主要优势总结：\n1. Factorial design 系统严谨（43 配置 × 4 seeds × 5 环境）\n2. LOEO 交叉验证（AUROC=0.981）\n3. 四级干预层级分析的长期社区价值\n4. ManiSkill non-CIVO 增加 discriminative validity\n5. Dual-critic convergence 的 structural insight\n6. Limitations section 诚实全面\n\n### R1 Should-Fix：\n- S1: 步数不对等应在正文显式讨论\n- S2: TAWM \"structural factor\" 应弱化或增加实验\n- S3: Online detector small-sample limitation 应承认\n\n### R1 总评：\n5/7 issues resolved, 2/7 still open（均 warning 级别）。作为 diagnostic/negative-result paper 是 solid work，主要限制是 locomotion-specificity 和 \"structural factor\" 缺实验验证。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "3",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的意见\n\n以下是 Reviewer 1（方法严谨性 + 实验充分性）的完整审稿意见。请对每个要点标注 `[AGREE]`（同意并说明理由）或 `[REBUT]`（反驳并引用论文具体 Section/Table/Figure 作为证据）。\n\n---\n\n**Reviewer 1 完整审稿意见：**\n\n### Issue 状态判定：\n| Issue | R1 判定 | 理由 |\n|-------|---------|------|\n| R1-N1 统计检验力 | [RESOLVED] | 4 seeds, \"strongest predictor\", LOEO AUROC=0.981, IQM |\n| R1-N4 单环境 | [RESOLVED] | 5 环境, discriminative validity, locomotion-specificity 诚实报告 |\n| R1-W1 Factorial 混淆 | [RESOLVED] | Primary vs secondary 标注, 2×2 grid 完整 |\n| R1-W2 步数不对等 | [STILL_OPEN] | Matched-timestep 比较存在但未显式讨论; 缺少 treatment 长跑数据; exp_045 未在正文呈现 |\n| R1-W3 Pathway B | [RESOLVED] | 2 seeds + \"preliminary/requires confirmation\" |\n| R2-W1 TAWM 对比 | [STILL_OPEN] | 仍为纯 architectural reasoning, \"structural factor\" 措辞过强 |\n| R1-W4 Signed error | [RESOLVED] | Appendix 完整呈现 |\n\n### R1 评分：方法严谨性 7/10\n\n### R1 的 CoRL 维度打分：\nOriginality 4/5, Quality 3/5, Clarity 4/5, Significance 3/5, Relevance 4/5, Limitations 4/5\n\n### R1 新发现的问题：\n\n**N-new-1 [warning]: Online CIVO Detector 评估样本量不足**\n- n=14 runs, 仅 5 正例, TPR=5/5 但统计意义有限\n- FPR=2/9 (22%) 意味着近 1/4 非 CIVO 被误报\n- 应与 NVE 静态分类（n=29）区分讨论\n\n**N-new-2 [minor]: IQM 报告不完整**\n- 仅对一个配置报告 IQM (175.2, n=4)\n- 其他关键 comparison 也应报告 IQM + stratified bootstrap CI\n\n**N-new-3 [minor]: Dual-critic convergence 因果推理跳跃**\n- ρ > 0.999 是 asymptotic 结果，early training 可能有差异\n- 与 wide dual-critic 3/4 prevention 成功存在张力\n- 主文 \"pessimism ineffective\" 叙事过于简化\n\n### R1 主要优势总结：\n1. Factorial design 系统严谨（43 配置 × 4 seeds × 5 环境）\n2. LOEO 交叉验证（AUROC=0.981）\n3. 四级干预层级分析的长期社区价值\n4. ManiSkill non-CIVO 增加 discriminative validity\n5. Dual-critic convergence 的 structural insight\n6. Limitations section 诚实全面\n\n### R1 Should-Fix：\n- S1: 步数不对等应在正文显式讨论\n- S2: TAWM \"structural factor\" 应弱化或增加实验\n- S3: Online detector small-sample limitation 应承认\n\n### R1 总评：\n5/7 issues resolved, 2/7 still open（均 warning 级别）。作为 diagnostic/negative-result paper 是 solid work，主要限制是 locomotion-specificity 和 \"structural factor\" 缺实验验证。"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-24T07:12:59.060046+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1463
}
```

</details>

---


### Assistant

_source line 242 · 2026-05-24T07:13:01.812397+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 19

## Round 19

2 recorded events


### User

_source line 243 · 2026-05-24T07:13:04.503193+00:00_

[Reviewer 1 审稿结果]:
Round 3 审稿报告已提交给 Review Director。

核心结论：**7/10 方法严谨性**，5/7 issues resolved，2 个 warning 级问题仍 open：

1. **R1-W2 步数不对等** — 105K vs 505K 的 matched-timestep comparison 存在但未显式讨论，缺少 treatment 长跑数据
2. **R2-W1 TAWM 对比** — "feedback architecture as the structural factor" 仍无实证，仅 architectural reasoning

两个 Round 1 critical issues（统计检验力 N1、单环境 N4）均已实质性解决。新发现 3 个额外问题（online detector 小样本、IQM 报告不完整、dual-critic convergence 叙事过简），均为 warning 或 minor 级别。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 244 · 2026-05-24T07:13:10.213405+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 20

## Round 20

10 recorded events


### User

_source line 245 · 2026-05-24T07:14:42.879909+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条评议

---

### Issue 状态判定回应

**[AGREE] R1-N1 统计检验力 [RESOLVED]**
同意。LOEO AUROC=0.981 提供了比简单 in-sample accuracy 更有说服力的验证。4 seeds × 多配置 × LOEO 的组合在 RL 诊断类工作中是合理的统计功效水平。Limitations 部分也诚实承认了 seed 数量限制（conclusion.tex:10）。

**[AGREE] R1-N4 单环境 [RESOLVED]**
同意 resolved 判定。5 环境（Walker Walk, Cheetah Run, PickCube-v1, StackCube-v1, PegInsertionSide-v1）的覆盖面已足够。但补充我的观察：ManiSkill 的 negative results 虽增加了 discriminative validity，却同时削弱了论文对 CoRL 的 relevance——CIVO 恰恰在 robotics-relevant 的 manipulation 任务中不出现（Section 4.3, results.tex:92-93），使得核心发现的 robotics 价值变得更模糊。R1 给 Relevance 4/5 我认为偏高。

**[AGREE] R1-W1 Factorial 混淆 [RESOLVED]**
同意。introduction.tex:6 中 primary vs secondary comparison 的标注清楚区分了单因素对比和多因素共变的情况。

**[AGREE] R1-W2 步数不对等 [STILL_OPEN]**
同意且补充。这个问题有两个层面：
1. **Baseline 505K vs treatment 105K**：论文声称 "105K steps, sufficient to observe collapse onset"（methodology.tex:58），但未讨论某些 treatment 是否可能在更长训练后 recover。results.tex:81 提到 seed 2 出现 self-correction，那其他 collapsed seeds 是否也可能在更长训练后 recover？这直接影响 "14-19% of baseline" 这一核心 claim 的可靠性。
2. **exp_045 缺失**：如果存在 matched-duration 实验数据但未呈现在正文中，这是一个审稿可见性问题。reviewer 不应需要猜测 appendix 中是否存在支持证据。

**[AGREE] R1-W3 Pathway B [RESOLVED]**
同意。"preliminary" 和 "requires confirmation" 的措辞恰当（results.tex:103），且只有 2 seeds 的情况下不做过强 claim 是负责任的。

**[AGREE] R2-W1 TAWM 对比 [STILL_OPEN]**
强烈同意。这也是我在 Round 1 (R2-W3) 关注的延伸。具体问题：
- Abstract 称 "the contrast with MPC identifies feedback architecture as the structural factor"，Conclusion 重复 "MPC re-planning versus imagination-based bootstrapping—is the structural factor"（conclusion.tex:4）——但论文**从未在 TD-MPC2/TAWM 上运行任何实验**。
- Related Work（related_work.tex:5）的论述 "the critical distinction is that MPC re-plans from real states, so model errors do not accumulate into a critic" 是合理的 architectural reasoning，但将其称为 "structural factor" 暗示了因果确认，而实际只有推理。
- 至少应做到以下之一：(a) 在 TD-MPC2 上复现 dt-conditioning 实验验证 CIVO 不出现，(b) 将 "structural factor" 弱化为 "hypothesized structural factor" 或 "architectural difference that our analysis suggests..."。
- 作为 warning 而非 critical 是合理的——这不影响 DreamerV3 侧的核心诊断结论，但影响论文的 generalizability claim 的可信度。

**[AGREE] R1-W4 Signed error [RESOLVED]**
同意。Appendix 中的 signed error 分析提供了充分证据。

---

### R1 新发现问题回应

**[AGREE] R1-N-new-1: Online CIVO Detector 样本量不足**
完全同意。我的审查（Section 4.7, analysis.tex 中 detector 部分）也独立注意到了这个问题：
- n=14 runs 中仅 5 个正例，TPR=5/5 在统计上等价于 "我们没有观察到 false negative"，不能推断 sensitivity。5 个正例的 95% CI 下界（Clopper-Pearson）为 47.8%，远低于声称的 100%。
- FPR=2/9 (22%) 更值得关注：在实际部署中，近 1/4 的误报意味着 practitioner 会频繁收到无意义的警告，降低对 detector 的信任。
- 论文将 detector 作为四项 contribution 之一（introduction.tex:15 "Online detection"），但以这个样本量作为独立贡献偏弱。建议：要么增加评估规模，要么将 detector 降级为 "preliminary tool" 而非正式 contribution。

**[REBUT] R1-N-new-2: IQM 报告不完整**
部分不同意。
- IQM 的主要价值在于替代 mean 来报告跨 seed 的聚合性能（Agarwal et al. 2021）。论文对核心配置（Walker Walk trained dt-embedding, n=4）报告了 IQM=175.2（results.tex:81），这是最关键的比较。
- 对于 n=1 或 n=2 的配置（Table 2 中多个条目），计算 IQM 本身就没有统计意义。要求所有比较都报告 IQM + stratified bootstrap CI 在当前实验规模下不现实，且不会改变核心结论。
- 但同意 R1 的潜在关注：如果论文引用了 Agarwal et al. 2021 的统计最佳实践，最好在报告数字时更系统地应用（至少对 n≥3 的配置报告 CI）。这是 minor 而非需要修改的问题。

**[AGREE] R1-N-new-3: Dual-critic convergence 因果推理**
同意这存在叙事过度简化的问题。具体：
- ρ > 0.999 是 n=7 dual-critic 配置的结果（results.tex 中 Section 4.6），但论文未报告 convergence 随训练进展的 trajectory——如果 early training 阶段 dual critics 有差异而后来才 converge，那 "Double Q pessimism ineffective" 的结论只在 asymptotic 意义上成立。
- 更关键的张力：如果 dual critics 真的完全 converge 使 pessimism 无效，wide dual-critic 的 3/4 prevention 成功（Table 2, results.tex:136）如何解释？论文在 Section 4.6 提到 "min drives recovery...Prevention requires min + capacity"，但 min 操作在 ρ > 0.999 下理论上应该无效（因为两个 critic 几乎相同）。这里的解释是 "通过不同机制" 而非 pessimism，但论文未充分阐述这个 "不同机制" 是什么。
- 建议：在 Section 4.6 或 Discussion 中增加 1-2 句解释 min operation 在 converged critics 下为何仍能 enable recovery（可能是 gradient 层面的效应而非 value 层面的 pessimism）。

---

### R1 评分回应

**方法严谨性 7/10**：[AGREE] 合理。factorial design 系统性强，但步数不对等和 TAWM 缺实验验证各扣约 1-1.5 分。

**CoRL 维度打分差异**：

| 维度 | R1 评分 | R2 评分 | 差异说明 |
|------|---------|---------|----------|
| Originality | 4/5 | 3/5 | CIVO 现象新颖但 factorial ablation 方法论是标准做法；negative result 的原创性 credit 存在争议 |
| Quality | 3/5 | 3/5 | 一致 |
| Clarity | 4/5 | 3.5/5 | Abstract 过于数字密集（我的 E1），F1-F7 双编号系统增加认知负担（我的 E2） |
| Significance | 3/5 | 2/5 | R1 高估了 significance。核心 actionable takeaway 是 "不要用 trained dt-embedding"——这对需要 temporal abstraction 的社区帮助有限 |
| Relevance | 4/5 | 2.5/5 | **主要分歧点**。ManiSkill negative results 表明 CIVO 是 locomotion-specific，而 CoRL 社区更关心 manipulation/contact-rich tasks。R1 对 relevance 的评估过于宽泛 |
| Limitations | 4/5 | 4/5 | 一致 |

---

### R1 Should-Fix 回应

**[AGREE] S1: 步数不对等**：应在正文 Section 3.6 或 Section 4.1 显式讨论 105K vs 505K 的 rationale，以及为什么 collapse 在 105K 足以确认。

**[AGREE] S2: TAWM "structural factor"**：必须弱化措辞或增加实验。当前 "identifies...as the structural factor" 的表述在没有 TAWM 实验的情况下超出了证据范围。

**[AGREE] S3: Online detector small-sample**：应在 Section 4.7 或 Discussion 中明确承认 n=14 的局限性。

---

### 综合评议

与 R1 的主要共识：
1. Factorial design 严谨，是本文最大优势
2. LOEO 交叉验证增强了可信度
3. 步数不对等和 TAWM 缺实验是两个 remaining open issues

与 R1 的主要分歧：
1. **Relevance 评分**（R1: 4/5 vs R2: 2.5/5）：我认为 R1 低估了 CIVO locomotion-specificity 对 CoRL venue fit 的负面影响。论文的核心发现恰恰在 robot-relevant 任务中不成立，这是一个根本性的 venue fit 问题。
2. **Significance 评分**（R1: 3/5 vs R2: 2/5）：negative result + no reliable fix 的贡献模式在 CoRL 的 deployment-oriented 社区中价值有限。R1 对 "长期社区价值" 的评估合理但偏乐观。
3. **Originality 评分**（R1: 4/5 vs R2: 3/5）：发现一个新 failure mode 有原创性，但方法论（factorial ablation + 标准 RL diagnostics）本身不新颖。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-24T07:15:09.914309+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 247 · 2026-05-24T07:15:10.066125+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-24T07:01:36.359339+00:00\", \"completed_at\": \"2026-05-24T07:05:17.530855+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-4\", \"message\": \"连续 4 页纯文本无任何 display item。第一个视觉锚点（Table 1 + Figure 1）直到第 5 页才出现。对于诊断/实证型论文，审稿人在前 4 页只看到密集文字，第一印象不利。建议将架构图或核心发现的概览图提前到第 1-2 页\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-8\", \"message\": \"正文仅 8 页，其中 display items 仅 4 个（Table 1-2, Figure 1-2）。实证型论文 8 页正文通常期望 5-8 个 display items，当前密度偏低\"}, {\"severity\": \"warning\", \"dimension\": \"page 17\", \"message\": \"Figure 6（CIVO mechanism diagram，展示 trained dt-embedding 如何通过反馈回路产生 asymmetric reward prediction）是核心机制概念图，但被放在 Appendix D.1 而非正文。这是论文最重要的概念可视化，审稿人在正文中看不到方法的直觉图示。强烈建议移入正文 Section 3 或 Section 4\"}, {\"severity\": \"warning\", \"dimension\": \"page 26\", \"message\": \"页面下方约 55% 为空白。Appendix G.2 文本在页面上半部分结束后留有大面积空白\"}, {\"severity\": \"warning\", \"dimension\": \"page 33\", \"message\": \"Table 22 位于页面中下部，上方约 45% 为空白。作为全文最后一页，视觉收尾松散\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 1 图例包含 8+ 配置项，图例文字较小（约 6-7pt），密集排列。建议增大图例字号或使用独立图例面板提高可读性\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 使用了灰色底色标记 CIVO-positive seeds，booktabs 风格正确，脚注齐全。排版合格\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2 使用了彩色线条 + 虚线区分不同 trajectory 类型，可读性良好。Caption 自包含\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2 intervention hierarchy 排版整洁，使用 booktabs 风格，有 Prev/Rate 列清晰标注\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Discussion + Conclusion 在最后一页正文，页面填充约 90%，空间利用合理\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Figure 3 ROC 曲线清晰，标注了 AUC 值和多个阈值点，可读性好\"}, {\"severity\": \"info\", \"dimension\": \"page 15\", \"message\": \"Figure 4 factorial validation 使用红色百分比标注，两面板清晰对比。文字标注略小但可读\"}, {\"severity\": \"info\", \"dim
…[truncated 665 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-24T07:15:10.066656+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-24T07:15:10.066961+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-24T07:17:18.170029+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"统计检验力严重不足：2-3 seeds 无法支撑 causal factor 声明\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 均认同统计效力不足\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。Seeds 增至 4，语言改为 strongest predictor，LOEO AUROC=0.981，IQM 报告。残留小问题：Abstract 中 isolate 一词仍携带因果含义。\"\n    action_items:\n      - round: 1\n        action: \"补 seeds 到 4 per key config\"\n        assigned_to: agent\n        status: done\n      - round: 1\n        action: \"弱化因果语言: causal factor → strongest predictor\"\n        assigned_to: paper_agent\n        status: done\n      - round: 1\n        action: \"统计报告改用 IQM + bootstrap CI per Agarwal et al. 2021\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Seeds 增至 4，因果语言全面弱化为 strongest predictor，LOEO 交叉验证 AUROC=0.981，IQM + bootstrap CI 报告完整。\"\n    resolution_round: 3\n\n  - id: \"R1-N2\"\n    summary: \"NVE 阈值 1.5× 为 post-hoc 选择，88.9% accuracy 是训练准确率，无独立验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 一致认为 post-hoc\"\n    action_items:\n      - round: 1\n        action: \"LOEO cross-validation: mean AUROC 0.981\"\n        assigned_to: agent\n        status: done\n    resolution: \"LOEO 交叉验证完成：3 环境 leave-one-out，mean AUROC 0.981，θ=1.5 在全部 fold 最优范围。论文措辞已改为 in-sample + LOEO cross-validated。\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"CoRL venue fit 严重不足：全文无 robotics 实验/讨论\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"最强共识。用户已确认 CoRL，要求补 robotics 实验\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 判定 STILL_OPEN。改善明显（ManiSkill 实验、robotics framing）但结构性问题未解：ManiSkill negative results 反向证明 CIVO 与 manipulation 无关；robotics framing 仍是 bookend 式；CIVO 是 locomotion-specific。R2 Venue Fit 5/10。R1 给 Relevance 4/5 但 R2 认为偏高（2.5/5）。\"\n    action_items:\n      - round: 1\n        action: \"Paper Agent 已添加 robotics framing: Abstract + Intro + Discussion\"\n        assigned_to: paper_agent\n        status: done\n      - round: 1\n        action: \"ManiSkill 实验（PickCube + StackCube + PegInsertion）\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N4\"\n    summary: \"单环境（Walker Walk）局限使因果声明不可泛化\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 一致。已扩展到 3 环境 + ManiSkill 计划中\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。5 环境覆盖（Walker Walk + Cheetah Run + 3 ManiSkill），CIVO locomotion-specificity 诚实报告，ManiSkill non-CIVO 增加 discriminative validity。\"\n    action_items:\n      - round: 1\n        action: \"Cheetah Run + ManiSkill 扩展\"\n        assigned_to: agent\n        status: done\n    resolution: \"从 1 环境扩展到 5 环境（Walker Walk, Cheetah Run, PickCube-v1, StackCube-v1, PegInsertionSide-v1），CIVO 确认为 locomotion-specific，ManiSkill non-CIVO 提供 discriminative validity。\"\n    resolution_round: 3\n\n  - id: \"R3-N1\"\n    summary: \"未使用 CoRL 2026 官方 PMLR 模板，desk reject 风险\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"依赖 venue 决策\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED。main.tex:5 使用 \\\\usepackage{corl_2026}。\"\n    action_items:\n      - round: 1\n        action: \"切换到 PMLR 模板\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"已使用 corl_2026 PMLR 模板。\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"纯诊断负面结果缺乏 actionable solution\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 critical, R1 AGREE with nuance, R3 partial REBUT\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 判定 STILL_OPEN。有改善（Practitioner guidelines、四级干预、online detector）但核心结论仍是 no reliable fix。最有效 solution = 不用该功能。Frozen embedding 71% 但 eval 差。Wide dual-critic 75% Walker 但 Cheetah 0/1。贡献度 6/10。\"\n    action_items:\n      - round: 1\n        action: \"Practitioner guidelines + 四级干预层级 + online detector\"\n        assigned_to: paper_agent\n        status: done\n      - round: 1\n        action: \"Frozen embedding / dual-critic mitigation 实验\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"Factorial design 存在混淆变量：secondary comparisons 同时改变多个因素\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R3 REBUT: 008d vs 008f 是干净对照\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。Primary vs secondary comparisons 明确标注，2×2 factorial grid 完整。\"\n    action_items:\n      - round: 1\n        action: \"论文显式标注 primary vs secondary comparisons\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Introduction 和 Results 中明确区分 primary comparison (008d vs 008f) 和 secondary comparisons，2×2 grid 完整。\"\n    resolution_round: 3\n\n  - id: \"R1-W2\"\n    summary: \"105K vs 505K 训练步数不对等，treatment 长期命运未知\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"Reviewer 补充: 008a/008e_v3 上升趋势未到头，可能是速度差非结构差\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 STILL_OPEN。Matched-timestep 比较存在（baseline 105K eval 报告）但未显式讨论步数不对等问题。exp_045 长跑数据未在正文呈现。1/4 seeds self-correct 暗示更长训练可能改变结论。\"\n    action_items:\n      - round: 3\n        action: \"在 Discussion 或 Appendix 显式讨论 105K vs 505K rationale 和 self-correction 现象\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"Pathway B (non-CIVO collapse) 解释不充分，仅 1 seed 证据\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 partial REBUT (baseline control)\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。2 seeds + preliminary/requires confirmation 措辞恰当。\"\n    action_items:\n      - round: 1\n        action: \"弱化声明: preliminary evidence + requires confirmation\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"2 seeds 证据 + 'preliminary evidence, requires confirmation' 措辞，力度与证据匹配。\"\n    resolution_round: 3\n\n  - id: \"R1-W4\"\n    summary: \"RSSM fidelity 仅报告 MAE，未验证 reward overprediction 方向性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 AGREE\"\n    action_items:\n      - round: 1\n        action: \"Signed reward error 分析\"\n        assigned_to: agent\n        status: done\n    resolution: \"Signed error 分析完成。dt=2 是负向偏差(underprediction -0.599)，排除 observation-level overprediction，CIVO 定位为 imagination-level prior drift。\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"与 TAWM 的对比仅基于 architectural reasoning，无实证\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 AGREE\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 STILL_OPEN 并强烈同意。Abstract/Conclusion 称 feedback architecture 为 the structural factor 但从未在 TD-MPC2/TAWM 上运行实验。应弱化为 hypothesized structural factor 或增加实验。\"\n    action_items:\n      - round: 3\n        action: \"弱化 structural factor 措辞为 hypothesized structural factor，或在 TD-MPC2 上验证\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"CIVO 与已知 value overestimation 的区分不够清晰\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R1/R3 partial REBUT: trained vs untrained 对比提供机制特异性\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。Related Work 提供清晰经验性区分（控制实验 + signed error + delusional bias 类比），数据支撑充分。\"\n    action_items:\n      - round: 1\n        action: \"Related Work/Discussion 增加显式 CIVO vs compounding error 对比\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Related Work 和 Discussion 提供了充分的经验性区分：untrained embedding 不触发 CIVO（NVE<0.6×），signed error 为负（-0.599），delusional bias 类比准确。\"\n    resolution_round: 3\n\n  - id: \"R2-W4\"\n    summary: \"Related Work 遗漏 (Becker-Ehmck 2023, Park 2021, Wang 2024, Colas 2018) + bib 冗余\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位均提及\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 判定 PARTIALLY RESOLVED。Park 2021、Wang 2024、Colas 2018 已引用；Becker-Ehmck 2023 仍未引用。Bib 从 77 条清理至 44 条，无 orphan。\"\n    action_items:\n      - round: 3\n        action: \"引用 Becker-Ehmck et al. 2023 multi-timestep models\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W1\"\n    summary: \"Limitations 作为 paragraph 嵌入 Conclusion 而非独立 Section\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"R1 REBUT (paragraph 可接受)\"\n    action_items: []\n    resolution: \"Limitations 作为 Conclusion paragraph，CoRL 要求 Limitations section 计入 8 页，当前形式可接受。\"\n    resolution_round: 1\n\n  - id: \"R3-W2\"\n    summary: \"Abstract 过长且缺乏 robotics motivation\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"R1 partial AGREE\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 判定 RESOLVED。约 150 词，robotics motivation 到位，88.9% accuracy 已替换为 AUROC。\"\n    action_items:\n      - round: 1\n        action: \"缩短 Abstract + 加 robotics motivation\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Abstract 约 150 词，首句含 robotics motivation，88.9% 替换为 26/29 AUROC=0.953。\"\n    resolution_round: 3\n\n  - id: \"R3-W3\"\n    summary: \"Bibliography 严重冗余：77 条中仅 29 条被引用\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"splates2025 author 为占位符\"\n      - round: 3\n        reviewers: [2]\n        note: \"Bib 从 77 条清理至 44 条，所有 44 条均被正文引用，无 orphan entries。\"\n    action_items:\n      - round: 1\n        action: \"清理 bib (77→44 条)\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Bib 清理至 44 条，全部被引用，无 orphan。\"\n    resolution_round: 3\n\n  - id: \"R3-W5\"\n    summary: \"fig4_mechanism_diagram.pdf 存在但未被论文引用\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"CIVO 机制图应引入 Section 6.1\"\n    action_items: []\n    resolution: \"fig4_mechanism_diagram 已在 Appendix 引用。\"\n    resolution_round: 1\n\n  - id: \"R3-N3\"\n    summary: \"换模板后正文可能超 8 页\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"需实际测试\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED。PDF 正文 8 页，References 第 9 页起，Appendix 第 11 页起。\"\n    action_items: []\n    resolution: \"正文 8 页，编译通过。\"\n    resolution_round: 3\n\n  - id: \"REV-1\"\n    summary: \"008f causal control 跨 seed 不稳定\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [\"research_reviewer\"]\n        note: \"exp_043 s1 完成：5/5 seeds 全部 NVE<1.5，008f 因果控制 robust\"\n    action_items: []\n    resolution: \"exp_043 确认 008f 5/5 seeds 全部 NVE<1.5，因果控制 robust。\"\n    resolution_round: 1\n\n  - id: \"REV-2\"\n    summary: \"105K vs 500K 比较不对等: 治疗组上升趋势未到头\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [\"research_reviewer\"]\n        note: \"exp_045 treatment extension 008d s3 延长到 300K 中\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"与 R1-W2 合并。两位 reviewer 一致判定 STILL_OPEN。exp_045 数据未在正文呈现。\"\n    action_items:\n      - round: 3\n        action: \"合并入 R1-W2 处理\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N-new-1\"\n    summary: \"Online CIVO Detector 评估样本量不足 (n=14, 仅 5 正例)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致。TPR=5/5 的 95% CI 下界仅 47.8%。FPR=2/9 (22%) 在实际部署中误报率过高。论文将 detector 作为四项 contribution 之一但样本量偏弱。\"\n    action_items:\n      - round: 3\n        action: \"承认 detector 的 small-sample limitation，或降级为 preliminary tool\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N-new-2\"\n    summary: \"Dual-critic convergence 主文叙事过于简化\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致。ρ>0.999 是 asymptotic 结果，与 wide dual-critic 3/4 prevention 成功存在张力。pessimism ineffective 的结论需 nuance：min operation 可能通过非 pessimism 机制发挥作用。\"\n    action_items:\n      - round: 3\n        action: \"在 Section 4.8 或 Discussion 增加 1-2 句解释 min operation 在 converged critics 下的机制\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N-new-3\"\n    summary: \"ManiSkill 和 Cheetah Run baseline eval 值在 Table 1 中缺失\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [2]\n        note: \"Table 1 中 ManiSkill 和 Cheetah Run 缺少 vanilla DreamerV3 baseline eval 值，读者无法判断相对性能。\"\n    action_items:\n      - round: 3\n        action: \"在 Table 1 或脚注中补充各环境 baseline eval 值\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"统计检验力严重不足：2-3 seeds 无法支撑 causal factor 声明\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 均认同统计效力不足\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。Seeds 增至 4，语言改为 strongest predictor，LOEO AUROC=0.981，IQM 报告。残留小问题：Abstract 中 isolate 一词仍携带因果含义。\"\n    action_items:\n      - round: 1\n        action: \"补 seeds 到 4 per key config\"\n        assigned_to: agent\n        status: done\n      - round: 1\n        action: \"弱化因果语言: causal factor → strongest predictor\"\n        assigned_to: paper_agent\n        status: done\n      - round: 1\n        action: \"统计报告改用 IQM + bootstrap CI per Agarwal et al. 2021\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Seeds 增至 4，因果语言全面弱化为 strongest predictor，LOEO 交叉验证 AUROC=0.981，IQM + bootstrap CI 报告完整。\"\n    resolution_round: 3\n\n  - id: \"R1-N2\"\n    summary: \"NVE 阈值 1.5× 为 post-hoc 选择，88.9% accuracy 是训练准确率，无独立验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 一致认为 post-hoc\"\n    action_items:\n      - round: 1\n        action: \"LOEO cross-validation: mean AUROC 0.981\"\n        assigned_to: agent\n        status: done\n    resolution: \"LOEO 交叉验证完成：3 环境 leave-one-out，mean AUROC 0.981，θ=1.5 在全部 fold 最优范围。论文措辞已改为 in-sample + LOEO cross-validated。\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"CoRL venue fit 严重不足：全文无 robotics 实验/讨论\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"最强共识。用户已确认 CoRL，要求补 robotics 实验\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 判定 STILL_OPEN。改善明显（ManiSkill 实验、robotics framing）但结构性问题未解：ManiSkill negative results 反向证明 CIVO 与 manipulation 无关；robotics framing 仍是 bookend 式；CIVO 是 locomotion-specific。R2 Venue Fit 5/10。R1 给 Relevance 4/5 但 R2 认为偏高（2.5/5）。\"\n    action_items:\n      - round: 1\n        action: \"Paper Agent 已添加 robotics framing: Abstract + Intro + Discussion\"\n        assigned_to: paper_agent\n        status: done\n      - round: 1\n        action: \"ManiSkill 实验（PickCube + StackCube + PegInsertion）\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N4\"\n    summary: \"单环境（Walker Walk）局限使因果声明不可泛化\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 一致。已扩展到 3 环境 + ManiSkill 计划中\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。5 环境覆盖（Walker Walk + Cheetah Run + 3 ManiSkill），CIVO locomotion-specificity 诚实报告，ManiSkill non-CIVO 增加 discriminative validity。\"\n    action_items:\n      - round: 1\n        action: \"Cheetah Run + ManiSkill 扩展\"\n        assigned_to: agent\n        status: done\n    resolution: \"从 1 环境扩展到 5 环境（Walker Walk, Cheetah Run, PickCube-v1, StackCube-v1, PegInsertionSide-v1），CIVO 确认为 locomotion-specific，ManiSkill non-CIVO 提供 discriminative validity。\"\n    resolution_round: 3\n\n  - id: \"R3-N1\"\n    summary: \"未使用 CoRL 2026 官方 PMLR 模板，desk reject 风险\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"依赖 venue 决策\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED。main.tex:5 使用 \\\\usepackage{corl_2026}。\"\n    action_items:\n      - round: 1\n        action: \"切换到 PMLR 模板\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"已使用 corl_2026 PMLR 模板。\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"纯诊断负面结果缺乏 actionable solution\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 critical, R1 AGREE with nuance, R3 partial REBUT\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 判定 STILL_OPEN。有改善（Practitioner guidelines、四级干预、online detector）但核心结论仍是 no reliable fix。最有效 solution = 不用该功能。Frozen embedding 71% 但 eval 差。Wide dual-critic 75% Walker 但 Cheetah 0/1。贡献度 6/10。\"\n    action_items:\n      - round: 1\n        action: \"Practitioner guidelines + 四级干预层级 + online detector\"\n        assigned_to: paper_agent\n        status: done\n      - round: 1\n        action: \"Frozen embedding / dual-critic mitigation 实验\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"Factorial design 存在混淆变量：secondary comparisons 同时改变多个因素\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R3 REBUT: 008d vs 008f 是干净对照\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。Primary vs secondary comparisons 明确标注，2×2 factorial grid 完整。\"\n    action_items:\n      - round: 1\n        action: \"论文显式标注 primary vs secondary comparisons\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Introduction 和 Results 中明确区分 primary comparison (008d vs 008f) 和 secondary comparisons，2×2 grid 完整。\"\n    resolution_round: 3\n\n  - id: \"R1-W2\"\n    summary: \"105K vs 505K 训练步数不对等，treatment 长期命运未知\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"Reviewer 补充: 008a/008e_v3 上升趋势未到头，可能是速度差非结构差\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 STILL_OPEN。Matched-timestep 比较存在（baseline 105K eval 报告）但未显式讨论步数不对等问题。exp_045 长跑数据未在正文呈现。1/4 seeds self-correct 暗示更长训练可能改变结论。\"\n    action_items:\n      - round: 3\n        action: \"在 Discussion 或 Appendix 显式讨论 105K vs 505K rationale 和 self-correction 现象\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"Pathway B (non-CIVO collapse) 解释不充分，仅 1 seed 证据\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 partial REBUT (baseline control)\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。2 seeds + preliminary/requires confirmation 措辞恰当。\"\n    action_items:\n      - round: 1\n        action: \"弱化声明: preliminary evidence + requires confirmation\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"2 seeds 证据 + 'preliminary evidence, requires confirmation' 措辞，力度与证据匹配。\"\n    resolution_round: 3\n\n  - id: \"R1-W4\"\n    summary: \"RSSM fidelity 仅报告 MAE，未验证 reward overprediction 方向性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 AGREE\"\n    action_items:\n      - round: 1\n        action: \"Signed reward error 分析\"\n        assigned_to: agent\n        status: done\n    resolution: \"Signed error 分析完成。dt=2 是负向偏差(underprediction -0.599)，排除 observation-level overprediction，CIVO 定位为 imagination-level prior drift。\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"与 TAWM 的对比仅基于 architectural reasoning，无实证\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 AGREE\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 STILL_OPEN 并强烈同意。Abstract/Conclusion 称 feedback architecture 为 the structural factor 但从未在 TD-MPC2/TAWM 上运行实验。应弱化为 hypothesized structural factor 或增加实验。\"\n    action_items:\n      - round: 3\n        action: \"弱化 structural factor 措辞为 hypothesized structural factor，或在 TD-MPC2 上验证\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"CIVO 与已知 value overestimation 的区分不够清晰\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R1/R3 partial REBUT: trained vs untrained 对比提供机制特异性\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。Related Work 提供清晰经验性区分（控制实验 + signed error + delusional bias 类比），数据支撑充分。\"\n    action_items:\n      - round: 1\n        action: \"Related Work/Discussion 增加显式 CIVO vs compounding error 对比\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Related Work 和 Discussion 提供了充分的经验性区分：untrained embedding 不触发 CIVO（NVE<0.6×），signed error 为负（-0.599），delusional bias 类比准确。\"\n    resolution_round: 3\n\n  - id: \"R2-W4\"\n    summary: \"Related Work 遗漏 (Becker-Ehmck 2023, Park 2021, Wang 2024, Colas 2018) + bib 冗余\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位均提及\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 判定 PARTIALLY RESOLVED。Park 2021、Wang 2024、Colas 2018 已引用；Becker-Ehmck 2023 仍未引用。Bib 从 77 条清理至 44 条，无 orphan。\"\n    action_items:\n      - round: 3\n        action: \"引用 Becker-Ehmck et al. 2023 multi-timestep models\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W1\"\n    summary: \"Limitations 作为 paragraph 嵌入 Conclusion 而非独立 Section\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"R1 REBUT (paragraph 可接受)\"\n    action_items: []\n    resolution: \"Limitations 作为 Conclusion paragraph，CoRL 要求 Limitations section 计入 8 页，当前形式可接受。\"\n    resolution_round: 1\n\n  - id: \"R3-W2\"\n    summary: \"Abstract 过长且缺乏 robotics motivation\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"R1 partial AGREE\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 判定 RESOLVED。约 150 词，robotics motivation 到位，88.9% accuracy 已替换为 AUROC。\"\n    action_items:\n      - round: 1\n        action: \"缩短 Abstract + 加 robotics motivation\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Abstract 约 150 词，首句含 robotics motivation，88.9% 替换为 26/29 AUROC=0.953。\"\n    resolution_round: 3\n\n  - id: \"R3-W3\"\n    summary: \"Bibliography 严重冗余：77 条中仅 29 条被引用\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"splates2025 author 为占位符\"\n      - round: 3\n        reviewers: [2]\n        note: \"Bib 从 77 条清理至 44 条，所有 44 条均被正文引用，无 orphan entries。\"\n    action_items:\n      - round: 1\n        action: \"清理 bib (77→44 条)\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Bib 清理至 44 条，全部被引用，无 orphan。\"\n    resolution_round: 3\n\n  - id: \"R3-W5\"\n    summary: \"fig4_mechanism_diagram.pdf 存在但未被论文引用\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"CIVO 机制图应引入 Section 6.1\"\n    action_items: []\n    resolution: \"fig4_mechanism_diagram 已在 Appendix 引用。\"\n    resolution_round: 1\n\n  - id: \"R3-N3\"\n    summary: \"换模板后正文可能超 8 页\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"需实际测试\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED。PDF 正文 8 页，References 第 9 页起，Appendix 第 11 页起。\"\n    action_items: []\n    resolution: \"正文 8 页，编译通过。\"\n    resolution_round: 3\n\n  - id: \"REV-1\"\n    summary: \"008f causal control 跨 seed 不稳定\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [\"research_reviewer\"]\n        note: \"exp_043 s1 完成：5/5 seeds 全部 NVE<1.5，008f 因果控制 robust\"\n    action_items: []\n    resolution: \"exp_043 确认 008f 5/5 seeds 全部 NVE<1.5，因果控制 robust。\"\n    resolution_round: 1\n\n  - id: \"REV-2\"\n    summary: \"105K vs 500K 比较不对等: 治疗组上升趋势未到头\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [\"research_reviewer\"]\n        note: \"exp_045 treatment extension 008d s3 延长到 300K 中\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"与 R1-W2 合并。两位 reviewer 一致判定 STILL_OPEN。exp_045 数据未在正文呈现。\"\n    action_items:\n      - round: 3\n        action: \"合并入 R1-W2 处理\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N-new-1\"\n    summary: \"Online CIVO Detector 评估样本量不足 (n=14, 仅 5 正例)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致。TPR=5/5 的 95% CI 下界仅 47.8%。FPR=2/9 (22%) 在实际部署中误报率过高。论文将 detector 作为四项 contribution 之一但样本量偏弱。\"\n    action_items:\n      - round: 3\n        action: \"承认 detector 的 small-sample limitation，或降级为 preliminary tool\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N-new-2\"\n    summary: \"Dual-critic convergence 主文叙事过于简化\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致。ρ>0.999 是 asymptotic 结果，与 wide dual-critic 3/4 prevention 成功存在张力。pessimism ineffective 的结论需 nuance：min operation 可能通过非 pessimism 机制发挥作用。\"\n    action_items:\n      - round: 3\n        action: \"在 Section 4.8 或 Discussion 增加 1-2 句解释 min operation 在 converged critics 下的机制\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N-new-3\"\n    summary: \"ManiSkill 和 Cheetah Run baseline eval 值在 Table 1 中缺失\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [2]\n        note: \"Table 1 中 ManiSkill 和 Cheetah Run 缺少 vanilla DreamerV3 baseline eval 值，读者无法判断相对性能。\"\n    action_items:\n      - round: 3\n        action: \"在 Table 1 或脚注中补充各环境 baseline eval 值\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-24T07:17:18.271142+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml\", \"bytes\": 15090}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-24T07:19:49.232200+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 3\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**目标 Venue**: CoRL 2026 Main Conference\n**审稿日期**: 2026-05-24\n**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验充分性 | R2: Venue Fit + 贡献度 + 写作质量）\n**轮次**: Round 3 继续审稿（修订评估）+ 交叉分享（1 轮收敛）\n**上轮评分**: Round 1 Strong Reject (4/10)\n\n---\n\n## Summary\n\n论文在 Round 1 (Strong Reject) 后进行了大幅修改：从 1 环境扩展到 5 环境（Walker Walk, Cheetah Run, PickCube-v1, StackCube-v1, PegInsertionSide-v1），关键配置 seeds 增至 4，引入 LOEO 交叉验证（AUROC=0.981），因果语言全面弱化为 \"strongest predictor\"，新增四级干预层级分析和在线 CIVO 检测器，切换至 CoRL 2026 PMLR 模板，添加 robotics framing 和 ManiSkill 实验。论文现在识别 CIVO 为 locomotion-specific（6/6 locomotion seeds 触发，0/5 manipulation configurations 触发），并提供了 discriminative validity（frozen-embedding 控制正确区分 CIVO 与环境特异性 transient）。\n\n---\n\n## Strengths\n\n1. **Factorial design 系统且严谨**（2/2 reviewer 共识）：43 配置 × 4 seeds × 5 环境的设计空间覆盖广泛；primary/secondary comparison 标注清晰；2×2 factorial grid 完整\n2. **LOEO 交叉验证显著增强统计可信度**：AUROC=0.953 (in-sample, n=29), 0.981 (LOEO, 3 folds) 在 RL 诊断类工作中是扎实的统计功效水平\n3. **四级干预层级分析**（gradient/output/representation/architecture）：提供了系统性的 negative result，对社区有长期参考价值。Gradient magnitude ≠ causal importance 的发现（reward head 38-49% 但 SGS 无效）是有洞见的\n4. **ManiSkill non-CIVO 结果增加 discriminative validity**：NVE 诊断能正确区分 dt-embedding-dependent CIVO 与环境特异性 transient（frozen controls 匹配 trained spikes），展示了方法论的特异性\n5. **Dual-critic convergence (ρ > 0.999)**：关于 imagination-based training 中 Double Q pessimism 失效的 structural insight 有价值\n6. **Limitations section 诚实全面**：主动承认 4-seed 局限、architecture 局限、locomotion-specificity，ManiSkill non-CIVO 如实报告\n7. **Signed error 分析**：dt=2 underprediction (SE=-0.599) 排除 observation-level reward overprediction，将 CIVO 定位为 imagination-level prior drift，与 compounding error 清晰区分\n\n---\n\n## Weaknesses（按严重性排序）\n\n### Critical（影响接收决定）\n\n**W-C1. CoRL Venue Fit 仍有结构性 gap [R2 判定 STILL_OPEN，R1 部分同意]**\n论文做了显著改进（ManiSkill 实验、robotics framing），但核心矛盾未解决：\n- **ManiSkill 结果反向证明 CIVO 与 manipulation 无关**：所有 3 个 ManiSkill 环境均未出现 dt-embedding-dependent CIVO（Section 4.3: \"CIVO is locomotion-specific in DreamerV3\"），frozen controls 表现相当甚至更高。论文的核心发现恰恰在 robotics-relevant manipulation 任务中不成立。\n- **Robotics framing 仍是 \"bookend\" 式的**：robotics motivation 集中在 Introduction 前两句和 Discussion 一个段落，方法和结果部分（Section 3-4，约 4 页）完全是通用 RL 分析。\n- **CoRL CFP 要求 \"focus on core robotics problems\"**：CIVO 是一个通用 RL/world-model 问题，并非 robotics-specific。论文自己承认 \"does not test...real-robot deployments\"（conclusion.tex:7）。\n- **Desk reject 风险已降低但未消除**：ManiSkill 实验使论文不至于完全没有 robot-relevant 实验，但严格的 AC 可能认为 negative ManiSkill 结果 + DMC-based 核心实验不满足 scope。\n\n**W-C2. 贡献模式对 CoRL deployment-oriented 社区偏弱 [R2 判定 STILL_OPEN]**\n论文从 \"纯诊断\" 升级为 \"诊断 + partial mitigation + detection\"，但：\n- **核心结论仍是 negative**：Table 2 总结 \"No level reliably eliminates CIVO across environments\"\n- **最有效 \"solution\" 是不使用该功能**：embedding removed = 100% prevention = 不做 temporal abstraction via dt-conditioning\n- **Partial mitigations 效果有限**：frozen embedding 5/7 prevention 但 eval 仍差（015b: 22% baseline）；wide dual-critic 3/4 Walker 但 Cheetah 0/1\n- **Practitioner guidelines 的核心建议**：\"不要用 trained dt-embedding\" + \"用 NVE 监控\"——对需要 temporal abstraction 的应用帮助有限\n\n### Warning（影响评分但不一票否决）\n\n**W-W1. 105K vs 505K 训练步数不对等未显式讨论 [2/2 reviewer 共识 STILL_OPEN]**\n论文在 105K 对治疗组和基线进行 matched-timestep 比较，但：\n- 未在正文讨论为什么 105K 足够确认 collapse（尤其当 1/4 seeds self-correct 时）\n- exp_045 延长到 300K 的数据未在正文呈现\n- 如果 self-correction 在更长时间窗口更普遍，\"all variable-rate configurations degrade\" (F1) 可能过强\n\n**W-W2. TAWM/MPC 对比仍无实证 [2/2 reviewer 共识 STILL_OPEN]**\nAbstract 和 Conclusion 称 \"feedback architecture as the structural factor\"，但从未在 TD-MPC2/TAWM 上运行实验。这一核心论断只有 architectural reasoning 支撑。应弱化为 \"hypothesized structural factor\" 或增加至少一个 MPC baseline 实验。\n\n**W-W3. Online CIVO Detector 评估样本量不足 [2/2 reviewer 共识，Round 3 新发现]**\nn=14 runs 中仅 5 个正例。TPR=5/5 的 95% CI 下界 (Clopper-Pearson) 仅 47.8%。FPR=2/9 (22%) 在部署场景中误报率过高。论文将 detector 作为四项 contribution 之一，但样本量不足以支撑独立贡献地位。\n\n**W-W4. Becker-Ehmck et al. (2023) 仍未引用 [R2 指出，PARTIALLY RESOLVED]**\n三篇遗漏文献已引用（Park 2021, Wang 2024, Colas 2018），但 Becker-Ehmck et al. (2023) \"Multi-timestep models for MBRL\" 仍缺失，与论文主题直接相关。\n\n### Minor\n\n**W-M1. Abstract 统计数据过密**：~150 词包含 6+ 数字指标（14-19%, 26/29, AUROC=0.953, 2.78×, ρ>0.999, 100% sensitivity），建议精简至 2-3 个关键数字。\n\n**W-M2. Dual-critic convergence 叙事过于简化 [2/2 reviewer 共识]**：ρ > 0.999 是 asymptotic 结果；与 wide dual-critic 3/4 prevention 成功存在张力；主文 \"pessimism ineffective\" 需 nuance——min operation 可能通过非 pessimism 机制发挥作用。\n\n**W-M3. ManiSkill 和 Cheetah Run baseline eval 值缺失**：Table 1 中这些环境缺少 vanilla DreamerV3 baseline 参照值，读者无法判断相对性能。\n\n**W-M4. Abstract 中 \"isolate\" 携带因果含义**，与全文 \"strongest predictor\" 措辞不一致。\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 共识度 |\n|------|----|----|--------|\n| R1-N1 统计检验力 | RESOLVED | RESOLVED | **2/2 一致** |\n| R1-N4 单环境 | RESOLVED | RESOLVED | **2/2 一致** |\n| R1-W1 Factorial 混淆 | RESOLVED | RESOLVED | **2/2 一致** |\n| R1-W2 步数不对等 | STILL_OPEN | STILL_OPEN | **2/2 一致** |\n| R1-W3 Pathway B | RESOLVED | RESOLVED | **2/2 一致** |\n| R2-W1 TAWM 无实证 | STILL_OPEN | STILL_OPEN | **2/2 一致** |\n| R1-W4 Signed error | RESOLVED | RESOLVED | **2/2 一致** |\n| R2-W3 CIVO 区分 | — | RESOLVED | R2 独立确认 |\n| R3-W2 Abstract | — | RESOLVED | R2 独立确认 |\n| R2-W4 Bib | — | PARTIALLY | Becker-Ehmck 仍缺 |\n| R1-N3 Venue fit | Relevance 4/5 | STILL_OPEN (5/10) | **分歧** |\n| R2-N3 Actionable | — | STILL_OPEN (6/10) | R2 独立判定 |\n| N-new-1 Detector 样本量 | WARNING | AGREE | **2/2 一致** |\n| N-new-3 Dual-critic | MINOR | AGREE | **2/2 一致** |\n\n---\n\n## Reviewer Divergence\n\n**1. CoRL Relevance（R1: 4/5 vs R2: 2.5/5）**\n- R1：temporal abstraction 是 CoRL 核心话题，world-model RL 直接关联 robot control\n- R2：CIVO 恰恰在 robotics-relevant manipulation 中不出现，核心发现是 locomotion-specific，CoRL 社区更关心 contact-rich manipulation\n- **Director 判断**：R2 的论点更有说服力。ManiSkill negative results 是论文的 honest science，但客观上削弱了对 CoRL 的 relevance。CIVO 仅在 DMC locomotion 中复现，而 DMC locomotion 不是 CoRL 的核心关注点。综合评估 relevance 约 3/5。\n\n**2. Significance（R1: 3/5 vs R2: 2/5）**\n- R1：四级干预层级分析对社区有长期价值\n- R2：negative result + no reliable fix 的贡献模式在 deployment-oriented 社区价值有限；核心 takeaway 是 \"不要用\"\n- **Director 判断**：部分同意双方。四级干预分析的系统性是 genuine contribution，但论文的 actionable 输出确实有限。综合约 2.5/5。\n\n**3. Originality（R1: 4/5 vs R2: 3/5）**\n- R1：首个系统诊断 DreamerV3 变速想象失败的工作，CIVO 现象识别新颖\n- R2：方法论（factorial ablation）是标准做法，negative result 的原创性 credit 存在争议\n- **Director 判断**：CIVO 现象的识别和因果分离确实新颖（特别是 gradient magnitude ≠ causal importance 的发现），但方法论框架本身不新。综合约 3.5/5。\n\n---\n\n## Questions for Authors\n\n1. 如果 treatment 训练延长到 300K-500K 步，self-correction 是否会更普遍？exp_045 的数据是否可以报告？\n2. \"Feedback architecture as the structural factor\" 能否弱化为 \"hypothesized structural factor\"，或者是否有计划在 TD-MPC2 上验证？\n3. CIVO 在 locomotion 出现但 manipulation 不出现的 reward density 假说（Discussion \"a possible mediator is reward density\"），是否有更直接的证据？\n4. Online detector 的 FPR=22% 在实际部署中是否可接受？是否有降低误报率的方案？\n5. Wide dual-critic 3/4 CIVO prevention 的成功机制是什么？如果 ρ > 0.999 使 pessimism 无效，min operation 通过什么机制起作用？\n\n---\n\n## Missing References\n\n- **Becker-Ehmck et al. (2023)** \"Multi-timestep models for Model-based RL\" — 直接研究 multi-timestep world model，与论文主题高度相关，在 Round 1 已提出但仍未引用\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（5 warnings, 0 critical, 12 info）。\n\n**主要发现**：\n1. **[warning] 前 4 页无 display item**：连续 4 页纯文本，第一个视觉锚点（Table 1 + Figure 1）直到第 5 页才出现。对诊断/实证型论文，审稿人第一印象不利。建议将架构图或核心发现概览图提前到第 1-2 页。\n2. **[warning] 正文 display item 密度偏低**：8 页正文仅 4 个 display items（Table 1-2, Figure 1-2），实证型论文通常期望 5-8 个。\n3. **[warning] CIVO mechanism diagram (Figure 6) 被放在 Appendix**：这是论文最重要的概念可视化，审稿人在正文中看不到方法的直觉图示。强烈建议移入正文。\n4. **[warning] Appendix 页面空白**：Page 26 和 Page 33 有大面积空白。\n5. **[info] 图表质量良好**：Figure 1/2 使用彩色线条和清晰标注；Table 1-2 使用 booktabs 风格；ROC 曲线标注 AUC 和阈值点。\n\n---\n\n## Overall Assessment\n\n**评分: Weak Reject (5/10)**\n**置信度: High (4/5)**\n\n**与 Round 1 (Strong Reject, 4/10) 的变化**：论文在方法论和实验充分性方面取得了显著进步：\n\n| 维度 | Round 1 | Round 3 | 变化 |\n|------|---------|---------|------|\n| 统计检验力 | Critical (2-3 seeds) | Resolved (4 seeds, LOEO) | ▲▲ |\n| 环境覆盖 | Critical (1 env) | Resolved (5 envs) | ▲▲ |\n| NVE 验证 | Critical (post-hoc) | Resolved (LOEO, AUROC=0.981) | ▲▲ |\n| 模板合规 | Critical (desk reject) | Resolved (PMLR) | ▲▲ |\n| Venue fit | Critical | Still open but improved | ▲ |\n| Actionable 贡献 | Warning | Still open but improved | ▲ |\n| CIVO 区分 | Warning | Resolved | ▲▲ |\n\n**Round 1 的 4 个 critical issues 中 3 个已 resolved**（统计检验力、单环境、模板），第 4 个（venue fit）有改善但结构性矛盾未解。\n\n**核心矛盾**（影响从 Weak Reject 上升到 Borderline 的障碍）：\n1. **Venue fit**：论文的核心发现（CIVO）仅在 DMC locomotion 中成立，在 robotics-relevant manipulation 中不出现。CoRL 要求 \"focus on core robotics problems\"，当前论文更适合 ICML/NeurIPS 的 RL/world-model track。\n2. **贡献模式**：diagnostic negative result + partial mitigation + detection 的组合在 ML theory venue 可以接受，但对 CoRL 的 deployment-oriented 社区偏弱。Practitioner 的最佳策略仍然是 \"不要用 trained dt-embedding\"。\n\n**如果提交到 ICML/NeurIPS**：方法论评分会提升至 Borderline Accept (6/10)——factorial design 严谨、LOEO 验证有力、四级干预分析有系统性贡献、CIVO 与 compounding error 的区分清晰。Venue fit 和 actionable 贡献的约束消失。\n\n**综合维度评分**（Director 综合两位 Reviewer）：\n\n| 维度 | 评分 | 理由 |\n|------|------|------|\n| Originality | 3.5/5 | CIVO 现象新颖，gradient ≠ causal importance 有洞见，方法论框架标准 |\n| Quality | 3/5 | Factorial design 严谨，LOEO 有力，但 CIVO 仅 2/5 环境复现，部分配置样本量小 |\n| Clarity | 4/5 | 结构清晰，F1-F7 叙事好，33 页 appendix 详尽 |\n| Significance | 2.5/5 | 四级干预有系统贡献，但 locomotion-specific + no reliable fix 限制 impact |\n| Relevance | 3/5 | Temporal abstraction 与 CoRL 相关，但核心发现在 manipulation 不成立 |\n| Limitations | 4/5 | 诚实全面 |\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 约 150 词，长度合理。Robotics motivation 到位（首句）。\n- 统计数据过密（6+ 数字指标），建议精简至 2-3 个关键数字\n- \"isolate\" 一词与全文 \"strongest predictor\" 不一致\n\n### Introduction (Section 1)\n- Robotics framing 明显改善（DayDreamer, TD-MPC2 引用，temporal abstraction 的 robotics 需求）\n- Contribution 列表 4 项与正文一致\n- 最后一段 robotics relevance 论述合理但稍显牵强\n\n### Related Work (Section 2)\n- CIVO vs compounding error 区分清晰（控制实验 + signed error）\n- Park 2021, Wang 2024, Colas 2018 已引用\n- Becker-Ehmck 2023 仍缺\n\n### Experimental Setup (Section 3)\n- Factorial design 展示专业，四因素清晰\n- Primary vs secondary comparison 标注到位\n- SGS, TCN, RAVE, Dual-critic 方法描述完整\n- 缺少对 105K vs 505K 步数选择的 rationale 讨论\n\n### Results (Section 4)\n- F1-F7 因果链叙事清晰\n- Table 1 信息密度高，灰色标记 CIVO-positive 有效\n- ManiSkill negative results 诚实呈现\n- 缺少 Cheetah/ManiSkill baseline eval 参照值\n- Online detector 评估样本量不足（n=14, 5 正例）\n- Dual-critic ρ > 0.999 结论需 nuance\n\n### Discussion (Section 5)\n- CIVO mechanism 段落简洁准确\n- Practitioner guidelines 可操作（NVE ≥ 1.5×, embedding freezing）\n- \"Implications for robot learning\" 提供了 reward density 假说\n- \"structural factor\" 措辞过强（无 MPC 实验验证）\n\n### Conclusion (Section 6)\n- Limitations paragraph 诚实（4 seeds, architecture, real-robot）\n- 措辞恰当，未过度泛化\n\n### Appendix\n- 33 页，极其详尽（完整 42 配置结果、NVE sensitivity、LOEO、gradient decomposition、entropy dynamics、dual-critic analysis）\n- Figure 6 (CIVO mechanism diagram) 应移入正文\n- 部分页面空白可优化",
  "project": "event-gated-adaptive-horizon",
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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 3\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**目标 Venue**: CoRL 2026 Main Conference\n**审稿日期**: 2026-05-24\n**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验充分性 | R2: Venue Fit + 贡献度 + 写作质量）\n**轮次**: Round 3 继续审稿（修订评估）+ 交叉分享（1 轮收敛）\n**上轮评分**: Round 1 Strong Reject (4/10)\n\n---\n\n## Summary\n\n论文在 Round 1 (Strong Reject) 后进行了大幅修改：从 1 环境扩展到 5 环境（Walker Walk, Cheetah Run, PickCube-v1, StackCube-v1, PegInsertionSide-v1），关键配置 seeds 增至 4，引入 LOEO 交叉验证（AUROC=0.981），因果语言全面弱化为 \"strongest predictor\"，新增四级干预层级分析和在线 CIVO 检测器，切换至 CoRL 2026 PMLR 模板，添加 robotics framing 和 ManiSkill 实验。论文现在识别 CIVO 为 locomotion-specific（6/6 locomotion seeds 触发，0/5 manipulation configurations 触发），并提供了 discriminative validity（frozen-embedding 控制正确区分 CIVO 与环境特异性 transient）。\n\n---\n\n## Strengths\n\n1. **Factorial design 系统且严谨**（2/2 reviewer 共识）：43 配置 × 4 seeds × 5 环境的设计空间覆盖广泛；primary/secondary comparison 标注清晰；2×2 factorial grid 完整\n2. **LOEO 交叉验证显著增强统计可信度**：AUROC=0.953 (in-sample, n=29), 0.981 (LOEO, 3 folds) 在 RL 诊断类工作中是扎实的统计功效水平\n3. **四级干预层级分析**（gradient/output/representation/architecture）：提供了系统性的 negative result，对社区有长期参考价值。Gradient magnitude ≠ causal importance 的发现（reward head 38-49% 但 SGS 无效）是有洞见的\n4. **ManiSkill non-CIVO 结果增加 discriminative validity**：NVE 诊断能正确区分 dt-embedding-dependent CIVO 与环境特异性 transient（frozen controls 匹配 trained spikes），展示了方法论的特异性\n5. **Dual-critic convergence (ρ > 0.999)**：关于 imagination-based training 中 Double Q pessimism 失效的 structural insight 有价值\n6. **Limitations section 诚实全面**：主动承认 4-seed 局限、architecture 局限、locomotion-specificity，ManiSkill non-CIVO 如实报告\n7. **Signed error 分析**：dt=2 underprediction (SE=-0.599) 排除 observation-level reward overprediction，将 CIVO 定位为 imagination-level prior drift，与 compounding error 清晰区分\n\n---\n\n## Weaknesses（按严重性排序）\n\n### Critical（影响接收决定）\n\n**W-C1. CoRL Venue Fit 仍有结构性 gap [R2 判定 STILL_OPEN，R1 部分同意]**\n论文做了显著改进（ManiSkill 实验、robotics framing），但核心矛盾未解决：\n- **ManiSkill 结果反向证明 CIVO 与 manipulation 无关**：所有 3 个 ManiSkill 环境均未出现 dt-embedding-dependent CIVO（Section 4.3: \"CIVO is locomotion-specific in DreamerV3\"），frozen controls 表现相当甚至更高。论文的核心发现恰恰在 robotics-relevant manipulation 任务中不成立。\n- **Robotics framing 仍是 \"bookend\" 式的**：robotics motivation 集中在 Introduction 前两句和 Discussion 一个段落，方法和结果部分（Section 3-4，约 4 页）完全是通用 RL 分析。\n- **CoRL CFP 要求 \"focus on core robotics problems\"**：CIVO 是一个通用 RL/world-model 问题，并非 robotics-specific。论文自己承认 \"does not test...real-robot deployments\"（conclusion.tex:7）。\n- **Desk reject 风险已降低但未消除**：ManiSkill 实验使论文不至于完全没有 robot-relevant 实验，但严格的 AC 可能认为 negative ManiSkill 结果 + DMC-based 核心实验不满足 scope。\n\n**W-C2. 贡献模式对 CoRL deployment-oriented 社区偏弱 [R2 判定 STILL_OPEN]**\n论文从 \"纯诊断\" 升级为 \"诊断 + partial mitigation + detection\"，但：\n- **核心结论仍是 negative**：Table 2 总结 \"No level reliably eliminates CIVO across environments\"\n- **最有效 \"solution\" 是不使用该功能**：embedding removed = 100% prevention = 不做 temporal abstraction via dt-conditioning\n- **Partial mitigations 效果有限**：frozen embedding 5/7 prevention 但 eval 仍差（015b: 22% baseline）；wide dual-critic 3/4 Walker 但 Cheetah 0/1\n- **Practitioner guidelines 的核心建议**：\"不要用 trained dt-embedding\" + \"用 NVE 监控\"——对需要 temporal abstraction 的应用帮助有限\n\n### Warning（影响评分但不一票否决）\n\n**W-W1. 105K vs 505K 训练步数不对等未显式讨论 [2/2 reviewer 共识 STILL_OPEN]**\n论文在 105K 对治疗组和基线进行 matched-timestep 比较，但：\n- 未在正文讨论为什么 105K 足够确认 collapse（尤其当 1/4 seeds self-correct 时）\n- exp_045 延长到 300K 的数据未在正文呈现\n- 如果 self-correction 在更长时间窗口更普遍，\"all variable-rate configurations degrade\" (F1) 可能过强\n\n**W-W2. TAWM/MPC 对比仍无实证 [2/2 reviewer 共识 STILL_OPEN]**\nAbstract 和 Conclusion 称 \"feedback architecture as the structural factor\"，但从未在 TD-MPC2/TAWM 上运行实验。这一核心论断只有 architectural reasoning 支撑。应弱化为 \"hypothesized structural factor\" 或增加至少一个 MPC baseline 实验。\n\n**W-W3. Online CIVO Detector 评估样本量不足 [2/2 reviewer 共识，Round 3 新发现]**\nn=14 runs 中仅 5 个正例。TPR=5/5 的 95% CI 下界 (Clopper-Pearson) 仅 47.8%。FPR=2/9 (22%) 在部署场景中误报率过高。论文将 detector 作为四项 contribution 之一，但样本量不足以支撑独立贡献地位。\n\n**W-W4. Becker-Ehmck et al. (2023) 仍未引用 [R2 指出，PARTIALLY RESOLVED]**\n三篇遗漏文献已引用（Park 2021, Wang 2024, Colas 2018），但 Becker-Ehmck et al. (2023) \"Multi-timestep models for MBRL\" 仍缺失，与论文主题直接相关。\n\n### Minor\n\n**W-M1. Abstract 统计数据过密**：~150 词包含 6+ 数字指标（14-19%, 26/29, AUROC=0.953, 2.78×, ρ>0.999, 100% sensitivity），建议精简至 2-3 个关键数字。\n\n**W-M2. Dual-critic convergence 叙事过于简化 [2/2 reviewer 共识]**：ρ > 0.999 是 asymptotic 结果；与 wide dual-critic 3/4 prevention 成功存在张力；主文 \"pessimism ineffective\" 需 nuance——min operation 可能通过非 pessimism 机制发挥作用。\n\n**W-M3. ManiSkill 和 Cheetah Run baseline eval 值缺失**：Table 1 中这些环境缺少 vanilla DreamerV3 baseline 参照值，读者无法判断相对性能。\n\n**W-M4. Abstract 中 \"isolate\" 携带因果含义**，与全文 \"strongest predictor\" 措辞不一致。\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 共识度 |\n|------|----|----|--------|\n| R1-N1 统计检验力 | RESOLVED | RESOLVED | **2/2 一致** |\n| R1-N4 单环境 | RESOLVED | RESOLVED | **2/2 一致** |\n| R1-W1 Factorial 混淆 | RESOLVED | RESOLVED | **2/2 一致** |\n| R1-W2 步数不对等 | STILL_OPEN | STILL_OPEN | **2/2 一致** |\n| R1-W3 Pathway B | RESOLVED | RESOLVED | **2/2 一致** |\n| R2-W1 TAWM 无实证 | STILL_OPEN | STILL_OPEN | **2/2 一致** |\n| R1-W4 Signed error | RESOLVED | RESOLVED | **2/2 一致** |\n| R2-W3 CIVO 区分 | — | RESOLVED | R2 独立确认 |\n| R3-W2 Abstract | — | RESOLVED | R2 独立确认 |\n| R2-W4 Bib | — | PARTIALLY | Becker-Ehmck 仍缺 |\n| R1-N3 Venue fit | Relevance 4/5 | STILL_OPEN (5/10) | **分歧** |\n| R2-N3 Actionable | — | STILL_OPEN (6/10) | R2 独立判定 |\n| N-new-1 Detector 样本量 | WARNING | AGREE | **2/2 一致** |\n| N-new-3 Dual-critic | MINOR | AGREE | **2/2 一致** |\n\n---\n\n## Reviewer Divergence\n\n**1. CoRL Relevance（R1: 4/5 vs R2: 2.5/5）**\n- R1：temporal abstraction 是 CoRL 核心话题，world-model RL 直接关联 robot control\n- R2：CIVO 恰恰在 robotics-relevant manipulation 中不出现，核心发现是 locomotion-specific，CoRL 社区更关心 contact-rich manipulation\n- **Director 判断**：R2 的论点更有说服力。ManiSkill negative results 是论文的 honest science，但客观上削弱了对 CoRL 的 relevance。CIVO 仅在 DMC locomotion 中复现，而 DMC locomotion 不是 CoRL 的核心关注点。综合评估 relevance 约 3/5。\n\n**2. Significance（R1: 3/5 vs R2: 2/5）**\n- R1：四级干预层级分析对社区有长期价值\n- R2：negative result + no reliable fix 的贡献模式在 deployment-oriented 社区价值有限；核心 takeaway 是 \"不要用\"\n- **Director 判断**：部分同意双方。四级干预分析的系统性是 genuine contribution，但论文的 actionable 输出确实有限。综合约 2.5/5。\n\n**3. Originality（R1: 4/5 vs R2: 3/5）**\n- R1：首个系统诊断 DreamerV3 变速想象失败的工作，CIVO 现象识别新颖\n- R2：方法论（factorial ablation）是标准做法，negative result 的原创性 credit 存在争议\n- **Director 判断**：CIVO 现象的识别和因果分离确实新颖（特别是 gradient magnitude ≠ causal importance 的发现），但方法论框架本身不新。综合约 3.5/5。\n\n---\n\n## Questions for Authors\n\n1. 如果 treatment 训练延长到 300K-500K 步，self-correction 是否会更普遍？exp_045 的数据是否可以报告？\n2. \"Feedback architecture as the structural factor\" 能否弱化为 \"hypothesized structural factor\"，或者是否有计划在 TD-MPC2 上验证？\n3. CIVO 在 locomotion 出现但 manipulation 不出现的 reward density 假说（Discussion \"a possible mediator is reward density\"），是否有更直接的证据？\n4. Online detector 的 FPR=22% 在实际部署中是否可接受？是否有降低误报率的方案？\n5. Wide dual-critic 3/4 CIVO prevention 的成功机制是什么？如果 ρ > 0.999 使 pessimism 无效，min operation 通过什么机制起作用？\n\n---\n\n## Missing References\n\n- **Becker-Ehmck et al. (2023)** \"Multi-timestep models for Model-based RL\" — 直接研究 multi-timestep world model，与论文主题高度相关，在 Round 1 已提出但仍未引用\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（5 warnings, 0 critical, 12 info）。\n\n**主要发现**：\n1. **[warning] 前 4 页无 display item**：连续 4 页纯文本，第一个视觉锚点（Table 1 + Figure 1）直到第 5 页才出现。对诊断/实证型论文，审稿人第一印象不利。建议将架构图或核心发现概览图提前到第 1-2 页。\n2. **[warning] 正文 display item 密度偏低**：8 页正文仅 4 个 display items（Table 1-2, Figure 1-2），实证型论文通常期望 5-8 个。\n3. **[warning] CIVO mechanism diagram (Figure 6) 被放在 Appendix**：这是论文最重要的概念可视化，审稿人在正文中看不到方法的直觉图示。强烈建议移入正文。\n4. **[warning] Appendix 页面空白**：Page 26 和 Page 33 有大面积空白。\n5. **[info] 图表质量良好**：Figure 1/2 使用彩色线条和清晰标注；Table 1-2 使用 booktabs 风格；ROC 曲线标注 AUC 和阈值点。\n\n---\n\n## Overall Assessment\n\n**评分: Weak Reject (5/10)**\n**置信度: High (4/5)**\n\n**与 Round 1 (Strong Reject, 4/10) 的变化**：论文在方法论和实验充分性方面取得了显著进步：\n\n| 维度 | Round 1 | Round 3 | 变化 |\n|------|---------|---------|------|\n| 统计检验力 | Critical (2-3 seeds) | Resolved (4 seeds, LOEO) | ▲▲ |\n| 环境覆盖 | Critical (1 env) | Resolved (5 envs) | ▲▲ |\n| NVE 验证 | Critical (post-hoc) | Resolved (LOEO, AUROC=0.981) | ▲▲ |\n| 模板合规 | Critical (desk reject) | Resolved (PMLR) | ▲▲ |\n| Venue fit | Critical | Still open but improved | ▲ |\n| Actionable 贡献 | Warning | Still open but improved | ▲ |\n| CIVO 区分 | Warning | Resolved | ▲▲ |\n\n**Round 1 的 4 个 critical issues 中 3 个已 resolved**（统计检验力、单环境、模板），第 4 个（venue fit）有改善但结构性矛盾未解。\n\n**核心矛盾**（影响从 Weak Reject 上升到 Borderline 的障碍）：\n1. **Venue fit**：论文的核心发现（CIVO）仅在 DMC locomotion 中成立，在 robotics-relevant manipulation 中不出现。CoRL 要求 \"focus on core robotics problems\"，当前论文更适合 ICML/NeurIPS 的 RL/world-model track。\n2. **贡献模式**：diagnostic negative result + partial mitigation + detection 的组合在 ML theory venue 可以接受，但对 CoRL 的 deployment-oriented 社区偏弱。Practitioner 的最佳策略仍然是 \"不要用 trained dt-embedding\"。\n\n**如果提交到 ICML/NeurIPS**：方法论评分会提升至 Borderline Accept (6/10)——factorial design 严谨、LOEO 验证有力、四级干预分析有系统性贡献、CIVO 与 compounding error 的区分清晰。Venue fit 和 actionable 贡献的约束消失。\n\n**综合维度评分**（Director 综合两位 Reviewer）：\n\n| 维度 | 评分 | 理由 |\n|------|------|------|\n| Originality | 3.5/5 | CIVO 现象新颖，gradient ≠ causal importance 有洞见，方法论框架标准 |\n| Quality | 3/5 | Factorial design 严谨，LOEO 有力，但 CIVO 仅 2/5 环境复现，部分配置样本量小 |\n| Clarity | 4/5 | 结构清晰，F1-F7 叙事好，33 页 appendix 详尽 |\n| Significance | 2.5/5 | 四级干预有系统贡献，但 locomotion-specific + no reliable fix 限制 impact |\n| Relevance | 3/5 | Temporal abstraction 与 CoRL 相关，但核心发现在 manipulation 不成立 |\n| Limitations | 4/5 | 诚实全面 |\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 约 150 词，长度合理。Robotics motivation 到位（首句）。\n- 统计数据过密（6+ 数字指标），建议精简至 2-3 个关键数字\n- \"isolate\" 一词与全文 \"strongest predictor\" 不一致\n\n### Introduction (Section 1)\n- Robotics framing 明显改善（DayDreamer, TD-MPC2 引用，temporal abstraction 的 robotics 需求）\n- Contribution 列表 4 项与正文一致\n- 最后一段 robotics relevance 论述合理但稍显牵强\n\n### Related Work (Section 2)\n- CIVO vs compounding error 区分清晰（控制实验 + signed error）\n- Park 2021, Wang 2024, Colas 2018 已引用\n- Becker-Ehmck 2023 仍缺\n\n### Experimental Setup (Section 3)\n- Factorial design 展示专业，四因素清晰\n- Primary vs secondary comparison 标注到位\n- SGS, TCN, RAVE, Dual-critic 方法描述完整\n- 缺少对 105K vs 505K 步数选择的 rationale 讨论\n\n### Results (Section 4)\n- F1-F7 因果链叙事清晰\n- Table 1 信息密度高，灰色标记 CIVO-positive 有效\n- ManiSkill negative results 诚实呈现\n- 缺少 Cheetah/ManiSkill baseline eval 参照值\n- Online detector 评估样本量不足（n=14, 5 正例）\n- Dual-critic ρ > 0.999 结论需 nuance\n\n### Discussion (Section 5)\n- CIVO mechanism 段落简洁准确\n- Practitioner guidelines 可操作（NVE ≥ 1.5×, embedding freezing）\n- \"Implications for robot learning\" 提供了 reward density 假说\n- \"structural factor\" 措辞过强（无 MPC 实验验证）\n\n### Conclusion (Section 6)\n- Limitations paragraph 诚实（4 seeds, architecture, real-robot）\n- 措辞恰当，未过度泛化\n\n### Appendix\n- 33 页，极其详尽（完整 42 配置结果、NVE sensitivity、LOEO、gradient decomposition、entropy dynamics、dual-critic analysis）\n- Figure 6 (CIVO mechanism diagram) 应移入正文\n- 部分页面空白可优化",
    "project": "event-gated-adaptive-horizon",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject"
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-24T07:19:53.336272+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5e879064da2e47dad864c1f891eb37a8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4104
}
```

</details>

---


### Assistant

_source line 254 · 2026-05-24T07:20:12.174090+00:00_

Round 3 审稿完成。

**结果：Weak Reject (5/10)**，较 Round 1 (Strong Reject, 4/10) 提升一档。

**关键变化**：
- Round 1 的 4 个 critical issues 中 **3 个 resolved**（统计检验力、单环境泛化、模板合规）
- **Venue fit 改善但未解决**：ManiSkill 实验增加了 robotics 相关性，但 CIVO 仅在 locomotion 中出现、manipulation 中不成立，这个结构性矛盾使论文在 CoRL scope 上仍处于边缘
- **贡献模式改善但偏弱**：从纯诊断升级为诊断+干预+检测，但核心结论仍是 "没有可靠解决方案"

**两个 warning 级残留问题**（2/2 reviewer 共识）：步数不对等未显式讨论、TAWM "structural factor" 无实验验证

**建议**：如提交 ICML/NeurIPS RL track，venue fit 和 actionable 约束消失，评分可上升至 Borderline Accept (6/10)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 21

## Round 21

2 recorded events


### User

_source line 255 · 2026-05-24T07:20:13.461301+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- 7 个 issue 中 **5 个 AGREE**（R1-N1/N4/W1/W3/W4 resolved，R1-W2/R2-W1 still open）
- 新问题中 **N-new-1 AGREE**（detector 样本量）、**N-new-2 REBUT**（IQM 对 n≤2 配置无意义，不必所有比较都报告）、**N-new-3 AGREE**（dual-critic convergence 叙事过度简化）
- **主要分歧在 Relevance**（R1: 4/5 vs R2: 2.5/5）和 **Significance**（R1: 3/5 vs R2: 2/5）——CIVO 的 locomotion-specificity 使其对 CoRL 的 manipulation/deployment 社区价值有限

---

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 意见的交叉回应

---

## 1. R1-N3 [STILL_OPEN]: CoRL venue fit 不足

**[REBUT] R2-Issue-N3**

R2 的核心论点是 ManiSkill non-CIVO 结果反向证明 CIVO 与 robotics 无关。这一推理有逻辑跳跃：

1. **Locomotion IS a core robotics problem.** Walker Walk 和 Cheetah Run 是标准的连续控制 benchmark，直接对应双足/四足机器人控制。CIVO 在运动任务中 100% 复现（6/6 seeds across 2 environments）对 robotics locomotion 社区有直接实践警示价值。

2. **Temporal abstraction 是 CoRL 核心议题。** Variable-rate planning 对 real-robot deployment 至关重要（不同关节/层级需要不同控制频率）。论文诊断的是：为什么这一在 MPC 中有效的技术在 imagination-based actor-critic 中失败——这对准备在 DreamerV3 类系统中部署 temporal abstraction 的 robotics 团队有直接意义。

3. **ManiSkill non-CIVO 不削弱而是增强论文价值。** 它提供了 discriminative validity——告诉读者 CIVO 在何时不需要担心。一个只报告 "everywhere fails" 的论文反而更可疑。

4. **"Bookend" framing 的批评有一定道理**，但 Section 5 Discussion 的机制分析（MPC re-planning vs imagination bootstrapping, Section 5 paragraphs 1-3）和 online detector（Section 4.7）都是面向 deployment 的贡献，不仅仅是开头结尾提及 robotics。

**但我部分同意 R2**: 论文中间确实有 ~3 页（Sections 4.2-4.5 的 factorial ablation 细节）是纯 RL 方法论分析，缺少 robotics grounding。如果作者能在 Section 4.3 的 ManiSkill 讨论中增加一段关于为什么 locomotion dynamics（contact-rich, periodic gait patterns）特别容易触发 CIVO 的机制讨论，venue fit 会更强。

**我的评分**: Venue Fit 6.5/10（比 R2 的 5/10 高，但承认存在改善空间）。

---

## 2. R2-N3 [STILL_OPEN]: 纯诊断缺乏 actionable solution

**[AGREE] R2-Issue-N3，但程度不同**

R2 的观察在事实层面正确：Table 2 (Section 4.6) 核心结论确实是 "No level reliably eliminates CIVO across environments"，最有效方案是 embedding removed (100%) = 不用该功能。

但我认为 R2 低估了三个 actionable 贡献：

1. **NVE online detector**（Section 4.7, Algorithm 1 in Appendix F）是可直接部署的工具——TPR=5/5, FPR=2/9，虽然样本量小（我在 N-new-1 中已指出），但提供了实时监控 CIVO onset 的方法。

2. **Min + increased capacity 实现 recovery**（Section 4.8, Appendix G）：wide dual-critic 在 Walker 上 3/4 prevention rate，narrow dual-critic 即使不 prevent 也能 recover（16-19× recovery ratio）。这是具体的架构建议，不只是 "don't use it"。

3. **Frozen embedding 作为安全替代**（Table 1: 5/7 prevention rate, 71%）：虽然 eval 较差，但对需要 temporal conditioning 又不想触发 CIVO 的场景提供了中间方案。

**综合看**: R2 说论文更适合 ICML/NeurIPS，这个建议有道理——diagnostic negative result 在方法论 venue 的 impact 更直接。但 CoRL 也接受 methodology 贡献，前提是 robotics relevance 清晰。问题不在于论文没有 actionable solution，而在于 actionable solution（NVE detector, min+capacity）的统计支撑较弱（小样本），且最强方案（wide dual-critic）不跨环境泛化（Cheetah 0/1）。

**我的评分**: 贡献度 6.5/10（与 R2 的 6/10 接近）。

---

## 3. R2-W3 [RESOLVED]: CIVO 与 compounding error 区分

**[AGREE] R2-W3**

同意 R2 的 RESOLVED 判定。Section 2 (Related Work) 清晰区分了 CIVO 和 standard compounding error。Appendix D.1 的 signed reward error 分析（Table 15）提供了经验性证据：trained-embedding model 在 dt=2 时低估奖励（mean signed error = -0.150），排除了 observation-level overprediction。CIVO 的机制（value function internalization of reward prediction gap → positive feedback loop）与 compounding error（累积 model error）在 pathway 上有本质区别。

---

## 4. R2-W4/R3-W3 [PARTIALLY RESOLVED]: Becker-Ehmck 2023 缺失

**[AGREE] R2-W4**

如果 Becker-Ehmck 2023 确实涉及 temporal abstraction in model-based RL（如 "Temporal Difference Learning for Model Predictive Control" 或类似工作），且与论文的 variable-rate imagination mechanism 直接相关，则应被引用。Bib 从 77 条清理至 44 条是正确方向，但清理过程不应遗漏直接相关的工作。

我无法独立验证该引用的具体内容，但 R2 连续两轮指出同一遗漏，说明这不是边缘情况。建议作者补充。

---

## 5. R3-W2 [RESOLVED]: Abstract

**[AGREE] R2-R3-W2**

确认 Abstract 约 150 词，包含 robotics motivation。

---

## 6-7. R3-N1, R3-N3: 模板和页数

**[AGREE]**

已确认使用 `\usepackage{corl_2026}` 模板，8 页正文。

---

## 对 R2 额外发现的回应

### E1 [minor]: Abstract 统计数据过密

**[AGREE] R2-E1**

Abstract 包含至少 6 个数值指标：14-19%, 26/29, AUROC=0.953, 2.78×, ρ > 0.999, 100%。对于 ~150 词的 abstract，数字密度确实过高，影响可读性。建议保留 2-3 个最关键的数字（如 AUROC=0.953 和 "all variable-rate configurations degrade"），其余移至正文。但这是写作偏好问题，不影响接收决定。

### E2 [minor]: F1-F7 与标准编号混用

**[REBUT] R2-E2**

Section 编号为 4.1-4.8，F1-F7 是 findings 的逻辑编号。这在 findings-based diagnostic paper 中是合理的组织方式——类似于 empirical study 按 research question (RQ1-RQn) 组织 results section。Section 4.1 标题为 "F1: All Variable-Rate Configurations Degrade"，读者可以通过 section 编号 (4.1) 导航，也可以通过 finding 编号 (F1) 追踪论证链。两套编号不冲突。

### E3 [minor]: Limitations 作为 Conclusion paragraph

**[AGREE] R2-E3**

从 LaTeX 源码确认：Limitations 是 Section 6 (Conclusion) 内的 `\paragraph{Limitations.}`，而非独立 section。CoRL 2024/2025 的 submission guidelines 是否要求 standalone Limitations section 需要核实。如果 CoRL CFP 要求独立 Limitations section，当前格式不合规。即使不硬性要求，独立 section 也是更安全的选择。

### N1 [warning]: ManiSkill baseline eval 缺失

**[AGREE] R2-N1**

Table 1 的 ManiSkill 条目（PickCube 019b, StackCube 049, PegInsertion 050）缺少对应的 vanilla DreamerV3 baseline 评分。虽然脚注 c 提到 "NVE normalized against exp_019a_v2 (vanilla DreamerV3 on PickCube-v1)"，但 019a_v2 的 eval 值未出现在 Table 1 中。读者无法直接判断 ManiSkill 上 treatment 的 degradation 程度。Cheetah Run baseline（010b 对应的 untreated baseline）同理。

这是我在 Round 3 审查中未单独提出但确实存在的问题。Table 1 应补充 ManiSkill 和 Cheetah 的 baseline 行。

### N2 [warning]: Cheetah Run baseline 缺失

**[AGREE] R2-N2**

同上。Table 1 仅包含 Cheetah treated (010b) 和 frozen (046)，无 untreated baseline 行。Table 3 (Appendix) 可能有，但主表应自足。

### N3 [minor]: 1-seed 条目统计无意义

**[AGREE] R2-N3**

Table 2 中 TCN σ=0.1（1 seed, 1/1, 100%）和 TCN σ=1.0（1 seed, 1/1, 100%）的 prevention rate 在统计上无意义。我在 Round 3 审查中未专门提出此点，但 R2 的观察正确。这些条目要么应标注 "n=1, exploratory"，要么从 Table 2 移至 Appendix。Table 2 中保留 n≥2 的条目并注明 "*single-seed pilot, not statistically interpretable*" 是最低要求。

---

## 对 R2 总评的回应

**Venue Fit 5/10**: 我给 6.5/10。R2 的 "CIVO 与 robotics manipulation 无关" 论点过强——locomotion 是 core robotics，temporal abstraction 直接关联 deployment。但 "bookend" framing 批评有效。

**贡献度 6/10**: 我给 6.5/10。基本同意。NVE detector 和 min+capacity finding 提供了部分 actionable value，但整体贡献确实偏 diagnostic。

**写作质量 7/10**: 同意。论文结构清晰但 abstract 数字过密、baseline 行缺失。

**"论文更适合 ICML/NeurIPS"**: 这是一个合理但非决定性的观点。CoRL 历史上接受过 methodology-focused RL 论文（如 world model analysis、sim-to-real failure mode 研究）。关键在于作者是否能在 rebuttal 中加强 robotics grounding——如果能增加 1-2 段关于 locomotion-specific CIVO 的 robotics 机制讨论（为什么 gait patterns + contact dynamics 使 RSSM reward head 特别脆弱），venue fit 可以从 borderline 提升到 acceptable。

**"核心矛盾：CIVO 是 locomotion-specific negative result，robotics framing 装饰性"**: 部分同意 framing 可以更深入，但 "装饰性" 一词过强。论文的核心发现（imagination-based bootstrapping vs MPC re-planning 的结构性差异）对 robotics deployment 决策有直接指导意义。


---

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **7 个 R2 要点中 AGREE 5 个，REBUT 2 个**
- REBUT 的两个点：(1) CoRL venue fit — R2 低估了 locomotion 作为 core robotics 的相关性，以及 ManiSkill non-CIVO 结果的 discriminative validity 价值；(2) F1-F7 编号方式 — findings-based structure 在 diagnostic paper 中合理
- AGREE 的重点：贡献度偏 diagnostic（6.5/10）、Becker-Ehmck 引用缺失、ManiSkill/Cheetah baseline eval 在 Table 1 中缺失、1-seed 条目统计无意义、abstract 数字过密
- 与 R2 最大分歧在 venue fit 评分（我给 6.5 vs R2 的 5）和 "装饰性 framing" 的判断

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 256 · 2026-05-24T07:20:48.647348+00:00_

Round 3 审稿流程已完成。

**流程回顾**：
- Step 1：R1（方法/实验）+ R2（Venue/贡献/写作）独立初审 ✓
- Step 2：交叉分享 + 逐条回应 ✓
- Step 3：收敛判断——所有 issue 状态达成共识，评分分歧有充分论据，1 轮收敛 ✓
- Step 4：合成报告 + issue tracker 更新 + 投递 ✓

**Round 3 审稿结果**：**Weak Reject (5/10)**，较 Round 1 (Strong Reject, 4/10) 提升 1 分。

**改进确认**：Round 1 的 4 个 critical issues 中 3 个 resolved（统计检验力、单环境、模板合规），第 4 个（venue fit）有实质改善。

**残留问题**：
- 2 个 structural issues（venue fit + actionable 贡献模式）——这是 CoRL-specific 的约束，非方法论缺陷
- 2 个 warning（步数不对等讨论缺失 + TAWM "structural factor" 措辞过强）
- 1 个新 warning（online detector 小样本）
- 1 个 partial（Becker-Ehmck 引用）

**Reviewer 分歧**：主要在 Relevance（R1: 6.5/10 vs R2: 5/10）。R1 认为 locomotion 是 core robotics、ManiSkill non-CIVO 提供 discriminative validity；R2 认为 CIVO 恰恰在 manipulation 中不成立，削弱 CoRL relevance。Director 综合为 Relevance 3/5。

报告已投递至 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 22

## Round 22

28 recorded events


### User

_source line 257 · 2026-05-24T09:24:36.710254+00:00_

[Round 4 - 继续审稿]
论文已更新。请基于上一轮审稿意见，重点审查修改是否充分回应了之前提出的问题。
重点关注：
1. 上轮提出的问题是否已充分解决
2. 修改是否引入了新问题
3. 整体评分是否需要调整

上一轮审稿报告: `projects/event-gated-adaptive-horizon/artifacts/review_reports/round_3.md`
跨轮次问题追踪: `projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml`
请用 read_local_file 先读这两个文件,重点验证 status=in_progress 的 issue 是否已被充分修复。
派 Reviewer 时把 open/in_progress 的 issue 列表附在任务里,要求逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由。

[论文提交]
- 项目: event-gated-adaptive-horizon
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex
- 目标 venue: ICML 2026
- 截止日期: 未提供，请自行调研
- **引用验证**: ❌ 未启用

请继续审稿流程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-24T09:24:57.575330+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-24T09:24:58.128741+00:00_

1	issues:
2	  - id: "R1-N1"
3	    summary: "统计检验力严重不足：2-3 seeds 无法支撑 causal factor 声明"
4	    category: experiment
5	    severity: critical
6	    status: resolved
7	    first_raised_round: 1
8	    last_seen_round: 3
9	    mentions:
10	      - round: 1
11	        reviewers: [1, 2, 3]
12	        note: "三位 reviewer 均认同统计效力不足"
13	      - round: 3
14	        reviewers: [1, 2]
15	        note: "两位 reviewer 一致判定 RESOLVED。Seeds 增至 4，语言改为 strongest predictor，LOEO AUROC=0.981，IQR 报告。残留小问题：Abstract 中 isolate 一词仍携带因果含义。"
16	    action_items:
17	      - round: 1
18	        action: "补 seeds 到 4 per key config"
19	        assigned_to: agent
20	        status: done
21	      - round: 1
22	        action: "弱化因果语言: causal factor → strongest predictor"
23	        assigned_to: paper_agent
24	        status: done
25	      - round: 1
26	        action: "统计报告改用 IQM + bootstrap CI per Agarwal et al. 2021"
27	        assigned_to: paper_agent
28	        status: done
29	    resolution: "Seeds 增至 4，因果语言全面弱化为 strongest predictor，LOEO 交叉验证 AUROC=0.981，IQM + bootstrap CI 报告完整。"
30	    resolution_round: 3
31	
32	  - id: "R1-N2"
33	    summary: "NVE 阈值 1.5× 为 post-hoc 选择，88.9% accuracy 是训练准确率，无独立验证"
34	    category: method
35	    severity: critical
36	    status: resolved
37	    first_raised_round: 1
38	    last_seen_round: 1
39	    mentions:
40	      - round: 1
41	        reviewers: [1, 2, 3]
42	        note: "三位 reviewer 一致认为 post-hoc"
43	    action_items:
44	      - round: 1
45	        action: "LOEO cross-validation: mean AUROC 0.981"
46	        assigned_to: agent
47	        status: done
48	    resolution: "LOEO 交叉验证完成：3 环境 leave-one-out，mean AUROC 0.981，θ=1.5 在全部 fold 最优范围。论文措辞已改为 in-sample + LOEO cross-validated。"
49	    resolution_round: 1
50	
51	  - id: "R1-N3"
52	    summary: "CoRL venue fit 严重不足：全文无 robotics 实验/讨论"
53	    category: framing
54	    severity: critical
55	    status: in_progress
56	    first_raised_round: 1
57	    last_seen_round: 3
58	    mentions:
59	      - round: 1
60	      
…[truncated 15105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-24T09:24:58.129190+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ICML 2026 call for papers submission guidelines deadline page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ICML 2026 call for papers submission guidelines deadline page limit"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-24T09:25:03.052112+00:00_

Web search results for query: "ICML 2026 call for papers submission guidelines deadline page limit"

Links: [{"title":"ICML 2026 Call for Papers","url":"https://icml.cc/Conferences/2026/CallForPapers"},{"title":"ICML 2026 Call For Position Papers","url":"https://icml.cc/Conferences/2026/CallForPositionPapers"},{"title":"ICML 2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"},{"title":"2026 Dates and Deadlines","url":"https://icml.cc/Conferences/2026/Dates"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"Submission and Formatting Instructions for International ...","url":"https://media.icml.cc/Conferences/ICML2026/Styles/example_paper.pdf"},{"title":"ICML 2026 Call for Post-Conference Workshops","url":"https://icml.cc/Conferences/2026/CallForWorkshops"},{"title":"ICML 2026: Strictest New Rules Ever - LLMs Banned as Authors, Papers with AI Abuse Rejected","url":"https://eu.36kr.com/en/p/3540848514510723"},{"title":"ICML 2026","url":"https://icml.cc/"},{"title":"ICML 2026 Peer Review FAQ","url":"https://icml.cc/Conferences/2026/PeerReviewFAQ"}]

Based on the search results, here's the information about ICML 2026 call for papers submission guidelines:

## Submission Deadline

ICML 2026 paper submissions deadline is January 28, 2026.

## Page Limit

Papers must be prepared and submitted as a single file: 8 pages for the main paper, with unlimited pages for references, the impact statement, and appendices. Additionally, the final versions of accepted papers will be allowed one extra page for the main paper.

## Key Submission Guidelines

- There will be no separate deadline for the submission of supplementary material (all supplementary materials must be submitted by the full paper deadline)
- All papers will be reviewed in a double-blind process and accepted papers will be presented at the conference
- All submissions must be anonymized and may not contain any information with the
…[truncated 284 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "WebSearch",
  "elapsed_ms": 4922
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-24T09:25:38.279807+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-24T09:25:39.434668+00:00_

1	\documentclass{article}
2	
3	% Load xcolor before corl_2026 (which loads color internally)
4	\usepackage[table]{xcolor}
5	\usepackage{corl_2026}
6	
7	\usepackage[utf8]{inputenc}
8	\usepackage[T1]{fontenc}
9	\usepackage{amsmath,amssymb}
10	\usepackage{booktabs}
11	\usepackage{multirow}
12	\usepackage{graphicx}
13	\graphicspath{{../../artifacts/}}
14	\usepackage{colortbl}
15	\usepackage{caption}
16	\usepackage{subcaption}
17	\usepackage{array}
18	\usepackage{enumitem}
19	\usepackage{wrapfig}
20	\usepackage{algorithm}
21	\usepackage{algorithmic}
22	
23	% Custom commands
24	\newcommand{\dt}{\mathrm{dt}}
25	\newcommand{\nve}{\mathrm{nve}}
26	% SGS result values (018 seed 1: partial mitigation; seed 2: collapsed — 0/3 CIVO elimination)
27	\newcommand{\sgseval}{448.3}
28	\newcommand{\sgsnve}{1.66}
29	\newcommand{\sgsclaim}{reduced CIVO severity in one of two Walker seeds but eliminated it in neither (0/3 across environments)}
30	\newcommand{\ie}{\textit{i.e.}}
31	\newcommand{\eg}{\textit{e.g.}}
32	\newcommand{\cf}{\textit{cf.}}
33	\newcommand{\etal}{\textit{et al.}}
34	
35	\title{Why Temporal Abstraction Can Fail in Imagination-Based RL:\\
36	A Diagnostic Analysis of Variable-Rate DreamerV3}
37	
38	\author{
39	  Anonymous Authors
40	}
41	
42	\begin{document}
43	\maketitle
44	
45	\begin{abstract}
46	\input{sections/abstract_body}
47	\end{abstract}
48	
49	\keywords{World Models, Temporal Abstraction, Value Overestimation, DreamerV3}
50	
51	% --- INTRODUCTION ---
52	\input{sections/introduction}
53	
54	% --- RELATED WORK ---
55	\input{sections/related_work}
56	
57	% --- METHODOLOGY ---
58	\input{sections/methodology}
59	
60	% --- RESULTS ---
61	\input{sections/results}
62	
63	% --- ANALYSIS ---
64	\input{sections/analysis}
65	
66	% --- CONCLUSION ---
67	\input{sections/conclusion}
68	
69	% no \bibliographystyle needed — corl_2026.sty sets it automatically
70	\bibliography{references}
71	
72	% --- APPENDIX ---
73	\appendix
74	\input{sections/appendix}
75	
76	\end{document}
7
…[truncated 2 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 1154
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-24T09:25:39.585672+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex"
  }
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-24T09:25:39.586058+00:00_

1	World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales. We find that $\Delta t$-conditioning, effective in model-predictive control (MPC), cannot transfer to imagination-based actor-critic training: every variable-rate DreamerV3 configuration degrades to 14--19\% of baseline. Factorial diagnostics on two continuous-control tasks identify trained temporal embedding with multi-rate data exposure as the strongest predictor of this failure---\emph{conditioning-induced value overestimation} (CIVO; 27/30, AUROC${=}0.957$, LOEO cross-validated). The RSSM develops a reward prediction gap at $\Delta t{>}1$ that the critic internalizes as optimistic values; the contrast with MPC identifies feedback architecture as a hypothesized structural factor. No tested intervention across four levels (gradient, output, representation, architecture) reliably eliminates CIVO: dual critics converge in pure imagination, rendering Double Q pessimism ineffective, though min $+$ increased capacity enables recovery.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-24T09:25:39.638051+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-24T09:25:39.638613+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	World-model reinforcement learning enables sample-efficient learning directly on physical hardware \citep{wu2023daydreamer, hansen2024tdmpc2}. Real robotic tasks demand temporal abstraction: manipulation requires fast reactive grasping alongside slow approach planning, locomotion involves gait phases at different frequencies, and sim-to-real transfer must handle $\dt$ mismatches between simulation and hardware. TAWM \citep{nhu2025tawm} shows that conditioning a world model on step size $\dt$ yields consistent gains within TD-MPC2's MPC framework \citep{hansen2024tdmpc2}. Can the same $\dt$-conditioning bring temporal abstraction to imagination-based actor-critic methods like DreamerV3 \citep{hafner2023dreamerv3}, where policies are trained entirely in imagined rollouts?
5	
6	We find that it cannot. Every variable-rate configuration degrades performance catastrophically (14--19\% of baseline). Through a factorial analysis on Walker Walk \citep{tassa2018dmcontrol}, we isolate the combination of a \emph{trained} $\dt$-embedding and multi-rate data exposure as the strongest predictor. This combination enables the RSSM reward head to develop a $2.78\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$, which the critic internalizes as optimistic value estimates, a failure mode we term \emph{conditioning-induced value overestimation} (CIVO), analogous to delusional bias \citep{lu2018nondelusional} but model-induced rather than policy-class-induced. A normalized value-to-eval (NVE) threshold of $\geq 1.5\times$ achieves 27/30 classification ($n{=}30$, two environments, AUROC${=}0.957$, in-sample; LOEO cross-validated, Appendix~Table~\ref{tab:nve_loeo}).
7	Gradient decomposition reveals that gradient magnitude does not predict causal importance: the reward head contributes 38--49\% of $\nabla_\theta e_{\dt}$ yet reward-only stopping fails, while the observation decoder (16--22\%) carries the critical signal. A four-l
…[truncated 2311 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-24T09:25:51.690792+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-24T09:25:52.042748+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{CIVO mechanism.}
5	The RSSM develops a $2.78\times$ reward prediction gap under trained conditioning (Table~\ref{tab:rssm_fidelity}), analogous to delusional bias \citep{lu2018nondelusional}. Gradient magnitude $\neq$ causal importance: the reward head (38--49\% of $\nabla_\theta e_{\dt}$) fails when blocked alone; the observation decoder (16--22\%) carries the critical signal; full-pathway SGS (0/3) confirms forward-pass conditioning as the irreducible vulnerability. CIVO is upstream of estimation error---dual critics converge (\S\ref{sec:arch_results})---so standard corrections are inapplicable; MPC re-planning prevents accumulation (Appendix~\ref{sec:mpc_immune}).
6	
7	\paragraph{Practitioner guidelines.}
8	Monitor via NVE diagnostic ($\geq 1.5\times$, AUROC${=}0.957$; Table~\ref{tab:nve_loeo}). Freezing the $\dt$-embedding converts CIVO onset (7/7 trained locomotion, NVE $1.53$--$108\times$) to transient spikes that self-correct within 20K steps (2/3 frozen Walker, $1.71$--$1.88\times$; 0/2 frozen Cheetah); untreated, extreme CIVO ($70.6\times$) causes irrecoverable damage (Appendix~\ref{sec:appendix_analysis}).
9	
10	\paragraph{Training horizon.}
11	Our primary analysis uses 105K steps, sufficient to observe CIVO onset (45K--65K) and classify trajectories. Extended training (${\sim}$302K steps, one seed) shows complete self-recovery after approximately 170K additional steps post-onset---at substantial computational cost that the frozen $\dt$-embedding diagnostic eliminates entirely (Appendix~\ref{sec:extended_training}).
12	
13	\paragraph{Implications for robot learning.}
14	No $\dt$-embedding-dependent CIVO was observed in manipulation (Table~\ref{tab:cross_domain}). Both domains use dense shaped rewards, so reward sparsity cannot explain the boundary. Possible mediators include action-space periodicity, observation structure, and continuous versus contact-gated dynamics; the precise factors remai
…[truncated 23 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-24T09:25:52.043164+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-24T09:25:52.595867+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\nve$, \S\ref{sec:metrics}).
5	
6	%% ============================================================
7	%% TABLE 1: Main results summary
8	%% ============================================================
9	
10	\begin{table*}[t]
11	\centering
12	\caption{Key configurations and outcomes. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded. Complete results for all 43 configurations in Table~\ref{tab:complete_results}.}
13	\label{tab:main_results}
14	\footnotesize
15	\setlength{\tabcolsep}{4pt}
16	\begin{tabular}{llcccccl}
17	\toprule
18	\textbf{Exp} & \textbf{Config} & \textbf{dt\_emb} & \textbf{Sub} & \textbf{H} & \textbf{Eval@final} & \textbf{NVE} & \textbf{Outcome} \\
19	\midrule
20	001 & Baseline ($\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
21	\midrule
22	\rowcolor{gray!15}
23	008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\times$ & Full collapse \\
24	008f & No dt\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\times$ & Healthy \\
25	008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\times$ & Healthy \\
26	015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\times$ & Grad.\ starvation \\
27	022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\times$ & No CIVO \\
28	\midrule
29	\multicolumn{8}{l}{\textit{Cross-environment validation}} \\
30	\rowcolor{gray!15}
31	010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\times$ & Collapsed \\
32	019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\times$$^c$ & Transient onset \\
33	049 & StackCube-v1 & trn & 
…[truncated 1044 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-24T09:25:52.596377+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-24T09:25:53.229135+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We identify trained $\dt$-embedding with multi-rate data exposure as the strongest predictor of CIVO in DreamerV3 (27/30, AUROC${=}0.957$; LOEO cross-validated). No tested intervention reliably eliminates CIVO; in pure imagination, dual critics converge ($\rho > 0.999$), rendering Double Q pessimism ineffective. The feedback architecture---MPC re-planning versus imagination-based bootstrapping---is the hypothesized structural factor. Empirical validation on MPC-based architectures (e.g., TD-MPC2) remains future work.
5	
6	\paragraph{Limitations.}
7	Our analysis covers proprioceptive locomotion (DMC) and simulated manipulation (ManiSkill) but does not test pixel-based observations, Atari benchmarks, or real-robot deployments where sensor noise and actuation latency introduce additional confounds.
8	All experiments use DreamerV3's RSSM; whether CIVO manifests in other imagination-based architectures (e.g., IRIS \citep{micheli2023iris} or latent-space planners beyond TD-MPC2) remains open.
9	We characterize CIVO under fixed-$\dt$ subsampling; learned temporal gates warrant separate study.
10	Statistical power with 4 seeds per configuration is limited \citep{colas2018seeds}; the NVE threshold (LOEO AUROC${=}0.988$) may require recalibration for different reward scales.
11	Code: upon acceptance.
12	\label{sec:limitations}
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 632
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-24T09:25:53.378060+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex",
  "offset": "50",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex",
    "offset": "50",
    "limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-24T09:25:53.436568+00:00_

50	\label{sec:dual_critic_method}
51	
52	To test whether standard overestimation countermeasures address CIVO, we conduct a $2{\times}2$ factorial: \{single, dual\} $\times$ \{narrow (${\sim}1.2$M), wide (${\sim}2.4$M)\} critic parameters. The dual-critic variant follows TD3 \citep{fujimoto2018td3}: two independent value heads trained on shared RSSM features, with the actor optimizing $\min(v_1, v_2)$. The wide variant doubles hidden dimensions to control for capacity independently of the min operation.
53	
54	\subsection{Environment and Training Details}
55	\label{sec:env_details}
56	
57	All experiments use Walker Walk and Cheetah Run from the DeepMind Control Suite (DMC; \citealt{tassa2018dmcontrol}) with proprioceptive observations, chosen for their contrasting dynamics (6-joint biped vs.\ 2-joint runner). Walker Walk serves as the primary environment with the full factorial design; Cheetah Run serves as a severity-dependent generalization probe: CIVO manifests at $8$--$70\times$ NVE on Cheetah versus $2$--$5\times$ on Walker, testing whether interventions transfer under amplified severity rather than replicating the full factorial. The baseline runs for 500K steps (peak return 970.4); treatments run for 105K steps, sufficient to observe collapse onset. All hyperparameters follow the DreamerV3 defaults \citep{hafner2023dreamerv3} without task-specific tuning ($d{=}32$ temporal embedding; full hyperparameters in Appendix~\ref{sec:hyperparameters}). Training uses a single NVIDIA RTX PRO 6000 GPU (${\sim}80$ GPU-hours total). The codebase extends the official DreamerV3 implementation\footnote{\url{https://github.com/danijar/dreamerv3}, accessed March 2026.} with the variable-rate modules described in \S\ref{sec:variable_rate}.
58	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 58
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-24T09:25:58.557771+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "offset": "150",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "offset": "150",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-24T09:25:58.608436+00:00_

150	%% Forward-pass interventions
151	%% ============================================================
152	
153	\subsection{Forward-Pass Interventions}
154	\label{sec:forward_results}
155	
156	We test two forward-pass alternatives (Table~\ref{tab:intervention_hierarchy}). \textbf{RAVE} (value-level capping) fails: the EMA anchor tracks biased values during CIVO onset. \textbf{TCN} (representation-level noise) suppresses CIVO in 2 of 4 Walker seeds at $\sigma{=}0.2$ (NVE $< 1.0\times$, eval 45--91\%), but remaining seeds show runaway escalation, suggesting TCN gates rather than attenuates CIVO. Cross-environment transfer fails: Cheetah effective dose ($\sigma{=}1.0$) causes policy erosion to 15\% baseline; PickCube 0/1 (Appendix~\ref{sec:tcn_cross_env}). TCN is a \emph{diagnostic probe}, not a deployable mitigation.
157	
158	%% ============================================================
159	%% Architecture-Level Ablation
160	%% ============================================================
161	
162	\subsection{Architecture-Level Ablation}
163	\label{sec:arch_results}
164	
165	\paragraph{Critic convergence in pure imagination.}
166	Across all dual-critic configurations ($n{=}7$), critics trained on shared RSSM features converge ($\rho > 0.999$), with pessimism at 3--4\% of the independent-critic bound (\S\ref{sec:dual_critic_method}). Pessimistic estimation is thus ineffective; the min operation in wide dual-critic may instead regularize through gradient diversity (Appendix~\ref{sec:dual_critic_appendix}).
167	
168	\paragraph{$2{\times}2$ factorial: recovery vs.\ prevention.}
169	Min drives recovery: narrow dual-critic (${\sim}1.2$M) recovers fully (${\sim}16$--$19\times$ recovery ratio) despite $2\times$ fewer parameters. Prevention requires min $+$ capacity: wide dual-critic maintains $\nve \leq 1.4\times$ (3/3 prevention, 1/3 non-CIVO collapse). Cross-environment transfer is limited (Appendix~\ref{sec:dual_critic_appendix}).
170	
171	%% ==============================
…[truncated 625 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-24T09:27:10.888689+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "4",
  "text": "## Round 4 修订评估任务 — Reviewer 1（方法严谨性 + 残留问题验证）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex`\n**目标 Venue**: ⚠️ ICML 2026（从 CoRL 2026 转投）\n**Deadline**: 2026-01-28（已过期；可能处于 rebuttal 阶段或准备下一轮投稿）\n**页数限制**: 8 页正文 + unlimited appendix/references\n**模板**: 应使用 ICML 2026 官方样式（当前仍为 corl_2026，需核实）\n**匿名规则**: Double-blind\n**审查侧重**: 方法严谨性、Round 3 残留问题验证\n\n### 背景\n\nVenue 从 CoRL 2026 改为 ICML 2026。Round 3 评分 Weak Reject (5/10)，主因是 CoRL venue fit 和 actionable contribution 问题。转投 ICML 后需重新评估。\n\n### 必须逐条检查的 Issue（Round 3 open/in_progress）\n\n**1. R1-W2 / REV-2 [warning, in_progress]: 105K vs 505K 步数不对等**\n- Round 3 问题：未显式讨论步数不对等，exp_045 长跑数据未呈现\n- **已知修改**：Discussion 新增 \"Training horizon\" 段落，提及 \"Extended training (~302K steps, one seed) shows complete self-recovery after approximately 170K additional steps post-onset\"\n- **检查要点**：这段讨论是否充分回应了问题？302K 单 seed 数据是否在 Appendix 呈现？\"sufficient to observe collapse onset\" 的论证是否有力？1/4 self-correction 现象是否被合理讨论？\n\n**2. R2-W1 [warning, in_progress]: TAWM 对比无实证，\"structural factor\" 过强**\n- Round 3 问题：Abstract/Conclusion 称 \"the structural factor\" 但无 MPC 实验\n- **已知修改**：Abstract 改为 \"a hypothesized structural factor\"；Conclusion 改为 \"hypothesized structural factor. Empirical validation on MPC-based architectures (e.g., TD-MPC2) remains future work.\"\n- **检查要点**：措辞是否已充分弱化？全文是否一致使用 \"hypothesized\"？是否还有其他位置仍用 \"the structural factor\"？\n\n**3. R3-N-new-1 [warning, open]: Online detector 样本量不足**\n- Round 3 问题：n=14, 5 正例, TPR=5/5 统计意义有限，不应作为独立 contribution\n- **已知修改**：Contribution 4 改为 \"Preliminary diagnostic\"，报告 95% CI [47.8%, 100%]；Section 4.7 加 \"requires larger-sample validation before deployment\"\n- **检查要点**：降级是否充分？论文是否还在其他地方过度宣传 detector？\n\n**4. R3-N-new-2 [info, open]: Dual-critic convergence 叙事过简**\n- Round 3 问题：ρ>0.999 与 wide dual-critic 3/4 prevention 成功有张力\n- **已知修改**：Section 4.8 加 \"the min operation in wide dual-critic may instead regularize through gradient diversity\"\n- **检查要点**：\"gradient diversity\" 解释是否有支撑（Appendix 是否提供了证据）？是否解决了叙事张力？\n\n**5. R3-N-new-3 [warning, open]: Baseline eval 值缺失**\n- Round 3 问题：Table 1 中 ManiSkill/Cheetah 缺少 baseline\n- **已知修改**：Table 1 脚注加 \"Baselines: Walker 915.7 (row 001); Cheetah ~320; PickCube via exp_019a_v2; StackCube/PegInsertion not separately measured.\"\n- **检查要点**：脚注中的部分 baseline 是否足够？\"not separately measured\" 是否可接受？\n\n**6. 统计数据更新**：26/29 → 27/30, AUROC 0.953 → 0.957, 6/6 → 7/7 seeds\n- **检查要点**：新增数据是否一致反映在全文中？数字是否前后一致？\n\n### 额外要求\n- 检查论文是否引入了新的方法论问题\n- 评估 4 seeds 在 ICML 标准下是否足够\n- 给出方法严谨性评分（1-10）\n\n### 输出格式\n1. 对每个 issue 给出 [RESOLVED] 或 [STILL_OPEN] + 理由\n2. 列出新发现的问题（如有）\n3. 方法严谨性评分（1-10）+ 简要总评"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "4",
    "text": "## Round 4 修订评估任务 — Reviewer 1（方法严谨性 + 残留问题验证）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex`\n**目标 Venue**: ⚠️ ICML 2026（从 CoRL 2026 转投）\n**Deadline**: 2026-01-28（已过期；可能处于 rebuttal 阶段或准备下一轮投稿）\n**页数限制**: 8 页正文 + unlimited appendix/references\n**模板**: 应使用 ICML 2026 官方样式（当前仍为 corl_2026，需核实）\n**匿名规则**: Double-blind\n**审查侧重**: 方法严谨性、Round 3 残留问题验证\n\n### 背景\n\nVenue 从 CoRL 2026 改为 ICML 2026。Round 3 评分 Weak Reject (5/10)，主因是 CoRL venue fit 和 actionable contribution 问题。转投 ICML 后需重新评估。\n\n### 必须逐条检查的 Issue（Round 3 open/in_progress）\n\n**1. R1-W2 / REV-2 [warning, in_progress]: 105K vs 505K 步数不对等**\n- Round 3 问题：未显式讨论步数不对等，exp_045 长跑数据未呈现\n- **已知修改**：Discussion 新增 \"Training horizon\" 段落，提及 \"Extended training (~302K steps, one seed) shows complete self-recovery after approximately 170K additional steps post-onset\"\n- **检查要点**：这段讨论是否充分回应了问题？302K 单 seed 数据是否在 Appendix 呈现？\"sufficient to observe collapse onset\" 的论证是否有力？1/4 self-correction 现象是否被合理讨论？\n\n**2. R2-W1 [warning, in_progress]: TAWM 对比无实证，\"structural factor\" 过强**\n- Round 3 问题：Abstract/Conclusion 称 \"the structural factor\" 但无 MPC 实验\n- **已知修改**：Abstract 改为 \"a hypothesized structural factor\"；Conclusion 改为 \"hypothesized structural factor. Empirical validation on MPC-based architectures (e.g., TD-MPC2) remains future work.\"\n- **检查要点**：措辞是否已充分弱化？全文是否一致使用 \"hypothesized\"？是否还有其他位置仍用 \"the structural factor\"？\n\n**3. R3-N-new-1 [warning, open]: Online detector 样本量不足**\n- Round 3 问题：n=14, 5 正例, TPR=5/5 统计意义有限，不应作为独立 contribution\n- **已知修改**：Contribution 4 改为 \"Preliminary diagnostic\"，报告 95% CI [47.8%, 100%]；Section 4.7 加 \"requires larger-sample validation before deployment\"\n- **检查要点**：降级是否充分？论文是否还在其他地方过度宣传 detector？\n\n**4. R3-N-new-2 [info, open]: Dual-critic convergence 叙事过简**\n- Round 3 问题：ρ>0.999 与 wide dual-critic 3/4 prevention 成功有张力\n- **已知修改**：Section 4.8 加 \"the min operation in wide dual-critic may instead regularize through gradient diversity\"\n- **检查要点**：\"gradient diversity\" 解释是否有支撑（Appendix 是否提供了证据）？是否解决了叙事张力？\n\n**5. R3-N-new-3 [warning, open]: Baseline eval 值缺失**\n- Round 3 问题：Table 1 中 ManiSkill/Cheetah 缺少 baseline\n- **已知修改**：Table 1 脚注加 \"Baselines: Walker 915.7 (row 001); Cheetah ~320; PickCube via exp_019a_v2; StackCube/PegInsertion not separately measured.\"\n- **检查要点**：脚注中的部分 baseline 是否足够？\"not separately measured\" 是否可接受？\n\n**6. 统计数据更新**：26/29 → 27/30, AUROC 0.953 → 0.957, 6/6 → 7/7 seeds\n- **检查要点**：新增数据是否一致反映在全文中？数字是否前后一致？\n\n### 额外要求\n- 检查论文是否引入了新的方法论问题\n- 评估 4 seeds 在 ICML 标准下是否足够\n- 给出方法严谨性评分（1-10）\n\n### 输出格式\n1. 对每个 issue 给出 [RESOLVED] 或 [STILL_OPEN] + 理由\n2. 列出新发现的问题（如有）\n3. 方法严谨性评分（1-10）+ 简要总评"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-24T09:27:36.844039+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25955
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-24T09:27:36.945339+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "4",
  "text": "## Round 4 修订评估任务 — Reviewer 2（ICML Novelty/Significance + 格式）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex`\n**目标 Venue**: ⚠️ ICML 2026（从 CoRL 2026 转投）\n**Deadline**: 2026-01-28（已过期；可能处于 rebuttal 阶段或准备下一轮）\n**页数限制**: 8 页正文 + unlimited appendix/references\n**模板**: 应使用 ICML 2026 官方样式（当前文件仍为 `\\usepackage{corl_2026}`！）\n**匿名规则**: Double-blind\n**审查侧重**: ICML venue fit、novelty、significance、格式合规\n\n### 背景\n\nVenue 从 CoRL 2026 改为 ICML 2026。Round 3 两个 critical issues（venue fit 5/10, actionable contribution 6/10）在转投 ICML 后需完全重新评估：\n- ICML 对 diagnostic/negative-result paper 的接受度比 CoRL 高\n- ICML 不要求 \"core robotics problems\"\n- 但 ICML 对 novelty 和 broader impact 要求高\n\n### 必须逐条检查的 Issue\n\n**1. R1-N3 [critical, in_progress → 重新评估]: Venue fit**\n- Round 3 问题：CoRL 要求 \"core robotics problems\"，论文不满足\n- **Venue 变更**：ICML 2026 的 RL/world-model track 对 diagnostic/negative-result 论文更开放\n- **检查要点**：\n  - 论文是否适合 ICML 的 scope（RL, optimization, representation learning）？\n  - 当前的 robotics framing（Abstract 首句、Intro 前两段、Discussion implications）在 ICML 中是否仍合适，还是应该调整为更通用的 RL framing？\n  - ICML 的 broader impact 要求如何影响论文定位？\n\n**2. R2-N3 [critical, in_progress → 重新评估]: 纯诊断缺乏 actionable solution**\n- Round 3 问题：对 CoRL deployment-oriented 社区贡献偏弱\n- **Venue 变更**：ICML 接受 Henderson et al. (2018) 类型的 diagnostic/empirical study\n- **检查要点**：\n  - 在 ICML 标准下，diagnostic + partial mitigation + preliminary detection 的贡献模式是否足够？\n  - 与 ICML 历史上接受的 diagnostic/negative-result paper 对比如何？\n  - 四级干预层级分析的方法论贡献在 ICML 中的价值如何？\n\n**3. R3-N1 [critical] ⚠️ 模板不合规**\n- **严重问题**：main.tex:5 仍为 `\\usepackage{corl_2026}`，未切换到 ICML 2026 样式\n- ICML 2026 使用自己的样式文件（icml2026.sty），格式与 PMLR/CoRL 不同\n- **检查要点**：确认模板状态。如果确实仍是 CoRL 模板，这是 desk reject 风险。\n\n**4. R2-W4 [warning, resolved]: Becker-Ehmck 引用**\n- Issue tracker 标记为 resolved（解释为 Benechehab et al. 2023 的混淆）\n- **检查要点**：验证 Related Work 中是否引用了 benechehab2023multitimestep\n\n**5. 写作质量（针对 ICML）**\n- Round 3 发现：Abstract 统计数据过密、F1-F7 双编号\n- **检查要点**：\n  - Abstract 是否仍然数字过密？（看最新版本）\n  - 论文长度是否在 ICML 8 页限制内？\n  - Limitations section 是否满足 ICML 的 broader impact / societal impact 要求？\n  - 是否需要增加 impact statement（ICML 近年要求）？\n  - Keywords 是否适合 ICML？\n\n### ICML 2026 CFP 关键要求\n- 8 页正文 + unlimited references/appendix\n- Impact statement 必须包含\n- Double-blind\n- 接受范围广：ML theory, RL, optimization, representation learning, applications\n- 重视 novelty, significance, clarity\n\n### 输出格式\n1. 对每个 issue 给出判定 + 理由\n2. ICML venue fit 评分（1-10）\n3. Novelty 评分（1-10）\n4. Significance 评分（1-10）\n5. 写作质量评分（1-10）\n6. 简要总评 + 与 ICML 历史接受论文的对比"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "4",
    "text": "## Round 4 修订评估任务 — Reviewer 2（ICML Novelty/Significance + 格式）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex`\n**目标 Venue**: ⚠️ ICML 2026（从 CoRL 2026 转投）\n**Deadline**: 2026-01-28（已过期；可能处于 rebuttal 阶段或准备下一轮）\n**页数限制**: 8 页正文 + unlimited appendix/references\n**模板**: 应使用 ICML 2026 官方样式（当前文件仍为 `\\usepackage{corl_2026}`！）\n**匿名规则**: Double-blind\n**审查侧重**: ICML venue fit、novelty、significance、格式合规\n\n### 背景\n\nVenue 从 CoRL 2026 改为 ICML 2026。Round 3 两个 critical issues（venue fit 5/10, actionable contribution 6/10）在转投 ICML 后需完全重新评估：\n- ICML 对 diagnostic/negative-result paper 的接受度比 CoRL 高\n- ICML 不要求 \"core robotics problems\"\n- 但 ICML 对 novelty 和 broader impact 要求高\n\n### 必须逐条检查的 Issue\n\n**1. R1-N3 [critical, in_progress → 重新评估]: Venue fit**\n- Round 3 问题：CoRL 要求 \"core robotics problems\"，论文不满足\n- **Venue 变更**：ICML 2026 的 RL/world-model track 对 diagnostic/negative-result 论文更开放\n- **检查要点**：\n  - 论文是否适合 ICML 的 scope（RL, optimization, representation learning）？\n  - 当前的 robotics framing（Abstract 首句、Intro 前两段、Discussion implications）在 ICML 中是否仍合适，还是应该调整为更通用的 RL framing？\n  - ICML 的 broader impact 要求如何影响论文定位？\n\n**2. R2-N3 [critical, in_progress → 重新评估]: 纯诊断缺乏 actionable solution**\n- Round 3 问题：对 CoRL deployment-oriented 社区贡献偏弱\n- **Venue 变更**：ICML 接受 Henderson et al. (2018) 类型的 diagnostic/empirical study\n- **检查要点**：\n  - 在 ICML 标准下，diagnostic + partial mitigation + preliminary detection 的贡献模式是否足够？\n  - 与 ICML 历史上接受的 diagnostic/negative-result paper 对比如何？\n  - 四级干预层级分析的方法论贡献在 ICML 中的价值如何？\n\n**3. R3-N1 [critical] ⚠️ 模板不合规**\n- **严重问题**：main.tex:5 仍为 `\\usepackage{corl_2026}`，未切换到 ICML 2026 样式\n- ICML 2026 使用自己的样式文件（icml2026.sty），格式与 PMLR/CoRL 不同\n- **检查要点**：确认模板状态。如果确实仍是 CoRL 模板，这是 desk reject 风险。\n\n**4. R2-W4 [warning, resolved]: Becker-Ehmck 引用**\n- Issue tracker 标记为 resolved（解释为 Benechehab et al. 2023 的混淆）\n- **检查要点**：验证 Related Work 中是否引用了 benechehab2023multitimestep\n\n**5. 写作质量（针对 ICML）**\n- Round 3 发现：Abstract 统计数据过密、F1-F7 双编号\n- **检查要点**：\n  - Abstract 是否仍然数字过密？（看最新版本）\n  - 论文长度是否在 ICML 8 页限制内？\n  - Limitations section 是否满足 ICML 的 broader impact / societal impact 要求？\n  - 是否需要增加 impact statement（ICML 近年要求）？\n  - Keywords 是否适合 ICML？\n\n### ICML 2026 CFP 关键要求\n- 8 页正文 + unlimited references/appendix\n- Impact statement 必须包含\n- Double-blind\n- 接受范围广：ML theory, RL, optimization, representation learning, applications\n- 重视 novelty, significance, clarity\n\n### 输出格式\n1. 对每个 issue 给出判定 + 理由\n2. ICML venue fit 评分（1-10）\n3. Novelty 评分（1-10）\n4. Significance 评分（1-10）\n5. 写作质量评分（1-10）\n6. 简要总评 + 与 ICML 历史接受论文的对比"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-24T09:27:38.404252+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1458
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-24T09:27:38.404743+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "review_chat_id": "oc_dd4a07a509df7e5f9a31d65f776059bc"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "review_chat_id": "oc_dd4a07a509df7e5f9a31d65f776059bc"
  }
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-24T09:27:40.074149+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 1669
}
```

</details>

---


### Assistant

_source line 284 · 2026-05-24T09:27:50.598339+00:00_

Round 4 审稿已启动：
- **R1**（方法严谨性）和 **R2**（ICML novelty/significance/格式）已派发
- 视觉审查已启动
- 外部审稿未配置

**本轮重点**：
1. Venue 从 CoRL → ICML 后，Round 3 两个 critical issues（venue fit、actionable contribution）需完全重新评估
2. 模板仍为 `corl_2026`，这是 ICML 投稿的 desk reject 风险
3. 5 个 Round 3 open/in_progress issues 的修改验证
4. ICML 2026 deadline (2026-01-28) 已过期，需确认投稿阶段

等待 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 23

## Round 23

2 recorded events


### User

_source line 285 · 2026-05-24T09:32:07.062977+00:00_

[Reviewer 2 审稿意见]:
## Round 4 修订评估 — Reviewer 2（ICML Novelty/Significance + 格式）

**论文**: "Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
**目标 Venue**: ICML 2026（从 CoRL 转投）

---

## Round 3→4 修改追踪

在逐条审查前，先确认论文从 Round 3 到 Round 4 的关键修改：

| 修改点 | 位置 | 内容 |
|--------|------|------|
| Abstract 精简 | abstract_body.tex | 移除 "2.78×"、"ρ > 0.999"、detector 句；减少数字密度 |
| 措辞弱化 | abstract + conclusion | "the structural factor" → "a hypothesized structural factor" |
| 数据更新 | 全文 | 26/29 → 27/30, AUROC 0.953 → 0.957, LOEO 0.981 → 0.988 |
| Detector 降级 | introduction.tex:14 | "Online detection" → "Preliminary diagnostic" + CI [47.8%, 100%] |
| 步数问题回应 | analysis.tex:10-11 | 新增 "Training horizon" 段落：extended training ~302K 一个 seed 显示 self-recovery |
| Future work | conclusion.tex:4 | "Empirical validation on MPC-based architectures (e.g., TD-MPC2) remains future work" |
| 因果措辞 | analysis.tex:8 | "6/6" → "7/7", AUROC 更新 |
| Table 1 footnote | results.tex:47 | 新增 baseline 参考值 |
| Implications 更新 | analysis.tex:14 | 修正 reward density 解释："Both domains use dense shaped rewards, so reward sparsity cannot explain the boundary" |

这些修改直接回应了 Round 3 R1/R2 的具体意见，质量上有明显提升。

---

## 逐条 Issue 检查

### 1. R1-N3 [critical → 重新评估]: Venue fit（CoRL → ICML）
**[RESOLVED for ICML]**

ICML venue fit 与 CoRL 完全不同：
- **ICML 接受范围**：CFP 明确涵盖 "RL, optimization, representation learning"。本文的核心贡献——在 imagination-based actor-critic 中诊断 dt-conditioning 的 value overestimation 失败模式——完全属于 ICML 的 RL track。
- **Diagnostic/negative-result 传统**：ICML 有接受此类工作的先例。Henderson et al. (2018) "Deep Reinforcement Learning that Matters"（本文引用）正是 ICML 接受的大规模 diagnostic study，其核心也是 negative results + 方法论建议，没有提出新算法。
- **Robotics framing 的处理**：当前 Introduction 仍以 robotics motivation 开篇（"directly on physical hardware"、DayDreamer、TD-MPC2），这在 ICML 中不构成问题——robotics 应用是 RL 研究的合法动机。但论文可以考虑略微拓宽开篇 framing，将 temporal abstraction 的 motivation 从纯 robotics 扩展到更广泛的连续控制场景（如 Atari、game-playing），以更好匹配 ICML 受众。
- **不再是核心阻碍**：在 CoRL 中 venue fit 是 critical 问题（5/10），在 ICML 中不再是问题。

---

### 2. R2-N3 [critical → 重新评估]: 纯诊断缺乏 actionable solution
**[RESOLVED for ICML]**

ICML 对贡献模式的要求与 CoRL 不同：
- **ICML 接受标准**（reviewer instructions）："Papers that are technically sound, well-written, non-redundant with previous research, and useful to at least some fraction of the ICML community should be accepted."论文满足所有条件。
- **与 Henderson et al. (2018) 对比**：该论文也没有提出新方法，核心贡献是实验方法论和 negative findings。本文的 factorial design（43 配置 × 5 环境 × 四级干预）在系统性上至少与之相当。
- **贡献层次明确**：
  1. 新 failure mode 的识别和因果分离（CIVO, 27/30, AUROC=0.957）
  2. 架构边界的发现（MPC vs imagination-based bootstrapping）
  3. 四级干预层级的系统分析（gradient → output → representation → architecture）
  4. Preliminary diagnostic tool（降级为 preliminary 是诚实的）
- **在 ICML 中 "不要用 trained dt-embedding" 是合理贡献**：对 ICML 的方法论社区来说，知道某条看似合理的技术路线（dt-conditioning in imagination-based RL）为什么不可行，以及为什么标准 countermeasures（Double Q, gradient stopping）无法修复，本身就有价值。这类 "warning" 可以避免社区重复踩坑。

---

### 3. R3-N1 [critical] ⚠️ 模板不合规
**[STILL_OPEN — CRITICAL]**

这是当前最严重的问题：

- **main.tex:5 仍为 `\usepackage{corl_2026}`**。未切换到 ICML 2026 样式文件（`icml2026.sty`）。
- **PDF 页脚**（page 1 底部）明确显示："Submitted to the 10th Conference on Robot Learning (CoRL, 2026). Do not distribute." 这是 CoRL 特有的页脚文字。
- **ICML CFP 明确要求**："Authors must use the correct Style Files...Papers not conforming to formatting policies face rejection without review."
- **`\keywords{}` 命令**（main.tex:49）是 CoRL 模板特有的，ICML 模板可能不支持。
- **影响**：以当前状态提交到 ICML 将被 desk reject，无需进入实质审稿。

**必须修复**：
1. 下载 ICML 2026 样式文件（icml2026.zip）
2. 替换 `\usepackage{corl_2026}` 为 `\usepackage{icml2026}`
3. 移除或调整 `\keywords{}` 命令
4. 验证编译通过、格式正确

---

### 4. [NEW — CRITICAL] Impact Statement 缺失
**[STILL_OPEN — CRITICAL]**

ICML 2026 CFP 明确要求：
> "Required section at end of paper (before References), does not count toward page limit."

当前论文在 References 之前没有 Impact Statement。即使论文的 societal impact 有限，ICML 也要求至少包含一个标准声明：

> "This paper presents work whose goal is to advance the field of machine learning. There are many potential societal consequences of our work, none of which we feel must be specifically highlighted here."

**必须添加**：在 Conclusion/Limitations 之后、`\bibliography{}` 之前插入 Impact Statement section。

---

### 5. R2-W4 [warning, resolved]: Becker-Ehmck 引用
**[RESOLVED]**

Issue tracker 正确标记：Round 3 的 "Becker-Ehmck 2023" 系与 "Benechehab et al. 2023" 的混淆。相关引用 `benechehab2023multitimestep` 在 related_work.tex:8 中已被引用（"Multi-timestep world models learn predictions at variable horizons but do not examine the value overestimation pathology we isolate"）。确认 resolved。

---

### 6. 写作质量（针对 ICML）

**Abstract 数字密度（Round 3 E1）**：
**[PARTIALLY RESOLVED]** — 改善明显。Abstract 移除了 "2.78×"、"ρ > 0.999"、detector 句。但仍包含 "14-19%"、"27/30"、"AUROC=0.957"、"LOEO"。相比 Round 3 的 6+ 个数字指标，现在约 4 个，可接受但仍偏密。

**F1-F7 双编号（Round 3 E2）**：
**[STILL_OPEN]** — 未修改。Results section 仍使用 "F1"..."F7" 编号与 Section 编号并行。这对 ICML reviewer 来说是额外认知负担。建议：要么用 F1-F7 作为唯一编号系统（替代 subsection 编号），要么去掉 F 编号改用 descriptive subsection titles。

**论文长度**：
正文 8 页（pages 1-8），References 从 page 9 开始。符合 ICML 8 页限制 ✅

**Limitations section**：
存在于 Conclusion 的 paragraph 中（conclusion.tex:6-11）。ICML 不要求 Limitations 作为独立 section（与 NeurIPS 不同），当前形式可接受 ✅

**匿名合规**：
- "Anonymous Author(s)" ✅
- "Code: upon acceptance" ✅
- DreamerV3 仓库链接（官方仓库，非作者代码）✅
- 但页脚 "Submitted to the 10th Conference on Robot Learning (CoRL, 2026)" 在 ICML 提交中技术上暴露了此前的投稿 venue（尽管这更多是模板问题而非匿名问题）

**Keywords 适配**：
当前 keywords "World Models, Temporal Abstraction, Value Overestimation, DreamerV3" 内容上适合 ICML，但 `\keywords{}` 命令需确认 ICML 模板是否支持。

---

## Round 3 → Round 4 改进的其他确认

### R1-W2 步数不对等：[SUBSTANTIALLY ADDRESSED]
新增 "Training horizon" 段落（analysis.tex:10-11）提供了关键的 extended training 数据："Extended training (~302K steps, one seed) shows complete self-recovery after approximately 170K additional steps post-onset"。这直接回应了 "treatment 是否在更长训练后 recover" 的问题。

但 n=1 seed 的 extended training 数据仍然有限，且结论（self-recovery 需要 ~170K 额外步数，计算成本高）也支持论文的核心论点：CIVO 即使可以 recover，代价也很大。在 ICML 标准下，这个回应足够。

### R2-W1 TAWM "structural factor"：[RESOLVED]
两处修改充分回应：
1. Abstract: "a hypothesized structural factor"（而非 "the structural factor"）
2. Conclusion: "Empirical validation on MPC-based architectures (e.g., TD-MPC2) remains future work"

措辞准确反映了证据级别：architectural reasoning + 未经 TD-MPC2 实验验证 → 假说而非结论。

### R1-N-new-1 Online detector 样本量：[RESOLVED]
Contribution 4 从 "Online detection" 降级为 "Preliminary diagnostic"，明确标注 "TPR 95% CI [47.8%, 100%] (n=5/5), FPR 22% (2/9)"。这是对小样本限制的诚实披露。

---

## 评分（ICML 标准）

### ICML Venue Fit: 8/10
论文完全属于 ICML RL track 的范畴。Diagnostic/negative-result 论文在 ICML 有先例（Henderson et al. 2018）。唯一减分：robotics-heavy 的开篇 framing 可以更通用化以更好匹配 ICML 受众，但这是 minor 的 presentation 问题。

### Novelty: 7/10
- **CIVO 作为新 failure mode**：dt-conditioning 在 imagination-based RL 中引发 value overestimation 的发现是新颖的。之前没有工作系统地研究过这个特定的失败机制。
- **Factorial design 的诊断方法论**：将 Henderson et al. (2018) 的 factorial 方法论应用到 world-model RL 的特定问题中，方法论本身不新但应用有价值。
- **MPC vs imagination-based 的 architectural boundary**：这个洞察有概念新颖性，即使实验验证不完整（"hypothesized"）。
- **减分点**：论文没有提出新方法或新算法，核心工具（factorial ablation, NVE metric, gradient stopping）都是已有技术的组合。CIVO 现象虽新颖，但论文自己承认它在 manipulation 中不出现、在 locomotion 中可以通过 "不用 trained embedding" 避免。

### Significance: 6/10
- **对 world-model RL 社区的价值**：知道 dt-conditioning 在 imagination-based RL 中为什么失败、为什么 Double Q 和 gradient stopping 无法修复，可以帮助社区避免重复探索这条技术路线。
- **方法论示范**：四级干预层级分析为未来的 RL 诊断研究提供了一个可复用的框架。
- **减分点**：
  - 发现的 scope 有限——仅在 DreamerV3 + locomotion 中确认
  - Actionable outcome 弱——最有效建议是"不要用"
  - 未提出解决方案或新理论框架
  - 与 Henderson et al. (2018) 相比，后者的发现影响了整个 RL 社区的实验报告实践；本文的影响范围窄得多（仅 world-model RL + temporal abstraction）

### 写作质量: 7/10
- 结构清晰、专业
- Abstract 较 Round 3 改善明显但仍偏数字密集
- F1-F7 双编号增加认知负担
- 总体可读性良好，技术细节充分

---

## ICML 维度打分（4-point scale: Excellent / Good / Fair / Poor）

| 维度 | 评分 | 理由 |
|------|------|------|
| Soundness | Good (3/4) | Factorial design 严谨，LOEO 交叉验证有力；但 extended training 仅 1 seed，TAWM 对比无实验（已弱化为 hypothesized） |
| Presentation | Good (3/4) | 结构清晰，写作专业；Abstract 偏数字密集，F1-F7 双编号增加认知负担；模板问题需修复 |
| Significance | Fair (2/4) | 对 world-model RL 子社区有价值的 warning，但 scope 窄（DreamerV3 + locomotion），无解决方案 |
| Originality | Good (3/4) | CIVO 作为新 failure mode 有新颖性，MPC vs imagination 的 architectural boundary 有概念价值；方法论是已有技术组合 |

### Overall Recommendation: 4 (Weak Accept)
论文是一个 technically solid 的 diagnostic study，在 ICML RL track 中处于 borderline accept 区域。主要优势是 factorial design 的系统性和 CIVO 发现的新颖性；主要劣势是有限的 scope 和缺乏 constructive solution。

---

## 与 ICML 历史接受论文对比

| 对比论文 | 贡献类型 | 本文对比 |
|---------|---------|---------|
| Henderson et al. (2018) "RL that Matters" | Diagnostic，方法论指南 | 类似贡献模式，但影响范围窄得多 |
| Lyle et al. (2022) "Capacity Loss in RL" | 诊断 + partial mitigation | 本文结构类似：诊断→干预→发现干预不够 |
| Lambert et al. (2020) "Objective Mismatch" | Diagnostic, model-based RL | 类似领域的 diagnostic work |

本文的 systematic rigor 与上述论文相当，但 breadth of impact 偏窄。如果 reviewer 重视 "避免社区重复踩坑" 的价值，weak accept 是合理的；如果 reviewer 要求 constructive solution 或更广泛的适用性，可能会 weak reject。

---

## 总结

**两个 CRITICAL 格式问题必须立即修复**：
1. 模板从 `corl_2026` 切换到 `icml2026`（含页脚修复）
2. 添加 Impact Statement

**内容方面**，Round 3→4 的修改质量好——"hypothesized structural factor"、detector 降级、training horizon 段落、baseline 值补充都直接回应了具体审稿意见。转投 ICML 是正确决策：论文的贡献模式（diagnostic + negative result）在 ICML 中比 CoRL 更有竞争力。

**Remaining weakness**：novelty 和 significance 在 ICML 中处于 borderline 水平。如果审稿人认为 "在 DreamerV3 locomotion 中发现的一个可以通过不用 trained embedding 避免的 failure mode" 值得 ICML 版面，论文可以接受；如果审稿人期望更广泛的适用性或 constructive solution，论文偏弱。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 286 · 2026-05-24T09:32:14.290336+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 24

## Round 24

26 recorded events


### User

_source line 287 · 2026-05-24T09:32:18.644565+00:00_

[Reviewer 2 审稿结果]:
审稿完成。已提交 Round 4 评估，核心发现：

1. **两个 CRITICAL 格式问题**：模板仍为 `corl_2026`（PDF 页脚明确显示 CoRL），且缺少 ICML 必需的 Impact Statement——以当前状态提交会被 desk reject
2. **Venue fit 大幅改善**：从 CoRL 的 5/10 提升到 ICML 的 8/10，diagnostic/negative-result 论文在 ICML 有先例
3. **内容修改质量好**：Round 3 的具体审稿意见（"structural factor" 弱化、detector 降级、training horizon 数据、baseline 值补充）均已回应
4. **Overall**: ICML 标准下 Weak Accept (4/6)，soundness 和 originality 是 Good，significance 偏 Fair

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-24T09:32:36.224644+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/skills/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/skills/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 289 · 2026-05-24T09:32:38.234609+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/sessions/review_director_9a57450c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 2009
}
```

</details>

---


### Tool call

_source line 290 · 2026-05-24T09:32:38.285483+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-24T09:32:38.336246+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-24T09:32:47.025775+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool call

_source line 293 · 2026-05-24T09:32:47.076482+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-24T09:32:47.127147+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-24T09:32:47.578801+00:00_

{"result":"# 项目 event-gated-adaptive-horizon 概况\n\n## 实验状态 (133 个)\n\n- **exp_009a_baseline_walker_s2**: DONE (success) — \n- **exp_008e_v3_walker_s2**: DONE (negative) — \n- **exp_008e_v3_walker_s1**: DONE (success) — \n- **exp_006**: DONE (killed) — \n- **exp_008a**: DONE (killed) — \n- **exp_008c**: DONE (killed) — \n- **exp_008d**: DONE (killed) — \n- **exp_008e_v2_subsample_on_dt1_h15**: DONE (killed) — \n- **exp_rssm_fidelity_analysis**: DONE (success) — \n- **exp_008e_v3_subsample_on_dt1_h15**: DONE (success) — \n- **exp_009c_008f_walker_s2**: DONE (negative) — \n- **exp_006_fixed_dt2**: DONE (negative) — \n- **exp_008e_subsample_on_fixed_dt1**: DONE (killed) — \n- **exp_008e_subsample_on_dt1_h15**: DONE (killed) — \n- **exp_002_event_gated**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp_059_walker_trained_s5** (negative): Walker CIVO trigger 第5个独立seed验证。当前4/4 seeds触发sustained CIVO（p=0.0625 binomial test）。如果s5也触发 → p=0.03125，达到统计显著性阈值。关联 Claim 1: CIVO reproducibility。 ← 基于 exp_008d_civo_trigger_s3\n- **exp_008d_civo_trigger_s4** (success): Walker Walk CIVO trigger seed=4: trained dt_emb + subsample ON + H=8. 第四 seed 复现 CIVO (NVE>1.5×)，加强 Walker 因果论证的统计力度。Rebuttal 储备。 ← 基于 exp_008d_civo_trigger_s3\n- **exp_009b_008d_walker_s2** (negative): CIVO onset (NVE≥1.5×) reproduces on seed=2 with identical architecture, confirming the phenomenon is systematic rather than seed-specific. Collapse outcome may be stochastic. ← 基于 exp_008d_subsample_on_h8\n  [009b_literature_linkage](/api/workspace-files/projects/event-gated-adaptive-horizon/artifacts/exp_009b_008d_walker_s2/report/009b_literature_search.md)\n\n## 趋势\n成功 65 / 负向 36 / 失败 11 / 共 133\nnve_peak: 4.44 ↑（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nbjb1-40020: 空闲 cuda:0, cuda:1\nbjb1-45299: 无 GPU 信息\n\n## 告警\n- 016e: 已被终止 — unknown\n- exp_002_event_gated: 训练失败 — unknown\n- exp_006: 已被终止 — unknown\n- 
…[truncated 1245 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 553
}
```

</details>

---


### Tool result

_source line 296 · 2026-05-24T09:32:47.579241+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 502
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-24T09:32:47.629783+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-24T09:27:39.638747+00:00\", \"completed_at\": \"2026-05-24T09:31:41.105902+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 1-4\", \"message\": \"连续 4 页纯文本无任何 display item（figure/table/equation block）。审稿人打开论文后需读 4 页密集文字才能看到第一个视觉锚点（Table 1，page 5）。这严重损害第一印象——诊断/实证类论文的前 2 页内应至少有一个概览图或核心结果表。建议：将 Figure 6（CTVO 机制路径图，当前在 appendix page 17）或一个简化的架构/诊断框架概览图提前到 Section 1 或 Section 3 开头。\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-8\", \"message\": \"主体正文 8 页仅 4 个 display items（Table 1, Figure 1, Figure 2, Table 2）。对诊断分析类论文偏少，建议至少增加 1 个概念图（如 CTVO 机制图）和 1 个汇总可视化，使 display items 达到 6 个。\"}, {\"severity\": \"warning\", \"dimension\": \"page 3-4\", \"message\": \"Section 3（Experimental Setup）跨 2 页纯文本，描述了架构、变量率机制、diagnostic metrics 等复杂设计，但无任何图示辅助。建议加一个实验设计概览图或架构示意图（即使是简化版 Figure 6 中的 pathway 图）。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Section 5 Discussion + Section 6 Conclusion 挤在同一页，且全为纯文本。Discussion 没有任何 display item 辅助总结（如 finding summary 表或 limitation taxonomy 图），与前面的纯文本页叠加后，论文后半段给人\\\"全是字\\\"的压迫感。\"}, {\"severity\": \"warning\", \"dimension\": \"page 33\", \"message\": \"最后一页 Table 22 仅占页面约 35-40%，下方约 60% 为空白。可考虑将前页的某个表格移至此页平衡空间，或在此处放置附录中的某个图。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 使用 booktabs 风格，最优结果已加粗，格式规范。Figure 1（Learning Curves）清晰可读，诊断阈值虚线标注清楚。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 1 图例中有 6 条线，颜色区分度尚可，但在灰度打印下可能难以区分——建议辅以不同 line style（dashed/dotted）或 marker shape。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2（NVE trajectories）三种轨迹类型用颜色+标注区分，清晰度良好。Dashed 阈值线辅助阅读。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2（Intervention hierarchy）结构清晰，booktabs 风格，列对齐良好。\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Figure 3（ROC curve）附录中质量良好，95% CI shading 清晰
…[truncated 1180 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-24T09:32:56.317975+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-24T09:32:56.468884+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_reports/round_3.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-24T09:32:56.820279+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-24T09:32:56.870869+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-24T09:32:59.129067+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_reports/round_3.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_reports/round_3.md"
  }
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-24T09:32:59.330414+00:00_

1	---
2	round: 3
3	review_mode: continue
4	overall_score: weak reject
5	timestamp: 2026-05-24T07:19:49.260508+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# 审稿报告 — Round 3
12	
13	**论文**: "Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
14	**目标 Venue**: CoRL 2026 Main Conference
15	**审稿日期**: 2026-05-24
16	**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验充分性 | R2: Venue Fit + 贡献度 + 写作质量）
17	**轮次**: Round 3 继续审稿（修订评估）+ 交叉分享（1 轮收敛）
18	**上轮评分**: Round 1 Strong Reject (4/10)
19	
20	---
21	
22	## Summary
23	
24	论文在 Round 1 (Strong Reject) 后进行了大幅修改：从 1 环境扩展到 5 环境（Walker Walk, Cheetah Run, PickCube-v1, StackCube-v1, PegInsertionSide-v1），关键配置 seeds 增至 4，引入 LOEO 交叉验证（AUROC=0.981），因果语言全面弱化为 "strongest predictor"，新增四级干预层级分析和在线 CIVO 检测器，切换至 CoRL 2026 PMLR 模板，添加 robotics framing 和 ManiSkill 实验。论文现在识别 CIVO 为 locomotion-specific（6/6 locomotion seeds 触发，0/5 manipulation configurations 触发），并提供了 discriminative validity（frozen-embedding 控制正确区分 CIVO 与环境特异性 transient）。
25	
26	---
27	
28	## Strengths
29	
30	1. **Factorial design 系统且严谨**（2/2 reviewer 共识）：43 配置 × 4 seeds × 5 环境的设计空间覆盖广泛；primary/secondary comparison 标注清晰；2×2 factorial grid 完整
31	2. **LOEO 交叉验证显著增强统计可信度**：AUROC=0.953 (in-sample, n=29), 0.981 (LOEO, 3 folds) 在 RL 诊断类工作中是扎实的统计功效水平
32	3. **四级干预层级分析**（gradient/output/representation/architecture）：提供了系统性的 negative result，对社区有长期参考价值。Gradient magnitude ≠ causal importance 的发现（reward head 38-49% 但 SGS 无效）是有洞见的
33	4. **ManiSkill non-CIVO 结果增加 discriminative validity**：NVE 诊断能正确区分 dt-embedding-dependent CIVO 与环境特异性 transient（frozen controls 匹配 trained spikes），展示了方法论的特异性
34	5. **Dual-critic convergence (ρ > 0.999)**：关于 imagination-based training 中 Double Q pessimism 失效的 structural insight 有价值
35	6. **Limitations section 诚实全面**：主动承认 4-seed 局限、architecture 局限、locomotion-specificity，ManiSkill non-CIVO 如实报告
36	7. **Signed error 分析**：dt=2 underprediction (SE=-0.599) 排除 observation-level re
…[truncated 9946 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-24T09:32:59.381011+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-24T09:32:59.432497+00:00_

1	issues:
2	  - id: "R1-N1"
3	    summary: "统计检验力严重不足：2-3 seeds 无法支撑 causal factor 声明"
4	    category: experiment
5	    severity: critical
6	    status: resolved
7	    first_raised_round: 1
8	    last_seen_round: 3
9	    mentions:
10	      - round: 1
11	        reviewers: [1, 2, 3]
12	        note: "三位 reviewer 均认同统计效力不足"
13	      - round: 3
14	        reviewers: [1, 2]
15	        note: "两位 reviewer 一致判定 RESOLVED。Seeds 增至 4，语言改为 strongest predictor，LOEO AUROC=0.981，IQR 报告。残留小问题：Abstract 中 isolate 一词仍携带因果含义。"
16	    action_items:
17	      - round: 1
18	        action: "补 seeds 到 4 per key config"
19	        assigned_to: agent
20	        status: done
21	      - round: 1
22	        action: "弱化因果语言: causal factor → strongest predictor"
23	        assigned_to: paper_agent
24	        status: done
25	      - round: 1
26	        action: "统计报告改用 IQM + bootstrap CI per Agarwal et al. 2021"
27	        assigned_to: paper_agent
28	        status: done
29	    resolution: "Seeds 增至 4，因果语言全面弱化为 strongest predictor，LOEO 交叉验证 AUROC=0.981，IQM + bootstrap CI 报告完整。"
30	    resolution_round: 3
31	
32	  - id: "R1-N2"
33	    summary: "NVE 阈值 1.5× 为 post-hoc 选择，88.9% accuracy 是训练准确率，无独立验证"
34	    category: method
35	    severity: critical
36	    status: resolved
37	    first_raised_round: 1
38	    last_seen_round: 1
39	    mentions:
40	      - round: 1
41	        reviewers: [1, 2, 3]
42	        note: "三位 reviewer 一致认为 post-hoc"
43	    action_items:
44	      - round: 1
45	        action: "LOEO cross-validation: mean AUROC 0.981"
46	        assigned_to: agent
47	        status: done
48	    resolution: "LOEO 交叉验证完成：3 环境 leave-one-out，mean AUROC 0.981，θ=1.5 在全部 fold 最优范围。论文措辞已改为 in-sample + LOEO cross-validated。"
49	    resolution_round: 1
50	
51	  - id: "R1-N3"
52	    summary: "CoRL venue fit 严重不足：全文无 robotics 实验/讨论"
53	    category: framing
54	    severity: critical
55	    status: in_progress
56	    first_raised_round: 1
57	    last_seen_round: 3
58	    mentions:
59	      - round: 1
60	      
…[truncated 15105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-24T09:33:44.341573+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_round_4/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_round_4/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-24T09:33:44.743581+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_4/submitted.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-24T09:33:44.995051+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/reviewer_*_round_4*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/reviewer_*_round_4*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-24T09:33:45.045788+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-24T09:33:47.557184+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/reviewer_*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/reviewer_*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-24T09:33:47.658028+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 312 · 2026-05-24T09:34:20.213031+00:00_

已收到 Reviewer 2 的 Round 4 初审结果。核心发现记录：

**R2 Round 4 关键评估：**
- **CRITICAL-1**: 模板仍为 `corl_2026`（PDF 页脚显示 CoRL）→ 需换 ICML 模板，否则 desk reject
- **CRITICAL-2**: 缺少 ICML 必需的 Impact Statement → desk reject
- **正面**: Venue fit 从 CoRL 5/10 大幅提升至 ICML 8/10；Round 3 提出的具体问题已回应
- **Overall**: ICML 标准下 Weak Accept (4/6)

当前状态：等待 Reviewer 1 的 Round 4 评估。R1 完成后进入交叉分享阶段。

**Round 4 修订评估进度：**
| Reviewer | 状态 | 侧重 |
|----------|------|------|
| R1 | ⏳ 待返回 | 方法严谨性 + 实验充分性 |
| R2 | ✅ 已完成 | Venue Fit + 贡献度 + 写作质量 |

等待 R1 返回后，将两位 Reviewer 的完整审稿原文互发进行交叉响应（`[AGREE]`/`[REBUT]`），再合成最终报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 25

## Round 25

6 recorded events


### User

_source line 313 · 2026-05-24T09:34:20.219139+00:00_

[Reviewer 1 审稿意见]:

# Round 4 审稿报告 — Reviewer 1（方法严谨性 + 残留问题验证）

**论文**: "Why Temporal Abstraction Can Fail in Imagination-Based RL"
**目标 Venue**: ICML 2026（从 CoRL 转投）

---

## 总体评分

**方法严谨性**: 7.5/10（Round 3 为 7/10，提升 0.5 分）
**ICML Overall Recommendation**: 4/6 (Weak Accept)
**一句话总结**: Round 3 两个 open warning 均已实质性解决（步数不对等增加讨论+302K 延长数据，"structural factor" 弱化为 "hypothesized"），但数据更新引入了 seed 数量不一致问题（Methodology 说 4 seeds 而 Results 报告 5 seeds），模板仍为 CoRL 格式，需要在投稿前紧急修复。

## ICML 2026 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/4 (Good) | Factorial design 严谨，LOEO AUROC=0.988 有力，但 seed 数量前后不一致削弱可信度 |
| Presentation | 3/4 (Good) | F1-F7 结构清晰，但存在数字不一致、模板错误 |
| Significance | 3/4 (Good) | 对 imagination-based RL 社区有直接价值；转投 ICML 消除了 venue fit 问题 |
| Originality | 3/4 (Good) | 首个系统诊断 CIVO 的工作；四级干预层级和 dual-critic convergence 发现均为新贡献 |

---

## 逐条 Issue 检查

### 1. R1-W2 [warning, in_progress]: 105K vs 505K 步数不对等
**[RESOLVED]**

**修改内容确认**:
- Discussion Section 5 新增 "Training horizon" 段落（analysis.tex line 10-11）
- 正文明确说明："Our primary analysis uses 105K steps, sufficient to observe CIVO onset (45K--65K) and classify trajectories"
- 报告 302K 延长实验结果："Extended training (~302K steps, one seed) shows complete self-recovery after approximately 170K additional steps post-onset"
- Appendix D.4 "Extended Training Dynamics" 提供完整细节：exp_045 seed s3，NVE peak 4.91× at 132K → 自恢复至 NVE 0.05×，eval 867.6（94.7% of baseline），需约 170K 额外步数
- 论文将此与 frozen embedding 对比："at substantial computational cost that the frozen dt-embedding diagnostic eliminates entirely"

**评估**: 这是一个充分的回应。论文现在：(a) 明确论证 105K 足以观察 onset（45K-65K window）；(b) 提供 1 seed 的 302K 长跑证据显示自恢复可能但代价高昂；(c) 将此纳入 Discussion 而非隐藏在 Appendix。单 seed 长跑的统计效力有限，但对诊断论文而言足够——论文不声称自恢复率，只是展示其存在性。

---

### 2. R2-W1 [warning, in_progress]: TAWM 对比无实证，"structural factor" 过强
**[RESOLVED]**

**修改内容确认**:
- Abstract: "a hypothesized structural factor" ✓（此前为 "the structural factor"）
- Conclusion: "hypothesized structural factor. Empirical validation on MPC-based architectures (e.g., TD-MPC2) remains future work." ✓
- Grep 确认全文仅 Abstract 和 Conclusion 使用 "structural factor"，均已加 "hypothesized" ✓

**全文一致性检查**:
- Introduction Contribution 2: 使用 "Architectural boundary" 而非 "structural factor"，表述为事实观察（"dt-conditioning succeeds in TD-MPC2's MPC re-planning but fails under imagination-based bootstrapping"）——这是基于 TAWM 论文和本文实验的事实描述，不是假说，措辞合理
- Discussion paragraph 1: "MPC re-planning prevents accumulation"——呼应 Appendix D.5 的理论分析
- 无其他位置仍使用 "the structural factor"

**评估**: 措辞充分弱化且全文一致。"hypothesized" + "remains future work" 的组合恰当地将其定位为需要验证的假说。

---

### 3. R3-N-new-1 [warning, open]: Online detector 样本量不足
**[RESOLVED]**

**修改内容确认**:
- Introduction Contribution 4: 降级为 "Preliminary diagnostic"，不再作为独立 contribution 宣传 ✓
- 报告 95% Clopper-Pearson CI [47.8%, 100%]（n=5/5）——CI 下界 47.8% 诚实地展示了 small-sample 的不确定性 ✓
- Section 4.7 末尾："The detector requires larger-sample validation before deployment as a practical diagnostic tool." ✓

**全文其他位置检查**:
- Discussion "Practitioner guidelines" (analysis.tex line 7-8): "Monitor via NVE diagnostic (≥ 1.5×, AUROC=0.957)"——引用的是 NVE 阈值分类器（n=30, AUROC=0.957），不是 online detector（n=14），两者区分清晰 ✓
- Abstract: 已删除 "100% sensitivity" 的表述 ✓

**评估**: 降级充分。"Preliminary diagnostic" + Clopper-Pearson CI + "requires larger-sample validation" 的组合正确定位了这一贡献的成熟度。

---

### 4. R3-N-new-3 [info, open]: Dual-critic convergence 叙事过简
**[PARTIALLY RESOLVED]**

**修改内容确认**:
- Section 4.8 (results.tex line 166): "Pessimistic estimation is thus ineffective; the min operation in wide dual-critic may instead regularize through gradient diversity (Appendix G)."
- Appendix G.3 (appendix.tex line 910): "The mechanism for this synergy is an open question; we hypothesize that increased capacity improves value calibration quality while the min operation constrains the overestimation feedback loop during early training when the two critics briefly diverge."

**问题**:
- Section 4.8 说 "gradient diversity"，但 Appendix G.3 描述的机制是 "increased capacity + early-training divergence + overestimation feedback constraint"。两处的解释不一致
- "gradient diversity" 未被定义或测量——既无 gradient 方差/cosine similarity 的数据，也无理论论证
- Appendix G.3 的 "briefly diverge" 假说更具体也更诚实（承认为 open question），是更好的解释

**评估**: 核心叙事张力（ρ>0.999 yet min+capacity works）在 Appendix G.3 通过 "open question + early-training divergence hypothesis" 被合理地框定了。但主文 Section 4.8 的 "gradient diversity" 措辞过于具体且无支撑。建议 Section 4.8 改为与 Appendix G.3 一致的措辞，如 "may instead function through a capacity-dependent mechanism during early training (Appendix G)"。

这是一个 minor 措辞问题，不影响接收决定。

---

### 5. R3-N-new-2 [warning, open]: Baseline eval 值缺失
**[PARTIALLY RESOLVED]**

**修改内容确认**:
- Table 1 脚注（results.tex line 47）: "Baselines: Walker 915.7 (row 001); Cheetah ~320; PickCube via exp_019a_v2; StackCube/PegInsertion not separately measured."

**评估**:
- Walker: 已在 Table 1 row 001 显示 (915.7 @105K) ✓
- Cheetah: "~320" 为近似值——对于评估 CIVO 严重度（010b eval 51.7 = ~16% of ~320）足够，但精确值更好
- PickCube: "via exp_019a_v2" 但未给出 eval 值——读者仍无法判断 019b (26.64) 的 degradation 比例
- StackCube/PegInsertion: "not separately measured" 仍然是一个gap

**对论文论点的影响**: 有限。ManiSkill 环境的论点是 CIVO 不存在（frozen controls match trained），不需要 baseline 来判断 CIVO 是否发生。但如果要讨论 dt-conditioning 对 manipulation 任务的总体影响（即使不是 CIVO），baseline 值是必要的。

---

### 6. 统计数据更新 (26/29→27/30, AUROC 0.953→0.957, 6/6→7/7)
**[STILL_OPEN] — 发现多处不一致**

**数字更新一致性检查**:

| 指标 | 位置 | 值 | 一致？ |
|------|------|-----|--------|
| 分类 accuracy | Abstract | 27/30 | ✓ |
| 分类 accuracy | Introduction | 27/30 | ✓ |
| 分类 accuracy | Section 4.2 | 27/30 | ✓ |
| AUROC (in-sample) | Abstract | 0.957 | ✓ |
| AUROC (in-sample) | Introduction | 0.957 | ✓ |
| AUROC (in-sample) | Section 3.4 | 0.957 | ✓ |
| AUROC (in-sample) | Discussion | 0.957 | ✓ |
| AUROC (in-sample) | Conclusion | 0.957 | ✓ |
| AUROC (LOEO) | Section 3.4 | 0.988 | ✓ |
| AUROC (LOEO) | Limitations | 0.988 | ✓ |
| CIVO seeds | Introduction C1 | 7/7 | ✓ |
| CIVO seeds | Discussion | 7/7 | ✓ |

**⚠️ 不一致之处**:

**N-R4-1 [warning]: Seed 数量不一致**
- **Methodology Section 3.3** (methodology.tex line 32): "Key configurations use **4** seeds"
- **Results Section 4.2** (results.tex line 81): "all **five** Walker Walk seeds (peak NVE 1.53--4.72×)...IQM 175.2, **n=5**"
- **Conclusion Limitations** (conclusion.tex line 10): "Statistical power with **4** seeds per configuration is limited"
- **结论**: Methodology 和 Limitations 说 4 seeds，Results 说 5 seeds。如果确实增加了第 5 个 Walker seed，Methodology 和 Limitations 的 "4 seeds" 必须同步更新

**N-R4-2 [minor]: Figure 2 caption 未更新**
- **Figure 2 caption** (results.tex line 77): "n=**3** seeds plotted; seed~**4** data in Table"
- 如果有 5 个 Walker seeds，caption 应提及 seed 4 和 seed 5 的数据去向

**N-R4-3 [info]: IQM 值未变**
- IQM 从 175.2 (n=4) → 175.2 (n=5)：添加第 5 个 seed 后 IQM 保持完全相同在统计上不常见（though possible）。如果 IQM 确实没变，应该无问题。但建议作者 double-check 计算。

**N-R4-4 [minor]: Introduction "isolate" 未更新**
- Abstract 已改为 "identify"，但 Introduction line 6 仍使用 "we **isolate** the combination of a trained dt-embedding"
- Introduction Contribution 1 (line 11): "**isolate** trained dt-embedding + multi-rate exposure as jointly sufficient"
- Results Section 4 intro (line 4): "establish a **causal chain**"——虽然指的是 findings 的逻辑链，但 "causal chain" 措辞与全文弱化因果声明的方向不一致

---

## 新发现的问题

### N-R4-5 [critical]: 模板未更新
- **位置**: main.tex line 5
- **问题**: `\usepackage{corl_2026}` — 论文仍使用 CoRL 2026 模板，但目标 venue 已改为 ICML 2026
- **影响**: ICML 2026 使用自己的样式文件。提交 CoRL 格式的论文将导致**格式违规**，可能 desk reject
- **必须修改**: 替换为 ICML 2026 官方样式（`icml2026.sty`），同时检查页数、列宽、字体大小等是否合规

### N-R4-6 [minor]: Becker-Ehmck 2023 仍未引用
- Reviewer 2 在 Round 2 和 Round 3 均指出此遗漏，Round 4 仍未修复
- Grep 确认全文和 references 中均无 "Becker" 或 "ehmck" 匹配

### N-R4-7 [info]: ICML Limitations 格式
- 当前 Limitations 为 Conclusion Section 内的 `\paragraph{}`
- ICML 2026 reviewer form 包含 "Limitations assessment" 维度。虽然不硬性要求独立 section，但建议将 Limitations 独立为 section 以提升可见性

---

## ICML Venue Fit 评估

转投 ICML 后，venue fit 问题**基本消除**：

1. **ICML 核心受众**: RL methodology/analysis 论文是 ICML 的核心内容。CIVO 作为 imagination-based RL 的失败模式诊断，直接面向 ICML 的 world-model RL 读者群
2. **不再需要 robotics framing**: CoRL 审稿时 robotics relevance 是主要弱点。ICML 评价维度（Soundness, Significance, Originality, Presentation）全部与本文匹配
3. **Negative result 接受度**: ICML 历史上接受 diagnostic/negative result 论文（如 Henderson et al. 2018 "Deep RL That Matters"），本文的系统性 factorial 分析符合这一传统
4. **4-5 seeds 在 ICML 的充分性**: ICML RL 论文通常使用 3-10 seeds。本文的 5 seeds (Walker) + 2 seeds (Cheetah) + LOEO AUROC=0.988 满足 ICML 最低标准。Agarwal et al. 2021 IQM 报告是加分项

**评分: Venue Fit 8.5/10（vs Round 3 CoRL 的 6.5/10）**

---

## Issue 状态汇总

| Issue | Round 3 状态 | Round 4 状态 | 说明 |
|-------|-------------|-------------|------|
| R1-W2 步数不对等 | STILL_OPEN | **[RESOLVED]** | Discussion 新段 + Appendix D.4 302K 延长数据 |
| R2-W1 TAWM 对比 | STILL_OPEN | **[RESOLVED]** | "hypothesized structural factor" 全文一致 |
| N-new-1 Detector 样本量 | open | **[RESOLVED]** | 降级 "Preliminary" + CI + "requires validation" |
| N-new-3 Dual-critic 叙事 | open | **[PARTIALLY]** | Appendix 承认 open question，但主文 "gradient diversity" 措辞无支撑 |
| N-new-2 Baseline 缺失 | open | **[PARTIALLY]** | 脚注增加部分 baseline，2 个 ManiSkill 仍 "not measured" |
| 统计数据一致性 | — | **[STILL_OPEN]** | Seed 数量不一致（4 vs 5）、Figure caption 未更新 |
| 模板 | — | **[NEW, critical]** | 仍为 corl_2026，需改 ICML 2026 |
| Becker-Ehmck 引用 | R2 flagged ×2 | **[STILL_OPEN]** | 第三轮仍未引用 |

**Round 3 的 2 个 STILL_OPEN warning 全部 RESOLVED。**
**新增 1 个 critical（模板）+ 1 个 warning（seed 数量不一致）+ 若干 minor。**

---

## 方法严谨性总评

**评分: 7.5/10（ICML 标准）**

相较 Round 3 (7/10) 提升了 0.5 分，原因：
- 步数不对等问题通过 Discussion 段落 + 302K 延长数据实质性解决
- TAWM 措辞通过 "hypothesized" 一词和 future work 声明恰当弱化
- Detector 降级为 preliminary 诚实反映了统计效力限制

未达 8/10 的原因：
- **Seed 数量前后不一致**（4 vs 5）是一个 credibility 问题——reviewer 会质疑数据管理是否可靠
- **模板未更新**是 desk reject 风险
- **"gradient diversity" 无支撑**虽然是 minor，但反映了在添加解释时未配套实证的习惯

**ICML 推荐**: Weak Accept (4/6)。核心方法论和实验设计 sound，CIVO 发现对社区有价值，转投 ICML 消除了 venue fit 障碍。修复 seed 不一致和模板问题后可达 Accept (5/6)。


---

[Reviewer 1 审稿结果]:
审稿报告已提交。

核心结论：Round 3 的两个 open warning（步数不对等 + TAWM 措辞）均已 RESOLVED，但数据更新引入了新的不一致问题——Methodology/Limitations 说 "4 seeds" 而 Results 报告 5 Walker seeds，且模板仍为 `corl_2026` 未更新为 ICML 格式。方法严谨性从 7/10 提升至 7.5/10，ICML 推荐 Weak Accept (4/6)，修复 seed 不一致和模板后可达 Accept。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-24T09:35:02.859803+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Step 2 交叉分享 — Reviewer 2 的 Round 4 完整审稿意见\n\n请逐条回应，标注 [AGREE] 或 [REBUT]（附理由）。\n\n---\n\n### Reviewer 2 核心发现：\n\n**1. [CRITICAL] 模板仍为 `corl_2026`**\nPDF 页脚明确显示 CoRL。目标 venue 已改为 ICML 2026，以当前状态提交会被 desk reject。\n\n**2. [CRITICAL] 缺少 ICML 必需的 Impact Statement**\nICML 2026 要求 Broader Impact / Ethics Statement，当前论文中没有。\n\n**3. Venue fit 大幅改善**\n从 CoRL 的 5/10 提升到 ICML 的 8/10。Diagnostic/negative-result 论文在 ICML 有先例（Henderson et al. 2018 等）。\n\n**4. Round 3 具体审稿意见均已回应**\n\"structural factor\" 弱化、detector 降级、training horizon 数据、baseline 值补充——均已处理。\n\n**5. Overall: Weak Accept (4/6)**\nSoundness 和 Originality 为 Good，Significance 偏 Fair。\n\n---\n\n### 你的交叉任务：\n\n请特别关注以下问题，看你是否同意 R2 的判断：\n\n1. **Impact Statement 缺失是否为 critical**？你的审稿中未提及此问题——是你判断不需要，还是遗漏了？\n2. **R2 给 Significance 为 Fair**——你给了 3/4 (Good)。你是否仍维持你的评分？理由？\n3. **Venue fit 8/10 vs 你的 8.5/10**——差异可忽略，但请确认你是否同意 R2 的 ICML fit 评估。",
  "reviewer_id": "1",
  "project": "event-gated-adaptive-horizon",
  "round_number": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Step 2 交叉分享 — Reviewer 2 的 Round 4 完整审稿意见\n\n请逐条回应，标注 [AGREE] 或 [REBUT]（附理由）。\n\n---\n\n### Reviewer 2 核心发现：\n\n**1. [CRITICAL] 模板仍为 `corl_2026`**\nPDF 页脚明确显示 CoRL。目标 venue 已改为 ICML 2026，以当前状态提交会被 desk reject。\n\n**2. [CRITICAL] 缺少 ICML 必需的 Impact Statement**\nICML 2026 要求 Broader Impact / Ethics Statement，当前论文中没有。\n\n**3. Venue fit 大幅改善**\n从 CoRL 的 5/10 提升到 ICML 的 8/10。Diagnostic/negative-result 论文在 ICML 有先例（Henderson et al. 2018 等）。\n\n**4. Round 3 具体审稿意见均已回应**\n\"structural factor\" 弱化、detector 降级、training horizon 数据、baseline 值补充——均已处理。\n\n**5. Overall: Weak Accept (4/6)**\nSoundness 和 Originality 为 Good，Significance 偏 Fair。\n\n---\n\n### 你的交叉任务：\n\n请特别关注以下问题，看你是否同意 R2 的判断：\n\n1. **Impact Statement 缺失是否为 critical**？你的审稿中未提及此问题——是你判断不需要，还是遗漏了？\n2. **R2 给 Significance 为 Fair**——你给了 3/4 (Good)。你是否仍维持你的评分？理由？\n3. **Venue fit 8/10 vs 你的 8.5/10**——差异可忽略，但请确认你是否同意 R2 的 ICML fit 评估。",
    "reviewer_id": "1",
    "project": "event-gated-adaptive-horizon",
    "round_number": "4"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-24T09:35:25.622350+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22762
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-24T09:35:25.823609+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Step 2 交叉分享 — Reviewer 1 的 Round 4 完整审稿意见\n\n请逐条回应，标注 [AGREE] 或 [REBUT]（附理由）。\n\n---\n\n### Reviewer 1 核心发现：\n\n**1. [CRITICAL] 模板仍为 `corl_2026`**（与你的发现一致）\n\n**2. R1-W2 步数不对等 → [RESOLVED]**\nDiscussion 新增 \"Training horizon\" 段落，报告 302K 延长实验（exp_045 seed s3: NVE peak 4.91× → 自恢复至 0.05×, eval 867.6 = 94.7% baseline）。论文正确论证 105K 足以观察 onset (45K-65K window)。\n\n**3. R2-W1 TAWM 对比 → [RESOLVED]**\n\"hypothesized structural factor\" 全文一致，Conclusion 增加 \"Empirical validation on MPC-based architectures remains future work\"。\n\n**4. R3-N-new-1 Detector 样本量 → [RESOLVED]**\n降级为 \"Preliminary diagnostic\" + Clopper-Pearson CI [47.8%, 100%] + \"requires larger-sample validation\"。\n\n**5. R3-N-new-2 Dual-critic 叙事 → [PARTIALLY RESOLVED]**\nAppendix G.3 承认 open question，但主文 Section 4.8 使用 \"gradient diversity\" 措辞无实证支撑。建议改为 \"may instead function through a capacity-dependent mechanism during early training (Appendix G)\"。\n\n**6. [NEW, warning] N-R4-1: Seed 数量前后不一致**\n- Methodology Section 3.3: \"Key configurations use **4** seeds\"\n- Results Section 4.2: \"all **five** Walker Walk seeds, n=5\"\n- Conclusion Limitations: \"Statistical power with **4** seeds\"\n- Figure 2 caption: \"n=3 seeds plotted; seed 4 data in Table\"（若有 5 seeds 则应更新）\n- IQM 175.2 在 n=4→n=5 后完全不变——统计上不常见\n\n**7. [NEW, minor] N-R4-4: Introduction 仍用 \"isolate\" + \"causal chain\"**\nAbstract 已改 \"identify\"，但 Introduction line 6/11 仍使用 \"isolate\"，Results Section 4 使用 \"causal chain\"，与弱化因果声明的方向不一致。\n\n**8. [minor] N-R4-6: Becker-Ehmck 2023 仍未引用**\n第三轮指出仍未修复。\n\n**9. Overall: Weak Accept (4/6), 方法严谨性 7.5/10, Venue fit 8.5/10**\n\n---\n\n### 你的交叉任务：\n\n1. **N-R4-1 Seed 数量不一致**——你是否也注意到？这是否影响你对 Soundness 的评分？\n2. **\"gradient diversity\" 无支撑**——你是否同意 R1 的 PARTIALLY RESOLVED 判定？\n3. **R1 判定 R1-W2 (步数不对等) 和 R2-W1 (TAWM) 均为 RESOLVED**——你是否同意？\n4. **N-R4-4 Introduction \"isolate\" 残留**——严重性如何？\n5. **Becker-Ehmck 2023**——R1 也确认 Round 4 仍未引用。你之前在 Round 2/3 均提出此问题，Round 3 报告中指出已以 benechehab2023multitimestep 引用（认为审稿人混淆了作者名）。你是否接受这一解释？",
  "reviewer_id": "2",
  "project": "event-gated-adaptive-horizon",
  "round_number": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Step 2 交叉分享 — Reviewer 1 的 Round 4 完整审稿意见\n\n请逐条回应，标注 [AGREE] 或 [REBUT]（附理由）。\n\n---\n\n### Reviewer 1 核心发现：\n\n**1. [CRITICAL] 模板仍为 `corl_2026`**（与你的发现一致）\n\n**2. R1-W2 步数不对等 → [RESOLVED]**\nDiscussion 新增 \"Training horizon\" 段落，报告 302K 延长实验（exp_045 seed s3: NVE peak 4.91× → 自恢复至 0.05×, eval 867.6 = 94.7% baseline）。论文正确论证 105K 足以观察 onset (45K-65K window)。\n\n**3. R2-W1 TAWM 对比 → [RESOLVED]**\n\"hypothesized structural factor\" 全文一致，Conclusion 增加 \"Empirical validation on MPC-based architectures remains future work\"。\n\n**4. R3-N-new-1 Detector 样本量 → [RESOLVED]**\n降级为 \"Preliminary diagnostic\" + Clopper-Pearson CI [47.8%, 100%] + \"requires larger-sample validation\"。\n\n**5. R3-N-new-2 Dual-critic 叙事 → [PARTIALLY RESOLVED]**\nAppendix G.3 承认 open question，但主文 Section 4.8 使用 \"gradient diversity\" 措辞无实证支撑。建议改为 \"may instead function through a capacity-dependent mechanism during early training (Appendix G)\"。\n\n**6. [NEW, warning] N-R4-1: Seed 数量前后不一致**\n- Methodology Section 3.3: \"Key configurations use **4** seeds\"\n- Results Section 4.2: \"all **five** Walker Walk seeds, n=5\"\n- Conclusion Limitations: \"Statistical power with **4** seeds\"\n- Figure 2 caption: \"n=3 seeds plotted; seed 4 data in Table\"（若有 5 seeds 则应更新）\n- IQM 175.2 在 n=4→n=5 后完全不变——统计上不常见\n\n**7. [NEW, minor] N-R4-4: Introduction 仍用 \"isolate\" + \"causal chain\"**\nAbstract 已改 \"identify\"，但 Introduction line 6/11 仍使用 \"isolate\"，Results Section 4 使用 \"causal chain\"，与弱化因果声明的方向不一致。\n\n**8. [minor] N-R4-6: Becker-Ehmck 2023 仍未引用**\n第三轮指出仍未修复。\n\n**9. Overall: Weak Accept (4/6), 方法严谨性 7.5/10, Venue fit 8.5/10**\n\n---\n\n### 你的交叉任务：\n\n1. **N-R4-1 Seed 数量不一致**——你是否也注意到？这是否影响你对 Soundness 的评分？\n2. **\"gradient diversity\" 无支撑**——你是否同意 R1 的 PARTIALLY RESOLVED 判定？\n3. **R1 判定 R1-W2 (步数不对等) 和 R2-W1 (TAWM) 均为 RESOLVED**——你是否同意？\n4. **N-R4-4 Introduction \"isolate\" 残留**——严重性如何？\n5. **Becker-Ehmck 2023**——R1 也确认 Round 4 仍未引用。你之前在 Round 2/3 均提出此问题，Round 3 报告中指出已以 benechehab2023multitimestep 引用（认为审稿人混淆了作者名）。你是否接受这一解释？",
    "reviewer_id": "2",
    "project": "event-gated-adaptive-horizon",
    "round_number": "4"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-24T09:35:27.282872+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1459
}
```

</details>

---


### Assistant

_source line 318 · 2026-05-24T09:35:35.357480+00:00_

交叉分享已派发。两位 Reviewer 的初审高度一致：

- **评分**：均为 Weak Accept (4/6)
- **共识 CRITICAL**：模板仍为 `corl_2026`（两人均 flagged）；R2 额外发现缺少 ICML Impact Statement
- **Round 3 遗留问题**：R1-W2（步数不对等）和 R2-W1（TAWM 措辞）均 RESOLVED
- **新问题**：R1 发现 seed 数量不一致（Methodology 说 4，Results 报告 5）；R2 发现缺 Impact Statement

等待两位 Reviewer 的交叉回应。关键分歧点：Significance 评分（R1: Good 3/4 vs R2: Fair）和 seed 不一致的严重性判定。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 26

## Round 26

2 recorded events


### User

_source line 319 · 2026-05-24T09:36:07.837302+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 Round 4 意见的交叉回应

---

## 1. [CRITICAL] 模板仍为 `corl_2026`

**[AGREE] R2**

我在 Round 4 审稿中同样将此标记为 N-R4-5 [critical]。main.tex line 5 确认 `\usepackage{corl_2026}`。这是 desk reject 风险，无争议。

---

## 2. [CRITICAL] 缺少 ICML 必需的 Impact Statement

**[AGREE] R2 — 这是我的遗漏，不是判断不需要。**

我在 Round 4 审稿中未提及 Impact Statement / Broader Impact 缺失，这是审查疏忽。ICML 2026 Reviewer Instructions 明确包含 "Limitations assessment" 和 "Ethical Concerns" 作为 review form 维度。虽然 ICML 2025/2026 对 Broader Impact 的要求不如 NeurIPS 那样硬性（NeurIPS 曾要求独立 Broader Impact section），但缺少任何形式的 ethical/societal impact 讨论确实是一个合规风险。

具体来说：
- 论文当前的 Limitations 段落（Conclusion 内的 `\paragraph{}`）讨论了技术局限（seeds、architecture、reward scales），但**未涉及 broader impact**
- 对于一篇诊断 RL failure mode 的论文，broader impact 可以自然地讨论：(a) 该发现对安全部署 world-model RL 的意义；(b) 负面结果公开发表对社区的价值；(c) 不存在明显的负面社会影响
- 这段内容简短（3-5 句）但必须存在

**结论**: R2 正确识别了这一遗漏。我将其严重度评估为 **warning 而非 critical**——因为 ICML 对此的执行力度不如模板格式那样严格（不会自动 desk reject），但缺失确实会被 reviewer 在 form 中标记。

---

## 3. Venue fit 大幅改善

**[AGREE] R2**

我给 8.5/10，R2 给 8/10，差异可忽略。我同意 R2 的核心判断：ICML 是显著更好的 venue。Diagnostic/negative-result 论文在 ICML 有明确先例。0.5 分的差异来自我对 factorial design 在 ICML methodology track 中价值的略高估计，不影响结论。

**确认 ICML fit**: 同意 R2 的 8/10 评估。

---

## 4. Round 3 审稿意见回应

**[AGREE] R2**

与我的 Round 4 逐条检查结果一致：
- "structural factor" → "hypothesized structural factor": [RESOLVED] ✓
- Detector 降级 "Preliminary diagnostic" + CI: [RESOLVED] ✓
- Training horizon 302K 数据: [RESOLVED] ✓
- Baseline 值脚注: [PARTIALLY RESOLVED] ✓

---

## 5. Overall Weak Accept (4/6)

**[AGREE] R2**

我同样给出 Weak Accept (4/6)。

---

## 交叉任务专项回应

### Q1: Impact Statement 缺失是否为 critical？

如上所述，**这是我的遗漏**。我将其评估为 **high warning 而非 critical**：
- Critical = desk reject 风险。ICML 对 Impact Statement 的缺失不会自动 desk reject（不同于模板格式违规）
- 但 reviewer form 有 "Ethical Concerns" 和 "Limitations" 字段。完全缺失 broader impact 讨论会导致 reviewer 在这些字段给出负面标记
- 修复成本极低（3-5 句话），应该立即添加

### Q2: Significance — Fair vs Good？

**我维持 Good (3/4)，但承认这是 borderline。**

理由：
1. **CIVO 作为 failure mode 的发现价值**: 任何计划在 DreamerV3 或类似架构中使用 temporal abstraction 的研究者都需要知道这个结果。这不是一个小众问题——temporal abstraction 在 world-model RL 中是活跃的研究方向（TAWM, Director 等近期工作）
2. **Dual-critic convergence (ρ>0.999) 的 insight**: 这个发现超越了 CIVO 本身——它揭示了 pure-imagination training 中 Double Q pessimism 失效的结构性原因。这对任何在 imagination-based training 中使用 dual critic 的研究有广泛意义
3. **四级干预层级的系统性 negative result**: 不仅展示了 "什么不 work"，更展示了 "为什么不 work"（gradient pathway redundancy, representation-level coupling）

R2 给 Fair 的逻辑可能是：CIVO 是 locomotion-specific（2 环境），且无 actionable solution。这些都是合理的限制。但对 ICML 受众而言，systematic diagnostic methodology + structural insight 的组合达到了 Good 的门槛。

**如果 R2 的 Fair 是基于 "impact 局限于 DreamerV3 一个架构"**，我部分同意——论文未验证其他 imagination-based 架构。但 DreamerV3 是该领域最广泛使用的 baseline，其失败模式分析本身有足够的 significance。

**最终判断**: 维持 Good (3/4)，但认可 R2 的 Fair (2/4) 也是合理的。这属于 reviewer 间正常的评分分歧。

### Q3: Venue fit 8/10 vs 8.5/10

**接受 R2 的 8/10**。0.5 分差异无实质意义，我不坚持 8.5。两位 reviewer 一致认为 ICML 是合适的 venue。

---

## 两位 Reviewer 的共识与分歧总结

| 维度 | R1 | R2 | 共识？ |
|------|----|----|--------|
| Overall | Weak Accept (4/6) | Weak Accept (4/6) | ✅ 完全一致 |
| Soundness | Good (3/4) | Good (3/4) | ✅ 完全一致 |
| Originality | Good (3/4) | Good (3/4) | ✅ 完全一致 |
| Significance | **Good (3/4)** | **Fair (2/4)** | ⚠️ 分歧（见上） |
| Presentation | Good (3/4) | Good (3/4) | ✅ 完全一致 |
| 模板问题 | Critical | Critical | ✅ 完全一致 |
| Impact Statement | 遗漏（现补 warning） | Critical | ⚠️ 严重度分歧 |
| Venue fit (ICML) | 8.5→8/10 | 8/10 | ✅ 一致 |

**共识**: 论文在方法论上 sound，转投 ICML 后 venue fit 合理，需修复模板 + Impact Statement + seed 数量不一致后可达 Accept。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 320 · 2026-05-24T09:36:14.363338+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 27

## Round 27

18 recorded events


### User

_source line 321 · 2026-05-24T09:36:16.994873+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交。两位 Reviewer 在 Overall (Weak Accept 4/6)、Soundness、Originality、Presentation 上完全一致。唯一实质分歧是 Significance（我给 Good，R2 给 Fair）——我维持 Good 但承认 borderline，主要基于 dual-critic convergence insight 和 systematic negative result 的 ICML 社区价值。我补充承认了 Impact Statement 遗漏是审查疏忽。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-24T09:36:45.718650+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-24T09:36:45.770617+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-24T09:36:48.480089+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-24T09:36:48.781681+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-24T09:36:48.782154+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-24T09:36:48.832654+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-24T09:27:39.638747+00:00\", \"completed_at\": \"2026-05-24T09:31:41.105902+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 1-4\", \"message\": \"连续 4 页纯文本无任何 display item（figure/table/equation block）。审稿人打开论文后需读 4 页密集文字才能看到第一个视觉锚点（Table 1，page 5）。这严重损害第一印象——诊断/实证类论文的前 2 页内应至少有一个概览图或核心结果表。建议：将 Figure 6（CTVO 机制路径图，当前在 appendix page 17）或一个简化的架构/诊断框架概览图提前到 Section 1 或 Section 3 开头。\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-8\", \"message\": \"主体正文 8 页仅 4 个 display items（Table 1, Figure 1, Figure 2, Table 2）。对诊断分析类论文偏少，建议至少增加 1 个概念图（如 CTVO 机制图）和 1 个汇总可视化，使 display items 达到 6 个。\"}, {\"severity\": \"warning\", \"dimension\": \"page 3-4\", \"message\": \"Section 3（Experimental Setup）跨 2 页纯文本，描述了架构、变量率机制、diagnostic metrics 等复杂设计，但无任何图示辅助。建议加一个实验设计概览图或架构示意图（即使是简化版 Figure 6 中的 pathway 图）。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Section 5 Discussion + Section 6 Conclusion 挤在同一页，且全为纯文本。Discussion 没有任何 display item 辅助总结（如 finding summary 表或 limitation taxonomy 图），与前面的纯文本页叠加后，论文后半段给人\\\"全是字\\\"的压迫感。\"}, {\"severity\": \"warning\", \"dimension\": \"page 33\", \"message\": \"最后一页 Table 22 仅占页面约 35-40%，下方约 60% 为空白。可考虑将前页的某个表格移至此页平衡空间，或在此处放置附录中的某个图。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 使用 booktabs 风格，最优结果已加粗，格式规范。Figure 1（Learning Curves）清晰可读，诊断阈值虚线标注清楚。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 1 图例中有 6 条线，颜色区分度尚可，但在灰度打印下可能难以区分——建议辅以不同 line style（dashed/dotted）或 marker shape。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2（NVE trajectories）三种轨迹类型用颜色+标注区分，清晰度良好。Dashed 阈值线辅助阅读。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2（Intervention hierarchy）结构清晰，booktabs 风格，列对齐良好。\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Figure 3（ROC curve）附录中质量良好，95% CI shading 清晰
…[truncated 1180 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-24T09:37:05.431402+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
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

_source line 329 · 2026-05-24T09:37:05.431763+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-24T09:37:09.699055+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-24T09:37:10.251770+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_reports/round_3.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-24T09:37:10.352712+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-24T09:37:10.403437+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-24T09:37:15.524079+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_reports/round_3.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_reports/round_3.md"
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-24T09:37:15.926250+00:00_

1	---
2	round: 3
3	review_mode: continue
4	overall_score: weak reject
5	timestamp: 2026-05-24T07:19:49.260508+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# 审稿报告 — Round 3
12	
13	**论文**: "Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
14	**目标 Venue**: CoRL 2026 Main Conference
15	**审稿日期**: 2026-05-24
16	**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验充分性 | R2: Venue Fit + 贡献度 + 写作质量）
17	**轮次**: Round 3 继续审稿（修订评估）+ 交叉分享（1 轮收敛）
18	**上轮评分**: Round 1 Strong Reject (4/10)
19	
20	---
21	
22	## Summary
23	
24	论文在 Round 1 (Strong Reject) 后进行了大幅修改：从 1 环境扩展到 5 环境（Walker Walk, Cheetah Run, PickCube-v1, StackCube-v1, PegInsertionSide-v1），关键配置 seeds 增至 4，引入 LOEO 交叉验证（AUROC=0.981），因果语言全面弱化为 "strongest predictor"，新增四级干预层级分析和在线 CIVO 检测器，切换至 CoRL 2026 PMLR 模板，添加 robotics framing 和 ManiSkill 实验。论文现在识别 CIVO 为 locomotion-specific（6/6 locomotion seeds 触发，0/5 manipulation configurations 触发），并提供了 discriminative validity（frozen-embedding 控制正确区分 CIVO 与环境特异性 transient）。
25	
26	---
27	
28	## Strengths
29	
30	1. **Factorial design 系统且严谨**（2/2 reviewer 共识）：43 配置 × 4 seeds × 5 环境的设计空间覆盖广泛；primary/secondary comparison 标注清晰；2×2 factorial grid 完整
31	2. **LOEO 交叉验证显著增强统计可信度**：AUROC=0.953 (in-sample, n=29), 0.981 (LOEO, 3 folds) 在 RL 诊断类工作中是扎实的统计功效水平
32	3. **四级干预层级分析**（gradient/output/representation/architecture）：提供了系统性的 negative result，对社区有长期参考价值。Gradient magnitude ≠ causal importance 的发现（reward head 38-49% 但 SGS 无效）是有洞见的
33	4. **ManiSkill non-CIVO 结果增加 discriminative validity**：NVE 诊断能正确区分 dt-embedding-dependent CIVO 与环境特异性 transient（frozen controls 匹配 trained spikes），展示了方法论的特异性
34	5. **Dual-critic convergence (ρ > 0.999)**：关于 imagination-based training 中 Double Q pessimism 失效的 structural insight 有价值
35	6. **Limitations section 诚实全面**：主动承认 4-seed 局限、architecture 局限、locomotion-specificity，ManiSkill non-CIVO 如实报告
36	7. **Signed error 分析**：dt=2 underprediction (SE=-0.599) 排除 observation-level re
…[truncated 9946 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-24T09:37:15.976866+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-24T09:37:16.028085+00:00_

1	issues:
2	  - id: "R1-N1"
3	    summary: "统计检验力严重不足：2-3 seeds 无法支撑 causal factor 声明"
4	    category: experiment
5	    severity: critical
6	    status: resolved
7	    first_raised_round: 1
8	    last_seen_round: 3
9	    mentions:
10	      - round: 1
11	        reviewers: [1, 2, 3]
12	        note: "三位 reviewer 均认同统计效力不足"
13	      - round: 3
14	        reviewers: [1, 2]
15	        note: "两位 reviewer 一致判定 RESOLVED。Seeds 增至 4，语言改为 strongest predictor，LOEO AUROC=0.981，IQR 报告。残留小问题：Abstract 中 isolate 一词仍携带因果含义。"
16	    action_items:
17	      - round: 1
18	        action: "补 seeds 到 4 per key config"
19	        assigned_to: agent
20	        status: done
21	      - round: 1
22	        action: "弱化因果语言: causal factor → strongest predictor"
23	        assigned_to: paper_agent
24	        status: done
25	      - round: 1
26	        action: "统计报告改用 IQM + bootstrap CI per Agarwal et al. 2021"
27	        assigned_to: paper_agent
28	        status: done
29	    resolution: "Seeds 增至 4，因果语言全面弱化为 strongest predictor，LOEO 交叉验证 AUROC=0.981，IQM + bootstrap CI 报告完整。"
30	    resolution_round: 3
31	
32	  - id: "R1-N2"
33	    summary: "NVE 阈值 1.5× 为 post-hoc 选择，88.9% accuracy 是训练准确率，无独立验证"
34	    category: method
35	    severity: critical
36	    status: resolved
37	    first_raised_round: 1
38	    last_seen_round: 1
39	    mentions:
40	      - round: 1
41	        reviewers: [1, 2, 3]
42	        note: "三位 reviewer 一致认为 post-hoc"
43	    action_items:
44	      - round: 1
45	        action: "LOEO cross-validation: mean AUROC 0.981"
46	        assigned_to: agent
47	        status: done
48	    resolution: "LOEO 交叉验证完成：3 环境 leave-one-out，mean AUROC 0.981，θ=1.5 在全部 fold 最优范围。论文措辞已改为 in-sample + LOEO cross-validated。"
49	    resolution_round: 1
50	
51	  - id: "R1-N3"
52	    summary: "CoRL venue fit 严重不足：全文无 robotics 实验/讨论"
53	    category: framing
54	    severity: critical
55	    status: in_progress
56	    first_raised_round: 1
57	    last_seen_round: 3
58	    mentions:
59	      - round: 1
60	      
…[truncated 15105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Assistant

_source line 338 · 2026-05-24T09:37:39.441609+00:00_

R1 交叉回应已收到，要点记录：

- **Overall**: 两位 Reviewer 一致 Weak Accept (4/6)
- **Soundness / Originality / Presentation**: 完全一致
- **唯一分歧**: Significance（R1: Good, R2: Fair）—— R1 维持 Good，理由是 dual-critic convergence insight + systematic negative result 的 ICML 社区价值
- **R1 补充承认**: Impact Statement 遗漏是审查疏忽

等待 R2 交叉回应到达后进入报告合成阶段。当前 venue 已从 CoRL 切换至 ICML（评分体系 6 分制）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 28

## Round 28

26 recorded events


### User

_source line 339 · 2026-05-24T09:38:48.047325+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 Round 4 审稿意见的逐条评议

---

### 1. [CRITICAL] 模板仍为 `corl_2026`
**[AGREE]** 与我的发现完全一致。PDF 页脚显示 "Submitted to the 10th Conference on Robot Learning (CoRL, 2026)"。必须切换到 `icml2026.sty`。我在自己的审稿中也将此列为两个 CRITICAL 格式问题之一（另一个是缺少 Impact Statement，R1 似乎未提及）。

---

### 2. R1-W2 步数不对等 → [RESOLVED]
**[AGREE]** Discussion 新增的 "Training horizon" 段落（analysis.tex:10-11）提供了关键数据：exp_045 seed s3 在 302K 步后完全 self-recovery（NVE 4.91× → 0.05×, eval 867.6 = 94.7% baseline）。这充分证明了：
- 105K 步足以观察 CIVO onset（45K-65K window）
- Recovery 需要 ~170K 额外步数，计算成本高，支持论文的核心论点
- "14-19% of baseline" 的 claim 限定在 105K 时间窗口内是准确的

R1 给出 RESOLVED 是合理的。

---

### 3. R2-W1 TAWM 对比 → [RESOLVED]
**[AGREE]** 两处修改充分回应了我在 Round 3 交叉评议中的关切：
- Abstract/Conclusion: "a hypothesized structural factor"（全文一致）
- Conclusion: "Empirical validation on MPC-based architectures (e.g., TD-MPC2) remains future work"

措辞准确反映证据级别，不再 overclaim。

---

### 4. R3-N-new-1 Detector 样本量 → [RESOLVED]
**[AGREE]** 降级为 "Preliminary diagnostic" + Clopper-Pearson CI [47.8%, 100%] + "requires larger-sample validation"（results.tex:178）是对小样本限制的诚实披露。Contribution 列表中的表述（introduction.tex:14）也相应调整。

---

### 5. R3-N-new-2 Dual-critic "gradient diversity" → [PARTIALLY RESOLVED]
**[AGREE]** R1 的判定准确。

具体问题在 results.tex:166：
> "Pessimistic estimation is thus ineffective; the min operation in wide dual-critic may instead regularize through **gradient diversity** (Appendix G)."

- "gradient diversity" 是一个具有特定技术含义的术语（如 gradient diversity in distributed optimization），论文在此处使用它来解释为什么 wide dual-critic + min 能在 ρ > 0.999 下仍然有效，但 **appendix 中没有提供 gradient diversity 的直接证据**（如 gradient cosine similarity、gradient variance 等指标）。
- R1 建议改为 "may instead function through a capacity-dependent mechanism during early training (Appendix G)" 是更准确的替代方案。
- 同时，introduction.tex:13 中 "the min operation enables recovery through a different mechanism" 的措辞反而更合适——承认了机制不明但避免了无根据的猜测。主文 Section 4.8 应与此一致。

**影响 Soundness 评分**：此问题的严重性较低（"may" 限定词已降低了 claim 强度），但在 ICML 的 soundness 标准下，无支撑的机制假说不应出现在主文中。建议用 R1 的替代措辞或直接说 "the mechanism is an open question"。

---

### 对 Director 的 5 个具体问题的回答

#### Q1: N-R4-1 Seed 数量不一致——是否影响 Soundness？

**[AGREE]** 我独立确认了这个问题，而且问题比 R1 描述的更严重。

**不一致的具体位置**：
| 位置 | 文本 | 问题 |
|------|------|------|
| methodology.tex:32 | "Key configurations use **4** seeds" | 与 n=5 不一致 |
| results.tex:81 | "all **five** Walker Walk seeds...IQM $175.2$, $n{=}5$" | 声称 n=5 |
| conclusion.tex:10 | "Statistical power with **4** seeds" | 与 n=5 不一致 |
| Figure 2 caption (results.tex:77) | "n=3 seeds plotted; **seed 4** data in Table" | 应提及 seed 5 |

**更严重的问题——IQM 数值错误**：

从 Appendix（appendix.tex:600-604），5 个 Walker seeds 的 eval 值为：
- s1: 82.8, s2: 267.9, s3: 268, s4: 63.6, s5: 95.8

排序后：{63.6, 82.8, 95.8, 267.9, 268.0}

- **n=4 时 IQM**（25% trim, 去掉首尾各 1）：middle 2 = {82.8, 267.9} → mean = **175.35 ≈ 175.2** ✓
- **n=5 时 IQM**（25% trim, 去掉首尾各 1）：middle 3 = {82.8, 95.8, 267.9} → mean = **148.8**，**而非 175.2**

IQM 175.2 是 n=4 的正确值，添加第 5 个 seed（eval 95.8）后未重新计算。这是一个**数据完整性错误**，不是四舍五入问题。

**对 Soundness 的影响**：将我的 Soundness 评分从 Good (3/4) 微调至 Good- (2.75/4)。错误本身是 careless 而非 systematic，不影响核心结论（CIVO 仍然在所有 5 seeds 中出现），但对于一篇以统计严谨性为卖点的 diagnostic paper（引用 Agarwal et al. 2021、报告 LOEO AUROC），这类不一致会损害可信度。

**修复**：(1) 重新计算 n=5 的 IQM 并更新 results.tex:81；(2) methodology.tex:32 改为 "Key configurations use 4-5 seeds"；(3) conclusion.tex:10 同步更新；(4) Figure 2 caption 更新提及 seed 5。

---

#### Q2: "gradient diversity" 无支撑——是否同意 PARTIALLY RESOLVED？

**[AGREE]** 已在上文第 5 点详细说明。R1 的判定和替代措辞建议都合理。

---

#### Q3: R1-W2 和 R2-W1 均判为 RESOLVED——是否同意？

**[AGREE]** 两者均同意。理由已在上文第 2、3 点给出。

---

#### Q4: N-R4-4 Introduction "isolate" 残留——严重性如何？

**[REBUT — minor, not warning]**

R1 标为 minor 是合理的，但我认为这个问题的实际严重性比 R1 暗示的更低：

- "isolate" 在实验科学中是标准的 factorial ablation 术语——当你通过 2×2 设计控制其他变量来测试某因素的效应时，"isolate the effect of X" 是准确的描述。Abstract 用 "identify" 是更保守的选择，但 Introduction 和 Results 中的 "isolate" 并不 overclaim。
- "causal chain"（results.tex:4）更值得注意——"establish a causal chain" 暗示了因果推断，而 factorial ablation 提供的是 predictive/associative 证据。但在 RL 实验传统中，这种用法是常见的（Henderson et al. 2018 也使用类似措辞）。
- 建议将 "establish a causal chain" 改为 "trace a pathway" 或 "establish a predictive chain"。这是 minor 修改，不影响接收决定。

---

#### Q5: Becker-Ehmck 2023——是否接受混淆解释？

**[AGREE — 接受，降级为 non-issue]**

重新审视此问题：
1. Round 1 原始 issue 仅提到 "Becker-Ehmck 2023" 未给出论文标题
2. Philip Becker-Ehmck 的已知工作（TD-VAE, ICLR 2020）是关于 temporal abstraction in latent models，但那是 2020 年的
3. 我搜索后未找到一篇 2023 年的 "Becker-Ehmck" 论文与本文直接相关
4. Benechehab et al. 2023 (benechehab2023multitimestep) 关于 multi-timestep models in MBRL 的工作与本文直接相关，且已被引用（related_work.tex:8）
5. 两者的主题高度重叠（multi-timestep prediction in model-based RL），名字有一定相似性

混淆解释是合理的。如果确实存在一篇特定的 Becker-Ehmck 2023 论文应该引用，Round 1 reviewer 应该提供具体标题。在当前信息下，我不再追踪此 issue。R1 继续标记为 "仍未引用" 是 technically correct 但 practically irrelevant。

---

### 评分调整

**修改前（纯基于文本审查）→ 修改后（考虑 R1 的发现）**

| 维度 | R2 原始评分 | 调整后 | 理由 |
|------|------------|--------|------|
| Soundness | Good (3/4) | Good- (2.75/4) | Seed 数量不一致 + IQM 未重算是 data integrity 问题 |
| Presentation | Good (3/4) | Good (3/4) | 不变 |
| Significance | Fair (2/4) | Fair (2/4) | 不变 |
| Originality | Good (3/4) | Good (3/4) | 不变 |

**Overall Recommendation**: 维持 **4 (Weak Accept)**。Seed/IQM 不一致是 careless error 而非 fundamental flaw，可在 camera-ready 中修复。核心结论（CIVO 在所有 seeds 中出现、无可靠干预）不受影响。

---

### 与 R1 评分对比

| 维度 | R1 | R2 | 差异说明 |
|------|-----|-----|----------|
| Overall | 4 (Weak Accept) | 4 (Weak Accept) | 一致 |
| 方法严谨性 | 7.5/10 | 7/10 | R2 因 IQM 错误和 "gradient diversity" 略低 |
| Venue fit | 8.5/10 | 8/10 | 基本一致，R2 稍保守（robotics framing 在 ICML 中不加分也不减分） |

**两位 reviewer 的核心共识**：
1. 论文在 ICML 中比 CoRL 更合适
2. Factorial design 是最大优势
3. Scope 和 significance 是主要 weakness
4. 模板必须修复
5. Weak Accept 是当前合理的推荐

**我的补充（R1 未提及）**：
- **Impact Statement 缺失**：ICML 2026 要求 "Impact statement at end of paper (before References)"，当前论文缺少此 section。这与模板问题同样是 desk reject 风险。
- **Keywords**：`\keywords{}` 命令是 CoRL 特有的，ICML 模板可能不支持，切换模板时需处理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-24T09:39:15.672833+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-24T09:39:16.627256+00:00_

1	\documentclass{article}
2	
3	% Load xcolor before corl_2026 (which loads color internally)
4	\usepackage[table]{xcolor}
5	\usepackage{corl_2026}
6	
7	\usepackage[utf8]{inputenc}
8	\usepackage[T1]{fontenc}
9	\usepackage{amsmath,amssymb}
10	\usepackage{booktabs}
11	\usepackage{multirow}
12	\usepackage{graphicx}
13	\graphicspath{{../../artifacts/}}
14	\usepackage{colortbl}
15	\usepackage{caption}
16	\usepackage{subcaption}
17	\usepackage{array}
18	\usepackage{enumitem}
19	\usepackage{wrapfig}
20	\usepackage{algorithm}
21	\usepackage{algorithmic}
22	
23	% Custom commands
24	\newcommand{\dt}{\mathrm{dt}}
25	\newcommand{\nve}{\mathrm{nve}}
26	% SGS result values (018 seed 1: partial mitigation; seed 2: collapsed — 0/3 CIVO elimination)
27	\newcommand{\sgseval}{448.3}
28	\newcommand{\sgsnve}{1.66}
29	\newcommand{\sgsclaim}{reduced CIVO severity in one of two Walker seeds but eliminated it in neither (0/3 across environments)}
30	\newcommand{\ie}{\textit{i.e.}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-24T09:39:17.129858+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "impact|Impact Statement",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "impact|Impact Statement",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-24T09:39:17.632420+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-24T09:39:17.984344+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "IQM|175\\.2|interquartile",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "IQM|175\\.2|interquartile",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-24T09:39:18.035049+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex:81:The trained $\dt$-embedding precedes CIVO in all five Walker Walk seeds (peak NVE $1.53$--$4.72\times$), universally degrading performance to below 30\% of baseline (IQM $175.2$, $n{=}5$; \citealt{agarwal2021precipice}). Combined with Cheetah Run (\S\ref{sec:f6}), CIVO onset is universal across all seven tested seeds ($n{=}7$, two environments) with 6/7 suffering sustained policy collapse, 1/7 self-correcting (Appendix~\ref{sec:seed_divergence}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-24T09:39:29.735556+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "82\\.8|267\\.9|63\\.6|95\\.8",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "context": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "82\\.8|267\\.9|63\\.6|95\\.8",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "context": "3"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-24T09:39:30.438854+00:00_

23-005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\
24-\midrule
25-\rowcolor{gray!15}
26:008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\times$ & Full collapse \\
27-\rowcolor{gray!15}
28:009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\times$ & Transient CIVO \\
29-\rowcolor{gray!15}
30-008d\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\diamond$ @105K & 1.53$\times$ & Late-onset collapse \\
31-\rowcolor{gray!15}
32:008d\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\times$ & Full collapse \\
33-\rowcolor{gray!15}
34:059 & Factorial (s5) & trn & ON & 8 & 95.8 @105K & 4.72$\times$ & Collapse$^\dagger$ \\
35-008f & No dt\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\times$ & Healthy \\
36-008f s4 & No dt\_emb (s4) & --- & ON & 8 & 306.5 @105K & 1.41$\times$ & Healthy \\
37-009c s3 & No dt\_emb (s3) & --- & ON & 8 & 311.9 @105K & 1.04$\times$ & Healthy \\
--
161-\toprule
162-Threshold & TP & FP & FN & TN & Accuracy [95\% CI] & Precision & Recall & F1 \\
163-\midrule
164:$\geq 1.0\times$ & 3 & 4 & 0 & 4 & 63.6\% \; [30.8, 89.1] & 42.9\% & 100\% & 60.0\% \\
165-$\geq 1.2\times$ & 3 & 3 & 0 & 5 & 72.7\% \; [39.0, 94.0] & 50.0\% & 100\% & 66.7\% \\
166-$\geq 1.5\times$ & 3 & 3 & 0 & 5 & 72.7\% \; [39.0, 94.0] & 50.0\% & 100\% & 66.7\% \\
167-\rowcolor{gray!15}
--
204-\toprule
205-Threshold & TP & FP & FN & TN & Accuracy [95\% CI] & Precision & Recall & F1 \\
206-\midrule
207:$\geq 1.0\times$ & 9 & 2 & 0 & 6 & 88.2\% \; [63.6, 98.5] & 81.8\% & 100\% & 90.0\% \\
208-$\geq 1.2\times$ & 9 & 1 & 0 & 7 & 94.1\% \; [71.3, 99.9] & 90.0\% & 100\% & 94.7\% \\
209-\rowcolor{gray!15}
210-$\geq 1.5\times$ & 9 & 1 & 0 & 7 & 94.1\% \; [71.3, 99.9] & 90.0\% & 100\% & 94.7\% \\
211-$\geq 1.7\times$ & 7 & 1 & 2 & 7 & 82.4\% \; [56.6, 96.2] & 87.5\% & 77.8\% & 82.4\% \\
212-$\geq 2.0\times$ & 7 & 1 & 2 & 7 & 82.4\% \; [56.6, 96.2] & 87.5\% & 77.8\% & 82.4\% \\
213:$\geq 3.9\times$ & 7 & 0 & 2 & 8 & 88.2\% \; [63.6, 98.5] & 100\% & 77.8\% 
…[truncated 1736 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Grep",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-24T09:39:30.590045+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "seeds|n=4|n=5|seed 4|seed 5",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex",
  "output_mode": "content",
  "context": "2",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "seeds|n=4|n=5|seed 4|seed 5",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex",
    "output_mode": "content",
    "context": "2",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-24T09:39:30.590412+00:00_

30-\label{sec:factorial}
31-
32:[Omitted long matching line]
33-
34-\subsection{Diagnostic Metrics}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-24T09:39:31.343368+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "gradient diversity|capacity-dependent",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
  "output_mode": "content",
  "context": "2",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "gradient diversity|capacity-dependent",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
    "output_mode": "content",
    "context": "2",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-24T09:39:31.394023+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-566-\footnotetext{Experiment 008d terminated at 55K steps; the 105K data point uses continuation run 009e under identical configuration.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-567-
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex:568:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-569-
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-570-[Omitted long context line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-164-
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-165-\paragraph{Critic convergence in pure imagination.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex:166:Across all dual-critic configurations ($n{=}7$), critics trained on shared RSSM features converge ($\rho > 0.999$), with pessimism at 3--4\% of the independent-critic bound (\S\ref{sec:dual_critic_method}). Pessimistic estimation is thus ineffective; the min operation in wide dual-critic may instead regularize through gradient diversity (Appendix~\ref{sec:dual_critic_appendix}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-167-
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-168-\paragraph{$2{\times}2$ factorial: recovery vs.\ prevention.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-24T09:39:43.845012+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex",
  "offset": "28",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex",
    "offset": "28",
    "limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-24T09:39:44.096472+00:00_

28	
29	\subsection{Factorial Design}
30	\label{sec:factorial}
31	
32	We adopt a factorial ablation across four factors: $\dt$-embedding mode (trained / frozen / none), temporal subsampling (on / off), imagination horizon ($H{=}15$ / $H{=}8$), and imagination step size ($\dt{=}1$, $2$, $4$). The design (12 conditions, Table~\ref{tab:factorial_design} in Appendix~\ref{sec:appendix_factorial}) isolates trained $\dt$-embedding and multi-rate data exposure as orthogonal factors. Key configurations use 4 seeds; following \citet{agarwal2021precipice}, we report per-seed trajectories.
33	
34	\subsection{Diagnostic Metrics}
35	\label{sec:metrics}
36	
37	\paragraph{Normalized value-to-eval ratio ($\nve$).}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-24T09:39:44.548600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex",
    "limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-24T09:39:45.251919+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We identify trained $\dt$-embedding with multi-rate data exposure as the strongest predictor of CIVO in DreamerV3 (27/30, AUROC${=}0.957$; LOEO cross-validated). No tested intervention reliably eliminates CIVO; in pure imagination, dual critics converge ($\rho > 0.999$), rendering Double Q pessimism ineffective. The feedback architecture---MPC re-planning versus imagination-based bootstrapping---is the hypothesized structural factor. Empirical validation on MPC-based architectures (e.g., TD-MPC2) remains future work.
5	
6	\paragraph{Limitations.}
7	Our analysis covers proprioceptive locomotion (DMC) and simulated manipulation (ManiSkill) but does not test pixel-based observations, Atari benchmarks, or real-robot deployments where sensor noise and actuation latency introduce additional confounds.
8	All experiments use DreamerV3's RSSM; whether CIVO manifests in other imagination-based architectures (e.g., IRIS \citep{micheli2023iris} or latent-space planners beyond TD-MPC2) remains open.
9	We characterize CIVO under fixed-$\dt$ subsampling; learned temporal gates warrant separate study.
10	Statistical power with 4 seeds per configuration is limited \citep{colas2018seeds}; the NVE threshold (LOEO AUROC${=}0.988$) may require recalibration for different reward scales.
11	Code: upon acceptance.
12	\label{sec:limitations}
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-24T09:39:45.302723+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "offset": "75",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "offset": "75",
    "limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-24T09:39:45.403577+00:00_

75	\centering
76	\includegraphics[width=0.65\columnwidth]{figures/fig1_nve_trajectory.pdf}
77	\caption{NVE trajectories (mean $\pm$ seed range). Trained $\dt$-embedding (red, Walker Walk, $n{=}3$ seeds plotted; seed~4 data in Table~\ref{tab:complete_results}) exceeds the $1.5\times$ threshold (dashed) in all seeds; no-embedding control (blue) remains near $1.0\times$. Three trajectory types emerge: early collapse (seed~0), late-onset collapse (seed~3), and self-correction (seed~2). Dotted line marks the 35K diagnostic window onset.}
78	\label{fig:nve_trajectory}
79	\end{figure}
80	
81	The trained $\dt$-embedding precedes CIVO in all five Walker Walk seeds (peak NVE $1.53$--$4.72\times$), universally degrading performance to below 30\% of baseline (IQM $175.2$, $n{=}5$; \citealt{agarwal2021precipice}). Combined with Cheetah Run (\S\ref{sec:f6}), CIVO onset is universal across all seven tested seeds ($n{=}7$, two environments) with 6/7 suffering sustained policy collapse, 1/7 self-correcting (Appendix~\ref{sec:seed_divergence}).
82	
83	%% ============================================================
84	%% F3--F5: Summary (details in Appendix B)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-24T09:40:35.951952+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-24T09:40:35.952502+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-24T09:45:20.674084+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"统计检验力严重不足：2-3 seeds 无法支撑 causal factor 声明\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 均认同统计效力不足\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。Seeds 增至 4，语言改为 strongest predictor，LOEO AUROC=0.981，IQR 报告。残留小问题：Abstract 中 isolate 一词仍携带因果含义。\"\n    action_items:\n      - round: 1\n        action: \"补 seeds 到 4 per key config\"\n        assigned_to: agent\n        status: done\n      - round: 1\n        action: \"弱化因果语言: causal factor → strongest predictor\"\n        assigned_to: paper_agent\n        status: done\n      - round: 1\n        action: \"统计报告改用 IQM + bootstrap CI per Agarwal et al. 2021\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Seeds 增至 4，因果语言全面弱化为 strongest predictor，LOEO 交叉验证 AUROC=0.981，IQM + bootstrap CI 报告完整。\"\n    resolution_round: 3\n\n  - id: \"R1-N2\"\n    summary: \"NVE 阈值 1.5× 为 post-hoc 选择，88.9% accuracy 是训练准确率，无独立验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 一致认为 post-hoc\"\n    action_items:\n      - round: 1\n        action: \"LOEO cross-validation: mean AUROC 0.981\"\n        assigned_to: agent\n        status: done\n    resolution: \"LOEO 交叉验证完成：3 环境 leave-one-out，mean AUROC 0.981，θ=1.5 在全部 fold 最优范围。论文措辞已改为 in-sample + LOEO cross-validated。\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"CoRL venue fit 严重不足：全文无 robotics 实验/讨论\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"最强共识。用户已确认 CoRL，要求补 robotics 实验\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 判定 STILL_OPEN。ManiSkill negative results 反向证明 CIVO 与 manipulation 无关。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Venue 切换至 ICML 2026。CoRL venue fit 问题不再适用。两位 reviewer 一致认为 ICML 是更合适的 venue。\"\n    action_items:\n      - round: 1\n        action: \"Paper Agent 已添加 robotics framing: Abstract + Intro + Discussion\"\n        assigned_to: paper_agent\n        status: done\n      - round: 1\n        action: \"ManiSkill 实验（PickCube + StackCube + PegInsertion）\"\n        assigned_to: agent\n        status: done\n    resolution: \"Venue 从 CoRL 切换至 ICML 2026。CIVO locomotion-specificity 在 ICML RL track 中不构成 venue fit 问题。\"\n    resolution_round: 4\n\n  - id: \"R1-N4\"\n    summary: \"单环境（Walker Walk）局限使因果声明不可泛化\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 一致。已扩展到 3 环境 + ManiSkill 计划中\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。5 环境覆盖。\"\n    action_items:\n      - round: 1\n        action: \"Cheetah Run + ManiSkill 扩展\"\n        assigned_to: agent\n        status: done\n    resolution: \"从 1 环境扩展到 5 环境（Walker Walk, Cheetah Run, PickCube-v1, StackCube-v1, PegInsertionSide-v1），CIVO 确认为 locomotion-specific，ManiSkill non-CIVO 提供 discriminative validity。\"\n    resolution_round: 3\n\n  - id: \"R3-N1\"\n    summary: \"未使用 CoRL 2026 官方 PMLR 模板，desk reject 风险\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"依赖 venue 决策\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED。main.tex:5 使用 corl_2026。\"\n    action_items:\n      - round: 1\n        action: \"切换到 PMLR 模板\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"已使用 corl_2026 PMLR 模板。注意：Round 4 venue 切换至 ICML 后此模板不再适用，见 N-R4-1。\"\n    resolution_round: 3\n\n  - id: \"R2-N3\"\n    summary: \"纯诊断负面结果缺乏 actionable solution\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 critical, R1 AGREE with nuance, R3 partial REBUT\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 判定 STILL_OPEN。有改善但核心结论仍是 no reliable fix。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"两位 reviewer 保留此 concern 但一致认为在 ICML 语境下严重性降低——ICML RL track 对 systematic negative results 更宽容。R1 Significance Good (borderline)，R2 Fair。\"\n    action_items:\n      - round: 1\n        action: \"Practitioner guidelines + 四级干预层级 + online detector\"\n        assigned_to: paper_agent\n        status: done\n      - round: 1\n        action: \"Frozen embedding / dual-critic mitigation 实验\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"Factorial design 存在混淆变量：secondary comparisons 同时改变多个因素\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R3 REBUT: 008d vs 008f 是干净对照\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。\"\n    action_items:\n      - round: 1\n        action: \"论文显式标注 primary vs secondary comparisons\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Introduction 和 Results 中明确区分 primary comparison (008d vs 008f) 和 secondary comparisons，2×2 grid 完整。\"\n    resolution_round: 3\n\n  - id: \"R1-W2\"\n    summary: \"105K vs 505K 训练步数不对等，treatment 长期命运未知\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"Reviewer 补充: 008a/008e_v3 上升趋势未到头\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 STILL_OPEN。exp_045 长跑数据未在正文呈现。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。Discussion 新增 training horizon 段落：exp_045 s3 在 302K 步后完全 self-recovery（NVE 4.91× → 0.05×, eval 867.6 = 94.7% baseline）。105K 步足以观察 onset，recovery 需 ~170K 额外步数。\"\n    action_items:\n      - round: 3\n        action: \"在 Discussion 或 Appendix 显式讨论 105K vs 505K rationale 和 self-correction 现象\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Discussion 新增 exp_045 self-recovery 数据，充分证明 105K 步足以观察 CIVO onset，recovery 计算成本高。\"\n    resolution_round: 4\n\n  - id: \"R1-W3\"\n    summary: \"Pathway B (non-CIVO collapse) 解释不充分，仅 1 seed 证据\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 partial REBUT (baseline control)\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。\"\n    action_items:\n      - round: 1\n        action: \"弱化声明: preliminary evidence + requires confirmation\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"2 seeds 证据 + 'preliminary evidence, requires confirmation' 措辞，力度与证据匹配。\"\n    resolution_round: 3\n\n  - id: \"R1-W4\"\n    summary: \"RSSM fidelity 仅报告 MAE，未验证 reward overprediction 方向性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 AGREE\"\n    action_items:\n      - round: 1\n        action: \"Signed reward error 分析\"\n        assigned_to: agent\n        status: done\n    resolution: \"Signed error 分析完成。dt=2 是负向偏差(underprediction -0.599)，排除 observation-level overprediction，CIVO 定位为 imagination-level prior drift。\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"与 TAWM 的对比仅基于 architectural reasoning，无实证\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 AGREE\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 STILL_OPEN。Abstract/Conclusion 称 feedback architecture 为 the structural factor。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。Abstract/Conclusion 改为 'a hypothesized structural factor'，Conclusion 显式声明 'Empirical validation on MPC-based architectures remains future work'。\"\n    action_items:\n      - round: 3\n        action: \"弱化 structural factor 措辞为 hypothesized structural factor\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"措辞全文弱化为 'hypothesized structural factor'，未来工作显式声明。\"\n    resolution_round: 4\n\n  - id: \"R2-W3\"\n    summary: \"CIVO 与已知 value overestimation 的区分不够清晰\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R1/R3 partial REBUT\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。\"\n    action_items:\n      - round: 1\n        action: \"Related Work/Discussion 增加显式 CIVO vs compounding error 对比\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Related Work 和 Discussion 提供了充分的经验性区分：untrained embedding 不触发 CIVO，signed error 为负，delusional bias 类比准确。\"\n    resolution_round: 3\n\n  - id: \"R2-W4\"\n    summary: \"Related Work 遗漏 (Becker-Ehmck 2023, Park 2021, Wang 2024, Colas 2018) + bib 冗余\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位均提及\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 判定 PARTIALLY RESOLVED。Becker-Ehmck 2023 仍缺。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 接受混淆解释：Becker-Ehmck 2023 实为 Benechehab et al. 2023 (arXiv:2310.05672)，已引用。降级为 non-issue。\"\n    action_items:\n      - round: 3\n        action: \"引用 Becker-Ehmck et al. 2023 multi-timestep models\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Park 2021、Wang 2024、Colas 2018 已引用。Becker-Ehmck 2023 经调查确认审稿人混淆作者名——实为 Benechehab et al. 2023，已引用。Bib 清理至 44 条无 orphan。\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"Limitations 作为 paragraph 嵌入 Conclusion 而非独立 Section\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"R1 REBUT (paragraph 可接受)\"\n    action_items: []\n    resolution: \"Limitations 作为 Conclusion paragraph，形式可接受。\"\n    resolution_round: 1\n\n  - id: \"R3-W2\"\n    summary: \"Abstract 过长且缺乏 robotics motivation\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"R1 partial AGREE\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 判定 RESOLVED。约 150 词，robotics motivation 到位。\"\n    action_items:\n      - round: 1\n        action: \"缩短 Abstract + 加 robotics motivation\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Abstract 约 150 词，首句含 robotics motivation，88.9% 替换为 26/29 AUROC=0.953。\"\n    resolution_round: 3\n\n  - id: \"R3-W3\"\n    summary: \"Bibliography 严重冗余：77 条中仅 29 条被引用\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"splates2025 author 为占位符\"\n      - round: 3\n        reviewers: [2]\n        note: \"Bib 从 77 条清理至 44 条，全部被引用。\"\n    action_items:\n      - round: 1\n        action: \"清理 bib (77→44 条)\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Bib 清理至 44 条，全部被引用，无 orphan。\"\n    resolution_round: 3\n\n  - id: \"R3-W5\"\n    summary: \"fig4_mechanism_diagram.pdf 存在但未被论文引用\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"CIVO 机制图应引入正文\"\n    action_items: []\n    resolution: \"fig4_mechanism_diagram 已在 Appendix 引用。\"\n    resolution_round: 1\n\n  - id: \"R3-N3\"\n    summary: \"换模板后正文可能超 8 页\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"需实际测试\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED。正文 8 页。\"\n    action_items: []\n    resolution: \"正文 8 页，编译通过。注意：ICML 模板切换后需重新确认页数。\"\n    resolution_round: 3\n\n  - id: \"REV-1\"\n    summary: \"008f causal control 跨 seed 不稳定\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [\"research_reviewer\"]\n        note: \"exp_043 s1 完成：5/5 seeds 全部 NVE<1.5，008f 因果控制 robust\"\n    action_items: []\n    resolution: \"exp_043 确认 008f 5/5 seeds 全部 NVE<1.5，因果控制 robust。\"\n    resolution_round: 1\n\n  - id: \"REV-2\"\n    summary: \"105K vs 500K 比较不对等: 治疗组上升趋势未到头\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [\"research_reviewer\"]\n        note: \"exp_045 treatment extension 008d s3 延长到 300K 中\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"与 R1-W2 合并。两位 reviewer 一致判定 STILL_OPEN。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"随 R1-W2 一同 RESOLVED。exp_045 数据已在 Discussion 呈现。\"\n    action_items:\n      - round: 3\n        action: \"合并入 R1-W2 处理\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"随 R1-W2 一同解决。exp_045 self-recovery 数据已在 Discussion 呈现。\"\n    resolution_round: 4\n\n  - id: \"R3-N-new-1\"\n    summary: \"Online CIVO Detector 评估样本量不足 (n=14, 仅 5 正例)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致。TPR=5/5 的 95% CI 下界仅 47.8%。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。Detector 降级为 preliminary diagnostic，Clopper-Pearson CI [47.8%, 100%] 已披露，Contribution 列表相应调整。\"\n    action_items:\n      - round: 3\n        action: \"承认 detector 的 small-sample limitation，或降级为 preliminary tool\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Detector 降级为 preliminary diagnostic，CI 披露，contribution 列表调整。\"\n    resolution_round: 4\n\n  - id: \"R3-N-new-2\"\n    summary: \"Dual-critic convergence 主文叙事过于简化\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致。ρ>0.999 是 asymptotic 结果，与 wide dual-critic 3/4 prevention 存在张力。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 PARTIALLY RESOLVED。results.tex:166 使用 'gradient diversity' 术语但 Appendix G 无量化支撑。R1 建议改为 'capacity-dependent mechanism'，R2 同意。introduction.tex:13 的 'different mechanism' 措辞更合适。\"\n    action_items:\n      - round: 3\n        action: \"在 Section 4.8 或 Discussion 增加 1-2 句解释 min operation 在 converged critics 下的机制\"\n        assigned_to: paper_agent\n        status: done\n      - round: 4\n        action: \"将 results.tex:166 'gradient diversity' 替换为 'capacity-dependent mechanism during early training' 或 'the mechanism is an open question'\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N-new-3\"\n    summary: \"ManiSkill 和 Cheetah Run baseline eval 值在 Table 1 中缺失\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [2]\n        note: \"Table 1 中 ManiSkill 和 Cheetah Run 缺少 vanilla DreamerV3 baseline eval 值。\"\n      - round: 4\n        reviewers: [2]\n        note: \"未修复。仍缺少 baseline 参照值。\"\n    action_items:\n      - round: 3\n        action: \"在 Table 1 或脚注中补充各环境 baseline eval 值\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"N-R4-1\"\n    summary: \"模板仍为 corl_2026，未切换至 ICML 2026 (icml2026.sty)\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致。main.tex:5 仍使用 \\\\usepackage{corl_2026}，PDF 页脚显示 CoRL。Desk reject 风险极高。\"\n    action_items:\n      - round: 4\n        action: \"切换 main.tex 为 icml2026.sty 模板，处理 \\\\keywords{} 等 CoRL 特有命令\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"N-R4-2\"\n    summary: \"缺少 ICML 2026 要求的 Impact Statement\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"R2 发现，R1 承认审查遗漏。ICML 2026 要求 Impact Statement 在 References 前。当前论文完全没有此 section。Desk reject 风险。\"\n    action_items:\n      - round: 4\n        action: \"在 References 前添加 Impact Statement section\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"N-R4-3\"\n    summary: \"IQM 计算错误：n=5 seeds 报告了 n=4 的 IQM 值 175.2（正确值 148.8）\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"R2 发现并验证。Walker 5 seeds eval: {63.6, 82.8, 95.8, 267.9, 268.0}。n=4 IQM=175.35≈175.2（去掉首尾各1）。n=5 IQM=148.83（去掉首尾各1，middle 3 mean）。results.tex:81 报告 IQM 175.2, n=5 是数据完整性错误——添加 seed 5 后未重新计算。错误性质 careless 非 systematic，不影响核心结论。\"\n    action_items:\n      - round: 4\n        action: \"重新计算 n=5 IQM 并更新 results.tex:81\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"N-R4-4\"\n    summary: \"Seed 数量叙述全文不一致（methodology 说 4，results 说 5，Figure 2 caption 漏 seed 5）\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 系统验证并发现更严重。methodology.tex:32 '4 seeds'，results.tex:81 'n=5'，conclusion.tex:10 '4 seeds'，Figure 2 caption 'seed 4 data in Table' 未提 seed 5。\"\n    action_items:\n      - round: 4\n        action: \"统一全文 seed 数量叙述（methodology.tex:32, conclusion.tex:10, Figure 2 caption）\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"N-R4-5\"\n    summary: \"'causal chain' 措辞暗示因果推断，factorial ablation 仅提供 predictive 证据\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"R2 建议将 results.tex:4 'establish a causal chain' 改为 'trace a pathway' 或 'establish a predictive chain'。Minor 修改。R1 标记 'isolate' 为 minor，R2 REBUT 认为 factorial ablation 中 'isolate' 是标准用语。\"\n    action_items:\n      - round: 4\n        action: \"考虑将 'causal chain' 改为 'predictive chain' 或 'trace a pathway'\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"统计检验力严重不足：2-3 seeds 无法支撑 causal factor 声明\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 均认同统计效力不足\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。Seeds 增至 4，语言改为 strongest predictor，LOEO AUROC=0.981，IQR 报告。残留小问题：Abstract 中 isolate 一词仍携带因果含义。\"\n    action_items:\n      - round: 1\n        action: \"补 seeds 到 4 per key config\"\n        assigned_to: agent\n        status: done\n      - round: 1\n        action: \"弱化因果语言: causal factor → strongest predictor\"\n        assigned_to: paper_agent\n        status: done\n      - round: 1\n        action: \"统计报告改用 IQM + bootstrap CI per Agarwal et al. 2021\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Seeds 增至 4，因果语言全面弱化为 strongest predictor，LOEO 交叉验证 AUROC=0.981，IQM + bootstrap CI 报告完整。\"\n    resolution_round: 3\n\n  - id: \"R1-N2\"\n    summary: \"NVE 阈值 1.5× 为 post-hoc 选择，88.9% accuracy 是训练准确率，无独立验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 一致认为 post-hoc\"\n    action_items:\n      - round: 1\n        action: \"LOEO cross-validation: mean AUROC 0.981\"\n        assigned_to: agent\n        status: done\n    resolution: \"LOEO 交叉验证完成：3 环境 leave-one-out，mean AUROC 0.981，θ=1.5 在全部 fold 最优范围。论文措辞已改为 in-sample + LOEO cross-validated。\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"CoRL venue fit 严重不足：全文无 robotics 实验/讨论\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"最强共识。用户已确认 CoRL，要求补 robotics 实验\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 判定 STILL_OPEN。ManiSkill negative results 反向证明 CIVO 与 manipulation 无关。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Venue 切换至 ICML 2026。CoRL venue fit 问题不再适用。两位 reviewer 一致认为 ICML 是更合适的 venue。\"\n    action_items:\n      - round: 1\n        action: \"Paper Agent 已添加 robotics framing: Abstract + Intro + Discussion\"\n        assigned_to: paper_agent\n        status: done\n      - round: 1\n        action: \"ManiSkill 实验（PickCube + StackCube + PegInsertion）\"\n        assigned_to: agent\n        status: done\n    resolution: \"Venue 从 CoRL 切换至 ICML 2026。CIVO locomotion-specificity 在 ICML RL track 中不构成 venue fit 问题。\"\n    resolution_round: 4\n\n  - id: \"R1-N4\"\n    summary: \"单环境（Walker Walk）局限使因果声明不可泛化\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 reviewer 一致。已扩展到 3 环境 + ManiSkill 计划中\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。5 环境覆盖。\"\n    action_items:\n      - round: 1\n        action: \"Cheetah Run + ManiSkill 扩展\"\n        assigned_to: agent\n        status: done\n    resolution: \"从 1 环境扩展到 5 环境（Walker Walk, Cheetah Run, PickCube-v1, StackCube-v1, PegInsertionSide-v1），CIVO 确认为 locomotion-specific，ManiSkill non-CIVO 提供 discriminative validity。\"\n    resolution_round: 3\n\n  - id: \"R3-N1\"\n    summary: \"未使用 CoRL 2026 官方 PMLR 模板，desk reject 风险\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"依赖 venue 决策\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED。main.tex:5 使用 corl_2026。\"\n    action_items:\n      - round: 1\n        action: \"切换到 PMLR 模板\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"已使用 corl_2026 PMLR 模板。注意：Round 4 venue 切换至 ICML 后此模板不再适用，见 N-R4-1。\"\n    resolution_round: 3\n\n  - id: \"R2-N3\"\n    summary: \"纯诊断负面结果缺乏 actionable solution\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 critical, R1 AGREE with nuance, R3 partial REBUT\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 判定 STILL_OPEN。有改善但核心结论仍是 no reliable fix。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"两位 reviewer 保留此 concern 但一致认为在 ICML 语境下严重性降低——ICML RL track 对 systematic negative results 更宽容。R1 Significance Good (borderline)，R2 Fair。\"\n    action_items:\n      - round: 1\n        action: \"Practitioner guidelines + 四级干预层级 + online detector\"\n        assigned_to: paper_agent\n        status: done\n      - round: 1\n        action: \"Frozen embedding / dual-critic mitigation 实验\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"Factorial design 存在混淆变量：secondary comparisons 同时改变多个因素\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R3 REBUT: 008d vs 008f 是干净对照\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。\"\n    action_items:\n      - round: 1\n        action: \"论文显式标注 primary vs secondary comparisons\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Introduction 和 Results 中明确区分 primary comparison (008d vs 008f) 和 secondary comparisons，2×2 grid 完整。\"\n    resolution_round: 3\n\n  - id: \"R1-W2\"\n    summary: \"105K vs 505K 训练步数不对等，treatment 长期命运未知\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"Reviewer 补充: 008a/008e_v3 上升趋势未到头\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 STILL_OPEN。exp_045 长跑数据未在正文呈现。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。Discussion 新增 training horizon 段落：exp_045 s3 在 302K 步后完全 self-recovery（NVE 4.91× → 0.05×, eval 867.6 = 94.7% baseline）。105K 步足以观察 onset，recovery 需 ~170K 额外步数。\"\n    action_items:\n      - round: 3\n        action: \"在 Discussion 或 Appendix 显式讨论 105K vs 505K rationale 和 self-correction 现象\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Discussion 新增 exp_045 self-recovery 数据，充分证明 105K 步足以观察 CIVO onset，recovery 计算成本高。\"\n    resolution_round: 4\n\n  - id: \"R1-W3\"\n    summary: \"Pathway B (non-CIVO collapse) 解释不充分，仅 1 seed 证据\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 partial REBUT (baseline control)\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。\"\n    action_items:\n      - round: 1\n        action: \"弱化声明: preliminary evidence + requires confirmation\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"2 seeds 证据 + 'preliminary evidence, requires confirmation' 措辞，力度与证据匹配。\"\n    resolution_round: 3\n\n  - id: \"R1-W4\"\n    summary: \"RSSM fidelity 仅报告 MAE，未验证 reward overprediction 方向性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 AGREE\"\n    action_items:\n      - round: 1\n        action: \"Signed reward error 分析\"\n        assigned_to: agent\n        status: done\n    resolution: \"Signed error 分析完成。dt=2 是负向偏差(underprediction -0.599)，排除 observation-level overprediction，CIVO 定位为 imagination-level prior drift。\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"与 TAWM 的对比仅基于 architectural reasoning，无实证\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 AGREE\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 STILL_OPEN。Abstract/Conclusion 称 feedback architecture 为 the structural factor。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。Abstract/Conclusion 改为 'a hypothesized structural factor'，Conclusion 显式声明 'Empirical validation on MPC-based architectures remains future work'。\"\n    action_items:\n      - round: 3\n        action: \"弱化 structural factor 措辞为 hypothesized structural factor\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"措辞全文弱化为 'hypothesized structural factor'，未来工作显式声明。\"\n    resolution_round: 4\n\n  - id: \"R2-W3\"\n    summary: \"CIVO 与已知 value overestimation 的区分不够清晰\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R1/R3 partial REBUT\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。\"\n    action_items:\n      - round: 1\n        action: \"Related Work/Discussion 增加显式 CIVO vs compounding error 对比\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Related Work 和 Discussion 提供了充分的经验性区分：untrained embedding 不触发 CIVO，signed error 为负，delusional bias 类比准确。\"\n    resolution_round: 3\n\n  - id: \"R2-W4\"\n    summary: \"Related Work 遗漏 (Becker-Ehmck 2023, Park 2021, Wang 2024, Colas 2018) + bib 冗余\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位均提及\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 判定 PARTIALLY RESOLVED。Becker-Ehmck 2023 仍缺。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 接受混淆解释：Becker-Ehmck 2023 实为 Benechehab et al. 2023 (arXiv:2310.05672)，已引用。降级为 non-issue。\"\n    action_items:\n      - round: 3\n        action: \"引用 Becker-Ehmck et al. 2023 multi-timestep models\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Park 2021、Wang 2024、Colas 2018 已引用。Becker-Ehmck 2023 经调查确认审稿人混淆作者名——实为 Benechehab et al. 2023，已引用。Bib 清理至 44 条无 orphan。\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"Limitations 作为 paragraph 嵌入 Conclusion 而非独立 Section\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"R1 REBUT (paragraph 可接受)\"\n    action_items: []\n    resolution: \"Limitations 作为 Conclusion paragraph，形式可接受。\"\n    resolution_round: 1\n\n  - id: \"R3-W2\"\n    summary: \"Abstract 过长且缺乏 robotics motivation\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"R1 partial AGREE\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 判定 RESOLVED。约 150 词，robotics motivation 到位。\"\n    action_items:\n      - round: 1\n        action: \"缩短 Abstract + 加 robotics motivation\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Abstract 约 150 词，首句含 robotics motivation，88.9% 替换为 26/29 AUROC=0.953。\"\n    resolution_round: 3\n\n  - id: \"R3-W3\"\n    summary: \"Bibliography 严重冗余：77 条中仅 29 条被引用\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"splates2025 author 为占位符\"\n      - round: 3\n        reviewers: [2]\n        note: \"Bib 从 77 条清理至 44 条，全部被引用。\"\n    action_items:\n      - round: 1\n        action: \"清理 bib (77→44 条)\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Bib 清理至 44 条，全部被引用，无 orphan。\"\n    resolution_round: 3\n\n  - id: \"R3-W5\"\n    summary: \"fig4_mechanism_diagram.pdf 存在但未被论文引用\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"CIVO 机制图应引入正文\"\n    action_items: []\n    resolution: \"fig4_mechanism_diagram 已在 Appendix 引用。\"\n    resolution_round: 1\n\n  - id: \"R3-N3\"\n    summary: \"换模板后正文可能超 8 页\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"需实际测试\"\n      - round: 3\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED。正文 8 页。\"\n    action_items: []\n    resolution: \"正文 8 页，编译通过。注意：ICML 模板切换后需重新确认页数。\"\n    resolution_round: 3\n\n  - id: \"REV-1\"\n    summary: \"008f causal control 跨 seed 不稳定\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [\"research_reviewer\"]\n        note: \"exp_043 s1 完成：5/5 seeds 全部 NVE<1.5，008f 因果控制 robust\"\n    action_items: []\n    resolution: \"exp_043 确认 008f 5/5 seeds 全部 NVE<1.5，因果控制 robust。\"\n    resolution_round: 1\n\n  - id: \"REV-2\"\n    summary: \"105K vs 500K 比较不对等: 治疗组上升趋势未到头\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [\"research_reviewer\"]\n        note: \"exp_045 treatment extension 008d s3 延长到 300K 中\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"与 R1-W2 合并。两位 reviewer 一致判定 STILL_OPEN。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"随 R1-W2 一同 RESOLVED。exp_045 数据已在 Discussion 呈现。\"\n    action_items:\n      - round: 3\n        action: \"合并入 R1-W2 处理\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"随 R1-W2 一同解决。exp_045 self-recovery 数据已在 Discussion 呈现。\"\n    resolution_round: 4\n\n  - id: \"R3-N-new-1\"\n    summary: \"Online CIVO Detector 评估样本量不足 (n=14, 仅 5 正例)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致。TPR=5/5 的 95% CI 下界仅 47.8%。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 RESOLVED。Detector 降级为 preliminary diagnostic，Clopper-Pearson CI [47.8%, 100%] 已披露，Contribution 列表相应调整。\"\n    action_items:\n      - round: 3\n        action: \"承认 detector 的 small-sample limitation，或降级为 preliminary tool\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Detector 降级为 preliminary diagnostic，CI 披露，contribution 列表调整。\"\n    resolution_round: 4\n\n  - id: \"R3-N-new-2\"\n    summary: \"Dual-critic convergence 主文叙事过于简化\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致。ρ>0.999 是 asymptotic 结果，与 wide dual-critic 3/4 prevention 存在张力。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致判定 PARTIALLY RESOLVED。results.tex:166 使用 'gradient diversity' 术语但 Appendix G 无量化支撑。R1 建议改为 'capacity-dependent mechanism'，R2 同意。introduction.tex:13 的 'different mechanism' 措辞更合适。\"\n    action_items:\n      - round: 3\n        action: \"在 Section 4.8 或 Discussion 增加 1-2 句解释 min operation 在 converged critics 下的机制\"\n        assigned_to: paper_agent\n        status: done\n      - round: 4\n        action: \"将 results.tex:166 'gradient diversity' 替换为 'capacity-dependent mechanism during early training' 或 'the mechanism is an open question'\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N-new-3\"\n    summary: \"ManiSkill 和 Cheetah Run baseline eval 值在 Table 1 中缺失\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [2]\n        note: \"Table 1 中 ManiSkill 和 Cheetah Run 缺少 vanilla DreamerV3 baseline eval 值。\"\n      - round: 4\n        reviewers: [2]\n        note: \"未修复。仍缺少 baseline 参照值。\"\n    action_items:\n      - round: 3\n        action: \"在 Table 1 或脚注中补充各环境 baseline eval 值\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"N-R4-1\"\n    summary: \"模板仍为 corl_2026，未切换至 ICML 2026 (icml2026.sty)\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"两位 reviewer 一致。main.tex:5 仍使用 \\\\usepackage{corl_2026}，PDF 页脚显示 CoRL。Desk reject 风险极高。\"\n    action_items:\n      - round: 4\n        action: \"切换 main.tex 为 icml2026.sty 模板，处理 \\\\keywords{} 等 CoRL 特有命令\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"N-R4-2\"\n    summary: \"缺少 ICML 2026 要求的 Impact Statement\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"R2 发现，R1 承认审查遗漏。ICML 2026 要求 Impact Statement 在 References 前。当前论文完全没有此 section。Desk reject 风险。\"\n    action_items:\n      - round: 4\n        action: \"在 References 前添加 Impact Statement section\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"N-R4-3\"\n    summary: \"IQM 计算错误：n=5 seeds 报告了 n=4 的 IQM 值 175.2（正确值 148.8）\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"R2 发现并验证。Walker 5 seeds eval: {63.6, 82.8, 95.8, 267.9, 268.0}。n=4 IQM=175.35≈175.2（去掉首尾各1）。n=5 IQM=148.83（去掉首尾各1，middle 3 mean）。results.tex:81 报告 IQM 175.2, n=5 是数据完整性错误——添加 seed 5 后未重新计算。错误性质 careless 非 systematic，不影响核心结论。\"\n    action_items:\n      - round: 4\n        action: \"重新计算 n=5 IQM 并更新 results.tex:81\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"N-R4-4\"\n    summary: \"Seed 数量叙述全文不一致（methodology 说 4，results 说 5，Figure 2 caption 漏 seed 5）\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 系统验证并发现更严重。methodology.tex:32 '4 seeds'，results.tex:81 'n=5'，conclusion.tex:10 '4 seeds'，Figure 2 caption 'seed 4 data in Table' 未提 seed 5。\"\n    action_items:\n      - round: 4\n        action: \"统一全文 seed 数量叙述（methodology.tex:32, conclusion.tex:10, Figure 2 caption）\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"N-R4-5\"\n    summary: \"'causal chain' 措辞暗示因果推断，factorial ablation 仅提供 predictive 证据\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"R2 建议将 results.tex:4 'establish a causal chain' 改为 'trace a pathway' 或 'establish a predictive chain'。Minor 修改。R1 标记 'isolate' 为 minor，R2 REBUT 认为 factorial ablation 中 'isolate' 是标准用语。\"\n    action_items:\n      - round: 4\n        action: \"考虑将 'causal chain' 改为 'predictive chain' 或 'trace a pathway'\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 361 · 2026-05-24T09:45:20.876535+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml\", \"bytes\": 19258}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-24T09:47:33.409803+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 4\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**目标 Venue**: ICML 2026（Round 4 从 CoRL 切换）\n**审稿日期**: 2026-05-24\n**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验充分性 | R2: Novelty + 贡献度 + 写作质量）\n**轮次**: Round 4 继续审稿（修订评估）+ 交叉分享（1 轮收敛）\n**上轮评分**: Round 3 Weak Reject (5/10, CoRL)\n\n---\n\n## Summary\n\n论文从 Round 3 (Weak Reject 5/10, CoRL) 转投 ICML 2026 并进行了多项修订：(1) TAWM/MPC 对比措辞弱化为 \"hypothesized structural factor\"；(2) Discussion 新增 exp_045 self-recovery 数据（302K 步后 NVE 4.91× → 0.05×, eval 94.7% baseline），解决了步数不对等问题；(3) Online CIVO Detector 降级为 \"preliminary diagnostic\" 并披露 Clopper-Pearson CI；(4) Walker Walk 扩展至 5 seeds。\n\n然而，模板仍为 corl_2026（未切换 icml2026.sty），缺少 ICML 要求的 Impact Statement，且存在 IQM 计算错误（n=5 seeds 报告了 n=4 的 IQM 值 175.2，正确值应为 148.8）和 seed 数量叙述不一致（methodology/conclusion 说 4 seeds，results 说 n=5）。\n\n---\n\n## Strengths\n\n1. **Factorial design 系统严谨**（2/2 共识，持续优势）：43 配置 × 4-5 seeds × 5 环境，primary/secondary comparison 清晰标注\n2. **LOEO 交叉验证统计可信度高**：AUROC=0.981 (LOEO, 3 folds)\n3. **四级干预层级分析**：gradient/output/representation/architecture 提供系统性 negative result。Gradient magnitude ≠ causal importance 的发现有洞见\n4. **ManiSkill discriminative validity**：NVE 诊断正确区分 CIVO 与 transient\n5. **Dual-critic convergence insight**：ρ > 0.999 揭示 imagination-based 训练中 Double Q pessimism 的结构性失效\n6. **exp_045 self-recovery 数据**（Round 4 新增）：302K 步后完全恢复（eval 94.7% baseline），充分证明 105K 步足以观察 onset 且 recovery 计算成本高\n7. **Venue 切换至 ICML**：消除了 Round 3 的核心矛盾（CIVO locomotion-specificity vs CoRL manipulation focus）\n8. **措辞诚实度提升**：\"hypothesized structural factor\"、\"preliminary diagnostic\"、Limitations 诚实全面\n\n---\n\n## Weaknesses（按严重性排序）\n\n### Critical（影响接收决定）\n\n**W-C1. 模板仍为 corl_2026，未切换至 icml2026.sty [2/2 共识，Round 4 新发现]**\nmain.tex:5 仍使用 `\\usepackage{corl_2026}`，PDF 页脚显示 \"Submitted to the 10th Conference on Robot Learning (CoRL, 2026)\"。ICML 2026 要求使用 icml2026.sty 模板。**Desk reject 风险极高。**\n\n**W-C2. 缺少 Impact Statement [R2 发现，R1 承认审查遗漏]**\nICML 2026 要求论文在 References 前包含 Impact Statement section。当前论文完全没有此 section。**Desk reject 风险。**\n\n**W-C3. IQM 计算错误——数据完整性问题 [R2 发现并独立验证]**\nresults.tex:81 报告 \"IQM $175.2$, $n{=}5$\"，但经验证：\n- Walker 5 seeds eval: {63.6, 82.8, 95.8, 267.9, 268.0}\n- n=4 IQM（trim 1 each side）: mean(82.8, 267.9) = **175.35 ≈ 175.2** ✓\n- n=5 IQM（trim 1 each side）: mean(82.8, 95.8, 267.9) = **148.8** ≠ 175.2\n\nIQM 175.2 是 n=4 的正确值；添加第 5 个 seed（eval 95.8）后未重新计算。对于一篇以统计严谨性为卖点、引用 Agarwal et al. (2021) 的 diagnostic paper，此错误损害可信度。**错误性质为 careless 而非 systematic，不影响核心结论（CIVO 在所有 5 seeds 中出现），但必须修复。**\n\n### Warning（影响评分但不一票否决）\n\n**W-W1. Seed 数量叙述全文不一致 [R1 提出，R2 系统验证]**\n| 位置 | 文本 | 问题 |\n|------|------|------|\n| methodology.tex:32 | \"Key configurations use **4** seeds\" | 实际 Walker 是 5 seeds |\n| results.tex:81 | \"all **five** Walker Walk seeds...n=5\" | 正确 |\n| conclusion.tex:10 | \"Statistical power with **4** seeds\" | 与 n=5 不一致 |\n| Figure 2 caption | \"n=3 seeds plotted; seed 4 data in Table\" | 未提及 seed 5 |\n\n**W-W2. \"gradient diversity\" 术语无支撑证据 [2/2 共识，PARTIALLY RESOLVED]**\nresults.tex:166: \"the min operation in wide dual-critic may instead regularize through gradient diversity (Appendix G)\"。Appendix G 未提供 gradient diversity 的量化证据。建议改为 \"may instead function through a capacity-dependent mechanism during early training\" 或 \"the mechanism is an open question\"。introduction.tex:13 的 \"different mechanism\" 措辞更恰当。\n\n**W-W3. 贡献模式——scope 和 significance 有限 [延续 Round 3，2/2 共识]**\n- 核心结论仍是 negative（no reliable intervention eliminates CIVO）\n- 最有效 \"solution\" 是不使用该功能（embedding removed = 100% prevention）\n- CIVO 仅在 locomotion 中复现\n- 在 ICML 语境下，systematic negative result 的贡献度评价比 CoRL 更宽容，严重性降级\n\n**W-W4. ManiSkill 和 Cheetah Run baseline eval 值缺失 [延续 Round 3，未修复]**\nTable 1 中这些环境缺少 vanilla DreamerV3 baseline eval 值，读者无法判断相对性能。\n\n### Minor\n\n**W-M1. \"causal chain\" 措辞 [R2 建议]**\nresults.tex:4 中 \"establish a causal chain\" 暗示因果推断，factorial ablation 提供 predictive/associative 证据。建议改为 \"trace a pathway\" 或 \"establish a predictive chain\"。\n\n**W-M2. Abstract \"isolate\" 残留 [R1 minor，R2 REBUT 降级]**\nR2 认为 \"isolate\" 在 factorial ablation 语境中是标准用语，不构成 overclaim。Director 同意——minor at most。\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 共识度 |\n|------|----|----|--------|\n| 模板 corl_2026 (NEW) | CRITICAL | CRITICAL (AGREE) | **2/2 一致** |\n| Impact Statement 缺失 (NEW) | 承认遗漏 | CRITICAL | R2 独立发现 |\n| IQM 计算错误 (NEW) | — | CRITICAL (验证) | R2 独立发现 |\n| Seed 数量不一致 (NEW) | 提出 | AGREE (更严重) | **2/2 一致** |\n| R1-W2 步数不对等 | RESOLVED | AGREE RESOLVED | **2/2 一致** |\n| R2-W1 TAWM 对比 | RESOLVED | AGREE RESOLVED | **2/2 一致** |\n| R3-N-new-1 Detector 样本量 | RESOLVED | AGREE RESOLVED | **2/2 一致** |\n| R3-N-new-2 Dual-critic | PARTIALLY | AGREE PARTIALLY | **2/2 一致** |\n| R2-W4 Becker-Ehmck | 仍未引用 | 接受混淆解释 | **R2 覆盖，non-issue** |\n| Significance | Good (borderline) | Fair | **分歧（minor）** |\n\n---\n\n## Reviewer Divergence\n\n**1. Significance（R1: Good borderline vs R2: Fair）**\n- R1：dual-critic convergence insight 和 systematic negative result 在 ICML 社区有价值\n- R2：negative result + no reliable fix 的贡献模式 significance 有限\n- **Director 判断**：R1 borderline Good 合理但偏乐观。ICML RL track 接受 systematic negative results，但论文的 actionable output 确实有限。综合约 Fair+ (2.5/4)。\n\n**2. \"isolate\" 严重性（R1: minor vs R2: non-issue）**\n- R1：与 \"strongest predictor\" 不一致\n- R2：factorial ablation 中 \"isolate\" 是标准用语\n- **Director 判断**：同意 R2。Minor at most。\n\n---\n\n## Questions for Authors\n\n1. IQM 175.2 是 n=4 的值——请重新计算 n=5 的 IQM（经计算应为 ~148.8）并更新 results.tex:81。\n2. methodology.tex:32 说 \"4 seeds\"，results.tex:81 说 \"n=5\"——Walker Walk 的实际 seed 数是多少？请统一全文叙述（methodology.tex:32, conclusion.tex:10, Figure 2 caption）。\n3. 是否计划切换到 icml2026.sty 并添加 Impact Statement？这两项是 desk reject 风险。\n4. results.tex:166 中 \"gradient diversity\" 在 Appendix G 中是否有量化支撑？如果没有，是否考虑弱化措辞？\n5. Wide dual-critic 在 Walker 3/4 prevention 但 Cheetah 0/1——是否有对 environment-dependence 的解释？\n\n---\n\n## Missing References\n\nRound 3 遗留的 Becker-Ehmck 2023 问题已解决：R2 确认混淆解释合理（实为 Benechehab et al. 2023，已引用于 related_work.tex）。无新增缺失引用。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（1 critical, 4 warnings, 12 info）。\n\n**主要发现**：\n1. **[critical] 前 4 页无 display item**：连续 4 页纯文本，第一个视觉锚点（Table 1）直到第 5 页。建议将 Figure 6（CIVO 机制图，当前 Appendix page 17）提前到 Section 1/3。\n2. **[warning] 正文 display item 密度偏低**：8 页正文仅 4 个 display items（Table 1-2, Figure 1-2），实证型论文通常期望 6+。\n3. **[warning] Section 3 跨 2 页纯文本**：复杂实验设计无图示辅助。\n4. **[warning] Discussion + Conclusion 挤在同一页全纯文本**。\n5. **[warning] 最后一页 Table 22 仅占 35-40%**，大面积空白。\n6. **[info] 图表质量良好**：Figure 1/2 清晰，Table 1/2 booktabs 规范，ROC 曲线标注清晰。\n7. **[info] Figure 6（CIVO mechanism diagram）是全文最有解释力的图**，强烈建议简化版移入正文。\n\n---\n\n## Overall Assessment\n\n**评分: Weak Accept (6/10)**\n**置信度: High (4/5)**\n\n**与 Round 3 (Weak Reject, 5/10, CoRL) 的变化**：\n\n| 维度 | Round 3 | Round 4 | 变化 |\n|------|---------|---------|------|\n| Venue fit | STILL_OPEN (CoRL mismatch) | **RESOLVED** (→ ICML) | ▲▲▲ |\n| 步数不对等 | STILL_OPEN | RESOLVED (exp_045 data) | ▲▲ |\n| TAWM 对比 | STILL_OPEN | RESOLVED (hypothesized) | ▲▲ |\n| Detector 样本量 | OPEN | RESOLVED (preliminary) | ▲ |\n| Becker-Ehmck 引用 | PARTIALLY | RESOLVED (混淆解释) | ▲ |\n| 模板合规 | RESOLVED (CoRL PMLR) | **NEW CRITICAL** (仍是 CoRL) | ▼▼ |\n| Impact Statement | — | **NEW CRITICAL** (ICML 要求) | ▼▼ |\n| IQM 数据完整性 | — | **NEW CRITICAL** (n=5 报 n=4 值) | ▼ |\n| Seed 叙述一致性 | — | **NEW WARNING** | ▼ |\n\n**核心判断**：\n\nVenue 切换是 Round 4 最重要的变化。Round 3 的两个核心障碍（CoRL venue fit + deployment-oriented 社区的贡献期望）在 ICML 语境下大幅缓解——ICML RL track 接受 systematic diagnostic/negative results，factorial design + LOEO 验证的方法论水平匹配 ICML 标准。Round 3 报告本身也预测了\"如果提交到 ICML：Borderline Accept (6/10)\"。\n\n新发现的格式问题（模板、Impact Statement）是 desk reject 风险但容易修复；IQM 错误虽不影响核心结论但损害可信度。\n\n**如果格式问题和 IQM 修复后**：评分可上调至 Borderline Accept (6.5/10)。\n\n**综合维度评分**（Director 综合两位 Reviewer）：\n\n| 维度 | 评分 | 理由 |\n|------|------|------|\n| Originality | 3.5/5 | CIVO 现象新颖，gradient ≠ causal importance 有洞见，方法论框架标准 |\n| Soundness | 3/5 | Factorial design 严谨，LOEO 有力，但 IQM 错误 + gradient diversity 无支撑损害可信度 |\n| Clarity | 3/5 | 结构清晰，但模板错误 + 缺 Impact Statement + seed 叙述不一致 |\n| Significance | 2.5/5 | 四级干预有系统贡献，ICML 对 negative results 更宽容，但 actionable output 有限 |\n| Relevance (ICML) | 4/5 | World-model RL + temporal abstraction 是 ICML RL track 核心话题 |\n| Limitations | 4/5 | 诚实全面 |\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 约 150 词，长度合理\n- \"isolate\" 在 factorial ablation 语境中可接受（R2 判断）\n- 统计数据密度仍偏高（6+ 数字指标），建议精简\n\n### Introduction\n- Robotics framing 保留（从 CoRL 延续），在 ICML 中不加分也不减分\n- Contribution 列表 4 项清晰，detector 已降级为 \"preliminary\"\n\n### Experimental Setup (Section 3)\n- methodology.tex:32 \"Key configurations use 4 seeds\" 与实际 n=5 不一致——**必须修复**\n- Factorial design 展示专业，四因素清晰\n\n### Results (Section 4)\n- **IQM 175.2 是 n=4 值，n=5 应为 148.8——必须修复**\n- Figure 2 caption 提到 \"seed 4\" 但未提及 seed 5\n- \"gradient diversity\" (results.tex:166) 无 Appendix 支撑——建议弱化\n- exp_045 self-recovery 数据有效回应了步数不对等问题\n- \"establish a causal chain\" (results.tex:4) 建议改为 \"trace a pathway\"\n\n### Discussion (Section 5)\n- \"hypothesized structural factor\" 措辞准确\n- exp_045 training horizon 讨论充分\n\n### Conclusion (Section 6)\n- conclusion.tex:10 \"4 seeds\" 与 n=5 不一致——**必须修复**\n- Limitations paragraph 诚实全面\n\n### Format Issues（Desk Reject 风险）\n- **模板**: main.tex:5 仍为 `\\usepackage{corl_2026}` → 需切换 icml2026.sty\n- **Impact Statement**: 缺失 → 需在 References 前添加\n- **Keywords**: `\\keywords{}` 为 CoRL 特有，ICML 模板需处理\n- 切换模板后需重新确认页数限制\n\n---\n\n## Issue Tracker Summary (Round 4)\n\n### 本轮新解决 (5)\n| Issue | 状态 |\n|-------|------|\n| R1-N3 CoRL venue fit | RESOLVED (venue → ICML) |\n| R1-W2 步数不对等 | RESOLVED (exp_045 data) |\n| R2-W1 TAWM 无实证 | RESOLVED (hypothesized) |\n| R3-N-new-1 Detector 样本量 | RESOLVED (preliminary) |\n| R2-W4 Becker-Ehmck | RESOLVED (混淆解释) |\n\n### 本轮新发现 (5)\n| Issue | 严重性 |\n|-------|--------|\n| N-R4-1 模板 corl_2026 | CRITICAL |\n| N-R4-2 Impact Statement 缺失 | CRITICAL |\n| N-R4-3 IQM 计算错误 | CRITICAL |\n| N-R4-4 Seed 数量不一致 | WARNING |\n| N-R4-5 \"causal chain\" 措辞 | INFO |\n\n### 遗留未解决 (4)\n| Issue | 严重性 | 状态 |\n|-------|--------|------|\n| R2-N3 Actionable 贡献弱 | WARNING (降级) | in_progress |\n| R3-N-new-2 gradient diversity | WARNING | in_progress |\n| R3-N-new-3 Baseline eval 缺失 | WARNING | open |\n| N-R4-5 \"causal chain\" | INFO | open |\n\n### 全局统计\n- 总 issues: 26\n- Resolved: 18\n- In Progress: 2\n- Open: 6",
  "project": "event-gated-adaptive-horizon",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak accept",
  "review_chat_id": "oc_dd4a07a509df7e5f9a31d65f776059bc"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 4\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**目标 Venue**: ICML 2026（Round 4 从 CoRL 切换）\n**审稿日期**: 2026-05-24\n**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验充分性 | R2: Novelty + 贡献度 + 写作质量）\n**轮次**: Round 4 继续审稿（修订评估）+ 交叉分享（1 轮收敛）\n**上轮评分**: Round 3 Weak Reject (5/10, CoRL)\n\n---\n\n## Summary\n\n论文从 Round 3 (Weak Reject 5/10, CoRL) 转投 ICML 2026 并进行了多项修订：(1) TAWM/MPC 对比措辞弱化为 \"hypothesized structural factor\"；(2) Discussion 新增 exp_045 self-recovery 数据（302K 步后 NVE 4.91× → 0.05×, eval 94.7% baseline），解决了步数不对等问题；(3) Online CIVO Detector 降级为 \"preliminary diagnostic\" 并披露 Clopper-Pearson CI；(4) Walker Walk 扩展至 5 seeds。\n\n然而，模板仍为 corl_2026（未切换 icml2026.sty），缺少 ICML 要求的 Impact Statement，且存在 IQM 计算错误（n=5 seeds 报告了 n=4 的 IQM 值 175.2，正确值应为 148.8）和 seed 数量叙述不一致（methodology/conclusion 说 4 seeds，results 说 n=5）。\n\n---\n\n## Strengths\n\n1. **Factorial design 系统严谨**（2/2 共识，持续优势）：43 配置 × 4-5 seeds × 5 环境，primary/secondary comparison 清晰标注\n2. **LOEO 交叉验证统计可信度高**：AUROC=0.981 (LOEO, 3 folds)\n3. **四级干预层级分析**：gradient/output/representation/architecture 提供系统性 negative result。Gradient magnitude ≠ causal importance 的发现有洞见\n4. **ManiSkill discriminative validity**：NVE 诊断正确区分 CIVO 与 transient\n5. **Dual-critic convergence insight**：ρ > 0.999 揭示 imagination-based 训练中 Double Q pessimism 的结构性失效\n6. **exp_045 self-recovery 数据**（Round 4 新增）：302K 步后完全恢复（eval 94.7% baseline），充分证明 105K 步足以观察 onset 且 recovery 计算成本高\n7. **Venue 切换至 ICML**：消除了 Round 3 的核心矛盾（CIVO locomotion-specificity vs CoRL manipulation focus）\n8. **措辞诚实度提升**：\"hypothesized structural factor\"、\"preliminary diagnostic\"、Limitations 诚实全面\n\n---\n\n## Weaknesses（按严重性排序）\n\n### Critical（影响接收决定）\n\n**W-C1. 模板仍为 corl_2026，未切换至 icml2026.sty [2/2 共识，Round 4 新发现]**\nmain.tex:5 仍使用 `\\usepackage{corl_2026}`，PDF 页脚显示 \"Submitted to the 10th Conference on Robot Learning (CoRL, 2026)\"。ICML 2026 要求使用 icml2026.sty 模板。**Desk reject 风险极高。**\n\n**W-C2. 缺少 Impact Statement [R2 发现，R1 承认审查遗漏]**\nICML 2026 要求论文在 References 前包含 Impact Statement section。当前论文完全没有此 section。**Desk reject 风险。**\n\n**W-C3. IQM 计算错误——数据完整性问题 [R2 发现并独立验证]**\nresults.tex:81 报告 \"IQM $175.2$, $n{=}5$\"，但经验证：\n- Walker 5 seeds eval: {63.6, 82.8, 95.8, 267.9, 268.0}\n- n=4 IQM（trim 1 each side）: mean(82.8, 267.9) = **175.35 ≈ 175.2** ✓\n- n=5 IQM（trim 1 each side）: mean(82.8, 95.8, 267.9) = **148.8** ≠ 175.2\n\nIQM 175.2 是 n=4 的正确值；添加第 5 个 seed（eval 95.8）后未重新计算。对于一篇以统计严谨性为卖点、引用 Agarwal et al. (2021) 的 diagnostic paper，此错误损害可信度。**错误性质为 careless 而非 systematic，不影响核心结论（CIVO 在所有 5 seeds 中出现），但必须修复。**\n\n### Warning（影响评分但不一票否决）\n\n**W-W1. Seed 数量叙述全文不一致 [R1 提出，R2 系统验证]**\n| 位置 | 文本 | 问题 |\n|------|------|------|\n| methodology.tex:32 | \"Key configurations use **4** seeds\" | 实际 Walker 是 5 seeds |\n| results.tex:81 | \"all **five** Walker Walk seeds...n=5\" | 正确 |\n| conclusion.tex:10 | \"Statistical power with **4** seeds\" | 与 n=5 不一致 |\n| Figure 2 caption | \"n=3 seeds plotted; seed 4 data in Table\" | 未提及 seed 5 |\n\n**W-W2. \"gradient diversity\" 术语无支撑证据 [2/2 共识，PARTIALLY RESOLVED]**\nresults.tex:166: \"the min operation in wide dual-critic may instead regularize through gradient diversity (Appendix G)\"。Appendix G 未提供 gradient diversity 的量化证据。建议改为 \"may instead function through a capacity-dependent mechanism during early training\" 或 \"the mechanism is an open question\"。introduction.tex:13 的 \"different mechanism\" 措辞更恰当。\n\n**W-W3. 贡献模式——scope 和 significance 有限 [延续 Round 3，2/2 共识]**\n- 核心结论仍是 negative（no reliable intervention eliminates CIVO）\n- 最有效 \"solution\" 是不使用该功能（embedding removed = 100% prevention）\n- CIVO 仅在 locomotion 中复现\n- 在 ICML 语境下，systematic negative result 的贡献度评价比 CoRL 更宽容，严重性降级\n\n**W-W4. ManiSkill 和 Cheetah Run baseline eval 值缺失 [延续 Round 3，未修复]**\nTable 1 中这些环境缺少 vanilla DreamerV3 baseline eval 值，读者无法判断相对性能。\n\n### Minor\n\n**W-M1. \"causal chain\" 措辞 [R2 建议]**\nresults.tex:4 中 \"establish a causal chain\" 暗示因果推断，factorial ablation 提供 predictive/associative 证据。建议改为 \"trace a pathway\" 或 \"establish a predictive chain\"。\n\n**W-M2. Abstract \"isolate\" 残留 [R1 minor，R2 REBUT 降级]**\nR2 认为 \"isolate\" 在 factorial ablation 语境中是标准用语，不构成 overclaim。Director 同意——minor at most。\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 共识度 |\n|------|----|----|--------|\n| 模板 corl_2026 (NEW) | CRITICAL | CRITICAL (AGREE) | **2/2 一致** |\n| Impact Statement 缺失 (NEW) | 承认遗漏 | CRITICAL | R2 独立发现 |\n| IQM 计算错误 (NEW) | — | CRITICAL (验证) | R2 独立发现 |\n| Seed 数量不一致 (NEW) | 提出 | AGREE (更严重) | **2/2 一致** |\n| R1-W2 步数不对等 | RESOLVED | AGREE RESOLVED | **2/2 一致** |\n| R2-W1 TAWM 对比 | RESOLVED | AGREE RESOLVED | **2/2 一致** |\n| R3-N-new-1 Detector 样本量 | RESOLVED | AGREE RESOLVED | **2/2 一致** |\n| R3-N-new-2 Dual-critic | PARTIALLY | AGREE PARTIALLY | **2/2 一致** |\n| R2-W4 Becker-Ehmck | 仍未引用 | 接受混淆解释 | **R2 覆盖，non-issue** |\n| Significance | Good (borderline) | Fair | **分歧（minor）** |\n\n---\n\n## Reviewer Divergence\n\n**1. Significance（R1: Good borderline vs R2: Fair）**\n- R1：dual-critic convergence insight 和 systematic negative result 在 ICML 社区有价值\n- R2：negative result + no reliable fix 的贡献模式 significance 有限\n- **Director 判断**：R1 borderline Good 合理但偏乐观。ICML RL track 接受 systematic negative results，但论文的 actionable output 确实有限。综合约 Fair+ (2.5/4)。\n\n**2. \"isolate\" 严重性（R1: minor vs R2: non-issue）**\n- R1：与 \"strongest predictor\" 不一致\n- R2：factorial ablation 中 \"isolate\" 是标准用语\n- **Director 判断**：同意 R2。Minor at most。\n\n---\n\n## Questions for Authors\n\n1. IQM 175.2 是 n=4 的值——请重新计算 n=5 的 IQM（经计算应为 ~148.8）并更新 results.tex:81。\n2. methodology.tex:32 说 \"4 seeds\"，results.tex:81 说 \"n=5\"——Walker Walk 的实际 seed 数是多少？请统一全文叙述（methodology.tex:32, conclusion.tex:10, Figure 2 caption）。\n3. 是否计划切换到 icml2026.sty 并添加 Impact Statement？这两项是 desk reject 风险。\n4. results.tex:166 中 \"gradient diversity\" 在 Appendix G 中是否有量化支撑？如果没有，是否考虑弱化措辞？\n5. Wide dual-critic 在 Walker 3/4 prevention 但 Cheetah 0/1——是否有对 environment-dependence 的解释？\n\n---\n\n## Missing References\n\nRound 3 遗留的 Becker-Ehmck 2023 问题已解决：R2 确认混淆解释合理（实为 Benechehab et al. 2023，已引用于 related_work.tex）。无新增缺失引用。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（1 critical, 4 warnings, 12 info）。\n\n**主要发现**：\n1. **[critical] 前 4 页无 display item**：连续 4 页纯文本，第一个视觉锚点（Table 1）直到第 5 页。建议将 Figure 6（CIVO 机制图，当前 Appendix page 17）提前到 Section 1/3。\n2. **[warning] 正文 display item 密度偏低**：8 页正文仅 4 个 display items（Table 1-2, Figure 1-2），实证型论文通常期望 6+。\n3. **[warning] Section 3 跨 2 页纯文本**：复杂实验设计无图示辅助。\n4. **[warning] Discussion + Conclusion 挤在同一页全纯文本**。\n5. **[warning] 最后一页 Table 22 仅占 35-40%**，大面积空白。\n6. **[info] 图表质量良好**：Figure 1/2 清晰，Table 1/2 booktabs 规范，ROC 曲线标注清晰。\n7. **[info] Figure 6（CIVO mechanism diagram）是全文最有解释力的图**，强烈建议简化版移入正文。\n\n---\n\n## Overall Assessment\n\n**评分: Weak Accept (6/10)**\n**置信度: High (4/5)**\n\n**与 Round 3 (Weak Reject, 5/10, CoRL) 的变化**：\n\n| 维度 | Round 3 | Round 4 | 变化 |\n|------|---------|---------|------|\n| Venue fit | STILL_OPEN (CoRL mismatch) | **RESOLVED** (→ ICML) | ▲▲▲ |\n| 步数不对等 | STILL_OPEN | RESOLVED (exp_045 data) | ▲▲ |\n| TAWM 对比 | STILL_OPEN | RESOLVED (hypothesized) | ▲▲ |\n| Detector 样本量 | OPEN | RESOLVED (preliminary) | ▲ |\n| Becker-Ehmck 引用 | PARTIALLY | RESOLVED (混淆解释) | ▲ |\n| 模板合规 | RESOLVED (CoRL PMLR) | **NEW CRITICAL** (仍是 CoRL) | ▼▼ |\n| Impact Statement | — | **NEW CRITICAL** (ICML 要求) | ▼▼ |\n| IQM 数据完整性 | — | **NEW CRITICAL** (n=5 报 n=4 值) | ▼ |\n| Seed 叙述一致性 | — | **NEW WARNING** | ▼ |\n\n**核心判断**：\n\nVenue 切换是 Round 4 最重要的变化。Round 3 的两个核心障碍（CoRL venue fit + deployment-oriented 社区的贡献期望）在 ICML 语境下大幅缓解——ICML RL track 接受 systematic diagnostic/negative results，factorial design + LOEO 验证的方法论水平匹配 ICML 标准。Round 3 报告本身也预测了\"如果提交到 ICML：Borderline Accept (6/10)\"。\n\n新发现的格式问题（模板、Impact Statement）是 desk reject 风险但容易修复；IQM 错误虽不影响核心结论但损害可信度。\n\n**如果格式问题和 IQM 修复后**：评分可上调至 Borderline Accept (6.5/10)。\n\n**综合维度评分**（Director 综合两位 Reviewer）：\n\n| 维度 | 评分 | 理由 |\n|------|------|------|\n| Originality | 3.5/5 | CIVO 现象新颖，gradient ≠ causal importance 有洞见，方法论框架标准 |\n| Soundness | 3/5 | Factorial design 严谨，LOEO 有力，但 IQM 错误 + gradient diversity 无支撑损害可信度 |\n| Clarity | 3/5 | 结构清晰，但模板错误 + 缺 Impact Statement + seed 叙述不一致 |\n| Significance | 2.5/5 | 四级干预有系统贡献，ICML 对 negative results 更宽容，但 actionable output 有限 |\n| Relevance (ICML) | 4/5 | World-model RL + temporal abstraction 是 ICML RL track 核心话题 |\n| Limitations | 4/5 | 诚实全面 |\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 约 150 词，长度合理\n- \"isolate\" 在 factorial ablation 语境中可接受（R2 判断）\n- 统计数据密度仍偏高（6+ 数字指标），建议精简\n\n### Introduction\n- Robotics framing 保留（从 CoRL 延续），在 ICML 中不加分也不减分\n- Contribution 列表 4 项清晰，detector 已降级为 \"preliminary\"\n\n### Experimental Setup (Section 3)\n- methodology.tex:32 \"Key configurations use 4 seeds\" 与实际 n=5 不一致——**必须修复**\n- Factorial design 展示专业，四因素清晰\n\n### Results (Section 4)\n- **IQM 175.2 是 n=4 值，n=5 应为 148.8——必须修复**\n- Figure 2 caption 提到 \"seed 4\" 但未提及 seed 5\n- \"gradient diversity\" (results.tex:166) 无 Appendix 支撑——建议弱化\n- exp_045 self-recovery 数据有效回应了步数不对等问题\n- \"establish a causal chain\" (results.tex:4) 建议改为 \"trace a pathway\"\n\n### Discussion (Section 5)\n- \"hypothesized structural factor\" 措辞准确\n- exp_045 training horizon 讨论充分\n\n### Conclusion (Section 6)\n- conclusion.tex:10 \"4 seeds\" 与 n=5 不一致——**必须修复**\n- Limitations paragraph 诚实全面\n\n### Format Issues（Desk Reject 风险）\n- **模板**: main.tex:5 仍为 `\\usepackage{corl_2026}` → 需切换 icml2026.sty\n- **Impact Statement**: 缺失 → 需在 References 前添加\n- **Keywords**: `\\keywords{}` 为 CoRL 特有，ICML 模板需处理\n- 切换模板后需重新确认页数限制\n\n---\n\n## Issue Tracker Summary (Round 4)\n\n### 本轮新解决 (5)\n| Issue | 状态 |\n|-------|------|\n| R1-N3 CoRL venue fit | RESOLVED (venue → ICML) |\n| R1-W2 步数不对等 | RESOLVED (exp_045 data) |\n| R2-W1 TAWM 无实证 | RESOLVED (hypothesized) |\n| R3-N-new-1 Detector 样本量 | RESOLVED (preliminary) |\n| R2-W4 Becker-Ehmck | RESOLVED (混淆解释) |\n\n### 本轮新发现 (5)\n| Issue | 严重性 |\n|-------|--------|\n| N-R4-1 模板 corl_2026 | CRITICAL |\n| N-R4-2 Impact Statement 缺失 | CRITICAL |\n| N-R4-3 IQM 计算错误 | CRITICAL |\n| N-R4-4 Seed 数量不一致 | WARNING |\n| N-R4-5 \"causal chain\" 措辞 | INFO |\n\n### 遗留未解决 (4)\n| Issue | 严重性 | 状态 |\n|-------|--------|------|\n| R2-N3 Actionable 贡献弱 | WARNING (降级) | in_progress |\n| R3-N-new-2 gradient diversity | WARNING | in_progress |\n| R3-N-new-3 Baseline eval 缺失 | WARNING | open |\n| N-R4-5 \"causal chain\" | INFO | open |\n\n### 全局统计\n- 总 issues: 26\n- Resolved: 18\n- In Progress: 2\n- Open: 6",
    "project": "event-gated-adaptive-horizon",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak accept",
    "review_chat_id": "oc_dd4a07a509df7e5f9a31d65f776059bc"
  }
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-24T09:47:37.477024+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5e879064da2e47dad864c1f891eb37a8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4067
}
```

</details>

---


### Assistant

_source line 364 · 2026-05-24T09:47:47.118549+00:00_

Round 4 审稿报告已投递。

**评分：Weak Accept (6/10)**，较 Round 3 (Weak Reject 5/10) 上调一档。

**关键变化**：
- Venue 切换至 ICML 消除了 Round 3 最大障碍（CoRL venue fit）
- 步数不对等、TAWM 措辞、Detector 样本量等 3 个 Round 3 遗留问题全部 RESOLVED
- 但 R2 发现了 3 个新 CRITICAL 问题：模板仍为 CoRL、缺 Impact Statement、IQM 计算错误（n=5 报了 n=4 的值）

**两位 Reviewer 核心共识**：Overall Weak Accept，格式问题和 IQM 修复后可上调至 Borderline Accept (6.5/10)。唯一分歧是 Significance（R1 Good borderline vs R2 Fair），已在报告中取 Fair+ 折中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 29

## Round 29

2 recorded events


### User

_source line 365 · 2026-05-24T09:47:49.717007+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。核心发现：

1. **IQM 数据错误确认**：第 5 个 seed (eval 95.8) 加入后 IQM 应为 ~148.8 而非 175.2——n=4 的值未重新计算，是数据完整性问题
2. **"gradient diversity" 无支撑**：同意 R1 的 PARTIALLY RESOLVED，主文应弱化措辞
3. **R1-W2 步数、R2-W1 TAWM**：同意均为 RESOLVED
4. **"isolate" 残留**：minor 问题，factorial ablation 语境下可接受，"causal chain" 建议弱化
5. **Becker-Ehmck**：接受混淆解释，降级为 non-issue
6. **补充 R1 遗漏**：ICML Impact Statement 缺失同样是 desk reject 风险
7. **Overall**：与 R1 一致，维持 Weak Accept (4/6)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 366 · 2026-05-24T09:47:59.315981+00:00_

Round 4 审稿报告已在收到 R2 完整交叉回应后合成并投递完毕（Weak Accept 6/10）。此消息为 R2 交叉回应的摘要确认，所有要点已纳入已提交的报告中。无需额外操作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director"
}
```

</details>

---


## Round 30

## Round 30

42 recorded events


### User

_source line 367 · 2026-05-24T14:59:45.835693+00:00_

[Round 5 - 继续审稿]
论文已更新。请基于上一轮审稿意见，重点审查修改是否充分回应了之前提出的问题。
重点关注：
1. 上轮提出的问题是否已充分解决
2. 修改是否引入了新问题
3. 整体评分是否需要调整

上一轮审稿报告: `projects/event-gated-adaptive-horizon/artifacts/review_reports/round_4.md`
跨轮次问题追踪: `projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml`
请用 read_local_file 先读这两个文件,重点验证 status=in_progress 的 issue 是否已被充分修复。
派 Reviewer 时把 open/in_progress 的 issue 列表附在任务里,要求逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由。

[论文提交]
- 项目: event-gated-adaptive-horizon
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex
- 目标 venue: ICML 2026
- 截止日期: 未提供，请自行调研
- **引用验证**: ❌ 未启用

请继续审稿流程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-24T15:00:02.527772+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_reports/round_4.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_reports/round_4.md"
  }
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-24T15:00:02.996935+00:00_

1	---
2	round: 4
3	review_mode: continue
4	overall_score: weak accept
5	timestamp: 2026-05-24T09:47:33.409986+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# 审稿报告 — Round 4
12	
13	**论文**: "Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
14	**目标 Venue**: ICML 2026（Round 4 从 CoRL 切换）
15	**审稿日期**: 2026-05-24
16	**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验充分性 | R2: Novelty + 贡献度 + 写作质量）
17	**轮次**: Round 4 继续审稿（修订评估）+ 交叉分享（1 轮收敛）
18	**上轮评分**: Round 3 Weak Reject (5/10, CoRL)
19	
20	---
21	
22	## Summary
23	
24	论文从 Round 3 (Weak Reject 5/10, CoRL) 转投 ICML 2026 并进行了多项修订：(1) TAWM/MPC 对比措辞弱化为 "hypothesized structural factor"；(2) Discussion 新增 exp_045 self-recovery 数据（302K 步后 NVE 4.91× → 0.05×, eval 94.7% baseline），解决了步数不对等问题；(3) Online CIVO Detector 降级为 "preliminary diagnostic" 并披露 Clopper-Pearson CI；(4) Walker Walk 扩展至 5 seeds。
25	
26	然而，模板仍为 corl_2026（未切换 icml2026.sty），缺少 ICML 要求的 Impact Statement，且存在 IQM 计算错误（n=5 seeds 报告了 n=4 的 IQM 值 175.2，正确值应为 148.8）和 seed 数量叙述不一致（methodology/conclusion 说 4 seeds，results 说 n=5）。
27	
28	---
29	
30	## Strengths
31	
32	1. **Factorial design 系统严谨**（2/2 共识，持续优势）：43 配置 × 4-5 seeds × 5 环境，primary/secondary comparison 清晰标注
33	2. **LOEO 交叉验证统计可信度高**：AUROC=0.981 (LOEO, 3 folds)
34	3. **四级干预层级分析**：gradient/output/representation/architecture 提供系统性 negative result。Gradient magnitude ≠ causal importance 的发现有洞见
35	4. **ManiSkill discriminative validity**：NVE 诊断正确区分 CIVO 与 transient
36	5. **Dual-critic convergence insight**：ρ > 0.999 揭示 imagination-based 训练中 Double Q pessimism 的结构性失效
37	6. **exp_045 self-recovery 数据**（Round 4 新增）：302K 步后完全恢复（eval 94.7% baseline），充分证明 105K 步足以观察 onset 且 recovery 计算成本高
38	7. **Venue 切换至 ICML**：消除了 Round 3 的核心矛盾（CIVO locomotion-specificity vs CoRL manipulation focus）
39	8. **措辞诚实度提升**："hypothesized structural factor"、"preliminary diagnostic"、Limitations 诚实全面
40	
41	---
42	
43	## Weaknesses（按严重性排序）
44	
45	### Crit
…[truncated 9369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 469
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-24T15:00:02.997505+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-24T15:00:03.872919+00:00_

1	issues:
2	  - id: "R1-N1"
3	    summary: "统计检验力严重不足：2-3 seeds 无法支撑 causal factor 声明"
4	    category: experiment
5	    severity: critical
6	    status: resolved
7	    first_raised_round: 1
8	    last_seen_round: 3
9	    mentions:
10	      - round: 1
11	        reviewers: [1, 2, 3]
12	        note: "三位 reviewer 均认同统计效力不足"
13	      - round: 3
14	        reviewers: [1, 2]
15	        note: "两位 reviewer 一致判定 RESOLVED。Seeds 增至 4，语言改为 strongest predictor，LOEO AUROC=0.981，IQR 报告。残留小问题：Abstract 中 isolate 一词仍携带因果含义。"
16	    action_items:
17	      - round: 1
18	        action: "补 seeds 到 4 per key config"
19	        assigned_to: agent
20	        status: done
21	      - round: 1
22	        action: "弱化因果语言: causal factor → strongest predictor"
23	        assigned_to: paper_agent
24	        status: done
25	      - round: 1
26	        action: "统计报告改用 IQM + bootstrap CI per Agarwal et al. 2021"
27	        assigned_to: paper_agent
28	        status: done
29	    resolution: "Seeds 增至 4，因果语言全面弱化为 strongest predictor，LOEO 交叉验证 AUROC=0.981，IQM + bootstrap CI 报告完整。"
30	    resolution_round: 3
31	
32	  - id: "R1-N2"
33	    summary: "NVE 阈值 1.5× 为 post-hoc 选择，88.9% accuracy 是训练准确率，无独立验证"
34	    category: method
35	    severity: critical
36	    status: resolved
37	    first_raised_round: 1
38	    last_seen_round: 1
39	    mentions:
40	      - round: 1
41	        reviewers: [1, 2, 3]
42	        note: "三位 reviewer 一致认为 post-hoc"
43	    action_items:
44	      - round: 1
45	        action: "LOEO cross-validation: mean AUROC 0.981"
46	        assigned_to: agent
47	        status: done
48	    resolution: "LOEO 交叉验证完成：3 环境 leave-one-out，mean AUROC 0.981，θ=1.5 在全部 fold 最优范围。论文措辞已改为 in-sample + LOEO cross-validated。"
49	    resolution_round: 1
50	
51	  - id: "R1-N3"
52	    summary: "CoRL venue fit 严重不足：全文无 robotics 实验/讨论"
53	    category: framing
54	    severity: critical
55	    status: resolved
56	    first_raised_round: 1
57	    last_seen_round: 4
58	    mentions:
59	      - round: 1
60	        r
…[truncated 18190 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 875
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-24T15:00:03.923742+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-24T15:00:03.975109+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-24T15:00:23.507097+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-24T15:00:25.415183+00:00_

{"result":"# 项目 event-gated-adaptive-horizon 概况\n\n## 实验状态 (133 个)\n\n- **exp_009a_baseline_walker_s2**: DONE (success) — \n- **exp_008e_v3_walker_s2**: DONE (negative) — \n- **exp_008e_v3_walker_s1**: DONE (success) — \n- **exp_006**: DONE (killed) — \n- **exp_008a**: DONE (killed) — \n- **exp_008c**: DONE (killed) — \n- **exp_008d**: DONE (killed) — \n- **exp_008e_v2_subsample_on_dt1_h15**: DONE (killed) — \n- **exp_rssm_fidelity_analysis**: DONE (success) — \n- **exp_008e_v3_subsample_on_dt1_h15**: DONE (success) — \n- **exp_009c_008f_walker_s2**: DONE (negative) — \n- **exp_006_fixed_dt2**: DONE (negative) — \n- **exp_008e_subsample_on_fixed_dt1**: DONE (killed) — \n- **exp_008e_subsample_on_dt1_h15**: DONE (killed) — \n- **exp_002_event_gated**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp_059_walker_trained_s5** (negative): Walker CIVO trigger 第5个独立seed验证。当前4/4 seeds触发sustained CIVO（p=0.0625 binomial test）。如果s5也触发 → p=0.03125，达到统计显著性阈值。关联 Claim 1: CIVO reproducibility。 ← 基于 exp_008d_civo_trigger_s3\n- **exp_008d_civo_trigger_s4** (success): Walker Walk CIVO trigger seed=4: trained dt_emb + subsample ON + H=8. 第四 seed 复现 CIVO (NVE>1.5×)，加强 Walker 因果论证的统计力度。Rebuttal 储备。 ← 基于 exp_008d_civo_trigger_s3\n- **exp_009b_008d_walker_s2** (negative): CIVO onset (NVE≥1.5×) reproduces on seed=2 with identical architecture, confirming the phenomenon is systematic rather than seed-specific. Collapse outcome may be stochastic. ← 基于 exp_008d_subsample_on_h8\n  [009b_literature_linkage](/api/workspace-files/projects/event-gated-adaptive-horizon/artifacts/exp_009b_008d_walker_s2/report/009b_literature_search.md)\n\n## 趋势\n成功 65 / 负向 36 / 失败 11 / 共 133\nnve_peak: 4.44 ↑（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nbjb1-40020: 空闲 cuda:0, cuda:1\nbjb1-45299: 无 GPU 信息\n\n## 告警\n- 016e: 已被终止 — unknown\n- exp_002_event_gated: 训练失败 — unknown\n- exp_006: 已被终止 — unknown\n- 
…[truncated 1245 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1908
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-24T15:00:25.465889+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
    "limit": "50"
  }
}
```

</details>

---
